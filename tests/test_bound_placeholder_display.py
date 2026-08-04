from __future__ import annotations

from bound_placeholder_display import (
    build_bound_placeholder_display_segments,
    compact_bound_placeholder_display,
)


BINDING_ID = "BSK732WYQ424ZIEQ6"
AUTO = f"[LOCATIE_{BINDING_ID}_02]"
MANUAL = f"[EMAIL_{BINDING_ID}_HANDMATIG_03]"


def test_strict_bound_placeholders_receive_short_display_aliases() -> None:
    assert compact_bound_placeholder_display(AUTO) == "[LOCATIE_02]"
    assert compact_bound_placeholder_display(MANUAL) == "[EMAIL_H_03]"


def test_non_bound_and_near_bound_values_remain_unchanged() -> None:
    values = [
        "[LOCATIE_02]",
        "[LOCATIE_BSK732WYQ424ZIEQ6]",
        "[LOCATIE_bsk732wyq424zieq6_02]",
        "[DRAFT]",
        "vrije vervangtekst",
    ]
    assert [compact_bound_placeholder_display(value) for value in values] == values


def test_display_segments_preserve_complete_source_and_offsets() -> None:
    text = f"Voor 😀 {AUTO} staat tekst en daarna {MANUAL}."
    segments = build_bound_placeholder_display_segments(text, highlight_spans=[])

    assert "".join(segment["source_text"] for segment in segments) == text
    assert "".join(segment["display_text"] for segment in segments) == (
        "Voor 😀 [LOCATIE_02] staat tekst en daarna [EMAIL_H_03]."
    )

    compact = [segment for segment in segments if segment["compacted"]]
    assert [segment["source_text"] for segment in compact] == [AUTO, MANUAL]
    assert [segment["display_text"] for segment in compact] == [
        "[LOCATIE_02]",
        "[EMAIL_H_03]",
    ]
    assert all(segment["protected"] for segment in compact)
    assert all(segment["end_utf16"] > segment["start_utf16"] for segment in compact)


def test_highlight_visibility_does_not_control_compaction_or_protection() -> None:
    text = f"A {AUTO} Z"
    start = text.index(AUTO)
    end = start + len(AUTO)

    hidden = build_bound_placeholder_display_segments(text, highlight_spans=[])
    visible = build_bound_placeholder_display_segments(text, highlight_spans=[(start, end)])

    hidden_token = next(segment for segment in hidden if segment["compacted"])
    visible_token = next(segment for segment in visible if segment["compacted"])

    assert hidden_token["display_text"] == visible_token["display_text"] == "[LOCATIE_02]"
    assert hidden_token["highlighted"] is False
    assert visible_token["highlighted"] is True
    assert hidden_token["protected"] is True
    assert visible_token["protected"] is True


def test_offsets_after_compacted_tokens_still_point_into_full_source() -> None:
    text = f"A {AUTO} einde"
    segments = build_bound_placeholder_display_segments(text, highlight_spans=[])
    trailing = next(segment for segment in segments if segment["source_text"] == " einde")

    assert trailing["start_utf16"] == len(f"A {AUTO}".encode("utf-16-le")) // 2
    assert text.encode("utf-16-le")[
        trailing["start_utf16"] * 2 : trailing["end_utf16"] * 2
    ].decode("utf-16-le") == " einde"
