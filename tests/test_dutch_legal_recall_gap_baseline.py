from __future__ import annotations

import re
from typing import Any

import pytest


LEGAL_REFERENCE_TEXT = " ".join(
    [
        "Rolnummer 10598721 / UE VERZ 26-441 staat vermeld op de beschikking.",
        "Ook zaak ARN 26/4412 wordt genoemd.",
        "De zaakreferentie ZK-WOON-55091 hoort bij clientreferentie CL-FAM-55201.",
        "De interne klantreferentie is WR-KLANT-2026-7712.",
        "Factuur FACT-2026-4481 hoort bij camera CAM-MAAS-2026-0518.",
        "Incident INC-2026-0912 en reparatie REP-2026-4410 staan in het dossier.",
        "Claimreferentie CLM-2026-112233 hoort bij de letselschadeclaim.",
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


def _entity_candidates() -> list[str] | None:
    """Return known entity names when Dutch recognizer helpers are importable."""

    candidates: set[str] = set()
    try:
        from dutch_recognizers import get_dutch_entity_names, get_dutch_legal_entity_names
    except Exception:
        return None

    for callback in (
        lambda: get_dutch_entity_names(include_legal=True),
        get_dutch_legal_entity_names,
    ):
        try:
            candidates.update(str(name) for name in callback())
        except Exception:
            pass
    return sorted(candidates) or None


def _analyze_text(text: str) -> list[Any]:
    """Call the project analyzer without depending on Streamlit or app startup."""

    try:
        from presidio_helpers import analyze
    except Exception as exc:  # pragma: no cover - environment dependent
        pytest.skip(f"presidio_helpers unavailable: {exc}")

    entities = _entity_candidates()
    attempts = [
        {"text": text, "entities": entities, "language": "nl", "score_threshold": 0.0},
        {"text": text, "entities": entities, "language": "nl"},
        {"text": text, "entities": entities},
        {"text": text},
    ]
    for kwargs in attempts:
        clean_kwargs = {key: value for key, value in kwargs.items() if value is not None}
        try:
            results = analyze(**clean_kwargs)
        except TypeError:
            continue
        except Exception as exc:  # pragma: no cover - model/runtime dependent
            pytest.skip(f"analyzer unavailable in this environment: {exc}")
        return list(results or [])

    pytest.skip("No supported presidio_helpers.analyze call signature available")


def _result_to_row(text: str, result: Any) -> dict[str, Any]:
    if isinstance(result, dict):
        start = result.get("start")
        end = result.get("end")
        entity_type = result.get("entity_type", "")
        detected_text = result.get("text")
    else:
        start = getattr(result, "start", None)
        end = getattr(result, "end", None)
        entity_type = getattr(result, "entity_type", "")
        detected_text = getattr(result, "text", None)

    if detected_text is None and isinstance(start, int) and isinstance(end, int):
        detected_text = text[start:end]

    return {
        "text": str(detected_text or ""),
        "entity_type": str(entity_type or ""),
        "start": start,
        "end": end,
        "source": "analyzer",
    }


def _scan_candidate_rows(text: str, analyzer_results: list[Any]) -> list[dict[str, Any]]:
    try:
        from candidate_scanner import scan_unmasked_candidates
    except Exception:
        return []

    attempts = [
        lambda: scan_unmasked_candidates(text, analyzer_results=analyzer_results, max_candidates=100),
        lambda: scan_unmasked_candidates(text, analyzer_results=analyzer_results),
        lambda: scan_unmasked_candidates(text),
    ]
    for attempt in attempts:
        try:
            candidates = attempt()
        except TypeError:
            continue
        except Exception:
            return []
        rows: list[dict[str, Any]] = []
        for candidate in candidates or []:
            if isinstance(candidate, dict):
                rows.append(
                    {
                        "text": str(candidate.get("text", "")),
                        "entity_type": str(candidate.get("entity_type", "")),
                        "start": candidate.get("start"),
                        "end": candidate.get("end"),
                        "source": "candidate_scanner",
                    }
                )
        return rows
    return []


def _detected_rows(text: str) -> list[dict[str, Any]]:
    analyzer_results = _analyze_text(text)
    analyzer_rows = [_result_to_row(text, result) for result in analyzer_results]
    return analyzer_rows + _scan_candidate_rows(text, analyzer_results)


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


@pytest.mark.xfail(reason="Known recall gap: Dutch legal reference numbers are not consistently detected", strict=False)
def test_known_gap_legal_reference_numbers_should_be_detectable():
    rows = _detected_rows(LEGAL_REFERENCE_TEXT)

    missing = _missing_values(rows, LEGAL_REFERENCE_VALUES)

    assert missing == []


@pytest.mark.xfail(reason="Known misclassification gap: claim code can be classified as phone number", strict=False)
def test_known_gap_claim_reference_must_not_be_phone_number():
    rows = _detected_rows(LEGAL_REFERENCE_TEXT)

    claim_rows = [row for row in rows if _normalize("CLM-2026-112233") in _normalize(row["text"])]

    assert claim_rows, "CLM-2026-112233 should be detected as a legal/claim reference value"
    assert all("PHONE" not in row["entity_type"].upper() for row in claim_rows)


@pytest.mark.xfail(reason="Known recall gap: client, dossier and zaak numbers are not consistently detected", strict=False)
def test_known_gap_client_dossier_and_zaak_numbers_should_be_detectable():
    rows = _detected_rows(CLIENT_DOSSIER_TEXT)

    missing = _missing_values(rows, CLIENT_DOSSIER_VALUES)

    assert missing == []


@pytest.mark.xfail(reason="Known recall gap: rolnummer and Rechtspraak-like zaak codes are not consistently detected", strict=False)
def test_known_gap_rechtspraak_like_rolnummers_should_be_detectable():
    rows = _detected_rows(LEGAL_REFERENCE_TEXT)

    missing = _missing_values(rows, ["10598721 / UE VERZ 26-441", "ARN 26/4412"])

    assert missing == []


@pytest.mark.xfail(reason="Known precision gap: generic legal role words may be over-masked", strict=False)
def test_known_gap_role_words_alone_should_not_be_detected_as_person_values():
    rows = _detected_rows(ROLE_ONLY_TEXT)

    detected_person_values = {
        _normalize(row["text"])
        for row in rows
        if "PERSON" in row["entity_type"].upper() or "PERSOON" in row["entity_type"].upper()
    }

    assert detected_person_values.isdisjoint({_normalize(role) for role in ROLE_WORDS})


@pytest.mark.xfail(reason="Known over-masking risk: legal role structure must remain readable", strict=False)
def test_known_gap_overmasking_should_not_remove_legal_role_structure():
    rows = [row for row in _detected_rows(OVERMASKING_TEXT) if row["source"] == "analyzer"]
    masked_text = _mask_analyzer_spans(OVERMASKING_TEXT, rows).lower()

    for role in ["minderjarige", "arts", "getuige", "slachtoffer"]:
        assert role in masked_text
    assert masked_text.count("[mask]") < 4
