from __future__ import annotations

from copy import deepcopy

from scrub_key import (
    build_scrub_key,
    scrub_key_from_json,
    scrub_key_to_json,
    validate_scrub_key,
)
from scrub_key_import import (
    IMPORT_PRIVACY_WARNING,
    build_scrub_key_import_result,
    validate_scrub_key_import_text,
)
from scrub_key_reinsert import build_reinsert_mapping, reinsert_from_scrub_key


SYNTHETIC_ROWS = [
    {
        "original_value": "BETROKKENE-TEST-A",
        "placeholder": "[PERSOON_1]",
        "entity_type": "PERSON",
        "type_label": "Naam",
        "source": "detected",
        "review_status": "auto_detected",
        "include": True,
        "timestamp": "2026-06-10T09:00:00Z",
    },
    {
        "original_value": "DOSSIER-TEST-2026-001",
        "placeholder": "[DOSSIER_1]",
        "entity_type": "LEGAL_REFERENCE",
        "type_label": "Dossiernummer",
        "source": "manual",
        "review_status": "manual",
        "include": True,
        "timestamp": "2026-06-10T09:05:00Z",
    },
]


FORBIDDEN_LIFECYCLE_OR_RECOVERY_FIELDS = {
    "expires_at",
    "delete_after",
    "deleted_at",
    "auto_delete",
    "hidden_recovery",
    "recovery_copy",
    "recovery_token",
}


def _valid_scrub_key() -> dict:
    return build_scrub_key(SYNTHETIC_ROWS, document_label="WP29 synthetisch testdossier")


def test_scrub_key_export_is_deterministic_and_carries_safety_policy_markers():
    scrub_key = _valid_scrub_key()

    first_json = scrub_key_to_json(scrub_key)
    second_json = scrub_key_to_json(scrub_key)
    restored = scrub_key_from_json(first_json)

    assert first_json == second_json
    assert validate_scrub_key(restored) == []
    assert restored["privacy_model"] == "pseudonymization_not_full_anonymization"
    assert restored["reversible"] is True
    assert restored["storage_policy"] == "local_only_protect_key"
    assert restored["external_ai_policy"] == "do_not_share_key_unless_explicitly_intended_and_allowed"
    assert restored["excluded_rows_policy"] == "omitted"
    assert not FORBIDDEN_LIFECYCLE_OR_RECOVERY_FIELDS.intersection(restored.keys())


def test_valid_import_roundtrip_is_local_visible_and_warning_only():
    result = build_scrub_key_import_result(scrub_key_to_json(_valid_scrub_key()))

    assert result["ok"] is True
    assert result["errors"] == []
    assert result["warnings"] == [IMPORT_PRIVACY_WARNING]
    assert result["item_count"] == 2
    assert result["reversible"] is True
    assert result["privacy_model"] == "pseudonymization_not_full_anonymization"
    assert result["mapping_rows"][0]["original_value"] == "BETROKKENE-TEST-A"
    assert result["mapping_rows"][0]["placeholder"] == "[PERSOON_1]"


def test_malformed_json_import_fails_closed_without_mapping_rows():
    result = build_scrub_key_import_result("{this is not json")

    assert result["ok"] is False
    assert result["mapping_rows"] == []
    assert result["item_count"] == 0
    assert result["reversible"] is False
    assert result["warnings"] == [IMPORT_PRIVACY_WARNING]
    assert any("geen geldige JSON" in error for error in result["errors"])
    assert "BETROKKENE-TEST-A" not in " ".join(result["errors"])


def test_non_object_json_import_is_rejected_safely():
    errors = validate_scrub_key_import_text("[]")

    assert errors
    assert any("ongeldig hoofdformaat" in error for error in errors)


def test_missing_required_item_field_is_rejected_without_normalised_rows():
    scrub_key = _valid_scrub_key()
    del scrub_key["items"][0]["timestamp"]

    result = build_scrub_key_import_result(scrub_key_to_json(scrub_key))

    assert result["ok"] is False
    assert result["mapping_rows"] == []
    assert any("timestamp" in error for error in result["errors"])


def test_invalid_items_structure_is_rejected():
    scrub_key = _valid_scrub_key()
    scrub_key["items"] = {"placeholder": "[PERSOON_1]"}
    scrub_key["item_count"] = 1

    result = build_scrub_key_import_result(scrub_key_to_json(scrub_key))

    assert result["ok"] is False
    assert result["mapping_rows"] == []
    assert any("items list" in error for error in result["errors"])


def test_wrong_policy_markers_are_rejected_without_schema_migration():
    scrub_key = _valid_scrub_key()
    scrub_key["reversible"] = False
    scrub_key["privacy_model"] = "anonymization"
    scrub_key["excluded_rows_policy"] = "included_as_inactive"

    result = build_scrub_key_import_result(scrub_key_to_json(scrub_key))
    joined_errors = " ".join(result["errors"])

    assert result["ok"] is False
    assert "reversible=true" in joined_errors
    assert "pseudonymization" in joined_errors
    assert "excluded_rows_policy=omitted" in joined_errors


def test_duplicate_placeholder_tampering_is_reported_and_not_reinserted():
    scrub_key = _valid_scrub_key()
    duplicate = dict(scrub_key["items"][0])
    duplicate["original_value"] = "BETROKKENE-TEST-B"
    scrub_key["items"].append(duplicate)
    scrub_key["item_count"] = len(scrub_key["items"])

    mapping_result = build_reinsert_mapping(scrub_key)
    result = reinsert_from_scrub_key("Controle [PERSOON_1].", scrub_key)

    assert mapping_result["duplicate_placeholders"] == ["[PERSOON_1]"]
    assert "[PERSOON_1]" not in mapping_result["mapping"]
    assert result["text"] == "Controle [PERSOON_1]."
    assert "BETROKKENE-TEST-A" not in result["text"]
    assert "BETROKKENE-TEST-B" not in result["text"]
    assert result["duplicate_placeholders"] == ["[PERSOON_1]"]
    assert result["replacement_count"] == 0


def test_mismatch_unknown_placeholder_is_visible_and_not_guessed():
    result = reinsert_from_scrub_key("Tekst met onbekende [ONBEKEND_1].", _valid_scrub_key())

    assert result["text"] == "Tekst met onbekende [ONBEKEND_1]."
    assert result["unknown_placeholders"] == ["[ONBEKEND_1]"]
    assert result["replacement_count"] == 0


def test_old_timestamp_is_not_expiry_blocked_or_deleted_by_helpers():
    scrub_key = _valid_scrub_key()
    scrub_key["items"][0]["timestamp"] = "2000-01-01T00:00:00Z"

    result = build_scrub_key_import_result(scrub_key_to_json(scrub_key))

    assert result["ok"] is True
    assert result["errors"] == []
    assert result["item_count"] == 2
    assert result["scrub_key"]["items"][0]["timestamp"] == "2000-01-01T00:00:00Z"


def test_helpers_do_not_add_hidden_recovery_deletion_or_expiry_state():
    imported = build_scrub_key_import_result(scrub_key_to_json(_valid_scrub_key()))["scrub_key"]

    assert not FORBIDDEN_LIFECYCLE_OR_RECOVERY_FIELDS.intersection(imported.keys())
    for item in imported["items"]:
        assert not FORBIDDEN_LIFECYCLE_OR_RECOVERY_FIELDS.intersection(item.keys())


def test_import_and_reinsert_helpers_do_not_mutate_scrub_key():
    scrub_key = _valid_scrub_key()
    original = deepcopy(scrub_key)

    build_scrub_key_import_result(scrub_key_to_json(scrub_key))
    reinsert_from_scrub_key("[PERSOON_1]", scrub_key)

    assert scrub_key == original


def test_reinsert_remains_local_deterministic_no_ai_no_cloud():
    first = reinsert_from_scrub_key("[PERSOON_1] / [DOSSIER_1]", _valid_scrub_key())
    second = reinsert_from_scrub_key("[PERSOON_1] / [DOSSIER_1]", _valid_scrub_key())

    assert first == second
    assert first["local_only"] is True
    assert first["ai_processing"] is False
    assert first["cloud_processing"] is False
    assert first["text"] == "BETROKKENE-TEST-A / DOSSIER-TEST-2026-001"


def test_examples_use_synthetic_values_only():
    exported = scrub_key_to_json(_valid_scrub_key())

    assert "BETROKKENE-TEST-A" in exported
    assert "DOSSIER-TEST-2026-001" in exported
    assert "Jan Jansen" not in exported
    assert "Piet de Vries" not in exported
    assert "123456782" not in exported
