"""Helper logic for adding a manually supplied replacement row.

This module is deliberately Streamlit-free so the MVP manual mask entry can be
unit-tested without touching UI state. Tests use synthetic examples only.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Any, Iterable
import re


MANUAL_MASK_TYPE_TO_ENTITY_TYPE = {
    "Persoon": "PERSON",
    "Organisatie": "ORGANIZATION",
    "Zaaknummer": "NL_LEGAL_CASE_NUMBER",
    "Dossiernummer": "NL_DOSSIER_NUMBER",
    "Datum": "DATE_TIME",
    "Anders": "MANUAL",
}

MANUAL_MASK_TYPE_OPTIONS = tuple(MANUAL_MASK_TYPE_TO_ENTITY_TYPE.keys())

_ENTITY_TYPE_TO_TYPE_LABEL = {
    "PERSON": "Naam / persoon",
    "ORGANIZATION": "Organisatie",
    "NL_LEGAL_CASE_NUMBER": "Zaaknummer",
    "NL_DOSSIER_NUMBER": "Dossiernummer",
    "DATE_TIME": "Datum/tijd",
    "MANUAL": "Handmatige vervanging",
}

_ENTITY_TYPE_TO_PLACEHOLDER_PREFIX = {
    "PERSON": "PERSOON",
    "ORGANIZATION": "ORGANISATIE",
    "NL_LEGAL_CASE_NUMBER": "ZAAKNUMMER",
    "NL_DOSSIER_NUMBER": "DOSSIERNUMMER",
    "DATE_TIME": "DATUM",
    "MANUAL": "WAARDE",
}


@dataclass(frozen=True)
class ManualMaskValidation:
    """Validation result for a manually supplied replacement value."""

    is_valid: bool
    message: str = ""


def normalise_manual_mask_value(value: Any) -> str:
    """Strip only outer whitespace; keep the inner text exact for replacement."""

    if value is None:
        return ""
    return str(value).strip()


def manual_type_to_entity_type(manual_type: str | None) -> str:
    """Map a user-facing manual mask type to the replacement-table entity type."""

    return MANUAL_MASK_TYPE_TO_ENTITY_TYPE.get((manual_type or "").strip(), "MANUAL")


def manual_type_label(manual_type: str | None) -> str:
    """Return a user-facing type label for the replacement table."""

    entity_type = manual_type_to_entity_type(manual_type)
    return _ENTITY_TYPE_TO_TYPE_LABEL.get(entity_type, "Handmatige vervanging")


def manual_mask_document_key(text: str | None) -> str:
    """Return a stable short key so manual rows stay scoped to the current text."""

    return sha256((text or "").encode("utf-8")).hexdigest()[:16]


def _row_dicts(existing_rows: Iterable[dict[str, Any]] | Any | None) -> list[dict[str, Any]]:
    if existing_rows is None:
        return []
    if hasattr(existing_rows, "to_dict"):
        try:
            return [dict(row) for row in existing_rows.to_dict("records")]
        except TypeError:
            pass
    return [dict(row) for row in existing_rows]


def build_manual_placeholder(manual_type: str | None, existing_rows: Iterable[dict[str, Any]] | Any | None = None) -> str:
    """Build a stable placeholder such as ``[PERSOON_HANDMATIG_01]``."""

    entity_type = manual_type_to_entity_type(manual_type)
    prefix = _ENTITY_TYPE_TO_PLACEHOLDER_PREFIX.get(entity_type, "WAARDE")
    pattern = re.compile(rf"^\[{re.escape(prefix)}_HANDMATIG_(\d+)\]$")
    max_seen = 0
    for row in _row_dicts(existing_rows):
        match = pattern.match(str(row.get("replace_with", "")).strip())
        if match:
            max_seen = max(max_seen, int(match.group(1)))
    return f"[{prefix}_HANDMATIG_{max_seen + 1:02d}]"


def validate_manual_mask_input(
    value: Any,
    *,
    source_text: str | None = None,
    existing_find_values: Iterable[str] | None = None,
) -> ManualMaskValidation:
    """Validate whether a manual value can be added to the replacement table."""

    find_text = normalise_manual_mask_value(value)
    if not find_text:
        return ManualMaskValidation(False, "Vul eerst de gemiste waarde in.")

    existing_values = {normalise_manual_mask_value(item) for item in (existing_find_values or [])}
    if find_text in existing_values:
        return ManualMaskValidation(False, "Deze waarde staat al in de vervangtabel.")

    if source_text is not None and find_text not in source_text:
        return ManualMaskValidation(False, "Deze waarde staat niet in de huidige tekst.")

    return ManualMaskValidation(True, "")


def build_manual_mask_row(
    *,
    find_text: Any,
    manual_type: str | None = None,
    replace_with: Any = None,
    existing_rows: Iterable[dict[str, Any]] | Any | None = None,
) -> dict[str, Any]:
    """Build a replacement-table row for a manually added value."""

    value = normalise_manual_mask_value(find_text)
    if not value:
        raise ValueError("Manual mask value cannot be empty")

    entity_type = manual_type_to_entity_type(manual_type)
    replacement = normalise_manual_mask_value(replace_with) or build_manual_placeholder(manual_type, existing_rows)

    return {
        "include": True,
        "remember": False,
        "find": value,
        "replace_with": replacement,
        "type_label": manual_type_label(manual_type),
        "entity_type": entity_type,
        "confidence": "",
        "score": None,
        "source_label": "Handmatig",
        "source": "manual",
        "review_status": "manual",
        "review_status_label": "Handmatig toegevoegd",
        "review_order": 30,
        "reason": "Handmatig toegevoegd",
        "context": "",
    }
