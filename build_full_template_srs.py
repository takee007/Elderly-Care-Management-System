"""
build_full_template_srs.py
Generates the complete Elderly Care Management System SRS strictly matching SRS_Template.docx.pdf
(IEEE Std 830 industry specification standard).
Produces:
1. Elderly_Care_Management_System_SRS_IEEE_Template.md
2. Elderly_Care_Management_System_SRS_IEEE_Template.html
3. Elderly_Care_Management_System_SRS_IEEE_Template.pdf
4. Elderly_Care_Management_System_SRS_IEEE_Template.docx
"""

import os
import sys
import subprocess
import base64
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

from data_srs_full import (
    METADATA, REVISION_HISTORY, INTENDED_AUDIENCE, USER_CLASSES,
    GLOSSARY, TBD_LIST, USE_CASES
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""

# -------------------------------------------------------------
# 1. GENERATE MARKDOWN DOCUMENT (.md)
# -------------------------------------------------------------
def generate_markdown(md_path):
    lines = []
    
    # Title / Metadata
    lines.append(f"# {METADATA['project_title']}")
    lines.append(f"## {METADATA['doc_title']}")
    lines.append(f"**Version:** {METADATA['version']}  ")
    lines.append(f"**Status:** {METADATA['status']}  ")
    lines.append(f"**Prepared by:** {METADATA['author_name']} ({METADATA['author_role']}, Student ID: {METADATA['student_id']})  ")
    lines.append(f"**Course:** {METADATA['course']}  ")
    lines.append(f"**Supervised by:** {METADATA['instructor']}  ")
    lines.append(f"**Organization:** {METADATA['organization']}  ")
    lines.append(f"**Date:** {METADATA['date']}  \n")
    lines.append("---\n")
    
    # Table of Contents
    lines.append("## Table of Contents\n")
    toc_items = [
        "1. Introduction",
        "   1.1 Purpose",
        "   1.2 Document Conventions",
        "   1.3 Intended Audience and Reading Suggestions",
        "   1.4 Product Scope",
        "   1.5 References",
        "2. Overall Description",
        "   2.1 Product Perspective",
        "   2.2 Product Functions",
        "   2.3 User Classes and Characteristics",
        "   2.4 Operating Environment",
        "   2.5 Design and Implementation Constraints",
        "   2.6 User Documentation",
        "   2.7 Assumptions and Dependencies",
        "3. External Interface Requirements",
        "   3.1 User Interfaces",
        "   3.2 Hardware Interfaces",
        "   3.3 Software Interfaces",
        "   3.4 Communications Interfaces",
        "4. Domain Model",
        "5. System Features (Use Cases)",
        "   5.1 Use Case UC-01: User Authentication & Role-Based Access Control",
        "   5.2 Use Case UC-02: Senior Resident Profile & Health Record Setup",
        "   5.3 Use Case UC-03: Medication Regimen Scheduling & Automated Pill Reminders",
        "   5.4 Use Case UC-04: Daily Caregiving & Medication Administration Logging",
        "   5.5 Use Case UC-05: Real-Time Vitals Tracking & Physiological Anomaly Alerting",
        "   5.6 Use Case UC-06: Doctor Appointment Scheduling & Clinical Teleconsultation Booking",
        "   5.7 Use Case UC-07: Emergency SOS Alert Dispatch & Incident Escalation Workflow",
        "   5.8 Use Case UC-08: Caregiver Shift Handoff & Clinical Progress Notes",
        "6. Other Nonfunctional Requirements",
        "   6.1 Performance Requirements",
        "   6.2 Safety Requirements",
        "   6.3 Security Requirements",
        "   6.4 Software Quality Attributes",
        "7. Other Requirements",
        "   7.1 Database Requirements",
        "   7.2 Internationalization & Localization Requirements",
        "   7.3 Legal, Regulatory & Data Privacy Requirements",
        "   7.4 Software Reuse & Architectural Extensibility",
        "Appendix A: Glossary",
        "Appendix B: Analysis Models",
        "Appendix C: Interface Examples",
        "Appendix D: To Be Determined (TBD) List"
    ]
    for item in toc_items:
        lines.append(f"- {item}")
    lines.append("\n---\n")
    
    # Revision History
    lines.append("## Revision History\n")
    lines.append("| Name | Date | Reason For Changes | Version | Date of Approval |")
    lines.append("| :--- | :--- | :--- | :--- | :--- |")
    for row in REVISION_HISTORY:
        lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} |")
    lines.append("\n---\n")
    
    # Section 1: Introduction
    lines.append("## 1. Introduction\n")
    lines.append("### 1.1 Purpose")
    lines.append("This Software Requirements Specification (SRS) document defines the complete functional and non-functional requirements for Version 1.0 (Final Release) of the **Elderly Care Management System (ECMS)**. This specification establishes a binding contract between project stakeholders—including institutional geriatric administrators, family guardians, caregiving personnel, clinical physicians, and software engineering teams. The scope of this document encompasses all core subsystems: User Authentication & Role-Based Access Control (RBAC), Senior Resident Health Profile Management, Medication Regimen Scheduling & Adherence Tracking, Real-Time Vitals Telemetry & Physiological Anomaly Detection, Doctor Appointment Coordination, Multi-Channel Emergency SOS Alert Escalation, and Caregiver Shift Handoff Documentation.\n")
    
    lines.append("### 1.2 Document Conventions")
    lines.append("This document strictly adheres to the **IEEE Std 830-1998 Recommended Practice for Software Requirements Specifications**. In accordance with academic and institutional submission guidelines:")
    lines.append("- **Typography & Aesthetics:** Formatted in strict **Black & White** typography to maximize legibility and ensure professional publication standards without distracting decorative borders or excessive coloration.")
    lines.append("- **Requirement Identification:** Requirements are uniquely tagged using standardized alphanumeric prefixes (e.g., `UC-XX` for Use Cases, `BR-XX` for Business Rules, `NFR-XX` for Non-Functional Requirements, and `DR-XX` for Data Requirements).")
    lines.append("- **Priority Classifications:** System features are classified according to MoSCoW prioritization (Must Have, Should Have, Could Have, and Won't Have for this release).\n")
    
    lines.append("### 1.3 Intended Audience and Reading Suggestions")
    lines.append("This document addresses five primary stakeholder categories, each requiring specific perspectives when reviewing the specification:\n")
    lines.append("| ID | Stakeholder | Description |")
    lines.append("| :--- | :--- | :--- |")
    for row in INTENDED_AUDIENCE:
        lines.append(f"| {row[0]} | {row[1]} | {row[2]} |")
    lines.append("\n**Suggested Reading Sequence:**")
    lines.append("1. **Executive Stakeholders & Guardians:** Review Section 1 (Introduction), Section 2 (Overall Description), and Appendix C (Interface Examples).")
    lines.append("2. **Engineering & Development Team:** Proceed systematically through Section 2 (System Architecture), Section 3 (External Interfaces), Section 4 (Domain Model), Section 5 (Detailed Use Cases), and Appendix B (Analysis Models).")
    lines.append("3. **QA & Validation Engineers:** Focus intensely on Section 5 (Use Case basic/alternate flows and Screen Entry Exception Tables) and Section 6 (Non-Functional Requirements).\n")
    
    lines.append("### 1.4 Product Scope")
    lines.append("The Elderly Care Management System (ECMS) is a dedicated healthcare coordination web application engineered to address the critical challenges of geriatric care: uncoordinated paper logs, dangerous medication omissions, delayed emergency responses, and lack of family oversight. ECMS unifies daily caregiving into a centralized, transparent digital ecosystem. Key objectives include:")
    lines.append("- Eliminating medication administration errors through scheduled dose reminders and mandatory caregiver verification.")
    lines.append("- Providing instant multi-channel emergency SOS alerting with audible sirens, SMS broadcasts, and GPS positioning.")
    lines.append("- Enabling real-time physiological telemetry monitoring with automatic anomaly detection for hypertensive crisis or hypoxia.")
    lines.append("- Establishing comprehensive clinical continuity across nursing shifts via structured electronic progress notes.")
    lines.append("- Delivering an accessible, high-contrast user interface tailored specifically to the visual and motor capabilities of elderly seniors (WCAG 2.1 AA compliant).\n")
    
    lines.append("### 1.5 References")
    lines.append("1. IEEE Computer Society, *IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications*, IEEE, New York, 1998.")
    lines.append("2. World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.1*, W3C Recommendation, 2018.")
    lines.append("3. World Health Organization (WHO), *Integrated Care for Older People (ICOPE): Guidance for Person-Centred Assessment and Pathways in Primary Care*, WHO, Geneva, 2019.")
    lines.append("4. Health Level Seven International, *HL7 FHIR Release 4.0.1: Fast Healthcare Interoperability Resources*, HL7, 2019.")
    lines.append("5. PHP Group, *PHP 8.2 Documentation & Secure PDO Guidelines*, 2024.")
    lines.append("6. Twilio Inc., *Twilio REST API Documentation for Programmable SMS & Voice*, 2024.\n")
    lines.append("---\n")
    
    # Section 2: Overall Description
    lines.append("## 2. Overall Description\n")
    lines.append("### 2.1 Product Perspective")
    lines.append("The Elderly Care Management System (ECMS) is a newly designed, self-contained web platform developed as an integrated solution for institutional care homes and assisted home care environments. It replaces fragmented, error-prone manual paper charts, unencrypted messaging groups, and uncoordinated telephone calls. ECMS operates as a centralized web application built on the LAMP (Linux, Apache, MySQL, PHP) architecture, integrating with external telecommunication SMS gateways, browser Web Audio APIs, and geolocation mapping services.\n")
    lines.append("The system is architected into three distinct functional tiers:")
    lines.append("1. **Presentation Tier:** Responsive HTML5/CSS3/JavaScript frontend tailored with accessible WCAG 2.1 AA standards, large touch controls, and high-contrast visuals.")
    lines.append("2. **Application Logic Tier:** Modular PHP backend implementing MVC patterns, authentication middleware, business rule validators, and REST API controllers.")
    lines.append("3. **Persistence Tier:** Relational MySQL 8.0 database engine operating in 3rd Normal Form (3NF) with InnoDB ACID transactions, foreign key constraints, and encrypted medical records.\n")
    
    lines.append("### 2.2 Product Functions")
    lines.append("The major functional capabilities provided by the Elderly Care Management System comprise:")
    lines.append("- **Resident Profile & Clinical History:** Centralized management of senior demographics, blood groups, chronic ailments, drug allergies, and primary emergency contacts.")
    lines.append("- **Medication Administration Record (MAR):** Prescribing, recurring daily scheduling, automated visual/audio alarms, and timestamped caregiver administration logging (Given, Missed, Refused).")
    lines.append("- **Vitals Telemetry & Anomaly Alerting:** Tracking Blood Pressure, Pulse, Blood Oxygen (SpO2), Temperature, and Blood Glucose, with automatic anomaly detection triggers.")
    lines.append("- **Doctor Appointment & Teleconsultation Scheduling:** Calendar slot reservations, concurrency lock management, and automated SMS clinical reminders.")
    lines.append("- **Emergency SOS Incident Management:** One-touch distress trigger with a 5-second false-alarm countdown, automated multi-channel siren broadcast, SMS dispatch, and incident audit tracking.")
    lines.append("- **Caregiver Shift Handoff:** Structured electronic handoff notes compiling completed care tasks, overdue items, and clinical progress notes between duty shifts.\n")
    
    lines.append("### 2.3 User Classes and Characteristics")
    lines.append("The system supports five distinct user classes with varying privileges and operational technical proficiencies:\n")
    lines.append("| ID | User Class | Description |")
    lines.append("| :--- | :--- | :--- |")
    for row in USER_CLASSES:
        lines.append(f"| {row[0]} | {row[1]} | {row[2]} |")
    lines.append("\n### 2.4 Operating Environment")
    lines.append("ECMS is designed to operate seamlessly across the following technological environment:")
    lines.append("- **Client Hardware:** Standard desktop/laptop personal computers, tablets (Apple iPad, Samsung Galaxy Tab with minimum 1024x768 resolution), and smartphones (iOS 14+, Android 10+).")
    lines.append("- **Client Browsers:** Modern evergreen web browsers supporting HTML5, CSS Grid, ES6 JavaScript, Web Audio API, and TLS 1.3 (Google Chrome 110+, Mozilla Firefox 110+, Apple Safari 16+, Microsoft Edge 110+).")
    lines.append("- **Server Environment:** Apache HTTP Server 2.4+ / Nginx on Ubuntu Linux 22.04 LTS / Windows Server, running PHP 8.2+ with PDO, OpenSSL, and cURL extensions.")
    lines.append("- **Database Server:** MySQL Community Server 8.0+ or MariaDB 10.6+ utilizing the InnoDB storage engine with UTF-8 (`utf8mb4`) character collation.")
    lines.append("- **Network Connectivity:** Minimum 3G mobile data or broadband connection (bandwidth >= 1.0 Mbps; latency < 150ms).\n")
    
    lines.append("### 2.5 Design and Implementation Constraints")
    lines.append("1. **Accessibility Standards (WCAG 2.1 AA):** The user interface for senior residents must feature a minimum font size of 16px (18px recommended for key labels), a contrast ratio of at least 4.5:1 for normal text and 3:1 for large graphical components, and touch target sizes of at least 44x44 CSS pixels.")
    lines.append("2. **Core Technology Stack:** In strict accordance with course and architectural requirements, the core web application must be developed using native HTML5, Vanilla CSS3, JavaScript, PHP, and MySQL without proprietary framework lock-ins.")
    lines.append("3. **Security Standards:** All database interactions must use PHP Data Objects (PDO) with parameterized prepared statements to eliminate SQL injection vulnerabilities. All passwords must be salted and hashed via Bcrypt (cost factor >= 12).")
    lines.append("4. **Responsive Layouts:** Interfaces must dynamically adapt across viewport widths from 360px (mobile) to 1920px (desktop) without loss of functionality or horizontal scrollbars.\n")
    
    lines.append("### 2.6 User Documentation")
    lines.append("The project deliverables include comprehensive user documentation:")
    lines.append("- **Caregiver Quick-Start Operational Card (PDF):** A laminated 2-page pocket guide detailing vitals logging, dose administration, and shift handoff workflows.")
    lines.append("- **Senior Resident Visual Guide:** A simplified visual booklet with large iconography explaining how to review daily schedules and trigger/cancel emergency SOS alerts.")
    lines.append("- **Administrator Deployment & Maintenance Guide:** Technical documentation covering LAMP installation, cron setup, database backups, and security configurations.\n")
    
    lines.append("### 2.7 Assumptions and Dependencies")
    lines.append("- **Assumptions:** Users have access to compatible browser devices and basic internet connectivity. Caregivers possess basic literacy in operating mobile touch devices. Guardians provide accurate clinical baseline data during resident onboarding.")
    lines.append("- **Dependencies:** Continuous uptime of external telecommunications SMS gateways (Twilio API) for emergency dispatch; continuous operation of local SMTP mail servers; and browser permission access to device Geolocation and Web Audio subsystems.\n")
    lines.append("---\n")
    
    # Section 3: External Interface Requirements
    lines.append("## 3. External Interface Requirements\n")
    lines.append("### 3.1 User Interfaces")
    lines.append("The user interface of ECMS is built on a card-based visual design pattern emphasizing clarity, high contrast, and rapid touch navigation. Key UI standards include:")
    lines.append("- **Consistent Header & Navigation:** Displays the logged-in user profile, active senior resident selector, persistent SOS trigger, and role-appropriate navigational links.")
    lines.append("- **Status Indication Badges:** Distinct high-contrast badges for clinical metrics (Normal: `#10B981` green, Warning: `#F59E0B` amber, Critical Anomaly: `#EF4444` red).")
    lines.append("- **Modal Windows:** Destructive and life-critical actions (e.g., medication omission, appointment cancellation, SOS triggering) require explicit confirmation dialogs with clear 'Confirm' and 'Cancel' buttons.")
    lines.append("- **Senior-Optimized Interface:** Senior dashboards eliminate nested menus, presenting single-tap cards for 'Today's Medicine', 'My Doctor', and a prominent 80px high 'EMERGENCY SOS' button.\n")
    
    lines.append("### 3.2 Hardware Interfaces")
    lines.append("- **Touchscreen Tablets & Smartphones:** Responsive capacitive touch support for tap, long-press (2-second SOS hold), and scroll gestures.")
    lines.append("- **Audio Output Hardware:** Interfaces with device sound cards and internal speakers via the Web Audio API to produce an 85+ dB emergency warning siren during distress escalation.")
    lines.append("- **GPS Telemetry Receivers:** Interfaces with hardware GPS sensors via the HTML5 Geolocation API to harvest coordinates during emergency SOS dispatches.\n")
    
    lines.append("### 3.3 Software Interfaces")
    lines.append("- **Database Engine (MySQL 8.0):** Communicates via TCP/IP on port 3306 using PHP PDO with strict transaction isolation (READ COMMITTED).")
    lines.append("- **Twilio REST SMS Gateway:** Communicates over outbound HTTPS POST requests with JSON payloads to send urgent SMS alerts to mobile telephone networks.")
    lines.append("- **Leaflet.js / OpenStreetMap Service:** Interfaces with open-source tile servers over HTTPS to render interactive emergency incident location pins.")
    lines.append("- **Web Audio API:** Standard W3C browser audio engine generating multi-frequency synthesized siren tones locally on client devices without requiring external audio file downloads.\n")
    
    lines.append("### 3.4 Communications Interfaces")
    lines.append("- **HTTPS / TLS 1.3:** All web traffic between client browsers and the ECMS web server must be encrypted using Transport Layer Security (TLS 1.3) with modern cipher suites.")
    lines.append("- **RESTful JSON Protocol:** Asynchronous data communications (AJAX) utilize standard HTTP methods (GET, POST, PUT, DELETE) with `application/json` content-type headers.")
    lines.append("- **SMTP / TLS:** Outbound email summaries and appointment reminders are routed through standard SMTP over port 587 with STARTTLS encryption.\n")
    lines.append("---\n")
    
    # Section 4: Domain Model
    lines.append("## 4. Domain Model\n")
    lines.append("The domain model defines the core conceptual entities, their attributes, operations, and interrelationships within the geriatric care management domain. The central entity is the **Senior Resident**, whose care ecosystem is supported by family guardians, clinical caregivers, and attending physicians.\n")
    lines.append("### Core Domain Entities:")
    lines.append("1. **User:** Base actor entity encapsulating `user_id`, `email`, `password_hash`, `role` (Admin, Guardian, Caregiver, Doctor, Senior), `phone`, `status`, and `created_at`.")
    lines.append("2. **Senior:** Represents the care recipient, capturing `senior_id`, `mrn_number`, `full_name`, `dob`, `gender`, `blood_group`, `allergies`, `chronic_conditions`, `room_number`, and `guardian_id`.")
    lines.append("3. **Medication:** Master pharmaceutical drug definition containing `med_id`, `generic_name`, `brand_name`, `dosage_form`, `strength`, and `contraindications`.")
    lines.append("4. **MedicationSchedule:** Recurring regimen entry storing `schedule_id`, `senior_id`, `med_id`, `frequency`, `scheduled_time`, `meal_relation`, `start_date`, and `end_date`.")
    lines.append("5. **MedicationLog:** Permanent administration record tracking `log_id`, `schedule_id`, `administered_at`, `status` (Given, Missed, Refused), `reason`, `caregiver_id`, and `signature_pin`.")
    lines.append("6. **VitalSign:** Longitudinal physiological telemetry storing `vital_id`, `senior_id`, `recorded_at`, `systolic_bp`, `diastolic_bp`, `pulse_rate`, `spo2`, `temperature`, `glucose`, `caregiver_id`, and `is_anomaly`.")
    lines.append("7. **Appointment:** Medical consultation booking containing `appointment_id`, `senior_id`, `doctor_id`, `scheduled_at`, `consultation_type` (In-Person, Teleconsult), `status`, and `notes`.")
    lines.append("8. **EmergencyAlert:** Incident management record tracking `alert_id`, `senior_id`, `triggered_at`, `trigger_source`, `latitude`, `longitude`, `status` (Triggered, Responding, Resolved), and `resolved_by`.")
    lines.append("9. **ShiftNote:** Shift handover continuity report tracking `shift_id`, `caregiver_id`, `shift_type`, `handover_to`, `progress_notes`, `overdue_tasks`, and `signed_at`.")
    lines.append("10. **AuditTrail:** Immutable security record capturing `audit_id`, `user_id`, `action`, `entity_affected`, `ip_address`, and `timestamp`.\n")
    lines.append("*(Refer to Appendix B for the comprehensive Entity-Relationship Diagram detailing primary keys, foreign key constraints, and 1:N cardinalities.)*\n")
    lines.append("---\n")
    
    # Section 5: System Features (Use Cases)
    lines.append("## 5. System Features (Use Cases)\n")
    lines.append("This section documents the eight (8) core system features of ECMS in exhaustive, structured IEEE Std 830 use case specifications. Each use case details operational triggers, preconditions, paired basic flows, alternate flows, sub-flows, business rules, non-functional constraints, and screen entry exception tables.\n")
    
    for uc in USE_CASES:
        lines.append(f"### {uc['num']} {uc['title']}\n")
        lines.append(f"**Brief Description:** {uc['brief_description']}\n")
        lines.append(f"**Business Trigger:** {uc['business_trigger']}\n")
        lines.append(f"**Preconditions:** {uc['preconditions']}\n")
        lines.append(f"**Basic Flow:**  \n*Assumptions: {uc['assumptions']}*\n")
        lines.append("| Line | System Actor Action | System Response |")
        lines.append("| :--- | :--- | :--- |")
        for step in uc['basic_flow']:
            lines.append(f"| {step[0]} | {step[1]} | {step[2]} |")
        lines.append(f"\n**Post Condition:** {uc['post_condition']}\n")
        
        # Alternate Flows
        for af in uc['alternate_flows']:
            lines.append(f"#### Alternate Flow ({af['name']})")
            lines.append(f"*{af['condition']}*\n")
            lines.append("| Line | System Actor Action | System Response |")
            lines.append("| :--- | :--- | :--- |")
            for step in af['steps']:
                lines.append(f"| {step[0]} | {step[1]} | {step[2]} |")
            lines.append(f"\n*{af['restart']}*  \n**Post Condition:** {af['post_condition']}\n")
            
        # Sub-Flows
        if 'sub_flows' in uc and uc['sub_flows']:
            for sf in uc['sub_flows']:
                lines.append(f"#### Sub-Flow: {sf['name']}\n")
                lines.append("| Line | System Actor Action | System Response |")
                lines.append("| :--- | :--- | :--- |")
                for step in sf['steps']:
                    lines.append(f"| {step[0]} | {step[1]} | {step[2]} |")
                lines.append(f"\n*{sf['return_statement']}*\n")
                
        # Business Rules
        lines.append("#### Business Rules:")
        for br in uc['business_rules']:
            lines.append(f"- {br}")
        lines.append("")
        
        # Non-Functional Requirements
        lines.append("#### Non-Functional Requirements:")
        for nfr in uc['nfr']:
            lines.append(f"- {nfr}")
        lines.append("")
        
        # Data Requirements
        lines.append("#### Data Requirements:")
        for dr in uc['data_requirements']:
            lines.append(f"- {dr}")
        lines.append("")
        
        # Screen Entry Exception Table
        lines.append("#### Screen Entry Exception Table:\n")
        lines.append("| Field | Constraint | Response |")
        lines.append("| :--- | :--- | :--- |")
        for exc in uc['exceptions']:
            lines.append(f"| {exc[0]} | {exc[1]} | {exc[2]} |")
        lines.append("\n---\n")
        
    # Section 6: Other Nonfunctional Requirements
    lines.append("## 6. Other Nonfunctional Requirements\n")
    lines.append("### 6.1 Performance Requirements")
    lines.append("- **Response Time:** Standard user interface pages must load and render completely within 1.2 seconds over a standard 4G/broadband connection.")
    lines.append("- **API Latency:** Asynchronous REST endpoints (e.g., vitals logging, dose status recording) must return JSON responses within 350 milliseconds under standard load.")
    lines.append("- **Concurrent Throughput:** The server infrastructure must support at least 250 active concurrent user sessions without performance degradation (CPU utilization < 70%).")
    lines.append("- **Database Query Execution:** 95% of database queries must execute in under 80 milliseconds, facilitated by indexed foreign keys and normalized schemas.")
    lines.append("- **Availability:** The system must maintain an operational availability of 99.9% (less than 8.7 hours of unplanned downtime per calendar year).\n")
    
    lines.append("### 6.2 Safety Requirements")
    lines.append("- **Clinical Contraindication Detection:** The medication scheduling engine must validate newly entered prescriptions against active drug profiles to prevent hazardous drug-drug interactions.")
    lines.append("- **Emergency Redundancy:** SOS alerts must broadcast across multiple redundant channels simultaneously: client browser audio sirens, real-time dashboard banners, SMS messages to family guardians, and backup SMS messages to attending doctors.")
    lines.append("- **Immutable Audit Integrity:** Medication administration records, vital sign entries, and emergency alerts cannot be permanently deleted; corrections must be preserved as historical addenda with caregiver identification.\n")
    
    lines.append("### 6.3 Security Requirements")
    lines.append("- **Password Storage & Cryptography:** All passwords must be salted and hashed using Bcrypt with a work factor of at least 12.")
    lines.append("- **SQL Injection Prevention:** All SQL interactions must be executed via PHP Data Objects (PDO) using prepared statements with bound parameters.")
    lines.append("- **Session Protection:** Authenticated user sessions must enforce 256-bit cryptographically secure session IDs transmitted via HTTP-only, Secure, SameSite=Strict cookies. Sessions must automatically expire after 15 minutes of user inactivity.")
    lines.append("- **Cross-Site Request Forgery (CSRF):** All state-changing POST/PUT requests must validate a synchronized CSRF token stored in the user's session.")
    lines.append("- **Role-Based Authorization (RBAC):** Server-side route middleware must verify user role permissions prior to executing any controller action, rejecting unauthorized access with an HTTP 403 Forbidden status.\n")
    
    lines.append("### 6.4 Software Quality Attributes")
    lines.append("- **Usability:** The interface must achieve a System Usability Scale (SUS) score of at least 85, verified through user testing with elderly seniors and geriatric care nurses.")
    lines.append("- **Reliability:** Mean Time Between Failures (MTBF) must exceed 720 operating hours. In the event of network disruption, the frontend client must cache pending entries locally and re-sync upon reconnection.")
    lines.append("- **Maintainability:** Codebase structured in a clean Model-View-Controller (MVC) architectural pattern with comprehensive inline docstrings and separation of concerns.")
    lines.append("- **Portability:** Fully standards-compliant across all modern web browsers (Chrome, Edge, Firefox, Safari) without requiring platform-specific plugins.\n")
    lines.append("---\n")
    
    # Section 7: Other Requirements
    lines.append("## 7. Other Requirements\n")
    lines.append("### 7.1 Database Requirements")
    lines.append("- Schema designed in strict 3rd Normal Form (3NF) to prevent data redundancy and anomalies.")
    lines.append("- InnoDB storage engine utilizing transactional integrity (ACID compliance) and foreign key cascade rules.")
    lines.append("- Automated daily cryptographic backup of the complete database with a 30-day retention schedule.\n")
    
    lines.append("### 7.2 Internationalization & Localization Requirements")
    lines.append("- Fully bilingual architecture supporting both English and Bengali (বাংলা) user interfaces.")
    lines.append("- Date and time formatting adhering to Bangladeshi standard formats (DD/MM/YYYY and 12-hour AM/PM notation).")
    lines.append("- E.164 phone number formatting supporting standard 11-digit Bangladeshi mobile networks (`+8801XXXXXXXXX`).\n")
    
    lines.append("### 7.3 Legal, Regulatory & Data Privacy Requirements")
    lines.append("- Full compliance with the Bangladesh Digital Security Act and international healthcare data privacy principles (HIPAA / GDPR benchmarks).")
    lines.append("- Explicit patient/guardian consent workflows for data processing and emergency telecommunications contact sharing.")
    lines.append("- Role-segregated data access ensuring financial guardians cannot alter medical prescriptions and clinical doctors cannot view billing financial data.\n")
    
    lines.append("### 7.4 Software Reuse & Architectural Extensibility")
    lines.append("- Modular RESTful API architecture facilitating future integration with commercial electronic medical record (EMR) systems and IoT biometric hardware.")
    lines.append("- Extensible notification service allowing seamless addition of WhatsApp Business API or push notification adapters.\n")
    lines.append("---\n")
    
    # Appendix A: Glossary
    lines.append("## Appendix A: Glossary\n")
    lines.append("| Term | Description |")
    lines.append("| :--- | :--- |")
    for row in GLOSSARY:
        lines.append(f"| **{row[0]}** | {row[1]} |")
    lines.append("\n---\n")
    
    # Appendix B: Analysis Models
    lines.append("## Appendix B: Analysis Models\n")
    lines.append("This appendix incorporates formal software engineering analysis models visualizing the functional decomposition, data flow, and structural relationships of the Elderly Care Management System.\n")
    lines.append("### B.1 Context Diagram (Level 0 DFD)")
    lines.append("Depicts the boundary of ECMS in relation to external entities: Administrator, Guardian, Caregiver, Doctor, Senior Resident, Twilio SMS Gateway, and SMTP Email Server.\n")
    lines.append("![Figure 4: Context Diagram (Level 0 DFD)](figures_png/fig_context_diagram.png)\n")
    lines.append("### B.2 Level 1 Data Flow Diagram (DFD)")
    lines.append("Visualizes the decomposition of ECMS into core sub-processes:")
    lines.append("- 1.0 User Authentication & Session Authorization")
    lines.append("- 2.0 Senior Resident Profile & Clinical Records Management")
    lines.append("- 3.0 Medication Scheduling & Administration Engine")
    lines.append("- 4.0 Real-Time Physiological Vitals Telemetry")
    lines.append("- 5.0 Medical Appointments & Teleconsultation Scheduling")
    lines.append("- 6.0 Emergency SOS Incident Dispatch & Siren Escalation")
    lines.append("- 7.0 Caregiver Shift Handoff & Clinical Progress Reporting\n")
    lines.append("### B.3 Entity-Relationship Diagram (ERD)")
    lines.append("Captures the relational data structure of ECMS across 10 tables (`users`, `seniors`, `medications`, `medication_schedules`, `medication_logs`, `vitals`, `appointments`, `emergency_alerts`, `shift_notes`, `audit_logs`).\n")
    lines.append("### B.4 State Machine Transition Models")
    lines.append("1. **Medication Schedule State:** `Scheduled` -> `Pending` -> `Administered (Given)` OR `Missed` OR `Refused`.")
    lines.append("2. **Emergency SOS Incident State:** `Triggered` -> `5-sec Countdown` -> `Dispatched/Broadcasting` -> `Caregiver Responding` -> `Resolved`.\n")
    lines.append("---\n")
    
    # Appendix C: Interface Examples
    lines.append("## Appendix C: Interface Examples\n")
    lines.append("### EXAMPLE 1: Caregiver Operations Dashboard (Screen Layout with Callouts)\n")
    lines.append("The primary operational workstation for duty caregivers, featuring real-time clinical telemetry, scheduled medication queues, and persistent emergency triggers.\n")
    
    callouts = [
        ["Resident Selector (1)", "Dropdown element allowing the caregiver to toggle between assigned senior residents in their care unit."],
        ["Active Emergency Banner (2)", "High-contrast dynamic red banner flashing during active SOS incidents, displaying resident name and room number."],
        ["Vitals Telemetry Cards (3)", "Real-time cards displaying latest Blood Pressure, Heart Rate, SpO2, and Blood Glucose with color-coded norm badges."],
        ["Medication Schedule Timetable (4)", "Chronological timetable detailing upcoming, due, and overdue medications for the current shift window."],
        ["Administration Action Buttons (5)", "One-click interactive buttons allowing the nurse to record dose status: 'Given' (green), 'Missed' (amber), 'Refused' (red)."],
        ["Shift Handoff Quick Notes (6)", "Interactive text panel for logging ongoing observational progress notes and flagging items for incoming staff."],
        ["Prominent Emergency SOS Trigger (7)", "Persistent 80px high red emergency distress button triggering the multi-channel siren and escalation sequence."]
    ]
    lines.append("| Callout Number | Description |")
    lines.append("| :--- | :--- |")
    for c in callouts:
        lines.append(f"| **{c[0]}** | {c[1]} |")
    lines.append("\n### EXAMPLE 2: Medication Administration Record Entry Screen (Field Constraints Table)\n")
    lines.append("Form field constraints for the medication intake logging screen, matching the industry specification format:\n")
    
    field_specs = [
        ["Resident Full Name", "Not editable text field. Auto-filled from active resident session."],
        ["Medical Record Number (MRN)", "Not editable alphanumeric label. Auto-filled from database."],
        ["Medication Name", "Not editable text field. Pre-selected from active prescription schedule."],
        ["Prescribed Dosage & Unit", "Not editable text field. Auto-filled (e.g., '10 mg Tablet')."],
        ["Scheduled Administration Time", "Not editable time field. Auto-filled (e.g., '08:00 AM')."],
        ["Actual Administration Timestamp", "Editable datetime field. Auto-filled with current system time. Mask: YYYY-MM-DD HH:MM:SS."],
        ["Administration Status", "Editable dropdown selection. Options: 'Given', 'Missed', 'Refused'. Mandatory field."],
        ["Reason for Exception / Omission", "Editable text field. Max 255 symbols. Mandatory if status is 'Missed' or 'Refused'."],
        ["Administering Caregiver", "Not editable text field. Auto-filled with authenticated caregiver name."],
        ["Caregiver Verification PIN", "Editable password field. Exactly 4 numeric digits. Masked entry for clinical non-repudiation."],
        ["Clinical Observation Notes", "Editable textarea. Max 1,000 symbols. Letters, digits, and clinical punctuation allowed."]
    ]
    lines.append("| Field | Description |")
    lines.append("| :--- | :--- |")
    for f in field_specs:
        lines.append(f"| **{f[0]}** | {f[1]} |")
    lines.append("\n---\n")
    
    # Appendix D: To Be Determined (TBD) List
    lines.append("## Appendix D: To Be Determined (TBD) List\n")
    lines.append("This section records architectural enhancements, third-party integrations, and advanced capabilities scheduled for Phase 2 and Phase 3 development iterations:\n")
    lines.append("| Item ID | Feature Title | Detailed Description | Target Milestone |")
    lines.append("| :--- | :--- | :--- | :--- |")
    for tbd in TBD_LIST:
        lines.append(f"| **{tbd[0]}** | {tbd[1]} | {tbd[2]} | {tbd[3]} |")
    lines.append("\n")
    
    # Write to file
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated Markdown: {md_path}")

# -------------------------------------------------------------
# 2. GENERATE STANDALONE HTML DOCUMENT (.html)
# -------------------------------------------------------------
def generate_html(html_path):
    logo_b64 = get_base64_image(os.path.join(BASE_DIR, "iub_logo.png"))
    
    # Prepare figure images if they exist
    fig2_b64 = get_base64_image(os.path.join(BASE_DIR, "figures_png", "fig2_proposed_system.png"))
    fig3_b64 = get_base64_image(os.path.join(BASE_DIR, "figures_png", "fig3_system_architecture.png"))
    fig5_b64 = get_base64_image(os.path.join(BASE_DIR, "figures_png", "fig5_er_diagram.png"))
    fig_context_b64 = get_base64_image(os.path.join(BASE_DIR, "figures_png", "fig_context_diagram.png"))
    fig6_b64 = get_base64_image(os.path.join(BASE_DIR, "figures_png", "fig6_data_flow_diagram.png"))
    
    h = []
    h.append("<!DOCTYPE html>")
    h.append("<html lang=\"en\">")
    h.append("<head>")
    h.append("<meta charset=\"UTF-8\">")
    h.append("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
    h.append(f"<title>{METADATA['doc_title']} - {METADATA['project_title']}</title>")
    h.append("""<style>
  @page {
    size: A4 portrait;
    margin: 20mm 18mm 20mm 18mm;
    @bottom-center {
      content: counter(page);
      font-size: 10pt;
      font-family: Arial, Helvetica, sans-serif;
      color: #000000;
    }
  }

  @page :first {
    @bottom-center {
      content: none;
    }
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: Arial, Helvetica, sans-serif;
    background: #FFFFFF;
    color: #000000;
    line-height: 1.55;
    padding: 20px;
    max-width: 920px;
    margin: 0 auto;
    font-size: 13px;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  /* Cover Page Styling */
  .cover-page {
    text-align: center;
    padding: 20px 20px 40px;
    min-height: 94vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    page-break-after: always;
    break-after: page;
    border: none;
    box-sizing: border-box;
  }

  @media print {
    .cover-page {
      height: 9.0in;
      max-height: 9.0in;
      margin-bottom: 0;
      padding-top: 10px;
      padding-bottom: 15px;
      page-break-after: always;
      break-after: page;
    }
  }

  .cover-logo-box {
    margin-bottom: 20px;
  }

  .cover-logo {
    width: 200px;
    max-width: 200px;
    height: auto;
    display: block;
    margin: 0 auto;
  }

  .cover-title-box {
    margin-bottom: 28px;
  }

  .cover-doc-title {
    font-size: 16pt;
    font-weight: bold;
    color: #000000;
    line-height: 1.35;
  }

  .cover-project-title {
    font-size: 18pt;
    font-weight: bold;
    color: #000000;
    line-height: 1.35;
    margin-top: 6px;
  }

  .cover-version-status {
    font-size: 11pt;
    font-style: italic;
    color: #333333;
    margin-top: 6px;
  }

  .cover-prepared-box {
    margin-bottom: 24px;
    line-height: 1.45;
  }

  .cover-meta-label {
    font-size: 10.5pt;
    font-weight: bold;
    color: #000000;
    margin-bottom: 2px;
  }

  .cover-meta-value {
    font-size: 12.5pt;
    color: #000000;
    font-weight: bold;
  }

  .cover-meta-sub {
    font-size: 11pt;
    color: #000000;
  }

  .cover-inst-box {
    line-height: 1.4;
  }

  .cover-dept {
    font-size: 11pt;
    font-weight: bold;
    color: #000000;
  }

  .cover-inst {
    font-size: 11pt;
    color: #000000;
  }

  .cover-date {
    font-size: 10.5pt;
    color: #000000;
    margin-top: 4px;
  }

  /* Document Body Typography */
  .section-divider {
    page-break-before: always;
    break-before: page;
    padding-top: 15px;
  }

  h1, h2, h3, h4 {
    color: #000000;
    font-family: Arial, Helvetica, sans-serif;
    font-weight: bold;
    page-break-after: avoid;
    break-after: avoid;
  }

  h1 {
    font-size: 18pt;
    margin-top: 24px;
    margin-bottom: 12px;
    padding-bottom: 4px;
    border-bottom: 1.5px solid #000000;
  }

  h2 {
    font-size: 14pt;
    margin-top: 20px;
    margin-bottom: 10px;
    padding-bottom: 3px;
    border-bottom: 1px solid #333333;
  }

  h3 {
    font-size: 12pt;
    margin-top: 16px;
    margin-bottom: 8px;
  }

  h4 {
    font-size: 10.5pt;
    margin-top: 12px;
    margin-bottom: 6px;
  }

  p {
    margin-bottom: 10px;
    text-align: justify;
    line-height: 1.55;
    color: #000000;
  }

  ul, ol {
    margin-left: 24px;
    margin-bottom: 12px;
  }

  li {
    margin-bottom: 4px;
    line-height: 1.5;
    color: #000000;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0 18px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  th, td {
    border: 1px solid #B0B0B0;
    padding: 7px 10px;
    text-align: left;
    vertical-align: top;
    color: #000000;
  }

  th {
    background-color: #EEEEEE;
    font-weight: bold;
    color: #000000;
    border-bottom: 2px solid #000000;
  }

  tr:nth-child(even) td {
    background-color: #FAFAFA;
  }

  /* Figures */
  .figure-box {
    text-align: center;
    margin: 16px 0;
    page-break-inside: avoid;
  }

  .figure-box img {
    max-width: 90%;
    height: auto;
    border: 1px solid #D0D0D0;
  }

  .figure-caption {
    font-size: 9.5pt;
    font-weight: bold;
    color: #000000;
    margin-top: 6px;
  }

  .use-case-card {
    margin-bottom: 24px;
    page-break-inside: avoid;
  }

  .toc-list {
    list-style-type: none;
    margin-left: 0;
  }

  .toc-list li {
    padding: 3px 0;
  }

  .toc-sub {
    margin-left: 20px;
    list-style-type: none;
  }
</style>
</head>
<body>
""")
    
    # ---------------- PAGE 1: COVER PAGE ----------------
    h.append("<div class=\"cover-page\">")
    h.append("  <div class=\"cover-logo-box\">")
    if logo_b64:
        h.append(f"    <img src=\"{logo_b64}\" alt=\"IUB Logo\" class=\"cover-logo\">")
    h.append("  </div>")
    
    h.append("  <div class=\"cover-title-box\">")
    h.append(f"    <div class=\"cover-doc-title\">{METADATA['doc_title']}</div>")
    h.append(f"    <div class=\"cover-project-title\">{METADATA['project_title']}</div>")
    h.append(f"    <div class=\"cover-version-status\">{METADATA['version']} | Status: {METADATA['status']}</div>")
    h.append("    <div style=\"font-size: 9.5pt; color: #444; margin-top: 4px;\">Industry Specification Standard IEEE Std 830-1998 Compliant</div>")
    h.append("  </div>")
    
    h.append("  <div class=\"cover-prepared-box\">")
    h.append("    <div class=\"cover-meta-label\">Prepared by:</div>")
    h.append(f"    <div class=\"cover-meta-value\">{METADATA['author_name']}</div>")
    h.append(f"    <div class=\"cover-meta-sub\">{METADATA['author_role']}</div>")
    h.append(f"    <div class=\"cover-meta-sub\">Student ID: {METADATA['student_id']}</div>")
    h.append(f"    <div class=\"cover-meta-sub\" style=\"margin-top: 4px;\">{METADATA['course']}</div>")
    h.append("  </div>")
    
    h.append("  <div class=\"cover-prepared-box\">")
    h.append("    <div class=\"cover-meta-label\">Supervised by:</div>")
    h.append(f"    <div class=\"cover-meta-value\" style=\"font-size: 11pt;\">{METADATA['instructor']}</div>")
    h.append("  </div>")
    
    h.append("  <div class=\"cover-inst-box\">")
    h.append("    <div class=\"cover-dept\">Department of Computer Science and Engineering</div>")
    h.append(f"    <div class=\"cover-inst\">{METADATA['organization']}</div>")
    h.append(f"    <div class=\"cover-date\">{METADATA['date']}</div>")
    h.append("  </div>")
    h.append("</div>") # End Cover Page
    
    # ---------------- PAGE 2: TABLE OF CONTENTS ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>Table of Contents</h1>")
    h.append("<ul class=\"toc-list\">")
    h.append("  <li><strong>1. Introduction</strong>")
    h.append("    <ul class=\"toc-sub\">")
    h.append("      <li>1.1 Purpose</li><li>1.2 Document Conventions</li><li>1.3 Intended Audience and Reading Suggestions</li><li>1.4 Product Scope</li><li>1.5 References</li>")
    h.append("    </ul>")
    h.append("  </li>")
    h.append("  <li><strong>2. Overall Description</strong>")
    h.append("    <ul class=\"toc-sub\">")
    h.append("      <li>2.1 Product Perspective</li><li>2.2 Product Functions</li><li>2.3 User Classes and Characteristics</li><li>2.4 Operating Environment</li><li>2.5 Design and Implementation Constraints</li><li>2.6 User Documentation</li><li>2.7 Assumptions and Dependencies</li>")
    h.append("    </ul>")
    h.append("  </li>")
    h.append("  <li><strong>3. External Interface Requirements</strong>")
    h.append("    <ul class=\"toc-sub\">")
    h.append("      <li>3.1 User Interfaces</li><li>3.2 Hardware Interfaces</li><li>3.3 Software Interfaces</li><li>3.4 Communications Interfaces</li>")
    h.append("    </ul>")
    h.append("  </li>")
    h.append("  <li><strong>4. Domain Model</strong></li>")
    h.append("  <li><strong>5. System Features (Use Cases)</strong>")
    h.append("    <ul class=\"toc-sub\">")
    h.append("      <li>5.1 Use Case UC-01: User Authentication & Role-Based Access Control</li>")
    h.append("      <li>5.2 Use Case UC-02: Senior Resident Profile & Health Record Setup</li>")
    h.append("      <li>5.3 Use Case UC-03: Medication Regimen Scheduling & Automated Pill Reminders</li>")
    h.append("      <li>5.4 Use Case UC-04: Daily Caregiving & Medication Administration Logging</li>")
    h.append("      <li>5.5 Use Case UC-05: Real-Time Vitals Tracking & Physiological Anomaly Alerting</li>")
    h.append("      <li>5.6 Use Case UC-06: Doctor Appointment Scheduling & Clinical Teleconsultation Booking</li>")
    h.append("      <li>5.7 Use Case UC-07: Emergency SOS Alert Dispatch & Incident Escalation Workflow</li>")
    h.append("      <li>5.8 Use Case UC-08: Caregiver Shift Handoff & Clinical Progress Notes</li>")
    h.append("    </ul>")
    h.append("  </li>")
    h.append("  <li><strong>6. Other Nonfunctional Requirements</strong>")
    h.append("    <ul class=\"toc-sub\">")
    h.append("      <li>6.1 Performance Requirements</li><li>6.2 Safety Requirements</li><li>6.3 Security Requirements</li><li>6.4 Software Quality Attributes</li>")
    h.append("    </ul>")
    h.append("  </li>")
    h.append("  <li><strong>7. Other Requirements</strong>")
    h.append("    <ul class=\"toc-sub\">")
    h.append("      <li>7.1 Database Requirements</li><li>7.2 Internationalization & Localization Requirements</li><li>7.3 Legal, Regulatory & Data Privacy Requirements</li><li>7.4 Software Reuse & Architectural Extensibility</li>")
    h.append("    </ul>")
    h.append("  </li>")
    h.append("  <li><strong>Appendix A: Glossary</strong></li>")
    h.append("  <li><strong>Appendix B: Analysis Models</strong></li>")
    h.append("  <li><strong>Appendix C: Interface Examples</strong></li>")
    h.append("  <li><strong>Appendix D: To Be Determined (TBD) List</strong></li>")
    h.append("</ul>")
    h.append("</div>")
    
    # ---------------- PAGE 3: REVISION HISTORY ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>Revision History</h1>")
    h.append("<table>")
    h.append("  <thead><tr><th>Name</th><th>Date</th><th>Reason For Changes</th><th>Version</th><th>Date of Approval</th></tr></thead>")
    h.append("  <tbody>")
    for r in REVISION_HISTORY:
        h.append(f"    <tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td><strong>{r[3]}</strong></td><td>{r[4]}</td></tr>")
    h.append("  </tbody>")
    h.append("</table>")
    h.append("</div>")
    
    # ---------------- SECTION 1: INTRODUCTION ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>1. Introduction</h1>")
    h.append("<h2>1.1 Purpose</h2>")
    h.append("<p>This Software Requirements Specification (SRS) document defines the complete functional and non-functional requirements for Version 1.0 (Final Release) of the <strong>Elderly Care Management System (ECMS)</strong>. This specification establishes a binding contract between project stakeholders—including institutional geriatric administrators, family guardians, caregiving personnel, clinical physicians, and software engineering teams. The scope of this document encompasses all core subsystems: User Authentication & Role-Based Access Control (RBAC), Senior Resident Health Profile Management, Medication Regimen Scheduling & Adherence Tracking, Real-Time Vitals Telemetry & Physiological Anomaly Detection, Doctor Appointment Coordination, Multi-Channel Emergency SOS Alert Escalation, and Caregiver Shift Handoff Documentation.</p>")
    
    h.append("<h2>1.2 Document Conventions</h2>")
    h.append("<p>This document strictly adheres to the <strong>IEEE Std 830-1998 Recommended Practice for Software Requirements Specifications</strong>. In accordance with academic and institutional submission guidelines:</p>")
    h.append("<ul>")
    h.append("  <li><strong>Typography & Aesthetics:</strong> Formatted in strict <strong>Black & White</strong> typography to maximize legibility and ensure professional publication standards without distracting decorative borders or excessive coloration.</li>")
    h.append("  <li><strong>Requirement Identification:</strong> Requirements are uniquely tagged using standardized alphanumeric prefixes (e.g., <code>UC-XX</code> for Use Cases, <code>BR-XX</code> for Business Rules, <code>NFR-XX</code> for Non-Functional Requirements, and <code>DR-XX</code> for Data Requirements).</li>")
    h.append("  <li><strong>Priority Classifications:</strong> System features are classified according to MoSCoW prioritization (Must Have, Should Have, Could Have, and Won't Have for this release).</li>")
    h.append("</ul>")
    
    h.append("<h2>1.3 Intended Audience and Reading Suggestions</h2>")
    h.append("<p>This document addresses five primary stakeholder categories, each requiring specific perspectives when reviewing the specification:</p>")
    h.append("<table>")
    h.append("  <thead><tr><th>ID</th><th>Stakeholder</th><th>Description</th></tr></thead>")
    h.append("  <tbody>")
    for row in INTENDED_AUDIENCE:
        h.append(f"    <tr><td><strong>{row[0]}</strong></td><td><strong>{row[1]}</strong></td><td>{row[2]}</td></tr>")
    h.append("  </tbody>")
    h.append("</table>")
    h.append("<p><strong>Suggested Reading Sequence:</strong></p>")
    h.append("<ol>")
    h.append("  <li><strong>Executive Stakeholders & Guardians:</strong> Review Section 1 (Introduction), Section 2 (Overall Description), and Appendix C (Interface Examples).</li>")
    h.append("  <li><strong>Engineering & Development Team:</strong> Proceed systematically through Section 2 (System Architecture), Section 3 (External Interfaces), Section 4 (Domain Model), Section 5 (Detailed Use Cases), and Appendix B (Analysis Models).</li>")
    h.append("  <li><strong>QA & Validation Engineers:</strong> Focus intensely on Section 5 (Use Case basic/alternate flows and Screen Entry Exception Tables) and Section 6 (Non-Functional Requirements).</li>")
    h.append("</ol>")
    
    h.append("<h2>1.4 Product Scope</h2>")
    h.append("<p>The Elderly Care Management System (ECMS) is a dedicated healthcare coordination web application engineered to address the critical challenges of geriatric care: uncoordinated paper logs, dangerous medication omissions, delayed emergency responses, and lack of family oversight. ECMS unifies daily caregiving into a centralized, transparent digital ecosystem. Key objectives include:</p>")
    h.append("<ul>")
    h.append("  <li>Eliminating medication administration errors through scheduled dose reminders and mandatory caregiver verification.</li>")
    h.append("  <li>Providing instant multi-channel emergency SOS alerting with audible sirens, SMS broadcasts, and GPS positioning.</li>")
    h.append("  <li>Enabling real-time physiological telemetry monitoring with automatic anomaly detection for hypertensive crisis or hypoxia.</li>")
    h.append("  <li>Establishing comprehensive clinical continuity across nursing shifts via structured electronic progress notes.</li>")
    h.append("  <li>Delivering an accessible, high-contrast user interface tailored specifically to the visual and motor capabilities of elderly seniors (WCAG 2.1 AA compliant).</li>")
    h.append("</ul>")
    
    h.append("<h2>1.5 References</h2>")
    h.append("<ol>")
    h.append("  <li>IEEE Computer Society, <em>IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications</em>, IEEE, New York, 1998.</li>")
    h.append("  <li>World Wide Web Consortium (W3C), <em>Web Content Accessibility Guidelines (WCAG) 2.1</em>, W3C Recommendation, 2018.</li>")
    h.append("  <li>World Health Organization (WHO), <em>Integrated Care for Older People (ICOPE): Guidance for Person-Centred Assessment and Pathways in Primary Care</em>, WHO, Geneva, 2019.</li>")
    h.append("  <li>Health Level Seven International, <em>HL7 FHIR Release 4.0.1: Fast Healthcare Interoperability Resources</em>, HL7, 2019.</li>")
    h.append("  <li>PHP Group, <em>PHP 8.2 Documentation & Secure PDO Guidelines</em>, 2024.</li>")
    h.append("  <li>Twilio Inc., <em>Twilio REST API Documentation for Programmable SMS & Voice</em>, 2024.</li>")
    h.append("</ol>")
    h.append("</div>")
    
    # ---------------- SECTION 2: OVERALL DESCRIPTION ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>2. Overall Description</h1>")
    h.append("<h2>2.1 Product Perspective</h2>")
    h.append("<p>The Elderly Care Management System (ECMS) is a newly designed, self-contained web platform developed as an integrated solution for institutional care homes and assisted home care environments. It replaces fragmented, error-prone manual paper charts, unencrypted messaging groups, and uncoordinated telephone calls. ECMS operates as a centralized web application built on the LAMP (Linux, Apache, MySQL, PHP) architecture, integrating with external telecommunication SMS gateways, browser Web Audio APIs, and geolocation mapping services.</p>")
    h.append("<p>The system is architected into three distinct functional tiers:</p>")
    h.append("<ol>")
    h.append("  <li><strong>Presentation Tier:</strong> Responsive HTML5/CSS3/JavaScript frontend tailored with accessible WCAG 2.1 AA standards, large touch controls, and high-contrast visuals.</li>")
    h.append("  <li><strong>Application Logic Tier:</strong> Modular PHP backend implementing MVC patterns, authentication middleware, business rule validators, and REST API controllers.</li>")
    h.append("  <li><strong>Persistence Tier:</strong> Relational MySQL 8.0 database engine operating in 3rd Normal Form (3NF) with InnoDB ACID transactions, foreign key constraints, and encrypted medical records.</li>")
    h.append("</ol>")
    if fig3_b64:
        h.append("<div class=\"figure-box\">")
        h.append(f"  <img src=\"{fig3_b64}\" alt=\"System Architecture\">")
        h.append("  <div class=\"figure-caption\">Figure 1: Multi-Tier Architectural Perspective of ECMS</div>")
        h.append("</div>")
        
    h.append("<h2>2.2 Product Functions</h2>")
    h.append("<p>The major functional capabilities provided by the Elderly Care Management System comprise:</p>")
    h.append("<ul>")
    h.append("  <li><strong>Resident Profile & Clinical History:</strong> Centralized management of senior demographics, blood groups, chronic ailments, drug allergies, and primary emergency contacts.</li>")
    h.append("  <li><strong>Medication Administration Record (MAR):</strong> Prescribing, recurring daily scheduling, automated visual/audio alarms, and timestamped caregiver administration logging (Given, Missed, Refused).</li>")
    h.append("  <li><strong>Vitals Telemetry & Anomaly Alerting:</strong> Tracking Blood Pressure, Pulse, Blood Oxygen (SpO2), Temperature, and Blood Glucose, with automatic anomaly detection triggers.</li>")
    h.append("  <li><strong>Doctor Appointment & Teleconsultation Scheduling:</strong> Calendar slot reservations, concurrency lock management, and automated SMS clinical reminders.</li>")
    h.append("  <li><strong>Emergency SOS Incident Management:</strong> One-touch distress trigger with a 5-second false-alarm countdown, automated multi-channel siren broadcast, SMS dispatch, and incident audit tracking.</li>")
    h.append("  <li><strong>Caregiver Shift Handoff:</strong> Structured electronic handoff notes compiling completed care tasks, overdue items, and clinical progress notes between duty shifts.</li>")
    h.append("</ul>")
    if fig2_b64:
        h.append("<div class=\"figure-box\">")
        h.append(f"  <img src=\"{fig2_b64}\" alt=\"Proposed System Workflow\">")
        h.append("  <div class=\"figure-caption\">Figure 2: Top-Level Functional Workflow of ECMS</div>")
        h.append("</div>")
        
    h.append("<h2>2.3 User Classes and Characteristics</h2>")
    h.append("<p>The system supports five distinct user classes with varying privileges and operational technical proficiencies:</p>")
    h.append("<table>")
    h.append("  <thead><tr><th>ID</th><th>User Class</th><th>Description</th></tr></thead>")
    h.append("  <tbody>")
    for row in USER_CLASSES:
        h.append(f"    <tr><td><strong>{row[0]}</strong></td><td><strong>{row[1]}</strong></td><td>{row[2]}</td></tr>")
    h.append("  </tbody>")
    h.append("</table>")
    
    h.append("<h2>2.4 Operating Environment</h2>")
    h.append("<p>ECMS is designed to operate seamlessly across the following technological environment:</p>")
    h.append("<ul>")
    h.append("  <li><strong>Client Hardware:</strong> Standard desktop/laptop personal computers, tablets (Apple iPad, Samsung Galaxy Tab with minimum 1024x768 resolution), and smartphones (iOS 14+, Android 10+).</li>")
    h.append("  <li><strong>Client Browsers:</strong> Modern evergreen web browsers supporting HTML5, CSS Grid, ES6 JavaScript, Web Audio API, and TLS 1.3 (Google Chrome 110+, Mozilla Firefox 110+, Apple Safari 16+, Microsoft Edge 110+).</li>")
    h.append("  <li><strong>Server Environment:</strong> Apache HTTP Server 2.4+ / Nginx on Ubuntu Linux 22.04 LTS / Windows Server, running PHP 8.2+ with PDO, OpenSSL, and cURL extensions.</li>")
    h.append("  <li><strong>Database Server:</strong> MySQL Community Server 8.0+ or MariaDB 10.6+ utilizing the InnoDB storage engine with UTF-8 (<code>utf8mb4</code>) character collation.</li>")
    h.append("  <li><strong>Network Connectivity:</strong> Minimum 3G mobile data or broadband connection (bandwidth &ge; 1.0 Mbps; latency &lt; 150ms).</li>")
    h.append("</ul>")
    
    h.append("<h2>2.5 Design and Implementation Constraints</h2>")
    h.append("<ol>")
    h.append("  <li><strong>Accessibility Standards (WCAG 2.1 AA):</strong> The user interface for senior residents must feature a minimum font size of 16px (18px recommended for key labels), a contrast ratio of at least 4.5:1 for normal text and 3:1 for large graphical components, and touch target sizes of at least 44x44 CSS pixels.</li>")
    h.append("  <li><strong>Core Technology Stack:</strong> In strict accordance with course and architectural requirements, the core web application must be developed using native HTML5, Vanilla CSS3, JavaScript, PHP, and MySQL without proprietary framework lock-ins.</li>")
    h.append("  <li><strong>Security Standards:</strong> All database interactions must use PHP Data Objects (PDO) with parameterized prepared statements to eliminate SQL injection vulnerabilities. All passwords must be salted and hashed via Bcrypt (cost factor &ge; 12).</li>")
    h.append("  <li><strong>Responsive Layouts:</strong> Interfaces must dynamically adapt across viewport widths from 360px (mobile) to 1920px (desktop) without loss of functionality or horizontal scrollbars.</li>")
    h.append("</ol>")
    
    h.append("<h2>2.6 User Documentation</h2>")
    h.append("<p>The project deliverables include comprehensive user documentation:</p>")
    h.append("<ul>")
    h.append("  <li><strong>Caregiver Quick-Start Operational Card (PDF):</strong> A laminated 2-page pocket guide detailing vitals logging, dose administration, and shift handoff workflows.</li>")
    h.append("  <li><strong>Senior Resident Visual Guide:</strong> A simplified visual booklet with large iconography explaining how to review daily schedules and trigger/cancel emergency SOS alerts.</li>")
    h.append("  <li><strong>Administrator Deployment & Maintenance Guide:</strong> Technical documentation covering LAMP installation, cron setup, database backups, and security configurations.</li>")
    h.append("</ul>")
    
    h.append("<h2>2.7 Assumptions and Dependencies</h2>")
    h.append("<ul>")
    h.append("  <li><strong>Assumptions:</strong> Users have access to compatible browser devices and basic internet connectivity. Caregivers possess basic literacy in operating mobile touch devices. Guardians provide accurate clinical baseline data during resident onboarding.</li>")
    h.append("  <li><strong>Dependencies:</strong> Continuous uptime of external telecommunications SMS gateways (Twilio API) for emergency dispatch; continuous operation of local SMTP mail servers; and browser permission access to device Geolocation and Web Audio subsystems.</li>")
    h.append("</ul>")
    h.append("</div>")
    
    # ---------------- SECTION 3: EXTERNAL INTERFACE REQUIREMENTS ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>3. External Interface Requirements</h1>")
    h.append("<h2>3.1 User Interfaces</h2>")
    h.append("<p>The user interface of ECMS is built on a card-based visual design pattern emphasizing clarity, high contrast, and rapid touch navigation. Key UI standards include:</p>")
    h.append("<ul>")
    h.append("  <li><strong>Consistent Header & Navigation:</strong> Displays the logged-in user profile, active senior resident selector, persistent SOS trigger, and role-appropriate navigational links.</li>")
    h.append("  <li><strong>Status Indication Badges:</strong> Distinct high-contrast badges for clinical metrics (Normal: <code>#10B981</code> green, Warning: <code>#F59E0B</code> amber, Critical Anomaly: <code>#EF4444</code> red).</li>")
    h.append("  <li><strong>Modal Windows:</strong> Destructive and life-critical actions (e.g., medication omission, appointment cancellation, SOS triggering) require explicit confirmation dialogs with clear 'Confirm' and 'Cancel' buttons.</li>")
    h.append("  <li><strong>Senior-Optimized Interface:</strong> Senior dashboards eliminate nested menus, presenting single-tap cards for 'Today's Medicine', 'My Doctor', and a prominent 80px high 'EMERGENCY SOS' button.</li>")
    h.append("</ul>")
    
    h.append("<h2>3.2 Hardware Interfaces</h2>")
    h.append("<ul>")
    h.append("  <li><strong>Touchscreen Tablets & Smartphones:</strong> Responsive capacitive touch support for tap, long-press (2-second SOS hold), and scroll gestures.</li>")
    h.append("  <li><strong>Audio Output Hardware:</strong> Interfaces with device sound cards and internal speakers via the Web Audio API to produce an 85+ dB emergency warning siren during distress escalation.</li>")
    h.append("  <li><strong>GPS Telemetry Receivers:</strong> Interfaces with hardware GPS sensors via the HTML5 Geolocation API to harvest coordinates during emergency SOS dispatches.</li>")
    h.append("</ul>")
    
    h.append("<h2>3.3 Software Interfaces</h2>")
    h.append("<ul>")
    h.append("  <li><strong>Database Engine (MySQL 8.0):</strong> Communicates via TCP/IP on port 3306 using PHP PDO with strict transaction isolation (READ COMMITTED).</li>")
    h.append("  <li><strong>Twilio REST SMS Gateway:</strong> Communicates over outbound HTTPS POST requests with JSON payloads to send urgent SMS alerts to mobile telephone networks.</li>")
    h.append("  <li><strong>Leaflet.js / OpenStreetMap Service:</strong> Interfaces with open-source tile servers over HTTPS to render interactive emergency incident location pins.</li>")
    h.append("  <li><strong>Web Audio API:</strong> Standard W3C browser audio engine generating multi-frequency synthesized siren tones locally on client devices without requiring external audio file downloads.</li>")
    h.append("</ul>")
    
    h.append("<h2>3.4 Communications Interfaces</h2>")
    h.append("<ul>")
    h.append("  <li><strong>HTTPS / TLS 1.3:</strong> All web traffic between client browsers and the ECMS web server must be encrypted using Transport Layer Security (TLS 1.3) with modern cipher suites.</li>")
    h.append("  <li><strong>RESTful JSON Protocol:</strong> Asynchronous data communications (AJAX) utilize standard HTTP methods (GET, POST, PUT, DELETE) with <code>application/json</code> content-type headers.</li>")
    h.append("  <li><strong>SMTP / TLS:</strong> Outbound email summaries and appointment reminders are routed through standard SMTP over port 587 with STARTTLS encryption.</li>")
    h.append("</ul>")
    h.append("</div>")
    
    # ---------------- SECTION 4: DOMAIN MODEL ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>4. Domain Model</h1>")
    h.append("<p>The domain model defines the core conceptual entities, their attributes, operations, and interrelationships within the geriatric care management domain. The central entity is the <strong>Senior Resident</strong>, whose care ecosystem is supported by family guardians, clinical caregivers, and attending physicians.</p>")
    h.append("<h3>Core Domain Entities:</h3>")
    h.append("<ol>")
    h.append("  <li><strong>User:</strong> Base actor entity encapsulating <code>user_id</code>, <code>email</code>, <code>password_hash</code>, <code>role</code> (Admin, Guardian, Caregiver, Doctor, Senior), <code>phone</code>, <code>status</code>, and <code>created_at</code>.</li>")
    h.append("  <li><strong>Senior:</strong> Represents the care recipient, capturing <code>senior_id</code>, <code>mrn_number</code>, <code>full_name</code>, <code>dob</code>, <code>gender</code>, <code>blood_group</code>, <code>allergies</code>, <code>chronic_conditions</code>, <code>room_number</code>, and <code>guardian_id</code>.</li>")
    h.append("  <li><strong>Medication:</strong> Master pharmaceutical drug definition containing <code>med_id</code>, <code>generic_name</code>, <code>brand_name</code>, <code>dosage_form</code>, <code>strength</code>, and <code>contraindications</code>.</li>")
    h.append("  <li><strong>MedicationSchedule:</strong> Recurring regimen entry storing <code>schedule_id</code>, <code>senior_id</code>, <code>med_id</code>, <code>frequency</code>, <code>scheduled_time</code>, <code>meal_relation</code>, <code>start_date</code>, and <code>end_date</code>.</li>")
    h.append("  <li><strong>MedicationLog:</strong> Permanent administration record tracking <code>log_id</code>, <code>schedule_id</code>, <code>administered_at</code>, <code>status</code> (Given, Missed, Refused), <code>reason</code>, <code>caregiver_id</code>, and <code>signature_pin</code>.</li>")
    h.append("  <li><strong>VitalSign:</strong> Longitudinal physiological telemetry storing <code>vital_id</code>, <code>senior_id</code>, <code>recorded_at</code>, <code>systolic_bp</code>, <code>diastolic_bp</code>, <code>pulse_rate</code>, <code>spo2</code>, <code>temperature</code>, <code>glucose</code>, <code>caregiver_id</code>, and <code>is_anomaly</code>.</li>")
    h.append("  <li><strong>Appointment:</strong> Medical consultation booking containing <code>appointment_id</code>, <code>senior_id</code>, <code>doctor_id</code>, <code>scheduled_at</code>, <code>consultation_type</code> (In-Person, Teleconsult), <code>status</code>, and <code>notes</code>.</li>")
    h.append("  <li><strong>EmergencyAlert:</strong> Incident management record tracking <code>alert_id</code>, <code>senior_id</code>, <code>triggered_at</code>, <code>trigger_source</code>, <code>latitude</code>, <code>longitude</code>, <code>status</code> (Triggered, Responding, Resolved), and <code>resolved_by</code>.</li>")
    h.append("  <li><strong>ShiftNote:</strong> Shift handover continuity report tracking <code>shift_id</code>, <code>caregiver_id</code>, <code>shift_type</code>, <code>handover_to</code>, <code>progress_notes</code>, <code>overdue_tasks</code>, and <code>signed_at</code>.</li>")
    h.append("  <li><strong>AuditTrail:</strong> Immutable security record capturing <code>audit_id</code>, <code>user_id</code>, <code>action</code>, <code>entity_affected</code>, <code>ip_address</code>, and <code>timestamp</code>.</li>")
    h.append("</ol>")
    if fig5_b64:
        h.append("<div class=\"figure-box\">")
        h.append(f"  <img src=\"{fig5_b64}\" alt=\"Entity Relationship Diagram\">")
        h.append("  <div class=\"figure-caption\">Figure 3: Conceptual Domain Entity-Relationship Diagram (ERD)</div>")
        h.append("</div>")
    h.append("</div>")
    
    # ---------------- SECTION 5: USE CASES ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>5. System Features (Use Cases)</h1>")
    h.append("<p>This section documents the eight (8) core system features of ECMS in exhaustive, structured IEEE Std 830 use case specifications. Each use case details operational triggers, preconditions, paired basic flows, alternate flows, sub-flows, business rules, non-functional constraints, and screen entry exception tables.</p>")
    
    for uc in USE_CASES:
        h.append("<div class=\"use-case-card\">")
        h.append(f"<h2>{uc['num']} {uc['title']}</h2>")
        h.append(f"<p><strong>Brief Description:</strong> {uc['brief_description']}</p>")
        h.append(f"<p><strong>Business Trigger:</strong> {uc['business_trigger']}</p>")
        h.append(f"<p><strong>Preconditions:</strong> {uc['preconditions']}</p>")
        h.append(f"<p><strong>Basic Flow:</strong> (<em>Assumptions: {uc['assumptions']}</em>)</p>")
        
        # Basic Flow Table
        h.append("<table>")
        h.append("  <thead><tr><th style=\"width:8%;\">Line</th><th style=\"width:46%;\">System Actor Action</th><th style=\"width:46%;\">System Response</th></tr></thead>")
        h.append("  <tbody>")
        for step in uc['basic_flow']:
            h.append(f"    <tr><td style=\"text-align:center;\"><strong>{step[0]}</strong></td><td>{step[1]}</td><td>{step[2]}</td></tr>")
        h.append("  </tbody>")
        h.append("</table>")
        h.append(f"<p><strong>Post Condition:</strong> {uc['post_condition']}</p>")
        
        # Alternate Flows
        for af in uc['alternate_flows']:
            h.append(f"<h3>Alternate Flow ({af['name']})</h3>")
            h.append(f"<p><em>{af['condition']}</em></p>")
            h.append("<table>")
            h.append("  <thead><tr><th style=\"width:8%;\">Line</th><th style=\"width:46%;\">System Actor Action</th><th style=\"width:46%;\">System Response</th></tr></thead>")
            h.append("  <tbody>")
            for step in af['steps']:
                h.append(f"    <tr><td style=\"text-align:center;\"><strong>{step[0]}</strong></td><td>{step[1]}</td><td>{step[2]}</td></tr>")
            h.append("  </tbody>")
            h.append("</table>")
            h.append(f"<p><em>{af['restart']}</em></p>")
            h.append(f"<p><strong>Post Condition:</strong> {af['post_condition']}</p>")
            
        # Sub-Flows
        if 'sub_flows' in uc and uc['sub_flows']:
            for sf in uc['sub_flows']:
                h.append(f"<h3>Sub-Flow: {sf['name']}</h3>")
                h.append("<table>")
                h.append("  <thead><tr><th style=\"width:8%;\">Line</th><th style=\"width:46%;\">System Actor Action</th><th style=\"width:46%;\">System Response</th></tr></thead>")
                h.append("  <tbody>")
                for step in sf['steps']:
                    h.append(f"    <tr><td style=\"text-align:center;\"><strong>{step[0]}</strong></td><td>{step[1]}</td><td>{step[2]}</td></tr>")
                h.append("  </tbody>")
                h.append("</table>")
                h.append(f"<p><em>{sf['return_statement']}</em></p>")
                
        # Business Rules
        h.append("<h4>Business Rules:</h4>")
        h.append("<ul>")
        for br in uc['business_rules']:
            h.append(f"  <li>{br}</li>")
        h.append("</ul>")
        
        # NFRs
        h.append("<h4>Non-Functional Requirements:</h4>")
        h.append("<ul>")
        for nfr in uc['nfr']:
            h.append(f"  <li>{nfr}</li>")
        h.append("</ul>")
        
        # Data Requirements
        h.append("<h4>Data Requirements:</h4>")
        h.append("<ul>")
        for dr in uc['data_requirements']:
            h.append(f"  <li>{dr}</li>")
        h.append("</ul>")
        
        # Screen Entry Exception Table
        h.append("<h4>Screen Entry Exception Table:</h4>")
        h.append("<table>")
        h.append("  <thead><tr><th style=\"width:25%;\">Field</th><th style=\"width:35%;\">Constraint</th><th style=\"width:40%;\">Response</th></tr></thead>")
        h.append("  <tbody>")
        for exc in uc['exceptions']:
            h.append(f"    <tr><td><strong>{exc[0]}</strong></td><td>{exc[1]}</td><td>{exc[2]}</td></tr>")
        h.append("  </tbody>")
        h.append("</table>")
        h.append("</div>") # End use-case-card
        
    h.append("</div>") # End Section 5
    
    # ---------------- SECTION 6: OTHER NFRs ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>6. Other Nonfunctional Requirements</h1>")
    h.append("<h2>6.1 Performance Requirements</h2>")
    h.append("<ul>")
    h.append("  <li><strong>Response Time:</strong> Standard user interface pages must load and render completely within 1.2 seconds over a standard 4G/broadband connection.</li>")
    h.append("  <li><strong>API Latency:</strong> Asynchronous REST endpoints (e.g., vitals logging, dose status recording) must return JSON responses within 350 milliseconds under standard load.</li>")
    h.append("  <li><strong>Concurrent Throughput:</strong> The server infrastructure must support at least 250 active concurrent user sessions without performance degradation (CPU utilization &lt; 70%).</li>")
    h.append("  <li><strong>Database Query Execution:</strong> 95% of database queries must execute in under 80 milliseconds, facilitated by indexed foreign keys and normalized schemas.</li>")
    h.append("  <li><strong>Availability:</strong> The system must maintain an operational availability of 99.9% (less than 8.7 hours of unplanned downtime per calendar year).</li>")
    h.append("</ul>")
    
    h.append("<h2>6.2 Safety Requirements</h2>")
    h.append("<ul>")
    h.append("  <li><strong>Clinical Contraindication Detection:</strong> The medication scheduling engine must validate newly entered prescriptions against active drug profiles to prevent hazardous drug-drug interactions.</li>")
    h.append("  <li><strong>Emergency Redundancy:</strong> SOS alerts must broadcast across multiple redundant channels simultaneously: client browser audio sirens, real-time dashboard banners, SMS messages to family guardians, and backup SMS messages to attending doctors.</li>")
    h.append("  <li><strong>Immutable Audit Integrity:</strong> Medication administration records, vital sign entries, and emergency alerts cannot be permanently deleted; corrections must be preserved as historical addenda with caregiver identification.</li>")
    h.append("</ul>")
    
    h.append("<h2>6.3 Security Requirements</h2>")
    h.append("<ul>")
    h.append("  <li><strong>Password Storage & Cryptography:</strong> All passwords must be salted and hashed using Bcrypt with a work factor of at least 12.</li>")
    h.append("  <li><strong>SQL Injection Prevention:</strong> All SQL interactions must be executed via PHP Data Objects (PDO) using prepared statements with bound parameters.</li>")
    h.append("  <li><strong>Session Protection:</strong> Authenticated user sessions must enforce 256-bit cryptographically secure session IDs transmitted via HTTP-only, Secure, SameSite=Strict cookies. Sessions must automatically expire after 15 minutes of user inactivity.</li>")
    h.append("  <li><strong>Cross-Site Request Forgery (CSRF):</strong> All state-changing POST/PUT requests must validate a synchronized CSRF token stored in the user's session.</li>")
    h.append("  <li><strong>Role-Based Authorization (RBAC):</strong> Server-side route middleware must verify user role permissions prior to executing any controller action, rejecting unauthorized access with an HTTP 403 Forbidden status.</li>")
    h.append("</ul>")
    
    h.append("<h2>6.4 Software Quality Attributes</h2>")
    h.append("<ul>")
    h.append("  <li><strong>Usability:</strong> The interface must achieve a System Usability Scale (SUS) score of at least 85, verified through user testing with elderly seniors and geriatric care nurses.</li>")
    h.append("  <li><strong>Reliability:</strong> Mean Time Between Failures (MTBF) must exceed 720 operating hours. In the event of network disruption, the frontend client must cache pending entries locally and re-sync upon reconnection.</li>")
    h.append("  <li><strong>Maintainability:</strong> Codebase structured in a clean Model-View-Controller (MVC) architectural pattern with comprehensive inline docstrings and separation of concerns.</li>")
    h.append("  <li><strong>Portability:</strong> Fully standards-compliant across all modern web browsers (Chrome, Edge, Firefox, Safari) without requiring platform-specific plugins.</li>")
    h.append("</ul>")
    h.append("</div>")
    
    # ---------------- SECTION 7: OTHER REQUIREMENTS ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>7. Other Requirements</h1>")
    h.append("<h2>7.1 Database Requirements</h2>")
    h.append("<ul>")
    h.append("  <li>Schema designed in strict 3rd Normal Form (3NF) to prevent data redundancy and anomalies.</li>")
    h.append("  <li>InnoDB storage engine utilizing transactional integrity (ACID compliance) and foreign key cascade rules.</li>")
    h.append("  <li>Automated daily cryptographic backup of the complete database with a 30-day retention schedule.</li>")
    h.append("</ul>")
    
    h.append("<h2>7.2 Internationalization & Localization Requirements</h2>")
    h.append("<ul>")
    h.append("  <li>Fully bilingual architecture supporting both English and Bengali (বাংলা) user interfaces.</li>")
    h.append("  <li>Date and time formatting adhering to Bangladeshi standard formats (DD/MM/YYYY and 12-hour AM/PM notation).</li>")
    h.append("  <li>E.164 phone number formatting supporting standard 11-digit Bangladeshi mobile networks (<code>+8801XXXXXXXXX</code>).</li>")
    h.append("</ul>")
    
    h.append("<h2>7.3 Legal, Regulatory & Data Privacy Requirements</h2>")
    h.append("<ul>")
    h.append("  <li>Full compliance with the Bangladesh Digital Security Act and international healthcare data privacy principles (HIPAA / GDPR benchmarks).</li>")
    h.append("  <li>Explicit patient/guardian consent workflows for data processing and emergency telecommunications contact sharing.</li>")
    h.append("  <li>Role-segregated data access ensuring financial guardians cannot alter medical prescriptions and clinical doctors cannot view billing financial data.</li>")
    h.append("</ul>")
    
    h.append("<h2>7.4 Software Reuse & Architectural Extensibility</h2>")
    h.append("<ul>")
    h.append("  <li>Modular RESTful API architecture facilitating future integration with commercial electronic medical record (EMR) systems and IoT biometric hardware.</li>")
    h.append("  <li>Extensible notification service allowing seamless addition of WhatsApp Business API or push notification adapters.</li>")
    h.append("</ul>")
    h.append("</div>")
    
    # ---------------- APPENDIX A: GLOSSARY ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>Appendix A: Glossary</h1>")
    h.append("<table>")
    h.append("  <thead><tr><th style=\"width:20%;\">Term</th><th style=\"width:80%;\">Description</th></tr></thead>")
    h.append("  <tbody>")
    for row in GLOSSARY:
        h.append(f"    <tr><td><strong>{row[0]}</strong></td><td>{row[1]}</td></tr>")
    h.append("  </tbody>")
    h.append("</table>")
    h.append("</div>")
    
    # ---------------- APPENDIX B: ANALYSIS MODELS ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>Appendix B: Analysis Models</h1>")
    h.append("<p>This appendix incorporates formal software engineering analysis models visualizing the functional decomposition, data flow, and structural relationships of the Elderly Care Management System.</p>")
    h.append("<h2>B.1 Context Diagram (Level 0 DFD)</h2>")
    h.append("<p>Depicts the boundary of ECMS in relation to external entities: Administrator, Guardian, Caregiver, Doctor, Senior Resident, Twilio SMS Gateway, and SMTP Email Server.</p>")
    if fig_context_b64:
        h.append("<div class=\"figure-box\">")
        h.append(f"  <img src=\"{fig_context_b64}\" alt=\"Context Diagram (Level 0 DFD)\">")
        h.append("  <div class=\"figure-caption\">Figure 4: Context Diagram (Level 0 DFD) of ECMS</div>")
        h.append("</div>")
    h.append("<h2>B.2 Level 1 Data Flow Diagram (DFD)</h2>")
    h.append("<p>Visualizes the decomposition of ECMS into core sub-processes:</p>")
    h.append("<ul>")
    h.append("  <li>1.0 User Authentication & Session Authorization</li>")
    h.append("  <li>2.0 Senior Resident Profile & Clinical Records Management</li>")
    h.append("  <li>3.0 Medication Scheduling & Administration Engine</li>")
    h.append("  <li>4.0 Real-Time Physiological Vitals Telemetry</li>")
    h.append("  <li>5.0 Medical Appointments & Teleconsultation Scheduling</li>")
    h.append("  <li>6.0 Emergency SOS Incident Dispatch & Siren Escalation</li>")
    h.append("  <li>7.0 Caregiver Shift Handoff & Clinical Progress Reporting</li>")
    h.append("</ul>")
    if fig6_b64:
        h.append("<div class=\"figure-box\">")
        h.append(f"  <img src=\"{fig6_b64}\" alt=\"Data Flow Diagram\">")
        h.append("  <div class=\"figure-caption\">Figure 5: Level 1 Data Flow Diagram (DFD) of ECMS</div>")
        h.append("</div>")
        
    h.append("<h2>B.3 Entity-Relationship Diagram (ERD)</h2>")
    h.append("<p>Captures the relational data structure of ECMS across 10 tables (<code>users</code>, <code>seniors</code>, <code>medications</code>, <code>medication_schedules</code>, <code>medication_logs</code>, <code>vitals</code>, <code>appointments</code>, <code>emergency_alerts</code>, <code>shift_notes</code>, <code>audit_logs</code>).</p>")
    h.append("<h2>B.4 State Machine Transition Models</h2>")
    h.append("<ol>")
    h.append("  <li><strong>Medication Schedule State:</strong> <code>Scheduled</code> &rarr; <code>Pending</code> &rarr; <code>Administered (Given)</code> OR <code>Missed</code> OR <code>Refused</code>.</li>")
    h.append("  <li><strong>Emergency SOS Incident State:</strong> <code>Triggered</code> &rarr; <code>5-sec Countdown</code> &rarr; <code>Dispatched/Broadcasting</code> &rarr; <code>Caregiver Responding</code> &rarr; <code>Resolved</code>.</li>")
    h.append("</ol>")
    h.append("</div>")
    
    # ---------------- APPENDIX C: INTERFACE EXAMPLES ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>Appendix C: Interface Examples</h1>")
    h.append("<h2>EXAMPLE 1: Caregiver Operations Dashboard (Screen Layout with Callouts)</h2>")
    h.append("<p>The primary operational workstation for duty caregivers, featuring real-time clinical telemetry, scheduled medication queues, and persistent emergency triggers.</p>")
    fig12_b64 = get_base64_image(os.path.join(BASE_DIR, "figures_png", "fig12_dashboard_callouts.png"))
    if fig12_b64:
        h.append("<div class=\"figure-box\">")
        h.append(f"  <img src=\"{fig12_b64}\" alt=\"Caregiver Operations Dashboard Layout\">")
        h.append("  <div class=\"figure-caption\">Figure 6: Caregiver Operations Dashboard Layout with Callouts (1) to (7)</div>")
        h.append("</div>")
    
    callouts = [
        ["Resident Selector (1)", "Dropdown element allowing the caregiver to toggle between assigned senior residents in their care unit."],
        ["Active Emergency Banner (2)", "High-contrast dynamic red banner flashing during active SOS incidents, displaying resident name and room number."],
        ["Vitals Telemetry Cards (3)", "Real-time cards displaying latest Blood Pressure, Heart Rate, SpO2, and Blood Glucose with color-coded norm badges."],
        ["Medication Schedule Timetable (4)", "Chronological timetable detailing upcoming, due, and overdue medications for the current shift window."],
        ["Administration Action Buttons (5)", "One-click interactive buttons allowing the nurse to record dose status: 'Given' (green), 'Missed' (amber), 'Refused' (red)."],
        ["Shift Handoff Quick Notes (6)", "Interactive text panel for logging ongoing observational progress notes and flagging items for incoming staff."],
        ["Prominent Emergency SOS Trigger (7)", "Persistent 80px high red emergency distress button triggering the multi-channel siren and escalation sequence."]
    ]
    h.append("<table>")
    h.append("  <thead><tr><th style=\"width:30%;\">Callout Number</th><th style=\"width:70%;\">Description</th></tr></thead>")
    h.append("  <tbody>")
    for c in callouts:
        h.append(f"    <tr><td><strong>{c[0]}</strong></td><td>{c[1]}</td></tr>")
    h.append("  </tbody>")
    h.append("</table>")
    
    h.append("<h2>EXAMPLE 2: Medication Administration Record Entry Screen (Field Constraints Table)</h2>")
    h.append("<p>Form field constraints for the medication intake logging screen, matching the industry specification format:</p>")
    
    field_specs = [
        ["Resident Full Name", "Not editable text field. Auto-filled from active resident session."],
        ["Medical Record Number (MRN)", "Not editable alphanumeric label. Auto-filled from database."],
        ["Medication Name", "Not editable text field. Pre-selected from active prescription schedule."],
        ["Prescribed Dosage & Unit", "Not editable text field. Auto-filled (e.g., '10 mg Tablet')."],
        ["Scheduled Administration Time", "Not editable time field. Auto-filled (e.g., '08:00 AM')."],
        ["Actual Administration Timestamp", "Editable datetime field. Auto-filled with current system time. Mask: YYYY-MM-DD HH:MM:SS."],
        ["Administration Status", "Editable dropdown selection. Options: 'Given', 'Missed', 'Refused'. Mandatory field."],
        ["Reason for Exception / Omission", "Editable text field. Max 255 symbols. Mandatory if status is 'Missed' or 'Refused'."],
        ["Administering Caregiver", "Not editable text field. Auto-filled with authenticated caregiver name."],
        ["Caregiver Verification PIN", "Editable password field. Exactly 4 numeric digits. Masked entry for clinical non-repudiation."],
        ["Clinical Observation Notes", "Editable textarea. Max 1,000 symbols. Letters, digits, and clinical punctuation allowed."]
    ]
    h.append("<table>")
    h.append("  <thead><tr><th style=\"width:30%;\">Field</th><th style=\"width:70%;\">Description</th></tr></thead>")
    h.append("  <tbody>")
    for f in field_specs:
        h.append(f"    <tr><td><strong>{f[0]}</strong></td><td>{f[1]}</td></tr>")
    h.append("  </tbody>")
    h.append("</table>")
    h.append("</div>")
    
    # ---------------- APPENDIX D: TBD LIST ----------------
    h.append("<div class=\"section-divider\">")
    h.append("<h1>Appendix D: To Be Determined (TBD) List</h1>")
    h.append("<p>This section records architectural enhancements, third-party integrations, and advanced capabilities scheduled for Phase 2 and Phase 3 development iterations:</p>")
    h.append("<table>")
    h.append("  <thead><tr><th style=\"width:15%;\">Item ID</th><th style=\"width:25%;\">Feature Title</th><th style=\"width:45%;\">Detailed Description</th><th style=\"width:15%;\">Target Milestone</th></tr></thead>")
    h.append("  <tbody>")
    for tbd in TBD_LIST:
        h.append(f"    <tr><td><strong>{tbd[0]}</strong></td><td><strong>{tbd[1]}</strong></td><td>{tbd[2]}</td><td>{tbd[3]}</td></tr>")
    h.append("  </tbody>")
    h.append("</table>")
    h.append("</div>")
    
    h.append("</body>")
    h.append("</html>")
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write("\n".join(h))
    print(f"Generated HTML: {html_path}")

# -------------------------------------------------------------
# 3. COMPILE PDF VIA HEADLESS CHROME
# -------------------------------------------------------------
def compile_pdf(html_path, pdf_path):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    file_url = f"file:///{os.path.abspath(html_path).replace(os.sep, '/')}"
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--virtual-time-budget=7000",
        "--no-pdf-header-footer",
        f"--print-to-pdf={os.path.abspath(pdf_path)}",
        file_url
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        if os.path.exists(pdf_path):
            size = os.path.getsize(pdf_path)
            print(f"Created PDF: {os.path.basename(pdf_path)} ({size:,} bytes)")
        else:
            print(f"Failed to generate {os.path.basename(pdf_path)}: {res.stderr}")
    except Exception as e:
        print(f"Error compiling {pdf_path}: {e}")

# -------------------------------------------------------------
# 4. GENERATE DOCX VIA python-docx
# -------------------------------------------------------------
def set_cell_margins_docx(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_background_docx(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders_docx(table, color="CCCCCC", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def add_heading_docx(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    h.paragraph_format.keep_with_next = True
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(5)
    for run in h.runs:
        run.font.name = 'Arial'
        if level == 1:
            run.font.size = Pt(15)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
        elif level == 2:
            run.font.size = Pt(12)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
        elif level == 3:
            run.font.size = Pt(10.5)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
    return h

def add_p_docx(doc, text="", bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.bold = True
        r_b.font.name = 'Arial'
        r_b.font.size = Pt(9.5)
        r_b.font.color.rgb = RGBColor(0, 0, 0)
    if text:
        r = p.add_run(text)
        r.italic = italic
        r.font.name = 'Arial'
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_bullet_docx(doc, text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.bold = True
        r_b.font.name = 'Arial'
        r_b.font.size = Pt(9.5)
        r_b.font.color.rgb = RGBColor(0, 0, 0)
    r = p.add_run(text)
    r.font.name = 'Arial'
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_table_docx(doc, headers, data, col_widths=None):
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders_docx(table, color="B0B0B0", sz="4")
    
    # Header row
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        set_cell_background_docx(hdr_cells[i], "EEEEEE")
        set_cell_margins_docx(hdr_cells[i], top=100, bottom=100, left=130, right=130)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.name = 'Arial'
            run.font.size = Pt(9)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
            
    # Data rows
    for r_idx, row in enumerate(data):
        row_cells = table.rows[r_idx + 1].cells
        bg_col = "FFFFFF" if r_idx % 2 == 0 else "F9F9F9"
        for c_idx, val in enumerate(row):
            row_cells[c_idx].text = str(val)
            set_cell_background_docx(row_cells[c_idx], bg_col)
            set_cell_margins_docx(row_cells[c_idx], top=80, bottom=80, left=130, right=130)
            p = row_cells[c_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.name = 'Arial'
                run.font.size = Pt(8.5)
                run.font.color.rgb = RGBColor(0, 0, 0)
                
    # Column widths
    if col_widths:
        for row in table.rows:
            for idx, w in enumerate(col_widths):
                row.cells[idx].width = Inches(w)
                
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return table

def add_image_docx(doc, img_path, caption, width_in=5.6):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(3)
        run = p_img.add_run()
        run.add_picture(img_path, width=Inches(width_in))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(8)
        r_c = p_cap.add_run(caption)
        r_c.font.name = 'Arial'
        r_c.font.size = Pt(9)
        r_c.font.bold = True
        r_c.font.color.rgb = RGBColor(0, 0, 0)

def generate_docx(docx_path):
    doc = Document()
    
    # Set standard margins (1 inch)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
    # Page 1: Cover Page
    logo_path = os.path.join(BASE_DIR, "iub_logo.png")
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(20)
        p_logo.paragraph_format.space_after = Pt(20)
        run_logo = p_logo.add_run()
        run_logo.add_picture(logo_path, width=Inches(2.5))
        
    p_t = doc.add_paragraph()
    p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t.paragraph_format.space_after = Pt(4)
    r_t1 = p_t.add_run(f"{METADATA['doc_title']}\n")
    r_t1.bold = True
    r_t1.font.size = Pt(16)
    r_t1.font.name = 'Arial'
    r_t1.font.color.rgb = RGBColor(0, 0, 0)
    
    r_t2 = p_t.add_run(f"{METADATA['project_title']}\n")
    r_t2.bold = True
    r_t2.font.size = Pt(18)
    r_t2.font.name = 'Arial'
    r_t2.font.color.rgb = RGBColor(0, 0, 0)
    
    r_t3 = p_t.add_run(f"{METADATA['version']} | Status: {METADATA['status']}\n")
    r_t3.italic = True
    r_t3.font.size = Pt(11)
    r_t3.font.name = 'Arial'
    r_t3.font.color.rgb = RGBColor(80, 80, 80)
    
    r_t4 = p_t.add_run("Industry Specification Standard IEEE Std 830-1998 Compliant")
    r_t4.font.size = Pt(9.5)
    r_t4.font.name = 'Arial'
    r_t4.font.color.rgb = RGBColor(100, 100, 100)
    
    p_prep = doc.add_paragraph()
    p_prep.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_prep.paragraph_format.space_before = Pt(36)
    p_prep.paragraph_format.space_after = Pt(4)
    r_prep = p_prep.add_run("Prepared by:\n")
    r_prep.bold = True
    r_prep.font.size = Pt(10.5)
    r_prep.font.name = 'Arial'
    r_name = p_prep.add_run(f"{METADATA['author_name']}\n")
    r_name.bold = True
    r_name.font.size = Pt(12.5)
    r_name.font.name = 'Arial'
    r_role = p_prep.add_run(f"{METADATA['author_role']}\nStudent ID: {METADATA['student_id']}\n{METADATA['course']}")
    r_role.font.size = Pt(10.5)
    r_role.font.name = 'Arial'
    
    p_sup = doc.add_paragraph()
    p_sup.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sup.paragraph_format.space_before = Pt(24)
    p_sup.paragraph_format.space_after = Pt(4)
    r_sup1 = p_sup.add_run("Supervised by:\n")
    r_sup1.bold = True
    r_sup1.font.size = Pt(10.5)
    r_sup1.font.name = 'Arial'
    r_sup2 = p_sup.add_run(f"{METADATA['instructor']}")
    r_sup2.bold = True
    r_sup2.font.size = Pt(11)
    r_sup2.font.name = 'Arial'
    
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(36)
    r_inst1 = p_inst.add_run("Department of Computer Science and Engineering\n")
    r_inst1.bold = True
    r_inst1.font.size = Pt(11)
    r_inst1.font.name = 'Arial'
    r_inst2 = p_inst.add_run(f"{METADATA['organization']}\n{METADATA['date']}")
    r_inst2.font.size = Pt(10.5)
    r_inst2.font.name = 'Arial'
    
    doc.add_page_break()
    
    # Page 2: Table of Contents
    add_heading_docx(doc, "Table of Contents", level=1)
    toc_text = [
        "1. Introduction",
        "   1.1 Purpose", "   1.2 Document Conventions", "   1.3 Intended Audience and Reading Suggestions", "   1.4 Product Scope", "   1.5 References",
        "2. Overall Description",
        "   2.1 Product Perspective", "   2.2 Product Functions", "   2.3 User Classes and Characteristics", "   2.4 Operating Environment", "   2.5 Design and Implementation Constraints", "   2.6 User Documentation", "   2.7 Assumptions and Dependencies",
        "3. External Interface Requirements",
        "   3.1 User Interfaces", "   3.2 Hardware Interfaces", "   3.3 Software Interfaces", "   3.4 Communications Interfaces",
        "4. Domain Model",
        "5. System Features (Use Cases)",
        "   5.1 Use Case UC-01: User Authentication & Role-Based Access Control",
        "   5.2 Use Case UC-02: Senior Resident Profile & Health Record Setup",
        "   5.3 Use Case UC-03: Medication Regimen Scheduling & Automated Pill Reminders",
        "   5.4 Use Case UC-04: Daily Caregiving & Medication Administration Logging",
        "   5.5 Use Case UC-05: Real-Time Vitals Tracking & Physiological Anomaly Alerting",
        "   5.6 Use Case UC-06: Doctor Appointment Scheduling & Clinical Teleconsultation Booking",
        "   5.7 Use Case UC-07: Emergency SOS Alert Dispatch & Incident Escalation Workflow",
        "   5.8 Use Case UC-08: Caregiver Shift Handoff & Clinical Progress Notes",
        "6. Other Nonfunctional Requirements",
        "   6.1 Performance Requirements", "   6.2 Safety Requirements", "   6.3 Security Requirements", "   6.4 Software Quality Attributes",
        "7. Other Requirements",
        "   7.1 Database Requirements", "   7.2 Internationalization & Localization Requirements", "   7.3 Legal, Regulatory & Data Privacy Requirements", "   7.4 Software Reuse & Architectural Extensibility",
        "Appendix A: Glossary",
        "Appendix B: Analysis Models",
        "Appendix C: Interface Examples",
        "Appendix D: To Be Determined (TBD) List"
    ]
    for item in toc_text:
        add_p_docx(doc, item)
        
    doc.add_page_break()
    
    # Page 3: Revision History
    add_heading_docx(doc, "Revision History", level=1)
    rev_headers = ["Name", "Date", "Reason For Changes", "Version", "Date of Approval"]
    add_table_docx(doc, rev_headers, REVISION_HISTORY, [1.5, 1.2, 2.5, 0.8, 1.2])
    
    doc.add_page_break()
    
    # Section 1: Introduction
    add_heading_docx(doc, "1. Introduction", level=1)
    add_heading_docx(doc, "1.1 Purpose", level=2)
    add_p_docx(doc, "This Software Requirements Specification (SRS) document defines the complete functional and non-functional requirements for Version 1.0 (Final Release) of the Elderly Care Management System (ECMS). This specification establishes a binding contract between project stakeholders—including institutional geriatric administrators, family guardians, caregiving personnel, clinical physicians, and software engineering teams. The scope of this document encompasses all core subsystems: User Authentication & Role-Based Access Control (RBAC), Senior Resident Health Profile Management, Medication Regimen Scheduling & Adherence Tracking, Real-Time Vitals Telemetry & Physiological Anomaly Detection, Doctor Appointment Coordination, Multi-Channel Emergency SOS Alert Escalation, and Caregiver Shift Handoff Documentation.")
    
    add_heading_docx(doc, "1.2 Document Conventions", level=2)
    add_p_docx(doc, "This document strictly adheres to the IEEE Std 830-1998 Recommended Practice for Software Requirements Specifications. In accordance with academic and institutional submission guidelines:")
    add_bullet_docx(doc, "Formatted in strict Black & White typography to maximize legibility and ensure professional publication standards without distracting decorative borders or excessive coloration.", bold_prefix="Typography & Aesthetics: ")
    add_bullet_docx(doc, "Requirements are uniquely tagged using standardized alphanumeric prefixes (e.g., UC-XX for Use Cases, BR-XX for Business Rules, NFR-XX for Non-Functional Requirements, and DR-XX for Data Requirements).", bold_prefix="Requirement Identification: ")
    add_bullet_docx(doc, "System features are classified according to MoSCoW prioritization (Must Have, Should Have, Could Have, and Won't Have for this release).", bold_prefix="Priority Classifications: ")
    
    add_heading_docx(doc, "1.3 Intended Audience and Reading Suggestions", level=2)
    add_p_docx(doc, "This document addresses five primary stakeholder categories, each requiring specific perspectives when reviewing the specification:")
    add_table_docx(doc, ["ID", "Stakeholder", "Description"], INTENDED_AUDIENCE, [0.8, 1.8, 4.4])
    
    add_heading_docx(doc, "1.4 Product Scope", level=2)
    add_p_docx(doc, "The Elderly Care Management System (ECMS) is a dedicated healthcare coordination web application engineered to address the critical challenges of geriatric care: uncoordinated paper logs, dangerous medication omissions, delayed emergency responses, and lack of family oversight. Key objectives include:")
    add_bullet_docx(doc, "Eliminating medication administration errors through scheduled dose reminders and mandatory caregiver verification.")
    add_bullet_docx(doc, "Providing instant multi-channel emergency SOS alerting with audible sirens, SMS broadcasts, and GPS positioning.")
    add_bullet_docx(doc, "Enabling real-time physiological telemetry monitoring with automatic anomaly detection for hypertensive crisis or hypoxia.")
    add_bullet_docx(doc, "Establishing comprehensive clinical continuity across nursing shifts via structured electronic progress notes.")
    add_bullet_docx(doc, "Delivering an accessible, high-contrast user interface tailored specifically to the visual and motor capabilities of elderly seniors (WCAG 2.1 AA compliant).")
    
    add_heading_docx(doc, "1.5 References", level=2)
    refs = [
        "IEEE Computer Society, IEEE Std 830-1998: IEEE Recommended Practice for Software Requirements Specifications, IEEE, New York, 1998.",
        "World Wide Web Consortium (W3C), Web Content Accessibility Guidelines (WCAG) 2.1, W3C Recommendation, 2018.",
        "World Health Organization (WHO), Integrated Care for Older People (ICOPE): Guidance for Person-Centred Assessment and Pathways in Primary Care, WHO, Geneva, 2019.",
        "Health Level Seven International, HL7 FHIR Release 4.0.1: Fast Healthcare Interoperability Resources, HL7, 2019.",
        "PHP Group, PHP 8.2 Documentation & Secure PDO Guidelines, 2024.",
        "Twilio Inc., Twilio REST API Documentation for Programmable SMS & Voice, 2024."
    ]
    for r in refs:
        add_bullet_docx(doc, r)
        
    doc.add_page_break()
    
    # Section 2: Overall Description
    add_heading_docx(doc, "2. Overall Description", level=1)
    add_heading_docx(doc, "2.1 Product Perspective", level=2)
    add_p_docx(doc, "The Elderly Care Management System (ECMS) is a newly designed, self-contained web platform developed as an integrated solution for institutional care homes and assisted home care environments. It replaces fragmented, error-prone manual paper charts, unencrypted messaging groups, and uncoordinated telephone calls. ECMS operates as a centralized web application built on the LAMP (Linux, Apache, MySQL, PHP) architecture, integrating with external telecommunication SMS gateways, browser Web Audio APIs, and geolocation mapping services.")
    add_p_docx(doc, "The system is architected into three distinct functional tiers:")
    add_bullet_docx(doc, "Responsive HTML5/CSS3/JavaScript frontend tailored with accessible WCAG 2.1 AA standards, large touch controls, and high-contrast visuals.", bold_prefix="1. Presentation Tier: ")
    add_bullet_docx(doc, "Modular PHP backend implementing MVC patterns, authentication middleware, business rule validators, and REST API controllers.", bold_prefix="2. Application Logic Tier: ")
    add_bullet_docx(doc, "Relational MySQL 8.0 database engine operating in 3rd Normal Form (3NF) with InnoDB ACID transactions, foreign key constraints, and encrypted medical records.", bold_prefix="3. Persistence Tier: ")
    add_image_docx(doc, os.path.join(BASE_DIR, "figures_png", "fig3_system_architecture.png"), "Figure 1: Multi-Tier Architectural Perspective of ECMS")
    
    add_heading_docx(doc, "2.2 Product Functions", level=2)
    add_p_docx(doc, "The major functional capabilities provided by the Elderly Care Management System comprise:")
    add_bullet_docx(doc, "Centralized management of senior demographics, blood groups, chronic ailments, drug allergies, and primary emergency contacts.", bold_prefix="Resident Profile & Clinical History: ")
    add_bullet_docx(doc, "Prescribing, recurring daily scheduling, automated visual/audio alarms, and timestamped caregiver administration logging (Given, Missed, Refused).", bold_prefix="Medication Administration Record (MAR): ")
    add_bullet_docx(doc, "Tracking Blood Pressure, Pulse, Blood Oxygen (SpO2), Temperature, and Blood Glucose, with automatic anomaly detection triggers.", bold_prefix="Vitals Telemetry & Anomaly Alerting: ")
    add_bullet_docx(doc, "Calendar slot reservations, concurrency lock management, and automated SMS clinical reminders.", bold_prefix="Doctor Appointment & Teleconsultation Scheduling: ")
    add_bullet_docx(doc, "One-touch distress trigger with a 5-second false-alarm countdown, automated multi-channel siren broadcast, SMS dispatch, and incident audit tracking.", bold_prefix="Emergency SOS Incident Management: ")
    add_bullet_docx(doc, "Structured electronic handoff notes compiling completed care tasks, overdue items, and clinical progress notes between duty shifts.", bold_prefix="Caregiver Shift Handoff: ")
    add_image_docx(doc, os.path.join(BASE_DIR, "figures_png", "fig2_proposed_system.png"), "Figure 2: Top-Level Functional Workflow of ECMS")
    
    add_heading_docx(doc, "2.3 User Classes and Characteristics", level=2)
    add_p_docx(doc, "The system supports five distinct user classes with varying privileges and operational technical proficiencies:")
    add_table_docx(doc, ["ID", "User Class", "Description"], USER_CLASSES, [0.8, 1.8, 4.4])
    
    add_heading_docx(doc, "2.4 Operating Environment", level=2)
    add_bullet_docx(doc, "Standard desktop/laptop personal computers, tablets (Apple iPad, Samsung Galaxy Tab with minimum 1024x768 resolution), and smartphones (iOS 14+, Android 10+).", bold_prefix="Client Hardware: ")
    add_bullet_docx(doc, "Modern evergreen web browsers supporting HTML5, CSS Grid, ES6 JavaScript, Web Audio API, and TLS 1.3 (Google Chrome 110+, Mozilla Firefox 110+, Apple Safari 16+, Microsoft Edge 110+).", bold_prefix="Client Browsers: ")
    add_bullet_docx(doc, "Apache HTTP Server 2.4+ / Nginx on Ubuntu Linux 22.04 LTS / Windows Server, running PHP 8.2+ with PDO, OpenSSL, and cURL extensions.", bold_prefix="Server Environment: ")
    add_bullet_docx(doc, "MySQL Community Server 8.0+ or MariaDB 10.6+ utilizing the InnoDB storage engine with UTF-8 (utf8mb4) character collation.", bold_prefix="Database Server: ")
    add_bullet_docx(doc, "Minimum 3G mobile data or broadband connection (bandwidth >= 1.0 Mbps; latency < 150ms).", bold_prefix="Network Connectivity: ")
    
    add_heading_docx(doc, "2.5 Design and Implementation Constraints", level=2)
    add_bullet_docx(doc, "The user interface for senior residents must feature a minimum font size of 16px, a contrast ratio of at least 4.5:1, and touch targets of at least 44x44 pixels.", bold_prefix="1. Accessibility Standards (WCAG 2.1 AA): ")
    add_bullet_docx(doc, "Built using native HTML5, Vanilla CSS3, JavaScript, PHP, and MySQL without proprietary framework lock-ins.", bold_prefix="2. Core Technology Stack: ")
    add_bullet_docx(doc, "All database queries executed via PHP Data Objects (PDO) with parameterized prepared statements. Passwords hashed using Bcrypt (cost factor >= 12).", bold_prefix="3. Security Standards: ")
    add_bullet_docx(doc, "Interfaces must dynamically adapt across viewport widths from 360px to 1920px without horizontal scrollbars.", bold_prefix="4. Responsive Layouts: ")
    
    add_heading_docx(doc, "2.6 User Documentation", level=2)
    add_bullet_docx(doc, "A laminated 2-page pocket guide detailing vitals logging, dose administration, and shift handoff workflows.", bold_prefix="Caregiver Quick-Start Operational Card (PDF): ")
    add_bullet_docx(doc, "A simplified visual booklet with large iconography explaining daily schedules and SOS alert triggers.", bold_prefix="Senior Resident Visual Guide: ")
    add_bullet_docx(doc, "Technical documentation covering LAMP installation, cron setup, database backups, and security configurations.", bold_prefix="Administrator Deployment & Maintenance Guide: ")
    
    add_heading_docx(doc, "2.7 Assumptions and Dependencies", level=2)
    add_bullet_docx(doc, "Users have access to compatible browser devices and basic internet connectivity. Caregivers possess basic mobile touch literacy. Guardians provide accurate clinical baseline data.", bold_prefix="Assumptions: ")
    add_bullet_docx(doc, "Continuous uptime of external telecommunications SMS gateways (Twilio API); operational SMTP mail servers; and browser permission access to Geolocation and Web Audio subsystems.", bold_prefix="Dependencies: ")
    
    doc.add_page_break()
    
    # Section 3: External Interfaces
    add_heading_docx(doc, "3. External Interface Requirements", level=1)
    add_heading_docx(doc, "3.1 User Interfaces", level=2)
    add_bullet_docx(doc, "Displays user profile, active senior selector, persistent SOS trigger, and role-appropriate links.", bold_prefix="Consistent Header & Navigation: ")
    add_bullet_docx(doc, "Distinct high-contrast badges (Normal: green, Warning: amber, Critical Anomaly: red).", bold_prefix="Status Indication Badges: ")
    add_bullet_docx(doc, "Destructive and life-critical actions require explicit confirmation dialogs with clear 'Confirm' and 'Cancel' options.", bold_prefix="Modal Windows: ")
    add_bullet_docx(doc, "Presents single-tap cards for 'Today's Medicine', 'My Doctor', and an 80px high 'EMERGENCY SOS' button.", bold_prefix="Senior-Optimized Interface: ")
    
    add_heading_docx(doc, "3.2 Hardware Interfaces", level=2)
    add_bullet_docx(doc, "Capacitive touch support for tap, long-press (2-second SOS hold), and scroll gestures.", bold_prefix="Touchscreen Tablets & Smartphones: ")
    add_bullet_docx(doc, "Interfaces with device speakers via Web Audio API to produce an 85+ dB emergency warning siren.", bold_prefix="Audio Output Hardware: ")
    add_bullet_docx(doc, "Interfaces with hardware GPS sensors via HTML5 Geolocation API to harvest coordinates during emergency SOS dispatches.", bold_prefix="GPS Telemetry Receivers: ")
    
    add_heading_docx(doc, "3.3 Software Interfaces", level=2)
    add_bullet_docx(doc, "TCP/IP on port 3306 using PHP PDO with strict transaction isolation (READ COMMITTED).", bold_prefix="Database Engine (MySQL 8.0): ")
    add_bullet_docx(doc, "HTTPS POST requests with JSON payloads to dispatch urgent SMS alerts to mobile telephone networks.", bold_prefix="Twilio REST SMS Gateway: ")
    add_bullet_docx(doc, "Interfaces with open-source tile servers over HTTPS to render interactive emergency incident location pins.", bold_prefix="Leaflet.js / OpenStreetMap Service: ")
    add_bullet_docx(doc, "Synthesizes multi-frequency siren audio locally on client devices without requiring external audio file downloads.", bold_prefix="Web Audio API: ")
    
    add_heading_docx(doc, "3.4 Communications Interfaces", level=2)
    add_bullet_docx(doc, "All traffic encrypted using TLS 1.3 with modern cipher suites.", bold_prefix="HTTPS / TLS 1.3: ")
    add_bullet_docx(doc, "Asynchronous data communications (AJAX) utilize standard HTTP methods (GET, POST, PUT, DELETE) with application/json headers.", bold_prefix="RESTful JSON Protocol: ")
    add_bullet_docx(doc, "Outbound email summaries and appointment reminders routed through standard SMTP over port 587 with STARTTLS encryption.", bold_prefix="SMTP / TLS: ")
    
    doc.add_page_break()
    
    # Section 4: Domain Model
    add_heading_docx(doc, "4. Domain Model", level=1)
    add_p_docx(doc, "The domain model defines the core conceptual entities, their attributes, operations, and interrelationships within the geriatric care management domain. The central entity is the Senior Resident, whose care ecosystem is supported by family guardians, clinical caregivers, and attending physicians.")
    domain_entities = [
        "Base actor entity encapsulating user_id, email, password_hash, role (Admin, Guardian, Caregiver, Doctor, Senior), phone, status, and created_at.",
        "Represents the care recipient, capturing senior_id, mrn_number, full_name, dob, gender, blood_group, allergies, chronic_conditions, room_number, and guardian_id.",
        "Master pharmaceutical drug definition containing med_id, generic_name, brand_name, dosage_form, strength, and contraindications.",
        "Recurring regimen entry storing schedule_id, senior_id, med_id, frequency, scheduled_time, meal_relation, start_date, and end_date.",
        "Permanent administration record tracking log_id, schedule_id, administered_at, status (Given, Missed, Refused), reason, caregiver_id, and signature_pin.",
        "Longitudinal physiological telemetry storing vital_id, senior_id, recorded_at, systolic_bp, diastolic_bp, pulse_rate, spo2, temperature, glucose, caregiver_id, and is_anomaly.",
        "Medical consultation booking containing appointment_id, senior_id, doctor_id, scheduled_at, consultation_type (In-Person, Teleconsult), status, and notes.",
        "Incident management record tracking alert_id, senior_id, triggered_at, trigger_source, latitude, longitude, status (Triggered, Responding, Resolved), and resolved_by.",
        "Shift handover continuity report tracking shift_id, caregiver_id, shift_type, handover_to, progress_notes, overdue_tasks, and signed_at.",
        "Immutable security record capturing audit_id, user_id, action, entity_affected, ip_address, and timestamp."
    ]
    entity_names = ["1. User: ", "2. Senior: ", "3. Medication: ", "4. MedicationSchedule: ", "5. MedicationLog: ", "6. VitalSign: ", "7. Appointment: ", "8. EmergencyAlert: ", "9. ShiftNote: ", "10. AuditTrail: "]
    for name, desc in zip(entity_names, domain_entities):
        add_bullet_docx(doc, desc, bold_prefix=name)
        
    add_image_docx(doc, os.path.join(BASE_DIR, "figures_png", "fig5_er_diagram.png"), "Figure 3: Conceptual Domain Entity-Relationship Diagram (ERD)")
    
    doc.add_page_break()
    
    # Section 5: Detailed Use Cases
    add_heading_docx(doc, "5. System Features (Use Cases)", level=1)
    add_p_docx(doc, "This section documents the eight (8) core system features of ECMS in exhaustive, structured IEEE Std 830 use case specifications. Each use case details operational triggers, preconditions, paired basic flows, alternate flows, sub-flows, business rules, non-functional constraints, and screen entry exception tables.")
    
    for uc in USE_CASES:
        add_heading_docx(doc, f"{uc['num']} {uc['title']}", level=2)
        add_p_docx(doc, uc['brief_description'], bold_prefix="Brief Description: ")
        add_p_docx(doc, uc['business_trigger'], bold_prefix="Business Trigger: ")
        add_p_docx(doc, uc['preconditions'], bold_prefix="Preconditions: ")
        add_p_docx(doc, f"Assumptions: {uc['assumptions']}", bold_prefix="Basic Flow: ", italic=True)
        
        # Basic flow table
        add_table_docx(doc, ["Line", "System Actor Action", "System Response"], uc['basic_flow'], [0.8, 3.1, 3.1])
        add_p_docx(doc, uc['post_condition'], bold_prefix="Post Condition: ")
        
        # Alternate Flows
        for af in uc['alternate_flows']:
            add_heading_docx(doc, f"Alternate Flow ({af['name']})", level=3)
            add_p_docx(doc, af['condition'], italic=True)
            add_table_docx(doc, ["Line", "System Actor Action", "System Response"], af['steps'], [0.8, 3.1, 3.1])
            add_p_docx(doc, af['restart'], italic=True)
            add_p_docx(doc, af['post_condition'], bold_prefix="Post Condition: ")
            
        # Sub-Flows
        if 'sub_flows' in uc and uc['sub_flows']:
            for sf in uc['sub_flows']:
                add_heading_docx(doc, f"Sub-Flow: {sf['name']}", level=3)
                add_table_docx(doc, ["Line", "System Actor Action", "System Response"], sf['steps'], [0.8, 3.1, 3.1])
                add_p_docx(doc, sf['return_statement'], italic=True)
                
        # Business Rules
        add_heading_docx(doc, "Business Rules:", level=3)
        for br in uc['business_rules']:
            add_bullet_docx(doc, br)
            
        # NFRs
        add_heading_docx(doc, "Non-Functional Requirements:", level=3)
        for nfr in uc['nfr']:
            add_bullet_docx(doc, nfr)
            
        # Data Requirements
        add_heading_docx(doc, "Data Requirements:", level=3)
        for dr in uc['data_requirements']:
            add_bullet_docx(doc, dr)
            
        # Screen Entry Exception Table
        add_heading_docx(doc, "Screen Entry Exception Table:", level=3)
        add_table_docx(doc, ["Field", "Constraint", "Response"], uc['exceptions'], [2.0, 2.5, 2.5])
        doc.add_paragraph().paragraph_format.space_after = Pt(8)
        
    doc.add_page_break()
    
    # Section 6: Other Nonfunctional Requirements
    add_heading_docx(doc, "6. Other Nonfunctional Requirements", level=1)
    add_heading_docx(doc, "6.1 Performance Requirements", level=2)
    add_bullet_docx(doc, "Standard user interface pages must load and render completely within 1.2 seconds over a standard 4G/broadband connection.", bold_prefix="Response Time: ")
    add_bullet_docx(doc, "Asynchronous REST endpoints (e.g., vitals logging, dose status recording) must return JSON responses within 350 milliseconds under standard load.", bold_prefix="API Latency: ")
    add_bullet_docx(doc, "The server infrastructure must support at least 250 active concurrent user sessions without performance degradation (CPU utilization < 70%).", bold_prefix="Concurrent Throughput: ")
    add_bullet_docx(doc, "95% of database queries must execute in under 80 milliseconds, facilitated by indexed foreign keys and normalized schemas.", bold_prefix="Database Query Execution: ")
    add_bullet_docx(doc, "The system must maintain an operational availability of 99.9% (less than 8.7 hours of unplanned downtime per calendar year).", bold_prefix="Availability: ")
    
    add_heading_docx(doc, "6.2 Safety Requirements", level=2)
    add_bullet_docx(doc, "The medication scheduling engine must validate newly entered prescriptions against active drug profiles to prevent hazardous drug-drug interactions.", bold_prefix="Clinical Contraindication Detection: ")
    add_bullet_docx(doc, "SOS alerts must broadcast across multiple redundant channels simultaneously: client browser audio sirens, real-time dashboard banners, SMS messages to family guardians, and backup SMS messages to attending doctors.", bold_prefix="Emergency Redundancy: ")
    add_bullet_docx(doc, "Medication administration records, vital sign entries, and emergency alerts cannot be permanently deleted; corrections must be preserved as historical addenda with caregiver identification.", bold_prefix="Immutable Audit Integrity: ")
    
    add_heading_docx(doc, "6.3 Security Requirements", level=2)
    add_bullet_docx(doc, "All passwords must be salted and hashed using Bcrypt with a work factor of at least 12.", bold_prefix="Password Storage & Cryptography: ")
    add_bullet_docx(doc, "All SQL interactions must be executed via PHP Data Objects (PDO) using prepared statements with bound parameters.", bold_prefix="SQL Injection Prevention: ")
    add_bullet_docx(doc, "Authenticated user sessions must enforce 256-bit cryptographically secure session IDs transmitted via HTTP-only, Secure, SameSite=Strict cookies. Sessions must automatically expire after 15 minutes of user inactivity.", bold_prefix="Session Protection: ")
    add_bullet_docx(doc, "All state-changing POST/PUT requests must validate a synchronized CSRF token stored in the user's session.", bold_prefix="Cross-Site Request Forgery (CSRF): ")
    add_bullet_docx(doc, "Server-side route middleware must verify user role permissions prior to executing any controller action, rejecting unauthorized access with an HTTP 403 Forbidden status.", bold_prefix="Role-Based Authorization (RBAC): ")
    
    add_heading_docx(doc, "6.4 Software Quality Attributes", level=2)
    add_bullet_docx(doc, "The interface must achieve a System Usability Scale (SUS) score of at least 85, verified through user testing with elderly seniors and geriatric care nurses.", bold_prefix="Usability: ")
    add_bullet_docx(doc, "Mean Time Between Failures (MTBF) must exceed 720 operating hours. In the event of network disruption, the frontend client must cache pending entries locally and re-sync upon reconnection.", bold_prefix="Reliability: ")
    add_bullet_docx(doc, "Codebase structured in a clean Model-View-Controller (MVC) architectural pattern with comprehensive inline docstrings and separation of concerns.", bold_prefix="Maintainability: ")
    add_bullet_docx(doc, "Fully standards-compliant across all modern web browsers (Chrome, Edge, Firefox, Safari) without requiring platform-specific plugins.", bold_prefix="Portability: ")
    
    doc.add_page_break()
    
    # Section 7: Other Requirements
    add_heading_docx(doc, "7. Other Requirements", level=1)
    add_heading_docx(doc, "7.1 Database Requirements", level=2)
    add_bullet_docx(doc, "Schema designed in strict 3rd Normal Form (3NF) to prevent data redundancy and anomalies.")
    add_bullet_docx(doc, "InnoDB storage engine utilizing transactional integrity (ACID compliance) and foreign key cascade rules.")
    add_bullet_docx(doc, "Automated daily cryptographic backup of the complete database with a 30-day retention schedule.")
    
    add_heading_docx(doc, "7.2 Internationalization & Localization Requirements", level=2)
    add_bullet_docx(doc, "Fully bilingual architecture supporting both English and Bengali (বাংলা) user interfaces.")
    add_bullet_docx(doc, "Date and time formatting adhering to Bangladeshi standard formats (DD/MM/YYYY and 12-hour AM/PM notation).")
    add_bullet_docx(doc, "E.164 phone number formatting supporting standard 11-digit Bangladeshi mobile networks (+8801XXXXXXXXX).")
    
    add_heading_docx(doc, "7.3 Legal, Regulatory & Data Privacy Requirements", level=2)
    add_bullet_docx(doc, "Full compliance with the Bangladesh Digital Security Act and international healthcare data privacy principles (HIPAA / GDPR benchmarks).")
    add_bullet_docx(doc, "Explicit patient/guardian consent workflows for data processing and emergency telecommunications contact sharing.")
    add_bullet_docx(doc, "Role-segregated data access ensuring financial guardians cannot alter medical prescriptions and clinical doctors cannot view billing financial data.")
    
    add_heading_docx(doc, "7.4 Software Reuse & Architectural Extensibility", level=2)
    add_bullet_docx(doc, "Modular RESTful API architecture facilitating future integration with commercial electronic medical record (EMR) systems and IoT biometric hardware.")
    add_bullet_docx(doc, "Extensible notification service allowing seamless addition of WhatsApp Business API or push notification adapters.")
    
    doc.add_page_break()
    
    # Appendices
    add_heading_docx(doc, "Appendix A: Glossary", level=1)
    add_table_docx(doc, ["Term", "Description"], GLOSSARY, [1.5, 5.5])
    
    doc.add_page_break()
    add_heading_docx(doc, "Appendix B: Analysis Models", level=1)
    add_heading_docx(doc, "B.1 Context Diagram (Level 0 DFD)", level=2)
    add_p_docx(doc, "Depicts the boundary of ECMS in relation to external entities: Administrator, Guardian, Caregiver, Doctor, Senior Resident, Twilio SMS Gateway, and SMTP Email Server.")
    add_image_docx(doc, os.path.join(BASE_DIR, "figures_png", "fig_context_diagram.png"), "Figure 4: Context Diagram (Level 0 DFD) of ECMS")
    add_heading_docx(doc, "B.2 Level 1 Data Flow Diagram (DFD)", level=2)
    add_p_docx(doc, "Visualizes the decomposition of ECMS into core sub-processes:")
    add_bullet_docx(doc, "1.0 User Authentication & Session Authorization")
    add_bullet_docx(doc, "2.0 Senior Resident Profile & Clinical Records Management")
    add_bullet_docx(doc, "3.0 Medication Scheduling & Administration Engine")
    add_bullet_docx(doc, "4.0 Real-Time Physiological Vitals Telemetry")
    add_bullet_docx(doc, "5.0 Medical Appointments & Teleconsultation Scheduling")
    add_bullet_docx(doc, "6.0 Emergency SOS Incident Dispatch & Siren Escalation")
    add_bullet_docx(doc, "7.0 Caregiver Shift Handoff & Clinical Progress Reporting")
    add_image_docx(doc, os.path.join(BASE_DIR, "figures_png", "fig6_data_flow_diagram.png"), "Figure 5: Level 1 Data Flow Diagram (DFD) of ECMS")
    
    add_heading_docx(doc, "B.3 Entity-Relationship Diagram (ERD)", level=2)
    add_p_docx(doc, "Captures the relational data structure of ECMS across 10 tables (users, seniors, medications, medication_schedules, medication_logs, vitals, appointments, emergency_alerts, shift_notes, audit_logs).")
    add_heading_docx(doc, "B.4 State Machine Transition Models", level=2)
    add_bullet_docx(doc, "Scheduled -> Pending -> Administered (Given) OR Missed OR Refused.", bold_prefix="1. Medication Schedule State: ")
    add_bullet_docx(doc, "Triggered -> 5-sec Countdown -> Dispatched/Broadcasting -> Caregiver Responding -> Resolved.", bold_prefix="2. Emergency SOS Incident State: ")
    
    doc.add_page_break()
    add_heading_docx(doc, "Appendix C: Interface Examples", level=1)
    add_heading_docx(doc, "EXAMPLE 1: Caregiver Operations Dashboard (Screen Layout with Callouts)", level=2)
    add_p_docx(doc, "The primary operational workstation for duty caregivers, featuring real-time clinical telemetry, scheduled medication queues, and persistent emergency triggers.")
    add_image_docx(doc, os.path.join(BASE_DIR, "figures_png", "fig12_dashboard_callouts.png"), "Figure 6: Caregiver Operations Dashboard Layout with Callouts (1) to (7)")
    callouts_data = [
        ["Resident Selector (1)", "Dropdown element allowing the caregiver to toggle between assigned senior residents in their care unit."],
        ["Active Emergency Banner (2)", "High-contrast dynamic red banner flashing during active SOS incidents, displaying resident name and room number."],
        ["Vitals Telemetry Cards (3)", "Real-time cards displaying latest Blood Pressure, Heart Rate, SpO2, and Blood Glucose with color-coded norm badges."],
        ["Medication Schedule Timetable (4)", "Chronological timetable detailing upcoming, due, and overdue medications for the current shift window."],
        ["Administration Action Buttons (5)", "One-click interactive buttons allowing the nurse to record dose status: 'Given' (green), 'Missed' (amber), 'Refused' (red)."],
        ["Shift Handoff Quick Notes (6)", "Interactive text panel for logging ongoing observational progress notes and flagging items for incoming staff."],
        ["Prominent Emergency SOS Trigger (7)", "Persistent 80px high red emergency distress button triggering the multi-channel siren and escalation sequence."]
    ]
    add_table_docx(doc, ["Callout Number", "Description"], callouts_data, [2.2, 4.8])
    
    add_heading_docx(doc, "EXAMPLE 2: Medication Administration Record Entry Screen (Field Constraints Table)", level=2)
    add_p_docx(doc, "Form field constraints for the medication intake logging screen, matching the industry specification format:")
    field_specs_data = [
        ["Resident Full Name", "Not editable text field. Auto-filled from active resident session."],
        ["Medical Record Number (MRN)", "Not editable alphanumeric label. Auto-filled from database."],
        ["Medication Name", "Not editable text field. Pre-selected from active prescription schedule."],
        ["Prescribed Dosage & Unit", "Not editable text field. Auto-filled (e.g., '10 mg Tablet')."],
        ["Scheduled Administration Time", "Not editable time field. Auto-filled (e.g., '08:00 AM')."],
        ["Actual Administration Timestamp", "Editable datetime field. Auto-filled with current system time. Mask: YYYY-MM-DD HH:MM:SS."],
        ["Administration Status", "Editable dropdown selection. Options: 'Given', 'Missed', 'Refused'. Mandatory field."],
        ["Reason for Exception / Omission", "Editable text field. Max 255 symbols. Mandatory if status is 'Missed' or 'Refused'."],
        ["Administering Caregiver", "Not editable text field. Auto-filled with authenticated caregiver name."],
        ["Caregiver Verification PIN", "Editable password field. Exactly 4 numeric digits. Masked entry for clinical non-repudiation."],
        ["Clinical Observation Notes", "Editable textarea. Max 1,000 symbols. Letters, digits, and clinical punctuation allowed."]
    ]
    add_table_docx(doc, ["Field", "Description"], field_specs_data, [2.2, 4.8])
    
    doc.add_page_break()
    add_heading_docx(doc, "Appendix D: To Be Determined (TBD) List", level=1)
    add_p_docx(doc, "This section records architectural enhancements, third-party integrations, and advanced capabilities scheduled for Phase 2 and Phase 3 development iterations:")
    add_table_docx(doc, ["Item ID", "Feature Title", "Detailed Description", "Target Milestone"], TBD_LIST, [1.0, 1.8, 3.2, 1.0])
    
    doc.save(docx_path)
    print(f"Generated DOCX: {docx_path}")

# -------------------------------------------------------------
# MAIN PIPELINE EXECUTION
# -------------------------------------------------------------
def main():
    import shutil
    md_file = os.path.join(BASE_DIR, "Elderly_Care_Management_System_SRS_IEEE_Template.md")
    html_file = os.path.join(BASE_DIR, "Elderly_Care_Management_System_SRS_IEEE_Template.html")
    pdf_file = os.path.join(BASE_DIR, "Elderly_Care_Management_System_SRS_IEEE_Template.pdf")
    docx_file = os.path.join(BASE_DIR, "Elderly_Care_Management_System_SRS_IEEE_Template.docx")
    
    print("Step 1: Generating Markdown document...")
    generate_markdown(md_file)
    
    print("Step 2: Generating HTML document...")
    generate_html(html_file)
    
    print("Step 3: Compiling PDF document via Headless Chrome...")
    compile_pdf(html_file, pdf_file)
    
    print("Step 4: Generating Microsoft Word document (.docx)...")
    generate_docx(docx_file)
    
    # Synchronize primary filenames
    shutil.copyfile(docx_file, os.path.join(BASE_DIR, "Elderly_Care_Management_System_SRS.docx"))
    shutil.copyfile(pdf_file, os.path.join(BASE_DIR, "Software_Requirements_Specification_SRS.pdf"))
    print("Synchronized Elderly_Care_Management_System_SRS.docx and Software_Requirements_Specification_SRS.pdf")
    
    print("\nAll deliverables generated successfully!")

if __name__ == "__main__":
    main()
