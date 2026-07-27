"""Pure Scrub Key import/reload helpers for SolidPrivacy Scrub.

This module parses previously downloaded Scrub Key JSON, validates both explicit
legacy v1.0 keys and document-bound v1.1 keys, and normalises mappings for the
local reinsert workflow. It avoids file-system writes, server-side storage,
cloud processing and UI side effects.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any

from scrub_key import scrub_key_from_json, validate_scrub_key
from scrub_key_binding import (
    BOUND_SCHEMA_VERSION,
    LEGACY_SCHEMA_VERSION,
    validate_bound_scrub_key,
)

IMPORT_PRIVACY_WARNING = (
    "Een Scrub Key maakt vervangen waarden lokaal herleidbaar. "
    "Gebruik dit bestand alleen lokaal en deel het niet met AI-diensten of derden "
    "tenzij dat bewust en toegestaan is."
)


def _text(value: Any) -> str:
    return str(value or "").strip()


def validate_scrub_key_structure(scrub_key: Any) -> list[str]:
    """Validate one supported Scrub Key version without document matching.

    Legacy v1.0 uses the established model. Bound v1.1 uses the frozen binding,
    item and canonical-digest validation. Unsupported versions remain rejected.
    """

    if not isinstance(scrub_key, Mapping):
        return ["Scrub Key must be a dictionary."]

    schema_version = _text(scrub_key.get("schema_version"))
    if schema_version == BOUND_SCHEMA_VERSION:
        return list(validate_bound_scrub_key(scrub_key).get("errors", []))
    return validate_scrub_key(scrub_key)


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

    validation_issues = validate_scrub_key_structure(scrub_key)
    if validation_issues:
        return scrub_key, [f"Scrub Key is niet geldig: {issue}" for issue in validation_issues]

    return scrub_key, []


def validate_scrub_key_import_text(json_text: Any) -> list[str]:
    """Return safe validation errors for a candidate Scrub Key JSON string."""

    _scrub_key, errors = _validation_errors_for_text(json_text)
    return errors


def normalise_scrub_key_items(scrub_key: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Convert Scrub Key items to review-table-like mapping rows."""

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
    """Parse, validate and normalise one supported Scrub Key JSON string."""

    scrub_key, errors = _validation_errors_for_text(json_text)
    schema_version = _text(scrub_key.get("schema_version")) if isinstance(scrub_key, Mapping) else ""
    if errors:
        return {
            "ok": False,
            "errors": errors,
            "warnings": [IMPORT_PRIVACY_WARNING],
            "scrub_key": scrub_key,
            "mapping_rows": [],
            "item_count": 0,
            "reversible": False,
            "schema_version": schema_version,
            "legacy_unbound": schema_version == LEGACY_SCHEMA_VERSION,
            "key_binding_id": "",
            "mapping_digest_valid": None,
        }

    assert scrub_key is not None
    mapping_rows = normalise_scrub_key_items(scrub_key)
    bound_validation = (
        validate_bound_scrub_key(scrub_key)
        if schema_version == BOUND_SCHEMA_VERSION
        else None
    )
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
        "schema_version": schema_version,
        "legacy_unbound": schema_version == LEGACY_SCHEMA_VERSION,
        "key_binding_id": (
            bound_validation.get("key_binding_id", "") if bound_validation else ""
        ),
        "mapping_digest_valid": (
            bound_validation.get("mapping_digest_valid") if bound_validation else None
        ),
    }
