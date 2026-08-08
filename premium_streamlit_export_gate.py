"""Executable Streamlit guard for Premium review-to-export readiness.

This module is intentionally narrow: it does not build export payloads or alter
recognition/replacement semantics. It only enforces that the existing export
surface stays unavailable until human review is explicitly current for the
active processing generation.
"""
from __future__ import annotations

from typing import Any, Mapping, MutableMapping, Sequence

import streamlit as st

from premium_streamlit_state import (
    cache_review_rows,
    get_core_flow_state,
    mark_review_complete,
    set_stage_summary,
)
from premium_core_flow_state import Stage


EXPERT_REVIEW_RECONFIRM_LABEL = "Controle opnieuw afronden"


def export_surface_is_current(session_state: MutableMapping[str, Any]) -> bool:
    """Return whether document export is valid for the current lineage."""
    return get_core_flow_state(session_state).export_is_current


def _review_summary(rows: Sequence[Mapping[str, Any]]) -> str:
    manual_count = sum(1 for row in rows if str(row.get("source", "")) == "manual")
    summary = f"{len(rows)} gecontroleerd"
    if manual_count:
        summary += f" · {manual_count} handmatig toegevoegd"
    return summary


def render_export_readiness_gate(
    session_state: MutableMapping[str, Any],
    *,
    is_expert: bool,
    generation: str,
    reviewed_rows: Sequence[Mapping[str, Any]],
) -> bool:
    """Render the explicit Expert re-completion gate and return export eligibility.

    Presentation-only Standard/Expert switches keep a completed current review
    eligible. A real review edit clears review/export lineage elsewhere in the
    state model; this guard then blocks every downstream export control until
    the user explicitly completes review again. Processing/source changes are
    not review-completable here and remain blocked until reprocessing.
    """
    state = get_core_flow_state(session_state)
    if state.export_is_current:
        return True

    current_processing_is_reviewable = (
        bool(generation)
        and state.source_generation == generation
        and state.processed_generation == generation
    )
    if not current_processing_is_reviewable:
        if is_expert:
            st.warning(
                "Downloaden is geblokkeerd omdat de bron of verwerkingsinstellingen zijn gewijzigd. "
                "Verwerk het document opnieuw en rond daarna de controle af."
            )
        return False

    if not is_expert:
        return False

    st.warning(
        "De controle is gewijzigd. Downloaden blijft geblokkeerd totdat je de huidige "
        "controle opnieuw expliciet afrondt."
    )
    if st.button(
        EXPERT_REVIEW_RECONFIRM_LABEL,
        type="primary",
        use_container_width=True,
        key="premium_expert_recomplete_review",
    ):
        cache_review_rows(session_state, generation, reviewed_rows)
        set_stage_summary(session_state, Stage.REVIEW, _review_summary(reviewed_rows))
        mark_review_complete(session_state)
        st.rerun()

    st.caption(
        "De aangepaste vervangtabel blijft bewaard. Er wordt niets automatisch goedgekeurd of geëxporteerd."
    )
    return False
