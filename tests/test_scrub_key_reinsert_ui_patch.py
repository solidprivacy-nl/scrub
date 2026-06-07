from pathlib import Path


PATCH_TEXT = Path("fix_streamlit_nested_expanders.py").read_text(encoding="utf-8")


def test_reinsert_helper_is_imported_and_used_by_streamlit_patch():
    assert "from scrub_key_reinsert import reinsert_from_scrub_key" in PATCH_TEXT
    assert "reinsert_from_scrub_key(reinsert_input_text, active_reinsert_scrub_key)" in PATCH_TEXT


def test_reinsert_ui_labels_are_present():
    assert "Originele waarden terugzetten" in PATCH_TEXT
    assert "Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten" in PATCH_TEXT
    assert "Zet originele waarden lokaal terug" in PATCH_TEXT
    assert "Herstelde tekst" in PATCH_TEXT
    assert "Download herstelde tekst (.txt)" in PATCH_TEXT


def test_reinsert_warning_mentions_sensitive_and_confidential_output():
    assert "terugzetten herstelt originele gevoelige waarden" in PATCH_TEXT
    assert "persoonsgegevens of vertrouwelijke informatie" in PATCH_TEXT
    assert "Controleer het resultaat zorgvuldig voordat u het deelt" in PATCH_TEXT


def test_reinsert_ui_contains_local_only_no_ai_no_cloud_wording():
    assert "lokaal uitgevoerd" in PATCH_TEXT.lower()
    assert "geen AI- of cloudverwerking" in PATCH_TEXT
    assert "AI-verwerking" in PATCH_TEXT
    assert "Cloudverwerking" in PATCH_TEXT


def test_reinsert_requires_explicit_button_before_helper_call():
    button_index = PATCH_TEXT.index('st.button("Zet originele waarden lokaal terug", key="run_local_reinsert")')
    helper_index = PATCH_TEXT.index("reinsert_from_scrub_key(reinsert_input_text, active_reinsert_scrub_key)")
    assert button_index < helper_index


def test_reinsert_ui_shows_required_audit_summary_fields():
    for marker in [
        "Controleverslag terugzetten",
        "Mappingregels totaal",
        "Actieve mappingregels",
        "Uitgesloten mappingregels",
        "Aantal teruggezette waarden",
        "Niet gevonden placeholders",
        "Onbekende placeholders in tekst",
        "Dubbele placeholders in sleutel",
        "Validatieproblemen",
        "Lokaal uitgevoerd",
        "AI-verwerking",
        "Cloudverwerking",
        "replacement_count",
        "item_count",
        "active_item_count",
        "excluded_item_count",
        "placeholders_not_found",
        "unknown_placeholders",
        "duplicate_placeholders",
        "validation_issues",
        "local_only",
        "ai_processing",
        "cloud_processing",
    ]:
        assert marker in PATCH_TEXT


def test_reinsert_ui_keeps_existing_scrub_key_export_and_import_labels():
    assert "Scrub Key (JSON)" in PATCH_TEXT
    assert "Download Scrub Key (.json)" in PATCH_TEXT
    assert "Scrub Key laden" in PATCH_TEXT
    assert "Upload Scrub Key JSON (.json)" in PATCH_TEXT
    assert "Of plak Scrub Key JSON" in PATCH_TEXT
    assert "Valideer en laad Scrub Key" in PATCH_TEXT


def test_reinsert_ui_keeps_existing_download_and_export_markers_unblocked():
    assert 'st.subheader("4. Download opgeschoonde bestanden")' in PATCH_TEXT
    assert "Eindcontrole vóór download" in PATCH_TEXT
    assert "Extra exportcontrole" in PATCH_TEXT
    assert "st.warning(EXPORT_GUIDANCE)" in PATCH_TEXT
    assert "st.stop()" not in PATCH_TEXT
    assert "blocks_export = True" not in PATCH_TEXT
    assert "changes_export_semantics = True" not in PATCH_TEXT


def test_reinsert_ui_does_not_add_ai_calls_cloud_calls_or_document_rehydration():
    forbidden_markers = [
        "openai",
        "anthropic",
        "requests.post",
        "httpx.post",
        "cloud processing call",
        "rehydrat",
        "restore_original_document",
        "download_docx_reinserted",
        "download_pdf_reinserted",
    ]
    lower_patch = PATCH_TEXT.lower()
    for marker in forbidden_markers:
        assert marker.lower() not in lower_patch


def test_reinsert_patch_does_not_alter_existing_replacement_application_or_scrubbed_download_functions():
    assert "def apply_replacements_to_text" not in PATCH_TEXT
    assert "apply_replacements_to_text =" not in PATCH_TEXT
    assert "export_text = apply_replacements_to_text" not in PATCH_TEXT
    assert "download_txt" not in PATCH_TEXT
    assert "download_csv" not in PATCH_TEXT
    assert "download_docx" not in PATCH_TEXT
    assert "download_pdf" not in PATCH_TEXT
