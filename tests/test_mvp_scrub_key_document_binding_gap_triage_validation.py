from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_PATH = ROOT / "output/validation/mvp_scrub_key_document_binding_gap_triage_validation.json"


def test_binding_gap_triage_validation_evidence_is_committed() -> None:
    evidence = json.loads(VALIDATION_PATH.read_text(encoding="utf-8"))

    assert evidence["workpackage"] == "SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE"
    assert evidence["targeted_tests_passed"] is True
    assert evidence["source_roundtrip_cases"] == 15
    assert evidence["source_roundtrip_failures"] == 0
    assert evidence["critical_findings_triaged"] == 1
    assert evidence["medium_findings_triaged"] == 1
    assert evidence["implementation_authorized"] is False
    assert evidence["production_ready"] is False
    assert evidence["human_review_required"] is True
    assert evidence["next_workpackage"] == "SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS"


def test_temporary_binding_triage_operator_is_removed_before_merge() -> None:
    assert not (ROOT / ".github/workflows/mvp_scrub_key_binding_triage_operator.yml").exists()
