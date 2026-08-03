"""Conservative candidate scanner for unresolved Dutch care references.

This is a review-only fallback for the Care profile. It scans only after strong
care-administrative labels, excludes already detected spans and returns
unchecked candidate rows. It does not scan free clinical text, provider names,
organizations, dates, medication, dosages or laboratory values.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Iterable, List, Mapping, Sequence, Tuple


@dataclass(frozen=True)
class CareCandidate:
    text: str
    entity_type: str
    score: float
    start: int
    end: int
    reason: str
    context: str

    def as_dict(self) -> dict:
        return {
            "text": self.text,
            "entity_type": self.entity_type,
            "score": self.score,
            "start": self.start,
            "end": self.end,
            "reason": self.reason,
            "context": self.context,
        }


# The automatic care recognizers accept conservative -_/ shapes. The candidate
# layer also accepts dots and compact spaces so a malformed but strongly labeled
# reference can still be surfaced for human review.
CANDIDATE_VALUE_RE = re.compile(
    r"(?P<value>"
    r"(?=[A-Z0-9][A-Z0-9. _/-]{4,59}\b)"
    r"(?=[A-Z0-9. _/-]*[A-Z])"
    r"(?=[A-Z0-9. _/-]*\d)"
    r"[A-Z0-9]+(?:[. _/-][A-Z0-9]+){1,10}"
    r"|\d{5,16}"
    r")",
    flags=re.IGNORECASE,
)

CARE_LABELS: tuple[tuple[str, str, float], ...] = (
    (r"pati[eë]ntnummer|patientnummer|pati[eë]ntnr\.?|patientnr\. ?", "NL_PATIENT_NUMBER", 0.74),
    (r"cli[eë]ntnummer|clientnummer|cli[eë]ntnr\.?|clientnr\. ?", "NL_CARE_CLIENT_NUMBER", 0.74),
    (r"medisch\s+dossiernummer|zorgdossiernummer|medisch\s+dossiernr\. ?", "NL_MEDICAL_RECORD_NUMBER", 0.74),
    (r"EPD[-\s]?nummer|ECD[-\s]?nummer|EPD\s*nr\.?|ECD\s*nr\. ?", "NL_EPD_ECD_NUMBER", 0.76),
    (r"verzekerdennummer|zorgverzekeringsnummer|verzekerdennr\. ?", "NL_HEALTH_INSURANCE_NUMBER", 0.74),
    (r"verwijsnummer|verwijzingsnummer|verwijsnr\. ?", "NL_REFERRAL_NUMBER", 0.74),
    (r"behandelnummer|zorgtrajectnummer|receptnummer|behandelnr\.?|trajectnummer", "NL_TREATMENT_REFERENCE", 0.72),
    (r"monsternummer|sample[-\s]?ID|labnummer|laboratoriumnummer|accessienummer|onderzoeks[-\s]?ID", "NL_LAB_SAMPLE_NUMBER", 0.74),
    (r"MIC[-\s]?nummer|MIM[-\s]?nummer|VIM[-\s]?nummer|zorgincidentnummer|incidentnummer|medicatiefoutnummer", "NL_CARE_INCIDENT_NUMBER", 0.76),
    (r"CIZ[-\s]?nummer|Wlz[-\s]?indicatie|Wmo[-\s]?beschikking|zorgtoewijzing|PGB[-\s]?nummer|indicatiebesluit", "NL_CARE_INDICATION_REFERENCE", 0.74),
)


def _field(result: Any, name: str, default=None):
    if isinstance(result, Mapping):
        return result.get(name, default)
    return getattr(result, name, default)


def _overlaps(start: int, end: int, spans: Sequence[Tuple[int, int]]) -> bool:
    return any(start < other_end and end > other_start for other_start, other_end in spans)


def _line_end(text: str, start: int, max_chars: int = 100) -> int:
    end = min(len(text), start + max_chars)
    newline = text.find("\n", start, end)
    carriage = text.find("\r", start, end)
    semicolon = text.find(";", start, end)
    return min([end] + [index for index in (newline, carriage, semicolon) if index >= 0])


def _context(text: str, start: int, end: int, radius: int = 55) -> str:
    return text[max(0, start - radius):min(len(text), end + radius)]


def _negative_value(value: str) -> bool:
    stripped = value.strip(" .,;:\t\r\n")
    if re.fullmatch(r"\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}", stripped):
        return True
    if re.fullmatch(r"\d{4}[-/.]\d{1,2}[-/.]\d{1,2}", stripped):
        return True
    if re.fullmatch(r"\d{1,2}[.:]\d{2}", stripped):
        return True
    if re.match(r"^(?:DBC|ICD)(?:[-. /]|$)", stripped, flags=re.IGNORECASE):
        return True
    return False


def _dedupe(candidates: Iterable[CareCandidate]) -> List[CareCandidate]:
    best = {}
    for candidate in candidates:
        key = (candidate.start, candidate.end, candidate.entity_type)
        previous = best.get(key)
        if previous is None or candidate.score > previous.score:
            best[key] = candidate
    return sorted(best.values(), key=lambda candidate: (candidate.start, -candidate.score))


def scan_unmasked_care_candidates(
    text: str,
    analyzer_results=None,
    max_candidates: int = 30,
) -> List[dict]:
    """Return unresolved, strongly labeled care-reference candidates for review."""

    source = text or ""
    existing_spans: list[tuple[int, int]] = []
    for result in analyzer_results or []:
        start = _field(result, "start")
        end = _field(result, "end")
        if isinstance(start, int) and isinstance(end, int):
            existing_spans.append((start, end))

    candidates: list[CareCandidate] = []
    for labels, entity_type, score in CARE_LABELS:
        label_re = re.compile(
            rf"(?<!\w)(?:{labels})(?!\w)\s*(?:is|:|#|=|-)?\s*",
            flags=re.IGNORECASE | re.MULTILINE,
        )
        for label_match in label_re.finditer(source):
            search_start = label_match.end()
            search_end = _line_end(source, search_start)
            value_match = CANDIDATE_VALUE_RE.search(source[search_start:search_end])
            if not value_match:
                continue
            start = search_start + value_match.start("value")
            end = search_start + value_match.end("value")
            value = source[start:end].strip(" .,;:\t\r\n")
            trim_left = len(source[start:end]) - len(source[start:end].lstrip())
            start += trim_left
            end = start + len(value)
            if not value or _negative_value(value) or _overlaps(start, end, existing_spans):
                continue
            candidates.append(
                CareCandidate(
                    text=value,
                    entity_type=entity_type,
                    score=score,
                    start=start,
                    end=end,
                    reason="Sterk zorglabel met nog niet automatisch herkende referentie",
                    context=_context(source, start, end),
                )
            )

    return [candidate.as_dict() for candidate in _dedupe(candidates)[:max_candidates]]
