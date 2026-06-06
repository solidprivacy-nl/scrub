from candidate_scanner import scan_unmasked_candidates
from test_cases.legal_regression_cases import (
    CANDIDATE_SCANNER_TEXT,
    EXPECTED_CANDIDATES,
    NEGATIVE_VALUES,
)


def test_candidate_scanner_finds_expected_reference_like_values():
    rows = scan_unmasked_candidates(CANDIDATE_SCANNER_TEXT, analyzer_results=[])
    found = {row["text"] for row in rows}

    missing = EXPECTED_CANDIDATES - found
    assert not missing, f"Expected candidates were not found: {sorted(missing)}"


def test_candidate_scanner_does_not_suggest_known_false_positives():
    rows = scan_unmasked_candidates(CANDIDATE_SCANNER_TEXT, analyzer_results=[])
    found = {row["text"] for row in rows}

    unexpected = NEGATIVE_VALUES & found
    assert not unexpected, f"False-positive values were suggested: {sorted(unexpected)}"


def test_candidate_scanner_preserves_context_by_returning_value_only():
    rows = scan_unmasked_candidates(CANDIDATE_SCANNER_TEXT, analyzer_results=[])
    found = {row["text"] for row in rows}

    assert "reparatienummer REP-2026-4410" not in found
    assert "intern incidentnummer INC-2026-0912" not in found
    assert "kenteken XX123X" not in found
    assert "REP-2026-4410" in found
    assert "INC-2026-0912" in found
    assert "XX123X" in found


def test_candidate_scanner_respects_existing_analyzer_spans():
    start = CANDIDATE_SCANNER_TEXT.index("REP-2026-4410")
    end = start + len("REP-2026-4410")

    class ExistingResult:
        pass

    existing = ExistingResult()
    existing.start = start
    existing.end = end

    rows = scan_unmasked_candidates(CANDIDATE_SCANNER_TEXT, analyzer_results=[existing])
    found = {row["text"] for row in rows}

    assert "REP-2026-4410" not in found
