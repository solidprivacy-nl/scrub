"""Pure adapters between recognition-profile configuration and the current UI."""

from __future__ import annotations

from typing import Any, Iterable, Sequence

from candidate_scanner import scan_unmasked_candidates
from care_candidate_scanner import scan_unmasked_care_candidates
from care_profile_policy import ACTION_REVIEW_SELECTED
from care_test_examples import TEST_CASES as CARE_TEST_CASES
from recognition_profiles import (
    PROFILE_DUTCH_CARE_STRICT,
    PROFILE_DUTCH_LEGAL_STRICT,
    entity_names_for_profile,
    get_profile,
    policy_action_for_profile_entity,
    profile_id_from_internal_value,
    profile_options,
    resolve_profile_result_collisions,
)
from review_status import AUTO_DETECTED, NEEDS_REVIEW


CARE_EXAMPLE_BY_NAME = {
    str(case["name"]): str(case["text"])
    for case in CARE_TEST_CASES
}


def current_profile_options_with_care() -> dict[str, str]:
    """Return the future four-option Streamlit mapping in stable order."""

    return dict(profile_options(include_care=True))


def profile_id_for_internal_value(internal_value: str) -> str:
    return profile_id_from_internal_value(internal_value)


def configured_threshold(internal_value: str) -> float:
    return get_profile(profile_id_for_internal_value(internal_value)).threshold


def configured_description(internal_value: str) -> str:
    return get_profile(profile_id_for_internal_value(internal_value)).description_nl


def configured_entity_names(
    internal_value: str,
    available_entities: Sequence[str],
    *,
    dutch_general_entities: Iterable[str] = (),
    dutch_legal_entities: Iterable[str] = (),
    dutch_care_entities: Iterable[str] = (),
) -> list[str]:
    return entity_names_for_profile(
        profile_id_for_internal_value(internal_value),
        available_entities,
        dutch_general_entities=dutch_general_entities,
        dutch_legal_entities=dutch_legal_entities,
        dutch_care_entities=dutch_care_entities,
    )


def resolve_configured_analysis_results(internal_value: str, results: Sequence[Any]) -> list[Any]:
    return resolve_profile_result_collisions(
        results,
        profile_id_for_internal_value(internal_value),
    )


def scan_configured_candidates(
    internal_value: str,
    text: str,
    analyzer_results=None,
    max_candidates: int = 50,
) -> list[dict]:
    profile_id = profile_id_for_internal_value(internal_value)
    if profile_id == PROFILE_DUTCH_LEGAL_STRICT:
        return scan_unmasked_candidates(
            text,
            analyzer_results,
            max_candidates=max_candidates,
        )
    if profile_id == PROFILE_DUTCH_CARE_STRICT:
        return scan_unmasked_care_candidates(
            text,
            analyzer_results,
            max_candidates=min(max_candidates, 30),
        )
    return []


def detected_reason(internal_value: str, entity_type: str) -> str:
    profile_id = profile_id_for_internal_value(internal_value)
    action = policy_action_for_profile_entity(profile_id, entity_type)
    if profile_id == PROFILE_DUTCH_CARE_STRICT and action == ACTION_REVIEW_SELECTED:
        return "Automatisch herkend — controleren"
    return "Automatisch herkend"


def detected_review_status(internal_value: str, entity_type: str) -> str:
    """Return profile-aware status while leaving detected rows selected by default."""

    profile_id = profile_id_for_internal_value(internal_value)
    action = policy_action_for_profile_entity(profile_id, entity_type)
    if profile_id == PROFILE_DUTCH_CARE_STRICT and action == ACTION_REVIEW_SELECTED:
        return NEEDS_REVIEW
    return AUTO_DETECTED


def care_example_names() -> list[str]:
    return list(CARE_EXAMPLE_BY_NAME)


def care_example_text(name: str) -> str:
    return CARE_EXAMPLE_BY_NAME.get(str(name or ""), "")
