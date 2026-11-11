from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timezone

from ..database import get_db
from ..models import User, Senior, Medication, MedicationLog, AuditTrail
from ..schemas import MedicationCreate, MedicationOut, MedicationLogCreate, MedicationLogOut
from ..auth import get_current_user, require_roles

router = APIRouter(prefix="/medications", tags=["Medication Administration & MAR"])

@router.get("/", response_model=List[MedicationOut])
def get_medications(
    senior_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Medication)
    if senior_id:
        query = query.filter(Medication.senior_id == senior_id)
    return query.all()

@router.post("/", response_model=MedicationOut, status_code=status.HTTP_201_CREATED)
def prescribe_medication(
    med_in: MedicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["ADMIN", "DOCTOR"]))
):
    senior = db.query(Senior).filter(Senior.id == med_in.senior_id).first()
    if not senior:
        raise HTTPException(status_code=404, detail="Senior record not found")

    new_med = Medication(
        senior_id=med_in.senior_id,
        name=med_in.name,
        dosage=med_in.dosage,
        frequency=med_in.frequency,
        scheduled_times=med_in.scheduled_times,
        instructions=med_in.instructions,
        prescription_status="ACTIVE",
        prescribed_by=current_user.full_name,
        start_date=med_in.start_date,
        end_date=med_in.end_date
    )
    db.add(new_med)
    db.commit()
    db.refresh(new_med)

    # Pre-populate today's scheduled dose logs for this medication
    times = [t.strip() for t in new_med.scheduled_times.split(",") if t.strip()]
    for t in times:
        dose_log = MedicationLog(
            medication_id=new_med.id,
            senior_id=senior.id,
            scheduled_time=t,
            status="PENDING"
        )
        db.add(dose_log)
    db.commit()

    audit = AuditTrail(
        user_id=current_user.id,
        user_email=current_user.email,
        action="MEDICATION_PRESCRIBED",
        details=f"Prescribed {new_med.name} {new_med.dosage} for {senior.full_name}"
    )
    db.add(audit)
    db.commit()

    return new_med

@router.get("/logs", response_model=List[MedicationLogOut])
def get_medication_logs(
    senior_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(MedicationLog)
    if senior_id:
        query = query.filter(MedicationLog.senior_id == senior_id)
    return query.order_by(MedicationLog.id.desc()).limit(100).all()

@router.post("/logs", response_model=MedicationLogOut)
def record_medication_dose(
    log_in: MedicationLogCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    med = db.query(Medication).filter(Medication.id == log_in.medication_id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")

    # Look for existing pending log for this time today or create a new one
    existing_log = db.query(MedicationLog).filter(
        MedicationLog.medication_id == log_in.medication_id,
        MedicationLog.scheduled_time == log_in.scheduled_time,
        MedicationLog.status == "PENDING"
    ).first()

    if existing_log:
        existing_log.status = log_in.status
        existing_log.administered_at = datetime.now(timezone.utc)
        existing_log.administered_by = current_user.full_name
        existing_log.notes = log_in.notes
        db.commit()
        db.refresh(existing_log)
        result_log = existing_log
    else:
        new_log = MedicationLog(
            medication_id=log_in.medication_id,
            senior_id=log_in.senior_id,
            scheduled_time=log_in.scheduled_time,
            administered_at=datetime.now(timezone.utc),
            status=log_in.status,
            notes=log_in.notes,
            administered_by=current_user.full_name
        )
        db.add(new_log)
        db.commit()
        db.refresh(new_log)
        result_log = new_log

    audit = AuditTrail(
        user_id=current_user.id,
        user_email=current_user.email,
        action="MEDICATION_DOSE_LOGGED",
        details=f"Dose of {med.name} recorded as {log_in.status} by {current_user.full_name}"
    )
    db.add(audit)
    db.commit()

    return result_log
