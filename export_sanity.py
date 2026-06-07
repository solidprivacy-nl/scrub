"""Advisory export sanity checks for Scrub Legal.

This helper prepares Dutch, user-facing warnings for the export step. It is
purely advisory: it does not block downloads, mutate review rows or change which
replacement rows are included in export.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from review_summary import (
    NEEDS_REVIEW,
    _is_checked,
    _lower,
    _normalise_rows,
    _row_status,
    build_review_summary,
)


CONTROL_NEEDED_WARNING = (
    "Let op: {count} regel(s) met 'Controle nodig' staan niet aangevinkt. "
    "Controleer deze waarden handmatig voordat u het bestand gebruikt."
)
CANDIDATE_NOT_INCLUDED_WARNING = (
    "Let op: {count} mogelijke kandidaatwaarde(n) worden niet meegenomen in de export. "
    "Niet-aangevinkte kandidaten blijven mogelijk zichtbaar in de uitvoer."
)
NO_REPLACEMENTS_WARNING = (
    "Er zijn geen vervangingen geselecteerd. De export kan daardoor gelijk blijven "
    "aan de invoer."
)
USER_REVIEW_REQUIRED_WARNING = (
    "Gebruikerscontrole blijft nodig: controleer het opgeschoonde document altijd zelf "
    "vóór gebruik of delen."
)
ADVISORY_EXPORT_WARNING = (
    "De export is een hulpmiddel en geen garantie op volledige anonimisering. "
    "Downloaden blijft mogelijk, maar de gebruiker blijft verantwoordelijk voor de eindcontrole."
)


def _to_int(value: Any) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def _is_export_summary(value: Any) -> bool:
    return isinstance(value, Mapping) and "total_rows" in value and "include" not in value


def _is_candidate_row(row: Mapping[str, Any]) -> bool:
    source = _lower(row.get("source"))
    candidate_marker = _lower(row.get("candidate"))
    return source == "candidate" or candidate_marker in {"1", "true", "yes", "ja"}


def _normalise_export_summary(summary: Mapping[str, Any]) -> dict[str, int | bool | str | dict[str, Any]]:
    review_summary = dict(summary.get("review_summary", summary))
    checked_rows = _to_int(summary.get("checked_rows_included_in_export", review_summary.get("checked_rows_included_in_export")))
    total_rows = _to_int(summary.get("total_rows", review_summary.get("total_rows")))
    unchecked_control_needed_rows = _to_int(
        summary.get("unchecked_control_needed_rows", review_summary.get("open_candidate_rows"))
    )
    candidate_rows_not_included = _to_int(
        summary.get("candidate_rows_not_included", review_summary.get("open_candidate_rows"))
    )

    normalised: dict[str, int | bool | str | dict[str, Any]] = {
        "total_rows": total_rows,
        "checked_rows_included_in_export": checked_rows,
        "unchecked_rows_excluded_from_export": _to_int(
            summary.get(
                "unchecked_rows_excluded_from_export",
                review_summary.get("unchecked_rows_excluded_from_export"),
            )
        ),
        "unchecked_control_needed_rows": unchecked_control_needed_rows,
        "candidate_rows_not_included": candidate_rows_not_included,
        "no_replacements_selected": bool(summary.get("no_replacements_selected", checked_rows == 0)),
        "user_review_required": True,
        "export_is_advisory": True,
        "blocks_export": False,
        "changes_export_semantics": False,
        "review_summary": review_summary,
    }
    normalised["ready_label"] = export_sanity_ready_label(normalised)
    return normalised


def build_export_sanity_checks(rows: Any) -> dict[str, int | bool | str | dict[str, Any]]:
    """Build advisory export sanity flags from replacement review rows.

    The returned flags are intended for warning text only. They must not be used
    to block downloads or to change export inclusion behavior.
    """
    records = _normalise_rows(rows)
    review_summary = build_review_summary(records)

    unchecked_control_needed_rows = sum(
        1
        for row in records
        if _row_status(row) == NEEDS_REVIEW and not _is_checked(row.get("include"))
    )
    candidate_rows_not_included = sum(
        1 for row in records if _is_candidate_row(row) and not _is_checked(row.get("include"))
    )
    checked_rows = _to_int(review_summary.get("checked_rows_included_in_export"))

    summary: dict[str, int | bool | str | dict[str, Any]] = {
        "total_rows": _to_int(review_summary.get("total_rows")),
        "checked_rows_included_in_export": checked_rows,
        "unchecked_rows_excluded_from_export": _to_int(
            review_summary.get("unchecked_rows_excluded_from_export")
        ),
        "unchecked_control_needed_rows": unchecked_control_needed_rows,
        "candidate_rows_not_included": candidate_rows_not_included,
        "no_replacements_selected": checked_rows == 0,
        "user_review_required": True,
        "export_is_advisory": True,
        "blocks_export": False,
        "changes_export_semantics": False,
        "review_summary": review_summary,
    }
    summary["ready_label"] = export_sanity_ready_label(summary)
    return summary


def _as_export_sanity_summary(summary_or_rows: Any) -> dict[str, int | bool | str | dict[str, Any]]:
    if _is_export_summary(summary_or_rows):
        return _normalise_export_summary(summary_or_rows)
    return build_export_sanity_checks(summary_or_rows)


def export_sanity_warnings(summary_or_rows: Any) -> list[str]:
    """Return Dutch user-facing warnings for the export step."""
    summary = _as_export_sanity_summary(summary_or_rows)
    warnings: list[str] = []

    unchecked_control_needed_rows = _to_int(summary.get("unchecked_control_needed_rows"))
    candidate_rows_not_included = _to_int(summary.get("candidate_rows_not_included"))

    if unchecked_control_needed_rows > 0:
        warnings.append(CONTROL_NEEDED_WARNING.format(count=unchecked_control_needed_rows))
    if candidate_rows_not_included > 0:
        warnings.append(CANDIDATE_NOT_INCLUDED_WARNING.format(count=candidate_rows_not_included))
    if bool(summary.get("no_replacements_selected")):
        warnings.append(NO_REPLACEMENTS_WARNING)

    warnings.append(USER_REVIEW_REQUIRED_WARNING)
    warnings.append(ADVISORY_EXPORT_WARNING)
    return warnings


def export_sanity_ready_label(summary_or_rows: Any) -> str:
    """Return a compact Dutch readiness label for advisory display."""
    if _is_export_summary(summary_or_rows):
        total_rows = _to_int(summary_or_rows.get("total_rows"))
        checked_rows = _to_int(summary_or_rows.get("checked_rows_included_in_export"))
        unchecked_control_needed_rows = _to_int(summary_or_rows.get("unchecked_control_needed_rows"))
        candidate_rows_not_included = _to_int(summary_or_rows.get("candidate_rows_not_included"))
        no_replacements_selected = bool(summary_or_rows.get("no_replacements_selected", checked_rows == 0))
    else:
        summary = build_export_sanity_checks(summary_or_rows)
        total_rows = _to_int(summary.get("total_rows"))
        checked_rows = _to_int(summary.get("checked_rows_included_in_export"))
        unchecked_control_needed_rows = _to_int(summary.get("unchecked_control_needed_rows"))
        candidate_rows_not_included = _to_int(summary.get("candidate_rows_not_included"))
        no_replacements_selected = bool(summary.get("no_replacements_selected"))

    if total_rows == 0:
        return "Geen vervangregels gevonden — controleer handmatig"
    if no_replacements_selected or checked_rows == 0:
        return "Geen vervangingen geselecteerd"
    if unchecked_control_needed_rows > 0 or candidate_rows_not_included > 0:
        return "Controle nodig vóór export"
    return "Klaar voor export na gebruikerscontrole"
