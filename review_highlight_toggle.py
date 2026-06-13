"""Safe helpers for the review preview highlight toggle.

The helpers are deliberately display-only. They do not mutate review rows,
export payloads, Scrub Key state or reinsert state. They only prepare escaped
HTML for already masked/replaced values that are present in the preview text.
"""

from __future__ import annotations

import html
import re
from collections.abc import Iterable
from typing import Any


HIGHLIGHT_CSS = """
<style>
.sp-review-highlight-preview {
    background: #f8fafc;
    border: 1px solid #e5e7eb;
    border-radius: 0.5rem;
    padding: 0.75rem;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    line-height: 1.45;
}
.sp-review-highlight-token {
    background: #fef3c7;
    border: 1px solid #f59e0b;
    border-radius: 0.25rem;
    padding: 0.05rem 0.15rem;
}
.sp-review-highlight-token::before {
    content: "gemarkeerd";
    display: inline-block;
    font-size: 0.65rem;
    line-height: 1;
    margin-right: 0.25rem;
    padding: 0.05rem 0.15rem;
    border: 1px solid currentColor;
    border-radius: 0.2rem;
}
</style>
""".strip()


def _safe_text(value: Any) -> str:
    if value is None:
        return ""
    try:
        if value != value:  # NaN check without pandas dependency
            return ""
    except Exception:
        pass
    return str(value).strip()


def _safe_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    try:
        if value != value:  # NaN check without pandas dependency
            return False
    except Exception:
        pass
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"true", "1", "yes", "y", "checked", "ja"}


def _iter_rows(review_rows: Any) -> Iterable[dict[str, Any]]:
    if review_rows is None:
        return []
    if hasattr(review_rows, "iterrows"):
        return (dict(row) for _, row in review_rows.iterrows())
    return (dict(row) for row in review_rows or [])


def build_highlight_terms(review_rows: Any) -> list[str]:
    """Return exact replacement values that may be highlighted.

    Only included rows with both ``find`` and ``replace_with`` are eligible.
    The returned terms are de-duplicated and sorted longest-first to avoid a
    short replacement value splitting a longer exact replacement value.
    """

    seen: set[str] = set()
    terms: list[str] = []
    for row in _iter_rows(review_rows):
        if not _safe_bool(row.get("include", False)):
            continue
        find_text = _safe_text(row.get("find"))
        replace_text = _safe_text(row.get("replace_with"))
        if not find_text or not replace_text:
            continue
        if replace_text in seen:
            continue
        seen.add(replace_text)
        terms.append(replace_text)
    return sorted(terms, key=len, reverse=True)


def find_exact_highlight_spans(text: str, terms: Iterable[str]) -> list[tuple[int, int]]:
    """Find non-overlapping exact spans for highlight terms in raw text."""

    raw_text = _safe_text(text)
    spans: list[tuple[int, int]] = []
    for term in terms:
        safe_term = _safe_text(term)
        if not safe_term:
            continue
        for match in re.finditer(re.escape(safe_term), raw_text):
            candidate = (match.start(), match.end())
            if any(candidate[0] < existing_end and candidate[1] > existing_start for existing_start, existing_end in spans):
                continue
            spans.append(candidate)
    return sorted(spans)


def build_highlighted_preview_html(text: str, terms: Iterable[str]) -> str:
    """Build escaped HTML for a marked preview.

    The raw document text is never inserted into HTML unescaped. Only escaped
    fragments are wrapped in a static ``mark`` element.
    """

    raw_text = _safe_text(text)
    spans = find_exact_highlight_spans(raw_text, terms)
    if not spans:
        escaped_text = html.escape(raw_text)
        return f"{HIGHLIGHT_CSS}\n<div class=\"sp-review-highlight-preview\">{escaped_text}</div>"

    parts: list[str] = []
    cursor = 0
    for start, end in spans:
        parts.append(html.escape(raw_text[cursor:start]))
        parts.append(
            "<mark class=\"sp-review-highlight-token\" "
            "aria-label=\"gemarkeerde vervanging\">"
            f"{html.escape(raw_text[start:end])}"
            "</mark>"
        )
        cursor = end
    parts.append(html.escape(raw_text[cursor:]))
    return f"{HIGHLIGHT_CSS}\n<div class=\"sp-review-highlight-preview\">{''.join(parts)}</div>"
