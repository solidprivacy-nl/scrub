from __future__ import annotations

import re
from typing import Any


LEGAL_REFERENCE_TEXT = " ".join(
    [
        "Rolnummer 10598721 / UE VERZ 26-441 staat vermeld op de beschikking.",
        "Ook zaak ARN 26/4412 wordt genoemd.",
        "De zaakreferentie ZK-WOON-55091 hoort bij clientreferentie CL-FAM-55201.",
        "De interne klantreferentie is WR-KLANT-2026-7712.",
        "Factuur FACT-2026-4481 hoort bij camera CAM-MAAS-2026-0518.",
        "Incident INC-2026-0912 en reparatie REP-2026-4410 staan in het dossier.",
        "Referentie CLM-2026-112233 hoort bij de letselschadezaak.",
    ]
)

CLIENT_DOSSIER_TEXT = (
    "De client met clientnummer CLNT-2026-0042 is gekoppeld aan "
    "dossiernummer DOS-2026-778899 en zaaknummer ZK-WOON-55091."
)

ROLE_ONLY_TEXT = (
    "De eiser verklaarde dat de verweerder aanwezig was. "
    "De getuige sprak met de arts. "
    "Het slachtoffer en de minderjarige worden alleen als rol aangeduid."
)

OVERMASKING_TEXT = (
    "De minderjarige bezocht de arts. "
    "De getuige verklaarde dat het slachtoffer niet thuis was."
)

LEGAL_REFERENCE_VALUES = [
    "10598721 / UE VERZ 26-441",
    "ARN 26/4412",
    "ZK-WOON-55091",
    "CL-FAM-55201",
    "WR-KLANT-2026-7712",
    "FACT-2026-4481",
    "CAM-MAAS-2026-0518",
    "INC-2026-0912",
    "REP-2026-4410",
    "CLM-2026-112233",
]

CLIENT_DOSSIER_VALUES = [
    "CLNT-2026-0042",
    "DOS-2026-778899",
    "ZK-WOON-55091",
]

ROLE_WORDS = ["eiser", "verweerder", "getuige", "arts", "slachtoffer", "minderjarige"]


def _normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def _result_to_row(text: str, result: Any, source: str) -> dict[str, Any]:
    if isinstance(result, dict):
        return {
            "text": str(result.get("text", "")),
            "entity_type": str(result.get("entity_type", "")),
            "start": result.get("start"),
            "end": result.get("end"),
            "source": source,
        }

    start = getattr(result, "start", None)
    end = getattr(result, "end", None)
    detected_text = text[start:end] if isinstance(start, int) and isinstance(end, int) else ""
    return {
        "text": detected_text,
        "entity_type": str(getattr(result, "entity_type", "") or ""),
        "start": start,
        "end": end,
        "source": source,
    }


def _detected_rows(text: str) -> list[dict[str, Any]]:
    from candidate_scanner import scan_unmasked_candidates
    from dutch_recognizers import get_dutch_entity_names, get_dutch_recognizers

    rows: list[dict[str, Any]] = []
    analyzer_results = []
    entities = get_dutch_entity_names(include_legal=True)
    for recognizer in get_dutch_recognizers(supported_language="en"):
        recognizer_results = list(recognizer.analyze(text, entities=entities, nlp_artifacts=None))
        analyzer_results.extend(recognizer_results)
        rows.extend(_result_to_row(text, result, recognizer.name) for result in recognizer_results)

    rows.extend(_result_to_row(text, result, "candidate_scanner") for result in scan_unmasked_candidates(text, analyzer_results=[]))
    return rows


def _detected_blob(rows: list[dict[str, Any]]) -> str:
    return "\n".join(_normalize(row["text"]) for row in rows if row.get("text"))


def _missing_values(rows: list[dict[str, Any]], expected_values: list[str]) -> list[str]:
    detected = _detected_blob(rows)
    return [value for value in expected_values if _normalize(value) not in detected]


def _mask_analyzer_spans(text: str, rows: list[dict[str, Any]]) -> str:
    masked = text
    spans: list[tuple[int, int]] = []
    for row in rows:
        start = row.get("start")
        end = row.get("end")
        if isinstance(start, int) and isinstance(end, int) and 0 <= start < end <= len(text):
            spans.append((start, end))
    for start, end in sorted(set(spans), reverse=True):
        masked = masked[:start] + "[MASK]" + masked[end:]
    return masked


def test_synthetic_gap_fixture_contains_required_legal_references():
    for value in LEGAL_REFERENCE_VALUES:
        assert value in LEGAL_REFERENCE_TEXT


def test_synthetic_role_fixture_contains_only_generic_role_words():
    lowered = ROLE_ONLY_TEXT.lower()
    for role in ROLE_WORDS:
        assert role in lowered


def test_legal_reference_numbers_are_detectable():
    rows = _detected_rows(LEGAL_REFERENCE_TEXT)

    missing = _missing_values(rows, LEGAL_REFERENCE_VALUES)

    assert missing == []


def test_clm_reference_must_not_be_phone_number():
    rows = _detected_rows(LEGAL_REFERENCE_TEXT)

    clm_rows = [row for row in rows if _normalize("CLM-2026-112233") in _normalize(row["text"])]

    assert clm_rows, "CLM-2026-112233 should be detected as a legal reference value"
    assert all("PHONE" not in row["entity_type"].upper() for row in clm_rows)


def test_client_dossier_and_zaak_numbers_are_detectable():
    rows = _detected_rows(CLIENT_DOSSIER_TEXT)

    missing = _missing_values(rows, CLIENT_DOSSIER_VALUES)

    assert missing == []


def test_rechtspraak_like_rolnummers_are_detectable():
    rows = _detected_rows(LEGAL_REFERENCE_TEXT)

    missing = _missing_values(rows, ["10598721 / UE VERZ 26-441", "ARN 26/4412"])

    assert missing == []


def test_role_words_alone_are_not_detected_as_person_values():
    rows = _detected_rows(ROLE_ONLY_TEXT)

    detected_person_values = {
        _normalize(row["text"])
        for row in rows
        if "PERSON" in row["entity_type"].upper() or "PERSOON" in row["entity_type"].upper()
    }

    assert detected_person_values.isdisjoint({_normalize(role) for role in ROLE_WORDS})


def test_overmasking_does_not_remove_legal_role_structure():
    rows = _detected_rows(OVERMASKING_TEXT)
    masked_text = _mask_analyzer_spans(OVERMASKING_TEXT, rows).lower()

    for role in ["minderjarige", "arts", "getuige", "slachtoffer"]:
        assert role in masked_text
    assert masked_text.count("[mask]") < 4
