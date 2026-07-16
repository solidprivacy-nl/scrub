from __future__ import annotations

import ast
import json
from pathlib import Path

from mvp_phase6_validation_manifest import (
    load_validation_manifest,
    validate_validation_manifest,
)
from mvp_phase6_validation_report import (
    build_validation_report,
    write_validation_report,
)


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "test_cases" / "mvp_phase6" / "validation_manifest.json"
MODULE_PATHS = [
    ROOT / "mvp_phase6_validation_manifest.py",
    ROOT / "mvp_phase6_detection_matrix.py",
    ROOT / "mvp_phase6_workflow_core.py",
    ROOT / "mvp_phase6_document_cases.py",
    ROOT / "mvp_phase6_validation_report.py",
]


def _manifest() -> dict:
    return load_validation_manifest(MANIFEST_PATH)


def _report() -> dict:
    return build_validation_report(_manifest())


def _case(report: dict, case_id: str) -> dict:
    return next(item for item in report["cases"] if item["id"] == case_id)


def test_manifest_is_valid_versioned_and_synthetic_only() -> None:
    manifest = _manifest()

    assert validate_validation_manifest(manifest) == []
    assert manifest["schema"] == "solidprivacy.mvp_phase6_validation_matrix"
    assert manifest["schema_version"] == "1.0"
    assert manifest["synthetic_data_only"] is True
    assert manifest["human_review_required"] is True
    assert manifest["production_readiness_claim"] is False
    assert {case["document_type"] for case in manifest["cases"]} == {
        "txt",
        "docx",
        "pdf",
    }


def test_manifest_uses_only_explicit_synthetic_values() -> None:
    text = MANIFEST_PATH.read_text(encoding="utf-8")

    for marker in [
        "Testdam",
        "Testerveld",
        "example.invalid",
        "DOS-2026-778899",
        "ZK-WOON-55091",
        "CLNT-2026-0042",
        "lantaarnbloem",
    ]:
        assert marker in text

    for prohibited in ["Jan Jansen", "Piet de Vries", "example.com"]:
        assert prohibited not in text


def test_txt_case_exercises_manual_addition_scrub_key_exports_and_roundtrip() -> None:
    case = _case(_report(), "txt_legal_core_roundtrip")

    assert case["status"] == "pass"
    assert case["source_import_type"] == "txt"
    assert case["roundtrip_exact"] is True
    assert case["export_import_types"] == ["docx", "pdf"]
    assert case["export_placeholders_visible"] is True
    assert case["scrub_key_validation_issues"] == []
    assert case["scrub_report_requires_manual_review"] is True
    assert case["reinsert_replacement_count"] == case["scrub_key_item_count"]

    additions = {item["value"]: item for item in case["manual_additions"]}
    assert additions["Mila Testerveld"]["placeholder"] == "[PERSOON_HANDMATIG_01]"
    assert additions["lantaarnbloem"]["placeholder"] == "[WAARDE_HANDMATIG_01]"
    assert all(item["is_valid"] for item in additions.values())


def test_txt_detection_evidence_covers_expected_values_and_preserves_roles() -> None:
    case = _case(_report(), "txt_legal_core_roundtrip")
    detection = case["detection"]

    assert detection["detection_expectations_met"] is True
    assert detection["missing_expected_values"] == []
    assert detection["context_preservation_met"] is True
    assert detection["removed_preserved_terms"] == []
    assert detection["local_only"] is True
    assert detection["ai_processing"] is False
    assert detection["cloud_processing"] is False
    assert set(detection["expected_values"]) >= {
        "DOS-2026-778899",
        "ZK-WOON-55091",
        "CLNT-2026-0042",
        "mila.testerveld@example.invalid",
    }
    email_rows = [
        row
        for row in detection["rows"]
        if row["entity_type"] == "EMAIL_ADDRESS"
    ]
    assert any(
        row["text"] == "mila.testerveld@example.invalid"
        for row in email_rows
    )


def test_docx_case_records_hygiene_and_header_footer_reinsert_limits() -> None:
    case = _case(_report(), "docx_mixed_structure_roundtrip")

    assert case["status"] == "pass_with_known_limitations"
    assert case["source_import_type"] == "docx"
    assert case["scrubbed_import_type"] == "docx"
    assert case["restored_import_type"] == "docx"
    assert case["body_roundtrip_values_present"] is True
    assert case["hygiene_severity"] == "high"
    assert {"headers_detected", "footers_detected"}.issubset(
        set(case["hygiene_findings"])
    )
    assert case["audit_expectations_met"] is True
    assert case["limitation_expectations_met"] is True
    assert case["roundtrip_complete"] is False
    assert set(case["expected_residual_placeholders"]).issubset(
        set(case["residual_placeholders"])
    )


def test_pdf_case_preserves_text_roundtrip_and_explicit_txt_only_boundary() -> None:
    case = _case(_report(), "pdf_text_based_to_txt_reinsert")

    assert case["status"] == "pass_with_known_limitations"
    assert case["source_import_type"] == "pdf"
    assert case["scrubbed_import_type"] == "pdf"
    assert case["roundtrip_text_equal"] is True
    assert case["reinsert_output_type"] == "txt"
    assert case["restored_pdf_supported"] is False
    assert case["ocr_supported"] is False
    assert case["limitation_contract_met"] is True


def test_report_is_machine_readable_and_never_claims_production_readiness() -> None:
    report = _report()

    assert report["schema"] == "solidprivacy.mvp_phase6_validation_report"
    assert report["schema_version"] == "1.0"
    assert report["case_count"] == 3
    assert report["failing_case_count"] == 0
    assert report["failing_cases"] == []
    assert report["synthetic_data_only"] is True
    assert report["human_review_required"] is True
    assert report["production_ready"] is False
    assert report["production_readiness_claim"] is False
    assert report["local_only"] is True
    assert report["ai_processing"] is False
    assert report["cloud_processing"] is False
    assert report["ocr_processing"] is False
    assert report["next_recommended_package"] == (
        "SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE"
    )

    categories = {item["category"] for item in report["evidence_gaps"]}
    assert categories == {
        "known_docx_reinsert_limitation",
        "known_pdf_reinsert_limitation",
    }


def test_report_writer_is_deterministic(tmp_path: Path) -> None:
    output = tmp_path / "report.json"
    first = write_validation_report(_manifest(), output)
    first_text = output.read_text(encoding="utf-8")
    second = write_validation_report(_manifest(), output)

    assert first == second
    assert first_text == output.read_text(encoding="utf-8")
    assert json.loads(first_text) == first


def test_validation_modules_do_not_import_streamlit_or_external_ai_clients() -> None:
    imported_roots: set[str] = set()
    for path in MODULE_PATHS:
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".")[0])

    assert "streamlit" not in imported_roots
    assert "openai" not in imported_roots
    assert "requests" not in imported_roots
    assert "httpx" not in imported_roots
