from premium_app_shell import (
    STAGE_LABELS,
    build_app_shell_view,
    stage_is_active,
    standard_view_hides_configuration_sidebar,
)
from premium_core_flow_state import CoreFlowState, PresentationMode, Stage, Workflow


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
    state = CoreFlowState(presentation_mode=PresentationMode.EXPERT, stage=Stage.REVIEW)
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
        state = CoreFlowState(stage=active)
        assert [stage_is_active(state, stage) for stage in Stage].count(True) == 1
        assert STAGE_LABELS[active] == build_app_shell_view(state).active_stage_label
