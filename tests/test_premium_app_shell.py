import pytest

from premium_app_shell import (
    STAGE_LABELS,
    StagePanelStatus,
    build_app_shell_view,
    open_stage,
    stage_can_open,
    stage_is_active,
    standard_view_hides_configuration_sidebar,
)
from premium_core_flow_state import CoreFlowState, PresentationMode, Stage, Workflow


def processed_state(generation="g1"):
    return CoreFlowState().with_source(generation).with_processed_result(generation)


def reviewed_state(generation="g1"):
    return processed_state(generation).complete_review()


def test_standard_shell_uses_approved_labels_and_hides_configuration_sidebar():
    state = CoreFlowState()
    view = build_app_shell_view(state)
    assert view.workflow_label == "Anonimiseren"
    assert view.presentation_label == "Standaard"
    assert view.stage_labels == ("Toevoegen", "Controleren", "Downloaden")
    assert view.active_stage_label == "Toevoegen"
    assert view.show_configuration_sidebar is False
    assert standard_view_hides_configuration_sidebar(state) is True


def test_expert_shell_keeps_same_stage_model_and_exposes_configuration_surface():
    state = processed_state().with_presentation_mode(PresentationMode.EXPERT)
    view = build_app_shell_view(state)
    assert view.presentation_label == "Expert"
    assert view.stage_labels == ("Toevoegen", "Controleren", "Downloaden")
    assert view.active_stage_label == "Controleren"
    assert view.show_configuration_sidebar is True
    assert standard_view_hides_configuration_sidebar(state) is False


def test_reinsert_workflow_uses_customer_facing_top_level_label():
    state = CoreFlowState(workflow=Workflow.REINSERT)
    assert build_app_shell_view(state).workflow_label == "Terugzetten"


def test_exactly_one_stage_is_active():
    for active in Stage:
        if active is Stage.ADD:
            state = CoreFlowState(stage=active)
        elif active is Stage.REVIEW:
            state = processed_state()
        else:
            state = reviewed_state()
        assert [stage_is_active(state, stage) for stage in Stage].count(True) == 1
        assert STAGE_LABELS[active] == build_app_shell_view(state).active_stage_label


def test_initial_standard_workspace_has_active_add_and_passive_future_stages():
    panels = build_app_shell_view(CoreFlowState()).stage_panels
    assert [panel.status for panel in panels] == [
        StagePanelStatus.ACTIVE,
        StagePanelStatus.FUTURE,
        StagePanelStatus.FUTURE,
    ]
    assert [panel.can_open for panel in panels] == [True, False, False]


def test_successful_processing_auto_state_maps_to_completed_add_active_review():
    panels = build_app_shell_view(
        processed_state(),
        {Stage.ADD: "contract.docx · Juridisch"},
    ).stage_panels
    assert [panel.status for panel in panels] == [
        StagePanelStatus.COMPLETED,
        StagePanelStatus.ACTIVE,
        StagePanelStatus.FUTURE,
    ]
    assert panels[0].summary == "contract.docx · Juridisch"
    assert panels[2].can_open is False


def test_explicit_review_completion_maps_to_download_and_compact_summaries():
    view = build_app_shell_view(
        reviewed_state(),
        {
            Stage.ADD: "contract.docx · Juridisch",
            Stage.REVIEW: "14 gecontroleerd · 1 handmatig toegevoegd",
        },
    )
    assert [panel.status for panel in view.stage_panels] == [
        StagePanelStatus.COMPLETED,
        StagePanelStatus.COMPLETED,
        StagePanelStatus.ACTIVE,
    ]
    assert view.stage_panels[0].summary == "contract.docx · Juridisch"
    assert view.stage_panels[1].summary == "14 gecontroleerd · 1 handmatig toegevoegd"


def test_returning_to_earlier_stage_preserves_valid_lineage_until_an_edit_occurs():
    original = reviewed_state()
    returned = open_stage(original, Stage.ADD)
    assert returned.source_generation == original.source_generation
    assert returned.processed_generation == original.processed_generation
    assert returned.reviewed_generation == original.reviewed_generation
    assert returned.export_generation == original.export_generation
    assert stage_can_open(returned, Stage.REVIEW) is True
    assert stage_can_open(returned, Stage.DOWNLOAD) is True
    assert [panel.status for panel in build_app_shell_view(returned).stage_panels] == [
        StagePanelStatus.ACTIVE,
        StagePanelStatus.COMPLETED,
        StagePanelStatus.COMPLETED,
    ]


def test_processing_affecting_change_fails_closed_to_add_and_future_downstream():
    stale = reviewed_state().invalidate_for_processing_change()
    assert [panel.status for panel in build_app_shell_view(stale).stage_panels] == [
        StagePanelStatus.ACTIVE,
        StagePanelStatus.FUTURE,
        StagePanelStatus.FUTURE,
    ]
    assert stage_can_open(stale, Stage.REVIEW) is False
    assert stage_can_open(stale, Stage.DOWNLOAD) is False


def test_ineligible_future_stage_cannot_be_opened():
    with pytest.raises(ValueError, match="not eligible"):
        open_stage(CoreFlowState(), Stage.DOWNLOAD)


def test_summaries_are_not_rendered_for_active_or_future_stages():
    view = build_app_shell_view(
        CoreFlowState(),
        {
            Stage.ADD: "should stay hidden while active",
            Stage.REVIEW: "should stay hidden while future",
        },
    )
    assert view.stage_panels[0].summary is None
    assert view.stage_panels[1].summary is None
