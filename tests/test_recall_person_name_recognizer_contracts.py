from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = REPO_ROOT / "tests" / "fixtures" / "person_name_recognizer_contract_cases.json"

REQUIRED_GROUPS = ["positive_cases", "candidate_only_cases", "negative_cases", "preserve_terms"]

REQUIRED_PRESERVE_TERMS = {
    "cliënt",
    "slachtoffer",
    "minderjarige",
    "arts",
    "getuige",
    "eiser",
    "verweerder",
    "verpleegkundige",
    "zorgmedewerker",
    "behandelaar",
    "mantelzorger",
    "mr.",
}

DISALLOWED_CLAIMS = [
    "Alle persoonsnamen worden altijd gevonden.",
    "Alle persoonsgegevens worden altijd gevonden.",
    "De app is veilig zonder menselijke review.",
    "De benchmark bewijst production readiness.",
]

NON_CLAIM_CUES = [
    "disallowed",
    "disallowed claims",
    "disallowed wording",
    "product-claim boundary",
    "product-claim policy",
    "verboden",
    "niet gezegd",
]

DOCUMENTATION_FILES = [
    REPO_ROOT / "PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md",
    REPO_ROOT / "RECALL_PERSON_NAME_RECOGNIZER_PLAN.md",
    REPO_ROOT / "RECALL_PRECISION_SCORECARD.md",
    REPO_ROOT / "CHANGELOG.md",
    REPO_ROOT / "RISK_REGISTER.md",
    REPO_ROOT / "DECISION_LOG.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_contract_fixture() -> dict:
    return json.loads(read_text(FIXTURE_PATH))


def all_cases(fixture: dict) -> list[dict]:
    return [*fixture["positive_cases"], *fixture["candidate_only_cases"], *fixture["negative_cases"]]


def test_contract_fixture_metadata_is_non_enforcing():
    metadata = load_contract_fixture()["metadata"]

    assert metadata["status"] == "contract_only"
    assert metadata["synthetic"] is True
    assert metadata["product_gate"] is False
    assert metadata["thresholds_enforced"] is False
    assert metadata["product_claim"] is False


def test_required_contract_groups_exist_and_are_non_empty():
    fixture = load_contract_fixture()

    for group in REQUIRED_GROUPS:
        assert group in fixture, f"Missing contract group: {group}"
        assert fixture[group], f"Contract group must not be empty: {group}"


def test_positive_cases_are_value_only_future_contracts():
    fixture = load_contract_fixture()

    for case in fixture["positive_cases"]:
        expected = case["expected_sensitive_value"]
        assert expected in case["text"], case["case_id"]
        assert expected != case["text"], case["case_id"]
        assert case["mode"] == "hard_recognizer_future", case["case_id"]
        assert case["expected_entity_type"] in {"PERSON", "NL_LEGAL_PARTY_NAME"}, case["case_id"]

        for preserve_term in case.get("preserve_terms", []):
            assert preserve_term not in expected, (
                f"{case['case_id']} should keep preserve term {preserve_term!r} outside expected sensitive value {expected!r}"
            )


def test_candidate_only_cases_require_review_and_forbid_automatic_replacement():
    fixture = load_contract_fixture()

    for case in fixture["candidate_only_cases"]:
        expected = case["expected_sensitive_value"]
        assert case["mode"] == "candidate_only_future", case["case_id"]
        assert case["review_required"] is True, case["case_id"]
        assert case["automatic_replacement_allowed"] is False, case["case_id"]
        assert expected in case["text"], case["case_id"]
        for extra_value in case.get("additional_sensitive_values", []):
            assert extra_value in case["text"], case["case_id"]


def test_negative_cases_do_not_claim_person_matches():
    fixture = load_contract_fixture()

    for case in fixture["negative_cases"]:
        assert case["mode"] == "must_not_match_person", case["case_id"]
        assert case["expected_sensitive_value"] is None, case["case_id"]


def test_single_surname_policy_cases_are_explicit():
    fixture = load_contract_fixture()
    cases = all_cases(fixture)

    strong_context = {
        case.get("expected_sensitive_value")
        for case in cases
        if case.get("strong_context") is True and case.get("expected_sensitive_value") in {"Bakker", "Jansen"}
    }
    without_context = {
        case.get("single_surname")
        for case in cases
        if case.get("strong_context") is False and case.get("mode") == "must_not_match_person"
    }

    assert {"Bakker", "Jansen"}.issubset(strong_context)
    assert {"Bakker", "Jansen"}.issubset(without_context)

    for case in cases:
        if case.get("single_surname") in {"Bakker", "Jansen"} and case.get("strong_context") is False:
            assert case["mode"] == "must_not_match_person", case["case_id"]
        if case.get("expected_sensitive_value") in {"Bakker", "Jansen"} and case.get("strong_context") is True:
            assert case["mode"] in {"hard_recognizer_future", "candidate_only_future"}, case["case_id"]


def test_required_preserve_terms_are_declared():
    fixture = load_contract_fixture()
    declared = set(fixture["preserve_terms"])

    assert REQUIRED_PRESERVE_TERMS.issubset(declared)


def test_disallowed_product_claims_only_appear_as_non_claim_boundaries():
    for path in DOCUMENTATION_FILES:
        text = read_text(path)
        lowered = text.lower()
        for claim in DISALLOWED_CLAIMS:
            start = 0
            while True:
                index = text.find(claim, start)
                if index == -1:
                    break
                before = lowered[max(0, index - 350) : index]
                assert any(cue in before for cue in NON_CLAIM_CUES), (
                    f"{path} contains disallowed product claim {claim!r} outside an explicit non-claim/disallowed section"
                )
                start = index + len(claim)


def test_contracts_do_not_introduce_enforcement_or_gate():
    fixture = load_contract_fixture()
    contract_doc = read_text(REPO_ROOT / "PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md").lower()
    scorecard = read_text(REPO_ROOT / "RECALL_PRECISION_SCORECARD.md").lower()

    assert fixture["metadata"]["status"] == "contract_only"
    assert fixture["metadata"]["thresholds_enforced"] is False
    assert fixture["metadata"]["product_gate"] is False
    assert fixture["metadata"]["product_claim"] is False

    combined_text = f"{contract_doc}\n{scorecard}"
    assert "contract_only" in combined_text
    assert "no threshold enforcement" in combined_text
    assert "no production gate" in combined_text
    assert "no product claim" in combined_text
