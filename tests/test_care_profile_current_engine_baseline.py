from care_profile_baseline import build_current_care_baseline


def test_current_care_baseline_is_complete_evidence_not_a_readiness_claim():
    report = build_current_care_baseline()

    assert report["schema_version"] == "1.0"
    assert report["synthetic_data_only"] is True
    assert report["production_ready"] is False
    assert report["human_review_required"] is True
    assert report["case_count"] == 8
    assert len(report["cases"]) == 8
    assert report["expected_value_count"] >= report["found_value_count"] >= 0
    assert 0.0 <= report["indicative_recall"] <= 1.0
    assert report["preserve_overlap_count"] >= 0


def test_each_baseline_case_keeps_exact_expectation_evidence():
    report = build_current_care_baseline()

    for case in report["cases"]:
        assert case["expected_value_count"] == len(case["expectations"])
        assert case["found_value_count"] == sum(
            1 for expectation in case["expectations"] if expectation["found"]
        )
        for expectation in case["expectations"]:
            assert expectation["policy_bucket"] in {"replace", "review_selected"}
            assert expectation["value"]
            assert expectation["expected_entity_type"]
            assert isinstance(expectation["detected_entity_types"], list)
            assert isinstance(expectation["detected_spans"], list)


def test_baseline_scope_excludes_generic_ner_and_cloud_processing():
    report = build_current_care_baseline()

    assert "generic NER excluded" in report["scope"]
    assert report["profile"] == "current_custom_recognizers_before_care_profile"
