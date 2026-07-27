"""Pure helpers for creating document-bound Scrub Key export artifacts.

The helpers keep Streamlit/session details outside the binding model. They do not
modify arbitrary custom replacement values: only recognised legacy or bound
placeholder tokens are losslessly rebound to the active document ID.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any

from scrub_key import build_scrub_key
from scrub_key_binding import (
    BINDING_VERSION,
    BOUND_SCHEMA_VERSION,
    MAPPING_DIGEST_ALGORITHM,
    build_bound_placeholder,
    compute_mapping_digest,
    generate_document_binding_id,
    parse_bound_placeholder,
    validate_document_binding_id,
)

SESSION_BINDING_IDS_KEY = "document_binding_ids"

_LEGACY_MANUAL_PLACEHOLDER_RE = re.compile(
    r"^\[(?P<label>[A-Z][A-Z0-9_]*?)_HANDMATIG_(?P<index>\d{2,})\]$"
)
_LEGACY_AUTOMATIC_PLACEHOLDER_RE = re.compile(
    r"^\[(?P<label>[A-Z][A-Z0-9_]*?)_(?P<index>\d{2,})\]$"
)


def document_binding_id_for_scope(
    state: Any,
    scope_key: Any,
    *,
    random_bytes: bytes | None = None,
) -> str:
    """Return one stable local binding ID for a source-text scope."""

    if not hasattr(state, "get") or not hasattr(state, "__setitem__"):
        raise TypeError("state must provide mapping-style get and item assignment.")
    scope = str(scope_key or "").strip()
    if not scope:
        raise ValueError("scope_key cannot be empty.")

    raw_mapping = state.get(SESSION_BINDING_IDS_KEY, {})
    mapping = dict(raw_mapping) if isinstance(raw_mapping, Mapping) else {}
    existing = str(mapping.get(scope, "")).strip()
    if existing and not validate_document_binding_id(existing):
        return existing

    binding_id = generate_document_binding_id(random_bytes=random_bytes)
    mapping[scope] = binding_id
    state[SESSION_BINDING_IDS_KEY] = mapping
    return binding_id


def bind_existing_placeholder(value: Any, document_binding_id: str) -> str | None:
    """Rebind a recognised placeholder token; leave free replacement text alone."""

    token = str(value or "").strip()
    parsed = parse_bound_placeholder(token)
    if parsed is not None:
        return build_bound_placeholder(
            parsed["entity_label"],
            parsed["index"],
            document_binding_id,
            manual=parsed["manual"],
        )

    manual_match = _LEGACY_MANUAL_PLACEHOLDER_RE.fullmatch(token)
    if manual_match is not None:
        return build_bound_placeholder(
            manual_match.group("label"),
            int(manual_match.group("index")),
            document_binding_id,
            manual=True,
        )

    automatic_match = _LEGACY_AUTOMATIC_PLACEHOLDER_RE.fullmatch(token)
    if automatic_match is not None:
        return build_bound_placeholder(
            automatic_match.group("label"),
            int(automatic_match.group("index")),
            document_binding_id,
        )
    return None


def build_bound_scrub_key(
    rows: Any,
    *,
    document_binding_id: str,
    document_label: str | None = None,
) -> dict[str, Any]:
    """Build a schema-1.1 key from current reviewed export rows."""

    binding_errors = validate_document_binding_id(document_binding_id)
    if binding_errors:
        raise ValueError(binding_errors[0])

    scrub_key = build_scrub_key(rows, document_label=document_label)
    scrub_key["schema_version"] = BOUND_SCHEMA_VERSION
    scrub_key["binding_version"] = BINDING_VERSION
    scrub_key["document_binding_id"] = document_binding_id
    scrub_key["mapping_digest_algorithm"] = MAPPING_DIGEST_ALGORITHM
    scrub_key["mapping_digest"] = compute_mapping_digest(scrub_key)
    return scrub_key
