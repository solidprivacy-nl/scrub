from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from recall_benchmark_runner import SUMMARY_FIELDS, run_benchmark


REPORT_JSON_FILENAME = "recall_benchmark_report.json"
REPORT_MARKDOWN_FILENAME = "recall_benchmark_summary.md"

DIAGNOSTIC_METADATA = {
    "status": "diagnostic_only",
    "synthetic_corpus": True,
    "production_gate": False,
    "thresholds_enforced": False,
}


def build_diagnostic_report(corpus_root: str | Path = "corpus", report: dict | None = None) -> dict:
    """Build a diagnostic report payload without applying thresholds or gates."""

    benchmark_report = report if report is not None else run_benchmark(corpus_root)
    return {
        "metadata": dict(DIAGNOSTIC_METADATA),
        "report": benchmark_report,
    }


def validate_report_payload(payload: dict) -> None:
    """Validate report structure only; never fail on recall/precision quality."""

    metadata = payload.get("metadata")
    report = payload.get("report")
    if not isinstance(metadata, dict):
        raise ValueError("Report payload must contain metadata")
    if not isinstance(report, dict):
        raise ValueError("Report payload must contain report")

    expected_metadata = DIAGNOSTIC_METADATA
    for key, expected_value in expected_metadata.items():
        if metadata.get(key) != expected_value:
            raise ValueError(f"metadata.{key} must be {expected_value!r}")

    documents = report.get("documents")
    summary = report.get("summary")
    if not isinstance(documents, list):
        raise ValueError("report.documents must be a list")
    if not isinstance(summary, dict):
        raise ValueError("report.summary must be a dict")

    missing_summary_fields = [field for field in SUMMARY_FIELDS if field not in summary]
    if missing_summary_fields:
        raise ValueError(f"report.summary missing fields: {missing_summary_fields}")


def _document_count(report: dict, document: dict, key: str) -> int:
    value = document.get(key, 0)
    if isinstance(value, list):
        return len(value)
    if isinstance(value, int):
        return value
    return 0


def render_markdown_summary(payload: dict) -> str:
    """Render a human-readable diagnostic summary.

    This is intentionally descriptive only. It does not compare against thresholds
    and does not create a product safety claim.
    """

    validate_report_payload(payload)
    report = payload["report"]
    summary = report["summary"]
    documents = report["documents"]

    lines = [
        "# Diagnostic recall benchmark report",
        "",
        "Status: diagnostic only",
        "Generated from synthetic corpus",
        "No production threshold",
        "No product safety claim",
        "",
        "## Summary",
        "",
    ]

    for field in SUMMARY_FIELDS:
        lines.append(f"- {field}: {summary.get(field, 0)}")

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This report is diagnostic. It does not prove that all sensitive data is detected.",
            "It does not enforce recall/precision thresholds and it is not a production gate.",
            "Candidate-scanner output is review-candidate visibility, not automatic masking proof.",
            "",
            "## Documents",
            "",
        ]
    )

    if not documents:
        lines.append("No document reports were generated.")
    else:
        for document in documents:
            lines.extend(
                [
                    f"### {document.get('document_id', 'unknown_document')}",
                    "",
                    f"- domain: {document.get('domain', '')}",
                    f"- source_file: {document.get('source_file', '')}",
                    f"- gold_label_count: {document.get('gold_label_count', 0)}",
                    f"- prediction_count: {document.get('prediction_count', 0)}",
                    f"- missed_required_count: {_document_count(report, document, 'missed_required')}",
                    f"- wrong_type_count: {_document_count(report, document, 'wrong_type')}",
                    f"- preserve_term_hit_count: {_document_count(report, document, 'preserve_term_hits')}",
                    f"- known_trap_hit_count: {_document_count(report, document, 'known_trap_hits')}",
                    "",
                ]
            )

    return "\n".join(lines).rstrip() + "\n"


def write_report(
    corpus_root: str | Path = "corpus",
    output_dir: str | Path = "output/recall_benchmark",
    payload: dict | None = None,
    strict: bool = False,
) -> dict[str, Path]:
    """Write JSON and Markdown diagnostic report files to an explicit output directory."""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    report_payload = payload if payload is not None else build_diagnostic_report(corpus_root)
    if strict:
        validate_report_payload(report_payload)

    json_path = output_path / REPORT_JSON_FILENAME
    markdown_path = output_path / REPORT_MARKDOWN_FILENAME

    json_path.write_text(json.dumps(report_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(render_markdown_summary(report_payload), encoding="utf-8")

    return {"json": json_path, "markdown": markdown_path}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate diagnostic recall benchmark JSON and Markdown reports.")
    parser.add_argument("--corpus", default="corpus", help="Corpus root containing .gold.json sidecars.")
    parser.add_argument("--output", default="output/recall_benchmark", help="Output directory for report files.")
    parser.add_argument("--strict", action="store_true", help="Validate report schema/integrity only; never enforce quality thresholds.")
    args = parser.parse_args(argv)

    paths = write_report(corpus_root=args.corpus, output_dir=args.output, strict=args.strict)
    print(f"Wrote diagnostic recall benchmark JSON: {paths['json']}")
    print(f"Wrote diagnostic recall benchmark Markdown: {paths['markdown']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
