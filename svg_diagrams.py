import exact_rich_pictures
import exact_fig2_builder
import exact_fig4_builder
import exact_fig5_builder
import exact_fig6_10_builder
import exact_fig11_builder

def get_fig1_existing_system_svg():
    return exact_rich_pictures.get_exact_fig1_existing_rich_picture_svg()

def get_fig2_proposed_system_svg():
    return exact_fig2_builder.get_exact_demo_style_fig2_svg()


def get_fig3_architecture_svg():
    return """<svg viewBox="0 0 500 460" width="100%" height="240" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; font-family:Arial, Helvetica, sans-serif;">
  <defs>
    <marker id="f3-arrow-up" viewBox="0 0 10 10" refX="5" refY="2" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 1.5 8 L 5 0 L 8.5 8 z" fill="#000000"/>
    </marker>
    <marker id="f3-arrow-down" viewBox="0 0 10 10" refX="5" refY="8" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 1.5 0 L 5 8 L 8.5 0 z" fill="#000000"/>
    </marker>
  </defs>

  <!-- 1. PRESENTATION LAYER (Green Box) -->
  <g transform="translate(75, 20)">
    <rect width="350" height="90" fill="#70ae47" stroke="#385723" stroke-width="1.5"/>
    <text x="175" y="52" font-size="18" font-weight="bold" fill="#ffffff" text-anchor="middle">Presentation Layer</text>
  </g>

  <!-- Arrows between Presentation and Application -->
  <!-- Left Arrow Up -->
  <line x1="190" y1="182" x2="190" y2="116" stroke="#000000" stroke-width="1.2" marker-end="url(#f3-arrow-up)"/>
  <!-- Right Arrow Down -->
  <line x1="295" y1="114" x2="295" y2="180" stroke="#000000" stroke-width="1.2" marker-end="url(#f3-arrow-down)"/>

  <!-- 2. APPLICATION LAYER (Orange Box) -->
  <g transform="translate(75, 185)">
    <rect width="350" height="90" fill="#ee7d31" stroke="#c55a11" stroke-width="1.5"/>
    <text x="175" y="52" font-size="18" font-weight="bold" fill="#ffffff" text-anchor="middle">Application Layer</text>
  </g>

  <!-- Arrows between Application and Data -->
  <!-- Left Arrow Up -->
  <line x1="190" y1="347" x2="190" y2="281" stroke="#000000" stroke-width="1.2" marker-end="url(#f3-arrow-up)"/>
  <!-- Right Arrow Down -->
  <line x1="295" y1="279" x2="295" y2="345" stroke="#000000" stroke-width="1.2" marker-end="url(#f3-arrow-down)"/>

  <!-- 3. DATA LAYER (Gray Box) -->
  <g transform="translate(75, 350)">
    <rect width="350" height="90" fill="#a5a5a5" stroke="#595959" stroke-width="1.5"/>
    <text x="175" y="52" font-size="18" font-weight="bold" fill="#ffffff" text-anchor="middle">Data Layer</text>
  </g>
</svg>"""


def get_fig4_sdlc_svg():
    return exact_fig4_builder.get_exact_demo_style_fig4_svg()

def get_fig5_erd_svg():
    return exact_fig5_builder.get_exact_demo_style_fig5_svg()

def get_fig6_dfd_svg():
    return exact_fig6_10_builder.get_exact_demo_style_fig6_svg()

def get_fig7_uc_usermgmt_svg():
    return exact_fig6_10_builder.get_exact_demo_style_fig7_svg()

def get_fig8_uc_medmgmt_svg():
    return exact_fig6_10_builder.get_exact_demo_style_fig8_svg()

def get_fig9_uc_apptmgt_svg():
    return exact_fig6_10_builder.get_exact_demo_style_fig9_svg()

def get_fig10_uc_care_sos_svg():
    return exact_fig6_10_builder.get_exact_demo_style_fig10_svg()

def get_fig11_gantt_svg():
    return exact_fig11_builder.get_exact_demo_style_fig11_svg()

