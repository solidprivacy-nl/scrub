from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "PROCESSED_TEXT_SELECTION_MASKING_PLAN.md"


def _plan() -> str:
    return PLAN.read_text(encoding="utf-8")


def test_plan_exists_and_is_planning_only():
    text = _plan()
    assert "Status: planning and discussion only" in text
    assert "This plan does not authorize implementation" in text


def test_plan_keeps_review_table_authoritative():
    text = _plan()
    lowered = text.lower()
    assert "review table remains the source of truth and fallback" in lowered
    assert "already verified manual-mask path" in lowered


def test_first_version_is_all_exact_only():
    text = _plan()
    assert "Mask all exact occurrences" in text
    assert '"requested_scope": "all_exact"' in text
    assert "Do not support “only this occurrence” yet" in text


def test_occurrence_specific_semantics_are_explicitly_deferred():
    text = _plan()
    assert "span-aware replacement model" in text
    assert "occurrence-specific replacement" in text
    assert "separate architecture project" in text


def test_component_is_bounded_and_server_authoritative():
    text = _plan()
    assert "bidirectional Streamlit custom component" in text
    assert "Frontend values are untrusted input" in text
    assert "The component may not" in text
    assert "Python remains authoritative" in text


def test_no_streamlit_upgrade_is_combined_with_feature():
    text = _plan()
    assert "Do not combine this feature with a Streamlit major/minor upgrade" in text
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    lockfile = (ROOT / "poetry.lock").read_text(encoding="utf-8")
    assert 'streamlit = "^1.39.0"' in pyproject
    assert 'name = "streamlit"' in lockfile
    assert 'version = "1.39.0"' in lockfile


def test_current_static_component_limitation_is_grounded():
    text = _plan()
    current_ui = (ROOT / "side_by_side_review_panel_ui.py").read_text(encoding="utf-8")
    assert "components.html" in current_ui
    assert "visual_only" in current_ui
    assert "mutation_allowed" in current_ui
    assert "components.html" in text


def test_existing_manual_row_path_is_reused():
    text = _plan()
    helper = (ROOT / "manual_mask_entry.py").read_text(encoding="utf-8")
    assert "build_manual_mask_row" in helper
    assert "manual_mask_document_key" in helper
    assert "build_manual_mask_row" in text
    assert "document-bound placeholder" in text


def test_collision_replay_and_stale_guards_are_required():
    text = _plan()
    assert "embedded-substring collision" in text
    assert "replayed event ID" in text
    assert "stale document scope" in text
    assert "stale preview hash" in text


def test_security_contract_blocks_external_data_paths():
    text = _plan()
    assert "No analytics, telemetry, CDN" in text
    assert "local storage" in text
    assert "session storage" in text
    assert "No selection or document content leaves the existing Streamlit session" in text


def test_scrub_key_export_and_reinsert_semantics_remain_unchanged():
    text = _plan()
    assert "No Scrub Key schema, digest, binding or warning changes" in text
    assert "no output filename, MIME type or supported-format change" in text
    assert "reinsert continues through the normal bound Scrub Key mapping" in text


def test_plan_defines_sequential_workpackages_and_explicit_approval_gate():
    text = _plan()
    expected = (
        "SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT",
        "SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL",
        "SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE",
        "SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION",
        "SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION",
        "SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY",
    )
    for workpackage in expected:
        assert workpackage in text
    assert "explicit coordinator approval" in text.lower()
