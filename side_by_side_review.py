"""Pure helper model for a future side-by-side review surface.

WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER explores a safe data shape for:

    source text left | processed/checked text right
                     | optional highlights integrated in the processed text

This module does not render Streamlit UI, does not implement synchronized
scrolling, does not mutate the review table, does not apply replacements, does
not write Scrub Key data, does not change export/download behavior, does not
change reinsert behavior, does not add dependencies, does not call cloud services
and does not use real data fixtures.
"""

from __future__ import annotations

from html import escape
from typing import Any, Iterable

from review_highlight_toggle import build_highlight_terms, find_exact_highlight_spans


SOURCE_PANE_ID = "source_text_left"
PROCESSED_PANE_ID = "processed_checked_text_right"
HIGHLIGHT_TOGGLE_LABEL = "Markeringen tonen"
HIGHLIGHT_TOGGLE_LABEL_EXPLICIT = "Markeringen tonen in verwerkte tekst"
COMPACT_LEGEND_LABEL = "Geel = vervangen of gemaskeerde waarde"
TABLE_FALLBACK_COPY = "De vervangtabel blijft leidend. Controleer bij twijfel de tabel hieronder."


def _safe_text(value: Any) -> str:
    if value is None:
        return ""
    try:
        if value != value:  # NaN check without importing pandas/numpy
            return ""
    except Exception:
        pass
    return str(value)


def _safe_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    try:
        if value != value:  # NaN check without importing pandas/numpy
            return False
    except Exception:
        pass
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"true", "1", "yes", "y", "checked", "ja"}


def _iter_rows(review_rows: Any) -> Iterable[dict[str, Any]]:
    if review_rows is None:
        return []
    if hasattr(review_rows, "iterrows"):
        return (dict(row) for _, row in review_rows.iterrows())
    return (dict(row) for row in review_rows or [])


def _included_review_count(review_rows: Any) -> int:
    return sum(1 for row in _iter_rows(review_rows) if _safe_bool(row.get("include", False)))


def build_side_by_side_review_model(
    *,
    source_text: Any,
    processed_text: Any,
    review_rows: Any = None,
    highlights_enabled: bool = False,
    selected_occurrence_id: str | None = None,
) -> dict[str, Any]:
    """Build a non-mutating side-by-side review data model.

    The helper prepares structured data for a future UI, but deliberately avoids
    rendering HTML or changing any product state. Highlight spans are exact spans
    in the processed text only. Source text is never highlighted by this helper.
    """

    source = _safe_text(source_text)
    processed = _safe_text(processed_text)
    highlight_terms = build_highlight_terms(review_rows)
    highlight_spans = find_exact_highlight_spans(processed, highlight_terms) if highlights_enabled else []

    return {
        "model_type": "side_by_side_review_prototype_helper",
        "layout": {
            "mode": "side_by_side",
            "source_position": "left",
            "processed_position": "right",
            "source_label": "Brontekst",
            "processed_label": "Verwerkte tekst",
            "alternate_source_label": "Originele tekst",
            "alternate_processed_label": "Gecontroleerde tekst",
        },
        "source_pane": {
            "pane_id": SOURCE_PANE_ID,
            "position": "left",
            "label": "Brontekst",
            "text": source,
            "escaped_text": escape(source),
            "editable": False,
            "highlight_spans": [],
        },
        "processed_pane": {
            "pane_id": PROCESSED_PANE_ID,
            "position": "right",
            "label": "Verwerkte tekst",
            "text": processed,
            "escaped_text": escape(processed),
            "highlight_terms": highlight_terms,
            "highlight_spans": highlight_spans,
            "highlights_enabled": bool(highlights_enabled),
            "highlights_visual_only": True,
            "highlight_scope": "processed_pane_only",
        },
        "highlight_toggle": {
            "label": HIGHLIGHT_TOGGLE_LABEL,
            "explicit_label": HIGHLIGHT_TOGGLE_LABEL_EXPLICIT,
            "enabled": bool(highlights_enabled),
            "visual_only": True,
            "only_visual_aid": True,
            "must_not_change_source_text": True,
            "must_not_change_review_table_state": True,
            "must_not_change_export_payloads": True,
            "must_not_change_scrub_key_state": True,
            "must_not_change_reinsert_behavior": True,
        },
        "compact_legend": {
            "enabled_when_highlights_visible": bool(highlights_enabled and highlight_spans),
            "label": COMPACT_LEGEND_LABEL,
            "single_legend_only": True,
            "repeated_inline_gemarkeerd_labels": False,
        },
        "review_table": {
            "source_of_truth": True,
            "fallback": True,
            "copy": TABLE_FALLBACK_COPY,
            "included_review_count": _included_review_count(review_rows),
            "mutation_allowed": False,
        },
        "serial_review": {
            "relationship": "guided_layer",
            "not_table_replacement": True,
            "selected_occurrence_id": selected_occurrence_id,
            "intended_behavior": "selection_may_focus_context_in_future_ui_only",
            "mutation_allowed": False,
        },
        "replacement_review": {
            "relationship": "task_oriented_future_layer",
            "allowed_first_actions": ["Vervangen", "Zichtbaar houden", "Aanpassen", "Later controleren"],
            "allowed_first_scopes": ["Alleen deze plek", "Alle exact dezelfde waarden"],
            "helper_internals_visible": False,
            "blocked_user_facing_internals": [
                "all_normalized",
                "creates_mapping",
                "mapping_candidates",
                "export_readiness",
                "raw decision states",
                "audit fields",
            ],
        },
        "scroll_sync": {
            "desired_later": True,
            "implemented": False,
            "requires_separate_package": True,
            "requires_separate_tests": True,
            "custom_component_required_here": False,
        },
        "boundaries": {
            "report_only": True,
            "mutation_allowed": False,
            "review_table_mutation": False,
            "replacement_mutation": False,
            "automatic_replacement": False,
            "scrub_key_writes": False,
            "scrub_key_schema_change": False,
            "export_blocking": False,
            "export_download_behavior_change": False,
            "reinsert_behavior_change": False,
            "click_to_mark": False,
            "advanced_editor": False,
            "full_document_marking": False,
            "synchronized_scroll_implementation": False,
            "custom_html_component_implementation": False,
            "cloud_processing": False,
            "real_data": False,
        },
    }


def summarize_side_by_side_review_model(model: dict[str, Any]) -> dict[str, Any]:
    """Return a compact audit summary for tests and future UI callers."""

    processed_pane = model.get("processed_pane", {})
    review_table = model.get("review_table", {})
    boundaries = model.get("boundaries", {})
    scroll_sync = model.get("scroll_sync", {})
    return {
        "model_type": model.get("model_type"),
        "source_position": model.get("layout", {}).get("source_position"),
        "processed_position": model.get("layout", {}).get("processed_position"),
        "highlights_enabled": processed_pane.get("highlights_enabled", False),
        "highlight_count": len(processed_pane.get("highlight_spans", [])),
        "review_table_source_of_truth": review_table.get("source_of_truth", False),
        "review_table_fallback": review_table.get("fallback", False),
        "synchronized_scroll_implemented": scroll_sync.get("implemented", False),
        "mutation_allowed": boundaries.get("mutation_allowed", True),
        "scrub_key_writes": boundaries.get("scrub_key_writes", True),
        "export_download_behavior_change": boundaries.get("export_download_behavior_change", True),
        "reinsert_behavior_change": boundaries.get("reinsert_behavior_change", True),
    }
