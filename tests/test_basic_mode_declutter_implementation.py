from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_TEXT = (REPO_ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")
SIDE_BY_SIDE_TEXT = (REPO_ROOT / "side_by_side_review_panel_ui.py").read_text(encoding="utf-8")


def test_review_mode_state_is_captured_from_side_by_side_panel() -> None:
    assert "side_by_side_review_state = render_side_by_side_review_panel(" in APP_TEXT
    assert 'review_mode = side_by_side_review_state.get("review_mode", "Basiscontrole")' in APP_TEXT
    assert 'is_expert_review = review_mode == "Expertcontrole"' in APP_TEXT
    assert "is_basic_review = not is_expert_review" in APP_TEXT


def test_basiscontrole_default_and_session_key_remain_in_side_by_side_selector() -> None:
    for marker in [
        "Basiscontrole",
        "Expertcontrole",
        "REVIEW_MODE_OPTIONS",
        "index=0",
        "solidprivacy_review_mode",
        "mode_switch_visibility_only",
    ]:
        assert marker in SIDE_BY_SIDE_TEXT


def test_basiscontrole_uses_calmer_replacement_table_label() -> None:
    assert "replacement_table_label = (" in APP_TEXT
    assert "Details aanpassen — vervangtabel" in APP_TEXT
    assert "Vervangtabel controleren —" in APP_TEXT


def test_manual_missed_value_entry_remains_available_outside_expert_guard() -> None:
    assert 'with st.expander("Gemiste waarde toevoegen", expanded=False):' in APP_TEXT
    assert 'with st.expander("Gemiste waarde toevoegen", expanded=False):' in APP_TEXT.split(
        'with st.expander("Extra controlehulpen", expanded=False):'
    )[0]


def test_expert_only_review_controls_are_guarded() -> None:
    guarded_markers = [
        'with st.expander("Waarom controleren?"',
        'with st.expander("Extra controlehulpen"',
        'with st.expander("Geavanceerde details bij de vervangtabel"',
        "render_serial_review_panel(",
        'with st.expander("Herbruikbare vervangingen"',
        'with st.expander("Technische informatie"',
    ]

    for marker in guarded_markers:
        marker_index = APP_TEXT.find(marker)
        assert marker_index >= 0, marker
        nearby_prefix = APP_TEXT[max(0, marker_index - 160):marker_index]
        assert "if is_expert_review:" in nearby_prefix, marker

    assert 'if st_operator not in ("highlight", "synthesize") and is_expert_review:' in APP_TEXT


def test_candidate_values_are_contextual_in_basiscontrole() -> None:
    assert "if is_expert_review or candidate_rows:" in APP_TEXT
    assert "Mogelijk extra te controleren waarden" in APP_TEXT
    assert "Geen mogelijke gemiste referenties gevonden door de auditlaag." in APP_TEXT


def test_document_scrub_key_audit_and_docx_hygiene_remain_available() -> None:
    for marker in [
        "Document downloaden",
        "Download opgeschoonde tekst (.txt)",
        "Download opgeschoond Word-bestand (.docx)",
        "Download opgeschoonde PDF (.pdf)",
        "Scrub Key downloaden",
        "Download Scrub Key (.json)",
        "Audit en technische bestanden",
        "Download vervangtabel (.csv)",
        "Download scrubrapport (.txt)",
        "render_docx_hygiene_audit_panel(docx_bytes, source_label=docx_filename)",
    ]:
        assert marker in APP_TEXT


def test_export_scrub_key_reinsert_and_recognizer_paths_remain_present() -> None:
    for marker in [
        "analyze(",
        "build_placeholder_replacements",
        "apply_replacements_to_text",
        "build_bound_scrub_key",
        "export_key_json",
        "reinsert_from_scrub_key",
        "reinsert_docx_bytes",
        "reinsert_txt_bytes",
        "replacement_report_csv",
        "scrub_report_txt",
    ]:
        assert marker in APP_TEXT


def test_no_nested_expander_grouping_is_introduced() -> None:
    lowered = APP_TEXT.lower()
    assert 'with st.expander("meer controleopties"' not in lowered
    assert 'st.expander("meer controleopties"' not in lowered
