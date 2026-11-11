"""
build_crystal_clear_fig5.py
Generates a publication-grade, ultra-high-definition Entity-Relationship Diagram (Fig 5)
for the Elderly Care Management System matching the demo.pdf Crow's Foot & EER layout.
Renders at 3520 x 2900 resolution via Headless Chrome with scale factor 2.0.
"""

import os
import subprocess
import tempfile
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PNG_OUT = os.path.join(BASE_DIR, "figures_png", "fig5_er_diagram.png")

def get_high_res_fig5_svg():
    # Canvas: 1760 x 1450
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1760 1450" width="1760" height="1450" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <defs>
    <!-- Arrowhead markers -->
    <marker id="er-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#000000"/>
    </marker>
    <marker id="er-arrow-down" viewBox="0 0 10 10" refX="5" refY="9" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 1.5 0 L 5 9 L 8.5 0 z" fill="#000000"/>
    </marker>
  </defs>

  <!-- ======================================================== -->
  <!-- 1. USER (Top Center - Green Box)                         -->
  <!-- ======================================================== -->
  <g transform="translate(780, 30)">
    <rect width="240" height="210" rx="10" ry="10" fill="#e8f8e8" stroke="#385723" stroke-width="2"/>
    <path d="M 0 42 L 240 42" stroke="#385723" stroke-width="1.8"/>
    <text x="120" y="29" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">USER</text>
    <text x="18" y="74" font-size="15" font-weight="bold" fill="#000000" text-decoration="underline">User_ID</text>
    <text x="18" y="106" font-size="15" fill="#000000">UserName</text>
    <text x="18" y="138" font-size="15" fill="#000000">Email</text>
    <text x="18" y="170" font-size="15" fill="#000000">Password</text>
    <text x="18" y="202" font-size="15" fill="#000000">Role</text>
  </g>

  <!-- Connection from USER to Disjoint Circle (d) -->
  <line x1="895" y1="240" x2="895" y2="300" stroke="#000000" stroke-width="1.8"/>
  <line x1="905" y1="240" x2="905" y2="300" stroke="#000000" stroke-width="1.8"/>
  <text x="922" y="275" font-size="15" font-weight="bold" fill="#000000">Type=?</text>

  <!-- Disjoint Specialization Circle (d) -->
  <circle cx="900" cy="320" r="20" fill="#ffffff" stroke="#000000" stroke-width="2"/>
  <text x="900" y="327" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">d</text>

  <!-- Left Branch from (d) to Senior Profile (S) -->
  <line x1="880" y1="320" x2="660" y2="320" stroke="#000000" stroke-width="1.8"/>
  <line x1="660" y1="320" x2="660" y2="368" stroke="#000000" stroke-width="1.8" marker-end="url(#er-arrow-down)"/>
  <text x="765" y="312" font-size="15" font-weight="bold" fill="#000000">S</text>

  <!-- Right Branch from (d) to Caregiver (C) -->
  <line x1="920" y1="320" x2="1220" y2="320" stroke="#000000" stroke-width="1.8"/>
  <line x1="1220" y1="320" x2="1220" y2="388" stroke="#000000" stroke-width="1.8" marker-end="url(#er-arrow-down)"/>
  <text x="1070" y="312" font-size="15" font-weight="bold" fill="#000000">C</text>

  <!-- ======================================================== -->
  <!-- 2. CAREGIVER (Upper Right - Pink Box)                    -->
  <!-- ======================================================== -->
  <g transform="translate(1100, 390)">
    <rect width="240" height="70" rx="10" ry="10" fill="#fde8f0" stroke="#b85450" stroke-width="2"/>
    <text x="120" y="43" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">CAREGIVER</text>
  </g>

  <!-- ======================================================== -->
  <!-- 3. SENIOR_PROFILE (Center Left - Yellow Box)             -->
  <!-- ======================================================== -->
  <g transform="translate(510, 370)">
    <rect width="300" height="550" rx="10" ry="10" fill="#fff7d6" stroke="#c49b27" stroke-width="2"/>
    <path d="M 0 44 L 300 44" stroke="#c49b27" stroke-width="1.8"/>
    <text x="150" y="30" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">SENIOR_PROFILE</text>
    
    <text x="18" y="78" font-size="15" font-weight="bold" fill="#000000" text-decoration="underline">Profile_ID</text>
    <text x="18" y="112" font-size="15" fill="#000000">Name(First, Last)</text>
    <text x="18" y="146" font-size="15" fill="#000000">Phone</text>
    <text x="18" y="180" font-size="15" fill="#000000">Address</text>
    <text x="18" y="214" font-size="15" fill="#000000">DateOfBirth</text>
    <text x="18" y="248" font-size="15" fill="#000000">Gender</text>
    <text x="18" y="282" font-size="15" fill="#000000">BloodGroup</text>
    <text x="18" y="316" font-size="15" fill="#000000">Emergency_Name</text>
    <text x="18" y="350" font-size="15" fill="#000000">Emergency_Phone</text>
    <text x="18" y="384" font-size="15" fill="#000000">PrimaryDoctor</text>
    <text x="18" y="418" font-size="15" fill="#000000">ChronicAilments</text>
    <text x="18" y="452" font-size="15" fill="#000000">DrugAllergies</text>
    <text x="18" y="486" font-size="15" fill="#000000">JoinDate</text>
    <text x="18" y="516" font-size="15" fill="#000000">[AdherenceRate]</text>
    <text x="18" y="542" font-size="15" fill="#000000">[ActiveAlerts]</text>
  </g>

  <!-- ======================================================== -->
  <!-- 4. CLINIC_HOSPITAL (Middle Left - Purple Box)            -->
  <!-- ======================================================== -->
  <g transform="translate(60, 470)">
    <rect width="230" height="150" rx="10" ry="10" fill="#f0ecf8" stroke="#7d5ba6" stroke-width="2"/>
    <path d="M 0 42 L 230 42" stroke="#7d5ba6" stroke-width="1.8"/>
    <text x="115" y="29" font-size="17" font-weight="bold" fill="#000000" text-anchor="middle">CLINIC_HOSPITAL</text>
    <text x="18" y="76" font-size="15" font-weight="bold" fill="#000000" text-decoration="underline">Clinic_ID</text>
    <text x="18" y="108" font-size="15" fill="#000000">Name</text>
    <text x="18" y="138" font-size="15" fill="#000000">Description</text>
  </g>

  <!-- Relationship: CLINIC_HOSPITAL belongs to SENIOR_PROFILE -->
  <line x1="290" y1="545" x2="510" y2="545" stroke="#000000" stroke-width="1.8"/>
  <!-- Tick marks at Clinic: || -->
  <line x1="305" y1="535" x2="305" y2="555" stroke="#000000" stroke-width="1.8"/>
  <line x1="312" y1="535" x2="312" y2="555" stroke="#000000" stroke-width="1.8"/>
  <text x="400" y="535" font-size="15" font-weight="bold" fill="#000000" text-anchor="middle">belongs to</text>
  <!-- Tick marks at Senior: || -->
  <line x1="488" y1="535" x2="488" y2="555" stroke="#000000" stroke-width="1.8"/>
  <line x1="495" y1="535" x2="495" y2="555" stroke="#000000" stroke-width="1.8"/>

  <!-- Senior Profile Top Loop: View Info -->
  <path d="M 510 440 L 440 440 L 440 330 L 580 330 L 580 370" fill="none" stroke="#000000" stroke-width="1.8"/>
  <line x1="498" y1="430" x2="498" y2="450" stroke="#000000" stroke-width="1.8"/>
  <line x1="491" y1="430" x2="491" y2="450" stroke="#000000" stroke-width="1.8"/>
  <line x1="570" y1="360" x2="590" y2="360" stroke="#000000" stroke-width="1.8"/>
  <text x="415" y="350" font-size="15" font-weight="bold" fill="#000000">View Info</text>

  <!-- Relationship: CAREGIVER - SENIOR_PROFILE (View Info) -->
  <line x1="1100" y1="425" x2="810" y2="490" stroke="#000000" stroke-width="1.8"/>
  <!-- Tick marks at Caregiver -->
  <line x1="1080" y1="418" x2="1086" y2="438" stroke="#000000" stroke-width="1.8"/>
  <line x1="1088" y1="416" x2="1094" y2="436" stroke="#000000" stroke-width="1.8"/>
  <text x="960" y="445" font-size="15" font-weight="bold" fill="#000000">View Info</text>
  <!-- Crow's foot at Senior -->
  <line x1="810" y1="490" x2="830" y2="478" stroke="#000000" stroke-width="1.8"/>
  <line x1="810" y1="490" x2="830" y2="502" stroke="#000000" stroke-width="1.8"/>

  <!-- ======================================================== -->
  <!-- 5. CARE_LOG (Middle Right - Teal/Cyan Box)                -->
  <!-- ======================================================== -->
  <g transform="translate(1380, 560)">
    <rect width="240" height="170" rx="10" ry="10" fill="#daf2f0" stroke="#2f857d" stroke-width="2"/>
    <path d="M 0 42 L 240 42" stroke="#2f857d" stroke-width="1.8"/>
    <text x="120" y="29" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">CARE_LOG</text>
    <text x="18" y="78" font-size="15" font-weight="bold" fill="#000000" text-decoration="underline">Log_ID</text>
    <text x="18" y="112" font-size="15" fill="#000000">{Date}</text>
    <text x="18" y="146" font-size="15" fill="#000000">Status</text>
  </g>

  <!-- Relationship: CAREGIVER records CARE_LOG -->
  <path d="M 1340 425 L 1500 425 L 1500 560" fill="none" stroke="#000000" stroke-width="1.8"/>
  <line x1="1355" y1="415" x2="1355" y2="435" stroke="#000000" stroke-width="1.8"/>
  <line x1="1362" y1="415" x2="1362" y2="435" stroke="#000000" stroke-width="1.8"/>
  <text x="1440" y="415" font-size="15" font-weight="bold" fill="#000000" text-anchor="middle">records</text>
  <!-- Circle + Crow's foot at CARE_LOG -->
  <circle cx="1500" cy="535" r="7" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <line x1="1500" y1="560" x2="1488" y2="542" stroke="#000000" stroke-width="1.8"/>
  <line x1="1500" y1="560" x2="1512" y2="542" stroke="#000000" stroke-width="1.8"/>

  <!-- Relationship: SENIOR_PROFILE View CARE_LOG -->
  <path d="M 810 570 L 1080 570 L 1080 645 L 1380 645" fill="none" stroke="#000000" stroke-width="1.8"/>
  <line x1="825" y1="560" x2="825" y2="580" stroke="#000000" stroke-width="1.8"/>
  <line x1="832" y1="560" x2="832" y2="580" stroke="#000000" stroke-width="1.8"/>
  <text x="1090" y="560" font-size="15" font-weight="bold" fill="#000000">View</text>
  <!-- Crow's foot at CARE_LOG -->
  <line x1="1380" y1="645" x2="1360" y2="633" stroke="#000000" stroke-width="1.8"/>
  <line x1="1380" y1="645" x2="1360" y2="657" stroke="#000000" stroke-width="1.8"/>

  <!-- ======================================================== -->
  <!-- 6. APPOINTMENT (Lower Center - Orange Box)               -->
  <!-- ======================================================== -->
  <g transform="translate(900, 780)">
    <rect width="250" height="210" rx="10" ry="10" fill="#fff0dc" stroke="#d79b00" stroke-width="2"/>
    <path d="M 0 42 L 250 42" stroke="#d79b00" stroke-width="1.8"/>
    <text x="125" y="29" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">APPOINTMENT</text>
    <text x="18" y="76" font-size="15" font-weight="bold" fill="#000000" text-decoration="underline">Appt_ID</text>
    <text x="18" y="108" font-size="15" fill="#000000">DoctorName</text>
    <text x="18" y="140" font-size="15" fill="#000000">Date(Start, End)</text>
    <text x="18" y="172" font-size="15" fill="#000000">Reason</text>
    <text x="18" y="202" font-size="15" fill="#000000">Status</text>
  </g>

  <!-- Relationship: SENIOR_PROFILE Apply APPOINTMENT -->
  <path d="M 810 680 L 1025 680 L 1025 780" fill="none" stroke="#000000" stroke-width="1.8"/>
  <circle cx="828" cy="680" r="7" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="1010" y="730" font-size="15" font-weight="bold" fill="#000000">Apply</text>
  <!-- Circle + Crow's foot at APPOINTMENT -->
  <circle cx="1025" cy="755" r="7" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <line x1="1025" y1="780" x2="1013" y2="762" stroke="#000000" stroke-width="1.8"/>
  <line x1="1025" y1="780" x2="1037" y2="762" stroke="#000000" stroke-width="1.8"/>

  <!-- Relationship: APPOINTMENT update status CARE_LOG -->
  <path d="M 1150 885 L 1500 885 L 1500 730" fill="none" stroke="#000000" stroke-width="1.8"/>
  <circle cx="1168" cy="885" r="7" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="1465" y="870" font-size="15" font-weight="bold" fill="#000000" text-anchor="middle">update status</text>
  <circle cx="1500" cy="748" r="7" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>

  <!-- ======================================================== -->
  <!-- 7. DOSE_LOG (Bottom Left - Sky Blue Box)                 -->
  <!-- ======================================================== -->
  <g transform="translate(120, 1050)">
    <rect width="260" height="180" rx="10" ry="10" fill="#e3f0fc" stroke="#4a7bb0" stroke-width="2"/>
    <path d="M 0 42 L 260 42" stroke="#4a7bb0" stroke-width="1.8"/>
    <text x="130" y="29" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">DOSE_LOG</text>
    <text x="18" y="78" font-size="15" font-weight="bold" fill="#000000" text-decoration="underline">Log_ID</text>
    <text x="18" y="112" font-size="15" fill="#000000">Date(Month, Year)</text>
    <text x="18" y="146" font-size="15" fill="#000000">TotalMissedDoses</text>
    <text x="18" y="176" font-size="15" fill="#000000">SOS_AlertCount</text>
  </g>

  <!-- ======================================================== -->
  <!-- 8. MEDICATION (Bottom Center - Salmon Box)               -->
  <!-- ======================================================== -->
  <g transform="translate(740, 1120)">
    <rect width="280" height="270" rx="10" ry="10" fill="#ffe8e8" stroke="#b85450" stroke-width="2"/>
    <path d="M 0 42 L 280 42" stroke="#b85450" stroke-width="1.8"/>
    <text x="140" y="29" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">MEDICATION</text>
    <text x="18" y="78" font-size="15" font-weight="bold" fill="#000000" text-decoration="underline">Med_ID</text>
    <text x="18" y="110" font-size="15" fill="#000000">MedName</text>
    <text x="18" y="142" font-size="15" fill="#000000">Dosage</text>
    <text x="18" y="174" font-size="15" fill="#000000">Frequency</text>
    <text x="18" y="206" font-size="15" fill="#000000">[AdherenceRate]</text>
    <text x="18" y="238" font-size="15" fill="#000000">PrescriptionStatus</text>
    <text x="18" y="266" font-size="15" fill="#000000">StartDate</text>
  </g>

  <!-- Relationship: SENIOR_PROFILE View Info MEDICATION -->
  <path d="M 650 920 L 650 1210 L 740 1210" fill="none" stroke="#000000" stroke-width="1.8"/>
  <line x1="640" y1="935" x2="660" y2="935" stroke="#000000" stroke-width="1.8"/>
  <text x="630" y="1060" font-size="15" font-weight="bold" fill="#000000" text-anchor="middle">View Info</text>
  <!-- Crow's foot at MEDICATION -->
  <line x1="740" y1="1210" x2="720" y2="1198" stroke="#000000" stroke-width="1.8"/>
  <line x1="740" y1="1210" x2="720" y2="1222" stroke="#000000" stroke-width="1.8"/>

  <!-- Relationship: DOSE_LOG Calculates MEDICATION -->
  <path d="M 380 1140 L 520 1140 L 520 1310 L 740 1310" fill="none" stroke="#000000" stroke-width="1.8"/>
  <circle cx="398" cy="1140" r="7" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="560" y="1230" font-size="15" font-weight="bold" fill="#000000" text-anchor="middle">Calculates</text>
  <!-- Tick marks at Medication: || -->
  <line x1="720" y1="1300" x2="720" y2="1320" stroke="#000000" stroke-width="1.8"/>
  <line x1="727" y1="1300" x2="727" y2="1320" stroke="#000000" stroke-width="1.8"/>

  <!-- Relationship: CARE_LOG Process MEDICATION -->
  <path d="M 1620 645 L 1680 645 L 1680 1310 L 1020 1310" fill="none" stroke="#000000" stroke-width="1.8"/>
  <line x1="1630" y1="635" x2="1630" y2="655" stroke="#000000" stroke-width="1.8"/>
  <line x1="1637" y1="635" x2="1637" y2="655" stroke="#000000" stroke-width="1.8"/>
  <text x="1695" y="980" font-size="15" font-weight="bold" fill="#000000" text-anchor="middle">Process</text>
  <!-- Crow's foot at MEDICATION -->
  <line x1="1020" y1="1310" x2="1040" y2="1298" stroke="#000000" stroke-width="1.8"/>
  <line x1="1020" y1="1310" x2="1040" y2="1322" stroke="#000000" stroke-width="1.8"/>
</svg>"""

def render_high_res_png():
    svg_code = get_high_res_fig5_svg()
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #ffffff; width: 1760px; height: 1450px; overflow: hidden; }}
  svg {{ display: block; width: 1760px; height: 1450px; }}
</style>
</head>
<body>
{svg_code}
</body>
</html>"""

    tmp_html = os.path.join(BASE_DIR, "temp_fig5_hd.html")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html)

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    tmp_user_dir = tempfile.mkdtemp()
    
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={tmp_user_dir}",
        "--window-size=1760,1450",
        "--force-device-scale-factor=2.0",
        f"--screenshot={os.path.abspath(PNG_OUT)}",
        f"file:///{os.path.abspath(tmp_html).replace(os.sep, '/')}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
    if os.path.exists(tmp_html):
        os.remove(tmp_html)
        
    if os.path.exists(PNG_OUT):
        sz = os.path.getsize(PNG_OUT)
        print(f"Generated High-Res PNG: {PNG_OUT} ({sz:,} bytes)")
        im = Image.open(PNG_OUT)
        print(f"Rendered Image Dimensions: {im.size}")
        return True
    else:
        print(f"Failed to generate PNG: {res.stderr}")
        return False

if __name__ == "__main__":
    render_high_res_png()
