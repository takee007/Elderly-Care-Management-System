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
    gap: 6px;
    font-size: 10.5px;
  }

  .cover-index-item {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 6px;
    padding: 4.5px 8px;
    display: flex;
    align-items: center;
    gap: 7px;
    color: #CBD5E1;
  }

  .cover-index-num {
    background: #0D9488;
    color: white;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 9.5px;
    flex-shrink: 0;
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
        <p>• <strong>Senior-Centric Accessibility:</strong> WCAG AAA (≥7:1) contrast, minimum <strong>14pt (18.67px)</strong> body text on Senior UI (14px minimum across clinical portals), &amp; ≥56px touch targets.</p>
        <p>• <strong>5 Role-Isolated Portals:</strong> Dedicated interfaces for Family Members, Caregivers, Senior Residents, Physicians, and Administrators.</p>
        <p>• <strong>Zero-Error Safety &amp; SOS:</strong> Color-coded eMAR adherence, shift handoff logs, and 1-tap 999 SOS dispatch.</p>
      </div>
    </div>

    <div>
      <h3 style="font-size:11px; text-transform:uppercase; letter-spacing:1px; color:#94A3B8; margin-bottom:5px;">
        Sequenced Interface Specification (15 Pages • 12 Dedicated Screens)
      </h3>
      <div class="cover-index-grid">
        <div class="cover-index-item"><span class="cover-index-num">1</span> Design System Tokens &amp; Accessibility</div>
        <div class="cover-index-item"><span class="cover-index-num">2</span> Multi-Role Screen Flow &amp; IA</div>
        <div class="cover-index-item"><span class="cover-index-num">3</span> Screen 1: Multi-Role Authentication</div>
        <div class="cover-index-item"><span class="cover-index-num">4</span> Screen 2: Central Family Dashboard</div>
        <div class="cover-index-item"><span class="cover-index-num">5</span> Screen 3: Elderly Profile &amp; Health Record</div>
        <div class="cover-index-item"><span class="cover-index-num">6</span> Screen 4: Medicine Schedule &amp; Tracker</div>
        <div class="cover-index-item"><span class="cover-index-num">7</span> Screen 5: Add Medication Form Modal</div>
        <div class="cover-index-item"><span class="cover-index-num">8</span> Screen 6: Doctor Appointment Tracking</div>
        <div class="cover-index-item"><span class="cover-index-num">9</span> Screen 7: Daily Care Routine Checklist</div>
        <div class="cover-index-item"><span class="cover-index-num">10</span> Screen 8: Caregiver Shift Handoff Log</div>
        <div class="cover-index-item"><span class="cover-index-num">11</span> Screen 9: Instant Emergency SOS Portal</div>
        <div class="cover-index-item"><span class="cover-index-num">12</span> Screen 10: Senior Resident Dashboard</div>
        <div class="cover-index-item"><span class="cover-index-num">13</span> Screen 11: Physician EHR &amp; Consult Portal</div>
        <div class="cover-index-item"><span class="cover-index-num">14</span> Screen 12: Admin Governance &amp; Audit Logs</div>
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
          <div class="card-header-hf"><h4>Reconciled Typography Hierarchy</h4></div>
          <div style="display:flex; flex-direction:column; gap:5px; font-size:11.5px;">
            <div><span style="font-size:17px; font-weight:800;">Heading 1 (24px / 18pt)</span> — Portal &amp; Section Titles</div>
            <div><span style="font-size:14.5px; font-weight:700;">Heading 2 (20px / 15pt)</span> — Card Headers &amp; Modals</div>
            <div><span style="font-size:15px; font-weight:700; color:#0F766E;">Senior Body (14pt / 18.67px min)</span> — Accessible Senior UI</div>
            <div><span style="font-size:14px; font-weight:500; color:var(--slate-700);">Clinical Body (14px / 10.5pt min)</span> — EHR &amp; Staff Tables</div>
          </div>
        </div>

        <div class="card-hf">
          <div class="card-header-hf"><h4>Interactive Badges &amp; Buttons</h4></div>
          <div style="display:flex; flex-wrap:wrap; gap:6px; align-items:center;">
            <span class="badge-hf badge-green">✓ Dose Completed</span>
            <span class="badge-hf badge-amber">⏳ Due in 25m</span>
            <span class="badge-hf badge-red">🚨 Critical SOS</span>
            <span class="badge-hf badge-blue">🩺 Physician Review</span>
            <div style="width:100%; height:1px; background:#E2E8F0; margin:4px 0;"></div>
            <button class="btn-hf btn-primary">Primary Action</button>
            <button class="btn-hf btn-secondary">Secondary Option</button>
            <button class="btn-hf btn-danger">Emergency Dial</button>
          </div>
        </div>
      </div>

      <!-- Accessibility Guidelines Box -->
      <div class="card-hf" style="background:#F0FDFA; border-color:#99F6E4;">
        <h4 style="font-size:12px; font-weight:700; color:#0F766E; margin-bottom:4px;">Reconciled Geriatric &amp; Elderly-Friendly UX Guidelines (WCAG 2.1 AAA)</h4>
        <div class="grid-3" style="font-size:11px; color:#115E59;">
          <div>• <strong>Minimum Body Size:</strong> Strict <strong>14pt (18.67px)</strong> minimum body text in Senior Resident UI; <strong>14px</strong> minimum on dense clinical tables.</div>
          <div>• <strong>Touch Targets:</strong> Minimum <strong>48px</strong> clinical controls; <strong>56px–72px+</strong> buttons in Senior Resident UI.</div>
          <div>• <strong>Dual Encoding &amp; Contrast:</strong> ≥7:1 contrast ratio; every state pairs color + icon + text label.</div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Typography Reconciliation</h3>
        <p>Reconciles senior accessibility and clinical density under one rulebook: <strong>14pt (18.67px)</strong> minimum body floor across Senior Portal and <strong>14px</strong> minimum across clinical staff interfaces (eliminating legacy 13px copy).</p>
      </div>

      <div class="spec-card">
        <h3>Design Tokens</h3>
        <span class="token-tag">#0D9488 Brand</span>
        <span class="token-tag">#0F172A Base</span>
        <span class="token-tag">14pt / 18.67px Senior</span>
        <span class="token-tag">14px Clinical Body</span>
        <span class="token-tag">≥56px Senior Touch</span>
        <span class="token-tag">Inter / Plus Jakarta</span>
      </div>

      <div class="spec-card">
        <h3>Key Standards</h3>
        <ul>
          <li>Card-based modular layouts across 5 role portals.</li>
          <li>Real-time timestamp &amp; audit trail verification.</li>
          <li>Optimized for tablets, desktops &amp; nurse stations.</li>
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
      <div style="display:flex; flex-direction:column; gap:10px; height:100%;">
        <!-- Flow top -->
        <div style="display:flex; justify-content:center; align-items:center; gap:14px;">
          <div class="card-hf" style="width:190px; text-align:center; background:#F1F5F9; border-style:dashed; padding:7px 10px;">
            <div style="font-size:9.5px; font-weight:700; color:var(--slate-400);">SYSTEM ENTRY</div>
            <strong style="font-size:11.5px;">Elderly Care Web App</strong>
          </div>
          <div style="font-size:16px; color:var(--primary); font-weight:bold;">➔</div>
          <div class="card-hf" style="width:310px; text-align:center; border:2px solid var(--primary); padding:7px 10px;">
            <div style="font-size:9.5px; font-weight:700; color:var(--primary);">SCREEN 1: MULTI-ROLE AUTHENTICATION</div>
            <strong style="font-size:11px;">Family • Caregiver • Senior • Physician • Admin</strong>
          </div>
        </div>

        <div style="text-align:center; font-size:11.5px; color:var(--slate-400);">⬇ (Role-Based Access Control Routing)</div>

        <!-- 4 Role Hubs Row -->
        <div class="grid-4" style="gap:8px;">
          <div class="card-hf" style="text-align:center; background:linear-gradient(135deg, #0F172A, #1E293B); color:white; padding:8px;">
            <div style="font-size:9px; font-weight:700; color:#5EEAD4;">GUARDIAN HUB</div>
            <strong style="font-size:11px;">Screen 2: Family</strong>
            <p style="font-size:9px; color:#94A3B8; margin-top:2px;">Vitals, Meds, Care Notes</p>
          </div>
          <div class="card-hf" style="text-align:center; background:#FFFBEB; border:1.5px solid #F59E0B; padding:8px;">
            <div style="font-size:9px; font-weight:700; color:#B45309;">ACCESSIBLE 14PT UI</div>
            <strong style="font-size:11px; color:#78350F;">Screen 10: Senior</strong>
            <p style="font-size:9px; color:#92400E; margin-top:2px;">Large Meds, Dial, 999 SOS</p>
          </div>
          <div class="card-hf" style="text-align:center; background:#EFF6FF; border:1.5px solid #2563EB; padding:8px;">
            <div style="font-size:9px; font-weight:700; color:#1D4ED8;">CLINICAL MD EHR</div>
            <strong style="font-size:11px; color:#1E3A8A;">Screen 11: Physician</strong>
            <p style="font-size:9px; color:#1E40AF; margin-top:2px;">Records, Rx, Teleconsult</p>
          </div>
          <div class="card-hf" style="text-align:center; background:#F8FAFC; border:1.5px solid #475569; padding:8px;">
            <div style="font-size:9px; font-weight:700; color:#475569;">GOVERNANCE &amp; RBAC</div>
            <strong style="font-size:11px; color:#0F172A;">Screen 12: Admin</strong>
            <p style="font-size:9px; color:#334155; margin-top:2px;">Users, KPIs, Audit Logs</p>
          </div>
        </div>

        <div style="text-align:center; font-size:11.5px; color:var(--slate-400);">⬇ (Shared Clinical Operations Modules)</div>

        <!-- 4 Branches -->
        <div class="grid-4" style="gap:8px;">
          <div class="card-hf" style="text-align:center; padding:7px;">
            <span style="font-size:15px;">👤</span>
            <div style="font-size:10.5px; font-weight:700; color:var(--slate-800);">Screen 3: Profile</div>
            <p style="font-size:9px; color:var(--slate-600);">Medical History &amp; Allergies</p>
          </div>
          <div class="card-hf" style="text-align:center; border-color:#99F6E4; padding:7px;">
            <span style="font-size:15px;">💊</span>
            <div style="font-size:10.5px; font-weight:700; color:var(--primary-dark);">Screen 4 &amp; 5: Meds</div>
            <p style="font-size:9px; color:var(--slate-600);">eMAR &amp; Add Prescription</p>
          </div>
          <div class="card-hf" style="text-align:center; padding:7px;">
            <span style="font-size:15px;">🩺</span>
            <div style="font-size:10.5px; font-weight:700; color:var(--slate-800);">Screen 6: Visits</div>
            <p style="font-size:9px; color:var(--slate-600);">Doctor &amp; Clinic Schedule</p>
          </div>
          <div class="card-hf" style="text-align:center; padding:7px;">
            <span style="font-size:15px;">📋</span>
            <div style="font-size:10.5px; font-weight:700; color:var(--slate-800);">Screen 7: Routine</div>
            <p style="font-size:9px; color:var(--slate-600);">Meals, Hydration &amp; Checks</p>
          </div>
        </div>

        <!-- Bottom Row -->
        <div style="display:flex; justify-content:center; gap:20px; align-items:center;">
          <div class="card-hf" style="width:240px; text-align:center; padding:7px;">
            <span style="font-size:14px;">🤝</span>
            <div style="font-size:10.5px; font-weight:700;">Screen 8: Caregiver Station</div>
            <p style="font-size:9px; color:var(--slate-600);">Vitals Telemetry, eMAR &amp; Shift Notes</p>
          </div>
          <div style="font-size:16px; color:var(--rose-600); font-weight:bold;">⮂</div>
          <div class="card-hf" style="width:240px; text-align:center; background:#FFE4E6; border:1.5px solid #F43F5E; padding:7px;">
            <span style="font-size:14px;">🚨</span>
            <div style="font-size:10.5px; font-weight:700; color:#9F1239;">Screen 9: EMERGENCY SOS</div>
            <p style="font-size:9px; color:#9F1239;">999 Broadcast, ER Brief &amp; Triage</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Architecture Strategy</h3>
        <p><strong>Role-Routed Topology:</strong> Each persona lands on an interface tailored to their workflow (accessible large cards for Seniors, EHR workspaces for Physicians, governance/audit tools for Admins).</p>
      </div>

      <div class="spec-card">
        <h3>Screen Sequence</h3>
        <ul>
          <li><strong>Screen 1:</strong> 5-role auth gateway</li>
          <li><strong>Screens 2–7:</strong> Family &amp; daily care ops</li>
          <li><strong>Screens 8–9:</strong> Caregiver handoff &amp; SOS</li>
          <li><strong>Screen 10:</strong> Dedicated Senior UI (14pt)</li>
          <li><strong>Screen 11:</strong> Physician EHR &amp; teleconsult</li>
          <li><strong>Screen 12:</strong> Admin RBAC &amp; audit logs</li>
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
        <h1>03. Screen 1: Multi-Role Authentication Portal</h1>
        <p>Secure RBAC login with instant role switching across Family, Caregiver, Senior, Physician &amp; Admin portals</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 1 of 12</span>
      <span class="pill">Auth &amp; 5 Roles</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame">
      <div class="mockup-chrome">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url">https://elderlycare.portal/login</div>
        <span style="font-size:10px; color:var(--primary); font-weight:bold;">SSL 256-bit • JWT RBAC</span>
      </div>
      <div class="app-shell" style="align-items:center; justify-content:center; padding:12px; gap:14px; background:linear-gradient(135deg, #F8FAFC 0%, #EEF2F6 100%);">
        <div class="card-hf" style="width:295px; padding:16px; box-shadow:var(--shadow-lg); border-radius:12px;">
          <div style="text-align:center; margin-bottom:10px;">
            <div style="width:38px; height:38px; background:linear-gradient(135deg, #0D9488, #0F766E); border-radius:10px; margin:0 auto 6px; display:flex; align-items:center; justify-content:center; color:white; font-size:18px; font-weight:bold;">
              🩺
            </div>
            <h2 style="font-size:16px; font-weight:800; color:var(--slate-900);">Elderly Care Portal</h2>
            <p style="font-size:10.5px; color:var(--slate-600); margin-top:2px;">Role-Authorized Healthcare Access</p>
          </div>

          <div style="display:flex; flex-direction:column; gap:8px;">
            <div>
              <label style="font-size:10.5px; font-weight:700; color:var(--slate-700); display:block; margin-bottom:2px;">Institutional Email Address</label>
              <input type="text" value="nurse.fatema@probin.org.bd" style="width:100%; padding:7px 9px; border:1px solid #CBD5E1; border-radius:6px; font-size:11px; color:var(--slate-800); background:#FFFFFF;" readonly>
            </div>
            <div>
              <label style="font-size:10.5px; font-weight:700; color:var(--slate-700); display:block; margin-bottom:2px;">Password</label>
              <input type="password" value="password123" style="width:100%; padding:7px 9px; border:1px solid #CBD5E1; border-radius:6px; font-size:11px; color:var(--slate-800); background:#FFFFFF;" readonly>
            </div>
            <button class="btn-hf btn-primary" style="padding:8px; font-size:11.5px; margin-top:2px;">
              Sign In to Portal ➔
            </button>
          </div>

          <div style="margin-top:10px; padding-top:8px; border-top:1px solid var(--slate-100); text-align:center;">
            <span style="font-size:9.5px; color:var(--slate-400);">Emergency Line Always Active</span><br>
            <strong style="font-size:10.5px; color:var(--rose-600);">National 999 • Health Helpline 16263</strong>
          </div>
        </div>

        <!-- 5-Role Quick Persona Switcher -->
        <div class="card-hf" style="width:270px; padding:14px; box-shadow:var(--shadow-md); border-radius:12px;">
          <div class="card-header-hf" style="margin-bottom:6px; padding-bottom:4px;">
            <h4>5-Role Instant Portal Selector</h4>
            <span class="badge-hf badge-green">RBAC</span>
          </div>
          <div style="display:flex; flex-direction:column; gap:5px; font-size:10.5px;">
            <div style="padding:5px 8px; border-radius:6px; background:#ECFDF5; border:1px solid #6EE7B7;"><strong>👩‍⚕️ Caregiver</strong> → Telemetry &amp; eMAR</div>
            <div style="padding:5px 8px; border-radius:6px; background:#EFF6FF; border:1px solid #93C5FD;"><strong>🩺 Physician</strong> → EHR, Rx &amp; Telehealth</div>
            <div style="padding:5px 8px; border-radius:6px; background:#FFFBEB; border:1px solid #FCD34D;"><strong>👴 Senior Resident</strong> → 14pt Accessible UI</div>
            <div style="padding:5px 8px; border-radius:6px; background:#F5F3FF; border:1px solid #C4B5FD;"><strong>👨‍👩‍👧 Family Guardian</strong> → Live Monitoring</div>
            <div style="padding:5px 8px; border-radius:6px; background:#F1F5F9; border:1px solid #CBD5E1;"><strong>🛡️ Administrator</strong> → Users, RBAC &amp; Audit</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Screen Purpose</h3>
        <p>Routes all 5 clinical and resident personas into strictly isolated interfaces verified via JWT RBAC tokens.</p>
      </div>

      <div class="spec-card">
        <h3>UX Details</h3>
        <ul>
          <li><strong>5-Role Switcher:</strong> Supports Guardian, Caregiver, Senior, Physician &amp; Admin portals.</li>
          <li><strong>Accessible Entry:</strong> Minimum 48px touch targets &amp; clear contrast.</li>
          <li><strong>Emergency Access:</strong> 999 / 16263 helplines visible prior to login.</li>
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
      <span class="pill highlight">Screen 2 of 12</span>
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
      <span class="pill highlight">Screen 3 of 12</span>
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
      <span class="pill highlight">Screen 4 of 12</span>
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
      <span class="pill highlight">Screen 5 of 12</span>
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
      <span class="pill highlight">Screen 6 of 12</span>
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
      <span class="pill highlight">Screen 7 of 12</span>
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
      <span class="pill highlight">Screen 8 of 12</span>
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
                  <input type="text" placeholder="Add shift handoff note..." style="flex:1; padding:5px 8px; border:1px solid #CBD5E1; border-radius:5px; font-size:10.5px;">
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
      <span class="pill">Screen 9 of 12</span>
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

<!-- PAGE 12: SCREEN 10 - SENIOR RESIDENT DASHBOARD -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon" style="background:linear-gradient(135deg, #D97706, #B45309);">SR</div>
      <div class="page-title-group">
        <h1>12. Screen 10: Senior Resident Accessible Dashboard</h1>
        <p>WCAG AAA dedicated senior portal featuring ≥14pt (18.67px) text, large ≥56px buttons, med reminders &amp; 999 SOS</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 10 of 12</span>
      <span class="pill" style="background:#FEF3C7; color:#92400E; border-color:#FCD34D;">Senior WCAG AAA UI</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame" style="background:#0B1120; border-color:#334155;">
      <div class="mockup-chrome" style="background:#0F172A; border-color:#1E293B; color:#CBD5E1;">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url" style="background:#1E293B; border-color:#334155; color:#94A3B8;">https://elderlycare.portal/senior-ui</div>
        <span class="badge-hf" style="background:#FEF3C7; color:#92400E;">SENIOR RESIDENT MODE • 14pt+</span>
      </div>
      <div class="app-shell" style="background:#0B1120; color:#F8FAFC; flex-direction:column; padding:12px 16px; gap:10px;">
        <!-- Friendly Senior Header -->
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #1E293B; padding-bottom:8px;">
          <div>
            <div style="font-size:20px; font-weight:800; color:#FFFFFF;">Hello, Alhaj Shamsuddin Sahib!</div>
            <div style="font-size:14pt; color:#CBD5E1; line-height:1.3;">Suite 204 (Padma Wing) &bull; Nurse on Duty: <strong style="color:#34D399;">Fatema Begum (RN)</strong></div>
          </div>
          <div style="background:#1E293B; border:1px solid #334155; padding:6px 12px; border-radius:8px; text-align:right;">
            <div style="font-size:10px; color:#94A3B8; font-weight:700;">ACCESSIBILITY FLOOR</div>
            <div style="font-size:12px; color:#5EEAD4; font-weight:800;">Min Body: 14pt (18.67px)</div>
          </div>
        </div>

        <!-- Giant SOS Banner -->
        <div style="background:radial-gradient(circle at center, #7F1D1D 0%, #450A0A 100%); border:2px solid #EF4444; border-radius:12px; padding:10px 16px; display:flex; align-items:center; justify-content:space-between; gap:14px;">
          <div style="display:flex; align-items:center; gap:14px;">
            <div style="width:76px; height:76px; border-radius:50%; background:linear-gradient(135deg, #EF4444, #B91C1C); border:3px solid #FFFFFF; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:0 0 18px rgba(239,68,68,0.8); flex-shrink:0;">
              <span style="font-size:17px; font-weight:900; color:#FFFFFF; line-height:1;">HELP</span>
              <span style="font-size:9px; font-weight:700; color:#FECACA;">SOS 999</span>
            </div>
            <div>
              <div style="font-size:17px; font-weight:800; color:#FFFFFF;">Need Immediate Medical Help or Nurse Assistance?</div>
              <div style="font-size:14pt; color:#FECACA;">Tap once to alert Nurse Station &amp; Son Tanvir (5-sec cancel countdown prevents accidents).</div>
            </div>
          </div>
          <button style="background:#FFFFFF; color:#991B1B; border:none; border-radius:999px; padding:10px 16px; font-size:13px; font-weight:800; min-height:48px; white-space:nowrap;">
            ✕ 5s CANCEL GUARD
          </button>
        </div>

        <!-- Large Touch Cards Row -->
        <div style="display:grid; grid-template-columns:1.18fr 1.12fr 0.9fr; flex:1; gap:10px;">
          <!-- My Medicines Today -->
          <div style="background:#0F172A; border:2px solid #10B981; border-radius:10px; padding:10px; display:flex; flex-direction:column; gap:7px;">
            <div style="font-size:16px; font-weight:800; color:#34D399;">💊 My Medicines Today</div>
            <div style="background:#064E3B; border:1px solid #10B981; border-radius:8px; padding:8px 10px; display:flex; justify-content:space-between; align-items:center; gap:6px;">
              <div>
                <div style="font-size:14pt; font-weight:800; color:#FFFFFF; line-height:1.15;">Tab. Comet 500mg</div>
                <div style="font-size:14pt; color:#A7F3D0; line-height:1.2;">08:30 AM • Morning</div>
              </div>
              <span style="font-size:13px; color:#34D399; font-weight:800; white-space:nowrap;">✓ TAKEN</span>
            </div>
            <div style="background:#1E293B; border:1px solid #475569; border-radius:8px; padding:8px 10px; display:flex; justify-content:space-between; align-items:center; gap:6px;">
              <div>
                <div style="font-size:14pt; font-weight:800; color:#FFFFFF; line-height:1.15;">Tab. Camlosart 5/20</div>
                <div style="font-size:14pt; color:#FCD34D; line-height:1.2;">08:30 PM • Tap to mark</div>
              </div>
              <span style="padding:4px 7px; border-radius:6px; background:#F59E0B; color:#0F172A; font-size:10px; font-weight:800; white-space:nowrap;">DUE</span>
            </div>
          </div>

          <!-- Daily Schedule -->
          <div style="background:#0F172A; border:2px solid #38BDF8; border-radius:10px; padding:10px; display:flex; flex-direction:column; gap:7px;">
            <div style="font-size:16px; font-weight:800; color:#38BDF8;">📅 Today's Routine</div>
            <div style="background:#1E293B; border-left:4px solid #10B981; padding:6px 9px; border-radius:6px;">
              <div style="font-size:14pt; font-weight:700; color:#FFFFFF; line-height:1.15;">08:30 AM • Breakfast &amp; BP</div>
              <div style="font-size:14pt; color:#CBD5E1; line-height:1.2;">Tray with morning meds</div>
            </div>
            <div style="background:#1E293B; border-left:4px solid #38BDF8; padding:6px 9px; border-radius:6px;">
              <div style="font-size:14pt; font-weight:700; color:#FFFFFF; line-height:1.15;">11:00 AM • Courtyard Walk</div>
              <div style="font-size:14pt; color:#CBD5E1; line-height:1.2;">15-min gentle stretch</div>
            </div>
            <div style="background:#1E293B; border-left:4px solid #A855F7; padding:6px 9px; border-radius:6px;">
              <div style="font-size:14pt; font-weight:700; color:#FFFFFF; line-height:1.15;">03:30 PM • Video Call</div>
              <div style="font-size:14pt; color:#CBD5E1; line-height:1.2;">Call Son Tanvir</div>
            </div>
          </div>

          <!-- Giant Speed Dial Buttons -->
          <div style="background:#0F172A; border:2px solid #A855F7; border-radius:10px; padding:10px; display:flex; flex-direction:column; gap:10px;">
            <div style="font-size:16px; font-weight:800; color:#C084FC;">📞 1-Tap Speed Dial</div>
            <div style="font-size:14pt; color:#E2E8F0; line-height:1.25;">Direct audio dial with large buttons:</div>
            <div style="display:flex; flex-direction:column; gap:10px; margin-top:auto;">
              <button style="background:linear-gradient(135deg, #7C3AED, #6D28D9); color:#FFFFFF; border:none; border-radius:10px; min-height:58px; font-size:14pt; font-weight:800; cursor:pointer;">
                📞 Call Son Tanvir
              </button>
              <button style="background:linear-gradient(135deg, #0284C7, #0369A1); color:#FFFFFF; border:none; border-radius:10px; min-height:58px; font-size:14pt; font-weight:800; cursor:pointer;">
                💗 Call Duty Nurse
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Specs Sidebar -->
    <div class="specs-sidebar">
      <div class="spec-card">
        <h3>Senior Accessibility</h3>
        <p>Built exclusively for aging eyes and motor-impaired hands using WCAG AAA high-contrast dark slate surfaces and oversized action controls.</p>
      </div>

      <div class="spec-card">
        <h3>Typography &amp; Safety</h3>
        <ul>
          <li><strong>14pt (18.67px) Floor:</strong> Zero microscopic text; all body reminders scale ≥14pt.</li>
          <li><strong>Large Touch Buttons:</strong> Speed dial &amp; SOS targets exceed 56px–76px height.</li>
          <li><strong>Accidental Tap Guard:</strong> 5-second audible beep countdown before dispatching 999 SOS.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>WCAG Tokens</h3>
        <span class="token-tag">14pt / 18.67px Body</span>
        <span class="token-tag">≥56px Buttons</span>
        <span class="token-tag">7:1 Contrast</span>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 13: SCREEN 11 - PHYSICIAN PORTAL -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon" style="background:linear-gradient(135deg, #0284C7, #1D4ED8);">MD</div>
      <div class="page-title-group">
        <h1>13. Screen 11: Physician Clinical EHR &amp; Consultation Portal</h1>
        <p>Dedicated MD workspace for longitudinal EHR review, e-prescribing, allergy checks &amp; video teleconsultations</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 11 of 12</span>
      <span class="pill" style="background:#DBEAFE; color:#1E40AF; border-color:#93C5FD;">DOCTOR Role Portal</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame">
      <div class="mockup-chrome">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url">https://elderlycare.portal/physician-ehr</div>
        <span class="badge-hf badge-blue">🩺 BMDC Verified • Dr. Hasan (FCPS)</span>
      </div>
      <div class="app-shell">
        <!-- Physician Patient Queue Sidebar -->
        <div class="app-sidebar" style="width:165px;">
          <div>
            <div class="nav-header">
              <div class="nav-logo-box" style="background:#0284C7;">MD</div>
              <span style="font-size:11.5px; font-weight:800; color:white;">Physician EHR</span>
            </div>
            <div style="font-size:9.5px; text-transform:uppercase; color:#64748B; padding:2px 6px 5px; font-weight:700;">Select Resident</div>
            <div class="nav-menu">
              <div class="nav-link active" style="background:#0284C7; flex-direction:column; align-items:flex-start; gap:1px;">
                <span style="font-size:10.5px;">Shamsuddin Ahmed</span>
                <span style="font-size:8.5px; color:#BAE6FD;">BD-MRN-90210 • Suite 204</span>
              </div>
              <div class="nav-link" style="flex-direction:column; align-items:flex-start; gap:1px;">
                <span style="font-size:10.5px;">Begum Rokeya C.</span>
                <span style="font-size:8.5px; color:#64748B;">BD-MRN-90211 • Suite 108</span>
              </div>
              <div class="nav-link" style="flex-direction:column; align-items:flex-start; gap:1px;">
                <span style="font-size:10.5px;">Kazi Nurul Huda</span>
                <span style="font-size:8.5px; color:#64748B;">BD-MRN-90212 • Suite 312</span>
              </div>
              <div class="nav-link" style="flex-direction:column; align-items:flex-start; gap:1px;">
                <span style="font-size:10.5px;">Sultana Razia B.</span>
                <span style="font-size:8.5px; color:#64748B;">BD-MRN-90213 • Suite 102</span>
              </div>
            </div>
          </div>
          <div style="padding:6px; background:rgba(56,189,248,0.12); border-radius:6px; font-size:9.5px; color:#BAE6FD;">
            Active Patient Load: <strong>4 Residents</strong>
          </div>
        </div>

        <div class="app-main">
          <div class="app-topbar">
            <div>
              <span style="font-size:12px; font-weight:800; color:var(--slate-900);">Geriatric Clinical EHR Console</span>
              <span style="font-size:10.5px; color:var(--slate-600); margin-left:6px;">Prof. Dr. Syed Rafiqul Hasan, MBBS, FCPS</span>
            </div>
            <div style="display:flex; gap:6px;">
              <button class="btn-hf btn-secondary" style="padding:4px 9px; font-size:10.5px;">📅 Schedule Consult</button>
              <button class="btn-hf btn-primary" style="padding:4px 10px; font-size:10.5px;">💊 + Prescribe Medication</button>
            </div>
          </div>

          <div class="app-content" style="gap:8px;">
            <!-- EHR Banner with Drug Allergies -->
            <div class="card-hf" style="border-left:4px solid #0284C7; padding:8px 12px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <div>
                  <strong style="font-size:13px; color:var(--slate-900);">Alhaj Mohammad Shamsuddin Ahmed</strong>
                  <span style="font-size:10px; color:var(--slate-600); margin-left:6px;">MRN: BD-MRN-90210 &bull; Blood: <strong>B+</strong> &bull; DOB: 1948-02-15</span>
                </div>
                <span class="badge-hf badge-red">⚠ ALLERGY: Penicillin, Sulfa Drugs</span>
              </div>
              <div style="font-size:10.5px; color:var(--slate-700);">
                <strong>Chronic Conditions:</strong> Type 2 Diabetes Mellitus, Stage 1 Hypertension, CKD Stage 2 &nbsp;|&nbsp;
                <strong>Guardian:</strong> Tanvir Ahmed (+880 1712-889900)
              </div>
            </div>

            <!-- Vitals Log + Consultations Grid -->
            <div class="grid-2" style="flex:1;">
              <div class="card-hf" style="padding:8px 10px;">
                <div class="card-header-hf" style="margin-bottom:5px; padding-bottom:4px; gap:8px;">
                  <h4>Physiological Vitals Telemetry</h4>
                  <span class="badge-hf badge-red" style="white-space:nowrap;">1 Anomaly</span>
                </div>
                <table style="width:100%; font-size:9.5px; border-collapse:collapse;">
                  <tr style="background:#F1F5F9; text-align:left;">
                    <th style="padding:3px 5px; white-space:nowrap;">BP</th><th style="padding:3px 5px;">Pulse</th><th style="padding:3px 5px;">SpO2</th><th style="padding:3px 5px;">Glucose</th><th style="padding:3px 5px;">Status</th>
                  </tr>
                  <tr style="background:#FFF1F2; border-bottom:1px solid #E2E8F0;">
                    <td style="padding:4px 5px; white-space:nowrap;"><strong>144 / 92</strong></td><td style="white-space:nowrap; padding:4px 5px;">86 bpm</td><td style="padding:4px 5px;">95%</td><td style="white-space:nowrap; padding:4px 5px;">148 mg/dL</td>
                    <td style="padding:4px 5px;"><span class="badge-hf badge-red" style="font-size:8px; padding:1px 5px; white-space:nowrap;">Hypertensive</span></td>
                  </tr>
                  <tr style="border-bottom:1px solid #E2E8F0;">
                    <td style="padding:4px 5px; white-space:nowrap;">125 / 82</td><td style="white-space:nowrap; padding:4px 5px;">74 bpm</td><td style="padding:4px 5px;">97%</td><td style="white-space:nowrap; padding:4px 5px;">126 mg/dL</td>
                    <td style="padding:4px 5px;"><span class="badge-hf badge-green" style="font-size:8px; padding:1px 5px;">Optimal</span></td>
                  </tr>
                  <tr>
                    <td style="padding:4px 5px; white-space:nowrap;">122 / 80</td><td style="white-space:nowrap; padding:4px 5px;">72 bpm</td><td style="padding:4px 5px;">98%</td><td style="white-space:nowrap; padding:4px 5px;">112 mg/dL</td>
                    <td style="padding:4px 5px;"><span class="badge-hf badge-green" style="font-size:8px; padding:1px 5px;">Optimal</span></td>
                  </tr>
                </table>

                <div style="margin-top:8px; padding-top:6px; border-top:1px solid #E2E8F0;">
                  <div style="font-size:10.5px; font-weight:700; margin-bottom:4px;">Scheduled Consultations</div>
                  <div style="background:#EFF6FF; border:1px solid #BFDBFE; border-radius:6px; padding:6px 8px; display:flex; justify-content:space-between; align-items:center; gap:8px;">
                    <div>
                      <div style="font-size:10px; font-weight:700; color:#1E3A8A;">Video Teleconsult &bull; Tomorrow 10:30 AM</div>
                      <div style="font-size:9px; color:#1E40AF;">Glycemic &amp; BP titration (BSMMU/BIRDEM)</div>
                    </div>
                    <button class="btn-hf btn-primary" style="background:#2563EB; padding:4px 8px; font-size:9.5px; white-space:nowrap;">🎥 Launch Jitsi</button>
                  </div>
                </div>
              </div>

              <!-- Active Prescriptions + Auto eMAR Sync -->
              <div class="card-hf" style="padding:8px 10px;">
                <div class="card-header-hf" style="margin-bottom:5px; padding-bottom:4px; gap:8px;">
                  <h4>Active MD Prescriptions</h4>
                  <span style="font-size:9.5px; color:var(--primary-dark); font-weight:700; white-space:nowrap;">Auto-Syncs to eMAR ✓</span>
                </div>
                <div style="display:flex; flex-direction:column; gap:5px; font-size:10px;">
                  <div style="padding:5px 8px; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px;">
                    <div style="display:flex; justify-content:space-between;"><strong>Tab. Comet 500mg (Metformin)</strong><span class="badge-hf badge-green" style="font-size:8.5px;">500 mg</span></div>
                    <div style="color:var(--slate-600); font-size:9px;">Twice daily post-meal &bull; Schedule: 08:30, 20:30</div>
                  </div>
                  <div style="padding:5px 8px; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px;">
                    <div style="display:flex; justify-content:space-between;"><strong>Tab. Camlosart 5/20</strong><span class="badge-hf badge-green" style="font-size:8.5px;">5/20 mg</span></div>
                    <div style="color:var(--slate-600); font-size:9px;">Once daily morning &bull; Verify BP before dose</div>
                  </div>
                  <div style="padding:5px 8px; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px;">
                    <div style="display:flex; justify-content:space-between;"><strong>Tab. Rosuva 10mg</strong><span class="badge-hf badge-green" style="font-size:8.5px;">10 mg</span></div>
                    <div style="color:var(--slate-600); font-size:9px;">Once daily bedtime &bull; Schedule: 22:00</div>
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
        <h3>Clinical MD Authority</h3>
        <p>Separates physician ordering workflows from nurse execution. Doctors review longitudinal trends before issuing new prescriptions.</p>
      </div>

      <div class="spec-card">
        <h3>Physician Capabilities</h3>
        <ul>
          <li><strong>Allergy Guardrail:</strong> High-contrast drug allergy banner pinned atop EHR header.</li>
          <li><strong>Order-to-eMAR Sync:</strong> Prescribing creates timed <code>PENDING</code> slots for duty nurses.</li>
          <li><strong>Integrated Telehealth:</strong> One-click encrypted Jitsi Meet video consultation rooms.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>Clinical Tokens</h3>
        <span class="token-tag">#0284C7 Medical Blue</span>
        <span class="token-tag">EHR Timeline</span>
        <span class="token-tag">Jitsi Telehealth</span>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 14: SCREEN 12 - ADMINISTRATOR DASHBOARD -->
<div class="page">
  <div class="page-nav-bar">
    <div class="brand-badge">
      <div class="brand-logo-icon" style="background:linear-gradient(135deg, #334155, #0F172A);">AD</div>
      <div class="page-title-group">
        <h1>14. Screen 12: Administrator Governance, RBAC &amp; Audit Dashboard</h1>
        <p>Enterprise system monitoring KPIs, user lifecycle provisioning, RBAC permissions matrix &amp; HIPAA audit logs</p>
      </div>
    </div>
    <div class="meta-pills">
      <span class="pill highlight">Screen 12 of 12</span>
      <span class="pill">ADMIN Role Portal</span>
    </div>
  </div>

  <div class="screen-layout">
    <div class="mockup-frame">
      <div class="mockup-chrome">
        <div class="window-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
        <div class="mockup-url">https://elderlycare.portal/admin-governance</div>
        <span class="badge-hf badge-green">● Telemetry Socket Online</span>
      </div>
      <div class="app-shell">
        <div class="app-sidebar">
          <div>
            <div class="nav-header">
              <div class="nav-logo-box" style="background:#475569;">AD</div>
              <span style="font-size:11.5px; font-weight:800; color:white;">ECMS Admin</span>
            </div>
            <div class="nav-menu">
              <div class="nav-link active" style="background:#334155;">📈 System KPIs</div>
              <div class="nav-link">👥 User Accounts</div>
              <div class="nav-link">🔐 Role Permissions</div>
              <div class="nav-link">📜 HIPAA Audit Logs</div>
              <div class="nav-link" style="color:#FDA4AF;">🚨 SOS Dispatches</div>
            </div>
          </div>
          <div style="padding:6px; background:rgba(255,255,255,0.06); border-radius:6px; font-size:9.5px;">
            <div style="color:#94A3B8;">Director</div>
            <div style="color:#5EEAD4; font-weight:bold;">Engr. Tariqul Islam</div>
          </div>
        </div>

        <div class="app-main">
          <div class="app-topbar">
            <strong style="font-size:12px; color:var(--slate-900);">National Elderly Care Administration &amp; Audit Intelligence</strong>
            <div style="display:flex; gap:6px;">
              <button class="btn-hf btn-secondary" style="padding:4px 9px; font-size:10px;">⬇ Export Audit Trail (JSON)</button>
              <button class="btn-hf btn-primary" style="padding:4px 9px; font-size:10px;">+ Add New User</button>
            </div>
          </div>

          <div class="app-content" style="gap:8px;">
            <!-- System Monitoring KPIs -->
            <div class="grid-4">
              <div class="stat-card-hf" style="padding:6px 10px;">
                <div style="font-size:9px; color:var(--slate-400); font-weight:700;">TOTAL SENIORS</div>
                <div style="font-size:16px; font-weight:800;">4 <span style="font-size:9.5px; color:var(--emerald-600);">Active</span></div>
              </div>
              <div class="stat-card-hf" style="padding:6px 10px;">
                <div style="font-size:9px; color:var(--slate-400); font-weight:700;">VITALS TELEMETRY</div>
                <div style="font-size:16px; font-weight:800;">5 <span style="font-size:9.5px; color:var(--rose-600);">(1 Anomaly)</span></div>
              </div>
              <div class="stat-card-hf" style="padding:6px 10px;">
                <div style="font-size:9px; color:var(--slate-400); font-weight:700;">MAR ADHERENCE</div>
                <div style="font-size:16px; font-weight:800; color:var(--primary-dark);">96.4%</div>
              </div>
              <div class="stat-card-hf" style="padding:6px 10px;">
                <div style="font-size:9px; color:var(--slate-400); font-weight:700;">EMERGENCY ALERTS</div>
                <div style="font-size:16px; font-weight:800;">0 <span style="font-size:9.5px; color:var(--slate-600);">Active</span></div>
              </div>
            </div>

            <!-- RBAC Users Table + Permissions & Audit Split -->
            <div class="grid-2" style="flex:1;">
              <div class="card-hf" style="padding:8px 10px;">
                <div class="card-header-hf" style="margin-bottom:5px; padding-bottom:4px;">
                  <h4>RBAC System User Management (5 Accounts)</h4>
                </div>
                <table style="width:100%; font-size:9.2px; border-collapse:collapse;">
                  <tr style="background:#F1F5F9; text-align:left;">
                    <th style="padding:3px;">User</th><th style="padding:3px;">Role</th><th style="padding:3px;">Status</th><th style="padding:3px;">Control</th>
                  </tr>
                  <tr style="border-bottom:1px solid #E2E8F0;">
                    <td style="padding:3.5px;"><strong>Engr. Tariqul Islam</strong></td><td>ADMIN</td><td><span class="badge-hf badge-green" style="font-size:8px; padding:1px 5px;">ACTIVE</span></td><td style="color:var(--slate-400);">Current Session</td>
                  </tr>
                  <tr style="border-bottom:1px solid #E2E8F0;">
                    <td style="padding:3.5px;">Prof. Dr. S. R. Hasan</td><td>DOCTOR</td><td><span class="badge-hf badge-green" style="font-size:8px; padding:1px 5px;">ACTIVE</span></td><td><span class="badge-hf badge-red" style="font-size:8px; padding:1px 5px;">Terminate</span></td>
                  </tr>
                  <tr style="border-bottom:1px solid #E2E8F0;">
                    <td style="padding:3.5px;">Fatema Begum (RN)</td><td>CAREGIVER</td><td><span class="badge-hf badge-green" style="font-size:8px; padding:1px 5px;">ACTIVE</span></td><td><span class="badge-hf badge-red" style="font-size:8px; padding:1px 5px;">Terminate</span></td>
                  </tr>
                  <tr style="border-bottom:1px solid #E2E8F0;">
                    <td style="padding:3.5px;">Tanvir Ahmed</td><td>GUARDIAN</td><td><span class="badge-hf badge-green" style="font-size:8px; padding:1px 5px;">ACTIVE</span></td><td><span class="badge-hf badge-red" style="font-size:8px; padding:1px 5px;">Terminate</span></td>
                  </tr>
                  <tr>
                    <td style="padding:3.5px;">Shamsuddin Ahmed</td><td>SENIOR</td><td><span class="badge-hf badge-green" style="font-size:8px; padding:1px 5px;">ACTIVE</span></td><td><span class="badge-hf badge-red" style="font-size:8px; padding:1px 5px;">Terminate</span></td>
                  </tr>
                </table>
              </div>

              <div class="card-hf" style="padding:8px 10px;">
                <div class="card-header-hf" style="margin-bottom:5px; padding-bottom:4px;">
                  <h4>Role Permissions &amp; HIPAA Audit Trail</h4>
                </div>
                <table style="width:100%; font-size:8.5px; border-collapse:collapse; margin-bottom:6px;">
                  <tr style="background:#0F172A; color:white; text-align:center;">
                    <th style="padding:3px 5px; text-align:left;">Module</th><th style="padding:3px 5px;">Admin</th><th style="padding:3px 5px;">Doctor</th><th style="padding:3px 5px;">Nurse</th><th style="padding:3px 5px;">Senior</th><th style="padding:3px 5px;">Family</th>
                  </tr>
                  <tr style="border-bottom:1px solid #E2E8F0; text-align:center;">
                    <td style="padding:3px 5px; text-align:left;">EHR / Prescribe</td><td>✓</td><td>✓</td><td>MAR Only</td><td>Self View</td><td>Monitor</td>
                  </tr>
                  <tr style="border-bottom:1px solid #E2E8F0; text-align:center;">
                    <td style="padding:3px 5px; text-align:left;">Users / Audit Log</td><td>✓ Full</td><td>—</td><td>—</td><td>—</td><td>—</td>
                  </tr>
                </table>
                <div style="font-size:9px; display:flex; flex-direction:column; gap:3px;">
                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:4px; padding:3px 6px;"><strong>USER_LOGIN:</strong> dr.hasan@probin.org.bd &bull; Authenticated via JWT</div>
                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:4px; padding:3px 6px;"><strong>VITALS_RECORDED:</strong> Fatema Begum &bull; Anomaly Flagged (144/92)</div>
                  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:4px; padding:3px 6px;"><strong>SOS_RESOLVED:</strong> Emergency #1 closed with clinical note</div>
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
        <h3>Governance &amp; Security</h3>
        <p>Enforces strict RBAC least-privilege isolation, account lifecycle termination/reactivation, and immutable compliance auditing.</p>
      </div>

      <div class="spec-card">
        <h3>Admin Capabilities</h3>
        <ul>
          <li><strong>System Monitoring:</strong> Real-time resident census, vitals anomalies &amp; MAR rate.</li>
          <li><strong>Self-Lockout Guard:</strong> Admin cannot terminate their own active session.</li>
          <li><strong>Audit Export:</strong> One-click downloadable HIPAA JSON compliance trail.</li>
        </ul>
      </div>

      <div class="spec-card">
        <h3>Governance Tokens</h3>
        <span class="token-tag">JWT RBAC</span>
        <span class="token-tag">Audit JSON</span>
        <span class="token-tag">System KPIs</span>
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

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if os.path.exists(chrome_path):
    pdf_path = os.path.abspath("Elderly_Care_Management_System_High_Fidelity_Design.pdf")
    html_url = "file:///" + os.path.abspath("high_fidelity_design.html").replace("\\", "/")
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--virtual-time-budget=8000",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_url,
    ]
    subprocess.run(cmd, check=True, timeout=60)
    print(f"Generated {pdf_path} successfully.")
