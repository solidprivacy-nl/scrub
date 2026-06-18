from __future__ import annotations

import json
from pathlib import Path

from person_name_recognizer_helper import find_contract_backed_person_name_matches


REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = REPO_ROOT / "tests" / "fixtures" / "person_name_recognizer_contract_cases.json"
ACCEPTED_PERSON_ENTITY_TYPES = {"PERSON", "NL_LEGAL_PARTY_NAME"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_contract_fixture() -> dict:
    return json.loads(read_text(FIXTURE_PATH))


def hard_matches(text: str):
    return find_contract_backed_person_name_matches(text)


def matched_values(text: str) -> set[str]:
    return {match.text for match in hard_matches(text)}


def test_positive_contract_cases_are_recognized_value_only():
    fixture = load_contract_fixture()

    for case in fixture["positive_cases"]:
        matches = hard_matches(case["text"])
        values = {match.text for match in matches}
        expected = case["expected_sensitive_value"]

        assert expected in values, f"{case['case_id']} should recognize {expected!r}; got {sorted(values)}"
        matched = next(match for match in matches if match.text == expected)
        assert case["text"][matched.start : matched.end] == expected
        assert matched.entity_type in ACCEPTED_PERSON_ENTITY_TYPES

        for preserve_term in case.get("preserve_terms", []):
            assert preserve_term not in matched.text, (
                f"{case['case_id']} included preserve term {preserve_term!r} in value-only span {matched.text!r}"
            )


def test_negative_contract_cases_do_not_match_as_person_names():
    fixture = load_contract_fixture()

    for case in fixture["negative_cases"]:
        matches = hard_matches(case["text"])
        assert matches == [], f"{case['case_id']} must not produce PERSON-name matches, got {matches!r}"


def test_single_surname_policy_is_limited_to_strong_context():
    assert matched_values("Later noteerde arts Bakker dat de cliënt stabiel was.") == {"Bakker"}
    assert matched_values("Arts Jansen bevestigde dat de minderjarige stabiel was.") == {"Jansen"}
    assert matched_values("Bakker staat los in deze synthetische zin zonder rolcontext.") == set()
    assert matched_values("Jansen staat los in deze synthetische zin zonder rolcontext.") == set()


def test_candidate_only_contract_cases_are_not_hard_recognizer_matches():
    fixture = load_contract_fixture()

    for case in fixture["candidate_only_cases"]:
        values = matched_values(case["text"])
        assert case["expected_sensitive_value"] not in values, (
            f"{case['case_id']} is candidate-only and must not become a hard recognizer match"
        )
        for extra_value in case.get("additional_sensitive_values", []):
            assert extra_value not in values, (
                f"{case['case_id']} extra value {extra_value!r} is candidate-only and must not become a hard recognizer match"
            )


def test_role_context_terms_remain_outside_value_spans():
    examples = [
        "De cliënt Youssef Ait Ben kreeg aanvullende begeleiding.",
        "Verpleegkundige Sara El Idrissi sprak met de mantelzorger.",
        "Mantelzorger Fatima Zahra kreeg de planning per e-mail.",
        "mr. Lina de Vries bespreekt de zaak met de cliënt.",
        "Later noteerde de rechter dat getuige Fatima El Amrani aanwezig was.",
    ]
    preserve_terms = set(load_contract_fixture()["preserve_terms"])

    for text in examples:
        matches = hard_matches(text)
        assert matches, f"expected at least one value-only name match for {text!r}"
        for match in matches:
            assert all(term not in match.text for term in preserve_terms), (
                f"value-only span {match.text!r} must not include preserve/context terms"
            )
