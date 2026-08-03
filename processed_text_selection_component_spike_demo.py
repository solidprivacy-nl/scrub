"""Standalone synthetic demo for the processed-text selection component spike.

Run manually with:

    streamlit run processed_text_selection_component_spike_demo.py

The demo may inspect a selection through the pure action model, but it never
calls ``commit_manual_mask`` and never creates or inserts a replacement row.
"""

from __future__ import annotations

from typing import Any, Mapping

import streamlit as st

from manual_mask_entry import manual_mask_document_key
from processed_text_selection_component import (
    COMPONENT_HEIGHT,
    render_processed_text_selection_component_spike,
)
from selection_mask_action import (
    SelectionActionState,
    inspect_selection,
    parse_commit_event,
    processed_text_hash,
)


SYNTHETIC_EXISTING_VALUE = "SYNTHETIC-BESTAAND"
SYNTHETIC_MISSED_VALUE = "SYNTHETIC-ALFA"
SYNTHETIC_PLACEHOLDER = "[PERSOON_BAAAAAAAAAAAAAAAA_01]"

SOURCE_TEXT = (
    "😀 Synthetische starttekst voor de Unicode-offsetproef.\n\n"
    f"De bestaande waarde {SYNTHETIC_EXISTING_VALUE} is al gemaskeerd. "
    f"De gemiste waarde {SYNTHETIC_MISSED_VALUE} staat nog zichtbaar.\n\n"
    f"Verderop staat {SYNTHETIC_MISSED_VALUE} nogmaals, zodat de server twee "
    "exacte voorkomens moet rapporteren. Alle waarden in deze demo zijn synthetisch."
)
PROCESSED_TEXT = SOURCE_TEXT.replace(SYNTHETIC_EXISTING_VALUE, SYNTHETIC_PLACEHOLDER)
HIGHLIGHT_START = PROCESSED_TEXT.index(SYNTHETIC_PLACEHOLDER)
HIGHLIGHT_SPANS = ((HIGHLIGHT_START, HIGHLIGHT_START + len(SYNTHETIC_PLACEHOLDER)),)
EXISTING_ROWS = (
    {
        "include": True,
        "remember": False,
        "find": SYNTHETIC_EXISTING_VALUE,
        "replace_with": SYNTHETIC_PLACEHOLDER,
        "entity_type": "PERSON",
        "source": "synthetic_spike_demo",
    },
)
DOCUMENT_SCOPE_KEY = manual_mask_document_key(SOURCE_TEXT)
PROCESSED_HASH = processed_text_hash(PROCESSED_TEXT)


def _state() -> SelectionActionState:
    state = st.session_state.get("component_spike_action_state")
    if isinstance(state, SelectionActionState):
        return state
    state = SelectionActionState()
    st.session_state["component_spike_action_state"] = state
    return state


def _inspection_result() -> Mapping[str, Any]:
    value = st.session_state.get("component_spike_inspection_result")
    return dict(value) if isinstance(value, Mapping) else {}


def _scroll_ratio(event: Mapping[str, Any], field: str) -> float | None:
    ui_state = event.get("ui_state")
    if not isinstance(ui_state, Mapping):
        return None
    value = ui_state.get(field)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    ratio = float(value)
    return ratio if 0.0 <= ratio <= 1.0 else None


def _handle_component_event(event: Mapping[str, Any]) -> None:
    event_id = str(event.get("event_id", ""))
    if not event_id or event_id == st.session_state.get("component_spike_last_raw_event_id"):
        return
    st.session_state["component_spike_last_raw_event_id"] = event_id
    st.session_state["component_spike_last_raw_event"] = dict(event)

    action = str(event.get("action", ""))
    if action == "inspect_selection":
        result = inspect_selection(
            event,
            source_text=SOURCE_TEXT,
            processed_text=PROCESSED_TEXT,
            current_document_scope_key=DOCUMENT_SCOPE_KEY,
            existing_rows=EXISTING_ROWS,
            marked_ranges=HIGHLIGHT_SPANS,
            document_binding_id="BAAAAAAAAAAAAAAAA",
            state=_state(),
        )
        st.session_state["component_spike_inspection_result"] = result.to_dict()
        st.session_state["component_spike_restore_source"] = _scroll_ratio(
            event,
            "source_scroll_ratio",
        )
        st.session_state["component_spike_restore_processed"] = _scroll_ratio(
            event,
            "processed_scroll_ratio",
        )
        st.rerun()

    if action == "commit_manual_mask":
        try:
            parsed = parse_commit_event(event)
        except ValueError as exc:
            st.session_state["component_spike_commit_status"] = {
                "valid": False,
                "message": str(exc),
            }
        else:
            st.session_state["component_spike_commit_status"] = {
                "valid": True,
                "message": (
                    "Geldig commit-intent ontvangen voor "
                    f"‘{parsed.requested_type}’. De spike heeft bewust geen rij toegevoegd."
                ),
                "event": dict(event),
            }
            _state().invalidate_inspection(parsed.inspection_id)
            st.session_state["component_spike_inspection_result"] = {}
        st.rerun()


st.set_page_config(page_title="SolidPrivacy component spike", layout="wide")
st.title("Processed-text selection component spike")
st.caption(
    "Synthetische, niet-muterende technische proef. Selecteer SYNTHETIC-ALFA in "
    "Verwerkte tekst en gebruik rechterklik, Shift+F10 of Masker selectie."
)
st.info(
    "De proef valideert selecties en kan een commit-intent tonen, maar wijzigt geen "
    "vervangtabel, document, export, Scrub Key of reinsertstatus."
)

raw_event = render_processed_text_selection_component_spike(
    source_text=SOURCE_TEXT,
    processed_text=PROCESSED_TEXT,
    highlight_spans=HIGHLIGHT_SPANS,
    document_scope_key=DOCUMENT_SCOPE_KEY,
    processed_text_hash=PROCESSED_HASH,
    inspection_result=_inspection_result(),
    restore_source_scroll_ratio=st.session_state.get("component_spike_restore_source"),
    restore_processed_scroll_ratio=st.session_state.get("component_spike_restore_processed"),
    key="processed_text_selection_component_spike_demo",
)

if isinstance(raw_event, Mapping):
    _handle_component_event(raw_event)

commit_status = st.session_state.get("component_spike_commit_status")
if isinstance(commit_status, Mapping):
    if commit_status.get("valid"):
        st.success(str(commit_status.get("message", "Geldig niet-muterend intent ontvangen.")))
    else:
        st.error(str(commit_status.get("message", "Ongeldig intent-event.")))

with st.expander("Laatste component-event — synthetische technische details"):
    st.json(st.session_state.get("component_spike_last_raw_event", {}))

with st.expander("Componentgrenzen"):
    st.write(
        {
            "component_height": COMPONENT_HEIGHT,
            "document_scope_key": DOCUMENT_SCOPE_KEY,
            "processed_text_hash": PROCESSED_HASH,
            "highlight_spans_python": HIGHLIGHT_SPANS,
            "calls_commit_manual_mask": False,
            "replacement_rows_added": 0,
            "production_ui_integrated": False,
        }
    )
