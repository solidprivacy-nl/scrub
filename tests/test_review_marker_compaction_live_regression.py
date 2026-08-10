from __future__ import annotations

from bound_placeholder_display import build_bound_placeholder_display_segments
from side_by_side_review import build_side_by_side_review_model


LOCATION_TOKEN = "[LOCATIE_B37SY5MSY72CBRPCB_01]"
ORGANIZATION_TOKEN = "[ORGANISATIE_B37SY5MSY72CBRPCB_02]"


def _rows() -> list[dict[str, object]]:
    return [
        {
            "include": True,
            "find": "SYNTHETIC_LOCATION",
            "replace_with": LOCATION_TOKEN,
        },
        {
            "include": True,
            "find": "SYNTHETIC_ORGANIZATION",
            "replace_with": ORGANIZATION_TOKEN,
        },
    ]


def test_leading_document_whitespace_does_not_shift_processed_marker_spans() -> None:
    processed = (
        "\n\n    Rapport SYNTHETIC inspectiebezoek aan "
        f"{ORGANIZATION_TOKEN}, locatie {LOCATION_TOKEN} in SYNTHETIC_CITY\n"
    )

    model = build_side_by_side_review_model(
        source_text="SYNTHETIC source",
        processed_text=processed,
        review_rows=_rows(),
        highlights_enabled=True,
    )

    assert model["processed_pane"]["text"] == processed
    spans = model["processed_pane"]["highlight_spans"]
    assert len(spans) == 2
    assert [processed[start:end] for start, end in spans] == [
        ORGANIZATION_TOKEN,
        LOCATION_TOKEN,
    ]
    assert spans[0][0] == processed.index(ORGANIZATION_TOKEN)
    assert spans[1][0] == processed.index(LOCATION_TOKEN)


def test_exact_marker_boundaries_keep_bound_placeholders_compactable() -> None:
    processed = f"\n   {ORGANIZATION_TOKEN}, locatie {LOCATION_TOKEN} in SYNTHETIC_CITY"
    model = build_side_by_side_review_model(
        source_text="SYNTHETIC source",
        processed_text=processed,
        review_rows=_rows(),
        highlights_enabled=True,
    )

    segments = build_bound_placeholder_display_segments(
        processed,
        model["processed_pane"]["highlight_spans"],
    )
    compacted = [segment for segment in segments if segment["compacted"]]

    assert [segment["source_text"] for segment in compacted] == [
        ORGANIZATION_TOKEN,
        LOCATION_TOKEN,
    ]
    assert [segment["display_text"] for segment in compacted] == [
        "[ORGANISATIE_02]",
        "[LOCATIE_01]",
    ]
    assert all(segment["highlighted"] for segment in compacted)
    assert not any(
        segment["highlighted"] and not segment["compacted"]
        for segment in segments
    )


def test_marker_toggle_off_still_preserves_compact_display_with_whitespace() -> None:
    processed = f"\n\n  {LOCATION_TOKEN}  \n"
    segments = build_bound_placeholder_display_segments(processed, [])

    compacted = [segment for segment in segments if segment["compacted"]]
    assert len(compacted) == 1
    assert compacted[0]["source_text"] == LOCATION_TOKEN
    assert compacted[0]["display_text"] == "[LOCATIE_01]"
    assert compacted[0]["highlighted"] is False
