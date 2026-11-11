# Generate Fig 2: Proposed System Rich Picture matching demo.pdf p9_0_X75.png exactly

def get_exact_demo_style_fig2_svg():
    return """<svg viewBox="0 0 820 360" width="820" height="360" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <defs>
    <marker id="f2-arrow-right" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
    <marker id="f2-arrow-left" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 8 1.5 L 0 5 L 8 8.5 z" fill="#000000"/>
    </marker>
    <marker id="f2-arrow-down" viewBox="0 0 10 10" refX="5" refY="8" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 1.5 0 L 5 8 L 8.5 0 z" fill="#000000"/>
    </marker>
    <marker id="f2-arrow-up" viewBox="0 0 10 10" refX="5" refY="2" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 1.5 8 L 5 0 L 8.5 8 z" fill="#000000"/>
    </marker>
  </defs>

  <!-- ================= TOP: HOSPITAL / CLINIC (Classical Building) ================= -->
  <g transform="translate(340, 15)">
    <!-- Roof pediment -->
    <path d="M 0 32 L 50 5 L 100 32 Z" fill="#000000"/>
    <rect x="5" y="32" width="90" height="5" fill="#000000"/>
    <!-- 4 Pillars -->
    <rect x="12" y="39" width="12" height="30" fill="#000000"/>
    <rect x="34" y="39" width="12" height="30" fill="#000000"/>
    <rect x="56" y="39" width="12" height="30" fill="#000000"/>
    <rect x="78" y="39" width="12" height="30" fill="#000000"/>
    <!-- Base -->
    <rect x="2" y="69" width="96" height="7" fill="#000000"/>
    <!-- Medical Cross on roof -->
    <rect x="47" y="14" width="6" height="13" fill="#ffffff"/>
    <rect x="43.5" y="17.5" width="13" height="6" fill="#ffffff"/>
    <text x="50" y="90" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Hospital / Clinic</text>
  </g>

  <!-- ================= LEFT: SENIOR CITIZEN (Single Outline Person) ================= -->
  <g transform="translate(20, 165)">
    <!-- Head -->
    <circle cx="28" cy="22" r="14" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
    <!-- Shoulders -->
    <path d="M 2 72 C 2 44, 54 44, 54 72" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
    <text x="28" y="94" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Senior Citizen</text>
  </g>

  <!-- ================= CENTER: ELDERLY CARE MANAGEMENT SYSTEM (Browser Window + Globe) ================= -->
  <g transform="translate(355, 175)">
    <!-- Browser window -->
    <rect x="0" y="0" width="75" height="55" fill="#ffffff" stroke="#00a8e8" stroke-width="2"/>
    <rect x="0" y="0" width="75" height="14" fill="#00a8e8"/>
    <!-- Tree / diagram inside browser -->
    <rect x="28" y="18" width="18" height="10" fill="#00a8e8"/>
    <line x1="37" y1="28" x2="37" y2="34" stroke="#00a8e8" stroke-width="1.5"/>
    <line x1="18" y1="34" x2="56" y2="34" stroke="#00a8e8" stroke-width="1.5"/>
    <line x1="18" y1="34" x2="18" y2="40" stroke="#00a8e8" stroke-width="1.5"/>
    <line x1="56" y1="34" x2="56" y2="40" stroke="#00a8e8" stroke-width="1.5"/>
    <rect x="12" y="40" width="12" height="7" fill="#00a8e8"/>
    <rect x="50" y="40" width="12" height="7" fill="#00a8e8"/>
    
    <!-- Globe Icon overlapping bottom-right -->
    <g transform="translate(42, 28)">
      <circle cx="22" cy="22" r="21" fill="#ffffff" stroke="#00a8e8" stroke-width="2"/>
      <line x1="1" y1="22" x2="43" y2="22" stroke="#00a8e8" stroke-width="1.8"/>
      <ellipse cx="22" cy="22" rx="11" ry="21" fill="none" stroke="#00a8e8" stroke-width="1.8"/>
    </g>

    <text x="42" y="75" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">Elderly Care</text>
    <text x="42" y="88" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">Management System</text>
  </g>

  <!-- ================= RIGHT: CAREGIVER / GUARDIAN (Blue 3-Person Icon) ================= -->
  <g transform="translate(695, 185)">
    <!-- Left Person -->
    <circle cx="20" cy="18" r="12" fill="#0088ce"/>
    <path d="M 2 50 C 2 35, 38 35, 38 50 Z" fill="#0088ce"/>
    <!-- Right Person -->
    <circle cx="68" cy="18" r="12" fill="#0088ce"/>
    <path d="M 50 50 C 50 35, 86 35, 86 50 Z" fill="#0088ce"/>
    <!-- Center Person -->
    <circle cx="44" cy="12" r="14" fill="#00b4d8"/>
    <path d="M 16 52 C 16 35, 72 35, 72 52 Z" fill="#00b4d8"/>
    <text x="44" y="72" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Caregiver /</text>
    <text x="44" y="86" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Guardian</text>
  </g>

  <!-- ================= TOP CONNECTIONS ================= -->
  <!-- Hospital to Senior (Left top route, exactly like demo bank to employee) -->
  <line x1="335" y1="52" x2="265" y2="52" stroke="#000000" stroke-width="1"/>
  <line x1="265" y1="52" x2="265" y2="78" stroke="#000000" stroke-width="1"/>
  <line x1="265" y1="78" x2="35" y2="78" stroke="#000000" stroke-width="1"/>
  <line x1="35" y1="78" x2="35" y2="160" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-down)"/>
  <text x="145" y="72" font-size="9" fill="#000000" text-anchor="middle">Receives Medical Consultation &amp; Care</text>

  <!-- System to Hospital (Right top route, exactly like demo HR to bank) -->
  <line x1="745" y1="180" x2="745" y2="45" stroke="#000000" stroke-width="1"/>
  <line x1="745" y1="45" x2="455" y2="45" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-left)"/>
  <text x="590" y="39" font-size="9" fill="#000000" text-anchor="middle">Schedules Appointments &amp; Syncs e-Rx</text>

  <!-- ================= LEFT: SENIOR TO SYSTEM ARROWS ================= -->
  <!-- 1. Top curved arrow: Trigger SOS -->
  <line x1="48" y1="150" x2="48" y2="135" stroke="#000000" stroke-width="1"/>
  <line x1="48" y1="135" x2="355" y2="135" stroke="#000000" stroke-width="1"/>
  <line x1="355" y1="135" x2="355" y2="170" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-down)"/>
  <text x="195" y="130" font-size="9" font-weight="bold" fill="#000000" text-anchor="middle">Trigger 1-Touch Emergency SOS</text>

  <!-- 2. View Medication Schedule & Alarms -->
  <line x1="350" y1="180" x2="75" y2="180" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-left)"/>
  <text x="210" y="174" font-size="9" fill="#000000" text-anchor="middle">Audio &amp; Visual Medication Alarms</text>

  <!-- 3. Confirm Dose Taken -->
  <line x1="75" y1="202" x2="350" y2="202" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-right)"/>
  <text x="210" y="196" font-size="9" fill="#000000" text-anchor="middle">1-Tap &quot;Taken&quot; Dose Confirmation</text>

  <!-- 4. View Daily Care Tasks & Vitals -->
  <line x1="350" y1="224" x2="75" y2="224" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-left)"/>
  <text x="210" y="218" font-size="9" fill="#000000" text-anchor="middle">View Daily Care Routine &amp; Tasks</text>

  <!-- 5. View Doctor Appointments -->
  <line x1="75" y1="246" x2="350" y2="246" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-right)"/>
  <text x="210" y="240" font-size="9" fill="#000000" text-anchor="middle">View Upcoming Doctor Appointments</text>

  <!-- 6. Bottom curved arrow: View Health Profile -->
  <line x1="48" y1="262" x2="48" y2="295" stroke="#000000" stroke-width="1"/>
  <line x1="48" y1="295" x2="390" y2="295" stroke="#000000" stroke-width="1"/>
  <line x1="390" y1="295" x2="390" y2="270" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-up)"/>
  <text x="210" y="290" font-size="9" fill="#000000" text-anchor="middle">View Health Profile &amp; Emergency Info</text>

  <!-- ================= RIGHT: SYSTEM TO CAREGIVER / GUARDIAN ARROWS ================= -->
  <!-- 1. Top curved arrow: Receive SOS -->
  <line x1="425" y1="172" x2="425" y2="135" stroke="#000000" stroke-width="1"/>
  <line x1="425" y1="135" x2="685" y2="135" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-right)"/>
  <text x="555" y="130" font-size="9" font-weight="bold" fill="#000000" text-anchor="middle">Receive Instant SOS Alert with GPS pin</text>

  <!-- 2. Real-time Adherence Tracking -->
  <line x1="445" y1="180" x2="685" y2="180" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-right)"/>
  <text x="565" y="174" font-size="9" fill="#000000" text-anchor="middle">Real-time Adherence Monitoring</text>

  <!-- 3. Log Daily ADL Tasks & Vitals -->
  <line x1="685" y1="202" x2="445" y2="202" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-left)"/>
  <text x="565" y="196" font-size="9" fill="#000000" text-anchor="middle">Log Daily Tasks &amp; Vitals (BP, Sugar)</text>

  <!-- 4. Submit Shift Handoff Notes -->
  <line x1="685" y1="224" x2="445" y2="224" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-left)"/>
  <text x="565" y="218" font-size="9" fill="#000000" text-anchor="middle">Submit Digital Shift Handoff Notes</text>

  <!-- 5. Configure Medication Schedules -->
  <line x1="685" y1="246" x2="445" y2="246" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-left)"/>
  <text x="565" y="240" font-size="9" fill="#000000" text-anchor="middle">Configure Prescriptions &amp; Schedules</text>

  <!-- 6. Bottom curved arrow: Updates Care Status -->
  <line x1="685" y1="295" x2="415" y2="295" stroke="#000000" stroke-width="1"/>
  <line x1="415" y1="295" x2="415" y2="270" stroke="#000000" stroke-width="1" marker-end="url(#f2-arrow-up)"/>
  <text x="565" y="290" font-size="9" fill="#000000" text-anchor="middle">Review Monthly Compliance Reports</text>

  <!-- Caption at bottom -->
  <text x="410" y="345" font-size="13" font-weight="bold" fill="#000000" text-anchor="middle">Fig 2: Proposed System Rich Picture</text>
</svg>"""
