from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SPEC = REPO_ROOT / "STREAMLIT_FEASIBILITY_BOUNDARY_REVIEW.md"


def _text() -> str:
    return SPEC.read_text(encoding="utf-8")


def test_wp42_allows_only_small_static_read_only_highlight_preview():
    text = _text().lower()

    assert "small static read-only highlight review preview" in text
    assert "static/read-only highlight preview" in text
    assert "synthetic text or extracted main text only" in text
    assert "no mutation" in text
    assert "current review table remains authoritative" in text


def test_wp42_blocks_broad_streamlit_document_ui_and_mutation():
    text = _text().lower()

    for phrase in [
        "not yet feasible as the long-term professional document-centric review interface",
        "broad document ui rewrite",
        "click-to-mark sensitive text",
        "multi-pane synchronized editing",
        "mutation of review decisions from highlights",
        "export blocking based on highlight state",
        "changing include/replace decisions from the highlight pane",
        "direct mutation of scrub key rows",
    ]:
        assert phrase in text


def test_wp42_requires_safe_rendering_and_no_raw_user_html():
    text = _text().lower()

    assert "escape source document text before rendering" in text
    assert "avoid rendering user text as raw html" in text
    assert "generate markup only from trusted code" in text
    assert "not use external javascript or cloud assets" in text
    assert "avoid storing source text in logs" in text


def test_wp42_state_boundary_keeps_review_table_authoritative():
    text = _text().lower()

    assert "selected_span_id" in text
    assert "selected_row_id" in text
    assert "must not store or mutate" in text
    assert "final include/exclude decision" in text
    assert "replace_with value" in text
    assert "scrub key content" in text
    assert "export eligibility" in text
    assert "production review table remains the control/audit surface" in text


def test_wp42_recommends_helper_before_streamlit_ui_change():
    text = _text().lower()

    assert "wp42b — static highlight preview helper and tests" in text
    assert "build a pure helper/model" in text
    assert "no streamlit ui change yet unless explicitly approved" in text
    assert "wp43 — frontend architecture decision" in text


def test_wp42_explicitly_changes_no_ui_runtime_or_real_data():
    text = _text().lower()

    for phrase in [
        "wp42 did not change",
        "presidio_streamlit.py",
        "fix_streamlit_nested_expanders.py",
        "review table behavior",
        "export/download behavior",
        "scrub key behavior",
        "reinsert behavior",
        "dependencies",
        "cloud processing",
        "real-data fixtures",
    ]:
        assert phrase in text
