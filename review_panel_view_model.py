"""Pure review-panel view-model helper for SolidPrivacy Scrub.

WP_REVIEW_PANEL_VIEW_MODEL_HELPER combines the report-only serial review queue
with safe context-card data for a future small review panel. It does not render
Streamlit UI, mutate review rows, apply replacements, change exports, write
Scrub Key mappings, change reinsert behavior, add dependencies, call cloud
services or use real-data fixtures.
"""

from __future__ import annotations

from html import escape
from typing import Any, Iterable

from context_cards import build_context_card
from serial_review import build_serial_review_queue


def _rows_as_list(review_rows: Iterable[dict[str, Any]] | None) -> list[dict[str, Any]]:
    return list(review_rows or [])


def _find_source_row(rows: list[dict[str, Any]], current_item: dict[str, Any] | None) -> dict[str, Any] | None:
    if not current_item:
        return None

    occurrence_id = str(current_item.get("occurrence_id") or "")
    input_index = current_item.get("input_index")
    if isinstance(input_index, int) and 0 <= input_index < len(rows):
        candidate = rows[input_index]
        if str(candidate.get("occurrence_id") or "") == occurrence_id:
            return candidate

    for row in rows:
        if str(row.get("occurrence_id") or "") == occurrence_id:
            return row
    return None


def _has_offsets(row: dict[str, Any] | None) -> bool:
    if row is None:
        return False
    return row.get("start_offset") not in (None, "") and row.get("end_offset") not in (None, "")


def _fallback_context_card(current_item: dict[str, Any], source_row: dict[str, Any] | None) -> dict[str, Any] | None:
    context_preview = str((source_row or {}).get("context_preview") or current_item.get("context_preview") or "")
    if not context_preview:
        return None
    return {
        "card_type": "context_preview_fallback",
        "occurrence_id": current_item.get("occurrence_id", ""),
        "context_preview": context_preview,
        "escaped_context_preview": escape(context_preview),
        "match_text": current_item.get("source_text", ""),
        "escaped_match": escape(str(current_item.get("source_text", ""))),
        "entity_type": current_item.get("entity_type", ""),
        "review_state": current_item.get("review_state", ""),
        "replacement_preview": current_item.get("suggested_replacement", ""),
        "risk_flags": list(current_item.get("risk_flags", [])),
        "offset_valid": False,
        "validation_errors": ["missing_offsets"],
        "report_only": True,
        "mutation_allowed": False,
        "export_blocking": False,
        "scrub_key_changes": False,
        "raw_html_allowed": False,
        "automatic_replacement": False,
        "fuzzy_matching": False,
        "document_editor_state": False,
    }


def _build_current_context_card(
    *,
    displayed_text: Any,
    current_item: dict[str, Any] | None,
    source_row: dict[str, Any] | None,
    context_window: int,
) -> tuple[dict[str, Any] | None, list[str]]:
    warnings: list[str] = []
    if current_item is None:
        warnings.append("no_current_item")
        return None, warnings

    if not _has_offsets(source_row):
        fallback = _fallback_context_card(current_item, source_row)
        if fallback is None:
            warnings.append("missing_offsets_no_context_preview")
            return None, warnings
        warnings.append("missing_offsets_context_preview_fallback")
        return fallback, warnings

    card = build_context_card(
        displayed_text=displayed_text,
        start_offset=(source_row or {}).get("start_offset"),
        end_offset=(source_row or {}).get("end_offset"),
        source_text=current_item.get("source_text", ""),
        label=current_item.get("source_text", ""),
        entity_type=current_item.get("entity_type", ""),
        review_state=current_item.get("review_state", "needs_review"),
        replacement_preview=current_item.get("suggested_replacement", ""),
        source=str((source_row or {}).get("source") or "serial_review"),
        risk_flags=current_item.get("risk_flags", []),
        context_window=context_window,
        occurrence_id=current_item.get("occurrence_id", ""),
    )
    if not card["offset_valid"]:
        warnings.extend(f"context_card_invalid: {reason}" for reason in card["validation_errors"])
    return card, warnings


def build_review_panel_view_model(
    *,
    displayed_text: Any,
    review_rows: Iterable[dict[str, Any]] | None,
    current_index: int = 0,
    current_occurrence_id: str | None = None,
    filter_mode: str = "all",
    context_window: int = 80,
) -> dict[str, Any]:
    """Build a safe, non-mutating view model for a future review panel.

    The queue comes from ``serial_review.py``. The current context card comes
    from ``context_cards.py`` when exact offsets are available. Missing offsets
    degrade to an escaped context-preview fallback or a warning; they do not
    crash, trigger fuzzy matching, guess intent or mutate review data.
    """

    warnings: list[str] = []
    rows = _rows_as_list(review_rows)

    try:
        queue = build_serial_review_queue(
            rows,
            current_index=current_index,
            current_occurrence_id=current_occurrence_id,
            filter_mode=filter_mode,
        )
    except Exception as exc:  # defensive report-only degradation for future callers
        queue = build_serial_review_queue([])
        warnings.append(f"serial_review_queue_error: {exc}")

    current_item = queue["current_item"]
    source_row = _find_source_row(rows, current_item)
    current_context_card, context_warnings = _build_current_context_card(
        displayed_text=displayed_text,
        current_item=current_item,
        source_row=source_row,
        context_window=context_window,
    )
    warnings.extend(context_warnings)

    return {
        "panel_type": "review_panel_view_model",
        "queue": queue,
        "current_item": current_item,
        "current_context_card": current_context_card,
        "next_item": queue["next_item"],
        "previous_item": queue["previous_item"],
        "unresolved_count": queue["unresolved_count"],
        "high_risk_count": queue["high_risk_count"],
        "duplicate_exact_value_count": queue["duplicate_exact_value_count"],
        "same_value_occurrence_ids": queue["same_value_occurrence_ids"],
        "audit_summary": queue["audit_summary"],
        "warnings": warnings,
        "report_only": True,
        "mutation_allowed": False,
        "export_blocking": False,
        "scrub_key_changes": False,
        "scrub_key_mapping_written": False,
        "reinsert_changes": False,
        "table_first_baseline": True,
        "review_table_mutation": False,
        "replacement_mutation": False,
        "automatic_replacement": False,
        "fuzzy_matching": False,
        "guessed_intent": False,
        "cloud_processing": False,
    }
