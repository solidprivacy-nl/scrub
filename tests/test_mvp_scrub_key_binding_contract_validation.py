from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_PATH = ROOT / "output/validation/mvp_scrub_key_binding_contract_validation.json"


def test_binding_contract_validation_evidence_is_committed() -> None:
    evidence = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8"))

    assert evidence["workpackage"] == "SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS"
    assert evidence["contract_schema"] == "solidprivacy.scrub_key_binding_contract"
    assert evidence["contract_schema_version"] == "1.0"
    assert evidence["proposed_bound_key_schema_version"] == "1.1"
    assert evidence["binding_id_pattern"] == "^B[A-Z2-7]{16}$"
    assert evidence["binding_payload_entropy_bits"] == 80
    assert evidence["mapping_digest_algorithm"] == "sha256"
    assert evidence["canonical_fixture_digest_independently_recomputed"] is True
    assert evidence["binding_status_count"] == 8
    assert evidence["fail_closed_status_count"] == 6
    assert evidence["legacy_v1_status_explicit"] is True
    assert evidence["three_step_reinsert_ux_preserved"] is True
    assert evidence["new_source_or_key_confirmation_buttons"] is False
    assert evidence["new_source_or_key_confirmation_checkboxes"] is False
    assert evidence["final_confidential_download_acknowledgement_preserved"] is True
    assert evidence["implementation_authorized"] is False
    assert evidence["product_code_changed"] is False
    assert evidence["production_ready"] is False
    assert evidence["human_review_required"] is True
    assert evidence["next_workpackage"] == "SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION"


def test_temporary_binding_contract_operator_is_absent() -> None:
    assert not (ROOT / ".github/workflows/mvp_scrub_key_binding_contract_operator.yml").exists()
