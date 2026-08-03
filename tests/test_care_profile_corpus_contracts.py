from care_profile_policy import ACTION_REPLACE, ACTION_REVIEW_SELECTED, policy_for_entity
from care_test_examples import TEST_CASES, all_expected_values, get_case


REQUIRED_DOCUMENT_TYPES = {
    "dagrapportage",
    "zorgplan_evaluatie",
    "verpleegkundige_overdracht",
    "ontslagbrief",
    "verwijsbrief",
    "medicatieoverzicht",
    "laboratoriumrapport",
    "mic_mim_vim_rapport",
}


def test_care_corpus_contains_eight_stable_document_families():
    assert len(TEST_CASES) == 8
    assert {case["document_type"] for case in TEST_CASES} == REQUIRED_DOCUMENT_TYPES
    assert len({case["id"] for case in TEST_CASES}) == len(TEST_CASES)


def test_every_expected_identifier_occurs_exactly_in_its_synthetic_text():
    for case in TEST_CASES:
        text = case["text"]
        for value in all_expected_values(case):
            assert value in text, f"{case['id']}: expected value not present: {value}"


def test_every_preserve_phrase_and_ambiguity_trap_occurs_in_text():
    for case in TEST_CASES:
        text = case["text"]
        assert case["preserve"], f"{case['id']}: preserve list must not be empty"
        for phrase in case["preserve"]:
            assert phrase in text, f"{case['id']}: preserve phrase not present: {phrase}"
        for trap in case["ambiguity_traps"]:
            assert trap in text, f"{case['id']}: ambiguity trap not present: {trap}"


def test_corpus_buckets_match_the_frozen_policy():
    for case in TEST_CASES:
        for item in case["replace"]:
            rule = policy_for_entity(item["entity_type"])
            assert rule is not None, f"{case['id']}: missing policy for {item['entity_type']}"
            assert rule.action == ACTION_REPLACE
        for item in case["review_selected"]:
            rule = policy_for_entity(item["entity_type"])
            assert rule is not None, f"{case['id']}: missing policy for {item['entity_type']}"
            assert rule.action == ACTION_REVIEW_SELECTED


def test_corpus_uses_only_synthetic_email_domains():
    for case in TEST_CASES:
        for item in case["replace"]:
            if item["entity_type"] == "EMAIL_ADDRESS":
                assert item["value"].endswith(".invalid")


def test_clinical_meaning_is_represented_in_every_case():
    clinical_markers = (
        "medicatie",
        "diagnose",
        "bloeddruk",
        "allerg",
        "zorgdoel",
        "uitslag",
        "mobil",
        "observ",
        "incident",
        "behandeling",
    )
    for case in TEST_CASES:
        blob = " ".join(case["preserve"]).lower()
        assert any(marker in blob for marker in clinical_markers), case["id"]


def test_get_case_uses_stable_ids():
    case = get_case("care_laboratory_report_v1")
    assert case["document_type"] == "laboratoriumrapport"
