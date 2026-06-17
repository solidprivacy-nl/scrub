from __future__ import annotations

import json

from recall_benchmark_report import (
    DIAGNOSTIC_METADATA,
    REPORT_JSON_FILENAME,
    REPORT_MARKDOWN_FILENAME,
    SUMMARY_FIELDS,
    build_diagnostic_report,
    main,
    render_markdown_summary,
    validate_report_payload,
    write_report,
)


def _fake_benchmark_report() -> dict:
    return {
        "documents": [
            {
                "document_id": "unit_doc",
                "source_file": "corpus/legal/unit.txt",
                "domain": "legal",
                "gold_label_count": 2,
                "prediction_count": 1,
                "matched_exact": [],
                "matched_text_normalized": [],
                "matched_overlap": [],
                "missed_required": [{"id": "L001", "required": True}],
                "wrong_type": [{"label": {"id": "L002"}, "predictions": []}],
                "false_positive_candidates": [],
                "preserve_term_hits": [{"preserve_term": {"term": "arts"}}],
                "known_trap_hits": [{"known_trap": {"text": "artikel 7:669 BW"}}],
            }
        ],
        "summary": {
            "document_count": 1,
            "gold_label_count": 2,
            "prediction_count": 1,
            "required_label_count": 2,
            "matched_required_exact_count": 0,
            "matched_required_text_normalized_count": 0,
            "matched_required_overlap_count": 0,
            "missed_required_count": 1,
            "wrong_type_count": 1,
            "false_positive_candidate_count": 0,
            "preserve_term_hit_count": 1,
            "known_trap_hit_count": 1,
        },
    }


def test_json_metadata_is_diagnostic_only():
    payload = build_diagnostic_report(report=_fake_benchmark_report())

    assert payload["metadata"] == DIAGNOSTIC_METADATA
    assert payload["metadata"]["status"] == "diagnostic_only"
    assert payload["metadata"]["synthetic_corpus"] is True
    assert payload["metadata"]["production_gate"] is False
    assert payload["metadata"]["thresholds_enforced"] is False


def test_markdown_summary_contains_required_interpretation_and_fields():
    payload = build_diagnostic_report(report=_fake_benchmark_report())
    markdown = render_markdown_summary(payload)

    assert "# Diagnostic recall benchmark report" in markdown
    assert "Status: diagnostic only" in markdown
    assert "No production threshold" in markdown
    assert "No product safety claim" in markdown
    for field in SUMMARY_FIELDS:
        assert field in markdown
    assert "This report is diagnostic" in markdown
    assert "unit_doc" in markdown


def test_write_report_outputs_valid_json_and_markdown(tmp_path):
    payload = build_diagnostic_report(report=_fake_benchmark_report())
    paths = write_report(output_dir=tmp_path, payload=payload, strict=True)

    json_path = paths["json"]
    markdown_path = paths["markdown"]
    assert json_path.name == REPORT_JSON_FILENAME
    assert markdown_path.name == REPORT_MARKDOWN_FILENAME
    assert json_path.exists()
    assert markdown_path.exists()

    loaded = json.loads(json_path.read_text(encoding="utf-8"))
    assert loaded["metadata"]["status"] == "diagnostic_only"
    assert markdown_path.read_text(encoding="utf-8").strip()


def test_no_threshold_gate_for_low_or_missing_counts():
    report = _fake_benchmark_report()
    report["summary"].update(
        {
            "gold_label_count": 100,
            "prediction_count": 0,
            "required_label_count": 100,
            "matched_required_exact_count": 0,
            "missed_required_count": 100,
        }
    )
    payload = build_diagnostic_report(report=report)

    validate_report_payload(payload)
    markdown = render_markdown_summary(payload)

    assert "missed_required_count: 100" in markdown
    assert payload["metadata"]["production_gate"] is False
    assert payload["metadata"]["thresholds_enforced"] is False


def test_cli_smoke_writes_report_files(tmp_path):
    output_dir = tmp_path / "recall_benchmark"

    result = main(["--corpus", "corpus", "--output", str(output_dir), "--strict"])

    assert result == 0
    assert (output_dir / REPORT_JSON_FILENAME).exists()
    assert (output_dir / REPORT_MARKDOWN_FILENAME).exists()
