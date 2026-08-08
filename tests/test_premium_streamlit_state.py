from premium_core_flow_state import PresentationMode, Stage, Workflow
from premium_streamlit_state import (
    ALLOW_LIST_KEY,
    ANALYSIS_GENERATION_KEY,
    ANALYSIS_RESULTS_KEY,
    ANALYZER_PARAMS_KEY,
    CORE_STATE_KEY,
    DENY_LIST_KEY,
    ENTITIES_KEY,
    OPERATOR_VALUE_KEY,
    PROFILE_LABEL_KEY,
    STAGE_SUMMARIES_KEY,
    THRESHOLD_KEY,
    analyzer_model_label,
    cache_analysis_results,
    get_cached_analysis_results,
    get_core_flow_state,
    get_stage_summaries,
    mark_processing_complete,
    mark_review_complete,
    persist_processing_settings,
    processing_generation,
    select_stage,
    set_stage_summary,
    stored_analyzer_params,
    stored_entities,
    stored_operator_value,
    stored_profile_label,
    stored_string_list,
    stored_threshold,
    synchronize_processing_generation,
    synchronize_shell_choices,
)


def generation(
    text="Contract A",
    profile="Dutch Legal Strict",
    operator="replace",
    threshold=0.5,
    entities=None,
    allow_list=None,
    deny_list=None,
    analyzer_params=None,
):
    return processing_generation(
        text=text,
        profile=profile,
        operator=operator,
        threshold=threshold,
        entities=entities or ["PERSON", "EMAIL_ADDRESS"],
        allow_list=allow_list or [],
        deny_list=deny_list or [],
        analyzer_params=analyzer_params or ["flair", "ner-english-large", "", ""],
    )


def test_adapter_initializes_standard_anonymize_state():
    session = {}
    state = get_core_flow_state(session)
    assert session[CORE_STATE_KEY] is state
    assert state.workflow is Workflow.ANONYMIZE
    assert state.presentation_mode is PresentationMode.STANDARD
    assert state.stage is Stage.ADD


def test_presentation_switch_preserves_processing_lineage_and_analysis_cache():
    session = {}
    g = generation()
    synchronize_processing_generation(session, g)
    mark_processing_complete(session, g)
    cache_analysis_results(session, g, ["result"])
    before = get_core_flow_state(session)
    after = synchronize_shell_choices(
        session,
        workflow=Workflow.ANONYMIZE,
        presentation_mode=PresentationMode.EXPERT,
    )
    assert after.source_generation == before.source_generation
    assert after.processed_generation == before.processed_generation
    assert after.stage is Stage.REVIEW
    assert get_cached_analysis_results(session, g) == ["result"]


def test_workflow_switch_fails_closed_clears_cache_and_keeps_presentation_choice():
    session = {}
    g = generation()
    synchronize_processing_generation(session, g)
    mark_processing_complete(session, g)
    cache_analysis_results(session, g, ["result"])
    set_stage_summary(session, Stage.ADD, "contract.docx")
    state = synchronize_shell_choices(
        session,
        workflow=Workflow.REINSERT,
        presentation_mode=PresentationMode.EXPERT,
    )
    assert state.workflow is Workflow.REINSERT
    assert state.presentation_mode is PresentationMode.EXPERT
    assert state.stage is Stage.ADD
    assert state.source_generation is None
    assert state.processed_generation is None
    assert ANALYSIS_GENERATION_KEY not in session
    assert ANALYSIS_RESULTS_KEY not in session
    assert STAGE_SUMMARIES_KEY not in session


def test_processing_generation_is_deterministic_and_changes_with_inputs():
    assert generation() == generation()
    assert generation(text="Contract B") != generation(text="Contract A")
    assert generation(profile="Dutch Care Strict") != generation(profile="Dutch Legal Strict")


def test_changed_processing_generation_invalidates_downstream_summaries_and_analysis():
    session = {}
    first = generation()
    synchronize_processing_generation(session, first)
    mark_processing_complete(session, first)
    mark_review_complete(session)
    cache_analysis_results(session, first, ["result"])
    set_stage_summary(session, Stage.ADD, "contract.docx · Juridisch")
    set_stage_summary(session, Stage.REVIEW, "14 gecontroleerd")

    changed_state, changed = synchronize_processing_generation(
        session, generation(text="Gewijzigd contract")
    )
    assert changed is True
    assert changed_state.stage is Stage.ADD
    assert changed_state.processed_generation is None
    assert changed_state.reviewed_generation is None
    assert changed_state.export_generation is None
    assert STAGE_SUMMARIES_KEY not in session
    assert ANALYSIS_GENERATION_KEY not in session
    assert ANALYSIS_RESULTS_KEY not in session


def test_current_generation_analysis_cache_distinguishes_empty_results_from_missing_cache():
    session = {}
    g = generation()
    assert get_cached_analysis_results(session, g) is None
    cache_analysis_results(session, g, [])
    assert get_cached_analysis_results(session, g) == []
    assert get_cached_analysis_results(session, generation(text="Other")) is None


def test_analysis_cache_returns_copy_not_mutable_internal_list():
    session = {}
    g = generation()
    cache_analysis_results(session, g, ["a"])
    first = get_cached_analysis_results(session, g)
    assert first == ["a"]
    first.append("b")
    assert get_cached_analysis_results(session, g) == ["a"]


def test_same_generation_is_noop():
    session = {}
    g = generation()
    first, changed = synchronize_processing_generation(session, g)
    assert changed is True
    second, changed = synchronize_processing_generation(session, g)
    assert changed is False
    assert second == first


def test_processing_and_review_completion_auto_advance_state():
    session = {}
    g = generation()
    synchronize_processing_generation(session, g)
    assert mark_processing_complete(session, g).stage is Stage.REVIEW
    completed = mark_review_complete(session)
    assert completed.stage is Stage.DOWNLOAD
    assert completed.export_is_current is True


def test_explicit_return_to_add_preserves_current_lineage():
    session = {}
    g = generation()
    synchronize_processing_generation(session, g)
    mark_processing_complete(session, g)
    mark_review_complete(session)
    before = get_core_flow_state(session)
    after = select_stage(session, Stage.ADD)
    assert after.stage is Stage.ADD
    assert after.source_generation == before.source_generation
    assert after.processed_generation == before.processed_generation
    assert after.reviewed_generation == before.reviewed_generation
    assert after.export_generation == before.export_generation


def test_explicit_return_to_review_fails_closed_for_export():
    session = {}
    g = generation()
    synchronize_processing_generation(session, g)
    mark_processing_complete(session, g)
    mark_review_complete(session)
    after = select_stage(session, Stage.REVIEW)
    assert after.stage is Stage.REVIEW
    assert after.processed_generation == g
    assert after.reviewed_generation is None
    assert after.export_generation is None


def test_stage_summaries_are_compact_session_metadata_only():
    session = {}
    set_stage_summary(session, Stage.ADD, "contract.docx · Juridisch")
    set_stage_summary(session, Stage.REVIEW, "14 gecontroleerd · 1 handmatig toegevoegd")
    assert get_stage_summaries(session) == {
        Stage.ADD: "contract.docx · Juridisch",
        Stage.REVIEW: "14 gecontroleerd · 1 handmatig toegevoegd",
    }


def test_processing_setting_helpers_preserve_valid_values_and_defensive_copies():
    session = {}
    persist_processing_settings(
        session,
        profile_label="Zorgcontrole — streng",
        operator="replace",
        threshold=0.31,
        entities=["PERSON", "NL_PATIENT_NUMBER"],
        allow_list=["voorbeeld"],
        deny_list=["extra"],
        analyzer_params=("flair", "flair/ner-english-large", "", ""),
    )
    assert session[PROFILE_LABEL_KEY] == "Zorgcontrole — streng"
    assert session[OPERATOR_VALUE_KEY] == "replace"
    assert session[THRESHOLD_KEY] == 0.31
    assert session[ENTITIES_KEY] == ["PERSON", "NL_PATIENT_NUMBER"]
    assert session[ALLOW_LIST_KEY] == ["voorbeeld"]
    assert session[DENY_LIST_KEY] == ["extra"]
    assert session[ANALYZER_PARAMS_KEY] == ("flair", "flair/ner-english-large", "", "")

    assert stored_profile_label(session, ["Zorgcontrole — streng", "Juridische controle — streng"]) == "Zorgcontrole — streng"
    assert stored_operator_value(session, ["replace", "highlight", "synthesize"]) == "replace"
    assert stored_threshold(session, 0.30) == 0.31
    assert stored_entities(session, ["PERSON", "NL_PATIENT_NUMBER"], ["PERSON"]) == ["PERSON", "NL_PATIENT_NUMBER"]
    allow_copy = stored_string_list(session, ALLOW_LIST_KEY)
    allow_copy.append("mutatie")
    assert session[ALLOW_LIST_KEY] == ["voorbeeld"]
    assert stored_analyzer_params(session, ("flair", "flair/ner-english-large", "", "")) == (
        "flair",
        "flair/ner-english-large",
        "",
        "",
    )


def test_model_label_roundtrips_known_and_custom_analyzer_configuration():
    options = ["spaCy/en_core_web_lg", "flair/ner-english-large", "Azure AI Language", "Other"]
    assert analyzer_model_label(("flair", "flair/ner-english-large", "", ""), options) == "flair/ner-english-large"
    assert analyzer_model_label(("spaCy", "en_core_web_lg", "", ""), options) == "spaCy/en_core_web_lg"
    assert analyzer_model_label(("custom", "my-model", "", ""), options) == "Other"


def test_standard_care_to_expert_to_standard_is_presentation_only_when_settings_do_not_change():
    session = {}
    persist_processing_settings(
        session,
        profile_label="Zorgcontrole — streng",
        operator="replace",
        threshold=0.30,
        entities=["PERSON", "NL_PATIENT_NUMBER"],
        allow_list=[],
        deny_list=[],
        analyzer_params=("flair", "flair/ner-english-large", "", ""),
    )
    original_generation = generation(
        profile="Dutch Care Strict",
        threshold=stored_threshold(session, 0.30),
        entities=stored_entities(session, ["PERSON", "NL_PATIENT_NUMBER"], ["PERSON"]),
        analyzer_params=stored_analyzer_params(session, ("flair", "flair/ner-english-large", "", "")),
    )
    synchronize_processing_generation(session, original_generation)
    mark_processing_complete(session, original_generation)
    mark_review_complete(session)

    synchronize_shell_choices(
        session,
        workflow=Workflow.ANONYMIZE,
        presentation_mode=PresentationMode.EXPERT,
    )
    expert_generation = generation(
        profile="Dutch Care Strict",
        operator=stored_operator_value(session, ["replace", "highlight", "synthesize"]),
        threshold=stored_threshold(session, 0.30),
        entities=stored_entities(session, ["PERSON", "NL_PATIENT_NUMBER"], ["PERSON"]),
        allow_list=stored_string_list(session, ALLOW_LIST_KEY),
        deny_list=stored_string_list(session, DENY_LIST_KEY),
        analyzer_params=stored_analyzer_params(session, ("flair", "flair/ner-english-large", "", "")),
    )
    state, changed = synchronize_processing_generation(session, expert_generation)
    assert changed is False
    assert state.stage is Stage.DOWNLOAD
    assert state.reviewed_generation == original_generation

    synchronize_shell_choices(
        session,
        workflow=Workflow.ANONYMIZE,
        presentation_mode=PresentationMode.STANDARD,
    )
    standard_generation = generation(
        profile="Dutch Care Strict",
        operator=stored_operator_value(session, ["replace", "highlight", "synthesize"]),
        threshold=stored_threshold(session, 0.30),
        entities=stored_entities(session, ["PERSON", "NL_PATIENT_NUMBER"], ["PERSON"]),
        allow_list=stored_string_list(session, ALLOW_LIST_KEY),
        deny_list=stored_string_list(session, DENY_LIST_KEY),
        analyzer_params=stored_analyzer_params(session, ("flair", "flair/ner-english-large", "", "")),
    )
    state, changed = synchronize_processing_generation(session, standard_generation)
    assert changed is False
    assert state.stage is Stage.DOWNLOAD
    assert stored_profile_label(session, ["Zorgcontrole — streng", "Juridische controle — streng"]) == "Zorgcontrole — streng"


def test_real_expert_processing_change_invalidates_downstream_once_and_then_stabilizes():
    session = {}
    original = generation(profile="Dutch Care Strict", threshold=0.30)
    synchronize_processing_generation(session, original)
    mark_processing_complete(session, original)
    mark_review_complete(session)

    changed_generation = generation(profile="Dutch Care Strict", threshold=0.45)
    state, changed = synchronize_processing_generation(session, changed_generation)
    assert changed is True
    assert state.stage is Stage.ADD
    assert state.processed_generation is None
    assert state.reviewed_generation is None
    assert state.export_generation is None

    stable_state, changed_again = synchronize_processing_generation(session, changed_generation)
    assert changed_again is False
    assert stable_state == state


def test_operator_and_entity_changes_are_processing_affecting():
    base = generation(operator="replace", entities=["PERSON", "EMAIL_ADDRESS"])
    assert generation(operator="highlight", entities=["PERSON", "EMAIL_ADDRESS"]) != base
    assert generation(operator="replace", entities=["PERSON"]) != base
