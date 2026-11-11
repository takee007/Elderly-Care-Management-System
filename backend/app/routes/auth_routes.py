from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel, EmailStr

from ..database import get_db
from ..models import User, Senior, AuditTrail
from ..schemas import UserCreate, UserOut, Token, UserLogin, UserStatusUpdate
from ..auth import verify_password, get_password_hash, create_access_token, get_current_user, require_roles

router = APIRouter(prefix="/auth", tags=["Authentication & Access Control"])

class DemoLoginRequest(BaseModel):
    role: str  # ADMIN, DOCTOR, CAREGIVER, SENIOR, GUARDIAN

@router.post("/login", response_model=Token)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.email).first()
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if user.status != "ACTIVE":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is deactivated. Contact System Administrator.",
        )

    # Log to Audit Trail
    audit = AuditTrail(
        user_id=user.id,
        user_email=user.email,
        action="USER_LOGIN_SUCCESS",
        details=f"User {user.email} authenticated successfully with role {user.role}"
    )
    db.add(audit)
    db.commit()

    token = create_access_token(data={"sub": user.email, "role": user.role, "uid": user.id})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "role": user.role
    }

@router.post("/demo-login", response_model=Token)
def demo_login(req: DemoLoginRequest, db: Session = Depends(get_db)):
    """Fast switch convenience endpoint for presentations and demonstrations"""
    target_role = req.role.upper()
    user = db.query(User).filter(User.role == target_role).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"No demo user found for role {target_role}")

    if user.status != "ACTIVE":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"The account for role {target_role} is currently {user.status.lower()}. Contact administrator."
        )

    token = create_access_token(data={"sub": user.email, "role": user.role, "uid": user.id})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "role": user.role
    }

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered in ECMS")
    
    hashed_pw = get_password_hash(user_in.password)
    new_user = User(
        email=user_in.email,
        hashed_password=hashed_pw,
        full_name=user_in.full_name,
        role=user_in.role.upper(),
        phone=user_in.phone,
        status="ACTIVE"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    audit = AuditTrail(
        user_id=new_user.id,
        user_email=new_user.email,
        action="USER_REGISTERED",
        details=f"Registered new {new_user.role}: {new_user.full_name}"
    )
    db.add(audit)
    db.commit()

    return new_user

@router.get("/me")
def read_current_user_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    linked_senior = None
    if current_user.role == "SENIOR":
        senior = db.query(Senior).filter(Senior.user_id == current_user.id).first()
        if not senior:
            # fallback match by first name or room
            senior = db.query(Senior).first()
        if senior:
            linked_senior = {
                "id": senior.id,
                "mrn": senior.mrn,
                "full_name": senior.full_name,
                "room_number": senior.room_number,
                "emergency_phone": senior.emergency_phone
            }
    elif current_user.role == "GUARDIAN":
        senior = db.query(Senior).filter(Senior.guardian_id == current_user.id).first()
        if not senior:
            senior = db.query(Senior).first()
        if senior:
            linked_senior = {
                "id": senior.id,
                "mrn": senior.mrn,
                "full_name": senior.full_name,
                "room_number": senior.room_number
            }

    return {
        "id": current_user.id,
        "email": current_user.email,
        "full_name": current_user.full_name,
        "role": current_user.role,
        "phone": current_user.phone,
        "status": current_user.status,
        "created_at": current_user.created_at,
        "linked_senior": linked_senior
    }

@router.get("/users", response_model=List[UserOut])
def get_all_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["ADMIN"]))
):
    return db.query(User).order_by(User.id.asc()).all()

@router.post("/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(require_roles(["ADMIN"]))
):
    """Admin provisions a new RBAC system user"""
    existing = db.query(User).filter(User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail=f"Email '{user_in.email}' is already registered in ECMS.")
    
    valid_roles = ["ADMIN", "DOCTOR", "CAREGIVER", "SENIOR", "GUARDIAN"]
    clean_role = user_in.role.upper().strip()
    if clean_role not in valid_roles:
        raise HTTPException(status_code=400, detail=f"Invalid role '{clean_role}'. Permitted roles: {', '.join(valid_roles)}")

    hashed_pw = get_password_hash(user_in.password)
    new_user = User(
        email=user_in.email.strip().lower(),
        hashed_password=hashed_pw,
        full_name=user_in.full_name.strip(),
        role=clean_role,
        phone=user_in.phone.strip() if user_in.phone else None,
        status="ACTIVE"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    audit = AuditTrail(
        user_id=current_admin.id,
        user_email=current_admin.email,
        action="USER_PROVISIONED",
        details=f"Admin {current_admin.email} provisioned new {clean_role} user: {new_user.full_name} ({new_user.email})"
    )
    db.add(audit)
    db.commit()

    return new_user

@router.patch("/users/{user_id}/status", response_model=UserOut)
def update_user_status(
    user_id: int,
    status_in: UserStatusUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(require_roles(["ADMIN"]))
):
    """Admin terminates, suspends, or reactivates an account"""
    target_user = db.query(User).filter(User.id == user_id).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="User not found")

    new_status = status_in.status.upper().strip()
    if new_status not in ["ACTIVE", "TERMINATED", "SUSPENDED"]:
        raise HTTPException(status_code=400, detail="Invalid status. Must be ACTIVE, TERMINATED, or SUSPENDED.")

    # Guard: Administrator cannot terminate their own active account
    if target_user.id == current_admin.id and new_status != "ACTIVE":
        raise HTTPException(
            status_code=400,
            detail="Security violation: System Administrator cannot terminate or suspend their own account."
        )

    prev_status = target_user.status
    target_user.status = new_status
    db.commit()
    db.refresh(target_user)

    action_label = "USER_TERMINATED" if new_status == "TERMINATED" else ("USER_REACTIVATED" if new_status == "ACTIVE" else "USER_SUSPENDED")
    audit = AuditTrail(
        user_id=current_admin.id,
        user_email=current_admin.email,
        action=action_label,
        details=f"Admin {current_admin.email} set user {target_user.email} status from {prev_status} to {new_status}"
    )
    db.add(audit)
    db.commit()

    return target_user

@router.delete("/users/{user_id}")
def delete_or_terminate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(require_roles(["ADMIN"]))
):
    """Safely terminate or purge a user account"""
    target_user = db.query(User).filter(User.id == user_id).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="User not found")

    if target_user.id == current_admin.id:
        raise HTTPException(status_code=400, detail="Security violation: Cannot delete your own administrator account.")

    email = target_user.email
    role = target_user.role

    # Check for foreign key links to senior records
    has_links = db.query(Senior).filter((Senior.user_id == user_id) | (Senior.guardian_id == user_id)).first()
    if has_links:
        target_user.status = "TERMINATED"
        db.commit()
        msg = f"User {email} has linked resident records. Account was set to TERMINATED to preserve audit history."
    else:
        db.delete(target_user)
        db.commit()
        msg = f"User {email} was permanently deleted."

    audit = AuditTrail(
        user_id=current_admin.id,
        user_email=current_admin.email,
        action="USER_TERMINATED",
        details=f"Admin {current_admin.email} removed/terminated user {email} ({role})"
    )
    db.add(audit)
    db.commit()

    return {"message": msg, "user_id": user_id}
