-- ═══════════════════════════════════════════════════════════════════════════
-- ECMS – MySQL Schema (mirrors the SQLAlchemy models in backend/app/models.py)
-- Run once:  mysql -u root -p < db/schema.sql
-- ═══════════════════════════════════════════════════════════════════════════

CREATE DATABASE IF NOT EXISTS ecms_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ecms_db;

-- ── Users ─────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS users (
  id              INT AUTO_INCREMENT PRIMARY KEY,
  email           VARCHAR(120) NOT NULL UNIQUE,
  hashed_password VARCHAR(255) NOT NULL,
  full_name       VARCHAR(100) NOT NULL,
  role            ENUM('ADMIN','DOCTOR','CAREGIVER','SENIOR','GUARDIAN') NOT NULL DEFAULT 'CAREGIVER',
  phone           VARCHAR(30),
  status          ENUM('ACTIVE','INACTIVE') NOT NULL DEFAULT 'ACTIVE',
  created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ── Seniors ───────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS seniors (
  id               INT AUTO_INCREMENT PRIMARY KEY,
  mrn              VARCHAR(50)  NOT NULL UNIQUE,
  full_name        VARCHAR(100) NOT NULL,
  date_of_birth    VARCHAR(30)  NOT NULL,
  gender           ENUM('MALE','FEMALE','OTHER') NOT NULL,
  blood_group      VARCHAR(10),
  room_number      VARCHAR(30)  NOT NULL,
  phone            VARCHAR(30),
  address          VARCHAR(255),
  emergency_name   VARCHAR(100) NOT NULL,
  emergency_phone  VARCHAR(50)  NOT NULL,
  primary_doctor   VARCHAR(100),
  chronic_ailments TEXT,
  drug_allergies   TEXT,
  guardian_id      INT,
  user_id          INT,
  created_at       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (guardian_id) REFERENCES users(id) ON DELETE SET NULL,
  FOREIGN KEY (user_id)     REFERENCES users(id) ON DELETE SET NULL
);

-- ── Medications ───────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS medications (
  id                  INT AUTO_INCREMENT PRIMARY KEY,
  senior_id           INT          NOT NULL,
  name                VARCHAR(120) NOT NULL,
  dosage              VARCHAR(60)  NOT NULL,
  frequency           VARCHAR(60)  NOT NULL,
  scheduled_times     VARCHAR(100) NOT NULL,
  instructions        VARCHAR(255),
  prescription_status ENUM('ACTIVE','PAUSED','DISCONTINUED') NOT NULL DEFAULT 'ACTIVE',
  prescribed_by       VARCHAR(100),
  start_date          VARCHAR(30)  NOT NULL,
  end_date            VARCHAR(30),
  FOREIGN KEY (senior_id) REFERENCES seniors(id) ON DELETE CASCADE
);

-- ── Medication Logs ───────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS medication_logs (
  id              INT AUTO_INCREMENT PRIMARY KEY,
  medication_id   INT         NOT NULL,
  senior_id       INT         NOT NULL,
  scheduled_time  VARCHAR(30) NOT NULL,
  administered_at DATETIME,
  status          ENUM('PENDING','GIVEN','MISSED','REFUSED') NOT NULL DEFAULT 'PENDING',
  notes           VARCHAR(255),
  administered_by VARCHAR(100),
  FOREIGN KEY (medication_id) REFERENCES medications(id) ON DELETE CASCADE,
  FOREIGN KEY (senior_id)     REFERENCES seniors(id)     ON DELETE CASCADE
);

-- ── Vitals ────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS vitals (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  senior_id     INT     NOT NULL,
  recorded_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  systolic_bp   INT     NOT NULL,
  diastolic_bp  INT     NOT NULL,
  pulse_rate    INT     NOT NULL,
  spo2          INT     NOT NULL,
  temperature   DECIMAL(5,2) NOT NULL,
  blood_glucose INT     NOT NULL,
  is_anomaly    TINYINT(1) NOT NULL DEFAULT 0,
  anomaly_notes VARCHAR(255),
  recorded_by   VARCHAR(100) NOT NULL,
  FOREIGN KEY (senior_id) REFERENCES seniors(id) ON DELETE CASCADE
);

-- ── Appointments ──────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS appointments (
  id                 INT AUTO_INCREMENT PRIMARY KEY,
  senior_id          INT          NOT NULL,
  doctor_id          INT,
  doctor_name        VARCHAR(100) NOT NULL,
  specialty          VARCHAR(100) NOT NULL,
  scheduled_at       DATETIME     NOT NULL,
  consultation_type  ENUM('IN_PERSON','TELECONSULT') NOT NULL DEFAULT 'IN_PERSON',
  status             ENUM('SCHEDULED','COMPLETED','CANCELLED') NOT NULL DEFAULT 'SCHEDULED',
  notes              TEXT,
  teleconsult_link   VARCHAR(255),
  FOREIGN KEY (senior_id) REFERENCES seniors(id)  ON DELETE CASCADE,
  FOREIGN KEY (doctor_id) REFERENCES users(id)     ON DELETE SET NULL
);

-- ── Emergency Alerts ──────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS emergency_alerts (
  id           INT AUTO_INCREMENT PRIMARY KEY,
  senior_id    INT         NOT NULL,
  triggered_at DATETIME    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  trigger_type ENUM('SOS_BUTTON','FALL_DETECTION','VITALS_ANOMALY') NOT NULL DEFAULT 'SOS_BUTTON',
  latitude     DECIMAL(10,7),
  longitude    DECIMAL(10,7),
  status       ENUM('TRIGGERED','DISPATCHED','RESPONDING','RESOLVED') NOT NULL DEFAULT 'TRIGGERED',
  resolved_at  DATETIME,
  resolved_by  VARCHAR(100),
  notes        TEXT,
  FOREIGN KEY (senior_id) REFERENCES seniors(id) ON DELETE CASCADE
);

-- ── Shift Notes ───────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS shift_notes (
  id               INT AUTO_INCREMENT PRIMARY KEY,
  caregiver_id     INT          NOT NULL,
  caregiver_name   VARCHAR(100) NOT NULL,
  shift_date       VARCHAR(30)  NOT NULL,
  shift_type       ENUM('MORNING','EVENING','NIGHT') NOT NULL,
  handover_to      VARCHAR(100) NOT NULL,
  notes            TEXT         NOT NULL,
  flagged_seniors  TEXT,
  signed_at        DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (caregiver_id) REFERENCES users(id) ON DELETE CASCADE
);

-- ── Audit Logs ────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS audit_logs (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  user_id    INT,
  user_email VARCHAR(120) NOT NULL,
  action     VARCHAR(100) NOT NULL,
  details    TEXT,
  ip_address VARCHAR(50)  NOT NULL DEFAULT '127.0.0.1',
  timestamp  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP
);

