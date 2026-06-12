#!/usr/bin/env python3
"""WP24 report-only false-negative residual-risk report builder.

This helper consumes the WP23 entity-class scorecard and writes JSON/Markdown
residual-risk artifacts. It is intentionally report-only: technical input errors
may fail, but recall/precision scores never create a production gate.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from build_entity_scorecard import build_from_inputs as build_scorecard_from_inputs
except ModuleNotFoundError:  # pragma: no cover - import path fallback for tests/importers
    import importlib.util
    import sys

    _SCORECARD_PATH = Path(__file__).resolve().with_name("build_entity_scorecard.py")
    _SPEC = importlib.util.spec_from_file_location("build_entity_scorecard", _SCORECARD_PATH)
    if _SPEC is None or _SPEC.loader is None:
        raise
    _MODULE = importlib.util.module_from_spec(_SPEC)
    sys.modules[_SPEC.name] = _MODULE
    _SPEC.loader.exec_module(_MODULE)
    build_scorecard_from_inputs = _MODULE.build_from_inputs


RESIDUAL_RISK_SCHEMA_VERSION = "wp24_false_negative_residual_risk_report_v1"
DEFAULT_REPORT_DIR = Path("benchmark/reports")
DEFAULT_GOLD_DIR = Path("benchmark/gold/examples")


def _as_count(value: Any) -> int:
    return int(value or 0)


def _risk_level(gold_count: int, false_negative_count: int, recall_normalized: Any) -> str:
    if gold_count == 0:
        return "not_yet_baselined"
    if recall_normalized is None:
        return "not_measurable"
    if false_negative_count > 0:
        return "high_residual_risk"
    return "diagnostic_no_current_false_negative"


def _coverage_warnings(scorecard: dict[str, Any]) -> list[str]:
    warnings = [str(warning) for warning in scorecard.get("warnings", [])]
    coverage_warnings = []
    if any("schema example" in warning.lower() for warning in warnings):
        coverage_warnings.append("Current gold sidecars are schema examples only, not complete corpus labels.")
    if not scorecard.get("prediction_file"):
        coverage_warnings.append("Runner/scorecard currently scores supplied prediction JSON only; no prediction file was supplied.")
    return coverage_warnings


def _overall_risk_level(scorecard: dict[str, Any]) -> str:
    overall = scorecard.get("overall", {})
    if _coverage_warnings(scorecard):
        return "critical_unresolved_due_to_coverage_limits"
    return _risk_level(
        _as_count(overall.get("gold_count")),
        _as_count(overall.get("false_negative_count")),
        overall.get("recall_normalized"),
    )


def _domain_summary_text(domain: str, gold_count: int, false_negative_count: int, recall_normalized: Any) -> str:
    if gold_count == 0:
        return f"{domain}: no gold labels are currently baselined for this domain."
    if recall_normalized is None:
        return f"{domain}: recall is not measurable yet."
    if false_negative_count > 0:
        return f"{domain}: {false_negative_count} normalized false negative(s) remain visible in the synthetic benchmark."
    return f"{domain}: no normalized false negatives in current supplied synthetic scorecard, but coverage remains limited."


def summarize_domain(domain: str, metrics: dict[str, Any]) -> dict[str, Any]:
    gold_count = _as_count(metrics.get("gold_count"))
    false_negative_count = _as_count(metrics.get("false_negative_count"))
    return {
        "domain": domain,
        "gold_count": gold_count,
        "prediction_count": _as_count(metrics.get("prediction_count")),
        "false_negative_count": false_negative_count,
        "false_positive_count": _as_count(metrics.get("false_positive_count")),
        "recall_normalized": metrics.get("recall_normalized"),
        "precision_normalized": metrics.get("precision_normalized"),
        "residual_risk_level": _risk_level(gold_count, false_negative_count, metrics.get("recall_normalized")),
        "summary": _domain_summary_text(domain, gold_count, false_negative_count, metrics.get("recall_normalized")),
    }


def summarize_entity(item: dict[str, Any]) -> dict[str, Any]:
    gold_count = _as_count(item.get("gold_count"))
    false_negative_count = _as_count(item.get("false_negative_count"))
    return {
        "entity_class": item.get("entity_class"),
        "gold_count": gold_count,
        "prediction_count": _as_count(item.get("prediction_count")),
        "false_negative_count": false_negative_count,
        "false_positive_count": _as_count(item.get("false_positive_count")),
        "recall_normalized": item.get("recall_normalized"),
        "precision_normalized": item.get("precision_normalized"),
        "residual_risk_level": _risk_level(gold_count, false_negative_count, item.get("recall_normalized")),
    }


def build_residual_risk_report(scorecard: dict[str, Any], generated_at: str | None = None) -> dict[str, Any]:
    """Build a report-only residual-risk report from a WP23 scorecard."""
    failure_counts = scorecard.get("failure_counts", {})
    coverage_limitations = [
        "Current gold sidecars are schema examples only; they are not complete labels for the full synthetic corpus.",
        "The runner/scorecard scores supplied prediction JSON only; it does not invoke recognizers or establish accepted baselines.",
        "No recall/precision threshold or production-blocking gate is applied.",
        "No production safety claim is supported.",
    ]
    coverage_limitations.extend(_coverage_warnings(scorecard))

    per_domain = {
        domain: summarize_domain(domain, metrics)
        for domain, metrics in sorted(scorecard.get("per_domain", {}).items())
    }
    per_entity_class = [summarize_entity(item) for item in scorecard.get("per_entity_class", [])]
    unsupported_or_not_yet_baselined = [
        str(item["entity_class"])
        for item in per_entity_class
        if item["gold_count"] == 0
    ]

    return {
        "schema_version": RESIDUAL_RISK_SCHEMA_VERSION,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "synthetic_only": True,
        "report_only": True,
        "thresholds_applied": False,
        "production_gate": False,
        "safe_for_production_claim": False,
        "policy": {
            "risk_visible": True,
            "no_production_safety_claim": True,
            "no_recall_precision_threshold": True,
            "ci_must_not_fail_on_low_scores": True,
            "ci_may_fail_on_technical_errors": True,
            "no_real_documents": True,
            "no_cloud_calls": True,
        },
        "warnings": [
            "Synthetic benchmark only; this report does not prove real-world safety.",
            "Report-only residual-risk report; no threshold or production gate is applied.",
            "Do not use this report as a claim that Scrub is safe for real confidential production documents.",
            *coverage_limitations,
        ],
        "coverage_status": {
            "current_benchmark_coverage_status": "foundation_only_not_full_corpus",
            "known_limitations": coverage_limitations,
            "gold_file_count": len(scorecard.get("gold_files", [])),
            "prediction_file": scorecard.get("prediction_file"),
            "scorecard_schema_version": scorecard.get("schema_version"),
            "not_yet_baselined_entity_classes": unsupported_or_not_yet_baselined,
        },
        "overall_false_negative_risk_summary": {
            "residual_risk_level": _overall_risk_level(scorecard),
            "gold_count": _as_count(scorecard.get("overall", {}).get("gold_count")),
            "prediction_count": _as_count(scorecard.get("overall", {}).get("prediction_count")),
            "false_negative_count": _as_count(scorecard.get("overall", {}).get("false_negative_count")),
            "recall_normalized": scorecard.get("overall", {}).get("recall_normalized"),
            "summary": "False-negative risk remains unresolved until complete labels, recognizer-backed predictions, accepted baselines and residual-risk policy exist.",
        },
        "per_domain_residual_risk": per_domain,
        "per_entity_class_residual_risk": per_entity_class,
        "preserve_term_risk_summary": {
            "failure_count": _as_count(failure_counts.get("preserve_term_failure_count")),
            "risk": "Over-masking or detecting preserve terms can damage legal/care meaning.",
            "details": scorecard.get("details", {}).get("preserve_term_failures", []),
        },
        "known_trap_false_positive_risk_summary": {
            "known_trap_failure_count": _as_count(failure_counts.get("known_trap_failure_count")),
            "false_positive_count": _as_count(failure_counts.get("false_positive_count")),
            "risk": "False positives on known traps can mask context, legal articles, dates, times or labels incorrectly.",
            "details": scorecard.get("details", {}).get("known_trap_failures", []),
        },
        "partial_overlap_near_miss_summary": {
            "partial_overlap_diagnostic_count": _as_count(failure_counts.get("partial_overlap_diagnostic_count")),
            "risk": "Partial overlaps are diagnostics only and must not hide false negatives.",
            "details": scorecard.get("details", {}).get("partial_overlaps", []),
        },
        "unsupported_or_not_yet_baselined_classes": unsupported_or_not_yet_baselined,
        "recommended_next_benchmark_data_work": [
            "Create complete gold-label sidecars for the committed synthetic legal, zorg and mixed corpus.",
            "Add recognizer-backed prediction export/input for the runner without changing recognizer logic in this package.",
            "Define accepted baselines before any score threshold is introduced.",
            "Keep reporting exact and normalized metrics separately.",
        ],
        "recommended_next_product_risk_mitigations": [
            "Run WP29 — Scrub Key secure import/export tests.",
            "Continue human review and final review summary as required safeguards.",
            "Do not claim production safety until false-negative residual risk, hidden document content risk and local runtime trust are addressed.",
            "Use WP24 output as internal/support guidance, not marketing accuracy evidence.",
        ],
        "source_scorecard": {
            "schema_version": scorecard.get("schema_version"),
            "gold_files": scorecard.get("gold_files", []),
            "prediction_file": scorecard.get("prediction_file"),
        },
    }


def fmt(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# SolidPrivacy Scrub — False-negative residual-risk report",
        "",
        f"Generated: `{report['generated_at']}`",
        "",
        "## Policy",
        "",
        "- Synthetic benchmark only.",
        "- Report-only.",
        "- No production safety claim.",
        "- No recall/precision threshold.",
        "- CI must not fail on low scores yet.",
        "- Technical errors such as malformed JSON or broken offsets may fail.",
        "- No real documents and no cloud calls.",
        "",
        "## Coverage status",
        "",
        f"- Status: `{report['coverage_status']['current_benchmark_coverage_status']}`",
        f"- Gold files: `{report['coverage_status']['gold_file_count']}`",
        f"- Prediction file: `{report['coverage_status']['prediction_file'] or 'none'}`",
        "",
        "Known limitations:",
        "",
    ]
    lines.extend(f"- {item}" for item in report["coverage_status"]["known_limitations"])

    overall = report["overall_false_negative_risk_summary"]
    lines.extend([
        "",
        "## Overall false-negative risk",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| `residual_risk_level` | `{overall['residual_risk_level']}` |",
        f"| `gold_count` | {overall['gold_count']} |",
        f"| `prediction_count` | {overall['prediction_count']} |",
        f"| `false_negative_count` | {overall['false_negative_count']} |",
        f"| `recall_normalized` | {fmt(overall['recall_normalized'])} |",
        "",
        overall["summary"],
        "",
        "## Per-domain residual risk",
        "",
        "| Domain | Gold | Predictions | False negatives | False positives | Recall normalized | Precision normalized | Risk |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ])
    for domain, item in report["per_domain_residual_risk"].items():
        lines.append(
            f"| `{domain}` | {item['gold_count']} | {item['prediction_count']} | "
            f"{item['false_negative_count']} | {item['false_positive_count']} | "
            f"{fmt(item['recall_normalized'])} | {fmt(item['precision_normalized'])} | "
            f"`{item['residual_risk_level']}` |"
        )

    lines.extend([
        "",
        "## Per-entity-class residual risk",
        "",
        "| Entity class | Gold | Predictions | False negatives | False positives | Recall normalized | Precision normalized | Risk |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ])
    for item in report["per_entity_class_residual_risk"]:
        lines.append(
            f"| `{item['entity_class']}` | {item['gold_count']} | {item['prediction_count']} | "
            f"{item['false_negative_count']} | {item['false_positive_count']} | "
            f"{fmt(item['recall_normalized'])} | {fmt(item['precision_normalized'])} | "
            f"`{item['residual_risk_level']}` |"
        )

    lines.extend([
        "",
        "## Preserve-term, known-trap and near-miss summaries",
        "",
        f"- Preserve-term failures: `{report['preserve_term_risk_summary']['failure_count']}`",
        f"- Known-trap failures: `{report['known_trap_false_positive_risk_summary']['known_trap_failure_count']}`",
        f"- False positives: `{report['known_trap_false_positive_risk_summary']['false_positive_count']}`",
        f"- Partial-overlap diagnostics: `{report['partial_overlap_near_miss_summary']['partial_overlap_diagnostic_count']}`",
        "",
        "## Unsupported or not-yet-baselined classes",
        "",
    ])
    if report["unsupported_or_not_yet_baselined_classes"]:
        lines.extend(f"- `{entity_class}`" for entity_class in report["unsupported_or_not_yet_baselined_classes"])
    else:
        lines.append("- None in the supplied scorecard.")

    lines.extend([
        "",
        "## Recommended next benchmark/data work",
        "",
    ])
    lines.extend(f"- {item}" for item in report["recommended_next_benchmark_data_work"])
    lines.extend([
        "",
        "## Recommended next product-risk mitigations",
        "",
    ])
    lines.extend(f"- {item}" for item in report["recommended_next_product_risk_mitigations"])
    lines.append("")
    return "\n".join(lines)


def write_residual_risk_report(report: dict[str, Any], output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "false_negative_residual_risk_report.json"
    md_path = output_dir / "false_negative_residual_risk_report.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(report), encoding="utf-8")
    return json_path, md_path


def build_from_scorecard_file(scorecard_path: Path) -> dict[str, Any]:
    with scorecard_path.open("r", encoding="utf-8") as handle:
        return build_residual_risk_report(json.load(handle))


def build_from_inputs(repo_root: Path, gold_path: Path, predictions_path: Path | None, include_schema_examples: bool = True) -> dict[str, Any]:
    scorecard = build_scorecard_from_inputs(repo_root, gold_path, predictions_path, include_schema_examples)
    return build_residual_risk_report(scorecard)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build a report-only false-negative residual-risk report.")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--gold", type=Path, default=DEFAULT_GOLD_DIR, help="Gold sidecar file or directory.")
    parser.add_argument("--predictions", type=Path, default=None, help="Optional prediction JSON file.")
    parser.add_argument("--scorecard", type=Path, default=None, help="Optional existing WP23 scorecard JSON file.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_REPORT_DIR, help="Directory for JSON and Markdown artifacts.")
    parser.add_argument("--only-complete", action="store_true", help="Skip schema_example_only sidecars.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repo_root = args.repo_root.resolve()
    output_dir = args.output_dir if args.output_dir.is_absolute() else repo_root / args.output_dir

    if args.scorecard is not None:
        scorecard_path = args.scorecard if args.scorecard.is_absolute() else repo_root / args.scorecard
        report = build_from_scorecard_file(scorecard_path)
    else:
        gold_path = args.gold if args.gold.is_absolute() else repo_root / args.gold
        predictions_path = None if args.predictions is None else (args.predictions if args.predictions.is_absolute() else repo_root / args.predictions)
        report = build_from_inputs(repo_root, gold_path, predictions_path, include_schema_examples=not args.only_complete)

    json_path, md_path = write_residual_risk_report(report, output_dir)
    print(f"Wrote report-only residual-risk JSON: {json_path}")
    print(f"Wrote report-only residual-risk Markdown: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
