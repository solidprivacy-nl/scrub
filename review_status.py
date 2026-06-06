"""Review status model for the Scrub replacement table.

This module separates user-facing review state from recognizer internals. The
recognizer may know entity types, scores and sources; the legal user needs a
simple answer: is this already applied, does it need review, is it manual, or is
it remembered from earlier work?
"""

from __future__ import annotations

from typing import Any


AUTO_DETECTED = "auto_detected"
NEEDS_REVIEW = "needs_review"
MANUAL = "manual"
REMEMBERED = "remembered"

STATUS_LABELS_NL = {
    AUTO_DETECTED: "Automatisch vervangen",
    NEEDS_REVIEW: "Controle nodig",
    MANUAL: "Handmatig toegevoegd",
    REMEMBERED: "Onthouden vervanging",
}

STATUS_SORT_ORDER = {
    NEEDS_REVIEW: 10,
    AUTO_DETECTED: 20,
    MANUAL: 30,
    REMEMBERED: 40,
}


def review_status_for_source(source: str | None, entity_type: str | None = None, score: Any = None) -> str:
    """Return the stable review status for a replacement-table row.

    Source remains the primary signal:
    - candidate rows are review-only and should not be silently applied;
    - detected rows are already selected for replacement;
    - manual rows were added by the user;
    - remembered rows come from reusable memory.

    Score/entity_type are accepted for future extension, but v12.1 deliberately
    keeps the model simple and predictable.
    """
    normalised_source = (source or "").strip().lower()
    normalised_entity = (entity_type or "").strip().upper()

    if normalised_source == "candidate":
        return NEEDS_REVIEW
    if normalised_source == "remembered" or normalised_entity == "REMEMBERED":
        return REMEMBERED
    if normalised_source == "manual" or normalised_entity == "MANUAL":
        return MANUAL
    if normalised_source == "detected":
        return AUTO_DETECTED
    return NEEDS_REVIEW


def review_status_label(status: str | None) -> str:
    return STATUS_LABELS_NL.get(status or "", "Controle nodig")


def review_status_order(status: str | None) -> int:
    return STATUS_SORT_ORDER.get(status or "", STATUS_SORT_ORDER[NEEDS_REVIEW])
