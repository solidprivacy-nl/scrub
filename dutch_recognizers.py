"""Dutch / European + Dutch legal recognizers for SolidPrivacy Scrub.

Design goals:
- local-first/offline compatible;
- conservative pattern recognition with validation where possible;
- directly usable by the existing Presidio Streamlit demo;
- registered under language="en" by default because the current demo analyses
  with English NER models while adding Dutch pattern recognizers.

Phase 1-3 update:
- keeps the existing Dutch/EU recognizers;
- adds Dutch legal-profession recognizers;
- tightens false-positive behaviour around BSN, dates and phone numbers;
- adds entity helper functions so the UI can distinguish General Dutch from
  Dutch Legal Strict mode.
"""

from __future__ import annotations

import re
from typing import Iterable, List

from presidio_analyzer import Pattern, PatternRecognizer


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
]


# -------------------------
# Utility / validation logic
# -------------------------


def _digits(value: str) -> str:
    return re.sub(r"\D", "", value or "")


def _looks_like_date(value: str) -> bool:
    """Return True for common date-shaped strings.

    Prevents Dutch recognizers from classifying dates such as 15-12-2025,
    2025-12-15 or 15122025 as BSNs or phone numbers.
    """
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


# -------------------------
# Validated recognizers
# -------------------------


class DutchBSNRecognizer(PatternRecognizer):
    """Recognize Dutch BSN candidates using pattern + 11-test validation.

    Conservative by design:
    - accepts only contiguous 8 or 9 digit values;
    - rejects date-shaped values;
    - rejects phone-shaped values;
    - validates with the Dutch 11-proef.
    """

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


def get_dutch_recognizers(supported_language: str = "en") -> List[PatternRecognizer]:
    """Return Dutch/EU + Dutch legal recognizers for the current app.

    The recognizers stay conservative enough for legal/business documents:
    high-confidence formats use higher scores; generic matter identifiers require
    legal context words in the actual match to avoid broad false positives.
    """

    general_recognizers: List[PatternRecognizer] = [
        DutchBSNRecognizer(supported_language=supported_language),
        DutchPhoneRecognizer(supported_language=supported_language),
        _pattern_recognizer(
            entity="NL_POSTCODE",
            regex=r"\b[1-9][0-9]{3}\s?[A-Z]{2}\b",
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
        _pattern_recognizer(
            entity="NL_KVK_NUMBER",
            regex=(
                r"\b(?:kvk(?:[-\s]?nummer|\s?nr\.)?|kamer\s+van\s+koophandel)"
                r"[:\s#-]*\d{8}\b"
            ),
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
        _pattern_recognizer(
            entity="NL_DRIVER_LICENSE",
            regex=(
                r"\b(?:rijbewijs(?:nummer)?|rijbewijsnr\.?|rijbewijs nr\.?)"
                r"[:\s#-]*[A-Z0-9]{7,12}\b"
            ),
            score=0.82,
            context=["rijbewijs", "rijbewijsnummer"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_BIG_NUMBER",
            regex=r"\b(?:big(?:[-\s]?nummer|\s?nr\.)?)[:\s#-]*\d{11}\b",
            score=0.86,
            context=["big", "big-nummer", "zorgverlener", "arts"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_ADDRESS",
            regex=(
                r"\b[A-ZÀ-ÖØ-Þ][\wÀ-ÿ'’.-]*(?:\s+[A-ZÀ-ÖØ-Þa-zà-ÿ][\wÀ-ÿ'’.-]*){0,3}"
                r"(?:straat|laan|weg|plein|dreef|hof|kade|singel|gracht|steeg|park|boulevard|pad|plantsoen)"
                r"\s+\d{1,5}\s?[A-Za-z]{0,3}"
                r"(?:\s*,?\s*[1-9][0-9]{3}\s?[A-Z]{2}\s+[A-ZÀ-ÖØ-Þ][\wÀ-ÿ'’.-]*(?:\s+[A-ZÀ-ÖØ-Þa-zà-ÿ][\wÀ-ÿ'’.-]*){0,3})?\b"
            ),
            score=0.66,
            context=["adres", "woonadres", "vestigingsadres", "straat", "huisnummer"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_DATE_OF_BIRTH",
            regex=(
                r"\b(?:geboortedatum|geb\.\s?datum|geboren\s+op|datum\s+geboorte|dob)"
                r"[:\s]*(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}[-/.]\d{1,2}[-/.]\d{1,2})\b"
            ),
            score=0.84,
            context=["geboortedatum", "geboren", "datum geboorte"],
            supported_language=supported_language,
        ),
    ]

    legal_recognizers: List[PatternRecognizer] = [
        _pattern_recognizer(
            entity="NL_ECLI",
            regex=r"\bECLI:NL:[A-Z0-9]{2,12}:\d{4}:[A-Z0-9.:-]+\b",
            score=0.95,
            context=["ecli", "uitspraak", "vonnis", "arrest", "beschikking"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_PARKETNUMMER",
            regex=(
                r"\b(?:parketnummer|parketnr\.?|parket\s?nr\.?)[:\s]*\d{2}/\d{6}-\d{2}\b"
                r"|\b\d{2}/\d{6}-\d{2}\b"
            ),
            score=0.88,
            context=["parketnummer", "officier", "strafzaak", "tenlastelegging"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_LEGAL_CASE_NUMBER",
            regex=(
                r"\b(?:zaaknummer|zaaknr\.?|zaak\s?nr\.?|zaak-/rolnummer)[:\s#-]*"
                r"[A-Z0-9][A-Z0-9 ./-]{4,60}\b"
                r"|\bC/\d{2}/\d{5,6}\s*/\s*(?:HA|KG|FA|JE|CV|RK|ZA|EXPL|VERZ|BESL)"
                r"\s*[A-Z]{0,3}\s*\d{2}[-/]\d{1,5}\b"
            ),
            score=0.86,
            context=["zaaknummer", "rolnummer", "rechtbank", "procedure"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_ROLNUMMER",
            regex=(
                r"\b(?:rolnummer|rolnr\.?|rol\s?nr\.?)[:\s#-]*"
                r"[A-Z0-9][A-Z0-9 ./-]{4,45}\b"
            ),
            score=0.84,
            context=["rolnummer", "rolnr", "civiel", "procedure"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_REKESTNUMMER",
            regex=(
                r"\b(?:rekestnummer|rekestnr\.?|rekest\s?nr\.?)[:\s#-]*"
                r"[A-Z0-9][A-Z0-9 ./-]{4,45}\b"
            ),
            score=0.84,
            context=["rekestnummer", "verzoekschrift", "beschikking"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_DOSSIER_NUMBER",
            regex=(
                r"\b(?:dossiernummer|dossiernr\.?|dossier\s?nr\.?|dossier|kenmerk|referentie)"
                r"[:\s#-]*[A-Z0-9][A-Z0-9./_-]{3,30}\b"
            ),
            score=0.78,
            context=["dossiernummer", "dossier", "kenmerk", "referentie", "advocaat"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_CLIENT_NUMBER",
            regex=(
                r"\b(?:cliëntnummer|clientnummer|cliëntnr\.?|clientnr\.?|cliënt\s?nr\.?|client\s?nr\.?)"
                r"[:\s#-]*[A-Z0-9][A-Z0-9./_-]{3,24}\b"
            ),
            score=0.82,
            context=["cliëntnummer", "clientnummer", "cliënt", "client"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_CJIB_NUMBER",
            regex=(
                r"\b(?:cjib(?:[-\s]?(?:nummer|nr\.?)?)?)[:\s#-]*\d{8,16}\b"
            ),
            score=0.86,
            context=["cjib", "boete", "beschikking", "sanctie"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_POLICE_REPORT_NUMBER",
            regex=(
                r"\b(?:proces-verbaalnummer|proces-verbaal\s?nr\.?|pv-nummer|pv\s?nr\.?)"
                r"[:\s#-]*[A-Z0-9][A-Z0-9./_-]{4,30}\b"
            ),
            score=0.82,
            context=["proces-verbaal", "politie", "aangifte", "strafzaak"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_INSURANCE_CLAIM_NUMBER",
            regex=(
                r"\b(?:schadenummer|schadenr\.?|claimnummer|claimnr\.?|polisnummer|polisnr\.?)"
                r"[:\s#-]*[A-Z0-9][A-Z0-9./_-]{4,30}\b"
            ),
            score=0.80,
            context=["schadenummer", "claimnummer", "polisnummer", "verzekeraar"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_LEGAL_PARTY_NAME",
            regex=(
                r"\b(?:eiser|gedaagde|verzoeker|verweerder|appellant|geïntimeerde|geintimeerde|"
                r"belanghebbende|verdachte|slachtoffer|benadeelde\s+partij|minderjarige|cliënt|client|"
                r"tegenpartij|wederpartij)\s+(?:de\s+heer|mevrouw|mr\.?|drs\.?)?\s*"
                r"[A-ZÀ-ÖØ-Þ][\wÀ-ÿ'’.-]+(?:\s+(?:van|de|der|den|ten|ter|el|al|la|du|op|aan|"
                r"[A-ZÀ-ÖØ-Þ][\wÀ-ÿ'’.-]+)){0,5}\b"
            ),
            score=0.76,
            context=LEGAL_ROLE_CONTEXT,
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_COURT_OR_AUTHORITY",
            regex=(
                r"\b(?:Rechtbank|Gerechtshof|Hoge\s+Raad|Raad\s+van\s+State|"
                r"Centrale\s+Raad\s+van\s+Beroep|College\s+van\s+Beroep\s+voor\s+het\s+bedrijfsleven)"
                r"(?:\s+[A-ZÀ-ÖØ-Þ][\wÀ-ÿ'’.-]+){0,5}\b"
            ),
            score=0.70,
            context=["rechtbank", "gerechtshof", "hoge raad", "uitspraak", "zitting"],
            supported_language=supported_language,
        ),
    ]

    return general_recognizers + legal_recognizers
