from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_REPORT = (
    ROOT / "output" / "validation" / "mvp_phase6_synthetic_validation_report.json"
)
TRIAGE_REPORT = (
    ROOT / "output" / "validation" / "mvp_phase6_false_negative_gap_triage.json"
)
TRIAGE_MD = ROOT / "MVP_PHASE6_FALSE_NEGATIVE_GAP_TRIAGE.md"


def _json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_triage_schema_and_product_claim_boundaries() -> None:
    triage = _json(TRIAGE_REPORT)

    assert triage["schema"] == "solidprivacy.mvp_phase6_gap_triage"
    assert triage["schema_version"] == "1.0"
    assert triage["synthetic_data_only"] is True
    assert triage["human_review_required"] is True
    assert triage["production_ready"] is False
    assert triage["production_readiness_claim"] is False
    assert triage["product_code_change_required_in_this_package"] is False


def test_triage_matches_every_source_evidence_gap() -> None:
    source = _json(SOURCE_REPORT)
    triage = _json(TRIAGE_REPORT)

    source_keys = {
        (item["case_id"], item["category"])
        for item in source["evidence_gaps"]
    }
    triage_keys = {
        (item["case_id"], item["source_category"])
        for item in triage["classifications"]
    }

    assert source["evidence_gap_count"] == 2
    assert triage["input_evidence_gap_count"] == 2
    assert triage_keys == source_keys


def test_no_recognizer_fix_is_claimed_without_detection_evidence() -> None:
    source = _json(SOURCE_REPORT)
    triage = _json(TRIAGE_REPORT)

    source_categories = {item["category"] for item in source["evidence_gaps"]}
    assert "false_negative_or_detection_gap" not in source_categories
    assert "over_masking_or_context_loss" not in source_categories

    assert triage["detection_false_negative_count"] == 0
    assert triage["misclassification_count"] == 0
    assert triage["role_over_masking_count"] == 0
    assert triage["recognizer_fix_required"] is False
    assert all(
        item["recognizer_fix_required"] is False
        for item in triage["classifications"]
    )


def test_document_findings_route_to_fidelity_hardening() -> None:
    triage = _json(TRIAGE_REPORT)
    classifications = {
        item["source_category"]: item
        for item in triage["classifications"]
    }

    docx = classifications["known_docx_reinsert_limitation"]
    assert docx["classification"] == "document_fidelity_and_reinsert_scope"
    assert docx["observed_evidence"]["main_document_body_roundtrip_passed"] is True
    assert docx["observed_evidence"]["docx_hygiene_findings_visible"] is True
    assert docx["accepted_without_followup"] is False

    pdf = classifications["known_pdf_reinsert_limitation"]
    assert pdf["classification"] == "document_format_product_boundary"
    assert pdf["observed_evidence"]["text_roundtrip_passed"] is True
    assert pdf["observed_evidence"]["restored_pdf_supported"] is False
    assert pdf["observed_evidence"]["ocr_supported"] is False
    assert pdf["accepted_without_followup"] is False

    assert {
        item["routed_workpackage"]
        for item in triage["classifications"]
    } == {"SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING"}
    assert triage["next_recommended_package"] == (
        "SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING"
    )


def test_methodology_correction_is_recorded_and_false_gap_removed() -> None:
    triage = _json(TRIAGE_REPORT)
    source = _json(SOURCE_REPORT)
    markdown = TRIAGE_MD.read_text(encoding="utf-8")

    corrections = triage["methodology_corrections"]
    assert len(corrections) == 1
    assert ".invalid" in corrections[0]["issue"]
    assert "example.com" in corrections[0]["correction"]
    assert source["cases"][0]["detection"]["detection_expectations_met"] is True
    assert source["cases"][0]["detection"]["missing_expected_values"] == []
    assert "no email false-negative evidence" in markdown


def test_triage_is_evidence_only_and_contains_no_runtime_code() -> None:
    markdown = TRIAGE_MD.read_text(encoding="utf-8")

    assert "No recognizer fix package should be opened" in markdown
    assert "Human review remains mandatory" in markdown
    assert "No OCR or restored-PDF implementation is authorized" in markdown
    assert not TRIAGE_REPORT.name.endswith(".py")
