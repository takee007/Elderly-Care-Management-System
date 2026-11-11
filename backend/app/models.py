from datetime import datetime, timezone
from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, Float, ForeignKey, Text, Enum
)
from sqlalchemy.orm import relationship
from .database import Base

class RoleEnum(str):
    ADMIN = "ADMIN"
    DOCTOR = "DOCTOR"
    CAREGIVER = "CAREGIVER"
    SENIOR = "SENIOR"
    GUARDIAN = "GUARDIAN"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(120), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)
    role = Column(String(30), nullable=False, default="CAREGIVER")  # ADMIN, DOCTOR, CAREGIVER, SENIOR, GUARDIAN
    phone = Column(String(30), nullable=True)
    status = Column(String(20), default="ACTIVE")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    seniors_as_guardian = relationship("Senior", back_populates="guardian", foreign_keys="[Senior.guardian_id]")

class Senior(Base):
    __tablename__ = "seniors"

    id = Column(Integer, primary_key=True, index=True)
    mrn = Column(String(50), unique=True, index=True, nullable=False)  # Medical Record Number
    full_name = Column(String(100), nullable=False)
    date_of_birth = Column(String(30), nullable=False)
    gender = Column(String(20), nullable=False)
    blood_group = Column(String(10), nullable=True)
    room_number = Column(String(30), nullable=False)
    phone = Column(String(30), nullable=True)
    address = Column(String(255), nullable=True)
    emergency_name = Column(String(100), nullable=False)
    emergency_phone = Column(String(50), nullable=False)
    primary_doctor = Column(String(100), nullable=True)
    chronic_ailments = Column(Text, nullable=True)
    drug_allergies = Column(Text, nullable=True)
    guardian_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    guardian = relationship("User", foreign_keys=[guardian_id], back_populates="seniors_as_guardian")
    medications = relationship("Medication", back_populates="senior", cascade="all, delete-orphan")
    vitals = relationship("VitalSign", back_populates="senior", cascade="all, delete-orphan")
    appointments = relationship("Appointment", back_populates="senior", cascade="all, delete-orphan")
    emergency_alerts = relationship("EmergencyAlert", back_populates="senior", cascade="all, delete-orphan")

class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    senior_id = Column(Integer, ForeignKey("seniors.id"), nullable=False)
    name = Column(String(120), nullable=False)
    dosage = Column(String(60), nullable=False)
    frequency = Column(String(60), nullable=False)
    scheduled_times = Column(String(100), nullable=False)  # e.g. "08:00, 20:00"
    instructions = Column(String(255), nullable=True)
    prescription_status = Column(String(30), default="ACTIVE")  # ACTIVE, PAUSED, DISCONTINUED
    prescribed_by = Column(String(100), nullable=True)
    start_date = Column(String(30), nullable=False)
    end_date = Column(String(30), nullable=True)

    senior = relationship("Senior", back_populates="medications")
    logs = relationship("MedicationLog", back_populates="medication", cascade="all, delete-orphan")

class MedicationLog(Base):
    __tablename__ = "medication_logs"

    id = Column(Integer, primary_key=True, index=True)
    medication_id = Column(Integer, ForeignKey("medications.id"), nullable=False)
    senior_id = Column(Integer, ForeignKey("seniors.id"), nullable=False)
    scheduled_time = Column(String(30), nullable=False)
    administered_at = Column(DateTime, nullable=True)
    status = Column(String(30), default="PENDING")  # PENDING, GIVEN, MISSED, REFUSED
    notes = Column(String(255), nullable=True)
    administered_by = Column(String(100), nullable=True)

    medication = relationship("Medication", back_populates="logs")

class VitalSign(Base):
    __tablename__ = "vitals"

    id = Column(Integer, primary_key=True, index=True)
    senior_id = Column(Integer, ForeignKey("seniors.id"), nullable=False)
    recorded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    systolic_bp = Column(Integer, nullable=False)   # mmHg (norm: 90-130)
    diastolic_bp = Column(Integer, nullable=False)  # mmHg (norm: 60-85)
    pulse_rate = Column(Integer, nullable=False)    # bpm (norm: 60-100)
    spo2 = Column(Integer, nullable=False)          # % (norm: 95-100)
    temperature = Column(Float, nullable=False)     # °F (norm: 97.5 - 99.0)
    blood_glucose = Column(Integer, nullable=False) # mg/dL (norm: 70-140)
    is_anomaly = Column(Boolean, default=False)
    anomaly_notes = Column(String(255), nullable=True)
    recorded_by = Column(String(100), nullable=False)

    senior = relationship("Senior", back_populates="vitals")

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    senior_id = Column(Integer, ForeignKey("seniors.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    doctor_name = Column(String(100), nullable=False)
    specialty = Column(String(100), nullable=False)
    scheduled_at = Column(DateTime, nullable=False)
    consultation_type = Column(String(30), default="IN_PERSON")  # IN_PERSON, TELECONSULT
    status = Column(String(30), default="SCHEDULED")  # SCHEDULED, COMPLETED, CANCELLED
    notes = Column(Text, nullable=True)
    teleconsult_link = Column(String(255), nullable=True)

    senior = relationship("Senior", back_populates="appointments")

class EmergencyAlert(Base):
    __tablename__ = "emergency_alerts"

    id = Column(Integer, primary_key=True, index=True)
    senior_id = Column(Integer, ForeignKey("seniors.id"), nullable=False)
    triggered_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    trigger_type = Column(String(50), default="SOS_BUTTON")  # SOS_BUTTON, FALL_DETECTION, VITALS_ANOMALY
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    status = Column(String(30), default="TRIGGERED")  # TRIGGERED, DISPATCHED, RESPONDING, RESOLVED
    resolved_at = Column(DateTime, nullable=True)
    resolved_by = Column(String(100), nullable=True)
    notes = Column(Text, nullable=True)

    senior = relationship("Senior", back_populates="emergency_alerts")

class ShiftNote(Base):
    __tablename__ = "shift_notes"

    id = Column(Integer, primary_key=True, index=True)
    caregiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    caregiver_name = Column(String(100), nullable=False)
    shift_date = Column(String(30), nullable=False)
    shift_type = Column(String(30), nullable=False)  # MORNING, EVENING, NIGHT
    handover_to = Column(String(100), nullable=False)
    notes = Column(Text, nullable=False)
    flagged_seniors = Column(Text, nullable=True)
    signed_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class AuditTrail(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    user_email = Column(String(120), nullable=False)
    action = Column(String(100), nullable=False)
    details = Column(Text, nullable=True)
    ip_address = Column(String(50), default="127.0.0.1")
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
