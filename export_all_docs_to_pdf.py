"""
Generate standalone styled HTML files and publication-grade PDF documents
for:
1. Requirements Elicitation Document
2. Requirements Analysis Document (RAD)
Features exact IUB Cover Page on Page 1 (with official IUB Logo, centered titles,
student metadata, course info, semester, instructor, institution)
and strict Black & White academic styling for all text.
"""

import os
import subprocess
import base64

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""

def strip_header_metadata(md_content):
    parts = md_content.split('---')
    if len(parts) >= 3:
        # parts[0] is title, parts[1] is metadata table/block, parts[2:] is main body
        return '---'.join(parts[2:]).strip()
    return md_content

def create_standalone_html(title, doc_name, md_content, output_html_path):
    logo_base64 = get_base64_image("iub_logo.png")
    body_md = strip_header_metadata(md_content)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>

<style>
  @page {{
    size: A4 portrait;
    margin: 20mm 18mm 20mm 18mm;
    @bottom-center {{
      content: counter(page);
      font-size: 10pt;
      font-family: Arial, Helvetica, sans-serif;
      color: #000000;
    }}
  }}

  @page :first {{
    @bottom-center {{
      content: none;
    }}
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
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
  }}

  /* Cover Page Styling */
  .cover-page {{
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
  }}

  @media print {{
    .cover-page {{
      height: 9.0in;
      max-height: 9.0in;
      border-bottom: none;
      margin-bottom: 0;
      padding-top: 10px;
      padding-bottom: 15px;
      page-break-after: always;
      break-after: page;
    }}
  }}

  .cover-logo-box {{
    margin-bottom: 20px;
  }}

  .cover-logo {{
    width: 200px;
    max-width: 200px;
    height: auto;
    display: block;
    margin: 0 auto;
  }}

  .cover-title-box {{
    margin-bottom: 32px;
  }}

  .cover-doc-title {{
    font-size: 16pt;
    font-weight: bold;
    color: #000000;
    line-height: 1.35;
  }}

  .cover-project-title {{
    font-size: 18pt;
    font-weight: bold;
    color: #000000;
    line-height: 1.35;
    margin-top: 4px;
  }}

  .cover-prepared-box {{
    margin-bottom: 26px;
    line-height: 1.45;
  }}

  .cover-bold-label {{
    font-size: 13pt;
    font-weight: bold;
    color: #000000;
    margin-bottom: 6px;
  }}

  .cover-bold-text {{
    font-size: 13pt;
    font-weight: bold;
    color: #000000;
    margin-bottom: 14px;
  }}

  .cover-bold-id {{
    font-size: 12.5pt;
    font-weight: bold;
    color: #000000;
  }}

  .cover-course-box {{
    font-size: 12pt;
    line-height: 1.5;
    color: #000000;
    margin-bottom: 26px;
  }}

  .cover-semester-box {{
    font-size: 13pt;
    color: #000000;
    margin-bottom: 26px;
  }}

  .cover-submitted-box {{
    margin-bottom: 10px;
    line-height: 1.45;
  }}

  .cover-light-label {{
    font-size: 11pt;
    color: #000000;
    margin-bottom: 8px;
  }}

  .cover-bold-instructor {{
    font-size: 13.5pt;
    font-weight: bold;
    color: #000000;
    margin-bottom: 18px;
  }}

  .cover-university-text {{
    font-size: 12.5pt;
    color: #000000;
  }}

  .cover-page-break {{
    page-break-after: always;
    break-after: page;
    height: 0;
    margin: 0;
    padding: 0;
  }}

  /* Headings: Strict Black and White with NO BORDER LINES */
  h1 {{
    font-size: 22px;
    font-weight: bold;
    color: #000000;
    border: none;
    padding-bottom: 0;
    margin-top: 24px;
    margin-bottom: 12px;
    page-break-after: avoid;
  }}

  h1:first-of-type {{
    margin-top: 0;
  }}

  h2 {{
    font-size: 16px;
    font-weight: bold;
    color: #000000;
    border: none;
    padding-bottom: 0;
    margin-top: 20px;
    margin-bottom: 10px;
    page-break-after: avoid;
  }}

  h3 {{
    font-size: 14px;
    font-weight: bold;
    color: #000000;
    margin-top: 16px;
    margin-bottom: 6px;
    page-break-after: avoid;
  }}

  h4 {{
    font-size: 13px;
    font-weight: bold;
    color: #000000;
    margin-top: 12px;
    margin-bottom: 4px;
    page-break-after: avoid;
  }}

  p {{
    margin-bottom: 10px;
    color: #000000;
    line-height: 1.55;
  }}

  strong, b {{
    font-weight: bold;
    color: #000000;
  }}

  em, i {{
    font-style: italic;
    color: #000000;
  }}

  ul, ol {{
    margin-left: 22px;
    margin-bottom: 12px;
    color: #000000;
  }}

  li {{
    margin-bottom: 4px;
    color: #000000;
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0 18px;
    font-size: 12px;
    page-break-inside: auto;
    border: 1px solid #000000;
  }}

  tr {{
    page-break-inside: avoid;
    page-break-after: auto;
  }}

  th {{
    background: #f0f0f0;
    color: #000000;
    font-weight: bold;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #000000;
  }}

  td {{
    padding: 6px 8px;
    border: 1px solid #b0b0b0;
    color: #000000;
  }}

  tr:nth-child(even) td {{
    background: #f9f9f9;
  }}

  blockquote {{
    border: none;
    background: #f7f7f7;
    padding: 6px 12px;
    margin: 12px 0;
    font-style: italic;
    color: #000000;
  }}

  code {{
    font-family: 'Courier New', Courier, monospace;
    font-size: 11.5px;
    background: #f2f2f2;
    padding: 1px 4px;
    border: 1px solid #d0d0d0;
    color: #000000;
  }}

  pre {{
    background: #f8f8f8;
    color: #000000;
    padding: 10px;
    border: 1px solid #b0b0b0;
    border-radius: 2px;
    overflow-x: auto;
    margin: 12px 0;
  }}

  pre code {{
    background: transparent;
    color: #000000;
    border: none;
    padding: 0;
  }}

  .mermaid {{
    margin: 18px 0;
    padding: 12px;
    background: #ffffff;
    border: 1px solid #000000;
    display: flex;
    justify-content: center;
    page-break-inside: avoid;
  }}

  .mermaid svg {{
    max-width: 100%;
    height: auto;
  }}

  .mermaid svg text {{
    fill: #000000 !important;
    font-family: Arial, Helvetica, sans-serif !important;
  }}

  .mermaid svg rect, 
  .mermaid svg circle, 
  .mermaid svg polygon, 
  .mermaid svg path {{
    stroke: #000000 !important;
  }}

  hr {{
    display: none !important;
    border: none !important;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
  }}

  @media print {{
    body {{
      padding: 0;
      max-width: 100%;
    }}
  }}
</style>
</head>
<body>

<!-- PAGE 1: IUB OFFICIAL FRONT COVER PAGE -->
<div class="cover-page">
  <div class="cover-logo-box">
    <img src="{logo_base64}" class="cover-logo" alt="Independent University Bangladesh" />
  </div>

  <div class="cover-title-box">
    <div class="cover-doc-title">{doc_name} for</div>
    <div class="cover-project-title">Elderly Care Management System</div>
  </div>

  <div class="cover-prepared-box">
    <div class="cover-bold-label">Prepared By</div>
    <div class="cover-bold-text">Farzana Sadia Takee</div>
    <div class="cover-bold-id">ID- 2211175</div>
  </div>

  <div class="cover-course-box">
    <div>Course Code: CSE309</div>
    <div>Course Title: <strong>Web Programming</strong></div>
    <div>Section: 02</div>
  </div>

  <div class="cover-semester-box">
    <strong>Autumn 2025</strong>
  </div>

  <div class="cover-submitted-box">
    <div class="cover-light-label">Submitted to</div>
    <div class="cover-bold-instructor">Md Abu Sayed</div>
    <div class="cover-university-text">Independent University Bangladesh</div>
  </div>
</div>

<!-- PAGE 2+: DOCUMENT CONTENT -->
<div id="content"></div>

<script>
  mermaid.initialize({{
    startOnLoad: false,
    theme: 'neutral',
    securityLevel: 'loose'
  }});

  const rawMd = {repr(body_md)};

  const renderer = new marked.Renderer();
  const originalCode = renderer.code.bind(renderer);

  renderer.code = function(code, language) {{
    if (language === 'mermaid') {{
      return `<div class="mermaid">${{code}}</div>`;
    }}
    return originalCode(code, language);
  }};

  marked.setOptions({{ renderer: renderer }});
  document.getElementById('content').innerHTML = marked.parse(rawMd);

  mermaid.run();
</script>

</body>
</html>
"""
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Created HTML: {os.path.basename(output_html_path)}")

def html_to_pdf(html_path, pdf_path):
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
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if os.path.exists(pdf_path):
            size = os.path.getsize(pdf_path)
            print(f"Created PDF: {os.path.basename(pdf_path)} ({size:,} bytes)")
        else:
            print(f"Failed to generate {os.path.basename(pdf_path)}: {res.stderr}")
    except Exception as e:
        print(f"Error compiling {pdf_path}: {e}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    docs = [
        (
            "Requirements Elicitation Document - Elderly Care Management System",
            "Requirements Elicitation Document",
            os.path.join(base_dir, "Requirements_Elicitation_Document.md"),
            os.path.join(base_dir, "Requirements_Elicitation_Document.html"),
            os.path.join(base_dir, "Requirements_Elicitation_Document.pdf")
        ),
        (
            "Requirements Analysis Document (RAD) - Elderly Care Management System",
            "Requirements Analysis Document (RAD)",
            os.path.join(base_dir, "Requirements_Analysis_Document.md"),
            os.path.join(base_dir, "Requirements_Analysis_Document.html"),
            os.path.join(base_dir, "Requirements_Analysis_Document.pdf")
        )
    ]

    for title, doc_name, md_p, html_p, pdf_p in docs:
        with open(md_p, "r", encoding="utf-8") as f:
            md_content = f.read()
        create_standalone_html(title, doc_name, md_content, html_p)
        html_to_pdf(html_p, pdf_p)

if __name__ == "__main__":
    main()
