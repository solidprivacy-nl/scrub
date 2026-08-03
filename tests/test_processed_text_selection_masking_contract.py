from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md"
FIXTURE_PATH = ROOT / "test_cases" / "processed_text_selection_masking" / "contract.json"


def _contract_text() -> str:
    return CONTRACT_PATH.read_text(encoding="utf-8")


def _fixture() -> dict:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def test_contract_is_approved_and_all_exact_only():
    text = _contract_text()
    fixture = _fixture()

    assert "Status: approved implementation contract" in text
    assert "all safe exact occurrences" in text
    assert fixture["scope"] == "all_exact"
    assert "occurrence-specific masking" in text


def test_two_stage_protocol_is_frozen():
    text = _contract_text()
    fixture = _fixture()

    assert fixture["actions"] == {
        "inspect": "inspect_selection",
        "commit": "commit_manual_mask",
    }
    assert "Stage A — inspect selection" in text
    assert "Stage B — commit manual mask" in text
    assert "server-derived occurrence count" in text


def test_payload_and_selection_limits_are_explicit():
    fixture = _fixture()
    limits = fixture["limits"]

    assert limits == {
        "max_payload_utf8_bytes": 8192,
        "max_selection_codepoints": 160,
        "max_selection_lines": 1,
        "replay_event_history": 128,
        "ready_max_occurrences": 5,
        "confirmation_max_occurrences": 20,
    }


def test_event_identifier_and_hash_formats_accept_only_frozen_examples():
    fixture = _fixture()
    formats = fixture["formats"]

    assert re.fullmatch(formats["event_id_regex"], "sel_01J8Y7ZQMRM1VY2R5JQ6E3F2A9")
    assert not re.fullmatch(formats["event_id_regex"], "short")
    assert re.fullmatch(formats["document_scope_key_regex"], "0123456789abcdef")
    assert not re.fullmatch(formats["document_scope_key_regex"], "0123456789ABCDEF")
    assert re.fullmatch(formats["processed_text_hash_regex"], "a" * 64)
    assert formats["offset_unit"] == "utf16_code_units"


def test_occurrence_thresholds_do_not_overlap_or_leave_a_gap():
    fixture = _fixture()
    limits = fixture["limits"]

    ready = range(1, limits["ready_max_occurrences"] + 1)
    confirm = range(
        limits["ready_max_occurrences"] + 1,
        limits["confirmation_max_occurrences"] + 1,
    )

    assert list(ready) == [1, 2, 3, 4, 5]
    assert list(confirm) == list(range(6, 21))
    assert limits["confirmation_max_occurrences"] + 1 == 21
    assert fixture["confirmation_policy"] == {
        "ready": "1_to_5",
        "confirmation_required": "6_to_20",
        "blocked": "more_than_20",
    }


def test_quick_type_keys_and_mappings_are_unique_and_complete():
    fixture = _fixture()
    quick_types = fixture["quick_types"]

    expected_keys = (
        "person",
        "organization",
        "location",
        "email",
        "phone",
        "date_time",
        "reference",
        "other",
    )
    assert tuple(item["key"] for item in quick_types) == expected_keys
    assert len({item["key"] for item in quick_types}) == len(quick_types)
    assert len({item["user_label"] for item in quick_types}) == len(quick_types)
    assert all(item["entity_type"] for item in quick_types)
    assert all(item["placeholder_prefix"] for item in quick_types)


def test_manual_selection_row_contract_preserves_review_authority():
    fixture = _fixture()

    assert fixture["row_contract"] == {
        "include": True,
        "remember": False,
        "source": "manual_selection",
        "source_label": "Handmatig uit tekst",
        "review_status": "manual",
    }
    text = _contract_text()
    assert "review table remains the source of truth and fallback" in text
    assert "existing `Gemiste waarde toevoegen` flow remains available" in text


def test_collision_contract_is_fail_closed():
    fixture = _fixture()
    collision = fixture["collision_policy"]

    assert collision["block_embedded_substrings"] is True
    assert collision["block_exact_duplicate_rows"] is True
    assert collision["block_nested_included_find_values"] is True
    assert collision["block_marked_range_intersection"] is True
    assert set(collision["token_continuation_categories"]) == {
        "unicode_letter",
        "unicode_number",
        "unicode_combining_mark",
        "underscore",
        "hyphen_or_dash",
        "apostrophe",
    }


def test_replay_stale_state_and_single_use_inspection_are_required():
    text = _contract_text()

    assert "Every event ID is processed at most once" in text
    assert "bounded to the most recent 128 event IDs" in text
    assert "A successful commit consumes its inspection ID" in text
    assert "changed source" in text
    assert "No automatic retry may repeat a mutation" in text


def test_accessibility_and_visible_fallback_are_frozen():
    fixture = _fixture()
    text = _contract_text()

    assert fixture["fallbacks"] == {
        "manual_form": "Gemiste waarde toevoegen",
        "visible_action": "Masker selectie",
        "undo": "Ongedaan maken",
    }
    for required in (
        "Shift+F10",
        "Arrow Up/Down",
        "Enter or Space",
        "ARIA live region",
        'role="menu"',
        'role="menuitem"',
    ):
        assert required in text


def test_security_contract_adds_no_external_or_browser_persistence_path():
    fixture = _fixture()
    security = fixture["security"]

    assert security["server_authoritative"] is True
    for key in (
        "external_network_calls",
        "browser_persistence",
        "external_assets",
        "frontend_placeholder_creation",
        "frontend_table_mutation",
        "scrub_key_semantics_changed",
        "export_semantics_changed",
        "reinsert_semantics_changed",
    ):
        assert security[key] is False


def test_contract_authorizes_only_the_pure_action_model_next():
    text = _contract_text()

    assert "This contract authorizes only the next package" in text
    assert "SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL" in text
    assert "must remain Streamlit-free and browser-free" in text
    assert "A component spike starts only after" in text
