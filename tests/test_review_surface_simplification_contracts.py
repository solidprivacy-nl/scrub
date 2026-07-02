from pathlib import Path


APP_TEXT = Path("presidio_streamlit.py").read_text(encoding="utf-8")
SIDE_BY_SIDE_TEXT = Path("side_by_side_review_panel_ui.py").read_text(encoding="utf-8")
SERIAL_REVIEW_TEXT = Path("serial_review_panel_ui.py").read_text(encoding="utf-8")
MANUAL_MASK_TEXT = Path("manual_mask_entry.py").read_text(encoding="utf-8")
PLAN_TEXT = Path("REVIEW_SURFACE_SIMPLIFICATION_PLAN.md").read_text(encoding="utf-8")
CONTRACT_TEXT = Path("REVIEW_SURFACE_SIMPLIFICATION_CONTRACTS.md").read_text(encoding="utf-8")
COMBINED_CONTRACT_TEXT = PLAN_TEXT + "\n" + CONTRACT_TEXT


def test_plan_exists_and_states_three_step_target():
    assert "# SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_PLAN" in PLAN_TEXT
    for marker in ["Voeg document toe", "Controleer resultaat", "Download veilig"]:
        assert marker in COMBINED_CONTRACT_TEXT


def test_review_table_source_of_truth_boundary_is_explicit():
    lowered = COMBINED_CONTRACT_TEXT.lower()
    assert "review table remains source of truth and fallback" in lowered
    assert "replacement table remains reachable" in lowered


def test_side_by_side_review_remains_primary_surface():
    lowered = COMBINED_CONTRACT_TEXT.lower()
    assert "side-by-side review remains the primary" in lowered
    assert "render_side_by_side_review_panel" in APP_TEXT
    assert "Brontekst" in SIDE_BY_SIDE_TEXT
    assert "Verwerkte tekst" in SIDE_BY_SIDE_TEXT


def test_manual_missed_value_entry_remains_available():
    assert "Gemiste waarde toevoegen" in CONTRACT_TEXT
    assert "manual_mask_entry" in COMBINED_CONTRACT_TEXT
    assert "replacement table" in CONTRACT_TEXT
    for marker in [
        "from manual_mask_entry import",
        "build_manual_mask_row",
        "validate_manual_mask_input",
        "manual_mask_document_key",
    ]:
        assert marker in APP_TEXT
    assert "build_manual_mask_row" in MANUAL_MASK_TEXT


def test_export_download_semantics_are_protected():
    for marker in [
        "Export/download semantics must not change",
        "Download filenames must not change",
        "Download MIME types must not change",
        "Export content must not change",
        "Scrub Key JSON semantics must not change",
        "Audit downloads must remain available",
    ]:
        assert marker in CONTRACT_TEXT


def test_scrub_key_remains_separated_and_warning_protected():
    lowered = CONTRACT_TEXT.lower()
    assert "scrub key must remain visually separated" in lowered
    assert "warning-protected" in lowered
    assert "Scrub Key" in APP_TEXT


def test_audit_and_technical_details_remain_available():
    lowered = CONTRACT_TEXT.lower()
    assert "technical/audit details may be collapsed or secondary, but not removed" in lowered
    assert "docx hygiene" in lowered
    assert "audit" in lowered


def test_no_prohibited_behavior_is_allowed_by_contract():
    lowered = CONTRACT_TEXT.lower()
    for marker in [
        "cloud processing",
        "ai processing",
        "ocr",
        "restored pdf",
        "pdf-to-docx reconstruction",
        "direct click-to-mark in document text",
        "advanced editor",
        "full-document marking",
        "export blocking based on a new hidden gate",
    ]:
        assert marker in lowered
    assert "must not introduce or endorse" in lowered


def test_old_replacement_decision_helper_panel_stays_out():
    lowered = CONTRACT_TEXT.lower()
    assert "old replacement decision helper panel must not return" in lowered
    assert "normal user-facing ui" in lowered


def test_future_implementation_must_be_separate():
    lowered = CONTRACT_TEXT.lower()
    assert "this package does not implement ui changes" in lowered
    assert "future implementation requires a separate workpackage" in lowered
    assert "scrub-wp_review_surface_simplification_implementation" in lowered


def test_serial_review_stays_available_as_secondary_review_aid():
    assert "render_serial_review_panel" in APP_TEXT
    assert "Stap voor stap controleren" in SERIAL_REVIEW_TEXT
    assert "secondary" in CONTRACT_TEXT.lower() or "secondary" in PLAN_TEXT.lower()
