# Build script to generate the complete 53-page Software Requirements Specification (SRS)
# for Elderly Care Management System, exactly matching demo.pdf in structure, style, and page count.

import os
import subprocess
import tempfile
import base64
import pypdf
import svg_diagrams

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""

def build_html():
    logo_base64 = get_base64_image("iub_logo.png")
    
    # CSS Styles matching demo.pdf (Arial, clean margins, bordered tables, exact letter page dimensions)
    css = """
    @page {
      size: letter portrait;
      margin: 0;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      margin: 0;
      padding: 0;
      background: #e2e8f0;
      font-family: Arial, Helvetica, sans-serif;
      color: #111827;
      font-size: 11pt;
      line-height: 1.45;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }
    .page {
      width: 8.5in;
      height: 11in;
      padding: 0.8in 0.85in 0.8in 0.85in;
      margin: 20px auto;
      background: #ffffff;
      position: relative;
      page-break-after: always;
      overflow: hidden;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    @media print {
      body {
        background: #ffffff;
      }
      .page {
        margin: 0;
        box-shadow: none;
        page-break-after: always;
      }
    }
    .page-number {
      position: absolute;
      bottom: 0.45in;
      left: 0;
      right: 0;
      text-align: center;
      font-size: 10.5pt;
      color: #374151;
    }
    
    /* Cover Page Styles */
    .cover-container {
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      text-align: center;
      padding: 0.4in 0.2in 0.2in 0.2in;
    }
    .cover-logo {
      width: 130px;
      height: auto;
      margin: 0 auto 20px auto;
    }
    .cover-title {
      font-size: 21pt;
      font-weight: bold;
      color: #0f172a;
      line-height: 1.35;
      margin-top: 15px;
      margin-bottom: 30px;
    }
    .cover-title span {
      display: block;
      color: #0d9488;
      font-size: 23pt;
      margin-top: 10px;
    }
    .cover-section-title {
      font-size: 13pt;
      font-weight: bold;
      color: #1e293b;
      margin-bottom: 8px;
    }
    .cover-meta {
      font-size: 11.5pt;
      color: #334155;
      line-height: 1.5;
      margin-bottom: 25px;
    }
    
    /* Document Typography */
    h1.sec-title {
      font-size: 16pt;
      font-weight: bold;
      color: #0f172a;
      margin-bottom: 12px;
      border-bottom: 1.5px solid #cbd5e1;
      padding-bottom: 4px;
    }
    h2.sub-title {
      font-size: 13pt;
      font-weight: bold;
      color: #0f766e;
      margin-top: 14px;
      margin-bottom: 8px;
    }
    h3.subsub-title {
      font-size: 11.5pt;
      font-weight: bold;
      color: #1e293b;
      margin-top: 10px;
      margin-bottom: 6px;
    }
    p {
      margin-bottom: 10px;
      text-align: justify;
      color: #1f2937;
      font-size: 10.5pt;
      line-height: 1.45;
    }
    ul, ol {
      margin-left: 20px;
      margin-bottom: 10px;
      font-size: 10.5pt;
    }
    li {
      margin-bottom: 4px;
      line-height: 1.4;
      color: #1f2937;
    }
    
    /* Table Styling */
    table.data-table {
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0;
      font-size: 9.5pt;
    }
    table.data-table th, table.data-table td {
      border: 1px solid #94a3b8;
      padding: 6px 8px;
      text-align: left;
      vertical-align: top;
    }
    table.data-table th {
      background-color: #f1f5f9;
      font-weight: bold;
      color: #0f172a;
    }
    table.data-table tr:nth-child(even) td {
      background-color: #f8fafc;
    }
    
    /* Use Case Narration Table */
    table.uc-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 8px;
      font-size: 9.5pt;
    }
    table.uc-table th, table.uc-table td {
      border: 1px solid #94a3b8;
      padding: 6px 8px;
      vertical-align: top;
    }
    table.uc-table td.uc-label {
      width: 25%;
      font-weight: bold;
      background-color: #f1f5f9;
      color: #0f172a;
    }
    table.uc-subtable {
      width: 100%;
      border-collapse: collapse;
      margin: 0;
    }
    table.uc-subtable th, table.uc-subtable td {
      border: 1px solid #cbd5e1;
      padding: 4px 6px;
      font-size: 9pt;
    }
    table.uc-subtable th {
      background-color: #e2e8f0;
      font-weight: bold;
      color: #1e293b;
    }

    /* Diagrams & Captions */
    .diagram-wrapper {
      margin: 10px 0 6px 0;
      text-align: center;
    }
    .fig-caption {
      font-size: 10pt;
      font-weight: bold;
      color: #334155;
      text-align: center;
      margin-top: 4px;
      margin-bottom: 8px;
    }
    
    /* TOC Styles */
    .toc-item {
      display: flex;
      justify-content: space-between;
      margin-bottom: 6px;
      font-size: 10.5pt;
      line-height: 1.35;
    }
    .toc-item.level-1 {
      font-weight: bold;
      color: #0f172a;
      margin-top: 6px;
    }
    .toc-item.level-2 {
      padding-left: 18px;
      color: #334155;
    }
    .toc-item.level-3 {
      padding-left: 36px;
      color: #475569;
      font-size: 10pt;
    }
    .toc-dots {
      flex: 1;
      border-bottom: 1px dotted #94a3b8;
      margin: 0 8px 3px 8px;
    }
    """

    pages_html = []

    # =========================================================================
    # PAGE 1: COVER PAGE
    # =========================================================================
    p1 = f"""
    <div class="page" id="page-1">
      <div class="cover-container">
        <div>
          <img src="{logo_base64}" class="cover-logo" alt="IUB Logo" />
          <div class="cover-title">
            Software Requirements Specification<br>
            for<br>
            <span>Elderly Care Management System</span>
          </div>
        </div>

        <div>
          <div class="cover-section-title">Prepared By</div>
          <div class="cover-meta">
            <strong>Farzana Sadia Takee</strong><br>
            2211175<br>
            Course Code: CSE309<br>
            Course Title: Web Application and Internet<br>
            Section: 05<br>
            Autumn 2025
          </div>

          <div class="cover-section-title">Submitted to</div>
          <div class="cover-meta">
            <strong>MS. Shanjita Akter Prome</strong><br>
            Adjunct Faculty<br>
            Independent University Bangladesh
          </div>
        </div>
      </div>
    </div>
    """
    pages_html.append(p1)

    # =========================================================================
    # PAGE 2: TABLE OF CONTENTS (Part 1)
    # =========================================================================
    p2 = """
    <div class="page" id="page-2">
      <h1 class="sec-title">Table of Contents</h1>
      
      <div class="toc-item level-1"><span>Abstract</span><span class="toc-dots"></span><span>4</span></div>
      
      <div class="toc-item level-1"><span>Introduction</span><span class="toc-dots"></span><span>5</span></div>
      <div class="toc-item level-2"><span>1.1 Background</span><span class="toc-dots"></span><span>5</span></div>
      <div class="toc-item level-2"><span>1.2 Motivation</span><span class="toc-dots"></span><span>6</span></div>
      <div class="toc-item level-2"><span>1.3 Problem Statement</span><span class="toc-dots"></span><span>7</span></div>
      <div class="toc-item level-2"><span>1.4 Objective</span><span class="toc-dots"></span><span>8</span></div>

      <div class="toc-item level-1"><span>System Overview</span><span class="toc-dots"></span><span>10</span></div>
      <div class="toc-item level-2"><span>2.1 System Users</span><span class="toc-dots"></span><span>10</span></div>
      <div class="toc-item level-2"><span>2.2 System Architecture</span><span class="toc-dots"></span><span>12</span></div>
      <div class="toc-item level-2"><span>2.3 System Modules</span><span class="toc-dots"></span><span>13</span></div>
      <div class="toc-item level-2"><span>2.4 Security and Verification</span><span class="toc-dots"></span><span>15</span></div>
      <div class="toc-item level-2"><span>2.5 Software Development Tools</span><span class="toc-dots"></span><span>16</span></div>
      <div class="toc-item level-2"><span>2.6 Advantages of Using The System</span><span class="toc-dots"></span><span>17</span></div>

      <div class="toc-item level-1"><span>System Life Cycle</span><span class="toc-dots"></span><span>18</span></div>
      <div class="toc-item level-2"><span>3.1 Software Development Life Cycle</span><span class="toc-dots"></span><span>18</span></div>
      <div class="toc-item level-3"><span>3.1.1 SDLC Phases</span><span class="toc-dots"></span><span>18</span></div>

      <div class="toc-item level-1"><span>Requirement Engineering</span><span class="toc-dots"></span><span>20</span></div>
      <div class="toc-item level-2"><span>4.1 Requirement Elicitation</span><span class="toc-dots"></span><span>20</span></div>
      <div class="toc-item level-2"><span>4.2 Requirement Analysis</span><span class="toc-dots"></span><span>20</span></div>
      <div class="toc-item level-3"><span>4.2.1 Feasibility Study</span><span class="toc-dots"></span><span>20</span></div>
      <div class="toc-item level-3"><span>4.2.2 Requirement Classification</span><span class="toc-dots"></span><span>21</span></div>
      <div class="toc-item level-3"><span>4.2.3 Conflict and Redundancy Resolution</span><span class="toc-dots"></span><span>21</span></div>
      <div class="toc-item level-2"><span>4.3 Requirement Documentation</span><span class="toc-dots"></span><span>22</span></div>

      <div class="toc-item level-1"><span>Functional requirements</span><span class="toc-dots"></span><span>23</span></div>
      <div class="toc-item level-2"><span>5.1 Feature List with Description</span><span class="toc-dots"></span><span>23</span></div>
      <div class="toc-item level-2"><span>5.2 Feature Table</span><span class="toc-dots"></span><span>25</span></div>

      <div class="toc-item level-1"><span>System Specification Diagrams</span><span class="toc-dots"></span><span>28</span></div>
      <div class="toc-item level-2"><span>6.1 Entity Relationship Diagram</span><span class="toc-dots"></span><span>28</span></div>
      <div class="toc-item level-2"><span>6.3 Data Flow Diagram</span><span class="toc-dots"></span><span>29</span></div>
      <div class="toc-item level-2"><span>6.4 Use Case Diagram</span><span class="toc-dots"></span><span>30</span></div>
      <div class="toc-item level-3"><span>6.4.1 User Management Subsystem</span><span class="toc-dots"></span><span>30</span></div>
      <div class="toc-item level-3"><span>6.4.2 Medication Management Subsystem</span><span class="toc-dots"></span><span>31</span></div>
      <div class="toc-item level-3"><span>6.4.3 Appointment Management Subsystem</span><span class="toc-dots"></span><span>31</span></div>
      <div class="toc-item level-3"><span>6.4.4 Daily Care & Emergency SOS Subsystem</span><span class="toc-dots"></span><span>32</span></div>

      <div class="page-number">2</div>
    </div>
    """
    pages_html.append(p2)

    # =========================================================================
    # PAGE 3: TABLE OF CONTENTS (Part 2)
    # =========================================================================
    p3 = """
    <div class="page" id="page-3">
      <div class="toc-item level-2"><span>6.5 Use Case Narration Table</span><span class="toc-dots"></span><span>33</span></div>
      <div class="toc-item level-3"><span>6.5.1 User Management Subsystem Use Case Narration Table</span><span class="toc-dots"></span><span>33</span></div>
      <div class="toc-item level-3"><span>6.5.2 Medication Management Subsystem Use Case Narration Table</span><span class="toc-dots"></span><span>37</span></div>
      <div class="toc-item level-3"><span>6.5.3 Appointment Management Subsystem Use Case Narration Table</span><span class="toc-dots"></span><span>40</span></div>
      <div class="toc-item level-3"><span>6.5.4 Daily Care & Emergency SOS Subsystem Use Case Narration Table</span><span class="toc-dots"></span><span>43</span></div>

      <div class="toc-item level-2"><span>6.6 CRUD Matrix</span><span class="toc-dots"></span><span>46</span></div>
      <div class="toc-item level-2"><span>6.7 Activity Table</span><span class="toc-dots"></span><span>47</span></div>
      <div class="toc-item level-2"><span>6.8 Gantt chart</span><span class="toc-dots"></span><span>48</span></div>

      <div class="toc-item level-1"><span>Non-Functional Requirements</span><span class="toc-dots"></span><span>49</span></div>
      <div class="toc-item level-2"><span>7.1 Feature List with Description</span><span class="toc-dots"></span><span>49</span></div>

      <div class="toc-item level-1"><span>Result Analysis</span><span class="toc-dots"></span><span>51</span></div>
      <div class="toc-item level-2"><span>8.1 SWOT Analysis</span><span class="toc-dots"></span><span>51</span></div>
      <div class="toc-item level-2"><span>8.2 Risk Matrix</span><span class="toc-dots"></span><span>51</span></div>

      <div class="toc-item level-1"><span>Conclusion</span><span class="toc-dots"></span><span>52</span></div>

      <div class="toc-item level-1"><span>References</span><span class="toc-dots"></span><span>53</span></div>

      <div class="page-number">3</div>
    </div>
    """
    pages_html.append(p3)

    # =========================================================================
    # PAGE 4: ABSTRACT
    # =========================================================================
    p4 = """
    <div class="page" id="page-4">
      <h1 class="sec-title">Abstract</h1>
      <p>
        The <strong>Elderly Care Management System</strong> is a Web-based application that automates, streamlines, and centralizes daily eldercare operations and healthcare supervision. Traditionally, elderly care activities—such as medication administration tracking, doctor appointment scheduling, vital sign monitoring, and caregiver shift handoffs—have been managed manually using handwritten paper logs, physical pillboxes, and fragmented telephone communications. Consequently, families and eldercare institutions face significant inefficiencies, frequent medication errors, missed clinical appointments, and potentially fatal delays during sudden medical emergencies.
      </p>
      <p>
        The Elderly Care Management System directly resolves these critical vulnerabilities by introducing a unified, multi-role digital ecosystem connecting elderly citizens, family guardians, visiting or residential caregivers, and medical practitioners. By offering real-time medication reminders, single-tap adherence logging, digital prescription archives, structured activities of daily living (ADL) checklists, and instantaneous emergency SOS panic alerting with live GPS broadcast, the platform eliminates human error and provides round-the-clock peace of mind for family guardians.
      </p>
      <p>
        Developed using an accessible frontend architecture and a robust, secure relational backend, the system adheres strictly to health data privacy protocols, role-based access control (RBAC), and universal accessibility standards (WCAG 2.1 AA) tailored for senior citizens. This comprehensive Software Requirements Specification (SRS) report establishes the architectural foundation, functional and non-functional specifications, UML behavioral models, relational database schemas, and verification frameworks governing the development and deployment of the platform.
      </p>
      <div class="page-number">4</div>
    </div>
    """
    pages_html.append(p4)

    # =========================================================================
    # PAGE 5: 1. INTRODUCTION & 1.1 BACKGROUND
    # =========================================================================
    p5 = """
    <div class="page" id="page-5">
      <h1 class="sec-title">Introduction</h1>
      <p>
        The purpose of the Elderly Care Management System is to automate, digitize, and coordinate home care and health supervision routines for aging seniors. In modern society, shifting socio-demographic structures, the rapid growth of nuclear families, and demanding professional obligations make it increasingly difficult for adult children and family guardians to administer continuous, error-free care for their aging parents manually. The Elderly Care Management System provides an integrated, methodical, web-enabled solution to this pervasive challenge, establishing a consistent and transparent channel for managing geriatric health routines while enhancing safety, speed, accuracy, and overall quality of life.
      </p>

      <h2 class="sub-title">1.1 Background</h2>
      <p>
        Global demographic transitions indicate an unprecedented increase in the senior citizen population. Concurrently, a substantial portion of the elderly demographic experiences chronic conditions such as hypertension, diabetes mellitus, cardiovascular ailments, arthritis, and mild cognitive impairments. Managing these multi-morbidities necessitates complex polypharmacy regimens, regular clinical checkups, continuous physiological vital sign tracking, and assistance with activities of daily living (ADLs).
      </p>
      <p>
        In traditional domestic and institutional care environments, care coordination depends on memory, handwritten paper diaries, and manual telephone inquiries. When family members leave for work or reside in distant cities, they remain in a persistent state of anxiety, unable to verify whether their senior relatives took their critical morning cardiovascular medication, consumed balanced meals, or attended their scheduled clinical consultations. Furthermore, professional caregivers working rotating shifts lack standardized handoff documentation, creating hazardous blind spots in patient history. A centralized web application addresses these challenges by consolidating health data into an auditable, real-time platform accessible from any standard web browser.
      </p>
      <div class="page-number">5</div>
    </div>
    """
    pages_html.append(p5)

    # =========================================================================
    # PAGE 6: 1.2 MOTIVATION
    # =========================================================================
    p6 = """
    <div class="page" id="page-6">
      <h2 class="sub-title">1.2 Motivation</h2>
      <p>
        Several critical real-world factors motivated the conception and development of the Elderly Care Management System:
      </p>
      <ol>
        <li>
          <strong>Rapid Growth of the Geriatric Demographic:</strong> As life expectancy expands and nuclear family arrangements become the predominant societal norm, the reliance on structured digital care management systems has grown exponentially. Families need reliable technological tools that bridge physical distances and ensure proactive elder supervision.
        </li>
        <li>
          <strong>Eradication of Lethal Medication Errors:</strong> Medical literature highlights that polypharmacy omissions, dosage duplications, and adverse drug-drug interactions represent leading causes of preventable emergency geriatric hospital admissions. Automating medication schedules with timestamped adherence confirmation removes reliance on vulnerable senior memory.
        </li>
        <li>
          <strong>Elimination of Caregiver Communication Breakdowns:</strong> Visiting caregivers, domestic aides, and relatives frequently fail to communicate vital observations during shift changes. A centralized digital handoff log ensures seamless continuity of care, recording completed meals, fluid intake, hygiene, and abnormal vital readings.
        </li>
        <li>
          <strong>Immediate Life-Safety Escalation in Emergencies:</strong> In acute episodes such as domestic falls, sudden chest pain, or respiratory distress, seniors often cannot unlock smartphones or dial emergency telephone numbers. A dedicated, one-touch SOS mechanism that dispatches real-time distress alerts with GPS coordinates to both family and paramedics is vital for saving lives.
        </li>
        <li>
          <strong>Actionable Clinical Data for Physicians:</strong> Doctors routinely encounter patients who cannot accurately recall their past adherence history or physiological fluctuations. Providing clinicians with verified longitudinal records dramatically improves diagnostic accuracy and therapeutic efficacy.
        </li>
      </ol>
      <div class="page-number">6</div>
    </div>
    """
    pages_html.append(p6)

    # =========================================================================
    # PAGE 7: 1.3 PROBLEM STATEMENT
    # =========================================================================
    p7 = """
    <div class="page" id="page-7">
      <h2 class="sub-title">1.3 Problem Statement</h2>
      <p>
        Manual systems, physical paper organizers, and informal verbal communications are still the standard methods employed by families and care aides to manage eldercare routines. These outdated administrative workflows result in severe operational challenges, safety risks, and emotional stress, including:
      </p>
      <ol>
        <li>
          <strong>Medication Mismanagement and Dose Omissions:</strong> Elderly individuals frequently forget whether they have consumed their daily prescription doses. Physical pillboxes offer no verification mechanism, leading to dangerous under-dosing or life-threatening accidental double-dosing.
        </li>
        <li>
          <strong>Lack of Real-Time Care Visibility for Family Members:</strong> Working guardians lack real-time visibility into the daily wellbeing of their elderly relatives. They must repeatedly disrupt their workdays with phone calls that may go unanswered, causing severe panic and emotional distress.
        </li>
        <li>
          <strong>Unaccountable and Fragmented Caregiver Handoffs:</strong> Professional care aides currently record care activities on arbitrary paper notebooks or convey them verbally. If an aide forgets to document a high blood pressure reading or an omitted evening meal, subsequent caregivers remain unaware, compromising patient safety.
        </li>
        <li>
          <strong>Misplaced Prescriptions and Missed Clinic Appointments:</strong> Physical paper prescriptions, laboratory blood reports, and doctor appointment slips are easily lost, leading to missed specialist consultations and discontinued therapies.
        </li>
        <li>
          <strong>Delayed Crisis Response During Acute Incidents:</strong> When a senior suffers a sudden fall or stroke, every minute delay in emergency response can cause permanent disability or fatality. Current manual setups lack an instantaneous, one-touch panic dispatch mechanism.
        </li>
      </ol>
      <div class="page-number">7</div>
    </div>
    """
    pages_html.append(p7)

    # =========================================================================
    # PAGE 8: FIG 1 & 1.4 OBJECTIVE (Part 1)
    # =========================================================================
    p8 = f"""
    <div class="page" id="page-8">
      <div class="diagram-wrapper">
        {svg_diagrams.get_fig1_existing_system_svg()}
        <div class="fig-caption">Fig 1: Existing System Rich Picture</div>
      </div>

      <h2 class="sub-title">1.4 Objective</h2>
      <p>
        The primary objectives of the Elderly Care Management System are:
      </p>
      <ol>
        <li>
          <strong>Centralize Senior Health Baselines:</strong> Create an automated, unified cloud repository to maintain complete senior profiles, emergency contacts, primary physicians, chronic conditions, and critical drug allergies without manual paperwork.
        </li>
        <li>
          <strong>Automate Medication Schedules & Adherence Tracking:</strong> Provide an intuitive interface to configure dosage timings and enable seniors and caregivers to confirm dose administration with a single click, logging exact timestamps.
        </li>
        <li>
          <strong>Streamline Clinical Appointments & Medical Records:</strong> Enable family guardians to schedule, view, and manage doctor consultations, diagnostic tests, and digital prescription scans.
        </li>
        <li>
          <strong>Standardize Daily Care Routines (ADLs) and Shift Handoffs:</strong> Provide a structured checklist for daily nutrition, hygiene, mobility, and vital signs, coupled with an immutable shift handoff logging system for caregivers.
        </li>
      </ol>
      <div class="page-number">8</div>
    </div>
    """
    pages_html.append(p8)

    # =========================================================================
    # PAGE 9: 1.4 OBJECTIVE (Part 2) & FIG 2
    # =========================================================================
    p9 = f"""
    <div class="page" id="page-9">
      <ol start="5">
        <li>
          <strong>Provide Instant Emergency SOS Alerting with Critical Medical Brief:</strong> Empower seniors to trigger an instantaneous distress alert with a single button press, broadcasting real-time GPS coordinates, emergency contacts, blood group, and allergy warnings via SMS, email, and dashboard alarms.
        </li>
        <li>
          <strong>Ensure Health Data Privacy and Role-Based Protection:</strong> Implement strict authentication, salted cryptographic password hashing, role-based access control (RBAC), and encrypted communications to safeguard sensitive medical and personal data.
        </li>
        <li>
          <strong>Deliver Longitudinal Wellness Analytics:</strong> Generate automated visual reports and exportable PDF summaries illustrating medication adherence rates and vital trends for family review and clinical consultations.
        </li>
      </ol>

      <div class="diagram-wrapper">
        {svg_diagrams.get_fig2_proposed_system_svg()}
        <div class="fig-caption">Fig 2: Proposed System Rich Picture</div>
      </div>
      <div class="page-number">9</div>
    </div>
    """
    pages_html.append(p9)

    # =========================================================================
    # PAGE 10: 2. SYSTEM OVERVIEW & 2.1 SYSTEM USERS (Part 1)
    # =========================================================================
    p10 = """
    <div class="page" id="page-10">
      <h1 class="sec-title">System Overview</h1>
      <p>
        The Elderly Care Management System allows families, caregivers, and healthcare professionals to coordinate, monitor, and safeguard geriatric health routines efficiently. In the past, eldercare required heavy manual effort, physical paper record-keeping, and disjointed phone calls that introduced dangerous communication gaps. As a result, critical tasks were frequently overlooked, and emergencies escalated unchecked. The Elderly Care Management System addresses these issues by offering an integrated web application that standardizes schedules, logs daily care, and dispatches instant alerts.
      </p>

      <h2 class="sub-title">2.1 System Users</h2>
      <p>
        The system supports five distinct user classes, each with tailored interfaces and granular operational privileges:
      </p>
      <ul>
        <li>
          <strong>Elderly Senior Citizen:</strong> The primary beneficiary of the platform. Interacts through a high-contrast, large-font interface optimized for seniors with mild visual or motor limitations. Seniors can view daily medication alarms, tap a single large confirmation button to mark doses as 'Taken', review the day's meals, and trigger the high-priority Emergency SOS button during crises.
        </li>
        <li>
          <strong>Family Member / Primary Guardian:</strong> The administrative overseer of the senior's care plan. Guardians can register senior profiles, input and modify medication regimens, schedule doctor consultations, review caregiver shift notes, monitor adherence analytics, and receive real-time SMS alerts during missed doses or SOS activations.
        </li>
        <li>
          <strong>Professional Caregiver:</strong> Certified home nurses, visiting aides, or residential care staff. Caregivers access a mobile-optimized shift dashboard to record completed daily living tasks (hygiene, feeding, mobility), log measured physiological vitals (blood pressure, blood glucose, temperature), administer medication doses, and compile digital shift handover reports for incoming staff.
        </li>
      </ul>
      <div class="page-number">10</div>
    </div>
    """
    pages_html.append(p10)

    # =========================================================================
    # PAGE 11: 2.1 SYSTEM USERS (Part 2)
    # =========================================================================
    p11 = """
    <div class="page" id="page-11">
      <ul>
        <li>
          <strong>Healthcare Provider / Doctor:</strong> Medical specialists, geriatricians, and clinic physicians overseeing the senior's clinical care. Doctors can securely access authorized patient profiles, review longitudinal medication adherence graphs, examine vital sign trends, formulate electronic prescriptions, and document clinical visit notes directly into the patient's archive.
        </li>
        <li>
          <strong>Emergency First Responder / Paramedic:</strong> Emergency medical personnel responding to distress alerts. When an SOS alert is activated, first responders receive an automated, time-limited emergency health token granting immediate read-only access to vital baseline data: blood group, known drug allergies (e.g., Penicillin), chronic conditions, home address, and guardian telephone contacts.
        </li>
        <li>
          <strong>System Administrator:</strong> Technical personnel responsible for maintaining platform integrity, managing user credentials, monitoring database performance, enforcing security policies, inspecting audit trails, and executing automated system backups.
        </li>
      </ul>
      <p>
        All system interactions are governed by a strict Role-Based Access Control (RBAC) engine. Each user role is restricted to its designated data domain, ensuring complete confidentiality of personal medical data while maintaining seamless collaboration across the caregiving network.
      </p>
      <div class="page-number">11</div>
    </div>
    """
    pages_html.append(p11)

    # =========================================================================
    # PAGE 12: 2.2 SYSTEM ARCHITECTURE
    # =========================================================================
    p12 = """
    <div class="page" id="page-12">
      <h2 class="sub-title">2.2 System Architecture</h2>
      <p>
        The Elderly Care Management System is designed following a modern <strong>3-Tier Layered Architecture</strong>, ensuring high maintainability, robust security, scalability, and clean separation of concerns. The architecture comprises three distinct layers:
      </p>
      <ol>
        <li>
          <strong>Presentation Layer (Client Tier):</strong> The top-level interface through which users interact with the system via web browsers on desktop computers, tablets, or smartphones. Built using HTML5, CSS3, and JavaScript, the presentation tier delivers responsive dashboards tailored to user roles. It features senior-accessible typography (large touch targets, high contrast, ARIA screen-reader labels), interactive adherence charts, and asynchronous AJAX form submissions for smooth user experience.
        </li>
        <li>
          <strong>Application / Business Logic Layer (Server Tier):</strong> The middle tier executing core business logic, application routing, and security policies. Developed using PHP 8.2 on an MVC structure, this tier validates inputs, verifies user authentication tokens, coordinates dosage scheduling algorithms, processes caregiver shift handovers, dispatches automated SMS/email alerts via external gateways, and logs all data mutations.
        </li>
        <li>
          <strong>Data & Storage Layer (Database Tier):</strong> The persistence layer consisting of a relational MySQL 8.0 database engine. This layer stores user accounts, senior clinical baselines, medication master lists, scheduled dose logs, doctor appointments, daily care checklists, and emergency SOS audit logs. It enforces strict foreign key constraints, indexes high-frequency queries, and secures sensitive medical data.
        </li>
      </ol>
      <div class="page-number">12</div>
    </div>
    """
    pages_html.append(p12)

    # =========================================================================
    # PAGE 13: FIG 3 & 2.3 SYSTEM MODULES (Part 1)
    # =========================================================================
    p13 = f"""
    <div class="page" id="page-13">
      <div class="diagram-wrapper">
        {svg_diagrams.get_fig3_architecture_svg()}
        <div class="fig-caption">Fig 3: System Architecture [5]</div>
      </div>

      <h2 class="sub-title">2.3 System Modules</h2>
      <p>
        The Elderly Care Management System is divided into eight well-defined, interoperable modules addressing specific caregiving domains:
      </p>
      <p>
        <strong>Module One: User & Role-Based Authentication:</strong> Manages account provisioning, login authentication, password reset workflows, profile customization, and role assignment (Senior, Guardian, Caregiver, Doctor, Admin). It enforces secure session management and access validation across all application endpoints.
      </p>
      <p>
        <strong>Module Two: Elderly Profile & Health Baseline:</strong> Maintains comprehensive digital profiles for seniors, documenting full names, birth dates, blood types, home addresses, GPS coordinates, chronic ailments (e.g., hypertension, diabetes), primary physician details, and critical drug allergy flags.
      </p>
      <p>
        <strong>Module Three: Medication Management & Adherence Tracker:</strong> Enables guardians and doctors to configure medication regimens, specify dosage units, set daily timings, and attach instructions. Generates visual reminders and allows seniors/caregivers to confirm dose consumption with a single click.
      </p>
      <div class="page-number">13</div>
    </div>
    """
    pages_html.append(p13)

    # =========================================================================
    # PAGE 14: 2.3 SYSTEM MODULES (Part 2)
    # =========================================================================
    p14 = """
    <div class="page" id="page-14">
      <p>
        <strong>Module Four: Doctor Appointment & Clinical History:</strong> Streamlines the booking, rescheduling, and tracking of specialist consultations, laboratory diagnostic appointments, and physical therapy sessions. Features digital document uploads for doctor prescriptions, laboratory reports, and discharge summaries.
      </p>
      <p>
        <strong>Module Five: Daily Care Tasks & ADL Routine:</strong> Coordinates non-pharmacological activities of daily living (ADLs). Caregivers and guardians establish daily schedules for personal hygiene, meals, fluid intake, and mobility exercises. Caregivers log task completion and record measured physiological vitals (blood pressure, pulse rate, glucose levels).
      </p>
      <p>
        <strong>Module Six: Caregiver Shift Handoff & Care Notes:</strong> Standardizes the transition between outgoing and incoming care aides. Outgoing staff must document a structured shift report detailing completed tasks, vital trends, senior mood, and pending instructions, requiring digital acknowledgment by the incoming aide and guardian.
      </p>
      <p>
        <strong>Module Seven: Emergency SOS Alert & Notification:</strong> The critical life-safety module. When the senior or caregiver activates the prominent SOS button, the system triggers loud browser audio alarms, sends immediate SMS and email alerts containing GPS coordinates, and generates an emergency medical summary for paramedics.
      </p>
      <p>
        <strong>Module Eight: Family Oversight Dashboard & Reports:</strong> Aggregates care data into visual charts, tracking monthly medication compliance percentages, vital sign stability, and daily task completion. Facilitates one-click PDF report generation for clinical review.
      </p>
      <div class="page-number">14</div>
    </div>
    """
    pages_html.append(p14)

    # =========================================================================
    # PAGE 15: 2.4 SECURITY AND VERIFICATION
    # =========================================================================
    p15 = """
    <div class="page" id="page-15">
      <h2 class="sub-title">2.4 Security and Verification</h2>
      <p>
        Given that the Elderly Care Management System processes sensitive personal and clinical data, security is an essential non-negotiable requirement. The system incorporates multi-layered defensive controls:
      </p>
      <ol>
        <li>
          <strong>Authentication:</strong> All users must register and authenticate using verified email credentials and strong passwords. User passwords are encrypted using one-way cryptographic hashing via <em>Argon2id / Bcrypt</em> with dynamic salting. Passwords are never stored in plain text.
        </li>
        <li>
          <strong>Authorization & RBAC:</strong> Granular Role-Based Access Control ensures that users can only access endpoints and data authorized for their role. Caregivers cannot alter medical prescriptions, seniors cannot access administrative settings, and doctors can only inspect assigned patient records.
        </li>
        <li>
          <strong>Session Management:</strong> Authenticated sessions use cryptographically random 128-bit session tokens stored with <code>HttpOnly</code>, <code>SameSite=Strict</code>, and <code>Secure</code> flags to prevent cross-site scripting (XSS) session hijacking. Inactive sessions automatically expire after 20 minutes.
        </li>
        <li>
          <strong>Input Validation & SQL Injection Prevention:</strong> All client inputs undergo strict server-side validation and sanitization. All database interactions utilize PHP Data Objects (PDO) with parameterized prepared statements, preventing SQL injection vulnerabilities.
        </li>
        <li>
          <strong>Data Protection & Audit Trail:</strong> All communications operate over encrypted HTTPS/TLS 1.3 channels. Critical events—such as medication schedule changes, dose cancellations, and SOS activations—are logged in an immutable audit table with timestamps and user IP addresses.
        </li>
      </ol>
      <div class="page-number">15</div>
    </div>
    """
    pages_html.append(p15)

    # =========================================================================
    # PAGE 16: 2.5 SOFTWARE DEVELOPMENT TOOLS
    # =========================================================================
    p16 = """
    <div class="page" id="page-16">
      <h2 class="sub-title">2.5 Software Development Tools</h2>
      <p>
        The system is constructed using modern, industry-standard development technologies chosen for reliability, security, accessibility, and high performance:
      </p>
      <table class="data-table">
        <thead>
          <tr>
            <th style="width: 22%;">Category</th>
            <th style="width: 25%;">Tools/Technology</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Frontend</strong></td>
            <td>HTML5, CSS3, JavaScript (ES6+)</td>
            <td>Constructs responsive semantic markup, senior-accessible visual styling (WCAG AA), audio alerts, and interactive DOM manipulation.</td>
          </tr>
          <tr>
            <td><strong>Backend</strong></td>
            <td>PHP 8.2</td>
            <td>Implements MVC architecture, RESTful routing, domain business logic, cryptographic hashing, and database communication.</td>
          </tr>
          <tr>
            <td><strong>Database</strong></td>
            <td>MySQL 8.0</td>
            <td>Provides ACID-compliant relational data storage, foreign key enforcement, indexing, and transactional data integrity.</td>
          </tr>
          <tr>
            <td><strong>Server & Staging</strong></td>
            <td>Apache / XAMPP</td>
            <td>Hosts local and staging application servers, managing virtual hosts and HTTP request lifecycles.</td>
          </tr>
          <tr>
            <td><strong>Design & Modeling</strong></td>
            <td>Draw.io / Lucidchart</td>
            <td>Used for designing system architecture, ER diagrams, DFD data pipelines, and UML Use Case diagrams.</td>
          </tr>
          <tr>
            <td><strong>Version Control</strong></td>
            <td>Git & GitHub</td>
            <td>Maintains source code versioning, branch management, collaborative tracking, and milestone releases.</td>
          </tr>
          <tr>
            <td><strong>Testing Tools</strong></td>
            <td>PHPUnit, Chrome DevTools</td>
            <td>Executes backend unit testing, API endpoint validation, accessibility checks, and frontend performance profiling.</td>
          </tr>
          <tr>
            <td><strong>Notification Service</strong></td>
            <td>Twilio SMS API / SMTP</td>
            <td>Dispatches real-time SMS distress messages and email alerts for emergency SOS and medication notifications.</td>
          </tr>
        </tbody>
      </table>
      <div class="page-number">16</div>
    </div>
    """
    pages_html.append(p16)

    # =========================================================================
    # PAGE 17: 2.6 ADVANTAGES OF USING THE SYSTEM
    # =========================================================================
    p17 = """
    <div class="page" id="page-17">
      <h2 class="sub-title">2.6 Advantages of Using The System</h2>
      <ol>
        <li>
          <strong>Elimination of Paperwork & Administrative Burdens:</strong> Eliminates physical prescription slips, paper notebooks, and unstructured medication logs. All care data is structured and immediately retrievable.
        </li>
        <li>
          <strong>Dramatic Reduction in Geriatric Medication Errors:</strong> Synchronized dosage schedules, loud audio-visual reminders, and single-click dose confirmations eliminate missed doses and prevent accidental overdoses.
        </li>
        <li>
          <strong>Unbroken Transparency for Working Family Guardians:</strong> Enables family members to view real-time adherence logs and care activities from their workplace or mobile phones, completely removing caregiver anxiety.
        </li>
        <li>
          <strong>Caregiver Accountability and Seamless Shift Continuity:</strong> Digital shift handoffs and mandatory vital sign logging ensure visiting staff are held accountable and that critical clinical changes are communicated.
        </li>
        <li>
          <strong>Rapid Emergency Crisis Intervention:</strong> The one-touch SOS button bypasses complicated smartphone navigation, broadcasting GPS locations and medical allergy briefs to paramedics and family within seconds.
        </li>
        <li>
          <strong>Empirical Data for Medical Consultations:</strong> Provides visiting physicians with verified, longitudinal adherence records and physiological trends, improving diagnosis and therapeutic outcomes.
        </li>
      </ol>
      <div class="page-number">17</div>
    </div>
    """
    pages_html.append(p17)

    # =========================================================================
    # PAGE 18: 3. SYSTEM LIFE CYCLE & 3.1 SDLC
    # =========================================================================
    p18 = """
    <div class="page" id="page-18">
      <h1 class="sec-title">System Life Cycle</h1>
      <h2 class="sub-title">3.1 Software Development Life Cycle</h2>
      <p>
        The development of the Elderly Care Management System adheres to a structured <strong>Waterfall / Iterative SDLC</strong> methodology. Because healthcare software directly impacts patient wellbeing and life safety, a systematic, phased engineering approach is required to guarantee clinical accuracy, requirement stability, and rigorous testing before production deployment.
      </p>

      <h3 class="subsub-title">3.1.1 SDLC Phases</h3>
      <ol>
        <li>
          <strong>Requirement Analysis:</strong> In this opening phase, comprehensive user requirements were elicited through geriatric literature review, family guardian interviews, and clinical safety guidelines. Requirements were classified, refined, and documented in this formal specification.
        </li>
        <li>
          <strong>System Design:</strong> Translates verified requirements into detailed technical blueprints. Involves modeling 3-tier architecture, designing normalized relational database schemas (ERD), mapping data flows (DFD), formulating subsystem use cases, and creating accessible wireframes.
        </li>
        <li>
          <strong>Implementation (Coding):</strong> Modular construction of frontend interfaces (HTML5/CSS3/JS) and backend domain controllers (PHP 8.2, MySQL). Core modules—Authentication, Medication, Appointments, Care Routines, and Emergency SOS—are programmed following PSR-12 coding conventions.
        </li>
        <li>
          <strong>Testing & Quality Assurance:</strong> Rigorous validation including unit tests, integration tests across database boundaries, usability testing with senior personas, security vulnerability audits, and latency simulations for the SOS dispatch engine.
        </li>
        <li>
          <strong>Deployment & Release:</strong> Deploying the verified application onto a production cloud server environment configured with HTTPS/TLS certificates, database indexing, and automated backup cron jobs.
        </li>
        <li>
          <strong>Maintenance & Evolution:</strong> Post-release monitoring, server performance tuning, periodic security patch installation, and ongoing feature refinements based on stakeholder feedback.
        </li>
      </ol>
      <div class="page-number">18</div>
    </div>
    """
    pages_html.append(p18)

    # =========================================================================
    # PAGE 19: FIG 4: SDLC PROCESS DIAGRAM
    # =========================================================================
    p19 = f"""
    <div class="page" id="page-19">
      <div class="diagram-wrapper">
        {svg_diagrams.get_fig4_sdlc_svg()}
        <div class="fig-caption">Fig 4: SDLC Process Diagram</div>
      </div>
      <p>
        As illustrated in Figure 4, the software engineering process progresses through six clearly defined stages. The iterative feedback loop between the Testing phase and the System Design / Implementation phases ensures that any edge-case bugs, usability bottlenecks, or accessibility shortcomings identified during verification are immediately rectified prior to final deployment. This disciplined lifecycle ensures high software reliability, data integrity, and compliance with academic and professional standards.
      </p>
      <div class="page-number">19</div>
    </div>
    """
    pages_html.append(p19)

    # =========================================================================
    # PAGE 20: 4. REQUIREMENT ENGINEERING & 4.1 & 4.2 & 4.2.1
    # =========================================================================
    p20 = """
    <div class="page" id="page-20">
      <h1 class="sec-title">Requirement Engineering</h1>
      <p>
        Requirement Engineering ensures that system requirements are systematically gathered, analyzed, refined, resolved of ambiguities, and documented with absolute clarity.
      </p>

      <h2 class="sub-title">4.1 Requirement Elicitation</h2>
      <p>
        During the elicitation phase, multi-source techniques were employed:
      </p>
      <ul>
        <li>
          <strong>Stakeholder Interviews:</strong> Conducted in-depth interviews with family guardians managing eldercare and professional home caregivers to identify everyday pain points, forgotten tasks, and emergency vulnerabilities.
        </li>
        <li>
          <strong>Domain Documentation Review:</strong> Reviewed geriatric clinical guidelines, traditional paper medication charts, and caregiver handoff logs to understand the essential data entities and regulatory standards.
        </li>
        <li>
          <strong>Direct Observation:</strong> Observed typical daily routines of senior citizens, noting visual, cognitive, and physical interaction constraints that dictate accessibility design.
        </li>
      </ul>

      <h2 class="sub-title">4.2 Requirement Analysis</h2>
      <h3 class="subsub-title">4.2.1 Feasibility Study</h3>
      <p>
        A rigorous feasibility assessment was conducted across four primary dimensions:
      </p>
      <p>
        <strong>Technical Feasibility:</strong> The technology stack (PHP, MySQL, HTML5/CSS3, JavaScript, Twilio API) consists of proven, open-source technologies capable of sub-second query execution, low memory overhead, and responsive rendering on all modern web browsers without specialized hardware.
      </p>
      <p>
        <strong>Economic Feasibility:</strong> The platform utilizes open-source development frameworks and database engines, avoiding costly licensing fees. Operational cloud hosting expenses are minimal, while the return on investment (ROI)—measured in preventable emergency medical hospitalizations—is substantial.
      </p>
      <p>
        <strong>Operational Feasibility:</strong> The interface incorporates large typography, high contrast, and simplified single-click workflows specifically tailored for non-technical seniors and busy caregivers, ensuring rapid adoption and low training barriers.
      </p>
      <div class="page-number">20</div>
    </div>
    """
    pages_html.append(p20)

    # =========================================================================
    # PAGE 21: 4.2.1 (Schedule) & 4.2.2 & 4.2.3
    # =========================================================================
    p21 = """
    <div class="page" id="page-21">
      <p>
        <strong>Schedule Feasibility:</strong> The project scope has been structured into modular sprints executable within the academic semester timeframe (12 weeks / 48 working days), ensuring timely delivery of all documentation, database models, and functional modules.
      </p>

      <h3 class="subsub-title">4.2.2 Requirement Classification</h3>
      <p>
        All gathered requirements were systematically classified into three distinct categories:
      </p>
      <ol>
        <li>
          <strong>Functional Requirements:</strong> Core capabilities including user authentication, senior profile management, medication scheduling, adherence logging, clinic appointments, daily care checklists, caregiver shift handoffs, and emergency SOS dispatch.
        </li>
        <li>
          <strong>Non-Functional Requirements:</strong> Operational constraints and quality attributes including performance (page load &lt; 2s), security (Argon2id hashing, TLS 1.3), reliability (99.9% uptime), accessibility (WCAG 2.1 AA), and data integrity.
        </li>
        <li>
          <strong>User Interface Requirements:</strong> Ergonomic design criteria including high-contrast color palettes, 18px+ font options, prominent touch targets, and responsive cross-device layouts.
        </li>
      </ol>

      <h3 class="subsub-title">4.2.3 Conflict and Redundancy Resolution</h3>
      <p>
        During stakeholder elicitation, several operational conflicts were identified and resolved:
      </p>
      <ul>
        <li>
          <em>Conflict:</em> Caregivers requested rapid single-click shift logging, whereas Guardians demanded granular vital records. <em>Resolution:</em> Implemented smart pre-populated forms with mandatory vital fields and optional detailed notes.
        </li>
        <li>
          <em>Conflict:</em> Modification of medication schedules. <em>Resolution:</em> Restricted prescription schedule alterations exclusively to Guardians and Doctors; caregivers are restricted to logging administration events with explanatory rationale.
        </li>
      </ul>
      <div class="page-number">21</div>
    </div>
    """
    pages_html.append(p21)

    # =========================================================================
    # PAGE 22: 4.3 REQUIREMENT DOCUMENTATION
    # =========================================================================
    p22 = """
    <div class="page" id="page-22">
      <h2 class="sub-title">4.3 Requirement Documentation</h2>
      <p>
        The documented specifications established in this Software Requirements Specification comprise the following comprehensive artifacts:
      </p>
      <ol>
        <li>
          <strong>Full Functional and Non-Functional Catalog:</strong> Detailed descriptions of all user capabilities and operational quality attributes.
        </li>
        <li>
          <strong>Structured Feature Specification Table:</strong> Complete matrix identifying feature IDs, descriptions, preconditions, roles, and priority levels.
        </li>
        <li>
          <strong>Architectural & Process Diagrams:</strong> High-resolution 3-Tier Architecture Diagram, SDLC Process Model, Entity Relationship Diagram (ERD), and Data Flow Diagrams (DFD Context and Level 1).
        </li>
        <li>
          <strong>UML Behavioral Use Case Diagrams:</strong> Complete subsystem use case models covering User Management, Medication Management, Appointment Scheduling, and Daily Care & Emergency SOS.
        </li>
        <li>
          <strong>Detailed Use Case Narration Tables:</strong> Comprehensive step-by-step actor events, system responses, alternative flows, and post-conditions for all critical use cases.
        </li>
        <li>
          <strong>Process-to-Entity CRUD Matrix:</strong> Explicit mapping of Create, Read, Update, and Delete permissions across user roles and data stores.
        </li>
        <li>
          <strong>Activity Schedule & Gantt Chart:</strong> Complete work breakdown structure (Activities A through Q) mapped against academic delivery milestones.
        </li>
        <li>
          <strong>Strategic Result Analysis:</strong> Comprehensive SWOT Analysis and Risk Mitigation Matrix addressing technical, operational, and clinical risks.
        </li>
      </ol>
      <div class="page-number">22</div>
    </div>
    """
    pages_html.append(p22)

    # =========================================================================
    # PAGE 23: 5. FUNCTIONAL REQUIREMENTS & 5.1 (Part 1)
    # =========================================================================
    p23 = """
    <div class="page" id="page-23">
      <h1 class="sec-title">Functional requirements</h1>
      <p>
        The Elderly Care Management System enables seniors, family guardians, professional caregivers, and healthcare providers to register accounts, authenticate securely, and manage all dimensions of geriatric care via the web. The functional requirements are organized into sixteen modular features:
      </p>

      <h2 class="sub-title">5.1 Feature List with Description</h2>
      <p>
        <strong>1. User Account Registration & Provisioning:</strong> Allows family guardians, caregivers, and medical practitioners to create new accounts by providing full name, email address, contact phone number, and a secure password. The system validates uniqueness and sets account status.
      </p>
      <p>
        <strong>2. Role-Based Login & Session Control:</strong> Authenticates registered users based on their assigned role (Senior, Guardian, Caregiver, Doctor, Admin). Generates secure session tokens, enforces login attempt limits, and directs users to their tailored dashboard.
      </p>
      <p>
        <strong>3. Senior Health Profile Management:</strong> Enables guardians to create and update comprehensive digital profiles for senior relatives. Stores date of birth, blood group, known drug allergies, primary physician, home address, and GPS coordinates.
      </p>
      <p>
        <strong>4. Medication Master List & Dosage Scheduling:</strong> Allows guardians and doctors to input prescribed medications, brand names, generic formulations, dosage units (e.g., 50mg, 1 tablet), daily frequency (morning, afternoon, night), and meal instructions.
      </p>
      <div class="page-number">23</div>
    </div>
    """
    pages_html.append(p23)

    # =========================================================================
    # PAGE 24: 5.1 (Part 2)
    # =========================================================================
    p24 = """
    <div class="page" id="page-24">
      <p>
        <strong>5. Real-Time Dose Adherence Logging:</strong> Provides intuitive controls for seniors or caregivers to mark scheduled medication doses as 'Taken', 'Missed', or 'Skipped' with a single tap, recording exact timestamps and mandatory omission notes.
      </p>
      <p>
        <strong>6. Automated Dosage Audio-Visual Reminders:</strong> Displays prominent visual alarm banners and plays audio chimes 15 minutes prior to scheduled medication times, alerting seniors even if they are in another room.
      </p>
      <p>
        <strong>7. Doctor Appointment Scheduling & Calendar:</strong> Enables guardians to schedule clinical consultations, hospital checkups, and diagnostic tests. Displays an interactive monthly calendar with automated email/SMS reminders.
      </p>
      <p>
        <strong>8. Digital Prescription & Medical Document Archive:</strong> Provides encrypted cloud storage for uploading scanned doctor prescriptions, blood test results, and hospital discharge summaries, accessible to authorized doctors and family members.
      </p>
      <p>
        <strong>9. Activities of Daily Living (ADL) Care Checklist:</strong> Establishes a daily routine checklist for visiting caregivers and seniors, tracking essential non-medical tasks including bathing, oral hygiene, meals, fluid intake, and mobility exercises.
      </p>
      <p>
        <strong>10. Physiological Vital Signs Logging:</strong> Allows caregivers to record measured vital signs (systolic/diastolic blood pressure, pulse rate, blood glucose, body temperature), automatically flagging abnormal clinical readings in red.
      </p>
      <div class="page-number">24</div>
    </div>
    """
    pages_html.append(p24)

    # =========================================================================
    # PAGE 25: 5.1 (Part 3) & 5.2 FEATURE TABLE (Part 1)
    # =========================================================================
    p25 = """
    <div class="page" id="page-25">
      <p>
        <strong>11. Caregiver Shift Handoff & Care Notes:</strong> Mandates outgoing caregivers to submit an electronic shift handover summary documenting completed tasks, vital trends, patient mood, and pending items, requiring digital sign-off from incoming staff.
      </p>
      <p>
        <strong>12. Instant Emergency SOS Alert & Multichannel Broadcast:</strong> Prominent one-touch panic button that instantly dispatches browser alarms, SMS messages, and emails with live GPS coordinates and emergency clinical briefs to guardians and paramedics.
      </p>
      <p>
        <strong>13. Family Guardian Monitoring Dashboard:</strong> Consolidates daily adherence rates, vital trends, and caregiver logs into intuitive visual graphs for working family members.
      </p>

      <h2 class="sub-title">5.2 Feature Table</h2>
      <table class="data-table">
        <thead>
          <tr>
            <th style="width: 14%;">Feature ID</th>
            <th style="width: 26%;">Feature Name</th>
            <th>Description</th>
            <th style="width: 18%;">Precondition</th>
            <th style="width: 14%;">Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>FR-01</strong></td>
            <td>User Registration</td>
            <td>Register new user accounts with role selection</td>
            <td>Valid email & phone</td>
            <td>All Users</td>
          </tr>
          <tr>
            <td><strong>FR-02</strong></td>
            <td>Login Authentication</td>
            <td>Verify credentials and initiate secure session</td>
            <td>Active account</td>
            <td>All Users</td>
          </tr>
          <tr>
            <td><strong>FR-03</strong></td>
            <td>Senior Profile Setup</td>
            <td>Create and manage senior clinical baseline</td>
            <td>Guardian logged in</td>
            <td>Guardian</td>
          </tr>
          <tr>
            <td><strong>FR-04</strong></td>
            <td>Medication Scheduling</td>
            <td>Configure dosage, timing, and meal rules</td>
            <td>Senior profile exists</td>
            <td>Guardian, Doctor</td>
          </tr>
        </tbody>
      </table>
      <div class="page-number">25</div>
    </div>
    """
    pages_html.append(p25)

    # =========================================================================
    # PAGE 26: 5.2 FEATURE TABLE (Part 2)
    # =========================================================================
    p26 = """
    <div class="page" id="page-26">
      <table class="data-table">
        <thead>
          <tr>
            <th style="width: 14%;">Feature ID</th>
            <th style="width: 26%;">Feature Name</th>
            <th>Description</th>
            <th style="width: 18%;">Precondition</th>
            <th style="width: 14%;">Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>FR-05</strong></td>
            <td>Dose Adherence Logging</td>
            <td>Log dose as Taken, Missed, or Skipped</td>
            <td>Scheduled dose exists</td>
            <td>Senior, Caregiver</td>
          </tr>
          <tr>
            <td><strong>FR-06</strong></td>
            <td>Dosage Audio Reminders</td>
            <td>Audio chimes and visual alert banners</td>
            <td>Upcoming dosage time</td>
            <td>System, Senior</td>
          </tr>
          <tr>
            <td><strong>FR-07</strong></td>
            <td>Appointment Scheduling</td>
            <td>Book and track doctor clinical consultations</td>
            <td>Senior profile exists</td>
            <td>Guardian, Doctor</td>
          </tr>
          <tr>
            <td><strong>FR-08</strong></td>
            <td>Prescription Archive</td>
            <td>Upload and view digital prescription scans</td>
            <td>Appointment / Visit</td>
            <td>Doctor, Guardian</td>
          </tr>
          <tr>
            <td><strong>FR-09</strong></td>
            <td>Daily ADL Checklist</td>
            <td>Structure and track meals, hygiene, mobility</td>
            <td>Active senior care plan</td>
            <td>Caregiver, Senior</td>
          </tr>
          <tr>
            <td><strong>FR-10</strong></td>
            <td>Vitals Logging</td>
            <td>Record BP, pulse, glucose with anomaly flags</td>
            <td>Caregiver on duty</td>
            <td>Caregiver</td>
          </tr>
        </tbody>
      </table>
      <div class="page-number">26</div>
    </div>
    """
    pages_html.append(p26)

    # =========================================================================
    # PAGE 27: 5.2 FEATURE TABLE (Part 3)
    # =========================================================================
    p27 = """
    <div class="page" id="page-27">
      <table class="data-table">
        <thead>
          <tr>
            <th style="width: 14%;">Feature ID</th>
            <th style="width: 26%;">Feature Name</th>
            <th>Description</th>
            <th style="width: 18%;">Precondition</th>
            <th style="width: 14%;">Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>FR-11</strong></td>
            <td>Shift Handoff Notes</td>
            <td>Outgoing caregiver logs shift summary</td>
            <td>End of care shift</td>
            <td>Caregiver, Guardian</td>
          </tr>
          <tr>
            <td><strong>FR-12</strong></td>
            <td>Emergency SOS Trigger</td>
            <td>One-touch panic button for medical crises</td>
            <td>Any system screen</td>
            <td>Senior, Caregiver</td>
          </tr>
          <tr>
            <td><strong>FR-13</strong></td>
            <td>Multichannel SOS Alert</td>
            <td>Broadcast SMS, email, and GPS coordinates</td>
            <td>SOS button triggered</td>
            <td>System</td>
          </tr>
          <tr>
            <td><strong>FR-14</strong></td>
            <td>Family Live Dashboard</td>
            <td>Central monitoring of vitals and adherence</td>
            <td>Guardian logged in</td>
            <td>Guardian</td>
          </tr>
          <tr>
            <td><strong>FR-15</strong></td>
            <td>PDF Compliance Export</td>
            <td>Export monthly health and adherence report</td>
            <td>Adherence data exists</td>
            <td>Guardian, Doctor</td>
          </tr>
          <tr>
            <td><strong>FR-16</strong></td>
            <td>System Audit Logging</td>
            <td>Log all user operations and mutations</td>
            <td>User action performed</td>
            <td>System, Admin</td>
          </tr>
        </tbody>
      </table>
      <div class="page-number">27</div>
    </div>
    """
    pages_html.append(p27)

    # =========================================================================
    # PAGE 28: 6. SYSTEM SPECIFICATION DIAGRAMS & 6.1 ERD
    # =========================================================================
    p28 = f"""
    <div class="page" id="page-28">
      <h1 class="sec-title">System Specification Diagrams</h1>
      <h2 class="sub-title">6.1 Entity Relationship Diagram</h2>
      <p>
        The Entity Relationship Diagram (ERD) defines the relational database architecture supporting the Elderly Care Management System. The schema is fully normalized to Third Normal Form (3NF), ensuring data integrity, elimination of update anomalies, and efficient indexing across primary and foreign key constraints.
      </p>
      <div class="diagram-wrapper">
        {svg_diagrams.get_fig5_erd_svg()}
        <div class="fig-caption">Fig 5: ER Diagram</div>
      </div>
      <div class="page-number">28</div>
    </div>
    """
    pages_html.append(p28)

    # =========================================================================
    # PAGE 29: 6.3 DATA FLOW DIAGRAM
    # =========================================================================
    p29 = f"""
    <div class="page" id="page-29">
      <h2 class="sub-title">6.3 Data Flow Diagram</h2>
      <p>
        The Data Flow Diagram illustrates how information flows through the system, transitioning from external entities (Senior, Guardian, Caregiver, Doctor, Paramedics) through central application processes and into persistent relational data stores.
      </p>
      <div class="diagram-wrapper">
        {svg_diagrams.get_fig6_dfd_svg()}
        <div class="fig-caption">Fig 6: Data Flow Diagram</div>
      </div>
      <div class="page-number">29</div>
    </div>
    """
    pages_html.append(p29)

    # =========================================================================
    # PAGE 30: 6.4 USE CASE DIAGRAM & 6.4.1
    # =========================================================================
    p30 = f"""
    <div class="page" id="page-30">
      <h1 class="sec-title">6.4 Use Case Diagram</h1>
      <h2 class="sub-title">6.4.1 User Management Subsystem</h2>
      <p>
        The User Management Subsystem governs account creation, credential verification, profile updates, and role-based access enforcement for Seniors, Guardians, Caregivers, Doctors, and Administrators.
      </p>
      <div class="diagram-wrapper">
        {svg_diagrams.get_fig7_uc_usermgmt_svg()}
        <div class="fig-caption">Fig 7: User Management Subsystem Use Case Diagram</div>
      </div>
      <div class="page-number">30</div>
    </div>
    """
    pages_html.append(p30)

    # =========================================================================
    # PAGE 31: 6.4.2 MEDICATION & 6.4.3 APPOINTMENT USE CASE DIAGRAMS
    # =========================================================================
    p31 = f"""
    <div class="page" id="page-31">
      <h2 class="sub-title" style="margin-top: 0;">6.4.2 Medication Management Subsystem</h2>
      <div class="diagram-wrapper">
        {svg_diagrams.get_fig8_uc_medmgmt_svg()}
        <div class="fig-caption">Fig 8: Medication Management Subsystem Use Case Diagram</div>
      </div>

      <h2 class="sub-title">6.4.3 Appointment Scheduling Subsystem</h2>
      <div class="diagram-wrapper">
        {svg_diagrams.get_fig9_uc_apptmgt_svg()}
        <div class="fig-caption">Fig 9: Appointment Scheduling Subsystem Use Case Diagram</div>
      </div>
      <div class="page-number">31</div>
    </div>
    """
    pages_html.append(p31)

    # =========================================================================
    # PAGE 32: 6.4.4 DAILY CARE & EMERGENCY SOS USE CASE DIAGRAM
    # =========================================================================
    p32 = f"""
    <div class="page" id="page-32">
      <h2 class="sub-title" style="margin-top: 0;">6.4.4 Daily Care & Emergency SOS Subsystem</h2>
      <p>
        This life-safety subsystem encompasses daily living routine coordination, caregiver vital logging, shift handover note compilation, and instantaneous one-touch Emergency SOS distress broadcasting with GPS coordinates.
      </p>
      <div class="diagram-wrapper">
        {svg_diagrams.get_fig10_uc_care_sos_svg()}
        <div class="fig-caption">Fig 10: Daily Care & Emergency SOS Subsystem Use Case Diagram</div>
      </div>
      <div class="page-number">32</div>
    </div>
    """
    pages_html.append(p32)

    # =========================================================================
    # PAGE 33: 6.5 USE CASE NARRATION - UC-01 CREATE ACCOUNT
    # =========================================================================
    p33 = """
    <div class="page" id="page-33">
      <h1 class="sec-title">6.5 Use Case Narration Table</h1>
      <h2 class="sub-title">6.5.1 User Management Subsystem Use Case Narration Table</h2>

      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>Create Account</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Family Guardian, Caregiver, Doctor</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Users register a new account on the Elderly Care Management System by providing identification and credentials.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>User must not have an existing active account with the provided email. User must provide valid registration data.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. User navigates to Registration page and inputs full name, email, phone number, role, and password.</td>
                  <td>2. System validates input formats, password strength, and verifies email uniqueness.</td>
                </tr>
                <tr>
                  <td>3. User clicks "Create Account" button.</td>
                  <td>4. System hashes password with Argon2id, creates database record, and displays success confirmation.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 02:</strong> System displays error "Email is already registered. Please login."<br>
            <strong>Alt 04:</strong> System highlights invalid phone number or weak password and prompts correction.
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>New user account is created in the database and the user can log in to their dashboard.</td>
        </tr>
      </table>
      <div class="page-number">33</div>
    </div>
    """
    pages_html.append(p33)

    # =========================================================================
    # PAGE 34: UC-02 LOGIN
    # =========================================================================
    p34 = """
    <div class="page" id="page-34">
      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>Login</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Senior, Family Guardian, Caregiver, Doctor, Admin</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Users authenticate into the system to access role-specific caregiving and oversight features.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>A valid registered user account must exist.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. User enters registered email/phone and password on login screen.</td>
                  <td>2. System verifies credentials against stored cryptographic hash.</td>
                </tr>
                <tr>
                  <td>3. User clicks "Login" button.</td>
                  <td>4. System creates authenticated session and loads role-tailored dashboard.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 02:</strong> System displays "Invalid email or password" and increments failed attempts counter.<br>
            <strong>Alt 04:</strong> Account locked temporarily after 5 consecutive failed attempts for security.
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>User is granted an active session and access to authorized features based on their assigned role.</td>
        </tr>
      </table>
      <div class="page-number">34</div>
    </div>
    """
    pages_html.append(p34)

    # =========================================================================
    # PAGE 35: UC-03 EDIT HEALTH PROFILE
    # =========================================================================
    p35 = """
    <div class="page" id="page-35">
      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>Edit Profile & Medical Baseline</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Family Guardian</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Family Guardian updates senior personal details, home address, emergency contacts, blood group, and chronic conditions.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>Guardian must be logged in. A senior profile must exist under the guardian's management.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. Guardian navigates to "Senior Profile" and clicks "Edit Baseline".</td>
                  <td>2. System loads current profile fields in editable form.</td>
                </tr>
                <tr>
                  <td>3. Guardian updates emergency phone, address, or chronic ailments and clicks "Save Changes".</td>
                  <td>4. System validates inputs, updates database, and displays "Profile updated successfully".</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 04:</strong> If mandatory emergency phone number is blank, system displays validation warning and prevents submission.
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>Updated senior baseline and emergency contact details are committed to the database and immediately visible to caregivers.</td>
        </tr>
      </table>
      <div class="page-number">35</div>
    </div>
    """
    pages_html.append(p35)

    # =========================================================================
    # PAGE 36: UC-04 VIEW USER & CAREGIVER LIST
    # =========================================================================
    p36 = """
    <div class="page" id="page-36">
      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>View User & Caregiver List</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Family Guardian, System Administrator</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Guardian or Administrator inspects the list of registered caregivers, seniors, and active care personnel.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>User must be logged in as Family Guardian or System Administrator.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. User navigates to "Care Team Directory" screen.</td>
                  <td>2. System queries database and retrieves assigned caregivers and contact details.</td>
                </tr>
                <tr>
                  <td>3. User reviews caregiver credentials, contact numbers, and shift assignments.</td>
                  <td>4. System provides options to contact, assign new shifts, or revoke caregiver access.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 02:</strong> If no caregivers are currently assigned, system displays message "No caregivers assigned yet. Click Assign Caregiver to invite staff."
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>Authorized user has complete oversight of all personnel interacting with the senior.</td>
        </tr>
      </table>
      <div class="page-number">36</div>
    </div>
    """
    pages_html.append(p36)

    # =========================================================================
    # PAGE 37: 6.5.2 UC-05 ADD MEDICATION & SCHEDULE
    # =========================================================================
    p37 = """
    <div class="page" id="page-37">
      <h2 class="sub-title">6.5.2 Medication Management Subsystem Use Case Narration Table</h2>

      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>Add Medication & Dosage Schedule</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Family Guardian, Healthcare Provider / Doctor</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Guardian or Doctor inputs a new prescription regimen, specifying medication name, dosage amount, timing, and meal relation.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>User must be logged in as Guardian or Doctor. Senior profile must exist.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. User opens "Add Medication" screen.</td>
                  <td>2. System displays prescription configuration form.</td>
                </tr>
                <tr>
                  <td>3. User enters drug name (e.g., Amlodipine), dose (5mg), schedule times (08:00 AM, 08:00 PM), meal rule (After breakfast), and clicks "Save Schedule".</td>
                  <td>4. System validates entries, creates dosage schedule records in database, and initializes daily reminder alarms.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 04:</strong> If dose timing is unselected, system highlights missing required timing and prompts completion.
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>New medication schedule is saved and scheduled reminder alarms appear on senior and caregiver dashboards.</td>
        </tr>
      </table>
      <div class="page-number">37</div>
    </div>
    """
    pages_html.append(p37)

    # =========================================================================
    # PAGE 38: UC-06 LOG DOSE TAKEN / MISSED
    # =========================================================================
    p38 = """
    <div class="page" id="page-38">
      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>Log Dose Taken / Missed</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Elderly Senior, Professional Caregiver</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Senior or Caregiver records whether a scheduled medication dose was consumed, missed, or skipped.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>A scheduled medication dose event must exist for the current date and time.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. When reminder triggers, user clicks large green "Taken" button (or "Missed/Skipped").</td>
                  <td>2. System prompts for optional note (mandatory reason if Skipped).</td>
                </tr>
                <tr>
                  <td>3. User confirms action.</td>
                  <td>4. System writes timestamped dose log to database, updates adherence stats, and silences reminder alarm.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 01:</strong> If dose remains unconfirmed 30 minutes after scheduled time, system marks status as "Pending Warning" and alerts Guardian.
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>Dose status is permanently recorded in the adherence log and updated in the Guardian's live feed.</td>
        </tr>
      </table>
      <div class="page-number">38</div>
    </div>
    """
    pages_html.append(p38)

    # =========================================================================
    # PAGE 39: UC-07 VIEW MEDICATION ADHERENCE HISTORY
    # =========================================================================
    p39 = """
    <div class="page" id="page-39">
      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>View Medication Adherence Record</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Family Guardian, Healthcare Provider / Doctor</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Guardian or Doctor reviews weekly and monthly compliance rates, tracking taken vs missed doses.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>Historical dose logging records must exist in the database.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. User navigates to "Medication Adherence History" panel.</td>
                  <td>2. System calculates compliance percentage and renders monthly adherence calendar.</td>
                </tr>
                <tr>
                  <td>3. User filters by specific medication or date range.</td>
                  <td>4. System displays granular log table with exact timestamps, status, and caregiver notes.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 02:</strong> If adherence falls below 80%, system displays prominent clinical advisory flag recommending guardian review.
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>User gains full visibility into pharmacological adherence trends.</td>
        </tr>
      </table>
      <div class="page-number">39</div>
    </div>
    """
    pages_html.append(p39)

    # =========================================================================
    # PAGE 40: 6.5.3 UC-09 SCHEDULE APPOINTMENT
    # =========================================================================
    p40 = """
    <div class="page" id="page-40">
      <h2 class="sub-title">6.5.3 Appointment Scheduling Subsystem Use Case Narration Table</h2>

      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>Schedule Doctor Appointment</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Family Guardian, Healthcare Provider / Doctor</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Guardian books a medical consultation, diagnostic test, or hospital follow-up for the senior.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>Senior profile must exist. Guardian or Doctor must be logged in.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. Guardian clicks "Book Doctor Appointment".</td>
                  <td>2. System displays appointment entry form.</td>
                </tr>
                <tr>
                  <td>3. Guardian inputs doctor name, clinic address, appointment date, time, and reason for visit.</td>
                  <td>4. System validates date, saves appointment record, and sets automated reminder notifications.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 04:</strong> If selected date is in the past, system rejects entry with error "Appointment date must be in the future."
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>Appointment is confirmed, listed on the family calendar, and scheduled reminders are queued.</td>
        </tr>
      </table>
      <div class="page-number">40</div>
    </div>
    """
    pages_html.append(p40)

    # =========================================================================
    # PAGE 41: UC-10 VIEW UPCOMING APPOINTMENTS
    # =========================================================================
    p41 = """
    <div class="page" id="page-41">
      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>View Upcoming Appointments</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Family Guardian, Senior, Caregiver</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Users inspect the schedule of upcoming hospital visits, doctor consultations, and diagnostic tests.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>User must be logged in. Scheduled appointment records must exist.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. User opens "Appointments" screen.</td>
                  <td>2. System fetches all scheduled consultations ordered chronologically.</td>
                </tr>
                <tr>
                  <td>3. User selects a specific appointment card.</td>
                  <td>4. System displays full doctor credentials, clinic address, visit objective, and directions.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 02:</strong> If no upcoming appointments exist, system displays "No upcoming visits scheduled. Click Schedule to add an appointment."
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>All stakeholders are informed of upcoming clinic dates, ensuring timely transportation and preparation.</td>
        </tr>
      </table>
      <div class="page-number">41</div>
    </div>
    """
    pages_html.append(p41)

    # =========================================================================
    # PAGE 42: UC-11 RESCHEDULE / CANCEL APPOINTMENT
    # =========================================================================
    p42 = """
    <div class="page" id="page-42">
      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>Update / Reschedule Appointment</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Family Guardian, Doctor</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Guardian or Doctor updates the date, time, clinic location, or cancels a scheduled medical consultation.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>An active scheduled appointment must exist.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. User selects appointment and clicks "Reschedule" (or "Cancel").</td>
                  <td>2. System opens editable schedule dialog.</td>
                </tr>
                <tr>
                  <td>3. User modifies date/time and provides reason for change.</td>
                  <td>4. System updates appointment record, recalculates reminder triggers, and sends notification to caregiver.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 03:</strong> If appointment is cancelled, system updates status to 'Cancelled' and prompts user to archive notes.
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>Updated schedule is committed, calendar is synchronized, and obsolete alarms are removed.</td>
        </tr>
      </table>
      <div class="page-number">42</div>
    </div>
    """
    pages_html.append(p42)

    # =========================================================================
    # PAGE 43: 6.5.4 UC-13 LOG DAILY CARE TASKS & VITALS
    # =========================================================================
    p43 = """
    <div class="page" id="page-43">
      <h2 class="sub-title">6.5.4 Daily Care & Emergency SOS Subsystem Use Case Narration Table</h2>

      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>Log Daily Care Tasks & Vitals</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Professional Caregiver, Senior</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Caregiver records completion of non-medical daily tasks (hygiene, meals, walk) and enters measured vital signs.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>Caregiver must be logged in and assigned to the senior. Daily routine checklist must exist.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. Caregiver opens "Daily Care Checklist" screen.</td>
                  <td>2. System displays scheduled tasks (Breakfast, Bathing, Physical Mobility).</td>
                </tr>
                <tr>
                  <td>3. Caregiver checks off completed tasks and inputs measured Blood Pressure (120/80) and Glucose (6.2).</td>
                  <td>4. System validates numerical ranges, stores logs in database, and updates Guardian's live feed.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 04:</strong> If entered blood pressure exceeds safety threshold (&gt;150 systolic), system flags reading in bright red and notifies Guardian.
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>Daily care tasks and vitals are logged with timestamps, establishing an accountable audit trail.</td>
        </tr>
      </table>
      <div class="page-number">43</div>
    </div>
    """
    pages_html.append(p43)

    # =========================================================================
    # PAGE 44: UC-14 SUBMIT SHIFT HANDOFF NOTE
    # =========================================================================
    p44 = """
    <div class="page" id="page-44">
      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>Submit Shift Handoff Care Note</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Professional Caregiver (Outgoing), Guardian</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Outgoing caregiver compiles end-of-shift handover report covering completed tasks, senior mood, and pending items.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>Caregiver shift must be nearing completion. Senior profile must be active.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. Outgoing caregiver clicks "Complete Shift & Handoff".</td>
                  <td>2. System auto-populates day's completed doses, tasks, and vitals summary.</td>
                </tr>
                <tr>
                  <td>3. Caregiver adds subjective notes (e.g. "Senior felt mild knee stiffness; rested at 3 PM") and submits.</td>
                  <td>4. System saves immutable handover log, sends notification to incoming aide and Guardian.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 03:</strong> Incoming caregiver reviews and clicks "Acknowledge Shift Note", confirming handoff.
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>Care continuity is preserved without communication breakdown; report is archived in senior's permanent log.</td>
        </tr>
      </table>
      <div class="page-number">44</div>
    </div>
    """
    pages_html.append(p44)

    # =========================================================================
    # PAGE 45: UC-15 TRIGGER EMERGENCY SOS ALERT
    # =========================================================================
    p45 = """
    <div class="page" id="page-45">
      <table class="uc-table">
        <tr>
          <td class="uc-label">Use Case Name</td>
          <td><strong>Trigger Emergency SOS Alert</strong></td>
        </tr>
        <tr>
          <td class="uc-label">Actors</td>
          <td>Elderly Senior, Caregiver, Family Guardian</td>
        </tr>
        <tr>
          <td class="uc-label">Description</td>
          <td>Senior or Caregiver activates the prominent emergency panic button during acute medical crises or domestic falls.</td>
        </tr>
        <tr>
          <td class="uc-label">Precondition</td>
          <td>System is active on senior tablet, mobile phone, or caregiver terminal.</td>
        </tr>
        <tr>
          <td class="uc-label">Typical course of events</td>
          <td>
            <table class="uc-subtable">
              <thead>
                <tr><th style="width:50%;">Actors Events</th><th>System Response</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td>1. Senior presses the large red "EMERGENCY SOS" button.</td>
                  <td>2. System captures live GPS coordinates and sounds local visual/audio distress alarm.</td>
                </tr>
                <tr>
                  <td>3. System immediately dispatches emergency SMS and emails to Guardian and ambulance dispatch.</td>
                  <td>4. Emergency broadcast includes senior name, home address, GPS link, blood group, and drug allergies.</td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
        <tr>
          <td class="uc-label">Alternative Flows</td>
          <td>
            <strong>Alt 01:</strong> 10-second cancellation window provided in case of accidental tap, allowing immediate disarm with PIN.
          </td>
        </tr>
        <tr>
          <td class="uc-label">Post Condition</td>
          <td>Emergency alert is permanently logged in audit table; all guardians and emergency personnel receive distress dispatch.</td>
        </tr>
      </table>
      <div class="page-number">45</div>
    </div>
    """
    pages_html.append(p45)

    # =========================================================================
    # PAGE 46: 6.6 CRUD MATRIX
    # =========================================================================
    p46 = """
    <div class="page" id="page-46">
      <h2 class="sub-title">6.6 CRUD Matrix</h2>
      <p>
        The CRUD Matrix establishes data access privileges across the primary relational entities, defining which user roles have permission to <strong>Create (C)</strong>, <strong>Read (R)</strong>, <strong>Update (U)</strong>, or <strong>Delete (D)</strong> specific database records.
      </p>

      <table class="data-table" style="margin-top: 15px;">
        <thead>
          <tr>
            <th style="width: 32%;">Process / Entity</th>
            <th style="width: 13%;">Senior</th>
            <th style="width: 14%;">Guardian</th>
            <th style="width: 14%;">Caregiver</th>
            <th style="width: 13%;">Doctor</th>
            <th style="width: 14%;">Admin</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>User Account</strong></td>
            <td>R</td>
            <td>CRU</td>
            <td>CRU</td>
            <td>CRU</td>
            <td>CRUD</td>
          </tr>
          <tr>
            <td><strong>Senior Profile Baseline</strong></td>
            <td>R</td>
            <td>CRUD</td>
            <td>R</td>
            <td>RU</td>
            <td>RD</td>
          </tr>
          <tr>
            <td><strong>Medication Schedule</strong></td>
            <td>R</td>
            <td>CRUD</td>
            <td>R</td>
            <td>CRUD</td>
            <td>RD</td>
          </tr>
          <tr>
            <td><strong>Dose Adherence Log</strong></td>
            <td>CR</td>
            <td>RU</td>
            <td>CRU</td>
            <td>R</td>
            <td>RD</td>
          </tr>
          <tr>
            <td><strong>Doctor Appointments</strong></td>
            <td>R</td>
            <td>CRUD</td>
            <td>R</td>
            <td>CRUD</td>
            <td>RD</td>
          </tr>
          <tr>
            <td><strong>Prescription Documents</strong></td>
            <td>R</td>
            <td>CRUD</td>
            <td>R</td>
            <td>CRUD</td>
            <td>RD</td>
          </tr>
          <tr>
            <td><strong>Daily Care Tasks (ADL)</strong></td>
            <td>R</td>
            <td>CRUD</td>
            <td>CRU</td>
            <td>R</td>
            <td>RD</td>
          </tr>
          <tr>
            <td><strong>Shift Handoff Notes</strong></td>
            <td>R</td>
            <td>RU</td>
            <td>CRU</td>
            <td>R</td>
            <td>RD</td>
          </tr>
          <tr>
            <td><strong>Emergency SOS Alerts</strong></td>
            <td>CR</td>
            <td>CRU</td>
            <td>CRU</td>
            <td>R</td>
            <td>RD</td>
          </tr>
          <tr>
            <td><strong>System Audit Trail</strong></td>
            <td>-</td>
            <td>R</td>
            <td>-</td>
            <td>-</td>
            <td>CRD</td>
          </tr>
        </tbody>
      </table>
      <div class="page-number">46</div>
    </div>
    """
    pages_html.append(p46)

    # =========================================================================
    # PAGE 47: 6.7 ACTIVITY TABLE (Part 1)
    # =========================================================================
    p47 = """
    <div class="page" id="page-47">
      <h2 class="sub-title">6.7 Activity Table</h2>
      <p>
        The Activity Table outlines the work breakdown structure (WBS) for engineering and delivering the Elderly Care Management System, indicating activity identifiers, task descriptions, estimated durations, and prerequisite dependencies.
      </p>

      <table class="data-table" style="margin-top: 15px;">
        <thead>
          <tr>
            <th style="width: 8%;">SL</th>
            <th style="width: 14%;">Activity Code</th>
            <th>Activity Name</th>
            <th style="width: 18%;">Duration (Days)</th>
            <th style="width: 18%;">Dependency</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td><strong>A</strong></td>
            <td>Project Topic Selection & Scope Definition</td>
            <td>1</td>
            <td>-</td>
          </tr>
          <tr>
            <td>2</td>
            <td><strong>B</strong></td>
            <td>Requirement Elicitation & Feature Selection</td>
            <td>2</td>
            <td>A</td>
          </tr>
          <tr>
            <td>3</td>
            <td><strong>C</strong></td>
            <td>System Architecture & Database Schema Design</td>
            <td>2</td>
            <td>B</td>
          </tr>
          <tr>
            <td>4</td>
            <td><strong>D</strong></td>
            <td>User Authentication & RBAC Engine</td>
            <td>2</td>
            <td>C</td>
          </tr>
          <tr>
            <td>5</td>
            <td><strong>E</strong></td>
            <td>Senior Health Baseline & Profile Module</td>
            <td>3</td>
            <td>D</td>
          </tr>
          <tr>
            <td>6</td>
            <td><strong>F</strong></td>
            <td>Medication Master & Dosage Scheduling Module</td>
            <td>3</td>
            <td>E</td>
          </tr>
          <tr>
            <td>7</td>
            <td><strong>G</strong></td>
            <td>Real-Time Dose Adherence Logging & Reminders</td>
            <td>2</td>
            <td>F</td>
          </tr>
          <tr>
            <td>8</td>
            <td><strong>H</strong></td>
            <td>Doctor Appointment & Calendar Module</td>
            <td>3</td>
            <td>E</td>
          </tr>
          <tr>
            <td>9</td>
            <td><strong>I</strong></td>
            <td>Digital Prescription & Clinical Archive</td>
            <td>2</td>
            <td>H</td>
          </tr>
          <tr>
            <td>10</td>
            <td><strong>J</strong></td>
            <td>Daily Care Checklist & ADL Routine Module</td>
            <td>2</td>
            <td>E</td>
          </tr>
          <tr>
            <td>11</td>
            <td><strong>K</strong></td>
            <td>Caregiver Shift Handoff & Care Notes Module</td>
            <td>2</td>
            <td>J</td>
          </tr>
        </tbody>
      </table>
      <div class="page-number">47</div>
    </div>
    """
    pages_html.append(p47)

    # =========================================================================
    # PAGE 48: 6.7 ACTIVITY TABLE (Part 2) & 6.8 GANTT CHART
    # =========================================================================
    p48 = f"""
    <div class="page" id="page-48">
      <table class="data-table" style="margin-top: 0; margin-bottom: 10px;">
        <thead>
          <tr>
            <th style="width: 8%;">SL</th>
            <th style="width: 14%;">Activity Code</th>
            <th>Activity Name</th>
            <th style="width: 18%;">Duration (Days)</th>
            <th style="width: 18%;">Dependency</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>12</td>
            <td><strong>L</strong></td>
            <td>Instant Emergency SOS Panic & SMS Broadcast</td>
            <td>2</td>
            <td>E</td>
          </tr>
          <tr>
            <td>13</td>
            <td><strong>M</strong></td>
            <td>Family Guardian Oversight Live Dashboard</td>
            <td>2</td>
            <td>G, K, L</td>
          </tr>
          <tr>
            <td>14</td>
            <td><strong>N</strong></td>
            <td>Compliance Analytics & PDF Reporting</td>
            <td>2</td>
            <td>M</td>
          </tr>
          <tr>
            <td>15</td>
            <td><strong>O</strong></td>
            <td>End-to-End System Testing & Quality Assurance</td>
            <td>4</td>
            <td>All</td>
          </tr>
          <tr>
            <td>16</td>
            <td><strong>P</strong></td>
            <td>Comprehensive SRS Documentation Compilation</td>
            <td>3</td>
            <td>O</td>
          </tr>
          <tr>
            <td>17</td>
            <td><strong>Q</strong></td>
            <td>Cloud Deployment, Live Demonstration & Release</td>
            <td>1</td>
            <td>P</td>
          </tr>
        </tbody>
      </table>

      <h2 class="sub-title">6.8 Gantt chart</h2>
      <div class="diagram-wrapper">
        {svg_diagrams.get_fig11_gantt_svg()}
        <div class="fig-caption">Fig 11: Gantt Chart</div>
      </div>
      <div class="page-number">48</div>
    </div>
    """
    pages_html.append(p48)

    # =========================================================================
    # PAGE 49: 7. NON-FUNCTIONAL REQUIREMENTS & 7.1 (Part 1)
    # =========================================================================
    p49 = """
    <div class="page" id="page-49">
      <h1 class="sec-title">Non-Functional Requirements</h1>
      <p>
        The non-functional requirements define the quality attributes, operational constraints, and performance benchmarks governing the Elderly Care Management System. They ensure the platform remains reliable, secure, accessible, and scalable over long-term usage.
      </p>

      <h2 class="sub-title">7.1 Feature List with Description</h2>
      <ol>
        <li>
          <strong>Performance & Response Latency:</strong>
          <ul>
            <li>Standard page loads, dashboard queries, and schedule lookups must render in under 2.0 seconds over standard 4G and domestic broadband connections.</li>
            <li>Database query execution latency must remain under 200 milliseconds for 95% of transactions.</li>
            <li>Critical Emergency SOS dispatch routines must execute within 1.0 second of trigger confirmation, ensuring zero latency during life-safety crises.</li>
          </ul>
        </li>
        <li>
          <strong>Reliability & Availability:</strong>
          <ul>
            <li>The system must maintain 99.9% scheduled uptime throughout production deployment.</li>
            <li>Automated nightly database snapshots must be stored in redundant, offsite storage to prevent data loss in the event of server failures.</li>
            <li>Graceful degradation ensures that if external SMS gateways experience latency, local audio-visual alarms continue operating without failure.</li>
          </ul>
        </li>
        <li>
          <strong>Security & Health Data Confidentiality:</strong>
          <ul>
            <li>All HTTP transactions must strictly operate over Transport Layer Security (TLS 1.3) with valid SSL certificates.</li>
            <li>All stored user passwords must use salted cryptographic hashing via Argon2id / Bcrypt with cost factor 12.</li>
            <li>Sensitive senior baseline data—such as chronic conditions and drug allergies—is encrypted at rest using AES-256 standards.</li>
          </ul>
        </li>
        <li>
          <strong>Usability & Senior Accessibility:</strong>
          <ul>
            <li>The interface strictly complies with WCAG 2.1 AA accessibility standards, featuring high-contrast themes and scalable fonts (18px+ default for seniors).</li>
            <li>Interactive buttons feature large touch targets (minimum 48x48 pixels) to accommodate elderly users with mild motor tremors or arthritis.</li>
          </ul>
        </li>
      </ol>
      <div class="page-number">49</div>
    </div>
    """
    pages_html.append(p49)

    # =========================================================================
    # PAGE 50: 7.1 (Part 2)
    # =========================================================================
    p50 = """
    <div class="page" id="page-50">
      <ol start="5">
        <li>
          <strong>Scalability:</strong>
          <ul>
            <li>The system architecture utilizes a stateless PHP application tier capable of horizontal scaling behind standard load balancers.</li>
            <li>The MySQL database schema incorporates indexed lookup keys on high-frequency tables (Dose Logs, Appointments, Vitals), supporting up to 10,000 active senior care plans simultaneously without database locking contention.</li>
          </ul>
        </li>
        <li>
          <strong>Portability & Cross-Browser Compatibility:</strong>
          <ul>
            <li>The web application is fully responsive and verified to execute seamlessly across all major modern browsers: Google Chrome, Mozilla Firefox, Apple Safari, and Microsoft Edge.</li>
            <li>Mobile responsiveness is guaranteed on iOS and Android smartphones and tablets without requiring proprietary native downloads.</li>
          </ul>
        </li>
        <li>
          <strong>Maintainability & Code Standards:</strong>
          <ul>
            <li>All backend source code adheres to PSR-12 coding style guidelines, featuring modular MVC separation and comprehensive docstring documentation.</li>
            <li>Database migrations and seeders are version-controlled to enable rapid deployment and consistent staging across testing and production environments.</li>
          </ul>
        </li>
        <li>
          <strong>Data Integrity & Auditability:</strong>
          <ul>
            <li>All database tables enforce strict relational foreign key constraints, preventing orphaned records.</li>
            <li>Critical medical events—including medication additions, dose cancellations, and SOS activations—are committed to an append-only audit trail with immutable timestamps and IP records.</li>
          </ul>
        </li>
      </ol>
      <div class="page-number">50</div>
    </div>
    """
    pages_html.append(p50)

    # =========================================================================
    # PAGE 51: 8. RESULT ANALYSIS & 8.1 SWOT & 8.2 RISK MATRIX
    # =========================================================================
    p51 = """
    <div class="page" id="page-51">
      <h1 class="sec-title">Result Analysis</h1>
      <h2 class="sub-title">8.1 SWOT Analysis</h2>

      <table class="data-table" style="margin-top: 10px; margin-bottom: 12px;">
        <thead>
          <tr>
            <th style="width: 50%;">Strength</th>
            <th style="width: 50%;">Weakness</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              &bull; Eliminates manual eldercare paperwork.<br>
              &bull; Real-time medication adherence tracking.<br>
              &bull; Instant 1-touch SOS with GPS location.<br>
              &bull; Seamless caregiver shift continuity.<br>
              &bull; Multi-role integration (Senior, Family, Doctor).
            </td>
            <td>
              &bull; Dependent on stable internet connectivity.<br>
              &bull; Requires initial technical onboarding for seniors.<br>
              &bull; Relies on caregiver integrity for accurate vital inputs.
            </td>
          </tr>
          <tr>
            <th>Opportunities</th>
            <th>Threats</th>
          </tr>
          <tr>
            <td>
              &bull; Integration with wearable IoT health monitors.<br>
              &bull; Automated AI predictive fall detection.<br>
              &bull; Telemedicine video consultation expansion.<br>
              &bull; Automated pharmacy prescription refilling.
            </td>
            <td>
              &bull; Cybersecurity and health data breach risks.<br>
              &bull; Cloud server downtime during emergency crises.<br>
              &bull; Resistance to technology adoption by seniors.
            </td>
          </tr>
        </tbody>
      </table>

      <h2 class="sub-title">8.2 Risk Matrix</h2>
      <table class="data-table">
        <thead>
          <tr>
            <th style="width: 25%;">Risk Factor</th>
            <th style="width: 15%;">Likelihood</th>
            <th style="width: 15%;">Impact</th>
            <th>Solution / Mitigation Strategy</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Database Loss / Corruption</td>
            <td>Low</td>
            <td>High</td>
            <td>Automated daily offsite cloud backups & InnoDB transaction logs.</td>
          </tr>
          <tr>
            <td>Unauthorized Health Access</td>
            <td>Low</td>
            <td>High</td>
            <td>Argon2id hashing, TLS 1.3 encryption, and strict RBAC verification.</td>
          </tr>
          <tr>
            <td>Network Failure during SOS</td>
            <td>Medium</td>
            <td>High</td>
            <td>Local audio-visual alarm activates immediately; SMS dispatched asynchronously.</td>
          </tr>
          <tr>
            <td>Caregiver Handoff Neglect</td>
            <td>Medium</td>
            <td>Medium</td>
            <td>Mandatory digital shift sign-off before clock-out is permitted.</td>
          </tr>
        </tbody>
      </table>
      <div class="page-number">51</div>
    </div>
    """
    pages_html.append(p51)

    # =========================================================================
    # PAGE 52: 9. CONCLUSION
    # =========================================================================
    p52 = """
    <div class="page" id="page-52">
      <h1 class="sec-title">Conclusion</h1>
      <p>
        This Software Requirements Specification proposes a comprehensive, methodical, and human-centric approach to modernizing and automating geriatric care routines. Traditional eldercare systems—heavily reliant on physical pillboxes, handwritten notebooks, and fragmented phone communications—expose aging seniors to preventable medication omissions, shift communication breakdowns, and fatal emergency response delays.
      </p>
      <p>
        The proposed <strong>Elderly Care Management System</strong> addresses these vulnerabilities through an integrated, multi-role web platform. By synchronizing medication schedules with real-time adherence logging, streamlining doctor consultations and digital prescription archives, standardizing daily living (ADL) routines, enforcing caregiver shift handoff accountability, and providing an instantaneous one-touch Emergency SOS broadcast with GPS coordinates and medical briefs, the platform establishes an unbroken circle of care around the senior.
      </p>
      <p>
        The architectural design, relational schema, UML behavioral models, and verification frameworks articulated throughout this report demonstrate that the system is technically, economically, and operationally feasible. Built upon an accessible frontend and a secure relational backend, the Elderly Care Management System delivers profound socio-technological value: eliminating dangerous medication errors, fostering professional accountability, and granting working family members 24/7 peace of mind while preserving the independence and dignity of aging senior citizens.
      </p>
      <div class="page-number">52</div>
    </div>
    """
    pages_html.append(p52)

    # =========================================================================
    # PAGE 53: 10. REFERENCES
    # =========================================================================
    p53 = """
    <div class="page" id="page-53">
      <h1 class="sec-title">References</h1>
      <ol style="margin-left: 24px; font-size: 10pt; line-height: 1.6;">
        <li>
          IEEE Computer Society, <em>"IEEE Recommended Practice for Software Requirements Specifications,"</em> IEEE Std 830-1998, Institute of Electrical and Electronics Engineers, New York, 1998.
        </li>
        <li>
          ISO/IEC/IEEE, <em>"Systems and software engineering &mdash; Life cycle processes &mdash; Requirements engineering,"</em> ISO/IEC/IEEE 29148:2018, Geneva, Switzerland, 2018.
        </li>
        <li>
          World Health Organization (WHO), <em>"Medication Safety in Polypharmacy: Technical Report,"</em> WHO Patient Safety Global Action, World Health Organization, Geneva, 2019.
        </li>
        <li>
          World Health Organization (WHO), <em>"World Report on Ageing and Health,"</em> WHO Press, Geneva, 2015.
        </li>
        <li>
          B. Bryan, <em>"Software Architecture Patterns: Layered Architecture Patterns,"</em> Medium Software Engineering Publication, Available: <span style="font-family: monospace; font-size: 8.5pt;">https://yapbryan6.medium.com/software-architecture-patterns-layered-architecture-patterns-975ff2abec6f</span>, [Accessed: Oct. 2025].
        </li>
        <li>
          World Wide Web Consortium (W3C), <em>"Web Content Accessibility Guidelines (WCAG) 2.1,"</em> W3C Recommendation, Available: <span style="font-family: monospace; font-size: 8.5pt;">https://www.w3.org/TR/WCAG21/</span>, 2018.
        </li>
        <li>
          Open Web Application Security Project (OWASP), <em>"OWASP Top 10: The Ten Most Critical Web Application Security Risks,"</em> OWASP Foundation, 2021.
        </li>
        <li>
          R. S. Pressman and B. R. Maxim, <em>"Software Engineering: A Practitioner's Approach,"</em> 9th ed., McGraw-Hill Education, New York, 2020.
        </li>
      </ol>
      <div class="page-number">53</div>
    </div>
    """
    pages_html.append(p53)

    # Assemble complete HTML document
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Software Requirements Specification for Elderly Care Management System</title>
<style>
{css}
</style>
</head>
<body>
{''.join(pages_html)}
</body>
</html>
"""
    return html_content

def compile_to_pdf(html_file, pdf_file):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    file_url = "file:///" + os.path.abspath(html_file).replace("\\", "/")
    tmp_user_dir = tempfile.mkdtemp()
    
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--user-data-dir=" + tmp_user_dir,
        "--print-to-pdf=" + os.path.abspath(pdf_file),
        file_url
    ]
    print(f"Running Chrome to compile {pdf_file}...")
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if os.path.exists(pdf_file):
        size = os.path.getsize(pdf_file)
        reader = pypdf.PdfReader(pdf_file)
        print(f"SUCCESS! Created PDF: {pdf_file} ({size:,} bytes) with {len(reader.pages)} pages.")
        return len(reader.pages)
    else:
        print(f"FAILED to generate PDF: {res.stderr}")
        return 0

def main():
    html_output = "Elderly_Care_Management_System_SRS_Demo_Style.html"
    pdf_output = "Elderly_Care_Management_System_SRS_Demo_Style.pdf"

    print("Generating HTML content...")
    html_content = build_html()
    with open(html_output, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved {html_output}")

    page_count = compile_to_pdf(html_output, pdf_output)
    print(f"Final Page Count: {page_count}")

if __name__ == "__main__":
    main()
