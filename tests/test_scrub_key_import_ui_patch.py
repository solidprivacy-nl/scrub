from pathlib import Path


PATCH_TEXT = Path("fix_streamlit_nested_expanders.py").read_text(encoding="utf-8")


def test_scrub_key_import_helper_is_used_by_streamlit_patch():
    assert "from scrub_key_import import IMPORT_PRIVACY_WARNING, build_scrub_key_import_result" in PATCH_TEXT
    assert "build_scrub_key_import_result(scrub_key_import_text)" in PATCH_TEXT


def test_scrub_key_load_ui_label_and_input_paths_are_present():
    assert "Scrub Key laden" in PATCH_TEXT
    assert "Upload Scrub Key JSON (.json)" in PATCH_TEXT
    assert "Of plak Scrub Key JSON" in PATCH_TEXT
    assert "Valideer en laad Scrub Key" in PATCH_TEXT


def test_scrub_key_load_ui_contains_pseudonymization_and_local_key_warnings():
    assert "lokaal herleidbaar" in PATCH_TEXT
    assert "pseudonimisering" in PATCH_TEXT
    assert "geen volledige anonimisering" in PATCH_TEXT
    assert "Bewaar deze sleutel lokaal" in PATCH_TEXT
    assert "AI-diensten of derden" in PATCH_TEXT


def test_imported_scrub_key_is_validated_before_rows_are_loaded():
    validation_index = PATCH_TEXT.index("build_scrub_key_import_result(scrub_key_import_text)")
    ok_check_index = PATCH_TEXT.index('scrub_key_import_result.get("ok")')
    load_index = PATCH_TEXT.index('st.session_state["scrub_key_import_rows"]')

    assert validation_index < ok_check_index < load_index
    assert 'scrub_key_import_result.get("mapping_rows", [])' in PATCH_TEXT


def test_imported_rows_are_loaded_into_review_table_without_silent_replacement():
    assert 'if st.button("Valideer en laad Scrub Key", key="load_scrub_key_import")' in PATCH_TEXT
    assert 'if "scrub_key_import_rows" in st.session_state' in PATCH_TEXT
    assert "default_editor_rows.append(imported_row)" in PATCH_TEXT
    assert "replacement_editor" in PATCH_TEXT


def test_scrub_key_import_ui_does_not_add_ai_output_or_rehydrate_flow():
    assert "AI-output" not in PATCH_TEXT
    assert "rehydrat" not in PATCH_TEXT.lower()
    assert "restore_original" not in PATCH_TEXT
    assert "scrub_key_from_json" not in PATCH_TEXT


def test_existing_scrub_key_export_block_is_kept():
    assert "Scrub Key (JSON)" in PATCH_TEXT
    assert "Download Scrub Key (.json)" in PATCH_TEXT
    assert "scrub_key_to_json(scrub_key)" in PATCH_TEXT
    assert "solidprivacy_scrub_key.json" in PATCH_TEXT


def test_existing_download_and_export_markers_are_kept_unblocked():
    assert 'st.subheader("4. Download opgeschoonde bestanden")' in PATCH_TEXT
    assert "Eindcontrole vóór download" in PATCH_TEXT
    assert "Extra exportcontrole" in PATCH_TEXT
    assert "st.warning(EXPORT_GUIDANCE)" in PATCH_TEXT
    assert "st.stop()" not in PATCH_TEXT
    assert "blocks_export = True" not in PATCH_TEXT


def test_patch_does_not_alter_existing_replacement_application_or_download_functions():
    assert "def apply_replacements_to_text" not in PATCH_TEXT
    assert "apply_replacements_to_text =" not in PATCH_TEXT
    assert "export_text = apply_replacements_to_text" not in PATCH_TEXT
    assert "download_txt" not in PATCH_TEXT
    assert "download_csv" not in PATCH_TEXT
    assert "download_docx" not in PATCH_TEXT
    assert "download_pdf" not in PATCH_TEXT
