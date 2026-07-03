from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PLAN_TEXT = (REPO_ROOT / "BASIC_EXPERT_REVIEW_MODE_PLAN.md").read_text(encoding="utf-8")
APP_TEXT = (REPO_ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")
SIDE_BY_SIDE_TEXT = (REPO_ROOT / "side_by_side_review_panel_ui.py").read_text(encoding="utf-8")
SERIAL_REVIEW_TEXT = (REPO_ROOT / "serial_review_panel_ui.py").read_text(encoding="utf-8")
MANUAL_MASK_TEXT = (REPO_ROOT / "manual_mask_entry.py").read_text(encoding="utf-8")


def test_plan_exists_and_recommends_basiscontrole_expertcontrole() -> None:
    assert "# SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_PLAN" in PLAN_TEXT
    assert "Basiscontrole" in PLAN_TEXT
    assert "Expertcontrole" in PLAN_TEXT
    assert "Basiscontrole is not weaker review." in PLAN_TEXT
    assert "Basiscontrole is lower cognitive load with the same safety boundaries." in PLAN_TEXT
    assert "Expertcontrole is full inspection, tuning, audit and troubleshooting." in PLAN_TEXT


def test_basiscontrole_default_flow_is_protected() -> None:
    for marker in [
        "Basiscontrole should become the default user-facing MVP flow",
        "1. Voeg document toe",
        "2. Controleer resultaat",
        "3. Download veilig",
        "side-by-side review",
        "Markeringen tonen",
        "Gemiste waarde toevoegen",
        "Details aanpassen",
    ]:
        assert marker in PLAN_TEXT


def test_expertcontrole_full_control_scope_is_protected() -> None:
    for marker in [
        "full replacement table",
        "include/remember/find/replace_with review",
        "candidate audit values",
        "recognition details",
        "thresholds/settings",
        "Scrub Key details",
        "audit downloads",
        "DOCX hygiene audit",
        "serial review",
        "troubleshooting and legal/privacy audit work",
    ]:
        assert marker in PLAN_TEXT


def test_mode_switch_visibility_only_boundary_is_explicit() -> None:
    for marker in [
        "Switching modes must not reset uploaded text, replacement decisions or session state.",
        "Switching modes changes visibility/grouping only.",
        "recognizer behavior",
        "replacement logic",
        "export output",
        "Scrub Key JSON",
        "reinsert behavior",
        "audit generation",
        "Mode selection should be treated as UI state, not processing state.",
    ]:
        assert marker in PLAN_TEXT


def test_basis_secondary_grouping_is_defined() -> None:
    for marker in [
        "Details aanpassen",
        "Vervangtabel controleren",
        "Stap voor stap controleren",
        "Mogelijk extra te controleren waarden",
        "Herbruikbare vervangingen",
        "Meer bestanden",
        "Scrub Key downloaden",
        "Audit en technische bestanden",
        "Technische informatie",
        "Geavanceerde herkenningsdetails",
    ]:
        assert marker in PLAN_TEXT


def test_conditional_disclosure_is_required() -> None:
    for marker in [
        "DOCX hygiene audit only appears for DOCX or DOCX-derived flows",
        "PDF limitations only appear for PDF input",
        "candidate audit values only appear when candidates exist",
        "Scrub Key warning appears when the Scrub Key section is opened",
        "recognition details are primarily in Expertcontrole",
    ]:
        assert marker in PLAN_TEXT


def test_safety_boundaries_are_explicit() -> None:
    for marker in [
        "legal/professional context",
        "review table as source of truth internally",
        "manual missed-value correction",
        "export/download semantics",
        "Scrub Key warning protection",
        "local-only/no-cloud/no-AI boundary",
        "no OCR",
        "no restored PDF promise",
        "no PDF-to-DOCX reconstruction",
        "no hidden export gate",
        "no advanced editor",
        "no click-to-mark implementation",
        "no full-document marking",
    ]:
        assert marker in PLAN_TEXT


def test_implementation_sequence_requires_contract_tests_first() -> None:
    assert "SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_CONTRACT_TESTS" in PLAN_TEXT
    assert "SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_IMPLEMENTATION" in PLAN_TEXT
    assert "SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_APP_VERIFY_CLOSEOUT" in PLAN_TEXT
    assert "Implementation must not start until contract tests are merged." in PLAN_TEXT


def test_current_ui_paths_still_exist_for_future_mode_split() -> None:
    for marker in [
        "render_side_by_side_review_panel",
        "2. Controleer resultaat",
        "Markeringen tonen",
        "Gemiste waarde toevoegen",
        "Vervangtabel controleren",
        "Scrub Key downloaden",
        "Document downloaden",
        "Audit en technische bestanden",
        "render_docx_hygiene_audit_panel",
    ]:
        assert marker in APP_TEXT or marker in SIDE_BY_SIDE_TEXT
    assert "Stap voor stap controleren" in SERIAL_REVIEW_TEXT
    assert "build_manual_mask_row" in MANUAL_MASK_TEXT


def test_contract_package_does_not_approve_implementation_yet() -> None:
    for marker in [
        "Do not implement the mode switch until contract tests are merged.",
        "mode switch is visibility-only",
        "no export/Scrub Key/reinsert/recognizer/benchmark/runtime semantics changed",
    ]:
        assert marker in PLAN_TEXT
