"""Synthetic detection evidence helpers for MVP Phase 6."""

from __future__ import annotations

import re
from typing import Any, Iterable, Mapping

from candidate_scanner import scan_unmasked_candidates
from dutch_recognizers import get_dutch_entity_names, get_dutch_recognizers


def normalise(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value or "").lower())


def _result_to_row(text: str, result: Any, source: str) -> dict[str, Any]:
    if isinstance(result, Mapping):
        start = result.get("start")
        end = result.get("end")
        detected_text = result.get("text")
        if not detected_text and isinstance(start, int) and isinstance(end, int):
            detected_text = text[start:end]
        return {
            "text": str(detected_text or ""),
            "entity_type": str(result.get("entity_type", "") or ""),
            "start": start,
            "end": end,
            "score": result.get("score"),
            "source": source,
        }

    start = getattr(result, "start", None)
    end = getattr(result, "end", None)
    detected_text = text[start:end] if isinstance(start, int) and isinstance(end, int) else ""
    return {
        "text": detected_text,
        "entity_type": str(getattr(result, "entity_type", "") or ""),
        "start": start,
        "end": end,
        "score": getattr(result, "score", None),
        "source": source,
    }


def detect_dutch_values(text: str) -> dict[str, Any]:
    entities = get_dutch_entity_names(include_legal=True)
    analyzer_results: list[Any] = []
    rows: list[dict[str, Any]] = []

    for recognizer in get_dutch_recognizers(supported_language="en"):
        recognizer_results = list(
            recognizer.analyze(text, entities=entities, nlp_artifacts=None)
        )
        analyzer_results.extend(recognizer_results)
        rows.extend(
            _result_to_row(text, result, recognizer.name)
            for result in recognizer_results
        )

    candidate_results = scan_unmasked_candidates(
        text,
        analyzer_results=analyzer_results,
    )
    rows.extend(
        _result_to_row(text, result, "candidate_scanner")
        for result in candidate_results
    )

    unique_rows: list[dict[str, Any]] = []
    seen: set[tuple[Any, ...]] = set()
    for row in rows:
        key = (
            row.get("start"),
            row.get("end"),
            row.get("entity_type"),
            row.get("text"),
        )
        if key in seen:
            continue
        seen.add(key)
        unique_rows.append(row)

    return {
        "rows": unique_rows,
        "analyzer_result_count": len(analyzer_results),
        "candidate_result_count": len(candidate_results),
        "local_only": True,
        "ai_processing": False,
        "cloud_processing": False,
    }


def evaluate_detection(
    text: str,
    expected_values: Iterable[str] | None = None,
    preserved_terms: Iterable[str] | None = None,
) -> dict[str, Any]:
    detection = detect_dutch_values(text)
    rows = list(detection["rows"])
    detected_blob = "\n".join(
        normalise(row.get("text")) for row in rows if row.get("text")
    )
    expected = [str(value) for value in (expected_values or [])]
    missing = [value for value in expected if normalise(value) not in detected_blob]

    spans: list[tuple[int, int]] = []
    for row in rows:
        start = row.get("start")
        end = row.get("end")
        if isinstance(start, int) and isinstance(end, int) and 0 <= start < end <= len(text):
            spans.append((start, end))
    masked = text
    for start, end in sorted(set(spans), reverse=True):
        masked = masked[:start] + "[MASK]" + masked[end:]

    preserved = [str(term) for term in (preserved_terms or [])]
    removed_terms = [term for term in preserved if term.lower() not in masked.lower()]

    return {
        **detection,
        "expected_values": expected,
        "missing_expected_values": missing,
        "preserved_terms": preserved,
        "removed_preserved_terms": removed_terms,
        "detection_expectations_met": not missing,
        "context_preservation_met": not removed_terms,
    }
