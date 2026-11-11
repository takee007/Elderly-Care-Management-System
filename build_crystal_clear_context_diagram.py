"""
build_crystal_clear_context_diagram.py
Generates an ultra-high-definition, publication-grade Level 0 Context Diagram (DFD)
for the Elderly Care Management System (ECMS).
Features:
- Central Process 0.0: Elderly Care Management System (ECMS)
- 7 External Entities: Administrator, Guardian, Caregiver, Doctor, Senior Resident,
  Twilio SMS Gateway, SMTP Email Server.
- Exact geometric intersections, zero overlap, generous margins, sharp contrast.
- Output: 3920 x 2880 pixels rendered via Headless Chrome.
"""

import os
import subprocess
import tempfile
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PNG_OUT_CONTEXT = os.path.join(BASE_DIR, "figures_png", "fig_context_diagram.png")
PNG_OUT_FIG0 = os.path.join(BASE_DIR, "figures_png", "fig0_context_diagram.png")
PNG_OUT_LEVEL0 = os.path.join(BASE_DIR, "figures_png", "fig_context_level0_dfd.png")

def get_high_res_context_diagram_svg():
    # Canvas: 1960 x 1440
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1960 1440" width="1960" height="1440" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <defs>
    <!-- Sharp, high-contrast arrowhead markers -->
    <marker id="arr-r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#000000"/>
    </marker>
    <marker id="arr-l" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 10 1.5 L 1 5 L 10 8.5 z" fill="#000000"/>
    </marker>
    <marker id="arr-u" viewBox="0 0 10 10" refX="5" refY="1" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 1.5 10 L 5 1 L 8.5 10 z" fill="#000000"/>
    </marker>
    <marker id="arr-d" viewBox="0 0 10 10" refX="5" refY="9" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 1.5 0 L 5 9 L 8.5 0 z" fill="#000000"/>
    </marker>
  </defs>

  <!-- ======================================================== -->
  <!-- CENTRAL PROCESS: 0.0 ECMS CORE ENGINE                    -->
  <!-- Center: (980, 720), Radius: 165                          -->
  <!-- ======================================================== -->
  <circle cx="980" cy="720" r="165" fill="#ffffff" stroke="#000000" stroke-width="2.4"/>
  
  <!-- Process Number 0.0 -->
  <text x="980" y="650" font-size="24" font-weight="bold" fill="#000000" text-anchor="middle">0.0</text>
  <line x1="880" y1="670" x2="1080" y2="670" stroke="#000000" stroke-width="1.8"/>
  
  <!-- System Title -->
  <text x="980" y="708" font-size="20" font-weight="bold" fill="#000000" text-anchor="middle">Elderly Care</text>
  <text x="980" y="738" font-size="20" font-weight="bold" fill="#000000" text-anchor="middle">Management System</text>
  <text x="980" y="768" font-size="17" font-weight="bold" fill="#000000" text-anchor="middle">(ECMS)</text>

  <!-- ======================================================== -->
  <!-- 7 EXTERNAL ENTITIES (Terminators)                        -->
  <!-- ======================================================== -->

  <!-- 1. Administrator (Top Center) -->
  <rect x="850" y="60" width="260" height="76" rx="8" ry="8" fill="#ffffff" stroke="#000000" stroke-width="2.2"/>
  <text x="980" y="96" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">Administrator</text>
  <text x="980" y="122" font-size="13" fill="#333333" text-anchor="middle">[System Manager]</text>

  <!-- 2. Doctor (Top Left) -->
  <rect x="70" y="240" width="260" height="76" rx="8" ry="8" fill="#ffffff" stroke="#000000" stroke-width="2.2"/>
  <text x="200" y="276" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">Doctor</text>
  <text x="200" y="302" font-size="13" fill="#333333" text-anchor="middle">[Healthcare Specialist]</text>

  <!-- 3. Senior Resident (Bottom Left) -->
  <rect x="70" y="1120" width="260" height="76" rx="8" ry="8" fill="#ffffff" stroke="#000000" stroke-width="2.2"/>
  <text x="200" y="1156" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">Senior Resident</text>
  <text x="200" y="1182" font-size="13" fill="#333333" text-anchor="middle">[Care Recipient]</text>

  <!-- 4. Caregiver (Bottom Center) -->
  <rect x="850" y="1300" width="260" height="76" rx="8" ry="8" fill="#ffffff" stroke="#000000" stroke-width="2.2"/>
  <text x="980" y="1336" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">Caregiver</text>
  <text x="980" y="1362" font-size="13" fill="#333333" text-anchor="middle">[Clinical Staff / Nurse]</text>

  <!-- 5. Guardian (Bottom Right) -->
  <rect x="1630" y="1120" width="260" height="76" rx="8" ry="8" fill="#ffffff" stroke="#000000" stroke-width="2.2"/>
  <text x="1760" y="1156" font-size="18" font-weight="bold" fill="#000000" text-anchor="middle">Guardian</text>
  <text x="1760" y="1182" font-size="13" fill="#333333" text-anchor="middle">[Family Member / Sponsor]</text>

  <!-- 6. Twilio SMS Gateway (Top Right) -->
  <rect x="1630" y="240" width="260" height="76" rx="8" ry="8" fill="#ffffff" stroke="#000000" stroke-width="2.2"/>
  <text x="1760" y="276" font-size="17" font-weight="bold" fill="#000000" text-anchor="middle">Twilio SMS Gateway</text>
  <text x="1760" y="302" font-size="13" fill="#333333" text-anchor="middle">[Telephony Dispatch API]</text>

  <!-- 7. SMTP Email Server (Middle Right) -->
  <rect x="1630" y="680" width="260" height="76" rx="8" ry="8" fill="#ffffff" stroke="#000000" stroke-width="2.2"/>
  <text x="1760" y="716" font-size="17" font-weight="bold" fill="#000000" text-anchor="middle">SMTP Email Server</text>
  <text x="1760" y="742" font-size="13" fill="#333333" text-anchor="middle">[Messaging Cloud Service]</text>

  <!-- ======================================================== -->
  <!-- DATA FLOWS: 1. ADMINISTRATOR <-> ECMS                    -->
  <!-- ======================================================== -->
  <!-- ECMS -> Administrator (Left vertical line at X=930) -->
  <line x1="930" y1="556" x2="930" y2="144" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-u)"/>
  <text x="915" y="340" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="end">System Health Metrics, Audit Trail Reports</text>

  <!-- Administrator -> ECMS (Right vertical line at X=1030) -->
  <line x1="1030" y1="136" x2="1030" y2="556" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-d)"/>
  <text x="1045" y="340" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="start">System Configurations, Staff &amp; Role Setup</text>

  <!-- ======================================================== -->
  <!-- DATA FLOWS: 2. DOCTOR <-> ECMS                           -->
  <!-- ======================================================== -->
  <!-- Doctor -> ECMS (Stepped orthogonal, turns down at X=480, enters circle at Y=600) -->
  <path d="M 330 262 L 480 262 L 480 600 L 859 600" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-r)"/>
  <text x="670" y="590" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Prescription Orders &amp; Dosage Guidelines</text>

  <!-- ECMS -> Doctor (Leaves circle at Y=655, turns up at X=410, enters Doctor at Y=292) -->
  <path d="M 830 655 L 410 655 L 410 292 L 338 292" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-l)"/>
  <text x="620" y="675" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Senior Clinical History &amp; Vitals Trends</text>

  <!-- ======================================================== -->
  <!-- DATA FLOWS: 3. SENIOR RESIDENT <-> ECMS                  -->
  <!-- ======================================================== -->
  <!-- Senior Resident -> ECMS (Leaves Senior at Y=1142, turns up at X=410, enters circle at Y=770) -->
  <path d="M 330 1142 L 410 1142 L 410 770 L 815 770" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-r)"/>
  <text x="615" y="760" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">One-Touch SOS Signals &amp; Dose Check-ins</text>

  <!-- ECMS -> Senior Resident (Leaves circle at Y=830, turns down at X=480, enters Senior at Y=1172) -->
  <path d="M 857 830 L 480 830 L 480 1172 L 338 1172" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-l)"/>
  <text x="670" y="848" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Visual/Audio Pill Chimes &amp; Schedule Prompts</text>

  <!-- ======================================================== -->
  <!-- DATA FLOWS: 4. CAREGIVER <-> ECMS                        -->
  <!-- ======================================================== -->
  <!-- Caregiver -> ECMS (Left vertical line at X=930) -->
  <line x1="930" y1="1300" x2="930" y2="888" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-u)"/>
  <text x="915" y="1100" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="end">Shift Handoffs, Vitals Readings, Care Logs</text>

  <!-- ECMS -> Caregiver (Right vertical line at X=1030) -->
  <line x1="1030" y1="884" x2="1030" y2="1292" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-d)"/>
  <text x="1045" y="1100" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="start">Daily Care Schedules &amp; Urgent Resident Alerts</text>

  <!-- ======================================================== -->
  <!-- DATA FLOWS: 5. TWILIO SMS GATEWAY <-> ECMS               -->
  <!-- ======================================================== -->
  <!-- ECMS -> Twilio (Leaves circle at Y=600, turns up at X=1480, enters Twilio at Y=262) -->
  <path d="M 1101 600 L 1480 600 L 1480 262 L 1622 262" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-r)"/>
  <text x="1290" y="590" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Emergency SOS Dispatch &amp; SMS Broadcasts</text>

  <!-- Twilio -> ECMS (Leaves Twilio at Y=292, turns down at X=1550, enters circle at Y=655) -->
  <path d="M 1630 292 L 1550 292 L 1550 655 L 1130 655" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-l)"/>
  <text x="1340" y="675" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">SMS Delivery Status (DLR) &amp; Inbound Replies</text>

  <!-- ======================================================== -->
  <!-- DATA FLOWS: 6. SMTP EMAIL SERVER <-> ECMS                -->
  <!-- ======================================================== -->
  <!-- ECMS -> SMTP (Clean straight horizontal line at Y=705) -->
  <line x1="1145" y1="705" x2="1622" y2="705" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-r)"/>
  <text x="1385" y="697" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Weekly Clinical Digests &amp; Password Reset Tokens</text>

  <!-- SMTP -> ECMS (Clean straight horizontal line at Y=735) -->
  <line x1="1630" y1="735" x2="1147" y2="735" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-l)"/>
  <text x="1385" y="753" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Delivery Status Notifications (DSN) &amp; Bounces</text>

  <!-- ======================================================== -->
  <!-- DATA FLOWS: 7. GUARDIAN <-> ECMS                         -->
  <!-- ======================================================== -->
  <!-- Guardian -> ECMS (Leaves Guardian at Y=1142, turns up at X=1550, enters circle at Y=770) -->
  <path d="M 1630 1142 L 1550 1142 L 1550 770 L 1145 770" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-l)"/>
  <text x="1340" y="788" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Care Directives &amp; Teleconsult Bookings</text>

  <!-- ECMS -> Guardian (Leaves circle at Y=830, turns down at X=1480, enters Guardian at Y=1172) -->
  <path d="M 1103 830 L 1480 830 L 1480 1172 L 1622 1172" fill="none" stroke="#000000" stroke-width="1.8" marker-end="url(#arr-r)"/>
  <text x="1290" y="848" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Daily Care Progress, Adherence &amp; SOS Alerts</text>
</svg>"""

def render_high_res_png():
    svg_code = get_high_res_context_diagram_svg()
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #ffffff; width: 1960px; height: 1440px; overflow: hidden; }}
  svg {{ display: block; width: 1960px; height: 1440px; }}
</style>
</head>
<body>
{svg_code}
</body>
</html>"""

    tmp_html = os.path.join(BASE_DIR, "temp_context_hd.html")
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
        "--window-size=1960,1440",
        "--force-device-scale-factor=2.0",
        f"--screenshot={os.path.abspath(PNG_OUT_CONTEXT)}",
        f"file:///{os.path.abspath(tmp_html).replace(os.sep, '/')}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
    if os.path.exists(tmp_html):
        os.remove(tmp_html)
        
    if os.path.exists(PNG_OUT_CONTEXT):
        import shutil
        shutil.copyfile(PNG_OUT_CONTEXT, PNG_OUT_FIG0)
        shutil.copyfile(PNG_OUT_CONTEXT, PNG_OUT_LEVEL0)
        
        sz = os.path.getsize(PNG_OUT_CONTEXT)
        print(f"Generated High-Res PNG: {PNG_OUT_CONTEXT} ({sz:,} bytes)")
        im = Image.open(PNG_OUT_CONTEXT)
        print(f"Rendered Image Dimensions: {im.size}")
        return True
    else:
        print(f"Failed to generate PNG: {res.stderr}")
        return False

if __name__ == "__main__":
    render_high_res_png()
