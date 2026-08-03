from dataclasses import dataclass

from care_candidate_scanner import scan_unmasked_care_candidates


@dataclass
class Result:
    start: int
    end: int


def test_care_candidate_scanner_surfaces_only_strongly_labelled_unresolved_codes():
    text = (
        "Patiëntnummer: PAT.2026.1148.\n"
        "Monsternummer: LAB 2026 4412.\n"
        "De bloeddruk is 123/78 mmHg en metformine 500 mg is toegediend."
    )

    candidates = scan_unmasked_care_candidates(text)

    assert [(item["entity_type"], item["text"]) for item in candidates] == [
        ("NL_PATIENT_NUMBER", "PAT.2026.1148"),
        ("NL_LAB_SAMPLE_NUMBER", "LAB 2026 4412"),
    ]
    assert all("zorglabel" in item["reason"] for item in candidates)
    assert all(item["context"] for item in candidates)


def test_care_candidate_scanner_excludes_already_detected_spans():
    text = "Patiëntnummer: PAT.2026.1148."
    start = text.index("PAT.2026.1148")
    end = start + len("PAT.2026.1148")

    assert scan_unmasked_care_candidates(text, [Result(start, end)]) == []
    assert scan_unmasked_care_candidates(
        text,
        [{"start": start, "end": end}],
    ) == []


def test_care_candidate_scanner_rejects_dates_times_and_clinical_codes():
    text = (
        "Patiëntnummer: 14-02-1948.\n"
        "Incidentnummer: 20:15.\n"
        "Behandelnummer: DBC-2026-7711.\n"
        "Diagnosecode ICD-10 E11.9.\n"
        "Glucose: 4,4 mmol/L."
    )

    assert scan_unmasked_care_candidates(text) == []


def test_care_candidate_scanner_does_not_scan_free_clinical_text():
    text = (
        "Metformine 500 mg tweemaal daags. Bloeddruk 123/78 mmHg. "
        "Pijnscore 6. Controle over zes weken."
    )

    assert scan_unmasked_care_candidates(text) == []


def test_care_candidate_scanner_respects_limit_and_deduplicates():
    text = (
        "Patiëntnummer: PAT.2026.1148.\n"
        "Patiëntnr: PAT.2026.1148.\n"
        "Cliëntnummer: CL.ZORG.7712."
    )

    candidates = scan_unmasked_care_candidates(text, max_candidates=2)
    assert len(candidates) == 2
    assert candidates[0]["text"] == "PAT.2026.1148"
