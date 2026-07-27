from __future__ import annotations

import ast
import json
from copy import deepcopy
from pathlib import Path

import pytest

from scrub_key_binding import (
    BINDING_ID_RE,
    BOUND_PLACEHOLDER_RE,
    BOUND_SCHEMA_VERSION,
    BINDING_VERSION,
    LEGACY_UNBOUND_WARNING,
    build_bound_placeholder,
    canonical_mapping_digest_payload,
    compute_mapping_digest,
    extract_document_binding_ids,
    generate_document_binding_id,
    parse_bound_placeholder,
    validate_bound_scrub_key,
    validate_document_binding_id,
    validate_document_key_binding,
)


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "test_cases/mvp_phase6/scrub_key_binding_contract.json"
MODULE_PATH = ROOT / "scrub_key_binding.py"
LEGACY_MODEL_PATH = ROOT / "scrub_key.py"
UI_PATH = ROOT / "reinsert_mode_ui.py"


def load_fixture() -> dict:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def key_variant(name: str) -> dict:
    fixture = load_fixture()
    if name == "canonical_bound_key":
        return deepcopy(fixture["canonical_bound_key"])
    if name == "legacy_v1_key":
        return deepcopy(fixture["legacy_v1_key"])
    if name == "invalid_digest_key":
        key = deepcopy(fixture["canonical_bound_key"])
        key["mapping_digest"] = "0" * 64
        return key
    if name == "item_binding_mismatch_key":
        key = deepcopy(fixture["canonical_bound_key"])
        key["items"][0]["placeholder"] = "[PERSOON_BP6R3T5VW2XY4ZA7C_01]"
        return key
    raise KeyError(name)


def test_injected_binding_id_generation_is_deterministic_and_valid() -> None:
    generated = generate_document_binding_id(b"\x00" * 10)

    assert generated == "BAAAAAAAAAAAAAAAA"
    assert BINDING_ID_RE.fullmatch(generated)
    assert validate_document_binding_id(generated) == []
    assert generate_document_binding_id(b"\x00" * 10) == generated


def test_binding_id_generation_rejects_invalid_injected_bytes() -> None:
    with pytest.raises(TypeError, match="must be bytes"):
        generate_document_binding_id("not-bytes")  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="exactly 10 bytes"):
        generate_document_binding_id(b"too short")


def test_normal_binding_id_generation_stays_inside_contract() -> None:
    generated = generate_document_binding_id()

    assert BINDING_ID_RE.fullmatch(generated)
    assert len(generated) == 17
    assert validate_document_binding_id(generated) == []


def test_binding_id_validation_matches_contract_fixture() -> None:
    fixture = load_fixture()

    assert validate_document_binding_id(fixture["binding_id"]) == []
    assert validate_document_binding_id(fixture["other_binding_id"]) == []
    for invalid in fixture["invalid_binding_ids"]:
        assert validate_document_binding_id(invalid)


def test_build_and_parse_bound_placeholders_match_contract() -> None:
    binding_id = load_fixture()["binding_id"]

    automatic = build_bound_placeholder("PERSOON", 1, binding_id)
    manual = build_bound_placeholder("PERSOON", "1", binding_id, manual=True)
    underscored = build_bound_placeholder("IP_ADRES", 2, binding_id)

    assert automatic == "[PERSOON_BK7M4Q2XR5TD3W6YZ_01]"
    assert manual == "[PERSOON_BK7M4Q2XR5TD3W6YZ_HANDMATIG_01]"
    assert underscored == "[IP_ADRES_BK7M4Q2XR5TD3W6YZ_02]"
    assert BOUND_PLACEHOLDER_RE.fullmatch(automatic)

    assert parse_bound_placeholder(automatic) == {
        "placeholder": automatic,
        "entity_label": "PERSOON",
        "document_binding_id": binding_id,
        "manual": False,
        "index": 1,
        "index_text": "01",
    }
    assert parse_bound_placeholder(manual)["manual"] is True  # type: ignore[index]
    assert parse_bound_placeholder(underscored)["entity_label"] == "IP_ADRES"  # type: ignore[index]


def test_placeholder_builder_rejects_invalid_values_without_guessing() -> None:
    binding_id = load_fixture()["binding_id"]

    with pytest.raises(ValueError, match="entity_label"):
        build_bound_placeholder("persoon", 1, binding_id)
    with pytest.raises(ValueError, match="positive integer"):
        build_bound_placeholder("PERSOON", 0, binding_id)
    with pytest.raises(ValueError, match="positive integer"):
        build_bound_placeholder("PERSOON", True, binding_id)
    with pytest.raises(ValueError, match="Document binding ID"):
        build_bound_placeholder("PERSOON", 1, "invalid")
    with pytest.raises(TypeError, match="manual must be a boolean"):
        build_bound_placeholder("PERSOON", 1, binding_id, manual="yes")  # type: ignore[arg-type]

    for malformed in [
        "[PERSOON_BK7M4Q2XR5TD3W6YZ_1]",
        "[persoon_BK7M4Q2XR5TD3W6YZ_01]",
        "[PERSOON-BK7M4Q2XR5TD3W6YZ-01]",
        "[PERSOON_BK7M4Q2XR5TD3W6YZ_HANDMATIG]",
    ]:
        assert parse_bound_placeholder(malformed) is None


def test_extract_document_binding_ids_is_sorted_unique_and_strict() -> None:
    fixture = load_fixture()
    first = fixture["binding_id"]
    second = fixture["other_binding_id"]
    text = (
        f"[PERSOON_{second}_01] / [DOSSIERNUMMER_{first}_01] / "
        f"[PERSOON_{first}_HANDMATIG_02] / [PERSOON_{first}_1]"
    )

    assert extract_document_binding_ids(text) == sorted([first, second])
    assert extract_document_binding_ids(123) == []


def test_canonical_payload_and_digest_match_frozen_fixture() -> None:
    fixture = load_fixture()
    key = fixture["canonical_bound_key"]

    assert canonical_mapping_digest_payload(key) == fixture["canonical_digest_payload"]
    assert compute_mapping_digest(key) == fixture["expected_mapping_digest"]
    assert compute_mapping_digest(key) == key["mapping_digest"]


def test_digest_is_order_independent_but_semantics_sensitive() -> None:
    fixture = load_fixture()
    original = deepcopy(fixture["canonical_bound_key"])
    reordered = deepcopy(original)
    reordered["items"].reverse()
    metadata_changed = deepcopy(original)
    metadata_changed["document_label"] = "Ander zichtbaar label"
    metadata_changed["items"][0]["type_label"] = "Andere zichtbare tekst"
    semantics_changed = deepcopy(original)
    semantics_changed["items"][0]["original_value"] = "ANDERE-SYNTHETISCHE-WAARDE"

    expected = fixture["expected_mapping_digest"]
    assert compute_mapping_digest(reordered) == expected
    assert compute_mapping_digest(metadata_changed) == expected
    assert compute_mapping_digest(semantics_changed) != expected


def test_digest_helpers_reject_non_mapping_or_invalid_items_without_mutation() -> None:
    fixture = load_fixture()
    key = deepcopy(fixture["canonical_bound_key"])
    before = deepcopy(key)

    assert compute_mapping_digest(key) == fixture["expected_mapping_digest"]
    assert key == before

    with pytest.raises(ValueError, match="must be a mapping"):
        canonical_mapping_digest_payload([])  # type: ignore[arg-type]
    broken = deepcopy(key)
    broken["items"] = "not-a-list"
    with pytest.raises(ValueError, match="items must be a list"):
        compute_mapping_digest(broken)


def test_canonical_bound_key_validates_without_mutation() -> None:
    key = key_variant("canonical_bound_key")
    before = deepcopy(key)

    result = validate_bound_scrub_key(key)

    assert result == {
        "ok": True,
        "errors": [],
        "error_codes": [],
        "warnings": [],
        "key_binding_id": "BK7M4Q2XR5TD3W6YZ",
        "mapping_digest_valid": True,
    }
    assert key == before


def test_bound_key_validation_rejects_digest_and_item_binding_problems() -> None:
    invalid_digest = validate_bound_scrub_key(key_variant("invalid_digest_key"))
    item_mismatch = validate_bound_scrub_key(key_variant("item_binding_mismatch_key"))

    assert invalid_digest["ok"] is False
    assert invalid_digest["error_codes"] == ["invalid_mapping_digest"]
    assert invalid_digest["mapping_digest_valid"] is False
    assert item_mismatch["ok"] is False
    assert "invalid_bound_key" in item_mismatch["error_codes"]
    assert any("does not match document_binding_id" in error for error in item_mismatch["errors"])


def test_bound_key_validation_rejects_invalid_metadata_duplicates_and_policy() -> None:
    fixture = load_fixture()

    invalid_id = deepcopy(fixture["canonical_bound_key"])
    invalid_id["document_binding_id"] = "INVALID"
    invalid_id["mapping_digest"] = compute_mapping_digest(invalid_id)
    assert "invalid_bound_key" in validate_bound_scrub_key(invalid_id)["error_codes"]

    duplicate = deepcopy(fixture["canonical_bound_key"])
    duplicate["items"].append(deepcopy(duplicate["items"][0]))
    duplicate["item_count"] = 3
    duplicate["mapping_digest"] = compute_mapping_digest(duplicate)
    duplicate_result = validate_bound_scrub_key(duplicate)
    assert any("Duplicate bound placeholder" in error for error in duplicate_result["errors"])

    wrong_policy = deepcopy(fixture["canonical_bound_key"])
    wrong_policy["storage_policy"] = "cloud_storage"
    wrong_policy["mapping_digest"] = compute_mapping_digest(wrong_policy)
    assert any("storage_policy" in error for error in validate_bound_scrub_key(wrong_policy)["errors"])


def test_document_key_binding_matches_every_frozen_status_case() -> None:
    fixture = load_fixture()

    for case in fixture["binding_validation_cases"]:
        result = validate_document_key_binding(case["document_text"], key_variant(case["key_variant"]))
        assert result["binding_status"] == case["expected_status"], case["id"]
        assert result["replacement_allowed"] is case["replacement_allowed"], case["id"]
        assert result["verified_document_match"] is case["verified_document_match"], case["id"]
        assert result["legacy_unbound"] is case["legacy_unbound"], case["id"]
        assert set(fixture["required_result_fields"]).issubset(result), case["id"]


def test_bound_match_is_verified_and_digest_valid() -> None:
    key = key_variant("canonical_bound_key")
    text = "[PERSOON_BK7M4Q2XR5TD3W6YZ_01]"

    result = validate_document_key_binding(text, key)

    assert result["ok"] is True
    assert result["binding_status"] == "bound_match"
    assert result["replacement_allowed"] is True
    assert result["verified_document_match"] is True
    assert result["legacy_unbound"] is False
    assert result["document_binding_ids"] == ["BK7M4Q2XR5TD3W6YZ"]
    assert result["key_binding_id"] == "BK7M4Q2XR5TD3W6YZ"
    assert result["mapping_digest_valid"] is True
    assert result["errors"] == []


def test_fail_closed_statuses_never_allow_replacement() -> None:
    fixture = load_fixture()
    fail_closed = {
        "binding_mismatch",
        "mixed_document_bindings",
        "missing_document_binding",
        "invalid_mapping_digest",
        "invalid_bound_key",
        "legacy_key_for_bound_document",
    }

    for case in fixture["binding_validation_cases"]:
        result = validate_document_key_binding(case["document_text"], key_variant(case["key_variant"]))
        if result["binding_status"] in fail_closed:
            assert result["ok"] is False
            assert result["replacement_allowed"] is False
            assert result["verified_document_match"] is False
            assert result["errors"]


def test_legacy_unbound_is_explicit_and_not_a_verified_match() -> None:
    result = validate_document_key_binding("[PERSOON_01]", key_variant("legacy_v1_key"))

    assert result["ok"] is True
    assert result["binding_status"] == "legacy_unbound"
    assert result["replacement_allowed"] is True
    assert result["verified_document_match"] is False
    assert result["legacy_unbound"] is True
    assert result["mapping_digest_valid"] is None
    assert result["warnings"] == [LEGACY_UNBOUND_WARNING]


def test_invalid_or_unsupported_keys_fail_without_guessing() -> None:
    not_a_key = validate_document_key_binding("[PERSOON_01]", [])
    unsupported = key_variant("legacy_v1_key")
    unsupported["schema_version"] = "9.9"
    unsupported_result = validate_document_key_binding("[PERSOON_01]", unsupported)

    assert not_a_key["binding_status"] == "invalid_bound_key"
    assert not_a_key["replacement_allowed"] is False
    assert unsupported_result["binding_status"] == "invalid_bound_key"
    assert unsupported_result["replacement_allowed"] is False


def test_model_does_not_mutate_document_or_key_inputs() -> None:
    key = key_variant("canonical_bound_key")
    text = "[PERSOON_BK7M4Q2XR5TD3W6YZ_01]"
    key_before = deepcopy(key)
    text_before = text

    validate_document_key_binding(text, key)
    validate_bound_scrub_key(key)
    compute_mapping_digest(key)

    assert key == key_before
    assert text == text_before


def test_model_is_streamlit_free_and_has_no_network_or_file_side_effects() -> None:
    tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
    imported_roots: set[str] = set()
    function_names = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])

    for forbidden in ["streamlit", "requests", "httpx", "openai", "anthropic", "pathlib", "os"]:
        assert forbidden not in imported_roots
    for forbidden_function in ["open", "write_text", "write_bytes", "unlink", "remove"]:
        assert forbidden_function not in function_names


def test_model_package_does_not_integrate_current_export_or_reinsert_paths() -> None:
    legacy_model = LEGACY_MODEL_PATH.read_text(encoding="utf-8")
    ui = UI_PATH.read_text(encoding="utf-8")

    assert 'SCRUB_KEY_SCHEMA_VERSION = "1.0"' in legacy_model
    assert "from scrub_key_binding import" not in legacy_model
    assert "from scrub_key_binding import" not in ui
    assert "document_binding_id" not in ui
