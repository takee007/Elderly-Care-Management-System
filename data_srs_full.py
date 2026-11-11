"""
data_srs_full.py
Complete, exhaustive data definitions for Elderly Care Management System SRS
strictly following SRS_Template.docx.pdf (IEEE Std 830 industry template).
"""

METADATA = {
    "project_title": "Elderly Care Management System (ECMS)",
    "doc_title": "Software Requirements Specification",
    "version": "Version 1.0 (Final Release)",
    "status": "Approved",
    "author_name": "Farzana Sadia Takee",
    "author_role": "Lead System Analyst & Full-Stack Developer",
    "student_id": "2211175",
    "course": "CSE309 - Web Programming (Section: 02, Autumn 2025)",
    "instructor": "Md Abu Sayed, Senior Lecturer, Department of Computer Science & Engineering",
    "organization": "Independent University, Bangladesh (IUB)",
    "date": "October 18, 2025"
}

REVISION_HISTORY = [
    ["Farzana Sadia Takee", "September 05, 2025", "Initial Draft of ECMS SRS based on Stakeholder Elicitation", "0.1", "September 10, 2025"],
    ["Farzana Sadia Takee", "September 22, 2025", "Integrated Domain Model, Detailed Use Case Flows, and Exception Tables", "0.5", "September 28, 2025"],
    ["Farzana Sadia Takee", "October 08, 2025", "Added Comprehensive NFRs, External Interfaces, and UI Annotations", "0.9", "October 12, 2025"],
    ["Farzana Sadia Takee", "October 18, 2025", "Final Release for System Verification & CSE309 Academic Evaluation", "1.0", "October 18, 2025"]
]

INTENDED_AUDIENCE = [
    ["S-1", "Family Guardian", "Checking correspondence of family oversight goals, resident health transparency, automated SMS notification requirements, and digital billing transparency."],
    ["S-2", "Development Team", "Forming the accurate architectural vision of the project, implementing frontend responsive interfaces, backend PHP endpoints, database schemas, and business rules without ambiguity."],
    ["S-3", "QA / Testing Team", "Formulating test plans, automated verification scripts, boundary exception test suites, and compliance audits against WCAG 2.1 AA accessibility standards."],
    ["S-4", "Project Manager / BA", "Estimating development velocity, planning sprint resource allocations, tracking requirements traceability matrices, and managing delivery timelines."],
    ["S-5", "Caregivers & Physicians", "Validating operational clinical workflows, medication administration protocols, vital sign alert thresholds, and shift handover procedures."]
]

USER_CLASSES = [
    ["U-1", "System Administrator", "A technical superuser who manages system configurations, user account lifecycles, role-based access permissions, audit trail integrity, and automated database backups."],
    ["U-2", "Family Guardian", "A registered family sponsor who onboards elderly residents, manages medical records, monitors daily care logs, receives emergency notifications, and manages financial billing."],
    ["U-3", "Professional Caregiver / Nurse", "A certified clinical staff member who logs daily vitals telemetry, records medication administration adherence, tracks ADLs, and logs shift handoff notes."],
    ["U-4", "Consulting Physician / Doctor", "A licensed medical practitioner who reviews longitudinal health records, prescribes medication schedules, establishes vital threshold alert boundaries, and conducts teleconsultations."],
    ["U-5", "Elderly Senior Resident", "The primary care recipient who utilizes a simplified, high-contrast, large-button interface to view daily schedules, receive pill alarms, and trigger one-touch emergency SOS alerts."]
]

GLOSSARY = [
    ["ADL", "Activities of Daily Living: Basic daily self-care tasks (eating, bathing, mobility, medication intake) tracked in geriatric care."],
    ["API", "Application Programming Interface: A formal set of HTTP REST endpoints allowing structured data interchange between frontend and backend."],
    ["Bcrypt", "A key derivation and password hashing function based on the Blowfish cipher, incorporating adaptive work factors to defeat brute-force attacks."],
    ["BPM", "Beats Per Minute: Clinical metric denoting heart rate in vitals monitoring."],
    ["CSRF", "Cross-Site Request Forgery: A web security vulnerability mitigated in ECMS via cryptographically secure session-bound tokens."],
    ["DFD", "Data Flow Diagram: A graphical modeling technique depicting the movement, transformation, and storage of data across system processes."],
    ["EHR", "Electronic Health Record: Digital medical history of a resident including diagnoses, allergies, vitals, and clinical progress notes."],
    ["ERD", "Entity-Relationship Diagram: A visual database modeling artifact detailing tables, columns, primary/foreign keys, and entity cardinalities."],
    ["FHIR", "Fast Healthcare Interoperability Resources: Healthcare data exchange standard guidelines referenced for medical record schemas."],
    ["GDPR / DPA", "General Data Protection Regulation / Digital Security Act: Legal frameworks governing personal healthcare data privacy and non-repudiation."],
    ["GUI", "Graphical User Interface: Visual interface elements enabling interactive human-computer interaction."],
    ["HIPAA", "Health Insurance Portability and Accountability Act: Benchmark regulatory standard for medical data protection and confidentiality."],
    ["HTTP / HTTPS", "Hypertext Transfer Protocol Secure: Encrypted communication protocol utilizing TLS 1.3 for secure web transactions."],
    ["IoT", "Internet of Things: Networked physical devices (e.g., Bluetooth pulse oximeters, smart wearable panic pendants)."],
    ["JSON", "JavaScript Object Notation: Standard lightweight data interchange format used across ECMS asynchronous REST endpoints."],
    ["LAMP", "Linux, Apache, MySQL, PHP: The open-source web application software stack hosting the ECMS production environment."],
    ["MAR", "Medication Administration Record: The formal clinical record of medications prescribed, scheduled, administered, missed, or refused."],
    ["MVC", "Model-View-Controller: Architectural software design pattern separating data logic, presentation, and user interaction."],
    ["NFR", "Non-Functional Requirement: System operational attributes including performance, security, reliability, and usability."],
    ["PDO", "PHP Data Objects: A consistent abstraction layer providing parameterized database queries to eliminate SQL injection."],
    ["RBAC", "Role-Based Access Control: Security mechanism restricting system access based on authenticated user roles (Admin, Guardian, Caregiver, Doctor, Senior)."],
    ["REST", "Representational State Transfer: Architectural style for networked applications using standard HTTP verbs (GET, POST, PUT, DELETE)."],
    ["SDLC", "Software Development Life Cycle: Structured framework (Agile Scrum) guiding the engineering and iterative delivery of ECMS."],
    ["SMS", "Short Message Service: Telecommunications protocol utilized for urgent offline emergency and pill reminder dispatches."],
    ["SOS", "Distress signal triggering immediate multi-channel incident escalation, SMS alerts, and sirens during medical crises."],
    ["SpO2", "Peripheral capillary oxygen saturation: Vital sign metric denoting the percentage of oxygenated hemoglobin in the blood."],
    ["SRS", "Software Requirements Specification: Comprehensive formal document specifying system behavior, constraints, and quality attributes."],
    ["SUS", "System Usability Scale: Standardized 10-item questionnaire used to quantify interface usability and user satisfaction."],
    ["TLS", "Transport Layer Security: Cryptographic protocol providing end-to-end communication security over computer networks."],
    ["WCAG 2.1 AA", "Web Content Accessibility Guidelines Level AA: International standard ensuring usability for elderly users and persons with disabilities."]
]

TBD_LIST = [
    ["TBD-01", "Hardware Telemetry Integration", "Direct Bluetooth Low Energy (BLE) pairing with digital sphygmomanometers and finger pulse oximeters for zero-click vitals telemetry ingestion.", "Phase 2 (Sprint 6)"],
    ["TBD-02", "WebRTC Teleconsultation", "Integration of embedded, peer-to-peer encrypted video calling directly within the Doctor Appointment module.", "Phase 2 (Sprint 7)"],
    ["TBD-03", "AI Predictive Health Scoring", "Machine learning classification model analyzing longitudinal vitals trends to predict sepsis or dehydration risk 24 hours prior to acute onset.", "Phase 3 (Sprint 9)"],
    ["TBD-04", "National EHR Interoperability", "HL7 FHIR API export adapters for interoperability with Bangladesh DGHS (Directorate General of Health Services) hospital databases.", "Phase 3 (Sprint 10)"],
    ["TBD-05", "Wearable GPS Geofencing", "Integration with GPS wearable smart bands to trigger automatic perimeter-breach SOS alerts for residents with advanced dementia.", "Phase 3 (Sprint 11)"]
]

USE_CASES = [
    {
        "id": "UC-01",
        "num": "5.1",
        "title": "Use Case UC-01: User Authentication & Role-Based Access Control (RBAC)",
        "brief_description": "Enables registered system actors (Administrators, Guardians, Caregivers, Doctors, and Seniors) to securely authenticate using their verified credentials. The system validates the session and grants access strictly to authorized role-specific dashboards.",
        "business_trigger": "A user accesses the ECMS login portal or attempts to request an internal protected route.",
        "preconditions": "The user must possess an active, non-suspended account in the system database with configured role permissions.",
        "assumptions": "The client browser supports modern cookies, JavaScript, and TLS 1.3 encryption.",
        "basic_flow": [
            ("1", "The user navigates to the ECMS secure login portal and enters their registered email address and password.",
             "The system validates client-side input formatting and renders an active login submission state."),
            ("2", "The user clicks the 'Secure Login' button to transmit credentials.",
             "The system computes the Bcrypt verification hash against the stored credentials in the users database table."),
            ("3", "The system verifies matching credentials and retrieves the actor's role attribute (Admin, Guardian, Caregiver, Doctor, Senior).",
             "The system generates a cryptographically secure 256-bit session token, sets an HTTP-only secure cookie, and initializes the role permission matrix."),
            ("4", "The system audits the successful login event with client IP and timestamp.",
             "The system redirects the authenticated actor directly to their designated role dashboard.")
        ],
        "post_condition": "The user is authenticated, an active encrypted session is maintained, and role-appropriate navigational menus are loaded.",
        "alternate_flows": [
            {
                "name": "AF1: Invalid Credentials Entered",
                "condition": "If at line 2 in Basic Flow the email does not exist or the password hash fails verification, then:",
                "steps": [
                    ("1", "The user submits unverified or mismatched credentials.",
                     "The system increments the failed login attempt counter for the given username and IP address."),
                    ("2", "The user observes an error notification: 'Invalid email or password combination. Please try again.'",
                     "The system resets the password field while preserving the email field, logging the security event.")
                ],
                "restart": "The use case restarts at line 1 in Basic Flow.",
                "post_condition": "No session is created, the system remains locked, and the failed attempt is recorded."
            },
            {
                "name": "AF2: Account Lockout after Excessive Failures",
                "condition": "If at line 2 in Basic Flow the failed login counter reaches five (5) consecutive unsuccessful attempts within 15 minutes, then:",
                "steps": [
                    ("1", "The user submits a fifth consecutive erroneous credential pair.",
                     "The system flags the account as temporarily locked for a 15-minute cooldown period."),
                    ("2", "The user receives a high-priority warning modal: 'Account locked due to multiple failed login attempts. Try again in 15 minutes or contact Administrator.'",
                     "The system dispatches an automated security notification email to the account's registered address and disables login form submissions.")
                ],
                "restart": "The use case terminates.",
                "post_condition": "Account login is temporarily disabled, and an administrative security incident is logged."
            }
        ],
        "sub_flows": [
            {
                "name": "SF1: Two-Factor Authentication (2FA) Verification",
                "steps": [
                    ("1", "For Administrator and Doctor roles, the system generates a 6-digit one-time verification passcode (OTP) and sends it via SMS/email.",
                     "The system displays a modal requesting the time-sensitive 6-digit OTP code."),
                    ("2", "The actor inputs the 6-digit OTP code and clicks 'Verify Passcode'.",
                     "The system validates the token against the active session hash within the 5-minute validity window.")
                ],
                "return_statement": "Return to Basic Flow line 3."
            }
        ],
        "business_rules": [
            "BR-01: Passwords must contain a minimum of 8 characters, including at least one uppercase letter, one digit, and one special character.",
            "BR-02: Passwords must be hashed using Bcrypt with a minimum cost factor of 12 prior to database persistence.",
            "BR-03: Inactive authenticated sessions must automatically terminate after 15 minutes of user inactivity.",
            "BR-04: Role escalation is strictly prohibited; users can only access endpoints authorized by their primary role."
        ],
        "nfr": [
            "NFR-01: Credential verification and dashboard redirection must complete within 800 milliseconds under standard network conditions.",
            "NFR-02: Authentication endpoints must be protected against brute-force attacks via IP-based rate limiting (maximum 10 requests per minute)."
        ],
        "data_requirements": [
            "DR-01: User email string (RFC 5322 compliant, max 100 characters).",
            "DR-02: User password string (UTF-8, minimum 8 characters, max 72 characters for Bcrypt hashing).",
            "DR-03: Session token (256-bit cryptographically secure pseudorandom string stored in HTTP-only, SameSite=Strict cookie)."
        ],
        "exceptions": [
            ["Email Address", "Must be a valid RFC 5322 email format", "Message: 'Invalid email format – please enter a valid address'"],
            ["Password", "Length must be between 8 and 72 characters", "Message: 'Password must be at least 8 characters with 1 digit and 1 special symbol'"],
            ["Account Status", "Account must be in 'Active' state", "Message: 'Account is deactivated – please contact system administrator'"]
        ]
    },
    {
        "id": "UC-02",
        "num": "5.2",
        "title": "Use Case UC-02: Senior Resident Profile & Health Record Setup",
        "brief_description": "Allows Family Guardians or System Administrators to register a new elderly resident into the ECMS repository, documenting demographic details, baseline vital norms, chronic diagnoses, dietary restrictions, mobility status, and emergency contacts.",
        "business_trigger": "A family guardian registers an elderly relative for home or institutional geriatric care coordination.",
        "preconditions": "The actor is logged in with an active Guardian or Administrator role.",
        "assumptions": "The guardian has accurate clinical history, National ID/birth registration, and attending physician details available.",
        "basic_flow": [
            ("1", "The guardian clicks 'Add New Senior Resident' on the Guardian Management portal.",
             "The system renders the multi-step resident onboarding form with demographic, clinical, and emergency contact tabs."),
            ("2", "The guardian enters full legal name, date of birth, blood group, gender, emergency contact phone, and residential room/bed assignment.",
             "The system performs real-time field validation, verifying date formatting and phone number syntax."),
            ("3", "The guardian enters known chronic conditions (e.g., Hypertension, Type-2 Diabetes, Dementia) and drug allergies.",
             "The system checks the entered allergies against the national drug formulary allergy registry."),
            ("4", "The guardian submits the completed resident profile.",
             "The system assigns a unique Medical Record Number (MRN), stores the record in the seniors table, and triggers an onboarding confirmation.")
        ],
        "post_condition": "A new senior resident profile is persisted in the database, linked to the guardian, and accessible by assigned caregivers.",
        "alternate_flows": [
            {
                "name": "AF1: Duplicate Senior Registration Detected",
                "condition": "If at line 2 in Basic Flow the senior's National ID or full name and birth date match an existing active resident, then:",
                "steps": [
                    ("1", "The guardian inputs details of an already registered individual.",
                     "The system queries the seniors table and detects an identical NID/name conflict."),
                    ("2", "The system displays an alert modal: 'A senior resident with this National ID already exists in the system.'",
                     "The system prompts the user to link their guardian account to the existing profile or contact support.")
                ],
                "restart": "The use case terminates or redirects to Guardian Linkage Request.",
                "post_condition": "Duplicate resident records are prevented, ensuring database entity uniqueness."
            }
        ],
        "sub_flows": [
            {
                "name": "SF1: Emergency Contact Verification",
                "steps": [
                    ("1", "The guardian enters primary and secondary emergency contact phone numbers.",
                     "The system sends an automated SMS confirmation token to verify primary emergency contact reachability."),
                    ("2", "The guardian confirms the received token on the interface.",
                     "The system marks the emergency contact as 'Verified'.")
                ],
                "return_statement": "Return to Basic Flow line 4."
            }
        ],
        "business_rules": [
            "BR-05: Every senior resident must have at least one verified primary emergency contact number.",
            "BR-06: Senior age must be at least 60 years old at the time of registration, or marked with a special geriatric dispensation flag.",
            "BR-07: Drug allergy tags are mandatory; if no allergies exist, the actor must explicitly check 'No Known Drug Allergies (NKDA)'."
        ],
        "nfr": [
            "NFR-03: Resident registration and MRN assignment must complete within 1.0 second.",
            "NFR-04: Senior health records must be encrypted at rest using AES-256."
        ],
        "data_requirements": [
            "DR-04: Senior Full Legal Name (1-100 characters).",
            "DR-05: Date of Birth (YYYY-MM-DD, age >= 60).",
            "DR-06: Blood Group (Enum: A+, A-, B+, B-, AB+, AB-, O+, O-).",
            "DR-07: Emergency Contact Phone (E.164 international format, e.g., +88017XXXXXXXX)."
        ],
        "exceptions": [
            ["Senior Full Name", "Max 100 characters, alphabetic characters only", "Message: 'Invalid name – letters and spaces only'"],
            ["Date of Birth", "Must represent an age of 60 or greater", "Message: 'Senior resident must be at least 60 years of age'"],
            ["Emergency Phone", "Valid Bangladeshi or international phone number", "Message: 'Invalid phone number format – please enter valid 11-digit mobile number'"]
        ]
    },
    {
        "id": "UC-03",
        "num": "5.3",
        "title": "Use Case UC-03: Medication Regimen Scheduling & Automated Pill Reminders",
        "brief_description": "Enables Consulting Physicians or Family Guardians to schedule recurring drug prescriptions, dosages, administration routes, meal associations, and daily timings. The system schedules automated audio and SMS alerts.",
        "business_trigger": "A doctor issues a new prescription or a guardian updates an ongoing chronic medication schedule.",
        "preconditions": "The senior resident profile exists and the prescribing doctor or guardian is authenticated.",
        "assumptions": "Medication names are matched against standard pharmaceutical generic nomenclatures.",
        "basic_flow": [
            ("1", "The physician selects a senior resident and navigates to the 'Medication Schedule' tab.",
             "The system displays active medications, dosage calendars, and a 'Prescribe New Medication' action."),
            ("2", "The physician enters medication name, dosage strength (e.g., 5mg, 500mg), form (Tablet, Syrup, Injection), and route.",
             "The system searches the pharmaceutical database to autocomplete generic drug names."),
            ("3", "The physician specifies frequency (Once daily, Twice daily, Every 8 hours) and meal timing (Before Meal, After Meal).",
             "The system computes daily administration schedule times (e.g., 08:00 AM, 08:00 PM)."),
            ("4", "The physician sets regimen start date, end date, and any special instructions.",
             "The system validates dosage ranges against geriatric safety thresholds and checks for drug-drug interactions."),
            ("5", "The physician clicks 'Save & Activate Regimen'.",
             "The system creates scheduled slots in the medication_schedules table and initializes automated reminder cron triggers.")
        ],
        "post_condition": "A new medication regimen is active, and daily reminder timers are queued for caregiver and senior interfaces.",
        "alternate_flows": [
            {
                "name": "AF1: Severe Drug-Drug Interaction Detected",
                "condition": "If at line 4 in Basic Flow the newly prescribed drug has a known contraindication with an existing active medication, then:",
                "steps": [
                    ("1", "The physician attempts to save a conflicting drug regimen (e.g., Warfarin + Aspirin).",
                     "The clinical interaction engine identifies a Level-1 severe bleeding hazard."),
                    ("2", "The system displays a prominent modal alert detailing the clinical interaction hazard.",
                     "The physician is required to either cancel the entry or enter a clinical justification override code.")
                ],
                "restart": "The use case restarts at line 2 in Basic Flow if canceled, or proceeds to line 5 upon authorized override.",
                "post_condition": "Contraindicated drug combinations are prevented or audited with physician rationale."
            }
        ],
        "sub_flows": [
            {
                "name": "SF1: Automated Reminder Notification Dispatch",
                "steps": [
                    ("1", "The background cron trigger detects a scheduled dosage window within 15 minutes.",
                     "The system pushes a visual pill card notification to the caregiver's dashboard and plays a gentle audio chime on the senior's tablet."),
                    ("2", "If unacknowledged within 10 minutes past the due time, the system dispatches an SMS reminder.",
                     "The system logs the reminder dispatch event.")
                ],
                "return_statement": "Return to main scheduling flow."
            }
        ],
        "business_rules": [
            "BR-08: Only verified Physicians or authorized Guardians can create or modify medication schedules.",
            "BR-09: End dates cannot precede start dates; ongoing chronic medications must be flagged with 'Indefinite' status.",
            "BR-10: Medication reminder notifications must fire exactly 15 minutes before and at the exact scheduled dosage timestamp."
        ],
        "nfr": [
            "NFR-05: Drug interaction checks must evaluate against the local clinical database within 300 milliseconds.",
            "NFR-06: Scheduled reminder notifications must dispatch with 99.9% on-time accuracy."
        ],
        "data_requirements": [
            "DR-08: Medication Name (String, max 100 chars).",
            "DR-09: Dosage Amount and Unit (e.g., '500 mg', '10 ml', '1 drop').",
            "DR-10: Administration Times (Array of HH:MM strings).",
            "DR-11: Meal Association (Enum: 'Before Meal', 'After Meal', 'With Food', 'Empty Stomach')."
        ],
        "exceptions": [
            ["Medication Name", "Mandatory text field, max 100 characters", "Message: 'Medication name cannot be empty'"],
            ["Dosage Strength", "Positive numeric value with valid unit", "Message: 'Please enter a valid numeric dosage and unit'"],
            ["Start Date", "Must be equal to or greater than today's date", "Message: 'Start date cannot be in the past'"]
        ]
    },
    {
        "id": "UC-04",
        "num": "5.4",
        "title": "Use Case UC-04: Daily Caregiving & Medication Administration Logging",
        "brief_description": "Enables the assigned Duty Caregiver or Nurse to record real-time medication intake status (Given, Missed, Refused) for scheduled doses, recording time of administration, caregiver PIN, and clinical observations.",
        "business_trigger": "The scheduled medication administration time arrives, or a caregiver physically administers medication to a senior resident.",
        "preconditions": "The caregiver is authenticated, and a scheduled medication slot exists for the senior resident.",
        "assumptions": "The caregiver is physically co-located with the resident or confirming home care administration.",
        "basic_flow": [
            ("1", "The caregiver opens the 'Daily MAR (Medication Administration Record)' dashboard.",
             "The system displays a chronologically sorted list of pending, due, and completed medications for the resident."),
            ("2", "The caregiver locates the due dose and clicks the 'Administer' button.",
             "The system displays the medication confirmation modal with resident photo, drug name, dosage, and meal instructions."),
            ("3", "The caregiver physically administers the dose and selects the status 'Given'.",
             "The system captures current timestamp and auto-populates administering caregiver credentials."),
            ("4", "The caregiver enters optional observation notes and enters their 4-digit verification PIN.",
             "The system validates the caregiver PIN, stores the log in medication_logs, updates schedule state to 'Administered', and sends a real-time sync event to the Guardian portal.")
        ],
        "post_condition": "The dose is permanently marked as 'Given' with full timestamped auditability.",
        "alternate_flows": [
            {
                "name": "AF1: Resident Refuses Medication",
                "condition": "If at line 3 in Basic Flow the senior resident refuses to take the prescribed medication, then:",
                "steps": [
                    ("1", "The caregiver selects status 'Refused' on the confirmation modal.",
                     "The system mandates entry of a clinical refusal reason (e.g., Nausea, Agitation, Discomfort)."),
                    ("2", "The caregiver inputs the refusal explanation and submits.",
                     "The system records the omission, flags the dose in amber/red on the dashboard, and queues an instant alert to the Guardian and Doctor.")
                ],
                "restart": "The use case terminates.",
                "post_condition": "Dose is recorded as 'Refused', preventing duplicate administration while notifying supervisors."
            },
            {
                "name": "AF2: Dose Missed Due to Resident Sleep or Absence",
                "condition": "If at line 3 in Basic Flow the dose is not administered within 60 minutes of scheduled time, then:",
                "steps": [
                    ("1", "The system's automated adherence cron detects an overdue slot.",
                     "The system marks the slot as 'Missed'."),
                    ("2", "The system displays an overdue warning to the duty caregiver.",
                     "The caregiver is prompted to either log late administration with justification or confirm omission.")
                ],
                "restart": "The use case restarts at line 2 in Basic Flow if late administration is approved.",
                "post_condition": "The adherence record reflects accurate clinical reality."
            }
        ],
        "sub_flows": [
            {
                "name": "SF1: Guardian Immediate Notification Dispatch",
                "steps": [
                    ("1", "The system triggers a background web-hook upon status change to 'Refused' or 'Missed'.",
                     "The notification service sends an SMS alert to the registered Guardian phone number."),
                    ("2", "The system writes the dispatch status to the notification_logs table.",
                     "The alert is displayed on the Guardian's live feed.")
                ],
                "return_statement": "Return to Basic Flow line 4."
            }
        ],
        "business_rules": [
            "BR-11: A medication record entry cannot be deleted or retroactively altered once submitted; corrections require a supplementary addendum note.",
            "BR-12: If status is 'Refused' or 'Missed', the reason field is mandatory and must contain at least 10 characters.",
            "BR-13: Caregiver PIN is mandatory for non-repudiation of medication administration."
        ],
        "nfr": [
            "NFR-07: Dose logging submission must be committed to the database within 400 milliseconds.",
            "NFR-08: The MAR interface must render on mobile tablets without horizontal scrolling."
        ],
        "data_requirements": [
            "DR-12: Administration Status (Enum: 'Given', 'Missed', 'Refused').",
            "DR-13: Actual Administration Timestamp (Datetime YYYY-MM-DD HH:MM:SS).",
            "DR-14: Caregiver Verification PIN (4-digit numeric string).",
            "DR-15: Clinical Observation Notes (Text, max 500 characters)."
        ],
        "exceptions": [
            ["Status Reason", "Mandatory if status is not 'Given', min 10 chars", "Message: 'Please provide a clinical explanation for missed or refused medication'"],
            ["Caregiver PIN", "Must match the 4-digit PIN of the logged-in caregiver", "Message: 'Incorrect verification PIN – entry rejected'"],
            ["Timestamp", "Cannot be set in the future", "Message: 'Administration timestamp cannot exceed current system time'"]
        ]
    },
    {
        "id": "UC-05",
        "num": "5.5",
        "title": "Use Case UC-05: Real-Time Vitals Tracking & Physiological Anomaly Alerting",
        "brief_description": "Enables Caregivers to log physiological vital signs (Blood Pressure, Heart Rate, SpO2, Temperature, Blood Glucose) and allows the system to automatically detect critical abnormal thresholds and trigger escalation sirens.",
        "business_trigger": "A caregiver conducts a scheduled morning/evening vitals check, or a resident reports acute physical discomfort.",
        "preconditions": "The caregiver is authenticated, and baseline physiological thresholds are defined for the resident.",
        "assumptions": "Vitals are measured using calibrated clinical diagnostic instruments (e.g., digital cuff, pulse oximeter).",
        "basic_flow": [
            ("1", "The caregiver selects the senior resident and clicks 'Record New Vitals'.",
             "The system renders the vitals entry form with fields for Systolic/Diastolic BP, Heart Rate, SpO2, Temperature, and Blood Glucose."),
            ("2", "The caregiver inputs measured values (e.g., BP: 120/80 mmHg, Pulse: 72 bpm, SpO2: 98%, Temp: 98.6°F).",
             "The system performs real-time client-side range validation and displays immediate color-coded indicator badges (Green: Normal)."),
            ("3", "The caregiver adds contextual observations (e.g., 'Resident resting comfortably after breakfast').",
             "The system computes the composite Early Warning Score (EWS) for the resident."),
            ("4", "The caregiver clicks 'Save Vitals Record'.",
             "The system stores values in the vitals table, updates longitudinal trend graphs, and displays a success notification.")
        ],
        "post_condition": "Vitals are recorded, trend charts are updated, and health status remains in 'Stable' condition.",
        "alternate_flows": [
            {
                "name": "AF1: Critical Vital Anomaly Detected (Hypertensive Crisis / Hypoxia)",
                "condition": "If at line 2 in Basic Flow any vital sign exceeds defined critical thresholds (e.g., Systolic BP > 180, SpO2 < 90%, Pulse > 120 bpm), then:",
                "steps": [
                    ("1", "The caregiver enters an abnormal reading (e.g., SpO2 = 87%, BP = 190/110 mmHg).",
                     "The system immediately flashes a high-contrast Red Alert banner on the screen and sounds an emergency audio alert chime."),
                    ("2", "The system prompts the caregiver to immediately re-verify the reading and confirm patient positioning.",
                     "The system dispatches an automated high-priority SMS alert to the attending Physician and Family Guardian with exact readings."),
                    ("3", "The caregiver confirms the reading and selects 'Dispatch Emergency Response' if necessary.",
                     "The system escalates the incident to the Emergency SOS dispatch queue.")
                ],
                "restart": "The use case proceeds to line 4 with an 'Anomaly Flag' active.",
                "post_condition": "Vitals are saved with an urgent clinical escalation flag, alerting guardians and physicians."
            }
        ],
        "sub_flows": [
            {
                "name": "SF1: Longitudinal Trend Analysis Rendering",
                "steps": [
                    ("1", "Upon saving new vitals, the system queries the previous 30 days of telemetry.",
                     "The system calculates 7-day moving averages and identifies upward or downward physiological drift."),
                    ("2", "The system updates the SVG sparkline visualization on the resident's summary card.",
                     "The caregiver views the real-time visual trajectory.")
                ],
                "return_statement": "Return to Basic Flow line 4."
            }
        ],
        "business_rules": [
            "BR-14: Standard physiological alert boundaries: Systolic BP > 140 or < 90 mmHg; SpO2 < 92%; Heart Rate > 100 or < 50 bpm; Blood Glucose > 200 or < 70 mg/dL.",
            "BR-15: Custom doctor-prescribed thresholds override default system boundaries for specific residents (e.g., COPD or chronic hypotension patients).",
            "BR-16: Critical anomaly alerts must persist on the screen until explicitly acknowledged by a licensed nurse or physician."
        ],
        "nfr": [
            "NFR-09: Anomaly detection rules must evaluate in less than 150 milliseconds upon form input.",
            "NFR-10: Critical SMS alert dispatches must be submitted to the telecommunications gateway within 5 seconds."
        ],
        "data_requirements": [
            "DR-16: Systolic BP (Integer, 50-250 mmHg).",
            "DR-17: Diastolic BP (Integer, 30-150 mmHg).",
            "DR-18: Pulse Rate (Integer, 30-220 BPM).",
            "DR-19: SpO2 Blood Oxygen (Integer, 50-100 %).",
            "DR-20: Body Temperature (Decimal, 90.0-108.0 °F)."
        ],
        "exceptions": [
            ["Systolic BP", "Numeric, between 50 and 250", "Message: 'Systolic value out of physiological range (50-250)'"],
            ["SpO2", "Numeric percentage, between 50 and 100", "Message: 'SpO2 must be between 50% and 100%'"],
            ["Temperature", "Numeric, between 90.0 and 108.0 °F", "Message: 'Temperature out of measurable range (90.0-108.0 °F)'"]
        ]
    },
    {
        "id": "UC-06",
        "num": "5.6",
        "title": "Use Case UC-06: Doctor Appointment Scheduling & Clinical Teleconsultation Booking",
        "brief_description": "Allows Family Guardians or Caregivers to book, reschedule, or cancel clinical medical appointments and teleconsultations with specialized geriatric physicians, managing schedule conflicts and clinical reminders.",
        "business_trigger": "A senior resident requires a routine health checkup, specialist review, or follow-up teleconsultation.",
        "preconditions": "The user is authenticated, the resident profile is active, and attending doctors have active availability slots.",
        "assumptions": "Doctors maintain updated digital availability schedules in the ECMS provider registry.",
        "basic_flow": [
            ("1", "The guardian clicks 'Book Medical Appointment' on the resident care portal.",
             "The system displays a directory of registered doctors, specializations (Cardiology, Geriatrics, Neurology), and clinic venues."),
            ("2", "The guardian selects a doctor, chooses consultation mode (In-Person Clinic or Teleconsultation), and picks a calendar date.",
             "The system queries the appointments table and renders real-time available 30-minute time slots."),
            ("3", "The guardian selects an open time slot and enters the chief clinical complaint / reason for visit.",
             "The system locks the selected slot for 10 minutes to prevent double-booking conflicts."),
            ("4", "The guardian confirms the appointment booking.",
             "The system creates the record with status 'Confirmed', generates an iCalendar invite, and dispatches SMS confirmations to the doctor and guardian.")
        ],
        "post_condition": "The medical appointment is confirmed, calendar slots are reserved, and reminders are queued.",
        "alternate_flows": [
            {
                "name": "AF1: Schedule Conflict / Slot Already Reserved",
                "condition": "If at line 3 in Basic Flow another user confirms the same time slot simultaneously, then:",
                "steps": [
                    ("1", "The guardian attempts to confirm a slot that was just reserved.",
                     "The system detects a concurrency lock conflict on the appointment slot."),
                    ("2", "The system displays an alert: 'The selected appointment slot has just been booked. Please choose another available time.'",
                     "The system refreshes the available slots view with current real-time data.")
                ],
                "restart": "The use case restarts at line 2 in Basic Flow.",
                "post_condition": "Double-booking is prevented."
            },
            {
                "name": "AF2: Appointment Cancellation / Rescheduling",
                "condition": "If a guardian cancels or reschedules an existing appointment at least 24 hours prior to the slot, then:",
                "steps": [
                    ("1", "The guardian navigates to active appointments and clicks 'Cancel / Reschedule Appointment'.",
                     "The system prompts for cancellation reason and confirms user intent."),
                    ("2", "The guardian inputs the reason and confirms cancellation.",
                     "The system releases the time slot back to public availability, sets appointment status to 'Cancelled', and notifies the physician via SMS/email.")
                ],
                "restart": "The use case terminates.",
                "post_condition": "The slot is freed, and status is updated with cancellation audit logs."
            }
        ],
        "sub_flows": [
            {
                "name": "SF1: Automated 24-Hour Clinical Reminder",
                "steps": [
                    ("1", "The background cron worker scans for appointments occurring within 24 hours.",
                     "The system compiles appointment details, doctor name, and clinic address / teleconsultation URL."),
                    ("2", "The system dispatches SMS reminders to the guardian and resident.",
                     "The notification timestamp is updated.")
                ],
                "return_statement": "Return to main scheduling flow."
            }
        ],
        "business_rules": [
            "BR-17: In-person and teleconsultation appointment slots must be configured in 30-minute discrete intervals.",
            "BR-18: Cancellations within 2 hours of scheduled time require administrative override or incur a standard late cancellation flag.",
            "BR-19: A resident cannot have two overlapping appointments scheduled on the same date and time."
        ],
        "nfr": [
            "NFR-11: Available slot queries across 30 days of physician schedules must render in under 500 milliseconds.",
            "NFR-12: The scheduling system must support concurrent bookings without race conditions via database row-level locking."
        ],
        "data_requirements": [
            "DR-21: Doctor ID (Foreign key linking to doctors table).",
            "DR-22: Appointment Date & Time (YYYY-MM-DD HH:MM:SS).",
            "DR-23: Consultation Type (Enum: 'In-Person', 'Teleconsultation').",
            "DR-24: Chief Complaint / Clinical Notes (Text, max 500 characters)."
        ],
        "exceptions": [
            ["Appointment Date", "Must be a future date", "Message: 'Appointment date must be scheduled for a future day'"],
            ["Chief Complaint", "Mandatory text, min 5 chars, max 500 chars", "Message: 'Please provide a brief reason for the medical visit'"],
            ["Slot Selection", "Must select a valid available slot", "Message: 'Please select an available appointment time slot'"]
        ]
    },
    {
        "id": "UC-07",
        "num": "5.7",
        "title": "Use Case UC-07: Emergency SOS Alert Dispatch & Incident Escalation Workflow",
        "brief_description": "Enables an Elderly Senior Resident (via a single prominent screen touch or physical pendant) or Caregiver to trigger an instantaneous high-priority distress alert. The system broadcasts audio sirens, dispatches SMS notifications with GPS coordinates, and escalates to family guardians and emergency response teams.",
        "business_trigger": "A senior resident experiences an acute fall, severe chest pain, sudden breathlessness, or a caregiver encounters a medical collapse.",
        "preconditions": "The resident profile is active, and verified emergency contacts are registered.",
        "assumptions": "The senior device has network connectivity, or the gateway provides cellular SMS fallback.",
        "basic_flow": [
            ("1", "The senior resident taps the giant red 'EMERGENCY SOS' button on their visual tablet, or holds it for 2 seconds.",
             "The system displays a prominent 5-second countdown modal with a loud audible chime and 'Cancel if Accidental' option."),
            ("2", "The countdown expires without cancellation.",
             "The system initiates the High-Priority Emergency Protocol, capturing current timestamp and GPS coordinates."),
            ("3", "The system broadcasts an emergency siren audio alert to all active caregiver dashboards on the local network.",
             "The system simultaneously transmits urgent SMS distress messages to the primary Family Guardian and attending Doctor with resident name, room number, and phone link."),
            ("4", "The on-duty caregiver clicks 'Acknowledge Emergency' on their dashboard.",
             "The system changes emergency state to 'Responding', records the caregiver's identity, silences sirens, and displays emergency instructions.")
        ],
        "post_condition": "Emergency SOS is logged, responders are notified, and an active incident management record is tracked until resolved.",
        "alternate_flows": [
            {
                "name": "AF1: Accidental SOS False Alarm Canceled",
                "condition": "If at line 1 in Basic Flow the senior resident accidentally presses the SOS button and taps 'Cancel' within the 5-second window, then:",
                "steps": [
                    ("1", "The senior resident taps 'Cancel False Alarm' during the 5-second countdown.",
                     "The system halts the emergency dispatch sequence and silences the warning chime."),
                    ("2", "The system displays a reassuring confirmation: 'Emergency alert canceled. Stay safe!'",
                     "The system logs the false alarm event in audit_logs for sensitivity monitoring without alerting external family contacts.")
                ],
                "restart": "The use case terminates.",
                "post_condition": "No external SMS messages are sent, and normal operation resumes."
            },
            {
                "name": "AF2: Unacknowledged SOS Escalation to External 999 Emergency Services",
                "condition": "If at line 4 in Basic Flow no on-duty caregiver acknowledges the emergency within 180 seconds (3 minutes), then:",
                "steps": [
                    ("1", "The emergency escalation timer exceeds the 3-minute threshold without caregiver acknowledgment.",
                     "The system triggers Level-2 Maximum Escalation."),
                    ("2", "The system dispatches secondary SMS broadcasts to secondary family guardians and the facility chief administrator.",
                     "The system displays a prominent one-touch direct dial link to Bangladesh Emergency Services (999) and local hospital ambulances.")
                ],
                "restart": "The use case terminates upon external responder arrival.",
                "post_condition": "Incident is escalated to maximum severity, ensuring guaranteed life safety response."
            }
        ],
        "sub_flows": [
            {
                "name": "SF1: GPS Geolocation Ingestion",
                "steps": [
                    ("1", "The browser or device Geolocation API retrieves current latitude and longitude coordinates.",
                     "The system constructs an OpenStreetMap / Google Maps emergency location URL."),
                    ("2", "The location link is appended directly into the outbound emergency SMS payload.",
                     "The recipient can tap the link for turn-by-turn navigation.")
                ],
                "return_statement": "Return to Basic Flow line 3."
            }
        ],
        "business_rules": [
            "BR-20: Emergency SOS dispatches bypass all system throttling, quiet hours, and do-not-disturb filters.",
            "BR-21: The 5-second cancellation countdown is strictly limited to prevent accidental false alarms while maintaining life-critical speed.",
            "BR-22: Every SOS incident must remain in 'Active/Responding' state until a verified clinical staff member completes a formal 'Incident Resolution Report'."
        ],
        "nfr": [
            "NFR-13: The entire SOS dispatch sequence (database creation, audio siren trigger, SMS transmission) must complete in under 3.0 seconds.",
            "NFR-14: Emergency sirens must emit at maximum system audio volume (utilizing Web Audio API at 85+ dB output)."
        ],
        "data_requirements": [
            "DR-25: Emergency Alert ID (Auto-increment primary key).",
            "DR-26: Trigger Source (Enum: 'Senior One-Touch', 'Caregiver Manual', 'Vitals Anomaly Auto-Trigger').",
            "DR-27: Incident Status (Enum: 'Triggered', 'Responding', 'Resolved', 'False Alarm').",
            "DR-28: GPS Coordinates (Latitude and Longitude decimal strings)."
        ],
        "exceptions": [
            ["Network Outage", "System loses internet connection during SOS trigger", "Message: 'Network disconnected – attempting local cellular SMS dispatch and sounding local siren'"],
            ["GPS Unavailable", "Device location permissions denied", "Message: 'GPS coordinates unavailable – defaulting to registered resident room/bed address'"],
            ["Resolution Notes", "Mandatory min 20 chars to close incident", "Message: 'Incident resolution requires detailed clinical documentation'"]
        ]
    },
    {
        "id": "UC-08",
        "num": "5.8",
        "title": "Use Case UC-08: Caregiver Shift Handoff & Clinical Progress Notes",
        "brief_description": "Enables the outgoing duty caregiver to document structured clinical progress notes, summarized care activities, upcoming medication requirements, and special resident behavioral observations for the incoming shift caregiver, ensuring seamless continuity of care.",
        "business_trigger": "A caregiver's scheduled duty shift ends (e.g., Morning to Evening shift handoff at 02:00 PM or 10:00 PM).",
        "preconditions": "The outgoing caregiver is authenticated and has active care assignments during the shift window.",
        "assumptions": "The incoming shift caregiver is available to review and co-sign the digital handoff summary.",
        "basic_flow": [
            ("1", "The outgoing caregiver clicks 'Complete Shift Handoff' on the clinical portal.",
             "The system automatically aggregates care events completed during the shift: medications given, vitals checked, ADL logs, and any reported anomalies."),
            ("2", "The outgoing caregiver reviews the automated summary and enters narrative clinical progress notes (e.g., resident mood, dietary intake, mobility changes).",
             "The system verifies note completeness and checks for pending unresolved tasks."),
            ("3", "The outgoing caregiver tags any high-priority follow-up items for the next shift (e.g., 'Monitor fluid intake; Dr. Rahman visiting at 04:00 PM').",
             "The system formats the handoff report and prompts for outgoing caregiver signature / PIN."),
            ("4", "The outgoing caregiver enters their PIN and submits the handoff report.",
             "The system stores the report in the shift_notes table, transitions shift status, and flags the handoff summary as 'Pending Acknowledgment' for incoming staff.")
        ],
        "post_condition": "A structured, permanent shift handoff record is logged, providing complete clinical continuity and legal accountability.",
        "alternate_flows": [
            {
                "name": "AF1: Pending Overdue Care Tasks Detected at Shift End",
                "condition": "If at line 1 in Basic Flow there are unadministered scheduled medications or unrecorded vital checks within the shift period, then:",
                "steps": [
                    ("1", "The system identifies open incomplete tasks assigned to the shift.",
                     "The system displays a warning banner listing the uncompleted tasks."),
                    ("2", "The caregiver is required to either complete the task immediately or provide an explicit handover delegation reason.",
                     "The caregiver documents the delegation rationale and continues.")
                ],
                "restart": "The use case proceeds to line 2 in Basic Flow.",
                "post_condition": "Care omissions are prevented from slipping through shift transitions."
            }
        ],
        "sub_flows": [
            {
                "name": "SF1: Incoming Caregiver Digital Co-Signature",
                "steps": [
                    ("1", "The incoming caregiver logs into their shift dashboard.",
                     "The system displays the mandatory 'Shift Handover Acknowledgment' modal detailing the outgoing report."),
                    ("2", "The incoming caregiver reads the summary and enters their PIN to accept care responsibility.",
                     "The system updates the handoff record to 'Acknowledged' with both timestamps.")
                ],
                "return_statement": "Return to main shift handoff flow."
            }
        ],
        "business_rules": [
            "BR-23: A caregiver cannot formally clock out until the shift handoff report has been submitted.",
            "BR-24: Handoff progress notes must be retained in the permanent medical audit archive for a minimum of 5 years.",
            "BR-25: High-priority follow-up tags must remain pinned to the top of the caregiver dashboard until marked as completed."
        ],
        "nfr": [
            "NFR-15: Shift summary automated compilation must execute in under 600 milliseconds.",
            "NFR-16: All handoff submissions must generate a tamper-evident cryptographic hash for clinical non-repudiation."
        ],
        "data_requirements": [
            "DR-29: Outgoing Caregiver ID and Incoming Caregiver ID.",
            "DR-30: Shift Type (Enum: 'Morning [06:00-14:00]', 'Evening [14:00-22:00]', 'Night [22:00-06:00]').",
            "DR-31: Narrative Progress Notes (Text, min 20 chars, max 2000 chars).",
            "DR-32: High-Priority Follow-up Flag (Boolean)."
        ],
        "exceptions": [
            ["Progress Notes", "Mandatory text, minimum 20 characters", "Message: 'Please enter detailed clinical progress notes (min 20 characters)'"],
            ["Caregiver PIN", "Must match authenticated caregiver PIN", "Message: 'Invalid PIN – handoff submission rejected'"],
            ["Unresolved Tasks", "Must be completed or delegated", "Message: 'Please complete or provide delegation explanation for pending tasks'"]
        ]
    }
]

print("data_srs_full.py created with all 8 detailed use cases.")
