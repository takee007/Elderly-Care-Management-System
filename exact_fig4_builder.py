# Generate exact Fig 4 SDLC Process Diagram matching demo.pdf p19_0_X98.png pixel-for-pixel

def get_exact_demo_style_fig4_svg():
    return """<svg viewBox="0 0 540 520" width="100%" height="350" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <defs>
    <!-- Arrowhead marker: pointing forward along line direction -->
    <marker id="sdlc-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000000"/>
    </marker>
  </defs>

  <!-- 1. REQUIREMENT ANALYSIS (Orange/Peach #ffe6cc) -->
  <g transform="translate(31, 0)">
    <rect width="210" height="60" fill="#ffe6cc" stroke="#d79b00" stroke-width="1.2"/>
    <text x="105" y="35" font-size="14" fill="#000000" text-anchor="middle">Requirement Analysis</text>
  </g>

  <!-- Step Arrow 1 -> 2 -->
  <line x1="241" y1="30" x2="271" y2="30" stroke="#000000" stroke-width="1.2"/>
  <line x1="271" y1="30" x2="271" y2="88" stroke="#000000" stroke-width="1.2" marker-end="url(#sdlc-arrow)"/>

  <!-- 2. SYSTEM DESIGN (Purple/Lavender #e1d5e7) -->
  <g transform="translate(91, 90)">
    <rect width="210" height="60" fill="#e1d5e7" stroke="#9673a6" stroke-width="1.2"/>
    <text x="105" y="35" font-size="14" fill="#000000" text-anchor="middle">System Design</text>
  </g>

  <!-- Step Arrow 2 -> 3 -->
  <line x1="301" y1="120" x2="327" y2="120" stroke="#000000" stroke-width="1.2"/>
  <line x1="327" y1="120" x2="327" y2="178" stroke="#000000" stroke-width="1.2" marker-end="url(#sdlc-arrow)"/>

  <!-- 3. IMPLEMENTATION (Light Blue #dae8fc) -->
  <g transform="translate(141, 180)">
    <rect width="210" height="60" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.2"/>
    <text x="105" y="35" font-size="14" fill="#000000" text-anchor="middle">Implementation</text>
  </g>

  <!-- Step Arrow 3 -> 4 -->
  <line x1="351" y1="210" x2="376" y2="210" stroke="#000000" stroke-width="1.2"/>
  <line x1="376" y1="210" x2="376" y2="268" stroke="#000000" stroke-width="1.2" marker-end="url(#sdlc-arrow)"/>

  <!-- 4. TESTING (Light Red/Pink #f8cecc) -->
  <g transform="translate(191, 270)">
    <rect width="210" height="60" fill="#f8cecc" stroke="#b85450" stroke-width="1.2"/>
    <text x="105" y="35" font-size="14" fill="#000000" text-anchor="middle">Testing</text>
  </g>

  <!-- Step Arrow 4 -> 5 -->
  <line x1="401" y1="300" x2="439" y2="300" stroke="#000000" stroke-width="1.2"/>
  <line x1="439" y1="300" x2="439" y2="358" stroke="#000000" stroke-width="1.2" marker-end="url(#sdlc-arrow)"/>

  <!-- 5. DEPLOYMENT (Light Yellow #fff2cc) -->
  <g transform="translate(261, 360)">
    <rect width="210" height="60" fill="#fff2cc" stroke="#d6b656" stroke-width="1.2"/>
    <text x="105" y="35" font-size="14" fill="#000000" text-anchor="middle">Deployment</text>
  </g>

  <!-- Step Arrow 5 -> 6 -->
  <line x1="471" y1="390" x2="504" y2="390" stroke="#000000" stroke-width="1.2"/>
  <line x1="504" y1="390" x2="504" y2="448" stroke="#000000" stroke-width="1.2" marker-end="url(#sdlc-arrow)"/>

  <!-- 6. MAINTENANCE (Light Green #d5e8d4) -->
  <g transform="translate(321, 450)">
    <rect width="210" height="60" fill="#d5e8d4" stroke="#82b366" stroke-width="1.2"/>
    <text x="105" y="35" font-size="14" fill="#000000" text-anchor="middle">Maintainance</text>
  </g>

  <!-- ================= FEEDBACK LOOPS (From Maintainance back to each phase) ================= -->

  <!-- Loop 1: Back to Requirement Analysis -->
  <line x1="321" y1="505" x2="11" y2="505" stroke="#000000" stroke-width="1.2"/>
  <line x1="11" y1="505" x2="11" y2="30" stroke="#000000" stroke-width="1.2"/>
  <line x1="11" y1="30" x2="29" y2="30" stroke="#000000" stroke-width="1.2" marker-end="url(#sdlc-arrow)"/>

  <!-- Loop 2: Back to System Design -->
  <line x1="321" y1="490" x2="71" y2="490" stroke="#000000" stroke-width="1.2"/>
  <line x1="71" y1="490" x2="71" y2="120" stroke="#000000" stroke-width="1.2"/>
  <line x1="71" y1="120" x2="89" y2="120" stroke="#000000" stroke-width="1.2" marker-end="url(#sdlc-arrow)"/>

  <!-- Loop 3: Back to Implementation -->
  <line x1="321" y1="480" x2="111" y2="480" stroke="#000000" stroke-width="1.2"/>
  <line x1="111" y1="480" x2="111" y2="210" stroke="#000000" stroke-width="1.2"/>
  <line x1="111" y1="210" x2="139" y2="210" stroke="#000000" stroke-width="1.2" marker-end="url(#sdlc-arrow)"/>

  <!-- Loop 4: Back to Testing -->
  <line x1="321" y1="465" x2="171" y2="465" stroke="#000000" stroke-width="1.2"/>
  <line x1="171" y1="465" x2="171" y2="300" stroke="#000000" stroke-width="1.2"/>
  <line x1="171" y1="300" x2="189" y2="300" stroke="#000000" stroke-width="1.2" marker-end="url(#sdlc-arrow)"/>

  <!-- Loop 5: Back to Deployment -->
  <line x1="321" y1="450" x2="211" y2="450" stroke="#000000" stroke-width="1.2"/>
  <line x1="211" y1="450" x2="211" y2="390" stroke="#000000" stroke-width="1.2"/>
  <line x1="211" y1="390" x2="259" y2="390" stroke="#000000" stroke-width="1.2" marker-end="url(#sdlc-arrow)"/>
</svg>"""
