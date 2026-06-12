"""Static highlight preview helper for SolidPrivacy Scrub.

WP42B builds safe, read-only rendering inputs for a future highlight preview.
It does not render Streamlit UI, mutate review rows, change exports, touch Scrub
Key data, call cloud services, add dependencies or use real-data fixtures.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from typing import Any

ALLOWED_CATEGORIES = {
    "confirmed_sensitive",
    "needs_review",
    "candidate_missed_value",
    "manual_added",
    "preserve_context",
    "high_risk_unresolved",
    "hidden_content_warning",
}

DEFAULT_CATEGORY = "needs_review"

CATEGORY_LABELS = {
    "confirmed_sensitive": "Bevestigd gevoelig",
    "needs_review": "Controle nodig",
    "candidate_missed_value": "Mogelijk gemist gegeven",
    "manual_added": "Handmatig toegevoegd",
    "preserve_context": "Context behouden",
    "high_risk_unresolved": "Hoog risico onopgelost",
    "hidden_content_warning": "Verborgen inhoud waarschuwing",
}


@dataclass(frozen=True)
class HighlightSpan:
    """Non-authoritative span model for static review preview."""

    span_id: str
    row_id: str
    start_offset: int
    end_offset: int
    label: str
    category: str = DEFAULT_CATEGORY
    entity_type: str = ""
    status: str = ""
    source: str = ""
    replacement_preview: str = ""
    reason: str = ""
    context_before: str = ""
    context_after: str = ""


def _coerce_span(raw: HighlightSpan | dict[str, Any]) -> HighlightSpan:
    if isinstance(raw, HighlightSpan):
        return raw
    if not isinstance(raw, dict):
        raise TypeError("Highlight span must be a dict or HighlightSpan.")
    return HighlightSpan(
        span_id=str(raw.get("span_id", "")),
        row_id=str(raw.get("row_id", "")),
        start_offset=int(raw.get("start_offset", -1)),
        end_offset=int(raw.get("end_offset", -1)),
        label=str(raw.get("label", "")),
        category=str(raw.get("category", DEFAULT_CATEGORY)) or DEFAULT_CATEGORY,
        entity_type=str(raw.get("entity_type", "")),
        status=str(raw.get("status", "")),
        source=str(raw.get("source", "")),
        replacement_preview=str(raw.get("replacement_preview", "")),
        reason=str(raw.get("reason", "")),
        context_before=str(raw.get("context_before", "")),
        context_after=str(raw.get("context_after", "")),
    )


def validate_highlight_spans(text: str, spans: list[HighlightSpan | dict[str, Any]]) -> dict[str, Any]:
    """Validate static highlight spans against the exact displayed text."""
    if not isinstance(text, str):
        return {
            "valid_spans": [],
            "invalid_spans": [],
            "errors": ["Preview text must be a string."],
            "safe_to_render": False,
        }

    valid: list[dict[str, Any]] = []
    invalid: list[dict[str, Any]] = []
    seen_ids: set[str] = set()

    for raw in spans:
        try:
            span = _coerce_span(raw)
        except (TypeError, ValueError) as exc:
            invalid.append({"span_id": "", "reason": str(exc)})
            continue

        reasons: list[str] = []
        if not span.span_id:
            reasons.append("span_id is required")
        if span.span_id in seen_ids:
            reasons.append("span_id must be unique")
        if span.start_offset < 0 or span.end_offset <= span.start_offset:
            reasons.append("invalid offset range")
        if span.end_offset > len(text):
            reasons.append("end_offset outside displayed text")
        if span.category not in ALLOWED_CATEGORIES:
            reasons.append("unsupported category")

        actual_text = ""
        if not reasons:
            actual_text = text[span.start_offset : span.end_offset]
            if actual_text != span.label:
                reasons.append("span label does not match displayed text offsets")

        if reasons:
            invalid.append({
                "span_id": span.span_id,
                "row_id": span.row_id,
                "reasons": reasons,
                "start_offset": span.start_offset,
                "end_offset": span.end_offset,
                "label": span.label,
            })
            continue

        seen_ids.add(span.span_id)
        valid.append({
            "span_id": span.span_id,
            "row_id": span.row_id,
            "start_offset": span.start_offset,
            "end_offset": span.end_offset,
            "label": span.label,
            "category": span.category,
            "category_label": CATEGORY_LABELS[span.category],
            "entity_type": span.entity_type,
            "status": span.status,
            "source": span.source,
            "replacement_preview": span.replacement_preview,
            "reason": span.reason,
            "context_before": span.context_before,
            "context_after": span.context_after,
        })

    return {
        "valid_spans": valid,
        "invalid_spans": invalid,
        "errors": [],
        "safe_to_render": not invalid,
    }


def build_static_highlight_preview(text: str, spans: list[HighlightSpan | dict[str, Any]]) -> dict[str, Any]:
    """Build escaped, non-authoritative rendering inputs for a static preview."""
    validation = validate_highlight_spans(text, spans)
    valid_spans = sorted(validation["valid_spans"], key=lambda item: (item["start_offset"], item["end_offset"]))

    segments: list[dict[str, Any]] = []
    cursor = 0
    for span in valid_spans:
        start = span["start_offset"]
        end = span["end_offset"]
        if start < cursor:
            invalid = dict(span)
            invalid["reasons"] = ["overlapping span"]
            validation["invalid_spans"].append(invalid)
            continue
        if cursor < start:
            plain_text = text[cursor:start]
            segments.append({
                "type": "text",
                "text": plain_text,
                "escaped_text": escape(plain_text),
            })
        span_text = text[start:end]
        segments.append({
            "type": "highlight",
            "text": span_text,
            "escaped_text": escape(span_text),
            "span_id": span["span_id"],
            "row_id": span["row_id"],
            "category": span["category"],
            "category_label": span["category_label"],
            "aria_label": f"{span['category_label']}: {span_text}",
            "non_authoritative": True,
        })
        cursor = end

    if cursor < len(text):
        plain_text = text[cursor:]
        segments.append({
            "type": "text",
            "text": plain_text,
            "escaped_text": escape(plain_text),
        })

    return {
        "preview_type": "static_highlight_preview",
        "report_only": True,
        "read_only": True,
        "non_authoritative": True,
        "mutation_allowed": False,
        "export_blocking": False,
        "scrub_key_changes": False,
        "ui_required": False,
        "external_assets": False,
        "text_length": len(text) if isinstance(text, str) else 0,
        "segments": segments,
        "valid_spans": valid_spans,
        "invalid_spans": validation["invalid_spans"],
        "errors": validation["errors"],
        "safe_to_render": validation["safe_to_render"] and not validation["invalid_spans"],
        "category_labels": CATEGORY_LABELS,
        "warning": "Static preview only; the review table remains authoritative.",
    }
