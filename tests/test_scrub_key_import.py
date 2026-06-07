import json

from scrub_key import build_scrub_key, scrub_key_to_json
from scrub_key_import import (
    IMPORT_PRIVACY_WARNING,
    build_scrub_key_import_result,
    normalise_scrub_key_items,
    validate_scrub_key_import_text,
)


VALID_SYNTHETIC_ROWS = [
    {
        "original_value": "BETROKKENE-TEST-IMPORT-A",
        "placeholder": "[PERSOON_1]",
        "entity_type": "PERSON",
        "type_label": "Naam",
        "source": "detected",
        "review_status": "auto_detected",
        "include": True,
        "timestamp": "2026-06-07T11:00:00Z",
    },
    {
        "original_value": "ZAAK-TEST-IMPORT-2026-001",
        "placeholder": "[ZAAKNUMMER_1]",
        "entity_type": "LEGAL_REFERENCE",
        "type_label": "Zaaknummer",
        "source": "manual",
        "review_status": "manual",
        "include": True,
        "timestamp": "2026-06-07T11:05:00Z",
    },
]


def _valid_scrub_key_json():
    scrub_key = build_scrub_key(VALID_SYNTHETIC_ROWS, document_label="Import testdossier")
    return scrub_key_to_json(scrub_key)


def test_import_result_accepts_valid_scrub_key_json_and_normalises_rows():
    result = build_scrub_key_import_result(_valid_scrub_key_json())

    assert result["ok"] is True
    assert result["errors"] == []
    assert result["item_count"] == 2
    assert result["reversible"] is True
    assert result["privacy_model"] == "pseudonymization_not_full_anonymization"
    assert result["document_label"] == "Import testdossier"

    first_row = result["mapping_rows"][0]
    assert first_row["find"] == "BETROKKENE-TEST-IMPORT-A"
    assert first_row["replace_with"] == "[PERSOON_1]"
    assert first_row["original_value"] == "BETROKKENE-TEST-IMPORT-A"
    assert first_row["placeholder"] == "[PERSOON_1]"
    assert first_row["include"] is True


def test_import_result_contains_local_key_privacy_warning():
    result = build_scrub_key_import_result(_valid_scrub_key_json())

    assert IMPORT_PRIVACY_WARNING in result["warnings"]
    assert "lokaal herleidbaar" in result["warnings"][0]
    assert "AI-diensten" in result["warnings"][0]


def test_validate_import_text_returns_safe_error_for_empty_text():
    errors = validate_scrub_key_import_text("  ")

    assert errors == ["Scrub Key JSON ontbreekt of is leeg."]


def test_validate_import_text_returns_safe_error_for_invalid_json():
    errors = validate_scrub_key_import_text("{niet-json")

    assert errors == ["Scrub Key JSON is geen geldige JSON."]


def test_validate_import_text_returns_error_for_invalid_top_level_format():
    errors = validate_scrub_key_import_text("[]")

    assert errors
    assert errors[0].startswith("Scrub Key JSON heeft een ongeldig hoofdformaat:")


def test_import_result_reports_structural_validation_errors_without_mapping_rows():
    scrub_key = json.loads(_valid_scrub_key_json())
    scrub_key["items"][0]["timestamp"] = ""

    result = build_scrub_key_import_result(json.dumps(scrub_key))

    assert result["ok"] is False
    assert result["mapping_rows"] == []
    assert result["item_count"] == 0
    assert any("timestamp" in error for error in result["errors"])
    assert IMPORT_PRIVACY_WARNING in result["warnings"]


def test_normalise_scrub_key_items_does_not_mutate_input_key():
    scrub_key = build_scrub_key(VALID_SYNTHETIC_ROWS, document_label="Import testdossier")
    original_first_item = dict(scrub_key["items"][0])

    rows = normalise_scrub_key_items(scrub_key)

    assert rows[0]["find"] == original_first_item["original_value"]
    assert scrub_key["items"][0] == original_first_item


def test_import_examples_use_synthetic_dutch_legal_values_only():
    result = build_scrub_key_import_result(_valid_scrub_key_json())
    imported_text = json.dumps(result, ensure_ascii=False)

    assert "BETROKKENE-TEST-IMPORT-A" in imported_text
    assert "ZAAK-TEST-IMPORT-2026-001" in imported_text
    assert "Jan Jansen" not in imported_text
    assert "Piet de Vries" not in imported_text
