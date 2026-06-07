from copy import deepcopy

from scrub_key import build_scrub_key
from scrub_key_reinsert import (
    build_reinsert_mapping,
    detect_placeholders,
    reinsert_from_scrub_key,
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
        "timestamp": "2026-06-07T12:00:00Z",
    },
    {
        "original_value": "ZAAK-TEST-2026-001",
        "placeholder": "[ZAAKNUMMER_1]",
        "entity_type": "LEGAL_REFERENCE",
        "type_label": "Zaaknummer",
        "source": "manual",
        "review_status": "manual",
        "include": True,
        "timestamp": "2026-06-07T12:05:00Z",
    },
    {
        "original_value": "TESTSTRAAT 1, 1000 AA TESTDAM",
        "placeholder": "[ADRES_1]",
        "entity_type": "LOCATION",
        "type_label": "Adres",
        "source": "detected",
        "review_status": "auto_detected",
        "include": True,
        "timestamp": "2026-06-07T12:10:00Z",
    },
]


def _valid_scrub_key():
    return build_scrub_key(VALID_SYNTHETIC_ROWS, document_label="Reinsert testdossier")


def test_valid_reinsert_with_one_placeholder():
    scrub_key = _valid_scrub_key()

    result = reinsert_from_scrub_key("Verzoeker [PERSOON_1] verschijnt ter zitting.", scrub_key)

    assert result["text"] == "Verzoeker BETROKKENE-TEST-A verschijnt ter zitting."
    assert result["replacement_count"] == 1
    assert result["item_count"] == 3
    assert result["active_item_count"] == 3
    assert result["placeholders_not_found"] == ["[ADRES_1]", "[ZAAKNUMMER_1]"]
    assert result["unknown_placeholders"] == []
    assert result["validation_issues"] == []
    assert result["reinserted"] is True


def test_valid_reinsert_with_multiple_placeholders():
    scrub_key = _valid_scrub_key()
    text = "[PERSOON_1] woont op [ADRES_1]. Zaaknummer: [ZAAKNUMMER_1]."

    result = reinsert_from_scrub_key(text, scrub_key)

    assert result["text"] == (
        "BETROKKENE-TEST-A woont op TESTSTRAAT 1, 1000 AA TESTDAM. "
        "Zaaknummer: ZAAK-TEST-2026-001."
    )
    assert result["replacement_count"] == 3
    assert result["placeholders_not_found"] == []
    assert result["reinserted"] is True


def test_reinsert_repeated_placeholder_occurrences_in_text():
    scrub_key = _valid_scrub_key()
    text = "[PERSOON_1] verklaart dat [PERSOON_1] bereikbaar is."

    result = reinsert_from_scrub_key(text, scrub_key)

    assert result["text"] == "BETROKKENE-TEST-A verklaart dat BETROKKENE-TEST-A bereikbaar is."
    assert result["replacement_count"] == 2
    assert result["reinserted"] is True


def test_placeholder_from_key_not_found_in_text_is_reported():
    scrub_key = _valid_scrub_key()

    result = reinsert_from_scrub_key("Geen placeholders in deze tekst.", scrub_key)

    assert result["text"] == "Geen placeholders in deze tekst."
    assert result["replacement_count"] == 0
    assert result["placeholders_not_found"] == ["[ADRES_1]", "[PERSOON_1]", "[ZAAKNUMMER_1]"]
    assert result["reinserted"] is False


def test_text_contains_unknown_placeholder_not_present_in_key():
    scrub_key = _valid_scrub_key()
    text = "Bekende waarde [PERSOON_1], onbekende waarde [ONBEKEND_1]."

    result = reinsert_from_scrub_key(text, scrub_key)

    assert "BETROKKENE-TEST-A" in result["text"]
    assert "[ONBEKEND_1]" in result["text"]
    assert result["unknown_placeholders"] == ["[ONBEKEND_1]"]
    assert result["replacement_count"] == 1


def test_invalid_scrub_key_returns_validation_issues_without_changing_text():
    scrub_key = _valid_scrub_key()
    scrub_key["items"][0]["timestamp"] = ""
    text = "Waarde [PERSOON_1]."

    result = reinsert_from_scrub_key(text, scrub_key)

    assert result["text"] == text
    assert result["replacement_count"] == 0
    assert result["validation_issues"]
    assert any("timestamp" in issue for issue in result["validation_issues"])
    assert result["reinserted"] is False


def test_duplicate_placeholder_entries_are_detected_and_not_reinserted():
    scrub_key = _valid_scrub_key()
    duplicate_item = dict(scrub_key["items"][0])
    duplicate_item["original_value"] = "BETROKKENE-TEST-B"
    scrub_key["items"].append(duplicate_item)
    scrub_key["item_count"] = len(scrub_key["items"])

    mapping_result = build_reinsert_mapping(scrub_key)
    result = reinsert_from_scrub_key("Dubbel: [PERSOON_1].", scrub_key)

    assert mapping_result["duplicate_placeholders"] == ["[PERSOON_1]"]
    assert "[PERSOON_1]" not in mapping_result["mapping"]
    assert result["text"] == "Dubbel: [PERSOON_1]."
    assert result["duplicate_placeholders"] == ["[PERSOON_1]"]
    assert result["replacement_count"] == 0
    assert result["reinserted"] is False


def test_excluded_rows_are_not_reinserted_if_present_in_malformed_or_imported_data():
    scrub_key = _valid_scrub_key()
    scrub_key["items"].append(
        {
            "original_value": "UITGESLOTEN-TEST-WAARDE",
            "placeholder": "[UITGESLOTEN_1]",
            "entity_type": "LEGAL_REFERENCE",
            "type_label": "Referentie",
            "source": "candidate",
            "review_status": "needs_review",
            "include_state": "excluded",
            "timestamp": "2026-06-07T12:20:00Z",
            "document_label": "Reinsert testdossier",
        }
    )
    scrub_key["item_count"] = len(scrub_key["items"])

    result = reinsert_from_scrub_key("Niet terugzetten: [UITGESLOTEN_1].", scrub_key)

    assert result["text"] == "Niet terugzetten: [UITGESLOTEN_1]."
    assert "UITGESLOTEN-TEST-WAARDE" not in result["text"]
    assert result["excluded_item_count"] == 1
    assert result["unknown_placeholders"] == ["[UITGESLOTEN_1]"]
    assert result["replacement_count"] == 0


def test_examples_use_synthetic_dutch_legal_values_only():
    scrub_key = _valid_scrub_key()
    result = reinsert_from_scrub_key("[PERSOON_1] / [ZAAKNUMMER_1] / [ADRES_1]", scrub_key)

    assert "BETROKKENE-TEST-A" in result["text"]
    assert "ZAAK-TEST-2026-001" in result["text"]
    assert "TESTSTRAAT 1, 1000 AA TESTDAM" in result["text"]
    assert "Jan Jansen" not in result["text"]
    assert "Piet de Vries" not in result["text"]


def test_helper_does_not_mutate_input_scrub_key():
    scrub_key = _valid_scrub_key()
    original = deepcopy(scrub_key)

    build_reinsert_mapping(scrub_key)
    reinsert_from_scrub_key("[PERSOON_1]", scrub_key)

    assert scrub_key == original


def test_no_ai_or_cloud_behavior_is_reported():
    scrub_key = _valid_scrub_key()

    result = reinsert_from_scrub_key("[PERSOON_1]", scrub_key)

    assert result["local_only"] is True
    assert result["ai_processing"] is False
    assert result["cloud_processing"] is False


def test_detect_placeholders_is_conservative_and_deterministic():
    text = "[PERSOON_1] [ZAAKNUMMER_1] [geen-placeholder] [PERSOON_1]"

    assert detect_placeholders(text) == ["[PERSOON_1]", "[ZAAKNUMMER_1]"]
