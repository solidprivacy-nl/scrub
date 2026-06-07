"""Pure deterministic Scrub Key reinsert helpers for SolidPrivacy Scrub.

These helpers prepare the v13.3 local reinsert workflow. They deliberately avoid
Streamlit UI integration, AI calls, cloud processing, document export changes,
file-system persistence and any other side effects.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Mapping
from typing import Any

from scrub_key import validate_scrub_key

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


def detect_placeholders(text: Any) -> list[str]:
    """Return unique placeholder-looking tokens found in text.

    This is intentionally conservative and aimed at Scrub placeholders such as
    ``[PERSOON_1]`` or ``[ZAAKNUMMER_1]``. It does not attempt to parse arbitrary
    bracketed text.
    """
    return _unique_sorted(PLACEHOLDER_PATTERN.findall(_text(text)))


def build_reinsert_mapping(scrub_key: Any) -> dict[str, Any]:
    """Build a deterministic placeholder-to-original mapping from a Scrub Key.

    Invalid Scrub Keys return validation issues and an empty mapping. Items with
    ``include_state`` other than ``included`` are ignored. Duplicate placeholders
    are reported and excluded from the mapping to avoid ambiguous reinsertion.
    """
    validation_issues = validate_scrub_key(scrub_key)
    items = _items(scrub_key)
    included_items = [item for item in items if item.get("include_state") == "included"]
    excluded_items = [item for item in items if item.get("include_state") != "included"]

    if validation_issues:
        return {
            "mapping": {},
            "item_count": len(items),
            "active_item_count": 0,
            "excluded_item_count": len(excluded_items),
            "duplicate_placeholders": [],
            "validation_issues": validation_issues,
        }

    placeholders = [_normalised_text(item.get("placeholder")) for item in included_items]
    duplicate_placeholders = _unique_sorted(
        [placeholder for placeholder, count in Counter(placeholders).items() if count > 1]
    )
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


def reinsert_from_scrub_key(text: Any, scrub_key: Any) -> dict[str, Any]:
    """Reinsert original values into scrubbed text using a valid Scrub Key.

    The function is deterministic and side-effect free. It returns both the
    reinserted text and an audit summary. Invalid keys do not modify the text;
    validation issues are returned clearly.
    """
    original_text = _text(text)
    mapping_result = build_reinsert_mapping(scrub_key)
    mapping: dict[str, str] = dict(mapping_result.get("mapping", {}))
    validation_issues = list(mapping_result.get("validation_issues", []))
    duplicate_placeholders = list(mapping_result.get("duplicate_placeholders", []))

    placeholders_in_text = detect_placeholders(original_text)
    known_placeholders = set(mapping.keys())

    if validation_issues:
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
        }

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
    }
