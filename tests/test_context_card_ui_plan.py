from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PLAN = REPO_ROOT / "CONTEXT_CARD_UI_PLAN.md"
THIS_TEST = Path(__file__)


def _plan_text() -> str:
    return PLAN.read_text(encoding="utf-8")


def _lowered_plan_text() -> str:
    return _plan_text().lower()


def test_context_card_ui_plan_references_helper_and_required_boundaries():
    text = _plan_text()
    lowered = text.lower()

    assert "context_cards.py" in text
    for required in [
        "report-only",
        "non-authoritative",
        "table-first baseline",
        "no startup source mutation",
        "no click-to-mark",
        "no advanced editor",
        "no export blocking",
        "no scrub key mutation",
        "no reinsert behavior change",
        "synthetic-only",
    ]:
        assert required in lowered


def test_context_card_ui_plan_names_context_card_builder_functions():
    text = _plan_text()

    assert "context_cards.py" in text
    assert "build_context_card" in text
    assert "build_context_cards" in text


def test_context_card_ui_plan_contains_required_card_fields():
    text = _plan_text()

    for field in [
        "prefix_text",
        "match_text",
        "suffix_text",
        "entity_type",
        "review_state",
        "replacement_preview",
        "source",
        "risk_flags",
        "offset_valid",
        "validation_errors",
    ]:
        assert field in text


def test_context_card_ui_plan_hardens_full_boundary_contract():
    lowered = _lowered_plan_text()

    for required in [
        "report-only",
        "non-authoritative",
        "table-first baseline",
        "existing review table remains authoritative control/fallback",
        "no startup source mutation",
        "no full-document marking",
        "no click-to-mark",
        "no advanced editor",
        "no inline editing",
        "no word/pdf layout rendering",
        "no export blocking",
        "no scrub key mutation",
        "no reinsert behavior change",
        "no review table mutation",
        "synthetic-only",
    ]:
        assert required in lowered


def test_context_card_ui_plan_preserves_review_table_and_runtime_boundaries():
    lowered = _lowered_plan_text()

    for required in [
        "existing review table",
        "authoritative audit/control surface",
        "authoritative control and fallback",
        "does not implement ui",
        "no streamlit ui implementation",
        "no full-document marking",
        "no inline editing",
        "no word/pdf layout rendering",
        "no review table mutation",
        "no dependency changes",
        "no cloud processing",
        "real-data fixtures",
    ]:
        assert required in lowered


def test_context_card_ui_plan_links_serial_review_without_mutation():
    text = _plan_text()
    lowered = text.lower()

    assert "serial_review.py" in text
    assert "current_item" in text
    assert "next/previous review stays helper-driven" in lowered
    assert "the context card mutates nothing" in lowered
    assert "the review table remains the source of truth" in lowered


def test_context_card_ui_plan_keeps_context_cards_display_only():
    lowered = _lowered_plan_text()

    for required in [
        "display data only",
        "must not write decisions",
        "must not write decisions, mappings, scrub key data, export eligibility or reinsert state",
        "it must not apply a decision to same-value occurrences",
        "no automatic replacement",
        "no hidden mutation",
    ]:
        assert required in lowered


def test_context_card_ui_plan_uses_synthetic_only_test_values():
    rendered = THIS_TEST.read_text(encoding="utf-8") + _plan_text()
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]

    assert "synthetic" in rendered.lower()
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
