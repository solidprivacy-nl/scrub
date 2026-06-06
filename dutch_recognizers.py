"""Dutch / European + Dutch legal recognizers for SolidPrivacy Scrub.

Phase 1-3 v7 update:
- adds a central Dutch legal reference taxonomy and contextual reference
  recognizer for client references, school references, invoice numbers,
  internal references, administrative references and domain-specific
  reference codes;
- keeps context words readable and masks only the sensitive reference value.

Phase 1-3 v5 hotfix update:
- adds value-only rolnummer detection for Dutch court role-number formats
  with spaced procedure codes such as "CV EXPL 26-9921", while preserving
  the label/context text.

Phase 1-3 v4 hotfix update:
- fixes Presidio context-enhancer crash by adding AnalysisExplanation metadata
  to custom capture recognizer results;

Phase 1-3 v3 update:
- tightens legal-party name spans so role/context words such as "slachtoffer",
  "minderjarige", "verzoeker" and "verweerder" are preserved;
- prevents party-name recognizers from crossing sentence or line boundaries;
- prevents court/authority recognizers from crossing into following case-number
  lines;
- keeps labelled legal identifiers value-only: the label remains readable and
  only the actual number/reference is replaced.

The current Streamlit demo analyses with language="en" while using Dutch custom
recognizers. Therefore these recognizers default to supported_language="en".
"""

from __future__ import annotations

import re
from typing import Iterable, List, Sequence, Tuple

from legal_reference_taxonomy import (
    LEGAL_REFERENCE_CATEGORIES,
    REFERENCE_ENTITY_TYPES,
    WEAK_REFERENCE_KEYWORDS,
)

from presidio_analyzer import AnalysisExplanation, EntityRecognizer, Pattern, PatternRecognizer, RecognizerResult


DUTCH_GENERAL_ENTITY_NAMES = [
    "NL_BSN",
    "NL_POSTCODE",
    "NL_IBAN",
    "NL_KVK_NUMBER",
    "NL_VAT_NUMBER",
    "NL_PHONE_NUMBER",
    "NL_LICENSE_PLATE",
    "NL_DRIVER_LICENSE",
    "NL_BIG_NUMBER",
    "NL_ADDRESS",
    "NL_DATE_OF_BIRTH",
]

DUTCH_LEGAL_ENTITY_NAMES = [
    "NL_ECLI",
    "NL_LEGAL_CASE_NUMBER",
    "NL_ROLNUMMER",
    "NL_REKESTNUMMER",
    "NL_PARKETNUMMER",
    "NL_DOSSIER_NUMBER",
    "NL_CLIENT_NUMBER",
    "NL_CJIB_NUMBER",
    "NL_POLICE_REPORT_NUMBER",
    "NL_INSURANCE_CLAIM_NUMBER",
    "NL_LEGAL_PARTY_NAME",
    "NL_COURT_OR_AUTHORITY",
    *REFERENCE_ENTITY_TYPES,
]

DUTCH_ENTITY_NAMES = DUTCH_GENERAL_ENTITY_NAMES + DUTCH_LEGAL_ENTITY_NAMES

LEGAL_ROLE_CONTEXT = [
    "eiser",
    "gedaagde",
    "verzoeker",
    "verweerder",
    "appellant",
    "geïntimeerde",
    "geintimeerde",
    "belanghebbende",
    "verdachte",
    "slachtoffer",
    "benadeelde partij",
    "minderjarige",
    "cliënt",
    "client",
    "tegenpartij",
    "wederpartij",
    "advocaat",
    "raadsman",
    "raadvrouw",
    "gemachtigde",
    "notaris",
    "deurwaarder",
    "curator",
    "bewindvoerder",
    "mentor",
]

LEGAL_IDENTIFIER_CONTEXT = [
    "zaaknummer",
    "rolnummer",
    "rekestnummer",
    "parketnummer",
    "dossiernummer",
    "dossiernr",
    "cliëntnummer",
    "clientnummer",
    "kenmerk",
    "referentie",
    "beschikking",
    "cjib",
    "proces-verbaal",
    "pv-nummer",
    "schadenummer",
    "polisnummer",
    "cliëntnummer",
    "clientnummer",
    "klantnummer",
    "schoolreferentie",
    "zaakreferentie",
    "factuurnummer",
    "interne klantreferentie",
]

# Presidio PatternRecognizer uses case-insensitive matching. For names and Dutch
# postcode letters we need true uppercase checks to avoid matching normal words
# like "is" as if they were initials/letters. Python regex lets us locally turn
# case-insensitivity off with (?-i:...).
UPPER = r"(?-i:[A-ZÀ-ÖØ-Þ])"
POSTCODE_LETTERS = r"(?-i:[A-Z]{2})"
# Name tokens are deliberately strict. They may contain Dutch letters, hyphens
# and apostrophes, but not dots, digits or underscores. Dots/newlines caused the
# previous over-broad spans, e.g. "minderjarige Sami El Amrani.\nVerweerder
# Peter Bakker" becoming one masked block.
NAME_TOKEN = rf"{UPPER}[A-Za-zÀ-ÖØ-öø-ÿ'’\-]*"
NAME_PARTICLE = r"(?:van|de|der|den|ten|ter|el|al|la|du|op|aan|bin|ibn)"
NAME_GAP = r"[ \t]+"
NAME_VALUE = rf"{NAME_TOKEN}(?:(?:{NAME_GAP}{NAME_PARTICLE})?{NAME_GAP}{NAME_TOKEN}){{0,4}}"


# -------------------------
# Utility / validation logic
# -------------------------


def _digits(value: str) -> str:
    return re.sub(r"\D", "", value or "")


def _looks_like_date(value: str) -> bool:
    """Return True for common date-shaped strings."""
    text = (value or "").strip()
    digits = _digits(text)

    if re.fullmatch(r"\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}", text):
        return True
    if re.fullmatch(r"\d{4}[-/.]\d{1,2}[-/.]\d{1,2}", text):
        return True

    if len(digits) == 8:
        # ddmmyyyy or yyyymmdd
        day = int(digits[0:2])
        month = int(digits[2:4])
        year = int(digits[4:8])
        if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2099:
            return True
        year = int(digits[0:4])
        month = int(digits[4:6])
        day = int(digits[6:8])
        if 1900 <= year <= 2099 and 1 <= month <= 12 and 1 <= day <= 31:
            return True

    return False


def _normalise_to_dutch_phone_digits(value: str) -> str:
    digits = _digits(value)
    if digits.startswith("0031"):
        return "0" + digits[4:]
    if digits.startswith("31"):
        return "0" + digits[2:]
    return digits


def _looks_like_phone(value: str) -> bool:
    digits = _normalise_to_dutch_phone_digits(value)
    return len(digits) == 10 and digits.startswith("0")


def _looks_like_amount(value: str) -> bool:
    text = (value or "").strip()
    return bool(re.search(r"(?:€|eur\b|euro\b)\s*\d", text, flags=re.IGNORECASE))


def _pattern_recognizer(
    entity: str,
    regex: str,
    score: float,
    context: Iterable[str] | None = None,
    supported_language: str = "en",
) -> PatternRecognizer:
    return PatternRecognizer(
        supported_entity=entity,
        patterns=[Pattern(name=entity.lower(), regex=regex, score=score)],
        context=list(context or []),
        supported_language=supported_language,
    )


class RegexCaptureRecognizer(EntityRecognizer):
    """Regex recognizer that returns only a named capture group named 'value'.

    Presidio's standard PatternRecognizer returns the whole regex match. For
    legal text this is often too broad: "dossiernummer is ARB-2026-00421" should
    keep the label and replace only "ARB-2026-00421". This recognizer matches the
    full phrase for context but returns only the sensitive value span.
    """

    def __init__(
        self,
        entity: str,
        patterns: Sequence[Tuple[str, str]],
        score: float,
        context: Iterable[str] | None = None,
        supported_language: str = "en",
    ) -> None:
        super().__init__(
            supported_entities=[entity],
            supported_language=supported_language,
            name=f"{entity}_capture_recognizer",
        )
        self.entity = entity
        self.patterns = [(name, re.compile(pattern, flags=re.IGNORECASE | re.MULTILINE)) for name, pattern in patterns]
        self.score = score
        self.context = list(context or [])

    def load(self) -> None:  # Required by EntityRecognizer; no model to load.
        return None

    def analyze(self, text: str, entities: List[str], nlp_artifacts=None) -> List[RecognizerResult]:
        if entities and self.entity not in entities:
            return []

        results: List[RecognizerResult] = []
        for _name, pattern in self.patterns:
            for match in pattern.finditer(text or ""):
                if "value" in match.groupdict() and match.group("value") is not None:
                    start, end = match.span("value")
                else:
                    start, end = match.span()

                # Trim accidental boundary whitespace/punctuation from captured values.
                while start < end and text[start].isspace():
                    start += 1
                while end > start and text[end - 1] in " \t\r\n.,;:":
                    end -= 1
                if start >= end:
                    continue

                explanation = AnalysisExplanation(
                    recognizer=self.name,
                    original_score=self.score,
                    pattern_name=_name,
                    pattern=pattern.pattern,
                    textual_explanation=(
                        f"Detected by `{self.name}` using capture-group pattern `{_name}`; "
                        "only the named value span is returned so Dutch legal context remains readable."
                    ),
                )

                results.append(
                    RecognizerResult(
                        entity_type=self.entity,
                        start=start,
                        end=end,
                        score=self.score,
                        analysis_explanation=explanation,
                        recognition_metadata={
                            RecognizerResult.RECOGNIZER_NAME_KEY: self.name,
                            RecognizerResult.RECOGNIZER_IDENTIFIER_KEY: getattr(self, "id", self.name),
                        },
                    )
                )
        return results


REFERENCE_VALUE_REGEX = re.compile(
    r"\b(?:"
    # Common uppercase/legal admin codes: CL-FAM-55201, FACT-2026-4481,
    # WR-KLANT-2026-7712, HRZ-SAM-2026-04, PL1700-20260518-334455.
    r"(?=[A-Z0-9][A-Z0-9./_-]{4,49}\b)(?=[A-Z0-9./_-]*[A-Z])(?=[A-Z0-9./_-]*\d)"
    r"[A-Z0-9]+(?:[./_-][A-Z0-9]+){1,8}"
    r"|"
    # Dutch appellate / court formats like 200.345.678/01 OK.
    r"\d{3}\.\d{3}\.\d{3}/\d{2}\s+[A-Z]{1,5}"
    r"|"
    # Case references with procedure blocks, e.g. 10598721 / UE VERZ 26-441.
    r"\d{6,9}\s*/\s*(?:[A-Z]{1,5}\s+){1,4}\d{2}[-/]\d{1,6}"
    r")\b"
)


def _keyword_to_regex(keyword: str) -> str:
    """Turn a taxonomy keyword into a forgiving but bounded regex."""
    escaped = re.escape(keyword.strip())
    escaped = escaped.replace(r"\ ", r"[ \t]+")
    # Allow optional punctuation after common abbreviations by keeping dots literal
    # where the taxonomy includes them, but still use word-ish boundaries around
    # the phrase so "kenmerk" does not match inside another word.
    return rf"(?<!\w){escaped}(?!\w)"


def _next_line_or_sentence_end(text: str, start: int, max_chars: int = 120) -> int:
    """Return a local search boundary after a context keyword.

    Reference values are usually on the same line or in the same short phrase.
    Keeping a short boundary prevents the recognizer from swallowing remote codes
    later in the paragraph.
    """
    hard_end = min(len(text), start + max_chars)
    candidates = [hard_end]
    for sep in ["\n", "\r", ";"]:
        idx = text.find(sep, start, hard_end)
        if idx != -1:
            candidates.append(idx)
    # A full stop may be part of appellate numbers (200.345.678/01 OK), so only
    # use it as a boundary when it appears after a reasonable distance.
    dot = text.find(".", start, hard_end)
    if dot != -1 and dot - start > 25:
        candidates.append(dot)
    return min(candidates)


def _is_negative_reference_value(value: str) -> bool:
    candidate = (value or "").strip()
    if not candidate:
        return True
    if _looks_like_date(candidate) or _looks_like_amount(candidate):
        return True
    if re.fullmatch(r"\d{1,2}[.:]\d{2}", candidate):
        return True
    # Legal article references must remain readable and should not be treated as
    # matter references merely because they contain numbers and separators.
    if re.fullmatch(r"\d{1,2}:\d{1,4}[a-z]?", candidate, flags=re.IGNORECASE):
        return True
    if re.fullmatch(r"[1-9][0-9]{3}\s?[A-Z]{2}", candidate):
        return True
    return False


def _is_strong_reference_value(value: str) -> bool:
    candidate = (value or "").strip()
    separators = sum(candidate.count(ch) for ch in "-_/.")
    has_letters = bool(re.search(r"[A-Z]", candidate))
    has_digits = bool(re.search(r"\d", candidate))
    return has_letters and has_digits and (separators >= 2 or len(candidate) >= 9)


class DutchContextualReferenceRecognizer(EntityRecognizer):
    """Recognize Dutch legal/admin reference values using context taxonomy.

    This is deliberately not a blind uppercase-code recognizer. It only returns a
    value when a legal/administrative context word is nearby. The context word is
    preserved and only the value span is returned.
    """

    def __init__(self, supported_language: str = "en") -> None:
        super().__init__(
            supported_entities=REFERENCE_ENTITY_TYPES,
            supported_language=supported_language,
            name="DutchContextualReferenceRecognizer",
        )
        self.categories = LEGAL_REFERENCE_CATEGORIES

    def load(self) -> None:
        return None

    def analyze(self, text: str, entities: List[str], nlp_artifacts=None) -> List[RecognizerResult]:
        wanted = set(entities or REFERENCE_ENTITY_TYPES)
        results: List[RecognizerResult] = []
        seen = set()
        source_text = text or ""

        for category in self.categories:
            entity_type = category["entity_type"]
            if entity_type not in wanted:
                continue
            base_score = float(category.get("score", 0.76))
            for keyword in category.get("keywords", []):
                keyword_pattern = re.compile(_keyword_to_regex(keyword), flags=re.IGNORECASE | re.MULTILINE)
                for keyword_match in keyword_pattern.finditer(source_text):
                    search_start = keyword_match.end()
                    search_end = _next_line_or_sentence_end(source_text, search_start)
                    local_text = source_text[search_start:search_end]
                    value_match = REFERENCE_VALUE_REGEX.search(local_text)
                    if not value_match:
                        continue

                    start = search_start + value_match.start()
                    end = search_start + value_match.end()
                    value = source_text[start:end].strip()
                    trim_left = len(source_text[start:end]) - len(source_text[start:end].lstrip(" \t:=-#"))
                    trim_right = len(source_text[start:end]) - len(source_text[start:end].rstrip(" \t.,;:"))
                    start += trim_left
                    if trim_right:
                        end -= trim_right
                    value = source_text[start:end]

                    if start >= end or _is_negative_reference_value(value):
                        continue

                    score = base_score
                    if keyword.lower() in WEAK_REFERENCE_KEYWORDS and not _is_strong_reference_value(value):
                        score = max(0.55, score - 0.16)
                    elif keyword.lower() in WEAK_REFERENCE_KEYWORDS:
                        score = max(0.68, score - 0.06)

                    key = (entity_type, start, end)
                    if key in seen:
                        continue
                    seen.add(key)

                    explanation = AnalysisExplanation(
                        recognizer=self.name,
                        original_score=score,
                        pattern_name=f"taxonomy_keyword:{keyword}",
                        pattern=REFERENCE_VALUE_REGEX.pattern,
                        textual_explanation=(
                            f"Detected Dutch legal/admin reference value after context keyword '{keyword}'. "
                            "Only the value span is returned so the legal context remains readable."
                        ),
                    )
                    results.append(
                        RecognizerResult(
                            entity_type=entity_type,
                            start=start,
                            end=end,
                            score=score,
                            analysis_explanation=explanation,
                            recognition_metadata={
                                RecognizerResult.RECOGNIZER_NAME_KEY: self.name,
                                RecognizerResult.RECOGNIZER_IDENTIFIER_KEY: getattr(self, "id", self.name),
                            },
                        )
                    )
        return results


# -------------------------
# Validated recognizers
# -------------------------


class DutchBSNRecognizer(PatternRecognizer):
    """Recognize Dutch BSN candidates using pattern + 11-test validation."""

    PATTERNS = [
        Pattern(
            name="nl_bsn_contiguous_8_or_9_digits",
            regex=r"(?<!\d)\d{8,9}(?!\d)",
            score=0.72,
        )
    ]

    CONTEXT = [
        "bsn",
        "burgerservicenummer",
        "burger service nummer",
        "sofinummer",
        "sociaal fiscaal nummer",
        "identificatienummer",
        "persoonsnummer",
    ]

    def __init__(self, supported_language: str = "en") -> None:
        super().__init__(
            supported_entity="NL_BSN",
            patterns=self.PATTERNS,
            context=self.CONTEXT,
            supported_language=supported_language,
        )

    @classmethod
    def is_valid_bsn(cls, value: str) -> bool:
        if _looks_like_date(value) or _looks_like_phone(value):
            return False
        stripped = (value or "").strip()
        if not re.fullmatch(r"\d{8,9}", stripped):
            return False
        digits = _digits(stripped)
        if len(digits) == 8:
            digits = "0" + digits
        if len(digits) != 9:
            return False
        if len(set(digits)) == 1:
            return False
        numbers = [int(d) for d in digits]
        checksum = sum(numbers[i] * (9 - i) for i in range(8)) - numbers[8]
        return checksum % 11 == 0

    def validate_result(self, pattern_text: str) -> bool:
        return self.is_valid_bsn(pattern_text)


class DutchPhoneRecognizer(PatternRecognizer):
    """Recognize Dutch phone numbers conservatively."""

    PATTERNS = [
        Pattern(
            name="nl_mobile_phone",
            regex=(
                r"(?<!\w)(?:\+31\s?6|0031\s?6|0\s?6)"
                r"(?:[\s.-]?\d){8}(?!\w)"
            ),
            score=0.85,
        ),
        Pattern(
            name="nl_landline_phone",
            regex=(
                r"(?<!\w)(?:\+31\s?|0031\s?|0)"
                r"(?:10|13|15|20|23|24|26|30|33|35|36|38|40|43|45|46|50|53|55|58|70|71|72|73|74|75|76|77|78|79)"
                r"(?:[\s.-]?\d){7}(?!\w)"
            ),
            score=0.78,
        ),
    ]

    CONTEXT = ["telefoon", "tel", "mobiel", "gsm", "bellen", "contactnummer"]

    def __init__(self, supported_language: str = "en") -> None:
        super().__init__(
            supported_entity="NL_PHONE_NUMBER",
            patterns=self.PATTERNS,
            context=self.CONTEXT,
            supported_language=supported_language,
        )

    @classmethod
    def is_valid_phone(cls, value: str) -> bool:
        if _looks_like_date(value) or _looks_like_amount(value):
            return False
        digits = _normalise_to_dutch_phone_digits(value)
        if len(digits) != 10:
            return False
        if not digits.startswith("0"):
            return False
        if len(set(digits)) <= 2:
            return False
        return True

    def validate_result(self, pattern_text: str) -> bool:
        return self.is_valid_phone(pattern_text)


# -------------------------
# Public API used by app/helpers
# -------------------------


def get_dutch_general_entity_names() -> List[str]:
    return list(DUTCH_GENERAL_ENTITY_NAMES)


def get_dutch_legal_entity_names() -> List[str]:
    return list(DUTCH_LEGAL_ENTITY_NAMES)


def get_dutch_entity_names(include_legal: bool = True) -> List[str]:
    if include_legal:
        return list(DUTCH_ENTITY_NAMES)
    return list(DUTCH_GENERAL_ENTITY_NAMES)


def get_dutch_recognizers(supported_language: str = "en") -> List[EntityRecognizer]:
    """Return Dutch/EU + Dutch legal recognizers for the current app."""

    general_recognizers: List[EntityRecognizer] = [
        DutchBSNRecognizer(supported_language=supported_language),
        DutchPhoneRecognizer(supported_language=supported_language),
        _pattern_recognizer(
            entity="NL_POSTCODE",
            regex=rf"\b[1-9][0-9]{{3}}\s?{POSTCODE_LETTERS}\b",
            score=0.80,
            context=["postcode", "adres", "woonplaats", "plaats"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_IBAN",
            regex=r"\bNL\s?\d{2}\s?[A-Z]{4}\s?(?:\d\s?){10}\b",
            score=0.90,
            context=["iban", "rekening", "rekeningnummer", "bankrekening"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_VAT_NUMBER",
            regex=r"\bNL\s?\d{9}\s?B\s?\d{2}\b",
            score=0.90,
            context=["btw", "btw-nummer", "vat", "vat number", "omzetbelasting"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_KVK_NUMBER",
            patterns=[
                (
                    "kvk_labeled_value",
                    r"\b(?:kvk(?:[-\s]?nummer|\s?nr\.)?|kamer\s+van\s+koophandel)\s*(?:is|:|#|-)?\s*(?P<value>\d{8})\b",
                ),
            ],
            score=0.88,
            context=["kvk", "kamer van koophandel", "handelsregister"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_LICENSE_PLATE",
            regex=(
                r"\b(?:kenteken[:\s]*)?"
                r"(?:[A-Z]{2}-\d{2}-\d{2}|\d{2}-\d{2}-[A-Z]{2}|\d{2}-[A-Z]{2}-\d{2}|"
                r"[A-Z]{2}-\d{2}-[A-Z]{2}|[A-Z]{2}-[A-Z]{2}-\d{2}|"
                r"\d{2}-[A-Z]{2}-[A-Z]{2})\b"
            ),
            score=0.72,
            context=["kenteken", "voertuig", "auto"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_DRIVER_LICENSE",
            patterns=[
                (
                    "driver_license_labeled_value",
                    rf"\b(?:rijbewijs(?:nummer)?|rijbewijsnr\.?|rijbewijs\s*nr\.?)\s*(?:is|:|#|-)?\s*(?P<value>{UPPER}?[A-Z0-9]{{7,12}})\b",
                ),
            ],
            score=0.82,
            context=["rijbewijs", "rijbewijsnummer"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_BIG_NUMBER",
            patterns=[
                (
                    "big_labeled_value",
                    r"\bbig\s*[-\s]?\s*(?:nummer|nr\.?)\s*(?:is|:|#|-)?\s*(?P<value>\d{11})\b",
                ),
            ],
            score=0.88,
            context=["big", "big-nummer", "zorgverlener", "arts"],
            supported_language=supported_language,
        ),
        PatternRecognizer(
            supported_entity="NL_ADDRESS",
            patterns=[
                Pattern(
                    name="nl_address_street_suffix",
                    regex=(
                        rf"\b{NAME_TOKEN}(?:[ \t]+[A-Za-zÀ-ÖØ-öø-ÿ'’\-]+){{0,3}}"
                        r"(?:straat|laan|weg|plein|dreef|hof|kade|singel|gracht|steeg|park|boulevard|pad|plantsoen)"
                        r"[ \t]+\d{1,5}\s?[A-Za-z]{0,3}"
                        rf"(?:[ \t]*,?[ \t]*[1-9][0-9]{{3}}\s?{POSTCODE_LETTERS}(?:[ \t\r\n]+{NAME_TOKEN}(?:[ \t]+[A-Za-zÀ-ÖØ-öø-ÿ'’\-]+){{0,3}})?)?\b"
                    ),
                    score=0.66,
                ),
                Pattern(
                    name="nl_address_street_prefix",
                    regex=(
                        r"\b(?:Straat|Laan|Weg|Plein|Dreef|Hof|Kade|Singel|Gracht|Steeg|Park|Boulevard|Pad|Plantsoen)"
                        rf"(?:[ \t]+(?:van|de|der|den|ten|ter|het|{NAME_TOKEN})){{1,5}}"
                        r"[ \t]+\d{1,5}\s?[A-Za-z]{0,3}"
                        rf"(?:[ \t]*,?[ \t]*[1-9][0-9]{{3}}\s?{POSTCODE_LETTERS}(?:[ \t\r\n]+{NAME_TOKEN}(?:[ \t]+[A-Za-zÀ-ÖØ-öø-ÿ'’\-]+){{0,3}})?)?\b"
                    ),
                    score=0.70,
                ),
            ],
            context=["adres", "woonadres", "vestigingsadres", "straat", "huisnummer", "woont"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_DATE_OF_BIRTH",
            patterns=[
                (
                    "date_of_birth_labeled_value",
                    r"\b(?:geboortedatum|geb\.\s?datum|geboren\s+op|datum\s+geboorte|dob)\s*(?:is|:)?\s*(?P<value>\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}[-/.]\d{1,2}[-/.]\d{1,2})\b",
                ),
            ],
            score=0.84,
            context=["geboortedatum", "geboren", "datum geboorte"],
            supported_language=supported_language,
        ),
    ]

    legal_recognizers: List[EntityRecognizer] = [
        _pattern_recognizer(
            entity="NL_ECLI",
            regex=r"\bECLI:NL:[A-Z0-9]{2,12}:\d{4}:[A-Z0-9.:-]+\b",
            score=0.95,
            context=["ecli", "uitspraak", "vonnis", "arrest", "beschikking"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_PARKETNUMMER",
            regex=r"\b\d{2}/\d{6}-\d{2}\b",
            score=0.88,
            context=["parketnummer", "officier", "strafzaak", "tenlastelegging"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_PARKETNUMMER",
            patterns=[
                (
                    "parket_labeled_value",
                    r"\b(?:parketnummer|parketnr\.?|parket\s?nr\.?)\s*(?:is|:|#|-)?\s*(?P<value>\d{2}/\d{6}-\d{2})\b",
                ),
            ],
            score=0.91,
            context=["parketnummer", "officier", "strafzaak", "tenlastelegging"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_LEGAL_CASE_NUMBER",
            regex=(
                r"\bC/\d{2}/\d{5,6}\s*/\s*(?:HA|KG|FA|JE|CV|RK|ZA|EXPL|VERZ|BESL)"
                r"\s*[A-Z]{0,3}\s*\d{2}[-/]\d{1,5}\b"
            ),
            score=0.88,
            context=["zaaknummer", "rolnummer", "rechtbank", "procedure"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_LEGAL_CASE_NUMBER",
            patterns=[
                (
                    "legal_case_labeled_value",
                    r"\b(?:zaaknummer|zaaknr\.?|zaak\s?nr\.?|zaak-/rolnummer)\s*(?:is|:|#|-)?\s*(?P<value>C/\d{2}/\d{5,6}\s*/\s*(?:HA|KG|FA|JE|CV|RK|ZA|EXPL|VERZ|BESL)\s*[A-Z]{0,3}\s*\d{2}[-/]\d{1,5}|[A-Z0-9]{1,8}[-_/][A-Z0-9]{2,12}(?:[-_/][A-Z0-9]{1,12})?)\b",
                ),
            ],
            score=0.86,
            context=["zaaknummer", "rolnummer", "rechtbank", "procedure"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_ROLNUMMER",
            patterns=[
                (
                    "rolnummer_spaced_procedure_code",
                    # Examples: "rolnummer CV EXPL 26-9921", "rolnr HA ZA 24-123".
                    # The role/procedure label remains readable; only the actual
                    # number/code is returned as the sensitive span.
                    r"\b(?:rolnummer|rolnr\.?|rol\s?nr\.?)\s*(?:is|:|#|-)?\s*(?P<value>(?:[A-Z]{1,5}\s+){1,4}\d{2}[-/]\d{1,6})\b",
                ),
                (
                    "rolnummer_compact_labeled_value",
                    r"\b(?:rolnummer|rolnr\.?|rol\s?nr\.?)\s*(?:is|:|#|-)?\s*(?P<value>[A-Z0-9]{1,8}[-_/][A-Z0-9]{2,12}(?:[-_/][A-Z0-9]{1,12})?)\b",
                ),
            ],
            score=0.86,
            context=["rolnummer", "rolnr", "civiel", "procedure"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_REKESTNUMMER",
            patterns=[
                (
                    "rekestnummer_labeled_value",
                    r"\b(?:rekestnummer|rekestnr\.?|rekest\s?nr\.?)\s*(?:is|:|#|-)?\s*(?P<value>[A-Z0-9]{1,8}[-_/][A-Z0-9]{2,12}(?:[-_/][A-Z0-9]{1,12})?)\b",
                ),
            ],
            score=0.84,
            context=["rekestnummer", "verzoekschrift", "beschikking"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_DOSSIER_NUMBER",
            patterns=[
                (
                    "dossier_labeled_value",
                    rf"\b(?:dossiernummer|dossiernr\.?|dossier\s?nr\.?|kenmerk|referentie)\s*(?:is|:|#|-)?\s*(?P<value>(?:{UPPER}[A-Z0-9]{{1,7}}[-_/])?\d{{4}}[-_/]\d{{3,8}}|{UPPER}[A-Z0-9]{{1,7}}[-_/]\d{{3,12}}|\d{{5,12}})\b",
                ),
            ],
            score=0.83,
            context=["dossiernummer", "dossier", "kenmerk", "referentie", "advocaat"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_CLIENT_NUMBER",
            patterns=[
                (
                    "client_labeled_value",
                    rf"\b(?:cliëntnummer|clientnummer|cliëntnr\.?|clientnr\.?|cliënt\s?nr\.?|client\s?nr\.?)\s*(?:is|:|#|-)?\s*(?P<value>(?:{UPPER}[A-Z0-9]{{0,7}}[-_/])?\d{{3,12}}|{UPPER}[A-Z0-9]{{1,7}}[-_/]\d{{3,12}})\b",
                ),
            ],
            score=0.86,
            context=["cliëntnummer", "clientnummer", "cliënt", "client"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_CJIB_NUMBER",
            patterns=[
                (
                    "cjib_labeled_value",
                    r"\bcjib\s*[-\s]?\s*(?:nummer|nr\.?)?\s*(?:is|:|#|-)?\s*(?P<value>\d{8,16})\b",
                ),
            ],
            score=0.88,
            context=["cjib", "boete", "beschikking", "sanctie"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_POLICE_REPORT_NUMBER",
            patterns=[
                (
                    "police_report_labeled_value",
                    r"\b(?:proces-verbaalnummer|proces-verbaal\s?nr\.?|pv-nummer|pv\s?nr\.?)\s*(?:is|:|#|-)?\s*(?P<value>[A-Z0-9][A-Z0-9./_-]{4,30})\b",
                ),
            ],
            score=0.84,
            context=["proces-verbaal", "politie", "aangifte", "strafzaak"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_INSURANCE_CLAIM_NUMBER",
            patterns=[
                (
                    "insurance_claim_labeled_value",
                    rf"\b(?:schadenummer|schadenr\.?|claimnummer|claimnr\.?|polisnummer|polisnr\.?)\s*(?:is|:|#|-)?\s*(?P<value>(?:{UPPER}[A-Z0-9]{{1,7}}[-_/])?\d{{4}}[-_/]\d{{3,12}}|{UPPER}[A-Z0-9]{{1,7}}[-_/]\d{{4,12}}|\d{{5,16}})\b",
                ),
            ],
            score=0.87,
            context=["schadenummer", "claimnummer", "polisnummer", "verzekeraar"],
            supported_language=supported_language,
        ),
        RegexCaptureRecognizer(
            entity="NL_LEGAL_PARTY_NAME",
            patterns=[
                (
                    "legal_role_name_value_only",
                    rf"\b(?:eiser|gedaagde|verzoeker|verweerder|appellant|geïntimeerde|geintimeerde|belanghebbende|verdachte|slachtoffer|benadeelde[ \t]+partij|minderjarige|cliënt|client|tegenpartij|wederpartij)[ \t]+(?:(?:de[ \t]+heer|mevrouw|mr\.?|drs\.?)[ \t]+)?(?P<value>{NAME_VALUE})\b",
                ),
            ],
            score=0.79,
            context=LEGAL_ROLE_CONTEXT,
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_COURT_OR_AUTHORITY",
            regex=(
                r"\b(?:Rechtbank|Gerechtshof|Hoge[ \t]+Raad|Raad[ \t]+van[ \t]+State|"
                r"Centrale[ \t]+Raad[ \t]+van[ \t]+Beroep|College[ \t]+van[ \t]+Beroep[ \t]+voor[ \t]+het[ \t]+bedrijfsleven)"
                rf"(?:[ \t]+{NAME_TOKEN}){{0,3}}\b"
            ),
            score=0.70,
            context=["rechtbank", "gerechtshof", "hoge raad", "uitspraak", "zitting"],
            supported_language=supported_language,
        ),
    ]


    legal_recognizers.append(DutchContextualReferenceRecognizer(supported_language=supported_language))

    return general_recognizers + legal_recognizers
