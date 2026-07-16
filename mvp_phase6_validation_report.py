"""Build the machine-readable MVP Phase 6 synthetic validation report."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from mvp_phase6_document_cases import run_docx_case, run_pdf_case
from mvp_phase6_validation_manifest import validate_validation_manifest
from mvp_phase6_workflow_core import FIXED_BASELINE_TIMESTAMP, run_txt_case


REPORT_SCHEMA = "solidprivacy.mvp_phase6_validation_report"
REPORT_SCHEMA_VERSION = "1.0"


def build_validation_report(manifest: Mapping[str, Any]) -> dict[str, Any]:
    issues = validate_validation_manifest(manifest)
    if issues:
        raise ValueError("Invalid Phase 6 validation manifest: " + "; ".join(issues))

    results: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        document_type = case["document_type"]
        if document_type == "txt":
            results.append(run_txt_case(case))
        elif document_type == "docx":
            results.append(run_docx_case(case))
        elif document_type == "pdf":
            results.append(run_pdf_case(case))
        else:
            raise ValueError(f"Unsupported document type: {document_type}")

    gaps: list[dict[str, Any]] = []
    for result in results:
        if result["document_type"] == "txt":
            for value in result["detection"].get("missing_expected_values", []):
                gaps.append(
                    {
                        "case_id": result["id"],
                        "category": "false_negative_or_detection_gap",
                        "value": value,
                    }
                )
            for term in result["detection"].get("removed_preserved_terms", []):
                gaps.append(
                    {
                        "case_id": result["id"],
                        "category": "over_masking_or_context_loss",
                        "value": term,
                    }
                )
        elif result["document_type"] == "docx" and result.get("residual_placeholders"):
            gaps.append(
                {
                    "case_id": result["id"],
                    "category": "known_docx_reinsert_limitation",
                    "value": list(result["residual_placeholders"]),
                }
            )
        elif result["document_type"] == "pdf":
            gaps.append(
                {
                    "case_id": result["id"],
                    "category": "known_pdf_reinsert_limitation",
                    "value": "restored TXT only; no OCR or restored PDF",
                }
            )

    failing_cases = [item["id"] for item in results if item["status"] == "fail"]
    return {
        "schema": REPORT_SCHEMA,
        "schema_version": REPORT_SCHEMA_VERSION,
        "generated_at": FIXED_BASELINE_TIMESTAMP,
        "manifest_schema": manifest["schema"],
        "manifest_schema_version": manifest["schema_version"],
        "synthetic_data_only": True,
        "human_review_required": True,
        "production_ready": False,
        "production_readiness_claim": False,
        "local_only": True,
        "ai_processing": False,
        "cloud_processing": False,
        "ocr_processing": False,
        "case_count": len(results),
        "failing_case_count": len(failing_cases),
        "failing_cases": failing_cases,
        "evidence_gap_count": len(gaps),
        "evidence_gaps": gaps,
        "cases": results,
        "next_recommended_package": "SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE",
    }


def write_validation_report(
    manifest: Mapping[str, Any],
    output_path: str | Path,
) -> dict[str, Any]:
    report = build_validation_report(manifest)
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return report
