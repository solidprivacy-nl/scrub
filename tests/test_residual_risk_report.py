import importlib.util
import json
import sys
from pathlib import Path


def load_residual_module():
    module_path = Path(__file__).resolve().parents[1] / "benchmark" / "build_residual_risk_report.py"
    spec = importlib.util.spec_from_file_location("build_residual_risk_report", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sample_scorecard():
    return {
        "schema_version": "wp23_entity_class_scorecard_v1",
        "generated_at": "2026-06-12T10:00:00+00:00",
        "synthetic_only": True,
        "report_only": True,
        "thresholds_applied": False,
        "production_gate": False,
        "safe_for_production_claim": False,
        "warnings": [
            "Synthetic benchmark only; results do not prove real-world safety.",
            "benchmark/gold/examples/mini.gold.example.json: schema example only; metrics are diagnostic, not full corpus results",
        ],
        "overall": {
            "gold_count": 3,
            "prediction_count": 3,
            "false_negative_count": 1,
            "false_positive_count": 1,
            "recall_normalized": 0.666667,
            "precision_normalized": 0.666667,
        },
        "per_domain": {
            "legal": {
                "gold_count": 2,
                "prediction_count": 2,
                "false_negative_count": 1,
                "false_positive_count": 1,
                "recall_normalized": 0.5,
                "precision_normalized": 0.5,
            },
            "zorg": {
                "gold_count": 1,
                "prediction_count": 1,
                "false_negative_count": 0,
                "false_positive_count": 0,
                "recall_normalized": 1.0,
                "precision_normalized": 1.0,
            },
        },
        "per_entity_class": [
            {
                "entity_class": "PERSON",
                "gold_count": 1,
                "prediction_count": 1,
                "false_negative_count": 0,
                "false_positive_count": 0,
                "recall_normalized": 1.0,
                "precision_normalized": 1.0,
            },
            {
                "entity_class": "PHONE",
                "gold_count": 1,
                "prediction_count": 1,
                "false_negative_count": 1,
                "false_positive_count": 1,
                "recall_normalized": 0.0,
                "precision_normalized": 0.0,
            },
            {
                "entity_class": "BSN",
                "gold_count": 0,
                "prediction_count": 0,
                "false_negative_count": 0,
                "false_positive_count": 0,
                "recall_normalized": None,
                "precision_normalized": None,
            },
        ],
        "failure_counts": {
            "false_negative_count": 1,
            "false_positive_count": 1,
            "preserve_term_failure_count": 1,
            "known_trap_failure_count": 1,
            "partial_overlap_diagnostic_count": 1,
        },
        "details": {
            "false_negatives": [{"entity_class": "PHONE", "expected_text": "06 1234 5678"}],
            "false_positives": [{"entity_class": "BSN", "text": "13-03-2026"}],
            "preserve_term_failures": [{"term": "cliënt"}],
            "known_trap_failures": [{"trap_text": "13-03-2026"}],
            "partial_overlaps": [{"policy": "diagnostic_only"}],
        },
        "gold_files": ["benchmark/gold/examples/mini.gold.example.json"],
        "prediction_file": None,
    }


def test_residual_report_contains_required_policy_and_limitations():
    module = load_residual_module()

    report = module.build_residual_risk_report(sample_scorecard(), generated_at="2026-06-12T12:30:00+00:00")

    assert report["schema_version"] == "wp24_false_negative_residual_risk_report_v1"
    assert report["synthetic_only"] is True
    assert report["report_only"] is True
    assert report["thresholds_applied"] is False
    assert report["production_gate"] is False
    assert report["safe_for_production_claim"] is False
    assert report["policy"]["risk_visible"] is True
    assert report["policy"]["no_production_safety_claim"] is True
    assert report["policy"]["no_recall_precision_threshold"] is True
    assert report["policy"]["ci_must_not_fail_on_low_scores"] is True
    assert "schema examples only" in " ".join(report["coverage_status"]["known_limitations"])
    assert "supplied prediction JSON only" in " ".join(report["coverage_status"]["known_limitations"])
    assert report["overall_false_negative_risk_summary"]["residual_risk_level"] == "critical_unresolved_due_to_coverage_limits"


def test_residual_report_summarizes_domain_entity_preserve_trap_and_near_miss_risks():
    module = load_residual_module()
    report = module.build_residual_risk_report(sample_scorecard(), generated_at="2026-06-12T12:30:00+00:00")

    assert report["per_domain_residual_risk"]["legal"]["residual_risk_level"] == "high_residual_risk"
    by_entity = {item["entity_class"]: item for item in report["per_entity_class_residual_risk"]}
    assert by_entity["PHONE"]["residual_risk_level"] == "high_residual_risk"
    assert by_entity["BSN"]["residual_risk_level"] == "not_yet_baselined"
    assert "BSN" in report["unsupported_or_not_yet_baselined_classes"]
    assert report["preserve_term_risk_summary"]["failure_count"] == 1
    assert report["known_trap_false_positive_risk_summary"]["known_trap_failure_count"] == 1
    assert report["partial_overlap_near_miss_summary"]["partial_overlap_diagnostic_count"] == 1


def test_residual_markdown_contains_no_safety_claim_and_next_work():
    module = load_residual_module()
    report = module.build_residual_risk_report(sample_scorecard(), generated_at="2026-06-12T12:30:00+00:00")

    markdown = module.render_markdown(report)

    assert "No production safety claim" in markdown
    assert "No recall/precision threshold" in markdown
    assert "Current gold sidecars are schema examples only" in markdown
    assert "WP29 — Scrub Key secure import/export tests" in markdown
    assert "`PHONE`" in markdown
    assert "`partial_overlap_near_miss_summary`" not in markdown


def test_write_residual_risk_report_outputs_json_and_markdown(tmp_path):
    module = load_residual_module()
    report = module.build_residual_risk_report(sample_scorecard(), generated_at="2026-06-12T12:30:00+00:00")

    json_path, md_path = module.write_residual_risk_report(report, tmp_path / "reports")

    parsed = json.loads(json_path.read_text(encoding="utf-8"))
    assert parsed["schema_version"] == "wp24_false_negative_residual_risk_report_v1"
    assert md_path.read_text(encoding="utf-8").startswith("# SolidPrivacy Scrub — False-negative residual-risk report")
