from __future__ import annotations

from pathlib import Path

PLAN = Path("STATIC_HIGHLIGHT_PREVIEW_UI_PLAN.md")


def _plan_text() -> str:
    return PLAN.read_text(encoding="utf-8")


def test_static_highlight_preview_ui_plan_exists_and_is_planning_only():
    text = _plan_text()

    assert "WP42C" in text
    assert "planning/documentation-only" in text
    assert "read-only" in text
    assert "non-authoritative" in text
    assert "review-assistive only" in text


def test_static_highlight_preview_ui_plan_preserves_authoritative_table_boundary():
    text = _plan_text()

    assert "The existing replacement table remains the source of truth" in text
    assert "Pas beslissingen aan in de vervangtabel hieronder" in text
    assert "mutation_allowed is False" in text
    assert "export_blocking is False" in text
    assert "scrub_key_changes is False" in text


def test_static_highlight_preview_ui_plan_blocks_mutating_behaviour():
    text = _plan_text()

    forbidden_boundaries = [
        "change include/exclude decisions",
        "edit replacements",
        "mutate review table rows",
        "mutate Scrub Key rows",
        "affect export eligibility",
        "block exports",
        "create or delete mappings",
        "mark text as sensitive from the preview",
        "use external JavaScript or cloud assets",
        "render user text as raw HTML",
        "process real-data fixtures",
    ]

    for boundary in forbidden_boundaries:
        assert boundary in text


def test_static_highlight_preview_ui_plan_requires_escaped_rendering_and_accessibility():
    text = _plan_text()

    assert "render only `escaped_text`" in text
    assert "must not render raw `text` values as HTML" in text
    assert "must not rely on color alone" in text
    assert "visible category label or legend" in text
    assert "table fallback remains available" in text


def test_static_highlight_preview_ui_plan_has_no_runtime_or_ui_file_changes():
    text = _plan_text()

    assert "does not change:" in text
    assert "`presidio_streamlit.py`;" in text
    assert "`fix_streamlit_nested_expanders.py`;" in text
    assert "any Streamlit patch file" in text
    assert "review table behavior" in text
    assert "export/download behavior" in text
    assert "Scrub Key behavior" in text
    assert "helper runtime behavior" in text
    assert "cloud processing" in text
    assert "real-data fixtures" in text


def test_static_highlight_preview_ui_plan_requires_explicit_ui_approval_next():
    text = _plan_text()

    assert "WP42D — Static highlight preview UI integration" in text
    assert "Only start WP42D if the coordinator explicitly approves UI work" in text
    assert "require app verification" in text
