"""Pure deterministic Scrub Key reinsert helpers for SolidPrivacy Scrub.

The helpers support explicit legacy v1.0 compatibility and document-bound v1.1
keys. Document/key binding is validated before any deterministic replacement.
They avoid Streamlit, AI, cloud processing, persistence and file-system writes.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Mapping
from typing import Any

from scrub_key import validate_scrub_key
from scrub_key_binding import (
    BOUND_SCHEMA_VERSION,
    validate_bound_scrub_key,
    validate_document_key_binding,
)

PLACEHOLDER_PATTERN = re.compile(r"\[[A-Z][A-Z0-9_:-]*_[0-9]+\]")


def _text(value: Any) -> str:
    return str(value or "")


def _normalised_text(value: Any) -> str:
    return str(value or "").strip()


def _items(scrub_key: Any) -> list[Mapping[str, Any]]:
    if not isinstance(scrub_key, Mapping):
        return []
    raw_items = scrub_key.get("items")
    if not isinstance(raw_items, list):
        return []
    return [item for item in raw_items if isinstance(item, Mapping)]


def _unique_sorted(values: list[str] | set[str]) -> list[str]:
    return sorted({value for value in values if value})


def _unique_in_order(values: list[str]) -> list[str]:
    result: list[str] = []
    for value in values:
        if value and value not in result:
            result.append(value)
    return result


def _scrub_key_structure_issues(scrub_key: Any) -> list[str]:
    if not isinstance(scrub_key, Mapping):
        return ["Scrub Key must be a dictionary."]
    if _normalised_text(scrub_key.get("schema_version")) == BOUND_SCHEMA_VERSION:
        return list(validate_bound_scrub_key(scrub_key).get("errors", []))
    return validate_scrub_key(scrub_key)


def detect_placeholders(text: Any) -> list[str]:
    """Return unique placeholder-looking tokens found in text."""

    return _unique_sorted(PLACEHOLDER_PATTERN.findall(_text(text)))


def build_reinsert_mapping(scrub_key: Any) -> dict[str, Any]:
    """Build a deterministic placeholder-to-original mapping from a supported key.

    Structurally invalid keys return an empty mapping. Excluded items are ignored.
    Duplicate placeholders are reported and excluded to avoid ambiguous restoration.
    """

    validation_issues = _scrub_key_structure_issues(scrub_key)
    items = _items(scrub_key)
    included_items = [item for item in items if item.get("include_state") == "included"]
    excluded_items = [item for item in items if item.get("include_state") != "included"]
    placeholders = [_normalised_text(item.get("placeholder")) for item in included_items]
    duplicate_placeholders = _unique_sorted(
        [placeholder for placeholder, count in Counter(placeholders).items() if count > 1]
    )

    if validation_issues:
        return {
            "mapping": {},
            "item_count": len(items),
            "active_item_count": 0,
            "excluded_item_count": len(excluded_items),
            "duplicate_placeholders": duplicate_placeholders,
            "validation_issues": validation_issues,
        }

    duplicate_set = set(duplicate_placeholders)
    mapping: dict[str, str] = {}
    for item in included_items:
        placeholder = _normalised_text(item.get("placeholder"))
        original_value = _text(item.get("original_value"))
        if not placeholder or placeholder in duplicate_set:
            continue
        mapping[placeholder] = original_value

    return {
        "mapping": mapping,
        "item_count": len(items),
        "active_item_count": len(included_items),
        "excluded_item_count": len(excluded_items),
        "duplicate_placeholders": duplicate_placeholders,
        "validation_issues": [],
    }


def _binding_fields(binding_result: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "binding_status": binding_result.get("binding_status", "invalid_bound_key"),
        "replacement_allowed": binding_result.get("replacement_allowed") is True,
        "verified_document_match": binding_result.get("verified_document_match") is True,
        "legacy_unbound": binding_result.get("legacy_unbound") is True,
        "binding_warnings": list(binding_result.get("warnings", [])),
        "document_binding_ids": list(binding_result.get("document_binding_ids", [])),
        "key_binding_id": _normalised_text(binding_result.get("key_binding_id")),
        "mapping_digest_valid": binding_result.get("mapping_digest_valid"),
    }


def reinsert_from_scrub_key(
    text: Any,
    scrub_key: Any,
    *,
    binding_text: Any | None = None,
) -> dict[str, Any]:
    """Reinsert original values only after document/key binding validation.

    ``binding_text`` lets document-level callers validate one combined supported
    text surface and then apply the already-approved key to individual text nodes.
    No replacement occurs for any fail-closed binding status.
    """

    original_text = _text(text)
    binding_surface = original_text if binding_text is None else _text(binding_text)
    binding_result = validate_document_key_binding(binding_surface, scrub_key)
    mapping_result = build_reinsert_mapping(scrub_key)
    mapping: dict[str, str] = dict(mapping_result.get("mapping", {}))
    duplicate_placeholders = list(mapping_result.get("duplicate_placeholders", []))
    placeholders_in_text = detect_placeholders(original_text)
    binding_fields = _binding_fields(binding_result)

    validation_issues = _unique_in_order(
        list(binding_result.get("errors", []))
        + list(mapping_result.get("validation_issues", []))
    )
    if not binding_fields["replacement_allowed"] or validation_issues:
        return {
            "text": original_text,
            "replacement_count": 0,
            "item_count": mapping_result.get("item_count", 0),
            "active_item_count": mapping_result.get("active_item_count", 0),
            "excluded_item_count": mapping_result.get("excluded_item_count", 0),
            "placeholders_not_found": [],
            "unknown_placeholders": placeholders_in_text,
            "duplicate_placeholders": duplicate_placeholders,
            "validation_issues": validation_issues,
            "reinserted": False,
            "local_only": True,
            "ai_processing": False,
            "cloud_processing": False,
            **binding_fields,
        }

    known_placeholders = set(mapping.keys())
    reinserted_text = original_text
    replacement_count = 0
    placeholders_not_found: list[str] = []

    for placeholder, original_value in mapping.items():
        occurrences = reinserted_text.count(placeholder)
        if occurrences == 0:
            placeholders_not_found.append(placeholder)
            continue
        reinserted_text = reinserted_text.replace(placeholder, original_value)
        replacement_count += occurrences

    ambiguous_placeholders = set(duplicate_placeholders)
    unknown_placeholders = _unique_sorted(
        set(placeholders_in_text) - known_placeholders - ambiguous_placeholders
    )

    return {
        "text": reinserted_text,
        "replacement_count": replacement_count,
        "item_count": mapping_result.get("item_count", 0),
        "active_item_count": mapping_result.get("active_item_count", 0),
        "excluded_item_count": mapping_result.get("excluded_item_count", 0),
        "placeholders_not_found": _unique_sorted(placeholders_not_found),
        "unknown_placeholders": unknown_placeholders,
        "duplicate_placeholders": duplicate_placeholders,
        "validation_issues": [],
        "reinserted": replacement_count > 0,
        "local_only": True,
        "ai_processing": False,
        "cloud_processing": False,
        **binding_fields,
    }
