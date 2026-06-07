"""Pure Scrub Key model helpers for SolidPrivacy Scrub.

A Scrub Key is a local mapping between original values and scrubbed
placeholders. The helpers in this module deliberately avoid UI integration,
cloud processing, file-system persistence and time-based side effects.
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Mapping
from typing import Any

SCRUB_KEY_SCHEMA = "solidprivacy.scrub_key"
SCRUB_KEY_SCHEMA_VERSION = "1.0"

REQUIRED_ITEM_FIELDS = (
    "original_value",
    "placeholder",
    "entity_type",
    "type_label",
    "source",
    "review_status",
    "include_state",
    "timestamp",
)

TRUE_VALUES = {"1", "true", "yes", "ja", "y", "on", "checked", "aangevinkt", "included", "meenemen"}
FALSE_VALUES = {"0", "false", "no", "nee", "n", "off", "unchecked", "uit", "excluded", "niet meenemen"}

FIELD_ALIASES: dict[str, tuple[str, ...]] = {
    "original_value": (
        "original_value",
        "original",
        "found_text",
        "text",
        "Gevonden tekst",
        "gevonden_tekst",
    ),
    "placeholder": (
        "placeholder",
        "replacement",
        "replace_with",
        "scrubbed_value",
        "Vervangen door",
        "vervangen_door",
    ),
    "entity_type": (
        "entity_type",
        "entity",
        "type",
        "Entity Type",
        "Entiteitstype",
    ),
    "type_label": (
        "type_label",
        "user_facing_type_label",
        "display_label",
        "Type gegeven",
        "type_gegeven",
    ),
    "source": (
        "source",
        "Bron",
        "bron",
    ),
    "review_status": (
        "review_status",
        "review_status_label",
        "status",
        "Status",
    ),
    "include": (
        "include",
        "included",
        "include_state",
        "Meenemen",
        "meenemen",
    ),
    "timestamp": (
        "timestamp",
        "created_at",
        "reviewed_at",
        "updated_at",
        "Tijdstip",
        "tijdstip",
    ),
    "document_label": (
        "document_label",
        "project_label",
        "dossier_label",
        "Document",
        "Project",
        "Dossier",
    ),
}


def _normalise_rows(rows: Any) -> list[dict[str, Any]]:
    """Return review rows as dictionaries without importing pandas."""
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


def _first_text(row: Mapping[str, Any], field_name: str) -> str:
    for alias in FIELD_ALIASES[field_name]:
        if alias in row:
            return _text(row.get(alias))
    return ""


def _include_state(row: Mapping[str, Any]) -> str:
    raw_value = None
    for alias in FIELD_ALIASES["include"]:
        if alias in row:
            raw_value = row.get(alias)
            break

    if isinstance(raw_value, bool):
        return "included" if raw_value else "excluded"
    if raw_value is None:
        return "excluded"
    if isinstance(raw_value, (int, float)):
        return "included" if raw_value != 0 else "excluded"

    normalised = _lower(raw_value)
    if normalised in TRUE_VALUES:
        return "included"
    if normalised in FALSE_VALUES:
        return "excluded"
    return "excluded"


def build_scrub_key(rows: Any, document_label: str | None = None) -> dict[str, Any]:
    """Build a deterministic Scrub Key from reviewed replacement rows.

    Excluded rows are omitted by design. This keeps the first pure model aligned
    with current export semantics: only rows selected by the reviewer become part
    of the reversible mapping.
    """
    records = _normalise_rows(rows)
    fallback_document_label = _text(document_label) or None
    items: list[dict[str, Any]] = []

    for row in records:
        include_state = _include_state(row)
        if include_state != "included":
            continue

        item_document_label = _first_text(row, "document_label") or fallback_document_label
        item = {
            "original_value": _first_text(row, "original_value"),
            "placeholder": _first_text(row, "placeholder"),
            "entity_type": _first_text(row, "entity_type"),
            "type_label": _first_text(row, "type_label"),
            "source": _first_text(row, "source"),
            "review_status": _first_text(row, "review_status"),
            "include_state": include_state,
            "timestamp": _first_text(row, "timestamp"),
            "document_label": item_document_label,
        }
        items.append(item)

    return {
        "schema": SCRUB_KEY_SCHEMA,
        "schema_version": SCRUB_KEY_SCHEMA_VERSION,
        "workflow": "Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit",
        "privacy_model": "pseudonymization_not_full_anonymization",
        "reversible": True,
        "storage_policy": "local_only_protect_key",
        "external_ai_policy": "do_not_share_key_unless_explicitly_intended_and_allowed",
        "excluded_rows_policy": "omitted",
        "document_label": fallback_document_label,
        "item_count": len(items),
        "items": items,
    }


def scrub_key_to_json(scrub_key: Mapping[str, Any]) -> str:
    """Serialize a Scrub Key to stable, human-readable JSON."""
    return json.dumps(dict(scrub_key), ensure_ascii=False, indent=2, sort_keys=True)


def scrub_key_from_json(text: str) -> dict[str, Any]:
    """Load a Scrub Key JSON string into a dictionary."""
    loaded = json.loads(text)
    if not isinstance(loaded, dict):
        raise ValueError("Scrub Key JSON must contain an object at the top level.")
    return loaded


def validate_scrub_key(scrub_key: Any) -> list[str]:
    """Return validation messages for a Scrub Key.

    An empty list means the key is structurally valid. Validation is deliberately
    conservative and does not attempt to verify whether values are real PII.
    """
    issues: list[str] = []

    if not isinstance(scrub_key, Mapping):
        return ["Scrub Key must be a dictionary."]

    if scrub_key.get("schema") != SCRUB_KEY_SCHEMA:
        issues.append(f"Missing or invalid schema: expected {SCRUB_KEY_SCHEMA}.")
    if not scrub_key.get("schema_version"):
        issues.append("Missing schema_version.")
    if scrub_key.get("reversible") is not True:
        issues.append("Scrub Key must explicitly mark reversible=true.")
    if scrub_key.get("privacy_model") != "pseudonymization_not_full_anonymization":
        issues.append("Scrub Key must explicitly mark pseudonymization, not full anonymization.")
    if scrub_key.get("excluded_rows_policy") != "omitted":
        issues.append("Scrub Key must state excluded_rows_policy=omitted for this model version.")

    items = scrub_key.get("items")
    if not isinstance(items, list):
        issues.append("Missing or invalid items list.")
        return issues

    if scrub_key.get("item_count") != len(items):
        issues.append("item_count does not match the number of items.")

    for index, item in enumerate(items):
        if not isinstance(item, Mapping):
            issues.append(f"Item {index} must be a dictionary.")
            continue
        for field_name in REQUIRED_ITEM_FIELDS:
            if field_name not in item:
                issues.append(f"Item {index} missing required field: {field_name}.")
            elif _text(item.get(field_name)) == "":
                issues.append(f"Item {index} has empty required field: {field_name}.")
        if item.get("include_state") not in {"included", "excluded"}:
            issues.append(f"Item {index} has invalid include_state.")

    return issues
