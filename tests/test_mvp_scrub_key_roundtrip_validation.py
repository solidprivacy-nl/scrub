from __future__ import annotations

import ast
from copy import deepcopy
from pathlib import Path

from mvp_scrub_key_roundtrip_validation import (
    CANONICAL_ROWS,
    build_canonical_scrub_key,
    build_variant_scrub_key,
    evaluate_roundtrip_case,
    load_roundtrip_manifest,
    run_roundtrip_validation,
)


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "mvp_scrub_key_roundtrip_validation.py"
THIS_TEST = ROOT / "tests/test_mvp_scrub_key_roundtrip_validation.py"


def test_manifest_is_versioned_synthetic_and_has_unique_cases() -> None:
    manifest = load_roundtrip_manifest()
    case_ids = [case["id"] for case in manifest["cases"]]

    assert manifest["schema"] == "solidprivacy.mvp_scrub_key_roundtrip_manifest"
    assert manifest["schema_version"] == "1.0"
    assert manifest["synthetic_only"] is True
    assert len(case_ids) == 15
    assert len(case_ids) == len(set(case_ids))


def test_every_manifest_case_matches_existing_helper_behavior() -> None:
    manifest = load_roundtrip_manifest()
    results = [evaluate_roundtrip_case(case) for case in manifest["cases"]]

    assert all(result["matches_expected"] for result in results)
    assert all(result["local_only"] for result in results)
    assert not any(result["ai_processing"] for result in results)
    assert not any(result["cloud_processing"] for result in results)


def test_intact_and_repeated_placeholder_roundtrips_are_deterministic() -> None:
    manifest = load_roundtrip_manifest()
    by_id = {case["id"]: case for case in manifest["cases"]}

    intact_first = evaluate_roundtrip_case(by_id["intact_roundtrip"])
    intact_second = evaluate_roundtrip_case(by_id["intact_roundtrip"])
    repeated = evaluate_roundtrip_case(by_id["repeated_placeholder_occurrences"])

    assert intact_first == intact_second
    assert intact_first["actual"]["replacement_count"] == 2
    assert intact_first["actual"]["unknown_placeholders"] == []
    assert repeated["actual"]["replacement_count"] == 2
    assert repeated["actual"]["placeholders_not_found"] == ["[DOSSIER_1]"]


def test_unknown_translated_and_merged_placeholders_remain_visible() -> None:
    manifest = load_roundtrip_manifest()
    by_id = {case["id"]: case for case in manifest["cases"]}

    unknown = evaluate_roundtrip_case(by_id["unknown_placeholder_injected"])
    translated = evaluate_roundtrip_case(by_id["translated_placeholders"])
    merged = evaluate_roundtrip_case(by_id["merged_placeholder_token"])

    assert unknown["actual"]["unknown_placeholders"] == ["[ONBEKEND_1]"]
    assert translated["actual"]["unknown_placeholders"] == ["[CASE_1]", "[PERSON_1]"]
    assert merged["actual"]["unknown_placeholders"] == ["[PERSOON_DOSSIER_1]"]
    assert translated["actual"]["replacement_count"] == 0
    assert merged["actual"]["replacement_count"] == 0


def test_malformed_placeholder_changes_are_signalled_indirectly() -> None:
    manifest = load_roundtrip_manifest()
    by_id = {case["id"]: case for case in manifest["cases"]}

    for case_id in ["malformed_missing_bracket", "underscore_removed", "lowercase_placeholder"]:
        result = evaluate_roundtrip_case(by_id[case_id])
        assert result["expected_safety_class"] == "indirect_corruption_signal"
        assert result["actual"]["unknown_placeholders"] == []
        assert result["actual"]["placeholders_not_found"] == ["[PERSOON_1]"]
        assert result["actual"]["replacement_count"] == 1


def test_duplicate_incomplete_and_invalid_keys_fail_visibly() -> None:
    manifest = load_roundtrip_manifest()
    by_id = {case["id"]: case for case in manifest["cases"]}

    duplicate = evaluate_roundtrip_case(by_id["duplicate_placeholder_in_key"])
    incomplete = evaluate_roundtrip_case(by_id["incomplete_key"])
    invalid = evaluate_roundtrip_case(by_id["tampered_item_count"])

    assert duplicate["actual"]["duplicate_placeholders"] == ["[PERSOON_1]"]
    assert "[PERSOON_1]" in duplicate["actual"]["text"]
    assert incomplete["actual"]["unknown_placeholders"] == ["[DOSSIER_1]"]
    assert invalid["actual"]["has_validation_issue"] is True
    assert invalid["actual"]["replacement_count"] == 0


def test_disjoint_wrong_key_is_visible_but_same_namespace_wrong_key_is_not() -> None:
    manifest = load_roundtrip_manifest()
    by_id = {case["id"]: case for case in manifest["cases"]}

    disjoint = evaluate_roundtrip_case(by_id["wrong_key_disjoint_namespace"])
    same_namespace = evaluate_roundtrip_case(by_id["wrong_key_same_placeholder_namespace"])

    assert disjoint["actual"]["replacement_count"] == 0
    assert disjoint["actual"]["unknown_placeholders"] == ["[DOSSIER_1]", "[PERSOON_1]"]
    assert same_namespace["actual"]["replacement_count"] == 2
    assert same_namespace["actual"]["unknown_placeholders"] == []
    assert same_namespace["actual"]["placeholders_not_found"] == []
    assert same_namespace["actual"]["has_validation_issue"] is False
    assert same_namespace["actual"]["text"] == "VERKEERDE-PERSOON / VERKEERD-DOSSIER"


def test_report_records_critical_document_binding_gap_and_indirect_diagnostic_limit() -> None:
    report = run_roundtrip_validation()
    findings = {finding["id"]: finding for finding in report["findings"]}

    assert report["validation_complete"] is True
    assert report["failed_case_count"] == 0
    assert report["case_count"] == 15
    assert report["critical_finding_count"] == 1
    assert report["medium_finding_count"] == 1
    assert findings["scrub_key_document_binding_missing"]["severity"] == "critical"
    assert findings["scrub_key_document_binding_missing"]["risk"] == "R2"
    assert findings["scrub_key_document_binding_missing"]["requires_separate_triage"] is True
    assert findings["malformed_placeholder_detection_is_indirect"]["risk"] == "R3"
    assert report["next_workpackage"] == "SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE"
    assert report["production_ready"] is False
    assert report["human_review_required"] is True
    assert report["product_code_changed"] is False


def test_report_is_deterministic_and_local_only() -> None:
    first = run_roundtrip_validation()
    second = run_roundtrip_validation()

    assert first == second
    assert first["synthetic_only"] is True
    assert first["local_only"] is True
    assert first["external_ai_used"] is False
    assert first["cloud_processing_used"] is False


def test_key_variants_do_not_mutate_canonical_rows_or_key() -> None:
    rows_before = deepcopy(CANONICAL_ROWS)
    canonical_before = build_canonical_scrub_key()

    for variant in [
        "canonical",
        "duplicate_person_placeholder",
        "person_only",
        "tampered_item_count",
        "disjoint_wrong_key",
        "same_placeholders_wrong_originals",
        "same_original_distinct_placeholders",
    ]:
        build_variant_scrub_key(variant)

    assert CANONICAL_ROWS == rows_before
    assert build_canonical_scrub_key() == canonical_before


def test_validation_module_and_test_do_not_import_streamlit_or_network_clients() -> None:
    imported_roots: set[str] = set()
    for path in [MODULE, THIS_TEST]:
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".")[0])

    assert "streamlit" not in imported_roots
    assert "requests" not in imported_roots
    assert "httpx" not in imported_roots
    assert "openai" not in imported_roots
    assert "anthropic" not in imported_roots


def test_examples_are_synthetic_only() -> None:
    report_text = str(run_roundtrip_validation())

    assert "BETROKKENE-TEST-A" in report_text
    assert "DOSSIER-TEST-2026-001" in report_text
    assert "Jan Jansen" not in report_text
    assert "Piet de Vries" not in report_text
    assert "123456782" not in report_text
