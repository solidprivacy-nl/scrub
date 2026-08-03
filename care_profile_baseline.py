"""Current deterministic recognizer baseline for the synthetic care corpus.

This baseline intentionally uses the recognizers that exist before the dedicated
Zorgfilter recognizer package. It records evidence and never claims production
readiness. Generic NER-model results are outside this pure baseline.
"""

from __future__ import annotations

import re
from typing import Any, Dict, Iterable, List, Sequence

from care_test_examples import TEST_CASES


def _normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value or "").lower())


def _result_row(text: str, result: Any, recognizer_name: str) -> Dict[str, Any]:
    start = getattr(result, "start", None)
    end = getattr(result, "end", None)
    detected_text = ""
    if isinstance(start, int) and isinstance(end, int) and 0 <= start < end <= len(text):
        detected_text = text[start:end]
    return {
        "text": detected_text,
        "entity_type": str(getattr(result, "entity_type", "") or ""),
        "start": start,
        "end": end,
        "score": float(getattr(result, "score", 0.0) or 0.0),
        "recognizer": recognizer_name,
    }


def detect_with_current_custom_recognizers(text: str) -> List[Dict[str, Any]]:
    """Run the current Dutch custom recognizers without a generic NER model."""

    from dutch_recognizers import get_dutch_entity_names, get_dutch_recognizers

    entities = get_dutch_entity_names(include_legal=True)
    rows: List[Dict[str, Any]] = []
    for recognizer in get_dutch_recognizers(supported_language="en"):
        results = recognizer.analyze(text, entities=entities, nlp_artifacts=None)
        rows.extend(_result_row(text, result, recognizer.name) for result in results)
    rows.sort(key=lambda row: (row.get("start", -1), row.get("end", -1), row.get("entity_type", "")))
    return rows


def _matching_rows(value: str, rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    needle = _normalize(value)
    if not needle:
        return []
    return [row for row in rows if needle in _normalize(row.get("text", ""))]


def _phrase_spans(text: str, phrase: str) -> List[tuple[int, int]]:
    spans: List[tuple[int, int]] = []
    start = 0
    while True:
        index = text.find(phrase, start)
        if index < 0:
            return spans
        spans.append((index, index + len(phrase)))
        start = index + max(1, len(phrase))


def _spans_overlap(first: tuple[int, int], second: tuple[int, int]) -> bool:
    return first[0] < second[1] and second[0] < first[1]


def _preserve_overlaps(
    text: str,
    preserve_phrases: Iterable[str],
    rows: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    overlaps: List[Dict[str, Any]] = []
    detected_spans = [
        (int(row["start"]), int(row["end"]), row)
        for row in rows
        if isinstance(row.get("start"), int) and isinstance(row.get("end"), int)
    ]
    for phrase in preserve_phrases:
        for phrase_span in _phrase_spans(text, phrase):
            for start, end, row in detected_spans:
                if _spans_overlap(phrase_span, (start, end)):
                    overlaps.append(
                        {
                            "preserve_phrase": phrase,
                            "detected_text": row.get("text", ""),
                            "entity_type": row.get("entity_type", ""),
                            "recognizer": row.get("recognizer", ""),
                        }
                    )
    return overlaps


def build_current_care_baseline(
    cases: Sequence[Dict[str, Any]] = TEST_CASES,
) -> Dict[str, Any]:
    """Build a deterministic evidence report for the pre-Zorgfilter recognizers."""

    case_reports: List[Dict[str, Any]] = []
    total_expected = 0
    total_found = 0
    total_preserve_overlaps = 0

    for case in cases:
        text = str(case["text"])
        rows = detect_with_current_custom_recognizers(text)
        expectations: List[Dict[str, Any]] = []
        for policy_bucket in ("replace", "review_selected"):
            for item in case.get(policy_bucket, []):
                value = str(item["value"])
                matches = _matching_rows(value, rows)
                total_expected += 1
                if matches:
                    total_found += 1
                expectations.append(
                    {
                        "value": value,
                        "expected_entity_type": str(item["entity_type"]),
                        "policy_bucket": policy_bucket,
                        "found": bool(matches),
                        "detected_entity_types": sorted(
                            {str(row.get("entity_type", "")) for row in matches}
                        ),
                        "detected_spans": [str(row.get("text", "")) for row in matches],
                    }
                )

        preserve_overlaps = _preserve_overlaps(text, case.get("preserve", []), rows)
        total_preserve_overlaps += len(preserve_overlaps)
        case_reports.append(
            {
                "id": case["id"],
                "name": case["name"],
                "sector": case["sector"],
                "document_type": case["document_type"],
                "expected_value_count": len(expectations),
                "found_value_count": sum(1 for item in expectations if item["found"]),
                "expectations": expectations,
                "preserve_overlaps": preserve_overlaps,
                "detected_rows": rows,
            }
        )

    recall = (total_found / total_expected) if total_expected else 0.0
    return {
        "schema_version": "1.0",
        "profile": "current_custom_recognizers_before_care_profile",
        "scope": "deterministic Dutch custom recognizers only; generic NER excluded",
        "synthetic_data_only": True,
        "production_ready": False,
        "human_review_required": True,
        "case_count": len(case_reports),
        "expected_value_count": total_expected,
        "found_value_count": total_found,
        "indicative_recall": round(recall, 6),
        "preserve_overlap_count": total_preserve_overlaps,
        "cases": case_reports,
    }
