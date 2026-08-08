"""Small session-state adapter for the Premium staged workspace.

The adapter stores only the pure ``CoreFlowState``, compact presentation
summaries, current-generation analysis output and processing-setting values
needed to keep Standard/Expert a presentation-only choice. It never invokes
recognition, replacement, export, Scrub Key, reinsert or audit behavior itself.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any, Iterable, Mapping, MutableMapping, Optional, Sequence

from premium_app_shell import open_stage
from premium_core_flow_state import CoreFlowState, PresentationMode, Stage, Workflow


CORE_STATE_KEY = "_premium_core_flow_state"
STAGE_SUMMARIES_KEY = "_premium_stage_summaries"
ANALYSIS_GENERATION_KEY = "_premium_analysis_generation"
ANALYSIS_RESULTS_KEY = "_premium_analysis_results"
PROFILE_LABEL_KEY = "_premium_profile_label"
OPERATOR_VALUE_KEY = "_premium_operator_value"
THRESHOLD_KEY = "_premium_threshold"
ENTITIES_KEY = "_premium_entities"
ALLOW_LIST_KEY = "_premium_allow_list"
DENY_LIST_KEY = "_premium_deny_list"
ANALYZER_PARAMS_KEY = "_premium_analyzer_params"


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


def stored_profile_label(
    session_state: Mapping[str, Any],
    options: Sequence[str],
    *,
    default_index: int = 1,
) -> str:
    """Return the persisted profile label or a deterministic valid default."""
    option_list = [str(option) for option in options]
    if not option_list:
        raise ValueError("profile options must not be empty")
    safe_default_index = min(max(int(default_index), 0), len(option_list) - 1)
    stored = session_state.get(PROFILE_LABEL_KEY)
    if isinstance(stored, str) and stored in option_list:
        return stored
    return option_list[safe_default_index]


def stored_operator_value(
    session_state: Mapping[str, Any],
    valid_operators: Iterable[str],
    *,
    default: str = "replace",
) -> str:
    """Return a persisted operator without silently coercing a valid Expert choice."""
    valid = tuple(str(value) for value in valid_operators)
    if not valid:
        raise ValueError("valid operators must not be empty")
    fallback = default if default in valid else valid[0]
    stored = session_state.get(OPERATOR_VALUE_KEY)
    if isinstance(stored, str) and stored in valid:
        return stored
    return fallback


def stored_threshold(session_state: Mapping[str, Any], default: float) -> float:
    """Return the persisted recognition threshold when it is a valid slider value."""
    try:
        value = float(session_state.get(THRESHOLD_KEY, default))
    except (TypeError, ValueError):
        return float(default)
    if 0.0 <= value <= 1.0:
        return value
    return float(default)


def stored_entities(
    session_state: Mapping[str, Any],
    available_entities: Sequence[str],
    default_entities: Sequence[str],
) -> list[str]:
    """Return persisted entity selection, preserving an intentional empty selection."""
    available = set(str(entity) for entity in available_entities)
    stored = session_state.get(ENTITIES_KEY)
    source = stored if isinstance(stored, list) else list(default_entities)
    return [str(entity) for entity in source if str(entity) in available]


def stored_string_list(
    session_state: Mapping[str, Any], key: str, default: Sequence[str] = ()
) -> list[str]:
    """Return a defensive copy of one persisted string-list setting."""
    stored = session_state.get(key)
    source = stored if isinstance(stored, list) else list(default)
    return [str(value) for value in source]


def stored_analyzer_params(
    session_state: Mapping[str, Any], default: Sequence[Any]
) -> tuple[Any, Any, Any, Any]:
    """Return the persisted four-part analyzer configuration or a safe default."""
    stored = session_state.get(ANALYZER_PARAMS_KEY)
    source = stored if isinstance(stored, (list, tuple)) and len(stored) == 4 else default
    values = tuple(source)
    if len(values) != 4:
        raise ValueError("analyzer params must contain exactly four values")
    return values  # type: ignore[return-value]


def analyzer_model_label(
    analyzer_params: Sequence[Any], model_options: Sequence[str]
) -> str:
    """Map persisted analyzer params back to the matching Expert model selector value."""
    if not model_options:
        raise ValueError("model options must not be empty")
    package = str(analyzer_params[0]) if len(analyzer_params) > 0 else ""
    model = str(analyzer_params[1]) if len(analyzer_params) > 1 else ""
    candidates = (model, f"{package}/{model}" if package and model else "", package)
    for candidate in candidates:
        if candidate in model_options:
            return candidate
    if "Other" in model_options:
        return "Other"
    return model_options[min(1, len(model_options) - 1)]


def persist_processing_settings(
    session_state: MutableMapping[str, Any],
    *,
    profile_label: str,
    operator: str,
    threshold: float,
    entities: Optional[Sequence[str]] = None,
    allow_list: Optional[Sequence[str]] = None,
    deny_list: Optional[Sequence[str]] = None,
    analyzer_params: Optional[Sequence[Any]] = None,
) -> None:
    """Persist processing-affecting choices independently of presentation mode."""
    session_state[PROFILE_LABEL_KEY] = str(profile_label)
    session_state[OPERATOR_VALUE_KEY] = str(operator)
    session_state[THRESHOLD_KEY] = float(threshold)
    if entities is not None:
        session_state[ENTITIES_KEY] = [str(entity) for entity in entities]
    if allow_list is not None:
        session_state[ALLOW_LIST_KEY] = [str(value) for value in allow_list]
    if deny_list is not None:
        session_state[DENY_LIST_KEY] = [str(value) for value in deny_list]
    if analyzer_params is not None:
        if len(analyzer_params) != 4:
            raise ValueError("analyzer params must contain exactly four values")
        session_state[ANALYZER_PARAMS_KEY] = tuple(analyzer_params)


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
