"""Thin Streamlit renderer for Premium staged-workspace chrome only.

Stage internals stay in ``presidio_streamlit.py`` for this workpackage. This
module renders application-panel headers rather than generic expanders and
routes explicit return/open actions through the pure core-flow state adapter.
"""
from __future__ import annotations

import streamlit as st

from premium_app_shell import StagePanelStatus, build_app_shell_view
from premium_core_flow_state import CoreFlowState, Stage
from premium_streamlit_state import get_stage_summaries, select_stage


_STAGE_NUMBER = {
    Stage.ADD: 1,
    Stage.REVIEW: 2,
    Stage.DOWNLOAD: 3,
}

_FUTURE_STATUS = {
    Stage.REVIEW: "Beschikbaar na verwerking",
    Stage.DOWNLOAD: "Beschikbaar na controle",
}


def render_stage_header(state: CoreFlowState, stage: Stage) -> None:
    """Render one persistent accordion-style stage header.

    Exactly one header is marked active by ``CoreFlowState``. Completed stages
    expose one explicit return action; future stages are visible but passive.
    """
    view = build_app_shell_view(state, get_stage_summaries(st.session_state))
    panel = next(item for item in view.stage_panels if item.stage is stage)
    number = _STAGE_NUMBER[stage]

    with st.container(border=True):
        label_col, action_col = st.columns([5, 1])
        with label_col:
            if panel.status is StagePanelStatus.ACTIVE:
                st.markdown(f"**● {number}. {panel.label}**")
                st.caption("Actieve werkruimte")
            elif panel.status is StagePanelStatus.COMPLETED:
                st.markdown(f"**✓ {number}. {panel.label}**")
                if panel.summary:
                    st.caption(panel.summary)
                else:
                    st.caption("Gereed")
            else:
                st.markdown(f"**○ {number}. {panel.label}**")
                st.caption(_FUTURE_STATUS.get(stage, "Nog niet beschikbaar"))

        with action_col:
            if panel.status is StagePanelStatus.COMPLETED and panel.can_open:
                if st.button(
                    "Openen",
                    key=f"premium_open_stage_{stage.value}",
                    use_container_width=True,
                ):
                    select_stage(st.session_state, stage)
                    st.rerun()
