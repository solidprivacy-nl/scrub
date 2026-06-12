#!/usr/bin/env python3
"""WP22 deterministic recall/precision runner for synthetic gold-label sidecars.

This script validates WP21 gold-label offsets and scores supplied prediction JSON.
It does not call recognizers, Streamlit, AI, cloud services, or apply CI thresholds.
"""
from __future__ import annotations

import argparse
import json
import re
import string
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ENTITY_CLASSES = [
    "PERSON", "ADDRESS", "EMAIL", "PHONE", "BSN", "IBAN", "DATE", "NL_POSTCODE",
    "CASE_NUMBER", "DOSSIER_NUMBER", "CLIENT_NUMBER", "CLAIM_NUMBER", "INCIDENT_NUMBER",
    "ECLI", "ORGANIZATION", "MEDICAL_OR_CARE_REFERENCE", "ROLE_OR_CONTEXT_TERM_TO_PRESERVE",
]
REPORT_SCHEMA_VERSION = "wp22_recall_precision_runner_v1"
DEFAULT_GOLD_DIR = Path("benchmark/gold/examples")


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def as_int(value: Any, name: str) -> int:
    if not isinstance(value, int):
        raise ValueError(f"{name} must be an integer, got {value!r}")
    return value


def validate_span(source_text: str, expected: str, start: int, end: int, context: str) -> None:
    if start < 0 or end <= start:
        raise ValueError(f"{context}: invalid offsets start={start} end={end}")
    actual = source_text[start:end]
    if actual != expected:
        raise ValueError(
            f"{context}: text/span mismatch at {start}:{end}; "
            f"expected {expected!r}, source has {actual!r}"
        )


def discover_gold_sidecars(gold_path: Path) -> list[Path]:
    if gold_path.is_file():
        return [gold_path]
    if not gold_path.exists():
        raise FileNotFoundError(f"Gold path does not exist: {gold_path}")
    return sorted(
        path for path in gold_path.rglob("*.json")
        if path.name.endswith((".gold.json", ".gold.example.json"))
    )


def load_gold_sidecars(
    gold_path: Path,
    repo_root: Path,
    include_schema_examples: bool = True,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[str], list[str]]:
    labels: list[dict[str, Any]] = []
    preserve_terms: list[dict[str, Any]] = []
    known_traps: list[dict[str, Any]] = []
    warnings: list[str] = []
    loaded_files: list[str] = []

    for sidecar_path in discover_gold_sidecars(gold_path):
        sidecar = read_json(sidecar_path)
        completeness = sidecar.get("completeness", "complete_gold_labels")
        if completeness == "schema_example_only":
            warning = f"{sidecar_path}: schema example only; metrics are diagnostic, not full corpus results"
            if include_schema_examples:
                warnings.append(warning)
            else:
                continue
        if sidecar.get("synthetic") is not True:
            raise ValueError(f"{sidecar_path}: synthetic must be true")

        source_file = str(sidecar["source_file"])
        source_path = repo_root / source_file
        if not source_path.exists():
            raise FileNotFoundError(f"{sidecar_path}: source_file not found: {source_file}")
        source_text = source_path.read_text(encoding=sidecar.get("source_text_encoding", "utf-8"))
        loaded_files.append(str(sidecar_path))
        base = {
            "document_id": str(sidecar["document_id"]),
            "domain": str(sidecar["domain"]),
            "source_file": source_file,
        }

        for raw in sidecar.get("labels", []):
            label = {**base, **raw}
            label["start"] = as_int(label["start"], f"{label['label_id']}.start")
            label["end"] = as_int(label["end"], f"{label['label_id']}.end")
            label["normalization_profile"] = str(label.get("normalization_profile", "exact"))
            label["acceptable_entity_mappings"] = list(label.get("acceptable_entity_mappings", []))
            label["required"] = bool(label.get("required", True))
            validate_span(source_text, str(label["text"]), label["start"], label["end"], f"{sidecar_path}:{label['label_id']}")
            labels.append(label)

        for raw in sidecar.get("preserve_terms", []):
            term = {**base, **raw}
            term["start"] = as_int(term["start"], f"{term['term_id']}.start")
            term["end"] = as_int(term["end"], f"{term['term_id']}.end")
            validate_span(source_text, str(term["term"]), term["start"], term["end"], f"{sidecar_path}:{term['term_id']}")
            preserve_terms.append(term)

        for raw in sidecar.get("known_traps", []):
            trap = {**base, **raw}
            trap["start"] = as_int(trap["start"], f"{trap['trap_id']}.start")
            trap["end"] = as_int(trap["end"], f"{trap['trap_id']}.end")
            trap["not_entity_class"] = list(trap.get("not_entity_class", []))
            validate_span(source_text, str(trap["text"]), trap["start"], trap["end"], f"{sidecar_path}:{trap['trap_id']}")
            known_traps.append(trap)

    return labels, preserve_terms, known_traps, warnings, loaded_files


def load_predictions(path: Path | None) -> tuple[list[dict[str, Any]], list[str]]:
    if path is None:
        return [], ["No predictions file supplied; reporting gold coverage with zero predictions."]
    data = read_json(path)
    predictions: list[dict[str, Any]] = []

    def add(raw: dict[str, Any], document_id: str | None = None, source_file: str | None = None) -> None:
        prediction = dict(raw)
        prediction["document_id"] = str(prediction.get("document_id") or document_id or "")
        prediction["entity_class"] = str(
            prediction.get("entity_class") or prediction.get("recognizer_label") or prediction.get("type") or ""
        )
        if not prediction["document_id"] or not prediction["entity_class"]:
            raise ValueError(f"Prediction lacks document_id or entity_class: {raw!r}")
        prediction["source_file"] = prediction.get("source_file") or source_file
        prediction["text"] = str(prediction.get("text", ""))
        prediction["start"] = as_int(prediction["start"], "prediction.start")
        prediction["end"] = as_int(prediction["end"], "prediction.end")
        predictions.append(prediction)

    if isinstance(data, list):
        for raw in data:
            add(raw)
    elif isinstance(data, dict) and "documents" in data:
        for document in data["documents"]:
            for raw in document.get("predictions", []):
                add(raw, document.get("document_id"), document.get("source_file"))
    elif isinstance(data, dict) and "predictions" in data:
        for raw in data["predictions"]:
            add(raw, data.get("document_id"), data.get("source_file"))
    else:
        raise ValueError(f"Unsupported predictions JSON shape in {path}")
    return predictions, []


def normalize_text(text: str, profile: str) -> str:
    value = text
    if profile in {"casefold", "iban_compact_uppercase"}:
        value = value.casefold()
    if profile in {
        "collapse_whitespace", "strip_outer_punctuation", "ignore_spaces_and_punctuation",
        "phone_digits_normalized", "iban_compact_uppercase",
    }:
        value = re.sub(r"\s+", " ", value.strip())
    if profile == "strip_outer_punctuation":
        return value.strip(string.punctuation + " \t\r\n'\"“”‘’.,;:")
    if profile == "ignore_spaces_and_punctuation":
        return "".join(char.casefold() for char in value if char.isalnum())
    if profile == "phone_digits_normalized":
        return "".join(char for char in value if char.isdigit())
    if profile == "iban_compact_uppercase":
        return "".join(char for char in value.upper() if char.isalnum())
    if profile == "date_string_exact":
        return value.strip()
    if profile == "casefold":
        return value.casefold()
    return value if profile == "collapse_whitespace" else text


def overlaps(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    return max(a_start, b_start) < min(a_end, b_end)


def prediction_matches_label_class(prediction: dict[str, Any], label: dict[str, Any]) -> bool:
    return prediction["entity_class"] == label["entity_class"] or prediction["entity_class"] in label.get("acceptable_entity_mappings", [])


def canonical_class_for_prediction(prediction: dict[str, Any], labels: list[dict[str, Any]]) -> str:
    if prediction["entity_class"] in ENTITY_CLASSES:
        return prediction["entity_class"]
    for label in labels:
        if prediction["document_id"] == label["document_id"] and prediction["entity_class"] in label.get("acceptable_entity_mappings", []):
            return label["entity_class"]
    return prediction["entity_class"]


def domain_for_prediction(prediction: dict[str, Any], labels: list[dict[str, Any]]) -> str:
    for label in labels:
        if label["document_id"] == prediction["document_id"]:
            return label["domain"]
    return "unknown"


def match_labels(labels: list[dict[str, Any]], predictions: list[dict[str, Any]], mode: str) -> tuple[set[str], set[int]]:
    matched_labels: set[str] = set()
    used_predictions: set[int] = set()
    for label in labels:
        for index, prediction in enumerate(predictions):
            if index in used_predictions or prediction["document_id"] != label["document_id"]:
                continue
            if not prediction_matches_label_class(prediction, label):
                continue
            if mode == "exact":
                is_match = prediction["start"] == label["start"] and prediction["end"] == label["end"]
            elif mode == "normalized":
                profile = label.get("normalization_profile", "exact")
                is_match = normalize_text(prediction["text"], profile) == normalize_text(label["text"], profile)
            else:
                raise ValueError(f"Unsupported match mode: {mode}")
            if is_match:
                matched_labels.add(label["label_id"])
                used_predictions.add(index)
                break
    return matched_labels, used_predictions


def ratio(numerator: int, denominator: int) -> float | None:
    return None if denominator == 0 else round(numerator / denominator, 6)


def empty_bucket() -> dict[str, Any]:
    return {
        "gold_count": 0, "prediction_count": 0,
        "true_positive_exact": 0, "true_positive_normalized": 0,
        "false_negative_exact": 0, "false_negative_normalized": 0,
        "false_positive_exact": 0, "false_positive_normalized": 0,
        "recall_exact": None, "recall_normalized": None,
        "precision_exact": None, "precision_normalized": None,
    }


def finalize(bucket: dict[str, Any]) -> dict[str, Any]:
    bucket["false_negative_exact"] = bucket["gold_count"] - bucket["true_positive_exact"]
    bucket["false_negative_normalized"] = bucket["gold_count"] - bucket["true_positive_normalized"]
    bucket["false_positive_exact"] = bucket["prediction_count"] - bucket["true_positive_exact"]
    bucket["false_positive_normalized"] = bucket["prediction_count"] - bucket["true_positive_normalized"]
    bucket["recall_exact"] = ratio(bucket["true_positive_exact"], bucket["gold_count"])
    bucket["recall_normalized"] = ratio(bucket["true_positive_normalized"], bucket["gold_count"])
    bucket["precision_exact"] = ratio(bucket["true_positive_exact"], bucket["prediction_count"])
    bucket["precision_normalized"] = ratio(bucket["true_positive_normalized"], bucket["prediction_count"])
    return bucket


def score_predictions(
    labels: list[dict[str, Any]],
    preserve_terms: list[dict[str, Any]],
    known_traps: list[dict[str, Any]],
    predictions: list[dict[str, Any]],
    warnings: list[str] | None = None,
    gold_files: list[str] | None = None,
    prediction_file: str | None = None,
) -> dict[str, Any]:
    required = [label for label in labels if label.get("required", True)]
    exact_label_ids, exact_prediction_ids = match_labels(required, predictions, "exact")
    normalized_label_ids, normalized_prediction_ids = match_labels(required, predictions, "normalized")
    labels_by_id = {label["label_id"]: label for label in required}

    by_entity = {entity_class: empty_bucket() for entity_class in ENTITY_CLASSES}
    by_domain: dict[str, dict[str, Any]] = defaultdict(empty_bucket)
    summary = empty_bucket()

    for label in required:
        by_entity[label["entity_class"]]["gold_count"] += 1
        by_domain[label["domain"]]["gold_count"] += 1
        summary["gold_count"] += 1
    for prediction in predictions:
        canonical = canonical_class_for_prediction(prediction, labels)
        if canonical in by_entity:
            by_entity[canonical]["prediction_count"] += 1
        by_domain[domain_for_prediction(prediction, labels)]["prediction_count"] += 1
        summary["prediction_count"] += 1

    exact_by_class = Counter(labels_by_id[label_id]["entity_class"] for label_id in exact_label_ids)
    norm_by_class = Counter(labels_by_id[label_id]["entity_class"] for label_id in normalized_label_ids)
    exact_by_domain = Counter(labels_by_id[label_id]["domain"] for label_id in exact_label_ids)
    norm_by_domain = Counter(labels_by_id[label_id]["domain"] for label_id in normalized_label_ids)

    for entity_class, bucket in by_entity.items():
        bucket["true_positive_exact"] = exact_by_class[entity_class]
        bucket["true_positive_normalized"] = norm_by_class[entity_class]
        finalize(bucket)
    for domain, bucket in by_domain.items():
        bucket["true_positive_exact"] = exact_by_domain[domain]
        bucket["true_positive_normalized"] = norm_by_domain[domain]
        finalize(bucket)
    summary["true_positive_exact"] = len(exact_label_ids)
    summary["true_positive_normalized"] = len(normalized_label_ids)
    finalize(summary)

    false_negatives = [
        {"document_id": label["document_id"], "label_id": label["label_id"], "entity_class": label["entity_class"],
         "expected_text": label["text"], "start": label["start"], "end": label["end"]}
        for label in required if label["label_id"] not in normalized_label_ids
    ]
    false_positives = [
        {"document_id": prediction["document_id"], "prediction_index": index, "entity_class": prediction["entity_class"],
         "text": prediction["text"], "start": prediction["start"], "end": prediction["end"]}
        for index, prediction in enumerate(predictions) if index not in normalized_prediction_ids
    ]
    partial_overlaps = [
        {"document_id": label["document_id"], "label_id": label["label_id"], "prediction_index": index,
         "entity_class": label["entity_class"], "gold_span": [label["start"], label["end"]],
         "prediction_span": [prediction["start"], prediction["end"]], "policy": "diagnostic_only"}
        for label in required
        for index, prediction in enumerate(predictions)
        if prediction["document_id"] == label["document_id"]
        and prediction_matches_label_class(prediction, label)
        and (prediction["start"], prediction["end"]) != (label["start"], label["end"])
        and overlaps(prediction["start"], prediction["end"], label["start"], label["end"])
    ]
    preserve_failures = [
        {"document_id": term["document_id"], "term_id": term["term_id"], "term": term["term"],
         "prediction_index": index, "prediction_entity_class": prediction["entity_class"],
         "reason": "prediction_overlaps_preserve_term"}
        for term in preserve_terms if term.get("expected_behavior") == "must_remain_readable"
        for index, prediction in enumerate(predictions)
        if prediction["document_id"] == term["document_id"]
        and overlaps(prediction["start"], prediction["end"], term["start"], term["end"])
    ]
    trap_failures = [
        {"document_id": trap["document_id"], "trap_id": trap["trap_id"], "trap_type": trap["trap_type"],
         "trap_text": trap["text"], "prediction_index": index, "prediction_entity_class": prediction["entity_class"],
         "reason": "prediction_overlaps_known_trap"}
        for trap in known_traps
        for index, prediction in enumerate(predictions)
        if prediction["document_id"] == trap["document_id"]
        and overlaps(prediction["start"], prediction["end"], trap["start"], trap["end"])
        and (trap.get("expected_behavior") == "must_not_match_as_sensitive_value" or prediction["entity_class"] in trap.get("not_entity_class", []))
    ]

    return {
        "schema_version": REPORT_SCHEMA_VERSION,
        "synthetic_only": True,
        "thresholds_applied": False,
        "gold_files": gold_files or [],
        "prediction_file": prediction_file,
        "warnings": warnings or [],
        "summary": summary,
        "by_domain": dict(sorted(by_domain.items())),
        "by_entity_class": by_entity,
        "false_negatives": false_negatives,
        "false_positives": false_positives,
        "preserve_term_failures": preserve_failures,
        "known_trap_failures": trap_failures,
        "partial_overlaps": partial_overlaps,
        "notes": [
            "WP22 runner is deterministic and local-only.",
            "No recognizer logic is executed; predictions must be supplied as JSON.",
            "Partial overlap is diagnostic-only and does not hide false negatives.",
            "No CI threshold or production gate is applied in WP22.",
        ],
    }


def run_benchmark(repo_root: Path, gold_path: Path, predictions_path: Path | None, include_schema_examples: bool = True) -> dict[str, Any]:
    labels, terms, traps, gold_warnings, gold_files = load_gold_sidecars(gold_path, repo_root, include_schema_examples)
    predictions, prediction_warnings = load_predictions(predictions_path)
    return score_predictions(labels, terms, traps, predictions, [*gold_warnings, *prediction_warnings], gold_files, str(predictions_path) if predictions_path else None)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run deterministic recall/precision scoring for synthetic gold-label sidecars.")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--gold", type=Path, default=DEFAULT_GOLD_DIR, help="Gold sidecar file or directory.")
    parser.add_argument("--predictions", type=Path, default=None, help="Optional prediction JSON file to score.")
    parser.add_argument("--output", type=Path, default=None, help="Optional JSON output path. Prints to stdout when omitted.")
    parser.add_argument("--only-complete", action="store_true", help="Skip schema_example_only sidecars.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    repo_root = args.repo_root.resolve()
    gold_path = args.gold if args.gold.is_absolute() else repo_root / args.gold
    predictions_path = None if args.predictions is None else (args.predictions if args.predictions.is_absolute() else repo_root / args.predictions)
    report = run_benchmark(repo_root, gold_path, predictions_path, include_schema_examples=not args.only_complete)
    output = json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True)
    if args.output:
        output_path = args.output if args.output.is_absolute() else repo_root / args.output
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
