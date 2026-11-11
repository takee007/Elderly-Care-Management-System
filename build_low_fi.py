"""
Generate Low-Fidelity Paper Wireframe PDF for Elderly Care Management System
Student: Farzana Sadia Takee (ID: 2211175)
"""
import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Elderly Care Management System - Low Fidelity Design</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Patrick+Hand&family=Inter:wght@400;600;700&family=Caveat:wght@600;700&display=swap');

  @page {
    size: A4 landscape;
    margin: 0;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Patrick Hand', 'Architects Daughter', cursive, sans-serif;
    color: #2D3748;
    background: #F4EFEA;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .page {
    width: 297mm;
    height: 210mm;
    page-break-after: always;
    position: relative;
    padding: 12mm 15mm;
    background-color: #FAF7F2;
    background-image: 
      linear-gradient(#E8E1D5 1px, transparent 1px),
      linear-gradient(90deg, #E8E1D5 1px, transparent 1px);
    background-size: 20px 20px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }

  /* Paper styling elements */
  .paper-tape {
    position: absolute;
    top: 8px;
    left: 45%;
    width: 110px;
    height: 24px;
    background: rgba(230, 215, 175, 0.7);
    transform: rotate(-1.5deg);
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    border-left: 2px dashed rgba(180, 160, 120, 0.5);
    border-right: 2px dashed rgba(180, 160, 120, 0.5);
    z-index: 10;
  }

  .page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px dashed #718096;
    padding-bottom: 6px;
    margin-bottom: 10px;
  }

  .page-title-box h1 {
    font-size: 22px;
    color: #1A202C;
    letter-spacing: 0.5px;
  }

  .page-title-box p {
    font-size: 13px;
    color: #4A5568;
    font-family: 'Inter', sans-serif;
  }

  .meta-tag {
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    background: #EDF2F7;
    border: 1.5px solid #CBD5E0;
    padding: 4px 10px;
    border-radius: 6px;
    font-weight: 600;
  }

  /* Canvas area for paper wireframe */
  .wireframe-container {
    flex: 1;
    display: grid;
    grid-template-columns: 1fr 260px;
    gap: 16px;
    height: calc(100% - 60px);
  }

  .wireframe-viewport {
    border: 2.5px solid #2D3748;
    border-radius: 8px;
    background: #FFFFFF;
    box-shadow: 4px 4px 0px rgba(45, 55, 72, 0.2);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  /* Browser / App Header bar */
  .app-topbar {
    height: 38px;
    background: #F7FAFC;
    border-bottom: 2px solid #2D3748;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 14px;
    font-size: 13px;
    font-weight: bold;
  }

  .window-dots {
    display: flex;
    gap: 5px;
  }

  .dot {
    width: 9px;
    height: 9px;
    border: 1.5px solid #4A5568;
    border-radius: 50%;
  }

  .app-body {
    flex: 1;
    display: flex;
    background: #FFFFFF;
    overflow: hidden;
  }

  /* Sidebar */
  .sketch-sidebar {
    width: 140px;
    border-right: 2px solid #2D3748;
    background: #F7FAFC;
    padding: 10px 8px;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .sketch-nav-item {
    padding: 5px 8px;
    border: 1.5px solid #A0AEC0;
    border-radius: 4px;
    font-size: 12px;
    background: #FFFFFF;
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .sketch-nav-item.active {
    background: #2D3748;
    color: #FFFFFF;
    border-color: #2D3748;
  }

  .sketch-content {
    flex: 1;
    padding: 12px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    gap: 10px;
    background: #FFFFFF;
  }

  /* Wireframe elements */
  .sketch-box {
    border: 2px solid #4A5568;
    border-radius: 6px;
    padding: 8px;
    background: #FFFFFF;
  }

  .placeholder-img {
    border: 1.5px dashed #718096;
    background: #F7FAFC;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    color: #718096;
  }

  .placeholder-img::before, .placeholder-img::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(to top right, transparent calc(50% - 1px), #CBD5E0, transparent calc(50% + 1px));
  }
  .placeholder-img::after {
    background: linear-gradient(to bottom right, transparent calc(50% - 1px), #CBD5E0, transparent calc(50% + 1px));
  }

  .sketch-btn {
    border: 2px solid #2D3748;
    background: #EDF2F7;
    padding: 5px 12px;
    border-radius: 5px;
    font-size: 12px;
    font-weight: bold;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    box-shadow: 2px 2px 0px #2D3748;
  }

  .sketch-btn.primary {
    background: #2D3748;
    color: #FFFFFF;
  }

  .sketch-btn.danger {
    background: #FEB2B2;
    border-color: #9B2C2C;
    color: #742A2A;
  }

  .sketch-input {
    border: 2px solid #718096;
    border-radius: 4px;
    padding: 5px 8px;
    font-size: 12px;
    background: #FFFFFF;
    color: #4A5568;
  }

  /* Annotation panel */
  .notes-panel {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .sticky-note {
    background: #FEFCBF;
    border: 1.5px solid #D69E2E;
    box-shadow: 3px 3px 6px rgba(0,0,0,0.08);
    border-radius: 4px;
    padding: 10px;
    transform: rotate(0.8deg);
  }

  .sticky-note.blue {
    background: #BEE3F8;
    border-color: #3182CE;
    transform: rotate(-0.8deg);
  }

  .sticky-note.green {
    background: #C6F6D5;
    border-color: #38A169;
  }

  .sticky-note h4 {
    font-size: 13px;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    margin-bottom: 4px;
    border-bottom: 1px dashed rgba(0,0,0,0.2);
    padding-bottom: 2px;
  }

  .sticky-note ul {
    list-style: none;
    padding: 0;
    font-size: 12px;
  }

  .sticky-note li {
    margin-bottom: 4px;
    position: relative;
    padding-left: 12px;
  }

  .sticky-note li::before {
    content: "•";
    position: absolute;
    left: 0;
    font-weight: bold;
  }

  /* Cover Page Styling */
  .cover-card {
    flex: 1;
    border: 3px solid #2D3748;
    border-radius: 12px;
    background: #FFFFFF;
    box-shadow: 8px 8px 0px rgba(45, 55, 72, 0.25);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 30px 40px;
    position: relative;
  }

  .cover-badge {
    position: absolute;
    top: 20px;
    right: 30px;
    background: #FEEBC8;
    border: 2px solid #C05621;
    color: #7B341E;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    font-size: 13px;
    padding: 6px 14px;
    border-radius: 20px;
    transform: rotate(2deg);
  }

  .cover-title {
    font-size: 38px;
    color: #1A202C;
    margin-bottom: 6px;
    line-height: 1.1;
  }

  .cover-subtitle {
    font-size: 20px;
    color: #4A5568;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
  }

  .info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin: 20px 0;
  }

  .info-box {
    border: 2px dashed #718096;
    border-radius: 8px;
    padding: 14px 18px;
    background: #F7FAFC;
  }

  .info-box h3 {
    font-size: 14px;
    font-family: 'Inter', sans-serif;
    color: #2D3748;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
  }

  .info-box p {
    font-size: 15px;
    color: #1A202C;
    line-height: 1.4;
  }

  .index-list {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
    margin-top: 10px;
    font-family: 'Inter', sans-serif;
    font-size: 12px;
  }

  .index-item {
    border: 1.5px solid #CBD5E0;
    border-radius: 6px;
    padding: 6px 10px;
    background: #FFFFFF;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .index-num {
    background: #2D3748;
    color: #FFFFFF;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    font-weight: bold;
  }

  /* Grid layout utils for screens */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 8px;
  }
  .grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 6px;
  }

  .card-header-sm {
    font-size: 12px;
    font-weight: bold;
    border-bottom: 1.5px dashed #CBD5E0;
    padding-bottom: 3px;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
  }

  .item-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 4px 6px;
    border-bottom: 1px solid #E2E8F0;
    font-size: 11px;
  }

  .badge-sketch {
    display: inline-block;
    padding: 2px 6px;
    border: 1px solid #718096;
    border-radius: 10px;
    font-size: 10px;
  }

  .badge-sketch.green { background: #C6F6D5; border-color: #276749; color: #22543D; }
  .badge-sketch.yellow { background: #FEFCBF; border-color: #B7791F; color: #744210; }
  .badge-sketch.red { background: #FED7D7; border-color: #9B2C2C; color: #742A2A; }

  /* Flow chart elements */
  .flow-diagram {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 10px;
    height: 100%;
  }

  .flow-row {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
  }

  .flow-card {
    border: 2px solid #2D3748;
    background: #FFFFFF;
    border-radius: 8px;
    padding: 10px 16px;
    text-align: center;
    box-shadow: 3px 3px 0px rgba(0,0,0,0.15);
    min-width: 140px;
  }

  .flow-arrow {
    font-size: 20px;
    font-weight: bold;
    color: #4A5568;
  }
</style>
</head>
<body>

<!-- PAGE 0: COVER & TITLE -->
<div class="page">
  <div class="paper-tape"></div>
  <div class="cover-card">
    <div>
      <h1 class="cover-title">Elderly Care Management System</h1>
      <p class="cover-subtitle">Low-Fidelity Paper Wireframe & Prototype Design Specification</p>
    </div>

    <div class="info-grid">
      <div class="info-box">
        <h3>Student Details</h3>
        <p><strong>Name:</strong> Farzana Sadia Takee</p>
        <p><strong>Student ID:</strong> 2211175</p>
        <p><strong>Course Project:</strong> Elderly Care Management System</p>
        <p><strong>Submission Type:</strong> Paper Wireframe / Low-Fidelity Design</p>
      </div>
      <div class="info-box">
        <h3>Design Philosophy</h3>
        <p>• <strong>Senior-Centric Usability:</strong> High contrast, large click targets, clear visual hierarchy.</p>
        <p>• <strong>Dual-Role Architecture:</strong> Seamless handoff between Family Members and Caregivers.</p>
        <p>• <strong>Safety First:</strong> Instant one-touch SOS and prominent medication alerts.</p>
      </div>
    </div>

    <div>
      <h3 style="font-family:'Inter',sans-serif; font-size:13px; text-transform:uppercase; color:#4A5568; margin-bottom:8px;">
        Sequenced Interface Index (1 Screen Per Page)
      </h3>
      <div class="index-list">
        <div class="index-item"><span class="index-num">1</span> Screen Flow & Sitemap Architecture</div>
        <div class="index-item"><span class="index-num">2</span> Landing & Role Authentication</div>
        <div class="index-item"><span class="index-num">3</span> Family Member Dashboard</div>
        <div class="index-item"><span class="index-num">4</span> Elderly Profile & Medical Details</div>
        <div class="index-item"><span class="index-num">5</span> Medicine Schedule & Tracker</div>
        <div class="index-item"><span class="index-num">6</span> Add / Edit Medication Form</div>
        <div class="index-item"><span class="index-num">7</span> Doctor Appointment Tracking</div>
        <div class="index-item"><span class="index-num">8</span> Daily Care Routine Checklist</div>
        <div class="index-item"><span class="index-num">9</span> Caregiver Info & Duty Notes</div>
        <div class="index-item"><span class="index-num">10</span> Emergency SOS Directory</div>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 1: ARCHITECTURE & SEQUENCE FLOW -->
<div class="page">
  <div class="paper-tape"></div>
  <div class="page-header">
    <div class="page-title-box">
      <h1>01. Navigation Flow & System Architecture</h1>
      <p>Hierarchical map showing user navigation and screen transition sequence</p>
    </div>
    <div class="meta-tag">Sequence Map</div>
  </div>

  <div class="wireframe-container">
    <div class="wireframe-viewport" style="padding: 16px; background:#FAFAFA;">
      <div class="flow-diagram">
        <div class="flow-row">
          <div class="flow-card" style="background:#E2E8F0;">
            <strong>[Start] Entry Point</strong><br>
            <span style="font-size:12px;">Web Application URL</span>
          </div>
          <div class="flow-arrow">➔</div>
          <div class="flow-card" style="border-style:dashed;">
            <strong>Screen 1: Landing & Login</strong><br>
            <span style="font-size:11px;">Role Select (Family / Caregiver)</span>
          </div>
        </div>

        <div style="text-align:center; font-size:18px;">⬇ (Authenticated Session)</div>

        <div class="flow-row">
          <div class="flow-card" style="background:#FEFCBF; border-width:3px;">
            <strong>Screen 2: Central Dashboard</strong><br>
            <span style="font-size:11px;">Elderly Status, Quick Stats & Alerts</span>
          </div>
        </div>

        <div style="text-align:center; font-size:18px;">⬇ (Navigation Menu Options)</div>

        <div class="grid-4" style="gap:10px;">
          <div class="flow-card">
            <strong>Screen 3</strong><br>
            <span style="font-size:11px;">Elderly Profile & Medical Records</span>
          </div>
          <div class="flow-card">
            <strong>Screen 4 & 5</strong><br>
            <span style="font-size:11px;">Medicine Tracker & Add Meds</span>
          </div>
          <div class="flow-card">
            <strong>Screen 6</strong><br>
            <span style="font-size:11px;">Doctor Appointment Tracking</span>
          </div>
          <div class="flow-card">
            <strong>Screen 7</strong><br>
            <span style="font-size:11px;">Daily Care Schedule Checklist</span>
          </div>
        </div>

        <div class="flow-row" style="margin-top:8px;">
          <div class="flow-card">
            <strong>Screen 8</strong><br>
            <span style="font-size:11px;">Caregiver Info & Shift Handoff</span>
          </div>
          <div class="flow-arrow">⮂</div>
          <div class="flow-card" style="background:#FED7D7; border-color:#9B2C2C;">
            <strong>Screen 9: EMERGENCY SOS</strong><br>
            <span style="font-size:11px;">One-Touch Call & Hospital Directory</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Notes Panel -->
    <div class="notes-panel">
      <div class="sticky-note">
        <h4>User Flow Rationale</h4>
        <ul>
          <li><strong>Zero Friction Login:</strong> Family members and caregivers can immediately switch roles.</li>
          <li><strong>Hub & Spoke Model:</strong> The Dashboard acts as the central command hub.</li>
          <li><strong>Persistent SOS:</strong> Emergency trigger accessible from every single screen.</li>
        </ul>
      </div>
      <div class="sticky-note blue">
        <h4>Target Personas</h4>
        <ul>
          <li><strong>Primary:</strong> Family Member (Son/Daughter) managing parent's care remotely.</li>
          <li><strong>Secondary:</strong> Daily In-Home Caregiver executing medication & meal schedules.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 2: SCREEN 1 - LOGIN / ROLE SELECTION -->
<div class="page">
  <div class="paper-tape"></div>
  <div class="page-header">
    <div class="page-title-box">
      <h1>02. Screen 1: Landing & Role-Based Login</h1>
      <p>Clean authentication portal with dual-role selector for Family and Caregiver</p>
    </div>
    <div class="meta-tag">Screen 1 of 9</div>
  </div>

  <div class="wireframe-container">
    <div class="wireframe-viewport">
      <div class="app-topbar">
        <div class="window-dots"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
        <span>Elderly Care Portal • Secure Access</span>
        <span>v1.0 (Low-Fi)</span>
      </div>
      <div class="app-body" style="align-items:center; justify-content:center; padding: 25px;">
        <div class="sketch-box" style="width: 360px; text-align:center; padding: 20px;">
          <div class="placeholder-img" style="width: 50px; height: 50px; margin: 0 auto 10px; border-radius:50%;">Logo</div>
          <h2 style="font-size:18px; margin-bottom:4px;">Elderly Care Management</h2>
          <p style="font-size:11px; color:#718096; margin-bottom:14px;">Sign in to monitor & manage elderly care routines</p>
          
          <div style="display:flex; justify-content:center; gap:8px; margin-bottom:14px;">
            <div class="sketch-btn primary" style="font-size:11px; padding:4px 10px;">Family Member</div>
            <div class="sketch-btn" style="font-size:11px; padding:4px 10px;">Caregiver Staff</div>
          </div>

          <div style="display:flex; flex-direction:column; gap:8px; text-align:left;">
            <div>
              <label style="font-size:11px; font-weight:bold;">Email / Phone Number:</label>
              <div class="sketch-input">[ user@familycare.org | ]</div>
            </div>
            <div>
              <label style="font-size:11px; font-weight:bold;">Password:</label>
              <div class="sketch-input">[ •••••••••••• ]</div>
            </div>
            <div style="display:flex; justify-content:space-between; font-size:11px; margin-top:2px;">
              <span>[X] Remember Me</span>
              <span style="text-decoration:underline; cursor:pointer;">Forgot Password?</span>
            </div>
            <div class="sketch-btn primary" style="margin-top:8px; padding:8px;">Sign In to Dashboard ➔</div>
          </div>
          <div style="margin-top:12px; font-size:11px; border-top:1px dashed #CBD5E0; padding-top:8px;">
            Need help? Emergency Hotline: <strong>999 / 911</strong>
          </div>
        </div>
      </div>
    </div>

    <div class="notes-panel">
      <div class="sticky-note">
        <h4>UI Wireframe Notes</h4>
        <ul>
          <li><strong>Role Toggle:</strong> Instantly switches permissions (View/Edit rights vs Care Log updates).</li>
          <li><strong>High Accessibility:</strong> Large input boxes for easy typing on touchpads or tablets.</li>
          <li><strong>Quick Recovery:</strong> Password reset and emergency support numbers clearly visible.</li>
        </ul>
      </div>
      <div class="sticky-note green">
        <h4>User Actions</h4>
        <ul>
          <li>Select user role.</li>
          <li>Enter credentials.</li>
          <li>Auto-route to Family Member Dashboard on submit.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 3: SCREEN 2 - FAMILY MEMBER DASHBOARD -->
<div class="page">
  <div class="paper-tape"></div>
  <div class="page-header">
    <div class="page-title-box">
      <h1>03. Screen 2: Family Member Central Dashboard</h1>
      <p>High-level overview: active patient vitals, upcoming meds, care schedule, and rapid SOS</p>
    </div>
    <div class="meta-tag">Screen 2 of 9</div>
  </div>

  <div class="wireframe-container">
    <div class="wireframe-viewport">
      <div class="app-topbar">
        <div style="display:flex; align-items:center; gap:8px;">
          <div class="window-dots"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
          <strong>ElderlyCare OS</strong>
        </div>
        <div style="font-size:11px;">Active Senior: <strong>Abdul Rahman (Age: 76)</strong></div>
        <div class="sketch-btn danger" style="padding:2px 8px; font-size:10px;">🚨 QUICK SOS</div>
      </div>
      <div class="app-body">
        <div class="sketch-sidebar">
          <div class="sketch-nav-item active">📊 Dashboard</div>
          <div class="sketch-nav-item">👤 Profile</div>
          <div class="sketch-nav-item">💊 Medicine</div>
          <div class="sketch-nav-item">🩺 Doctors</div>
          <div class="sketch-nav-item">📋 Daily Care</div>
          <div class="sketch-nav-item">🤝 Caregivers</div>
          <div class="sketch-nav-item">📞 Emergency</div>
        </div>
        <div class="sketch-content">
          <!-- Top alert banner -->
          <div class="sketch-box" style="background:#FEFCBF; border-color:#D69E2E; padding:6px 10px; display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:11px;">⚠️ <strong>Next Dose Due in 25 Mins:</strong> Atorvastatin 20mg (After Lunch)</span>
            <div class="sketch-btn" style="padding:2px 6px; font-size:10px;">Mark Taken</div>
          </div>

          <!-- Quick stats row -->
          <div class="grid-4">
            <div class="sketch-box" style="text-align:center;">
              <span style="font-size:10px; color:#718096;">Blood Pressure</span>
              <div style="font-size:16px; font-weight:bold;">124 / 82</div>
              <span class="badge-sketch green">Normal</span>
            </div>
            <div class="sketch-box" style="text-align:center;">
              <span style="font-size:10px; color:#718096;">Meds Today</span>
              <div style="font-size:16px; font-weight:bold;">3 of 5 Taken</div>
              <span class="badge-sketch yellow">60% Done</span>
            </div>
            <div class="sketch-box" style="text-align:center;">
              <span style="font-size:10px; color:#718096;">Next Appointment</span>
              <div style="font-size:14px; font-weight:bold;">Tomorrow 10 AM</div>
              <span style="font-size:10px;">Dr. Hasan (Cardio)</span>
            </div>
            <div class="sketch-box" style="text-align:center;">
              <span style="font-size:10px; color:#718096;">Assigned Caregiver</span>
              <div style="font-size:14px; font-weight:bold;">Nasreen Akhtar</div>
              <span class="badge-sketch green">On Shift Now</span>
            </div>
          </div>

          <!-- Main content split -->
          <div class="grid-2" style="flex:1;">
            <!-- Today's Schedule -->
            <div class="sketch-box" style="display:flex; flex-direction:column;">
              <div class="card-header-sm">
                <span>Today's Care Schedule (Sunday)</span>
                <span style="font-size:10px; text-decoration:underline;">View All</span>
              </div>
              <div class="item-row">
                <span>[X] 08:00 AM • Morning Walk & Breathing Exercise</span>
                <span class="badge-sketch green">Completed</span>
              </div>
              <div class="item-row">
                <span>[X] 08:45 AM • Breakfast & Morning Medications</span>
                <span class="badge-sketch green">Completed</span>
              </div>
              <div class="item-row" style="background:#FEFCBF;">
                <span>[ ] 01:30 PM • Lunch & Heart Medicine Dose</span>
                <span class="badge-sketch yellow">Pending</span>
              </div>
              <div class="item-row">
                <span>[ ] 05:00 PM • Evening Blood Sugar Check</span>
                <span class="badge-sketch">Upcoming</span>
              </div>
            </div>

            <!-- Doctor & Urgent notices -->
            <div class="sketch-box" style="display:flex; flex-direction:column;">
              <div class="card-header-sm">
                <span>Doctor Consultation & Caregiver Log</span>
                <span class="sketch-btn" style="padding:1px 6px; font-size:10px;">+ Note</span>
              </div>
              <div style="font-size:11px; padding:6px; border:1px solid #E2E8F0; border-radius:4px; margin-bottom:6px;">
                <strong>Latest Caregiver Update (11:20 AM):</strong><br>
                "Patient had good appetite during breakfast. Completed 15 min light walking in garden."
              </div>
              <div style="font-size:11px; padding:6px; border:1px solid #E2E8F0; border-radius:4px;">
                <strong>Upcoming Doctor Visit:</strong><br>
                Routine Cardiology Checkup at Square Hospital. Transport arranged by son.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="notes-panel">
      <div class="sticky-note">
        <h4>Dashboard UX Highlights</h4>
        <ul>
          <li><strong>One-Glance Digest:</strong> Family members immediately see if any medication is missed.</li>
          <li><strong>Vitals Cards:</strong> Shows latest BP, blood sugar, and caregiver shift status.</li>
          <li><strong>Red SOS Button:</strong> Positioned in header on every page for extreme emergencies.</li>
        </ul>
      </div>
      <div class="sticky-note blue">
        <h4>Key Interactions</h4>
        <ul>
          <li>Click 'Mark Taken' to record medication adherence.</li>
          <li>Click any nav item to jump to dedicated module.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 4: SCREEN 3 - ELDERLY PROFILE -->
<div class="page">
  <div class="paper-tape"></div>
  <div class="page-header">
    <div class="page-title-box">
      <h1>04. Screen 3: Elderly Profile & Medical History</h1>
      <p>Comprehensive profile: personal data, chronic illnesses, blood group, allergies, and doctors</p>
    </div>
    <div class="meta-tag">Screen 3 of 9</div>
  </div>

  <div class="wireframe-container">
    <div class="wireframe-viewport">
      <div class="app-topbar">
        <div><strong>ElderlyCare OS</strong> &gt; Elderly Profile</div>
        <div class="sketch-btn" style="padding:2px 8px; font-size:10px;">✎ Edit Profile</div>
      </div>
      <div class="app-body">
        <div class="sketch-sidebar">
          <div class="sketch-nav-item">📊 Dashboard</div>
          <div class="sketch-nav-item active">👤 Profile</div>
          <div class="sketch-nav-item">💊 Medicine</div>
          <div class="sketch-nav-item">🩺 Doctors</div>
          <div class="sketch-nav-item">📋 Daily Care</div>
          <div class="sketch-nav-item">🤝 Caregivers</div>
          <div class="sketch-nav-item">📞 Emergency</div>
        </div>
        <div class="sketch-content">
          <!-- Profile header box -->
          <div class="sketch-box" style="display:flex; gap:12px; align-items:center;">
            <div class="placeholder-img" style="width:70px; height:70px; border-radius:6px;">Photo</div>
            <div style="flex:1;">
              <h2 style="font-size:16px;">Abdul Rahman Chowdhury</h2>
              <div style="font-size:11px; color:#4A5568;">Age: 76 Years • Male • DOB: 14 Aug 1950 • Blood Group: <strong>B Positive (B+)</strong></div>
              <div style="font-size:11px; margin-top:4px;">Home Address: House 42, Road 11, Dhanmondi, Dhaka</div>
            </div>
            <div style="text-align:right;">
              <span class="badge-sketch red" style="font-weight:bold;">Allergy: Penicillin</span><br>
              <span class="badge-sketch yellow" style="margin-top:4px;">Mobility: Needs Cane</span>
            </div>
          </div>

          <!-- Medical records grid -->
          <div class="grid-3" style="flex:1;">
            <div class="sketch-box">
              <div class="card-header-sm">Chronic Conditions</div>
              <div class="item-row"><span>• Type-2 Diabetes</span> <span class="badge-sketch">Since 2012</span></div>
              <div class="item-row"><span>• Hypertension (High BP)</span> <span class="badge-sketch">Since 2015</span></div>
              <div class="item-row"><span>• Mild Osteoarthritis</span> <span class="badge-sketch">Knee Joint</span></div>
              <div class="item-row"><span>• Cataract (Post-Op)</span> <span class="badge-sketch">Both Eyes</span></div>
            </div>

            <div class="sketch-box">
              <div class="card-header-sm">Primary Healthcare Contacts</div>
              <div class="item-row">
                <div><strong>Dr. K. M. Hasan</strong><br><span style="font-size:10px;">Cardiologist, Square Hosp</span></div>
                <div class="sketch-btn" style="padding:2px 5px; font-size:10px;">📞 Call</div>
              </div>
              <div class="item-row">
                <div><strong>Dr. Nusrat Jahan</strong><br><span style="font-size:10px;">Endocrinologist (Diabetes)</span></div>
                <div class="sketch-btn" style="padding:2px 5px; font-size:10px;">📞 Call</div>
              </div>
              <div class="item-row">
                <div><strong>Square Hospital Helpline</strong><br><span style="font-size:10px;">Emergency Desk</span></div>
                <div class="sketch-btn danger" style="padding:2px 5px; font-size:10px;">🚨 SOS</div>
              </div>
            </div>

            <div class="sketch-box">
              <div class="card-header-sm">Special Care Directives</div>
              <p style="font-size:11px; line-height:1.4;">
                • Low-sodium diet mandatory.<br>
                • Hydration check every 2 hours.<br>
                • Keep walking stick beside bed at all times.<br>
                • Emergency contact son Tariq (01711-XXXXXX) if BP &gt; 150/95.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="notes-panel">
      <div class="sticky-note">
        <h4>Design Considerations</h4>
        <ul>
          <li><strong>Critical Health Flags:</strong> Blood group and Penicillin allergy stand out prominently.</li>
          <li><strong>Care Directives:</strong> Clear instructions for newly arriving or rotating caregivers.</li>
          <li><strong>Quick Call Actions:</strong> Fast dial buttons for primary treating physicians.</li>
        </ul>
      </div>
      <div class="sticky-note blue">
        <h4>Data Handled</h4>
        <ul>
          <li>Demographic & address details</li>
          <li>Medical conditions history</li>
          <li>Physician association records</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 5: SCREEN 4 - MEDICINE SCHEDULE & TRACKER -->
<div class="page">
  <div class="paper-tape"></div>
  <div class="page-header">
    <div class="page-title-box">
      <h1>05. Screen 4: Medicine Schedule & Reminders</h1>
      <p>Daily medication timeline categorized by Morning, Afternoon, Evening, and Bedtime</p>
    </div>
    <div class="meta-tag">Screen 4 of 9</div>
  </div>

  <div class="wireframe-container">
    <div class="wireframe-viewport">
      <div class="app-topbar">
        <div><strong>ElderlyCare OS</strong> &gt; Medicine Schedule & Tracker</div>
        <div class="sketch-btn primary" style="padding:3px 10px; font-size:10px;">+ Add New Medicine</div>
      </div>
      <div class="app-body">
        <div class="sketch-sidebar">
          <div class="sketch-nav-item">📊 Dashboard</div>
          <div class="sketch-nav-item">👤 Profile</div>
          <div class="sketch-nav-item active">💊 Medicine</div>
          <div class="sketch-nav-item">🩺 Doctors</div>
          <div class="sketch-nav-item">📋 Daily Care</div>
          <div class="sketch-nav-item">🤝 Caregivers</div>
          <div class="sketch-nav-item">📞 Emergency</div>
        </div>
        <div class="sketch-content">
          <!-- Filter tabs -->
          <div style="display:flex; gap:8px; border-bottom:1.5px solid #CBD5E0; padding-bottom:6px;">
            <div class="sketch-btn primary" style="padding:2px 8px; font-size:11px;">Today's Schedule (Oct 4)</div>
            <div class="sketch-btn" style="padding:2px 8px; font-size:11px;">All Prescriptions (8)</div>
            <div class="sketch-btn" style="padding:2px 8px; font-size:11px;">Refill Needed (2)</div>
          </div>

          <!-- Schedule timeline cards -->
          <div style="display:flex; flex-direction:column; gap:8px; overflow:hidden;">
            <!-- Morning Slot -->
            <div class="sketch-box" style="padding:6px 10px;">
              <div class="card-header-sm">
                <span>🌅 MORNING (08:00 AM - 09:00 AM) • 2 Medicines</span>
                <span class="badge-sketch green">All Taken (Verified by Nasreen)</span>
              </div>
              <div class="grid-2">
                <div class="item-row" style="background:#F0FFF4;">
                  <div><strong>Metformin 500mg</strong> (1 Tablet - With Breakfast)<br><span style="font-size:10px; color:#718096;">For Diabetes • Prescribed by Dr. Nusrat</span></div>
                  <span class="badge-sketch green">✓ Taken 08:35 AM</span>
                </div>
                <div class="item-row" style="background:#F0FFF4;">
                  <div><strong>Amlodipine 5mg</strong> (1 Tablet - After Breakfast)<br><span style="font-size:10px; color:#718096;">For Blood Pressure • Prescribed by Dr. Hasan</span></div>
                  <span class="badge-sketch green">✓ Taken 08:35 AM</span>
                </div>
              </div>
            </div>

            <!-- Afternoon Slot -->
            <div class="sketch-box" style="padding:6px 10px; border-color:#D69E2E; background:#FFFFF0;">
              <div class="card-header-sm">
                <span>☀️ AFTERNOON (01:30 PM - 02:00 PM) • 1 Medicine</span>
                <span class="badge-sketch yellow">Due in 25 Minutes</span>
              </div>
              <div class="item-row" style="background:#FFFFFF;">
                <div>
                  <strong>Atorvastatin 20mg</strong> (1 Tablet - After Lunch)<br>
                  <span style="font-size:10px; color:#718096;">Cholesterol Management • Prescribed by Dr. Hasan</span>
                </div>
                <div style="display:flex; gap:6px;">
                  <div class="sketch-btn primary" style="padding:3px 8px; font-size:10px;">Mark as Taken</div>
                  <div class="sketch-btn" style="padding:3px 6px; font-size:10px;">Snooze 15m</div>
                </div>
              </div>
            </div>

            <!-- Night Slot -->
            <div class="sketch-box" style="padding:6px 10px;">
              <div class="card-header-sm">
                <span>🌙 NIGHT / BEDTIME (09:30 PM - 10:00 PM) • 2 Medicines</span>
                <span class="badge-sketch">Scheduled</span>
              </div>
              <div class="grid-2">
                <div class="item-row">
                  <div><strong>Metformin 500mg</strong> (1 Tablet - After Dinner)</div>
                  <span class="badge-sketch">Upcoming</span>
                </div>
                <div class="item-row">
                  <div><strong>Calcium D3</strong> (1 Tablet - With Warm Milk)</div>
                  <span class="badge-sketch">Upcoming</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="notes-panel">
      <div class="sticky-note">
        <h4>Medicine Reminder Logic</h4>
        <ul>
          <li><strong>Chronological Blocks:</strong> Morning, Afternoon, Evening, Bedtime groupings avoid confusion.</li>
          <li><strong>Actionable Buttons:</strong> Simple one-click "Mark as Taken" or "Snooze".</li>
          <li><strong>Audit Trail:</strong> Displays exact timestamp and caregiver name who verified dosage.</li>
        </ul>
      </div>
      <div class="sticky-note green">
        <h4>Safety Impact</h4>
        <ul>
          <li>Prevents double-dosing and forgotten medicines.</li>
          <li>Alerts family instantly if dose is overdue by &gt; 30 mins.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 6: SCREEN 5 - ADD/EDIT MEDICATION FORM -->
<div class="page">
  <div class="paper-tape"></div>
  <div class="page-header">
    <div class="page-title-box">
      <h1>06. Screen 5: Add / Edit Medication Form</h1>
      <p>Modal / form for family members or doctors to input medication dosage, frequency, and instructions</p>
    </div>
    <div class="meta-tag">Screen 5 of 9</div>
  </div>

  <div class="wireframe-container">
    <div class="wireframe-viewport">
      <div class="app-topbar">
        <div><strong>ElderlyCare OS</strong> &gt; Add New Prescription</div>
        <div>[X] Close Window</div>
      </div>
      <div class="app-body" style="justify-content:center; align-items:center; background:#EDF2F7; padding:15px;">
        <div class="sketch-box" style="width: 520px; background:#FFFFFF; padding:14px; box-shadow: 4px 4px 0px rgba(0,0,0,0.15);">
          <div class="card-header-sm" style="font-size:14px;">
            <span>➕ Add Medication Schedule</span>
            <span style="font-size:11px; color:#718096;">* Required Fields</span>
          </div>

          <div style="display:flex; flex-direction:column; gap:8px; margin-top:8px;">
            <div class="grid-2">
              <div>
                <label style="font-size:11px; font-weight:bold;">Medicine Name:*</label>
                <div class="sketch-input">[ Atorvastatin Lipitor | ]</div>
              </div>
              <div>
                <label style="font-size:11px; font-weight:bold;">Dosage & Unit:*</label>
                <div class="sketch-input">[ 20 mg (1 Tablet) v ]</div>
              </div>
            </div>

            <div class="grid-3">
              <div>
                <label style="font-size:11px; font-weight:bold;">Frequency:*</label>
                <div class="sketch-input">[ Once Daily v ]</div>
              </div>
              <div>
                <label style="font-size:11px; font-weight:bold;">Timing Routine:*</label>
                <div class="sketch-input">[ After Lunch v ]</div>
              </div>
              <div>
                <label style="font-size:11px; font-weight:bold;">Time of Day:*</label>
                <div class="sketch-input">[ 01:30 PM ]</div>
              </div>
            </div>

            <div class="grid-2">
              <div>
                <label style="font-size:11px; font-weight:bold;">Prescribed By Doctor:</label>
                <div class="sketch-input">[ Dr. K. M. Hasan (Cardiology) v ]</div>
              </div>
              <div>
                <label style="font-size:11px; font-weight:bold;">Current Stock / Refill Alert:</label>
                <div class="sketch-input">[ 30 Pills (Alert at 5) ]</div>
              </div>
            </div>

            <div>
              <label style="font-size:11px; font-weight:bold;">Special Instructions & Caution:</label>
              <div class="sketch-input" style="height:36px;">[ Do not take with grapefruit juice. Take with full glass of water. ]</div>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:6px; border-top:1.5px dashed #CBD5E0; padding-top:8px;">
              <span style="font-size:11px;">[X] Enable SMS & App push reminder alerts</span>
              <div style="display:flex; gap:8px;">
                <div class="sketch-btn" style="padding:4px 10px;">Cancel</div>
                <div class="sketch-btn primary" style="padding:4px 14px;">Save & Activate Schedule</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="notes-panel">
      <div class="sticky-note">
        <h4>Form Field Validation</h4>
        <ul>
          <li><strong>Dosage Safeguards:</strong> Dropdowns ensure standard medical units (mg, ml, drops, puffs).</li>
          <li><strong>Instruction Box:</strong> Prevents dietary contraindications (e.g. food requirements).</li>
          <li><strong>Refill Automation:</strong> Tracks remaining pills and triggers re-order alert.</li>
        </ul>
      </div>
      <div class="sticky-note blue">
        <h4>User Inputs</h4>
        <ul>
          <li>Drug name and formulation</li>
          <li>Exact intake time & meal relation</li>
          <li>Notification preferences</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 7: SCREEN 6 - DOCTOR APPOINTMENT TRACKING -->
<div class="page">
  <div class="paper-tape"></div>
  <div class="page-header">
    <div class="page-title-box">
      <h1>07. Screen 6: Doctor Appointment Tracking</h1>
      <p>Healthcare appointments calendar, consultation logs, and medical booking manager</p>
    </div>
    <div class="meta-tag">Screen 6 of 9</div>
  </div>

  <div class="wireframe-container">
    <div class="wireframe-viewport">
      <div class="app-topbar">
        <div><strong>ElderlyCare OS</strong> &gt; Doctor Appointments</div>
        <div class="sketch-btn primary" style="padding:3px 10px; font-size:10px;">+ Book / Schedule Visit</div>
      </div>
      <div class="app-body">
        <div class="sketch-sidebar">
          <div class="sketch-nav-item">📊 Dashboard</div>
          <div class="sketch-nav-item">👤 Profile</div>
          <div class="sketch-nav-item">💊 Medicine</div>
          <div class="sketch-nav-item active">🩺 Doctors</div>
          <div class="sketch-nav-item">📋 Daily Care</div>
          <div class="sketch-nav-item">🤝 Caregivers</div>
          <div class="sketch-nav-item">📞 Emergency</div>
        </div>
        <div class="sketch-content">
          <!-- Next upcoming prominent card -->
          <div class="sketch-box" style="background:#EBF8FF; border-color:#3182CE; display:flex; justify-content:space-between; align-items:center;">
            <div>
              <span class="badge-sketch" style="background:#3182CE; color:#FFFFFF;">NEXT UPCOMING APPOINTMENT</span>
              <h3 style="font-size:15px; margin-top:3px;">Dr. K. M. Hasan — Senior Cardiologist</h3>
              <p style="font-size:11px; color:#4A5568;">Square Hospital, 3rd Floor, Room 314 • <strong>Tomorrow (Monday, Oct 5) at 10:30 AM</strong></p>
              <p style="font-size:10px; color:#2B6CB0; margin-top:2px;">Purpose: 3-Month Echo & Blood Pressure Review • Accompanied by: Tariq (Son)</p>
            </div>
            <div style="display:flex; flex-direction:column; gap:4px;">
              <div class="sketch-btn" style="padding:3px 8px; font-size:10px;">📍 View Clinic Map</div>
              <div class="sketch-btn" style="padding:3px 8px; font-size:10px;">🔔 Reminder Active</div>
            </div>
          </div>

          <!-- Appointments list split: Upcoming vs History -->
          <div class="grid-2" style="flex:1;">
            <div class="sketch-box">
              <div class="card-header-sm">Scheduled Future Visits</div>
              <div class="item-row">
                <div>
                  <strong>Dr. Nusrat Jahan (Endocrinologist)</strong><br>
                  <span style="font-size:10px;">Labaid Diagnostic, Dhanmondi</span><br>
                  <span style="font-size:10px; color:#718096;">Oct 18, 2026 • 05:00 PM • Fasting Glucose Test</span>
                </div>
                <div class="sketch-btn" style="padding:2px 6px; font-size:10px;">Reschedule</div>
              </div>
              <div class="item-row">
                <div>
                  <strong>Dr. Shahed Ali (Orthopedic)</strong><br>
                  <span style="font-size:10px;">Popular Hospital • Knee Pain Checkup</span><br>
                  <span style="font-size:10px; color:#718096;">Nov 02, 2026 • 11:00 AM</span>
                </div>
                <div class="sketch-btn" style="padding:2px 6px; font-size:10px;">Reschedule</div>
              </div>
            </div>

            <div class="sketch-box">
              <div class="card-header-sm">Past Consultation History & Prescription Reports</div>
              <div class="item-row">
                <div>
                  <strong>Routine Health Checkup</strong> — Sep 04, 2026<br>
                  <span style="font-size:10px; color:#718096;">Dr. K. M. Hasan • BP adjusted to 120/80</span>
                </div>
                <div class="sketch-btn" style="padding:2px 5px; font-size:10px;">📄 View RX</div>
              </div>
              <div class="item-row">
                <div>
                  <strong>Ophthalmology Eye Exam</strong> — Aug 12, 2026<br>
                  <span style="font-size:10px; color:#718096;">Vision stable, no laser required</span>
                </div>
                <div class="sketch-btn" style="padding:2px 5px; font-size:10px;">📄 View RX</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="notes-panel">
      <div class="sticky-note">
        <h4>Appointment UX Highlights</h4>
        <ul>
          <li><strong>Hero Alert Card:</strong> Immediate visibility of nearest upcoming doctor appointment.</li>
          <li><strong>Accompaniment Info:</strong> Identifies which family member will escort the senior.</li>
          <li><strong>Prescription Archive:</strong> Quick link to download previous doctor notes & prescriptions.</li>
        </ul>
      </div>
      <div class="sticky-note green">
        <h4>Reduces Missed Visits</h4>
        <ul>
          <li>Automated 24h and 2h SMS reminders to both caregiver and family member.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 8: SCREEN 7 - DAILY CARE SCHEDULE -->
<div class="page">
  <div class="paper-tape"></div>
  <div class="page-header">
    <div class="page-title-box">
      <h1>08. Screen 7: Daily Care Schedule & Activities</h1>
      <p>Routine checklist for meals, hygiene, physical mobility, hydration, and vitals recording</p>
    </div>
    <div class="meta-tag">Screen 7 of 9</div>
  </div>

  <div class="wireframe-container">
    <div class="wireframe-viewport">
      <div class="app-topbar">
        <div><strong>ElderlyCare OS</strong> &gt; Daily Care Routine</div>
        <div style="font-size:11px;">Today's Progress: <strong>4 of 7 Completed (57%)</strong></div>
      </div>
      <div class="app-body">
        <div class="sketch-sidebar">
          <div class="sketch-nav-item">📊 Dashboard</div>
          <div class="sketch-nav-item">👤 Profile</div>
          <div class="sketch-nav-item">💊 Medicine</div>
          <div class="sketch-nav-item">🩺 Doctors</div>
          <div class="sketch-nav-item active">📋 Daily Care</div>
          <div class="sketch-nav-item">🤝 Caregivers</div>
          <div class="sketch-nav-item">📞 Emergency</div>
        </div>
        <div class="sketch-content">
          <!-- Daily timeline interactive checklist -->
          <div style="display:flex; flex-direction:column; gap:6px; overflow:hidden;">
            <div class="item-row" style="background:#F0FFF4; padding:7px; border:1px solid #9AE6B4; border-radius:4px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:16px;">☑️</span>
                <div>
                  <strong>07:30 AM • Wakeup & Morning Hydration</strong><br>
                  <span style="font-size:10px; color:#4A5568;">1 Glass lukewarm water + lime • Verified by Nasreen (Caregiver)</span>
                </div>
              </div>
              <span class="badge-sketch green">Done 07:35 AM</span>
            </div>

            <div class="item-row" style="background:#F0FFF4; padding:7px; border:1px solid #9AE6B4; border-radius:4px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:16px;">☑️</span>
                <div>
                  <strong>08:15 AM • Light Morning Exercise & Sun Exposure</strong><br>
                  <span style="font-size:10px; color:#4A5568;">15 min garden walk with walking stick + ankle flexion</span>
                </div>
              </div>
              <span class="badge-sketch green">Done 08:30 AM</span>
            </div>

            <div class="item-row" style="background:#F0FFF4; padding:7px; border:1px solid #9AE6B4; border-radius:4px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:16px;">☑️</span>
                <div>
                  <strong>08:45 AM • Breakfast & Vitals Measurement</strong><br>
                  <span style="font-size:10px; color:#4A5568;">Oatmeal + egg white + Papaya • BP: 124/82 mmHg</span>
                </div>
              </div>
              <span class="badge-sketch green">Done 09:00 AM</span>
            </div>

            <div class="item-row" style="background:#FFFFF0; padding:7px; border:1.5px solid #D69E2E; border-radius:4px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:16px;">🔲</span>
                <div>
                  <strong>01:15 PM • Healthy Lunch Routine</strong><br>
                  <span style="font-size:10px; color:#4A5568;">Steamed rice, boiled fish curry, mixed green vegetables (low salt)</span>
                </div>
              </div>
              <div class="sketch-btn primary" style="padding:2px 8px; font-size:10px;">Mark as Done</div>
            </div>

            <div class="item-row" style="padding:7px; border:1px solid #E2E8F0; border-radius:4px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:16px;">🔲</span>
                <div>
                  <strong>04:30 PM • Afternoon Hydration & Physiotherapy</strong><br>
                  <span style="font-size:10px; color:#4A5568;">Coconut water / herbal tea + 15 min knee physiotherapy exercises</span>
                </div>
              </div>
              <span class="badge-sketch">Scheduled</span>
            </div>

            <div class="item-row" style="padding:7px; border:1px solid #E2E8F0; border-radius:4px;">
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:16px;">🔲</span>
                <div>
                  <strong>08:30 PM • Light Dinner & Warm Sponge Bath</strong><br>
                  <span style="font-size:10px; color:#4A5568;">Vegetable soup, 2 wheat rotis, ensure room is comfortable</span>
                </div>
              </div>
              <span class="badge-sketch">Scheduled</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="notes-panel">
      <div class="sticky-note">
        <h4>Holistic Daily Care</h4>
        <ul>
          <li><strong>Beyond Medicine:</strong> Incorporates hydration, diet, exercise, and mental stimulation.</li>
          <li><strong>Caregiver Handoff:</strong> Checked items generate a daily summary report for family.</li>
          <li><strong>Large Checkboxes:</strong> Easily tapped on mobile devices by attending staff.</li>
        </ul>
      </div>
      <div class="sticky-note blue">
        <h4>Task Types</h4>
        <ul>
          <li>Meal & nutrition routines</li>
          <li>Physical therapy / mobility</li>
          <li>Hygiene & vitals logging</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 9: SCREEN 8 - CAREGIVER INFORMATION & SHIFT LOG -->
<div class="page">
  <div class="paper-tape"></div>
  <div class="page-header">
    <div class="page-title-box">
      <h1>09. Screen 8: Caregiver Information & Shift Handoff</h1>
      <p>Caregiver roster, assigned shifts, duty checklists, direct calling, and daily observation logs</p>
    </div>
    <div class="meta-tag">Screen 8 of 9</div>
  </div>

  <div class="wireframe-container">
    <div class="wireframe-viewport">
      <div class="app-topbar">
        <div><strong>ElderlyCare OS</strong> &gt; Caregiver Directory & Shifts</div>
        <div class="sketch-btn primary" style="padding:3px 10px; font-size:10px;">+ Assign New Caregiver</div>
      </div>
      <div class="app-body">
        <div class="sketch-sidebar">
          <div class="sketch-nav-item">📊 Dashboard</div>
          <div class="sketch-nav-item">👤 Profile</div>
          <div class="sketch-nav-item">💊 Medicine</div>
          <div class="sketch-nav-item">🩺 Doctors</div>
          <div class="sketch-nav-item">📋 Daily Care</div>
          <div class="sketch-nav-item active">🤝 Caregivers</div>
          <div class="sketch-nav-item">📞 Emergency</div>
        </div>
        <div class="sketch-content">
          <!-- Active caregiver card -->
          <div class="sketch-box" style="display:flex; justify-content:space-between; align-items:center; background:#F0FFF4; border-color:#38A169;">
            <div style="display:flex; gap:12px; align-items:center;">
              <div class="placeholder-img" style="width:55px; height:55px; border-radius:50%;">Photo</div>
              <div>
                <span class="badge-sketch green" style="font-weight:bold;">CURRENTLY ACTIVE ON DUTY</span>
                <h3 style="font-size:14px; margin-top:2px;">Nasreen Akhtar (Certified Senior Nurse)</h3>
                <p style="font-size:11px; color:#4A5568;">Day Shift: 08:00 AM – 04:00 PM • Experience: 6 Years in Geriatric Care</p>
                <p style="font-size:10px; color:#22543D;">Agency: CareCompanion BD • Verified Police Clearance: Yes</p>
              </div>
            </div>
            <div style="display:flex; gap:6px;">
              <div class="sketch-btn" style="padding:4px 8px; font-size:10px;">📞 Call: 01812-XXXXXX</div>
              <div class="sketch-btn primary" style="padding:4px 8px; font-size:10px;">💬 Message</div>
            </div>
          </div>

          <!-- Secondary Caregivers & Shift Handover Notes -->
          <div class="grid-2" style="flex:1;">
            <div class="sketch-box">
              <div class="card-header-sm">Caregiver Roster & Shift Schedule</div>
              <div class="item-row">
                <div>
                  <strong>Faruk Hossain</strong> (Night Shift Caregiver)<br>
                  <span style="font-size:10px; color:#718096;">Shift: 08:00 PM – 08:00 AM • Tel: 01734-XXXXXX</span>
                </div>
                <span class="badge-sketch">Starts 8:00 PM</span>
              </div>
              <div class="item-row">
                <div>
                  <strong>Morium Begum</strong> (Weekend Relief)<br>
                  <span style="font-size:10px; color:#718096;">Fri & Sat Coverage • Tel: 01923-XXXXXX</span>
                </div>
                <span class="badge-sketch">On Leave</span>
              </div>
            </div>

            <div class="sketch-box">
              <div class="card-header-sm">Shift Handoff Log & Observation Notes</div>
              <div style="font-size:11px; padding:6px; background:#FAFAFA; border:1px solid #E2E8F0; border-radius:4px; margin-bottom:6px;">
                <strong>Logged by Nasreen (Oct 4, 11:30 AM):</strong><br>
                "Patient reported mild left knee soreness after walking. Applied warm compress. Appetite normal. Blood sugar at 110 mg/dL."
              </div>
              <div style="display:flex; gap:6px;">
                <div class="sketch-input" style="flex:1; font-size:11px;">[ Add daily handover observation note... ]</div>
                <div class="sketch-btn primary" style="padding:3px 8px; font-size:10px;">Submit</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="notes-panel">
      <div class="sticky-note">
        <h4>Caregiver Management UX</h4>
        <ul>
          <li><strong>Direct Connectivity:</strong> Family can phone or text the caregiver on duty with 1 tap.</li>
          <li><strong>Digital Shift Handover:</strong> Prevents critical care omissions when shifts change.</li>
          <li><strong>Vetted Records:</strong> Shows certification and agency contact info for transparency.</li>
        </ul>
      </div>
      <div class="sticky-note blue">
        <h4>Accountability</h4>
        <ul>
          <li>Shift clock-in and check-out logs.</li>
          <li>Mandatory shift-end handover remarks.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- PAGE 10: SCREEN 9 - EMERGENCY CONTACTS & SOS PROTOCOL -->
<div class="page">
  <div class="paper-tape"></div>
  <div class="page-header">
    <div class="page-title-box">
      <h1>10. Screen 9: Emergency Contacts & Quick SOS Protocol</h1>
      <p>High-priority rapid response portal with single-tap emergency calling and hospital routing</p>
    </div>
    <div class="meta-tag">Screen 9 of 9</div>
  </div>

  <div class="wireframe-container">
    <div class="wireframe-viewport">
      <div class="app-topbar" style="background:#FFF5F5; border-color:#E53E3E;">
        <div style="color:#C53030;"><strong>🚨 CRITICAL EMERGENCY & SOS MODULE</strong></div>
        <div class="sketch-btn danger" style="padding:2px 8px; font-size:10px;">⚠️ INITIATE SOS BROADCAST</div>
      </div>
      <div class="app-body">
        <div class="sketch-sidebar">
          <div class="sketch-nav-item">📊 Dashboard</div>
          <div class="sketch-nav-item">👤 Profile</div>
          <div class="sketch-nav-item">💊 Medicine</div>
          <div class="sketch-nav-item">🩺 Doctors</div>
          <div class="sketch-nav-item">📋 Daily Care</div>
          <div class="sketch-nav-item">🤝 Caregivers</div>
          <div class="sketch-nav-item active" style="background:#C53030; color:#FFFFFF; border-color:#9B2C2C;">📞 Emergency</div>
        </div>
        <div class="sketch-content" style="background:#FFF5F5;">
          <!-- Giant SOS Speed Dial Row -->
          <div class="grid-3">
            <div class="sketch-box" style="text-align:center; background:#FED7D7; border-color:#9B2C2C; padding:12px;">
              <span style="font-size:22px;">🚑</span>
              <h3 style="font-size:14px; color:#742A2A; margin:2px 0;">National Ambulance</h3>
              <div style="font-size:16px; font-weight:bold; color:#9B2C2C;">999 / 199</div>
              <div class="sketch-btn danger" style="margin-top:6px; padding:4px 12px; font-size:11px;">CALL IMMEDIATELY</div>
            </div>

            <div class="sketch-box" style="text-align:center; background:#FED7D7; border-color:#9B2C2C; padding:12px;">
              <span style="font-size:22px;">🏥</span>
              <h3 style="font-size:14px; color:#742A2A; margin:2px 0;">Square Hospital ER</h3>
              <div style="font-size:16px; font-weight:bold; color:#9B2C2C;">10616 / 02-8144400</div>
              <div class="sketch-btn danger" style="margin-top:6px; padding:4px 12px; font-size:11px;">CALL ER DESK</div>
            </div>

            <div class="sketch-box" style="text-align:center; background:#FED7D7; border-color:#9B2C2C; padding:12px;">
              <span style="font-size:22px;">👨‍⚕️</span>
              <h3 style="font-size:14px; color:#742A2A; margin:2px 0;">Dr. Hasan (Cardio)</h3>
              <div style="font-size:16px; font-weight:bold; color:#9B2C2C;">01713-XXXXXX</div>
              <div class="sketch-btn danger" style="margin-top:6px; padding:4px 12px; font-size:11px;">CALL PHYSICIAN</div>
            </div>
          </div>

          <!-- Family contacts & hospital location info -->
          <div class="grid-2" style="flex:1;">
            <div class="sketch-box" style="background:#FFFFFF;">
              <div class="card-header-sm">Family Member Emergency Contacts (Priority Order)</div>
              <div class="item-row">
                <div>
                  <strong>Tariq Rahman</strong> (Son - Priority 1)<br>
                  <span style="font-size:10px; color:#718096;">Distance: 10 mins away • Tel: 01711-XXXXXX</span>
                </div>
                <div class="sketch-btn" style="padding:2px 6px; font-size:10px;">📞 Call 1st</div>
              </div>
              <div class="item-row">
                <div>
                  <strong>Farzana Chowdhury</strong> (Daughter - Priority 2)<br>
                  <span style="font-size:10px; color:#718096;">Tel: 01819-XXXXXX • Alternative Contact</span>
                </div>
                <div class="sketch-btn" style="padding:2px 6px; font-size:10px;">📞 Call 2nd</div>
              </div>
            </div>

            <div class="sketch-box" style="background:#FFFFFF;">
              <div class="card-header-sm">Patient Emergency Medical Summary (For Paramedics)</div>
              <p style="font-size:11px; line-height:1.4;">
                • <strong>Full Name:</strong> Abdul Rahman Chowdhury (Age: 76)<br>
                • <strong>Blood Type:</strong> B Positive (B+)<br>
                • <strong>Severe Allergy:</strong> PENICILLIN (Causes Anaphylaxis)<br>
                • <strong>Key Conditions:</strong> Type 2 Diabetes, Hypertension, Stent placed in 2021<br>
                • <strong>Home GPS Coordinates:</strong> 23.7461° N, 90.3742° E
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="notes-panel">
      <div class="sticky-note red" style="background:#FED7D7; border-color:#E53E3E;">
        <h4>Emergency UI Principles</h4>
        <ul>
          <li><strong>High Affordance:</strong> Massive, non-confusing call buttons.</li>
          <li><strong>Instant Paramedic Brief:</strong> Blood type and Penicillin allergy instantly available to arriving medics.</li>
          <li><strong>One-Tap SMS Broadcast:</strong> Notifies all family members simultaneously with GPS pin.</li>
        </ul>
      </div>
      <div class="sticky-note">
        <h4>Compliance</h4>
        <ul>
          <li>Meets ISO medical emergency alert standards for senior citizens.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

</body>
</html>
"""

with open("low_fidelity_design.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated low_fidelity_design.html successfully.")
