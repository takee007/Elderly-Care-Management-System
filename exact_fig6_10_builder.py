# Generate exact Fig 6 (DFD) and Fig 7, 8, 9, 10 (Use Cases) for Elderly Care Management System
# matching demo.pdf p29-32 drawings pixel-for-pixel without duplicate captions inside diagrams

def get_exact_demo_style_fig6_svg():
    import build_crystal_clear_fig6
    return build_crystal_clear_fig6.get_high_res_fig6_svg()


def get_exact_demo_style_fig7_svg():
    return """<svg viewBox="0 0 660 330" width="100%" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <!-- System Boundary Box with Tab -->
  <rect x="25" y="15" width="195" height="24" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="122" y="32" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">User Management Subsystem</text>
  <rect x="25" y="39" width="605" height="150" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>

  <!-- 4 Use Case Ellipses -->
  <!-- 1. Create Account -->
  <ellipse cx="100" cy="110" rx="60" ry="26" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="100" y="114" font-size="11" fill="#000000" text-anchor="middle">Create Account</text>

  <!-- 2. Login -->
  <ellipse cx="250" cy="110" rx="60" ry="26" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="250" y="114" font-size="11" fill="#000000" text-anchor="middle">Login</text>

  <!-- 3. Edit Information -->
  <ellipse cx="400" cy="110" rx="65" ry="26" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="400" y="114" font-size="10.5" fill="#000000" text-anchor="middle">Edit Information</text>

  <!-- 4. User List -->
  <ellipse cx="550" cy="110" rx="60" ry="26" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="550" y="114" font-size="11" fill="#000000" text-anchor="middle">User List</text>

  <!-- ================= ACTORS ================= -->
  <!-- Left Actor: Senior / Guardian (Stick Figure) -->
  <g transform="translate(100, 245)">
    <circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="10" x2="0" y2="40" stroke="#000000" stroke-width="1.3"/>
    <line x1="-20" y1="20" x2="20" y2="20" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="-15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <text x="0" y="80" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">Senior / Guardian</text>
  </g>

  <!-- Right Actor: Admin / Caregiver (Stick Figure) -->
  <g transform="translate(500, 245)">
    <circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="10" x2="0" y2="40" stroke="#000000" stroke-width="1.3"/>
    <line x1="-20" y1="20" x2="20" y2="20" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="-15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <text x="0" y="80" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">Admin / Caregiver</text>
  </g>

  <!-- Connectors: Senior to Create Account, Login, Edit Info -->
  <line x1="100" y1="235" x2="100" y2="136" stroke="#000000" stroke-width="1.2"/>
  <line x1="100" y1="235" x2="235" y2="133" stroke="#000000" stroke-width="1.2"/>
  <line x1="100" y1="235" x2="365" y2="130" stroke="#000000" stroke-width="1.2"/>

  <!-- Connectors: Admin to User List -->
  <line x1="500" y1="235" x2="540" y2="136" stroke="#000000" stroke-width="1.2"/>

  <!-- Connector: Admin to Login (wrapping around boundary box like demo Fig 7) -->
  <path d="M 500 245 L 650 245 L 650 25 L 295 25 L 295 85" fill="none" stroke="#000000" stroke-width="1.2"/>
</svg>"""


def get_exact_demo_style_fig8_svg():
    return """<svg viewBox="0 0 660 330" width="100%" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <!-- System Boundary Box with Tab -->
  <rect x="25" y="15" width="245" height="24" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="147" y="32" font-size="10.5" font-weight="bold" fill="#000000" text-anchor="middle">Medication Management Subsystem</text>
  <rect x="25" y="39" width="605" height="165" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>

  <!-- 5 Use Case Ellipses -->
  <!-- 1. Schedule Medication -->
  <ellipse cx="95" cy="90" rx="60" ry="25" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="95" y="94" font-size="10" fill="#000000" text-anchor="middle">Schedule Medication</text>

  <!-- 2. View Dose Schedule -->
  <ellipse cx="235" cy="90" rx="60" ry="25" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="235" y="94" font-size="10" fill="#000000" text-anchor="middle">View Dose Schedule</text>

  <!-- 3. View Medication History (Center Lower) -->
  <ellipse cx="280" cy="165" rx="65" ry="25" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="280" y="169" font-size="10" fill="#000000" text-anchor="middle">View Med History</text>

  <!-- 4. Confirm Dose Intake -->
  <ellipse cx="400" cy="90" rx="60" ry="25" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="400" y="94" font-size="10" fill="#000000" text-anchor="middle">Confirm Dose Taken</text>

  <!-- 5. Update Medication Regimen -->
  <ellipse cx="545" cy="90" rx="60" ry="25" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="545" y="94" font-size="10" fill="#000000" text-anchor="middle">Update Regimen</text>

  <!-- ================= ACTORS ================= -->
  <!-- Left Actor: Senior / Guardian -->
  <g transform="translate(100, 245)">
    <circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="10" x2="0" y2="40" stroke="#000000" stroke-width="1.3"/>
    <line x1="-20" y1="20" x2="20" y2="20" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="-15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <text x="0" y="80" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">Senior / Guardian</text>
  </g>

  <!-- Right Actor: Doctor / Caregiver -->
  <g transform="translate(500, 245)">
    <circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="10" x2="0" y2="40" stroke="#000000" stroke-width="1.3"/>
    <line x1="-20" y1="20" x2="20" y2="20" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="-15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <text x="0" y="80" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">Doctor / Caregiver</text>
  </g>

  <!-- Connectors: Senior to Schedule, View Schedule, View History -->
  <line x1="100" y1="235" x2="95" y2="115" stroke="#000000" stroke-width="1.2"/>
  <line x1="100" y1="235" x2="215" y2="113" stroke="#000000" stroke-width="1.2"/>
  <line x1="100" y1="235" x2="235" y2="170" stroke="#000000" stroke-width="1.2"/>

  <!-- Connectors: Doctor to Confirm Dose, Update Regimen -->
  <line x1="500" y1="235" x2="425" y2="113" stroke="#000000" stroke-width="1.2"/>
  <line x1="500" y1="235" x2="540" y2="115" stroke="#000000" stroke-width="1.2"/>
</svg>"""


def get_exact_demo_style_fig9_svg():
    return """<svg viewBox="0 0 660 330" width="100%" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <!-- System Boundary Box with Tab -->
  <rect x="25" y="15" width="245" height="24" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="147" y="32" font-size="10.5" font-weight="bold" fill="#000000" text-anchor="middle">Appointment Scheduling Subsystem</text>
  <rect x="25" y="39" width="605" height="150" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>

  <!-- 3 Use Case Ellipses -->
  <!-- 1. View Appointment Records -->
  <ellipse cx="120" cy="110" rx="75" ry="26" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="120" y="114" font-size="10.5" fill="#000000" text-anchor="middle">View Appointments</text>

  <!-- 2. Book Appointment -->
  <ellipse cx="310" cy="110" rx="70" ry="26" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="310" y="114" font-size="10.5" fill="#000000" text-anchor="middle">Book Appointment</text>

  <!-- 3. View Consultation History -->
  <ellipse cx="500" cy="110" rx="75" ry="26" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="500" y="114" font-size="10.5" fill="#000000" text-anchor="middle">Consultation History</text>

  <!-- ================= ACTORS ================= -->
  <!-- Left Actor: Senior / Guardian -->
  <g transform="translate(180, 245)">
    <circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="10" x2="0" y2="40" stroke="#000000" stroke-width="1.3"/>
    <line x1="-20" y1="20" x2="20" y2="20" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="-15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <text x="0" y="80" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">Senior / Guardian</text>
  </g>

  <!-- Right Actor: Doctor / Clinic -->
  <g transform="translate(450, 245)">
    <circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="10" x2="0" y2="40" stroke="#000000" stroke-width="1.3"/>
    <line x1="-20" y1="20" x2="20" y2="20" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="-15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <text x="0" y="80" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">Doctor / Clinic</text>
  </g>

  <!-- Connectors: Senior to View Appointments -->
  <line x1="180" y1="235" x2="135" y2="136" stroke="#000000" stroke-width="1.2"/>

  <!-- Connectors: Doctor to Book Appointment, Consultation History -->
  <line x1="450" y1="235" x2="340" y2="135" stroke="#000000" stroke-width="1.2"/>
  <line x1="450" y1="235" x2="490" y2="136" stroke="#000000" stroke-width="1.2"/>
</svg>"""


def get_exact_demo_style_fig10_svg():
    return """<svg viewBox="0 0 660 330" width="100%" height="230" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <!-- System Boundary Box with Tab -->
  <rect x="25" y="15" width="280" height="24" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="165" y="32" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">Daily Care &amp; Emergency SOS Subsystem</text>
  <rect x="25" y="39" width="605" height="150" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>

  <!-- 4 Use Case Ellipses -->
  <!-- 1. Trigger SOS Alert -->
  <ellipse cx="95" cy="110" rx="60" ry="26" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="95" y="114" font-size="10.5" fill="#000000" text-anchor="middle">Trigger SOS Alert</text>

  <!-- 2. View Daily Care Plan -->
  <ellipse cx="235" cy="110" rx="65" ry="26" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="235" y="114" font-size="10.5" fill="#000000" text-anchor="middle">View Daily Care</text>

  <!-- 3. Log Vital Signs -->
  <ellipse cx="385" cy="110" rx="60" ry="26" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="385" y="114" font-size="10.5" fill="#000000" text-anchor="middle">Log Vital Signs</text>

  <!-- 4. Acknowledge SOS Alert -->
  <ellipse cx="530" cy="110" rx="65" ry="26" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
  <text x="530" y="114" font-size="10" fill="#000000" text-anchor="middle">Acknowledge SOS</text>

  <!-- ================= ACTORS ================= -->
  <!-- Left Actor: Senior Citizen -->
  <g transform="translate(100, 245)">
    <circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="10" x2="0" y2="40" stroke="#000000" stroke-width="1.3"/>
    <line x1="-20" y1="20" x2="20" y2="20" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="-15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <text x="0" y="80" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">Senior Citizen</text>
  </g>

  <!-- Right Actor: Caregiver / First Responder -->
  <g transform="translate(500, 245)">
    <circle cx="0" cy="0" r="10" fill="#ffffff" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="10" x2="0" y2="40" stroke="#000000" stroke-width="1.3"/>
    <line x1="-20" y1="20" x2="20" y2="20" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="-15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <line x1="0" y1="40" x2="15" y2="65" stroke="#000000" stroke-width="1.3"/>
    <text x="0" y="80" font-size="10" font-weight="bold" fill="#000000" text-anchor="middle">Caregiver / Responder</text>
  </g>

  <!-- Connectors: Senior to Trigger SOS, View Daily Care -->
  <line x1="100" y1="235" x2="95" y2="136" stroke="#000000" stroke-width="1.2"/>
  <line x1="100" y1="235" x2="215" y2="133" stroke="#000000" stroke-width="1.2"/>

  <!-- Connectors: Caregiver to Log Vital Signs, Acknowledge SOS -->
  <line x1="500" y1="235" x2="405" y2="133" stroke="#000000" stroke-width="1.2"/>
  <line x1="500" y1="235" x2="525" y2="136" stroke="#000000" stroke-width="1.2"/>
</svg>"""
