"""
Compile Requirements Elicitation, Requirements Analysis (RAD), and SRS
into a unified, interactive, print-ready HTML viewer portal with Mermaid.js rendering.
Student: Farzana Sadia Takee (ID: 2211175)
Project: Elderly Care Management System
"""

import os
import re

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    with open(os.path.join(base_dir, "Requirements_Elicitation_Document.md"), "r", encoding="utf-8") as f:
        elicitation_md = f.read()

    with open(os.path.join(base_dir, "Requirements_Analysis_Document.md"), "r", encoding="utf-8") as f:
        rad_md = f.read()

    with open(os.path.join(base_dir, "Software_Requirements_Specification_SRS.md"), "r", encoding="utf-8") as f:
        srs_md = f.read()

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Elderly Care Management System - Requirements Engineering Documentation</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>

<style>
  :root {{
    --primary: #0D9488;
    --primary-dark: #0F766E;
    --primary-light: #CCFBF1;
    --accent: #E11D48;
    --slate-900: #0F172A;
    --slate-800: #1E293B;
    --slate-700: #334155;
    --slate-600: #475569;
    --slate-500: #64748B;
    --slate-200: #E2E8F0;
    --slate-100: #F1F5F9;
    --slate-50: #F8FAFC;
    --emerald-600: #059669;
    --amber-500: #D97706;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #F1F5F9;
    color: var(--slate-800);
    line-height: 1.6;
  }}

  /* Top Navigation Bar */
  .portal-header {{
    background: #0F172A;
    color: white;
    padding: 12px 28px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }}

  .header-brand {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}

  .brand-badge {{
    width: 38px;
    height: 38px;
    background: linear-gradient(135deg, #0D9488, #059669);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    box-shadow: 0 2px 8px rgba(13, 148, 136, 0.4);
  }}

  .header-brand h1 {{
    font-size: 16px;
    font-weight: 800;
    letter-spacing: -0.3px;
    color: #F8FAFC;
  }}

  .header-brand p {{
    font-size: 11px;
    color: #94A3B8;
  }}

  /* Document Tabs */
  .doc-tabs {{
    display: flex;
    background: #1E293B;
    padding: 4px;
    border-radius: 10px;
    gap: 4px;
    border: 1px solid #334155;
  }}

  .tab-btn {{
    background: transparent;
    border: none;
    color: #94A3B8;
    padding: 8px 16px;
    border-radius: 6px;
    font-size: 12.5px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: inherit;
  }}

  .tab-btn:hover {{
    color: white;
    background: rgba(255,255,255,0.06);
  }}

  .tab-btn.active {{
    background: #0D9488;
    color: white;
    box-shadow: 0 2px 6px rgba(13, 148, 136, 0.3);
  }}

  .action-btns {{
    display: flex;
    gap: 8px;
    align-items: center;
  }}

  .btn-print {{
    background: #334155;
    color: #F8FAFC;
    border: 1px solid #475569;
    padding: 7px 14px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: inherit;
  }}

  .btn-print:hover {{
    background: #475569;
  }}

  /* Content Container */
  .portal-container {{
    max-width: 1080px;
    margin: 28px auto 60px;
    background: white;
    padding: 48px 56px;
    border-radius: 14px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    border: 1px solid #E2E8F0;
  }}

  /* Markdown Typography & Styling */
  .doc-content h1 {{
    font-size: 26px;
    font-weight: 800;
    color: var(--slate-900);
    border-bottom: 2px solid #E2E8F0;
    padding-bottom: 10px;
    margin-top: 32px;
    margin-bottom: 16px;
  }}

  .doc-content h1:first-child {{
    margin-top: 0;
  }}

  .doc-content h2 {{
    font-size: 21px;
    font-weight: 700;
    color: #0F766E;
    margin-top: 30px;
    margin-bottom: 12px;
    border-bottom: 1px solid #E2E8F0;
    padding-bottom: 6px;
  }}

  .doc-content h3 {{
    font-size: 17px;
    font-weight: 700;
    color: var(--slate-800);
    margin-top: 22px;
    margin-bottom: 8px;
  }}

  .doc-content h4 {{
    font-size: 15px;
    font-weight: 700;
    color: var(--slate-700);
    margin-top: 16px;
    margin-bottom: 6px;
  }}

  .doc-content p {{
    margin-bottom: 14px;
    color: #334155;
    font-size: 14.5px;
    line-height: 1.68;
  }}

  .doc-content ul, .doc-content ol {{
    margin-left: 24px;
    margin-bottom: 16px;
    font-size: 14.5px;
    color: #334155;
  }}

  .doc-content li {{
    margin-bottom: 6px;
  }}

  .doc-content table {{
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0 24px;
    font-size: 13.5px;
  }}

  .doc-content th {{
    background: #F1F5F9;
    color: var(--slate-900);
    font-weight: 700;
    text-align: left;
    padding: 10px 12px;
    border: 1px solid #CBD5E1;
  }}

  .doc-content td {{
    padding: 9px 12px;
    border: 1px solid #CBD5E1;
    color: var(--slate-700);
  }}

  .doc-content tr:nth-child(even) td {{
    background: #F8FAFC;
  }}

  .doc-content blockquote {{
    border-left: 4px solid #0D9488;
    background: #F0FDFA;
    padding: 10px 16px;
    margin: 16px 0;
    border-radius: 0 8px 8px 0;
    font-style: italic;
    color: #0F766E;
  }}

  .doc-content code {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 12.5px;
    background: #F1F5F9;
    padding: 2px 6px;
    border-radius: 4px;
    color: #0F766E;
  }}

  .doc-content pre {{
    background: #0F172A;
    color: #F8FAFC;
    padding: 16px;
    border-radius: 8px;
    overflow-x: auto;
    margin: 16px 0;
  }}

  .doc-content pre code {{
    background: transparent;
    color: #38BDF8;
    padding: 0;
  }}

  .mermaid {{
    margin: 24px 0;
    padding: 20px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    overflow-x: auto;
  }}

  /* Print Styles */
  @media print {{
    .portal-header {{
      display: none;
    }}
    body {{
      background: white;
    }}
    .portal-container {{
      max-width: 100%;
      margin: 0;
      padding: 0;
      border: none;
      box-shadow: none;
    }}
    .doc-content {{
      page-break-after: always;
    }}
  }}
</style>
</head>
<body>

<header class="portal-header">
  <div class="header-brand">
    <div class="brand-badge">🩺</div>
    <div>
      <h1>Elderly Care Management System</h1>
      <p>Farzana Sadia Takee (ID: 2211175) &bull; Requirements Engineering Assignment</p>
    </div>
  </div>

  <nav class="doc-tabs">
    <button class="tab-btn active" onclick="switchDoc('doc-elicitation', this)">
      <span>📑</span> 1. Requirements Elicitation
    </button>
    <button class="tab-btn" onclick="switchDoc('doc-rad', this)">
      <span>📐</span> 2. Requirements Analysis (RAD)
    </button>
    <button class="tab-btn" onclick="switchDoc('doc-srs', this)">
      <span>📜</span> 3. Software Requirements Spec (SRS)
    </button>
  </nav>

  <div class="action-btns">
    <button class="btn-print" onclick="window.print()">
      <span>🖨️</span> Print / Save PDF
    </button>
  </div>
</header>

<main class="portal-container">
  <div id="doc-elicitation" class="doc-content"></div>
  <div id="doc-rad" class="doc-content" style="display:none;"></div>
  <div id="doc-srs" class="doc-content" style="display:none;"></div>
</main>

<script>
  mermaid.initialize({{
    startOnLoad: false,
    theme: 'neutral',
    securityLevel: 'loose'
  }});

  // Embedded Raw Markdown Contents
  const rawDocs = {{
    elicitation: {repr(elicitation_md)},
    rad: {repr(rad_md)},
    srs: {repr(srs_md)}
  }};

  function renderDocument(containerId, rawMd) {{
    const container = document.getElementById(containerId);
    
    // Custom renderer for mermaid blocks
    const renderer = new marked.Renderer();
    const originalCode = renderer.code.bind(renderer);
    
    renderer.code = function(code, language) {{
      if (language === 'mermaid') {{
        return `<div class="mermaid">${{code}}</div>`;
      }}
      return originalCode(code, language);
    }};

    marked.setOptions({{ renderer: renderer }});
    container.innerHTML = marked.parse(rawMd);
  }}

  // Initial Render
  renderDocument('doc-elicitation', rawDocs.elicitation);
  renderDocument('doc-rad', rawDocs.rad);
  renderDocument('doc-srs', rawDocs.srs);

  mermaid.run();

  function switchDoc(targetId, btnElement) {{
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    btnElement.classList.add('active');

    document.querySelectorAll('.doc-content').forEach(doc => doc.style.display = 'none');
    const target = document.getElementById(targetId);
    target.style.display = 'block';

    // Rerun mermaid if needed for the revealed container
    setTimeout(() => {{
      mermaid.run();
    }}, 50);
  }}
</script>

</body>
</html>
"""

    output_path = os.path.join(base_dir, "requirements_specification_portal.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print("Generated requirements_specification_portal.html successfully!")

if __name__ == "__main__":
    main()
