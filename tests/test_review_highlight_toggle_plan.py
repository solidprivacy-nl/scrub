from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PLAN = REPO_ROOT / "REVIEW_HIGHLIGHT_TOGGLE_PLAN.md"
THIS_TEST = Path(__file__)


def _plan_text() -> str:
    return PLAN.read_text(encoding="utf-8")


def _lowered_plan_text() -> str:
    return _plan_text().lower()


def test_review_highlight_toggle_plan_contains_user_facing_labels():
    text = _plan_text()

    assert "Markeringen tonen" in text
    assert "Markeringen tonen in voorbeeldtekst" in text
    assert "De voorbeeldtekst blijft rustig en normaal leesbaar." in text
    assert "Vervangen/gemaskeerde waarden krijgen een subtiele visuele markering." in text


def test_review_highlight_toggle_plan_is_read_only_visual_only_and_table_first():
    lowered = _lowered_plan_text()

    for required in [
        "read-only",
        "visual-only",
        "non-authoritative",
        "non-mutating",
        "table-first baseline",
        "existing review table remains the source of truth and fallback",
        "review table remains source of truth",
    ]:
        assert required in lowered


def test_review_highlight_toggle_plan_preserves_simple_product_principles():
    lowered = _lowered_plan_text()

    for required in [
        "make the review interface simpler",
        "should not add a new decision layer",
        "show helper internals",
        "technical helper panel",
        "existing text preview remains unchanged",
        "simple display option",
    ]:
        assert required in lowered


def test_review_highlight_toggle_plan_allows_only_exact_already_replaced_preview_values():
    lowered = _lowered_plan_text()

    for required in [
        "already masked/replaced values in the preview text",
        "exact placeholders or replacement values already present in the preview",
        "use exact matching only",
        "included rows where `find` and `replace_with` are both non-empty",
        "values that appear exactly in the preview or generated output text",
    ]:
        assert required in lowered


def test_review_highlight_toggle_plan_forbids_guessing_and_wrong_values():
    lowered = _lowered_plan_text()

    for required in [
        "do not highlight values by guessing",
        "fuzzy matches",
        "inferred personal data",
        "hidden/offscreen document content",
        "non-included table rows",
        "ignored rows",
        "scrub key mappings not present in the current preview",
        "reinsert values",
        "document bytes or raw word/pdf layout content",
    ]:
        assert required in lowered


def test_review_highlight_toggle_plan_forbids_mutation_and_side_effects():
    lowered = _lowered_plan_text()

    for required in [
        "mutate the replacement table",
        "change `edited_replacements_df`",
        "apply replacements",
        "perform automatic replacement",
        "write scrub key mappings",
        "change scrub key schema",
        "change export/download behavior",
        "block export",
        "change reinsert behavior",
        "use cloud processing",
        "add dependencies",
    ]:
        assert required in lowered


def test_review_highlight_toggle_plan_blocks_old_static_highlight_route():
    text = _plan_text()

    for required in [
        "Do not restart static-highlight startup source mutation.",
        "Do not patch presidio_streamlit.py at startup.",
        "Do not implement click-to-mark.",
        "Do not implement an advanced editor.",
        "Do not implement full-document marking.",
    ]:
        assert required in text


def test_review_highlight_toggle_plan_raw_html_and_accessibility_contracts():
    lowered = _lowered_plan_text()

    for required in [
        "color must not be the only signal",
        "subtle and calm",
        "avoid a crowded interface",
        "avoid raw html unless all user/document text is safely escaped",
        "raw unsafe html",
        "requires escaping if html is ever used",
    ]:
        assert required in lowered


def test_review_highlight_toggle_plan_contract_test_route_and_implementation_gate():
    text = _plan_text()
    lowered = text.lower()

    assert "WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS" in text
    assert "WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION only after separate coordinator approval" in text
    assert "Do not implement the toggle in this package." in text
    assert "app verification because ui behavior would change" in lowered


def test_review_highlight_toggle_plan_uses_synthetic_only_test_values():
    rendered = THIS_TEST.read_text(encoding="utf-8") + _plan_text()
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]

    assert "synthetic" in rendered.lower()
    assert "real personal data" in rendered.lower()
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
