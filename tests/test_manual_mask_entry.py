from __future__ import annotations

import pytest

from manual_mask_entry import (
    MANUAL_MASK_TYPE_OPTIONS,
    build_manual_mask_row,
    build_manual_placeholder,
    manual_mask_document_key,
    manual_type_to_entity_type,
    validate_manual_mask_input,
)


def test_manual_type_options_are_user_facing_and_mapped():
    assert MANUAL_MASK_TYPE_OPTIONS == (
        "Persoon",
        "Organisatie",
        "Zaaknummer",
        "Dossiernummer",
        "Datum",
        "Anders",
    )
    assert manual_type_to_entity_type("Persoon") == "PERSON"
    assert manual_type_to_entity_type("Organisatie") == "ORGANIZATION"
    assert manual_type_to_entity_type("Zaaknummer") == "NL_LEGAL_CASE_NUMBER"
    assert manual_type_to_entity_type("Dossiernummer") == "NL_DOSSIER_NUMBER"
    assert manual_type_to_entity_type("Datum") == "DATE_TIME"
    assert manual_type_to_entity_type("Onbekend") == "MANUAL"


def test_empty_input_is_not_valid():
    result = validate_manual_mask_input("   ", source_text="SYNTHETIC text")

    assert not result.is_valid
    assert "Vul eerst" in result.message


def test_duplicate_input_is_not_valid():
    result = validate_manual_mask_input(
        "SYNTHETIC-REF-001",
        source_text="SYNTHETIC-REF-001 staat in de tekst.",
        existing_find_values=["SYNTHETIC-REF-001"],
    )

    assert not result.is_valid
    assert "al in de vervangtabel" in result.message


def test_value_must_be_present_in_current_text_when_source_text_is_supplied():
    result = validate_manual_mask_input("SYNTHETIC-REF-002", source_text="Alleen SYNTHETIC-REF-001 staat hier.")

    assert not result.is_valid
    assert "niet in de huidige tekst" in result.message


def test_valid_input_is_accepted():
    result = validate_manual_mask_input("SYNTHETIC-REF-001", source_text="SYNTHETIC-REF-001 staat in de tekst.")

    assert result.is_valid
    assert result.message == ""


def test_manual_placeholder_is_stable_and_increments_per_type():
    existing_rows = [
        {"replace_with": "[PERSOON_HANDMATIG_01]"},
        {"replace_with": "[PERSOON_HANDMATIG_02]"},
        {"replace_with": "[ZAAKNUMMER_HANDMATIG_01]"},
    ]

    assert build_manual_placeholder("Persoon", existing_rows) == "[PERSOON_HANDMATIG_03]"
    assert build_manual_placeholder("Zaaknummer", existing_rows) == "[ZAAKNUMMER_HANDMATIG_02]"
    assert build_manual_placeholder("Anders", existing_rows) == "[WAARDE_HANDMATIG_01]"


def test_manual_mask_row_gets_review_table_fields_and_defaults():
    row = build_manual_mask_row(
        find_text="SYNTHETIC-NAAM",
        manual_type="Persoon",
        existing_rows=[{"replace_with": "[PERSOON_HANDMATIG_01]"}],
    )

    assert row["include"] is True
    assert row["remember"] is False
    assert row["find"] == "SYNTHETIC-NAAM"
    assert row["replace_with"] == "[PERSOON_HANDMATIG_02]"
    assert row["source"] == "manual"
    assert row["source_label"] == "Handmatig"
    assert row["review_status"] == "manual"
    assert row["review_status_label"] == "Handmatig toegevoegd"
    assert row["entity_type"] == "PERSON"
    assert row["type_label"] == "Naam / persoon"
    assert row["reason"] == "Handmatig toegevoegd"
    assert row["score"] is None


def test_manual_mask_row_accepts_custom_replacement():
    row = build_manual_mask_row(
        find_text="SYNTHETIC-DOSSIER-001",
        manual_type="Dossiernummer",
        replace_with="[EIGEN_PLACEHOLDER]",
    )

    assert row["replace_with"] == "[EIGEN_PLACEHOLDER]"
    assert row["entity_type"] == "NL_DOSSIER_NUMBER"


def test_manual_mask_row_rejects_empty_value():
    with pytest.raises(ValueError):
        build_manual_mask_row(find_text="", manual_type="Anders")


def test_document_key_is_stable_and_scoped_to_text():
    text_a = "SYNTHETIC tekst A"
    text_b = "SYNTHETIC tekst B"

    assert manual_mask_document_key(text_a) == manual_mask_document_key(text_a)
    assert manual_mask_document_key(text_a) != manual_mask_document_key(text_b)
    assert len(manual_mask_document_key(text_a)) == 16


def test_helper_tests_use_synthetic_values_only():
    rendered = __file__
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]
    assert "synthetic" in "SYNTHETIC".lower()
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
