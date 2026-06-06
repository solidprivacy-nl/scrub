"""Dutch / European recognizers for the SolidPrivacy Scrub Presidio app.

These recognizers are intentionally pattern-based and conservative. They are
registered under language='en' because the current demo analyses with
language='en' and uses English NER models. The entity names are Dutch/EU
specific, but the recognizers can run without requiring a Dutch NLP model.

2026-06 update:
- BSN detection is now stricter and no longer accepts date-like values such as
  15-12-2025.
- Dutch phone detection is stricter and no longer accepts date-like values such
  as 20-11-2025.
"""

from __future__ import annotations

import re
from typing import Iterable, List

from presidio_analyzer import Pattern, PatternRecognizer


DUTCH_ENTITY_NAMES = [
    "NL_BSN",
    "NL_POSTCODE",
    "NL_IBAN",
    "NL_KVK_NUMBER",
    "NL_VAT_NUMBER",
    "NL_PHONE_NUMBER",
    "NL_LICENSE_PLATE",
    "NL_DRIVER_LICENSE",
    "NL_BIG_NUMBER",
]


def _digits(value: str) -> str:
    return re.sub(r"\D", "", value or "")


def _looks_like_date(value: str) -> bool:
    """Return True for common date-shaped strings.

    This prevents Dutch recognizers from classifying dates such as
    15-12-2025 or 2025-12-15 as BSNs or phone numbers.
    """

    text = (value or "").strip()

    if re.fullmatch(r"\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}", text):
        return True

    if re.fullmatch(r"\d{4}[-/.]\d{1,2}[-/.]\d{1,2}", text):
        return True

    return False


class DutchBSNRecognizer(PatternRecognizer):
    """Recognize Dutch BSN candidates using pattern + 11-test validation.

    Deliberately conservative:
    - accepts only contiguous 8 or 9 digit values;
    - rejects date-shaped values;
    - validates with the Dutch 11-test.

    This avoids false positives like 15-12-2025 becoming NL_BSN.
    """

    PATTERNS = [
        Pattern(
            name="nl_bsn_contiguous_8_or_9_digits",
            regex=r"(?<!\d)\d{8,9}(?!\d)",
            score=0.45,
        )
    ]

    CONTEXT = [
        "bsn",
        "burgerservicenummer",
        "sofinummer",
        "persoonsnummer",
        "burger service nummer",
    ]

    def __init__(self, supported_language: str = "en"):
        super().__init__(
            supported_entity="NL_BSN",
            patterns=self.PATTERNS,
            context=self.CONTEXT,
            supported_language=supported_language,
        )

    @classmethod
    def is_valid_bsn(cls, value: str) -> bool:
        if _looks_like_date(value):
            return False

        # Be conservative: a BSN should be written as digits only here.
        if not re.fullmatch(r"\d{8,9}", (value or "").strip()):
            return False

        digits = _digits(value)

        if len(digits) == 8:
            # BSNs can effectively be represented with a leading zero.
            digits = "0" + digits

        if len(digits) != 9:
            return False

        # Avoid obvious false positives such as 000000000 or 111111111.
        if len(set(digits)) == 1:
            return False

        numbers = [int(d) for d in digits]
        checksum = sum(numbers[i] * (9 - i) for i in range(8)) - numbers[8]
        return checksum % 11 == 0

    def validate_result(self, pattern_text: str) -> bool:
        return self.is_valid_bsn(pattern_text)


class DutchPhoneRecognizer(PatternRecognizer):
    """Recognize Dutch phone numbers conservatively.

    This recognizer avoids broad numeric matching. It accepts common Dutch
    phone formats such as:
    - 0612345678
    - 06 12345678
    - +31 6 12345678
    - 0201234567
    - 020 123 4567

    It rejects date-shaped values such as 20-11-2025.
    """

    PATTERNS = [
        Pattern(
            name="nl_mobile_phone",
            regex=(
                r"(?<![A-Za-z0-9])(?:06(?:[\s\-]?\d){8}|"
                r"(?:\+31|0031)[\s\-]?6(?:[\s\-]?\d){8})(?![A-Za-z0-9])"
            ),
            score=0.82,
        ),
        Pattern(
            name="nl_landline_phone",
            regex=(
                r"(?<![A-Za-z0-9])(?:0[1-9]\d{1,2}[\s\-]?\d{6,7}|"
                r"(?:\+31|0031)[\s\-]?[1-9]\d{1,2}[\s\-]?\d{6,7})(?![A-Za-z0-9])"
            ),
            score=0.72,
        ),
    ]

    CONTEXT = [
        "tel",
        "telefoon",
        "telefoonnummer",
        "mobiel",
        "mobiele nummer",
        "phone",
        "nummer",
        "contact",
    ]

    def __init__(self, supported_language: str = "en"):
        super().__init__(
            supported_entity="NL_PHONE_NUMBER",
            patterns=self.PATTERNS,
            context=self.CONTEXT,
            supported_language=supported_language,
        )

    @staticmethod
    def _normalise_to_dutch_digits(value: str) -> str:
        digits = _digits(value)

        if digits.startswith("0031"):
            return "0" + digits[4:]

        if digits.startswith("31"):
            return "0" + digits[2:]

        return digits

    @classmethod
    def is_valid_phone(cls, value: str) -> bool:
        if _looks_like_date(value):
            return False

        digits = cls._normalise_to_dutch_digits(value)

        # Normal Dutch phone numbers have 10 digits after normalisation.
        if len(digits) != 10:
            return False

        if not digits.startswith("0"):
            return False

        # Avoid repeated fake values.
        if len(set(digits)) <= 2:
            return False

        return True

    def validate_result(self, pattern_text: str) -> bool:
        return self.is_valid_phone(pattern_text)


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


def get_dutch_entity_names() -> List[str]:
    return list(DUTCH_ENTITY_NAMES)


def get_dutch_recognizers(supported_language: str = "en") -> List[PatternRecognizer]:
    """Return Dutch/EU recognizers for the current app.

    Keep these recognizers conservative enough for legal/business documents:
    high-confidence formats use higher scores; generic numeric identifiers use
    context words and lower scores to reduce false positives.
    """

    return [
        DutchBSNRecognizer(supported_language=supported_language),
        _pattern_recognizer(
            entity="NL_POSTCODE",
            regex=r"[1-9][0-9]{3}\s?[A-Z]{2}",
            score=0.80,
            context=["postcode", "adres", "woonplaats", "plaats"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_IBAN",
            regex=r"NL\s?\d{2}\s?[A-Z]{4}\s?(?:\d\s?){10}",
            score=0.90,
            context=["iban", "rekening", "rekeningnummer", "bankrekening"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_VAT_NUMBER",
            regex=r"NL\s?\d{9}\s?B\s?\d{2}",
            score=0.90,
            context=["btw", "btw-nummer", "vat", "vat number", "omzetbelasting"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_KVK_NUMBER",
            # Kept contiguous only; date-shaped strings are not candidates.
            regex=r"(?<!\d)\d{8}(?!\d)",
            score=0.35,
            context=["kvk", "kamer van koophandel", "handelsregister", "kvk-nummer"],
            supported_language=supported_language,
        ),
        DutchPhoneRecognizer(supported_language=supported_language),
        _pattern_recognizer(
            entity="NL_LICENSE_PLATE",
            # Conservative Dutch-style license plate pattern, requiring separators.
            regex=r"(?:[A-Z]{2}-\d{2}-\d{2}|\d{2}-\d{2}-[A-Z]{2}|\d{2}-[A-Z]{2}-\d{2}|[A-Z]{2}-\d{2}-[A-Z]{2}|[A-Z]{2}-[A-Z]{2}-\d{2}|\d{2}-[A-Z]{2}-[A-Z]{2})",
            score=0.70,
            context=["kenteken", "license plate", "voertuig", "auto"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_DRIVER_LICENSE",
            # Kept context-sensitive because document number formats can vary.
            regex=r"(?<!\d)\d{10}(?!\d)",
            score=0.30,
            context=["rijbewijs", "rijbewijsnummer", "driver license", "driving licence"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_BIG_NUMBER",
            regex=r"(?<!\d)\d{11}(?!\d)",
            score=0.35,
            context=["big", "big-register", "big nummer", "big-nummer", "zorgverlener"],
            supported_language=supported_language,
        ),
    ]
