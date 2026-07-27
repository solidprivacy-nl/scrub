"""Pure document/Scrub-Key binding model helpers.

The helpers in this module implement the frozen Phase 6 binding contract without
integrating it into current placeholder generation, Scrub Key export, reinsert
execution or Streamlit. They are deterministic when callers inject random bytes,
do not write files and do not access AI, cloud or network services.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
import secrets
from collections import Counter
from collections.abc import Mapping
from typing import Any

from scrub_key import SCRUB_KEY_SCHEMA, validate_scrub_key

LEGACY_SCHEMA_VERSION = "1.0"
BOUND_SCHEMA_VERSION = "1.1"
BINDING_VERSION = "1"
MAPPING_DIGEST_ALGORITHM = "sha256"
BINDING_RANDOM_BYTES = 10

BINDING_ID_RE = re.compile(r"^B[A-Z2-7]{16}$")
ENTITY_LABEL_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
BOUND_PLACEHOLDER_RE = re.compile(
    r"^\[(?P<label>[A-Z][A-Z0-9_]*?)_"
    r"(?P<binding_id>B[A-Z2-7]{16})"
    r"(?:_(?P<manual>HANDMATIG))?_"
    r"(?P<index>\d{2,})\]$"
)
BOUND_PLACEHOLDER_SEARCH_RE = re.compile(
    r"\[(?P<label>[A-Z][A-Z0-9_]*?)_"
    r"(?P<binding_id>B[A-Z2-7]{16})"
    r"(?:_(?P<manual>HANDMATIG))?_"
    r"(?P<index>\d{2,})\]"
)
LOWERCASE_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

BOUND_REQUIRED_ITEM_FIELDS = (
    "original_value",
    "placeholder",
    "entity_type",
    "type_label",
    "source",
    "review_status",
    "include_state",
    "timestamp",
)

BOUND_REQUIRED_POLICIES = {
    "privacy_model": "pseudonymization_not_full_anonymization",
    "reversible": True,
    "storage_policy": "local_only_protect_key",
    "external_ai_policy": "do_not_share_key_unless_explicitly_intended_and_allowed",
    "excluded_rows_policy": "omitted",
}

LEGACY_UNBOUND_WARNING = (
    "Legacy Scrub Key v1.0: document/key matching cannot be verified. "
    "Use only the key that belongs to this document and review the restored result."
)


def _text(value: Any) -> str:
    return str(value or "")


def _stripped(value: Any) -> str:
    return _text(value).strip()


def generate_document_binding_id(random_bytes: bytes | None = None) -> str:
    """Generate a local non-sensitive binding ID.

    Ten random bytes encode to exactly sixteen RFC 4648 base32 symbols. Tests can
    inject those bytes; normal callers receive cryptographically strong local
    randomness from :mod:`secrets`.
    """
    payload = secrets.token_bytes(BINDING_RANDOM_BYTES) if random_bytes is None else random_bytes
    if not isinstance(payload, bytes):
        raise TypeError("random_bytes must be bytes.")
    if len(payload) != BINDING_RANDOM_BYTES:
        raise ValueError(f"random_bytes must contain exactly {BINDING_RANDOM_BYTES} bytes.")
    encoded = base64.b32encode(payload).decode("ascii").rstrip("=")
    binding_id = f"B{encoded}"
    if validate_document_binding_id(binding_id):
        raise ValueError("Generated document binding ID does not match the contract.")
    return binding_id


def validate_document_binding_id(value: Any) -> list[str]:
    """Return validation errors for a document binding ID."""
    candidate = _stripped(value)
    if not candidate:
        return ["Document binding ID is missing."]
    if BINDING_ID_RE.fullmatch(candidate) is None:
        return ["Document binding ID must match B[A-Z2-7]{16}."]
    return []


def _validate_entity_label(value: Any) -> str:
    label = _stripped(value)
    if ENTITY_LABEL_RE.fullmatch(label) is None:
        raise ValueError("entity_label must start with A-Z and contain only A-Z, 0-9 or underscore.")
    return label


def _validate_index(value: Any) -> int:
    if isinstance(value, bool):
        raise ValueError("index must be a positive integer.")
    if isinstance(value, int):
        index = value
    elif isinstance(value, str) and value.strip().isdigit():
        index = int(value.strip())
    else:
        raise ValueError("index must be a positive integer.")
    if index < 1:
        raise ValueError("index must be a positive integer.")
    return index


def build_bound_placeholder(
    entity_label: Any,
    index: Any,
    document_binding_id: Any,
    manual: bool = False,
) -> str:
    """Build one automatic or manual placeholder using the frozen grammar."""
    label = _validate_entity_label(entity_label)
    validated_index = _validate_index(index)
    binding_id = _stripped(document_binding_id)
    binding_errors = validate_document_binding_id(binding_id)
    if binding_errors:
        raise ValueError(binding_errors[0])
    if not isinstance(manual, bool):
        raise TypeError("manual must be a boolean.")
    manual_segment = "_HANDMATIG" if manual else ""
    return f"[{label}_{binding_id}{manual_segment}_{validated_index:02d}]"


def parse_bound_placeholder(token: Any) -> dict[str, Any] | None:
    """Parse a complete bound placeholder, returning ``None`` for any near miss."""
    candidate = _text(token)
    match = BOUND_PLACEHOLDER_RE.fullmatch(candidate)
    if match is None:
        return None
    return {
        "placeholder": candidate,
        "entity_label": match.group("label"),
        "document_binding_id": match.group("binding_id"),
        "manual": match.group("manual") == "HANDMATIG",
        "index": int(match.group("index")),
        "index_text": match.group("index"),
    }


def extract_document_binding_ids(text: Any) -> list[str]:
    """Return sorted unique binding IDs from strict bound placeholders in text."""
    return sorted(
        {
            match.group("binding_id")
            for match in BOUND_PLACEHOLDER_SEARCH_RE.finditer(_text(text))
        }
    )


def canonical_mapping_digest_payload(scrub_key: Mapping[str, Any]) -> dict[str, Any]:
    """Return the exact canonical payload frozen by the binding contract."""
    if not isinstance(scrub_key, Mapping):
        raise ValueError("Scrub Key must be a mapping.")
    raw_items = scrub_key.get("items")
    if not isinstance(raw_items, list):
        raise ValueError("Scrub Key items must be a list.")

    canonical_items: list[dict[str, Any]] = []
    for index, item in enumerate(raw_items):
        if not isinstance(item, Mapping):
            raise ValueError(f"Scrub Key item {index} must be a mapping.")
        canonical_items.append(
            {
                "placeholder": _text(item.get("placeholder")),
                "original_value": _text(item.get("original_value")),
                "entity_type": _text(item.get("entity_type")),
                "include_state": _text(item.get("include_state")),
            }
        )

    canonical_items.sort(
        key=lambda item: (
            item["placeholder"],
            item["original_value"],
            item["entity_type"],
        )
    )

    return {
        "schema": scrub_key.get("schema"),
        "schema_version": scrub_key.get("schema_version"),
        "privacy_model": scrub_key.get("privacy_model"),
        "reversible": scrub_key.get("reversible"),
        "storage_policy": scrub_key.get("storage_policy"),
        "external_ai_policy": scrub_key.get("external_ai_policy"),
        "excluded_rows_policy": scrub_key.get("excluded_rows_policy"),
        "binding_version": scrub_key.get("binding_version"),
        "document_binding_id": scrub_key.get("document_binding_id"),
        "item_count": scrub_key.get("item_count"),
        "items": canonical_items,
    }


def compute_mapping_digest(scrub_key: Mapping[str, Any]) -> str:
    """Compute the canonical SHA-256 mapping digest."""
    payload = canonical_mapping_digest_payload(scrub_key)
    serialized = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def _bound_validation_result(
    *,
    errors: list[str],
    error_codes: list[str],
    warnings: list[str],
    key_binding_id: str,
    mapping_digest_valid: bool | None,
) -> dict[str, Any]:
    return {
        "ok": not errors,
        "errors": errors,
        "error_codes": error_codes,
        "warnings": warnings,
        "key_binding_id": key_binding_id,
        "mapping_digest_valid": mapping_digest_valid,
    }


def validate_bound_scrub_key(scrub_key: Any) -> dict[str, Any]:
    """Validate a schema-1.1 bound Scrub Key and its canonical digest."""
    errors: list[str] = []
    error_codes: list[str] = []
    warnings: list[str] = []

    def add_error(code: str, message: str) -> None:
        if code not in error_codes:
            error_codes.append(code)
        errors.append(message)

    if not isinstance(scrub_key, Mapping):
        add_error("invalid_bound_key", "Scrub Key must be a mapping.")
        return _bound_validation_result(
            errors=errors,
            error_codes=error_codes,
            warnings=warnings,
            key_binding_id="",
            mapping_digest_valid=None,
        )

    if scrub_key.get("schema") != SCRUB_KEY_SCHEMA:
        add_error("invalid_bound_key", f"Bound Scrub Key schema must be {SCRUB_KEY_SCHEMA}.")
    if scrub_key.get("schema_version") != BOUND_SCHEMA_VERSION:
        add_error("invalid_bound_key", f"Bound Scrub Key schema_version must be {BOUND_SCHEMA_VERSION}.")
    if scrub_key.get("binding_version") != BINDING_VERSION:
        add_error("invalid_bound_key", f"binding_version must be {BINDING_VERSION}.")

    key_binding_id = _stripped(scrub_key.get("document_binding_id"))
    binding_errors = validate_document_binding_id(key_binding_id)
    for message in binding_errors:
        add_error("invalid_bound_key", message)

    for field_name, expected_value in BOUND_REQUIRED_POLICIES.items():
        if scrub_key.get(field_name) != expected_value:
            add_error(
                "invalid_bound_key",
                f"{field_name} must equal {expected_value!r} for a bound Scrub Key.",
            )

    if scrub_key.get("mapping_digest_algorithm") != MAPPING_DIGEST_ALGORITHM:
        add_error("invalid_bound_key", "mapping_digest_algorithm must be sha256.")

    supplied_digest = _stripped(scrub_key.get("mapping_digest"))
    if LOWERCASE_SHA256_RE.fullmatch(supplied_digest) is None:
        add_error("invalid_mapping_digest", "mapping_digest must contain 64 lowercase hexadecimal characters.")

    items = scrub_key.get("items")
    items_are_mappings = isinstance(items, list) and all(isinstance(item, Mapping) for item in items)
    if not isinstance(items, list):
        add_error("invalid_bound_key", "Bound Scrub Key items must be a list.")
        items = []
    if scrub_key.get("item_count") != len(items):
        add_error("invalid_bound_key", "item_count does not match the number of items.")

    placeholders: list[str] = []
    for index, item in enumerate(items):
        if not isinstance(item, Mapping):
            add_error("invalid_bound_key", f"Item {index} must be a mapping.")
            continue
        for field_name in BOUND_REQUIRED_ITEM_FIELDS:
            if field_name not in item:
                add_error("invalid_bound_key", f"Item {index} missing required field: {field_name}.")
            elif _stripped(item.get(field_name)) == "":
                add_error("invalid_bound_key", f"Item {index} has empty required field: {field_name}.")
        if item.get("include_state") != "included":
            add_error("invalid_bound_key", f"Item {index} must have include_state=included.")

        placeholder = _stripped(item.get("placeholder"))
        placeholders.append(placeholder)
        parsed = parse_bound_placeholder(placeholder)
        if parsed is None:
            add_error("invalid_bound_key", f"Item {index} placeholder is not a valid bound placeholder.")
        elif key_binding_id and parsed["document_binding_id"] != key_binding_id:
            add_error(
                "invalid_bound_key",
                f"Item {index} placeholder binding ID does not match document_binding_id.",
            )

    for placeholder, count in Counter(placeholders).items():
        if placeholder and count > 1:
            add_error("invalid_bound_key", f"Duplicate bound placeholder: {placeholder}.")

    mapping_digest_valid: bool | None = None
    if items_are_mappings:
        try:
            expected_digest = compute_mapping_digest(scrub_key)
        except ValueError as exc:
            add_error("invalid_bound_key", str(exc))
        else:
            mapping_digest_valid = supplied_digest == expected_digest
            if not mapping_digest_valid and "invalid_mapping_digest" not in error_codes:
                add_error("invalid_mapping_digest", "mapping_digest does not match the canonical mapping payload.")

    return _bound_validation_result(
        errors=errors,
        error_codes=error_codes,
        warnings=warnings,
        key_binding_id=key_binding_id,
        mapping_digest_valid=mapping_digest_valid,
    )


def _binding_result(
    *,
    status: str,
    replacement_allowed: bool,
    verified_document_match: bool,
    legacy_unbound: bool,
    errors: list[str],
    warnings: list[str],
    document_binding_ids: list[str],
    key_binding_id: str,
    mapping_digest_valid: bool | None,
) -> dict[str, Any]:
    return {
        "ok": replacement_allowed and not errors,
        "binding_status": status,
        "replacement_allowed": replacement_allowed,
        "verified_document_match": verified_document_match,
        "legacy_unbound": legacy_unbound,
        "errors": errors,
        "warnings": warnings,
        "document_binding_ids": document_binding_ids,
        "key_binding_id": key_binding_id,
        "mapping_digest_valid": mapping_digest_valid,
    }


def validate_document_key_binding(text: Any, scrub_key: Any) -> dict[str, Any]:
    """Validate document/key binding before any deterministic replacement occurs."""
    document_binding_ids = extract_document_binding_ids(text)

    if not isinstance(scrub_key, Mapping):
        return _binding_result(
            status="invalid_bound_key",
            replacement_allowed=False,
            verified_document_match=False,
            legacy_unbound=False,
            errors=["Scrub Key must be a mapping."],
            warnings=[],
            document_binding_ids=document_binding_ids,
            key_binding_id="",
            mapping_digest_valid=None,
        )

    schema_version = _stripped(scrub_key.get("schema_version"))
    if schema_version == LEGACY_SCHEMA_VERSION:
        legacy_errors = validate_scrub_key(scrub_key)
        if legacy_errors:
            return _binding_result(
                status="invalid_bound_key",
                replacement_allowed=False,
                verified_document_match=False,
                legacy_unbound=True,
                errors=legacy_errors,
                warnings=[],
                document_binding_ids=document_binding_ids,
                key_binding_id="",
                mapping_digest_valid=None,
            )
        if document_binding_ids:
            return _binding_result(
                status="legacy_key_for_bound_document",
                replacement_allowed=False,
                verified_document_match=False,
                legacy_unbound=True,
                errors=["A legacy unbound Scrub Key cannot be used with bound document placeholders."],
                warnings=[LEGACY_UNBOUND_WARNING],
                document_binding_ids=document_binding_ids,
                key_binding_id="",
                mapping_digest_valid=None,
            )
        return _binding_result(
            status="legacy_unbound",
            replacement_allowed=True,
            verified_document_match=False,
            legacy_unbound=True,
            errors=[],
            warnings=[LEGACY_UNBOUND_WARNING],
            document_binding_ids=[],
            key_binding_id="",
            mapping_digest_valid=None,
        )

    bound_validation = validate_bound_scrub_key(scrub_key)
    key_binding_id = bound_validation.get("key_binding_id", "")
    if not bound_validation.get("ok"):
        error_codes = set(bound_validation.get("error_codes", []))
        status = "invalid_mapping_digest" if error_codes == {"invalid_mapping_digest"} else "invalid_bound_key"
        return _binding_result(
            status=status,
            replacement_allowed=False,
            verified_document_match=False,
            legacy_unbound=False,
            errors=list(bound_validation.get("errors", [])),
            warnings=list(bound_validation.get("warnings", [])),
            document_binding_ids=document_binding_ids,
            key_binding_id=key_binding_id,
            mapping_digest_valid=bound_validation.get("mapping_digest_valid"),
        )

    if not document_binding_ids:
        return _binding_result(
            status="missing_document_binding",
            replacement_allowed=False,
            verified_document_match=False,
            legacy_unbound=False,
            errors=["No bound document placeholder was found for this bound Scrub Key."],
            warnings=[],
            document_binding_ids=[],
            key_binding_id=key_binding_id,
            mapping_digest_valid=True,
        )

    if len(document_binding_ids) > 1:
        return _binding_result(
            status="mixed_document_bindings",
            replacement_allowed=False,
            verified_document_match=False,
            legacy_unbound=False,
            errors=["The document contains placeholders from multiple document binding IDs."],
            warnings=[],
            document_binding_ids=document_binding_ids,
            key_binding_id=key_binding_id,
            mapping_digest_valid=True,
        )

    if document_binding_ids[0] != key_binding_id:
        return _binding_result(
            status="binding_mismatch",
            replacement_allowed=False,
            verified_document_match=False,
            legacy_unbound=False,
            errors=["The document binding ID does not match the Scrub Key binding ID."],
            warnings=[],
            document_binding_ids=document_binding_ids,
            key_binding_id=key_binding_id,
            mapping_digest_valid=True,
        )

    return _binding_result(
        status="bound_match",
        replacement_allowed=True,
        verified_document_match=True,
        legacy_unbound=False,
        errors=[],
        warnings=[],
        document_binding_ids=document_binding_ids,
        key_binding_id=key_binding_id,
        mapping_digest_valid=True,
    )
