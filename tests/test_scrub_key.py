from scrub_key import (
    REQUIRED_ITEM_FIELDS,
    build_scrub_key,
    scrub_key_from_json,
    scrub_key_to_json,
    validate_scrub_key,
)


VALID_SYNTHETIC_ROWS = [
    {
        "original_value": "BETROKKENE-TEST-A",
        "placeholder": "[PERSOON_1]",
        "entity_type": "PERSON",
        "type_label": "Naam",
        "source": "detected",
        "review_status": "auto_detected",
        "include": True,
        "timestamp": "2026-06-07T10:00:00Z",
    },
    {
        "Gevonden tekst": "ZAAK-TEST-2026-001",
        "Vervangen door": "[ZAAKNUMMER_1]",
        "entity_type": "LEGAL_REFERENCE",
        "Type gegeven": "Zaaknummer",
        "source": "manual",
        "Status": "Handmatig toegevoegd",
        "Meenemen": "ja",
        "timestamp": "2026-06-07T10:05:00Z",
    },
]


def test_build_scrub_key_creates_valid_key_from_reviewed_rows():
    scrub_key = build_scrub_key(VALID_SYNTHETIC_ROWS, document_label="Dossier voorbeeld")

    assert scrub_key["schema"] == "solidprivacy.scrub_key"
    assert scrub_key["schema_version"] == "1.0"
    assert scrub_key["workflow"] == "Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit"
    assert scrub_key["privacy_model"] == "pseudonymization_not_full_anonymization"
    assert scrub_key["reversible"] is True
    assert scrub_key["document_label"] == "Dossier voorbeeld"
    assert scrub_key["item_count"] == 2
    assert validate_scrub_key(scrub_key) == []


def test_excluded_rows_are_omitted_according_to_spec():
    rows = VALID_SYNTHETIC_ROWS + [
        {
            "original_value": "VOORBEELD-REFERENTIE-UITGESLOTEN",
            "placeholder": "[REFERENTIE_2]",
            "entity_type": "LEGAL_REFERENCE",
            "type_label": "Referentie",
            "source": "candidate",
            "review_status": "needs_review",
            "include": False,
            "timestamp": "2026-06-07T10:10:00Z",
        }
    ]

    scrub_key = build_scrub_key(rows, document_label="Dossier voorbeeld")
    exported_originals = {item["original_value"] for item in scrub_key["items"]}

    assert scrub_key["excluded_rows_policy"] == "omitted"
    assert scrub_key["item_count"] == 2
    assert "VOORBEELD-REFERENTIE-UITGESLOTEN" not in exported_originals


def test_required_fields_exist_on_each_mapping_item():
    scrub_key = build_scrub_key(VALID_SYNTHETIC_ROWS, document_label="Dossier voorbeeld")

    for item in scrub_key["items"]:
        assert set(REQUIRED_ITEM_FIELDS).issubset(item.keys())
        assert item["include_state"] == "included"
        assert item["document_label"] == "Dossier voorbeeld"


def test_json_roundtrip_preserves_scrub_key():
    scrub_key = build_scrub_key(VALID_SYNTHETIC_ROWS, document_label="Dossier voorbeeld")

    json_text = scrub_key_to_json(scrub_key)
    loaded = scrub_key_from_json(json_text)

    assert loaded == scrub_key
    assert validate_scrub_key(loaded) == []


def test_validation_catches_missing_required_fields():
    scrub_key = build_scrub_key(VALID_SYNTHETIC_ROWS, document_label="Dossier voorbeeld")
    del scrub_key["items"][0]["placeholder"]
    scrub_key["items"][1]["timestamp"] = ""

    issues = validate_scrub_key(scrub_key)

    assert any("placeholder" in issue for issue in issues)
    assert any("timestamp" in issue for issue in issues)


def test_examples_use_synthetic_dutch_legal_values_only():
    scrub_key = build_scrub_key(VALID_SYNTHETIC_ROWS, document_label="Dossier voorbeeld")
    json_text = scrub_key_to_json(scrub_key)

    assert "BETROKKENE-TEST-A" in json_text
    assert "ZAAK-TEST-2026-001" in json_text
    assert "Dossier voorbeeld" in json_text
    assert "Jan Jansen" not in json_text
    assert "Piet de Vries" not in json_text
