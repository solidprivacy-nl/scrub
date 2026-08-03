"""Compact machine-readable summary of the Zorgfilter v1 recognizer contract."""

from __future__ import annotations

from collections import Counter
from typing import Any, Dict

from care_recognizer_contracts import (
    ALL_POSITIVE_CASES,
    CARE_RECOGNIZER_CONTRACT_SCHEMA_VERSION,
    CARE_RECOGNIZER_ENTITY_NAMES,
    CARE_RECOGNIZER_MODULE,
    CARE_RECOGNIZER_PUBLIC_API,
    CARE_RECOGNIZER_SUPPORTED_LANGUAGE,
    CONTEXTUAL_REVIEW_POSITIVE_CASES,
    NEGATIVE_CASES,
    REFERENCE_POSITIVE_CASES,
)


def build_care_recognizer_contract_summary() -> Dict[str, Any]:
    """Return stable counts and API/entity scope for validation artifacts."""

    policy_counts = Counter(case["policy_action"] for case in ALL_POSITIVE_CASES)
    family_counts = Counter(case["family"] for case in ALL_POSITIVE_CASES)
    entity_case_counts = Counter(case["entity_type"] for case in ALL_POSITIVE_CASES)
    return {
        "schema_version": CARE_RECOGNIZER_CONTRACT_SCHEMA_VERSION,
        "module": CARE_RECOGNIZER_MODULE,
        "public_api": list(CARE_RECOGNIZER_PUBLIC_API),
        "supported_language": CARE_RECOGNIZER_SUPPORTED_LANGUAGE,
        "entity_names": list(CARE_RECOGNIZER_ENTITY_NAMES),
        "entity_count": len(CARE_RECOGNIZER_ENTITY_NAMES),
        "reference_positive_case_count": len(REFERENCE_POSITIVE_CASES),
        "contextual_positive_case_count": len(CONTEXTUAL_REVIEW_POSITIVE_CASES),
        "positive_case_count": len(ALL_POSITIVE_CASES),
        "negative_case_count": len(NEGATIVE_CASES),
        "policy_counts": dict(sorted(policy_counts.items())),
        "family_counts": dict(sorted(family_counts.items())),
        "entity_case_counts": dict(sorted(entity_case_counts.items())),
        "production_ready": False,
        "human_review_required": True,
        "next_workpackage": "SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION",
    }
