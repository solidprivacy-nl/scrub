"""Safe context-card helper for SolidPrivacy Scrub.

WP_CONTEXT_CARD_HELPER builds small, report-only context cards around detected
values so reviewers can inspect local document context without a fragile
full-document editor or startup-time UI mutation.

This module does not render Streamlit UI, mutate review rows, apply replacements,
change exports, touch Scrub Key data, call cloud services, add dependencies or
use real-data fixtures.
"""

from __future__ import annotations

from html import escape
from hashlib import sha256
from typing import Any, Iterable


DEFAULT_CONTEXT_WINDOW = 80


def _clean_text(value: Any) -> str:
    return str(value or "")


def _coerce_int(value: Any, fallback: int = -1) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return fallback


def _coerce_context_window(value: Any) -> int:
    try:
        window = int(value)
    except (TypeError, ValueError):
        return DEFAULT_CONTEXT_WINDOW
    return max(0, window)


def _coerce_risk_flags(risk_flags: Iterable[Any] | None) -> list[str]:
    if risk_flags is None:
        return []
    if isinstance(risk_flags, (str, bytes)):
        return [_clean_text(risk_flags)]
    flags: list[str] = []
    for flag in risk_flags:
        text = _clean_text(flag).strip()
        if text:
            flags.append(text)
    return flags


def _stable_id(prefix: str, occurrence_id: str, start_offset: int, end_offset: int, source_text: str) -> str:
    seed = f"{occurrence_id}|{start_offset}|{end_offset}|{source_text}"
    digest = sha256(seed.encode("utf-8")).hexdigest()[:12]
    safe_occurrence = "".join(ch if ch.isalnum() or ch in {"-", "_"} else "-" for ch in occurrence_id)
    safe_occurrence = safe_occurrence.strip("-") or "occurrence"
    return f"{prefix}-{safe_occurrence}-{digest}"


def build_context_card(
    *,
    displayed_text: Any,
    start_offset: Any,
    end_offset: Any,
    source_text: Any = "",
    label: Any = "",
    entity_type: Any = "",
    review_state: Any = "needs_review",
    replacement_preview: Any = "",
    source: Any = "",
    risk_flags: Iterable[Any] | None = None,
    context_window: Any = DEFAULT_CONTEXT_WINDOW,
    occurrence_id: Any = "",
) -> dict[str, Any]:
    """Build one safe, non-authoritative context card.

    Offsets are zero-based and must point to the exact ``displayed_text`` that is
    shown to the reviewer. The helper intentionally does not do fuzzy matching,
    guessed intent, automatic replacement or document-wide editor state.

    Invalid inputs return an invalid card with validation errors instead of
    raising, so callers can report the issue safely.
    """

    errors: list[str] = []
    is_text = isinstance(displayed_text, str)
    text = displayed_text if is_text else ""
    if not is_text:
        errors.append("displayed_text must be a string")

    start = _coerce_int(start_offset)
    end = _coerce_int(end_offset)
    if start < 0 or end <= start:
        errors.append("invalid offset range")
    if is_text and end > len(text):
        errors.append("end_offset outside displayed_text")

    context_size = _coerce_context_window(context_window)
    label_text = _clean_text(label)
    expected_text = _clean_text(source_text) if _clean_text(source_text) else label_text
    occurrence = _clean_text(occurrence_id).strip()
    if not occurrence:
        occurrence = f"occurrence-{start}-{end}"

    actual_match = ""
    range_can_slice = is_text and start >= 0 and end > start and end <= len(text)
    if range_can_slice:
        actual_match = text[start:end]
        if expected_text and actual_match != expected_text:
            errors.append("source_text does not match displayed_text offsets")
        if label_text and expected_text and label_text != expected_text:
            errors.append("label does not match source_text")
    else:
        if expected_text:
            actual_match = ""

    offset_valid = not errors

    if range_can_slice:
        prefix_start = max(0, start - context_size)
        suffix_end = min(len(text), end + context_size)
        prefix_text = text[prefix_start:start]
        suffix_text = text[end:suffix_end]
    else:
        prefix_text = ""
        suffix_text = ""

    card_id = _stable_id("context-card", occurrence, start, end, expected_text or actual_match)

    return {
        "card_type": "context_card",
        "card_id": card_id,
        "occurrence_id": occurrence,
        "start_offset": start,
        "end_offset": end,
        "context_window": context_size,
        "prefix_text": prefix_text,
        "match_text": actual_match,
        "suffix_text": suffix_text,
        "escaped_prefix": escape(prefix_text),
        "escaped_match": escape(actual_match),
        "escaped_suffix": escape(suffix_text),
        "source_text": expected_text,
        "escaped_source_text": escape(expected_text),
        "label": label_text,
        "escaped_label": escape(label_text),
        "entity_type": _clean_text(entity_type),
        "review_state": _clean_text(review_state) or "needs_review",
        "replacement_preview": _clean_text(replacement_preview),
        "escaped_replacement_preview": escape(_clean_text(replacement_preview)),
        "source": _clean_text(source),
        "risk_flags": _coerce_risk_flags(risk_flags),
        "offset_valid": offset_valid,
        "validation_errors": errors,
        "report_only": True,
        "mutation_allowed": False,
        "export_blocking": False,
        "scrub_key_changes": False,
        "raw_html_allowed": False,
        "automatic_replacement": False,
        "fuzzy_matching": False,
        "document_editor_state": False,
    }


def build_context_cards(occurrences: Iterable[dict[str, Any]], displayed_text: Any) -> dict[str, Any]:
    """Build report-only cards for occurrence dictionaries.

    This convenience wrapper is still non-authoritative. It exists so future UI
    planning can consume a typed list without adding mutation semantics.
    """

    cards = [build_context_card(displayed_text=displayed_text, **occurrence) for occurrence in occurrences]
    invalid_cards = [card for card in cards if not card["offset_valid"]]
    return {
        "cards": cards,
        "total_cards": len(cards),
        "invalid_cards": invalid_cards,
        "invalid_count": len(invalid_cards),
        "report_only": True,
        "mutation_allowed": False,
        "export_blocking": False,
        "scrub_key_changes": False,
    }
