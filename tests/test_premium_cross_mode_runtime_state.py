from pathlib import Path

from premium_core_flow_state import PresentationMode, Stage, Workflow
from premium_streamlit_state import (
    SOURCE_TEXT_KEY,
    cache_analysis_results,
    cache_review_rows,
    get_cached_analysis_results,
    get_cached_review_rows,
    get_core_flow_state,
    mark_processing_complete,
    mark_review_complete,
    processing_generation,
    review_rows_changed,
    select_stage,
    stored_source_text,
    synchronize_processing_generation,
    synchronize_shell_choices,
)


ROOT = Path(__file__).resolve().parents[1]


def generation(text="Zorgbron", profile="Dutch Care Strict", threshold=0.30):
    return processing_generation(
        text=text,
        profile=profile,
        operator="replace",
        threshold=threshold,
        entities=["PERSON", "NL_CARE_CLIENT_NUMBER"],
        allow_list=["veilig"],
        deny_list=["extra"],
        analyzer_params=["flair", "ner-english-large", "", ""],
    )


def completed_download_session():
    session = {SOURCE_TEXT_KEY: "Cliënt C-100 heeft een afspraak."}
    current_generation = generation(text=session[SOURCE_TEXT_KEY])
    synchronize_processing_generation(session, current_generation)
    mark_processing_complete(session, current_generation)
    cache_analysis_results(session, current_generation, ["analysis"])
    cache_review_rows(
        session,
        current_generation,
        [
            {
                "include": True,
                "find": "C-100",
                "replace_with": "[CLIENT_01]",
                "score": float("nan"),
            }
        ],
    )
    mark_review_complete(session)
    return session, current_generation


def test_completed_standard_download_survives_expert_roundtrip_without_lineage_change():
    session, current_generation = completed_download_session()
    before = get_core_flow_state(session)

    expert = synchronize_shell_choices(
        session,
        workflow=Workflow.ANONYMIZE,
        presentation_mode=PresentationMode.EXPERT,
    )
    assert stored_source_text(session) == "Cliënt C-100 heeft een afspraak."
    assert get_cached_analysis_results(session, current_generation) == ["analysis"]
    assert get_cached_review_rows(session, current_generation)[0]["find"] == "C-100"
    assert expert.source_generation == before.source_generation
    assert expert.processed_generation == before.processed_generation
    assert expert.reviewed_generation == before.reviewed_generation
    assert expert.export_generation == before.export_generation

    standard = synchronize_shell_choices(
        session,
        workflow=Workflow.ANONYMIZE,
        presentation_mode=PresentationMode.STANDARD,
    )
    assert standard.source_generation == current_generation
    assert standard.processed_generation == current_generation
    assert standard.reviewed_generation == current_generation
    assert standard.export_generation == current_generation


def test_review_cache_is_generation_bound_and_cleared_by_real_processing_change():
    session, current_generation = completed_download_session()
    changed_generation = generation(text="Andere zorgbron")

    state, changed = synchronize_processing_generation(session, changed_generation)

    assert changed is True
    assert state.source_generation == changed_generation
    assert state.processed_generation is None
    assert state.reviewed_generation is None
    assert state.export_generation is None
    assert get_cached_analysis_results(session, current_generation) is None
    assert get_cached_review_rows(session, current_generation) is None
    assert get_cached_review_rows(session, changed_generation) is None


def test_review_row_change_detection_tolerates_nan_but_detects_decision_change():
    old = [{"include": True, "find": "C-100", "score": float("nan")}]
    same = [{"include": True, "find": "C-100", "score": float("nan")}]
    changed = [{"include": False, "find": "C-100", "score": float("nan")}]

    assert review_rows_changed(old, same) is False
    assert review_rows_changed(old, changed) is True


def test_expert_review_edit_can_fail_closed_back_to_review_without_losing_processing_lineage():
    session, current_generation = completed_download_session()
    assert review_rows_changed(
        get_cached_review_rows(session, current_generation),
        [{"include": False, "find": "C-100", "replace_with": "[CLIENT_01]", "score": float("nan")}],
    ) is True

    reopened = select_stage(session, Stage.REVIEW)

    assert reopened.source_generation == current_generation
    assert reopened.processed_generation == current_generation
    assert reopened.reviewed_generation is None
    assert reopened.export_generation is None


def test_streamlit_runtime_uses_shared_source_analysis_and_review_state_in_both_modes():
    source = (ROOT / "presidio_streamlit.py").read_text(encoding="utf-8")

    assert 'input_text = stored_source_text(st.session_state, "".join(demo_text))' in source
    assert 'if is_premium_standard\n            else "".join(demo_text)' not in source
    assert 'cached_analysis_results = get_cached_analysis_results(' in source
    assert 'if is_premium_standard and not stage_is_active(premium_state, Stage.ADD):' not in source
    assert 'cached_review_rows = get_cached_review_rows(' in source
    assert 'cache_review_rows(' in source
    assert 'review_working_set_changed' in source
    assert 'premium_state = select_stage(st.session_state, Stage.REVIEW)' in source
    assert 'st.session_state["_premium_cached_review_rows"] = (' not in source
