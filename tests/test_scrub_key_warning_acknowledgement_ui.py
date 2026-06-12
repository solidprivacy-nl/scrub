from pathlib import Path


PATCH_TEXT = Path("fix_streamlit_pdf_text_reinsert.py").read_text(encoding="utf-8")
DOCKERFILE_TEXT = Path("Dockerfile").read_text(encoding="utf-8")


def test_wp28c_post_patch_runs_after_main_scrub_key_ui_patch():
    assert "python fix_streamlit_nested_expanders.py && python fix_streamlit_pdf_text_reinsert.py" in DOCKERFILE_TEXT
    assert "WP28C — MVP Scrub Key warning/acknowledgement UI implementation" in PATCH_TEXT
    assert "after the main Scrub Key/reinsert UI has been injected" in PATCH_TEXT


def test_scrub_key_export_warning_acknowledgement_and_gating_are_present():
    assert "Belangrijk: deze Scrub Key kan originele vertrouwelijke waarden herstellen" in PATCH_TEXT
    assert "Download de sleutel alleen als u deze lokaal, apart en beveiligd kunt bewaren" in PATCH_TEXT
    assert "ack_scrub_key_export_risk" in PATCH_TEXT
    assert "Ik begrijp dat deze Scrub Key herleidbaar is" in PATCH_TEXT
    assert "Download Scrub Key (.json)" in PATCH_TEXT
    assert "disabled=not ack_scrub_key_export_risk" in PATCH_TEXT


def test_scrub_key_export_semantics_are_preserved_after_acknowledgement():
    assert "data=scrub_key_to_json(scrub_key)" in PATCH_TEXT
    assert 'file_name="solidprivacy_scrub_key.json"' in PATCH_TEXT
    assert 'mime="application/json"' in PATCH_TEXT
    assert "disabled=not ack_scrub_key_export_risk" in PATCH_TEXT
    assert "schema_version" not in PATCH_TEXT
    assert "encrypted" not in PATCH_TEXT.lower()
    assert "vault" not in PATCH_TEXT.lower()


def test_scrub_key_import_warning_acknowledgement_and_gating_are_present():
    assert "Laad alleen een Scrub Key die bij dit document of dossier hoort" in PATCH_TEXT
    assert "ack_scrub_key_import_risk" in PATCH_TEXT
    assert "Ik begrijp dat ik alleen een Scrub Key mag laden" in PATCH_TEXT
    assert "Valideer en laad Scrub Key" in PATCH_TEXT
    assert "disabled=not ack_scrub_key_import_risk" in PATCH_TEXT
    assert "build_scrub_key_import_result(scrub_key_import_text)" in PATCH_TEXT


def test_reinsert_mode_entry_warning_and_local_only_copy_are_present():
    assert "terugzetten herstelt originele gevoelige waarden" in PATCH_TEXT
    assert "persoonsgegevens, dossierinformatie of andere vertrouwelijke gegevens" in PATCH_TEXT
    assert "Terugzetten gebeurt lokaal met de geladen Scrub Key" in PATCH_TEXT
    assert "Gebruik de Scrub Key niet in externe AI-diensten" in PATCH_TEXT


def test_reinsert_action_acknowledgement_keys_are_unique_and_gated():
    expected_pairs = {
        "ack_reinsert_text_confidential": "run_local_reinsert",
        "ack_reinsert_txt_confidential": "run_txt_file_reinsert",
        "ack_reinsert_docx_confidential": "run_docx_file_reinsert",
        "ack_reinsert_pdf_text_confidential": "run_pdf_text_file_reinsert",
    }
    for ack_key, button_key in expected_pairs.items():
        assert ack_key in PATCH_TEXT
        assert button_key in PATCH_TEXT
        assert f"disabled=not {ack_key}" in PATCH_TEXT


def test_restored_download_acknowledgement_keys_are_unique_and_gated():
    expected_keys = [
        "ack_download_restored_text_confidential",
        "ack_download_restored_txt_confidential",
        "ack_download_restored_docx_confidential",
        "ack_download_restored_pdf_text_confidential",
    ]
    for ack_key in expected_keys:
        assert ack_key in PATCH_TEXT
        assert f"disabled=not {ack_key}" in PATCH_TEXT
    assert "De herstelde download bevat mogelijk weer originele persoonsgegevens" in PATCH_TEXT
    assert "Ik begrijp dat de download weer vertrouwelijke originele waarden kan bevatten" in PATCH_TEXT


def test_restored_download_file_names_mime_types_and_data_are_preserved():
    for marker in [
        'file_name="solidprivacy_herstelde_tekst.txt"',
        'file_name="solidprivacy_hersteld_txt_bestand.txt"',
        'file_name="solidprivacy_hersteld_docx_bestand.docx"',
        'file_name="solidprivacy_herstelde_txt_uit_pdf.txt"',
        'mime="text/plain"',
        'mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"',
        'data=reinsert_result.get("text", "")',
        'data=txt_reinsert_result.get("content_bytes", txt_reinsert_result.get("text", "").encode("utf-8"))',
        'data=docx_reinsert_result.get("docx_bytes", b"")',
        'data=str(pdf_text_restored_text).encode("utf-8")',
    ]:
        assert marker in PATCH_TEXT


def test_existing_reinsert_helpers_and_audit_fields_remain_visible():
    for marker in [
        "reinsert_from_scrub_key(reinsert_input_text, active_reinsert_scrub_key)",
        "reinsert_txt_bytes(",
        "reinsert_docx_bytes(",
        "reinsert_pdf_text_bytes(",
        "unknown_placeholders",
        "duplicate_placeholders",
        "placeholders_not_found",
        "validation_issues",
        "local_only",
        "ai_processing",
        "cloud_processing",
    ]:
        assert marker in PATCH_TEXT


def test_mismatch_warning_copy_is_strengthened_without_placeholder_repair():
    assert "De tekst bevat placeholders die niet in de geladen Scrub Key staan" in PATCH_TEXT
    assert "Deze waarden kunnen niet automatisch worden teruggezet met deze sleutel" in PATCH_TEXT
    assert "Deze mappings worden niet automatisch teruggezet om verkeerde herleiding te voorkomen" in PATCH_TEXT
    assert "silent repair" not in PATCH_TEXT.lower()
    assert "guess_original" not in PATCH_TEXT.lower()


def test_wp28c_does_not_add_forbidden_security_or_processing_claims():
    lower_patch = PATCH_TEXT.lower()
    for marker in [
        "requests.post",
        "httpx.post",
        "cloud processing call",
        "server-side key storage",
        "durable key vault",
        "key recovery service",
        "auto-delete",
        "automatic deletion",
        "expiry blocking",
        "schema migration",
        "restore_original_document",
        "openai",
        "anthropic",
    ]:
        assert marker not in lower_patch
    assert "st.stop()" not in PATCH_TEXT
    assert "blocks_export = True" not in PATCH_TEXT
    assert "changes_export_semantics = True" not in PATCH_TEXT
