from selection_mask_action import processed_text_hash, python_index_to_utf16_offset
from processed_text_selection_integration import (
    ACTION_STATES_KEY,
    FEEDBACK_KEY,
    INSPECTION_RESULTS_KEY,
    LAST_ACTIONS_KEY,
    MANUAL_ROWS_KEY,
    SCROLL_RESTORE_KEY,
    clear_selection_feedback,
    handle_selection_component_event,
    latest_selection_action,
    selection_action_state,
    selection_feedback,
    selection_inspection_result,
    selection_scroll_restore,
    undo_latest_selection_action,
)


SCOPE = "0123456789abcdef"
BINDING = "ABCDEFGHIJKLMNOP"
SOURCE = "Mevrouw Noor werkt bij Stichting Zorgpunt. Stichting Zorgpunt helpt Noor."
PROCESSED = SOURCE


def inspect_event(text="Stichting Zorgpunt", event_id="inspect_event_0001"):
    start = PROCESSED.index(text)
    end = start + len(text)
    return {
        "schema_version": 1,
        "action": "inspect_selection",
        "event_id": event_id,
        "document_scope_key": SCOPE,
        "processed_text_hash": processed_text_hash(PROCESSED),
        "selection": {
            "text": text,
            "start_utf16": python_index_to_utf16_offset(PROCESSED, start),
            "end_utf16": python_index_to_utf16_offset(PROCESSED, end),
            "intersects_marked_content": False,
        },
        "ui_state": {
            "source_scroll_ratio": 0.25,
            "processed_scroll_ratio": 0.30,
        },
    }


def commit_event(inspection, event_id="commit_event_0001", requested_type="organization"):
    return {
        "schema_version": 1,
        "action": "commit_manual_mask",
        "event_id": event_id,
        "inspection_id": inspection["inspection_id"],
        "requested_type": requested_type,
        "requested_scope": "all_exact",
        "confirmation_token": inspection["confirmation_token"],
    }


def test_no_event_is_a_noop():
    session = {}
    outcome = handle_selection_component_event(
        session,
        None,
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )
    assert not outcome.handled
    assert not outcome.rerun_required
    assert session == {}


def test_inspect_event_persists_server_result_scroll_and_action_state():
    session = {}
    outcome = handle_selection_component_event(
        session,
        inspect_event(),
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )

    assert outcome.handled
    assert outcome.rerun_required
    assert outcome.action == "inspect_selection"
    assert outcome.status == "ready"
    assert selection_inspection_result(session, SCOPE)["occurrence_count"] == 2
    assert selection_scroll_restore(session, SCOPE) == (0.25, 0.30)
    assert selection_feedback(session, SCOPE)["level"] == "info"
    assert SCOPE in session[ACTION_STATES_KEY]
    assert SCOPE in session[INSPECTION_RESULTS_KEY]
    assert SCOPE in session[SCROLL_RESTORE_KEY]


def test_commit_appends_one_normal_document_scoped_manual_row():
    session = {}
    handle_selection_component_event(
        session,
        inspect_event(),
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )
    inspection = selection_inspection_result(session, SCOPE)

    outcome = handle_selection_component_event(
        session,
        commit_event(inspection),
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )

    assert outcome.handled
    assert outcome.rerun_required
    assert outcome.status == "committed"
    assert outcome.row_added
    assert outcome.undo_available
    rows = session[MANUAL_ROWS_KEY][SCOPE]
    assert len(rows) == 1
    row = rows[0]
    assert row["find"] == "Stichting Zorgpunt"
    assert row["entity_type"] == "ORGANIZATION"
    assert row["source"] == "manual_selection"
    assert row["source_label"] == "Handmatig uit tekst"
    assert row["include"] is True
    assert row["remember"] is False
    assert row["selection_scope"] == "all_exact"
    assert row["selection_occurrence_count"] == 2
    assert "_B" in row["replace_with"]
    assert selection_inspection_result(session, SCOPE) == {}
    assert latest_selection_action(session, SCOPE) is not None
    assert selection_feedback(session, SCOPE)["level"] == "success"


def test_duplicate_component_value_is_ignored_without_feedback_overwrite():
    session = {}
    event = inspect_event()
    first = handle_selection_component_event(
        session,
        event,
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )
    feedback_before = dict(selection_feedback(session, SCOPE))
    second = handle_selection_component_event(
        session,
        event,
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )

    assert first.handled
    assert not second.handled
    assert not second.rerun_required
    assert second.duplicate_event_ignored
    assert selection_feedback(session, SCOPE) == feedback_before


def test_blocked_inspection_is_returned_to_component_and_fails_closed():
    session = {}
    event = inspect_event(text="Noor")
    outcome = handle_selection_component_event(
        session,
        event,
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )

    assert outcome.status == "blocked"
    assert outcome.issue_code == "embedded_substring"
    assert session.get(MANUAL_ROWS_KEY) is None
    assert selection_inspection_result(session, SCOPE)["status"] == "blocked"
    assert selection_feedback(session, SCOPE)["level"] == "warning"


def test_commit_revalidates_table_state_and_adds_no_row_when_stale():
    session = {}
    handle_selection_component_event(
        session,
        inspect_event(),
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )
    inspection = selection_inspection_result(session, SCOPE)
    changed_rows = [{"include": True, "find": "Noor", "replace_with": "[PERSOON_1]"}]

    outcome = handle_selection_component_event(
        session,
        commit_event(inspection),
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=changed_rows,
    )

    assert outcome.status == "blocked"
    assert outcome.issue_code == "stale_replacement_table"
    assert session.get(MANUAL_ROWS_KEY) is None
    assert selection_feedback(session, SCOPE)["level"] == "warning"


def test_undo_removes_only_latest_unchanged_selection_row():
    session = {}
    handle_selection_component_event(
        session,
        inspect_event(),
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )
    inspection = selection_inspection_result(session, SCOPE)
    handle_selection_component_event(
        session,
        commit_event(inspection),
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )

    outcome = undo_latest_selection_action(session, document_scope_key=SCOPE)

    assert outcome.handled
    assert outcome.rerun_required
    assert outcome.status == "undone"
    assert session[MANUAL_ROWS_KEY][SCOPE] == []
    assert latest_selection_action(session, SCOPE) is None
    assert selection_feedback(session, SCOPE)["level"] == "success"


def test_undo_fails_closed_after_row_edit():
    session = {}
    handle_selection_component_event(
        session,
        inspect_event(),
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )
    inspection = selection_inspection_result(session, SCOPE)
    handle_selection_component_event(
        session,
        commit_event(inspection),
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )
    session[MANUAL_ROWS_KEY][SCOPE][0]["replace_with"] = "[GEWIJZIGD]"

    outcome = undo_latest_selection_action(session, document_scope_key=SCOPE)

    assert outcome.status == "blocked"
    assert outcome.issue_code == "action_row_changed"
    assert len(session[MANUAL_ROWS_KEY][SCOPE]) == 1
    assert latest_selection_action(session, SCOPE) is not None


def test_state_and_feedback_are_document_scoped():
    session = {}
    other_scope = "fedcba9876543210"
    first_state = selection_action_state(session, SCOPE)
    second_state = selection_action_state(session, other_scope)
    assert first_state is not second_state

    handle_selection_component_event(
        session,
        inspect_event(),
        source_text=SOURCE,
        processed_text=PROCESSED,
        document_scope_key=SCOPE,
        document_binding_id=BINDING,
        existing_rows=[],
    )
    assert selection_inspection_result(session, other_scope) == {}
    assert selection_feedback(session, other_scope) == {}

    clear_selection_feedback(session, SCOPE)
    assert selection_feedback(session, SCOPE) == {}
    assert SCOPE not in session[FEEDBACK_KEY]
    assert SCOPE not in session.get(LAST_ACTIONS_KEY, {})
