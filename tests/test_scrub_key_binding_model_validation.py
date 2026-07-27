from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_PATH = ROOT / "output/validation/mvp_scrub_key_binding_model_validation.json"


def test_binding_model_validation_evidence_is_committed() -> None:
    evidence = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))

    assert evidence["workpackage"] == "SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION"
    assert evidence["status"] == "targeted_validation_passed"
    assert evidence["pure_model_module"] == "scrub_key_binding.py"
    assert evidence["contract_fixture_digest"] == (
        "516075e4970f0def6052aaac6885e12339e7cdbe012d4104aa7387c51a53faa3"
    )
    assert evidence["bound_statuses_implemented"] == 8
    assert evidence["fail_closed_statuses_implemented"] == 6
    assert evidence["legacy_v1_explicit_unbound"] is True
    assert evidence["streamlit_imported"] is False
    assert evidence["network_access"] is False
    assert evidence["file_writes"] is False
    assert evidence["export_integrated"] is False
    assert evidence["reinsert_integrated"] is False
    assert evidence["product_ui_changed"] is False
    assert evidence["production_ready"] is False
    assert evidence["human_review_required"] is True
    assert evidence["next_workpackage"] == "SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION"


def test_temporary_binding_model_operator_is_absent() -> None:
    assert not (ROOT / ".github/workflows/mvp_scrub_key_binding_model_operator.yml").exists()
