"""Candidate scanner for SolidPrivacy Scrub Dutch Legal Strict mode.

This module is deliberately a review/audit layer, not an automatic redaction
layer. It looks for suspicious reference-like values that were not already found
by Presidio recognizers. The UI can show them as unchecked rows in the editable
replacement table, so the user can decide whether to include them.

Design rules:
- Preserve context words such as dossiernummer, kenteken, factuurnummer.
- Suggest only the suspicious value, not the whole sentence.
- Do not suggest legal article references, dates, money amounts, pages or annexes.
- Prefer category-level review over one-off hotfixes.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple

try:
    from legal_reference_taxonomy import LEGAL_REFERENCE_CATEGORIES
except Exception:  # keep the app usable while files are being copied
    LEGAL_REFERENCE_CATEGORIES = []


@dataclass(frozen=True)
class Candidate:
    text: str
    entity_type: str
    placeholder: str
    score: float
    start: int
    end: int
    reason: str
    context: str

    def as_dict(self) -> dict:
        return {
            "text": self.text,
            "entity_type": self.entity_type,
            "placeholder": self.placeholder,
            "score": self.score,
            "start": self.start,
            "end": self.end,
            "reason": self.reason,
            "context": self.context,
        }


# Broad value shapes used only after a context cue has been found.
# This catches values like CL-FAM-55201, WR-KLANT-2026-7712, FACT-2026-4481,
# DOSS/2026/1189 and compact context-bound values such as XX123X after "kenteken".
CASE_NUMBER_VALUE_RE_PART = (
    r"(?:"
    r"C/\d{2}/\d{5,6}\s*/\s*(?:[A-Z]{1,5}\s+){1,4}\d{2}[-/]\d{1,6}"
    r"|\d{6,9}\s*/\s*(?:[A-Z]{1,5}\s+){1,4}\d{2}[-/]\d{1,6}"
    r"|[A-Z]{2,5}\s+\d{2}/\d{1,6}"
    r"|NL\d{2}\.\d{3,8}"
    r"|\d{3}\.\d{3}\.\d{3}/\d{2}\s+[A-Z]{1,5}"
    r")"
)

GENERIC_CONTEXTUAL_VALUE_RE_PART = (
    r"(?:"
    r"(?=[A-Z0-9][A-Z0-9./_-]{4,59}\b)(?=[A-Z0-9./_-]*[A-Z])(?=[A-Z0-9./_-]*\d)"
    r"[A-Z0-9]+(?:[./_-][A-Z0-9]+){0,10}"
    r"|"
    r"(?=[A-Z0-9]{5,12}\b)(?=[A-Z0-9]*[A-Z])(?=[A-Z0-9]*\d)[A-Z0-9]{5,12}"
    r")"
)

CONTEXTUAL_VALUE_RE = re.compile(r"\b(?:" + CASE_NUMBER_VALUE_RE_PART + r"|" + GENERIC_CONTEXTUAL_VALUE_RE_PART + r")\b")

# Stand-alone suspicious codes. These are shown as candidates only when they are
# not already detected and not obviously a date/article/amount.
STANDALONE_CODE_RE = re.compile(
    r"\b(?=[A-Z0-9][A-Z0-9./_-]{5,59}\b)(?=[A-Z0-9./_-]*[A-Z])(?=[A-Z0-9./_-]*\d)"
    r"[A-Z0-9]+(?:[./_-][A-Z0-9]+){1,10}\b"
)

# Pure lightweight fallback for KvK numbers. The main recognizer stack also has
# an NL_KVK_NUMBER recognizer, but this keeps the audit/candidate layer useful if
# the automatic recognizer misses a labelled 8-digit value.
KVK_LABELLED_VALUE_RE = re.compile(
    r"\b(?:kvk(?:[-\s]?nummer|\s?nr\.)?|kamer\s+van\s+koophandel|handelsregister)"
    r"(?:[ \t]+(?:vennootschap|bedrijf|organisatie|rechtspersoon|vereniging|stichting))?"
    r"\s*(?:is|:|#|-)?\s*(?P<value>\d{8})\b",
    flags=re.IGNORECASE | re.MULTILINE,
)

DUTCH_PLATE_CONTEXT = {
    "kenteken",
    "kentekennummer",
    "nummerplaat",
    "voertuig",
    "auto",
    "leaseauto",
    "bedrijfsauto",
    "bestelbus",
    "rdw",
}

GENERIC_CONTEXT_CUES = {
    "nummer",
    "referentie",
    "kenmerk",
    "dossier",
    "code",
    "registratie",
    "zaak",
    "factuur",
    "contract",
    "polis",
    "claim",
    "school",
    "uwv",
    "ind",
    "gemeente",
    "politie",
    "proces-verbaal",
    "pv",
}

NEGATIVE_NEARBY_CUES = {
    "artikel",
    "art.",
    "lid",
    "sub",
    "pagina",
    "bladzijde",
    "bijlage",
    "productie",
    "randnummer",
    "paragraaf",
}


def _overlaps(start: int, end: int, spans: Sequence[Tuple[int, int]]) -> bool:
    for other_start, other_end in spans:
        if start < other_end and end > other_start:
            return True
    return False


def _window(text: str, start: int, end: int, radius: int = 60) -> str:
    return text[max(0, start - radius) : min(len(text), end + radius)]


def _normalise_space(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def _looks_like_date_or_time(value: str) -> bool:
    v = (value or "").strip()
    if re.fullmatch(r"\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}", v):
        return True
    if re.fullmatch(r"\d{4}[-/.]\d{1,2}[-/.]\d{1,2}", v):
        return True
    if re.fullmatch(r"\d{1,2}[.:]\d{2}", v):
        return True
    return False


def _looks_like_money_or_article(value: str, context: str) -> bool:
    low = (context or "").lower()
    v = (value or "").strip()
    if "€" in low or "eur" in low or "euro" in low:
        return True
    if re.fullmatch(r"\d{1,2}:\d{1,4}[a-z]?", v, flags=re.IGNORECASE):
        return True
    # Avoid legal article references and document navigation references.
    if any(cue in low for cue in NEGATIVE_NEARBY_CUES) and not any(cue in low for cue in GENERIC_CONTEXT_CUES):
        return True
    return False


def _is_negative_candidate(value: str, context: str) -> bool:
    v = (value or "").strip(" .,;:\n\t")
    if len(v) < 5:
        return True
    if _looks_like_date_or_time(v) or _looks_like_money_or_article(v, context):
        return True
    # Plain Dutch postcode is already handled by NL_POSTCODE; do not duplicate it
    # as a suspicious reference.
    if re.fullmatch(r"[1-9][0-9]{3}\s?[A-Z]{2}", v, flags=re.IGNORECASE):
        return True
    return False


def _keyword_regex(keyword: str) -> re.Pattern:
    escaped = re.escape(keyword.strip()).replace(r"\ ", r"[ \t]+")
    return re.compile(rf"(?<!\w){escaped}(?!\w)", flags=re.IGNORECASE | re.MULTILINE)


def _search_boundary(text: str, start: int, max_chars: int = 120) -> int:
    hard_end = min(len(text), start + max_chars)
    candidates = [hard_end]
    for sep in ["\n", "\r", ";"]:
        idx = text.find(sep, start, hard_end)
        if idx != -1:
            candidates.append(idx)
    dot = text.find(".", start, hard_end)
    if dot != -1 and dot - start > 25:
        candidates.append(dot)
    return min(candidates)


def _placeholder_for(entity_type: str) -> str:
    labels = {
        "NL_SUSPICIOUS_REFERENCE_CANDIDATE": "<MOGELIJKE_REFERENTIE>",
        "NL_POSSIBLE_LICENSE_PLATE": "<MOGELIJK_KENTEKEN>",
        "NL_VEHICLE_REFERENCE": "<VOERTUIG_OF_KENTEKENREFERENTIE>",
        "NL_OBJECT_REFERENCE": "<OBJECTREFERENTIE>",
        "NL_INCIDENT_NUMBER": "<INCIDENTNUMMER>",
        "NL_CLAIM_NUMBER": "<CLAIMNUMMER>",
        "NL_OTHER_REFERENCE": "<OVERIGE_REFERENTIE>",
        "NL_LEGAL_CASE_NUMBER": "<ZAAKNUMMER>",
        "NL_KVK_NUMBER": "<KVK_NUMMER>",
    }
    for category in LEGAL_REFERENCE_CATEGORIES:
        if category.get("entity_type") == entity_type:
            return f"<{category.get('placeholder', entity_type)}>"
    return labels.get(entity_type, f"<{entity_type}>")


def _has_context_cue(context: str) -> bool:
    low = (context or "").lower()
    return any(cue in low for cue in GENERIC_CONTEXT_CUES) or any(cue in low for cue in DUTCH_PLATE_CONTEXT)


def _dedupe(candidates: Iterable[Candidate]) -> List[Candidate]:
    by_span = {}
    for candidate in candidates:
        key = (candidate.start, candidate.end, candidate.text)
        existing = by_span.get(key)
        if existing is None or candidate.score > existing.score:
            by_span[key] = candidate
    return sorted(by_span.values(), key=lambda item: (item.start, -item.score))


def scan_unmasked_candidates(text: str, analyzer_results=None, max_candidates: int = 50) -> List[dict]:
    """Return suspicious unmasked candidate values for review.

    analyzer_results may be Presidio RecognizerResult objects. Their spans are
    excluded so this scanner focuses on what likely remained unhandled.
    """
    source = text or ""
    existing_spans = []
    for res in analyzer_results or []:
        start = getattr(res, "start", None)
        end = getattr(res, "end", None)
        if isinstance(start, int) and isinstance(end, int):
            existing_spans.append((start, end))

    candidates: List[Candidate] = []

    # 1) Taxonomy-driven contextual values that were not detected. This uses the
    # same categories as the recognizer but keeps them as unchecked candidates in
    # case thresholds/entity filters missed them.
    for category in LEGAL_REFERENCE_CATEGORIES:
        entity_type = category.get("entity_type", "NL_CONTEXTUAL_REFERENCE")
        keywords = category.get("keywords", [])
        base_score = max(0.50, float(category.get("score", 0.70)) - 0.10)
        for keyword in keywords:
            for kw_match in _keyword_regex(keyword).finditer(source):
                search_start = kw_match.end()
                search_end = _search_boundary(source, search_start)
                local_text = source[search_start:search_end]
                value_match = CONTEXTUAL_VALUE_RE.search(local_text)
                if not value_match:
                    continue
                start = search_start + value_match.start()
                end = search_start + value_match.end()
                raw = source[start:end]
                trim_l = len(raw) - len(raw.lstrip(" \t:=-#"))
                trim_r = len(raw) - len(raw.rstrip(" \t.,;:"))
                start += trim_l
                if trim_r:
                    end -= trim_r
                value = source[start:end]
                ctx = _window(source, start, end)
                if _overlaps(start, end, existing_spans) or _is_negative_candidate(value, ctx):
                    continue
                candidates.append(
                    Candidate(
                        text=value,
                        entity_type=entity_type,
                        placeholder=_placeholder_for(entity_type),
                        score=base_score,
                        start=start,
                        end=end,
                        reason=f"Possible unmasked value after context keyword '{keyword}'",
                        context=_normalise_space(ctx),
                    )
                )

    # 2) Structured labelled KvK values. The value is numeric-only, so it needs a
    # dedicated context-bound fallback instead of the generic uppercase code logic.
    for match in KVK_LABELLED_VALUE_RE.finditer(source):
        start, end = match.span("value")
        value = source[start:end]
        ctx = _window(source, start, end)
        if _overlaps(start, end, existing_spans):
            continue
        candidates.append(
            Candidate(
                text=value,
                entity_type="NL_KVK_NUMBER",
                placeholder=_placeholder_for("NL_KVK_NUMBER"),
                score=0.78,
                start=start,
                end=end,
                reason="Eight-digit value after KvK/handelsregister context",
                context=_normalise_space(ctx),
            )
        )

    # 3) License plate / vehicle compact candidates. These are context-bound, not
    # blind plate recognition, because fake/test material often uses compact
    # examples such as XX123X.
    for match in re.finditer(r"\b(?=[A-Z0-9]{5,12}\b)(?=[A-Z0-9]*[A-Z])(?=[A-Z0-9]*\d)[A-Z0-9]{5,12}\b", source):
        start, end = match.span()
        value = match.group(0)
        ctx = _window(source, start, end)
        if _overlaps(start, end, existing_spans) or _is_negative_candidate(value, ctx):
            continue
        if any(cue in ctx.lower() for cue in DUTCH_PLATE_CONTEXT):
            candidates.append(
                Candidate(
                    text=value,
                    entity_type="NL_POSSIBLE_LICENSE_PLATE",
                    placeholder=_placeholder_for("NL_POSSIBLE_LICENSE_PLATE"),
                    score=0.66,
                    start=start,
                    end=end,
                    reason="Compact alphanumeric value near vehicle/kenteken context",
                    context=_normalise_space(ctx),
                )
            )

    # 4) Remaining standalone codes with generic legal/admin context nearby.
    for match in STANDALONE_CODE_RE.finditer(source):
        start, end = match.span()
        value = match.group(0)
        ctx = _window(source, start, end)
        if _overlaps(start, end, existing_spans) or _is_negative_candidate(value, ctx):
            continue
        if not _has_context_cue(ctx):
            continue
        candidates.append(
            Candidate(
                text=value,
                entity_type="NL_SUSPICIOUS_REFERENCE_CANDIDATE",
                placeholder=_placeholder_for("NL_SUSPICIOUS_REFERENCE_CANDIDATE"),
                score=0.52,
                start=start,
                end=end,
                reason="Reference-like code near legal/administrative context but not auto-masked",
                context=_normalise_space(ctx),
            )
        )

    return [candidate.as_dict() for candidate in _dedupe(candidates)[:max_candidates]]
