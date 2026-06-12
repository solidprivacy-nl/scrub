"""Pure placeholder audit helpers for SolidPrivacy Scrub.

WP33 uses the WP32 placeholder validation helper to classify placeholder-like
text without changing deterministic reinsert behavior. The helpers in this file
do not repair, rewrite, migrate or generate production placeholders.
"""

from __future__ import annotations

from collections.abc import Iterable
import re
from typing import Any

from placeholder_validation import PlaceholderValidationResult, classify_placeholder

ROBUST_OR_TRUNCATED_PATTERN = re.compile(r"\[\[[^\s\[\]]+(?:\]\]|\])?")
LEGACY_OR_CHANGED_PATTERN = re.compile(r"(?<!\[)\[[A-Za-z][A-Za-z0-9_:\-]*_[0-9]+\](?!\])")
CURLY_PLACEHOLDER_PATTERN = re.compile(r"\{\{[^{}\s]+\}\}")


def _text(value: Any) -> str:
    return str(value or "")


def _normalised_set(values: Iterable[Any] | None) -> set[str]:
    if values is None:
        return set()
    return {str(value).strip() for value in values if str(value or "").strip()}


def _unique_in_order(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value and value not in seen:
            ordered.append(value)
            seen.add(value)
    return ordered


def detect_placeholder_like_tokens(text: Any) -> list[str]:
    """Return placeholder-like tokens without attempting repair or guessing."""

    source = _text(text)
    matches: list[tuple[int, int, str]] = []
    for pattern in (ROBUST_OR_TRUNCATED_PATTERN, LEGACY_OR_CHANGED_PATTERN, CURLY_PLACEHOLDER_PATTERN):
        matches.extend((match.start(), match.end(), match.group(0)) for match in pattern.finditer(source))

    matches.sort(key=lambda item: (item[0], -(item[1] - item[0])))
    selected: list[tuple[int, int, str]] = []
    for start, end, token in matches:
        if any(start >= kept_start and end <= kept_end for kept_start, kept_end, _ in selected):
            continue
        selected.append((start, end, token))

    return _unique_in_order(token for _, _, token in selected)


def _issue_entry(result: PlaceholderValidationResult) -> dict[str, Any]:
    return {
        "placeholder": result.raw,
        "kind": result.kind,
        "issues": list(result.issues),
        "expected_integrity": result.expected_integrity,
    }


def audit_placeholders(text: Any, expected_placeholders: Iterable[Any] | None = None) -> dict[str, Any]:
    """Classify placeholder-like text for audit output.

    ``expected_placeholders`` may contain placeholders from a Scrub Key. When it is
    supplied, observed placeholder-like tokens that are not expected are reported
    as unknown, but they are not repaired or rewritten.
    """

    tokens = detect_placeholder_like_tokens(text)
    expected = _normalised_set(expected_placeholders)
    classified = [classify_placeholder(token) for token in tokens]

    legacy_placeholders = [result.raw for result in classified if result.kind == "legacy"]
    robust_placeholders = [result.raw for result in classified if result.kind == "robust"]
    malformed_robust_placeholders = [
        result.raw for result in classified if result.kind == "malformed_robust"
    ]
    integrity_failed_placeholders = [
        result.raw
        for result in classified
        if result.kind == "malformed_robust"
        and any(issue in result.issues for issue in ("integrity_mismatch", "invalid_integrity"))
    ]

    unknown_placeholder_like_tokens = [
        result.raw for result in classified if result.kind == "unknown_placeholder_like"
    ]
    if expected:
        unknown_placeholder_like_tokens.extend(
            result.raw
            for result in classified
            if result.kind in {"legacy", "robust"} and result.raw not in expected
        )

    placeholder_validation_issues = [
        _issue_entry(result)
        for result in classified
        if result.kind in {"malformed_robust", "unknown_placeholder_like"}
    ]
    if expected:
        placeholder_validation_issues.extend(
            {
                "placeholder": result.raw,
                "kind": result.kind,
                "issues": ["unknown_placeholder"],
                "expected_integrity": result.expected_integrity,
            }
            for result in classified
            if result.kind in {"legacy", "robust"} and result.raw not in expected
        )

    missing_placeholders = sorted(expected - set(tokens)) if expected else []

    return {
        "placeholder_format_summary": {
            "observed_placeholder_like_count": len(tokens),
            "legacy_count": len(legacy_placeholders),
            "robust_count": len(robust_placeholders),
            "malformed_robust_count": len(malformed_robust_placeholders),
            "integrity_failed_count": len(integrity_failed_placeholders),
            "unknown_placeholder_like_count": len(_unique_in_order(unknown_placeholder_like_tokens)),
            "missing_expected_count": len(missing_placeholders),
        },
        "observed_placeholder_like_tokens": tokens,
        "legacy_placeholders": legacy_placeholders,
        "robust_placeholders": robust_placeholders,
        "malformed_robust_placeholders": malformed_robust_placeholders,
        "integrity_failed_placeholders": integrity_failed_placeholders,
        "unknown_placeholder_like_tokens": _unique_in_order(unknown_placeholder_like_tokens),
        "missing_placeholders": missing_placeholders,
        "placeholder_validation_issues": placeholder_validation_issues,
    }
