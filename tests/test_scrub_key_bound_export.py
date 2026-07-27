from __future__ import annotations

from copy import deepcopy
from types import SimpleNamespace

from document_tools import build_placeholder_replacements, placeholder_for_entity
from manual_mask_entry import build_manual_mask_row, build_manual_placeholder
from scrub_key_binding import parse_bound_placeholder, validate_bound_scrub_key
from scrub_key_bound_export import (
    bind_existing_placeholder,
    build_bound_scrub_key,
    document_binding_id_for_scope,
)


BINDING_ID = "BK7M4Q2XR5TD3W6YZ"
OTHER_BINDING_ID = "BABCDEFGHIJKLMNOP"


def reviewed_rows() -> list[dict]:
    return [
        {
            "find": "BETROKKENE-TEST-A",
            "replace_with": f"[PERSOON_{BINDING_ID}_01]",
            "entity_type": "PERSON",
            "type_label": "Naam / persoon",
            "source": "detected",
            "review_status": "auto",
            "include": True,
            "timestamp": "2026-07-27T19:00:00Z",
        },
        {
            "find": "DOSSIER-TEST-2026-001",
            "replace_with": f"[DOSSIERNUMMER_{BINDING_ID}_HANDMATIG_01]",
            "entity_type": "NL_DOSSIER_NUMBER",
            "type_label": "Dossiernummer",
            "source": "manual",
            "review_status": "manual",
            "include": True,
            "timestamp": "2026-07-27T19:00:00Z",
        },
    ]


def test_document_binding_id_is_stable_per_scope_and_local() -> None:
    state: dict = {}
    first = document_binding_id_for_scope(
        state, "scope-a", random_bytes=b"0123456789"
    )
    second = document_binding_id_for_scope(
        state, "scope-a", random_bytes=b"abcdefghij"
    )
    other = document_binding_id_for_scope(
        state, "scope-b", random_bytes=b"abcdefghij"
    )
    assert first == second
    assert other != first
    assert parse_bound_placeholder(f"[PERSOON_{first}_01]") is not None


def test_existing_legacy_and_bound_placeholders_rebind_losslessly() -> None:
    assert bind_existing_placeholder("[PERSOON_01]", BINDING_ID) == (
        f"[PERSOON_{BINDING_ID}_01]"
    )
    assert bind_existing_placeholder("[PERSOON_HANDMATIG_02]", BINDING_ID) == (
        f"[PERSOON_{BINDING_ID}_HANDMATIG_02]"
    )
    assert bind_existing_placeholder(
        f"[IP_ADRES_{OTHER_BINDING_ID}_03]", BINDING_ID
    ) == f"[IP_ADRES_{BINDING_ID}_03]"
    assert bind_existing_placeholder("Synthetisch pseudoniem", BINDING_ID) is None


def test_document_tools_keep_legacy_default_and_support_bound_placeholders() -> None:
    assert placeholder_for_entity("PERSON", 1) == "[PERSOON_01]"
    assert placeholder_for_entity("PERSON", 1, BINDING_ID) == (
        f"[PERSOON_{BINDING_ID}_01]"
    )
    result = SimpleNamespace(start=0, end=17, entity_type="PERSON", score=0.99)
    replacements, report = build_placeholder_replacements(
        "BETROKKENE-TEST-A", [result], document_binding_id=BINDING_ID
    )
    assert replacements == {
        "BETROKKENE-TEST-A": f"[PERSOON_{BINDING_ID}_01]"
    }
    assert report[0]["placeholder"] == f"[PERSOON_{BINDING_ID}_01]"


def test_manual_helper_keeps_legacy_default_and_supports_bound_placeholders() -> None:
    assert build_manual_placeholder("Persoon") == "[PERSOON_HANDMATIG_01]"
    assert build_manual_placeholder(
        "Persoon", document_binding_id=BINDING_ID
    ) == f"[PERSOON_{BINDING_ID}_HANDMATIG_01]"
    row = build_manual_mask_row(
        find_text="BETROKKENE-TEST-A",
        manual_type="Persoon",
        document_binding_id=BINDING_ID,
    )
    assert row["replace_with"] == f"[PERSOON_{BINDING_ID}_HANDMATIG_01]"


def test_bound_scrub_key_export_matches_schema_and_digest_contract() -> None:
    rows = reviewed_rows()
    original = deepcopy(rows)
    key = build_bound_scrub_key(rows, document_binding_id=BINDING_ID)
    validation = validate_bound_scrub_key(key)
    assert rows == original
    assert validation["ok"] is True
    assert key["schema_version"] == "1.1"
    assert key["binding_version"] == "1"
    assert key["document_binding_id"] == BINDING_ID
    assert key["mapping_digest_algorithm"] == "sha256"
    assert len(key["mapping_digest"]) == 64


def test_custom_replacement_remains_unchanged_and_blocks_verified_key() -> None:
    rows = reviewed_rows()
    rows[0]["replace_with"] = "Synthetisch pseudoniem"
    key = build_bound_scrub_key(rows, document_binding_id=BINDING_ID)
    validation = validate_bound_scrub_key(key)
    assert rows[0]["replace_with"] == "Synthetisch pseudoniem"
    assert validation["ok"] is False
    assert "invalid_bound_key" in validation["error_codes"]
