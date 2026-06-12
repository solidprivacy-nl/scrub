from __future__ import annotations

from highlight_preview import (
    CATEGORY_LABELS,
    HighlightSpan,
    build_static_highlight_preview,
    validate_highlight_spans,
)


SYNTHETIC_TEXT = "Cliënt [PERSOON_1] woont aan [ADRES_1]. Zaak [ZAAK_1] blijft context."


def test_build_static_highlight_preview_escapes_text_and_preserves_labels():
    text = "SYNTHETIC <script> [PERSOON_1] & context"
    start = text.index("[PERSOON_1]")
    end = start + len("[PERSOON_1]")

    preview = build_static_highlight_preview(
        text,
        [
            HighlightSpan(
                span_id="span-1",
                row_id="row-1",
                start_offset=start,
                end_offset=end,
                label="[PERSOON_1]",
                category="confirmed_sensitive",
                entity_type="PERSON",
                status="confirmed",
                source="synthetic",
                replacement_preview="PERSOON_PLACEHOLDER",
                reason="Synthetic confirmed value",
            )
        ],
    )

    assert preview["preview_type"] == "static_highlight_preview"
    assert preview["read_only"] is True
    assert preview["non_authoritative"] is True
    assert preview["mutation_allowed"] is False
    assert preview["export_blocking"] is False
    assert preview["scrub_key_changes"] is False
    assert preview["ui_required"] is False
    assert preview["external_assets"] is False
    assert preview["safe_to_render"] is True
    assert "&lt;script&gt;" in "".join(segment["escaped_text"] for segment in preview["segments"])
    highlight = [segment for segment in preview["segments"] if segment["type"] == "highlight"][0]
    assert highlight["escaped_text"] == "[PERSOON_1]"
    assert highlight["category_label"] == "Bevestigd gevoelig"
    assert highlight["aria_label"] == "Bevestigd gevoelig: [PERSOON_1]"


def test_validate_highlight_spans_rejects_invalid_offsets_and_label_mismatch():
    result = validate_highlight_spans(
        SYNTHETIC_TEXT,
        [
            {
                "span_id": "bad-offset",
                "row_id": "row-1",
                "start_offset": -1,
                "end_offset": 5,
                "label": "Cliënt",
                "category": "needs_review",
            },
            {
                "span_id": "bad-label",
                "row_id": "row-2",
                "start_offset": 0,
                "end_offset": 6,
                "label": "Wrong",
                "category": "needs_review",
            },
        ],
    )

    assert result["valid_spans"] == []
    reasons = {reason for span in result["invalid_spans"] for reason in span["reasons"]}
    assert "invalid offset range" in reasons
    assert "span label does not match displayed text offsets" in reasons
    assert result["safe_to_render"] is False


def test_validate_highlight_spans_rejects_duplicate_and_unsupported_category():
    start = SYNTHETIC_TEXT.index("[PERSOON_1]")
    end = start + len("[PERSOON_1]")
    result = validate_highlight_spans(
        SYNTHETIC_TEXT,
        [
            {
                "span_id": "same",
                "row_id": "row-1",
                "start_offset": start,
                "end_offset": end,
                "label": "[PERSOON_1]",
                "category": "confirmed_sensitive",
            },
            {
                "span_id": "same",
                "row_id": "row-2",
                "start_offset": start,
                "end_offset": end,
                "label": "[PERSOON_1]",
                "category": "not_allowed",
            },
        ],
    )

    assert len(result["valid_spans"]) == 1
    assert len(result["invalid_spans"]) == 1
    assert "span_id must be unique" in result["invalid_spans"][0]["reasons"]
    assert "unsupported category" in result["invalid_spans"][0]["reasons"]


def test_build_static_highlight_preview_reports_overlapping_spans():
    first_start = SYNTHETIC_TEXT.index("[PERSOON_1]")
    first_end = first_start + len("[PERSOON_1]")

    preview = build_static_highlight_preview(
        SYNTHETIC_TEXT,
        [
            {
                "span_id": "a",
                "row_id": "row-a",
                "start_offset": first_start,
                "end_offset": first_end,
                "label": "[PERSOON_1]",
                "category": "needs_review",
            },
            {
                "span_id": "b",
                "row_id": "row-b",
                "start_offset": first_start + 1,
                "end_offset": first_end,
                "label": "PERSOON_1]",
                "category": "needs_review",
            },
        ],
    )

    assert preview["safe_to_render"] is False
    assert any("overlapping span" in span["reasons"] for span in preview["invalid_spans"])


def test_preview_contains_all_category_labels_and_no_real_data_examples():
    preview = build_static_highlight_preview(SYNTHETIC_TEXT, [])

    assert preview["category_labels"] == CATEGORY_LABELS
    rendered = repr(preview)
    assert "Jan Jansen" not in rendered
    assert "Piet de Vries" not in rendered
    assert "123456782" not in rendered


def test_non_string_text_is_rejected_safely():
    result = validate_highlight_spans(123, [])

    assert result["valid_spans"] == []
    assert result["safe_to_render"] is False
    assert result["errors"] == ["Preview text must be a string."]
