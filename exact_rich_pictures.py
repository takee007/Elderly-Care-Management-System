# Script to generate exact-style Rich Pictures for Elderly Care Management System
# Matching the exact visual style, icons, and layout shown in demo.pdf

def get_exact_fig1_existing_rich_picture_svg():
    return """<svg viewBox="0 0 820 540" width="820" height="540" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <defs>
    <!-- Arrowhead markers -->
    <marker id="arrow-right" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
    <marker id="arrow-left" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 8 1.5 L 0 5 L 8 8.5 z" fill="#000000"/>
    </marker>
    <marker id="arrow-down" viewBox="0 0 10 10" refX="5" refY="8" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 1.5 0 L 5 8 L 8.5 0 z" fill="#000000"/>
    </marker>
    <marker id="arrow-up" viewBox="0 0 10 10" refX="5" refY="2" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 1.5 8 L 5 0 L 8.5 8 z" fill="#000000"/>
    </marker>
  </defs>

  <!-- 1. HOSPITAL / CLINIC (Top Left) -->
  <g transform="translate(170, 25)">
    <!-- Classical building icon -->
    <path d="M 0 35 L 45 5 L 90 35 Z" fill="#111827"/>
    <rect x="5" y="35" width="80" height="6" fill="#111827"/>
    <!-- Pillars -->
    <rect x="12" y="43" width="10" height="32" fill="#111827"/>
    <rect x="30" y="43" width="10" height="32" fill="#111827"/>
    <rect x="50" y="43" width="10" height="32" fill="#111827"/>
    <rect x="68" y="43" width="10" height="32" fill="#111827"/>
    <!-- Base -->
    <rect x="2" y="75" width="86" height="8" fill="#111827"/>
    <!-- Medical Cross on roof -->
    <rect x="42" y="16" width="6" height="14" fill="#ffffff"/>
    <rect x="38" y="20" width="14" height="6" fill="#ffffff"/>
    <text x="45" y="98" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Hospital / Clinic</text>
  </g>

  <!-- 2. PHYSICAL MEDICAL FILES (Top Right) -->
  <g transform="translate(560, 45)">
    <!-- Back sheet -->
    <path d="M 10 5 L 45 5 L 58 18 L 58 65 L 10 65 Z" fill="#93c5fd" stroke="#2563eb" stroke-width="1.5"/>
    <!-- Middle sheet -->
    <path d="M 18 12 L 53 12 L 66 25 L 66 72 L 18 72 Z" fill="#60a5fa" stroke="#1d4ed8" stroke-width="1.5"/>
    <!-- Front sheet -->
    <path d="M 26 19 L 61 19 L 74 32 L 74 79 L 26 79 Z" fill="#2563eb" stroke="#1e40af" stroke-width="1.5"/>
    <!-- Folded corner on front sheet -->
    <path d="M 61 19 L 61 32 L 74 32 Z" fill="#93c5fd" stroke="#1e40af" stroke-width="1"/>
    <!-- Lines on front sheet -->
    <line x1="34" y1="42" x2="62" y2="42" stroke="#ffffff" stroke-width="2.5"/>
    <line x1="34" y1="52" x2="62" y2="52" stroke="#ffffff" stroke-width="2.5"/>
    <line x1="34" y1="62" x2="52" y2="62" stroke="#ffffff" stroke-width="2.5"/>
    <text x="50" y="96" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Paper Prescriptions</text>
  </g>

  <!-- 3. SENIOR CITIZEN (Left) - Orange 3-Person Silhouette Icon -->
  <g transform="translate(70, 190)">
    <!-- Left person -->
    <circle cx="22" cy="20" r="12" fill="#e65100"/>
    <path d="M 2 52 C 2 36, 42 36, 42 52 Z" fill="#e65100"/>
    <!-- Right person -->
    <circle cx="68" cy="20" r="12" fill="#e65100"/>
    <path d="M 48 52 C 48 36, 88 36, 88 52 Z" fill="#e65100"/>
    <!-- Center (front) person -->
    <circle cx="45" cy="14" r="14" fill="#f97316"/>
    <path d="M 18 54 C 18 36, 72 36, 72 54 Z" fill="#f97316"/>
    <text x="45" y="75" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Senior Citizen</text>
  </g>

  <!-- 4. SENIOR's HOME / RESIDENCE (Center) - Gray Building / House -->
  <g transform="translate(370, 185)">
    <!-- Multi-story building with windows (matching demo style) -->
    <rect x="10" y="5" width="45" height="75" fill="#6b7280" stroke="#374151" stroke-width="1.5"/>
    <!-- Windows grid -->
    <rect x="15" y="12" width="6" height="8" fill="#ffffff"/>
    <rect x="25" y="12" width="6" height="8" fill="#ffffff"/>
    <rect x="35" y="12" width="6" height="8" fill="#ffffff"/>
    <rect x="44" y="12" width="6" height="8" fill="#ffffff"/>

    <rect x="15" y="24" width="6" height="8" fill="#ffffff"/>
    <rect x="25" y="24" width="6" height="8" fill="#ffffff"/>
    <rect x="35" y="24" width="6" height="8" fill="#ffffff"/>
    <rect x="44" y="24" width="6" height="8" fill="#ffffff"/>

    <rect x="15" y="36" width="6" height="8" fill="#ffffff"/>
    <rect x="25" y="36" width="6" height="8" fill="#ffffff"/>
    <rect x="35" y="36" width="6" height="8" fill="#ffffff"/>
    <rect x="44" y="36" width="6" height="8" fill="#ffffff"/>

    <rect x="15" y="48" width="6" height="8" fill="#ffffff"/>
    <rect x="25" y="48" width="6" height="8" fill="#ffffff"/>
    <rect x="35" y="48" width="6" height="8" fill="#ffffff"/>
    <rect x="44" y="48" width="6" height="8" fill="#ffffff"/>

    <rect x="26" y="62" width="12" height="18" fill="#111827"/>
    <text x="32" y="96" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Senior's Home</text>
  </g>

  <!-- 5. CAREGIVER & FAMILY GUARDIAN (Right) - Blue 3-Person Silhouette Icon -->
  <g transform="translate(660, 200)">
    <!-- Left person -->
    <circle cx="22" cy="20" r="12" fill="#0284c7"/>
    <path d="M 2 52 C 2 36, 42 36, 42 52 Z" fill="#0284c7"/>
    <!-- Right person -->
    <circle cx="68" cy="20" r="12" fill="#0284c7"/>
    <path d="M 48 52 C 48 36, 88 36, 88 52 Z" fill="#0284c7"/>
    <!-- Center (front) person -->
    <circle cx="45" cy="14" r="14" fill="#0ea5e9"/>
    <path d="M 18 54 C 18 36, 72 36, 72 54 Z" fill="#0ea5e9"/>
    <text x="45" y="75" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Caregiver / Guardian</text>
  </g>

  <!-- 6. PAPER PILLBOX & CARE LOG SHEET (Bottom Center) -->
  <g transform="translate(365, 360)">
    <!-- Folded paper document (exact demo attendance sheet style) -->
    <path d="M 10 5 L 46 5 L 60 19 L 60 75 L 10 75 Z" fill="#ffffff" stroke="#000000" stroke-width="1.5"/>
    <path d="M 46 5 L 46 19 L 60 19 Z" fill="#e5e7eb" stroke="#000000" stroke-width="1.5"/>
    <text x="35" y="92" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">Handwritten Log</text>
    <text x="35" y="106" font-size="11" font-weight="bold" fill="#000000" text-anchor="middle">&amp; Pillbox</text>
  </g>

  <!-- ================= CONNECTING ARROWS & LABELS ================= -->

  <!-- Hospital to Senior (Left downward arrow) -->
  <line x1="180" y1="108" x2="105" y2="108" stroke="#000000" stroke-width="1"/>
  <line x1="105" y1="108" x2="105" y2="185" stroke="#000000" stroke-width="1" marker-end="url(#arrow-down)"/>
  <text x="105" y="145" font-size="9.5" fill="#000000" text-anchor="middle">Physical Clinic Visit</text>
  <text x="105" y="157" font-size="9.5" fill="#000000" text-anchor="middle">&amp; Consultation</text>

  <!-- Hospital to Home (Angled arrow) -->
  <line x1="260" y1="80" x2="385" y2="80" stroke="#000000" stroke-width="1"/>
  <line x1="385" y1="80" x2="385" y2="182" stroke="#000000" stroke-width="1" marker-end="url(#arrow-down)"/>
  <text x="330" y="74" font-size="9.5" fill="#000000" text-anchor="middle">Paper Prescription</text>

  <!-- Home to Files (Upper center to right) -->
  <line x1="400" y1="182" x2="400" y2="120" stroke="#000000" stroke-width="1"/>
  <line x1="400" y1="120" x2="550" y2="120" stroke="#000000" stroke-width="1"/>
  <line x1="550" y1="120" x2="550" y2="80" stroke="#000000" stroke-width="1"/>
  <line x1="550" y1="80" x2="570" y2="80" stroke="#000000" stroke-width="1" marker-end="url(#arrow-right)"/>
  <text x="475" y="112" font-size="9.5" fill="#000000" text-anchor="middle">manually files paper doctor slips</text>

  <!-- Caregiver to Files -->
  <line x1="710" y1="195" x2="710" y2="80" stroke="#000000" stroke-width="1"/>
  <line x1="710" y1="80" x2="655" y2="80" stroke="#000000" stroke-width="1" marker-end="url(#arrow-left)"/>
  <text x="690" y="140" font-size="9.5" fill="#000000">checks old paper slips</text>

  <!-- Between Senior and Home (Horizontal arrows) -->
  <!-- Arrow 1: Forgets doses -->
  <line x1="165" y1="205" x2="365" y2="205" stroke="#000000" stroke-width="1" marker-end="url(#arrow-right)"/>
  <text x="265" y="200" font-size="9.5" fill="#000000" text-anchor="middle">Forgets scheduled medicine</text>

  <!-- Arrow 2: Verbal care request -->
  <line x1="165" y1="225" x2="365" y2="225" stroke="#000000" stroke-width="1" marker-end="url(#arrow-right)"/>
  <text x="265" y="220" font-size="9.5" fill="#000000" text-anchor="middle">Relies on paper pillbox</text>

  <!-- Arrow 3: Inquires care -->
  <line x1="365" y1="245" x2="168" y2="245" stroke="#000000" stroke-width="1" marker-end="url(#arrow-left)"/>
  <text x="265" y="240" font-size="9.5" fill="#000000" text-anchor="middle">Confusion over dosages</text>

  <!-- Arrow 4: Panic during falls -->
  <line x1="165" y1="265" x2="365" y2="265" stroke="#000000" stroke-width="1" marker-end="url(#arrow-right)"/>
  <text x="265" y="260" font-size="9.5" fill="#000000" text-anchor="middle">Panicked call during emergency</text>

  <!-- Between Home and Caregiver / Guardian (Horizontal arrows) -->
  <!-- Arrow 1: Manually tracks -->
  <line x1="655" y1="205" x2="445" y2="205" stroke="#000000" stroke-width="1" marker-end="url(#arrow-left)"/>
  <text x="550" y="200" font-size="9.5" fill="#000000" text-anchor="middle">Manually administers medicine</text>

  <!-- Arrow 2: Verbal shift updates -->
  <line x1="655" y1="225" x2="445" y2="225" stroke="#000000" stroke-width="1" marker-end="url(#arrow-left)"/>
  <text x="550" y="220" font-size="9.5" fill="#000000" text-anchor="middle">Gives verbal shift updates</text>

  <!-- Arrow 3: Guardian calls -->
  <line x1="445" y1="245" x2="652" y2="245" stroke="#000000" stroke-width="1" marker-end="url(#arrow-right)"/>
  <text x="550" y="240" font-size="9.5" fill="#000000" text-anchor="middle">Guardian calls repeatedly</text>

  <!-- Arrow 4: Missed records -->
  <line x1="655" y1="265" x2="445" y2="265" stroke="#000000" stroke-width="1" marker-end="url(#arrow-left)"/>
  <text x="550" y="260" font-size="9.5" fill="#000000" text-anchor="middle">Unaccountable shift handover</text>

  <!-- Bottom: Senior to Handwritten Log Sheet -->
  <line x1="115" y1="270" x2="115" y2="400" stroke="#000000" stroke-width="1"/>
  <line x1="115" y1="400" x2="360" y2="400" stroke="#000000" stroke-width="1" marker-end="url(#arrow-right)"/>
  <text x="235" y="394" font-size="9.5" fill="#000000" text-anchor="middle">Checks paper pill organizer</text>

  <!-- Bottom: Caregiver to Handwritten Log Sheet -->
  <line x1="705" y1="280" x2="705" y2="400" stroke="#000000" stroke-width="1"/>
  <line x1="705" y1="400" x2="435" y2="400" stroke="#000000" stroke-width="1" marker-end="url(#arrow-left)"/>
  <text x="570" y="394" font-size="9.5" fill="#000000" text-anchor="middle">Handwrites vitals &amp; notes</text>

  <!-- Caption at very bottom (matching demo style) -->
  <text x="410" y="520" font-size="13" font-weight="bold" fill="#000000" text-anchor="middle">Fig 1: Existing System Rich Picture</text>
</svg>"""

def get_exact_fig2_proposed_rich_picture_svg():
    return """<svg viewBox="0 0 820 540" width="820" height="540" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <defs>
    <marker id="parrow-right" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0d9488"/>
    </marker>
    <marker id="parrow-left" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 8 1.5 L 0 5 L 8 8.5 z" fill="#0d9488"/>
    </marker>
    <marker id="parrow-down" viewBox="0 0 10 10" refX="5" refY="8" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 1.5 0 L 5 8 L 8.5 0 z" fill="#0d9488"/>
    </marker>
    <marker id="parrow-up" viewBox="0 0 10 10" refX="5" refY="2" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 1.5 8 L 5 0 L 8.5 8 z" fill="#0d9488"/>
    </marker>
    <marker id="parrow-red-down" viewBox="0 0 10 10" refX="5" refY="8" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 1.5 0 L 5 8 L 8.5 0 z" fill="#e11d48"/>
    </marker>
  </defs>

  <!-- 1. DOCTOR / HOSPITAL PORTAL (Top Left) -->
  <g transform="translate(160, 20)">
    <!-- Hospital / Doctor console icon -->
    <rect x="0" y="10" width="75" height="55" rx="5" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
    <rect x="8" y="18" width="59" height="32" fill="#ffffff" stroke="#86efac"/>
    <rect x="34" y="24" width="7" height="20" fill="#16a34a"/>
    <rect x="27.5" y="30.5" width="20" height="7" fill="#16a34a"/>
    <line x1="25" y1="65" x2="50" y2="65" stroke="#16a34a" stroke-width="3"/>
    <text x="37" y="82" font-size="11.5" font-weight="bold" fill="#000000" text-anchor="middle">Doctor / Clinic</text>
  </g>

  <!-- 2. CENTRAL CLOUD DATABASE & APPLICATION (Top Right) -->
  <g transform="translate(560, 20)">
    <!-- Cloud / Server Icon -->
    <rect x="0" y="8" width="85" height="60" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.8"/>
    <!-- Server disks -->
    <rect x="10" y="18" width="65" height="10" rx="3" fill="#3b82f6"/>
    <circle cx="18" cy="23" r="2" fill="#ffffff"/>
    <circle cx="25" cy="23" r="2" fill="#ffffff"/>

    <rect x="10" y="33" width="65" height="10" rx="3" fill="#3b82f6"/>
    <circle cx="18" cy="38" r="2" fill="#ffffff"/>
    <circle cx="25" cy="38" r="2" fill="#ffffff"/>

    <rect x="10" y="48" width="65" height="10" rx="3" fill="#3b82f6"/>
    <circle cx="18" cy="53" r="2" fill="#ffffff"/>
    <circle cx="25" cy="53" r="2" fill="#ffffff"/>
    <text x="42" y="82" font-size="11.5" font-weight="bold" fill="#000000" text-anchor="middle">Cloud Database</text>
  </g>

  <!-- 3. SENIOR CITIZEN WITH TABLET (Left) - Orange 3-Person Icon -->
  <g transform="translate(60, 190)">
    <circle cx="22" cy="20" r="12" fill="#e65100"/>
    <path d="M 2 52 C 2 36, 42 36, 42 52 Z" fill="#e65100"/>
    <circle cx="68" cy="20" r="12" fill="#e65100"/>
    <path d="M 48 52 C 48 36, 88 36, 88 52 Z" fill="#e65100"/>
    <circle cx="45" cy="14" r="14" fill="#f97316"/>
    <path d="M 18 54 C 18 36, 72 36, 72 54 Z" fill="#f97316"/>
    <text x="45" y="75" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Senior Citizen</text>
  </g>

  <!-- 4. CENTRAL CARE MANAGEMENT SYSTEM (Center Platform) -->
  <g transform="translate(350, 165)">
    <!-- Central Modern System Hub -->
    <rect x="0" y="0" width="120" height="110" rx="8" fill="#042f2e" stroke="#0d9488" stroke-width="2.5"/>
    <rect x="10" y="10" width="100" height="24" rx="4" fill="#0d9488"/>
    <text x="60" y="26" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">ELDERLY CARE</text>
    
    <rect x="10" y="38" width="100" height="18" rx="3" fill="#134e4a"/>
    <text x="60" y="51" font-size="8.5" fill="#ccfbf1" text-anchor="middle">Medication Engine</text>

    <rect x="10" y="60" width="100" height="18" rx="3" fill="#134e4a"/>
    <text x="60" y="73" font-size="8.5" fill="#ccfbf1" text-anchor="middle">ADL Shift Tracker</text>

    <rect x="10" y="82" width="100" height="18" rx="3" fill="#be123c"/>
    <text x="60" y="95" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">SOS Emergency</text>

    <text x="60" y="128" font-size="11.5" font-weight="bold" fill="#000000" text-anchor="middle">Care Platform</text>
  </g>

  <!-- 5. CAREGIVER & FAMILY GUARDIAN (Right) - Blue 3-Person Icon -->
  <g transform="translate(670, 190)">
    <circle cx="22" cy="20" r="12" fill="#0284c7"/>
    <path d="M 2 52 C 2 36, 42 36, 42 52 Z" fill="#0284c7"/>
    <circle cx="68" cy="20" r="12" fill="#0284c7"/>
    <path d="M 48 52 C 48 36, 88 36, 88 52 Z" fill="#0284c7"/>
    <circle cx="45" cy="14" r="14" fill="#0ea5e9"/>
    <path d="M 18 54 C 18 36, 72 36, 72 54 Z" fill="#0ea5e9"/>
    <text x="45" y="75" font-size="12" font-weight="bold" fill="#000000" text-anchor="middle">Caregiver / Guardian</text>
  </g>

  <!-- 6. FIRST RESPONDER & PARAMEDICS (Bottom Center) -->
  <g transform="translate(365, 360)">
    <!-- Ambulance / Emergency icon -->
    <rect x="5" y="10" width="75" height="42" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.8"/>
    <rect x="12" y="18" width="22" height="16" fill="#ffffff" stroke="#f87171"/>
    <!-- Red cross -->
    <rect x="54" y="18" width="6" height="18" fill="#dc2626"/>
    <rect x="48" y="24" width="18" height="6" fill="#dc2626"/>
    <!-- Wheels -->
    <circle cx="24" cy="54" r="8" fill="#1f2937"/>
    <circle cx="62" cy="54" r="8" fill="#1f2937"/>
    <circle cx="24" cy="54" r="3" fill="#ffffff"/>
    <circle cx="62" cy="54" r="3" fill="#ffffff"/>

    <text x="42" y="80" font-size="11.5" font-weight="bold" fill="#000000" text-anchor="middle">Emergency Services</text>
    <text x="42" y="94" font-size="10" fill="#4b5563" text-anchor="middle">(Paramedics / Hospital)</text>
  </g>

  <!-- ================= CONNECTING ARROWS & LABELS ================= -->

  <!-- Doctor to Central System (Top left to center) -->
  <line x1="240" y1="55" x2="380" y2="55" stroke="#0d9488" stroke-width="1.2"/>
  <line x1="380" y1="55" x2="380" y2="160" stroke="#0d9488" stroke-width="1.2" marker-end="url(#parrow-down)"/>
  <text x="310" y="48" font-size="9" fill="#000000" text-anchor="middle">Uploads e-Prescriptions</text>
  <text x="310" y="66" font-size="9" fill="#000000" text-anchor="middle">Reviews verified adherence</text>

  <!-- Central System to Database (Center to top right) -->
  <line x1="440" y1="160" x2="440" y2="55" stroke="#0d9488" stroke-width="1.2"/>
  <line x1="440" y1="55" x2="555" y2="55" stroke="#0d9488" stroke-width="1.2" marker-end="url(#parrow-right)"/>
  <text x="495" y="48" font-size="9" fill="#000000" text-anchor="middle">Syncs real-time records</text>

  <!-- Between Senior and Central System (Horizontal arrows) -->
  <line x1="345" y1="185" x2="160" y2="185" stroke="#0d9488" stroke-width="1.2" marker-end="url(#parrow-left)"/>
  <text x="250" y="178" font-size="9" fill="#000000" text-anchor="middle">Audio &amp; visual dose alarms</text>

  <line x1="160" y1="205" x2="345" y2="205" stroke="#0d9488" stroke-width="1.2" marker-end="url(#parrow-right)"/>
  <text x="250" y="198" font-size="9" fill="#000000" text-anchor="middle">1-Tap &quot;Taken&quot; dose logging</text>

  <line x1="345" y1="225" x2="160" y2="225" stroke="#0d9488" stroke-width="1.2" marker-end="url(#parrow-left)"/>
  <text x="250" y="218" font-size="9" fill="#000000" text-anchor="middle">Daily routine reminders</text>

  <line x1="160" y1="245" x2="345" y2="245" stroke="#e11d48" stroke-width="1.5" marker-end="url(#parrow-right)"/>
  <text x="250" y="238" font-size="9" font-weight="bold" fill="#be123c" text-anchor="middle">Triggers 1-Touch SOS panic</text>

  <!-- Between Central System and Caregiver / Guardian (Horizontal arrows) -->
  <line x1="665" y1="185" x2="475" y2="185" stroke="#0d9488" stroke-width="1.2" marker-end="url(#parrow-left)"/>
  <text x="570" y="178" font-size="9" fill="#000000" text-anchor="middle">Logs completed ADL tasks</text>

  <line x1="475" y1="205" x2="665" y2="205" stroke="#0d9488" stroke-width="1.2" marker-end="url(#parrow-right)"/>
  <text x="570" y="198" font-size="9" fill="#000000" text-anchor="middle">Live adherence dashboard</text>

  <line x1="665" y1="225" x2="475" y2="225" stroke="#0d9488" stroke-width="1.2" marker-end="url(#parrow-left)"/>
  <text x="570" y="218" font-size="9" fill="#000000" text-anchor="middle">Digital shift handoff notes</text>

  <line x1="475" y1="245" x2="665" y2="245" stroke="#e11d48" stroke-width="1.5" marker-end="url(#parrow-right)"/>
  <text x="570" y="238" font-size="9" font-weight="bold" fill="#be123c" text-anchor="middle">Instant SOS SMS with GPS pin</text>

  <!-- Bottom: Central System to Emergency First Responder -->
  <line x1="410" y1="280" x2="410" y2="355" stroke="#e11d48" stroke-width="1.8" marker-end="url(#parrow-red-down)"/>
  <text x="410" y="305" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">Auto-dispatches emergency call</text>
  <text x="410" y="318" font-size="9" fill="#991b1b" text-anchor="middle">Transmits GPS &amp; Allergy Health Brief</text>

  <!-- Caption at very bottom (matching demo style) -->
  <text x="410" y="520" font-size="13" font-weight="bold" fill="#000000" text-anchor="middle">Fig 2: Proposed System Rich Picture</text>
</svg>"""
