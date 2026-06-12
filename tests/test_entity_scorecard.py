import importlib.util
import json
import sys
from pathlib import Path


def load_scorecard_module():
    module_path = Path(__file__).resolve().parents[1] / "benchmark" / "build_entity_scorecard.py"
    spec = importlib.util.spec_from_file_location("build_entity_scorecard", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sample_wp22_report():
    return {
        "schema_version": "wp22_recall_precision_runner_v1",
        "synthetic_only": True,
        "thresholds_applied": False,
        "gold_files": ["benchmark/gold/examples/mini.gold.example.json"],
        "prediction_file": "predictions.json",
        "warnings": ["example warning"],
        "summary": {
            "gold_count": 2,
            "prediction_count": 3,
            "true_positive_exact": 1,
            "true_positive_normalized": 2,
            "false_negative_exact": 1,
            "false_negative_normalized": 0,
            "false_positive_exact": 2,
            "false_positive_normalized": 1,
            "recall_exact": 0.5,
            "recall_normalized": 1.0,
            "precision_exact": 0.333333,
            "precision_normalized": 0.666667,
        },
        "by_domain": {
            "legal": {
                "gold_count": 2,
                "prediction_count": 3,
                "true_positive_exact": 1,
                "true_positive_normalized": 2,
                "false_negative_exact": 1,
                "false_negative_normalized": 0,
                "false_positive_exact": 2,
                "false_positive_normalized": 1,
                "recall_exact": 0.5,
                "recall_normalized": 1.0,
                "precision_exact": 0.333333,
                "precision_normalized": 0.666667,
            }
        },
        "by_entity_class": {
            "PERSON": {
                "gold_count": 1,
                "prediction_count": 1,
                "true_positive_exact": 1,
                "true_positive_normalized": 1,
                "false_negative_exact": 0,
                "false_negative_normalized": 0,
                "false_positive_exact": 0,
                "false_positive_normalized": 0,
                "recall_exact": 1.0,
                "recall_normalized": 1.0,
                "precision_exact": 1.0,
                "precision_normalized": 1.0,
            },
            "PHONE": {
                "gold_count": 1,
                "prediction_count": 2,
                "true_positive_exact": 0,
                "true_positive_normalized": 1,
                "false_negative_exact": 1,
                "false_negative_normalized": 0,
                "false_positive_exact": 2,
                "false_positive_normalized": 1,
                "recall_exact": 0.0,
                "recall_normalized": 1.0,
                "precision_exact": 0.0,
                "precision_normalized": 0.5,
            },
        },
        "false_negatives": [],
        "false_positives": [{"document_id": "mini", "text": "extra"}],
        "preserve_term_failures": [{"term": "cliënt"}],
        "known_trap_failures": [{"trap_text": "13-03-2026"}],
        "partial_overlaps": [{"policy": "diagnostic_only"}],
    }


def test_build_scorecard_contains_required_report_only_fields():
    scorecard_module = load_scorecard_module()

    scorecard = scorecard_module.build_scorecard(sample_wp22_report(), generated_at="2026-06-12T10:00:00+00:00")

    assert scorecard["schema_version"] == "wp23_entity_class_scorecard_v1"
    assert scorecard["synthetic_only"] is True
    assert scorecard["report_only"] is True
    assert scorecard["thresholds_applied"] is False
    assert scorecard["production_gate"] is False
    assert scorecard["safe_for_production_claim"] is False
    assert scorecard["policy"]["ci_may_publish_report"] is True
    assert scorecard["policy"]["ci_may_fail_on_technical_errors"] is True
    assert scorecard["policy"]["ci_must_not_fail_on_scores_yet"] is True
    assert scorecard["overall"]["gold_count"] == 2
    assert scorecard["overall"]["prediction_count"] == 3
    assert scorecard["overall"]["true_positive_exact"] == 1
    assert scorecard["overall"]["true_positive_normalized"] == 2
    assert scorecard["overall"]["false_negative_count"] == 0
    assert scorecard["overall"]["false_positive_count"] == 1
    assert scorecard["failure_counts"]["preserve_term_failure_count"] == 1
    assert scorecard["failure_counts"]["known_trap_failure_count"] == 1
    assert scorecard["failure_counts"]["partial_overlap_diagnostic_count"] == 1


def test_scorecard_includes_zero_rows_for_all_entity_classes():
    scorecard_module = load_scorecard_module()

    scorecard = scorecard_module.build_scorecard(sample_wp22_report(), generated_at="2026-06-12T10:00:00+00:00")
    by_entity = {row["entity_class"]: row for row in scorecard["per_entity_class"]}

    assert "PERSON" in by_entity
    assert "MEDICAL_OR_CARE_REFERENCE" in by_entity
    assert by_entity["MEDICAL_OR_CARE_REFERENCE"]["gold_count"] == 0
    assert by_entity["MEDICAL_OR_CARE_REFERENCE"]["prediction_count"] == 0


def test_markdown_scorecard_contains_policy_and_metrics():
    scorecard_module = load_scorecard_module()
    scorecard = scorecard_module.build_scorecard(sample_wp22_report(), generated_at="2026-06-12T10:00:00+00:00")

    markdown = scorecard_module.render_markdown(scorecard)

    assert "Report-only" in markdown
    assert "No production-blocking threshold is applied" in markdown
    assert "No `safe for production` claim is made" in markdown
    assert "`PERSON`" in markdown
    assert "`preserve_term_failure_count` | 1" in markdown
    assert "`known_trap_failure_count` | 1" in markdown
    assert "`partial_overlap_diagnostic_count` | 1" in markdown


def test_write_scorecard_outputs_json_and_markdown(tmp_path):
    scorecard_module = load_scorecard_module()
    scorecard = scorecard_module.build_scorecard(sample_wp22_report(), generated_at="2026-06-12T10:00:00+00:00")

    json_path, md_path = scorecard_module.write_scorecard(scorecard, tmp_path / "reports")

    parsed = json.loads(json_path.read_text(encoding="utf-8"))
    assert parsed["schema_version"] == "wp23_entity_class_scorecard_v1"
    assert md_path.read_text(encoding="utf-8").startswith("# SolidPrivacy Scrub — Entity-class scorecard")
