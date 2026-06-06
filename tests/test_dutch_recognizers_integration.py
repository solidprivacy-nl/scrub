from dutch_recognizers import get_dutch_recognizers, get_dutch_entity_names
from test_cases.legal_regression_cases import EXPECTED_CANDIDATE_TYPES


INTEGRATION_TEXT = """
Zaaknummer: 10598721 / UE VERZ 26-441.
De wederpartij verwees naar intern incidentnummer INC-2026-0912.
In het dossier wordt daarnaast verwezen naar camerabeeld met referentie CAM-MAAS-2026-0518.
Claimreferentie verzekeraar: CLM-2026-112233.
De verhuurder heeft de melding geregistreerd onder reparatienummer REP-2026-4410.
Afdeling bestuursrecht
Zaaknummer: ARN 26/4412
Afdeling vreemdelingenzaken
Zaaknummer: NL26.12345
De gemeente gebruikt zaaknummer GEM-HLM-2026-2210.
Zaaknummer: 200.345.678/01 OK
KvK-nummer vennootschap: 76543210
"""


def _run_lightweight_recognizers(text: str):
    entities = get_dutch_entity_names(include_legal=True)
    results = []
    for recognizer in get_dutch_recognizers(supported_language="en"):
        if hasattr(recognizer, "load"):
            recognizer.load()
        results.extend(recognizer.analyze(text, entities=entities, nlp_artifacts=None))
    return results


def _value_map(results, text: str):
    mapped = {}
    for result in results:
        value = text[result.start : result.end]
        mapped.setdefault(value, set()).add(result.entity_type)
    return mapped


def test_dutch_recognizers_detect_v11_1_legal_reference_values():
    results = _run_lightweight_recognizers(INTEGRATION_TEXT)
    by_value = _value_map(results, INTEGRATION_TEXT)

    expected_values = {
        "10598721 / UE VERZ 26-441",
        "INC-2026-0912",
        "CAM-MAAS-2026-0518",
        "CLM-2026-112233",
        "REP-2026-4410",
        "ARN 26/4412",
        "NL26.12345",
        "GEM-HLM-2026-2210",
        "200.345.678/01 OK",
        "76543210",
    }

    missing = expected_values - set(by_value)
    assert not missing, f"Recognizer integration missed values: {sorted(missing)}"


def test_dutch_recognizers_assign_v11_1_reference_entity_types():
    results = _run_lightweight_recognizers(INTEGRATION_TEXT)
    by_value = _value_map(results, INTEGRATION_TEXT)

    expected_subset = {
        value: entity_type
        for value, entity_type in EXPECTED_CANDIDATE_TYPES.items()
        if value in INTEGRATION_TEXT and value != "XX123X" and value != "WR-KLANT-2026-7712" and value != "DOSS/2026/1189"
    }

    mismatches = {
        value: {"expected": expected_type, "actual": sorted(by_value.get(value, set()))}
        for value, expected_type in expected_subset.items()
        if expected_type not in by_value.get(value, set())
    }
    assert not mismatches, f"Recognizer integration type mismatches: {mismatches}"


def test_dutch_recognizers_return_value_only_not_context_label():
    results = _run_lightweight_recognizers(INTEGRATION_TEXT)
    values = {INTEGRATION_TEXT[result.start : result.end] for result in results}

    assert "Zaaknummer: 10598721 / UE VERZ 26-441" not in values
    assert "intern incidentnummer INC-2026-0912" not in values
    assert "Claimreferentie verzekeraar: CLM-2026-112233" not in values
    assert "KvK-nummer vennootschap: 76543210" not in values
