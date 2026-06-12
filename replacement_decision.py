"""Pure replacement-decision helpers for SolidPrivacy Scrub.

WP_REPLACE_LOGIC_HELPER adds a small data model and audit helper for future
review/replace flows. This module does not change UI behavior, export behavior,
Scrub Key schema, placeholder format, recognizer behavior or document content.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable

VALID_REVIEW_STATES = {
    "needs_review",
    "accepted",
    "edited",
    "ignored",
    "manual_added",
    "preserve_context",
    "unresolved",
}

VALID_SCOPES = {
    "this_occurrence",
    "all_exact",
    "all_normalized",
}

NON_REPLACEMENT_STATES = {"ignored", "preserve_context", "unresolved", "needs_review"}
REPLACEMENT_STATES = {"accepted", "edited", "manual_added"}


def _clean_text(value: Any) -> str:
    return str(value or "").strip()


def normalize_match_text(value: Any) -> str:
    """Return a conservative normalized text key for explicit same-value matching.

    This is not fuzzy matching. It only case-folds and collapses whitespace so
    workers can later build explicit, reviewable same-value behavior without
    guessing user intent.
    """

    return " ".join(_clean_text(value).casefold().split())


def _ordered_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value and value not in seen:
            ordered.append(value)
            seen.add(value)
    return ordered


@dataclass(frozen=True)
class ReplacementDecision:
    """Review decision for one detected or manually added item.

    The class records review intent only. It does not apply replacements to a
    document and does not create Scrub Key mappings.
    """

    occurrence_id: str
    source_text: str
    entity_type: str
    display_label: str
    suggested_replacement: str
    final_replacement: str | None = None
    review_state: str = "needs_review"
    scope: str = "this_occurrence"
    confidence: float | None = None
    context_preview: str = ""
    origin: str = "system"
    risk_flags: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if self.review_state not in VALID_REVIEW_STATES:
            raise ValueError(f"Unsupported review_state: {self.review_state}")
        if self.scope not in VALID_SCOPES:
            raise ValueError(f"Unsupported scope: {self.scope}")
        if not _clean_text(self.occurrence_id):
            raise ValueError("occurrence_id is required")
        if not _clean_text(self.source_text):
            raise ValueError("source_text is required")
        if self.confidence is not None and not 0 <= self.confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")

    @property
    def replacement_value(self) -> str | None:
        """Return the replacement value implied by the decision, if any."""

        if self.review_state in NON_REPLACEMENT_STATES:
            return None
        if self.review_state == "edited" and self.final_replacement is not None:
            return self.final_replacement
        if self.final_replacement is not None and self.review_state in REPLACEMENT_STATES:
            return self.final_replacement
        return self.suggested_replacement

    @property
    def creates_mapping(self) -> bool:
        """Whether this decision may later be eligible for a Scrub Key mapping."""

        return self.replacement_value is not None

    def as_dict(self) -> dict[str, Any]:
        return {
            "occurrence_id": self.occurrence_id,
            "source_text": self.source_text,
            "entity_type": self.entity_type,
            "display_label": self.display_label,
            "suggested_replacement": self.suggested_replacement,
            "final_replacement": self.final_replacement,
            "review_state": self.review_state,
            "scope": self.scope,
            "confidence": self.confidence,
            "context_preview": self.context_preview,
            "origin": self.origin,
            "risk_flags": list(self.risk_flags),
            "replacement_value": self.replacement_value,
            "creates_mapping": self.creates_mapping,
        }


def build_replacement_decision(
    *,
    occurrence_id: str,
    source_text: str,
    entity_type: str,
    display_label: str,
    suggested_replacement: str,
    final_replacement: str | None = None,
    review_state: str = "needs_review",
    scope: str = "this_occurrence",
    confidence: float | None = None,
    context_preview: str = "",
    origin: str = "system",
    risk_flags: Iterable[Any] | None = None,
) -> ReplacementDecision:
    """Create a validated replacement decision from simple values."""

    flags = tuple(_ordered_unique(_clean_text(flag) for flag in (risk_flags or [])))
    return ReplacementDecision(
        occurrence_id=_clean_text(occurrence_id),
        source_text=_clean_text(source_text),
        entity_type=_clean_text(entity_type),
        display_label=_clean_text(display_label),
        suggested_replacement=_clean_text(suggested_replacement),
        final_replacement=None if final_replacement is None else str(final_replacement),
        review_state=review_state,
        scope=scope,
        confidence=confidence,
        context_preview=str(context_preview or ""),
        origin=_clean_text(origin) or "system",
        risk_flags=flags,
    )


def matching_occurrence_ids(
    decision: ReplacementDecision,
    occurrences: Iterable[dict[str, Any]],
) -> list[str]:
    """Return occurrence ids affected by a decision scope.

    Occurrences are dictionaries with at least ``occurrence_id`` and
    ``source_text``. The helper does not mutate them.
    """

    matches: list[str] = []
    for occurrence in occurrences:
        occurrence_id = _clean_text(occurrence.get("occurrence_id"))
        source_text = _clean_text(occurrence.get("source_text"))
        if not occurrence_id or not source_text:
            continue
        if decision.scope == "this_occurrence" and occurrence_id == decision.occurrence_id:
            matches.append(occurrence_id)
        elif decision.scope == "all_exact" and source_text == decision.source_text:
            matches.append(occurrence_id)
        elif decision.scope == "all_normalized" and normalize_match_text(source_text) == normalize_match_text(
            decision.source_text
        ):
            matches.append(occurrence_id)
    return matches


def build_replacement_audit(decisions: Iterable[ReplacementDecision]) -> dict[str, Any]:
    """Build a report-only summary of replacement decisions."""

    decision_list = list(decisions)
    state_counts = {state: 0 for state in sorted(VALID_REVIEW_STATES)}
    for decision in decision_list:
        state_counts[decision.review_state] += 1

    all_flags = _ordered_unique(flag for decision in decision_list for flag in decision.risk_flags)
    ignored_items = [decision.occurrence_id for decision in decision_list if decision.review_state == "ignored"]
    manual_additions = [
        decision.occurrence_id
        for decision in decision_list
        if decision.review_state == "manual_added" or decision.origin == "manual"
    ]
    context_preserved = [
        decision.occurrence_id for decision in decision_list if decision.review_state == "preserve_context"
    ]
    mapping_candidates = [decision.occurrence_id for decision in decision_list if decision.creates_mapping]
    unresolved = [
        decision.occurrence_id
        for decision in decision_list
        if decision.review_state in {"needs_review", "unresolved"}
    ]
    apply_to_same_value_actions = [
        decision.occurrence_id for decision in decision_list if decision.scope != "this_occurrence"
    ]

    if any(decision.review_state == "unresolved" for decision in decision_list):
        readiness = "high_risk_unresolved"
    elif any(decision.review_state == "needs_review" for decision in decision_list):
        readiness = "review_recommended"
    else:
        readiness = "ready_for_export"

    return {
        "total_decisions": len(decision_list),
        "state_counts": state_counts,
        "ignored_items": ignored_items,
        "manual_additions": manual_additions,
        "context_preserved": context_preserved,
        "mapping_candidates": mapping_candidates,
        "unresolved_items": unresolved,
        "apply_to_same_value_actions": apply_to_same_value_actions,
        "risk_flags": all_flags,
        "export_readiness": readiness,
        "report_only": True,
        "export_blocking": False,
    }
