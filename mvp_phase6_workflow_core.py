"""Pure synthetic workflow helpers for MVP Phase 6 validation."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable, Mapping

from document_tools import (
    apply_replacements_to_text,
    docx_from_text,
    pdf_from_text,
    scrub_report_txt,
    uploaded_file_to_text,
)
from manual_mask_entry import (
    build_manual_mask_row,
    build_manual_placeholder,
    validate_manual_mask_input,
)
from scrub_key import (
    build_scrub_key,
    scrub_key_from_json,
    scrub_key_to_json,
    validate_scrub_key,
)
from scrub_key_reinsert import reinsert_from_scrub_key

from mvp_phase6_detection_matrix import evaluate_detection


FIXED_BASELINE_TIMESTAMP = "2026-07-17T18:20:00Z"


class UploadedBytes:
    """Minimal upload object compatible with document_tools helpers."""

    def __init__(self, name: str, content: bytes):
        self.name = name
        self._content = bytes(content)

    def getvalue(self) -> bytes:
        return self._content


def build_review_rows(
    case: Mapping[str, Any],
    source_text: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows = [deepcopy(dict(row)) for row in case.get("review_rows", [])]
    manual_results: list[dict[str, Any]] = []

    for addition in case.get("manual_additions", []) or []:
        value = str(addition.get("value") or "")
        manual_type = str(addition.get("manual_type") or "Anders")
        validation = validate_manual_mask_input(
            value,
            source_text=source_text,
            existing_find_values=[str(row.get("find") or "") for row in rows],
        )
        result: dict[str, Any] = {
            "value": value,
            "manual_type": manual_type,
            "is_valid": validation.is_valid,
            "message": validation.message,
        }
        if validation.is_valid:
            placeholder = build_manual_placeholder(manual_type, rows)
            row = build_manual_mask_row(
                find_text=value,
                manual_type=manual_type,
                replace_with=placeholder,
                existing_rows=rows,
            )
            row["timestamp"] = str(
                addition.get("timestamp") or FIXED_BASELINE_TIMESTAMP
            )
            rows.append(row)
            result["placeholder"] = placeholder
        manual_results.append(result)

    return rows, manual_results


def replacement_map(rows: Iterable[Mapping[str, Any]]) -> dict[str, str]:
    replacements: dict[str, str] = {}
    for row in rows:
        if not row.get("include", True):
            continue
        original = str(row.get("find") or row.get("original_value") or "")
        placeholder = str(
            row.get("replace_with") or row.get("placeholder") or ""
        )
        if original and placeholder:
            replacements[original] = placeholder
    return replacements


def _scrub_report_rows(rows: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "entity_type": row.get("entity_type", "UNKNOWN"),
            "detected_text": row.get("find") or row.get("original_value") or "",
            "placeholder": row.get("replace_with") or row.get("placeholder") or "",
            "score": row.get("score"),
            "source": row.get("source", ""),
            "reason": row.get("reason", ""),
        }
        for row in rows
    ]


def build_common_evidence(
    case: Mapping[str, Any],
    source_text: str,
) -> dict[str, Any]:
    rows, manual_results = build_review_rows(case, source_text)
    replacements = replacement_map(rows)
    scrubbed_text = apply_replacements_to_text(source_text, replacements)

    scrub_key = build_scrub_key(
        rows,
        document_label=str(case.get("document_label") or case.get("id")),
    )
    scrub_key_json = scrub_key_to_json(scrub_key)
    loaded_scrub_key = scrub_key_from_json(scrub_key_json)
    key_issues = validate_scrub_key(loaded_scrub_key)
    reinsert_result = reinsert_from_scrub_key(scrubbed_text, loaded_scrub_key)
    report_text = scrub_report_txt(
        _scrub_report_rows(rows),
        profile="Dutch Legal Strict",
        source_filename=f"{case.get('id')}.{case.get('document_type')}",
    ).decode("utf-8")

    return {
        "rows": rows,
        "manual_additions": manual_results,
        "replacement_map": replacements,
        "scrubbed_text": scrubbed_text,
        "scrub_key": loaded_scrub_key,
        "scrub_key_validation_issues": key_issues,
        "reinsert": reinsert_result,
        "scrub_report_text": report_text,
    }


def run_txt_case(case: Mapping[str, Any]) -> dict[str, Any]:
    source_text = str(case.get("source_text") or "")
    imported_text, import_type = uploaded_file_to_text(
        UploadedBytes(f"{case['id']}.txt", source_text.encode("utf-8"))
    )
    detection = evaluate_detection(
        imported_text,
        expected_values=case.get("expected_detected_values"),
        preserved_terms=case.get("expected_preserved_terms"),
    )
    common = build_common_evidence(case, imported_text)

    scrubbed_docx = docx_from_text(common["scrubbed_text"])
    scrubbed_pdf = pdf_from_text(common["scrubbed_text"])
    docx_text, docx_type = uploaded_file_to_text(
        UploadedBytes("scrubbed.docx", scrubbed_docx)
    )
    pdf_text, pdf_type = uploaded_file_to_text(
        UploadedBytes("scrubbed.pdf", scrubbed_pdf)
    )

    manual_valid = all(
        item.get("is_valid") for item in common["manual_additions"]
    )
    roundtrip_exact = common["reinsert"]["text"] == imported_text
    placeholders = list(common["replacement_map"].values())
    export_placeholders_visible = all(
        placeholder in docx_text and placeholder in pdf_text
        for placeholder in placeholders
    )
    status = (
        "pass"
        if manual_valid
        and roundtrip_exact
        and export_placeholders_visible
        and not common["scrub_key_validation_issues"]
        else "fail"
    )

    return {
        "id": case["id"],
        "document_type": "txt",
        "status": status,
        "source_import_type": import_type,
        "detection": detection,
        "manual_additions": common["manual_additions"],
        "review_row_count": len(common["rows"]),
        "scrubbed_text": common["scrubbed_text"],
        "scrub_key_item_count": common["scrub_key"].get("item_count"),
        "scrub_key_validation_issues": common["scrub_key_validation_issues"],
        "reinsert_replacement_count": common["reinsert"].get("replacement_count"),
        "roundtrip_exact": roundtrip_exact,
        "export_import_types": [docx_type, pdf_type],
        "export_placeholders_visible": export_placeholders_visible,
        "scrub_report_requires_manual_review": (
            "Manual review recommended: yes" in common["scrub_report_text"]
        ),
        "known_limitations": [],
        "local_only": True,
        "ai_processing": False,
        "cloud_processing": False,
    }
