from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel

from ..database import get_db
from ..models import User, Senior, Appointment, AuditTrail
from ..schemas import AppointmentCreate, AppointmentOut
from ..auth import get_current_user, require_roles

router = APIRouter(prefix="/appointments", tags=["Clinical Consultations & Telehealth"])

class StatusUpdate(BaseModel):
    status: str

@router.get("/")
def get_appointments(
    senior_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Appointment)
    if senior_id:
        query = query.filter(Appointment.senior_id == senior_id)
    elif current_user.role == "DOCTOR":
        query = query.filter(Appointment.doctor_name.ilike(f"%{current_user.full_name}%") | (Appointment.doctor_id == current_user.id))

    appointments = query.order_by(Appointment.scheduled_at.asc()).all()
    results = []
    for appt in appointments:
        senior = db.query(Senior).filter(Senior.id == appt.senior_id).first()
        results.append({
            "id": appt.id,
            "senior_id": appt.senior_id,
            "senior_name": senior.full_name if senior else "Unknown Resident",
            "room_number": senior.room_number if senior else "N/A",
            "doctor_id": appt.doctor_id,
            "doctor_name": appt.doctor_name,
            "specialty": appt.specialty,
            "scheduled_at": appt.scheduled_at.isoformat(),
            "consultation_type": appt.consultation_type,
            "status": appt.status,
            "notes": appt.notes,
            "teleconsult_link": appt.teleconsult_link
        })
    return results

@router.post("/", response_model=AppointmentOut, status_code=status.HTTP_201_CREATED)
def book_appointment(
    appt_in: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["ADMIN", "DOCTOR", "CAREGIVER"]))
):
    senior = db.query(Senior).filter(Senior.id == appt_in.senior_id).first()
    if not senior:
        raise HTTPException(status_code=404, detail="Senior not found")

    new_appt = Appointment(
        senior_id=appt_in.senior_id,
        doctor_id=appt_in.doctor_id,
        doctor_name=appt_in.doctor_name,
        specialty=appt_in.specialty,
        scheduled_at=appt_in.scheduled_at,
        consultation_type=appt_in.consultation_type,
        status="SCHEDULED",
        notes=appt_in.notes,
        teleconsult_link=appt_in.teleconsult_link or (
            f"https://meet.jit.si/ECMS-CareConsult-{appt_in.senior_id}-{int(appt_in.scheduled_at.timestamp())}"
            if appt_in.consultation_type == "TELECONSULT" else None
        )
    )
    db.add(new_appt)
    db.commit()
    db.refresh(new_appt)

    audit = AuditTrail(
        user_id=current_user.id,
        user_email=current_user.email,
        action="APPOINTMENT_SCHEDULED",
        details=f"Booked {new_appt.consultation_type} consultation with {new_appt.doctor_name} for {senior.full_name}"
    )
    db.add(audit)
    db.commit()

    return new_appt

@router.put("/{appt_id}/status")
def update_appointment_status(
    appt_id: int,
    status_update: StatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    appt = db.query(Appointment).filter(Appointment.id == appt_id).first()
    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appt.status = status_update.status.upper()
    db.commit()

    audit = AuditTrail(
        user_id=current_user.id,
        user_email=current_user.email,
        action="APPOINTMENT_STATUS_UPDATED",
        details=f"Appointment #{appt_id} updated to {appt.status}"
    )
    db.add(audit)
    db.commit()

    return {"message": "Appointment status updated successfully", "status": appt.status}
