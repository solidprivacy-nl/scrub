"""Small Streamlit renderer for the non-destructive serial review panel.

WP_SERIAL_REVIEW_UI keeps the existing review table as the source of truth. This
module only renders a helper-driven, report-only panel from review_panel_view_model.py.
It does not mutate review rows, apply replacements, write Scrub Key mappings,
block export, change reinsert behavior, add dependencies, call cloud services or
use real-data fixtures.
"""

from __future__ import annotations

from typing import Any

import streamlit as st

from review_panel_view_model import build_review_panel_view_model
from review_highlight_toggle_panel_ui import render_review_highlight_toggle_panel


FILTER_LABELS = {
    "all": "Alle items",
    "unresolved": "Openstaande items",
    "high_risk": "Risico-items",
    "high_risk_unresolved": "Openstaande risico-items",
}

VALID_PANEL_STATES = {
    "needs_review",
    "accepted",
    "edited",
    "ignored",
    "manual_added",
    "preserve_context",
    "unresolved",
    "high_risk_unresolved",
}


def _safe_text(value: Any) -> str:
    if value is None:
        return ""
    try:
        # pandas.NA / NaN compatibility without importing pandas here.
        if value != value:  # noqa: PLR0124 - intentional NaN check
            return ""
    except Exception:
        pass
    return str(value).strip()


def _safe_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    try:
        if value != value:  # NaN
            return False
    except Exception:
        pass
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"true", "1", "yes", "y", "checked", "ja"}


def _review_state_for_panel(row: Any) -> str:
    include = _safe_bool(row.get("include", True))
    source = _safe_text(row.get("source", ""))
    review_status = _safe_text(row.get("review_status", ""))

    if review_status in VALID_PANEL_STATES:
        return review_status
    if not include:
        return "ignored"
    if source == "candidate":
        return "unresolved"
    if source == "manual":
        return "manual_added"
    return "needs_review"


def _context_preview(displayed_text: str, start: int, end: int, fallback: str, window: int = 80) -> str:
    if fallback:
        return fallback
    if start < 0 or end <= start:
        return ""
    prefix_start = max(0, start - window)
    suffix_end = min(len(displayed_text), end + window)
    return displayed_text[prefix_start:suffix_end]


def _offsets_for(displayed_text: str, source_text: str) -> tuple[int | None, int | None]:
    if not displayed_text or not source_text:
        return None, None
    start = displayed_text.find(source_text)
    if start < 0:
        return None, None
    return start + 0, start + len(source_text)


def build_serial_review_panel_rows(displayed_text: str, edited_replacements_df: Any) -> list[dict[str, Any]]:
    """Build safe, report-only rows for the serial review panel view model.

    Exact ``str.find`` offsets are used only when the value is present in the
    displayed text. No fuzzy matching, guessed intent or automatic replacement is
    performed.
    """

    rows: list[dict[str, Any]] = []
    if edited_replacements_df is None:
        return rows

    iterator = edited_replacements_df.iterrows() if hasattr(edited_replacements_df, "iterrows") else enumerate(edited_replacements_df)
    for index, row in iterator:
        source_text = _safe_text(row.get("find", ""))
        if not source_text:
            continue

        replacement = _safe_text(row.get("replace_with", ""))
        entity_type = _safe_text(row.get("entity_type", "")) or "UNKNOWN"
        start, end = _offsets_for(displayed_text, source_text)
        fallback_context = _safe_text(row.get("context", ""))
        panel_row: dict[str, Any] = {
            "occurrence_id": f"review-row-{index}",
            "source_text": source_text,
            "entity_type": entity_type,
            "suggested_replacement": replacement,
            "review_state": _review_state_for_panel(row),
            "confidence": None,
            "context_preview": _context_preview(
                displayed_text,
                -1 if start is None else start,
                -1 if end is None else end,
                fallback_context,
            ),
            "risk_flags": ["candidate_review"] if _safe_text(row.get("source", "")) == "candidate" else [],
            "source": _safe_text(row.get("source", "review_table")) or "review_table",
        }
        if start is not None and end is not None:
            panel_row["start_offset"] = start
            panel_row["end_offset"] = end
        rows.append(panel_row)
    return rows


def _show_current_item(current_item: dict[str, Any]) -> None:
    st.markdown("**Huidig item**")
    st.caption("Gevonden waarde")
    st.code(current_item.get("source_text", ""), language=None)
    st.caption(f"Type: {current_item.get('entity_type', '')}")
    st.caption(f"Status: {current_item.get('review_state', '')}")
    st.caption("Voorgestelde vervanging")
    st.code(current_item.get("suggested_replacement", ""), language=None)
    risk_flags = current_item.get("risk_flags") or []
    st.caption("Risico’s: " + (", ".join(risk_flags) if risk_flags else "geen extra risicovlaggen"))


def _show_context_card(card: dict[str, Any] | None, warnings: list[str]) -> None:
    st.markdown("**Context**")
    if card is None:
        st.warning("Geen contextkaart beschikbaar; gebruik de bestaande vervangtabel als fallback.")
    elif card.get("card_type") == "context_preview_fallback":
        st.caption("Context preview fallback")
        st.text(card.get("context_preview", ""))
        st.caption("Match")
        st.code(card.get("match_text", ""), language=None)
    else:
        st.caption("Prefix")
        st.text(card.get("prefix_text", ""))
        st.caption("Match")
        st.code(card.get("match_text", ""), language=None)
        st.caption("Suffix")
        st.text(card.get("suffix_text", ""))

        validation_errors = card.get("validation_errors") or []
        if validation_errors:
            st.warning("Contextwaarschuwing: " + "; ".join(validation_errors))

    if warnings:
        st.caption("Waarschuwingen: " + " · ".join(warnings))


def render_serial_review_panel(*, displayed_text: str, edited_replacements_df: Any) -> dict[str, Any] | None:
    """Render the small serial review panel and return the report-only view model."""

    st.subheader("Serial review — experimentele reviewhulp")
    st.info(
        "Alleen-lezen hulpweergave. De bestaande vervangtabel blijft leidend voor "
        "beslissingen, Scrub Key en export."
    )
    st.caption(
        "table-first baseline · non-destructive · report-only · no Scrub Key mutation · "
        "no export blocking · no reinsert behavior change"
    )

    review_rows = build_serial_review_panel_rows(displayed_text, edited_replacements_df)
    if not review_rows:
        st.warning("Geen serial review items beschikbaar. De bestaande vervangtabel blijft de fallback.")
        return None

    current_index = int(st.session_state.get("serial_review_current_index", 0) or 0)
    current_occurrence_id = st.session_state.get("serial_review_current_occurrence_id")
    current_filter = st.session_state.get("serial_review_filter_mode", "all")
    if current_filter not in FILTER_LABELS:
        current_filter = "all"

    filter_mode = st.selectbox(
        "Serial review filter",
        list(FILTER_LABELS.keys()),
        index=list(FILTER_LABELS.keys()).index(current_filter),
        format_func=lambda value: FILTER_LABELS[value],
        key="serial_review_filter_mode",
        help="Dit filter wijzigt alleen de hulpweergave en niet de vervangtabel.",
    )

    view_model = build_review_panel_view_model(
        displayed_text=displayed_text,
        review_rows=review_rows,
        current_index=current_index,
        current_occurrence_id=current_occurrence_id,
        filter_mode=filter_mode,
        context_window=80,
    )
    queue = view_model["queue"]
    resolved_index = queue.get("current_index")
    if resolved_index is not None:
        st.session_state["serial_review_current_index"] = resolved_index

    metrics = st.columns(5)
    metrics[0].metric("Totaal", queue.get("total_items", 0))
    item_number = 0 if resolved_index is None else resolved_index + 1
    metrics[1].metric("Huidig", item_number)
    metrics[2].metric("Open", view_model.get("unresolved_count", 0))
    metrics[3].metric("Risico", view_model.get("high_risk_count", 0))
    metrics[4].metric("Exact gelijk", view_model.get("duplicate_exact_value_count", 0))

    current_item = view_model.get("current_item")
    if current_item is None:
        st.warning("Geen huidig item beschikbaar binnen dit filter.")
    else:
        left, right = st.columns(2)
        with left:
            _show_current_item(current_item)
        with right:
            _show_context_card(view_model.get("current_context_card"), view_model.get("warnings", []))

    nav_prev, nav_next, nav_unresolved = st.columns(3)
    with nav_prev:
        if st.button("Vorige", key="serial_review_previous_button", disabled=resolved_index in (None, 0)):
            st.session_state["serial_review_current_index"] = max((resolved_index or 0) - 1, 0)
            st.session_state["serial_review_current_occurrence_id"] = None
            st.rerun()
    with nav_next:
        at_end = resolved_index is None or resolved_index >= max(queue.get("total_items", 0) - 1, 0)
        if st.button("Volgende", key="serial_review_next_button", disabled=at_end):
            st.session_state["serial_review_current_index"] = (resolved_index or 0) + 1
            st.session_state["serial_review_current_occurrence_id"] = None
            st.rerun()
    with nav_unresolved:
        next_unresolved = view_model.get("next_item")
        if st.button("Volgende onopgeloste", key="serial_review_next_unresolved_button", disabled=next_unresolved is None):
            st.session_state["serial_review_current_occurrence_id"] = next_unresolved.get("occurrence_id")
            st.rerun()

    render_review_highlight_toggle_panel(
        displayed_text=displayed_text,
        edited_replacements_df=edited_replacements_df,
    )

    return view_model
