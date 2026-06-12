"""Placeholder validation helpers for SolidPrivacy Scrub.

This module supports the future robust placeholder format proposed in WP31:
``[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]``.

The helpers are deliberately additive. They do not generate production
placeholders, do not migrate legacy placeholders, do not change Scrub Key schema,
do not call AI/cloud services and do not change reinsert behavior.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import re
from typing import Literal

ROBUST_PLACEHOLDER_PREFIX = "[[SP_"
ROBUST_PLACEHOLDER_SUFFIX = "]]"
ROBUST_INTEGRITY_VERSION = "solidprivacy.placeholder.robust.v1"

ENTITY_PATTERN = re.compile(r"^[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*$")
COUNTER_PATTERN = re.compile(r"^[0-9]{4}$")
INTEGRITY_PATTERN = re.compile(r"^[A-F0-9]{4}$")
LEGACY_PLACEHOLDER_PATTERN = re.compile(r"^\[[A-Z][A-Z0-9_:-]*_[0-9]+\]$")

PlaceholderKind = Literal[
    "robust",
    "legacy",
    "malformed_robust",
    "unknown_placeholder_like",
    "not_placeholder_like",
]


@dataclass(frozen=True)
class PlaceholderValidationResult:
    """Structured result for placeholder classification/validation."""

    raw: str
    kind: PlaceholderKind
    is_valid: bool
    entity_type: str | None = None
    counter: str | None = None
    integrity: str | None = None
    expected_integrity: str | None = None
    issues: tuple[str, ...] = ()


def _text(value: object) -> str:
    return str(value or "").strip()


def is_legacy_placeholder(value: object) -> bool:
    """Return True for the current legacy placeholder shape only.

    Legacy placeholders remain a compatibility mode. This helper does not migrate
    them or reinterpret them as robust placeholders.
    """

    return bool(LEGACY_PLACEHOLDER_PATTERN.fullmatch(_text(value)))


def normalise_counter(counter: int | str) -> str:
    """Return a four-digit counter string for non-sensitive metadata."""

    if isinstance(counter, int):
        counter_text = f"{counter:04d}"
    else:
        counter_text = _text(counter)

    if not COUNTER_PATTERN.fullmatch(counter_text) or counter_text == "0000":
        raise ValueError("counter must be a four-digit string from 0001 to 9999")
    return counter_text


def validate_entity_type(entity_type: object) -> str:
    """Return a normalized entity type or raise ValueError."""

    entity_text = _text(entity_type)
    if not ENTITY_PATTERN.fullmatch(entity_text):
        raise ValueError("entity_type must use uppercase ASCII segments separated by underscores")
    return entity_text


def compute_integrity_token(entity_type: object, counter: int | str) -> str:
    """Return a deterministic four-hex integrity token.

    The token is derived only from non-sensitive placeholder metadata: the robust
    placeholder validation version, the stable technical entity type and the
    counter. It must not be derived directly from original sensitive values.

    This is a lightweight corruption-detection token, not cryptographic
    authenticity or Scrub Key tamper protection.
    """

    entity_text = validate_entity_type(entity_type)
    counter_text = normalise_counter(counter)
    material = f"{ROBUST_INTEGRITY_VERSION}|SP|{entity_text}|{counter_text}".encode("ascii")
    return hashlib.sha256(material).hexdigest().upper()[:4]


def _looks_placeholder_like(value: str) -> bool:
    return (
        value.startswith("[")
        or value.endswith("]")
        or value.startswith("{{")
        or value.endswith("}}")
        or value.startswith("⟦")
        or value.endswith("⟧")
    )


def _parse_robust_inner(raw: str) -> tuple[str | None, str | None, str | None, list[str]]:
    issues: list[str] = []

    if not raw.startswith("[["):
        issues.append("missing_opening_double_bracket")
    if not raw.endswith(ROBUST_PLACEHOLDER_SUFFIX):
        issues.append("missing_closing_double_bracket")

    inner = raw[2:-2] if raw.startswith("[[") and raw.endswith("]]") else raw[2:]
    if not inner.startswith("SP_"):
        issues.append("invalid_prefix")
        return None, None, None, issues

    body = inner[3:]
    parts = body.split("_")
    if len(parts) < 3:
        issues.append("missing_segments")
        return None, None, None, issues

    entity_type = "_".join(parts[:-2])
    counter = parts[-2]
    integrity = parts[-1]

    if not ENTITY_PATTERN.fullmatch(entity_type):
        issues.append("invalid_entity")
    if not COUNTER_PATTERN.fullmatch(counter) or counter == "0000":
        issues.append("invalid_counter")
    if not INTEGRITY_PATTERN.fullmatch(integrity):
        issues.append("invalid_integrity")

    return entity_type, counter, integrity, issues


def validate_robust_placeholder(value: object) -> PlaceholderValidationResult:
    """Validate a robust placeholder candidate without changing product behavior."""

    raw = _text(value)
    entity_type, counter, integrity, issues = _parse_robust_inner(raw)
    expected_integrity: str | None = None

    if entity_type and counter and not {"invalid_entity", "invalid_counter"}.intersection(issues):
        expected_integrity = compute_integrity_token(entity_type, counter)
        if integrity and INTEGRITY_PATTERN.fullmatch(integrity) and integrity != expected_integrity:
            issues.append("integrity_mismatch")

    kind: PlaceholderKind = "robust" if not issues else "malformed_robust"
    return PlaceholderValidationResult(
        raw=raw,
        kind=kind,
        is_valid=not issues,
        entity_type=entity_type,
        counter=counter,
        integrity=integrity,
        expected_integrity=expected_integrity,
        issues=tuple(issues),
    )


def classify_placeholder(value: object) -> PlaceholderValidationResult:
    """Classify a placeholder-like value without mutating or repairing it."""

    raw = _text(value)
    if raw.startswith("[["):
        if raw.startswith(ROBUST_PLACEHOLDER_PREFIX) or raw.endswith("]]"):
            return validate_robust_placeholder(raw)
        return PlaceholderValidationResult(raw=raw, kind="unknown_placeholder_like", is_valid=False)

    if is_legacy_placeholder(raw):
        return PlaceholderValidationResult(raw=raw, kind="legacy", is_valid=True)

    if raw.startswith(ROBUST_PLACEHOLDER_PREFIX):
        return validate_robust_placeholder(raw)

    if _looks_placeholder_like(raw):
        return PlaceholderValidationResult(raw=raw, kind="unknown_placeholder_like", is_valid=False)

    return PlaceholderValidationResult(raw=raw, kind="not_placeholder_like", is_valid=False)
