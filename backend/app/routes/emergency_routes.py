from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timezone
from pydantic import BaseModel

from ..database import get_db
from ..models import User, Senior, EmergencyAlert, AuditTrail
from ..schemas import EmergencyAlertCreate, EmergencyAlertOut
from ..auth import get_current_user, require_roles
from ..websocket_manager import manager

router = APIRouter(prefix="/emergency", tags=["Emergency SOS & Rapid Response"])

class ResolveAlertRequest(BaseModel):
    notes: str
    status: str = "RESOLVED"  # RESPONDING, RESOLVED

@router.get("/alerts")
def get_emergency_alerts(
    status_filter: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(EmergencyAlert)
    if status_filter:
        query = query.filter(EmergencyAlert.status == status_filter)
    
    alerts = query.order_by(EmergencyAlert.triggered_at.desc()).limit(50).all()
    results = []
    for a in alerts:
        senior = db.query(Senior).filter(Senior.id == a.senior_id).first()
        results.append({
            "id": a.id,
            "senior_id": a.senior_id,
            "senior_name": senior.full_name if senior else "Unknown Senior",
            "room_number": senior.room_number if senior else "N/A",
            "emergency_phone": senior.emergency_phone if senior else "N/A",
            "triggered_at": a.triggered_at.isoformat(),
            "trigger_type": a.trigger_type,
            "latitude": a.latitude,
            "longitude": a.longitude,
            "status": a.status,
            "resolved_at": a.resolved_at.isoformat() if a.resolved_at else None,
            "resolved_by": a.resolved_by,
            "notes": a.notes
        })
    return results

@router.post("/sos", status_code=status.HTTP_201_CREATED)
async def trigger_emergency_sos(
    alert_in: EmergencyAlertCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    senior = db.query(Senior).filter(Senior.id == alert_in.senior_id).first()
    if not senior:
        raise HTTPException(status_code=404, detail="Senior record not found")

    new_alert = EmergencyAlert(
        senior_id=alert_in.senior_id,
        trigger_type=alert_in.trigger_type,
        latitude=alert_in.latitude or 23.8151,
        longitude=alert_in.longitude or 90.4255,
        status="TRIGGERED",
        notes=alert_in.notes or "Immediate Senior SOS distress initiated via Emergency Button"
    )
    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)

    # Broadcast via WebSocket to ALL active users
    broadcast_payload = {
        "type": "EMERGENCY_SOS_ACTIVE",
        "alert_id": new_alert.id,
        "senior_id": senior.id,
        "senior_name": senior.full_name,
        "room_number": senior.room_number,
        "emergency_phone": senior.emergency_phone,
        "trigger_type": new_alert.trigger_type,
        "latitude": new_alert.latitude,
        "longitude": new_alert.longitude,
        "triggered_at": new_alert.triggered_at.isoformat(),
        "notes": new_alert.notes
    }
    await manager.broadcast(broadcast_payload)

    # Log to audit trail
    audit = AuditTrail(
        user_id=current_user.id,
        user_email=current_user.email,
        action="EMERGENCY_SOS_TRIGGERED",
        details=f"EMERGENCY SOS triggered for {senior.full_name} in Room {senior.room_number}"
    )
    db.add(audit)
    db.commit()

    return {
        "status": "EMERGENCY_DISPATCHED",
        "alert_id": new_alert.id,
        "senior_name": senior.full_name,
        "room_number": senior.room_number,
        "message": "Emergency dispatch notification broadcasted to all active clinical personnel and guardians."
    }

@router.post("/alerts/{alert_id}/resolve")
async def resolve_emergency_alert(
    alert_id: int,
    req: ResolveAlertRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["ADMIN", "DOCTOR", "CAREGIVER"]))
):
    alert = db.query(EmergencyAlert).filter(EmergencyAlert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")

    alert.status = req.status
    if req.status == "RESOLVED":
        alert.resolved_at = datetime.now(timezone.utc)
    alert.resolved_by = current_user.full_name
    alert.notes = (alert.notes or "") + f" | Response Update by {current_user.full_name}: {req.notes}"
    db.commit()

    senior = db.query(Senior).filter(Senior.id == alert.senior_id).first()

    # Broadcast resolution to WebSocket
    await manager.broadcast({
        "type": "EMERGENCY_SOS_RESOLVED",
        "alert_id": alert.id,
        "senior_name": senior.full_name if senior else "Resident",
        "status": alert.status,
        "resolved_by": current_user.full_name,
        "notes": req.notes
    })

    audit = AuditTrail(
        user_id=current_user.id,
        user_email=current_user.email,
        action="EMERGENCY_ALERT_RESOLVED",
        details=f"Alert #{alert_id} for senior {alert.senior_id} marked as {req.status} by {current_user.full_name}"
    )
    db.add(audit)
    db.commit()

    return {"message": "Emergency alert status updated", "alert_id": alert.id, "status": alert.status}
