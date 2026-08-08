"""Presentation-only primitives for the premium SolidPrivacy Scrub app shell.

The helpers in this module translate the independently approved core-flow state
into Dutch UI labels and visibility decisions. They deliberately do not invoke
recognition, replacement, export, Scrub Key, reinsert, audit, or Streamlit
session-state mutation. Production Streamlit integration remains the next slice
of SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION.
"""
from __future__ import annotations

from dataclasses import dataclass

from premium_core_flow_state import CoreFlowState, PresentationMode, Stage, Workflow


WORKFLOW_LABELS = {
    Workflow.ANONYMIZE: "Anonimiseren",
    Workflow.REINSERT: "Terugzetten",
}

PRESENTATION_LABELS = {
    PresentationMode.STANDARD: "Standaard",
    PresentationMode.EXPERT: "Expert",
}

STAGE_LABELS = {
    Stage.ADD: "Toevoegen",
    Stage.REVIEW: "Controleren",
    Stage.DOWNLOAD: "Downloaden",
}


@dataclass(frozen=True)
class AppShellView:
    workflow_label: str
    presentation_label: str
    stage_labels: tuple[str, str, str]
    active_stage_label: str
    show_configuration_sidebar: bool


def build_app_shell_view(state: CoreFlowState) -> AppShellView:
    """Return the shell-only view model for the current core-flow state."""
    return AppShellView(
        workflow_label=WORKFLOW_LABELS[state.workflow],
        presentation_label=PRESENTATION_LABELS[state.presentation_mode],
        stage_labels=tuple(STAGE_LABELS[stage] for stage in (Stage.ADD, Stage.REVIEW, Stage.DOWNLOAD)),
        active_stage_label=STAGE_LABELS[state.stage],
        show_configuration_sidebar=state.presentation_mode is PresentationMode.EXPERT,
    )


def stage_is_active(state: CoreFlowState, stage: Stage) -> bool:
    """Only one stage may be the dominant workspace at a time."""
    return state.stage is stage


def standard_view_hides_configuration_sidebar(state: CoreFlowState) -> bool:
    """Freeze the approved Standard-view rule without mutating any settings."""
    return state.presentation_mode is PresentationMode.STANDARD
