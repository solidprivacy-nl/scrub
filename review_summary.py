"""Final review summary helpers for Scrub Legal.

The export summary is a pure helper layer. It counts what is already selected for
export and what still needs human attention, without changing review rows or
export semantics.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

AUTO_DETECTED = "auto_detected"
NEEDS_REVIEW = "needs_review"
MANUAL = "manual"
REMEMBERED = "remembered"

STATUS_LABEL_AUTO_DETECTED = "Automatisch vervangen"
STATUS_LABEL_NEEDS_REVIEW = "Controle nodig"
STATUS_LABEL_MANUAL = "Handmatig toegevoegd"
STATUS_LABEL_REMEMBERED = "Onthouden vervanging"

TRUE_VALUES = {"1", "true", "yes", "ja", "y", "on", "checked", "aangevinkt"}
FALSE_VALUES = {"0", "false", "no", "nee", "n", "off", "unchecked", "uit"}


def _normalise_rows(rows: Any) -> list[dict[str, Any]]:
    """Return review rows as dictionaries.

    The Streamlit app works with pandas DataFrames, while tests and helper callers
    may pass a list of dictionaries. Keep this helper dependency-light by using
    duck typing instead of importing pandas.
    """
    if rows is None:
        return []
    if hasattr(rows, "to_dict"):
        try:
            records = rows.to_dict(orient="records")
            return [dict(row) for row in records]
        except TypeError:
            pass
    if isinstance(rows, Mapping):
        return [dict(rows)]
    if isinstance(rows, Iterable) and not isinstance(rows, (str, bytes)):
        return [dict(row) for row in rows if isinstance(row, Mapping)]
    return []


def _text(value: Any) -> str:
    return str(value or "").strip()


def _lower(value: Any) -> str:
    return _text(value).lower()


def _is_checked(value: Any) -> bool:
    """Interpret the include flag conservatively."""
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return value != 0
    normalised = _lower(value)
    if normalised in TRUE_VALUES:
        return True
    if normalised in FALSE_VALUES:
        return False
    return False


def _row_status(row: Mapping[str, Any]) -> str:
    """Infer the stable review status from status, label or source fields."""
    status = _lower(row.get("review_status"))
    if status in {AUTO_DETECTED, NEEDS_REVIEW, MANUAL, REMEMBERED}:
        return status

    label = _lower(row.get("review_status_label"))
    if label == STATUS_LABEL_AUTO_DETECTED.lower():
        return AUTO_DETECTED
    if label == STATUS_LABEL_NEEDS_REVIEW.lower():
        return NEEDS_REVIEW
    if label == STATUS_LABEL_MANUAL.lower():
        return MANUAL
    if label == STATUS_LABEL_REMEMBERED.lower():
        return REMEMBERED

    source = _lower(row.get("source"))
    entity_type = _text(row.get("entity_type")).upper()
    if source == "candidate":
        return NEEDS_REVIEW
    if source == "remembered" or entity_type == "REMEMBERED":
        return REMEMBERED
    if source == "manual" or entity_type == "MANUAL":
        return MANUAL
    if source == "detected":
        return AUTO_DETECTED
    return NEEDS_REVIEW


def build_review_summary(rows: Any) -> dict[str, int | bool | str]:
    """Build final export-readiness counts for the replacement table."""
    records = _normalise_rows(rows)
    statuses = [_row_status(row) for row in records]
    include_flags = [_is_checked(row.get("include")) for row in records]

    checked_rows = sum(1 for checked in include_flags if checked)
    unchecked_rows = len(records) - checked_rows
    open_candidate_rows = sum(
        1
        for row, status in zip(records, statuses)
        if status == NEEDS_REVIEW and not _is_checked(row.get("include"))
    )

    summary: dict[str, int | bool | str] = {
        "total_rows": len(records),
        "automatically_detected_rows": statuses.count(AUTO_DETECTED),
        "rows_needing_review": statuses.count(NEEDS_REVIEW),
        "manually_added_rows": statuses.count(MANUAL),
        "remembered_replacement_rows": statuses.count(REMEMBERED),
        "checked_rows_included_in_export": checked_rows,
        "unchecked_rows_excluded_from_export": unchecked_rows,
        "open_candidate_rows": open_candidate_rows,
        "open_candidate_warning": open_candidate_rows > 0,
    }
    summary["readiness_label"] = review_summary_readiness_label(summary)
    return summary


def review_summary_readiness_label(summary: Mapping[str, Any]) -> str:
    if int(summary.get("total_rows", 0) or 0) == 0:
        return "Geen vervangregels gevonden"
    if int(summary.get("checked_rows_included_in_export", 0) or 0) == 0:
        return "Niet klaar voor export"
    if bool(summary.get("open_candidate_warning")):
        return "Controle nodig voor export"
    return "Klaar voor export na gebruikerscontrole"


def review_summary_lines(summary: Mapping[str, Any]) -> list[str]:
    """Return short Dutch lines suitable for a Streamlit summary block."""
    lines = [
        f"Totaal aantal regels: {int(summary.get('total_rows', 0) or 0)}",
        f"Automatisch gevonden: {int(summary.get('automatically_detected_rows', 0) or 0)}",
        f"Controle nodig: {int(summary.get('rows_needing_review', 0) or 0)}",
        f"Handmatig toegevoegd: {int(summary.get('manually_added_rows', 0) or 0)}",
        f"Onthouden vervangingen: {int(summary.get('remembered_replacement_rows', 0) or 0)}",
        f"Meegenomen in export: {int(summary.get('checked_rows_included_in_export', 0) or 0)}",
        f"Niet meegenomen in export: {int(summary.get('unchecked_rows_excluded_from_export', 0) or 0)}",
    ]
    if bool(summary.get("open_candidate_warning")):
        lines.append(
            f"Let op: {int(summary.get('open_candidate_rows', 0) or 0)} mogelijke waarde(n) staan nog open voor controle."
        )
    return lines


def review_summary_markdown(summary: Mapping[str, Any]) -> str:
    return "\n".join(f"- {line}" for line in review_summary_lines(summary))
