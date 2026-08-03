"""Pure gap-triage model for Zorgfilter v1.

The module classifies every synthetic care-corpus expectation using the frozen
current-engine baseline. It does not implement, register or tune recognizers.
"""

from __future__ import annotations

from collections import Counter
from typing import Any, Dict, Mapping, Sequence

from care_profile_baseline import build_current_care_baseline


STATUS_CORRECT = "correct_entity"
STATUS_MISCLASSIFIED = "misclassified"
STATUS_MISSED = "missed"

ROUTE_REUSE_CURRENT = "reuse_current_recognizer"
ROUTE_GENERIC_PROFILE = "generic_profile_dependency"
ROUTE_CARE_REFERENCE = "dedicated_care_reference_recognizer"
ROUTE_CARE_RECLASSIFICATION = "care_specific_reclassification"
ROUTE_CONTEXTUAL_REVIEW = "contextual_care_review_recognizer"
ROUTE_COLLISION_GUARD = "care_collision_guard"

VALID_ROUTES = {
    ROUTE_REUSE_CURRENT,
    ROUTE_GENERIC_PROFILE,
    ROUTE_CARE_REFERENCE,
    ROUTE_CARE_RECLASSIFICATION,
    ROUTE_CONTEXTUAL_REVIEW,
    ROUTE_COLLISION_GUARD,
}

GENERIC_PROFILE_ENTITIES = {"PERSON", "EMAIL_ADDRESS"}

CONTEXTUAL_REVIEW_ENTITIES = {
    "NL_CARE_PROVIDER_NAME",
    "NL_CARE_ORGANIZATION",
    "NL_CARE_LOCATION_REFERENCE",
    "NL_ROOM_OR_BED_REFERENCE",
    "NL_CARE_EVENT_DATE",
}

CARE_REFERENCE_ENTITIES = {
    "NL_PATIENT_NUMBER",
    "NL_CARE_CLIENT_NUMBER",
    "NL_MEDICAL_RECORD_NUMBER",
    "NL_EPD_ECD_NUMBER",
    "NL_HEALTH_INSURANCE_NUMBER",
    "NL_REFERRAL_NUMBER",
    "NL_TREATMENT_REFERENCE",
    "NL_LAB_SAMPLE_NUMBER",
    "NL_CARE_INCIDENT_NUMBER",
    "NL_CARE_INDICATION_REFERENCE",
}

COLLISION_GUARD_ENTITIES = {"NL_AGB_CODE"}

CURRENT_REUSE_ENTITIES = {
    "NL_ADDRESS",
    "NL_BIG_NUMBER",
    "NL_BSN",
    "NL_DATE_OF_BIRTH",
    "NL_PHONE_NUMBER",
}


CONTRACT_FAMILIES: tuple[dict[str, Any], ...] = (
    {
        "id": "generic_profile_dependencies",
        "route": ROUTE_GENERIC_PROFILE,
        "entities": sorted(GENERIC_PROFILE_ENTITIES),
        "requirements": [
            "Use the approved local generic NER/profile layer for unlabeled patient and relative names.",
            "Keep exact generic e-mail recognition enabled in the Zorg profile.",
            "Do not treat the custom-rule-only baseline as a full-app PERSON or e-mail result.",
            "Require cross-profile regression before promotion.",
        ],
    },
    {
        "id": "care_reference_identifiers",
        "route": ROUTE_CARE_REFERENCE,
        "entities": sorted(CARE_REFERENCE_ENTITIES),
        "requirements": [
            "Use strong care context and return only the sensitive value span.",
            "Split the current broad NL_HEALTHCARE_REFERENCE behavior into policy-specific entities.",
            "Preserve labels such as patientnummer, EPD-nummer, verwijsnummer and incidentnummer.",
            "Reject dates, vital signs, dosages, laboratory values and clinical codes as reference values.",
        ],
    },
    {
        "id": "care_contextual_review",
        "route": ROUTE_CONTEXTUAL_REVIEW,
        "entities": sorted(CONTEXTUAL_REVIEW_ENTITIES),
        "requirements": [
            "Detect care-provider names after professional role context while preserving the role word.",
            "Detect organizations, departments, teams, locations and room/bed references only with bounded care context.",
            "Distinguish date of birth from admission, discharge, appointment, treatment and report dates.",
            "Route these values to review-selected policy rather than irreversible blind replacement.",
        ],
    },
    {
        "id": "care_collision_prevention",
        "route": ROUTE_COLLISION_GUARD,
        "entities": sorted(COLLISION_GUARD_ENTITIES),
        "requirements": [
            "Recognize AGB only with strong AGB/provider/practice context.",
            "Prevent an eight-digit AGB value from being accepted as BSN in the same labeled span.",
            "Prevent room numbers, dosages, times, vital signs and lab values from becoming care identifiers.",
            "Make overlapping recognizer precedence deterministic and testable.",
        ],
    },
    {
        "id": "clinical_preservation_guards",
        "route": ROUTE_COLLISION_GUARD,
        "entities": [],
        "requirements": [
            "Preserve diagnosis, symptoms, medication, dosage, administration schedules, lab values and units.",
            "Preserve observations, vital signs, allergies, treatment, care goals and professional role words.",
            "Keep rare-case indirect identifiability in audit evidence rather than blind pattern masking.",
            "Run negative contracts across all eight synthetic document families.",
        ],
    },
)


def _status(expectation: Mapping[str, Any]) -> str:
    if not expectation.get("found"):
        return STATUS_MISSED
    if expectation.get("expected_entity_type") in set(
        expectation.get("detected_entity_types", [])
    ):
        return STATUS_CORRECT
    return STATUS_MISCLASSIFIED


def _route_for(expectation: Mapping[str, Any]) -> tuple[str, tuple[str, ...], str]:
    entity_type = str(expectation["expected_entity_type"])
    status = _status(expectation)

    if status == STATUS_CORRECT and entity_type in CURRENT_REUSE_ENTITIES:
        return (
            ROUTE_REUSE_CURRENT,
            ("profile_composition", "cross_profile_regression"),
            "The current Dutch custom recognizer already returns the intended exact entity span.",
        )

    if entity_type in GENERIC_PROFILE_ENTITIES:
        return (
            ROUTE_GENERIC_PROFILE,
            ("generic_ner_profile_contract", "cross_profile_regression"),
            "The bounded baseline excludes generic NER; this expectation belongs to the generic profile layer rather than a new numeric care regex.",
        )

    if entity_type in COLLISION_GUARD_ENTITIES:
        return (
            ROUTE_COLLISION_GUARD,
            ("agb_context_contract", "bsn_agb_collision_guard", "negative_numeric_contracts"),
            "AGB requires strong care-provider context and explicit precedence over BSN-shaped numeric recognition.",
        )

    if entity_type in CONTEXTUAL_REVIEW_ENTITIES:
        return (
            ROUTE_CONTEXTUAL_REVIEW,
            (
                "context_bounded_span_contract",
                "review_selected_policy_contract",
                "clinical_context_preservation",
            ),
            "The value is context-dependent and must be surfaced for review without removing professional or clinical context.",
        )

    if entity_type in CARE_REFERENCE_ENTITIES:
        if status == STATUS_MISCLASSIFIED:
            return (
                ROUTE_CARE_RECLASSIFICATION,
                (
                    "care_entity_split_contract",
                    "value_only_span_contract",
                    "legacy_broad_entity_regression",
                ),
                "The exact span is already found under a broad legal/healthcare entity and needs a care-specific entity and policy.",
            )
        return (
            ROUTE_CARE_REFERENCE,
            (
                "care_reference_pattern_contract",
                "value_only_span_contract",
                "negative_numeric_contracts",
            ),
            "The patient-specific administrative reference is absent and needs a dedicated care-context recognizer.",
        )

    if status == STATUS_CORRECT:
        return (
            ROUTE_REUSE_CURRENT,
            ("profile_composition", "cross_profile_regression"),
            "The current recognizer already returns the expected entity.",
        )

    raise ValueError(
        f"No care gap route for entity={entity_type!r}, status={status!r}"
    )


def build_care_profile_gap_triage(
    baseline: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Classify all current care-corpus expectations and freeze next contracts."""

    source = dict(baseline or build_current_care_baseline())
    items: list[dict[str, Any]] = []
    route_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()
    entity_counts: Counter[str] = Counter()

    for case in source["cases"]:
        for expectation in case["expectations"]:
            status = _status(expectation)
            route, required_contracts, rationale = _route_for(expectation)
            route_counts[route] += 1
            status_counts[status] += 1
            entity_counts[str(expectation["expected_entity_type"])] += 1
            items.append(
                {
                    "case_id": case["id"],
                    "document_type": case["document_type"],
                    "value": expectation["value"],
                    "expected_entity_type": expectation["expected_entity_type"],
                    "policy_bucket": expectation["policy_bucket"],
                    "baseline_status": status,
                    "detected_entity_types": list(
                        expectation.get("detected_entity_types", [])
                    ),
                    "primary_route": route,
                    "required_contracts": list(required_contracts),
                    "rationale": rationale,
                }
            )

    unclassified = [item for item in items if item["primary_route"] not in VALID_ROUTES]
    return {
        "schema_version": "1.0",
        "source_profile": source["profile"],
        "synthetic_data_only": True,
        "production_ready": False,
        "human_review_required": True,
        "expectation_count": len(items),
        "classified_count": len(items) - len(unclassified),
        "unclassified_count": len(unclassified),
        "status_counts": dict(sorted(status_counts.items())),
        "route_counts": dict(sorted(route_counts.items())),
        "entity_counts": dict(sorted(entity_counts.items())),
        "contract_families": [dict(family) for family in CONTRACT_FAMILIES],
        "items": items,
        "next_workpackage": "SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS",
    }
