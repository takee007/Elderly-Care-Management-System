import os
import subprocess
import tempfile
import svg_diagrams

def render_svg_to_png(svg_html_snippet, output_png, width=800, height=420):
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ margin: 0; padding: 0; background: white; }}
  .container {{ width: {width}px; height: {height}px; display: flex; align-items: center; justify-content: center; }}
</style>
</head>
<body>
<div class="container">
{svg_html_snippet}
</div>
</body>
</html>"""
    
    tmp_html = output_png.replace(".png", ".html")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html)
        
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    tmp_user_dir = tempfile.mkdtemp()
    
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={tmp_user_dir}",
        f"--window-size={width},{height}",
        f"--screenshot={os.path.abspath(output_png)}",
        f"file:///{os.path.abspath(tmp_html).replace(os.sep, '/')}"
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=20)
    if os.path.exists(tmp_html):
        os.remove(tmp_html)
    
    if os.path.exists(output_png):
        print(f"Generated {output_png} ({os.path.getsize(output_png):,} bytes)")
        return True
    return False

def main():
    os.makedirs("figures_png", exist_ok=True)
    
    diagrams = [
        ("figures_png/fig_context_diagram.png", None, 1960, 1440),
        ("figures_png/fig1_existing_system.png", svg_diagrams.get_fig1_existing_system_svg(), 800, 420),
        ("figures_png/fig2_proposed_system.png", svg_diagrams.get_fig2_proposed_system_svg(), 800, 420),
        ("figures_png/fig3_system_architecture.png", svg_diagrams.get_fig3_architecture_svg(), 800, 420),
        ("figures_png/fig4_sdlc_process.png", svg_diagrams.get_fig4_sdlc_svg(), 800, 420),
        ("figures_png/fig5_er_diagram.png", svg_diagrams.get_fig5_erd_svg(), 800, 420),
        ("figures_png/fig6_data_flow_diagram.png", svg_diagrams.get_fig6_dfd_svg(), 800, 420),
        ("figures_png/fig7_uc_usermgmt.png", svg_diagrams.get_fig7_uc_usermgmt_svg(), 750, 300),
        ("figures_png/fig8_uc_medmgmt.png", svg_diagrams.get_fig8_uc_medmgmt_svg(), 750, 240),
        ("figures_png/fig9_uc_apptmgt.png", svg_diagrams.get_fig9_uc_apptmgt_svg(), 750, 240),
        ("figures_png/fig10_uc_care_sos.png", svg_diagrams.get_fig10_uc_care_sos_svg(), 750, 250),
        ("figures_png/fig11_gantt_chart.png", svg_diagrams.get_fig11_gantt_svg(), 800, 300),
    ]
    
    for path, svg, w, h in diagrams:
        if "context" in path:
            import build_crystal_clear_context_diagram
            build_crystal_clear_context_diagram.render_high_res_png()
        elif "fig5" in path:
            import build_crystal_clear_fig5
            build_crystal_clear_fig5.render_high_res_png()
        elif "fig6" in path:
            import build_crystal_clear_fig6
            build_crystal_clear_fig6.render_high_res_png()
        elif "fig11" in path:
            import exact_fig11_builder
            exact_fig11_builder.render_gantt_png(path)
        else:
            render_svg_to_png(svg, path, w, h)

if __name__ == "__main__":
    main()

