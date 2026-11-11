"""
Generate editable Microsoft Word (.docx) documents for:
1. Requirements Elicitation Document
2. Requirements Analysis Document (RAD)
Features exact IUB Cover Page on Page 1 (with official IUB Logo, centered titles,
student metadata, course info, semester, instructor, institution)
and strict Black & White academic styling for all text.
"""

import os
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, color_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_cover_page(doc, doc_title_type):
    # Centered IUB Logo
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "iub_logo.png")
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(12)
        p_logo.paragraph_format.space_after = Pt(20)
        p_logo.add_run().add_picture(logo_path, width=Inches(2.1))
    
    # Document Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(6)
    p_title.paragraph_format.space_after = Pt(28)
    r1 = p_title.add_run(f"{doc_title_type} for\n")
    r1.font.name = "Arial"
    r1.font.size = Pt(16)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(0, 0, 0)
    
    r2 = p_title.add_run("Elderly Care Management System")
    r2.font.name = "Arial"
    r2.font.size = Pt(18)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(0, 0, 0)

    # Prepared By
    p_prep = doc.add_paragraph()
    p_prep.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_prep.paragraph_format.space_before = Pt(8)
    p_prep.paragraph_format.space_after = Pt(24)
    
    r3 = p_prep.add_run("Prepared By\n")
    r3.font.name = "Arial"
    r3.font.size = Pt(13)
    r3.font.bold = True
    r3.font.color.rgb = RGBColor(0, 0, 0)
    
    r4 = p_prep.add_run("Farzana Sadia Takee\n\n")
    r4.font.name = "Arial"
    r4.font.size = Pt(13)
    r4.font.bold = True
    r4.font.color.rgb = RGBColor(0, 0, 0)
    
    r5 = p_prep.add_run("ID- 2211175")
    r5.font.name = "Arial"
    r5.font.size = Pt(12.5)
    r5.font.bold = True
    r5.font.color.rgb = RGBColor(0, 0, 0)

    # Course Details
    p_course = doc.add_paragraph()
    p_course.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_course.paragraph_format.space_before = Pt(8)
    p_course.paragraph_format.space_after = Pt(24)
    
    rc1 = p_course.add_run("Course Code: CSE309\nCourse Title: ")
    rc1.font.name = "Arial"
    rc1.font.size = Pt(12)
    rc1.font.color.rgb = RGBColor(0, 0, 0)
    
    rc2 = p_course.add_run("Web Programming\n")
    rc2.font.name = "Arial"
    rc2.font.size = Pt(12)
    rc2.font.bold = True
    rc2.font.color.rgb = RGBColor(0, 0, 0)
    
    rc3 = p_course.add_run("Section: 02")
    rc3.font.name = "Arial"
    rc3.font.size = Pt(12)
    rc3.font.color.rgb = RGBColor(0, 0, 0)

    # Semester
    p_sem = doc.add_paragraph()
    p_sem.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sem.paragraph_format.space_before = Pt(6)
    p_sem.paragraph_format.space_after = Pt(24)
    r_sem = p_sem.add_run("Autumn 2025")
    r_sem.font.name = "Arial"
    r_sem.font.size = Pt(13)
    r_sem.font.bold = True
    r_sem.font.color.rgb = RGBColor(0, 0, 0)

    # Submitted to
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(6)
    p_sub.paragraph_format.space_after = Pt(6)
    r_sub1 = p_sub.add_run("Submitted to\n\n")
    r_sub1.font.name = "Arial"
    r_sub1.font.size = Pt(11)
    r_sub1.font.color.rgb = RGBColor(0, 0, 0)
    
    r_sub2 = p_sub.add_run("Md Abu Sayed\n\n")
    r_sub2.font.name = "Arial"
    r_sub2.font.size = Pt(13.5)
    r_sub2.font.bold = True
    r_sub2.font.color.rgb = RGBColor(0, 0, 0)
    
    r_sub3 = p_sub.add_run("Independent University Bangladesh")
    r_sub3.font.name = "Arial"
    r_sub3.font.size = Pt(12.5)
    r_sub3.font.color.rgb = RGBColor(0, 0, 0)

    # Page Break after Cover Page
    doc.add_page_break()

def strip_header_metadata(md_content):
    parts = md_content.split('---')
    if len(parts) >= 3:
        return '---'.join(parts[2:]).strip()
    return md_content

def markdown_to_docx(md_path, docx_path, doc_title_type):
    doc = Document()
    
    # Page Margins 1 inch
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # PAGE 1: IUB Official Cover Page
    add_cover_page(doc, doc_title_type)

    with open(md_path, "r", encoding="utf-8") as f:
        full_text = f.read()

    body_text = strip_header_metadata(full_text)
    lines = body_text.splitlines()

    in_table = False
    table_rows = []
    in_code = False
    code_lines = []

    for line in lines:
        stripped = line.strip()

        # Code block handling
        if stripped.startswith("```"):
            if in_code:
                in_code = False
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.2)
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(6)
                r = p.add_run("\n".join(code_lines))
                r.font.name = "Courier New"
                r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor(0, 0, 0)
                code_lines = []
            else:
                in_code = True
                code_lines = []
            continue

        if in_code:
            code_lines.append(line.rstrip())
            continue

        # Table handling
        if "|" in stripped and not stripped.startswith("```"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            # Check if separator row
            if all(re.match(r'^:?-+:?$', c) for c in cells):
                continue
            if not in_table:
                in_table = True
                table_rows = [cells]
            else:
                table_rows.append(cells)
            continue
        else:
            if in_table:
                if len(table_rows) > 0:
                    num_cols = max(len(r) for r in table_rows)
                    t = doc.add_table(rows=len(table_rows), cols=num_cols)
                    t.alignment = WD_TABLE_ALIGNMENT.CENTER
                    t.autofit = True
                    for r_idx, row_data in enumerate(table_rows):
                        for c_idx in range(num_cols):
                            cell_val = row_data[c_idx] if c_idx < len(row_data) else ""
                            cell = t.cell(r_idx, c_idx)
                            p = cell.paragraphs[0]
                            p.paragraph_format.space_before = Pt(2)
                            p.paragraph_format.space_after = Pt(2)
                            
                            clean_val = cell_val.replace("**", "").replace("*", "")
                            run = p.add_run(clean_val)
                            run.font.name = "Arial"
                            run.font.color.rgb = RGBColor(0, 0, 0)
                            
                            if r_idx == 0:
                                set_cell_background(cell, "F0F0F0")
                                run.font.bold = True
                                run.font.size = Pt(9)
                            else:
                                if r_idx % 2 == 0:
                                    set_cell_background(cell, "F9F9F9")
                                run.font.size = Pt(8.5)
                    doc.add_paragraph() # Spacer
                in_table = False
                table_rows = []

        if not stripped:
            continue

        if stripped.startswith("# "):
            h = doc.add_heading(level=1)
            h.paragraph_format.space_before = Pt(14)
            h.paragraph_format.space_after = Pt(6)
            r = h.add_run(stripped[2:].strip())
            r.font.name = "Arial"
            r.font.size = Pt(16)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0, 0, 0)
        elif stripped.startswith("## "):
            h = doc.add_heading(level=2)
            h.paragraph_format.space_before = Pt(12)
            h.paragraph_format.space_after = Pt(4)
            r = h.add_run(stripped[3:].strip())
            r.font.name = "Arial"
            r.font.size = Pt(13)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0, 0, 0)
        elif stripped.startswith("### "):
            h = doc.add_heading(level=3)
            h.paragraph_format.space_before = Pt(10)
            h.paragraph_format.space_after = Pt(3)
            r = h.add_run(stripped[4:].strip())
            r.font.name = "Arial"
            r.font.size = Pt(11)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0, 0, 0)
        elif stripped.startswith("#### "):
            h = doc.add_heading(level=4)
            h.paragraph_format.space_before = Pt(8)
            h.paragraph_format.space_after = Pt(2)
            r = h.add_run(stripped[5:].strip())
            r.font.name = "Arial"
            r.font.size = Pt(10)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0, 0, 0)
        elif stripped.startswith("- ") or stripped.startswith("* "):
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            clean_text = stripped[2:].replace("**", "")
            r = p.add_run(clean_text)
            r.font.name = "Arial"
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(0, 0, 0)
        elif re.match(r'^\d+\.\s', stripped):
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            clean_text = re.sub(r'^\d+\.\s', '', stripped).replace("**", "")
            r = p.add_run(clean_text)
            r.font.name = "Arial"
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(0, 0, 0)
        elif stripped.startswith("---"):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
        else:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.15
            clean_text = stripped.replace("**", "")
            r = p.add_run(clean_text)
            r.font.name = "Arial"
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(0, 0, 0)

    doc.save(docx_path)
    print(f"Generated DOCX: {os.path.basename(docx_path)} ({os.path.getsize(docx_path):,} bytes)")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Requirements Elicitation Document DOCX
    elicitation_md = os.path.join(base_dir, "Requirements_Elicitation_Document.md")
    elicitation_docx = os.path.join(base_dir, "Requirements_Elicitation_Document.docx")
    markdown_to_docx(elicitation_md, elicitation_docx, "Requirements Elicitation Document")

    # 2. Requirements Analysis Document (RAD) DOCX
    rad_md = os.path.join(base_dir, "Requirements_Analysis_Document.md")
    rad_docx = os.path.join(base_dir, "Requirements_Analysis_Document.docx")
    markdown_to_docx(rad_md, rad_docx, "Requirements Analysis Document (RAD)")

if __name__ == "__main__":
    main()
