# Generate an editable Microsoft Word (.docx) document for Elderly Care Management System SRS
# that can be opened in Microsoft Word or uploaded directly to Google Docs for full editing.

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_background(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, color="CCCCCC", sz="4", val="single"):
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

def add_heading_styled(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    h.paragraph_format.keep_with_next = True
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(6)
    for run in h.runs:
        run.font.name = 'Arial'
        if level == 1:
            run.font.size = Pt(16)
            run.font.bold = True
            run.font.color.rgb = RGBColor(15, 23, 42)
        elif level == 2:
            run.font.size = Pt(13)
            run.font.bold = True
            run.font.color.rgb = RGBColor(15, 118, 110)
        elif level == 3:
            run.font.size = Pt(11.5)
            run.font.bold = True
            run.font.color.rgb = RGBColor(30, 41, 59)
    return h

def add_p(doc, text, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.bold = True
        r_b.font.name = 'Arial'
        r_b.font.size = Pt(10.5)
        r_b.font.color.rgb = RGBColor(17, 24, 39)
    r = p.add_run(text)
    r.italic = italic
    r.font.name = 'Arial'
    r.font.size = Pt(10.5)
    r.font.color.rgb = RGBColor(31, 41, 55)
    return p

def add_bullet(doc, text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.bold = True
        r_b.font.name = 'Arial'
        r_b.font.size = Pt(10.5)
    r = p.add_run(text)
    r.font.name = 'Arial'
    r.font.size = Pt(10.5)
    return p

def add_image_figure(doc, img_path, caption, width_in=6.0):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run = p_img.add_run()
        run.add_picture(img_path, width=Inches(width_in))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(12)
        r_cap = p_cap.add_run(caption)
        r_cap.bold = True
        r_cap.font.name = 'Arial'
        r_cap.font.size = Pt(10)
        r_cap.font.color.rgb = RGBColor(51, 65, 85)

def create_table_from_data(doc, headers, rows, col_widths=None):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table, color="94A3B8", sz="4")
    
    # Header Row
    hdr_cells = table.rows[0].cells
    for i, h_text in enumerate(headers):
        hdr_cells[i].text = h_text
        set_cell_background(hdr_cells[i], "F1F5F9")
        set_cell_margins(hdr_cells[i], top=120, bottom=120, left=150, right=150)
        p = hdr_cells[i].paragraphs[0]
        p.runs[0].font.bold = True
        p.runs[0].font.name = 'Arial'
        p.runs[0].font.size = Pt(9.5)
        p.runs[0].font.color.rgb = RGBColor(15, 23, 42)
    
    # Body Rows
    for r_idx, row_data in enumerate(rows):
        row_cells = table.rows[r_idx + 1].cells
        bg_color = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].text = str(val)
            set_cell_background(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=100, bottom=100, left=150, right=150)
            p = row_cells[c_idx].paragraphs[0]
            if p.runs:
                p.runs[0].font.name = 'Arial'
                p.runs[0].font.size = Pt(9)
                p.runs[0].font.color.rgb = RGBColor(31, 41, 55)

    if col_widths:
        for row in table.rows:
            for i, w in enumerate(col_widths):
                row.cells[i].width = Inches(w)
                
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    return table

def add_use_case_table(doc, uc_name, actors, desc, pre, typical_events, alt_flows, post):
    table = doc.add_table(rows=6, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table, color="94A3B8", sz="4")
    
    labels = ["Use Case Name", "Actors", "Description", "Precondition", "Typical course of events", "Post Condition"]
    values = [
        f"**{uc_name}**",
        actors,
        desc,
        pre,
        "",  # Sub-table placeholder
        post
    ]
    
    for idx, (label, val) in enumerate(zip(labels, values)):
        row = table.rows[idx]
        row.cells[0].width = Inches(1.8)
        row.cells[1].width = Inches(4.7)
        
        row.cells[0].text = label
        set_cell_background(row.cells[0], "F1F5F9")
        set_cell_margins(row.cells[0], top=100, bottom=100, left=140, right=140)
        p_lbl = row.cells[0].paragraphs[0]
        if p_lbl.runs:
            p_lbl.runs[0].font.bold = True
            p_lbl.runs[0].font.name = 'Arial'
            p_lbl.runs[0].font.size = Pt(9.5)
            p_lbl.runs[0].font.color.rgb = RGBColor(15, 23, 42)
            
        set_cell_margins(row.cells[1], top=100, bottom=100, left=140, right=140)
        p_val = row.cells[1].paragraphs[0]
        
        if label == "Typical course of events":
            # Add formatted events
            p_val.text = "Actors Events | System Response"
            p_val.runs[0].font.bold = True
            p_val.runs[0].font.name = 'Arial'
            p_val.runs[0].font.size = Pt(9)
            for act_evt, sys_res in typical_events:
                p_evt = row.cells[1].add_paragraph()
                p_evt.paragraph_format.space_after = Pt(2)
                r1 = p_evt.add_run(f"• User: {act_evt}\n")
                r1.font.name = 'Arial'
                r1.font.size = Pt(8.5)
                r2 = p_evt.add_run(f"  System: {sys_res}")
                r2.font.name = 'Arial'
                r2.font.size = Pt(8.5)
                r2.font.color.rgb = RGBColor(15, 118, 110)
            if alt_flows:
                p_alt = row.cells[1].add_paragraph()
                p_alt.paragraph_format.space_before = Pt(4)
                r_alt_lbl = p_alt.add_run("Alternative Flows:\n")
                r_alt_lbl.bold = True
                r_alt_lbl.font.size = Pt(8.5)
                r_alt = p_alt.add_run(alt_flows)
                r_alt.font.size = Pt(8.5)
                r_alt.font.color.rgb = RGBColor(71, 85, 105)
        else:
            p_val.text = val.replace("**", "")
            if p_val.runs:
                if label == "Use Case Name":
                    p_val.runs[0].font.bold = True
                p_val.runs[0].font.name = 'Arial'
                p_val.runs[0].font.size = Pt(9)
                p_val.runs[0].font.color.rgb = RGBColor(31, 41, 55)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

def main():
    doc = Document()
    
    # Configure 0.8 in margins (matching demo.pdf)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
        
    print("Building cover page...")
    # ================= COVER PAGE =================
    if os.path.exists("iub_logo.png"):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(30)
        p_logo.paragraph_format.space_after = Pt(20)
        run_logo = p_logo.add_run()
        run_logo.add_picture("iub_logo.png", width=Inches(1.8))
        
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(40)
    r_t1 = p_title.add_run("Software Requirements Specification\nfor\n")
    r_t1.font.name = 'Arial'
    r_t1.font.size = Pt(20)
    r_t1.font.bold = True
    r_t2 = p_title.add_run("Elderly Care Management System")
    r_t2.font.name = 'Arial'
    r_t2.font.size = Pt(22)
    r_t2.font.bold = True
    r_t2.font.color.rgb = RGBColor(13, 148, 136)
    
    p_by = doc.add_paragraph()
    p_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_by.paragraph_format.space_after = Pt(30)
    r_by_lbl = p_by.add_run("Prepared By\n")
    r_by_lbl.font.bold = True
    r_by_lbl.font.size = Pt(13)
    r_by = p_by.add_run("Farzana Sadia Takee\n2211175\nCourse Code: CSE309\nCourse Title: Web Application and Internet\nSection: 05\nAutumn 2025")
    r_by.font.size = Pt(11.5)
    r_by.font.color.rgb = RGBColor(51, 65, 85)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub_lbl = p_sub.add_run("Submitted to\n")
    r_sub_lbl.font.bold = True
    r_sub_lbl.font.size = Pt(13)
    r_sub = p_sub.add_run("MS. Shanjita Akter Prome\nAdjunct Faculty\nIndependent University Bangladesh")
    r_sub.font.size = Pt(11.5)
    r_sub.font.color.rgb = RGBColor(51, 65, 85)
    
    doc.add_page_break()

    # ================= TABLE OF CONTENTS =================
    add_heading_styled(doc, "Table of Contents", level=1)
    toc_data = [
        ("Abstract", "4"),
        ("Introduction", "5"),
        ("    1.1 Background", "5"),
        ("    1.2 Motivation", "6"),
        ("    1.3 Problem Statement", "7"),
        ("    1.4 Objective", "8"),
        ("System Overview", "10"),
        ("    2.1 System Users", "10"),
        ("    2.2 System Architecture", "12"),
        ("    2.3 System Modules", "13"),
        ("    2.4 Security and Verification", "15"),
        ("    2.5 Software Development Tools", "16"),
        ("    2.6 Advantages of Using The System", "17"),
        ("System Life Cycle", "18"),
        ("    3.1 Software Development Life Cycle", "18"),
        ("        3.1.1 SDLC Phases", "18"),
        ("Requirement Engineering", "20"),
        ("    4.1 Requirement Elicitation", "20"),
        ("    4.2 Requirement Analysis", "20"),
        ("        4.2.1 Feasibility Study", "20"),
        ("        4.2.2 Requirement Classification", "21"),
        ("        4.2.3 Conflict and Redundancy Resolution", "21"),
        ("    4.3 Requirement Documentation", "22"),
        ("Functional requirements", "23"),
        ("    5.1 Feature List with Description", "23"),
        ("    5.2 Feature Table", "25"),
        ("System Specification Diagrams", "28"),
        ("    6.1 Entity Relationship Diagram", "28"),
        ("    6.3 Data Flow Diagram", "29"),
        ("    6.4 Use Case Diagram", "30"),
        ("        6.4.1 User Management Subsystem", "30"),
        ("        6.4.2 Medication Management Subsystem", "31"),
        ("        6.4.3 Appointment Management Subsystem", "31"),
        ("        6.4.4 Daily Care & Emergency SOS Subsystem", "32"),
        ("    6.5 Use Case Narration Table", "33"),
        ("        6.5.1 User Management Subsystem", "33"),
        ("        6.5.2 Medication Management Subsystem", "37"),
        ("        6.5.3 Appointment Management Subsystem", "40"),
        ("        6.5.4 Daily Care & Emergency SOS Subsystem", "43"),
        ("    6.6 CRUD Matrix", "46"),
        ("    6.7 Activity Table", "47"),
        ("    6.8 Gantt chart", "48"),
        ("Non-Functional Requirements", "49"),
        ("    7.1 Feature List with Description", "49"),
        ("Result Analysis", "51"),
        ("    8.1 SWOT Analysis", "51"),
        ("    8.2 Risk Matrix", "51"),
        ("Conclusion", "52"),
        ("References", "53")
    ]
    for title, page in toc_data:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.space_after = Pt(3)
        r_title = p_t.add_run(title)
        r_title.font.name = 'Arial'
        r_title.font.size = Pt(10)
        if not title.startswith(" "):
            r_title.bold = True
        r_dots = p_t.add_run(" " + "." * max(10, 65 - len(title)*2) + " ")
        r_dots.font.color.rgb = RGBColor(148, 163, 184)
        r_pg = p_t.add_run(page)
        r_pg.font.bold = True
        r_pg.font.size = Pt(10)
        
    doc.add_page_break()

    # ================= ABSTRACT =================
    add_heading_styled(doc, "Abstract", level=1)
    add_p(doc, "The Elderly Care Management System is a Web-based application that automates, streamlines, and centralizes daily eldercare operations and healthcare supervision. Traditionally, elderly care activities—such as medication administration tracking, doctor appointment scheduling, vital sign monitoring, and caregiver shift handoffs—have been managed manually using handwritten paper logs, physical pillboxes, and fragmented telephone communications. Consequently, families and eldercare institutions face significant inefficiencies, frequent medication errors, missed clinical appointments, and potentially fatal delays during sudden medical emergencies.")
    add_p(doc, "The Elderly Care Management System directly resolves these critical vulnerabilities by introducing a unified, multi-role digital ecosystem connecting elderly citizens, family guardians, visiting or residential caregivers, and medical practitioners. By offering real-time medication reminders, single-tap adherence logging, digital prescription archives, structured activities of daily living (ADL) checklists, and instantaneous emergency SOS panic alerting with live GPS broadcast, the platform eliminates human error and provides round-the-clock peace of mind for family guardians.")
    add_p(doc, "Developed using an accessible frontend architecture and a robust, secure relational backend, the system adheres strictly to health data privacy protocols, role-based access control (RBAC), and universal accessibility standards (WCAG 2.1 AA) tailored for senior citizens. This comprehensive Software Requirements Specification (SRS) report establishes the architectural foundation, functional and non-functional specifications, UML behavioral models, relational database schemas, and verification frameworks governing the development and deployment of the platform.")
    doc.add_page_break()

    # ================= INTRODUCTION =================
    add_heading_styled(doc, "Introduction", level=1)
    add_p(doc, "The purpose of the Elderly Care Management System is to automate, digitize, and coordinate home care and health supervision routines for aging seniors. In modern society, shifting socio-demographic structures, the rapid growth of nuclear families, and demanding professional obligations make it increasingly difficult for adult children and family guardians to administer continuous, error-free care for their aging parents manually. The Elderly Care Management System provides an integrated, methodical, web-enabled solution to this pervasive challenge, establishing a consistent and transparent channel for managing geriatric health routines while enhancing safety, speed, accuracy, and overall quality of life.")
    
    add_heading_styled(doc, "1.1 Background", level=2)
    add_p(doc, "Global demographic transitions indicate an unprecedented increase in the senior citizen population. Concurrently, a substantial portion of the elderly demographic experiences chronic conditions such as hypertension, diabetes mellitus, cardiovascular ailments, arthritis, and mild cognitive impairments. Managing these multi-morbidities necessitates complex polypharmacy regimens, regular clinical checkups, continuous physiological vital sign tracking, and assistance with activities of daily living (ADLs).")
    add_p(doc, "In traditional domestic and institutional care environments, care coordination depends on memory, handwritten paper diaries, and manual telephone inquiries. When family members leave for work or reside in distant cities, they remain in a persistent state of anxiety, unable to verify whether their senior relatives took their critical morning cardiovascular medication, consumed balanced meals, or attended their scheduled clinical consultations. Furthermore, professional caregivers working rotating shifts lack standardized handoff documentation, creating hazardous blind spots in patient history. A centralized web application addresses these challenges by consolidating health data into an auditable, real-time platform accessible from any standard web browser.")
    doc.add_page_break()

    # ================= MOTIVATION & PROBLEM STATEMENT =================
    add_heading_styled(doc, "1.2 Motivation", level=2)
    add_p(doc, "Several critical real-world factors motivated the conception and development of the Elderly Care Management System:")
    add_bullet(doc, "As life expectancy expands and nuclear family arrangements become the predominant societal norm, the reliance on structured digital care management systems has grown exponentially.", bold_prefix="1. Growing Geriatric Demographic: ")
    add_bullet(doc, "Polypharmacy omissions, dosage duplications, and adverse drug interactions represent leading causes of preventable emergency geriatric hospital admissions.", bold_prefix="2. Eradication of Medication Errors: ")
    add_bullet(doc, "Visiting caregivers and relatives frequently fail to communicate vital observations during shift changes. A centralized digital handoff log ensures seamless continuity of care.", bold_prefix="3. Caregiver Handoff Continuity: ")
    add_bullet(doc, "In acute episodes like falls or cardiovascular crises, seniors cannot dial numbers. A dedicated, one-touch SOS mechanism dispatching GPS coordinates and medical briefs is vital.", bold_prefix="4. Rapid Emergency Crisis Intervention: ")
    add_bullet(doc, "Physicians routinely encounter patients who cannot recall their past adherence history. Objective longitudinal records improve diagnosis and therapeutic outcomes.", bold_prefix="5. Actionable Clinical Data for Doctors: ")
    
    add_heading_styled(doc, "1.3 Problem Statement", level=2)
    add_p(doc, "Manual systems, physical paper organizers, and informal verbal communications are still the standard methods employed by families and care aides to manage eldercare routines. These outdated administrative workflows result in severe operational challenges, safety risks, and emotional stress, including:")
    add_bullet(doc, "Elderly individuals frequently forget daily prescription doses. Physical pillboxes offer no verification mechanism, leading to dangerous under-dosing or double-dosing.", bold_prefix="1. Medication Mismanagement: ")
    add_bullet(doc, "Working guardians lack real-time visibility into the daily wellbeing of their elderly relatives, causing constant anxiety.", bold_prefix="2. Lack of Real-Time Visibility: ")
    add_bullet(doc, "Caregivers document care on arbitrary paper notebooks or convey them verbally, creating hazardous blind spots.", bold_prefix="3. Unaccountable Shift Handoffs: ")
    add_bullet(doc, "Prescriptions and appointment slips are easily misplaced, causing missed consultations.", bold_prefix="4. Misplaced Records & Appointments: ")
    add_bullet(doc, "When a senior falls, delayed emergency response can cause permanent disability or fatality.", bold_prefix="5. Delayed Crisis Response: ")
    
    add_image_figure(doc, "figures_png/fig1_existing_system.png", "Fig 1: Existing System Rich Picture", width_in=6.2)
    doc.add_page_break()

    # ================= OBJECTIVES & PROPOSED SYSTEM =================
    add_heading_styled(doc, "1.4 Objective", level=2)
    add_p(doc, "The primary objectives of the Elderly Care Management System are:")
    add_bullet(doc, "Provide a unified electronic repository of chronic conditions, blood type, drug allergies, primary physicians, and emergency contacts.", bold_prefix="1. Centralize Senior Health Baseline: ")
    add_bullet(doc, "Eliminate missed or duplicated medications through schedule alerts and single-click logging.", bold_prefix="2. Automate Medication Schedules & Adherence Tracking: ")
    add_bullet(doc, "Maintain scheduled appointments, clinic locations, and digital prescription archives accessible across family members.", bold_prefix="3. Streamline Healthcare Provider Consultations: ")
    add_bullet(doc, "Enable structured task checklists (meals, hydration, physical mobility, vital signs) with timestamped records.", bold_prefix="4. Standardize Daily Care Routines (ADLs): ")
    add_bullet(doc, "Deliver a single-touch panic button that dispatches real-time distress alerts, GPS location, and medical briefs to guardians and paramedics.", bold_prefix="5. Instant Emergency SOS Alerting: ")
    add_bullet(doc, "Protect personal medical records through encrypted storage, hashed authentication, and strict privilege segregation.", bold_prefix="6. Health Data Privacy and Role-Based Protection: ")
    add_bullet(doc, "Produce downloadable analytical charts and summaries for family peace of mind and clinical consultations.", bold_prefix="7. Deliver Longitudinal Wellness Analytics: ")
    
    add_image_figure(doc, "figures_png/fig2_proposed_system.png", "Fig 2: Proposed System Rich Picture", width_in=6.2)
    doc.add_page_break()

    # ================= SYSTEM OVERVIEW & USERS =================
    add_heading_styled(doc, "System Overview", level=1)
    add_p(doc, "The Elderly Care Management System allows families, caregivers, and healthcare professionals to coordinate, monitor, and safeguard geriatric health routines efficiently. In the past, eldercare required heavy manual effort, physical paper record-keeping, and disjointed phone calls that introduced dangerous communication gaps. As a result, critical tasks were frequently overlooked, and emergencies escalated unchecked. The Elderly Care Management System addresses these issues by offering an integrated web application that standardizes schedules, logs daily care, and dispatches instant alerts.")
    
    add_heading_styled(doc, "2.1 System Users", level=2)
    add_p(doc, "The system supports five distinct user classes, each with tailored interfaces and granular operational privileges:")
    add_bullet(doc, "Interacts through a high-contrast, large-font interface optimized for seniors. Can view daily medication alarms, tap single-click dose confirmations, and trigger the prominent Emergency SOS button.", bold_prefix="1. Elderly Senior Citizen: ")
    add_bullet(doc, "The administrative overseer of the care plan. Registers senior profiles, configures medication regimens, schedules doctor consultations, reviews caregiver shift notes, and receives distress SMS alerts.", bold_prefix="2. Family Member / Primary Guardian: ")
    add_bullet(doc, "Certified home nurses or visiting aides. Uses a mobile-optimized shift dashboard to record completed ADL tasks, log measured physiological vitals, and compile digital shift handover reports.", bold_prefix="3. Professional Caregiver: ")
    add_bullet(doc, "Medical specialists and clinic physicians. Securely reviews longitudinal adherence records, vital trends, enters clinical visit notes, and formulates electronic prescriptions.", bold_prefix="4. Healthcare Provider / Doctor: ")
    add_bullet(doc, "Emergency medical personnel responding to distress alerts. Receives read-only access to vital baseline data: blood group, drug allergies, chronic conditions, and guardian phone.", bold_prefix="5. First Responder / Paramedic: ")
    add_bullet(doc, "Technical personnel responsible for maintaining platform integrity, managing credentials, database performance, and security policies.", bold_prefix="6. System Administrator: ")
    doc.add_page_break()

    # ================= ARCHITECTURE & MODULES =================
    add_heading_styled(doc, "2.2 System Architecture", level=2)
    add_p(doc, "The Elderly Care Management System is designed following a modern 3-Tier Layered Architecture, ensuring high maintainability, robust security, scalability, and clean separation of concerns:")
    add_bullet(doc, "The top-level interface through which users interact with the system via web browsers on desktop computers, tablets, or smartphones. Built using HTML5, CSS3, and JavaScript, delivering responsive dashboards with senior-accessible typography and high-contrast themes.", bold_prefix="1. Presentation Layer (Client Tier): ")
    add_bullet(doc, "The middle tier executing core business logic, application routing, and security policies. Developed using PHP 8.2 on an MVC structure, coordinating authentication, scheduling algorithms, caregiver handoffs, and notification dispatching.", bold_prefix="2. Application / Business Logic Layer (Server Tier): ")
    add_bullet(doc, "The persistence layer consisting of a relational MySQL 8.0 database engine. Stores user accounts, senior clinical baselines, medication master lists, scheduled dose logs, doctor appointments, daily care checklists, and emergency SOS audit logs.", bold_prefix="3. Data & Storage Layer (Database Tier): ")
    
    add_image_figure(doc, "figures_png/fig3_system_architecture.png", "Fig 3: System Architecture [5]", width_in=3.6)
    
    add_heading_styled(doc, "2.3 System Modules", level=2)
    add_bullet(doc, "Manages account provisioning, login authentication, password reset, and role assignment (Senior, Guardian, Caregiver, Doctor, Admin).", bold_prefix="Module 1: User & Role-Based Authentication: ")
    add_bullet(doc, "Maintains comprehensive digital profiles for seniors, documenting full names, birth dates, blood types, home addresses, chronic ailments, and drug allergy flags.", bold_prefix="Module 2: Elderly Profile & Health Baseline: ")
    add_bullet(doc, "Enables guardians and doctors to configure medication regimens, specify dosage units, set daily timings, and attach instructions. Generates visual reminders and allows single-click adherence logging.", bold_prefix="Module 3: Medication Management & Adherence Tracker: ")
    add_bullet(doc, "Streamlines the booking, rescheduling, and tracking of specialist consultations and diagnostic tests. Features digital document uploads for doctor prescriptions and laboratory reports.", bold_prefix="Module 4: Doctor Appointment & Clinical History: ")
    add_bullet(doc, "Coordinates non-pharmacological activities of daily living (ADLs) including hygiene, meals, hydration, and mobility, while recording physiological vitals.", bold_prefix="Module 5: Daily Care Tasks & ADL Routine: ")
    add_bullet(doc, "Standardizes the transition between outgoing and incoming care aides with mandatory handover reports documenting completed tasks, vital trends, and patient mood.", bold_prefix="Module 6: Caregiver Shift Handoff & Care Notes: ")
    add_bullet(doc, "Dispatches loud browser alarms, SMS messages, and emails with live GPS coordinates and emergency clinical briefs to guardians and paramedics upon panic button activation.", bold_prefix="Module 7: Emergency SOS Alert & Notification: ")
    add_bullet(doc, "Aggregates care data into visual charts, tracking monthly medication compliance percentages, vital sign stability, and daily task completion.", bold_prefix="Module 8: Family Oversight Dashboard & Reports: ")
    doc.add_page_break()

    # ================= SECURITY & TOOLS & ADVANTAGES =================
    add_heading_styled(doc, "2.4 Security and Verification", level=2)
    add_p(doc, "Given that the Elderly Care Management System processes sensitive personal and clinical data, security is an essential non-negotiable requirement. The system incorporates multi-layered defensive controls:")
    add_bullet(doc, "Passwords encrypted using one-way cryptographic hashing via Argon2id / Bcrypt with dynamic salting. Passwords are never stored in plain text.", bold_prefix="1. Authentication: ")
    add_bullet(doc, "Granular Role-Based Access Control ensures that users can only access endpoints and data authorized for their role.", bold_prefix="2. Authorization & RBAC: ")
    add_bullet(doc, "Authenticated sessions use cryptographically random 128-bit session tokens stored with HttpOnly, SameSite=Strict, and Secure flags.", bold_prefix="3. Session Management: ")
    add_bullet(doc, "All database interactions utilize PHP Data Objects (PDO) with parameterized prepared statements, preventing SQL injection.", bold_prefix="4. Input Validation & SQLi Prevention: ")
    add_bullet(doc, "All communications operate over encrypted HTTPS/TLS 1.3 channels. Critical events are logged in an immutable audit table.", bold_prefix="5. Data Protection & Audit Trail: ")
    
    add_heading_styled(doc, "2.5 Software Development Tools", level=2)
    tools_headers = ["Category", "Tools/Technology", "Description"]
    tools_rows = [
        ["Frontend", "HTML5, CSS3, JavaScript (ES6+)", "Constructs responsive semantic markup, senior-accessible visual styling (WCAG AA), audio alerts, and interactive DOM manipulation."],
        ["Backend", "PHP 8.2", "Implements MVC architecture, RESTful routing, domain business logic, cryptographic hashing, and database communication."],
        ["Database", "MySQL 8.0", "Provides ACID-compliant relational data storage, foreign key enforcement, indexing, and transactional data integrity."],
        ["Server", "Apache / XAMPP", "Hosts local and staging application servers, managing virtual hosts and HTTP request lifecycles."],
        ["Design & Modeling", "Draw.io / Lucidchart", "Used for designing system architecture, ER diagrams, DFD data pipelines, and UML Use Case diagrams."],
        ["Version Control", "Git & GitHub", "Maintains source code versioning, branch management, collaborative tracking, and milestone releases."],
        ["Testing Tools", "PHPUnit, Chrome DevTools", "Executes backend unit testing, API endpoint validation, accessibility checks, and frontend performance profiling."],
        ["Notification Service", "Twilio SMS API / SMTP", "Dispatches real-time SMS distress messages and email alerts for emergency SOS and medication notifications."]
    ]
    create_table_from_data(doc, tools_headers, tools_rows, [1.5, 2.0, 3.2])
    
    add_heading_styled(doc, "2.6 Advantages of Using The System", level=2)
    add_bullet(doc, "Eliminates physical prescription slips, paper notebooks, and unstructured medication logs.", bold_prefix="1. Elimination of Paperwork: ")
    add_bullet(doc, "Synchronized dosage schedules, loud audio-visual reminders, and single-click confirmations eliminate missed doses.", bold_prefix="2. Reduction in Medication Errors: ")
    add_bullet(doc, "Enables family members to view real-time adherence logs and care activities from their workplace or mobile phones.", bold_prefix="3. Transparency for Working Guardians: ")
    add_bullet(doc, "Digital shift handoffs and mandatory vital sign logging ensure visiting staff are held accountable.", bold_prefix="4. Caregiver Accountability: ")
    add_bullet(doc, "One-touch SOS button bypasses complicated smartphone navigation, broadcasting GPS locations and medical briefs within seconds.", bold_prefix="5. Rapid Emergency Crisis Intervention: ")
    add_bullet(doc, "Provides visiting physicians with verified, longitudinal adherence records and physiological trends.", bold_prefix="6. Empirical Data for Consultations: ")
    doc.add_page_break()

    # ================= SDLC & REQUIREMENT ENGINEERING =================
    add_heading_styled(doc, "System Life Cycle", level=1)
    add_heading_styled(doc, "3.1 Software Development Life Cycle", level=2)
    add_p(doc, "The development of the Elderly Care Management System adheres to a structured Waterfall / Iterative SDLC methodology. Because healthcare software directly impacts patient wellbeing and life safety, a systematic, phased engineering approach is required to guarantee clinical accuracy, requirement stability, and rigorous testing before production deployment.")
    
    add_heading_styled(doc, "3.1.1 SDLC Phases", level=3)
    add_bullet(doc, "User requirements elicited through geriatric literature review, family guardian interviews, and clinical safety guidelines.", bold_prefix="1. Requirement Analysis: ")
    add_bullet(doc, "Translates verified requirements into 3-tier architecture, normalized relational schemas (ERD), data flows (DFD), and accessible wireframes.", bold_prefix="2. System Design: ")
    add_bullet(doc, "Modular construction of frontend interfaces (HTML5/CSS3/JS) and backend domain controllers (PHP 8.2, MySQL) following PSR-12 conventions.", bold_prefix="3. Implementation (Coding): ")
    add_bullet(doc, "Unit tests, integration tests across database boundaries, usability testing with senior personas, security audits, and SOS latency simulations.", bold_prefix="4. Testing & Quality Assurance: ")
    add_bullet(doc, "Deploying the verified application onto a production cloud server configured with HTTPS/TLS certificates and automated backup cron jobs.", bold_prefix="5. Deployment & Release: ")
    add_bullet(doc, "Post-release monitoring, server performance tuning, periodic security patch installation, and ongoing feature refinements.", bold_prefix="6. Maintenance & Evolution: ")
    
    add_image_figure(doc, "figures_png/fig4_sdlc_process.png", "Fig 4: SDLC Process Diagram", width_in=4.8)
    
    add_heading_styled(doc, "Requirement Engineering", level=1)
    add_heading_styled(doc, "4.1 Requirement Elicitation", level=2)
    add_p(doc, "Requirement elicitation employed structured interviews with family guardians, clinical documentation reviews of paper charts, and direct observational studies of senior daily routines.")
    
    add_heading_styled(doc, "4.2 Requirement Analysis & Feasibility Study", level=2)
    add_bullet(doc, "Open-source LAMP stack (PHP, MySQL, Apache) is mature, reliable, and capable of sub-second response times without proprietary hardware.", bold_prefix="Technical Feasibility: ")
    add_bullet(doc, "Minimal licensing and infrastructure costs with high return on investment (ROI) in preventable hospitalization reduction.", bold_prefix="Economic Feasibility: ")
    add_bullet(doc, "Senior-friendly high-contrast UI and intuitive single-click interactions ensure rapid adoption.", bold_prefix="Operational Feasibility: ")
    add_bullet(doc, "Structured into modular sprints delivering all functional milestones within the 12-week academic semester.", bold_prefix="Schedule Feasibility: ")
    doc.add_page_break()

    # ================= FUNCTIONAL REQUIREMENTS =================
    add_heading_styled(doc, "Functional requirements", level=1)
    add_heading_styled(doc, "5.1 Feature List with Description", level=2)
    features_desc = [
        ("FR-01: User Account Registration: ", "Allows family guardians, caregivers, and medical practitioners to create new accounts with email verification and role allocation."),
        ("FR-02: Role-Based Authentication: ", "Authenticates registered users based on their assigned role, generating secure session tokens and role-tailored dashboards."),
        ("FR-03: Senior Profile Management: ", "Enables guardians to maintain comprehensive digital profiles including DOB, blood group, drug allergies, primary physician, and home GPS coordinates."),
        ("FR-04: Medication Scheduling: ", "Allows guardians and doctors to configure prescribed medications, dosage amounts, daily timings, and meal instructions."),
        ("FR-05: Real-Time Dose Logging: ", "Provides intuitive controls for seniors or caregivers to mark doses as 'Taken', 'Missed', or 'Skipped' with mandatory omission notes."),
        ("FR-06: Audio-Visual Reminders: ", "Displays prominent visual banners and plays audio chimes 15 minutes prior to scheduled medication times."),
        ("FR-07: Doctor Appointments: ", "Facilitates booking specialist consultations, laboratory tests, and hospital follow-ups with calendar reminders."),
        ("FR-08: Prescription Archive: ", "Provides encrypted cloud storage for uploading scanned doctor prescriptions, blood test results, and discharge summaries."),
        ("FR-09: Daily ADL Checklist: ", "Establishes a daily routine checklist tracking essential non-medical tasks including bathing, oral hygiene, meals, and mobility."),
        ("FR-10: Vitals Recording: ", "Allows caregivers to record blood pressure, pulse rate, blood glucose, and body temperature, flagging abnormal readings in red."),
        ("FR-11: Shift Handoff Notes: ", "Mandates outgoing caregivers to submit an electronic shift handover summary documenting completed tasks, vital trends, and patient mood."),
        ("FR-12: Emergency SOS Trigger: ", "Prominent one-touch panic button that instantly dispatches browser alarms, SMS messages, and emails with live GPS coordinates and clinical briefs."),
        ("FR-13: Family Live Dashboard: ", "Consolidates daily adherence rates, vital trends, and caregiver logs into intuitive visual graphs for working family members."),
        ("FR-14: Audit Trail Logging: ", "Enforces strict input validation and writes immutable audit logs for all data mutations and emergency dispatches.")
    ]
    for b_lbl, desc in features_desc:
        add_bullet(doc, desc, bold_prefix=b_lbl)
        
    add_heading_styled(doc, "5.2 Feature Table", level=2)
    feat_headers = ["Feature ID", "Feature Name", "Description", "Precondition", "Role"]
    feat_rows = [
        ["FR-01", "User Registration", "Register new user accounts with role selection", "Valid email & phone", "All Users"],
        ["FR-02", "Login Authentication", "Verify credentials and initiate secure session", "Active account", "All Users"],
        ["FR-03", "Senior Profile Setup", "Create and manage senior clinical baseline", "Guardian logged in", "Guardian"],
        ["FR-04", "Medication Scheduling", "Configure dosage, timing, and meal rules", "Senior profile exists", "Guardian, Doctor"],
        ["FR-05", "Dose Adherence Logging", "Log dose as Taken, Missed, or Skipped", "Scheduled dose exists", "Senior, Caregiver"],
        ["FR-06", "Dosage Audio Reminders", "Audio chimes and visual alert banners", "Upcoming dosage time", "System, Senior"],
        ["FR-07", "Appointment Scheduling", "Book and track doctor clinical consultations", "Senior profile exists", "Guardian, Doctor"],
        ["FR-08", "Prescription Archive", "Upload and view digital prescription scans", "Appointment / Visit", "Doctor, Guardian"],
        ["FR-09", "Daily ADL Checklist", "Structure and track meals, hygiene, mobility", "Active care plan", "Caregiver, Senior"],
        ["FR-10", "Vitals Logging", "Record BP, pulse, glucose with anomaly flags", "Caregiver on duty", "Caregiver"],
        ["FR-11", "Shift Handoff Notes", "Outgoing caregiver logs shift summary", "End of care shift", "Caregiver, Guardian"],
        ["FR-12", "Emergency SOS Trigger", "One-touch panic button for medical crises", "Any system screen", "Senior, Caregiver"],
        ["FR-13", "Multichannel SOS Alert", "Broadcast SMS, email, and GPS coordinates", "SOS triggered", "System"],
        ["FR-14", "Family Live Dashboard", "Central monitoring of vitals and adherence", "Guardian logged in", "Guardian"],
        ["FR-15", "PDF Compliance Export", "Export monthly health and adherence report", "Adherence data exists", "Guardian, Doctor"],
        ["FR-16", "System Audit Logging", "Log all user operations and mutations", "Action performed", "System, Admin"]
    ]
    create_table_from_data(doc, feat_headers, feat_rows, [1.1, 1.6, 2.2, 1.2, 1.1])
    doc.add_page_break()

    # ================= SYSTEM SPECIFICATION DIAGRAMS =================
    add_heading_styled(doc, "System Specification Diagrams", level=1)
    add_heading_styled(doc, "6.1 Entity Relationship Diagram", level=2)
    add_p(doc, "The Entity Relationship Diagram (ERD) defines the relational database architecture supporting the Elderly Care Management System. The schema is fully normalized to Third Normal Form (3NF), ensuring data integrity, elimination of update anomalies, and efficient indexing across primary and foreign key constraints.")
    add_image_figure(doc, "figures_png/fig5_er_diagram.png", "Fig 5: ER Diagram", width_in=5.4)
    
    add_heading_styled(doc, "6.2 Context Diagram (Level 0 DFD)", level=2)
    add_p(doc, "The Context Diagram (Level 0 DFD) defines the conceptual boundary of the Elderly Care Management System (ECMS) and illustrates the high-level information exchanges between the central application engine and external components: Administrator, Guardian, Caregiver, Doctor, Senior Resident, Twilio SMS Gateway, and SMTP Email Server.")
    add_image_figure(doc, "figures_png/fig_context_diagram.png", "Fig 6a: Context Diagram (Level 0 DFD)", width_in=6.2)
    
    add_heading_styled(doc, "6.3 Data Flow Diagram", level=2)
    add_p(doc, "The Data Flow Diagram illustrates how information flows through the system, transitioning from external entities (Senior, Guardian, Caregiver, Doctor, Paramedics) through central application processes and into persistent relational data stores.")
    add_image_figure(doc, "figures_png/fig6_data_flow_diagram.png", "Fig 6b: Level 1 Data Flow Diagram", width_in=6.2)
    
    add_heading_styled(doc, "6.4 Use Case Diagram", level=2)
    add_heading_styled(doc, "6.4.1 User Management Subsystem", level=3)
    add_image_figure(doc, "figures_png/fig7_uc_usermgmt.png", "Fig 7: User Management Subsystem Use Case Diagram", width_in=5.8)
    
    add_heading_styled(doc, "6.4.2 Medication Management Subsystem", level=3)
    add_image_figure(doc, "figures_png/fig8_uc_medmgmt.png", "Fig 8: Medication Management Subsystem Use Case Diagram", width_in=5.8)
    
    add_heading_styled(doc, "6.4.3 Appointment Scheduling Subsystem", level=3)
    add_image_figure(doc, "figures_png/fig9_uc_apptmgt.png", "Fig 9: Appointment Scheduling Subsystem Use Case Diagram", width_in=5.8)
    
    add_heading_styled(doc, "6.4.4 Daily Care & Emergency SOS Subsystem", level=3)
    add_image_figure(doc, "figures_png/fig10_uc_care_sos.png", "Fig 10: Daily Care & Emergency SOS Subsystem Use Case Diagram", width_in=5.8)
    doc.add_page_break()

    # ================= USE CASE NARRATION TABLES =================
    add_heading_styled(doc, "6.5 Use Case Narration Table", level=1)
    
    add_heading_styled(doc, "6.5.1 User Management Subsystem Use Case Narration Table", level=2)
    add_use_case_table(doc,
        uc_name="Create Account",
        actors="Family Guardian, Caregiver, Doctor",
        desc="Users register a new account on the Elderly Care Management System by providing identification and credentials.",
        pre="User must not have an existing active account with the provided email. User must provide valid registration data.",
        typical_events=[
            ("User navigates to Registration page and inputs full name, email, phone number, role, and password.", "System validates input formats, password strength, and verifies email uniqueness."),
            ("User clicks 'Create Account' button.", "System hashes password with Argon2id, creates database record, and displays success confirmation.")
        ],
        alt_flows="Alt 02: System displays error 'Email is already registered. Please login.'\nAlt 04: System highlights invalid phone number or weak password and prompts correction.",
        post="New user account is created in the database and the user can log in to their dashboard."
    )
    
    add_use_case_table(doc,
        uc_name="Login",
        actors="Senior, Family Guardian, Caregiver, Doctor, Admin",
        desc="Users authenticate into the system to access role-specific caregiving and oversight features.",
        pre="A valid registered user account must exist.",
        typical_events=[
            ("User enters registered email/phone and password on login screen.", "System verifies credentials against stored cryptographic hash."),
            ("User clicks 'Login' button.", "System creates authenticated session and loads role-tailored dashboard.")
        ],
        alt_flows="Alt 02: System displays 'Invalid email or password' and increments failed attempts counter.\nAlt 04: Account locked temporarily after 5 consecutive failed attempts.",
        post="User is granted an active session and access to authorized features based on their assigned role."
    )
    
    add_use_case_table(doc,
        uc_name="Edit Profile & Medical Baseline",
        actors="Family Guardian",
        desc="Family Guardian updates senior personal details, home address, emergency contacts, blood group, and chronic conditions.",
        pre="Guardian must be logged in. A senior profile must exist under the guardian's management.",
        typical_events=[
            ("Guardian navigates to 'Senior Profile' and clicks 'Edit Baseline'.", "System loads current profile fields in editable form."),
            ("Guardian updates emergency phone, address, or chronic ailments and clicks 'Save Changes'.", "System validates inputs, updates database, and displays 'Profile updated successfully'.")
        ],
        alt_flows="Alt 04: If mandatory emergency phone number is blank, system displays validation warning and prevents submission.",
        post="Updated senior baseline and emergency contact details are committed to the database and immediately visible to caregivers."
    )

    add_heading_styled(doc, "6.5.2 Medication Management Subsystem Use Case Narration Table", level=2)
    add_use_case_table(doc,
        uc_name="Add Medication & Dosage Schedule",
        actors="Family Guardian, Healthcare Provider / Doctor",
        desc="Guardian or Doctor inputs a new prescription regimen, specifying medication name, dosage amount, timing, and meal relation.",
        pre="User must be logged in as Guardian or Doctor. Senior profile must exist.",
        typical_events=[
            ("User opens 'Add Medication' screen.", "System displays prescription configuration form."),
            ("User enters drug name (e.g., Amlodipine), dose (5mg), schedule times (08:00 AM, 08:00 PM), meal rule, and clicks 'Save Schedule'.", "System validates entries, creates dosage schedule records in database, and initializes daily reminder alarms.")
        ],
        alt_flows="Alt 04: If dose timing is unselected, system highlights missing required timing and prompts completion.",
        post="New medication schedule is saved and scheduled reminder alarms appear on senior and caregiver dashboards."
    )

    add_use_case_table(doc,
        uc_name="Log Dose Taken / Missed",
        actors="Elderly Senior, Professional Caregiver",
        desc="Senior or Caregiver records whether a scheduled medication dose was consumed, missed, or skipped.",
        pre="A scheduled medication dose event must exist for the current date and time.",
        typical_events=[
            ("When reminder triggers, user clicks large green 'Taken' button (or 'Missed/Skipped').", "System prompts for optional note (mandatory reason if Skipped)."),
            ("User confirms action.", "System writes timestamped dose log to database, updates adherence stats, and silences reminder alarm.")
        ],
        alt_flows="Alt 01: If dose remains unconfirmed 30 minutes after scheduled time, system marks status as 'Pending Warning' and alerts Guardian.",
        post="Dose status is permanently recorded in the adherence log and updated in the Guardian's live feed."
    )

    add_heading_styled(doc, "6.5.3 Appointment Scheduling Subsystem Use Case Narration Table", level=2)
    add_use_case_table(doc,
        uc_name="Schedule Doctor Appointment",
        actors="Family Guardian, Healthcare Provider / Doctor",
        desc="Guardian books a medical consultation, diagnostic test, or hospital follow-up for the senior.",
        pre="Senior profile must exist. Guardian or Doctor must be logged in.",
        typical_events=[
            ("Guardian clicks 'Book Doctor Appointment'.", "System displays appointment entry form."),
            ("Guardian inputs doctor name, clinic address, appointment date, time, and reason for visit.", "System validates date, saves appointment record, and sets automated reminder notifications.")
        ],
        alt_flows="Alt 04: If selected date is in the past, system rejects entry with error 'Appointment date must be in the future.'",
        post="Appointment is confirmed, listed on the family calendar, and scheduled reminders are queued."
    )

    add_heading_styled(doc, "6.5.4 Daily Care & Emergency SOS Subsystem Use Case Narration Table", level=2)
    add_use_case_table(doc,
        uc_name="Log Daily Care Tasks & Vitals",
        actors="Professional Caregiver, Senior",
        desc="Caregiver records completion of non-medical daily tasks (hygiene, meals, walk) and enters measured vital signs.",
        pre="Caregiver must be logged in and assigned to the senior. Daily routine checklist must exist.",
        typical_events=[
            ("Caregiver opens 'Daily Care Checklist' screen.", "System displays scheduled tasks (Breakfast, Bathing, Physical Mobility)."),
            ("Caregiver checks off completed tasks and inputs measured Blood Pressure (120/80) and Glucose (6.2).", "System validates numerical ranges, stores logs in database, and updates Guardian's live feed.")
        ],
        alt_flows="Alt 04: If entered blood pressure exceeds safety threshold (>150 systolic), system flags reading in bright red and notifies Guardian.",
        post="Daily care tasks and vitals are logged with timestamps, establishing an accountable audit trail."
    )

    add_use_case_table(doc,
        uc_name="Trigger Emergency SOS Alert",
        actors="Elderly Senior, Caregiver, Family Guardian",
        desc="Senior or Caregiver activates the prominent emergency panic button during acute medical crises or domestic falls.",
        pre="System is active on senior tablet, mobile phone, or caregiver terminal.",
        typical_events=[
            ("Senior presses the large red 'EMERGENCY SOS' button.", "System captures live GPS coordinates and sounds local visual/audio distress alarm."),
            ("System immediately dispatches emergency SMS and emails to Guardian and ambulance dispatch.", "Emergency broadcast includes senior name, home address, GPS link, blood group, and drug allergies.")
        ],
        alt_flows="Alt 01: 10-second cancellation window provided in case of accidental tap, allowing immediate disarm with PIN.",
        post="Emergency alert is permanently logged in audit table; all guardians and emergency personnel receive distress dispatch."
    )
    doc.add_page_break()

    # ================= CRUD MATRIX & ACTIVITY & GANTT =================
    add_heading_styled(doc, "6.6 CRUD Matrix", level=2)
    add_p(doc, "The CRUD Matrix establishes data access privileges across the primary relational entities, defining which user roles have permission to Create (C), Read (R), Update (U), or Delete (D) specific database records.")
    
    crud_headers = ["Process / Entity", "Senior", "Guardian", "Caregiver", "Doctor", "Admin"]
    crud_rows = [
        ["User Account", "R", "CRU", "CRU", "CRU", "CRUD"],
        ["Senior Profile Baseline", "R", "CRUD", "R", "RU", "RD"],
        ["Medication Schedule", "R", "CRUD", "R", "CRUD", "RD"],
        ["Dose Adherence Log", "CR", "RU", "CRU", "R", "RD"],
        ["Doctor Appointments", "R", "CRUD", "R", "CRUD", "RD"],
        ["Prescription Documents", "R", "CRUD", "R", "CRUD", "RD"],
        ["Daily Care Tasks (ADL)", "R", "CRUD", "CRU", "R", "RD"],
        ["Shift Handoff Notes", "R", "RU", "CRU", "R", "RD"],
        ["Emergency SOS Alerts", "CR", "CRU", "CRU", "R", "RD"],
        ["System Audit Trail", "-", "R", "-", "-", "CRD"]
    ]
    create_table_from_data(doc, crud_headers, crud_rows, [2.5, 0.9, 1.0, 1.0, 0.9, 0.9])
    
    add_heading_styled(doc, "6.7 Activity Table", level=2)
    act_headers = ["SL", "Activity Code", "Activity Name", "Duration (Days)", "Dependency"]
    act_rows = [
        ["1", "A", "Project Topic Selection & Scope Definition", "1", "-"],
        ["2", "B", "Requirement Elicitation & Feature Selection", "2", "A"],
        ["3", "C", "System Architecture & Database Schema Design", "2", "B"],
        ["4", "D", "User Authentication & RBAC Engine", "2", "C"],
        ["5", "E", "Senior Health Baseline & Profile Module", "3", "D"],
        ["6", "F", "Medication Master & Dosage Scheduling Module", "3", "E"],
        ["7", "G", "Real-Time Dose Adherence Logging & Reminders", "2", "F"],
        ["8", "H", "Doctor Appointment & Calendar Module", "3", "E"],
        ["9", "I", "Digital Prescription & Clinical Archive", "2", "H"],
        ["10", "J", "Daily Care Checklist & ADL Routine Module", "2", "E"],
        ["11", "K", "Caregiver Shift Handoff & Care Notes Module", "2", "J"],
        ["12", "L", "Instant Emergency SOS Panic & SMS Broadcast", "2", "E"],
        ["13", "M", "Family Guardian Oversight Live Dashboard", "2", "G, K, L"],
        ["14", "N", "Compliance Analytics & PDF Reporting", "2", "M"],
        ["15", "O", "End-to-End System Testing & Quality Assurance", "4", "All"],
        ["16", "P", "Comprehensive SRS Documentation Compilation", "3", "O"],
        ["17", "Q", "Cloud Deployment, Live Demonstration & Release", "1", "P"]
    ]
    create_table_from_data(doc, act_headers, act_rows, [0.6, 1.2, 3.2, 1.2, 1.0])
    
    add_heading_styled(doc, "6.8 Gantt chart", level=2)
    add_image_figure(doc, "figures_png/fig11_gantt_chart.png", "Fig 11: Gantt Chart", width_in=6.2)
    doc.add_page_break()

    # ================= NON-FUNCTIONAL REQUIREMENTS & RESULT ANALYSIS =================
    add_heading_styled(doc, "Non-Functional Requirements", level=1)
    add_heading_styled(doc, "7.1 Feature List with Description", level=2)
    add_bullet(doc, "Page loads render in under 2.0s over standard 4G/WiFi; query latency <200ms; Emergency SOS executes in <1.0s.", bold_prefix="1. Performance & Latency: ")
    add_bullet(doc, "99.9% scheduled uptime with automated nightly offsite database backups and failover protection.", bold_prefix="2. Reliability & Availability: ")
    add_bullet(doc, "Full TLS 1.3 encryption, Argon2id password hashing, and AES-256 encryption at rest for sensitive health baselines.", bold_prefix="3. Security & Confidentiality: ")
    add_bullet(doc, "WCAG 2.1 AA compliant with high-contrast themes, 18px+ font options, and large 48px touch targets for seniors.", bold_prefix="4. Usability & Senior Accessibility: ")
    add_bullet(doc, "Stateless PHP backend horizontally scalable to 10,000+ active care plans without locking contention.", bold_prefix="5. Scalability: ")
    add_bullet(doc, "Responsive HTML5/CSS3 cross-browser compatibility across Chrome, Firefox, Safari, and Edge.", bold_prefix="6. Portability: ")
    add_bullet(doc, "Strict PSR-12 coding guidelines, modular MVC architecture, and comprehensive docstring comments.", bold_prefix="7. Maintainability: ")
    
    add_heading_styled(doc, "Result Analysis", level=1)
    add_heading_styled(doc, "8.1 SWOT Analysis", level=2)
    swot_headers = ["Strength", "Weakness"]
    swot_rows = [
        [
            "• Eliminates manual eldercare paperwork.\n• Real-time medication adherence tracking.\n• Instant 1-touch SOS with GPS location.\n• Seamless caregiver shift continuity.\n• Multi-role integration (Senior, Family, Doctor).",
            "• Dependent on stable internet connectivity.\n• Requires initial technical onboarding for seniors.\n• Relies on caregiver integrity for accurate vital inputs."
        ],
        [
            "Opportunities\n• Integration with wearable IoT health monitors.\n• Automated AI predictive fall detection.\n• Telemedicine video consultation expansion.\n• Automated pharmacy prescription refilling.",
            "Threats\n• Cybersecurity and health data breach risks.\n• Cloud server downtime during emergency crises.\n• Resistance to technology adoption by seniors."
        ]
    ]
    create_table_from_data(doc, swot_headers, swot_rows, [3.6, 3.6])
    
    add_heading_styled(doc, "8.2 Risk Matrix", level=2)
    risk_headers = ["Risk Factor", "Likelihood", "Impact", "Solution / Mitigation Strategy"]
    risk_rows = [
        ["Database Loss / Corruption", "Low", "High", "Automated daily offsite cloud backups & InnoDB transaction logs."],
        ["Unauthorized Health Access", "Low", "High", "Argon2id hashing, TLS 1.3 encryption, and strict RBAC verification."],
        ["Network Failure during SOS", "Medium", "High", "Local audio-visual alarm activates immediately; SMS dispatched asynchronously."],
        ["Caregiver Handoff Neglect", "Medium", "Medium", "Mandatory digital shift sign-off before clock-out is permitted."]
    ]
    create_table_from_data(doc, risk_headers, risk_rows, [2.0, 1.0, 1.0, 3.2])
    doc.add_page_break()

    # ================= CONCLUSION & REFERENCES =================
    add_heading_styled(doc, "Conclusion", level=1)
    add_p(doc, "This Software Requirements Specification proposes a comprehensive, methodical, and human-centric approach to modernizing and automating geriatric care routines. Traditional eldercare systems—heavily reliant on physical pillboxes, handwritten notebooks, and fragmented phone communications—expose aging seniors to preventable medication omissions, shift communication breakdowns, and fatal emergency response delays.")
    add_p(doc, "The proposed Elderly Care Management System addresses these vulnerabilities through an integrated, multi-role web platform. By synchronizing medication schedules with real-time adherence logging, streamlining doctor consultations and digital prescription archives, standardizing daily living (ADL) routines, enforcing caregiver shift handoff accountability, and providing an instantaneous one-touch Emergency SOS broadcast with GPS coordinates and medical briefs, the platform establishes an unbroken circle of care around the senior.")
    add_p(doc, "The architectural design, relational schema, UML behavioral models, and verification frameworks articulated throughout this report demonstrate that the system is technically, economically, and operationally feasible. Built upon an accessible frontend and a secure relational backend, the Elderly Care Management System delivers profound socio-technological value: eliminating dangerous medication errors, fostering professional accountability, and granting working family members 24/7 peace of mind while preserving the independence and dignity of aging senior citizens.")
    
    add_heading_styled(doc, "References", level=1)
    refs = [
        "IEEE Computer Society, 'IEEE Recommended Practice for Software Requirements Specifications,' IEEE Std 830-1998, Institute of Electrical and Electronics Engineers, New York, 1998.",
        "ISO/IEC/IEEE, 'Systems and software engineering — Life cycle processes — Requirements engineering,' ISO/IEC/IEEE 29148:2018, Geneva, Switzerland, 2018.",
        "World Health Organization (WHO), 'Medication Safety in Polypharmacy: Technical Report,' WHO Patient Safety Global Action, World Health Organization, Geneva, 2019.",
        "World Health Organization (WHO), 'World Report on Ageing and Health,' WHO Press, Geneva, 2015.",
        "B. Bryan, 'Software Architecture Patterns: Layered Architecture Patterns,' Medium Software Engineering Publication, Available: https://yapbryan6.medium.com/software-architecture-patterns-layered-architecture-patterns-975ff2abec6f, [Accessed: Oct. 2025].",
        "World Wide Web Consortium (W3C), 'Web Content Accessibility Guidelines (WCAG) 2.1,' W3C Recommendation, Available: https://www.w3.org/TR/WCAG21/, 2018.",
        "Open Web Application Security Project (OWASP), 'OWASP Top 10: The Ten Most Critical Web Application Security Risks,' OWASP Foundation, 2021.",
        "R. S. Pressman and B. R. Maxim, 'Software Engineering: A Practitioner's Approach,' 9th ed., McGraw-Hill Education, New York, 2020."
    ]
    for idx, ref in enumerate(refs, 1):
        add_p(doc, f"[{idx}] {ref}")
        
    out_path = "Elderly_Care_Management_System_SRS.docx"
    doc.save(out_path)
    print(f"SUCCESS: Saved {out_path} ({os.path.getsize(out_path):,} bytes)")

if __name__ == "__main__":
    main()
