from pathlib import Path


PATCH_TEXT = Path("fix_streamlit_nested_expanders.py").read_text(encoding="utf-8")


def test_scrub_key_helpers_are_imported_by_streamlit_patch():
    assert "from scrub_key import build_scrub_key, scrub_key_to_json, validate_scrub_key" in PATCH_TEXT


def test_scrub_key_ui_block_is_present_near_download_section():
    assert "Scrub Key (JSON)" in PATCH_TEXT
    assert "Download Scrub Key (.json)" in PATCH_TEXT
    assert "solidprivacy_scrub_key.json" in PATCH_TEXT
    assert "application/json" in PATCH_TEXT


def test_scrub_key_export_uses_reviewed_replacements_and_timestamp_in_ui_layer():
    assert "scrub_key_rows = edited_replacements_df.copy()" in PATCH_TEXT
    assert "scrub_key_timestamp = datetime.now(timezone.utc)" in PATCH_TEXT
    assert "build_scrub_key(scrub_key_rows)" in PATCH_TEXT
    assert "scrub_key_to_json(scrub_key)" in PATCH_TEXT
    assert "validate_scrub_key(scrub_key)" in PATCH_TEXT


def test_scrub_key_warning_makes_pseudonymization_boundary_clear():
    assert "pseudonimisering" in PATCH_TEXT
    assert "geen volledige anonimisering" in PATCH_TEXT
    assert "Deel deze sleutel niet met AI-diensten of derden" in PATCH_TEXT


def test_scrub_key_ui_does_not_add_import_or_reinsert_flow():
    assert "scrub_key_from_json" not in PATCH_TEXT
    assert "reinsert" not in PATCH_TEXT.lower()
    assert "AI-output" not in PATCH_TEXT


def test_scrub_key_patch_does_not_remove_existing_download_or_export_markers():
    assert 'st.subheader("4. Download opgeschoonde bestanden")' in PATCH_TEXT
    assert "Eindcontrole vóór download" in PATCH_TEXT
    assert "Extra exportcontrole" in PATCH_TEXT
    assert "st.warning(EXPORT_GUIDANCE)" in PATCH_TEXT


def test_scrub_key_patch_does_not_change_existing_text_export_application():
    assert "export_text = apply_replacements_to_text(st_text, edited_replacements)" not in PATCH_TEXT
    assert "def apply_replacements_to_text" not in PATCH_TEXT
    assert "apply_replacements_to_text =" not in PATCH_TEXT
