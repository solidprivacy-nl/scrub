"""Pure Scrub Key import/reload helpers for SolidPrivacy Scrub.

This module prepares v13.2 import/reload without touching the Streamlit UI. It
parses a previously downloaded Scrub Key JSON string, validates it with the v13.0
model, and normalises the mappings into review-table-like rows for later UI and
reinsert work.

The helpers deliberately avoid file-system writes, server-side storage, cloud
processing and UI side effects.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any

from scrub_key import scrub_key_from_json, validate_scrub_key

IMPORT_PRIVACY_WARNING = (
    "Een Scrub Key maakt vervangen waarden lokaal herleidbaar. "
    "Gebruik dit bestand alleen lokaal en deel het niet met AI-diensten of derden "
    "tenzij dat bewust en toegestaan is."
)


def _text(value: Any) -> str:
    return str(value or "").strip()


def _validation_errors_for_text(json_text: Any) -> tuple[dict[str, Any] | None, list[str]]:
    """Parse and validate Scrub Key JSON text with safe user-facing errors."""
    if not isinstance(json_text, str) or _text(json_text) == "":
        return None, ["Scrub Key JSON ontbreekt of is leeg."]

    try:
        scrub_key = scrub_key_from_json(json_text)
    except json.JSONDecodeError:
        return None, ["Scrub Key JSON is geen geldige JSON."]
    except ValueError as exc:
        return None, [f"Scrub Key JSON heeft een ongeldig hoofdformaat: {exc}"]

    validation_issues = validate_scrub_key(scrub_key)
    if validation_issues:
        return scrub_key, [f"Scrub Key is niet geldig: {issue}" for issue in validation_issues]

    return scrub_key, []


def validate_scrub_key_import_text(json_text: Any) -> list[str]:
    """Return safe validation errors for a candidate Scrub Key JSON string."""
    _scrub_key, errors = _validation_errors_for_text(json_text)
    return errors


def normalise_scrub_key_items(scrub_key: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Convert Scrub Key items to review-table-like mapping rows.

    The normalised rows are intentionally simple and deterministic. They can be
    reused later by UI import/reload and deterministic reinsert helpers.
    """
    items = scrub_key.get("items")
    if not isinstance(items, list):
        return []

    rows: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, Mapping):
            continue
        rows.append(
            {
                "find": _text(item.get("original_value")),
                "replace_with": _text(item.get("placeholder")),
                "original_value": _text(item.get("original_value")),
                "placeholder": _text(item.get("placeholder")),
                "entity_type": _text(item.get("entity_type")),
                "type_label": _text(item.get("type_label")),
                "source": _text(item.get("source")),
                "review_status": _text(item.get("review_status")),
                "include": item.get("include_state") == "included",
                "include_state": _text(item.get("include_state")),
                "timestamp": _text(item.get("timestamp")),
                "document_label": _text(item.get("document_label"))
                or _text(scrub_key.get("document_label")),
            }
        )
    return rows


def build_scrub_key_import_result(json_text: Any) -> dict[str, Any]:
    """Parse, validate and normalise a Scrub Key JSON string.

    The return shape is deliberately UI-friendly while staying pure and
    side-effect free. `ok=True` means the Scrub Key is structurally valid and the
    `mapping_rows` can be used by later import/reload or reinsert work.
    """
    scrub_key, errors = _validation_errors_for_text(json_text)
    if errors:
        return {
            "ok": False,
            "errors": errors,
            "warnings": [IMPORT_PRIVACY_WARNING],
            "scrub_key": scrub_key,
            "mapping_rows": [],
            "item_count": 0,
            "reversible": False,
        }

    assert scrub_key is not None
    mapping_rows = normalise_scrub_key_items(scrub_key)
    return {
        "ok": True,
        "errors": [],
        "warnings": [IMPORT_PRIVACY_WARNING],
        "scrub_key": scrub_key,
        "mapping_rows": mapping_rows,
        "item_count": len(mapping_rows),
        "reversible": scrub_key.get("reversible") is True,
        "privacy_model": scrub_key.get("privacy_model"),
        "document_label": scrub_key.get("document_label"),
    }
