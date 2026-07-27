from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAGE_PATH = ROOT / "output/validation/mvp_scrub_key_document_binding_gap_triage.json"
SOURCE_REPORT_PATH = ROOT / "output/validation/mvp_scrub_key_roundtrip_validation_report.json"
TRIAGE_DOC_PATH = ROOT / "MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_triage_consumes_the_critical_roundtrip_finding() -> None:
    source = load_json(SOURCE_REPORT_PATH)
    triage = load_json(TRIAGE_PATH)
    source_findings = {finding["id"]: finding for finding in source["findings"]}

    assert source_findings["scrub_key_document_binding_missing"]["severity"] == "critical"
    assert triage["source_finding"] == "scrub_key_document_binding_missing"
    assert triage["severity"] == "critical"
    assert triage["risk"] == "R2"
    assert triage["status"] == "completed_triage"


def test_triage_separates_accidental_and_malicious_threats() -> None:
    triage = load_json(TRIAGE_PATH)
    threats = {threat["id"]: threat for threat in triage["threat_classes"]}

    assert threats["accidental_wrong_document_pairing"]["priority"] == "mvp_primary"
    assert threats["accidental_key_corruption"]["priority"] == "mvp_secondary"
    assert threats["malicious_tampering"]["priority"] == "deferred_security_layer"


def test_recommended_option_is_cross_format_and_preserves_three_step_ux() -> None:
    triage = load_json(TRIAGE_PATH)
    options = {option["id"]: option for option in triage["options"]}
    contract = triage["recommended_contract"]

    binding = options["binding_id_in_placeholder_namespace_and_key"]
    assert binding["decision"] == "recommend"
    assert binding["cross_format"] is True
    assert binding["survives_ai_roundtrip"] is True
    assert binding["detects_same_namespace_wrong_key"] is True
    assert contract["binding_id"]["contains_personal_data"] is False
    assert contract["binding_id"]["secret"] is False
    assert contract["binding_id"]["minimum_entropy_bits"] >= 80
    assert contract["ux_policy"]["flow"] == [
        "source_document_or_text",
        "corresponding_scrub_key",
        "restored_download",
    ]
    assert contract["ux_policy"]["new_confirmation_buttons"] is False
    assert contract["ux_policy"]["new_confirmation_checkboxes"] is False
    assert contract["ux_policy"]["final_confidential_download_acknowledgement"] is True


def test_weak_binding_options_are_explicitly_rejected() -> None:
    options = {option["id"]: option for option in load_json(TRIAGE_PATH)["options"]}

    assert options["document_label_match"]["decision"] == "reject_as_security_control"
    assert options["full_scrubbed_content_hash"]["decision"] == "reject_as_primary_binding"
    assert options["placeholder_set_or_order_hash"]["decision"] == "reject_as_sufficient_binding"
    assert options["filename_metadata_or_sidecar_only"]["decision"] == "reject_as_primary_binding"


def test_mapping_digest_is_not_misrepresented_as_authenticity() -> None:
    triage = load_json(TRIAGE_PATH)
    options = {option["id"]: option for option in triage["options"]}
    digest = triage["recommended_contract"]["mapping_digest"]
    boundaries = triage["mitigation_boundaries"]

    assert options["canonical_mapping_digest"]["decision"] == "recommend_as_complement"
    assert digest["algorithm"] == "sha256"
    assert digest["authenticity_claim"] is False
    assert boundaries["malicious_key_edit_with_recomputed_unkeyed_digest"] == "not_mitigated"
    assert options["signature_or_hmac"]["decision"] == "defer"


def test_bound_reinsert_contract_fails_closed_before_replacement() -> None:
    policy = load_json(TRIAGE_PATH)["recommended_contract"]["reinsert_policy"]

    assert policy["binding_mismatch"] == "fail_closed_zero_replacements"
    assert policy["mixed_binding_ids"] == "fail_closed_zero_replacements"
    assert policy["invalid_mapping_digest"] == "fail_closed_zero_replacements"
    assert policy["legacy_unbound_key"] == "explicit_legacy_status_and_warning"
    assert policy["unknown_duplicate_missing_placeholder_audit"] == "preserve"


def test_implementation_sequence_is_test_first_and_sequential() -> None:
    triage = load_json(TRIAGE_PATH)

    assert triage["approved_sequence"] == [
        "SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS",
        "SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION",
        "SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION",
        "SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION",
        "SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY",
    ]
    assert triage["implementation_authorized_in_this_package"] is False
    assert triage["next_workpackage"] == "SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS"


def test_triage_preserves_product_claim_boundaries() -> None:
    triage = load_json(TRIAGE_PATH)
    markdown = TRIAGE_DOC_PATH.read_text(encoding="utf-8")

    assert triage["mitigation_boundaries"]["production_ready"] is False
    assert triage["mitigation_boundaries"]["human_review_required"] is True
    assert "does not solve key leakage" in markdown
    assert "must not claim tamper-proof keys" in markdown
    assert "No implementation is authorized" in markdown


def test_triage_uses_synthetic_evidence_and_adds_no_product_imports() -> None:
    combined = TRIAGE_DOC_PATH.read_text(encoding="utf-8") + TRIAGE_PATH.read_text(encoding="utf-8")

    assert "BETROKKENE-TEST-A" not in combined
    assert "Jan Jansen" not in combined
    assert "requests.post" not in combined
    assert "openai" not in combined.lower()
    assert "anthropic" not in combined.lower()
