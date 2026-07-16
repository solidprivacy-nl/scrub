"""Manifest helpers for the synthetic MVP Phase 6 validation matrix."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


MATRIX_SCHEMA = "solidprivacy.mvp_phase6_validation_matrix"
MATRIX_SCHEMA_VERSION = "1.0"


def validate_validation_manifest(manifest: Any) -> list[str]:
    issues: list[str] = []
    if not isinstance(manifest, Mapping):
        return ["Manifest must be a JSON object."]
    if manifest.get("schema") != MATRIX_SCHEMA:
        issues.append(f"schema must be {MATRIX_SCHEMA}")
    if manifest.get("schema_version") != MATRIX_SCHEMA_VERSION:
        issues.append(f"schema_version must be {MATRIX_SCHEMA_VERSION}")
    if manifest.get("synthetic_data_only") is not True:
        issues.append("synthetic_data_only must be true")
    if manifest.get("human_review_required") is not True:
        issues.append("human_review_required must be true")
    if manifest.get("production_readiness_claim") is not False:
        issues.append("production_readiness_claim must be false")

    cases = manifest.get("cases")
    if not isinstance(cases, list) or not cases:
        issues.append("cases must be a non-empty list")
        return issues

    seen_ids: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, Mapping):
            issues.append(f"case {index} must be an object")
            continue
        case_id = str(case.get("id") or "").strip()
        if not case_id:
            issues.append(f"case {index} missing id")
        elif case_id in seen_ids:
            issues.append(f"duplicate case id: {case_id}")
        seen_ids.add(case_id)
        if case.get("document_type") not in {"txt", "docx", "pdf"}:
            issues.append(f"case {case_id or index} has unsupported document_type")
        if not isinstance(case.get("review_rows"), list) or not case.get("review_rows"):
            issues.append(f"case {case_id or index} requires review_rows")
    return issues


def load_validation_manifest(path: str | Path) -> dict[str, Any]:
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    issues = validate_validation_manifest(manifest)
    if issues:
        raise ValueError("Invalid Phase 6 validation manifest: " + "; ".join(issues))
    return manifest
