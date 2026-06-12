import json
from pathlib import Path

from placeholder_audit import audit_placeholders
from placeholder_validation import compute_integrity_token
from scrub_key import build_scrub_key
from scrub_key_reinsert import reinsert_from_scrub_key


FIXTURE_PATH = Path(__file__).parent / "fixtures" / "placeholder_corruption" / "ai_output_corruption_cases.json"

SYNTHETIC_ROWS = [
    {
        "original_value": "SYNTHETIC-PERSON-A",
        "placeholder": "[PERSOON_1]",
        "entity_type": "PERSON",
        "type_label": "Naam",
        "source": "synthetic",
        "review_status": "confirmed",
        "include": True,
        "timestamp": "2026-06-12T12:00:00Z",
    },
    {
        "original_value": "SYNTHETIC-PERSON-B",
        "placeholder": "[PERSOON_2]",
        "entity_type": "PERSON",
        "type_label": "Naam",
        "source": "synthetic",
        "review_status": "confirmed",
        "include": True,
        "timestamp": "2026-06-12T12:01:00Z",
    },
    {
        "original_value": "SYNTHETIC-CASE-001",
        "placeholder": "[ZAAKNUMMER_1]",
        "entity_type": "CASE_NUMBER",
        "type_label": "Zaaknummer",
        "source": "synthetic",
        "review_status": "confirmed",
        "include": True,
        "timestamp": "2026-06-12T12:02:00Z",
    },
]


def _load_fixture():
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def _legacy_expected():
    return _load_fixture()["expected_legacy_placeholders"]


def _case(case_id):
    for item in _load_fixture()["cases"]:
        if item["id"] == case_id:
            return item
    raise AssertionError(f"missing fixture case: {case_id}")


def _audit(case_id, expected=None):
    item = _case(case_id)
    return audit_placeholders(item["ai_output"], expected_placeholders=expected or _legacy_expected())


def _issue_names(audit):
    return {
        issue
        for entry in audit["placeholder_validation_issues"]
        for issue in entry.get("issues", [])
    }


def test_fixture_uses_only_synthetic_expected_values():
    fixture = _load_fixture()
    assert "No real personal data" in fixture["description"]
    scrub_key = build_scrub_key(SYNTHETIC_ROWS, document_label="WP34 synthetic corruption")
    assert all(item["original_value"].startswith("SYNTHETIC-") for item in scrub_key["items"])


def test_exact_legacy_output_still_reinserts_and_has_clean_audit():
    item = _case("legacy_exact_preserved_with_punctuation")
    scrub_key = build_scrub_key(SYNTHETIC_ROWS, document_label="WP34 synthetic corruption")

    reinserted = reinsert_from_scrub_key(item["ai_output"], scrub_key)
    audit = audit_placeholders(item["ai_output"], expected_placeholders=_legacy_expected())

    assert reinserted["replacement_count"] == 3
    assert reinserted["unknown_placeholders"] == []
    assert reinserted["placeholders_not_found"] == []
    assert audit["missing_placeholders"] == []
    assert audit["unknown_placeholder_like_tokens"] == []
    assert audit["legacy_placeholders"] == item["expected"]["legacy_placeholders"]


def test_translation_corruption_reports_unknown_and_missing():
    audit = _audit("translated_legacy_label")
    expected = _case("translated_legacy_label")["expected"]

    assert audit["missing_placeholders"] == expected["missing_placeholders"]
    assert audit["unknown_placeholder_like_tokens"] == expected["unknown_placeholder_like_tokens"]
    assert audit["legacy_placeholders"] == expected["legacy_placeholders"]


def test_summarization_deletion_reports_all_expected_placeholders_missing():
    audit = _audit("summary_deleted_placeholders")
    expected = _case("summary_deleted_placeholders")["expected"]

    assert audit["observed_placeholder_like_tokens"] == expected["observed_placeholder_like_tokens"]
    assert audit["missing_placeholders"] == expected["missing_placeholders"]
    assert audit["unknown_placeholder_like_tokens"] == expected["unknown_placeholder_like_tokens"]


def test_markdown_and_html_wrapping_preserves_exact_tokens():
    audit = _audit("markdown_html_exact_wrapping")
    expected = _case("markdown_html_exact_wrapping")["expected"]

    assert audit["legacy_placeholders"] == expected["legacy_placeholders"]
    assert audit["missing_placeholders"] == expected["missing_placeholders"]
    assert audit["unknown_placeholder_like_tokens"] == expected["unknown_placeholder_like_tokens"]


def test_html_split_placeholder_is_not_repaired_and_is_reported_missing():
    audit = _audit("html_split_placeholder")
    expected = _case("html_split_placeholder")["expected"]

    assert audit["legacy_placeholders"] == expected["legacy_placeholders"]
    assert audit["missing_placeholders"] == expected["missing_placeholders"]
    assert "[PERSOON_1]" not in audit["observed_placeholder_like_tokens"]


def test_spacing_mutation_is_not_repaired_and_is_reported_missing():
    audit = _audit("spacing_changed_placeholder")
    expected = _case("spacing_changed_placeholder")["expected"]

    assert audit["legacy_placeholders"] == expected["legacy_placeholders"]
    assert audit["missing_placeholders"] == expected["missing_placeholders"]
    assert "[ PERSOON_1 ]" not in audit["observed_placeholder_like_tokens"]


def test_truncated_robust_placeholder_reports_malformed_and_missing_expected():
    item = _case("truncated_robust_placeholder")
    audit = audit_placeholders(item["ai_output"], expected_placeholders=item["expected_robust"])

    assert audit["missing_placeholders"] == item["expected"]["missing_placeholders"]
    assert audit["malformed_robust_placeholders"] == item["expected"]["malformed_robust_placeholders"]
    assert item["expected"]["placeholder_issue_contains"] in _issue_names(audit)


def test_integrity_failed_robust_placeholder_reports_checksum_problem():
    item = _case("robust_integrity_mismatch")
    audit = audit_placeholders(item["ai_output"], expected_placeholders=item["expected_robust"])

    assert item["expected_robust"] == [f"[[SP_PERSON_0001_{compute_integrity_token('PERSON', '0001')}]]"]
    assert audit["missing_placeholders"] == item["expected"]["missing_placeholders"]
    assert audit["integrity_failed_placeholders"] == item["expected"]["integrity_failed_placeholders"]
    assert item["expected"]["placeholder_issue_contains"] in _issue_names(audit)


def test_placeholder_merge_reports_deleted_second_placeholder_missing():
    audit = _audit("merged_placeholders")
    expected = _case("merged_placeholders")["expected"]

    assert audit["missing_placeholders"] == expected["missing_placeholders"]
    assert audit["legacy_placeholders"] == expected["legacy_placeholders"]
    assert audit["placeholder_format_summary"]["missing_expected_count"] == 1


def test_invented_curly_placeholder_is_reported_without_repair():
    audit = _audit("invented_curly_placeholder")
    expected = _case("invented_curly_placeholder")["expected"]

    assert audit["missing_placeholders"] == expected["missing_placeholders"]
    assert audit["unknown_placeholder_like_tokens"] == expected["unknown_placeholder_like_tokens"]
    assert "unknown_placeholder_like" in {
        entry["kind"] for entry in audit["placeholder_validation_issues"]
    }
