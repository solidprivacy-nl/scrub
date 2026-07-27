from __future__ import annotations

import json
from pathlib import Path

from mvp_scrub_key_roundtrip_validation import run_roundtrip_validation


ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = ROOT / "output/validation/mvp_scrub_key_roundtrip_validation_report.json"


def test_committed_roundtrip_report_matches_deterministic_generator() -> None:
    committed = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    assert committed == run_roundtrip_validation()


def test_committed_roundtrip_report_records_evidence_and_safety_boundaries() -> None:
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    findings = {finding["id"]: finding for finding in report["findings"]}

    assert report["case_count"] == 15
    assert report["failed_case_count"] == 0
    assert report["finding_count"] == 2
    assert report["critical_finding_count"] == 1
    assert report["validation_complete"] is True
    assert report["local_only"] is True
    assert report["external_ai_used"] is False
    assert report["cloud_processing_used"] is False
    assert report["production_ready"] is False
    assert report["human_review_required"] is True
    assert findings["scrub_key_document_binding_missing"]["severity"] == "critical"
    assert findings["malformed_placeholder_detection_is_indirect"]["severity"] == "medium"
    assert report["next_workpackage"] == "SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE"


def test_temporary_roundtrip_operator_is_absent() -> None:
    assert not (
        ROOT / ".github/workflows/mvp_scrub_key_roundtrip_validation_operator.yml"
    ).exists()
