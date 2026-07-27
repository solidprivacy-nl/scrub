from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UI_PATH = ROOT / "reinsert_mode_ui.py"


def ui_source() -> str:
    return UI_PATH.read_text(encoding="utf-8")


def test_primary_flow_is_document_first_key_second_download_third() -> None:
    source = ui_source()

    document_heading = 'st.subheader("1. Voeg het bestand toe dat je wilt herstellen")'
    key_heading = 'st.subheader("2. Voeg de bijbehorende Scrub Key toe")'
    download_heading = 'st.subheader("3. Download het herstelde resultaat")'

    assert document_heading in source
    assert key_heading in source
    assert download_heading in source
    assert source.index(document_heading) < source.index(key_heading) < source.index(download_heading)


def test_one_document_uploader_recognises_supported_file_types() -> None:
    source = ui_source()

    assert 'key="reinsert_source_file"' in source
    assert 'type=["txt", "docx", "pdf"]' in source
    assert '"Of plak tekst in plaats van een bestand"' in source
    assert "build_reinsert_source(" in source


def test_scrub_key_is_automatically_parsed_and_validated() -> None:
    source = ui_source()

    assert 'key="reinsert_scrub_key_file"' in source
    assert 'type=["json"]' in source
    assert "build_scrub_key_import_result(scrub_key_text)" in source
    assert "_load_scrub_key_automatically(scrub_key_text)" in source
    assert "Scrub Key herkend en geldig" in source


def test_reinsert_runs_automatically_for_one_valid_source_and_key() -> None:
    source = ui_source()

    assert "build_reinsert_request_signature(source, active_key)" in source
    assert "run_reinsert_request(source, active_key)" in source
    assert "auto_reinsert_request_signature" in source


def test_redundant_preprocessing_gates_are_removed() -> None:
    source = ui_source()

    for removed_marker in [
        "ack_scrub_key_import_risk",
        "load_scrub_key_import",
        "Valideer en laad Scrub Key",
        "ack_reinsert_text_confidential",
        "run_local_reinsert",
        "ack_reinsert_txt_confidential",
        "run_txt_file_reinsert",
        "ack_reinsert_docx_confidential",
        "run_docx_file_reinsert",
        "ack_reinsert_pdf_text_confidential",
        "run_pdf_text_file_reinsert",
        "Zet DOCX-bestand lokaal terug",
    ]:
        assert removed_marker not in source


def test_one_final_confidentiality_gate_remains_at_download_boundary() -> None:
    source = ui_source()

    assert source.count("ack_auto_reinsert_download_confidential") == 2
    assert (
        "Ik begrijp dat het herstelde resultaat weer vertrouwelijke originele waarden bevat."
        in source
    )
    assert "disabled=not acknowledged" in source
    assert "CONFIDENTIAL_OUTPUT_WARNING" in source
    assert "RESTORED_DOWNLOAD_WARNING" in source


def test_existing_output_filenames_and_mime_types_are_preserved() -> None:
    source = ui_source()

    for marker in [
        'file_name="solidprivacy_herstelde_tekst.txt"',
        'file_name="solidprivacy_hersteld_txt_bestand.txt"',
        'file_name="solidprivacy_hersteld_docx_bestand.docx"',
        'file_name="solidprivacy_herstelde_txt_uit_pdf.txt"',
        'mime="text/plain"',
        'mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"',
    ]:
        assert marker in source


def test_pdf_and_docx_boundaries_remain_visible() -> None:
    source = ui_source()

    assert "geen herstelde PDF" in source
    assert "OCR is niet beschikbaar" in source
    assert "kop- en voetteksten" in source
    assert "bijgehouden wijzigingen" in source
    assert "metadata" in source
