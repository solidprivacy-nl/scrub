from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")
DOCUMENT_TOOLS = (ROOT / "document_tools.py").read_text(encoding="utf-8")
MANUAL = (ROOT / "manual_mask_entry.py").read_text(encoding="utf-8")
HELPER = (ROOT / "scrub_key_bound_export.py").read_text(encoding="utf-8")


def test_app_creates_one_binding_id_before_default_replacements() -> None:
    assert "document_binding_id_for_scope(" in APP
    assert "document_scope_key = manual_mask_document_key(st_text)" in APP
    assert "document_binding_id=document_binding_id" in APP
    assert "build_placeholder_replacements(" in APP


def test_automatic_candidate_remembered_and_manual_paths_are_binding_aware() -> None:
    assert "placeholder_for_entity(" in APP
    assert "placeholder_counts = Counter(" in APP
    assert "bind_existing_placeholder(" in APP
    assert "build_manual_placeholder(" in APP
    assert "document_binding_id," in APP
    assert "document_binding_id=document_binding_id" in APP
    assert "build_bound_placeholder" in DOCUMENT_TOOLS
    assert "build_bound_placeholder" in MANUAL


def test_bound_key_builder_and_validator_replace_legacy_export_builder() -> None:
    assert "build_bound_scrub_key(" in APP
    assert "validate_bound_scrub_key(" in APP
    assert "build_scrub_key as build_export_scrub_key" not in APP
    assert "validate_scrub_key as validate_export_scrub_key" not in APP
    assert 'file_name="solidprivacy_scrub_key.json"' in APP
    assert 'mime="application/json"' in APP


def test_free_custom_replacement_is_not_silently_rewritten() -> None:
    assert "return None" in HELPER
    assert "vrije aangepaste vervangtekst blijft wel in de documentexport staan" in APP
    assert "Alle geselecteerde vervangingen moeten documentgebonden placeholders zijn" in APP


def test_export_integration_adds_no_new_confirmation_gate() -> None:
    forbidden = [
        "Bevestig documentbinding",
        "Valideer documentbinding",
        "Genereer gebonden Scrub Key",
        "ack_document_binding",
    ]
    for marker in forbidden:
        assert marker not in APP


def test_document_export_names_and_mime_types_remain_stable() -> None:
    for marker in [
        'file_name="opgeschoonde_tekst.txt"',
        'docx_filename = "opgeschoonde_tekst.docx"',
        'file_name="opgeschoonde_tekst.pdf"',
        'mime="text/plain"',
        'mime="application/pdf"',
        'mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"',
    ]:
        assert marker in APP
