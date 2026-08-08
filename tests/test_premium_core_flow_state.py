import pytest

from premium_core_flow_state import (
    CoreFlowState,
    PresentationMode,
    Stage,
    Workflow,
    recommended_download,
)


def processed_state():
    return CoreFlowState().with_source("g1").with_processed_result("g1")


def test_initial_standard_anonymization_opens_at_add():
    state = CoreFlowState()
    assert (state.workflow, state.presentation_mode, state.stage) == (
        Workflow.ANONYMIZE, PresentationMode.STANDARD, Stage.ADD
    )


def test_expert_switch_preserves_authoritative_lineage():
    state = processed_state()
    assert state.with_presentation_mode(PresentationMode.EXPERT) == CoreFlowState(
        workflow=state.workflow, presentation_mode=PresentationMode.EXPERT,
        stage=state.stage, source_generation=state.source_generation,
        processed_generation=state.processed_generation,
        reviewed_generation=state.reviewed_generation,
        export_generation=state.export_generation,
    )


def test_returning_to_standard_preserves_state():
    state = processed_state().with_presentation_mode(PresentationMode.EXPERT)
    returned = state.with_presentation_mode(PresentationMode.STANDARD)
    assert returned.stage == Stage.REVIEW
    assert returned.source_generation == returned.processed_generation == "g1"


def test_valid_processing_advances_add_to_review():
    assert processed_state().stage == Stage.REVIEW


def test_invalid_or_stale_processing_cannot_advance():
    with pytest.raises(ValueError):
        CoreFlowState().with_source("g2").with_processed_result("g1")


def test_completed_current_review_advances_to_download():
    state = processed_state().complete_review()
    assert state.stage == Stage.DOWNLOAD
    assert state.export_is_current


def test_source_replacement_invalidates_review_and_download():
    state = processed_state().complete_review().with_source("g2")
    assert state.stage == Stage.ADD
    assert state.processed_generation is state.reviewed_generation is state.export_generation is None


def test_processing_affecting_profile_change_invalidates_downstream():
    state = processed_state().complete_review().invalidate_for_processing_change()
    assert state.stage == Stage.ADD
    assert state.source_generation == "g1"
    assert state.processed_generation is state.reviewed_generation is state.export_generation is None


def test_presentation_only_change_does_not_invalidate_processing():
    state = processed_state().complete_review()
    assert state.with_presentation_only_change() is state
    assert state.export_is_current


def test_manual_review_authority_is_outside_presentation_model():
    state = processed_state()
    before = state
    after = state.with_presentation_mode(PresentationMode.EXPERT).with_presentation_mode(PresentationMode.STANDARD)
    assert after.source_generation == before.source_generation
    assert after.processed_generation == before.processed_generation


def test_recommended_download_returns_only_existing_eligible_output():
    eligible = ["cleaned_txt", "cleaned_docx"]
    assert recommended_download("docx", eligible) == "cleaned_docx"
    assert recommended_download("docx", eligible) in eligible


def test_scrub_key_is_not_created_or_selected_by_download_priority():
    eligible = ["scrub_key", "cleaned_txt"]
    assert recommended_download("txt", eligible) == "cleaned_txt"


def test_scrub_key_alone_is_never_promoted_to_recommended_download():
    assert recommended_download("txt", ["scrub_key"]) is None
    assert recommended_download("docx", ["scrub_key"]) is None
    assert recommended_download("unknown", ["scrub_key"]) is None


def test_workflow_navigation_cannot_leak_stale_state():
    state = processed_state().complete_review().with_workflow(Workflow.REINSERT)
    assert state.workflow == Workflow.REINSERT
    assert state.stage == Stage.ADD
    assert state.source_generation is state.processed_generation is state.reviewed_generation is state.export_generation is None


def test_stage_transitions_are_pure_state_operations():
    original = CoreFlowState()
    processed = original.with_source("g1").with_processed_result("g1")
    reviewed = processed.complete_review()
    assert original == CoreFlowState()
    assert processed.stage == Stage.REVIEW
    assert reviewed.stage == Stage.DOWNLOAD
