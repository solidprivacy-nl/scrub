"""Pure Dutch care recognizers for SolidPrivacy Scrub Zorgfilter v1.

The module implements the frozen care-recognizer contract only. It is not
registered in the current app yet and contains no Streamlit, network, AI, cloud
or file-system behavior.

The current application analyses with ``language="en"`` while adding Dutch
custom recognizers. Therefore these recognizers default to
``supported_language="en"``.
"""

from __future__ import annotations

import re
from typing import Iterable, List, Sequence, Tuple

from presidio_analyzer import (
    AnalysisExplanation,
    EntityRecognizer,
    RecognizerResult,
)


DUTCH_CARE_ENTITY_NAMES: tuple[str, ...] = (
    "NL_PATIENT_NUMBER",
    "NL_CARE_CLIENT_NUMBER",
    "NL_MEDICAL_RECORD_NUMBER",
    "NL_EPD_ECD_NUMBER",
    "NL_HEALTH_INSURANCE_NUMBER",
    "NL_REFERRAL_NUMBER",
    "NL_TREATMENT_REFERENCE",
    "NL_LAB_SAMPLE_NUMBER",
    "NL_CARE_INCIDENT_NUMBER",
    "NL_CARE_INDICATION_REFERENCE",
    "NL_AGB_CODE",
    "NL_CARE_PROVIDER_NAME",
    "NL_CARE_ORGANIZATION",
    "NL_CARE_LOCATION_REFERENCE",
    "NL_ROOM_OR_BED_REFERENCE",
    "NL_CARE_EVENT_DATE",
)

# Keep name recognition strict and label-bound. Generic PERSON recognition stays
# in the generic local NER/profile layer.
UPPER = r"(?-i:[A-ZÀ-ÖØ-Þ])"
NAME_TOKEN = rf"{UPPER}[A-Za-zÀ-ÖØ-öø-ÿ'’\-]*"
NAME_PARTICLE = r"(?:van|de|der|den|ten|ter|el|al|la|du|op|aan|bin|ibn)"
NAME_GAP = r"[ \t]+"
NAME_VALUE = (
    rf"{NAME_TOKEN}"
    rf"(?:(?:{NAME_GAP}{NAME_PARTICLE})?{NAME_GAP}{NAME_TOKEN}){{0,4}}"
)

DATE_VALUE = r"\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}[-/.]\d{1,2}[-/.]\d{1,2}"
# Strong labels make numeric patient identifiers safe to support. Unlabelled
# numeric strings are deliberately outside this module.
REFERENCE_VALUE = r"(?:[A-Z0-9]+(?:[-_/][A-Z0-9]+){1,8}|\d{5,16})"


class CareRegexCaptureRecognizer(EntityRecognizer):
    """Return only a named ``value`` capture from bounded care-context regexes."""

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
            name=f"{entity}_care_capture_recognizer",
        )
        self.entity = entity
        self.patterns = tuple(
            (
                name,
                re.compile(pattern, flags=re.IGNORECASE | re.MULTILINE),
            )
            for name, pattern in patterns
        )
        self.score = float(score)
        self.context = tuple(context or ())

    def load(self) -> None:
        return None

    def analyze(
        self,
        text: str,
        entities: List[str],
        nlp_artifacts=None,
    ) -> List[RecognizerResult]:
        if entities and self.entity not in entities:
            return []

        source_text = text or ""
        results: List[RecognizerResult] = []
        seen: set[tuple[int, int]] = set()

        for pattern_name, pattern in self.patterns:
            for match in pattern.finditer(source_text):
                if "value" not in match.groupdict() or match.group("value") is None:
                    continue
                start, end = match.span("value")

                while start < end and source_text[start].isspace():
                    start += 1
                while end > start and source_text[end - 1] in " \t\r\n.,;:":
                    end -= 1
                if start >= end or (start, end) in seen:
                    continue
                seen.add((start, end))

                explanation = AnalysisExplanation(
                    recognizer=self.name,
                    original_score=self.score,
                    pattern_name=pattern_name,
                    pattern=pattern.pattern,
                    textual_explanation=(
                        f"Detected by `{self.name}` using bounded care-context "
                        f"pattern `{pattern_name}`. Only the named value span is "
                        "returned so the care label, professional role and clinical "
                        "meaning remain readable."
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
                            RecognizerResult.RECOGNIZER_IDENTIFIER_KEY: getattr(
                                self, "id", self.name
                            ),
                        },
                    )
                )

        return results


def _reference_recognizer(
    entity: str,
    labels_regex: str,
    score: float,
    supported_language: str,
) -> CareRegexCaptureRecognizer:
    return CareRegexCaptureRecognizer(
        entity=entity,
        patterns=[
            (
                f"{entity.lower()}_labelled_value",
                rf"(?<!\w)(?:{labels_regex})(?!\w)\s*(?:is|:|#|=|-)?\s*"
                rf"(?P<value>{REFERENCE_VALUE})(?![A-Z0-9_/-])",
            )
        ],
        score=score,
        context=re.split(r"\|", labels_regex),
        supported_language=supported_language,
    )


def _provider_recognizer(supported_language: str) -> CareRegexCaptureRecognizer:
    title = r"(?:(?:dr|dokter)\.?\s+)?"
    patterns = [
        (
            "reporter_with_professional_role",
            rf"\brapporteur\s*:\s*(?:verpleegkundige|verzorgende(?:\s+IG)?|"
            rf"persoonlijk\s+begeleider|zorgco[oö]rdinator)\s+{title}"
            rf"(?P<value>{NAME_VALUE})\b",
        ),
        (
            "reporting_or_transfer_role",
            rf"\b(?:overdragend\s+verpleegkundige|persoonlijk\s+begeleider|"
            rf"behandelend\s+(?:internist|arts|specialist)|hoofdbehandelaar|"
            rf"regiebehandelaar|huisarts|betrokken\s+arts|aanvrager)\s*:\s*"
            rf"{title}(?P<value>{NAME_VALUE})\b",
        ),
        (
            "prescriber_with_optional_role",
            rf"\bvoorschrijver\s*:\s*(?:(?:huisarts|arts|specialist|apotheker)\s+)?"
            rf"{title}(?P<value>{NAME_VALUE})\b",
        ),
        (
            "incident_reporter_with_role",
            rf"\bmelder\s*:\s*(?:verzorgende(?:\s+IG)?|verpleegkundige|arts|"
            rf"persoonlijk\s+begeleider)\s+{title}(?P<value>{NAME_VALUE})\b",
        ),
    ]
    return CareRegexCaptureRecognizer(
        entity="NL_CARE_PROVIDER_NAME",
        patterns=patterns,
        score=0.84,
        context=(
            "rapporteur",
            "verpleegkundige",
            "huisarts",
            "behandelend arts",
            "persoonlijk begeleider",
            "voorschrijver",
            "melder",
        ),
        supported_language=supported_language,
    )


def _organization_recognizer(supported_language: str) -> CareRegexCaptureRecognizer:
    # Bounded to labelled fields and stopped before sublocation punctuation.
    organization_value = r"(?-i:[A-ZÀ-ÖØ-Þ])[^,\.\r\n]{1,79}?"
    patterns = [
        (
            "labelled_care_organization",
            rf"\b(?:zorgorganisatie|ziekenhuis|apotheek|laboratorium|"
            rf"verzendende\s+organisatie|ontvangende\s+organisatie)\s*:\s*"
            rf"(?P<value>{organization_value})(?=\s*(?:,|\.|\r?$))",
        ),
        (
            "location_line_primary_organization",
            rf"\blocatie\s*:\s*(?P<value>{organization_value})"
            rf"(?=\s*,\s*(?:woonlocatie|locatie|afdeling|team|kamer|bed|appartement)\b)",
        ),
        (
            "location_line_lowercase_care_organization",
            r"\blocatie\s*:\s*(?P<value>(?:woonzorgcentrum|zorgcentrum|"
            r"verpleeghuis|ziekenhuis|zorggroep)\s+"
            r"(?-i:[A-ZÀ-ÖØ-Þ])[^,\.\r\n]{1,60}?)"
            r"(?=\s*,\s*(?:woonlocatie|locatie|afdeling|team|kamer|bed|appartement)\b)",
        ),
        (
            "labelled_practice_phrase",
            rf"(?P<value>praktijk\s+(?-i:[A-ZÀ-ÖØ-Þ])[^,\.\r\n]{{1,60}}?)"
            rf"(?=\s*(?:,|\.|\r?$))",
        ),
    ]
    return CareRegexCaptureRecognizer(
        entity="NL_CARE_ORGANIZATION",
        patterns=patterns,
        score=0.74,
        context=(
            "zorgorganisatie",
            "ziekenhuis",
            "apotheek",
            "laboratorium",
            "praktijk",
            "verzendende organisatie",
            "ontvangende organisatie",
        ),
        supported_language=supported_language,
    )


def _location_recognizer(supported_language: str) -> CareRegexCaptureRecognizer:
    patterns = [
        (
            "bounded_named_care_location",
            r"(?P<value>\b(?:woonlocatie|locatie|afdeling|team)\s+"
            r"(?-i:[A-ZÀ-ÖØ-Þ])[A-Za-zÀ-ÖØ-öø-ÿ0-9'’\-]*"
            r"(?:[ \t]+[A-Za-zÀ-ÖØ-öø-ÿ0-9'’\-]+){0,4})"
            r"(?=\s*(?:,|\.|\r?$))",
        )
    ]
    return CareRegexCaptureRecognizer(
        entity="NL_CARE_LOCATION_REFERENCE",
        patterns=patterns,
        score=0.72,
        context=("woonlocatie", "locatie", "afdeling", "team"),
        supported_language=supported_language,
    )


def _room_bed_recognizer(supported_language: str) -> CareRegexCaptureRecognizer:
    return CareRegexCaptureRecognizer(
        entity="NL_ROOM_OR_BED_REFERENCE",
        patterns=[
            (
                "room_bed_or_apartment_code",
                r"(?P<value>\b(?:kamer|bed|appartement)\s+"
                r"(?:[A-Z](?:-[A-Z0-9]+)?|\d{1,4}[A-Z]?|[A-Z]\d{1,4}|"
                r"[A-Z0-9]+-[A-Z0-9]+))\b",
            )
        ],
        score=0.72,
        context=("kamer", "bed", "appartement"),
        supported_language=supported_language,
    )


def _event_date_recognizer(supported_language: str) -> CareRegexCaptureRecognizer:
    labels = (
        r"opnamedatum|ontslagdatum|rapportagedatum|evaluatiedatum|incidentdatum|"
        r"afnamedatum|afspraakdatum|behandeldatum|onderzoeksdatum"
    )
    return CareRegexCaptureRecognizer(
        entity="NL_CARE_EVENT_DATE",
        patterns=[
            (
                "labelled_care_event_date",
                rf"\b(?:{labels})\s*(?:is|:)?\s*(?P<value>{DATE_VALUE})\b",
            )
        ],
        score=0.82,
        context=tuple(labels.split("|")),
        supported_language=supported_language,
    )


def get_dutch_care_entity_names() -> List[str]:
    """Return the frozen dedicated Zorgfilter v1 entity names."""

    return list(DUTCH_CARE_ENTITY_NAMES)


def get_dutch_care_recognizers(
    supported_language: str = "en",
) -> List[EntityRecognizer]:
    """Return pure, context-bound Zorgfilter v1 recognizers.

    The returned recognizers are not automatically registered in the current
    application. Profile composition is handled in a later workpackage.
    """

    recognizers: List[EntityRecognizer] = [
        _reference_recognizer(
            "NL_PATIENT_NUMBER",
            r"pati[eë]ntnummer|patientnummer|pati[eë]ntnr\.?|patientnr\. ?",
            0.91,
            supported_language,
        ),
        _reference_recognizer(
            "NL_CARE_CLIENT_NUMBER",
            r"cli[eë]ntnummer|clientnummer|cli[eë]ntnr\.?|clientnr\.?",
            0.90,
            supported_language,
        ),
        _reference_recognizer(
            "NL_MEDICAL_RECORD_NUMBER",
            r"medisch\s+dossiernummer|zorgdossiernummer|medisch\s+dossiernr\. ?",
            0.90,
            supported_language,
        ),
        _reference_recognizer(
            "NL_EPD_ECD_NUMBER",
            r"EPD[-\s]?nummer|ECD[-\s]?nummer|EPD\s*nr\.?|ECD\s*nr\. ?",
            0.92,
            supported_language,
        ),
        _reference_recognizer(
            "NL_HEALTH_INSURANCE_NUMBER",
            r"verzekerdennummer|zorgverzekeringsnummer|verzekerdennr\. ?",
            0.90,
            supported_language,
        ),
        _reference_recognizer(
            "NL_REFERRAL_NUMBER",
            r"verwijsnummer|verwijzingsnummer|verwijsnr\. ?",
            0.90,
            supported_language,
        ),
        _reference_recognizer(
            "NL_TREATMENT_REFERENCE",
            r"behandelnummer|zorgtrajectnummer|receptnummer|behandelnr\.?|trajectnummer",
            0.88,
            supported_language,
        ),
        _reference_recognizer(
            "NL_LAB_SAMPLE_NUMBER",
            r"monsternummer|sample[-\s]?ID|labnummer|laboratoriumnummer|"
            r"accessienummer|onderzoeks[-\s]?ID",
            0.90,
            supported_language,
        ),
        _reference_recognizer(
            "NL_CARE_INCIDENT_NUMBER",
            r"MIC[-\s]?nummer|MIM[-\s]?nummer|VIM[-\s]?nummer|"
            r"zorgincidentnummer|incidentnummer|medicatiefoutnummer",
            0.91,
            supported_language,
        ),
        _reference_recognizer(
            "NL_CARE_INDICATION_REFERENCE",
            r"CIZ[-\s]?nummer|Wlz[-\s]?indicatie|Wmo[-\s]?beschikking|"
            r"zorgtoewijzing|PGB[-\s]?nummer|indicatiebesluit",
            0.90,
            supported_language,
        ),
        CareRegexCaptureRecognizer(
            entity="NL_AGB_CODE",
            patterns=[
                (
                    "strong_agb_context_eight_digits",
                    r"\b(?:AGB[-\s]?(?:code|nummer|nr\.?)|AGB)\s*(?:is|:|#|=|-)?\s*"
                    r"(?P<value>\d{8})\b",
                )
            ],
            score=0.94,
            context=("AGB-code", "AGB-nummer", "AGB"),
            supported_language=supported_language,
        ),
        _provider_recognizer(supported_language),
        _organization_recognizer(supported_language),
        _location_recognizer(supported_language),
        _room_bed_recognizer(supported_language),
        _event_date_recognizer(supported_language),
    ]
    return recognizers
