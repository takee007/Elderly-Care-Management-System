"""
data_srs.py
Structured content for the Elderly Care Management System SRS
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
    ["S-1", "Family Guardian", "Review system scope, resident health transparency, SMS notifications, and verify that guardian oversight meets family caregiving expectations."],
    ["S-2", "Development Team", "Form an accurate architectural understanding, implementing frontend UI, backend PHP endpoints, database schemas, and business rules without ambiguity."],
    ["S-3", "QA / Testing Team", "Derive formal test suites, validation plans, boundary exception test cases, and accessibility verification against WCAG 2.1 AA standards."],
    ["S-4", "Project Manager / BA", "Estimate implementation velocity, track project milestones, allocate sprint tasks, and verify requirements traceability."],
    ["S-5", "Caregivers & Physicians", "Validate operational clinical workflows, medication administration schedules, vital sign anomaly detection, and shift handover procedures."]
]

USER_CLASSES = [
    ["U-1", "System Administrator", "Authorized technical superuser managing user account lifecycles, role permissions, system configuration, audit logs, and automated database backups."],
    ["U-2", "Family Guardian", "Registered family sponsor managing elderly resident registration, updating emergency contacts, viewing real-time health telemetry, and paying invoices."],
    ["U-3", "Professional Caregiver / Nurse", "Authenticated clinical staff member performing daily vitals telemetry logging, medication administration confirmation, and shift handover progress notes."],
    ["U-4", "Consulting Physician / Doctor", "Licensed healthcare provider reviewing senior medical records, prescribing medication regimens, setting vitals threshold alerts, and scheduling teleconsultations."],
    ["U-5", "Elderly Senior Resident", "Primary care recipient utilizing a simplified, high-contrast, large-button interface to view daily schedules, acknowledge pill reminders, and trigger emergency SOS alerts."]
]

GLOSSARY = [
    ["ADL", "Activities of Daily Living: Basic daily self-care tasks (eating, bathing, mobility, medication intake) tracked in geriatric care."],
    ["API", "Application Programming Interface: A formal set of HTTP REST endpoints allowing data interchange between frontend and backend."],
    ["Bcrypt", "A password-hashing function based on the Blowfish cipher, incorporating salting and computational cost factors to prevent brute-force attacks."],
    ["BPM", "Beats Per Minute: Clinical metric denoting heart rate in vitals monitoring."],
    ["CSRF", "Cross-Site Request Forgery: A web security vulnerability mitigated in ECMS via cryptographically secure session-bound tokens."],
    ["DFD", "Data Flow Diagram: A graphical representation of the flow of data through the information system."],
    ["EHR", "Electronic Health Record: Digital medical history of a resident including diagnoses, allergies, and clinical progress notes."],
    ["ERD", "Entity-Relationship Diagram: A visual database modeling artifact detailing tables, columns, foreign keys, and cardinalities."],
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

print("data_srs.py base structures defined.")
