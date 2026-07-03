from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_TEXT = (REPO_ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")
PLAN_TEXT = (REPO_ROOT / "SECONDARY_CONTROL_GROUPING_POLISH_PLAN.md").read_text(encoding="utf-8")
CONTRACT_TEXT = (REPO_ROOT / "REVIEW_SURFACE_SIMPLIFICATION_CONTRACTS.md").read_text(encoding="utf-8")


def test_secondary_grouping_plan_exists_and_targets_secondary_controls() -> None:
    assert "SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH" in PLAN_TEXT
    assert "secondary controls" in PLAN_TEXT
    assert "Meer controleopties" in PLAN_TEXT
    assert "less visually fragmented" in PLAN_TEXT


def test_plan_forbids_nested_streamlit_expanders() -> None:
    lowered = PLAN_TEXT.lower()

    assert "do not use nested streamlit expanders" in lowered
    assert "avoid `st.expander` inside another `st.expander`" in lowered
    assert "no nested-expander error" in lowered


def test_primary_review_surface_must_remain_visible() -> None:
    for marker in [
        "render_side_by_side_review_panel",
        "2. Controleer resultaat",
        "Markeringen tonen",
    ]:
        assert marker in APP_TEXT or marker in PLAN_TEXT
    assert "side-by-side review as the visible primary review surface" in PLAN_TEXT


def test_manual_entry_and_replacement_table_must_remain_reachable() -> None:
    for marker in [
        "Gemiste waarde toevoegen",
        "manual missed-value entry",
        "Vervangtabel controleren",
        "replacement table remains reachable",
        "source-of-truth",
    ]:
        assert marker in PLAN_TEXT or marker in APP_TEXT


def test_secondary_review_aids_must_remain_available() -> None:
    for marker in [
        "Extra controlehulpen",
        "Mogelijk extra te controleren waarden",
        "Geavanceerde details bij de vervangtabel",
        "Stap voor stap controleren",
        "Herbruikbare vervangingen",
    ]:
        assert marker in PLAN_TEXT or marker in APP_TEXT


def test_export_scrub_key_reinsert_and_audit_boundaries_are_protected() -> None:
    for marker in [
        "export content",
        "download filenames",
        "download MIME types",
        "Scrub Key JSON semantics",
        "Scrub Key warning meaning",
        "reinsert behavior",
        "audit downloads",
        "DOCX hygiene audit",
    ]:
        assert marker in PLAN_TEXT or marker in CONTRACT_TEXT


def test_prohibited_behavior_remains_out_of_scope() -> None:
    lowered = PLAN_TEXT.lower()
    for marker in [
        "cloud processing",
        "ai processing",
        "ocr",
        "restored pdf",
        "pdf-to-docx reconstruction",
        "click-to-mark",
        "advanced editor",
        "full-document marking",
        "hidden export gate",
        "old replacement decision helper panel",
    ]:
        assert marker in lowered


def test_next_package_is_implementation_not_more_planning() -> None:
    assert "SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION" in PLAN_TEXT
    assert "edit only the normal review-control grouping area" in PLAN_TEXT
    assert "use PR validation, Hugging Face sync and live app verification" in PLAN_TEXT
