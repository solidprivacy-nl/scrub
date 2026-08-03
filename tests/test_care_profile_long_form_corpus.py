from copy import deepcopy

from care_test_example_expansions import LONG_FORM_EXPANSIONS, expand_case_texts
from care_test_examples import TEST_CASES, all_expected_values
from profile_ui_support import care_example_names, care_example_text


EXPECTED_CASE_IDS = {
    "care_daily_nursing_report_v1",
    "care_plan_evaluation_v1",
    "care_nursing_transfer_v1",
    "care_discharge_letter_v1",
    "care_gp_referral_v1",
    "care_medication_overview_v1",
    "care_laboratory_report_v1",
    "care_incident_report_v1",
}


def _headings(text: str) -> list[str]:
    return [
        line.strip()
        for line in text.splitlines()
        if line.strip()
        and any(character.isalpha() for character in line)
        and line.strip() == line.strip().upper()
    ]


def test_long_form_expansions_cover_exactly_the_stable_care_cases():
    assert set(LONG_FORM_EXPANSIONS) == EXPECTED_CASE_IDS
    assert {str(case["id"]) for case in TEST_CASES} == EXPECTED_CASE_IDS


def test_long_form_expansions_add_no_new_obvious_identifying_values():
    forbidden_markers = (
        "nummer:",
        "geboortedatum",
        "woonadres",
        "telefoon",
        "e-mail",
        "@",
        ".invalid",
    )

    for case_id, addition in LONG_FORM_EXPANSIONS.items():
        lowered = addition.lower()
        assert len(addition.split()) >= 200, case_id
        assert not any(character.isdigit() for character in addition), case_id
        assert not any(marker in lowered for marker in forbidden_markers), case_id
        assert len(_headings(addition)) == 5, case_id


def test_expansion_helper_copies_cases_and_preserves_contract_metadata():
    source = [
        {
            "id": case_id,
            "text": f"KORTE BRONTEKST VOOR {case_id}",
            "replace": [{"value": "synthetic", "entity_type": "PERSON"}],
            "review_selected": [],
            "preserve": ["context"],
            "audit_only": [],
            "ambiguity_traps": [],
        }
        for case_id in sorted(EXPECTED_CASE_IDS)
    ]
    original = deepcopy(source)

    expanded = expand_case_texts(source)

    assert source == original
    assert expanded is not source
    assert len(expanded) == len(source)

    for source_case, expanded_case in zip(source, expanded):
        assert expanded_case is not source_case
        assert expanded_case["replace"] == source_case["replace"]
        assert expanded_case["replace"] is not source_case["replace"]
        assert expanded_case["text"].startswith(f"{source_case['text']}\n\n")
        assert expanded_case["text"].endswith("\n")


def test_all_visible_care_examples_are_long_form_and_structured():
    assert len(TEST_CASES) == 8

    for case in TEST_CASES:
        case_id = str(case["id"])
        text = str(case["text"])
        addition = LONG_FORM_EXPANSIONS[case_id]

        assert len(text.split()) >= 250, case_id
        assert len(_headings(text)) >= 6, case_id
        assert addition in text, case_id

        for value in all_expected_values(case):
            assert value in text, f"{case_id}: expected value missing: {value!r}"
            assert value not in addition, (
                f"{case_id}: expansion must not duplicate existing expected value {value!r}"
            )
        for phrase in case["preserve"]:
            assert phrase in text, f"{case_id}: preserve phrase missing: {phrase!r}"


def test_ui_adapter_exposes_the_same_long_form_examples():
    names = care_example_names()

    assert len(names) == 8
    for case in TEST_CASES:
        name = str(case["name"])
        assert name in names
        assert care_example_text(name) == case["text"]
        assert len(care_example_text(name).split()) >= 250
