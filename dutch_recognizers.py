"""Dutch / European recognizers for the SolidPrivacy Scrub Presidio app.

These recognizers are intentionally pattern-based and conservative. They are
registered under language='en' because the current demo analyses with
language='en' and uses English NER models. The entity names are Dutch/EU
specific, but the recognizers can run without requiring a Dutch NLP model.
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


class DutchBSNRecognizer(PatternRecognizer):
    """Recognize Dutch BSN candidates using pattern + 11-test validation."""

    PATTERNS = [
        Pattern(
            name="nl_bsn_candidate_8_or_9_digits",
            regex=r"(?<!\d)(?:\d[\s\-.]?){8,9}(?!\d)",
            score=0.35,
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

    @staticmethod
    def _digits(value: str) -> str:
        return re.sub(r"\D", "", value or "")

    @classmethod
    def is_valid_bsn(cls, value: str) -> bool:
        digits = cls._digits(value)

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
            regex=r"\b\d{8}\b",
            score=0.35,
            context=["kvk", "kamer van koophandel", "handelsregister", "kvk-nummer"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_PHONE_NUMBER",
            regex=r"(?<!\w)(?:\+31|0031|0)(?:[\s\-\.]?\d){8,10}(?!\w)",
            score=0.65,
            context=["tel", "telefoon", "mobiel", "phone", "nummer"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_LICENSE_PLATE",
            # Conservative Dutch-style license plate pattern, requiring separators.
            regex=r"\b(?:[A-Z]{2}-\d{2}-\d{2}|\d{2}-\d{2}-[A-Z]{2}|\d{2}-[A-Z]{2}-\d{2}|[A-Z]{2}-\d{2}-[A-Z]{2}|[A-Z]{2}-[A-Z]{2}-\d{2}|\d{2}-[A-Z]{2}-[A-Z]{2})\b",
            score=0.70,
            context=["kenteken", "license plate", "voertuig", "auto"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_DRIVER_LICENSE",
            # Kept context-sensitive because document number formats can vary.
            regex=r"\b\d{10}\b",
            score=0.30,
            context=["rijbewijs", "rijbewijsnummer", "driver license", "driving licence"],
            supported_language=supported_language,
        ),
        _pattern_recognizer(
            entity="NL_BIG_NUMBER",
            regex=r"\b\d{11}\b",
            score=0.35,
            context=["big", "big-register", "big nummer", "big-nummer", "zorgverlener"],
            supported_language=supported_language,
        ),
    ]
