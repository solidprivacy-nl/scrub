"""Small session-state adapter for the Premium staged workspace.

The adapter stores only the pure ``CoreFlowState``, compact presentation
summaries and current-generation analysis output. It never invokes recognition,
replacement, export, Scrub Key, reinsert or audit behavior itself.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping, MutableMapping, Optional, Sequence

from premium_app_shell import open_stage
from premium_core_flow_state import CoreFlowState, PresentationMode, Stage, Workflow


CORE_STATE_KEY = "_premium_core_flow_state"
STAGE_SUMMARIES_KEY = "_premium_stage_summaries"
ANALYSIS_GENERATION_KEY = "_premium_analysis_generation"
ANALYSIS_RESULTS_KEY = "_premium_analysis_results"


def get_core_flow_state(session_state: MutableMapping[str, Any]) -> CoreFlowState:
    state = session_state.get(CORE_STATE_KEY)
    if isinstance(state, CoreFlowState):
        return state
    state = CoreFlowState()
    session_state[CORE_STATE_KEY] = state
    return state


def set_core_flow_state(
    session_state: MutableMapping[str, Any], state: CoreFlowState
) -> CoreFlowState:
    session_state[CORE_STATE_KEY] = state
    return state


def synchronize_shell_choices(
    session_state: MutableMapping[str, Any],
    *,
    workflow: Workflow,
    presentation_mode: PresentationMode,
) -> CoreFlowState:
    """Apply top-level presentation/navigation choices without hidden reprocessing."""
    state = get_core_flow_state(session_state)
    previous_workflow = state.workflow
    state = state.with_workflow(workflow)
    state = state.with_presentation_mode(presentation_mode)
    if workflow is not previous_workflow:
        session_state.pop(ANALYSIS_GENERATION_KEY, None)
        session_state.pop(ANALYSIS_RESULTS_KEY, None)
        session_state.pop(STAGE_SUMMARIES_KEY, None)
    return set_core_flow_state(session_state, state)


def processing_generation(
    *,
    text: str,
    profile: str,
    operator: str,
    threshold: float,
    entities: Sequence[str],
    allow_list: Sequence[str],
    deny_list: Sequence[str],
    analyzer_params: Sequence[Any],
) -> str:
    """Return a deterministic privacy-safe lineage identifier for processing inputs."""
    payload = {
        "text": text,
        "profile": profile,
        "operator": operator,
        "threshold": float(threshold),
        "entities": list(entities),
        "allow_list": list(allow_list),
        "deny_list": list(deny_list),
        "analyzer_params": [str(value) for value in analyzer_params],
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def synchronize_processing_generation(
    session_state: MutableMapping[str, Any], generation: str
) -> tuple[CoreFlowState, bool]:
    """Fail closed when source or processing-affecting inputs changed.

    Returns ``(state, changed)`` so the UI can rerun immediately before showing
    stale downstream review/export state.
    """
    state = get_core_flow_state(session_state)
    if state.source_generation == generation:
        return state, False
    state = state.with_source(generation)
    set_core_flow_state(session_state, state)
    session_state.pop(STAGE_SUMMARIES_KEY, None)
    session_state.pop(ANALYSIS_GENERATION_KEY, None)
    session_state.pop(ANALYSIS_RESULTS_KEY, None)
    return state, True


def cache_analysis_results(
    session_state: MutableMapping[str, Any], generation: str, results: Sequence[Any]
) -> None:
    """Cache only analysis belonging to the current deterministic generation."""
    session_state[ANALYSIS_GENERATION_KEY] = generation
    session_state[ANALYSIS_RESULTS_KEY] = list(results)


def get_cached_analysis_results(
    session_state: Mapping[str, Any], generation: str
) -> Optional[list[Any]]:
    """Return current-generation analysis, including an intentionally empty result list."""
    if session_state.get(ANALYSIS_GENERATION_KEY) != generation:
        return None
    results = session_state.get(ANALYSIS_RESULTS_KEY)
    if not isinstance(results, list):
        return None
    return list(results)


def mark_processing_complete(
    session_state: MutableMapping[str, Any], generation: str
) -> CoreFlowState:
    state = get_core_flow_state(session_state).with_processed_result(generation)
    return set_core_flow_state(session_state, state)


def mark_review_complete(session_state: MutableMapping[str, Any]) -> CoreFlowState:
    state = get_core_flow_state(session_state).complete_review()
    return set_core_flow_state(session_state, state)


def select_stage(
    session_state: MutableMapping[str, Any], stage: Stage
) -> CoreFlowState:
    state = open_stage(get_core_flow_state(session_state), stage)
    return set_core_flow_state(session_state, state)


def get_stage_summaries(session_state: Mapping[str, Any]) -> dict[Stage, str]:
    raw = session_state.get(STAGE_SUMMARIES_KEY, {})
    if not isinstance(raw, Mapping):
        return {}
    summaries: dict[Stage, str] = {}
    for key, value in raw.items():
        try:
            stage = key if isinstance(key, Stage) else Stage(str(key))
        except ValueError:
            continue
        text = str(value).strip()
        if text:
            summaries[stage] = text
    return summaries


def set_stage_summary(
    session_state: MutableMapping[str, Any], stage: Stage, summary: str
) -> None:
    summaries = get_stage_summaries(session_state)
    text = str(summary).strip()
    if text:
        summaries[stage] = text
    else:
        summaries.pop(stage, None)
    session_state[STAGE_SUMMARIES_KEY] = summaries
