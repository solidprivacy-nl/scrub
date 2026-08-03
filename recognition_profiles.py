"""Pure recognition-profile configuration for SolidPrivacy Scrub.

The module centralizes the existing General Dutch, Legal and International
profile behavior and defines the future Care profile. It does not import
Streamlit, Presidio engines or the current application and changes no live UI or
analyzer behavior by itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Sequence

from care_profile_policy import (
    ACTION_REPLACE,
    ACTION_REVIEW_SELECTED,
    policy_for_entity,
)


PROFILE_DUTCH_GENERAL = "dutch_general"
PROFILE_DUTCH_CARE_STRICT = "dutch_care_strict"
PROFILE_DUTCH_LEGAL_STRICT = "dutch_legal_strict"
PROFILE_GENERAL_INTERNATIONAL = "general_international"

CURRENT_VISIBLE_PROFILE_IDS = (
    PROFILE_DUTCH_LEGAL_STRICT,
    PROFILE_DUTCH_GENERAL,
    PROFILE_GENERAL_INTERNATIONAL,
)
TARGET_STREAMLIT_PROFILE_IDS = (
    PROFILE_DUTCH_CARE_STRICT,
    PROFILE_DUTCH_LEGAL_STRICT,
    PROFILE_DUTCH_GENERAL,
    PROFILE_GENERAL_INTERNATIONAL,
)
DESKTOP_PROFILE_IDS = (
    PROFILE_DUTCH_GENERAL,
    PROFILE_DUTCH_CARE_STRICT,
    PROFILE_DUTCH_LEGAL_STRICT,
    PROFILE_GENERAL_INTERNATIONAL,
)

BASE_PROFILE_ENTITIES = (
    "PERSON",
    "LOCATION",
    "ORGANIZATION",
    "EMAIL_ADDRESS",
    "PHONE_NUMBER",
    "IBAN_CODE",
    "URL",
    "IP_ADDRESS",
    "GENERIC_PII",
    "DATE_TIME",
)


@dataclass(frozen=True)
class RecognitionProfile:
    profile_id: str
    internal_value: str
    label_nl: str
    short_label_nl: str
    description_nl: str
    threshold: float
    entity_groups: tuple[str, ...]
    candidate_scanner: str | None
    example_collection: str | None


PROFILE_DEFINITIONS: tuple[RecognitionProfile, ...] = (
    RecognitionProfile(
        profile_id=PROFILE_DUTCH_CARE_STRICT,
        internal_value="Dutch Care Strict",
        label_nl="Zorgcontrole — streng",
        short_label_nl="Zorg",
        description_nl=(
            "Extra controle op patiënt- en cliëntnummers, EPD/ECD- en dossiernummers, "
            "verwijzingen, laboratorium- en incidentreferenties, behandelaars, "
            "zorgorganisaties, locaties en exacte zorgdata. Diagnose, medicatie, "
            "dosering, laboratoriumwaarden en observaties blijven zo veel mogelijk leesbaar."
        ),
        threshold=0.30,
        entity_groups=("base", "dutch_general", "dutch_care"),
        candidate_scanner="care",
        example_collection="care",
    ),
    RecognitionProfile(
        profile_id=PROFILE_DUTCH_LEGAL_STRICT,
        internal_value="Dutch Legal Strict",
        label_nl="Juridische controle — streng",
        short_label_nl="Juridisch",
        description_nl=(
            "Extra herkenning voor zaaknummers, rolnummers, parketnummers, "
            "dossiernummers, cliëntreferenties, ECLI's en andere juridische of "
            "administratieve verwijzingen."
        ),
        threshold=0.30,
        entity_groups=("base", "dutch_general", "dutch_legal"),
        candidate_scanner="legal",
        example_collection="legal",
    ),
    RecognitionProfile(
        profile_id=PROFILE_DUTCH_GENERAL,
        internal_value="Dutch / EU",
        label_nl="Algemene Nederlandse controle",
        short_label_nl="Algemeen NL",
        description_nl=(
            "Herkenning voor algemene Nederlandse gegevens zoals BSN, postcode, KvK, "
            "btw-nummer, IBAN, telefoonnummers, adressen, kentekens, "
            "rijbewijsachtige nummers en BIG-nummers."
        ),
        threshold=0.35,
        entity_groups=("base", "dutch_general"),
        candidate_scanner=None,
        example_collection=None,
    ),
    RecognitionProfile(
        profile_id=PROFILE_GENERAL_INTERNATIONAL,
        internal_value="General / International",
        label_nl="Algemene internationale controle",
        short_label_nl="Internationaal",
        description_nl=(
            "Algemene herkenning op basis van de standaard herkenningsengine en het "
            "gekozen lokale NER-model."
        ),
        threshold=0.35,
        entity_groups=("all_supported",),
        candidate_scanner=None,
        example_collection=None,
    ),
)

PROFILE_BY_ID = {profile.profile_id: profile for profile in PROFILE_DEFINITIONS}
PROFILE_ID_BY_INTERNAL_VALUE = {
    profile.internal_value: profile.profile_id for profile in PROFILE_DEFINITIONS
}
PROFILE_ID_BY_LABEL = {
    profile.label_nl: profile.profile_id for profile in PROFILE_DEFINITIONS
}

# Exact-span precedence is intentionally narrow. Partial overlaps remain visible
# for later review and regression evidence.
CARE_EXACT_SPAN_SUPERSEDES: Mapping[str, frozenset[str]] = {
    "NL_PATIENT_NUMBER": frozenset(
        {"NL_HEALTHCARE_REFERENCE", "NL_CONTEXTUAL_REFERENCE", "NL_DOSSIER_NUMBER"}
    ),
    "NL_CARE_CLIENT_NUMBER": frozenset(
        {"NL_CLIENT_REFERENCE", "NL_CLIENT_NUMBER", "NL_HEALTHCARE_REFERENCE"}
    ),
    "NL_MEDICAL_RECORD_NUMBER": frozenset(
        {"NL_DOSSIER_NUMBER", "NL_HEALTHCARE_REFERENCE"}
    ),
    "NL_EPD_ECD_NUMBER": frozenset(
        {"NL_HEALTHCARE_REFERENCE", "NL_CONTEXTUAL_REFERENCE"}
    ),
    "NL_HEALTH_INSURANCE_NUMBER": frozenset(
        {"NL_HEALTHCARE_REFERENCE", "NL_INSURANCE_REFERENCE"}
    ),
    "NL_REFERRAL_NUMBER": frozenset(
        {"NL_HEALTHCARE_REFERENCE", "NL_CONTEXTUAL_REFERENCE"}
    ),
    "NL_TREATMENT_REFERENCE": frozenset(
        {"NL_HEALTHCARE_REFERENCE", "NL_CONTEXTUAL_REFERENCE"}
    ),
    "NL_LAB_SAMPLE_NUMBER": frozenset(
        {"NL_HEALTHCARE_REFERENCE", "NL_CONTEXTUAL_REFERENCE"}
    ),
    "NL_CARE_INCIDENT_NUMBER": frozenset(
        {"NL_INCIDENT_NUMBER", "NL_OTHER_REFERENCE", "NL_HEALTHCARE_REFERENCE"}
    ),
    "NL_CARE_INDICATION_REFERENCE": frozenset(
        {
            "NL_HEALTHCARE_REFERENCE",
            "NL_CONTEXTUAL_REFERENCE",
            "NL_CHILD_PROTECTION_REFERENCE",
        }
    ),
    "NL_AGB_CODE": frozenset({"NL_BSN"}),
    "NL_CARE_PROVIDER_NAME": frozenset({"PERSON"}),
    "NL_CARE_ORGANIZATION": frozenset({"ORGANIZATION"}),
    "NL_CARE_LOCATION_REFERENCE": frozenset({"LOCATION"}),
    "NL_CARE_EVENT_DATE": frozenset({"DATE_TIME"}),
}

CARE_GENERIC_REVIEW_SELECTED_ENTITIES = frozenset(
    {"ORGANIZATION", "LOCATION", "DATE_TIME"}
)


def get_profile(profile_id: str) -> RecognitionProfile:
    """Return one profile or raise a clear error for an unknown ID."""

    try:
        return PROFILE_BY_ID[profile_id]
    except KeyError as exc:
        raise ValueError(f"Unknown recognition profile: {profile_id}") from exc


def profile_id_from_internal_value(internal_value: str) -> str:
    try:
        return PROFILE_ID_BY_INTERNAL_VALUE[internal_value]
    except KeyError as exc:
        raise ValueError(f"Unknown profile internal value: {internal_value}") from exc


def profile_id_from_label(label_nl: str) -> str:
    try:
        return PROFILE_ID_BY_LABEL[label_nl]
    except KeyError as exc:
        raise ValueError(f"Unknown profile label: {label_nl}") from exc


def profile_options(
    *,
    include_care: bool = False,
    desktop_order: bool = False,
) -> tuple[tuple[str, str], ...]:
    """Return ``(label, internal_value)`` options in an explicit UI order.

    The default reproduces the currently visible three-profile Streamlit order.
    The later UI integration opts into Care. Desktop UI may request the compact
    desktop order separately.
    """

    if desktop_order:
        profile_ids = DESKTOP_PROFILE_IDS
    elif include_care:
        profile_ids = TARGET_STREAMLIT_PROFILE_IDS
    else:
        profile_ids = CURRENT_VISIBLE_PROFILE_IDS
    return tuple(
        (get_profile(profile_id).label_nl, get_profile(profile_id).internal_value)
        for profile_id in profile_ids
    )


def short_profile_options(*, desktop_order: bool = True) -> tuple[tuple[str, str], ...]:
    profile_ids = DESKTOP_PROFILE_IDS if desktop_order else TARGET_STREAMLIT_PROFILE_IDS
    return tuple(
        (get_profile(profile_id).short_label_nl, profile_id)
        for profile_id in profile_ids
    )


def entity_names_for_profile(
    profile_id: str,
    available_entities: Sequence[str],
    *,
    dutch_general_entities: Iterable[str] = (),
    dutch_legal_entities: Iterable[str] = (),
    dutch_care_entities: Iterable[str] = (),
) -> list[str]:
    """Resolve profile entities while preserving available-engine order."""

    profile = get_profile(profile_id)
    if "all_supported" in profile.entity_groups:
        return list(dict.fromkeys(available_entities))

    wanted = set(BASE_PROFILE_ENTITIES)
    if "dutch_general" in profile.entity_groups:
        wanted.update(dutch_general_entities)
    if "dutch_legal" in profile.entity_groups:
        wanted.update(dutch_legal_entities)
    if "dutch_care" in profile.entity_groups:
        wanted.update(dutch_care_entities)

    return [
        entity
        for entity in dict.fromkeys(available_entities)
        if entity in wanted
    ]


def policy_action_for_profile_entity(profile_id: str, entity_type: str) -> str:
    """Return the default review action for a detected entity in a profile."""

    get_profile(profile_id)
    if profile_id != PROFILE_DUTCH_CARE_STRICT:
        return ACTION_REPLACE

    rule = policy_for_entity(entity_type)
    if rule is not None:
        return rule.action
    if entity_type in CARE_GENERIC_REVIEW_SELECTED_ENTITIES:
        return ACTION_REVIEW_SELECTED
    return ACTION_REPLACE


def _field(result: Any, name: str) -> Any:
    if isinstance(result, Mapping):
        return result[name]
    return getattr(result, name)


def resolve_profile_result_collisions(
    results: Sequence[Any],
    profile_id: str,
) -> list[Any]:
    """Apply deterministic exact-span precedence for the Care profile.

    Input objects are returned unchanged and in their original order except for
    known exact-span loser entities. Non-Care profiles and partial overlaps are
    untouched.
    """

    get_profile(profile_id)
    if profile_id != PROFILE_DUTCH_CARE_STRICT:
        return list(results)

    entities_by_span: dict[tuple[int, int], set[str]] = {}
    for result in results:
        span = (int(_field(result, "start")), int(_field(result, "end")))
        entities_by_span.setdefault(span, set()).add(str(_field(result, "entity_type")))

    drop_keys: set[tuple[int, int, str]] = set()
    for span, entity_types in entities_by_span.items():
        for winner, losers in CARE_EXACT_SPAN_SUPERSEDES.items():
            if winner not in entity_types:
                continue
            for loser in losers & entity_types:
                drop_keys.add((span[0], span[1], loser))

    return [
        result
        for result in results
        if (
            int(_field(result, "start")),
            int(_field(result, "end")),
            str(_field(result, "entity_type")),
        )
        not in drop_keys
    ]


def profile_snapshot() -> dict[str, Any]:
    """Return a stable, serializable configuration snapshot."""

    return {
        "profiles": [
            {
                "profile_id": profile.profile_id,
                "internal_value": profile.internal_value,
                "label_nl": profile.label_nl,
                "short_label_nl": profile.short_label_nl,
                "threshold": profile.threshold,
                "entity_groups": list(profile.entity_groups),
                "candidate_scanner": profile.candidate_scanner,
                "example_collection": profile.example_collection,
            }
            for profile in PROFILE_DEFINITIONS
        ],
        "current_visible_profile_ids": list(CURRENT_VISIBLE_PROFILE_IDS),
        "target_streamlit_profile_ids": list(TARGET_STREAMLIT_PROFILE_IDS),
        "desktop_profile_ids": list(DESKTOP_PROFILE_IDS),
        "care_exact_span_supersedes": {
            winner: sorted(losers)
            for winner, losers in sorted(CARE_EXACT_SPAN_SUPERSEDES.items())
        },
        "live_ui_changed": False,
        "care_recognizers_registered": False,
        "production_ready": False,
        "human_review_required": True,
    }
