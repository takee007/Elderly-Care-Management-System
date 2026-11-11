# Generate Fig 11: Gantt Chart for Elderly Care Management System matching demo.pdf p48 Google Sheets layout exactly

import subprocess
import os
import tempfile

ACTIVITIES = [
    ("A", "Project Topic Selection", "1", "-", [0]),
    ("B", "Requirement Collection & Feature Selection", "2", "A", [1, 2]),
    ("C", "Create Account Module", "2", "B", [3, 4]),
    ("D", "Login Module", "2", "C", [5, 6]),
    ("E", "Dashboard (Senior & Guardian)", "3", "D", [7, 8, 9]),
    ("F", "Medication Scheduling Module", "3", "E", [10, 11, 12]),
    ("G", "Dose Adherence & Intake Logging", "2", "F", [13, 14]),
    ("H", "Daily Care Routine & Vitals Module", "3", "E", [10, 11, 12]),
    ("I", "Vital History & Anomaly Alert", "2", "H", [13, 14]),
    ("J", "Appointment Scheduling Module", "2", "E", [10, 11]),
    ("K", "Prescription Archive Module", "2", "J", [12, 13]),
    ("L", "Emergency SOS Dispatch Module", "1", "K", [14]),
    ("M", "Senior Profile Baseline Setup", "2", "C", [5, 6]),
    ("N", "Caregiver Shift Handoff Notes", "1", "M", [7]),
    ("O", "System Testing", "4", "All", [15, 16, 17, 18]),
    ("P", "Documentation", "3", "O", [19, 20, 21]),
    ("Q", "Final Deployment", "1", "P", [22]),
]

DAY_COLS = ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA"]

def generate_gantt_html():
    rows_html = ""
    # Header Row (Row 1) - Columns E to AA are blank cells in the actual spreadsheet!
    empty_day_cells = "".join(['<td class="day-cell"></td>' for _ in DAY_COLS])
    rows_html += f"""
    <tr>
      <td class="row-num">1</td>
      <td class="cell sl-col">SL</td>
      <td class="cell name-col">Activity Name</td>
      <td class="cell dur-col">Duration (Days)</td>
      <td class="cell dep-col">Dependency</td>
      {empty_day_cells}
    </tr>
    """

    for idx, (sl, name, dur, dep, active_days) in enumerate(ACTIVITIES, start=2):
        day_cells = ""
        for day_idx in range(len(DAY_COLS)):
            if day_idx in active_days:
                day_cells += '<td class="day-cell active-bar"></td>'
            else:
                day_cells += '<td class="day-cell"></td>'

        rows_html += f"""
        <tr>
          <td class="row-num">{idx}</td>
          <td class="cell sl-col">{sl}</td>
          <td class="cell name-col">{name}</td>
          <td class="cell dur-col">{dur}</td>
          <td class="cell dep-col">{dep}</td>
          {day_cells}
        </tr>
        """

    col_headers_days = "".join([f'<th class="col-header day-col">{col}</th>' for col in DAY_COLS])

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    padding: 0;
    background: #ffffff;
    font-family: Arial, Roboto, Helvetica, sans-serif;
    color: #111111;
    display: inline-block;
  }}
  .spreadsheet-container {{
    display: inline-block;
    background: #ffffff;
    border: 1px solid #d3d3d3;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }}
  /* Formula Bar */
  .formula-bar {{
    display: flex;
    align-items: center;
    background: #ffffff;
    border-bottom: 1px solid #e0e0e0;
    padding: 3px 6px;
    height: 24px;
    font-size: 11px;
    user-select: none;
  }}
  .cell-name-box {{
    display: flex;
    align-items: center;
    padding-left: 4px;
    padding-right: 6px;
    border-right: 1px solid #e0e0e0;
    height: 100%;
  }}
  .cell-name {{
    font-size: 11px;
    color: #333333;
    font-weight: 500;
  }}
  .dropdown-arrow {{
    font-size: 7px;
    margin-left: 5px;
    color: #666666;
  }}
  .fx-box {{
    display: flex;
    align-items: center;
    padding-left: 8px;
    padding-right: 10px;
    border-right: 1px solid #e0e0e0;
    height: 100%;
  }}
  .fx-icon {{
    color: #777777;
    font-style: italic;
    font-family: "Georgia", serif;
    font-size: 12px;
    font-weight: bold;
  }}
  .formula-input {{
    flex: 1;
    height: 100%;
  }}
  
  /* Table styling */
  .spreadsheet {{
    border-collapse: collapse;
    table-layout: fixed;
    background: #ffffff;
  }}
  th, td {{
    border: 1px solid #e0e0e0;
    padding: 0 4px;
    font-size: 11px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    height: 20px;
    line-height: 20px;
  }}
  
  /* Header rows and columns */
  .col-header {{
    background: #f8f9fa;
    color: #555555;
    font-weight: normal;
    text-align: center;
    border-bottom: 1px solid #c8c8c8;
    height: 21px;
    font-size: 10px;
    user-select: none;
  }}
  .col-header.selected-col {{
    background: #e8f0fe;
    color: #1a73e8;
    font-weight: bold;
  }}
  .row-num {{
    background: #f8f9fa;
    color: #555555;
    text-align: center;
    width: 26px;
    min-width: 26px;
    max-width: 26px;
    font-size: 9.5px;
    user-select: none;
    border-right: 1px solid #c8c8c8;
    padding: 0;
  }}
  
  /* Column widths */
  .col-a {{ width: 28px; min-width: 28px; max-width: 28px; }}
  .col-b {{ width: 245px; min-width: 245px; max-width: 245px; }}
  .col-c {{ width: 88px; min-width: 88px; max-width: 88px; }}
  .col-d {{ width: 78px; min-width: 78px; max-width: 78px; }}
  .day-col, .day-cell {{
    width: 21px;
    min-width: 21px;
    max-width: 21px;
    padding: 0;
    text-align: center;
  }}
  
  .sl-col {{ text-align: left; padding-left: 5px; }}
  .name-col {{ text-align: left; padding-left: 5px; }}
  .dur-col {{ text-align: left; padding-left: 5px; }}
  .dep-col {{ text-align: left; padding-left: 5px; }}
  
  /* Gantt red bar */
  .active-bar {{
    background: #cc0000 !important;
    border: 1px solid #ba0000 !important;
  }}
</style>
</head>
<body>
  <div class="spreadsheet-container">
    <div class="formula-bar">
      <div class="cell-name-box">
        <span class="cell-name">D35</span>
        <span class="dropdown-arrow">▼</span>
      </div>
      <div class="fx-box">
        <span class="fx-icon">fx</span>
      </div>
      <div class="formula-input"></div>
    </div>
    <table class="spreadsheet">
      <thead>
        <tr>
          <th class="col-header" style="width: 26px;"></th>
          <th class="col-header col-a">A</th>
          <th class="col-header col-b">B</th>
          <th class="col-header col-c">C</th>
          <th class="col-header col-d selected-col">D</th>
          {col_headers_days}
        </tr>
      </thead>
      <tbody>
        {rows_html}
      </tbody>
    </table>
  </div>
</body>
</html>"""
    return html

def render_gantt_png(output_png="figures_png/fig11_gantt_chart.png"):
    html_content = generate_gantt_html()
    tmp_html = output_png.replace(".png", ".html")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    tmp_user_dir = tempfile.mkdtemp()
    # Total table width is approx 26 + 28 + 245 + 88 + 78 + 23*21 = 948px
    # Height is approx 24 (formula) + 21 (header) + 18 * 20 (rows) = 405px
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={tmp_user_dir}",
        "--window-size=980,480",
        f"--screenshot={os.path.abspath(output_png)}",
        "file:///" + os.path.abspath(tmp_html).replace(os.sep, "/")
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=20)
    if os.path.exists(tmp_html):
        os.remove(tmp_html)

    # Now trim/crop any extra white margin if PIL is available
    try:
        from PIL import Image
        img = Image.open(output_png)
        # Bounding box of content: table is 956 wide, 430 high
        crop_w = min(960, img.width)
        crop_h = min(440, img.height)
        img_cropped = img.crop((0, 0, crop_w, crop_h))
        img_cropped.save(output_png)
    except Exception as e:
        print(f"PIL crop warning: {e}")

    print(f"Generated {output_png} ({os.path.getsize(output_png):,} bytes)")

def get_exact_demo_style_fig11_svg():
    # Return vector SVG representation for scalable rendering in HTML/PDF
    row_height = 20
    header_h = 21
    formula_h = 24
    total_height = formula_h + header_h + (len(ACTIVITIES) + 1) * row_height + 4
    
    col_a_w = 28
    col_b_w = 245
    col_c_w = 88
    col_d_w = 78
    day_w = 21
    table_x = 26
    table_w = col_a_w + col_b_w + col_c_w + col_d_w + len(DAY_COLS) * day_w
    svg_w = table_x + table_w
    
    cells_svg = []
    
    # Formula bar
    cells_svg.append(f'<rect x="0" y="0" width="{svg_w}" height="{formula_h}" fill="#ffffff" stroke="#d3d3d3" stroke-width="1"/>')
    cells_svg.append('<text x="8" y="16" font-size="11" font-weight="500" fill="#333333">D35</text>')
    cells_svg.append('<text x="32" y="15" font-size="7" fill="#666666">▼</text>')
    cells_svg.append(f'<line x1="44" y1="0" x2="44" y2="{formula_h}" stroke="#e0e0e0" stroke-width="1"/>')
    cells_svg.append('<text x="52" y="16" font-size="12" font-style="italic" font-family="Georgia, serif" font-weight="bold" fill="#777777">fx</text>')
    cells_svg.append(f'<line x1="70" y1="0" x2="70" y2="{formula_h}" stroke="#e0e0e0" stroke-width="1"/>')
    cells_svg.append(f'<line x1="0" y1="{formula_h}" x2="{svg_w}" y2="{formula_h}" stroke="#e0e0e0" stroke-width="1"/>')
    
    # Column Header row
    y_hdr = formula_h
    cells_svg.append(f'<rect x="0" y="{y_hdr}" width="{table_x}" height="{header_h}" fill="#f8f9fa" stroke="#e0e0e0" stroke-width="1"/>')
    cells_svg.append(f'<rect x="{table_x}" y="{y_hdr}" width="{table_w}" height="{header_h}" fill="#f8f9fa" stroke="#c8c8c8" stroke-width="1"/>')
    # Highlight Col D
    cells_svg.append(f'<rect x="{table_x + col_a_w + col_b_w + col_c_w}" y="{y_hdr}" width="{col_d_w}" height="{header_h}" fill="#e8f0fe" stroke="#c8c8c8" stroke-width="1"/>')
    
    # Header letters
    cells_svg.append(f'<text x="{table_x + col_a_w/2}" y="{y_hdr + 14}" font-size="10" fill="#555555" text-anchor="middle">A</text>')
    cells_svg.append(f'<text x="{table_x + col_a_w + col_b_w/2}" y="{y_hdr + 14}" font-size="10" fill="#555555" text-anchor="middle">B</text>')
    cells_svg.append(f'<text x="{table_x + col_a_w + col_b_w + col_c_w/2}" y="{y_hdr + 14}" font-size="10" fill="#555555" text-anchor="middle">C</text>')
    cells_svg.append(f'<text x="{table_x + col_a_w + col_b_w + col_c_w + col_d_w/2}" y="{y_hdr + 14}" font-size="10" font-weight="bold" fill="#1a73e8" text-anchor="middle">D</text>')
    
    x_cur = table_x + col_a_w + col_b_w + col_c_w + col_d_w
    for day_col in DAY_COLS:
        cells_svg.append(f'<rect x="{x_cur}" y="{y_hdr}" width="{day_w}" height="{header_h}" fill="#f8f9fa" stroke="#c8c8c8" stroke-width="1"/>')
        cells_svg.append(f'<text x="{x_cur + day_w/2}" y="{y_hdr + 14}" font-size="9" fill="#555555" text-anchor="middle">{day_col}</text>')
        x_cur += day_w
        
    # Table Header (Row 1)
    y_row1 = y_hdr + header_h
    cells_svg.append(f'<rect x="0" y="{y_row1}" width="{table_x}" height="{row_height}" fill="#f8f9fa" stroke="#c8c8c8" stroke-width="1"/>')
    cells_svg.append(f'<text x="{table_x/2}" y="{y_row1 + 14}" font-size="9.5" fill="#555555" text-anchor="middle">1</text>')
    
    cells_svg.append(f'<rect x="{table_x}" y="{y_row1}" width="{col_a_w}" height="{row_height}" fill="#ffffff" stroke="#e0e0e0" stroke-width="1"/>')
    cells_svg.append(f'<text x="{table_x + 5}" y="{y_row1 + 14}" font-size="11" fill="#111111">SL</text>')
    
    cells_svg.append(f'<rect x="{table_x + col_a_w}" y="{y_row1}" width="{col_b_w}" height="{row_height}" fill="#ffffff" stroke="#e0e0e0" stroke-width="1"/>')
    cells_svg.append(f'<text x="{table_x + col_a_w + 5}" y="{y_row1 + 14}" font-size="11" fill="#111111">Activity Name</text>')
    
    cells_svg.append(f'<rect x="{table_x + col_a_w + col_b_w}" y="{y_row1}" width="{col_c_w}" height="{row_height}" fill="#ffffff" stroke="#e0e0e0" stroke-width="1"/>')
    cells_svg.append(f'<text x="{table_x + col_a_w + col_b_w + 5}" y="{y_row1 + 14}" font-size="11" fill="#111111">Duration (Days)</text>')
    
    cells_svg.append(f'<rect x="{table_x + col_a_w + col_b_w + col_c_w}" y="{y_row1}" width="{col_d_w}" height="{row_height}" fill="#ffffff" stroke="#e0e0e0" stroke-width="1"/>')
    cells_svg.append(f'<text x="{table_x + col_a_w + col_b_w + col_c_w + 5}" y="{y_row1 + 14}" font-size="11" fill="#111111">Dependency</text>')
    
    # Grid lines for empty day cells in Row 1
    x_day = table_x + col_a_w + col_b_w + col_c_w + col_d_w
    for _ in DAY_COLS:
        cells_svg.append(f'<rect x="{x_day}" y="{y_row1}" width="{day_w}" height="{row_height}" fill="#ffffff" stroke="#e0e0e0" stroke-width="1"/>')
        x_day += day_w

    # Activity Rows (Rows 2 to 18)
    for idx, (sl, name, dur, dep, active_days) in enumerate(ACTIVITIES, start=2):
        y_r = y_row1 + (idx - 1) * row_height
        # Row number
        cells_svg.append(f'<rect x="0" y="{y_r}" width="{table_x}" height="{row_height}" fill="#f8f9fa" stroke="#c8c8c8" stroke-width="1"/>')
        cells_svg.append(f'<text x="{table_x/2}" y="{y_r + 14}" font-size="9.5" fill="#555555" text-anchor="middle">{idx}</text>')
        
        # Col A: SL
        cells_svg.append(f'<rect x="{table_x}" y="{y_r}" width="{col_a_w}" height="{row_height}" fill="#ffffff" stroke="#e0e0e0" stroke-width="1"/>')
        cells_svg.append(f'<text x="{table_x + 5}" y="{y_r + 14}" font-size="11" fill="#111111">{sl}</text>')
        
        # Col B: Name
        cells_svg.append(f'<rect x="{table_x + col_a_w}" y="{y_r}" width="{col_b_w}" height="{row_height}" fill="#ffffff" stroke="#e0e0e0" stroke-width="1"/>')
        cells_svg.append(f'<text x="{table_x + col_a_w + 5}" y="{y_r + 14}" font-size="11" fill="#111111">{name}</text>')
        
        # Col C: Duration
        cells_svg.append(f'<rect x="{table_x + col_a_w + col_b_w}" y="{y_r}" width="{col_c_w}" height="{row_height}" fill="#ffffff" stroke="#e0e0e0" stroke-width="1"/>')
        cells_svg.append(f'<text x="{table_x + col_a_w + col_b_w + 5}" y="{y_r + 14}" font-size="11" fill="#111111">{dur}</text>')
        
        # Col D: Dependency
        cells_svg.append(f'<rect x="{table_x + col_a_w + col_b_w + col_c_w}" y="{y_r}" width="{col_d_w}" height="{row_height}" fill="#ffffff" stroke="#e0e0e0" stroke-width="1"/>')
        cells_svg.append(f'<text x="{table_x + col_a_w + col_b_w + col_c_w + 5}" y="{y_r + 14}" font-size="11" fill="#111111">{dep}</text>')
        
        # Day columns with Red Bars
        x_d = table_x + col_a_w + col_b_w + col_c_w + col_d_w
        for day_i in range(len(DAY_COLS)):
            fill_color = "#cc0000" if day_i in active_days else "#ffffff"
            stroke_color = "#ba0000" if day_i in active_days else "#e0e0e0"
            cells_svg.append(f'<rect x="{x_d}" y="{y_r}" width="{day_w}" height="{row_height}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="1"/>')
            x_d += day_w

    content = "\n  ".join(cells_svg)
    return f"""<svg viewBox="0 0 {svg_w} {total_height}" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:Arial, Roboto, Helvetica, sans-serif;">
  {content}
</svg>"""

if __name__ == "__main__":
    render_gantt_png()
