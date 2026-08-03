"""Pure session/integration adapter for processed-text selection masking.

The adapter coordinates the already-tested action model with caller-owned state.
It imports no Streamlit module and performs no rendering or export work. The
production Streamlit file remains responsible for reruns and visible feedback.
"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from dataclasses import dataclass
import math
from typing import Any

from selection_mask_action import (
    ManualSelectionActionRecord,
    SelectionActionState,
    commit_manual_mask,
    inspect_selection,
    undo_manual_selection_action,
)


ACTION_STATES_KEY = "processed_text_selection_action_states"
INSPECTION_RESULTS_KEY = "processed_text_selection_inspection_results"
SCROLL_RESTORE_KEY = "processed_text_selection_scroll_restore"
LAST_ACTIONS_KEY = "processed_text_selection_last_actions"
FEEDBACK_KEY = "processed_text_selection_feedback"
MANUAL_ROWS_KEY = "manual_mask_rows"


@dataclass(frozen=True)
class SelectionIntegrationOutcome:
    handled: bool
    rerun_required: bool
    action: str = ""
    status: str = ""
    message: str = ""
    issue_code: str = ""
    row_added: bool = False
    undo_available: bool = False
    duplicate_event_ignored: bool = False


def _mapping_bucket(
    session: MutableMapping[str, Any],
    key: str,
) -> dict[str, Any]:
    value = session.get(key)
    if not isinstance(value, dict):
        value = {}
        session[key] = value
    return value


def _row_dicts(rows: Any) -> list[dict[str, Any]]:
    if rows is None:
        return []
    if hasattr(rows, "to_dict"):
        try:
            return [dict(row) for row in rows.to_dict("records")]
        except TypeError:
            pass
    return [dict(row) for row in rows]


def selection_action_state(
    session: MutableMapping[str, Any],
    document_scope_key: str,
) -> SelectionActionState:
    bucket = _mapping_bucket(session, ACTION_STATES_KEY)
    state = bucket.get(document_scope_key)
    if not isinstance(state, SelectionActionState):
        state = SelectionActionState()
        bucket[document_scope_key] = state
    return state


def selection_inspection_result(
    session: Mapping[str, Any],
    document_scope_key: str,
) -> dict[str, Any]:
    bucket = session.get(INSPECTION_RESULTS_KEY)
    if not isinstance(bucket, Mapping):
        return {}
    value = bucket.get(document_scope_key)
    return dict(value) if isinstance(value, Mapping) else {}


def selection_scroll_restore(
    session: Mapping[str, Any],
    document_scope_key: str,
) -> tuple[float | None, float | None]:
    bucket = session.get(SCROLL_RESTORE_KEY)
    if not isinstance(bucket, Mapping):
        return None, None
    value = bucket.get(document_scope_key)
    if not isinstance(value, Mapping):
        return None, None
    return _safe_ratio(value.get("source")), _safe_ratio(value.get("processed"))


def selection_feedback(
    session: Mapping[str, Any],
    document_scope_key: str,
) -> dict[str, Any]:
    bucket = session.get(FEEDBACK_KEY)
    if not isinstance(bucket, Mapping):
        return {}
    value = bucket.get(document_scope_key)
    return dict(value) if isinstance(value, Mapping) else {}


def clear_selection_feedback(
    session: MutableMapping[str, Any],
    document_scope_key: str,
) -> None:
    bucket = _mapping_bucket(session, FEEDBACK_KEY)
    bucket.pop(document_scope_key, None)


def _safe_ratio(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    ratio = float(value)
    return ratio if 0.0 <= ratio <= 1.0 else None


def _event_scroll_state(event: Mapping[str, Any]) -> dict[str, float | None]:
    ui_state = event.get("ui_state")
    if not isinstance(ui_state, Mapping):
        return {"source": None, "processed": None}
    return {
        "source": _safe_ratio(ui_state.get("source_scroll_ratio")),
        "processed": _safe_ratio(ui_state.get("processed_scroll_ratio")),
    }


def _store_feedback(
    session: MutableMapping[str, Any],
    document_scope_key: str,
    *,
    level: str,
    message: str,
    issue_code: str = "",
) -> None:
    bucket = _mapping_bucket(session, FEEDBACK_KEY)
    bucket[document_scope_key] = {
        "level": level,
        "message": str(message),
        "issue_code": str(issue_code),
    }


def _manual_rows_for_scope(
    session: MutableMapping[str, Any],
    document_scope_key: str,
) -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]]]:
    bucket = session.get(MANUAL_ROWS_KEY)
    if not isinstance(bucket, dict):
        bucket = {}
    raw_rows = bucket.get(document_scope_key, [])
    rows = [dict(row) for row in raw_rows] if isinstance(raw_rows, list) else []
    return bucket, rows


def _component_event_id(event: Mapping[str, Any]) -> str:
    value = event.get("event_id", "")
    return str(value) if isinstance(value, str) else ""


def handle_selection_component_event(
    session: MutableMapping[str, Any],
    event: Mapping[str, Any] | None,
    *,
    source_text: str,
    processed_text: str,
    document_scope_key: str,
    document_binding_id: str,
    existing_rows: Any,
    marked_ranges: Sequence[tuple[int, int]] = (),
) -> SelectionIntegrationOutcome:
    """Inspect or commit one component event and update caller-owned state.

    The caller must rerun immediately when ``rerun_required`` is true, before
    rendering export controls against stale rows.
    """

    if not isinstance(event, Mapping):
        return SelectionIntegrationOutcome(False, False)

    action = str(event.get("action", ""))
    event_id = _component_event_id(event)
    state = selection_action_state(session, document_scope_key)
    if event_id and state.has_event(event_id):
        return SelectionIntegrationOutcome(
            handled=False,
            rerun_required=False,
            action=action,
            duplicate_event_ignored=True,
        )

    inspection_bucket = _mapping_bucket(session, INSPECTION_RESULTS_KEY)
    scroll_bucket = _mapping_bucket(session, SCROLL_RESTORE_KEY)
    last_action_bucket = _mapping_bucket(session, LAST_ACTIONS_KEY)

    if action == "inspect_selection":
        result = inspect_selection(
            event,
            source_text=source_text,
            processed_text=processed_text,
            current_document_scope_key=document_scope_key,
            existing_rows=existing_rows,
            marked_ranges=marked_ranges,
            document_binding_id=document_binding_id,
            state=state,
        )
        inspection_bucket[document_scope_key] = result.to_dict()
        scroll_bucket[document_scope_key] = _event_scroll_state(event)
        if result.ok:
            _store_feedback(
                session,
                document_scope_key,
                level="info",
                message=result.message,
            )
        else:
            _store_feedback(
                session,
                document_scope_key,
                level="warning",
                message=result.message,
                issue_code=result.issue_code,
            )
        return SelectionIntegrationOutcome(
            handled=True,
            rerun_required=True,
            action=action,
            status=result.status,
            message=result.message,
            issue_code=result.issue_code,
        )

    if action == "commit_manual_mask":
        inspection_id = str(event.get("inspection_id", ""))
        prior_record = state.get_inspection(inspection_id)
        result = commit_manual_mask(
            event,
            source_text=source_text,
            processed_text=processed_text,
            current_document_scope_key=document_scope_key,
            existing_rows=existing_rows,
            state=state,
            marked_ranges=marked_ranges,
            document_binding_id=document_binding_id,
        )
        if result.ok and result.row is not None and result.action_record is not None:
            manual_bucket, manual_rows = _manual_rows_for_scope(
                session,
                document_scope_key,
            )
            manual_rows.append(dict(result.row))
            manual_bucket[document_scope_key] = manual_rows
            session[MANUAL_ROWS_KEY] = manual_bucket
            last_action_bucket[document_scope_key] = result.action_record
            inspection_bucket.pop(document_scope_key, None)
            _store_feedback(
                session,
                document_scope_key,
                level="success",
                message=result.message,
            )
            return SelectionIntegrationOutcome(
                handled=True,
                rerun_required=True,
                action=action,
                status=result.status,
                message=result.message,
                row_added=True,
                undo_available=True,
            )

        blocked_result = {
            "schema_version": 1,
            "status": "blocked",
            "event_id": event_id,
            "inspection_id": "",
            "selection_text": prior_record.selection_text if prior_record else "",
            "occurrence_count": prior_record.occurrence_count if prior_record else 0,
            "requested_scope": "all_exact",
            "allowed_types": [],
            "confirmation_token": "",
            "message": result.message,
            "issue_code": result.issue_code,
        }
        inspection_bucket[document_scope_key] = blocked_result
        _store_feedback(
            session,
            document_scope_key,
            level="warning",
            message=result.message,
            issue_code=result.issue_code,
        )
        return SelectionIntegrationOutcome(
            handled=True,
            rerun_required=True,
            action=action,
            status=result.status,
            message=result.message,
            issue_code=result.issue_code,
        )

    return SelectionIntegrationOutcome(False, False, action=action)


def latest_selection_action(
    session: Mapping[str, Any],
    document_scope_key: str,
) -> ManualSelectionActionRecord | None:
    bucket = session.get(LAST_ACTIONS_KEY)
    if not isinstance(bucket, Mapping):
        return None
    value = bucket.get(document_scope_key)
    return value if isinstance(value, ManualSelectionActionRecord) else None


def _comparable_value(value: Any) -> Any:
    if isinstance(value, float) and math.isnan(value):
        return None
    return value


def _current_action_row_unchanged(
    current_review_rows: Any,
    action: ManualSelectionActionRecord,
) -> bool:
    rows = [
        row
        for row in _row_dicts(current_review_rows)
        if str(row.get("manual_action_id", "")) == action.action_id
    ]
    if len(rows) != 1:
        return False
    current = rows[0]
    original = dict(action.row)
    protected_fields = (
        "include",
        "remember",
        "find",
        "replace_with",
        "entity_type",
        "type_label",
        "source",
        "manual_action_id",
    )
    return all(
        _comparable_value(current.get(field)) == _comparable_value(original.get(field))
        for field in protected_fields
    )


def undo_latest_selection_action(
    session: MutableMapping[str, Any],
    *,
    document_scope_key: str,
    current_review_rows: Any = None,
) -> SelectionIntegrationOutcome:
    """Undo only the latest unchanged selection-created row for this document."""

    action = latest_selection_action(session, document_scope_key)
    if action is None:
        return SelectionIntegrationOutcome(
            handled=False,
            rerun_required=False,
            action="undo",
            status="blocked",
            message="Er is geen recente tekstselectiemaskering om ongedaan te maken.",
            issue_code="no_latest_action",
        )

    if current_review_rows is not None and not _current_action_row_unchanged(
        current_review_rows,
        action,
    ):
        message = (
            "De handmatige rij is intussen gewijzigd en kan niet automatisch "
            "ongedaan worden gemaakt. Pas de rij aan in de vervangtabel."
        )
        _store_feedback(
            session,
            document_scope_key,
            level="warning",
            message=message,
            issue_code="action_row_changed",
        )
        return SelectionIntegrationOutcome(
            handled=True,
            rerun_required=False,
            action="undo",
            status="blocked",
            message=message,
            issue_code="action_row_changed",
        )

    manual_bucket, manual_rows = _manual_rows_for_scope(session, document_scope_key)
    result = undo_manual_selection_action(
        manual_rows,
        action,
        current_document_scope_key=document_scope_key,
    )
    if result.ok:
        manual_bucket[document_scope_key] = [dict(row) for row in result.rows]
        session[MANUAL_ROWS_KEY] = manual_bucket
        _mapping_bucket(session, LAST_ACTIONS_KEY).pop(document_scope_key, None)
        _mapping_bucket(session, INSPECTION_RESULTS_KEY).pop(document_scope_key, None)
        _store_feedback(
            session,
            document_scope_key,
            level="success",
            message=result.message,
        )
        return SelectionIntegrationOutcome(
            handled=True,
            rerun_required=True,
            action="undo",
            status=result.status,
            message=result.message,
        )

    _store_feedback(
        session,
        document_scope_key,
        level="warning",
        message=result.message,
        issue_code=result.issue_code,
    )
    return SelectionIntegrationOutcome(
        handled=True,
        rerun_required=False,
        action="undo",
        status=result.status,
        message=result.message,
        issue_code=result.issue_code,
    )
