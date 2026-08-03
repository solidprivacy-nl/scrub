"""Pure action model for masking a selection from the processed-text review pane.

This module implements the frozen two-stage contract without importing Streamlit,
rendering browser UI, mutating session state, writing files, or touching export,
Scrub Key or reinsert behavior. Callers supply current server-owned document state
and retain responsibility for document-scoped persistence and reruns.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass, field
from hashlib import sha256
import json
import re
import secrets
import unicodedata
from typing import Any, Literal

from manual_mask_entry import build_manual_mask_row


SCHEMA_VERSION = 1
INSPECT_ACTION = "inspect_selection"
COMMIT_ACTION = "commit_manual_mask"
REQUESTED_SCOPE = "all_exact"
MAX_PAYLOAD_UTF8_BYTES = 8192
MAX_SELECTION_CODEPOINTS = 160
MAX_REPLAY_EVENTS = 128
READY_MAX_OCCURRENCES = 5
CONFIRMATION_MAX_OCCURRENCES = 20

EVENT_ID_RE = re.compile(r"^[A-Za-z0-9_-]{16,80}$")
DOCUMENT_SCOPE_KEY_RE = re.compile(r"^[0-9a-f]{16}$")
LOWERCASE_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
STRICT_PLACEHOLDER_SEARCH_RE = re.compile(
    r"\[(?:[A-Z][A-Z0-9_]*)"
    r"(?:_B[A-Z2-7]{16})?"
    r"(?:_HANDMATIG)?"
    r"_\d{1,}\]"
)

TOKEN_CONTINUATION_PUNCTUATION = frozenset(
    {
        "_",
        "'",
        "’",
        "ʼ",
        "‐",
        "‑",
        "‒",
        "–",
        "—",
        "―",
        "−",
        "﹘",
        "﹣",
        "－",
    }
)

InspectionStatus = Literal["ready", "confirmation_required", "blocked"]
CommitStatus = Literal["committed", "blocked"]
UndoStatus = Literal["undone", "blocked"]


@dataclass(frozen=True)
class QuickMaskType:
    key: str
    user_label: str
    manual_label: str
    entity_type: str
    placeholder_prefix: str


QUICK_MASK_TYPES: tuple[QuickMaskType, ...] = (
    QuickMaskType("person", "Persoon", "Persoon", "PERSON", "PERSOON"),
    QuickMaskType(
        "organization",
        "Organisatie",
        "Organisatie",
        "ORGANIZATION",
        "ORGANISATIE",
    ),
    QuickMaskType(
        "location",
        "Adres of locatie",
        "Adres of locatie",
        "LOCATION",
        "LOCATIE",
    ),
    QuickMaskType(
        "email",
        "E-mailadres",
        "E-mailadres",
        "EMAIL_ADDRESS",
        "EMAIL",
    ),
    QuickMaskType(
        "phone",
        "Telefoonnummer",
        "Telefoonnummer",
        "NL_PHONE_NUMBER",
        "TELEFOON",
    ),
    QuickMaskType(
        "date_time",
        "Datum of tijd",
        "Datum of tijd",
        "DATE_TIME",
        "DATUM",
    ),
    QuickMaskType(
        "reference",
        "Nummer of referentie",
        "Nummer of referentie",
        "NL_OTHER_REFERENCE",
        "OVERIGE_REFERENTIE",
    ),
    QuickMaskType(
        "other",
        "Overige waarde",
        "Overige waarde",
        "MANUAL",
        "WAARDE",
    ),
)
QUICK_MASK_TYPE_BY_KEY = {item.key: item for item in QUICK_MASK_TYPES}
ALLOWED_TYPE_KEYS = tuple(item.key for item in QUICK_MASK_TYPES)


@dataclass(frozen=True)
class SelectionActionIssue:
    code: str
    message: str


class SelectionActionError(ValueError):
    """Structured fail-closed validation exception used inside the pure model."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message


@dataclass(frozen=True)
class InspectSelectionEvent:
    event_id: str
    document_scope_key: str
    processed_text_hash: str
    selection_text: str
    start_utf16: int
    end_utf16: int
    intersects_marked_content: bool
    source_scroll_ratio: float | None = None
    processed_scroll_ratio: float | None = None


@dataclass(frozen=True)
class CommitManualMaskEvent:
    event_id: str
    inspection_id: str
    requested_type: str
    requested_scope: str
    confirmation_token: str


@dataclass(frozen=True)
class SelectionEvaluation:
    status: InspectionStatus
    issue: SelectionActionIssue | None
    selection_text: str
    start_index: int
    end_index: int
    occurrence_ranges: tuple[tuple[int, int], ...]

    @property
    def occurrence_count(self) -> int:
        return len(self.occurrence_ranges)


@dataclass(frozen=True)
class InspectionRecord:
    inspection_id: str
    inspect_event_id: str
    document_scope_key: str
    document_binding_id: str
    processed_text_hash: str
    source_text_hash: str
    replacement_state_hash: str
    selection_text: str
    start_index: int
    end_index: int
    start_utf16: int
    end_utf16: int
    occurrence_ranges: tuple[tuple[int, int], ...]
    status: Literal["ready", "confirmation_required"]
    confirmation_token: str
    allowed_types: tuple[str, ...] = ALLOWED_TYPE_KEYS
    requested_scope: str = REQUESTED_SCOPE

    @property
    def occurrence_count(self) -> int:
        return len(self.occurrence_ranges)


@dataclass(frozen=True)
class InspectionResult:
    status: InspectionStatus
    event_id: str = ""
    inspection_id: str = ""
    selection_text: str = ""
    occurrence_count: int = 0
    requested_scope: str = REQUESTED_SCOPE
    allowed_types: tuple[str, ...] = ()
    confirmation_token: str = ""
    message: str = ""
    issue_code: str = ""
    record: InspectionRecord | None = None

    @property
    def ok(self) -> bool:
        return self.status in {"ready", "confirmation_required"}

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": SCHEMA_VERSION,
            "status": self.status,
            "event_id": self.event_id,
            "inspection_id": self.inspection_id,
            "selection_text": self.selection_text,
            "occurrence_count": self.occurrence_count,
            "requested_scope": self.requested_scope,
            "allowed_types": list(self.allowed_types),
            "confirmation_token": self.confirmation_token,
            "message": self.message,
            "issue_code": self.issue_code,
        }


@dataclass(frozen=True)
class ManualSelectionActionRecord:
    action_id: str
    commit_event_id: str
    inspect_event_id: str
    inspection_id: str
    document_scope_key: str
    find_text: str
    replace_with: str
    occurrence_count: int
    requested_type: str
    row: Mapping[str, Any]
    row_fingerprint: str


@dataclass(frozen=True)
class CommitResult:
    status: CommitStatus
    event_id: str = ""
    message: str = ""
    issue_code: str = ""
    row: Mapping[str, Any] | None = None
    action_record: ManualSelectionActionRecord | None = None

    @property
    def ok(self) -> bool:
        return self.status == "committed"


@dataclass(frozen=True)
class UndoResult:
    status: UndoStatus
    rows: tuple[dict[str, Any], ...]
    message: str
    issue_code: str = ""

    @property
    def ok(self) -> bool:
        return self.status == "undone"


@dataclass
class SelectionActionState:
    """Bounded, caller-owned replay and inspection state for one document session."""

    max_event_ids: int = MAX_REPLAY_EVENTS
    _event_ids: deque[str] = field(default_factory=deque, init=False, repr=False)
    _event_id_set: set[str] = field(default_factory=set, init=False, repr=False)
    _inspections: dict[str, InspectionRecord] = field(default_factory=dict, init=False, repr=False)

    def __post_init__(self) -> None:
        if isinstance(self.max_event_ids, bool) or not isinstance(self.max_event_ids, int):
            raise TypeError("max_event_ids must be an integer")
        if self.max_event_ids < 1:
            raise ValueError("max_event_ids must be positive")

    def has_event(self, event_id: str) -> bool:
        return event_id in self._event_id_set

    def record_event(self, event_id: str) -> bool:
        if event_id in self._event_id_set:
            return False
        self._event_ids.append(event_id)
        self._event_id_set.add(event_id)
        while len(self._event_ids) > self.max_event_ids:
            removed = self._event_ids.popleft()
            self._event_id_set.discard(removed)
        return True

    def save_inspection(self, record: InspectionRecord) -> None:
        self._inspections[record.inspection_id] = record

    def get_inspection(self, inspection_id: str) -> InspectionRecord | None:
        return self._inspections.get(inspection_id)

    def invalidate_inspection(self, inspection_id: str) -> InspectionRecord | None:
        return self._inspections.pop(inspection_id, None)

    def consume_inspection(self, inspection_id: str) -> InspectionRecord | None:
        return self.invalidate_inspection(inspection_id)

    @property
    def event_ids(self) -> tuple[str, ...]:
        return tuple(self._event_ids)

    @property
    def inspection_ids(self) -> tuple[str, ...]:
        return tuple(self._inspections)


def processed_text_hash(text: str) -> str:
    return sha256(str(text).encode("utf-8")).hexdigest()


def source_text_hash(text: str) -> str:
    return sha256(str(text).encode("utf-8")).hexdigest()


def _row_dicts(existing_rows: Iterable[Mapping[str, Any]] | Any | None) -> list[dict[str, Any]]:
    if existing_rows is None:
        return []
    if hasattr(existing_rows, "to_dict"):
        try:
            return [dict(row) for row in existing_rows.to_dict("records")]
        except TypeError:
            pass
    return [dict(row) for row in existing_rows]


def replacement_state_hash(existing_rows: Iterable[Mapping[str, Any]] | Any | None) -> str:
    normalized = []
    for row in _row_dicts(existing_rows):
        normalized.append(
            {
                "include": row.get("include"),
                "find": str(row.get("find", "")),
                "replace_with": str(row.get("replace_with", "")),
                "entity_type": str(row.get("entity_type", "")),
                "source": str(row.get("source", "")),
            }
        )
    payload = json.dumps(normalized, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256(payload.encode("utf-8")).hexdigest()


def _payload_size(event: Any) -> int:
    try:
        encoded = json.dumps(event, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise SelectionActionError("invalid_payload", "Het selectie-event is ongeldig.") from exc
    return len(encoded)


def _require_mapping(value: Any, code: str, message: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise SelectionActionError(code, message)
    return value


def _require_string(value: Any, *, code: str, message: str) -> str:
    if not isinstance(value, str):
        raise SelectionActionError(code, message)
    return value


def _require_int(value: Any, *, code: str, message: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise SelectionActionError(code, message)
    return value


def _require_bool(value: Any, *, code: str, message: str) -> bool:
    if not isinstance(value, bool):
        raise SelectionActionError(code, message)
    return value


def _optional_ratio(value: Any, *, field_name: str) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise SelectionActionError("invalid_ui_state", f"{field_name} moet een getal tussen 0 en 1 zijn.")
    ratio = float(value)
    if not 0.0 <= ratio <= 1.0:
        raise SelectionActionError("invalid_ui_state", f"{field_name} moet een getal tussen 0 en 1 zijn.")
    return ratio


def _validate_common_envelope(event: Any, expected_action: str) -> Mapping[str, Any]:
    mapping = _require_mapping(event, "invalid_payload", "Het selectie-event is ongeldig.")
    if _payload_size(mapping) > MAX_PAYLOAD_UTF8_BYTES:
        raise SelectionActionError("payload_too_large", "Het selectie-event is te groot.")

    version = _require_int(
        mapping.get("schema_version"),
        code="invalid_schema_version",
        message="De versie van het selectie-event wordt niet ondersteund.",
    )
    if version != SCHEMA_VERSION:
        raise SelectionActionError(
            "invalid_schema_version",
            "De versie van het selectie-event wordt niet ondersteund.",
        )

    action = _require_string(
        mapping.get("action"),
        code="invalid_action",
        message="De selectieactie wordt niet ondersteund.",
    )
    if action != expected_action:
        raise SelectionActionError("invalid_action", "De selectieactie wordt niet ondersteund.")

    event_id = _require_string(
        mapping.get("event_id"),
        code="invalid_event_id",
        message="Het selectie-event heeft geen geldig ID.",
    )
    if EVENT_ID_RE.fullmatch(event_id) is None:
        raise SelectionActionError("invalid_event_id", "Het selectie-event heeft geen geldig ID.")
    return mapping


def parse_inspect_event(event: Any) -> InspectSelectionEvent:
    mapping = _validate_common_envelope(event, INSPECT_ACTION)

    document_scope_key = _require_string(
        mapping.get("document_scope_key"),
        code="invalid_document_scope",
        message="De documentcontext van de selectie is ongeldig.",
    )
    if DOCUMENT_SCOPE_KEY_RE.fullmatch(document_scope_key) is None:
        raise SelectionActionError("invalid_document_scope", "De documentcontext van de selectie is ongeldig.")

    current_hash = _require_string(
        mapping.get("processed_text_hash"),
        code="invalid_processed_hash",
        message="De tekstversie van de selectie is ongeldig.",
    )
    if LOWERCASE_SHA256_RE.fullmatch(current_hash) is None:
        raise SelectionActionError("invalid_processed_hash", "De tekstversie van de selectie is ongeldig.")

    selection = _require_mapping(
        mapping.get("selection"),
        "invalid_selection",
        "De selectie is ongeldig.",
    )
    selection_text = _require_string(
        selection.get("text"),
        code="invalid_selection",
        message="De selectie is ongeldig.",
    )
    start_utf16 = _require_int(
        selection.get("start_utf16"),
        code="invalid_offsets",
        message="De selectiepositie is ongeldig.",
    )
    end_utf16 = _require_int(
        selection.get("end_utf16"),
        code="invalid_offsets",
        message="De selectiepositie is ongeldig.",
    )
    intersects = _require_bool(
        selection.get("intersects_marked_content"),
        code="invalid_selection",
        message="De selectie is ongeldig.",
    )

    ui_state_raw = mapping.get("ui_state")
    source_ratio = None
    processed_ratio = None
    if ui_state_raw is not None:
        ui_state = _require_mapping(
            ui_state_raw,
            "invalid_ui_state",
            "De weergavestatus van de selectie is ongeldig.",
        )
        source_ratio = _optional_ratio(ui_state.get("source_scroll_ratio"), field_name="source_scroll_ratio")
        processed_ratio = _optional_ratio(
            ui_state.get("processed_scroll_ratio"),
            field_name="processed_scroll_ratio",
        )

    return InspectSelectionEvent(
        event_id=event_id,
        document_scope_key=document_scope_key,
        processed_text_hash=current_hash,
        selection_text=selection_text,
        start_utf16=start_utf16,
        end_utf16=end_utf16,
        intersects_marked_content=intersects,
        source_scroll_ratio=source_ratio,
        processed_scroll_ratio=processed_ratio,
    )


def parse_commit_event(event: Any) -> CommitManualMaskEvent:
    mapping = _validate_common_envelope(event, COMMIT_ACTION)
    inspection_id = _require_string(
        mapping.get("inspection_id"),
        code="invalid_inspection",
        message="De selectie-inspectie is ongeldig of verlopen.",
    )
    if not 8 <= len(inspection_id) <= 160:
        raise SelectionActionError("invalid_inspection", "De selectie-inspectie is ongeldig of verlopen.")

    requested_type = _require_string(
        mapping.get("requested_type"),
        code="invalid_type",
        message="Het gekozen maskeringstype wordt niet ondersteund.",
    )
    if requested_type not in QUICK_MASK_TYPE_BY_KEY:
        raise SelectionActionError("invalid_type", "Het gekozen maskeringstype wordt niet ondersteund.")

    requested_scope = _require_string(
        mapping.get("requested_scope"),
        code="invalid_scope",
        message="De gekozen maskeringsscope wordt niet ondersteund.",
    )
    if requested_scope != REQUESTED_SCOPE:
        raise SelectionActionError("invalid_scope", "De gekozen maskeringsscope wordt niet ondersteund.")

    token = mapping.get("confirmation_token", "")
    confirmation_token = _require_string(
        token,
        code="invalid_confirmation",
        message="De bevestiging voor deze selectie is ongeldig.",
    )
    if len(confirmation_token) > 256:
        raise SelectionActionError("invalid_confirmation", "De bevestiging voor deze selectie is ongeldig.")

    return CommitManualMaskEvent(
        event_id=_require_string(
            mapping.get("event_id"),
            code="invalid_event_id",
            message="Het selectie-event heeft geen geldig ID.",
        ),
        inspection_id=inspection_id,
        requested_type=requested_type,
        requested_scope=requested_scope,
        confirmation_token=confirmation_token,
    )


def utf16_offset_to_index(text: str, offset: int) -> int:
    """Convert a JavaScript UTF-16 code-unit offset to a Python string index.

    An offset which falls between the two UTF-16 code units of one supplementary
    Unicode code point is rejected rather than rounded.
    """

    if isinstance(offset, bool) or not isinstance(offset, int):
        raise SelectionActionError("invalid_offsets", "De selectiepositie is ongeldig.")
    if offset < 0:
        raise SelectionActionError("invalid_offsets", "De selectiepositie is ongeldig.")

    units = 0
    for index, character in enumerate(text):
        if units == offset:
            return index
        next_units = units + (2 if ord(character) > 0xFFFF else 1)
        if units < offset < next_units:
            raise SelectionActionError(
                "split_surrogate_pair",
                "De selectiepositie splitst een Unicode-teken.",
            )
        units = next_units
    if units == offset:
        return len(text)
    raise SelectionActionError("invalid_offsets", "De selectiepositie valt buiten de tekst.")


def utf16_range_to_indices(text: str, start_utf16: int, end_utf16: int) -> tuple[int, int]:
    if end_utf16 <= start_utf16:
        raise SelectionActionError("invalid_offsets", "De selectiepositie is ongeldig.")
    start = utf16_offset_to_index(text, start_utf16)
    end = utf16_offset_to_index(text, end_utf16)
    if end <= start:
        raise SelectionActionError("invalid_offsets", "De selectiepositie is ongeldig.")
    return start, end


def python_index_to_utf16_offset(text: str, index: int) -> int:
    """Test/integration helper for constructing exact browser-compatible offsets."""

    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index <= len(text):
        raise ValueError("index must be within the Python string")
    return sum(2 if ord(character) > 0xFFFF else 1 for character in text[:index])


def find_exact_occurrences(source_text: str, selection_text: str) -> tuple[tuple[int, int], ...]:
    if not selection_text:
        return ()
    ranges: list[tuple[int, int]] = []
    cursor = 0
    while True:
        start = source_text.find(selection_text, cursor)
        if start < 0:
            break
        end = start + len(selection_text)
        ranges.append((start, end))
        cursor = end
    return tuple(ranges)


def _is_unicode_letter_or_number(character: str) -> bool:
    return unicodedata.category(character).startswith(("L", "N"))


def is_token_continuation(character: str) -> bool:
    if not character:
        return False
    category = unicodedata.category(character)
    return (
        category.startswith(("L", "N", "M"))
        or category == "Pd"
        or character in TOKEN_CONTINUATION_PUNCTUATION
    )


def embedded_occurrence_ranges(
    source_text: str,
    selection_text: str,
    occurrence_ranges: Sequence[tuple[int, int]],
) -> tuple[tuple[int, int], ...]:
    if not selection_text:
        return ()
    inspect_left = is_token_continuation(selection_text[0])
    inspect_right = is_token_continuation(selection_text[-1])
    embedded: list[tuple[int, int]] = []
    for start, end in occurrence_ranges:
        left_collision = inspect_left and start > 0 and is_token_continuation(source_text[start - 1])
        right_collision = (
            inspect_right
            and end < len(source_text)
            and is_token_continuation(source_text[end])
        )
        if left_collision or right_collision:
            embedded.append((start, end))
    return tuple(embedded)


def ranges_overlap(first: tuple[int, int], second: tuple[int, int]) -> bool:
    return first[0] < second[1] and second[0] < first[1]


def _row_is_included(row: Mapping[str, Any]) -> bool:
    value = row.get("include", True)
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() not in {"", "false", "0", "no", "nee", "excluded"}
    return bool(value)


def replacement_conflict(
    selection_text: str,
    existing_rows: Iterable[Mapping[str, Any]] | Any | None,
) -> SelectionActionIssue | None:
    rows = _row_dicts(existing_rows)
    for row in rows:
        existing = str(row.get("find", "")).strip()
        if existing == selection_text:
            return SelectionActionIssue("duplicate_value", "Deze waarde staat al in de vervangtabel.")

    for row in rows:
        if not _row_is_included(row):
            continue
        existing = str(row.get("find", "")).strip()
        if not existing or existing == selection_text:
            continue
        if selection_text in existing or existing in selection_text:
            return SelectionActionIssue(
                "nested_replacement_conflict",
                "Deze selectie overlapt met een bestaande vervangingsregel. Controleer dit in de vervangtabel.",
            )
    return None


def _selection_issue(message_code: str) -> SelectionActionIssue:
    messages = {
        "empty_selection": "Selecteer eerst een gemiste waarde.",
        "selection_too_long": "De selectie is te lang voor de snelle maskeringsroute.",
        "multiline_selection": "Selecteer één regel of gebruik ‘Gemiste waarde toevoegen’.",
        "control_character": "De selectie bevat niet-ondersteunde besturingstekens.",
        "punctuation_only": "Selecteer een waarde met ten minste één letter of cijfer.",
        "placeholder_selection": "Een bestaande Scrub-placeholder kan niet opnieuw worden gemaskeerd.",
        "marked_content": "De selectie overlapt met een bestaande maskering.",
        "selection_mismatch": "De tekst is intussen gewijzigd. Selecteer de waarde opnieuw.",
        "missing_in_source": "Deze waarde staat niet in de huidige brontekst.",
        "embedded_substring": (
            "Deze selectie komt ook voor als onderdeel van een langere waarde. "
            "Selecteer meer tekst of gebruik ‘Gemiste waarde toevoegen’."
        ),
        "too_many_occurrences": (
            "Deze selectie komt te vaak voor. Voeg de waarde via ‘Gemiste waarde toevoegen’ "
            "toe om de impact uitgebreider te controleren."
        ),
    }
    return SelectionActionIssue(message_code, messages[message_code])


def evaluate_selection(
    *,
    source_text: str,
    processed_text: str,
    selection_text: str,
    start_utf16: int,
    end_utf16: int,
    existing_rows: Iterable[Mapping[str, Any]] | Any | None = None,
    marked_ranges: Sequence[tuple[int, int]] = (),
    frontend_intersects_marked_content: bool = False,
) -> SelectionEvaluation:
    try:
        start_index, end_index = utf16_range_to_indices(processed_text, start_utf16, end_utf16)
    except SelectionActionError as exc:
        return SelectionEvaluation(
            status="blocked",
            issue=SelectionActionIssue(exc.code, exc.message),
            selection_text=selection_text,
            start_index=0,
            end_index=0,
            occurrence_ranges=(),
        )

    if selection_text == "":
        return SelectionEvaluation("blocked", _selection_issue("empty_selection"), "", start_index, end_index, ())
    if selection_text != selection_text.strip():
        return SelectionEvaluation(
            "blocked",
            SelectionActionIssue(
                "outer_whitespace",
                "De selectie bevat voor- of achterliggende spaties. Selecteer de waarde opnieuw.",
            ),
            selection_text,
            start_index,
            end_index,
            (),
        )
    if len(selection_text) > MAX_SELECTION_CODEPOINTS:
        return SelectionEvaluation(
            "blocked",
            _selection_issue("selection_too_long"),
            selection_text,
            start_index,
            end_index,
            (),
        )
    if any(character in "\r\n\t" for character in selection_text):
        return SelectionEvaluation(
            "blocked",
            _selection_issue("multiline_selection"),
            selection_text,
            start_index,
            end_index,
            (),
        )
    if any(unicodedata.category(character).startswith("C") for character in selection_text):
        return SelectionEvaluation(
            "blocked",
            _selection_issue("control_character"),
            selection_text,
            start_index,
            end_index,
            (),
        )
    if not any(_is_unicode_letter_or_number(character) for character in selection_text):
        return SelectionEvaluation(
            "blocked",
            _selection_issue("punctuation_only"),
            selection_text,
            start_index,
            end_index,
            (),
        )
    if STRICT_PLACEHOLDER_SEARCH_RE.search(selection_text):
        return SelectionEvaluation(
            "blocked",
            _selection_issue("placeholder_selection"),
            selection_text,
            start_index,
            end_index,
            (),
        )

    if processed_text[start_index:end_index] != selection_text:
        return SelectionEvaluation(
            "blocked",
            _selection_issue("selection_mismatch"),
            selection_text,
            start_index,
            end_index,
            (),
        )

    if frontend_intersects_marked_content or any(
        ranges_overlap((start_index, end_index), marked_range) for marked_range in marked_ranges
    ):
        return SelectionEvaluation(
            "blocked",
            _selection_issue("marked_content"),
            selection_text,
            start_index,
            end_index,
            (),
        )

    conflict = replacement_conflict(selection_text, existing_rows)
    if conflict is not None:
        return SelectionEvaluation("blocked", conflict, selection_text, start_index, end_index, ())

    occurrence_ranges = find_exact_occurrences(source_text, selection_text)
    if not occurrence_ranges:
        return SelectionEvaluation(
            "blocked",
            _selection_issue("missing_in_source"),
            selection_text,
            start_index,
            end_index,
            (),
        )

    if embedded_occurrence_ranges(source_text, selection_text, occurrence_ranges):
        return SelectionEvaluation(
            "blocked",
            _selection_issue("embedded_substring"),
            selection_text,
            start_index,
            end_index,
            occurrence_ranges,
        )

    count = len(occurrence_ranges)
    if count > CONFIRMATION_MAX_OCCURRENCES:
        issue = _selection_issue("too_many_occurrences")
        issue = SelectionActionIssue(
            issue.code,
            f"Deze selectie komt {count} keer voor. Voeg de waarde via ‘Gemiste waarde toevoegen’ "
            "toe om de impact uitgebreider te controleren.",
        )
        return SelectionEvaluation(
            "blocked",
            issue,
            selection_text,
            start_index,
            end_index,
            occurrence_ranges,
        )

    status: InspectionStatus = "ready" if count <= READY_MAX_OCCURRENCES else "confirmation_required"
    return SelectionEvaluation(
        status=status,
        issue=None,
        selection_text=selection_text,
        start_index=start_index,
        end_index=end_index,
        occurrence_ranges=occurrence_ranges,
    )


def _default_opaque_id(prefix: str) -> str:
    return f"{prefix}_{secrets.token_urlsafe(18).replace('-', '_')}"


def _occurrence_message(count: int) -> str:
    if count == 1:
        return "1 exact voorkomen in dit document"
    return f"{count} exacte voorkomens in dit document"


def _success_message(count: int, type_label: str) -> str:
    if count == 1:
        return f"1 exact voorkomen gemaskeerd als {type_label}."
    return f"{count} exacte voorkomens gemaskeerd als {type_label}."


def _blocked_inspection(
    *,
    issue: SelectionActionIssue,
    event_id: str = "",
    selection_text: str = "",
    occurrence_count: int = 0,
) -> InspectionResult:
    return InspectionResult(
        status="blocked",
        event_id=event_id,
        selection_text=selection_text,
        occurrence_count=occurrence_count,
        message=issue.message,
        issue_code=issue.code,
    )


def inspect_selection(
    event: Any,
    *,
    source_text: str,
    processed_text: str,
    current_document_scope_key: str,
    existing_rows: Iterable[Mapping[str, Any]] | Any | None = None,
    marked_ranges: Sequence[tuple[int, int]] = (),
    document_binding_id: str | None = None,
    state: SelectionActionState | None = None,
    inspection_id_factory: Callable[[], str] | None = None,
    confirmation_token_factory: Callable[[], str] | None = None,
) -> InspectionResult:
    try:
        parsed = parse_inspect_event(event)
    except SelectionActionError as exc:
        return _blocked_inspection(issue=SelectionActionIssue(exc.code, exc.message))

    active_state = state or SelectionActionState()
    if active_state.has_event(parsed.event_id):
        return _blocked_inspection(
            issue=SelectionActionIssue("replayed_event", "Deze selectieactie is al verwerkt."),
            event_id=parsed.event_id,
            selection_text=parsed.selection_text,
        )
    active_state.record_event(parsed.event_id)

    if DOCUMENT_SCOPE_KEY_RE.fullmatch(current_document_scope_key) is None:
        return _blocked_inspection(
            issue=SelectionActionIssue("invalid_server_scope", "De huidige documentcontext is ongeldig."),
            event_id=parsed.event_id,
            selection_text=parsed.selection_text,
        )
    if parsed.document_scope_key != current_document_scope_key:
        return _blocked_inspection(
            issue=SelectionActionIssue(
                "stale_document_scope",
                "De tekst is intussen gewijzigd. Selecteer de waarde opnieuw.",
            ),
            event_id=parsed.event_id,
            selection_text=parsed.selection_text,
        )

    current_processed_hash = processed_text_hash(processed_text)
    if parsed.processed_text_hash != current_processed_hash:
        return _blocked_inspection(
            issue=SelectionActionIssue(
                "stale_processed_text",
                "De tekst is intussen gewijzigd. Selecteer de waarde opnieuw.",
            ),
            event_id=parsed.event_id,
            selection_text=parsed.selection_text,
        )

    evaluation = evaluate_selection(
        source_text=source_text,
        processed_text=processed_text,
        selection_text=parsed.selection_text,
        start_utf16=parsed.start_utf16,
        end_utf16=parsed.end_utf16,
        existing_rows=existing_rows,
        marked_ranges=marked_ranges,
        frontend_intersects_marked_content=parsed.intersects_marked_content,
    )
    if evaluation.status == "blocked":
        assert evaluation.issue is not None
        return _blocked_inspection(
            issue=evaluation.issue,
            event_id=parsed.event_id,
            selection_text=parsed.selection_text,
            occurrence_count=evaluation.occurrence_count,
        )

    make_inspection_id = inspection_id_factory or (lambda: _default_opaque_id("inspection"))
    make_confirmation_token = confirmation_token_factory or (lambda: _default_opaque_id("confirm"))
    inspection_id = str(make_inspection_id())
    if not 8 <= len(inspection_id) <= 160:
        return _blocked_inspection(
            issue=SelectionActionIssue("invalid_server_inspection_id", "De selectie-inspectie kon niet worden aangemaakt."),
            event_id=parsed.event_id,
            selection_text=parsed.selection_text,
            occurrence_count=evaluation.occurrence_count,
        )
    if active_state.get_inspection(inspection_id) is not None:
        return _blocked_inspection(
            issue=SelectionActionIssue("duplicate_inspection_id", "De selectie-inspectie kon niet veilig worden aangemaakt."),
            event_id=parsed.event_id,
            selection_text=parsed.selection_text,
            occurrence_count=evaluation.occurrence_count,
        )

    confirmation_token = ""
    if evaluation.status == "confirmation_required":
        confirmation_token = str(make_confirmation_token())
        if not confirmation_token or len(confirmation_token) > 256:
            return _blocked_inspection(
                issue=SelectionActionIssue("invalid_server_confirmation", "De bevestiging kon niet veilig worden aangemaakt."),
                event_id=parsed.event_id,
                selection_text=parsed.selection_text,
                occurrence_count=evaluation.occurrence_count,
            )

    record = InspectionRecord(
        inspection_id=inspection_id,
        inspect_event_id=parsed.event_id,
        document_scope_key=current_document_scope_key,
        document_binding_id=str(document_binding_id or ""),
        processed_text_hash=current_processed_hash,
        source_text_hash=source_text_hash(source_text),
        replacement_state_hash=replacement_state_hash(existing_rows),
        selection_text=parsed.selection_text,
        start_index=evaluation.start_index,
        end_index=evaluation.end_index,
        start_utf16=parsed.start_utf16,
        end_utf16=parsed.end_utf16,
        occurrence_ranges=evaluation.occurrence_ranges,
        status=evaluation.status,
        confirmation_token=confirmation_token,
    )
    active_state.save_inspection(record)

    return InspectionResult(
        status=evaluation.status,
        event_id=parsed.event_id,
        inspection_id=inspection_id,
        selection_text=parsed.selection_text,
        occurrence_count=evaluation.occurrence_count,
        allowed_types=ALLOWED_TYPE_KEYS,
        confirmation_token=confirmation_token,
        message=_occurrence_message(evaluation.occurrence_count),
        record=record,
    )


def _blocked_commit(event_id: str, code: str, message: str) -> CommitResult:
    return CommitResult(status="blocked", event_id=event_id, issue_code=code, message=message)


def _row_fingerprint(row: Mapping[str, Any]) -> str:
    payload = json.dumps(dict(row), ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)
    return sha256(payload.encode("utf-8")).hexdigest()


def commit_manual_mask(
    event: Any,
    *,
    source_text: str,
    processed_text: str,
    current_document_scope_key: str,
    existing_rows: Iterable[Mapping[str, Any]] | Any | None,
    state: SelectionActionState,
    marked_ranges: Sequence[tuple[int, int]] = (),
    document_binding_id: str | None = None,
    action_id_factory: Callable[[], str] | None = None,
) -> CommitResult:
    try:
        parsed = parse_commit_event(event)
    except SelectionActionError as exc:
        return _blocked_commit("", exc.code, exc.message)

    if state.has_event(parsed.event_id):
        return _blocked_commit(parsed.event_id, "replayed_event", "Deze selectieactie is al verwerkt.")
    state.record_event(parsed.event_id)

    record = state.get_inspection(parsed.inspection_id)
    if record is None:
        return _blocked_commit(
            parsed.event_id,
            "missing_inspection",
            "De selectie-inspectie is ongeldig of verlopen. Selecteer de waarde opnieuw.",
        )

    def invalidate(code: str, message: str) -> CommitResult:
        state.invalidate_inspection(parsed.inspection_id)
        return _blocked_commit(parsed.event_id, code, message)

    if parsed.requested_scope != record.requested_scope:
        return invalidate("invalid_scope", "De gekozen maskeringsscope wordt niet ondersteund.")
    if parsed.requested_type not in record.allowed_types:
        return invalidate("invalid_type", "Het gekozen maskeringstype wordt niet ondersteund.")
    if current_document_scope_key != record.document_scope_key:
        return invalidate("stale_document_scope", "De tekst is intussen gewijzigd. Selecteer de waarde opnieuw.")
    if str(document_binding_id or "") != record.document_binding_id:
        return invalidate("stale_document_binding", "De documentbinding is intussen gewijzigd. Selecteer de waarde opnieuw.")
    if processed_text_hash(processed_text) != record.processed_text_hash:
        return invalidate("stale_processed_text", "De tekst is intussen gewijzigd. Selecteer de waarde opnieuw.")
    if source_text_hash(source_text) != record.source_text_hash:
        return invalidate("stale_source_text", "De brontekst is intussen gewijzigd. Selecteer de waarde opnieuw.")
    if replacement_state_hash(existing_rows) != record.replacement_state_hash:
        return invalidate("stale_replacement_table", "De vervangtabel is intussen gewijzigd. Selecteer de waarde opnieuw.")

    evaluation = evaluate_selection(
        source_text=source_text,
        processed_text=processed_text,
        selection_text=record.selection_text,
        start_utf16=record.start_utf16,
        end_utf16=record.end_utf16,
        existing_rows=existing_rows,
        marked_ranges=marked_ranges,
        frontend_intersects_marked_content=False,
    )
    if evaluation.status == "blocked":
        issue = evaluation.issue or SelectionActionIssue(
            "revalidation_failed",
            "Deze selectie kon niet veilig worden toegevoegd. Selecteer de waarde opnieuw.",
        )
        return invalidate(issue.code, issue.message)
    if evaluation.status != record.status or evaluation.occurrence_ranges != record.occurrence_ranges:
        return invalidate("changed_impact", "De impact is intussen gewijzigd. Selecteer de waarde opnieuw.")

    if record.status == "confirmation_required":
        if not parsed.confirmation_token or not secrets.compare_digest(
            parsed.confirmation_token,
            record.confirmation_token,
        ):
            return invalidate(
                "invalid_confirmation",
                "De bevestiging voor alle exacte voorkomens is ongeldig of verlopen.",
            )
    elif parsed.confirmation_token:
        return invalidate("unexpected_confirmation", "Voor deze selectie is geen bevestiging vereist.")

    quick_type = QUICK_MASK_TYPE_BY_KEY[parsed.requested_type]
    make_action_id = action_id_factory or (lambda: _default_opaque_id("manual_action"))
    action_id = str(make_action_id())
    if not 8 <= len(action_id) <= 160:
        return invalidate("invalid_action_id", "De handmatige actie kon niet veilig worden aangemaakt.")

    row = build_manual_mask_row(
        find_text=record.selection_text,
        manual_type=quick_type.manual_label,
        existing_rows=existing_rows,
        document_binding_id=document_binding_id,
    )
    row.update(
        {
            "entity_type": quick_type.entity_type,
            "source_label": "Handmatig uit tekst",
            "source": "manual_selection",
            "review_status": "manual",
            "review_status_label": "Handmatig uit tekst",
            "reason": "Handmatig toegevoegd vanuit tekstselectie",
            "context": "",
            "manual_action_id": action_id,
            "selection_event_id": record.inspect_event_id,
            "selection_commit_event_id": parsed.event_id,
            "selection_inspection_id": record.inspection_id,
            "selection_scope": REQUESTED_SCOPE,
            "selection_occurrence_count": record.occurrence_count,
        }
    )

    fingerprint = _row_fingerprint(row)
    action_record = ManualSelectionActionRecord(
        action_id=action_id,
        commit_event_id=parsed.event_id,
        inspect_event_id=record.inspect_event_id,
        inspection_id=record.inspection_id,
        document_scope_key=record.document_scope_key,
        find_text=record.selection_text,
        replace_with=str(row["replace_with"]),
        occurrence_count=record.occurrence_count,
        requested_type=parsed.requested_type,
        row=dict(row),
        row_fingerprint=fingerprint,
    )
    state.consume_inspection(record.inspection_id)
    return CommitResult(
        status="committed",
        event_id=parsed.event_id,
        message=_success_message(record.occurrence_count, quick_type.user_label),
        row=row,
        action_record=action_record,
    )


def undo_manual_selection_action(
    existing_rows: Iterable[Mapping[str, Any]] | Any | None,
    action_record: ManualSelectionActionRecord,
    *,
    current_document_scope_key: str,
) -> UndoResult:
    rows = _row_dicts(existing_rows)
    if current_document_scope_key != action_record.document_scope_key:
        return UndoResult(
            status="blocked",
            rows=tuple(rows),
            issue_code="wrong_document_scope",
            message="Ongedaan maken is niet beschikbaar voor een ander document.",
        )

    matching_indices = [
        index
        for index, row in enumerate(rows)
        if str(row.get("manual_action_id", "")) == action_record.action_id
    ]
    if len(matching_indices) != 1:
        return UndoResult(
            status="blocked",
            rows=tuple(rows),
            issue_code="action_row_missing",
            message="De handmatige actie kan niet meer veilig ongedaan worden gemaakt.",
        )

    index = matching_indices[0]
    current_row = rows[index]
    if _row_fingerprint(current_row) != action_record.row_fingerprint:
        return UndoResult(
            status="blocked",
            rows=tuple(rows),
            issue_code="action_row_changed",
            message="De handmatige rij is intussen gewijzigd en kan niet automatisch worden verwijderd.",
        )

    remaining = rows[:index] + rows[index + 1 :]
    return UndoResult(
        status="undone",
        rows=tuple(remaining),
        message="De handmatige maskering is ongedaan gemaakt.",
    )
