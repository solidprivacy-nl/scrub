"""Pure serial review queue helpers for SolidPrivacy Scrub.

WP_SERIAL_REVIEW_HELPER adds a small, report-only queue model for future
one-by-one review flows. This module does not change Streamlit UI behavior,
review table behavior, export behavior, Scrub Key schema, reinsert behavior,
recognizer behavior or document content.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable

VALID_SERIAL_REVIEW_STATES = {
    "needs_review",
    "accepted",
    "edited",
    "ignored",
    "manual_added",
    "preserve_context",
    "unresolved",
    "high_risk_unresolved",
}

UNRESOLVED_REVIEW_STATES = {"needs_review", "unresolved", "high_risk_unresolved"}

VALID_FILTER_MODES = {"all", "unresolved", "high_risk", "high_risk_unresolved"}

REPORT_ONLY = True
MUTATION_ALLOWED = False


def _clean_text(value: Any) -> str:
    return str(value or "").strip()


def _ordered_unique(values: Iterable[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value and value not in seen:
            ordered.append(value)
            seen.add(value)
    return tuple(ordered)


def _clean_risk_flags(value: Any) -> tuple[str, ...]:
    if value is None:
        return tuple()
    if isinstance(value, str):
        return _ordered_unique([_clean_text(value)])
    return _ordered_unique(_clean_text(flag) for flag in value)


def _clean_confidence(value: Any) -> float | None:
    if value is None or value == "":
        return None
    return float(value)


@dataclass(frozen=True)
class SerialReviewItem:
    """One report-only item in a future serial review queue.

    The item records review metadata only. It does not apply replacements, does
    not mutate review rows and does not write Scrub Key mappings.
    """

    occurrence_id: str
    source_text: str
    entity_type: str
    suggested_replacement: str
    review_state: str = "needs_review"
    confidence: float | None = None
    context_preview: str = ""
    risk_flags: tuple[str, ...] = field(default_factory=tuple)
    input_index: int = 0

    def __post_init__(self) -> None:
        if self.review_state not in VALID_SERIAL_REVIEW_STATES:
            raise ValueError(f"Unsupported review_state: {self.review_state}")
        if not _clean_text(self.occurrence_id):
            raise ValueError("occurrence_id is required")
        if not _clean_text(self.source_text):
            raise ValueError("source_text is required")
        if self.confidence is not None and not 0 <= self.confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")
        object.__setattr__(self, "occurrence_id", _clean_text(self.occurrence_id))
        object.__setattr__(self, "source_text", _clean_text(self.source_text))
        object.__setattr__(self, "entity_type", _clean_text(self.entity_type))
        object.__setattr__(self, "suggested_replacement", _clean_text(self.suggested_replacement))
        object.__setattr__(self, "context_preview", str(self.context_preview or ""))
        object.__setattr__(self, "risk_flags", _clean_risk_flags(self.risk_flags))

    @property
    def is_unresolved(self) -> bool:
        return self.review_state in UNRESOLVED_REVIEW_STATES

    @property
    def is_high_risk(self) -> bool:
        return self.review_state == "high_risk_unresolved" or bool(self.risk_flags)

    @property
    def is_high_risk_unresolved(self) -> bool:
        return self.is_unresolved and self.is_high_risk

    def as_dict(self) -> dict[str, Any]:
        return {
            "occurrence_id": self.occurrence_id,
            "source_text": self.source_text,
            "entity_type": self.entity_type,
            "suggested_replacement": self.suggested_replacement,
            "review_state": self.review_state,
            "confidence": self.confidence,
            "context_preview": self.context_preview,
            "risk_flags": list(self.risk_flags),
            "is_unresolved": self.is_unresolved,
            "is_high_risk": self.is_high_risk,
            "is_high_risk_unresolved": self.is_high_risk_unresolved,
            "input_index": self.input_index,
            "report_only": REPORT_ONLY,
            "mutation_allowed": MUTATION_ALLOWED,
        }


def build_serial_review_item(row: dict[str, Any], *, input_index: int = 0) -> SerialReviewItem:
    """Create a validated serial review item from one review-row dictionary."""

    return SerialReviewItem(
        occurrence_id=_clean_text(row.get("occurrence_id")),
        source_text=_clean_text(row.get("source_text")),
        entity_type=_clean_text(row.get("entity_type")),
        suggested_replacement=_clean_text(row.get("suggested_replacement")),
        review_state=_clean_text(row.get("review_state")) or "needs_review",
        confidence=_clean_confidence(row.get("confidence")),
        context_preview=str(row.get("context_preview") or ""),
        risk_flags=_clean_risk_flags(row.get("risk_flags")),
        input_index=input_index,
    )


def build_serial_review_items(rows: Iterable[dict[str, Any] | SerialReviewItem]) -> list[SerialReviewItem]:
    """Create serial review items while preserving original row order."""

    items: list[SerialReviewItem] = []
    for index, row in enumerate(rows):
        if isinstance(row, SerialReviewItem):
            items.append(row)
        else:
            items.append(build_serial_review_item(row, input_index=index))
    return items


def matching_exact_source_occurrence_ids(
    current_item: SerialReviewItem | dict[str, Any] | None,
    rows: Iterable[dict[str, Any] | SerialReviewItem],
) -> list[str]:
    """Return ids with exactly the same source_text as the current item.

    This is conservative exact matching only. It does not case-fold, collapse
    whitespace, normalize punctuation or guess user intent.
    """

    if current_item is None:
        return []
    item = current_item if isinstance(current_item, SerialReviewItem) else build_serial_review_item(current_item)
    all_items = build_serial_review_items(rows)
    return [candidate.occurrence_id for candidate in all_items if candidate.source_text == item.source_text]


def _priority(item: SerialReviewItem) -> tuple[int, int]:
    if item.is_high_risk_unresolved:
        return (0, item.input_index)
    if item.is_unresolved:
        return (1, item.input_index)
    return (2, item.input_index)


def _filtered_queue(items: Iterable[SerialReviewItem], filter_mode: str) -> list[SerialReviewItem]:
    if filter_mode not in VALID_FILTER_MODES:
        raise ValueError(f"Unsupported filter_mode: {filter_mode}")

    item_list = list(items)
    if filter_mode == "unresolved":
        item_list = [item for item in item_list if item.is_unresolved]
    elif filter_mode == "high_risk":
        item_list = [item for item in item_list if item.is_high_risk]
    elif filter_mode == "high_risk_unresolved":
        item_list = [item for item in item_list if item.is_high_risk_unresolved]

    return sorted(item_list, key=_priority)


def _resolve_current_index(
    queue_items: list[SerialReviewItem],
    *,
    current_index: int,
    current_occurrence_id: str | None,
) -> int | None:
    if not queue_items:
        return None
    if current_occurrence_id:
        clean_id = _clean_text(current_occurrence_id)
        for index, item in enumerate(queue_items):
            if item.occurrence_id == clean_id:
                return index
    return min(max(int(current_index), 0), len(queue_items) - 1)


def next_unresolved_item(queue_items: Iterable[SerialReviewItem], current_index: int | None) -> SerialReviewItem | None:
    """Return the next unresolved item after current_index without wrapping."""

    if current_index is None:
        return None
    items = list(queue_items)
    for item in items[current_index + 1 :]:
        if item.is_unresolved:
            return item
    return None


def previous_unresolved_item(queue_items: Iterable[SerialReviewItem], current_index: int | None) -> SerialReviewItem | None:
    """Return the previous unresolved item before current_index without wrapping."""

    if current_index is None:
        return None
    items = list(queue_items)
    for item in reversed(items[:current_index]):
        if item.is_unresolved:
            return item
    return None


def build_serial_review_audit(rows: Iterable[dict[str, Any] | SerialReviewItem]) -> dict[str, Any]:
    """Build a report-only audit summary for serial review rows."""

    items = build_serial_review_items(rows)
    state_counts = {state: 0 for state in sorted(VALID_SERIAL_REVIEW_STATES)}
    for item in items:
        state_counts[item.review_state] += 1

    duplicate_groups_by_value: dict[str, list[str]] = {}
    for item in items:
        duplicate_groups_by_value.setdefault(item.source_text, []).append(item.occurrence_id)
    duplicate_exact_value_groups = [
        {"occurrence_ids": ids, "count": len(ids)} for ids in duplicate_groups_by_value.values() if len(ids) > 1
    ]

    unresolved_ids = [item.occurrence_id for item in items if item.is_unresolved]
    high_risk_ids = [item.occurrence_id for item in items if item.is_high_risk]
    high_risk_unresolved_ids = [item.occurrence_id for item in items if item.is_high_risk_unresolved]

    if high_risk_unresolved_ids:
        review_readiness = "high_risk_unresolved"
    elif unresolved_ids:
        review_readiness = "review_recommended"
    else:
        review_readiness = "ready_for_export"

    return {
        "total_source_items": len(items),
        "state_counts": state_counts,
        "unresolved_count": len(unresolved_ids),
        "unresolved_occurrence_ids": unresolved_ids,
        "high_risk_count": len(high_risk_ids),
        "high_risk_occurrence_ids": high_risk_ids,
        "high_risk_unresolved_occurrence_ids": high_risk_unresolved_ids,
        "duplicate_exact_value_groups": duplicate_exact_value_groups,
        "review_readiness": review_readiness,
        "report_only": REPORT_ONLY,
        "mutation_allowed": MUTATION_ALLOWED,
        "export_blocking": False,
        "scrub_key_mapping_written": False,
    }


def build_serial_review_queue(
    rows: Iterable[dict[str, Any] | SerialReviewItem],
    *,
    current_index: int = 0,
    current_occurrence_id: str | None = None,
    filter_mode: str = "all",
) -> dict[str, Any]:
    """Build a stable, non-mutating serial review queue and audit summary."""

    all_items = build_serial_review_items(rows)
    queue_items = _filtered_queue(all_items, filter_mode)
    resolved_index = _resolve_current_index(
        queue_items,
        current_index=current_index,
        current_occurrence_id=current_occurrence_id,
    )
    current_item = None if resolved_index is None else queue_items[resolved_index]
    same_value_ids = matching_exact_source_occurrence_ids(current_item, all_items)
    audit = build_serial_review_audit(all_items)
    next_item = next_unresolved_item(queue_items, resolved_index)
    previous_item = previous_unresolved_item(queue_items, resolved_index)

    return {
        "items": [item.as_dict() for item in queue_items],
        "filter_mode": filter_mode,
        "total_items": len(queue_items),
        "total_source_items": len(all_items),
        "current_index": resolved_index,
        "current_item": None if current_item is None else current_item.as_dict(),
        "next_item": None if next_item is None else next_item.as_dict(),
        "previous_item": None if previous_item is None else previous_item.as_dict(),
        "unresolved_count": audit["unresolved_count"],
        "high_risk_count": audit["high_risk_count"],
        "duplicate_exact_value_count": len(same_value_ids),
        "same_value_occurrence_ids": same_value_ids,
        "audit_summary": audit,
        "report_only": REPORT_ONLY,
        "mutation_allowed": MUTATION_ALLOWED,
    }
