from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from ..models import User, Senior, VitalSign, Medication, MedicationLog, EmergencyAlert, AuditTrail
from ..schemas import SeniorCreate, SeniorOut
from ..auth import get_current_user, require_roles

router = APIRouter(prefix="/seniors", tags=["Senior Residents Management"])

@router.get("/")
def list_seniors(
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Senior)
    
    # If Guardian, filter to only their assigned seniors
    if current_user.role == "GUARDIAN":
        query = query.filter(Senior.guardian_id == current_user.id)
    # If Senior resident, filter to only their own record
    elif current_user.role == "SENIOR":
        query = query.filter(Senior.user_id == current_user.id)

    if search:
        query = query.filter(
            (Senior.full_name.ilike(f"%{search}%")) |
            (Senior.room_number.ilike(f"%{search}%")) |
            (Senior.mrn.ilike(f"%{search}%"))
        )

    seniors = query.order_by(Senior.room_number.asc()).all()

    # Enrich each senior record with vital status, alert count, medication adherence
    results = []
    for s in seniors:
        latest_vital = db.query(VitalSign).filter(VitalSign.senior_id == s.id).order_by(VitalSign.recorded_at.desc()).first()
        active_alerts = db.query(EmergencyAlert).filter(EmergencyAlert.senior_id == s.id, EmergencyAlert.status.in_(["TRIGGERED", "DISPATCHED", "RESPONDING"])).count()
        
        # Calculate adherence %
        total_logs = db.query(MedicationLog).filter(MedicationLog.senior_id == s.id).count()
        given_logs = db.query(MedicationLog).filter(MedicationLog.senior_id == s.id, MedicationLog.status == "GIVEN").count()
        adherence_rate = round((given_logs / total_logs * 100), 1) if total_logs > 0 else 100.0

        results.append({
            "id": s.id,
            "mrn": s.mrn,
            "full_name": s.full_name,
            "date_of_birth": s.date_of_birth,
            "gender": s.gender,
            "blood_group": s.blood_group,
            "room_number": s.room_number,
            "phone": s.phone,
            "address": s.address,
            "emergency_name": s.emergency_name,
            "emergency_phone": s.emergency_phone,
            "primary_doctor": s.primary_doctor,
            "chronic_ailments": s.chronic_ailments,
            "drug_allergies": s.drug_allergies,
            "guardian_id": s.guardian_id,
            "guardian_name": s.guardian.full_name if s.guardian else None,
            "active_alerts_count": active_alerts,
            "adherence_rate": adherence_rate,
            "latest_vital": {
                "systolic_bp": latest_vital.systolic_bp,
                "diastolic_bp": latest_vital.diastolic_bp,
                "pulse_rate": latest_vital.pulse_rate,
                "spo2": latest_vital.spo2,
                "temperature": latest_vital.temperature,
                "blood_glucose": latest_vital.blood_glucose,
                "is_anomaly": latest_vital.is_anomaly,
                "recorded_at": latest_vital.recorded_at.isoformat()
            } if latest_vital else None
        })

    return results

@router.get("/{senior_id}")
def get_senior_details(
    senior_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    senior = db.query(Senior).filter(Senior.id == senior_id).first()
    if not senior:
        raise HTTPException(status_code=404, detail="Senior record not found")

    vitals = db.query(VitalSign).filter(VitalSign.senior_id == senior_id).order_by(VitalSign.recorded_at.desc()).limit(10).all()
    medications = db.query(Medication).filter(Medication.senior_id == senior_id).all()
    active_alerts = db.query(EmergencyAlert).filter(EmergencyAlert.senior_id == senior_id).order_by(EmergencyAlert.triggered_at.desc()).all()

    return {
        "senior": {
            "id": senior.id,
            "mrn": senior.mrn,
            "full_name": senior.full_name,
            "date_of_birth": senior.date_of_birth,
            "gender": senior.gender,
            "blood_group": senior.blood_group,
            "room_number": senior.room_number,
            "phone": senior.phone,
            "address": senior.address,
            "emergency_name": senior.emergency_name,
            "emergency_phone": senior.emergency_phone,
            "primary_doctor": senior.primary_doctor,
            "chronic_ailments": senior.chronic_ailments,
            "drug_allergies": senior.drug_allergies,
            "guardian_name": senior.guardian.full_name if senior.guardian else None,
        },
        "recent_vitals": vitals,
        "medications": medications,
        "emergency_alerts": active_alerts
    }

@router.post("/", response_model=SeniorOut, status_code=status.HTTP_201_CREATED)
def create_senior(
    senior_in: SeniorCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["ADMIN", "DOCTOR"]))
):
    existing = db.query(Senior).filter(Senior.mrn == senior_in.mrn).first()
    if existing:
        raise HTTPException(status_code=400, detail="Senior with this MRN already exists")

    new_senior = Senior(**senior_in.model_dump())
    db.add(new_senior)
    db.commit()
    db.refresh(new_senior)

    audit = AuditTrail(
        user_id=current_user.id,
        user_email=current_user.email,
        action="SENIOR_PROFILE_CREATED",
        details=f"Created record for {new_senior.full_name} (MRN: {new_senior.mrn}, Room: {new_senior.room_number})"
    )
    db.add(audit)
    db.commit()

    return new_senior

@router.put("/{senior_id}", response_model=SeniorOut)
def update_senior(
    senior_id: int,
    senior_in: SeniorCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["ADMIN", "DOCTOR", "CAREGIVER"]))
):
    senior = db.query(Senior).filter(Senior.id == senior_id).first()
    if not senior:
        raise HTTPException(status_code=404, detail="Senior record not found")

    for field, value in senior_in.model_dump().items():
        setattr(senior, field, value)

    db.commit()
    db.refresh(senior)

    audit = AuditTrail(
        user_id=current_user.id,
        user_email=current_user.email,
        action="SENIOR_PROFILE_UPDATED",
        details=f"Updated record for {senior.full_name} (Room: {senior.room_number})"
    )
    db.add(audit)
    db.commit()

    return senior
