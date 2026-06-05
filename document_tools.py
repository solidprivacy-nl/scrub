from io import BytesIO, StringIO
from html import escape
import csv

import fitz  # PyMuPDF
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def uploaded_file_to_text(uploaded_file):
    """
    Convert uploaded .txt, .docx, or text-based .pdf to plain text.
    """
    filename = uploaded_file.name.lower()
    data = uploaded_file.getvalue()

    if filename.endswith(".txt"):
        return data.decode("utf-8", errors="ignore"), "txt"

    if filename.endswith(".docx"):
        doc = Document(BytesIO(data))
        return extract_docx_text(doc), "docx"

    if filename.endswith(".pdf"):
        return extract_pdf_text(data), "pdf"

    raise ValueError("Unsupported file type. Please upload .txt, .docx, or .pdf.")


def extract_docx_text(doc):
    parts = []

    for paragraph in iter_docx_paragraphs(doc):
        text = paragraph.text.strip()
        if text:
            parts.append(text)

    return "\n".join(parts)


def extract_pdf_text(pdf_bytes):
    parts = []

    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for page in doc:
            text = page.get_text("text", sort=True)
            if text.strip():
                parts.append(text)

    return "\n\n".join(parts)


def iter_docx_paragraphs(doc):
    """
    Yield paragraphs from body, tables, headers and footers.
    This does not cover every exotic Word object, but it is a good MVP.
    """
    for paragraph in doc.paragraphs:
        yield paragraph

    for table in doc.tables:
        yield from iter_table_paragraphs(table)

    for section in doc.sections:
        header_footer_parts = [
            section.header,
            section.footer,
            section.first_page_header,
            section.first_page_footer,
            section.even_page_header,
            section.even_page_footer,
        ]

        for part in header_footer_parts:
            for paragraph in part.paragraphs:
                yield paragraph
            for table in part.tables:
                yield from iter_table_paragraphs(table)


def iter_table_paragraphs(table):
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                yield paragraph
            for nested_table in cell.tables:
                yield from iter_table_paragraphs(nested_table)


def build_placeholder_replacements(text, analyze_results):
    """
    Build stable placeholders from Presidio results.

    Example:
    John Smith -> [PERSON_01]
    Rotterdam -> [LOCATION_01]
    """
    counters = {}
    replacements = {}
    report_rows = []

    sorted_results = sorted(analyze_results, key=lambda r: (r.start, r.end))

    for result in sorted_results:
        original = text[result.start:result.end].strip()

        if not original:
            continue

        if original in replacements:
            continue

        entity_type = result.entity_type
        counters[entity_type] = counters.get(entity_type, 0) + 1
        placeholder = f"[{entity_type}_{counters[entity_type]:02d}]"

        replacements[original] = placeholder

        report_rows.append(
            {
                "entity_type": entity_type,
                "detected_text": original,
                "placeholder": placeholder,
                "score": round(float(result.score), 3),
            }
        )

    return replacements, report_rows


def apply_replacements_to_text(text, replacements):
    """
    Apply longest replacements first to avoid partial replacement problems.
    """
    output = text

    for original, placeholder in sorted(
        replacements.items(), key=lambda item: len(item[0]), reverse=True
    ):
        output = output.replace(original, placeholder)

    return output


def anonymized_docx_from_original(uploaded_file, replacements):
    """
    Open original .docx and replace detected text inside existing paragraphs/runs.
    This preserves most normal Word formatting, but not all complex Word features.
    """
    doc = Document(BytesIO(uploaded_file.getvalue()))

    for paragraph in iter_docx_paragraphs(doc):
        replace_in_paragraph_runs(paragraph, replacements)

    output = BytesIO()
    doc.save(output)
    output.seek(0)
    return output.getvalue()


def replace_in_paragraph_runs(paragraph, replacements):
    for original, placeholder in sorted(
        replacements.items(), key=lambda item: len(item[0]), reverse=True
    ):
        while replace_once_in_runs(paragraph, original, placeholder):
            pass


def replace_once_in_runs(paragraph, old_text, new_text):
    """
    Replace one occurrence across Word runs.

    Word splits text into runs for formatting. This method tries to replace
    text without rebuilding the whole paragraph.
    """
    if not paragraph.runs:
        return False

    full_text = "".join(run.text for run in paragraph.runs)
    start = full_text.find(old_text)

    if start == -1:
        return False

    end = start + len(old_text)
    current_pos = 0
    replacement_done = False

    for run in paragraph.runs:
        run_text = run.text
        run_start = current_pos
        run_end = current_pos + len(run_text)
        current_pos = run_end

        if run_end <= start or run_start >= end:
            continue

        local_start = max(start - run_start, 0)
        local_end = min(end - run_start, len(run_text))

        before = run_text[:local_start]
        after = run_text[local_end:]

        if not replacement_done:
            if end <= run_end:
                run.text = before + new_text + after
            else:
                run.text = before + new_text
            replacement_done = True
        else:
            if end <= run_end:
                run.text = after
            else:
                run.text = ""

    return True


def docx_from_text(text):
    doc = Document()

    for line in text.splitlines():
        doc.add_paragraph(line)

    output = BytesIO()
    doc.save(output)
    output.seek(0)
    return output.getvalue()


def pdf_from_text(text):
    output = BytesIO()
    pdf = SimpleDocTemplate(output, pagesize=A4)
    styles = getSampleStyleSheet()
    normal = styles["Normal"]

    story = []

    for block in text.splitlines():
        safe_block = escape(block) if block.strip() else "&nbsp;"
        story.append(Paragraph(safe_block, normal))
        story.append(Spacer(1, 6))

    pdf.build(story)
    output.seek(0)
    return output.getvalue()


def replacement_report_csv(report_rows):
    output = StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=["entity_type", "detected_text", "placeholder", "score"],
    )
    writer.writeheader()

    for row in report_rows:
        writer.writerow(row)

    return output.getvalue().encode("utf-8")