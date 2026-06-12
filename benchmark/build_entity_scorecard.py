#!/usr/bin/env python3
"""WP23 report-only entity-class scorecard builder.

This helper wraps the WP22 recall/precision runner and writes CI-friendly JSON
and Markdown artifacts. It is intentionally report-only: malformed input may
fail the command, but recall/precision scores never create a production gate.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from run_recall_precision import ENTITY_CLASSES, run_benchmark
except ModuleNotFoundError:  # pragma: no cover - import path fallback for tests/importers
    import importlib.util
    import sys

    _RUNNER_PATH = Path(__file__).resolve().with_name("run_recall_precision.py")
    _SPEC = importlib.util.spec_from_file_location("run_recall_precision", _RUNNER_PATH)
    if _SPEC is None or _SPEC.loader is None:
        raise
    _MODULE = importlib.util.module_from_spec(_SPEC)
    sys.modules[_SPEC.name] = _MODULE
    _SPEC.loader.exec_module(_MODULE)
    ENTITY_CLASSES = _MODULE.ENTITY_CLASSES
    run_benchmark = _MODULE.run_benchmark


SCORECARD_SCHEMA_VERSION = "wp23_entity_class_scorecard_v1"
DEFAULT_REPORT_DIR = Path("benchmark/reports")
DEFAULT_GOLD_DIR = Path("benchmark/gold/examples")


def count(items: list[Any]) -> int:
    return len(items)


def _metric(bucket: dict[str, Any], key: str) -> Any:
    return bucket.get(key)


def _as_report_false_positive_count(bucket: dict[str, Any]) -> int:
    return int(bucket.get("false_positive_normalized", bucket.get("false_positive_count", 0)) or 0)


def _as_report_false_negative_count(bucket: dict[str, Any]) -> int:
    return int(bucket.get("false_negative_normalized", bucket.get("false_negative_count", 0)) or 0)


def summarize_entity_class(entity_class: str, bucket: dict[str, Any]) -> dict[str, Any]:
    return {
        "entity_class": entity_class,
        "gold_count": int(bucket.get("gold_count", 0) or 0),
        "prediction_count": int(bucket.get("prediction_count", 0) or 0),
        "true_positive_exact": int(bucket.get("true_positive_exact", 0) or 0),
        "true_positive_normalized": int(bucket.get("true_positive_normalized", 0) or 0),
        "false_negative_count": _as_report_false_negative_count(bucket),
        "false_positive_count": _as_report_false_positive_count(bucket),
        "recall_exact": _metric(bucket, "recall_exact"),
        "recall_normalized": _metric(bucket, "recall_normalized"),
        "precision_exact": _metric(bucket, "precision_exact"),
        "precision_normalized": _metric(bucket, "precision_normalized"),
    }


def build_scorecard(report: dict[str, Any], generated_at: str | None = None) -> dict[str, Any]:
    """Build a CI-friendly report-only entity-class scorecard from a WP22 report."""
    by_entity = report.get("by_entity_class", {})
    by_domain = report.get("by_domain", {})
    summary = report.get("summary", {})

    entity_classes = []
    for entity_class in ENTITY_CLASSES:
        entity_classes.append(summarize_entity_class(entity_class, by_entity.get(entity_class, {})))

    domain_metrics = {
        domain: {
            "gold_count": int(bucket.get("gold_count", 0) or 0),
            "prediction_count": int(bucket.get("prediction_count", 0) or 0),
            "true_positive_exact": int(bucket.get("true_positive_exact", 0) or 0),
            "true_positive_normalized": int(bucket.get("true_positive_normalized", 0) or 0),
            "false_negative_count": _as_report_false_negative_count(bucket),
            "false_positive_count": _as_report_false_positive_count(bucket),
            "recall_exact": _metric(bucket, "recall_exact"),
            "recall_normalized": _metric(bucket, "recall_normalized"),
            "precision_exact": _metric(bucket, "precision_exact"),
            "precision_normalized": _metric(bucket, "precision_normalized"),
        }
        for domain, bucket in sorted(by_domain.items())
    }

    return {
        "schema_version": SCORECARD_SCHEMA_VERSION,
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "synthetic_only": True,
        "report_only": True,
        "thresholds_applied": False,
        "production_gate": False,
        "safe_for_production_claim": False,
        "policy": {
            "ci_may_publish_report": True,
            "ci_may_fail_on_technical_errors": True,
            "ci_must_not_fail_on_scores_yet": True,
            "no_production_safety_claim": True,
            "no_real_documents": True,
            "no_cloud_calls": True,
        },
        "warnings": [
            "Synthetic benchmark only; results do not prove real-world safety.",
            "Report-only scorecard; no production-blocking threshold is applied.",
            *report.get("warnings", []),
        ],
        "overall": {
            "gold_count": int(summary.get("gold_count", 0) or 0),
            "prediction_count": int(summary.get("prediction_count", 0) or 0),
            "true_positive_exact": int(summary.get("true_positive_exact", 0) or 0),
            "true_positive_normalized": int(summary.get("true_positive_normalized", 0) or 0),
            "false_negative_count": _as_report_false_negative_count(summary),
            "false_positive_count": _as_report_false_positive_count(summary),
            "recall_exact": _metric(summary, "recall_exact"),
            "recall_normalized": _metric(summary, "recall_normalized"),
            "precision_exact": _metric(summary, "precision_exact"),
            "precision_normalized": _metric(summary, "precision_normalized"),
        },
        "per_domain": domain_metrics,
        "per_entity_class": entity_classes,
        "failure_counts": {
            "false_negative_count": count(report.get("false_negatives", [])),
            "false_positive_count": count(report.get("false_positives", [])),
            "preserve_term_failure_count": count(report.get("preserve_term_failures", [])),
            "known_trap_failure_count": count(report.get("known_trap_failures", [])),
            "partial_overlap_diagnostic_count": count(report.get("partial_overlaps", [])),
        },
        "details": {
            "false_negatives": report.get("false_negatives", []),
            "false_positives": report.get("false_positives", []),
            "preserve_term_failures": report.get("preserve_term_failures", []),
            "known_trap_failures": report.get("known_trap_failures", []),
            "partial_overlaps": report.get("partial_overlaps", []),
        },
        "source_report_schema_version": report.get("schema_version"),
        "gold_files": report.get("gold_files", []),
        "prediction_file": report.get("prediction_file"),
    }


def fmt(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def render_markdown(scorecard: dict[str, Any]) -> str:
    """Render the scorecard as Markdown for CI artifacts."""
    lines = [
        "# SolidPrivacy Scrub — Entity-class scorecard",
        "",
        f"Generated: `{scorecard['generated_at']}`",
        "",
        "## Policy",
        "",
        "- Synthetic benchmark only.",
        "- Report-only.",
        "- No production-blocking threshold is applied.",
        "- No `safe for production` claim is made.",
        "- CI may fail on technical errors such as malformed JSON, bad offsets or runner exceptions.",
        "- CI must not fail on recall/precision scores until a later approved threshold workpackage.",
        "",
        "## Overall metrics",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ]
    overall = scorecard["overall"]
    for key in [
        "gold_count", "prediction_count", "true_positive_exact", "true_positive_normalized",
        "false_negative_count", "false_positive_count", "recall_exact", "recall_normalized",
        "precision_exact", "precision_normalized",
    ]:
        lines.append(f"| `{key}` | {fmt(overall.get(key))} |")

    lines.extend([
        "",
        "## Per-domain metrics",
        "",
        "| Domain | Gold | Predictions | TP exact | TP normalized | FN | FP | Recall exact | Recall normalized | Precision exact | Precision normalized |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for domain, metrics in scorecard["per_domain"].items():
        lines.append(
            f"| `{domain}` | {metrics['gold_count']} | {metrics['prediction_count']} | "
            f"{metrics['true_positive_exact']} | {metrics['true_positive_normalized']} | "
            f"{metrics['false_negative_count']} | {metrics['false_positive_count']} | "
            f"{fmt(metrics['recall_exact'])} | {fmt(metrics['recall_normalized'])} | "
            f"{fmt(metrics['precision_exact'])} | {fmt(metrics['precision_normalized'])} |"
        )

    lines.extend([
        "",
        "## Per-entity-class metrics",
        "",
        "| Entity class | Gold | Predictions | TP exact | TP normalized | FN | FP | Recall exact | Recall normalized | Precision exact | Precision normalized |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for item in scorecard["per_entity_class"]:
        lines.append(
            f"| `{item['entity_class']}` | {item['gold_count']} | {item['prediction_count']} | "
            f"{item['true_positive_exact']} | {item['true_positive_normalized']} | "
            f"{item['false_negative_count']} | {item['false_positive_count']} | "
            f"{fmt(item['recall_exact'])} | {fmt(item['recall_normalized'])} | "
            f"{fmt(item['precision_exact'])} | {fmt(item['precision_normalized'])} |"
        )

    failure_counts = scorecard["failure_counts"]
    lines.extend([
        "",
        "## Failure and diagnostic counts",
        "",
        "| Count | Value |",
        "|---|---:|",
        f"| `preserve_term_failure_count` | {failure_counts['preserve_term_failure_count']} |",
        f"| `known_trap_failure_count` | {failure_counts['known_trap_failure_count']} |",
        f"| `partial_overlap_diagnostic_count` | {failure_counts['partial_overlap_diagnostic_count']} |",
        f"| `false_negative_count` | {failure_counts['false_negative_count']} |",
        f"| `false_positive_count` | {failure_counts['false_positive_count']} |",
        "",
        "## Warnings",
        "",
    ])
    lines.extend(f"- {warning}" for warning in scorecard.get("warnings", []))
    lines.append("")
    return "\n".join(lines)


def write_scorecard(scorecard: dict[str, Any], output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "entity_scorecard.json"
    md_path = output_dir / "entity_scorecard.md"
    json_path.write_text(json.dumps(scorecard, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(scorecard), encoding="utf-8")
    return json_path, md_path


def build_from_inputs(repo_root: Path, gold_path: Path, predictions_path: Path | None, include_schema_examples: bool = True) -> dict[str, Any]:
    report = run_benchmark(repo_root, gold_path, predictions_path, include_schema_examples=include_schema_examples)
    return build_scorecard(report)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build a report-only entity-class scorecard from the WP22 runner.")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--gold", type=Path, default=DEFAULT_GOLD_DIR, help="Gold sidecar file or directory.")
    parser.add_argument("--predictions", type=Path, default=None, help="Optional prediction JSON file.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_REPORT_DIR, help="Directory for JSON and Markdown artifacts.")
    parser.add_argument("--only-complete", action="store_true", help="Skip schema_example_only sidecars.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repo_root = args.repo_root.resolve()
    gold_path = args.gold if args.gold.is_absolute() else repo_root / args.gold
    predictions_path = None if args.predictions is None else (args.predictions if args.predictions.is_absolute() else repo_root / args.predictions)
    output_dir = args.output_dir if args.output_dir.is_absolute() else repo_root / args.output_dir
    scorecard = build_from_inputs(repo_root, gold_path, predictions_path, include_schema_examples=not args.only_complete)
    json_path, md_path = write_scorecard(scorecard, output_dir)
    print(f"Wrote report-only scorecard JSON: {json_path}")
    print(f"Wrote report-only scorecard Markdown: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
