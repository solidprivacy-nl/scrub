from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable, Iterable, Sequence


ENTITY_TYPE_TO_BENCHMARK_CLASS = {
    "PERSON": "PERSON",
    "EMAIL_ADDRESS": "EMAIL",
    "PHONE_NUMBER": "PHONE",
    "NL_PHONE_NUMBER": "PHONE",
    "IBAN_CODE": "IBAN",
    "IBAN": "IBAN",
    "NL_BSN": "BSN",
    "BSN": "BSN",
    "NL_POSTCODE": "NL_POSTCODE",
    "NL_LEGAL_CASE_NUMBER": "CASE_NUMBER",
    "NL_ROLNUMMER": "CASE_NUMBER",
    "NL_REKESTNUMMER": "CASE_NUMBER",
    "NL_PARKETNUMMER": "CASE_NUMBER",
    "NL_DOSSIER_NUMBER": "DOSSIER_NUMBER",
    "NL_CLIENT_REFERENCE": "CLIENT_NUMBER",
    "NL_CLIENT_NUMBER": "CLIENT_NUMBER",
    "NL_CLAIM_NUMBER": "CLAIM_NUMBER",
    "NL_INSURANCE_CLAIM_NUMBER": "CLAIM_NUMBER",
    "NL_INCIDENT_NUMBER": "INCIDENT_NUMBER",
    "NL_ECLI": "ECLI",
    "ECLI": "ECLI",
    "NL_HEALTHCARE_REFERENCE": "MEDICAL_OR_CARE_REFERENCE",
    "NL_BIG_NUMBER": "MEDICAL_OR_CARE_REFERENCE",
    # Ambiguous review-candidate class. A gold label's acceptable_entity_types is
    # still authoritative for whether this is accepted for that specific label.
    "NL_SUSPICIOUS_REFERENCE_CANDIDATE": "CASE_NUMBER",
}

SUMMARY_FIELDS = [
    "document_count",
    "gold_label_count",
    "prediction_count",
    "required_label_count",
    "matched_required_exact_count",
    "matched_required_text_normalized_count",
    "matched_required_overlap_count",
    "missed_required_count",
    "wrong_type_count",
    "false_positive_candidate_count",
    "preserve_term_hit_count",
    "known_trap_hit_count",
]


def normalize_value(value: str) -> str:
    """Return a value-normalized form for diagnostic matching."""

    return re.sub(r"[^a-z0-9]+", "", (value or "").lower().strip())


def spans_overlap(left_start: int, left_end: int, right_start: int, right_end: int) -> bool:
    return left_start < right_end and left_end > right_start


@dataclass(frozen=True)
class GoldLabel:
    id: str
    entity_class: str
    text: str
    start: int
    end: int
    sensitivity: str
    required: bool
    acceptable_entity_types: tuple[str, ...] = field(default_factory=tuple)
    notes: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> "GoldLabel":
        return cls(
            id=str(data["id"]),
            entity_class=str(data["entity_class"]),
            text=str(data["text"]),
            start=int(data["start"]),
            end=int(data["end"]),
            sensitivity=str(data["sensitivity"]),
            required=bool(data["required"]),
            acceptable_entity_types=tuple(str(item) for item in data.get("acceptable_entity_types", [])),
            notes=str(data.get("notes", "")),
        )


@dataclass(frozen=True)
class PreserveTerm:
    term: str
    start: int
    end: int
    reason: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> "PreserveTerm":
        return cls(
            term=str(data["term"]),
            start=int(data["start"]),
            end=int(data["end"]),
            reason=str(data.get("reason", "")),
        )


@dataclass(frozen=True)
class KnownTrap:
    text: str
    trap_type: str
    notes: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> "KnownTrap":
        return cls(
            text=str(data["text"]),
            trap_type=str(data.get("trap_type", "unknown_trap")),
            notes=str(data.get("notes", "")),
        )


@dataclass(frozen=True)
class GoldDocument:
    document_id: str
    domain: str
    document_type: str
    language: str
    source_file: str
    source_text: str
    labels: tuple[GoldLabel, ...]
    preserve_terms: tuple[PreserveTerm, ...]
    known_traps: tuple[KnownTrap, ...]


@dataclass(frozen=True)
class Prediction:
    text: str
    entity_type: str
    start: int
    end: int
    source: str
    score: float | None = None
    benchmark_class: str | None = None

    @classmethod
    def from_result(cls, source_text: str, result, source: str) -> "Prediction | None":
        if isinstance(result, dict):
            start = result.get("start")
            end = result.get("end")
            entity_type = str(result.get("entity_type", ""))
            text = str(result.get("text", ""))
            score = result.get("score")
        else:
            start = getattr(result, "start", None)
            end = getattr(result, "end", None)
            entity_type = str(getattr(result, "entity_type", "") or "")
            text = source_text[start:end] if isinstance(start, int) and isinstance(end, int) else ""
            score = getattr(result, "score", None)

        if not isinstance(start, int) or not isinstance(end, int) or start < 0 or end <= start or end > len(source_text):
            return None

        if not text:
            text = source_text[start:end]

        return cls(
            text=text,
            entity_type=entity_type,
            start=start,
            end=end,
            source=source,
            score=float(score) if isinstance(score, (int, float)) else None,
            benchmark_class=ENTITY_TYPE_TO_BENCHMARK_CLASS.get(entity_type),
        )


def _repo_root_from_corpus(corpus_root: Path) -> Path:
    return corpus_root if corpus_root.name != "corpus" else corpus_root.parent


def _validate_span(source_text: str, text: str, start: int, end: int, item: str) -> None:
    actual = source_text[start:end]
    if actual != text:
        raise ValueError(f"{item} offset mismatch: expected {text!r}, got {actual!r} at {start}:{end}")


def load_gold_documents(corpus_root: str | Path = "corpus") -> list[GoldDocument]:
    """Load all gold sidecars and validate basic source/offset integrity."""

    corpus_path = Path(corpus_root)
    repo_root = _repo_root_from_corpus(corpus_path)
    documents: list[GoldDocument] = []

    for sidecar_path in sorted(corpus_path.glob("**/*.gold.json")):
        data = json.loads(sidecar_path.read_text(encoding="utf-8"))
        if data.get("synthetic") is not True:
            raise ValueError(f"Sidecar must be synthetic: {sidecar_path}")

        source_file = repo_root / str(data["source_file"])
        source_text = source_file.read_text(encoding="utf-8")
        labels = tuple(GoldLabel.from_dict(item) for item in data.get("labels", []))
        preserve_terms = tuple(PreserveTerm.from_dict(item) for item in data.get("preserve_terms", []))
        known_traps = tuple(KnownTrap.from_dict(item) for item in data.get("known_traps", []))

        for label in labels:
            _validate_span(source_text, label.text, label.start, label.end, f"{sidecar_path}:{label.id}")
        for preserve_term in preserve_terms:
            _validate_span(source_text, preserve_term.term, preserve_term.start, preserve_term.end, f"{sidecar_path}:{preserve_term.term}")

        documents.append(
            GoldDocument(
                document_id=str(data["document_id"]),
                domain=str(data["domain"]),
                document_type=str(data.get("document_type", "")),
                language=str(data.get("language", "")),
                source_file=str(data["source_file"]),
                source_text=source_text,
                labels=labels,
                preserve_terms=preserve_terms,
                known_traps=known_traps,
            )
        )

    return documents


def collect_predictions(source_text: str) -> list[Prediction]:
    """Collect recognizer and candidate-scanner predictions without starting the app.

    Missing optional dependencies are treated as diagnostic absence, not as a
    product error, so the runner can still load corpus and produce a report in
    minimal CI environments.
    """

    raw_recognizer_results = []
    predictions: list[Prediction] = []

    try:
        from dutch_recognizers import get_dutch_entity_names, get_dutch_recognizers

        entities = get_dutch_entity_names(include_legal=True)
        for recognizer in get_dutch_recognizers(supported_language="en"):
            try:
                recognizer_results = list(recognizer.analyze(source_text, entities=entities, nlp_artifacts=None))
            except Exception:
                continue
            raw_recognizer_results.extend(recognizer_results)
            for result in recognizer_results:
                prediction = Prediction.from_result(source_text, result, source="recognizer")
                if prediction is not None:
                    predictions.append(prediction)
    except Exception:
        raw_recognizer_results = []

    try:
        from candidate_scanner import scan_unmasked_candidates

        for result in scan_unmasked_candidates(source_text, analyzer_results=raw_recognizer_results):
            prediction = Prediction.from_result(source_text, result, source="candidate_scanner")
            if prediction is not None:
                predictions.append(prediction)
    except Exception:
        pass

    return sorted(predictions, key=lambda item: (item.start, item.end, item.entity_type, item.source))


def _prediction_matches_type(label: GoldLabel, prediction: Prediction) -> bool:
    if prediction.entity_type in label.acceptable_entity_types:
        return True
    mapped_class = prediction.benchmark_class or ENTITY_TYPE_TO_BENCHMARK_CLASS.get(prediction.entity_type)
    return mapped_class == label.entity_class


def _prediction_to_dict(prediction: Prediction) -> dict:
    return asdict(prediction)


def _label_to_dict(label: GoldLabel) -> dict:
    data = asdict(label)
    data["acceptable_entity_types"] = list(label.acceptable_entity_types)
    return data


def _match_record(label: GoldLabel, prediction: Prediction, match_type: str) -> dict:
    return {
        "match_type": match_type,
        "label": _label_to_dict(label),
        "prediction": _prediction_to_dict(prediction),
    }


def _trap_spans(source_text: str, trap: KnownTrap) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    start = 0
    while True:
        idx = source_text.find(trap.text, start)
        if idx == -1:
            break
        spans.append((idx, idx + len(trap.text)))
        start = idx + max(1, len(trap.text))
    return spans


def compare_document(document: GoldDocument, predictions: Sequence[Prediction]) -> dict:
    matched_exact: list[dict] = []
    matched_text_normalized: list[dict] = []
    matched_overlap: list[dict] = []
    missed_required: list[dict] = []
    wrong_type: list[dict] = []
    used_prediction_indices: set[int] = set()

    for label in document.labels:
        exact_candidates = [
            (index, prediction)
            for index, prediction in enumerate(predictions)
            if prediction.start == label.start and prediction.end == label.end
        ]
        normalized_candidates = [
            (index, prediction)
            for index, prediction in enumerate(predictions)
            if normalize_value(prediction.text) == normalize_value(label.text)
        ]
        overlap_candidates = [
            (index, prediction)
            for index, prediction in enumerate(predictions)
            if spans_overlap(prediction.start, prediction.end, label.start, label.end)
        ]

        exact_match = next(((i, p) for i, p in exact_candidates if _prediction_matches_type(label, p)), None)
        normalized_match = next(((i, p) for i, p in normalized_candidates if _prediction_matches_type(label, p)), None)
        overlap_match = next(((i, p) for i, p in overlap_candidates if _prediction_matches_type(label, p)), None)

        if exact_match is not None:
            used_prediction_indices.add(exact_match[0])
            matched_exact.append(_match_record(label, exact_match[1], "exact"))
        if normalized_match is not None:
            used_prediction_indices.add(normalized_match[0])
            matched_text_normalized.append(_match_record(label, normalized_match[1], "text_normalized"))
        if overlap_match is not None:
            used_prediction_indices.add(overlap_match[0])
            matched_overlap.append(_match_record(label, overlap_match[1], "overlap"))

        wrong_type_candidates = [
            (index, prediction)
            for index, prediction in (exact_candidates + normalized_candidates + overlap_candidates)
            if not _prediction_matches_type(label, prediction)
        ]
        if wrong_type_candidates and exact_match is None and normalized_match is None and overlap_match is None:
            wrong_type.append(
                {
                    "label": _label_to_dict(label),
                    "predictions": [_prediction_to_dict(prediction) for _, prediction in wrong_type_candidates],
                }
            )
            used_prediction_indices.update(index for index, _ in wrong_type_candidates)

        if label.required and exact_match is None and normalized_match is None and overlap_match is None:
            missed_required.append(_label_to_dict(label))

    preserve_term_hits = []
    for preserve_term in document.preserve_terms:
        hits = [
            prediction
            for prediction in predictions
            if spans_overlap(prediction.start, prediction.end, preserve_term.start, preserve_term.end)
        ]
        for prediction in hits:
            preserve_term_hits.append({"preserve_term": asdict(preserve_term), "prediction": _prediction_to_dict(prediction)})

    known_trap_hits = []
    for trap in document.known_traps:
        for start, end in _trap_spans(document.source_text, trap):
            for prediction in predictions:
                if spans_overlap(prediction.start, prediction.end, start, end):
                    known_trap_hits.append(
                        {
                            "known_trap": asdict(trap),
                            "trap_span": {"start": start, "end": end},
                            "prediction": _prediction_to_dict(prediction),
                        }
                    )

    false_positive_candidates = [
        _prediction_to_dict(prediction)
        for index, prediction in enumerate(predictions)
        if index not in used_prediction_indices
    ]

    return {
        "document_id": document.document_id,
        "source_file": document.source_file,
        "domain": document.domain,
        "gold_label_count": len(document.labels),
        "prediction_count": len(predictions),
        "matched_exact": matched_exact,
        "matched_text_normalized": matched_text_normalized,
        "matched_overlap": matched_overlap,
        "missed_required": missed_required,
        "wrong_type": wrong_type,
        "false_positive_candidates": false_positive_candidates,
        "preserve_term_hits": preserve_term_hits,
        "known_trap_hits": known_trap_hits,
    }


def summarize_documents(document_reports: Sequence[dict]) -> dict:
    summary = {field: 0 for field in SUMMARY_FIELDS}
    summary["document_count"] = len(document_reports)

    for report in document_reports:
        summary["gold_label_count"] += int(report["gold_label_count"])
        summary["prediction_count"] += int(report["prediction_count"])
        required_count = int(report["gold_label_count"]) - sum(1 for item in report["missed_required"] if not item.get("required", True))
        summary["required_label_count"] += required_count
        summary["matched_required_exact_count"] += len(report["matched_exact"])
        summary["matched_required_text_normalized_count"] += len(report["matched_text_normalized"])
        summary["matched_required_overlap_count"] += len(report["matched_overlap"])
        summary["missed_required_count"] += len(report["missed_required"])
        summary["wrong_type_count"] += len(report["wrong_type"])
        summary["false_positive_candidate_count"] += len(report["false_positive_candidates"])
        summary["preserve_term_hit_count"] += len(report["preserve_term_hits"])
        summary["known_trap_hit_count"] += len(report["known_trap_hits"])

    return summary


def run_benchmark(
    corpus_root: str | Path = "corpus",
    prediction_provider: Callable[[str], Iterable[Prediction]] | None = None,
) -> dict:
    documents = load_gold_documents(corpus_root)
    provider = prediction_provider or collect_predictions
    reports = []

    for document in documents:
        predictions = list(provider(document.source_text))
        reports.append(compare_document(document, predictions))

    return {"documents": reports, "summary": summarize_documents(reports)}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the diagnostic recall benchmark against the synthetic gold-label corpus.")
    parser.add_argument("--corpus", default="corpus", help="Corpus root containing .gold.json sidecars.")
    parser.add_argument("--json", action="store_true", help="Print JSON report to stdout.")
    args = parser.parse_args(argv)

    report = run_benchmark(args.corpus)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        summary = report["summary"]
        print("Diagnostic recall benchmark summary")
        for field in SUMMARY_FIELDS:
            print(f"{field}: {summary[field]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
