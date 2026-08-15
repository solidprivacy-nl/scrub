"""Fail-safe precision resolver for Dutch address recognizer spans.

The base recognizer intentionally has broad recall. This resolver only narrows an
``NL_ADDRESS`` result when a stricter Dutch street + house-number expression is
found *inside* the already-recognized span. If no strict subspan can be proven,
the original result is preserved unchanged so recall cannot silently decrease.
"""

from __future__ import annotations

from copy import copy
import re
from typing import Iterable, List


_STREET_SUFFIX = (
    r"straat|laan|weg|plein|dreef|hof|kade|singel|gracht|steeg|park|"
    r"boulevard|pad|plantsoen"
)
_WORD = r"[A-Za-zÀ-ÖØ-öø-ÿ'’\-]+"
_TITLE_WORD = r"[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÖØ-öø-ÿ'’\-]*"
_PARTICLE = r"(?:van|de|der|den|ten|ter|het)"
_DESCRIPTOR = (
    r"(?:Oude|Nieuwe|Lange|Korte|Grote|Kleine|Hoge|Lage|Noorder|Zuider|"
    r"Ooster|Wester)"
)
_HOUSE_NUMBER = r"\d{1,5}(?:[A-Za-z]{1,3}|[-/]\d{1,4})?"
_POSTCODE = r"[1-9][0-9]{3}\s?[A-Z]{2}"
_CITY = rf"{_TITLE_WORD}(?:[ \t]+(?:{_PARTICLE}|{_TITLE_WORD})){{0,3}}"

# Prefix-street names such as ``Laan van Meerdervoort 55`` are explicit and
# therefore evaluated before suffix-street forms.
_PREFIX_ADDRESS_RE = re.compile(
    rf"\b(?:Straat|Laan|Weg|Plein|Dreef|Hof|Kade|Singel|Gracht|Steeg|Park|Boulevard|Pad|Plantsoen)"
    rf"(?:[ \t]+(?:{_PARTICLE}|{_TITLE_WORD})){{1,5}}"
    rf"[ \t]+{_HOUSE_NUMBER}"
    rf"(?:[ \t]*,?[ \t]*{_POSTCODE}(?:[ \t\r\n]+{_CITY})?)?\b"
)

# Suffix-street names are deliberately conservative. The previous recognizer
# allowed up to three arbitrary words before the suffix, which let sentence
# context become part of the address. We accept a single suffix token, plus one
# small, explicit descriptor class used in ordinary Dutch street names.
_SUFFIX_ADDRESS_RE = re.compile(
    rf"\b(?:{_DESCRIPTOR}[ \t]+)?{_WORD}(?:{_STREET_SUFFIX})"
    rf"[ \t]+{_HOUSE_NUMBER}"
    rf"(?:[ \t]*,?[ \t]*{_POSTCODE}(?:[ \t\r\n]+{_CITY})?)?\b",
    flags=re.IGNORECASE,
)


def _strict_address_subspan(value: str):
    """Return the best strict address match within an existing broad span."""
    text = value or ""
    candidates = []
    for priority, pattern in ((0, _PREFIX_ADDRESS_RE), (1, _SUFFIX_ADDRESS_RE)):
        for match in pattern.finditer(text):
            candidates.append((priority, match.start(), -(match.end() - match.start()), match))
    if not candidates:
        return None
    # Prefer an explicit prefix-street form, otherwise the earliest strict
    # suffix form; longest wins only within the same start position.
    return min(candidates, key=lambda item: (item[0], item[1], item[2]))[3]


def tighten_dutch_address_results(text: str, results: Iterable) -> List:
    """Narrow provably over-broad ``NL_ADDRESS`` spans, fail-safe on ambiguity.

    Result objects are shallow-copied before start/end are changed. Non-address
    entities and address results without a strict internal match are returned
    unchanged.
    """
    source = text or ""
    tightened = []
    for result in results or []:
        if getattr(result, "entity_type", None) != "NL_ADDRESS":
            tightened.append(result)
            continue

        start = getattr(result, "start", None)
        end = getattr(result, "end", None)
        if not isinstance(start, int) or not isinstance(end, int) or start < 0 or end > len(source) or start >= end:
            tightened.append(result)
            continue

        broad_value = source[start:end]
        match = _strict_address_subspan(broad_value)
        if match is None:
            tightened.append(result)
            continue

        new_start = start + match.start()
        new_end = start + match.end()
        if new_start == start and new_end == end:
            tightened.append(result)
            continue

        resolved = copy(result)
        resolved.start = new_start
        resolved.end = new_end
        tightened.append(resolved)

    return tightened
