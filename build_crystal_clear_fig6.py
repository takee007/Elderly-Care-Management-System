"""
build_crystal_clear_fig6.py
Generates a publication-grade, razor-sharp Data Flow Diagram (Figure 6)
strictly matching the demo.pdf Level-1 DFD layout with optimal typography,
perfect geometric spacing, and 100% crisp, legible text.
"""

import os
import subprocess
import tempfile
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PNG_OUT = os.path.join(BASE_DIR, "figures_png", "fig6_data_flow_diagram.png")

def get_high_res_fig6_svg():
    # Canvas: 1600 x 1150
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1150" width="1600" height="1150" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <defs>
    <!-- Sharp, high-contrast arrowhead markers -->
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#000000"/>
    </marker>
    <marker id="arrow-down" viewBox="0 0 10 10" refX="5" refY="9" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 1.5 0 L 5 9 L 8.5 0 z" fill="#000000"/>
    </marker>
    <marker id="arrow-up" viewBox="0 0 10 10" refX="5" refY="1" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 1.5 10 L 5 1 L 8.5 10 z" fill="#000000"/>
    </marker>
  </defs>

  <!-- ======================================================== -->
  <!-- 4 CENTRAL PROCESS CIRCLES (R = 72)                       -->
  <!-- ======================================================== -->
  
  <!-- Process 1: User Management -->
  <circle cx="800" cy="150" r="72" fill="#ffffff" stroke="#000000" stroke-width="2"/>
  <text x="800" y="143" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">User</text>
  <text x="800" y="166" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Management</text>

  <!-- Process 2: Medication Management -->
  <circle cx="800" cy="430" r="72" fill="#ffffff" stroke="#000000" stroke-width="2"/>
  <text x="800" y="423" font-size="15.5" font-weight="bold" fill="#000000" text-anchor="middle">Medication</text>
  <text x="800" y="446" font-size="15.5" font-weight="bold" fill="#000000" text-anchor="middle">Management</text>

  <!-- Process 3: Daily Care Management -->
  <circle cx="800" cy="710" r="72" fill="#ffffff" stroke="#000000" stroke-width="2"/>
  <text x="800" y="703" font-size="15.5" font-weight="bold" fill="#000000" text-anchor="middle">Daily Care</text>
  <text x="800" y="726" font-size="15.5" font-weight="bold" fill="#000000" text-anchor="middle">Management</text>

  <!-- Process 4: Appointment & SOS Management -->
  <circle cx="800" cy="990" r="72" fill="#ffffff" stroke="#000000" stroke-width="2"/>
  <text x="800" y="983" font-size="14.5" font-weight="bold" fill="#000000" text-anchor="middle">Appointment &amp;</text>
  <text x="800" y="1005" font-size="14.5" font-weight="bold" fill="#000000" text-anchor="middle">SOS Management</text>

  <!-- ======================================================== -->
  <!-- LEFT ENTITY BOXES (Width = 190, Height = 64)             -->
  <!-- Left X = 250, Right X = 440, Center = 345                 -->
  <!-- ======================================================== -->
  
  <!-- Left 1: Admin / Doctor -->
  <rect x="250" y="118" width="190" height="64" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="345" y="156" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Admin / Doctor</text>

  <!-- Left 2: Doctor -->
  <rect x="250" y="398" width="190" height="64" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="345" y="436" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Doctor</text>

  <!-- Left 3: Caregiver -->
  <rect x="250" y="678" width="190" height="64" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="345" y="716" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Caregiver</text>

  <!-- Left 4: First Responder -->
  <rect x="250" y="958" width="190" height="64" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="345" y="996" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">First Responder</text>

  <!-- ======================================================== -->
  <!-- RIGHT ENTITY BOXES (Width = 190, Height = 64)            -->
  <!-- Left X = 1160, Right X = 1350, Center = 1255             -->
  <!-- ======================================================== -->
  
  <!-- Right 1: Senior / Guardian -->
  <rect x="1160" y="118" width="190" height="64" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="1255" y="156" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Senior / Guardian</text>

  <!-- Right 2: Senior / Guardian -->
  <rect x="1160" y="398" width="190" height="64" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="1255" y="436" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Senior / Guardian</text>

  <!-- Right 3: Senior Citizen -->
  <rect x="1160" y="678" width="190" height="64" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="1255" y="716" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Senior Citizen</text>

  <!-- Right 4: Senior / Guardian -->
  <rect x="1160" y="958" width="190" height="64" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <text x="1255" y="996" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">Senior / Guardian</text>

  <!-- ======================================================== -->
  <!-- VERTICAL DOWN-CENTER FLOWS BETWEEN PROCESSES             -->
  <!-- ======================================================== -->
  
  <!-- Process 1 -> Process 2 -->
  <line x1="800" y1="222" x2="800" y2="350" stroke="#000000" stroke-width="1.8" marker-end="url(#arrow)"/>
  <text x="815" y="290" font-size="13.5" font-weight="bold" fill="#000000">User Details</text>

  <!-- Process 2 -> Process 3 -->
  <line x1="800" y1="502" x2="800" y2="630" stroke="#000000" stroke-width="1.8" marker-end="url(#arrow)"/>
  <text x="815" y="570" font-size="13.5" font-weight="bold" fill="#000000">Care Data</text>

  <!-- Process 3 -> Process 4 -->
  <line x1="800" y1="782" x2="800" y2="910" stroke="#000000" stroke-width="1.8" marker-end="url(#arrow)"/>
  <text x="815" y="850" font-size="13.5" font-weight="bold" fill="#000000">Vital &amp; SOS Logs</text>

  <!-- ======================================================== -->
  <!-- ROW 1 FLOWS: USER MANAGEMENT                             -->
  <!-- ======================================================== -->
  
  <!-- Left Box 1 -> Process 1 (Direct top line) -->
  <line x1="440" y1="136" x2="720" y2="136" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)"/>
  <text x="585" y="125" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Login</text>
  
  <!-- Process 1 -> Left Box 1 (Hooked return line) -->
  <path d="M 734 180 L 630 180 L 630 215 L 345 215 L 345 188" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow-up)"/>
  <text x="487" y="208" font-size="12" fill="#000000" text-anchor="middle">Checks Login, Dashboard Access, User List</text>

  <!-- Right Box 1 -> Process 1 (Direct top line) -->
  <line x1="1160" y1="136" x2="880" y2="136" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)"/>
  <text x="1015" y="125" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Login, Create Account, Edit Info</text>

  <!-- Process 1 -> Right Box 1 (Hooked return line) -->
  <path d="M 866 180 L 970 180 L 970 215 L 1255 215 L 1255 188" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow-up)"/>
  <text x="1112" y="208" font-size="12" fill="#000000" text-anchor="middle">Confirmation of Login, Account, Dashboard</text>

  <!-- ======================================================== -->
  <!-- ROW 2 FLOWS: MEDICATION MANAGEMENT                       -->
  <!-- ======================================================== -->
  
  <!-- Process 2 -> Left Box 2 (Direct top line) -->
  <line x1="728" y1="416" x2="446" y2="416" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)"/>
  <text x="585" y="405" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Prescription &amp; Dose View</text>

  <!-- Left Box 2 -> Process 2 (Hooked lower line, stops at circle bottom perimeter) -->
  <path d="M 345 462 L 345 498 L 760 498 L 760 493" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow-up)"/>
  <text x="550" y="490" font-size="12" fill="#000000" text-anchor="middle">Approve / Modify Medication Regimen</text>

  <!-- Right Box 2 -> Process 2 (Direct top line) -->
  <line x1="1160" y1="416" x2="880" y2="416" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)"/>
  <text x="1015" y="405" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Dose Confirm, Schedule Query</text>

  <!-- Process 2 -> Right Box 2 (Hooked lower line) -->
  <path d="M 840 491 L 840 498 L 1255 498 L 1255 468" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow-up)"/>
  <text x="1045" y="490" font-size="12" fill="#000000" text-anchor="middle">Dose Reminders, Adherence Report</text>

  <!-- ======================================================== -->
  <!-- ROW 3 FLOWS: DAILY CARE MANAGEMENT                       -->
  <!-- ======================================================== -->
  
  <!-- Process 3 -> Left Box 3 (Direct top line) -->
  <line x1="728" y1="696" x2="446" y2="696" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)"/>
  <text x="585" y="685" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Shift Care Status</text>

  <!-- Left Box 3 -> Process 3 (Hooked lower line, stops at circle bottom perimeter) -->
  <path d="M 345 742 L 345 778 L 760 778 L 760 773" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow-up)"/>
  <text x="550" y="770" font-size="12" fill="#000000" text-anchor="middle">Submit Shift Handoff, Vital Readings</text>

  <!-- Right Box 3 -> Process 3 (Direct top line) -->
  <line x1="1160" y1="696" x2="880" y2="696" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)"/>
  <text x="1015" y="685" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Request Daily Care Tasks</text>

  <!-- Process 3 -> Right Box 3 (Hooked lower line) -->
  <path d="M 840 771 L 840 778 L 1255 778 L 1255 748" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow-up)"/>
  <text x="1045" y="770" font-size="12" fill="#000000" text-anchor="middle">Daily Routine, Care Records</text>

  <!-- ======================================================== -->
  <!-- ROW 4 FLOWS: APPOINTMENT & SOS MANAGEMENT                -->
  <!-- ======================================================== -->
  
  <!-- Left Box 4 -> Process 4 (Clean top line at y=976) -->
  <line x1="440" y1="976" x2="720" y2="976" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)"/>
  <text x="585" y="965" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Acknowledge SOS, Consult Notes</text>

  <!-- Process 4 -> Left Box 4 (Hooked lower line dropped cleanly below circle) -->
  <path d="M 770 1060 L 770 1082 L 345 1082 L 345 1028" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow-up)"/>
  <text x="550" y="1075" font-size="12" fill="#000000" text-anchor="middle">Live GPS Coordinates, Emergency Health Brief</text>

  <!-- Right Box 4 -> Process 4 (Clean top line at y=976) -->
  <line x1="1160" y1="976" x2="880" y2="976" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)"/>
  <text x="1015" y="965" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle">Trigger SOS, Book Appointment</text>

  <!-- Process 4 -> Right Box 4 (Hooked lower line dropped cleanly below circle) -->
  <path d="M 830 1060 L 830 1082 L 1255 1082 L 1255 1028" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow-up)"/>
  <text x="1045" y="1075" font-size="12" fill="#000000" text-anchor="middle">SOS Broadcast Alert, Appointment Slot</text>

  <!-- ======================================================== -->
  <!-- LONG OUTER BYPASS CASCADES (User Details Lines)          -->
  <!-- ======================================================== -->
  
  <!-- Left Outer Bypass Line: From Top Process 1 around to Left 4 -->
  <path d="M 760 90 L 760 60 L 100 60 L 100 990 L 244 990" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)"/>
  <text x="82" y="550" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle" transform="rotate(-90 82 550)">User Details</text>

  <!-- Branch from Left Outer Line into Left Box 2 (Doctor) -->
  <line x1="100" y1="430" x2="244" y2="430" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)"/>
  <text x="172" y="420" font-size="12.5" font-weight="bold" fill="#000000" text-anchor="middle">User Details</text>

  <!-- Right Outer Bypass Line: From Top Process 1 around to Right 3 -->
  <path d="M 840 90 L 840 60 L 1500 60 L 1500 710 L 1356 710" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)"/>
  <text x="1518" y="430" font-size="13.5" font-weight="bold" fill="#000000" text-anchor="middle" transform="rotate(90 1518 430)">User Details</text>
</svg>"""

def render_high_res_png():
    svg_code = get_high_res_fig6_svg()
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #ffffff; width: 1600px; height: 1150px; overflow: hidden; }}
  svg {{ display: block; width: 1600px; height: 1150px; }}
</style>
</head>
<body>
{svg_code}
</body>
</html>"""

    tmp_html = os.path.join(BASE_DIR, "temp_fig6_hd.html")
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
        "--window-size=1600,1150",
        "--force-device-scale-factor=1.5",
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
