from __future__ import annotations

import json
from pathlib import Path

from mvp_document_fidelity_report import (
    build_document_fidelity_report,
    write_document_fidelity_report,
)
from mvp_phase6_validation_manifest import load_validation_manifest


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "test_cases" / "mvp_phase6" / "validation_manifest.json"
BASELINE = ROOT / "output" / "validation" / "mvp_phase6_synthetic_validation_report.json"
TRIAGE = ROOT / "output" / "validation" / "mvp_phase6_false_negative_gap_triage.json"


def _json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _report() -> dict:
    return build_document_fidelity_report(
        load_validation_manifest(MANIFEST),
        _json(BASELINE),
        _json(TRIAGE),
    )


def test_hardening_report_closes_docx_header_footer_finding() -> None:
    report = _report()

    assert report["schema"] == (
        "solidprivacy.mvp_phase6_document_fidelity_hardening_report"
    )
    assert report["schema_version"] == "1.0"
    assert report["docx_header_footer_reinsert_resolved"] is True
    assert report["resolved_finding_count"] == 1
    assert report["remaining_finding_count"] == 1

    resolved = report["resolved_findings"][0]
    assert resolved["source_category"] == "known_docx_reinsert_limitation"
    assert set(resolved["resolved_placeholders"]) == {
        "[CLIENT_REFERENTIE_01]",
        "[OVERIGE_REFERENTIE_01]",
    }
    assert any(part.startswith("word/header") for part in resolved["processed_parts"])
    assert any(part.startswith("word/footer") for part in resolved["processed_parts"])


def test_pdf_boundary_remains_explicit_and_unexpanded() -> None:
    report = _report()

    assert report["pdf_boundary_preserved"] is True
    remaining = report["remaining_findings"][0]
    assert remaining["category"] == "known_pdf_reinsert_limitation"
    assert remaining["status"] == "explicit_product_boundary"
    assert remaining["reinsert_output_type"] == "txt"
    assert remaining["restored_pdf_supported"] is False
    assert remaining["ocr_supported"] is False


def test_current_matrix_has_no_docx_residual_gap() -> None:
    current = _report()["current_validation_report"]
    docx = next(case for case in current["cases"] if case["document_type"] == "docx")

    assert current["failing_case_count"] == 0
    assert docx["roundtrip_complete"] is True
    assert docx["residual_placeholders"] == []
    assert docx["header_footer_roundtrip_values_present"] is True
    assert {gap["category"] for gap in current["evidence_gaps"]} == {
        "known_pdf_reinsert_limitation"
    }


def test_report_retains_privacy_and_claim_boundaries() -> None:
    report = _report()

    assert report["synthetic_data_only"] is True
    assert report["human_review_required"] is True
    assert report["production_ready"] is False
    assert report["production_readiness_claim"] is False
    assert report["local_only"] is True
    assert report["ai_processing"] is False
    assert report["cloud_processing"] is False
    assert report["ocr_processing"] is False
    assert report["next_recommended_package"] == (
        "SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION"
    )


def test_report_writer_is_deterministic(tmp_path: Path) -> None:
    output = tmp_path / "hardening.json"
    first = write_document_fidelity_report(
        load_validation_manifest(MANIFEST),
        _json(BASELINE),
        _json(TRIAGE),
        output,
    )
    first_text = output.read_text(encoding="utf-8")
    second = write_document_fidelity_report(
        load_validation_manifest(MANIFEST),
        _json(BASELINE),
        _json(TRIAGE),
        output,
    )

    assert first == second
    assert first_text == output.read_text(encoding="utf-8")
    assert json.loads(first_text) == first
