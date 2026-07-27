"""Synthetic adversarial Scrub Key roundtrip validation for Phase 6.

This module is deliberately pure and deterministic. It exercises the existing
Scrub Key and reinsert helpers without changing their semantics, calling AI,
using cloud processing, writing files or importing Streamlit.
"""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from scrub_key import build_scrub_key
from scrub_key_reinsert import reinsert_from_scrub_key

ROOT = Path(__file__).resolve().parent
DEFAULT_MANIFEST_PATH = ROOT / "test_cases/mvp_phase6/scrub_key_roundtrip_manifest.json"
REPORT_SCHEMA = "solidprivacy.mvp_scrub_key_roundtrip_validation_report"
REPORT_SCHEMA_VERSION = "1.0"

CANONICAL_ROWS = [
    {
        "original_value": "BETROKKENE-TEST-A",
        "placeholder": "[PERSOON_1]",
        "entity_type": "PERSON",
        "type_label": "Naam",
        "source": "detected",
        "review_status": "reviewed",
        "include": True,
        "timestamp": "2026-07-27T18:42:00+02:00",
        "document_label": "Synthetisch roundtripdossier",
    },
    {
        "original_value": "DOSSIER-TEST-2026-001",
        "placeholder": "[DOSSIER_1]",
        "entity_type": "LEGAL_REFERENCE",
        "type_label": "Dossiernummer",
        "source": "manual",
        "review_status": "reviewed",
        "include": True,
        "timestamp": "2026-07-27T18:42:00+02:00",
        "document_label": "Synthetisch roundtripdossier",
    },
]


def load_roundtrip_manifest(path: Path | str = DEFAULT_MANIFEST_PATH) -> dict[str, Any]:
    """Load and minimally validate the versioned synthetic manifest."""
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    if manifest.get("schema") != "solidprivacy.mvp_scrub_key_roundtrip_manifest":
        raise ValueError("Unexpected roundtrip manifest schema.")
    if manifest.get("schema_version") != "1.0":
        raise ValueError("Unsupported roundtrip manifest schema version.")
    if manifest.get("synthetic_only") is not True:
        raise ValueError("Roundtrip manifest must be marked synthetic_only=true.")
    cases = manifest.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("Roundtrip manifest must contain cases.")
    case_ids = [case.get("id") for case in cases if isinstance(case, dict)]
    if len(case_ids) != len(set(case_ids)):
        raise ValueError("Roundtrip manifest case ids must be unique.")
    return manifest


def build_canonical_scrub_key() -> dict[str, Any]:
    """Return the deterministic synthetic baseline key."""
    return build_scrub_key(CANONICAL_ROWS, document_label="Synthetisch roundtripdossier")


def build_variant_scrub_key(variant: str) -> dict[str, Any]:
    """Build one deterministic key variant used by the manifest."""
    canonical = build_canonical_scrub_key()

    if variant == "canonical":
        return canonical

    if variant == "duplicate_person_placeholder":
        key = deepcopy(canonical)
        duplicate = deepcopy(key["items"][0])
        duplicate["original_value"] = "BETROKKENE-TEST-B"
        key["items"].append(duplicate)
        key["item_count"] = len(key["items"])
        return key

    if variant == "person_only":
        key = deepcopy(canonical)
        key["items"] = [key["items"][0]]
        key["item_count"] = 1
        return key

    if variant == "tampered_item_count":
        key = deepcopy(canonical)
        key["item_count"] = 999
        return key

    if variant == "disjoint_wrong_key":
        rows = [
            {
                "original_value": "ANDERE-CLIENT",
                "placeholder": "[CLIENT_1]",
                "entity_type": "PERSON",
                "type_label": "Naam",
                "source": "detected",
                "review_status": "reviewed",
                "include": True,
                "timestamp": "2026-07-27T18:42:00+02:00",
            },
            {
                "original_value": "ANDERE-ZAAK-2026-999",
                "placeholder": "[ZAAK_1]",
                "entity_type": "LEGAL_REFERENCE",
                "type_label": "Zaaknummer",
                "source": "manual",
                "review_status": "reviewed",
                "include": True,
                "timestamp": "2026-07-27T18:42:00+02:00",
            },
        ]
        return build_scrub_key(rows, document_label="Ander synthetisch dossier")

    if variant == "same_placeholders_wrong_originals":
        key = deepcopy(canonical)
        key["items"][0]["original_value"] = "VERKEERDE-PERSOON"
        key["items"][1]["original_value"] = "VERKEERD-DOSSIER"
        key["document_label"] = "Verkeerd synthetisch dossier"
        for item in key["items"]:
            item["document_label"] = "Verkeerd synthetisch dossier"
        return key

    if variant == "same_original_distinct_placeholders":
        key = deepcopy(canonical)
        key["items"][1]["original_value"] = key["items"][0]["original_value"]
        return key

    raise ValueError(f"Unknown Scrub Key variant: {variant}")


def _expected_projection(case: dict[str, Any]) -> dict[str, Any]:
    return {
        "text": case["expected_text"],
        "replacement_count": case["expected_replacement_count"],
        "unknown_placeholders": case["expected_unknown_placeholders"],
        "placeholders_not_found": case["expected_placeholders_not_found"],
        "duplicate_placeholders": case["expected_duplicate_placeholders"],
        "has_validation_issue": case["expected_validation_issue"],
    }


def _actual_projection(result: dict[str, Any]) -> dict[str, Any]:
    return {
        "text": result.get("text", ""),
        "replacement_count": result.get("replacement_count", 0),
        "unknown_placeholders": result.get("unknown_placeholders", []),
        "placeholders_not_found": result.get("placeholders_not_found", []),
        "duplicate_placeholders": result.get("duplicate_placeholders", []),
        "has_validation_issue": bool(result.get("validation_issues")),
    }


def evaluate_roundtrip_case(case: dict[str, Any]) -> dict[str, Any]:
    """Execute one manifest case against the existing deterministic helper."""
    key = build_variant_scrub_key(str(case["key_variant"]))
    result = reinsert_from_scrub_key(case["input_text"], key)
    expected = _expected_projection(case)
    actual = _actual_projection(result)
    matches_expected = actual == expected

    return {
        "id": case["id"],
        "category": case["category"],
        "key_variant": case["key_variant"],
        "expected_safety_class": case["expected_safety_class"],
        "matches_expected": matches_expected,
        "expected": expected,
        "actual": actual,
        "local_only": result.get("local_only") is True,
        "ai_processing": result.get("ai_processing") is True,
        "cloud_processing": result.get("cloud_processing") is True,
        "validation_issues": result.get("validation_issues", []),
    }


def build_roundtrip_findings(case_results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Derive explicit risk findings from the deterministic case evidence."""
    by_id = {case["id"]: case for case in case_results}
    findings: list[dict[str, Any]] = []

    wrong_same_namespace = by_id["wrong_key_same_placeholder_namespace"]
    if (
        wrong_same_namespace["matches_expected"]
        and wrong_same_namespace["actual"]["replacement_count"] == 2
        and not wrong_same_namespace["actual"]["unknown_placeholders"]
        and not wrong_same_namespace["actual"]["placeholders_not_found"]
        and not wrong_same_namespace["validation_issues"]
    ):
        findings.append(
            {
                "id": "scrub_key_document_binding_missing",
                "severity": "critical",
                "risk": "R2",
                "evidence_case_ids": ["wrong_key_same_placeholder_namespace"],
                "description": (
                    "A structurally valid wrong or tampered Scrub Key that reuses the same "
                    "placeholder namespace can restore incorrect original values without a "
                    "detectable mismatch."
                ),
                "requires_separate_triage": True,
                "schema_or_export_change_may_be_required": True,
            }
        )

    indirect_ids = [
        "malformed_missing_bracket",
        "underscore_removed",
        "lowercase_placeholder",
    ]
    if all(by_id[case_id]["matches_expected"] for case_id in indirect_ids):
        findings.append(
            {
                "id": "malformed_placeholder_detection_is_indirect",
                "severity": "medium",
                "risk": "R3",
                "evidence_case_ids": indirect_ids,
                "description": (
                    "Malformed tokens outside the placeholder grammar are not identified as "
                    "unknown tokens; the audit signals them indirectly because the expected "
                    "Scrub Key placeholder is not found."
                ),
                "requires_separate_triage": True,
                "schema_or_export_change_may_be_required": False,
            }
        )

    return findings


def run_roundtrip_validation(path: Path | str = DEFAULT_MANIFEST_PATH) -> dict[str, Any]:
    """Run the complete deterministic matrix and return machine-readable evidence."""
    manifest = load_roundtrip_manifest(path)
    case_results = [evaluate_roundtrip_case(case) for case in manifest["cases"]]
    findings = build_roundtrip_findings(case_results)
    failed_case_ids = [case["id"] for case in case_results if not case["matches_expected"]]

    return {
        "schema": REPORT_SCHEMA,
        "schema_version": REPORT_SCHEMA_VERSION,
        "generated_at": "2026-07-27T18:42:00+02:00",
        "workpackage": "SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION",
        "synthetic_only": True,
        "local_only": all(case["local_only"] for case in case_results),
        "external_ai_used": any(case["ai_processing"] for case in case_results),
        "cloud_processing_used": any(case["cloud_processing"] for case in case_results),
        "case_count": len(case_results),
        "failed_case_count": len(failed_case_ids),
        "failed_case_ids": failed_case_ids,
        "finding_count": len(findings),
        "critical_finding_count": sum(finding["severity"] == "critical" for finding in findings),
        "medium_finding_count": sum(finding["severity"] == "medium" for finding in findings),
        "findings": findings,
        "cases": case_results,
        "validation_complete": not failed_case_ids,
        "production_ready": False,
        "human_review_required": True,
        "product_code_changed": False,
        "next_workpackage": "SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE",
    }
