import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_PATH = ROOT / "output" / "validation" / "care_profile_current_ui_integration.json"


def test_care_profile_ui_integration_snapshot_preserves_product_boundaries():
    snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))

    assert snapshot["schema_version"] == "1.0"
    assert snapshot["profile_count"] == 4
    assert snapshot["visible_profile_labels"] == [
        "Zorgcontrole — streng",
        "Juridische controle — streng",
        "Algemene Nederlandse controle",
        "Algemene internationale controle",
    ]
    assert snapshot["default_profile_label"] == "Juridische controle — streng"
    assert snapshot["dedicated_care_entity_count"] == 16
    assert snapshot["synthetic_care_example_count"] == 8
    assert snapshot["care_candidates_selected_by_default"] is False
    assert snapshot["review_selected_detections_selected_by_default"] is True
    assert snapshot["review_selected_status_label"] == "Controle nodig"
    assert snapshot["patient_identity_selected_for_replacement"] is True
    assert snapshot["clinical_meaning_preservation_required"] is True
    assert snapshot["export_semantics_changed"] is False
    assert snapshot["scrub_key_semantics_changed"] is False
    assert snapshot["reinsert_semantics_changed"] is False
    assert snapshot["cloud_document_processing_added"] is False
    assert snapshot["human_review_required"] is True
    assert snapshot["production_ready"] is False


def test_streamlit_source_exposes_care_without_silent_default_switch():
    source = (ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")

    assert "PROFILE_OPTIONS = current_profile_options_with_care()" in source
    assert 'profile_label = st.session_state.get("_premium_profile_label", profile_options[1])' in source
    assert 'profile_label = profile_options[1]' in source
    assert 'if st_recognition_profile == "Dutch Care Strict":' in source
    assert "care_example_names()" in source
    assert "resolve_configured_analysis_results(" in source
    assert "detected_review_status(" in source


def test_export_scrub_key_and_reinsert_imports_remain_present():
    source = (ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")

    assert "from scrub_key_bound_export import" in source
    assert "from scrub_key_import import" in source
    assert "from scrub_key_reinsert import" in source
    assert "from scrub_key_document_reinsert import" in source
    assert 'st.subheader("3. Exporteer resultaat")' in source
