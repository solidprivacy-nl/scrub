from pathlib import Path


PATCH_TEXT = Path("fix_streamlit_pdf_text_reinsert.py").read_text(encoding="utf-8")
DOCKERFILE_TEXT = Path("Dockerfile").read_text(encoding="utf-8")


def test_pdf_text_reinsert_helper_is_imported_and_used():
    assert "from scrub_key_pdf_text_reinsert import reinsert_pdf_text_bytes" in PATCH_TEXT
    assert "reinsert_pdf_text_bytes(" in PATCH_TEXT
    assert "pdf_text_reinsert_file.getvalue()" in PATCH_TEXT


def test_pdf_text_reinsert_ui_labels_are_present():
    for marker in [
        "PDF-tekst terugzetten naar TXT",
        "PDF-bestand terugzetten naar TXT",
        "Upload een PDF-bestand met placeholders",
        "Zet PDF-tekst lokaal terug",
        "Herstelde TXT-tekst uit PDF",
        "Download herstelde TXT uit PDF (.txt)",
        "Controleverslag PDF-tekst terugzetten",
    ]:
        assert marker in PATCH_TEXT


def test_pdf_text_reinsert_required_warnings_are_present():
    for marker in [
        "PDF-tekstextractie is niet altijd volledig",
        "Opmaak, tabellen, kolommen, headers, footers en visuele volgorde kunnen verloren gaan",
        "Deze functie maakt geen herstelde PDF",
        "De uitvoer is alleen herstelde TXT-tekst",
        "Scans of afbeelding-PDF’s worden niet ondersteund omdat OCR niet beschikbaar is",
        "terugzetten herstelt originele gevoelige waarden",
        "geen AI, geen cloudverwerking en geen OCR",
    ]:
        assert marker in PATCH_TEXT


def test_pdf_text_reinsert_audit_fields_are_present():
    for marker in [
        "document_type",
        "extracted_text_length",
        "replacement_count",
        "item_count",
        "active_item_count",
        "excluded_item_count",
        "placeholders_not_found",
        "unknown_placeholders",
        "duplicate_placeholders",
        "validation_issues",
        "unsupported_reason",
        "local_only",
        "ai_processing",
        "cloud_processing",
        "ocr_used",
        "pdf_output",
        "Documenttype",
        "Lengte geëxtraheerde tekst",
        "Niet-ondersteund reden",
        "Lokaal uitgevoerd",
        "AI-verwerking",
        "Cloudverwerking",
        "OCR gebruikt",
        "PDF-output",
    ]:
        assert marker in PATCH_TEXT


def test_pdf_text_reinsert_shows_local_no_ai_no_cloud_no_ocr_no_pdf_output():
    for marker in [
        "Lokaal uitgevoerd: Ja",
        "AI-verwerking: Nee",
        "Cloudverwerking: Nee",
        "OCR gebruikt: Nee",
        "PDF-output: Nee",
    ]:
        assert marker in PATCH_TEXT


def test_pdf_text_reinsert_accepts_pdf_only_and_requires_key():
    assert 'type=["pdf"]' in PATCH_TEXT
    assert "Laad eerst een geldige Scrub Key" in PATCH_TEXT
    assert "Upload eerst een PDF-bestand met placeholders" in PATCH_TEXT
    assert "active_pdf_text_reinsert_scrub_key" in PATCH_TEXT
    assert 'st.session_state.get("active_scrub_key", {})' in PATCH_TEXT


def test_pdf_text_reinsert_unsupported_case_does_not_offer_successful_download():
    assert "pdf_text_unsupported_reason" in PATCH_TEXT
    assert "pdf_text_can_download = not pdf_text_validation_issues and not pdf_text_unsupported_reason" in PATCH_TEXT
    assert "Geen bruikbare tekstlaag gevonden" in PATCH_TEXT
    assert "Scans of afbeelding-PDF’s worden niet ondersteund" in PATCH_TEXT
    assert "if pdf_text_can_download:" in PATCH_TEXT


def test_pdf_text_reinsert_is_inserted_before_anonymization_else_branch():
    insert_marker = 'pdf_insert_marker = \'\'\''
    assert insert_marker in PATCH_TEXT
    assert "+ pdf_text_reinsert_ui_block" in PATCH_TEXT
    assert "'''else:\\n'''" in PATCH_TEXT


def test_dockerfile_runs_pdf_text_reinsert_patch_after_existing_patch():
    assert "python fix_streamlit_nested_expanders.py && python fix_streamlit_pdf_text_reinsert.py" in DOCKERFILE_TEXT


def test_dockerfile_installs_runtime_pdf_parser_for_approved_ui_path():
    assert "pypdf" in DOCKERFILE_TEXT
    assert "poetry install --no-root" in DOCKERFILE_TEXT


def test_no_restored_pdf_ocr_cloud_ai_or_rehydration_behavior_added():
    lower_patch = PATCH_TEXT.lower()
    forbidden_markers = [
        "download herstelde pdf",
        "download_pdf_reinserted",
        "pdf_to_docx",
        "pytesseract",
        "ocr_used = true",
        "requests.post",
        "httpx.post",
        "cloud processing call",
        "restore_original_document",
        "automatic pdf rehydration",
        "server-side key storage",
        "durable key vault",
        "openai",
        "anthropic",
    ]
    for marker in forbidden_markers:
        assert marker not in lower_patch
    assert "st.stop()" not in PATCH_TEXT
    assert "blocks_export = True" not in PATCH_TEXT
    assert "changes_export_semantics = True" not in PATCH_TEXT
