"""Display-only compaction for document-bound placeholder tokens.

The helpers never mutate the source text or the schema-1.1 token. They provide a
short review alias plus exact UTF-16 source coordinates so interactive review can
remain server-authoritative and export/reinsert can keep the complete token.
"""

from __future__ import annotations

from html import escape
import re
from collections.abc import Iterable, Sequence
from typing import Any


_BOUND_PLACEHOLDER_RE = re.compile(
    r"\[(?P<label>[A-Z][A-Z0-9_]*?)_"
    r"(?P<binding_id>B[A-Z2-7]{16})"
    r"(?:_(?P<manual>HANDMATIG))?_"
    r"(?P<index>\d{2,})\]"
)


def _utf16_length(value: str) -> int:
    return len(value.encode("utf-16-le")) // 2


def compact_bound_placeholder_display(value: Any) -> str:
    """Return a short alias only for a strict full bound-placeholder token."""

    text = "" if value is None else str(value)
    match = _BOUND_PLACEHOLDER_RE.fullmatch(text)
    if match is None:
        return text
    manual = "_H" if match.group("manual") else ""
    return f"[{match.group('label')}{manual}_{match.group('index')}]"


def _normalize_highlight_spans(
    text: str,
    spans: Iterable[Sequence[int]] | None,
) -> list[tuple[int, int]]:
    normalized: list[tuple[int, int]] = []
    previous_end = 0
    for raw in spans or ():
        if isinstance(raw, (str, bytes)) or len(raw) != 2:
            raise ValueError("highlight span must contain start and end")
        start, end = raw
        if isinstance(start, bool) or isinstance(end, bool):
            raise ValueError("highlight span offsets must be integers")
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("highlight span offsets must be integers")
        if start < 0 or end <= start or end > len(text):
            raise ValueError("highlight span falls outside processed text")
        if normalized and start < previous_end:
            raise ValueError("highlight spans must be sorted and non-overlapping")
        normalized.append((start, end))
        previous_end = end
    return normalized


def _ranges_overlap(first_start: int, first_end: int, second_start: int, second_end: int) -> bool:
    return first_start < second_end and second_start < first_end


def build_bound_placeholder_display_segments(
    text: Any,
    highlight_spans: Iterable[Sequence[int]] | None = None,
) -> list[dict[str, Any]]:
    """Build lossless source/display segments with exact UTF-16 source offsets."""

    source = "" if text is None else str(text)
    highlights = _normalize_highlight_spans(source, highlight_spans)
    placeholders = [
        (match.start(), match.end(), match.group(0))
        for match in _BOUND_PLACEHOLDER_RE.finditer(source)
    ]

    boundaries = {0, len(source)}
    for start, end in highlights:
        boundaries.update((start, end))
    for start, end, _ in placeholders:
        boundaries.update((start, end))
    ordered = sorted(boundaries)

    segments: list[dict[str, Any]] = []
    for start, end in zip(ordered, ordered[1:]):
        if end <= start:
            continue
        source_text = source[start:end]
        placeholder = next(
            (
                token
                for token_start, token_end, token in placeholders
                if token_start == start and token_end == end
            ),
            None,
        )
        highlighted = any(
            _ranges_overlap(start, end, highlight_start, highlight_end)
            for highlight_start, highlight_end in highlights
        )
        display_text = (
            compact_bound_placeholder_display(placeholder)
            if placeholder is not None
            else source_text
        )
        segments.append(
            {
                "source_text": source_text,
                "display_text": display_text,
                "start": start,
                "end": end,
                "start_utf16": _utf16_length(source[:start]),
                "end_utf16": _utf16_length(source[:end]),
                "highlighted": highlighted,
                "compacted": placeholder is not None and display_text != source_text,
                "protected": highlighted or placeholder is not None,
                "full_placeholder": placeholder or "",
            }
        )

    if not segments:
        segments.append(
            {
                "source_text": "",
                "display_text": "",
                "start": 0,
                "end": 0,
                "start_utf16": 0,
                "end_utf16": 0,
                "highlighted": False,
                "compacted": False,
                "protected": False,
                "full_placeholder": "",
            }
        )
    return segments


def render_bound_placeholder_display_html(
    text: Any,
    highlight_spans: Iterable[Sequence[int]] | None = None,
) -> str:
    """Render escaped compact aliases while retaining full tokens as metadata."""

    parts: list[str] = []
    for segment in build_bound_placeholder_display_segments(text, highlight_spans):
        display_text = escape(str(segment["display_text"]))
        if not segment["compacted"] and not segment["highlighted"]:
            parts.append(display_text)
            continue

        full_placeholder = str(segment["full_placeholder"])
        compact_attributes = ""
        compact_class = ""
        if segment["compacted"]:
            compact_class = " sp-compact-placeholder"
            compact_attributes = (
                f' title="Volledige gebonden placeholder: {escape(full_placeholder)}"'
                f' aria-label="Gebonden placeholder, compact weergegeven als {display_text}"'
            )

        if segment["highlighted"]:
            parts.append(
                f'<mark class="sp-side-by-side-highlight-token{compact_class}"'
                f'{compact_attributes}>{display_text}</mark>'
            )
        else:
            parts.append(
                f'<span class="sp-compact-placeholder"{compact_attributes}>'
                f'{display_text}</span>'
            )
    return "".join(parts)
