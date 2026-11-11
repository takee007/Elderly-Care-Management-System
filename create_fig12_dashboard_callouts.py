"""
Generate fig12_dashboard_callouts.png
Clean, professional black & white UI wireframe diagram with callout circles (1) through (7)
for Appendix C Example 1 matching SRS_Template.docx.pdf.
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(BASE_DIR, "figures_png", "fig12_dashboard_callouts.png")

# Dimensions: 1200 x 750
w, h = 1200, 750
img = Image.new("RGB", (w, h), "#FFFFFF")
draw = ImageDraw.Draw(img)

# Try to load a clean TTF font, or fallback to default
try:
    font_title = ImageFont.truetype("arial.ttf", 22)
    font_bold = ImageFont.truetype("arialbd.ttf", 16)
    font_reg = ImageFont.truetype("arial.ttf", 14)
    font_small = ImageFont.truetype("arial.ttf", 12)
    font_badge = ImageFont.truetype("arialbd.ttf", 15)
except Exception:
    font_title = ImageFont.load_default()
    font_bold = ImageFont.load_default()
    font_reg = ImageFont.load_default()
    font_small = ImageFont.load_default()
    font_badge = ImageFont.load_default()

# Helper for drawing callout badges: black filled circle with white text
def draw_callout(draw, x, y, num_str):
    r = 16
    draw.ellipse([x - r, y - r, x + r, y + r], fill="#000000", outline="#000000")
    # center text
    draw.text((x - 6, y - 9), num_str, fill="#FFFFFF", font=font_badge)

# Outer Browser / Window Frame
draw.rectangle([20, 20, w - 20, h - 20], outline="#333333", width=2)
# Window Title Bar
draw.rectangle([20, 20, w - 20, 60], fill="#E5E7EB", outline="#333333", width=2)
draw.ellipse([35, 33, 47, 45], fill="#9CA3AF")
draw.ellipse([55, 33, 67, 45], fill="#9CA3AF")
draw.ellipse([75, 33, 87, 45], fill="#9CA3AF")
draw.text((105, 30), "ECMS - Caregiver Clinical Operations Dashboard | v1.0", fill="#000000", font=font_bold)

# Top Nav Bar
draw.rectangle([20, 60, w - 20, 115], fill="#F3F4F6", outline="#9CA3AF", width=1)
draw.text((40, 77), "Elderly Care Management System", fill="#000000", font=font_title)

# Callout 1: Senior Resident Selector Dropdown
draw.rectangle([540, 72, 880, 105], fill="#FFFFFF", outline="#000000", width=1)
draw.text((550, 79), "Active Resident: Abdul Karim (Age: 74, Rm 204) ▼", fill="#000000", font=font_reg)
draw_callout(draw, 895, 88, "1")

# Callout 7: Prominent Emergency SOS Trigger Button
draw.rectangle([940, 68, 1150, 108], fill="#000000", outline="#000000", width=2)
draw.text((965, 78), "[ EMERGENCY SOS ]", fill="#FFFFFF", font=font_bold)
draw_callout(draw, 1158, 62, "7")

# Callout 2: Active Emergency Alert Banner (High-contrast)
draw.rectangle([40, 130, w - 40, 175], fill="#F3F4F6", outline="#000000", width=2)
draw.text((60, 142), "CRITICAL ALERT: Elevated Systolic BP (182 mmHg) recorded for Abdul Karim (Room 204) - Attending Physician Notified", fill="#000000", font=font_bold)
draw_callout(draw, w - 60, 152, "2")

# Main Content Grid: Left 2/3 (Vitals + Meds), Right 1/3 (Shift Notes)
left_w = 760

# Callout 3: Vitals Telemetry Cards Header
draw.text((40, 195), "Real-Time Vitals Telemetry (Last updated: 10 mins ago)", fill="#000000", font=font_bold)
draw_callout(draw, 490, 203, "3")

# 4 Vitals Cards
v_cards = [
    ("Blood Pressure", "120 / 80", "mmHg", "Normal (Optimal)"),
    ("Pulse Rate", "72", "BPM", "Normal (Resting)"),
    ("Blood Oxygen", "98%", "SpO2", "Optimal Saturation"),
    ("Blood Glucose", "6.4", "mmol/L", "Fasting Target")
]
cw = 165
for i, (vt, val, unit, status) in enumerate(v_cards):
    cx = 40 + i * (cw + 17)
    draw.rectangle([cx, 225, cx + cw, 315], fill="#FFFFFF", outline="#666666", width=1)
    draw.text((cx + 10, 235), vt, fill="#333333", font=font_small)
    draw.text((cx + 10, 255), val, fill="#000000", font=font_title)
    draw.text((cx + 115, 262), unit, fill="#666666", font=font_small)
    draw.text((cx + 10, 292), status, fill="#000000", font=font_small)

# Callout 4 & 5: Medication Administration Record Timetable
draw.text((40, 335), "Today's Medication Administration Record (MAR)", fill="#000000", font=font_bold)
draw_callout(draw, 445, 343, "4")

# Table Header
draw.rectangle([40, 365, left_w, 395], fill="#E5E7EB", outline="#333333", width=1)
draw.text((50, 373), "Time", fill="#000000", font=font_bold)
draw.text((120, 373), "Medication & Dosage", fill="#000000", font=font_bold)
draw.text((315, 373), "Instructions", fill="#000000", font=font_bold)
draw.text((440, 373), "Status", fill="#000000", font=font_bold)
draw.text((545, 373), "Administration Action", fill="#000000", font=font_bold)
draw_callout(draw, left_w - 25, 380, "5")

# Table Rows
med_rows = [
    ("08:00 AM", "Metformin 500mg Tablet", "After Breakfast", "GIVEN", "[ View Log ]"),
    ("08:00 AM", "Donepezil 5mg Tablet", "With Water", "GIVEN", "[ View Log ]"),
    ("01:00 PM", "Multivitamin 1 Tab", "After Lunch", "PENDING", "[ Give ] [ Miss ] [ Refuse ]"),
    ("08:00 PM", "Amlodipine 5mg Tablet", "Bedtime", "QUEUED", "[ Give ] [ Miss ] [ Refuse ]")
]

for idx, (mt, md, mi, ms, ma) in enumerate(med_rows):
    ry = 395 + idx * 45
    bg = "#FFFFFF" if idx % 2 == 0 else "#F9FAFB"
    draw.rectangle([40, ry, left_w, ry + 45], fill=bg, outline="#D1D5DB", width=1)
    draw.text((50, ry + 14), mt, fill="#000000", font=font_reg)
    draw.text((120, ry + 14), md, fill="#000000", font=font_bold)
    draw.text((320, ry + 14), mi, fill="#4B5563", font=font_reg)
    draw.text((460, ry + 14), ms, fill="#000000", font=font_bold)
    draw.text((560, ry + 14), ma, fill="#000000", font=font_reg)

# Recent Activity Audit Trail (Bottom Left)
draw.text((40, 590), "Recent Care Activity Log:", fill="#000000", font=font_bold)
draw.rectangle([40, 615, left_w, 710], fill="#FAFAFA", outline="#9CA3AF", width=1)
draw.text((55, 625), "• 08:15 AM - Morning Vitals recorded by Nurse Shamima (BP: 120/80, Pulse: 72 bpm)", fill="#000000", font=font_small)
draw.text((55, 650), "• 08:22 AM - Metformin 500mg administered & co-signed with caregiver PIN 4421", fill="#000000", font=font_small)
draw.text((55, 675), "• 10:45 AM - Physical therapy mobility walk completed (15 minutes assisted)", fill="#000000", font=font_small)

# Right Column: Callout 6 Shift Handoff Quick Notes Area
right_x = 790
right_w = w - 40 - right_x
draw.text((right_x, 195), "Caregiver Shift Handoff Notes", fill="#000000", font=font_bold)
draw_callout(draw, right_x + 245, 203, "6")

draw.rectangle([right_x, 225, w - 40, 710], fill="#FFFFFF", outline="#333333", width=1)

# Sub-header in Shift Notes
draw.rectangle([right_x, 225, w - 40, 265], fill="#E5E7EB", outline="#333333", width=1)
draw.text((right_x + 15, 237), "Current Duty: Morning Shift (06:00 - 14:00)", fill="#000000", font=font_bold)

draw.text((right_x + 15, 280), "Clinical Progress Notes:", fill="#000000", font=font_bold)
notes_text = [
    "Resident in good spirits this morning.",
    "Ate 90% of breakfast (soft diet).",
    "Reported mild joint stiffness in left",
    "knee during morning ambulation.",
    "",
    "Flagged for Afternoon Shift:",
    "• Dr. Rahman scheduled teleconsult at",
    "  03:30 PM (Review lipid panel).",
    "• Monitor fluid intake (min 800ml).",
    "• 01:00 PM multivitamin pending."
]
for li, line in enumerate(notes_text):
    fnt = font_bold if "Flagged" in line else font_reg
    draw.text((right_x + 15, 305 + li * 22), line, fill="#000000", font=fnt)

draw.line([right_x + 15, 550, w - 55, 550], fill="#D1D5DB", width=1)
draw.text((right_x + 15, 565), "Duty Nurse: Shamima Akter, RN", fill="#000000", font=font_reg)
draw.text((right_x + 15, 590), "Handoff Status: In Progress", fill="#000000", font=font_small)

# Handoff Action Button
draw.rectangle([right_x + 15, 630, w - 55, 680], fill="#000000", outline="#000000", width=1)
draw.text((right_x + 55, 646), "SUBMIT & SIGN HANDOFF", fill="#FFFFFF", font=font_bold)

img.save(OUT_PATH, "PNG")
print(f"Created {OUT_PATH}")
