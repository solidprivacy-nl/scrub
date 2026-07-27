from __future__ import annotations

import hashlib
import json
import re
from copy import deepcopy
from pathlib import Path

from scrub_key_reinsert import detect_placeholders


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "test_cases/mvp_phase6/scrub_key_binding_contract.json"
SPEC_PATH = ROOT / "SCRUB_KEY_BINDING_CONTRACT.md"
REINSERT_UI_PATH = ROOT / "reinsert_mode_ui.py"


def load_contract() -> dict:
    return json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))


def canonical_digest(payload: dict) -> str:
    serialized = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def test_contract_is_versioned_and_not_an_implementation_package() -> None:
    contract = load_contract()

    assert contract["schema"] == "solidprivacy.scrub_key_binding_contract"
    assert contract["schema_version"] == "1.0"
    assert contract["implementation_authorized"] is False
    assert contract["production_ready"] is False
    assert contract["human_review_required"] is True
    assert contract["next_workpackage"] == "SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION"


def test_binding_id_grammar_accepts_only_the_frozen_base32_shape() -> None:
    contract = load_contract()
    pattern = re.compile(contract["binding_id_pattern"])

    assert pattern.fullmatch(contract["binding_id"])
    assert pattern.fullmatch(contract["other_binding_id"])
    assert len(contract["binding_id"]) == 17
    assert contract["binding_id"].startswith("B")
    for value in contract["invalid_binding_ids"]:
        assert pattern.fullmatch(value) is None


def test_bound_automatic_and_manual_placeholders_match_the_frozen_grammar() -> None:
    contract = load_contract()
    pattern = re.compile(contract["bound_placeholder_pattern"])

    for token in contract["automatic_placeholders"]:
        match = pattern.fullmatch(token)
        assert match is not None
        assert match.group("binding_id") == contract["binding_id"]
        assert match.group("manual") is None
        assert match.group("index").isdigit()

    for token in contract["manual_placeholders"]:
        match = pattern.fullmatch(token)
        assert match is not None
        assert match.group("binding_id") == contract["binding_id"]
        assert match.group("manual") == "HANDMATIG"
        assert match.group("index").isdigit()


def test_entity_labels_with_underscores_remain_parseable() -> None:
    pattern = re.compile(load_contract()["bound_placeholder_pattern"])
    match = pattern.fullmatch("[IP_ADRES_BK7M4Q2XR5TD3W6YZ_02]")

    assert match is not None
    assert match.group("label") == "IP_ADRES"
    assert match.group("binding_id") == "BK7M4Q2XR5TD3W6YZ"
    assert match.group("index") == "02"


def test_existing_general_placeholder_detector_already_sees_bound_tokens() -> None:
    contract = load_contract()
    text = " / ".join(contract["automatic_placeholders"] + contract["manual_placeholders"])

    assert detect_placeholders(text) == sorted(
        contract["automatic_placeholders"] + contract["manual_placeholders"]
    )


def test_bound_key_metadata_and_item_bindings_are_consistent() -> None:
    contract = load_contract()
    key = contract["canonical_bound_key"]
    placeholder_pattern = re.compile(contract["bound_placeholder_pattern"])

    assert key["schema"] == "solidprivacy.scrub_key"
    assert key["schema_version"] == "1.1"
    assert key["binding_version"] == "1"
    assert key["document_binding_id"] == contract["binding_id"]
    assert key["mapping_digest_algorithm"] == "sha256"
    assert re.fullmatch(r"[0-9a-f]{64}", key["mapping_digest"])
    assert key["item_count"] == len(key["items"])

    for item in key["items"]:
        match = placeholder_pattern.fullmatch(item["placeholder"])
        assert match is not None
        assert match.group("binding_id") == key["document_binding_id"]


def test_canonical_digest_fixture_is_exact_and_deterministic() -> None:
    contract = load_contract()
    payload = contract["canonical_digest_payload"]

    assert canonical_digest(payload) == contract["expected_mapping_digest"]
    assert contract["canonical_bound_key"]["mapping_digest"] == contract["expected_mapping_digest"]
    assert canonical_digest(deepcopy(payload)) == contract["expected_mapping_digest"]


def test_canonical_digest_is_order_independent_after_contract_sorting() -> None:
    contract = load_contract()
    key = contract["canonical_bound_key"]

    def payload_for(candidate: dict) -> dict:
        return {
            "schema": candidate["schema"],
            "schema_version": candidate["schema_version"],
            "privacy_model": candidate["privacy_model"],
            "reversible": candidate["reversible"],
            "storage_policy": candidate["storage_policy"],
            "external_ai_policy": candidate["external_ai_policy"],
            "excluded_rows_policy": candidate["excluded_rows_policy"],
            "binding_version": candidate["binding_version"],
            "document_binding_id": candidate["document_binding_id"],
            "item_count": candidate["item_count"],
            "items": [
                {
                    field: item[field]
                    for field in ["placeholder", "original_value", "entity_type", "include_state"]
                }
                for item in sorted(
                    candidate["items"],
                    key=lambda item: (
                        item["placeholder"],
                        item["original_value"],
                        item["entity_type"],
                    ),
                )
            ],
        }

    reversed_key = deepcopy(key)
    reversed_key["items"] = list(reversed(reversed_key["items"]))

    assert payload_for(key) == contract["canonical_digest_payload"]
    assert payload_for(reversed_key) == contract["canonical_digest_payload"]
    assert canonical_digest(payload_for(reversed_key)) == contract["expected_mapping_digest"]


def test_mapping_digest_changes_when_restoration_semantics_change() -> None:
    contract = load_contract()
    payload = deepcopy(contract["canonical_digest_payload"])
    payload["items"][0]["original_value"] = "ANDERE-SYNTHETISCHE-WAARDE"

    assert canonical_digest(payload) != contract["expected_mapping_digest"]


def test_binding_validation_status_matrix_is_complete_and_unique() -> None:
    contract = load_contract()
    cases = contract["binding_validation_cases"]
    statuses = {case["expected_status"] for case in cases}

    assert len({case["id"] for case in cases}) == len(cases)
    assert statuses == {
        "bound_match",
        "legacy_unbound",
        "binding_mismatch",
        "mixed_document_bindings",
        "missing_document_binding",
        "invalid_mapping_digest",
        "invalid_bound_key",
        "legacy_key_for_bound_document",
    }


def test_fail_closed_statuses_never_allow_replacement() -> None:
    fail_closed = {
        "binding_mismatch",
        "mixed_document_bindings",
        "missing_document_binding",
        "invalid_mapping_digest",
        "invalid_bound_key",
        "legacy_key_for_bound_document",
    }

    for case in load_contract()["binding_validation_cases"]:
        if case["expected_status"] in fail_closed:
            assert case["replacement_allowed"] is False
            assert case["verified_document_match"] is False


def test_bound_match_and_legacy_compatibility_are_not_conflated() -> None:
    cases = {case["id"]: case for case in load_contract()["binding_validation_cases"]}

    assert cases["bound_match"]["replacement_allowed"] is True
    assert cases["bound_match"]["verified_document_match"] is True
    assert cases["bound_match"]["legacy_unbound"] is False

    assert cases["legacy_unbound"]["replacement_allowed"] is True
    assert cases["legacy_unbound"]["verified_document_match"] is False
    assert cases["legacy_unbound"]["legacy_unbound"] is True


def test_future_binding_result_shape_is_frozen() -> None:
    assert load_contract()["required_result_fields"] == [
        "ok",
        "binding_status",
        "replacement_allowed",
        "verified_document_match",
        "legacy_unbound",
        "errors",
        "warnings",
        "document_binding_ids",
        "key_binding_id",
        "mapping_digest_valid",
    ]


def test_future_pure_helper_responsibilities_are_frozen() -> None:
    assert load_contract()["required_helper_responsibilities"] == [
        "validate_document_binding_id",
        "build_bound_placeholder",
        "parse_bound_placeholder",
        "canonical_mapping_digest_payload",
        "compute_mapping_digest",
        "validate_bound_scrub_key",
        "validate_document_key_binding",
    ]


def test_three_step_reinsert_ux_remains_unchanged_by_contract_package() -> None:
    contract = load_contract()["ux_contract"]
    ui_text = REINSERT_UI_PATH.read_text(encoding="utf-8")

    assert contract["steps"] == [
        "source_document_or_text",
        "corresponding_scrub_key",
        "restored_download",
    ]
    assert contract["new_source_or_key_buttons"] is False
    assert contract["new_source_or_key_checkboxes"] is False
    assert contract["final_confidential_download_acknowledgement"] is True
    assert 'st.subheader("1. Voeg het bestand of de tekst toe die je wilt herstellen")' in ui_text
    assert 'st.subheader("2. Voeg de bijbehorende Scrub Key toe")' in ui_text
    assert 'st.subheader("3. Download het herstelde resultaat")' in ui_text
    assert "Valideer en laad Scrub Key" not in ui_text
    assert "Zet DOCX-bestand lokaal terug" not in ui_text


def test_spec_explicitly_limits_security_claims_and_side_effects() -> None:
    spec = SPEC_PATH.read_text(encoding="utf-8")

    assert "not a signature or authenticity proof" in spec
    assert "does not provide encrypted key storage" in spec
    assert "must not be applied to bound placeholders" in spec
    assert "No partial restoration may occur before binding validation succeeds" in spec
    assert "No implementation is authorized" not in spec
    assert "Model implementation may start only when the contract fixture and contract tests are green" in spec
    for forbidden in [
        "requests.post",
        "httpx.post",
        "openai.chat",
        "server-side signing secret",
        "automatic placeholder repair",
    ]:
        assert forbidden not in spec


def test_contract_examples_are_synthetic_only() -> None:
    combined = CONTRACT_PATH.read_text(encoding="utf-8") + SPEC_PATH.read_text(encoding="utf-8")

    assert "BETROKKENE-TEST-A" in combined
    assert "DOSSIER-TEST-2026-001" in combined
    assert "Jan Jansen" not in combined
    assert "Piet de Vries" not in combined
    assert "123456782" not in combined
