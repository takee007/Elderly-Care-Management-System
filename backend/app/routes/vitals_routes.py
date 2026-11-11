from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timezone

from ..database import get_db
from ..models import User, Senior, VitalSign, EmergencyAlert, AuditTrail
from ..schemas import VitalSignCreate, VitalSignOut
from ..auth import get_current_user, require_roles
from ..websocket_manager import manager

router = APIRouter(prefix="/vitals", tags=["Vital Signs Telemetry & Anomaly Detection"])

def detect_vitals_anomalies(v: VitalSignCreate) -> tuple[bool, str]:
    anomalies = []
    
    # Blood Pressure checks
    if v.systolic_bp > 140 or v.diastolic_bp > 90:
        anomalies.append(f"Hypertensive Crisis / High BP ({v.systolic_bp}/{v.diastolic_bp} mmHg)")
    elif v.systolic_bp < 90 or v.diastolic_bp < 60:
        anomalies.append(f"Hypotension Warning ({v.systolic_bp}/{v.diastolic_bp} mmHg)")

    # Oxygen Saturation (SpO2)
    if v.spo2 < 93:
        anomalies.append(f"Hypoxemia / Critical Low SpO2 ({v.spo2}%)")

    # Pulse / Heart Rate
    if v.pulse_rate > 105:
        anomalies.append(f"Tachycardia / Elevated Pulse ({v.pulse_rate} bpm)")
    elif v.pulse_rate < 50:
        anomalies.append(f"Bradycardia / Low Pulse ({v.pulse_rate} bpm)")

    # Blood Glucose
    if v.blood_glucose > 180:
        anomalies.append(f"Hyperglycemia ({v.blood_glucose} mg/dL)")
    elif v.blood_glucose < 70:
        anomalies.append(f"Hypoglycemia Warning ({v.blood_glucose} mg/dL)")

    # Temperature
    if v.temperature > 100.4:
        anomalies.append(f"Pyrexia / Fever ({v.temperature}°F)")
    elif v.temperature < 96.0:
        anomalies.append(f"Hypothermia ({v.temperature}°F)")

    if anomalies:
        return True, " | ".join(anomalies)
    return False, "Normal physiologic parameters"

@router.get("/", response_model=List[VitalSignOut])
def get_vitals(
    senior_id: Optional[int] = None,
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(VitalSign)
    if senior_id:
        query = query.filter(VitalSign.senior_id == senior_id)
    return query.order_by(VitalSign.recorded_at.desc()).limit(limit).all()

@router.post("/", response_model=VitalSignOut, status_code=status.HTTP_201_CREATED)
async def record_vitals(
    vitals_in: VitalSignCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["ADMIN", "DOCTOR", "CAREGIVER"]))
):
    senior = db.query(Senior).filter(Senior.id == vitals_in.senior_id).first()
    if not senior:
        raise HTTPException(status_code=404, detail="Senior record not found")

    is_anomaly, anomaly_notes = detect_vitals_anomalies(vitals_in)

    new_vital = VitalSign(
        senior_id=vitals_in.senior_id,
        systolic_bp=vitals_in.systolic_bp,
        diastolic_bp=vitals_in.diastolic_bp,
        pulse_rate=vitals_in.pulse_rate,
        spo2=vitals_in.spo2,
        temperature=vitals_in.temperature,
        blood_glucose=vitals_in.blood_glucose,
        is_anomaly=is_anomaly,
        anomaly_notes=anomaly_notes if is_anomaly else None,
        recorded_by=current_user.full_name
    )
    db.add(new_vital)
    db.commit()
    db.refresh(new_vital)

    # If critical anomaly, automatically spawn an Emergency Alert
    if is_anomaly:
        alert = EmergencyAlert(
            senior_id=senior.id,
            trigger_type="VITALS_ANOMALY",
            status="TRIGGERED",
            notes=f"Clinical Vital Anomaly Detected: {anomaly_notes}"
        )
        db.add(alert)
        db.commit()
        db.refresh(alert)

        # Broadcast via WebSocket
        await manager.broadcast({
            "type": "VITALS_ANOMALY_ALERT",
            "alert_id": alert.id,
            "senior_id": senior.id,
            "senior_name": senior.full_name,
            "room_number": senior.room_number,
            "notes": anomaly_notes,
            "timestamp": new_vital.recorded_at.isoformat()
        })

    # Log to audit trail
    audit = AuditTrail(
        user_id=current_user.id,
        user_email=current_user.email,
        action="VITALS_RECORDED",
        details=f"Recorded telemetry for {senior.full_name}. Anomaly: {is_anomaly} ({anomaly_notes})"
    )
    db.add(audit)
    db.commit()

    return new_vital
