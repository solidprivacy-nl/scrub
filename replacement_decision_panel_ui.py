"""Staged/read-only Streamlit panel for replacement decisions.

WP_REPLACE_LOGIC_UI_IMPLEMENTATION adds the first small replacement-decision
companion panel. It uses replacement_decision.py for preview/audit output only.
It does not mutate review rows, does not write edited_replacements_df, does not
write Streamlit data-editor state, does not apply replacements, does not write Scrub Key mappings,
does not block export, does not call export/download functions, does not change reinsert behavior,
does not use fuzzy matching or guess intent, does not add dependencies, does
not call cloud services and does not use real data.
"""

from __future__ import annotations

from typing import Any, Iterable

import streamlit as st

from replacement_decision import (
    build_replacement_audit,
    build_replacement_decision,
    matching_occurrence_ids,
)


ALLOWED_VIEW_ONLY_SESSION_KEYS = {
    "replacement_decision_selected_occurrence_id",
    "replacement_decision_preview_state",
    "replacement_decision_preview_scope",
    "replacement_decision_preview_text",
    "replacement_decision_panel_expanded",
}

STATE_LABELS = {
    "needs_review": "Later controleren / needs_review",
    "accepted": "Vervangen / accepted",
    "edited": "Vervanging aanpassen / edited",
    "ignored": "Zichtbaar houden / ignored",
    "manual_added": "Handmatig gemiste waarde toevoegen / manual_added",
    "preserve_context": "Als context behouden / preserve_context",
    "unresolved": "Later controleren / unresolved",
}

SCOPE_LABELS = {
    "this_occurrence": "Alleen deze plek / this_occurrence",
    "all_exact": "Alle exact dezelfde waarden / all_exact",
    "all_normalized": "Alle genormaliseerde gelijke waarden / all_normalized — advisory only",
}

READ_ONLY_BOUNDARY = (
    "staged decision preview only · staged decision state is not applied state · "
    "existing review table remains source of truth and fallback · no review table mutation · "
    "no automatic replacement · does not write Scrub Key mappings · no Scrub Key writes · "
    "no export blocking · no reinsert behavior change"
)

DUTCH_BOUNDARY = (
    "Vervanghulp · Alleen voorbeeld / nog niet toegepast · "
    "Bestaande vervangtabel blijft leidend · Geen automatische vervanging · "
    "Geen Scrub Key wijziging · Export wordt niet geblokkeerd · "
    "Terugzetten/originele waarden blijft ongewijzigd"
)


def _safe_text(value: Any) -> str:
    if value is None:
        return ""
    try:
        if value != value:  # NaN check without pandas dependency
            return ""
    except Exception:
        pass
    return str(value).strip()


def _safe_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if 0 <= number <= 1 else None


def _row_to_preview(row: dict[str, Any], *, index: int) -> dict[str, Any] | None:
    source_text = _safe_text(row.get("source_text") or row.get("find"))
    suggested = _safe_text(row.get("suggested_replacement") or row.get("replace_with"))
    if not source_text:
        return None

    occurrence_id = _safe_text(row.get("occurrence_id")) or f"replacement-preview-row-{index}"
    return {
        "occurrence_id": occurrence_id,
        "source_text": source_text,
        "entity_type": _safe_text(row.get("entity_type")) or "UNKNOWN",
        "display_label": _safe_text(row.get("display_label") or row.get("type_label")) or "Review-item",
        "suggested_replacement": suggested,
        "confidence": _safe_float(row.get("confidence") if row.get("confidence") not in (None, "") else row.get("score")),
        "context_preview": _safe_text(row.get("context_preview") or row.get("context")),
        "origin": _safe_text(row.get("source")) or "review_table",
        "risk_flags": list(row.get("risk_flags") or []),
    }


def _iter_review_rows(review_rows: Any) -> Iterable[tuple[int, dict[str, Any]]]:
    if review_rows is None:
        return []
    if hasattr(review_rows, "iterrows"):
        return ((int(index), dict(row)) for index, row in review_rows.iterrows())
    return ((index, dict(row)) for index, row in enumerate(review_rows or []))


def build_replacement_decision_preview_rows(review_rows: Any) -> list[dict[str, Any]]:
    """Build non-mutating rows for the staged replacement decision panel."""

    rows: list[dict[str, Any]] = []
    for index, row in _iter_review_rows(review_rows):
        preview = _row_to_preview(row, index=index)
        if preview is not None:
            rows.append(preview)
    return rows


def _selected_row(rows: list[dict[str, Any]], selected_occurrence_id: str | None) -> dict[str, Any]:
    selected = _safe_text(selected_occurrence_id)
    if selected:
        for row in rows:
            if row["occurrence_id"] == selected:
                return row
    return rows[0]


def _show_decision_fields(decision_dict: dict[str, Any], affected_count: int) -> None:
    cols = st.columns(4)
    cols[0].metric("Decision state", decision_dict.get("review_state", ""))
    cols[1].metric("Scope", decision_dict.get("scope", ""))
    cols[2].metric("Affected count", affected_count)
    cols[3].metric("Creates mapping", "advisory yes" if decision_dict.get("creates_mapping") else "advisory no")

    st.caption("source_text")
    st.code(decision_dict.get("source_text", ""), language=None)
    st.caption(f"entity_type: {decision_dict.get('entity_type', '')}")
    st.caption("suggested_replacement")
    st.code(decision_dict.get("suggested_replacement", ""), language=None)
    replacement_value = decision_dict.get("replacement_value")
    st.caption("replacement_value preview — advisory/report-only/not applied")
    st.code("" if replacement_value is None else replacement_value, language=None)


def render_replacement_decision_panel(*, review_rows: Any, current_occurrence_id: str | None = None) -> dict[str, Any] | None:
    """Render a staged/read-only replacement decision preview panel.

    The panel is advisory only. It returns helper output for tests/handover but
    does not mutate review rows, data-editor state, Scrub Key state, export state
    or reinsert state.
    """

    panel_expanded = bool(st.session_state.get("replacement_decision_panel_expanded", False))
    with st.expander("Replacement decision helper", expanded=panel_expanded):
        st.markdown("**Replacement decision helper**")
        st.info(DUTCH_BOUNDARY)
        st.caption(READ_ONLY_BOUNDARY)
        st.warning(
            "staged decision preview only. staged decision state is not applied state. "
            "Preview/advisory/report-only/not applied."
        )

        preview_rows = build_replacement_decision_preview_rows(review_rows)
        if not preview_rows:
            st.warning("Geen replacement decision preview beschikbaar. De bestaande vervangtabel blijft leidend.")
            return None

        selected_default = current_occurrence_id or st.session_state.get("replacement_decision_selected_occurrence_id")
        selected_row = _selected_row(preview_rows, selected_default)
        occurrence_ids = [row["occurrence_id"] for row in preview_rows]
        selected_id = st.selectbox(
            "Selected occurrence",
            occurrence_ids,
            index=occurrence_ids.index(selected_row["occurrence_id"]),
            key="replacement_decision_selected_occurrence_id",
            help="Wijzigt alleen de voorbeeldweergave, niet de vervangtabel.",
        )
        selected_row = _selected_row(preview_rows, selected_id)

        preview_state = st.selectbox(
            "Preview decision state",
            list(STATE_LABELS.keys()),
            index=0,
            format_func=lambda value: STATE_LABELS[value],
            key="replacement_decision_preview_state",
            help="Alleen staged preview; dit wordt niet toegepast.",
        )
        preview_scope = st.selectbox(
            "Preview scope",
            list(SCOPE_LABELS.keys()),
            index=0,
            format_func=lambda value: SCOPE_LABELS[value],
            key="replacement_decision_preview_scope",
            help="all_normalized is advisory only en geen eerste mutating scope.",
        )
        preview_text = st.text_input(
            "Preview replacement text",
            value=selected_row.get("suggested_replacement", ""),
            key="replacement_decision_preview_text",
            help="Alleen voorbeeldtekst; schrijft niet terug naar de vervangtabel.",
        )

        risk_flags = list(selected_row.get("risk_flags") or [])
        if preview_scope == "all_normalized":
            risk_flags.append("all_normalized_advisory_only_not_mutating")

        decision = build_replacement_decision(
            occurrence_id=selected_row["occurrence_id"],
            source_text=selected_row["source_text"],
            entity_type=selected_row["entity_type"],
            display_label=selected_row["display_label"],
            suggested_replacement=selected_row.get("suggested_replacement", ""),
            final_replacement=preview_text if preview_state == "edited" else None,
            review_state=preview_state,
            scope=preview_scope,
            confidence=selected_row.get("confidence"),
            context_preview=selected_row.get("context_preview", ""),
            origin=selected_row.get("origin", "review_table"),
            risk_flags=risk_flags,
        )
        affected_ids = matching_occurrence_ids(decision, preview_rows)
        audit = build_replacement_audit([decision])
        decision_dict = decision.as_dict()

        _show_decision_fields(decision_dict, len(affected_ids))
        st.caption("Affected occurrence ids — advisory only")
        st.write(affected_ids)

        st.markdown("**Advisory audit fields**")
        audit_cols = st.columns(4)
        audit_cols[0].metric("Unresolved", len(audit.get("unresolved_items", [])))
        audit_cols[1].metric("Mapping candidates", len(audit.get("mapping_candidates", [])))
        audit_cols[2].metric("Risk flags", len(audit.get("risk_flags", [])))
        audit_cols[3].metric("Export readiness", audit.get("export_readiness", ""))
        st.caption("creates_mapping, mapping_candidates and export_readiness are advisory only.")
        st.caption("No review table mutation · No automatic replacement · does not write Scrub Key mappings · No Scrub Key writes · No export blocking · No reinsert behavior change")

        if audit.get("risk_flags"):
            st.warning("Risk flags: " + ", ".join(audit.get("risk_flags", [])))

        return {
            "decision": decision_dict,
            "affected_occurrence_ids": affected_ids,
            "affected_count": len(affected_ids),
            "audit": audit,
            "staged_decision_preview_only": True,
            "staged_decision_state_is_not_applied_state": True,
            "existing_review_table_remains_source_of_truth_and_fallback": True,
            "review_table_mutation": False,
            "automatic_replacement": False,
            "scrub_key_writes": False,
            "export_blocking": False,
            "reinsert_behavior_change": False,
            "fuzzy_matching": False,
            "guessed_intent": False,
            "cloud_processing": False,
        }
