from __future__ import annotations

from processed_text_selection_component import build_component_args
from selection_mask_action import processed_text_hash
from side_by_side_review_panel_ui import _highlighted_processed_inner_html


TOKEN = "[LOCATIE_BSK732WYQ424ZIEQ6_02]"


def test_component_receives_complete_token_and_hash_not_compact_alias() -> None:
    processed = f"A {TOKEN} Z"
    args = build_component_args(
        source_text="A Utrecht Z",
        processed_text=processed,
        highlight_spans=[(2, 2 + len(TOKEN))],
        document_scope_key="0123456789abcdef",
        processed_text_hash=processed_text_hash(processed),
        non_mutating_spike=False,
    )

    assert args["processed_text"] == processed
    assert TOKEN in args["processed_text"]
    assert "[LOCATIE_02]" not in args["processed_text"]
    assert args["processed_text_hash"] == processed_text_hash(processed)


def test_static_fallback_compacts_visible_text_but_keeps_full_token_as_metadata() -> None:
    processed = f"A {TOKEN} Z"
    html = _highlighted_processed_inner_html(
        processed,
        [(2, 2 + len(TOKEN))],
    )

    assert ">[LOCATIE_02]</mark>" in html
    assert f"Volledige gebonden placeholder: {TOKEN}" in html
    assert f">{TOKEN}</mark>" not in html


def test_static_fallback_compacts_even_when_visual_highlights_are_hidden() -> None:
    processed = f"A {TOKEN} Z"
    html = _highlighted_processed_inner_html(processed, [])

    assert ">[LOCATIE_02]</span>" in html
    assert f"Volledige gebonden placeholder: {TOKEN}" in html


def test_ui_module_declares_display_only_security_boundaries() -> None:
    source = open("side_by_side_review_panel_ui.py", encoding="utf-8").read()

    assert '"bound_placeholder_display_compaction": True' in source
    assert '"bound_placeholder_source_tokens_unchanged": True' in source
    assert '"bound_placeholder_binding_entropy_changed": False' in source
    assert "scrub_key_binding" not in source
    assert "scrub_key_bound_export" not in source
