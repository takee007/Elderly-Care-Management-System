"""
Generate High-Fidelity UI/UX Specification PDF for Elderly Care Management System
Student: Farzana Sadia Takee (ID: 2211175)
Figma / Canva grade Design Presentation
"""
import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Elderly Care Management System - High Fidelity Design</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

  @page {
    size: A4 landscape;
    margin: 0;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  :root {
    --primary: #0D9488;
    --primary-dark: #0F766E;
    --primary-light: #CCFBF1;
    --slate-900: #0F172A;
    --slate-800: #1E293B;
    --slate-700: #334155;
    --slate-600: #475569;
    --slate-400: #94A3B8;
    --slate-200: #E2E8F0;
    --slate-100: #F1F5F9;
    --slate-50: #F8FAFC;
    --emerald-600: #059669;
    --emerald-100: #D1FAE5;
    --amber-500: #F59E0B;
    --amber-100: #FEF3C7;
    --rose-600: #E11D48;
    --rose-500: #F43F5E;
    --rose-100: #FFE4E6;
    --blue-600: #2563EB;
    --blue-100: #DBEAFE;
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08), 0 2px 4px -2px rgba(0,0,0,0.06);
    --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.09), 0 4px 6px -4px rgba(0,0,0,0.05);
  }

  body {
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif;
    color: var(--slate-800);
    background: #E2E8F0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .page {
    width: 297mm;
    height: 210mm;
    page-break-after: always;
    position: relative;
    padding: 10mm 14mm;
    background: #F8FAFC;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }

  /* Presentation Header */
  .page-nav-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid var(--slate-200);
    padding-bottom: 6px;
    margin-bottom: 8px;
  }

  .brand-badge {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .brand-logo-icon {
    width: 26px;
    height: 26px;
    background: linear-gradient(135deg, #0D9488, #059669);
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 800;
    font-size: 14px;
    box-shadow: 0 2px 4px rgba(13, 148, 136, 0.3);
  }

  .page-title-group h1 {
    font-size: 18px;
    font-weight: 800;
    color: var(--slate-900);
    letter-spacing: -0.3px;
  }

  .page-title-group p {
    font-size: 11px;
    color: var(--slate-600);
    margin-top: 1px;
  }

  .meta-pills {
    display: flex;
    gap: 6px;
    align-items: center;
  }

  .pill {
    font-size: 10.5px;
    font-weight: 600;
    padding: 3px 9px;
    border-radius: 20px;
    background: var(--slate-100);
    color: var(--slate-700);
    border: 1px solid var(--slate-200);
  }

  .pill.highlight {
    background: var(--primary-light);
    color: var(--primary-dark);
    border-color: #99F6E4;
  }

  /* Main Workspace */
  .screen-layout {
    flex: 1;
    display: grid;
    grid-template-columns: 1fr 280px;
    gap: 14px;
    height: calc(100% - 46px);
  }

  /* Mockup Frame */
  .mockup-frame {
    background: #FFFFFF;
    border-radius: 12px;
    border: 1px solid #CBD5E1;
    box-shadow: var(--shadow-lg);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .mockup-chrome {
    height: 32px;
    background: #F1F5F9;
    border-bottom: 1px solid #CBD5E1;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 12px;
    font-size: 11px;
    color: var(--slate-600);
    font-weight: 600;
  }

  .window-dots {
    display: flex;
    gap: 5px;
  }

  .dot-red { width: 8px; height: 8px; border-radius: 50%; background: #EF4444; }
  .dot-yellow { width: 8px; height: 8px; border-radius: 50%; background: #F59E0B; }
  .dot-green { width: 8px; height: 8px; border-radius: 50%; background: #10B981; }

  .mockup-url {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    padding: 2px 16px;
    border-radius: 12px;
    font-size: 10px;
    color: var(--slate-400);
    width: 280px;
    text-align: center;
  }

  /* App Shell */
  .app-shell {
    flex: 1;
    display: flex;
    background: #F8FAFC;
    overflow: hidden;
  }

  /* Sidebar */
  .app-sidebar {
    width: 155px;
    background: #0F172A;
    color: #F8FAFC;
    padding: 10px 8px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .nav-header {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 4px 6px 12px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 8px;
  }

  .nav-logo-box {
    width: 22px;
    height: 22px;
    background: #0D9488;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 12px;
    color: white;
  }

  .nav-menu {
    display: flex;
    flex-direction: column;
    gap: 3px;
  }

  .nav-link {
    display: flex;
    align-items: center;
    gap: 7px;
    padding: 6px 8px;
    border-radius: 6px;
    font-size: 11px;
    color: #94A3B8;
    font-weight: 500;
  }

  .nav-link.active {
    background: #0D9488;
    color: #FFFFFF;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(13, 148, 136, 0.4);
  }

  .app-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: #F8FAFC;
  }

  .app-topbar {
    height: 42px;
    background: #FFFFFF;
    border-bottom: 1px solid var(--slate-200);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
  }

  .app-content {
    flex: 1;
    padding: 12px 14px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    overflow: hidden;
  }

  /* Figma Specs Sidebar */
  .specs-sidebar {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .spec-card {
    background: #FFFFFF;
    border-radius: 8px;
    border: 1px solid var(--slate-200);
    padding: 10px 12px;
    box-shadow: var(--shadow-sm);
  }

  .spec-card h3 {
    font-size: 12px;
    font-weight: 700;
    color: var(--slate-900);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .spec-card p, .spec-card li {
    font-size: 11px;
    color: var(--slate-600);
    line-height: 1.45;
  }

  .spec-card ul {
    list-style: none;
    padding: 0;
  }

  .spec-card li {
    margin-bottom: 5px;
    position: relative;
    padding-left: 12px;
  }

  .spec-card li::before {
    content: "•";
    position: absolute;
    left: 0;
    color: var(--primary);
    font-weight: bold;
  }

  .token-tag {
    display: inline-block;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 9.5px;
    font-weight: 600;
    margin: 2px;
    background: var(--slate-100);
    border: 1px solid var(--slate-200);
    color: var(--slate-700);
  }

  /* High-Fi Components */
  .btn-hf {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 11.5px;
    font-weight: 600;
    border: none;
    cursor: pointer;
  }

  .btn-primary {
    background: linear-gradient(135deg, #0D9488, #0F766E);
    color: #FFFFFF;
    box-shadow: 0 2px 4px rgba(13, 148, 136, 0.25);
  }

  .btn-danger {
    background: linear-gradient(135deg, #E11D48, #BE123C);
    color: #FFFFFF;
    box-shadow: 0 2px 4px rgba(225, 29, 72, 0.3);
  }

  .btn-secondary {
    background: #FFFFFF;
    color: var(--slate-700);
    border: 1px solid var(--slate-200);
  }

  .badge-hf {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 3px 8px;
    border-radius: 12px;
    font-size: 10px;
    font-weight: 600;
  }

  .badge-green { background: #D1FAE5; color: #065F46; }
  .badge-amber { background: #FEF3C7; color: #92400E; }
  .badge-red { background: #FFE4E6; color: #9F1239; }
  .badge-blue { background: #DBEAFE; color: #1E40AF; }

  .stat-card-hf {
    background: #FFFFFF;
    border: 1px solid var(--slate-200);
    border-radius: 8px;
    padding: 8px 12px;
    box-shadow: var(--shadow-sm);
  }

  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; }
  .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }

  .card-hf {
    background: #FFFFFF;
    border: 1px solid var(--slate-200);
    border-radius: 8px;
    padding: 10px 12px;
    box-shadow: var(--shadow-sm);
  }

  .card-header-hf {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    border-bottom: 1px solid var(--slate-100);
    padding-bottom: 6px;
  }

  .card-header-hf h4 {
    font-size: 12px;
    font-weight: 700;
    color: var(--slate-800);
  }

  /* Cover Page Styling */
  .cover-container {
    flex: 1;
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 60%, #0D9488 100%);
    border-radius: 16px;
    padding: 35px 45px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-lg);
  }

  .cover-top-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(13, 148, 136, 0.3);
    border: 1px solid #14B8A6;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    color: #5EEAD4;
    letter-spacing: 0.5px;
    width: fit-content;
  }

  .cover-hero h1 {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1.1;
    margin-top: 10px;
  }

  .cover-hero p {
    font-size: 18px;
    color: #94A3B8;
    margin-top: 6px;
    max-width: 650px;
    font-weight: 400;
  }

  .cover-cards-row {
    display: grid;
    grid-template-columns: 1.2fr 1.8fr;
    gap: 20px;
    margin: 15px 0;
  }

  .cover-info-card {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 12px;
    padding: 16px 20px;
  }

  .cover-info-card h3 {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #5EEAD4;
    margin-bottom: 8px;
    font-weight: 700;
  }

  .cover-info-card p {
    font-size: 13.5px;
    color: #E2E8F0;
    line-height: 1.5;
  }

  .cover-index-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    font-size: 11px;
  }

  .cover-index-item {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 6px;
    padding: 6px 10px;
    display: flex;
    align-items: center;
    gap: 8px;
    color: #CBD5E1;
  }

  .cover-index-num {
    background: #0D9488;
    color: white;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 10px;
  }
</style>
</head>
<body>

<!-- PAGE 0: COVER & TITLE -->
<div class="page">
  <div class="cover-container">
    <div>
      <div class="cover-hero">
        <h1>Elderly Care Management System</h1>
        <p>Comprehensive High-Fidelity UI/UX Prototype, Design System Tokens, and Interface Architecture for Geriatric Home Healthcare</p>
      </div>
    </div>

    <div class="cover-cards-row">
      <div class="cover-info-card">
        <h3>Academic Submission Profile</h3>
        <p><strong>Student Name:</strong> Farzana Sadia Takee</p>
        <p><strong>Student ID:</strong> 2211175</p>
        <p><strong>Project Title:</strong> Elderly Care Management System</p>
        <p><strong>Design Tooling:</strong> Figma / Canva Vector Grade Architecture</p>
        <p><strong>Date:</strong> October 2026</p>
      </div>

      <div class="cover-info-card">
        <h3>Design System Objectives</h3>
        <p>• <strong>Senior-Centric Readability:</strong> WCAG AAA contrast, minimum 14pt body text, and prominent visual cues.</p>
        <p>• <strong>Zero-Error Medication Safety:</strong> Color-coded dosage status with time stamps and audio-visual cues.</p>
        <p>• <strong>Caregiver Accountability:</strong> Structured daily handoff logs, vitals verification, and instant emergency dispatch.</p>
      </div>
    </div>

    <div>
      <h3 style="font-size:11px; text-transform:uppercase; letter-spacing:1px; color:#94A3B8; margin-bottom:6px;">
        Sequenced Interface Specification (1 Screen Per Page)
      </h3>
      <div class="cover-index-grid">
        <div class="cover-index-item"><span class="cover-index-num">1</span> Design System Tokens & Style Guide</div>
        <div class="cover-index-item"><span class="cover-index-num">2</span> Screen Flow & Information Architecture</div>
        <div class="cover-index-item"><span class="cover-index-num">3</span> Screen 1: Role-Based Authentication</div>
        <div class="cover-index-item"><span class="cover-index-num">4</span> Screen 2: Central Family Dashboard</div>
        <div class="cover-index-item"><span class="cover-index-num">5</span> Screen 3: Elderly Profile & Health Record</div>
        <div class="cover-index-item"><span class="cover-index-num">6</span> Screen 4: Medicine Schedule & Tracker</div>
        <div class="cover-index-item"><span class="cover-index-num">7</span> Screen 5: Add Medication Form Modal</div>
        <div class="cover-index-item"><span class="cover-index-num">8</span> Screen 6: Doctor Appointment Tracking</div>
        <div class="cover-index-item"><span class="cover-index-num">9</span> Screen 7: Daily Care Routine Checklist</div>
        <div class="cover-index-item"><span class="cover-index-num">10</span> Screen 8: Caregiver Shift Handoff Log</div>
        <div class="cover-index-item"><span class="cover-index-num">11</span> Screen 9: Instant Emergency SOS Portal</div>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 1: DESIGN SYSTEM & STYLE GUIDE -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon">EC</div>
      <div class="page-title-group">
        <h1>01. Design System & Design Tokens</h1>
        <p>Color Palette, Typography Scale, UI Components, and Accessibility Standards</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Design System v2.0</span>
      <span class="pill">Figma Tokens</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame" style="padding:16px; display:flex; flex-direction:column; gap:12px;">
      <!-- Color Palette Row -->
      <div>
        <h4 style="font-size:12px; font-weight:700; color:var(--slate-800); margin-bottom:6px;">Core Medical Color Tokens</h4>
        <div class="grid-4" style="gap:8px;">
          <div style="background:#0D9488; color:white; padding:10px; border-radius:6px;">
            <div style="font-size:11px; font-weight:700;">Teal Primary</div>
            <div style="font-size:10px; opacity:0.9;">#0D9488 • Brand & CTAs</div>
          </div>
          <div style="background:#0F172A; color:white; padding:10px; border-radius:6px;">
            <div style="font-size:11px; font-weight:700;">Deep Slate</div>
            <div style="font-size:10px; opacity:0.9;">#0F172A • High Contrast Text</div>
          </div>
          <div style="background:#F59E0B; color:white; padding:10px; border-radius:6px;">
            <div style="font-size:11px; font-weight:700;">Amber Alert</div>
            <div style="font-size:10px; opacity:0.9;">#F59E0B • Med Reminders</div>
          </div>
          <div style="background:#E11D48; color:white; padding:10px; border-radius:6px;">
            <div style="font-size:11px; font-weight:700;">Emergency Red</div>
            <div style="font-size:10px; opacity:0.9;">#E11D48 • SOS & Paramedics</div>
          </div>
        </div>
      </div>

      <!-- Typography & Components -->
      <div class="grid-2">
        <div class="card-hf">
          <div class="card-header-hf"><h4>Typography Hierarchy</h4></div>
          <div style="display:flex; flex-direction:column; gap:6px; font-size:11px;">
            <div><span style="font-size:16px; font-weight:800;">Heading 1 (24px)</span> — Section Titles</div>
            <div><span style="font-size:14px; font-weight:700;">Heading 2 (18px)</span> — Card Headers</div>
            <div><span style="font-size:12px; font-weight:600;">Subheading (14px)</span> — Data Labels</div>
            <div><span style="font-size:11px; font-weight:400; color:var(--slate-600);">Body Regular (13px) — High legibility medical text</span></div>
          </div>
        </div>

        <div class="card-hf">
          <div class="card-header-hf"><h4>Interactive Badges & Buttons</h4></div>
          <div style="display:flex; flex-wrap:wrap; gap:6px; align-items:center;">
            <span class="badge-hf badge-green">✓ Dose Completed</span>
            <span class="badge-hf badge-amber">⏳ Due in 25m</span>
            <span class="badge-hf badge-red">🚨 Critical SOS</span>
            <span class="badge-hf badge-blue">🩺 Doctor Visit</span>
            <div style="width:100%; height:1px; background:#E2E8F0; margin:4px 0;"></div>
            <button class="btn-hf btn-primary">Primary Action</button>
            <button class="btn-hf btn-secondary">Secondary Option</button>
            <button class="btn-hf btn-danger">Emergency Dial</button>
          </div>
        </div>
      </div>

      <!-- Accessibility Guidelines Box -->
      <div class="card-hf" style="background:#F0FDFA; border-color:#99F6E4;">
        <h4 style="font-size:12px; font-weight:700; color:#0F766E; margin-bottom:4px;">Geriatric & Elderly-Friendly UX Guidelines</h4>
        <div class="grid-3" style="font-size:11px; color:#115E59;">
          <div>• <strong>Touch Targets:</strong> Buttons and clickable tiles minimum 44px height.</div>
          <div>• <strong>WCAG AAA Contrast:</strong> Minimum 7:1 contrast ratio on all key text.</div>
          <div>• <strong>Dual Encoding:</strong> Information conveyed using both text + color icons.</div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Design Philosophy</h3>
        <p>A human-centered system designed specifically to bridge the communication gap between busy family members, non-technical elderly users, and home healthcare aides.</p>
      </div>

      <div class="spec-card">
        <h3>Design Tokens</h3>
        <span class="token-tag">#0D9488 Brand</span>
        <span class="token-tag">#0F172A Base</span>
        <span class="token-tag">#F8FAFC Canvas</span>
        <span class="token-tag">#E11D48 Urgent</span>
        <span class="token-tag">Inter / Plus Jakarta</span>
        <span class="token-tag">8px Radius Grid</span>
      </div>

      <div class="spec-card">
        <h3>Key Standards</h3>
        <ul>
          <li>Card-based modular layouts.</li>
          <li>Real-time timestamp verification.</li>
          <li>Optimized for desktop, laptop & tablet screens.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 2: ARCHITECTURE & SITEMAP FLOW -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon">EC</div>
      <div class="page-title-group">
        <h1>02. Screen Flow & Information Architecture</h1>
        <p>End-to-End User Journey from Authentication to Daily Operations and Emergency Protocol</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Architecture</span>
      <span class="pill">User Journey</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame" style="padding:16px; background:#F8FAFC;">
      <div style="display:flex; flex-direction:column; gap:14px; height:100%;">
        <!-- Flow top -->
        <div style="display:flex; justify-content:center; align-items:center; gap:16px;">
          <div class="card-hf" style="width:200px; text-align:center; background:#F1F5F9; border-style:dashed;">
            <div style="font-size:10px; font-weight:700; color:var(--slate-400);">SYSTEM ENTRY</div>
            <strong style="font-size:12px;">Elderly Care Web App</strong>
          </div>
          <div style="font-size:18px; color:var(--primary); font-weight:bold;">➔</div>
          <div class="card-hf" style="width:220px; text-align:center; border:2px solid var(--primary);">
            <div style="font-size:10px; font-weight:700; color:var(--primary);">SCREEN 1: AUTHENTICATION</div>
            <strong style="font-size:12px;">Role Toggle: Family / Caregiver</strong>
          </div>
        </div>

        <div style="text-align:center; font-size:14px; color:var(--slate-400);">⬇ (Secure Session Handshake)</div>

        <!-- Central Hub -->
        <div style="display:flex; justify-content:center;">
          <div class="card-hf" style="width:340px; text-align:center; background:linear-gradient(135deg, #0F172A, #1E293B); color:white; box-shadow:var(--shadow-md);">
            <div style="font-size:10px; font-weight:700; color:#5EEAD4;">CENTRAL COMMAND HUB</div>
            <strong style="font-size:14px;">Screen 2: Family Member Dashboard</strong>
            <p style="font-size:10px; color:#94A3B8; margin-top:2px;">Patient Status • Next Med Alert • Daily Schedule • SOS Action</p>
          </div>
        </div>

        <div style="text-align:center; font-size:14px; color:var(--slate-400);">⬇ (Core Functional Modules)</div>

        <!-- 4 Branches -->
        <div class="grid-4" style="gap:8px;">
          <div class="card-hf" style="text-align:center;">
            <span style="font-size:16px;">👤</span>
            <div style="font-size:11px; font-weight:700; color:var(--slate-800);">Screen 3: Profile</div>
            <p style="font-size:9.5px; color:var(--slate-600);">Medical History, Vitals & Allergies</p>
          </div>
          <div class="card-hf" style="text-align:center; border-color:#99F6E4;">
            <span style="font-size:16px;">💊</span>
            <div style="font-size:11px; font-weight:700; color:var(--primary-dark);">Screen 4 & 5: Meds</div>
            <p style="font-size:9.5px; color:var(--slate-600);">Schedule, Refill & Add Prescription</p>
          </div>
          <div class="card-hf" style="text-align:center;">
            <span style="font-size:16px;">🩺</span>
            <div style="font-size:11px; font-weight:700; color:var(--slate-800);">Screen 6: Doctors</div>
            <p style="font-size:9.5px; color:var(--slate-600);">Visits, Clinics & Prescription History</p>
          </div>
          <div class="card-hf" style="text-align:center;">
            <span style="font-size:16px;">📋</span>
            <div style="font-size:11px; font-weight:700; color:var(--slate-800);">Screen 7: Routine</div>
            <p style="font-size:9.5px; color:var(--slate-600);">Hydration, Meals, Exercise & BP</p>
          </div>
        </div>

        <!-- Bottom Row -->
        <div style="display:flex; justify-content:center; gap:20px; align-items:center; margin-top:4px;">
          <div class="card-hf" style="width:240px; text-align:center;">
            <span style="font-size:14px;">🤝</span>
            <div style="font-size:11px; font-weight:700;">Screen 8: Caregivers</div>
            <p style="font-size:9.5px; color:var(--slate-600);">Nurse Roster, Shift Timing & Care Notes</p>
          </div>
          <div style="font-size:16px; color:var(--rose-600); font-weight:bold;">⮂</div>
          <div class="card-hf" style="width:240px; text-align:center; background:#FFE4E6; border:1.5px solid #F43F5E;">
            <span style="font-size:14px;">🚨</span>
            <div style="font-size:11px; font-weight:700; color:#9F1239;">Screen 9: EMERGENCY SOS</div>
            <p style="font-size:9.5px; color:#9F1239;">Speed Dial 999, ER Desk & GPS Broadcast</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Architecture Strategy</h3>
        <p>The system utilizes a <strong>Hub-and-Spoke Topology</strong>. The Dashboard functions as the persistent anchor, ensuring non-technical users never get lost in deep sub-pages.</p>
      </div>

      <div class="spec-card">
        <h3>Screen Sequence</h3>
        <ul>
          <li><strong>Step 1:</strong> Role-based entry</li>
          <li><strong>Step 2:</strong> Main state overview</li>
          <li><strong>Step 3-7:</strong> Core healthcare ops</li>
          <li><strong>Step 8:</strong> Care staff coordination</li>
          <li><strong>Step 9:</strong> Instant emergency rescue</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 3: SCREEN 1 - AUTHENTICATION -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon">EC</div>
      <div class="page-title-group">
        <h1>03. Screen 1: Role-Based Authentication Portal</h1>
        <p>Secure login with instantaneous dual-role switching between Family Members and Caregivers</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 1 of 9</span>
      <span class="pill">Auth & Roles</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame">
      <div class="mockup-chrome">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url">https://elderlycare.portal/login</div>
        <span style="font-size:10px; color:var(--primary); font-weight:bold;">SSL 256-bit Encrypted</span>
      </div>
      <div class="app-shell" style="align-items:center; justify-content:center; background:linear-gradient(135deg, #F8FAFC 0%, #EEF2F6 100%);">
        <div class="card-hf" style="width:370px; padding:22px; box-shadow:var(--shadow-lg); border-radius:12px;">
          <div style="text-align:center; margin-bottom:16px;">
            <div style="width:44px; height:44px; background:linear-gradient(135deg, #0D9488, #0F766E); border-radius:10px; margin:0 auto 8px; display:flex; align-items:center; justify-content:center; color:white; font-size:22px; font-weight:bold; box-shadow:0 4px 6px rgba(13,148,136,0.3);">
              🩺
            </div>
            <h2 style="font-size:18px; font-weight:800; color:var(--slate-900);">Elderly Care Portal</h2>
            <p style="font-size:11px; color:var(--slate-600); margin-top:2px;">Dedicated Family & Caregiver Monitoring System</p>
          </div>

          <!-- Role Toggle Buttons -->
          <div style="background:#F1F5F9; padding:3px; border-radius:8px; display:flex; gap:3px; margin-bottom:14px;">
            <button style="flex:1; padding:6px; border:none; border-radius:6px; background:#0D9488; color:white; font-size:11px; font-weight:700; cursor:pointer; box-shadow:0 1px 3px rgba(0,0,0,0.1);">
              👨‍👩‍👧 Family Member
            </button>
            <button style="flex:1; padding:6px; border:none; border-radius:6px; background:transparent; color:var(--slate-600); font-size:11px; font-weight:600; cursor:pointer;">
              👩‍⚕️ Caregiver Staff
            </button>
          </div>

          <!-- Input Fields -->
          <div style="display:flex; flex-direction:column; gap:10px;">
            <div>
              <label style="font-size:10.5px; font-weight:700; color:var(--slate-700); display:block; margin-bottom:3px;">Email Address or Phone Number</label>
              <input type="text" value="tariq.rahman@caremail.com" style="width:100%; padding:8px 10px; border:1px solid #CBD5E1; border-radius:6px; font-size:11.5px; color:var(--slate-800); background:#FFFFFF; outline:none;" readonly>
            </div>
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:3px;">
                <label style="font-size:10.5px; font-weight:700; color:var(--slate-700);">Password</label>
                <span style="font-size:10px; color:var(--primary); font-weight:600; cursor:pointer;">Forgot Password?</span>
              </div>
              <input type="password" value="secretpassword" style="width:100%; padding:8px 10px; border:1px solid #CBD5E1; border-radius:6px; font-size:11.5px; color:var(--slate-800); background:#FFFFFF; outline:none;" readonly>
            </div>

            <div style="display:flex; align-items:center; gap:6px; margin:2px 0;">
              <input type="checkbox" checked style="accent-color:var(--primary);">
              <label style="font-size:10.5px; color:var(--slate-600);">Keep me securely logged in on this tablet</label>
            </div>

            <button class="btn-hf btn-primary" style="padding:9px; font-size:12px; margin-top:4px;">
              Sign In to Care Dashboard ➔
            </button>
          </div>

          <div style="margin-top:14px; padding-top:10px; border-top:1px solid var(--slate-100); text-align:center;">
            <span style="font-size:10px; color:var(--slate-400);">Need immediate emergency dispatch?</span><br>
            <strong style="font-size:11px; color:var(--rose-600);">Call 24/7 Ambulance: 999 / 10616</strong>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Screen Purpose</h3>
        <p>Guarantees safe role-isolated login. Family members access billing and prescriptions, while caregivers access clinical logs and shift reports.</p>
      </div>

      <div class="spec-card">
        <h3>UX Details</h3>
        <ul>
          <li><strong>Instant Role Switch:</strong> Single-click toggle between Family and Caregiver profiles.</li>
          <li><strong>Large Tap Targets:</strong> Designed for adult children and senior nurses on mobile/iPad.</li>
          <li><strong>Persistent Emergency Line:</strong> Critical phone numbers visible even before login.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>Figma Tokens</h3>
        <span class="token-tag">#0D9488 Primary</span>
        <span class="token-tag">12px Card Radius</span>
        <span class="token-tag">Shadow-LG</span>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 4: SCREEN 2 - FAMILY MEMBER DASHBOARD -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon">EC</div>
      <div class="page-title-group">
        <h1>04. Screen 2: Central Family Member Dashboard</h1>
        <p>Comprehensive status command center: vitals summary, upcoming medicine alert, daily routine & SOS</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 2 of 9</span>
      <span class="pill">Core Command Center</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame">
      <div class="mockup-chrome">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url">https://elderlycare.portal/dashboard</div>
        <span class="badge-hf badge-green">● System Live</span>
      </div>
      <div class="app-shell">
        <!-- Sidebar -->
        <div class="app-sidebar">
          <div>
            <div class="nav-header">
              <div class="nav-logo-box">EC</div>
              <span style="font-size:12px; font-weight:800; color:white;">ElderlyCare</span>
            </div>
            <div class="nav-menu">
              <div class="nav-link active">📊 Dashboard</div>
              <div class="nav-link">👤 Elderly Profile</div>
              <div class="nav-link">💊 Medicines</div>
              <div class="nav-link">🩺 Appointments</div>
              <div class="nav-link">📋 Daily Routine</div>
              <div class="nav-link">🤝 Caregivers</div>
              <div class="nav-link" style="color:#FDA4AF;">🚨 Emergency SOS</div>
            </div>
          </div>
          <div style="padding:6px; background:rgba(255,255,255,0.06); border-radius:6px; font-size:10px;">
            <div style="color:#94A3B8;">User: Tariq (Son)</div>
            <div style="color:#14B8A6; font-weight:bold;">Family Admin</div>
          </div>
        </div>

        <!-- Main Workspace -->
        <div class="app-main">
          <!-- Topbar -->
          <div class="app-topbar">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:12px; font-weight:700; color:var(--slate-800);">Active Care Profile:</span>
              <strong style="font-size:12px; color:var(--primary-dark);">Abdul Rahman Chowdhury (76 Yrs)</strong>
              <span class="badge-hf badge-green">Vitals Stable</span>
            </div>
            <button class="btn-hf btn-danger" style="padding:4px 10px; font-size:11px;">
              🚨 ONE-TOUCH SOS
            </button>
          </div>

          <div class="app-content">
            <!-- Urgent reminder banner -->
            <div style="background:linear-gradient(90deg, #FEF3C7, #FFFBEB); border:1px solid #FCD34D; border-radius:8px; padding:7px 12px; display:flex; justify-content:space-between; align-items:center;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:16px;">⏰</span>
                <div>
                  <strong style="font-size:11.5px; color:#92400E;">Next Scheduled Dose: Atorvastatin 20mg (1 Tab)</strong>
                  <span style="font-size:10px; color:#B45309; margin-left:6px;">Due after lunch in 25 mins</span>
                </div>
              </div>
              <button class="btn-hf btn-primary" style="padding:3px 10px; font-size:10.5px;">✓ Mark Taken</button>
            </div>

            <!-- 4 Quick Stats -->
            <div class="grid-4">
              <div class="stat-card-hf">
                <div style="font-size:10px; color:var(--slate-400); font-weight:700;">BLOOD PRESSURE</div>
                <div style="font-size:17px; font-weight:800; color:var(--slate-900); margin:2px 0;">124 / 82 <span style="font-size:10px; font-weight:normal; color:var(--slate-400);">mmHg</span></div>
                <span class="badge-hf badge-green">Normal Reading</span>
              </div>
              <div class="stat-card-hf">
                <div style="font-size:10px; color:var(--slate-400); font-weight:700;">TODAY'S MEDICINES</div>
                <div style="font-size:17px; font-weight:800; color:var(--slate-900); margin:2px 0;">3 of 5 <span style="font-size:10px; font-weight:normal; color:var(--slate-400);">Taken</span></div>
                <span class="badge-hf badge-amber">60% Complete</span>
              </div>
              <div class="stat-card-hf">
                <div style="font-size:10px; color:var(--slate-400); font-weight:700;">NEXT APPOINTMENT</div>
                <div style="font-size:14px; font-weight:800; color:var(--slate-900); margin:2px 0;">Tomorrow 10:30 AM</div>
                <span style="font-size:10px; color:var(--blue-600); font-weight:600;">Dr. Hasan (Cardio)</span>
              </div>
              <div class="stat-card-hf">
                <div style="font-size:10px; color:var(--slate-400); font-weight:700;">CAREGIVER ON DUTY</div>
                <div style="font-size:14px; font-weight:800; color:var(--slate-900); margin:2px 0;">Nasreen Akhtar</div>
                <span class="badge-hf badge-green">Active Shift</span>
              </div>
            </div>

            <!-- Content Split: Schedule & Caregiver log -->
            <div class="grid-2" style="flex:1;">
              <div class="card-hf">
                <div class="card-header-hf">
                  <h4>Today's Care Schedule (Sunday, Oct 4)</h4>
                  <span style="font-size:10px; color:var(--primary); font-weight:700; cursor:pointer;">View Full Routine ➔</span>
                </div>
                <div style="display:flex; flex-direction:column; gap:5px;">
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:5px 8px; background:#F8FAFC; border-radius:5px; font-size:10.5px;">
                    <div><strong>08:00 AM</strong> • Morning Walk & Breathing</div>
                    <span class="badge-hf badge-green">✓ Completed</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:5px 8px; background:#F8FAFC; border-radius:5px; font-size:10.5px;">
                    <div><strong>08:45 AM</strong> • Breakfast & Morning Meds</div>
                    <span class="badge-hf badge-green">✓ Completed</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:5px 8px; background:#FEF3C7; border-radius:5px; font-size:10.5px;">
                    <div><strong>01:30 PM</strong> • Healthy Lunch + Heart Dose</div>
                    <span class="badge-hf badge-amber">Due Soon</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; align-items:center; padding:5px 8px; background:#F8FAFC; border-radius:5px; font-size:10.5px;">
                    <div><strong>05:00 PM</strong> • Evening Sugar Check</div>
                    <span style="font-size:10px; color:var(--slate-400);">Scheduled</span>
                  </div>
                </div>
              </div>

              <div class="card-hf">
                <div class="card-header-hf">
                  <h4>Caregiver Live Observation Notes</h4>
                  <button class="btn-hf btn-secondary" style="padding:2px 7px; font-size:10px;">+ Add Note</button>
                </div>
                <div style="background:#F0FDFA; border:1px solid #CCFBF1; border-radius:6px; padding:8px; font-size:10.5px; color:#0F766E; margin-bottom:6px;">
                  <strong>Logged by Nasreen (11:20 AM):</strong><br>
                  "Patient ate full breakfast with great appetite. Blood sugar checked at 110 mg/dL. Finished 15 mins garden stroll safely."
                </div>
                <div style="background:#EFF6FF; border:1px solid #DBEAFE; border-radius:6px; padding:8px; font-size:10.5px; color:#1E40AF;">
                  <strong>Upcoming Doctor Preparation:</strong><br>
                  Echo reports from August kept ready in folder for tomorrow's visit with Dr. Hasan at Square Hospital.
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Screen Objective</h3>
        <p>Provide family members complete peace of mind in under 5 seconds. Immediate overview of vitals, adherence percentage, and live caregiver shift notes.</p>
      </div>

      <div class="spec-card">
        <h3>UX Components</h3>
        <ul>
          <li><strong>Amber Alert Banner:</strong> Highlights the immediate next medication.</li>
          <li><strong>Stat Cards:</strong> Real-time BP, pill count, and duty nurse status.</li>
          <li><strong>Instant SOS:</strong> Persistent Red trigger for immediate help.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>Data Handled</h3>
        <span class="token-tag">Vitals Stream</span>
        <span class="token-tag">Adherence %</span>
        <span class="token-tag">Shift Status</span>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 5: SCREEN 3 - ELDERLY PROFILE -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon">EC</div>
      <div class="page-title-group">
        <h1>05. Screen 3: Elderly Profile & Medical History</h1>
        <p>Comprehensive electronic health record: personal demographics, chronic conditions, and physician contacts</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 3 of 9</span>
      <span class="pill">EHR & Demographics</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame">
      <div class="mockup-chrome">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url">https://elderlycare.portal/profile/senior-01</div>
        <button class="btn-hf btn-secondary" style="padding:2px 8px; font-size:10px;">✎ Edit Records</button>
      </div>
      <div class="app-shell">
        <div class="app-sidebar">
          <div>
            <div class="nav-header">
              <div class="nav-logo-box">EC</div>
              <span style="font-size:12px; font-weight:800; color:white;">ElderlyCare</span>
            </div>
            <div class="nav-menu">
              <div class="nav-link">📊 Dashboard</div>
              <div class="nav-link active">👤 Elderly Profile</div>
              <div class="nav-link">💊 Medicines</div>
              <div class="nav-link">🩺 Appointments</div>
              <div class="nav-link">📋 Daily Routine</div>
              <div class="nav-link">🤝 Caregivers</div>
              <div class="nav-link" style="color:#FDA4AF;">🚨 Emergency SOS</div>
            </div>
          </div>
          <div style="font-size:10px; color:#94A3B8; padding:6px;">Record ID: EC-2026-881</div>
        </div>

        <div class="app-main">
          <div class="app-topbar">
            <span style="font-size:12px; font-weight:700; color:var(--slate-800);">Elderly Health Profile & Emergency Summary</span>
            <span class="badge-hf badge-red" style="font-weight:700;">⚠️ Penicillin Allergy</span>
          </div>

          <div class="app-content">
            <!-- Profile Hero Box -->
            <div class="card-hf" style="display:flex; gap:16px; align-items:center; background:linear-gradient(135deg, #FFFFFF, #F8FAFC);">
              <div style="width:68px; height:68px; border-radius:50%; background:#E2E8F0; border:2px solid var(--primary); display:flex; align-items:center; justify-content:center; font-size:30px;">
                👴
              </div>
              <div style="flex:1;">
                <div style="display:flex; align-items:center; gap:8px;">
                  <h2 style="font-size:16px; font-weight:800; color:var(--slate-900);">Abdul Rahman Chowdhury</h2>
                  <span class="badge-hf badge-blue">Blood Group: B+ (Positive)</span>
                </div>
                <div style="font-size:11px; color:var(--slate-600); margin-top:2px;">
                  Age: <strong>76 Years</strong> • Male • Born: 14 Aug 1950 • Weight: 68 kg • Height: 5' 7"
                </div>
                <div style="font-size:10.5px; color:var(--slate-400); margin-top:2px;">
                  Residential Address: House 42, Road 11, Dhanmondi R/A, Dhaka-1209
                </div>
              </div>
              <div style="display:flex; flex-direction:column; gap:4px; align-items:flex-end;">
                <span class="badge-hf badge-amber">Mobility: Walking Cane</span>
                <span class="badge-hf badge-green">Insurance: Active (Pragati Life)</span>
              </div>
            </div>

            <!-- Health Details Grid -->
            <div class="grid-3" style="flex:1;">
              <div class="card-hf">
                <div class="card-header-hf"><h4>Chronic Conditions</h4></div>
                <div style="display:flex; flex-direction:column; gap:6px; font-size:11px;">
                  <div style="display:flex; justify-content:space-between; padding:4px 6px; background:#F8FAFC; border-radius:4px;">
                    <span>• Type-2 Diabetes</span> <span class="badge-hf badge-amber">Since 2012</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; padding:4px 6px; background:#F8FAFC; border-radius:4px;">
                    <span>• Hypertension (High BP)</span> <span class="badge-hf badge-blue">Since 2015</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; padding:4px 6px; background:#F8FAFC; border-radius:4px;">
                    <span>• Coronary Stent</span> <span class="badge-hf badge-green">Placed 2021</span>
                  </div>
                  <div style="display:flex; justify-content:space-between; padding:4px 6px; background:#F8FAFC; border-radius:4px;">
                    <span>• Mild Osteoarthritis</span> <span style="font-size:10px; color:var(--slate-400);">Left Knee</span>
                  </div>
                </div>
              </div>

              <div class="card-hf">
                <div class="card-header-hf"><h4>Primary Doctors</h4></div>
                <div style="display:flex; flex-direction:column; gap:6px;">
                  <div style="padding:6px; background:#F8FAFC; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="font-size:11px;">Dr. K. M. Hasan</strong><br>
                      <span style="font-size:10px; color:var(--slate-600);">Cardiologist, Square Hospital</span>
                    </div>
                    <button class="btn-hf btn-secondary" style="padding:2px 6px; font-size:10px;">📞 Call</button>
                  </div>
                  <div style="padding:6px; background:#F8FAFC; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="font-size:11px;">Dr. Nusrat Jahan</strong><br>
                      <span style="font-size:10px; color:var(--slate-600);">Endocrinologist, Labaid</span>
                    </div>
                    <button class="btn-hf btn-secondary" style="padding:2px 6px; font-size:10px;">📞 Call</button>
                  </div>
                </div>
              </div>

              <div class="card-hf">
                <div class="card-header-hf"><h4>Care Directives & Diet</h4></div>
                <p style="font-size:10.5px; color:var(--slate-600); line-height:1.5;">
                  • <strong>Diet:</strong> Strict low-sodium, diabetic-friendly meals (under 1500 kcal).<br>
                  • <strong>Hydration:</strong> 200ml fluid intake prompt every 2 hours.<br>
                  • <strong>Fall Prevention:</strong> Non-slip bathroom mats & walking cane assistance mandatory.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Screen Purpose</h3>
        <p>A single-pane medical repository for attending clinicians and rotating caregivers, ensuring critical allergies and pre-existing conditions are never overlooked.</p>
      </div>

      <div class="spec-card">
        <h3>UI Features</h3>
        <ul>
          <li><strong>Critical Allergy Tag:</strong> Penicillin alert highlighted in vivid red.</li>
          <li><strong>Direct Calling:</strong> Fast dial triggers for primary treating physicians.</li>
          <li><strong>Mobility Flag:</strong> Prepares caregivers for physical support needs.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>Data Architecture</h3>
        <span class="token-tag">Demographics</span>
        <span class="token-tag">Allergy Protocol</span>
        <span class="token-tag">Physician Links</span>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 6: SCREEN 4 - MEDICINE SCHEDULE -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon">EC</div>
      <div class="page-title-group">
        <h1>06. Screen 4: Medicine Schedule & Tracker</h1>
        <p>Chronological prescription tracker organized by Morning, Afternoon, Evening, and Bedtime slots</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 4 of 9</span>
      <span class="pill">Medication Safety</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame">
      <div class="mockup-chrome">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url">https://elderlycare.portal/medications</div>
        <button class="btn-hf btn-primary" style="padding:2px 8px; font-size:10px;">+ Add Medication</button>
      </div>
      <div class="app-shell">
        <div class="app-sidebar">
          <div>
            <div class="nav-header">
              <div class="nav-logo-box">EC</div>
              <span style="font-size:12px; font-weight:800; color:white;">ElderlyCare</span>
            </div>
            <div class="nav-menu">
              <div class="nav-link">📊 Dashboard</div>
              <div class="nav-link">👤 Elderly Profile</div>
              <div class="nav-link active">💊 Medicines</div>
              <div class="nav-link">🩺 Appointments</div>
              <div class="nav-link">📋 Daily Routine</div>
              <div class="nav-link">🤝 Caregivers</div>
              <div class="nav-link" style="color:#FDA4AF;">🚨 Emergency SOS</div>
            </div>
          </div>
          <div style="font-size:10px; color:#94A3B8; padding:6px;">Daily Dose Target: 5 Pills</div>
        </div>

        <div class="app-main">
          <div class="app-topbar">
            <div style="display:flex; gap:6px;">
              <button class="btn-hf btn-primary" style="padding:3px 9px; font-size:10.5px;">Today's Schedule (Oct 4)</button>
              <button class="btn-hf btn-secondary" style="padding:3px 9px; font-size:10.5px;">All Prescriptions (8)</button>
              <button class="btn-hf btn-secondary" style="padding:3px 9px; font-size:10.5px;">Refill Alerts (2)</button>
            </div>
            <span class="badge-hf badge-green">3 of 5 Taken</span>
          </div>

          <div class="app-content">
            <!-- Morning Slot -->
            <div class="card-hf" style="border-left:4px solid #10B981; padding:8px 12px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                <strong style="font-size:11.5px; color:#065F46;">🌅 MORNING ROUTINE (08:00 AM – 09:00 AM)</strong>
                <span class="badge-hf badge-green">✓ All Taken (Verified by Nurse Nasreen)</span>
              </div>
              <div class="grid-2">
                <div style="display:flex; justify-content:space-between; align-items:center; background:#F0FDF4; border:1px solid #DCFCE7; border-radius:6px; padding:6px 10px;">
                  <div>
                    <strong style="font-size:11px;">Metformin 500mg</strong> <span style="font-size:10px; color:var(--slate-600);">(1 Tablet)</span><br>
                    <span style="font-size:9.5px; color:var(--slate-400);">With Breakfast • Dr. Nusrat</span>
                  </div>
                  <span class="badge-hf badge-green">Taken 08:35 AM</span>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:center; background:#F0FDF4; border:1px solid #DCFCE7; border-radius:6px; padding:6px 10px;">
                  <div>
                    <strong style="font-size:11px;">Amlodipine 5mg</strong> <span style="font-size:10px; color:var(--slate-600);">(1 Tablet)</span><br>
                    <span style="font-size:9.5px; color:var(--slate-400);">After Breakfast • Dr. Hasan</span>
                  </div>
                  <span class="badge-hf badge-green">Taken 08:35 AM</span>
                </div>
              </div>
            </div>

            <!-- Afternoon Slot -->
            <div class="card-hf" style="border-left:4px solid #F59E0B; background:#FFFBEB; padding:8px 12px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                <strong style="font-size:11.5px; color:#92400E;">☀️ AFTERNOON ROUTINE (01:30 PM – 02:00 PM)</strong>
                <span class="badge-hf badge-amber">⏳ Due in 25 Minutes</span>
              </div>
              <div style="display:flex; justify-content:space-between; align-items:center; background:#FFFFFF; border:1px solid #FDE68A; border-radius:6px; padding:8px 10px;">
                <div>
                  <strong style="font-size:12px;">Atorvastatin Lipitor 20mg</strong> <span style="font-size:10.5px; color:var(--slate-600);">(1 Tablet - Cholesterol)</span><br>
                  <span style="font-size:10px; color:var(--slate-400);">Take immediately following lunch with water • Prescribed by Dr. Hasan</span>
                </div>
                <div style="display:flex; gap:6px;">
                  <button class="btn-hf btn-primary" style="padding:4px 10px; font-size:10.5px;">✓ Mark Taken</button>
                  <button class="btn-hf btn-secondary" style="padding:4px 8px; font-size:10.5px;">Snooze 15m</button>
                </div>
              </div>
            </div>

            <!-- Bedtime Slot -->
            <div class="card-hf" style="border-left:4px solid #6366F1; padding:8px 12px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                <strong style="font-size:11.5px; color:#3730A3;">🌙 NIGHT & BEDTIME ROUTINE (09:30 PM – 10:00 PM)</strong>
                <span style="font-size:10px; color:var(--slate-400);">2 Doses Scheduled</span>
              </div>
              <div class="grid-2">
                <div style="display:flex; justify-content:space-between; align-items:center; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; padding:6px 10px;">
                  <div>
                    <strong style="font-size:11px;">Metformin 500mg</strong> <span style="font-size:10px; color:var(--slate-600);">(1 Tablet)</span><br>
                    <span style="font-size:9.5px; color:var(--slate-400);">After Dinner</span>
                  </div>
                  <span style="font-size:10px; color:var(--slate-400);">Upcoming</span>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:center; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; padding:6px 10px;">
                  <div>
                    <strong style="font-size:11px;">Calcium D3</strong> <span style="font-size:10px; color:var(--slate-600);">(1 Tablet)</span><br>
                    <span style="font-size:9.5px; color:var(--slate-400);">With Warm Milk</span>
                  </div>
                  <span style="font-size:10px; color:var(--slate-400);">Upcoming</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Screen Purpose</h3>
        <p>Eliminates missed or doubled medication doses. Real-time logging creates a verified digital audit trail with nurse verification.</p>
      </div>

      <div class="spec-card">
        <h3>Safety Controls</h3>
        <ul>
          <li><strong>Chronological Sorting:</strong> Clear time buckets prevent confusion.</li>
          <li><strong>One-Click Confirmation:</strong> Fast "Mark Taken" button updates family dashboard instantly.</li>
          <li><strong>Refill Tracking:</strong> Automatic counter notifies when 5 pills remain.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>Audit Trail</h3>
        <span class="token-tag">Timestamped</span>
        <span class="token-tag">Nurse ID</span>
        <span class="token-tag">Missed Alert</span>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 7: SCREEN 5 - ADD MEDICATION MODAL -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon">EC</div>
      <div class="page-title-group">
        <h1>07. Screen 5: Add / Edit Medication Form</h1>
        <p>Prescription entry form with dose validation, meal-timing association, and low-stock refill triggers</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 5 of 9</span>
      <span class="pill">Prescription Input</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame">
      <div class="mockup-chrome">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url">https://elderlycare.portal/medications/new</div>
        <span style="font-size:10px; color:var(--slate-400); cursor:pointer;">✕ Close Form</span>
      </div>
      <div class="app-shell" style="align-items:center; justify-content:center; background:rgba(15, 23, 42, 0.4); backdrop-filter:blur(3px);">
        <!-- Modal Card -->
        <div class="card-hf" style="width:480px; padding:18px; border-radius:12px; box-shadow:var(--shadow-lg);">
          <div class="card-header-hf">
            <div>
              <h3 style="font-size:14px; font-weight:800; color:var(--slate-900);">➕ Add Medication Schedule</h3>
              <p style="font-size:10px; color:var(--slate-400);">Ensure dosage matches physical prescription</p>
            </div>
            <span class="badge-hf badge-blue">New Prescription</span>
          </div>

          <div style="display:flex; flex-direction:column; gap:8px; margin-top:6px;">
            <div class="grid-2">
              <div>
                <label style="font-size:10.5px; font-weight:700; color:var(--slate-700); display:block; margin-bottom:2px;">Medicine Name *</label>
                <input type="text" value="Atorvastatin (Lipitor)" style="width:100%; padding:6px 8px; border:1px solid #CBD5E1; border-radius:6px; font-size:11px;" readonly>
              </div>
              <div>
                <label style="font-size:10.5px; font-weight:700; color:var(--slate-700); display:block; margin-bottom:2px;">Dosage & Unit *</label>
                <input type="text" value="20 mg (1 Tablet)" style="width:100%; padding:6px 8px; border:1px solid #CBD5E1; border-radius:6px; font-size:11px;" readonly>
              </div>
            </div>

            <div class="grid-3">
              <div>
                <label style="font-size:10.5px; font-weight:700; color:var(--slate-700); display:block; margin-bottom:2px;">Frequency *</label>
                <input type="text" value="Once Daily" style="width:100%; padding:6px 8px; border:1px solid #CBD5E1; border-radius:6px; font-size:11px;" readonly>
              </div>
              <div>
                <label style="font-size:10.5px; font-weight:700; color:var(--slate-700); display:block; margin-bottom:2px;">Meal Timing *</label>
                <input type="text" value="After Lunch" style="width:100%; padding:6px 8px; border:1px solid #CBD5E1; border-radius:6px; font-size:11px;" readonly>
              </div>
              <div>
                <label style="font-size:10.5px; font-weight:700; color:var(--slate-700); display:block; margin-bottom:2px;">Schedule Time *</label>
                <input type="text" value="01:30 PM" style="width:100%; padding:6px 8px; border:1px solid #CBD5E1; border-radius:6px; font-size:11px;" readonly>
              </div>
            </div>

            <div class="grid-2">
              <div>
                <label style="font-size:10.5px; font-weight:700; color:var(--slate-700); display:block; margin-bottom:2px;">Prescribed By</label>
                <input type="text" value="Dr. K. M. Hasan (Cardiology)" style="width:100%; padding:6px 8px; border:1px solid #CBD5E1; border-radius:6px; font-size:11px;" readonly>
              </div>
              <div>
                <label style="font-size:10.5px; font-weight:700; color:var(--slate-700); display:block; margin-bottom:2px;">Remaining Stock / Refill Alert</label>
                <input type="text" value="30 Pills (Alert at 5)" style="width:100%; padding:6px 8px; border:1px solid #CBD5E1; border-radius:6px; font-size:11px;" readonly>
              </div>
            </div>

            <div>
              <label style="font-size:10.5px; font-weight:700; color:var(--slate-700); display:block; margin-bottom:2px;">Special Instructions & Caution</label>
              <textarea style="width:100%; height:38px; padding:6px 8px; border:1px solid #CBD5E1; border-radius:6px; font-size:10.5px; resize:none;" readonly>Take with full glass of water. Avoid grapefruit juice while on this medication.</textarea>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--slate-100); padding-top:8px; margin-top:4px;">
              <div style="display:flex; align-items:center; gap:5px;">
                <input type="checkbox" checked style="accent-color:var(--primary);">
                <span style="font-size:10.5px; color:var(--slate-600);">Send SMS alert to son Tariq</span>
              </div>
              <div style="display:flex; gap:6px;">
                <button class="btn-hf btn-secondary" style="padding:5px 10px; font-size:11px;">Cancel</button>
                <button class="btn-hf btn-primary" style="padding:5px 14px; font-size:11px;">Save & Activate</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Form Validation</h3>
        <p>Medical safety constraints prevent accidental overdose entries or uncalibrated frequencies.</p>
      </div>

      <div class="spec-card">
        <h3>Key Fields</h3>
        <ul>
          <li><strong>Prescribing Doctor:</strong> Links the dose directly to clinical consultations.</li>
          <li><strong>Meal Timing:</strong> Before meal / with food / after meal selectors.</li>
          <li><strong>Inventory Counter:</strong> Automatically computes days until refill needed.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>Modal Behavior</h3>
        <span class="token-tag">Backdrop Blur</span>
        <span class="token-tag">Required Validation</span>
        <span class="token-tag">SMS Hook</span>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 8: SCREEN 6 - DOCTOR APPOINTMENTS -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon">EC</div>
      <div class="page-title-group">
        <h1>08. Screen 6: Doctor Appointment Tracking</h1>
        <p>Medical appointment calendar, physician directory, consultation reports, and family escort details</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 6 of 9</span>
      <span class="pill">Clinical Scheduling</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame">
      <div class="mockup-chrome">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url">https://elderlycare.portal/appointments</div>
        <button class="btn-hf btn-primary" style="padding:2px 8px; font-size:10px;">+ Book Visit</button>
      </div>
      <div class="app-shell">
        <div class="app-sidebar">
          <div>
            <div class="nav-header">
              <div class="nav-logo-box">EC</div>
              <span style="font-size:12px; font-weight:800; color:white;">ElderlyCare</span>
            </div>
            <div class="nav-menu">
              <div class="nav-link">📊 Dashboard</div>
              <div class="nav-link">👤 Elderly Profile</div>
              <div class="nav-link">💊 Medicines</div>
              <div class="nav-link active">🩺 Appointments</div>
              <div class="nav-link">📋 Daily Routine</div>
              <div class="nav-link">🤝 Caregivers</div>
              <div class="nav-link" style="color:#FDA4AF;">🚨 Emergency SOS</div>
            </div>
          </div>
          <div style="font-size:10px; color:#94A3B8; padding:6px;">Next: Tomorrow 10:30 AM</div>
        </div>

        <div class="app-main">
          <div class="app-topbar">
            <span style="font-size:12px; font-weight:700; color:var(--slate-800);">Doctor Consultation Schedule & History</span>
            <span class="badge-hf badge-blue">SMS Alert: 24h & 2h Prior</span>
          </div>

          <div class="app-content">
            <!-- Hero Next Appointment -->
            <div class="card-hf" style="background:linear-gradient(135deg, #EFF6FF, #DBEAFE); border:1px solid #BFDBFE; display:flex; justify-content:space-between; align-items:center; padding:10px 14px;">
              <div>
                <span class="badge-hf badge-blue" style="font-weight:700;">NEXT SCHEDULED CONSULTATION</span>
                <h3 style="font-size:15px; font-weight:800; color:#1E3A8A; margin-top:3px;">Dr. K. M. Hasan — Senior Cardiologist</h3>
                <p style="font-size:11px; color:#1E40AF;">
                  Square Hospital, Panthapath • <strong>Tomorrow (Monday, Oct 5) at 10:30 AM</strong> (Room 314)
                </p>
                <p style="font-size:10px; color:#2563EB; margin-top:2px;">
                  Clinical Goal: 3-Month Echo & ECG Review • Escort: Tariq (Son) • Transport Arranged
                </p>
              </div>
              <div style="display:flex; flex-direction:column; gap:4px;">
                <button class="btn-hf btn-primary" style="padding:4px 10px; font-size:10px;">📍 View Hospital Map</button>
                <button class="btn-hf btn-secondary" style="padding:4px 10px; font-size:10px;">🔔 Notification Active</button>
              </div>
            </div>

            <!-- Future vs Past split -->
            <div class="grid-2" style="flex:1;">
              <div class="card-hf">
                <div class="card-header-hf"><h4>Future Scheduled Visits</h4></div>
                <div style="display:flex; flex-direction:column; gap:6px;">
                  <div style="padding:6px 8px; background:#F8FAFC; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="font-size:11px;">Dr. Nusrat Jahan (Diabetes)</strong><br>
                      <span style="font-size:10px; color:var(--slate-600);">Labaid Diagnostic, Dhanmondi</span><br>
                      <span style="font-size:9.5px; color:var(--slate-400);">Oct 18, 2026 • 05:00 PM (Fasting Blood Sugar)</span>
                    </div>
                    <button class="btn-hf btn-secondary" style="padding:2px 6px; font-size:10px;">Reschedule</button>
                  </div>
                  <div style="padding:6px 8px; background:#F8FAFC; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="font-size:11px;">Dr. Shahed Ali (Orthopedic)</strong><br>
                      <span style="font-size:10px; color:var(--slate-600);">Popular Hospital, Shantinagar</span><br>
                      <span style="font-size:9.5px; color:var(--slate-400);">Nov 02, 2026 • 11:00 AM (Knee Joint Mobility)</span>
                    </div>
                    <button class="btn-hf btn-secondary" style="padding:2px 6px; font-size:10px;">Reschedule</button>
                  </div>
                </div>
              </div>

              <div class="card-hf">
                <div class="card-header-hf"><h4>Past Consultation Records & RX</h4></div>
                <div style="display:flex; flex-direction:column; gap:6px;">
                  <div style="padding:6px 8px; background:#F8FAFC; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="font-size:11px;">Routine Cardiology Follow-up</strong><br>
                      <span style="font-size:9.5px; color:var(--slate-400);">Sep 04, 2026 • Dr. K. M. Hasan (BP: 120/80)</span>
                    </div>
                    <button class="btn-hf btn-secondary" style="padding:2px 6px; font-size:10px;">📄 View RX</button>
                  </div>
                  <div style="padding:6px 8px; background:#F8FAFC; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="font-size:11px;">Ophthalmology Vision Assessment</strong><br>
                      <span style="font-size:9.5px; color:var(--slate-400);">Aug 12, 2026 • Vision stable, no cataract surgery</span>
                    </div>
                    <button class="btn-hf btn-secondary" style="padding:2px 6px; font-size:10px;">📄 View RX</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Screen Purpose</h3>
        <p>Centralizes all doctor appointments so family members can coordinate transport, tests, and family escorts well in advance.</p>
      </div>

      <div class="spec-card">
        <h3>Feature Highlights</h3>
        <ul>
          <li><strong>Escort Designation:</strong> Clearly designates which son/daughter will attend.</li>
          <li><strong>Digital Prescriptions:</strong> Instant access to scanned prescriptions from past visits.</li>
          <li><strong>Map Integration:</strong> Direct clinic navigation directions.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>System Integrations</h3>
        <span class="token-tag">Google Calendar</span>
        <span class="token-tag">SMS Reminders</span>
        <span class="token-tag">PDF RX Archive</span>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 9: SCREEN 7 - DAILY CARE ROUTINE -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon">EC</div>
      <div class="page-title-group">
        <h1>09. Screen 7: Daily Care Schedule & Activities</h1>
        <p>Holistic elderly lifestyle checklist: meals, hydration checks, light mobility, and vitals recording</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 7 of 9</span>
      <span class="pill">Daily Routine Checklist</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame">
      <div class="mockup-chrome">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url">https://elderlycare.portal/daily-schedule</div>
        <span class="badge-hf badge-green">4 of 7 Completed (57%)</span>
      </div>
      <div class="app-shell">
        <div class="app-sidebar">
          <div>
            <div class="nav-header">
              <div class="nav-logo-box">EC</div>
              <span style="font-size:12px; font-weight:800; color:white;">ElderlyCare</span>
            </div>
            <div class="nav-menu">
              <div class="nav-link">📊 Dashboard</div>
              <div class="nav-link">👤 Elderly Profile</div>
              <div class="nav-link">💊 Medicines</div>
              <div class="nav-link">🩺 Appointments</div>
              <div class="nav-link active">📋 Daily Routine</div>
              <div class="nav-link">🤝 Caregivers</div>
              <div class="nav-link" style="color:#FDA4AF;">🚨 Emergency SOS</div>
            </div>
          </div>
          <div style="font-size:10px; color:#94A3B8; padding:6px;">Shift Nurse: Nasreen</div>
        </div>

        <div class="app-main">
          <div class="app-topbar">
            <span style="font-size:12px; font-weight:700; color:var(--slate-800);">Daily Care Routine Checklist (Sunday, Oct 4)</span>
            <button class="btn-hf btn-secondary" style="padding:2px 8px; font-size:10px;">+ Add Custom Task</button>
          </div>

          <div class="app-content">
            <!-- Checklist items -->
            <div style="display:flex; flex-direction:column; gap:5px; overflow:hidden;">
              <div style="display:flex; justify-content:space-between; align-items:center; padding:7px 10px; background:#F0FDF4; border:1px solid #BBF7D0; border-radius:6px; font-size:11px;">
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="color:#059669; font-weight:bold; font-size:14px;">☑</span>
                  <div>
                    <strong>07:30 AM • Wakeup & Morning Hydration</strong><br>
                    <span style="font-size:9.5px; color:var(--slate-600);">1 Glass lukewarm water + lemon • Verified by Nurse Nasreen</span>
                  </div>
                </div>
                <span class="badge-hf badge-green">Done 07:35 AM</span>
              </div>

              <div style="display:flex; justify-content:space-between; align-items:center; padding:7px 10px; background:#F0FDF4; border:1px solid #BBF7D0; border-radius:6px; font-size:11px;">
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="color:#059669; font-weight:bold; font-size:14px;">☑</span>
                  <div>
                    <strong>08:15 AM • Light Morning Exercise & Sun Exposure</strong><br>
                    <span style="font-size:9.5px; color:var(--slate-600);">15 min garden walk with walking stick + ankle mobility</span>
                  </div>
                </div>
                <span class="badge-hf badge-green">Done 08:30 AM</span>
              </div>

              <div style="display:flex; justify-content:space-between; align-items:center; padding:7px 10px; background:#F0FDF4; border:1px solid #BBF7D0; border-radius:6px; font-size:11px;">
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="color:#059669; font-weight:bold; font-size:14px;">☑</span>
                  <div>
                    <strong>08:45 AM • Nutritious Breakfast & Vitals Measurement</strong><br>
                    <span style="font-size:9.5px; color:var(--slate-600);">Oatmeal, boiled egg white & papaya • BP: 124/82 mmHg (Normal)</span>
                  </div>
                </div>
                <span class="badge-hf badge-green">Done 09:00 AM</span>
              </div>

              <div style="display:flex; justify-content:space-between; align-items:center; padding:7px 10px; background:#FFFBEB; border:1px solid #FCD34D; border-radius:6px; font-size:11px;">
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="color:#D97706; font-size:14px;">☐</span>
                  <div>
                    <strong style="color:#92400E;">01:15 PM • Healthy Diabetic Lunch Routine</strong><br>
                    <span style="font-size:9.5px; color:#B45309;">Steamed rice, boiled rui fish curry, mixed green vegetables (low salt)</span>
                  </div>
                </div>
                <button class="btn-hf btn-primary" style="padding:3px 10px; font-size:10px;">Mark Done</button>
              </div>

              <div style="display:flex; justify-content:space-between; align-items:center; padding:7px 10px; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; font-size:11px;">
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="color:var(--slate-400); font-size:14px;">☐</span>
                  <div>
                    <strong>04:30 PM • Afternoon Hydration & Knee Physiotherapy</strong><br>
                    <span style="font-size:9.5px; color:var(--slate-600);">Fresh coconut water / herbal tea + 15 min knee flexion exercises</span>
                  </div>
                </div>
                <span style="font-size:10px; color:var(--slate-400);">Scheduled</span>
              </div>

              <div style="display:flex; justify-content:space-between; align-items:center; padding:7px 10px; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; font-size:11px;">
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="color:var(--slate-400); font-size:14px;">☐</span>
                  <div>
                    <strong>08:30 PM • Light Dinner & Bedtime Comfort Prep</strong><br>
                    <span style="font-size:9.5px; color:var(--slate-600);">Vegetable soup, 2 wheat rotis, room temperature check</span>
                  </div>
                </div>
                <span style="font-size:10px; color:var(--slate-400);">Scheduled</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Holistic Health Focus</h3>
        <p>Comprehensive care requires nutrition, hydration, and mobility, not just pills. This screen turns clinical directives into an achievable daily routine.</p>
      </div>

      <div class="spec-card">
        <h3>Key Features</h3>
        <ul>
          <li><strong>Digital Checkbox:</strong> Tap to toggle status with instantaneous timestamp.</li>
          <li><strong>Meal Composition:</strong> Explicitly states low-salt / diabetic instructions.</li>
          <li><strong>Caregiver Verification:</strong> Prevents missed nutrition or hydration gaps.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>Categories</h3>
        <span class="token-tag">Nutrition</span>
        <span class="token-tag">Vitals</span>
        <span class="token-tag">Hydration</span>
        <span class="token-tag">Mobility</span>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 10: SCREEN 8 - CAREGIVER INFO & HANDOFF -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon">EC</div>
      <div class="page-title-group">
        <h1>10. Screen 8: Caregiver Information & Shift Handoff Log</h1>
        <p>Caregiver directory, verified credentials, shift clock-in, duty checklist, and observation exchange</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 8 of 9</span>
      <span class="pill">Caregiver Coordination</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame">
      <div class="mockup-chrome">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url">https://elderlycare.portal/caregivers</div>
        <button class="btn-hf btn-primary" style="padding:2px 8px; font-size:10px;">+ Assign Caregiver</button>
      </div>
      <div class="app-shell">
        <div class="app-sidebar">
          <div>
            <div class="nav-header">
              <div class="nav-logo-box">EC</div>
              <span style="font-size:12px; font-weight:800; color:white;">ElderlyCare</span>
            </div>
            <div class="nav-menu">
              <div class="nav-link">📊 Dashboard</div>
              <div class="nav-link">👤 Elderly Profile</div>
              <div class="nav-link">💊 Medicines</div>
              <div class="nav-link">🩺 Appointments</div>
              <div class="nav-link">📋 Daily Routine</div>
              <div class="nav-link active">🤝 Caregivers</div>
              <div class="nav-link" style="color:#FDA4AF;">🚨 Emergency SOS</div>
            </div>
          </div>
          <div style="font-size:10px; color:#94A3B8; padding:6px;">Staff On Duty: 1</div>
        </div>

        <div class="app-main">
          <div class="app-topbar">
            <span style="font-size:12px; font-weight:700; color:var(--slate-800);">Caregiver Management & Digital Shift Log</span>
            <span class="badge-hf badge-green">● Clocked In at 07:55 AM</span>
          </div>

          <div class="app-content">
            <!-- Active Caregiver Card -->
            <div class="card-hf" style="display:flex; justify-content:space-between; align-items:center; background:#F0FDF4; border:1px solid #86EFAC; padding:10px 14px;">
              <div style="display:flex; gap:12px; align-items:center;">
                <div style="width:48px; height:48px; border-radius:50%; background:#DCFCE7; border:2px solid #16A34A; display:flex; align-items:center; justify-content:center; font-size:24px;">
                  👩‍⚕️
                </div>
                <div>
                  <span class="badge-hf badge-green" style="font-weight:700;">CURRENTLY ON ACTIVE SHIFT</span>
                  <h3 style="font-size:14px; font-weight:800; color:#14532D; margin-top:2px;">Nasreen Akhtar (Senior Certified Nurse)</h3>
                  <p style="font-size:11px; color:#166534;">
                    Day Shift: 08:00 AM – 04:00 PM • Agency: CareCompanion BD • 6 Yrs Geriatric Experience
                  </p>
                  <p style="font-size:10px; color:#15803D;">Verified Background Check • Police Cleared</p>
                </div>
              </div>
              <div style="display:flex; gap:6px;">
                <button class="btn-hf btn-secondary" style="padding:4px 10px; font-size:10.5px;">📞 Call: 01812-XXXXXX</button>
                <button class="btn-hf btn-primary" style="padding:4px 10px; font-size:10.5px;">💬 Instant Chat</button>
              </div>
            </div>

            <!-- Shift Handover & Observations -->
            <div class="grid-2" style="flex:1;">
              <div class="card-hf">
                <div class="card-header-hf"><h4>Secondary Caregiver Roster</h4></div>
                <div style="display:flex; flex-direction:column; gap:6px;">
                  <div style="padding:6px 8px; background:#F8FAFC; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="font-size:11px;">Faruk Hossain</strong> (Night Shift Nurse)<br>
                      <span style="font-size:9.5px; color:var(--slate-600);">Shift: 08:00 PM – 08:00 AM • Tel: 01734-XXXXXX</span>
                    </div>
                    <span class="badge-hf badge-blue">Starts 8 PM</span>
                  </div>
                  <div style="padding:6px 8px; background:#F8FAFC; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="font-size:11px;">Morium Begum</strong> (Weekend Relief)<br>
                      <span style="font-size:9.5px; color:var(--slate-600);">Fri & Sat Schedule • Tel: 01923-XXXXXX</span>
                    </div>
                    <span style="font-size:10px; color:var(--slate-400);">Off Duty</span>
                  </div>
                </div>
              </div>

              <div class="card-hf">
                <div class="card-header-hf"><h4>Shift Handover Observations</h4></div>
                <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; padding:6px 8px; font-size:10.5px; color:var(--slate-700); margin-bottom:6px;">
                  <strong>Nasreen Akhtar (Oct 4, 11:30 AM):</strong><br>
                  "Patient complained of mild stiffness in left knee joint after morning stroll. Administered 10 min warm compress. Appetite normal; consumed all breakfast. Blood sugar measured at 110 mg/dL."
                </div>
                <div style="display:flex; gap:6px;">
                  <input type="text" placeholder="Add clinical observation note for shift handoff..." style="flex:1; padding:5px 8px; border:1px solid #CBD5E1; border-radius:5px; font-size:10.5px;">
                  <button class="btn-hf btn-primary" style="padding:5px 10px; font-size:10px;">Post</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Screen Purpose</h3>
        <p>Facilitates smooth clinical handoffs between morning and night caregivers while keeping family members informed of daily behavioral changes.</p>
      </div>

      <div class="spec-card">
        <h3>Key Features</h3>
        <ul>
          <li><strong>Direct Connectivity:</strong> Family can phone or WhatsApp the caregiver with 1 tap.</li>
          <li><strong>Verified Staff Credentials:</strong> Displays nurse training and police clearance.</li>
          <li><strong>Observations Log:</strong> Real-time logging of physical discomfort or symptoms.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>Accountability</h3>
        <span class="token-tag">GPS Geofence</span>
        <span class="token-tag">Clock In/Out</span>
        <span class="token-tag">Handoff Notes</span>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 11: SCREEN 9 - EMERGENCY SOS -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon" style="background:#E11D48;">SOS</div>
      <div class="page-title-group">
        <h1 style="color:#BE123C;">11. Screen 9: Instant Emergency SOS & Paramedic Brief</h1>
        <p>Rapid one-touch emergency dispatch, hospital ER direct routing, and immediate medical summary</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill" style="background:#FFE4E6; color:#9F1239; border-color:#FECDD3;">Critical Safety Protocol</span>
      <span class="pill">Screen 9 of 9</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame" style="border-color:#FCA5A5;">
      <div class="mockup-chrome" style="background:#FFF1F2; border-color:#FECDD3;">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url" style="color:#BE123C; border-color:#FECDD3;">https://elderlycare.portal/emergency-sos</div>
        <span class="badge-hf badge-red">🚨 RAPID RESPONSE ACTIVE</span>
      </div>
      <div class="app-shell" style="background:#FFF5F5;">
        <div class="app-sidebar" style="background:#881337;">
          <div>
            <div class="nav-header">
              <div class="nav-logo-box" style="background:#E11D48;">SOS</div>
              <span style="font-size:12px; font-weight:800; color:white;">ElderlyCare</span>
            </div>
            <div class="nav-menu">
              <div class="nav-link" style="color:#FECDD3;">📊 Dashboard</div>
              <div class="nav-link" style="color:#FECDD3;">👤 Elderly Profile</div>
              <div class="nav-link" style="color:#FECDD3;">💊 Medicines</div>
              <div class="nav-link" style="color:#FECDD3;">🩺 Appointments</div>
              <div class="nav-link" style="color:#FECDD3;">📋 Daily Routine</div>
              <div class="nav-link" style="color:#FECDD3;">🤝 Caregivers</div>
              <div class="nav-link active" style="background:#BE123C; color:white;">🚨 Emergency SOS</div>
            </div>
          </div>
          <div style="font-size:10px; color:#FECDD3; padding:6px;">Hotline: 999 / 10616</div>
        </div>

        <div class="app-main" style="background:#FFF5F5;">
          <div class="app-topbar" style="background:#FFF1F2; border-color:#FECDD3;">
            <span style="font-size:12px; font-weight:800; color:#9F1239;">🚨 IMMEDIATE EMERGENCY BROADCAST CONSOLE</span>
            <button class="btn-hf btn-danger" style="padding:3px 12px; font-size:11px; animation:pulse 2s infinite;">
              ⚡ TRIGGER BROADCAST SMS TO ALL FAMILY
            </button>
          </div>

          <div class="app-content">
            <!-- 3 Big Speed-Dial Cards -->
            <div class="grid-3">
              <div class="card-hf" style="text-align:center; background:#FFFFFF; border:2px solid #F43F5E; padding:12px;">
                <span style="font-size:24px;">🚑</span>
                <div style="font-size:11px; font-weight:800; color:#881337; margin-top:2px;">National Ambulance</div>
                <div style="font-size:18px; font-weight:900; color:#E11D48; margin:2px 0;">999 / 199</div>
                <button class="btn-hf btn-danger" style="width:100%; padding:6px; font-size:11px; margin-top:4px;">
                  📞 CALL AMBULANCE NOW
                </button>
              </div>

              <div class="card-hf" style="text-align:center; background:#FFFFFF; border:2px solid #F43F5E; padding:12px;">
                <span style="font-size:24px;">🏥</span>
                <div style="font-size:11px; font-weight:800; color:#881337; margin-top:2px;">Square Hospital ER</div>
                <div style="font-size:17px; font-weight:900; color:#E11D48; margin:2px 0;">10616 / 02-8144400</div>
                <button class="btn-hf btn-danger" style="width:100%; padding:6px; font-size:11px; margin-top:4px;">
                  📞 CALL ER DESK NOW
                </button>
              </div>

              <div class="card-hf" style="text-align:center; background:#FFFFFF; border:2px solid #F43F5E; padding:12px;">
                <span style="font-size:24px;">👨‍⚕️</span>
                <div style="font-size:11px; font-weight:800; color:#881337; margin-top:2px;">Dr. Hasan (Cardio)</div>
                <div style="font-size:17px; font-weight:900; color:#E11D48; margin:2px 0;">01713-XXXXXX</div>
                <button class="btn-hf btn-danger" style="width:100%; padding:6px; font-size:11px; margin-top:4px;">
                  📞 CALL DOCTOR DIRECT
                </button>
              </div>
            </div>

            <!-- Family & Paramedic Brief -->
            <div class="grid-2" style="flex:1;">
              <div class="card-hf">
                <div class="card-header-hf"><h4>Family Emergency Contacts (Priority Order)</h4></div>
                <div style="display:flex; flex-direction:column; gap:6px;">
                  <div style="padding:6px 8px; background:#F8FAFC; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="font-size:11px;">Tariq Rahman</strong> <span class="badge-hf badge-green">Son • Priority 1</span><br>
                      <span style="font-size:9.5px; color:var(--slate-600);">Lives 10 mins away • Tel: 01711-XXXXXX</span>
                    </div>
                    <button class="btn-hf btn-secondary" style="padding:3px 8px; font-size:10px;">📞 Call 1st</button>
                  </div>
                  <div style="padding:6px 8px; background:#F8FAFC; border-radius:6px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                      <strong style="font-size:11px;">Farzana Chowdhury</strong> <span class="badge-hf badge-blue">Daughter • Priority 2</span><br>
                      <span style="font-size:9.5px; color:var(--slate-600);">Tel: 01819-XXXXXX • Alternative Contact</span>
                    </div>
                    <button class="btn-hf btn-secondary" style="padding:3px 8px; font-size:10px;">📞 Call 2nd</button>
                  </div>
                </div>
              </div>

              <div class="card-hf" style="background:#FFF1F2; border-color:#FECDD3;">
                <div class="card-header-hf" style="border-color:#FECDD3;">
                  <h4 style="color:#9F1239;">Paramedic Critical Health Brief (On Arrival)</h4>
                </div>
                <p style="font-size:10.5px; color:#881337; line-height:1.5;">
                  • <strong>Patient:</strong> Abdul Rahman Chowdhury (Age: 76 Years)<br>
                  • <strong>Blood Group:</strong> B Positive (B+)<br>
                  • <strong style="color:#E11D48; text-decoration:underline;">CRITICAL ALLERGY:</strong> PENICILLIN (Causes Anaphylaxis)<br>
                  • <strong>Key Conditions:</strong> Type 2 Diabetes, Hypertension, Coronary Stent (2021)<br>
                  • <strong>Home GPS Coordinates:</strong> 23.7461° N, 90.3742° E (Dhanmondi Road 11)
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Critical Life-Safety Protocol</h3>
        <p>In medical crises, every second counts. This screen provides massive single-touch speed dial triggers and broadcasts the senior's exact home location and vital history instantly.</p>
      </div>

      <div class="spec-card">
        <h3>Emergency Capabilities</h3>
        <ul>
          <li><strong>One-Tap Speed Dial:</strong> Direct links to National Ambulance and Hospital ER desk.</li>
          <li><strong>Paramedic Summary:</strong> Prevents lethal drug reactions (Penicillin allergy clearly flagged).</li>
          <li><strong>Automated Family Ping:</strong> Sends distress SMS with GPS pin to all relatives.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>Emergency Tokens</h3>
        <span class="token-tag">#E11D48 Vivid Red</span>
        <span class="token-tag">Speed Dial</span>
        <span class="token-tag">GPS Lat/Long</span>
      </div>
    </div>
  </div>
</div>

</body>
</html>
"""

with open("high_fidelity_design.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated high_fidelity_design.html successfully.")
