"""Presentation-only primitives for the premium SolidPrivacy Scrub app shell.

The helpers in this module translate the independently approved core-flow state
into Dutch UI labels, staged-workspace status and safe navigation decisions.
They deliberately do not invoke recognition, replacement, export, Scrub Key,
reinsert, audit, or Streamlit session-state mutation.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Mapping, Optional

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


class StagePanelStatus(str, Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    FUTURE = "future"


@dataclass(frozen=True)
class StagePanelView:
    stage: Stage
    label: str
    status: StagePanelStatus
    summary: Optional[str]
    can_open: bool

    @property
    def is_active(self) -> bool:
        return self.status is StagePanelStatus.ACTIVE


@dataclass(frozen=True)
class AppShellView:
    workflow_label: str
    presentation_label: str
    stage_labels: tuple[str, str, str]
    active_stage_label: str
    show_configuration_sidebar: bool
    stage_panels: tuple[StagePanelView, StagePanelView, StagePanelView]


def _processed_is_current(state: CoreFlowState) -> bool:
    generation = state.source_generation
    return generation is not None and state.processed_generation == generation


def _review_is_current(state: CoreFlowState) -> bool:
    generation = state.source_generation
    return (
        generation is not None
        and state.processed_generation == generation
        and state.reviewed_generation == generation
    )


def _export_lineage_is_current(state: CoreFlowState) -> bool:
    generation = state.source_generation
    return (
        generation is not None
        and state.processed_generation == generation
        and state.reviewed_generation == generation
        and state.export_generation == generation
    )


def stage_can_open(state: CoreFlowState, stage: Stage) -> bool:
    """Return whether a stage is eligible without changing processing lineage."""
    if stage is Stage.ADD:
        return True
    if stage is Stage.REVIEW:
        return _processed_is_current(state)
    if stage is Stage.DOWNLOAD:
        return _export_lineage_is_current(state)
    return False


def open_stage(state: CoreFlowState, stage: Stage) -> CoreFlowState:
    """Open an eligible stage with fail-closed downstream handling.

    Returning to Add is presentation-only until a processing-affecting input is
    actually changed. Reopening a completed Review is different: that stage is
    authoritative for export decisions, so Download becomes ineligible until
    the review is explicitly completed again. This prevents an edited review
    from leaving stale export lineage available through a completed header.
    """
    if not stage_can_open(state, stage):
        raise ValueError(f"stage {stage.value} is not eligible")
    if stage is Stage.REVIEW and _review_is_current(state):
        return replace(
            state,
            stage=Stage.REVIEW,
            reviewed_generation=None,
            export_generation=None,
        )
    return replace(state, stage=stage)


def stage_panel_status(state: CoreFlowState, stage: Stage) -> StagePanelStatus:
    if state.stage is stage:
        return StagePanelStatus.ACTIVE
    if stage is Stage.ADD and _processed_is_current(state):
        return StagePanelStatus.COMPLETED
    if stage is Stage.REVIEW and _review_is_current(state):
        return StagePanelStatus.COMPLETED
    if stage is Stage.DOWNLOAD and _export_lineage_is_current(state):
        return StagePanelStatus.COMPLETED
    return StagePanelStatus.FUTURE


def build_stage_panels(
    state: CoreFlowState,
    completed_summaries: Optional[Mapping[Stage, str]] = None,
) -> tuple[StagePanelView, StagePanelView, StagePanelView]:
    """Build the three persistent staged-workspace headers.

    Summaries are intentionally emitted only for completed stages so a summary
    cannot become a competing mini-form inside the active/future stage header.
    """
    summaries = completed_summaries or {}
    panels = []
    for stage in (Stage.ADD, Stage.REVIEW, Stage.DOWNLOAD):
        status = stage_panel_status(state, stage)
        panels.append(
            StagePanelView(
                stage=stage,
                label=STAGE_LABELS[stage],
                status=status,
                summary=summaries.get(stage) if status is StagePanelStatus.COMPLETED else None,
                can_open=stage_can_open(state, stage),
            )
        )
    return tuple(panels)  # type: ignore[return-value]


def build_app_shell_view(
    state: CoreFlowState,
    completed_summaries: Optional[Mapping[Stage, str]] = None,
) -> AppShellView:
    """Return the shell-only view model for the current core-flow state."""
    return AppShellView(
        workflow_label=WORKFLOW_LABELS[state.workflow],
        presentation_label=PRESENTATION_LABELS[state.presentation_mode],
        stage_labels=tuple(STAGE_LABELS[stage] for stage in (Stage.ADD, Stage.REVIEW, Stage.DOWNLOAD)),
        active_stage_label=STAGE_LABELS[state.stage],
        show_configuration_sidebar=state.presentation_mode is PresentationMode.EXPERT,
        stage_panels=build_stage_panels(state, completed_summaries),
    )


def stage_is_active(state: CoreFlowState, stage: Stage) -> bool:
    """Only one stage may be the dominant workspace at a time."""
    return state.stage is stage


def standard_view_hides_configuration_sidebar(state: CoreFlowState) -> bool:
    """Freeze the approved Standard-view rule without mutating any settings."""
    return state.presentation_mode is PresentationMode.STANDARD
