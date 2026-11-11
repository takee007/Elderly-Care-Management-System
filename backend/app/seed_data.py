from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from .database import SessionLocal, Base, engine
from .models import User, Senior, Medication, MedicationLog, VitalSign, Appointment, EmergencyAlert, ShiftNote, AuditTrail
from .auth import get_password_hash

def seed_database(db: Session, force: bool = False):
    # Check if data already exists
    if not force and db.query(User).first():
        print("Database already contains data. Skipping seed.")
        return

    if force:
        # Clear existing tables for fresh localization
        db.query(MedicationLog).delete()
        db.query(Medication).delete()
        db.query(VitalSign).delete()
        db.query(Appointment).delete()
        db.query(EmergencyAlert).delete()
        db.query(ShiftNote).delete()
        db.query(AuditTrail).delete()
        db.query(Senior).delete()
        db.query(User).delete()
        db.commit()

    print("Seeding Bangladesh Elderly Care Management System (Probin Sheba Kendro)...")

    # 1. Users for each role with authentic Bangladeshi profiles (100% English strings)
    hashed_pwd = get_password_hash("password123")

    admin = User(
        email="admin@probin.gov.bd",
        hashed_password=hashed_pwd,
        full_name="Engr. Md. Tariqul Islam",
        role="ADMIN",
        phone="+880 1711-098765",
        status="ACTIVE"
    )
    doctor = User(
        email="dr.hasan@probin.org.bd",
        hashed_password=hashed_pwd,
        full_name="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        role="DOCTOR",
        phone="+880 1819-234567",
        status="ACTIVE"
    )
    caregiver = User(
        email="nurse.fatema@probin.org.bd",
        hashed_password=hashed_pwd,
        full_name="Fatema Begum, BSc Nursing (RN)",
        role="CAREGIVER",
        phone="+880 1912-345678",
        status="ACTIVE"
    )
    guardian = User(
        email="tanvir.ahmed@gmail.com",
        hashed_password=hashed_pwd,
        full_name="Tanvir Ahmed",
        role="GUARDIAN",
        phone="+880 1712-889900",
        status="ACTIVE"
    )
    senior_user = User(
        email="shamsuddin@probin.org.bd",
        hashed_password=hashed_pwd,
        full_name="Alhaj Mohammad Shamsuddin Ahmed",
        role="SENIOR",
        phone="+880 1715-443322",
        status="ACTIVE"
    )

    db.add_all([admin, doctor, caregiver, guardian, senior_user])
    db.commit()
    db.refresh(admin)
    db.refresh(doctor)
    db.refresh(caregiver)
    db.refresh(guardian)
    db.refresh(senior_user)

    # 2. Bangladeshi Senior Residents
    senior1 = Senior(
        mrn="BD-MRN-90210",
        full_name="Alhaj Mohammad Shamsuddin Ahmed",
        date_of_birth="1948-02-15",
        gender="Male",
        blood_group="B+",
        room_number="Suite 204 (Padma Wing)",
        phone="+880 1715-443322",
        address="Probin Nibash Assisted Living, Dhanmondi Road 8/A, Dhaka-1209",
        emergency_name="Tanvir Ahmed (Son)",
        emergency_phone="+880 1712-889900",
        primary_doctor="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        chronic_ailments="Type 2 Diabetes Mellitus, Stage 1 Hypertension, Chronic Kidney Disease (Stage 2)",
        drug_allergies="Penicillin, Sulfa drugs",
        guardian_id=guardian.id,
        user_id=senior_user.id
    )

    senior2 = Senior(
        mrn="BD-MRN-90211",
        full_name="Begum Rokeya Chowdhury",
        date_of_birth="1944-11-20",
        gender="Female",
        blood_group="O+",
        room_number="Suite 108 (Meghna Wing)",
        phone="+880 1814-776655",
        address="Probin Nibash Assisted Living, Dhanmondi Road 8/A, Dhaka-1209",
        emergency_name="Nusrat Chowdhury (Daughter)",
        emergency_phone="+880 1819-987654",
        primary_doctor="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        chronic_ailments="Severe Knee Osteoarthritis, Post-Cataract Glaucoma",
        drug_allergies="None known (NKDA)",
        guardian_id=None,
        user_id=None
    )

    senior3 = Senior(
        mrn="BD-MRN-90212",
        full_name="Kazi Nurul Huda",
        date_of_birth="1942-08-10",
        gender="Male",
        blood_group="A+",
        room_number="Suite 312 (Jamuna Pavilion)",
        phone="+880 1911-332211",
        address="Probin Nibash Assisted Living, Dhanmondi Road 8/A, Dhaka-1209",
        emergency_name="Nasreen Huda (Wife)",
        emergency_phone="+880 1915-554433",
        primary_doctor="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        chronic_ailments="Early-Stage Alzheimer's Disease / Memory Care, Atrial Fibrillation",
        drug_allergies="Aspirin (Gastric Ulceration)",
        guardian_id=None,
        user_id=None
    )

    senior4 = Senior(
        mrn="BD-MRN-90213",
        full_name="Sultana Razia Begum",
        date_of_birth="1952-04-05",
        gender="Female",
        blood_group="AB+",
        room_number="Suite 102 (Surma Wing)",
        phone="+880 1718-990011",
        address="Probin Nibash Assisted Living, Dhanmondi Road 8/A, Dhaka-1209",
        emergency_name="Farhan Razia (Son)",
        emergency_phone="+880 1716-223344",
        primary_doctor="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        chronic_ailments="Coronary Artery Disease (Post-Stent), Bronchial Asthma",
        drug_allergies="Ibuprofen, NSAIDs",
        guardian_id=None,
        user_id=None
    )

    db.add_all([senior1, senior2, senior3, senior4])
    db.commit()
    db.refresh(senior1)
    db.refresh(senior2)
    db.refresh(senior3)
    db.refresh(senior4)

    # 3. Medications (Bangladeshi Formulations from Square, Incepta, Beximco, Renata)
    med1 = Medication(
        senior_id=senior1.id,
        name="Tab. Comet 500mg (Metformin HCl)",
        dosage="500 mg",
        frequency="Twice daily post-meal",
        scheduled_times="08:30, 20:30",
        instructions="Take immediately after meals with a glass of water (Square Pharmaceuticals)",
        prescription_status="ACTIVE",
        prescribed_by="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        start_date="2026-01-10"
    )
    med2 = Medication(
        senior_id=senior1.id,
        name="Tab. Camlosart 5/20 (Amlodipine + Olmesartan)",
        dosage="5/20 mg",
        frequency="Once daily morning post-breakfast",
        scheduled_times="08:30",
        instructions="Monitor blood pressure prior to administration (Incepta Pharmaceuticals)",
        prescription_status="ACTIVE",
        prescribed_by="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        start_date="2026-02-01"
    )
    med3 = Medication(
        senior_id=senior1.id,
        name="Tab. Rosuva 10mg (Rosuvastatin)",
        dosage="10 mg",
        frequency="Once daily at bedtime",
        scheduled_times="22:00",
        instructions="Take at night before sleep with water (Renata Limited)",
        prescription_status="ACTIVE",
        prescribed_by="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        start_date="2026-01-15"
    )
    med4 = Medication(
        senior_id=senior1.id,
        name="Cap. Bicozin (Vitamin B Complex + Zinc)",
        dosage="1 Capsule",
        frequency="Once daily at noon after lunch",
        scheduled_times="13:30",
        instructions="General geriatric nutrition and nerve support supplement (Square Pharmaceuticals)",
        prescription_status="ACTIVE",
        prescribed_by="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        start_date="2026-03-01"
    )
    med5 = Medication(
        senior_id=senior2.id,
        name="Tab. Seclo 20mg (Omeprazole)",
        dosage="20 mg",
        frequency="Once daily morning before breakfast",
        scheduled_times="07:30",
        instructions="Take on an empty stomach 30 minutes before morning breakfast (Square Pharmaceuticals)",
        prescription_status="ACTIVE",
        prescribed_by="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        start_date="2026-02-15"
    )
    med6 = Medication(
        senior_id=senior3.id,
        name="Tab. Alzepil 5mg (Donepezil HCl)",
        dosage="5 mg",
        frequency="Once daily at bedtime",
        scheduled_times="21:30",
        instructions="Cognitive support - administer with light evening snack (Beximco Pharma)",
        prescription_status="ACTIVE",
        prescribed_by="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        start_date="2026-04-12"
    )

    db.add_all([med1, med2, med3, med4, med5, med6])
    db.commit()
    db.refresh(med1)
    db.refresh(med2)
    db.refresh(med3)
    db.refresh(med4)
    db.refresh(med5)
    db.refresh(med6)

    # 4. Medication Administration Logs (eMAR in English)
    now = datetime.now(timezone.utc)
    log1 = MedicationLog(
        medication_id=med1.id,
        senior_id=senior1.id,
        scheduled_time="08:30",
        administered_at=now - timedelta(hours=5),
        status="GIVEN",
        administered_by="Fatema Begum, RN",
        notes="Administered with morning breakfast. Resident in stable condition."
    )
    log2 = MedicationLog(
        medication_id=med2.id,
        senior_id=senior1.id,
        scheduled_time="08:30",
        administered_at=now - timedelta(hours=5),
        status="GIVEN",
        administered_by="Fatema Begum, RN",
        notes="Blood pressure verified at 125/80 mmHg before successful administration."
    )
    log3 = MedicationLog(
        medication_id=med4.id,
        senior_id=senior1.id,
        scheduled_time="13:30",
        administered_at=now - timedelta(hours=1),
        status="GIVEN",
        administered_by="Fatema Begum, RN",
        notes="Administered 1 capsule with post-lunch water."
    )
    log4 = MedicationLog(
        medication_id=med1.id,
        senior_id=senior1.id,
        scheduled_time="20:30",
        status="PENDING",
        notes="Scheduled for post-dinner dose."
    )
    log5 = MedicationLog(
        medication_id=med3.id,
        senior_id=senior1.id,
        scheduled_time="22:00",
        status="PENDING",
        notes="Scheduled bedtime dose."
    )

    db.add_all([log1, log2, log3, log4, log5])

    # 5. Longitudinal Vitals Telemetry (All English)
    v1 = VitalSign(
        senior_id=senior1.id,
        recorded_at=now - timedelta(hours=18),
        systolic_bp=122,
        diastolic_bp=80,
        pulse_rate=72,
        spo2=98,
        temperature=98.4,
        blood_glucose=112,
        is_anomaly=False,
        anomaly_notes="Normal baseline blood pressure and blood glucose",
        recorded_by="Fatema Begum, RN"
    )
    v2 = VitalSign(
        senior_id=senior1.id,
        recorded_at=now - timedelta(hours=5),
        systolic_bp=125,
        diastolic_bp=82,
        pulse_rate=74,
        spo2=97,
        temperature=98.6,
        blood_glucose=126,
        is_anomaly=False,
        anomaly_notes="Stable post-prandial glucose reading",
        recorded_by="Fatema Begum, RN"
    )
    v3 = VitalSign(
        senior_id=senior1.id,
        recorded_at=now - timedelta(minutes=40),
        systolic_bp=144,
        diastolic_bp=92,
        pulse_rate=86,
        spo2=95,
        temperature=98.6,
        blood_glucose=148,
        is_anomaly=True,
        anomaly_notes="Elevated Blood Pressure Alert (144/92 mmHg) - Resident resting comfortably under observation",
        recorded_by="Fatema Begum, RN"
    )

    v4 = VitalSign(
        senior_id=senior2.id,
        recorded_at=now - timedelta(hours=4),
        systolic_bp=118,
        diastolic_bp=76,
        pulse_rate=70,
        spo2=99,
        temperature=98.2,
        blood_glucose=95,
        is_anomaly=False,
        anomaly_notes="Blood pressure and SpO2 in optimal range",
        recorded_by="Fatema Begum, RN"
    )

    v5 = VitalSign(
        senior_id=senior3.id,
        recorded_at=now - timedelta(hours=2),
        systolic_bp=130,
        diastolic_bp=82,
        pulse_rate=80,
        spo2=96,
        temperature=98.4,
        blood_glucose=105,
        is_anomaly=False,
        anomaly_notes="Jamuna Pavilion memory care routine observation",
        recorded_by="Fatema Begum, RN"
    )

    db.add_all([v1, v2, v3, v4, v5])

    # 6. Appointments
    appt1 = Appointment(
        senior_id=senior1.id,
        doctor_id=doctor.id,
        doctor_name="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        specialty="Geriatric Medicine & Cardiology (BSMMU/BIRDEM)",
        scheduled_at=now + timedelta(days=2, hours=4),
        consultation_type="TELECONSULT",
        status="SCHEDULED",
        notes="Glycemic control, kidney profile (serum creatinine) and hypertension teleconsultation review.",
        teleconsult_link=f"https://meet.jit.si/ECMS-BD-Shamsuddin-{senior1.id}"
    )
    appt2 = Appointment(
        senior_id=senior3.id,
        doctor_id=doctor.id,
        doctor_name="Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS",
        specialty="Neurology & Memory Care",
        scheduled_at=now + timedelta(days=4, hours=2),
        consultation_type="IN_PERSON",
        status="SCHEDULED",
        notes="Mini-Mental State Exam (MMSE) longitudinal cognitive progression assessment."
    )
    db.add_all([appt1, appt2])

    # 7. Shift Handoff
    shift_note = ShiftNote(
        caregiver_id=caregiver.id,
        caregiver_name="Fatema Begum, BSc Nursing (RN)",
        shift_date=datetime.now().strftime("%Y-%m-%d"),
        shift_type="MORNING",
        handover_to="Shirin Akhter, Diploma Nurse (Evening Shift Lead)",
        notes="All morning oral medications (Comet, Camlosart) administered on schedule. Mr. Shamsuddin exhibited mild BP elevation (144/92) at 12:15 PM; resting comfortably in lounge chair, hydration encouraged. Mrs. Begum Rokeya Chowdhury completed 20 minutes assisted walking with physiotherapist. National Emergency 999 and DGHS 16263 channels active.",
        flagged_seniors="Alhaj Mohammad Shamsuddin Ahmed (Suite 204 - Padma Wing) - Re-check blood pressure before dinner dose."
    )
    db.add(shift_note)

    # 8. Audit Trails
    db.add_all([
        AuditTrail(
            user_id=admin.id,
            user_email=admin.email,
            action="SYSTEM_INITIALIZATION_BD",
            details="Bangladesh Elderly Care Management System (Probin Sheba Kendro) initialized with national healthcare compliance standards."
        ),
        AuditTrail(
            user_id=caregiver.id,
            user_email=caregiver.email,
            action="VITALS_TELEMETRY_LOGGED",
            details="Recorded routine telemetry for Padma and Meghna ward residents. Dhaka Timezone UTC+6."
        )
    ])

    db.commit()
    print("Bangladesh Elderly Care Management System (Probin Sheba Kendro) seeded successfully in English.")

if __name__ == "__main__":
    db = SessionLocal()
    try:
        seed_database(db, force=True)
    finally:
        db.close()
