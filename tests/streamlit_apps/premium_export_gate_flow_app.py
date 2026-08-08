from __future__ import annotations

import streamlit as st

from premium_app_shell import standard_operator_is_supported
from premium_core_flow_state import PresentationMode, Stage, Workflow
from premium_streamlit_export_gate import render_export_readiness_gate
from premium_streamlit_state import (
    ANALYSIS_RESULTS_KEY,
    ALLOW_LIST_KEY,
    ANALYZER_PARAMS_KEY,
    DENY_LIST_KEY,
    ENTITIES_KEY,
    OPERATOR_VALUE_KEY,
    PROFILE_LABEL_KEY,
    REVIEW_ROWS_KEY,
    SOURCE_TEXT_KEY,
    THRESHOLD_KEY,
    cache_analysis_results,
    cache_review_rows,
    get_cached_analysis_results,
    get_cached_review_rows,
    get_core_flow_state,
    mark_processing_complete,
    mark_review_complete,
    persist_processing_settings,
    processing_generation,
    select_stage,
    stored_source_text,
    synchronize_processing_generation,
    synchronize_shell_choices,
)


SOURCE = "Cliënt Noor de Vries woont aan Voorbeeldstraat 10."
PROFILE = "Dutch Legal Strict"
ENTITIES = ["PERSON"]
ALLOW_LIST: list[str] = []
DENY_LIST: list[str] = []
ANALYZER_PARAMS = ("flair", "flair/ner-english-large", "", "")
INITIAL_ROWS = [
    {
        "include": True,
        "remember": False,
        "find": "Noor de Vries",
        "replace_with": "[PERSOON_TEST_01]",
        "entity_type": "PERSON",
        "source": "auto",
    }
]


def current_operator() -> str:
    return str(st.session_state.get(OPERATOR_VALUE_KEY, "replace"))


def current_threshold() -> float:
    return float(st.session_state.get(THRESHOLD_KEY, 0.40))


def generation_for(*, text: str, operator: str, threshold: float) -> str:
    return processing_generation(
        text=text,
        profile=PROFILE,
        operator=operator,
        threshold=threshold,
        entities=ENTITIES,
        allow_list=ALLOW_LIST,
        deny_list=DENY_LIST,
        analyzer_params=ANALYZER_PARAMS,
    )


def initialize_completed_flow() -> None:
    if st.session_state.get("_premium_export_gate_fixture_initialized"):
        return
    st.session_state[SOURCE_TEXT_KEY] = SOURCE
    persist_processing_settings(
        st.session_state,
        profile_label=PROFILE,
        operator="replace",
        threshold=0.40,
        entities=ENTITIES,
        allow_list=ALLOW_LIST,
        deny_list=DENY_LIST,
        analyzer_params=ANALYZER_PARAMS,
    )
    generation = generation_for(text=SOURCE, operator="replace", threshold=0.40)
    synchronize_processing_generation(st.session_state, generation)
    cache_analysis_results(st.session_state, generation, [{"entity_type": "PERSON", "text": "Noor de Vries"}])
    cache_review_rows(st.session_state, generation, INITIAL_ROWS)
    mark_processing_complete(st.session_state, generation)
    mark_review_complete(st.session_state)
    st.session_state["_premium_export_gate_fixture_initialized"] = True


initialize_completed_flow()

presentation_choice = st.radio(
    "Weergave",
    ["Standaard", "Expert"],
    horizontal=True,
    key="fixture_presentation_mode",
)
presentation_mode = (
    PresentationMode.STANDARD if presentation_choice == "Standaard" else PresentationMode.EXPERT
)
synchronize_shell_choices(
    st.session_state,
    workflow=Workflow.ANONYMIZE,
    presentation_mode=presentation_mode,
)

source_text = stored_source_text(st.session_state)
operator = current_operator()
threshold = current_threshold()
current_generation = generation_for(text=source_text, operator=operator, threshold=threshold)

if presentation_mode is PresentationMode.EXPERT:
    selected_operator = st.selectbox(
        "Expert operator",
        ["replace", "highlight", "synthesize"],
        index=["replace", "highlight", "synthesize"].index(operator),
        key="fixture_expert_operator",
    )
    if selected_operator != operator:
        persist_processing_settings(
            st.session_state,
            profile_label=PROFILE,
            operator=selected_operator,
            threshold=threshold,
            entities=ENTITIES,
            allow_list=ALLOW_LIST,
            deny_list=DENY_LIST,
            analyzer_params=ANALYZER_PARAMS,
        )
        synchronize_processing_generation(
            st.session_state,
            generation_for(text=source_text, operator=selected_operator, threshold=threshold),
        )
        st.rerun()

    current_rows_for_edit = get_cached_review_rows(st.session_state, current_generation)
    if current_rows_for_edit is not None and st.button("Wijzig reviewbeslissing", key="fixture_edit_review"):
        edited_rows = [dict(row) for row in current_rows_for_edit]
        edited_rows[0]["replace_with"] = "[PERSOON_TEST_99]"
        cache_review_rows(st.session_state, current_generation, edited_rows)
        select_stage(st.session_state, Stage.REVIEW)
        st.rerun()

    if st.button("Wijzig verwerkingsinstelling", key="fixture_change_processing"):
        new_threshold = 0.55 if threshold != 0.55 else 0.40
        persist_processing_settings(
            st.session_state,
            profile_label=PROFILE,
            operator=operator,
            threshold=new_threshold,
            entities=ENTITIES,
            allow_list=ALLOW_LIST,
            deny_list=DENY_LIST,
            analyzer_params=ANALYZER_PARAMS,
        )
        synchronize_processing_generation(
            st.session_state,
            generation_for(text=source_text, operator=operator, threshold=new_threshold),
        )
        st.rerun()
else:
    if not standard_operator_is_supported(operator):
        st.warning("EXPERT_OPERATOR_REQUIRED")

# Recalculate after any state transition and expose deterministic executable evidence.
source_text = stored_source_text(st.session_state)
operator = current_operator()
threshold = current_threshold()
current_generation = generation_for(text=source_text, operator=operator, threshold=threshold)
state = get_core_flow_state(st.session_state)
analysis_rows = get_cached_analysis_results(st.session_state, current_generation)
review_rows = get_cached_review_rows(st.session_state, current_generation)

st.markdown(f"STATE_SOURCE: `{source_text}`")
st.markdown(f"STATE_GENERATION: `{current_generation}`")
st.markdown(f"STATE_OPERATOR: `{operator}`")
st.markdown(f"STATE_ANALYSIS_CACHE: `{'current' if analysis_rows is not None else 'missing'}`")
st.markdown(f"STATE_REVIEW_CACHE: `{'current' if review_rows is not None else 'missing'}`")
st.markdown(
    f"STATE_REVIEW_ROW: `{review_rows[0].get('replace_with') if review_rows else 'missing'}`"
)
st.markdown(
    f"STATE_LINEAGE: `processed={'current' if state.processed_generation == current_generation else 'stale'};"
    f"reviewed={'current' if state.reviewed_generation == current_generation else 'stale'};"
    f"export={'current' if state.export_generation == current_generation else 'stale'}`"
)

export_ready = render_export_readiness_gate(
    st.session_state,
    is_expert=presentation_mode is PresentationMode.EXPERT,
    generation=current_generation,
    reviewed_rows=review_rows or [],
)
if export_ready:
    st.download_button(
        "Download opgeschoonde tekst (.txt)",
        data=b"synthetic-clean-output",
        file_name="opgeschoonde_tekst.txt",
        mime="text/plain",
        key="fixture_download",
    )
    st.success("EXPORT_AVAILABLE")
else:
    st.info("EXPORT_BLOCKED")
