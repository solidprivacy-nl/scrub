"""Evidence report for MVP Phase 6 document hygiene and fidelity hardening."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from mvp_phase6_validation_report import build_validation_report


REPORT_SCHEMA = "solidprivacy.mvp_phase6_document_fidelity_hardening_report"
REPORT_SCHEMA_VERSION = "1.0"
FIXED_TIMESTAMP = "2026-07-17T20:30:00Z"


def build_document_fidelity_report(
    manifest: Mapping[str, Any],
    baseline_report: Mapping[str, Any],
    triage_report: Mapping[str, Any],
) -> dict[str, Any]:
    current = build_validation_report(manifest)
    docx_case = next(
        item for item in current["cases"]
        if item["id"] == "docx_mixed_structure_roundtrip"
    )
    pdf_case = next(
        item for item in current["cases"]
        if item["id"] == "pdf_text_based_to_txt_reinsert"
    )

    docx_resolved = (
        docx_case["roundtrip_complete"] is True
        and docx_case["residual_placeholders"] == []
        and docx_case["header_footer_roundtrip_values_present"] is True
        and docx_case["audit_expectations_met"] is True
        and any(
            part.startswith("word/header")
            for part in docx_case["processed_parts"]
        )
        and any(
            part.startswith("word/footer")
            for part in docx_case["processed_parts"]
        )
    )
    pdf_boundary_preserved = (
        pdf_case["roundtrip_text_equal"] is True
        and pdf_case["reinsert_output_type"] == "txt"
        and pdf_case["restored_pdf_supported"] is False
        and pdf_case["ocr_supported"] is False
    )

    baseline_docx_gap = next(
        item
        for item in baseline_report["evidence_gaps"]
        if item["category"] == "known_docx_reinsert_limitation"
    )
    triage_docx = next(
        item
        for item in triage_report["classifications"]
        if item["source_category"] == "known_docx_reinsert_limitation"
    )

    resolved_findings = []
    if docx_resolved:
        resolved_findings.append(
            {
                "source_case_id": baseline_docx_gap["case_id"],
                "source_category": baseline_docx_gap["category"],
                "triage_classification": triage_docx["classification"],
                "resolution": "DOCX body, tables, headers and footers restore deterministically from the existing Scrub Key.",
                "resolved_placeholders": docx_case[
                    "resolved_header_footer_placeholders"
                ],
                "processed_parts": docx_case["processed_parts"],
            }
        )

    remaining_findings = [
        {
            "case_id": pdf_case["id"],
            "category": "known_pdf_reinsert_limitation",
            "status": "explicit_product_boundary",
            "reinsert_output_type": "txt",
            "restored_pdf_supported": False,
            "ocr_supported": False,
        }
    ]

    return {
        "schema": REPORT_SCHEMA,
        "schema_version": REPORT_SCHEMA_VERSION,
        "generated_at": FIXED_TIMESTAMP,
        "source_baseline_report": (
            "output/validation/mvp_phase6_synthetic_validation_report.json"
        ),
        "source_triage_report": (
            "output/validation/mvp_phase6_false_negative_gap_triage.json"
        ),
        "synthetic_data_only": True,
        "human_review_required": True,
        "production_ready": False,
        "production_readiness_claim": False,
        "local_only": True,
        "ai_processing": False,
        "cloud_processing": False,
        "ocr_processing": False,
        "docx_header_footer_reinsert_resolved": docx_resolved,
        "pdf_boundary_preserved": pdf_boundary_preserved,
        "resolved_finding_count": len(resolved_findings),
        "remaining_finding_count": len(remaining_findings),
        "resolved_findings": resolved_findings,
        "remaining_findings": remaining_findings,
        "current_validation_report": current,
        "next_recommended_package": (
            "SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION"
        ),
    }


def write_document_fidelity_report(
    manifest: Mapping[str, Any],
    baseline_report: Mapping[str, Any],
    triage_report: Mapping[str, Any],
    output_path: str | Path,
) -> dict[str, Any]:
    report = build_document_fidelity_report(
        manifest,
        baseline_report,
        triage_report,
    )
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return report
