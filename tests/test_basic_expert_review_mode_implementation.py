from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SIDE_BY_SIDE_TEXT = (REPO_ROOT / "side_by_side_review_panel_ui.py").read_text(encoding="utf-8")
APP_TEXT = (REPO_ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")
CONTRACT_TEXT = (REPO_ROOT / "tests/test_basic_expert_review_mode_contracts.py").read_text(encoding="utf-8")


def test_review_mode_selector_is_visible_and_defaults_to_basiscontrole() -> None:
    assert "def render_review_mode_selector" in SIDE_BY_SIDE_TEXT
    assert "Controleweergave" in SIDE_BY_SIDE_TEXT
    assert "Basiscontrole" in SIDE_BY_SIDE_TEXT
    assert "Expertcontrole" in SIDE_BY_SIDE_TEXT
    assert "REVIEW_MODE_OPTIONS" in SIDE_BY_SIDE_TEXT
    assert "index=0" in SIDE_BY_SIDE_TEXT
    assert "solidprivacy_review_mode" in SIDE_BY_SIDE_TEXT


def test_mode_selector_is_visibility_only() -> None:
    for marker in [
        "Deze keuze wijzigt alleen zichtbaarheid en groepering.",
        "mode_switch_visibility_only",
        "mutation_allowed": False,
        "review_table_mutation": False,
        "replacement_mutation": False,
        "scrub_key_writes": False,
        "export_download_behavior_change": False,
        "reinsert_behavior_change": False,
    ]:
        assert str(marker) in SIDE_BY_SIDE_TEXT


def test_basis_and_expert_copy_explain_user_paths() -> None:
    for marker in [
        "Basiscontrole: controleer de gemarkeerde tekst",
        "voeg gemiste waarden toe",
        "download daarna veilig",
        "Expertcontrole: alle detailcontroles",
        "auditinformatie",
        "technische hulpmiddelen",
    ]:
        assert marker in SIDE_BY_SIDE_TEXT


def test_side_by_side_review_remains_primary_surface() -> None:
    for marker in [
        "Markeringen tonen",
        "Brontekst",
        "Verwerkte tekst",
        "render_side_by_side_review_panel",
        "build_side_by_side_review_model",
        "build_preview_text",
    ]:
        assert marker in SIDE_BY_SIDE_TEXT


def test_existing_app_processing_and_export_paths_are_not_changed_by_mode_selector() -> None:
    for marker in [
        "analyze(",
        "build_placeholder_replacements",
        "apply_replacements_to_text",
        "build_export_scrub_key",
        "export_key_json",
        "reinsert_from_scrub_key",
        "Document downloaden",
        "Scrub Key downloaden",
        "Audit en technische bestanden",
    ]:
        assert marker in APP_TEXT


def test_contract_tests_remain_the_guardrail_for_future_deeper_split() -> None:
    for marker in [
        "Basiscontrole is not weaker review.",
        "Switching modes changes visibility/grouping only.",
        "Implementation must not start until contract tests are merged.",
        "no export/Scrub Key/reinsert/recognizer/benchmark/runtime semantics changed",
    ]:
        assert marker in CONTRACT_TEXT


def test_no_prohibited_behavior_is_introduced_in_review_mode_ui() -> None:
    lower = SIDE_BY_SIDE_TEXT.lower()
    for forbidden in [
        "cloud processing",
        "ai processing",
        "ocr",
        "restored pdf",
        "pdf-to-docx",
        "click-to-mark",
        "advanced editor",
        "full-document marking",
        "hidden export gate",
    ]:
        assert forbidden not in lower
