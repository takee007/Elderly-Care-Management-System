from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr

# Auth Schemas
class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    email: str
    full_name: str
    role: str

class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: str = "CAREGIVER"
    phone: Optional[str] = None

class UserStatusUpdate(BaseModel):
    status: str  # ACTIVE, TERMINATED, SUSPENDED

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: str
    phone: Optional[str] = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

# Senior Schemas
class SeniorBase(BaseModel):
    mrn: str
    full_name: str
    date_of_birth: str
    gender: str
    blood_group: Optional[str] = None
    room_number: str
    phone: Optional[str] = None
    address: Optional[str] = None
    emergency_name: str
    emergency_phone: str
    primary_doctor: Optional[str] = None
    chronic_ailments: Optional[str] = None
    drug_allergies: Optional[str] = None
    guardian_id: Optional[int] = None
    user_id: Optional[int] = None

class SeniorCreate(SeniorBase):
    pass

class SeniorOut(SeniorBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Vitals Schemas
class VitalSignCreate(BaseModel):
    senior_id: int
    systolic_bp: int
    diastolic_bp: int
    pulse_rate: int
    spo2: int
    temperature: float
    blood_glucose: int
    recorded_by: str
    notes: Optional[str] = None

class VitalSignOut(BaseModel):
    id: int
    senior_id: int
    recorded_at: datetime
    systolic_bp: int
    diastolic_bp: int
    pulse_rate: int
    spo2: int
    temperature: float
    blood_glucose: int
    is_anomaly: bool
    anomaly_notes: Optional[str] = None
    recorded_by: str

    class Config:
        from_attributes = True

# Medication Schemas
class MedicationCreate(BaseModel):
    senior_id: int
    name: str
    dosage: str
    frequency: str
    scheduled_times: str
    instructions: Optional[str] = None
    prescribed_by: Optional[str] = None
    start_date: str
    end_date: Optional[str] = None

class MedicationOut(BaseModel):
    id: int
    senior_id: int
    name: str
    dosage: str
    frequency: str
    scheduled_times: str
    instructions: Optional[str] = None
    prescription_status: str
    prescribed_by: Optional[str] = None
    start_date: str
    end_date: Optional[str] = None

    class Config:
        from_attributes = True

class MedicationLogCreate(BaseModel):
    medication_id: int
    senior_id: int
    scheduled_time: str
    status: str = "GIVEN"  # GIVEN, MISSED, REFUSED
    notes: Optional[str] = None
    administered_by: str

class MedicationLogOut(BaseModel):
    id: int
    medication_id: int
    senior_id: int
    scheduled_time: str
    administered_at: Optional[datetime] = None
    status: str
    notes: Optional[str] = None
    administered_by: Optional[str] = None

    class Config:
        from_attributes = True

# Appointment Schemas
class AppointmentCreate(BaseModel):
    senior_id: int
    doctor_id: Optional[int] = None
    doctor_name: str
    specialty: str
    scheduled_at: datetime
    consultation_type: str = "IN_PERSON"
    notes: Optional[str] = None
    teleconsult_link: Optional[str] = None

class AppointmentOut(BaseModel):
    id: int
    senior_id: int
    doctor_id: Optional[int] = None
    doctor_name: str
    specialty: str
    scheduled_at: datetime
    consultation_type: str
    status: str
    notes: Optional[str] = None
    teleconsult_link: Optional[str] = None

    class Config:
        from_attributes = True

# Emergency Alert Schemas
class EmergencyAlertCreate(BaseModel):
    senior_id: int
    trigger_type: str = "SOS_BUTTON"
    latitude: Optional[float] = 23.8151
    longitude: Optional[float] = 90.4255
    notes: Optional[str] = "Immediate Senior SOS distress initiated via Emergency Button"

class EmergencyAlertOut(BaseModel):
    id: int
    senior_id: int
    triggered_at: datetime
    trigger_type: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    status: str
    resolved_at: Optional[datetime] = None
    resolved_by: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True

# Shift Note Schemas
class ShiftNoteCreate(BaseModel):
    caregiver_id: int
    caregiver_name: str
    shift_date: str
    shift_type: str
    handover_to: str
    notes: str
    flagged_seniors: Optional[str] = None

class ShiftNoteOut(BaseModel):
    id: int
    caregiver_id: int
    caregiver_name: str
    shift_date: str
    shift_type: str
    handover_to: str
    notes: str
    flagged_seniors: Optional[str] = None
    signed_at: datetime

    class Config:
        from_attributes = True

# Audit Schemas
class AuditTrailOut(BaseModel):
    id: int
    user_id: Optional[int] = None
    user_email: str
    action: str
    details: Optional[str] = None
    ip_address: str
    timestamp: datetime

    class Config:
        from_attributes = True
