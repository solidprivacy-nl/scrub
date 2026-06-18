"""Contract-backed helper for safe Dutch PERSON-name recognition.

This helper implements a narrow, value-only role/title + name recognizer for
synthetic benchmark and follow-up development. It is intentionally bounded:
role/context words remain readable, weak name-near-contact/reference contexts
are not treated as hard recognizer matches, and single surnames require strong
role/title context.
"""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable, List


PERSON_NAME_ENTITY_TYPE = "NL_LEGAL_PARTY_NAME"

# Keep in sync with the safety policy in PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md.
PRESERVE_TERMS = {
    "cliënt",
    "client",
    "slachtoffer",
    "minderjarige",
    "arts",
    "getuige",
    "eiser",
    "verweerder",
    "verpleegkundige",
    "zorgmedewerker",
    "behandelaar",
    "mantelzorger",
    "mr.",
    "mr",
}

# Role/title cues are deliberately narrow and context-bound. Do not replace this
# with broad capitalization matching. The role cue is matched case-insensitively,
# but the following name value intentionally keeps uppercase-sensitive token
# checks so lowercase sentence words are not swallowed into the name span.
ROLE_OR_TITLE_CUE = r"(?i:arts|getuige|cliënt|client|verpleegkundige|mantelzorger|zorgmedewerker|behandelaar|mr\.?)"
UPPER = r"[A-ZÀ-ÖØ-Þ]"
NAME_TOKEN = rf"{UPPER}[A-Za-zÀ-ÖØ-öø-ÿ'’\-]*"
NAME_PARTICLE = r"(?:van|de|der|den|ten|ter|el|al|ait|ben|bin|ibn)"
NAME_GAP = r"[ \t]+"
NAME_VALUE = rf"{NAME_TOKEN}(?:(?:{NAME_GAP}{NAME_PARTICLE})?{NAME_GAP}{NAME_TOKEN}){{0,4}}"

ROLE_TITLE_NAME_RE = re.compile(
    rf"(?<!\w)(?P<context>{ROLE_OR_TITLE_CUE}){NAME_GAP}(?P<value>{NAME_VALUE})(?!\w)",
    flags=re.MULTILINE,
)


@dataclass(frozen=True)
class PersonNameMatch:
    """A value-only PERSON-name match returned by the helper."""

    start: int
    end: int
    text: str
    entity_type: str = PERSON_NAME_ENTITY_TYPE
    score: float = 0.79
    recognizer_name: str = "contract_backed_person_name_helper"


def _normalise_preserve_term(value: str) -> str:
    return (value or "").strip().lower()


def _contains_preserve_term(value: str, preserve_terms: Iterable[str] = PRESERVE_TERMS) -> bool:
    lowered_value = _normalise_preserve_term(value)
    return any(_normalise_preserve_term(term) == lowered_value for term in preserve_terms)


def _trim_value_span(text: str, start: int, end: int) -> tuple[int, int]:
    while start < end and text[start].isspace():
        start += 1
    while end > start and text[end - 1] in " \t\r\n.,;:":
        end -= 1
    return start, end


def find_contract_backed_person_name_matches(text: str) -> List[PersonNameMatch]:
    """Return value-only role/title PERSON-name matches.

    The helper only recognizes strong context cases such as ``arts Bakker`` or
    ``getuige Fatima El Amrani``. It intentionally does not hard-match weak
    name-near-contact/reference cases; those remain future candidate-only work.
    """

    source_text = text or ""
    matches: List[PersonNameMatch] = []
    seen: set[tuple[int, int]] = set()

    for match in ROLE_TITLE_NAME_RE.finditer(source_text):
        start, end = _trim_value_span(source_text, *match.span("value"))
        if start >= end:
            continue
        value = source_text[start:end]
        if _contains_preserve_term(value):
            continue
        key = (start, end)
        if key in seen:
            continue
        seen.add(key)
        matches.append(PersonNameMatch(start=start, end=end, text=value))

    return matches
