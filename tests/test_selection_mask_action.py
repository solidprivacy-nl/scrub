from __future__ import annotations

import json
from pathlib import Path

import pytest

from manual_mask_entry import build_manual_mask_row, manual_mask_document_key, manual_type_to_entity_type
from selection_mask_action import (
    ALLOWED_TYPE_KEYS,
    QUICK_MASK_TYPE_BY_KEY,
    SelectionActionState,
    commit_manual_mask,
    embedded_occurrence_ranges,
    evaluate_selection,
    find_exact_occurrences,
    inspect_selection,
    is_token_continuation,
    parse_commit_event,
    parse_inspect_event,
    processed_text_hash,
    python_index_to_utf16_offset,
    replacement_conflict,
    replacement_state_hash,
    undo_manual_selection_action,
    utf16_offset_to_index,
    utf16_range_to_indices,
)


SCOPE = "0123456789abcdef"
BINDING_ID = "BAAAAAAAAAAAAAAAA"
VALUE = "SYNTHETIC-ALFA"
BASE_TEXT = f"Voor {VALUE} staat synthetische context. Na {VALUE} volgt meer context."


def inspect_event(
    processed_text: str = BASE_TEXT,
    selection_text: str = VALUE,
    *,
    occurrence_index: int = 0,
    event_id: str = "inspect_event_0001",
    scope: str = SCOPE,
    current_hash: str | None = None,
    intersects_marked_content: bool = False,
    start_override: int | None = None,
    end_override: int | None = None,
) -> dict:
    starts = []
    cursor = 0
    while True:
        found = processed_text.find(selection_text, cursor)
        if found < 0:
            break
        starts.append(found)
        cursor = found + len(selection_text)
    start = starts[occurrence_index] if starts else 0
    end = start + len(selection_text)
    start_utf16 = python_index_to_utf16_offset(processed_text, start)
    end_utf16 = python_index_to_utf16_offset(processed_text, end)
    return {
        "schema_version": 1,
        "action": "inspect_selection",
        "event_id": event_id,
        "document_scope_key": scope,
        "processed_text_hash": current_hash or processed_text_hash(processed_text),
        "selection": {
            "text": selection_text,
            "start_utf16": start_utf16 if start_override is None else start_override,
            "end_utf16": end_utf16 if end_override is None else end_override,
            "intersects_marked_content": intersects_marked_content,
        },
        "ui_state": {
            "source_scroll_ratio": 0.25,
            "processed_scroll_ratio": 0.5,
        },
    }


def commit_event(
    inspection_id: str,
    *,
    event_id: str = "commit_event_0001",
    requested_type: str = "person",
    confirmation_token: str = "",
    requested_scope: str = "all_exact",
) -> dict:
    return {
        "schema_version": 1,
        "action": "commit_manual_mask",
        "event_id": event_id,
        "inspection_id": inspection_id,
        "requested_type": requested_type,
        "requested_scope": requested_scope,
        "confirmation_token": confirmation_token,
    }


def inspect_ready(
    *,
    source_text: str = BASE_TEXT,
    processed_text: str = BASE_TEXT,
    existing_rows=(),
    state: SelectionActionState | None = None,
    event_id: str = "inspect_event_0001",
    selection_text: str = VALUE,
    occurrence_index: int = 0,
    inspection_id: str = "inspection_test_0001",
    confirmation_token: str = "confirmation_test_0001",
    marked_ranges=(),
):
    active_state = state or SelectionActionState()
    result = inspect_selection(
        inspect_event(
            processed_text,
            selection_text,
            occurrence_index=occurrence_index,
            event_id=event_id,
        ),
        source_text=source_text,
        processed_text=processed_text,
        current_document_scope_key=SCOPE,
        existing_rows=existing_rows,
        marked_ranges=marked_ranges,
        document_binding_id=BINDING_ID,
        state=active_state,
        inspection_id_factory=lambda: inspection_id,
        confirmation_token_factory=lambda: confirmation_token,
    )
    return active_state, result


def repeated_source(count: int, value: str = VALUE) -> str:
    return " | ".join([value] * count)


def test_action_model_module_is_streamlit_and_browser_free():
    source = (Path(__file__).resolve().parents[1] / "selection_mask_action.py").read_text(encoding="utf-8")
    assert "import streamlit" not in source
    assert "components.html" not in source
    assert "components.declare_component" not in source
    assert "localstorage" not in source.lower()


def test_hidden_manual_labels_extend_mapping_without_changing_current_form_options():
    assert manual_type_to_entity_type("Adres of locatie") == "LOCATION"
    assert manual_type_to_entity_type("E-mailadres") == "EMAIL_ADDRESS"
    assert manual_type_to_entity_type("Telefoonnummer") == "NL_PHONE_NUMBER"
    assert manual_type_to_entity_type("Datum of tijd") == "DATE_TIME"
    assert manual_type_to_entity_type("Nummer of referentie") == "NL_OTHER_REFERENCE"
    assert manual_type_to_entity_type("Overige waarde") == "MANUAL"


def test_quick_type_contract_is_complete_and_unique():
    assert ALLOWED_TYPE_KEYS == (
        "person",
        "organization",
        "location",
        "email",
        "phone",
        "date_time",
        "reference",
        "other",
    )
    assert len(QUICK_MASK_TYPE_BY_KEY) == len(ALLOWED_TYPE_KEYS)
    assert QUICK_MASK_TYPE_BY_KEY["reference"].placeholder_prefix == "OVERIGE_REFERENTIE"


def test_inspect_parser_accepts_unknown_fields_but_freezes_known_values():
    event = inspect_event()
    event["future_field"] = {"ignored": True}
    parsed = parse_inspect_event(event)
    assert parsed.event_id == "inspect_event_0001"
    assert parsed.selection_text == VALUE
    assert parsed.source_scroll_ratio == 0.25
    assert parsed.processed_scroll_ratio == 0.5


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("schema_version", True),
        ("schema_version", 2),
        ("action", "unknown_action"),
        ("event_id", "short"),
        ("document_scope_key", "ABCDEF0123456789"),
        ("processed_text_hash", "A" * 64),
    ],
)
def test_inspect_parser_rejects_invalid_envelope_fields(field, value):
    event = inspect_event()
    event[field] = value
    with pytest.raises(ValueError):
        parse_inspect_event(event)


def test_inspect_parser_rejects_payload_over_8192_utf8_bytes():
    event = inspect_event()
    event["padding"] = "x" * 9000
    with pytest.raises(ValueError):
        parse_inspect_event(event)


def test_inspect_parser_rejects_bool_offsets_and_invalid_scroll_ratio():
    event = inspect_event()
    event["selection"]["start_utf16"] = True
    with pytest.raises(ValueError):
        parse_inspect_event(event)

    event = inspect_event()
    event["ui_state"]["processed_scroll_ratio"] = 1.01
    with pytest.raises(ValueError):
        parse_inspect_event(event)


def test_commit_parser_rejects_unknown_type_scope_and_long_token():
    with pytest.raises(ValueError):
        parse_commit_event(commit_event("inspection_test_0001", requested_type="unknown"))
    with pytest.raises(ValueError):
        parse_commit_event(commit_event("inspection_test_0001", requested_scope="one_only"))
    with pytest.raises(ValueError):
        parse_commit_event(commit_event("inspection_test_0001", confirmation_token="x" * 257))


def test_utf16_conversion_handles_bmp_accents_combining_marks_and_supplementary_characters():
    text = "AéE\u0301😀Z"
    offsets = [python_index_to_utf16_offset(text, index) for index in range(len(text) + 1)]
    assert offsets == [0, 1, 2, 3, 4, 6, 7]
    for index, offset in enumerate(offsets):
        assert utf16_offset_to_index(text, offset) == index
    assert utf16_range_to_indices(text, 4, 6) == (4, 5)


def test_utf16_conversion_rejects_split_surrogate_negative_and_out_of_range_offsets():
    text = "A😀Z"
    with pytest.raises(ValueError):
        utf16_offset_to_index(text, 2)
    with pytest.raises(ValueError):
        utf16_offset_to_index(text, -1)
    with pytest.raises(ValueError):
        utf16_offset_to_index(text, 99)


def test_exact_occurrences_are_non_overlapping_and_case_sensitive():
    assert find_exact_occurrences("AAAA", "AA") == ((0, 2), (2, 4))
    assert find_exact_occurrences("ALFA alfa ALFA", "ALFA") == ((0, 4), (10, 14))
    assert find_exact_occurrences("ALFA", "alfa") == ()


@pytest.mark.parametrize(
    "character",
    ["A", "9", "\u0301", "_", "-", "–", "'", "’"],
)
def test_token_continuation_contract(character):
    assert is_token_continuation(character)


@pytest.mark.parametrize("character", [" ", ".", ",", "@", "/"])
def test_non_token_boundaries_are_not_continuations(character):
    assert not is_token_continuation(character)


@pytest.mark.parametrize(
    ("source", "selection"),
    [
        ("SYNTHETIC-ALFABET", "SYNTHETIC-ALFA"),
        ("SYNTHETIC-ALFA-BETA", "SYNTHETIC-ALFA"),
        ("PREFIX'SYNTHETIC", "SYNTHETIC"),
        ("AB123C", "123"),
    ],
)
def test_embedded_occurrence_analysis_blocks_longer_tokens(source, selection):
    ranges = find_exact_occurrences(source, selection)
    assert embedded_occurrence_ranges(source, selection, ranges) == ranges


def test_standalone_occurrence_analysis_allows_punctuation_boundaries():
    source = f"({VALUE}), {VALUE}."
    ranges = find_exact_occurrences(source, VALUE)
    assert embedded_occurrence_ranges(source, VALUE, ranges) == ()


def test_replacement_conflict_blocks_exact_duplicate_regardless_of_include_state():
    issue = replacement_conflict(VALUE, [{"find": VALUE, "include": False}])
    assert issue is not None
    assert issue.code == "duplicate_value"


def test_replacement_conflict_blocks_nested_included_terms_but_not_excluded_terms():
    longer = f"{VALUE}-BETA"
    issue = replacement_conflict(VALUE, [{"find": longer, "include": True}])
    assert issue is not None
    assert issue.code == "nested_replacement_conflict"
    assert replacement_conflict(VALUE, [{"find": longer, "include": False}]) is None


@pytest.mark.parametrize(
    ("selection_text", "expected_code"),
    [
        ("", "invalid_offsets"),
        (" " + VALUE, "outer_whitespace"),
        ("x" * 161, "selection_too_long"),
        ("SYNTHETIC\nALFA", "multiline_selection"),
        ("SYNTHETIC\u200bALFA", "control_character"),
        ("---", "punctuation_only"),
        ("[PERSOON_HANDMATIG_01]", "placeholder_selection"),
        ("[PERSOON_BAAAAAAAAAAAAAAAA_01]", "placeholder_selection"),
    ],
)
def test_evaluation_blocks_invalid_quick_selections(selection_text, expected_code):
    processed = selection_text if selection_text else BASE_TEXT
    if selection_text:
        start = 0
        end = python_index_to_utf16_offset(processed, len(processed))
    else:
        start = 0
        end = 0
    result = evaluate_selection(
        source_text=processed,
        processed_text=processed,
        selection_text=selection_text,
        start_utf16=start,
        end_utf16=end,
    )
    assert result.status == "blocked"
    assert result.issue is not None
    assert result.issue.code == expected_code


def test_evaluation_blocks_selection_text_offset_mismatch():
    result = evaluate_selection(
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        selection_text="SYNTHETIC-BETA",
        start_utf16=python_index_to_utf16_offset(BASE_TEXT, BASE_TEXT.index(VALUE)),
        end_utf16=python_index_to_utf16_offset(BASE_TEXT, BASE_TEXT.index(VALUE) + len(VALUE)),
    )
    assert result.issue.code == "selection_mismatch"


def test_evaluation_blocks_frontend_or_server_marked_range_overlap():
    start = BASE_TEXT.index(VALUE)
    end = start + len(VALUE)
    event_start = python_index_to_utf16_offset(BASE_TEXT, start)
    event_end = python_index_to_utf16_offset(BASE_TEXT, end)

    frontend = evaluate_selection(
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        selection_text=VALUE,
        start_utf16=event_start,
        end_utf16=event_end,
        frontend_intersects_marked_content=True,
    )
    server = evaluate_selection(
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        selection_text=VALUE,
        start_utf16=event_start,
        end_utf16=event_end,
        marked_ranges=((start + 1, end),),
    )
    assert frontend.issue.code == "marked_content"
    assert server.issue.code == "marked_content"


def test_evaluation_blocks_embedded_and_nested_values():
    embedded_source = f"{VALUE}BETTER"
    embedded = evaluate_selection(
        source_text=embedded_source,
        processed_text=embedded_source,
        selection_text=VALUE,
        start_utf16=0,
        end_utf16=python_index_to_utf16_offset(embedded_source, len(VALUE)),
    )
    assert embedded.issue.code == "embedded_substring"

    nested = evaluate_selection(
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        selection_text=VALUE,
        start_utf16=python_index_to_utf16_offset(BASE_TEXT, BASE_TEXT.index(VALUE)),
        end_utf16=python_index_to_utf16_offset(BASE_TEXT, BASE_TEXT.index(VALUE) + len(VALUE)),
        existing_rows=[{"find": f"{VALUE} EXTRA", "include": True}],
    )
    assert nested.issue.code == "nested_replacement_conflict"


@pytest.mark.parametrize(
    ("count", "status"),
    [(1, "ready"), (5, "ready"), (6, "confirmation_required"), (20, "confirmation_required")],
)
def test_occurrence_impact_thresholds(count, status):
    text = repeated_source(count)
    result = evaluate_selection(
        source_text=text,
        processed_text=text,
        selection_text=VALUE,
        start_utf16=0,
        end_utf16=python_index_to_utf16_offset(text, len(VALUE)),
    )
    assert result.status == status
    assert result.occurrence_count == count


def test_more_than_twenty_occurrences_are_blocked_with_count():
    text = repeated_source(21)
    result = evaluate_selection(
        source_text=text,
        processed_text=text,
        selection_text=VALUE,
        start_utf16=0,
        end_utf16=python_index_to_utf16_offset(text, len(VALUE)),
    )
    assert result.status == "blocked"
    assert result.issue.code == "too_many_occurrences"
    assert "21" in result.issue.message


def test_inspection_rejects_stale_scope_hash_and_replayed_event():
    state = SelectionActionState()
    stale_scope = inspect_selection(
        inspect_event(scope="fedcba9876543210"),
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        state=state,
    )
    assert stale_scope.issue_code == "stale_document_scope"

    stale_hash = inspect_selection(
        inspect_event(event_id="inspect_event_0002", current_hash="a" * 64),
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        state=state,
    )
    assert stale_hash.issue_code == "stale_processed_text"

    state, first = inspect_ready(state=state, event_id="inspect_event_0003")
    replay = inspect_selection(
        inspect_event(event_id="inspect_event_0003"),
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        state=state,
    )
    assert first.ok
    assert replay.issue_code == "replayed_event"


def test_inspection_result_contains_only_server_owned_impact_and_types():
    state, result = inspect_ready()
    assert result.status == "ready"
    assert result.occurrence_count == 2
    assert result.allowed_types == ALLOWED_TYPE_KEYS
    assert result.confirmation_token == ""
    assert result.record is state.get_inspection("inspection_test_0001")
    rendered = result.to_dict()
    assert rendered["occurrence_count"] == 2
    assert rendered["requested_scope"] == "all_exact"


def test_confirmation_inspection_contains_server_token():
    text = repeated_source(6)
    state, result = inspect_ready(source_text=text, processed_text=text)
    assert result.status == "confirmation_required"
    assert result.confirmation_token == "confirmation_test_0001"
    assert state.get_inspection(result.inspection_id).confirmation_token == result.confirmation_token


def test_inspection_state_bounds_replay_history():
    state = SelectionActionState(max_event_ids=3)
    for event_id in ("event_identifier_01", "event_identifier_02", "event_identifier_03", "event_identifier_04"):
        assert state.record_event(event_id)
    assert state.event_ids == ("event_identifier_02", "event_identifier_03", "event_identifier_04")
    assert not state.has_event("event_identifier_01")
    assert not state.record_event("event_identifier_04")


def test_ready_commit_creates_one_bound_manual_selection_row_and_consumes_inspection():
    state, inspection = inspect_ready()
    result = commit_manual_mask(
        commit_event(inspection.inspection_id, requested_type="organization"),
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        existing_rows=(),
        state=state,
        document_binding_id=BINDING_ID,
        action_id_factory=lambda: "manual_action_test_0001",
    )
    assert result.ok
    row = dict(result.row)
    assert row["find"] == VALUE
    assert row["replace_with"] == "[ORGANISATIE_BAAAAAAAAAAAAAAAA_HANDMATIG_01]"
    assert row["entity_type"] == "ORGANIZATION"
    assert row["source"] == "manual_selection"
    assert row["source_label"] == "Handmatig uit tekst"
    assert row["include"] is True
    assert row["remember"] is False
    assert row["manual_action_id"] == "manual_action_test_0001"
    assert row["selection_occurrence_count"] == 2
    assert state.get_inspection(inspection.inspection_id) is None
    assert result.action_record.row_fingerprint


@pytest.mark.parametrize("type_key", ALLOWED_TYPE_KEYS)
def test_every_quick_type_builds_the_contract_entity_and_prefix(type_key):
    state, inspection = inspect_ready(
        event_id=f"inspect_{type_key}_0001",
        inspection_id=f"inspection_{type_key}_0001",
    )
    result = commit_manual_mask(
        commit_event(
            inspection.inspection_id,
            event_id=f"commit_{type_key}_0001",
            requested_type=type_key,
        ),
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        existing_rows=(),
        state=state,
        document_binding_id=BINDING_ID,
        action_id_factory=lambda key=type_key: f"manual_action_{key}_0001",
    )
    quick_type = QUICK_MASK_TYPE_BY_KEY[type_key]
    assert result.ok
    assert result.row["entity_type"] == quick_type.entity_type
    assert result.row["replace_with"].startswith(f"[{quick_type.placeholder_prefix}_{BINDING_ID}_HANDMATIG_")


def test_confirmation_commit_requires_exact_token_and_masks_all_six():
    text = repeated_source(6)
    state, inspection = inspect_ready(source_text=text, processed_text=text)
    missing = commit_manual_mask(
        commit_event(inspection.inspection_id, requested_type="other"),
        source_text=text,
        processed_text=text,
        current_document_scope_key=SCOPE,
        existing_rows=(),
        state=state,
        document_binding_id=BINDING_ID,
    )
    assert missing.issue_code == "invalid_confirmation"
    assert state.get_inspection(inspection.inspection_id) is None

    state, inspection = inspect_ready(
        source_text=text,
        processed_text=text,
        event_id="inspect_event_retry01",
        inspection_id="inspection_retry_0001",
    )
    committed = commit_manual_mask(
        commit_event(
            inspection.inspection_id,
            event_id="commit_event_retry001",
            requested_type="other",
            confirmation_token=inspection.confirmation_token,
        ),
        source_text=text,
        processed_text=text,
        current_document_scope_key=SCOPE,
        existing_rows=(),
        state=state,
        document_binding_id=BINDING_ID,
        action_id_factory=lambda: "manual_action_retry01",
    )
    assert committed.ok
    assert committed.row["selection_occurrence_count"] == 6


def test_ready_commit_rejects_unexpected_confirmation():
    state, inspection = inspect_ready()
    result = commit_manual_mask(
        commit_event(inspection.inspection_id, confirmation_token="unexpected_token"),
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        existing_rows=(),
        state=state,
        document_binding_id=BINDING_ID,
    )
    assert result.issue_code == "unexpected_confirmation"


@pytest.mark.parametrize(
    ("change", "expected_code"),
    [
        ("scope", "stale_document_scope"),
        ("binding", "stale_document_binding"),
        ("processed", "stale_processed_text"),
        ("source", "stale_source_text"),
        ("rows", "stale_replacement_table"),
    ],
)
def test_commit_revalidates_all_server_owned_state(change, expected_code):
    state, inspection = inspect_ready()
    source = BASE_TEXT
    processed = BASE_TEXT
    scope = SCOPE
    binding = BINDING_ID
    rows = ()
    if change == "scope":
        scope = "fedcba9876543210"
    elif change == "binding":
        binding = "BBBBBBBBBBBBBBBBB"
    elif change == "processed":
        processed = BASE_TEXT + " gewijzigd"
    elif change == "source":
        source = BASE_TEXT + " gewijzigd"
    elif change == "rows":
        rows = ({"find": "SYNTHETIC-BETA", "replace_with": "[WAARDE_01]", "include": True},)

    result = commit_manual_mask(
        commit_event(inspection.inspection_id),
        source_text=source,
        processed_text=processed,
        current_document_scope_key=scope,
        existing_rows=rows,
        state=state,
        document_binding_id=binding,
    )
    assert result.issue_code == expected_code
    assert state.get_inspection(inspection.inspection_id) is None


def test_commit_event_replay_does_not_duplicate_a_row():
    state, inspection = inspect_ready()
    event = commit_event(inspection.inspection_id)
    first = commit_manual_mask(
        event,
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        existing_rows=(),
        state=state,
        document_binding_id=BINDING_ID,
        action_id_factory=lambda: "manual_action_test_0002",
    )
    replay = commit_manual_mask(
        event,
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        existing_rows=(),
        state=state,
        document_binding_id=BINDING_ID,
    )
    assert first.ok
    assert replay.issue_code == "replayed_event"
    assert replay.row is None


def test_missing_or_consumed_inspection_cannot_commit():
    state = SelectionActionState()
    result = commit_manual_mask(
        commit_event("inspection_missing_0001"),
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        existing_rows=(),
        state=state,
        document_binding_id=BINDING_ID,
    )
    assert result.issue_code == "missing_inspection"


def test_action_id_is_separate_from_browser_event_ids():
    state, inspection = inspect_ready()
    result = commit_manual_mask(
        commit_event(inspection.inspection_id),
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        existing_rows=(),
        state=state,
        document_binding_id=BINDING_ID,
        action_id_factory=lambda: "manual_action_unique01",
    )
    record = result.action_record
    assert record.action_id == "manual_action_unique01"
    assert record.action_id != record.commit_event_id
    assert record.action_id != record.inspect_event_id


def test_undo_removes_only_the_unchanged_action_row():
    state, inspection = inspect_ready()
    committed = commit_manual_mask(
        commit_event(inspection.inspection_id),
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        existing_rows=(),
        state=state,
        document_binding_id=BINDING_ID,
        action_id_factory=lambda: "manual_action_undo0001",
    )
    unrelated = build_manual_mask_row(find_text="SYNTHETIC-BETA", manual_type="Anders")
    rows = [unrelated, dict(committed.row)]
    undone = undo_manual_selection_action(rows, committed.action_record, current_document_scope_key=SCOPE)
    assert undone.ok
    assert len(undone.rows) == 1
    assert undone.rows[0]["find"] == "SYNTHETIC-BETA"


def test_undo_blocks_wrong_document_changed_row_and_missing_row():
    state, inspection = inspect_ready()
    committed = commit_manual_mask(
        commit_event(inspection.inspection_id),
        source_text=BASE_TEXT,
        processed_text=BASE_TEXT,
        current_document_scope_key=SCOPE,
        existing_rows=(),
        state=state,
        document_binding_id=BINDING_ID,
        action_id_factory=lambda: "manual_action_undo0002",
    )
    row = dict(committed.row)

    wrong_scope = undo_manual_selection_action(
        [row],
        committed.action_record,
        current_document_scope_key="fedcba9876543210",
    )
    assert wrong_scope.issue_code == "wrong_document_scope"

    changed = dict(row)
    changed["include"] = False
    changed_result = undo_manual_selection_action(
        [changed],
        committed.action_record,
        current_document_scope_key=SCOPE,
    )
    assert changed_result.issue_code == "action_row_changed"

    missing = undo_manual_selection_action(
        [],
        committed.action_record,
        current_document_scope_key=SCOPE,
    )
    assert missing.issue_code == "action_row_missing"


def test_replacement_state_hash_is_order_and_state_sensitive_but_deterministic():
    rows = [
        {"include": True, "find": "SYNTHETIC-A", "replace_with": "[WAARDE_01]"},
        {"include": False, "find": "SYNTHETIC-B", "replace_with": "[WAARDE_02]"},
    ]
    first = replacement_state_hash(rows)
    assert first == replacement_state_hash(rows)
    assert first != replacement_state_hash(list(reversed(rows)))
    changed = [dict(row) for row in rows]
    changed[1]["include"] = True
    assert first != replacement_state_hash(changed)


def test_events_and_rows_contain_synthetic_values_only():
    rendered = json.dumps(
        {
            "scope": SCOPE,
            "value": VALUE,
            "base": BASE_TEXT,
            "binding": BINDING_ID,
        },
        ensure_ascii=False,
    )
    assert "SYNTHETIC" in rendered
