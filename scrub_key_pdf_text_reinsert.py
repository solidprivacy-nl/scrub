"""Pure text-based PDF Scrub Key reinsert helpers.

This helper spike supports local text extraction from text-based PDFs only.
It deliberately does not perform OCR, reconstruct PDF output, call AI services,
use cloud processing, write files, change UI behavior, or change export semantics.

Dependency decision:
- Uses pypdf for local PDF text extraction when the dependency is installed.
- pypdf is a Python PDF parser/reader dependency and does not require OCR,
  external services, AI calls, or PDF-to-DOCX reconstruction.
- The module remains import-safe when pypdf is unavailable, because GitHub
  Actions may not install project requirements in every test job.
- Extraction is deterministic for a given parser/input, but PDF text order and
  completeness are not guaranteed. Callers must surface limitations clearly.
"""

from __future__ import annotations

from io import BytesIO
from typing import Any

try:  # Keep module import-safe when optional dependency is absent in CI.
    from pypdf import PdfReader
except ImportError as exc:  # pragma: no cover - exercised by monkeypatch tests.
    PdfReader = None  # type: ignore[assignment]
    PYPDF_IMPORT_ERROR: Exception | None = exc
else:
    PYPDF_IMPORT_ERROR = None

from scrub_key_document_reinsert import reinsert_text_document

PDF_TEXT_LIMITATIONS = [
    "PDF text extraction is limited to existing selectable text layers.",
    "Scanned or image-only PDFs are unsupported because OCR is not used.",
    "Formatting, layout, tables, headers, footers and reading order are not guaranteed.",
    "Restored output is TXT/text only; no restored PDF output is produced.",
]

UNSUPPORTED_NO_TEXT_REASON = "Geen bruikbare tekstlaag gevonden. OCR is niet ondersteund in deze versie."
PYPDF_MISSING_REASON = "pypdf is niet geïnstalleerd. Installeer requirements.txt om lokale PDF-tekstextractie te gebruiken."


def _base_result() -> dict[str, Any]:
    return {
        "document_type": "pdf_text",
        "extracted_text": "",
        "restored_text": "",
        "text": "",
        "content": "",
        "content_bytes": b"",
        "replacement_count": 0,
        "item_count": 0,
        "active_item_count": 0,
        "excluded_item_count": 0,
        "placeholders_not_found": [],
        "unknown_placeholders": [],
        "duplicate_placeholders": [],
        "validation_issues": [],
        "unsupported_reason": None,
        "extraction_warnings": [],
        "limitations": list(PDF_TEXT_LIMITATIONS),
        "local_only": True,
        "ai_processing": False,
        "cloud_processing": False,
        "ocr_used": False,
        "pdf_output": False,
    }


def _validation_result(message: str, unsupported_reason: str | None = None) -> dict[str, Any]:
    result = _base_result()
    result["validation_issues"] = [message] if message else []
    result["unsupported_reason"] = unsupported_reason
    return result


def extract_text_from_pdf_bytes(content: bytes) -> dict[str, Any]:
    """Extract selectable text from PDF bytes using local parsing only.

    The function does not perform OCR and does not write files. A successful
    result only means that a selectable text layer was extracted; it does not
    guarantee layout fidelity, complete extraction or correct reading order.
    """
    if not isinstance(content, (bytes, bytearray)):
        return _validation_result("PDF content must be bytes.")

    if PdfReader is None:
        reason = PYPDF_MISSING_REASON
        if PYPDF_IMPORT_ERROR is not None:
            reason = f"{reason} Importfout: {PYPDF_IMPORT_ERROR}"
        return _validation_result(reason)

    raw_content = bytes(content)
    try:
        reader = PdfReader(BytesIO(raw_content))
    except Exception as exc:  # pypdf exposes multiple parser exceptions.
        return _validation_result(f"PDF content could not be parsed: {exc}")

    page_texts: list[str] = []
    extraction_warnings: list[str] = []

    for page_index, page in enumerate(reader.pages, start=1):
        try:
            page_text = page.extract_text() or ""
        except Exception as exc:  # keep extraction failure explicit and local.
            page_text = ""
            extraction_warnings.append(f"Page {page_index} text extraction failed: {exc}")
        page_texts.append(page_text)

    extracted_text = "\n".join(page_texts).strip()

    result = _base_result()
    result["page_count"] = len(reader.pages)
    result["extracted_text"] = extracted_text
    result["text"] = extracted_text
    result["content"] = extracted_text
    result["content_bytes"] = extracted_text.encode("utf-8")
    result["extraction_warnings"] = extraction_warnings

    if not extracted_text:
        result["unsupported_reason"] = UNSUPPORTED_NO_TEXT_REASON
        result["extraction_warnings"] = extraction_warnings + [UNSUPPORTED_NO_TEXT_REASON]

    return result


def reinsert_pdf_text_bytes(content: bytes, scrub_key: dict[str, Any]) -> dict[str, Any]:
    """Extract text from PDF bytes and reinsert Scrub Key values into TXT output.

    This function returns restored text/TXT fields only. It never creates restored
    PDF bytes and never performs OCR.
    """
    extraction_result = extract_text_from_pdf_bytes(content)

    if extraction_result.get("validation_issues") or extraction_result.get("unsupported_reason"):
        return {
            **_base_result(),
            "page_count": extraction_result.get("page_count", 0),
            "extracted_text": extraction_result.get("extracted_text", ""),
            "text": "",
            "content": "",
            "content_bytes": b"",
            "validation_issues": list(extraction_result.get("validation_issues", [])),
            "unsupported_reason": extraction_result.get("unsupported_reason"),
            "extraction_warnings": list(extraction_result.get("extraction_warnings", [])),
        }

    extracted_text = str(extraction_result.get("extracted_text", ""))
    text_result = reinsert_text_document(extracted_text, scrub_key)
    restored_text = str(text_result.get("text", ""))

    return {
        **dict(text_result),
        "document_type": "pdf_text",
        "extracted_text": extracted_text,
        "restored_text": restored_text,
        "text": restored_text,
        "content": restored_text,
        "content_bytes": restored_text.encode("utf-8"),
        "page_count": extraction_result.get("page_count", 0),
        "unsupported_reason": None,
        "extraction_warnings": list(extraction_result.get("extraction_warnings", [])),
        "limitations": list(PDF_TEXT_LIMITATIONS),
        "local_only": True,
        "ai_processing": False,
        "cloud_processing": False,
        "ocr_used": False,
        "pdf_output": False,
    }
