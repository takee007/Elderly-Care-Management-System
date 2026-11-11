from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from ..models import User, ShiftNote, AuditTrail
from ..schemas import ShiftNoteCreate, ShiftNoteOut
from ..auth import get_current_user, require_roles

router = APIRouter(prefix="/handoff", tags=["Caregiver Shift Handover"])

@router.get("/notes", response_model=List[ShiftNoteOut])
def get_shift_notes(
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(ShiftNote).order_by(ShiftNote.signed_at.desc()).limit(limit).all()

@router.post("/notes", response_model=ShiftNoteOut, status_code=status.HTTP_201_CREATED)
def submit_shift_handover(
    note_in: ShiftNoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["ADMIN", "CAREGIVER", "DOCTOR"]))
):
    new_note = ShiftNote(
        caregiver_id=current_user.id,
        caregiver_name=current_user.full_name,
        shift_date=note_in.shift_date,
        shift_type=note_in.shift_type.upper(),
        handover_to=note_in.handover_to,
        notes=note_in.notes,
        flagged_seniors=note_in.flagged_seniors
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    audit = AuditTrail(
        user_id=current_user.id,
        user_email=current_user.email,
        action="SHIFT_HANDOVER_SUBMITTED",
        details=f"Caregiver {current_user.full_name} submitted {new_note.shift_type} shift handover to {new_note.handover_to}"
    )
    db.add(audit)
    db.commit()

    return new_note
