from __future__ import annotations

from copy import deepcopy
from io import BytesIO

import pytest

from scrub_key import build_scrub_key
import scrub_key_pdf_text_reinsert as pdf_reinsert
from scrub_key_pdf_text_reinsert import (
    PDF_TEXT_LIMITATIONS,
    PYPDF_MISSING_REASON,
    UNSUPPORTED_NO_TEXT_REASON,
    extract_text_from_pdf_bytes,
    reinsert_pdf_text_bytes,
)

pypdf = pytest.importorskip("pypdf", reason="pypdf is required for PDF text extraction tests")
PdfWriter = pypdf.PdfWriter


VALID_SYNTHETIC_ROWS = [
    {
        "original_value": "BETROKKENE-TEST-A",
        "placeholder": "[PERSOON_1]",
        "entity_type": "PERSON",
        "type_label": "Naam",
        "source": "detected",
        "review_status": "auto_detected",
        "include": True,
        "timestamp": "2026-06-09T10:00:00Z",
    },
    {
        "original_value": "ZAAK-TEST-2026-001",
        "placeholder": "[ZAAKNUMMER_1]",
        "entity_type": "LEGAL_REFERENCE",
        "type_label": "Zaaknummer",
        "source": "manual",
        "review_status": "manual",
        "include": True,
        "timestamp": "2026-06-09T10:05:00Z",
    },
    {
        "original_value": "RECHTBANK TESTDAM",
        "placeholder": "[ORGANISATIE_01]",
        "entity_type": "ORGANIZATION",
        "type_label": "Organisatie",
        "source": "detected",
        "review_status": "auto_detected",
        "include": True,
        "timestamp": "2026-06-09T10:10:00Z",
    },
]


def _valid_scrub_key():
    return build_scrub_key(VALID_SYNTHETIC_ROWS, document_label="PDF text reinsert testdossier")


def _minimal_text_pdf(text: str) -> bytes:
    encoded_text = (
        text.replace("\\", "\\\\")
        .replace("(", "\\(")
        .replace(")", "\\)")
        .encode("latin-1")
    )
    stream = b"BT /F1 12 Tf 72 720 Td (" + encoded_text + b") Tj ET"
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"\nendstream",
    ]

    pdf = b"%PDF-1.4\n"
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf += f"{index} 0 obj\n".encode("ascii") + obj + b"\nendobj\n"

    xref_offset = len(pdf)
    pdf += f"xref\n0 {len(objects) + 1}\n".encode("ascii")
    pdf += b"0000000000 65535 f \n"
    for offset in offsets[1:]:
        pdf += f"{offset:010d} 00000 n \n".encode("ascii")
    pdf += (
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref_offset}\n%%EOF\n"
    ).encode("ascii")
    return pdf


def _blank_pdf() -> bytes:
    output = BytesIO()
    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)
    writer.write(output)
    return output.getvalue()


def test_extract_text_from_text_based_pdf():
    result = extract_text_from_pdf_bytes(_minimal_text_pdf("Zaak [ZAAKNUMMER_1]."))

    assert result["document_type"] == "pdf_text"
    assert "Zaak [ZAAKNUMMER_1]." in result["extracted_text"]
    assert result["unsupported_reason"] is None
    assert result["ocr_used"] is False
    assert result["pdf_output"] is False


def test_text_based_pdf_with_one_placeholder_reinserts_to_txt_only():
    result = reinsert_pdf_text_bytes(_minimal_text_pdf("Verzoeker [PERSOON_1]."), _valid_scrub_key())

    assert result["restored_text"] == "Verzoeker BETROKKENE-TEST-A."
    assert result["text"] == result["restored_text"]
    assert result["content"] == result["restored_text"]
    assert result["content_bytes"] == result["restored_text"].encode("utf-8")
    assert result["replacement_count"] == 1
    assert result["document_type"] == "pdf_text"
    assert result["pdf_output"] is False
    assert "pdf_bytes" not in result


def test_text_based_pdf_with_multiple_placeholders():
    result = reinsert_pdf_text_bytes(
        _minimal_text_pdf("[PERSOON_1] heeft zaak [ZAAKNUMMER_1] bij [ORGANISATIE_01]."),
        _valid_scrub_key(),
    )

    assert result["restored_text"] == (
        "BETROKKENE-TEST-A heeft zaak ZAAK-TEST-2026-001 bij RECHTBANK TESTDAM."
    )
    assert result["replacement_count"] == 3
    assert result["placeholders_not_found"] == []


def test_extracted_text_feeds_existing_deterministic_reinsert():
    result = reinsert_pdf_text_bytes(_minimal_text_pdf("[PERSOON_1] [PERSOON_1]"), _valid_scrub_key())

    assert result["restored_text"] == "BETROKKENE-TEST-A BETROKKENE-TEST-A"
    assert result["replacement_count"] == 2


def test_unknown_placeholder_remains_unchanged_and_is_reported():
    result = reinsert_pdf_text_bytes(
        _minimal_text_pdf("Bekend [PERSOON_1], onbekend [ONBEKEND_1]."),
        _valid_scrub_key(),
    )

    assert "BETROKKENE-TEST-A" in result["restored_text"]
    assert "[ONBEKEND_1]" in result["restored_text"]
    assert result["unknown_placeholders"] == ["[ONBEKEND_1]"]
    assert result["replacement_count"] == 1


def test_mapped_placeholders_not_found_are_reported():
    result = reinsert_pdf_text_bytes(_minimal_text_pdf("Alleen [PERSOON_1]."), _valid_scrub_key())

    assert result["placeholders_not_found"] == ["[ORGANISATIE_01]", "[ZAAKNUMMER_1]"]


def test_blank_or_image_only_pdf_is_unsupported():
    result = reinsert_pdf_text_bytes(_blank_pdf(), _valid_scrub_key())

    assert result["restored_text"] == ""
    assert result["replacement_count"] == 0
    assert result["unsupported_reason"] == UNSUPPORTED_NO_TEXT_REASON
    assert result["ocr_used"] is False
    assert result["pdf_output"] is False
    assert UNSUPPORTED_NO_TEXT_REASON in result["extraction_warnings"]


def test_invalid_pdf_bytes_return_validation_issues():
    result = reinsert_pdf_text_bytes(b"not a pdf", _valid_scrub_key())

    assert result["validation_issues"]
    assert result["restored_text"] == ""
    assert result["ocr_used"] is False
    assert result["pdf_output"] is False


def test_local_no_ai_no_cloud_audit_fields():
    result = reinsert_pdf_text_bytes(_minimal_text_pdf("[PERSOON_1]."), _valid_scrub_key())

    assert result["local_only"] is True
    assert result["ai_processing"] is False
    assert result["cloud_processing"] is False
    assert result["ocr_used"] is False
    assert result["pdf_output"] is False


def test_invalid_scrub_key_returns_validation_issues():
    scrub_key = _valid_scrub_key()
    scrub_key["items"][0]["timestamp"] = ""

    result = reinsert_pdf_text_bytes(_minimal_text_pdf("Waarde [PERSOON_1]."), scrub_key)

    assert result["restored_text"] == "Waarde [PERSOON_1]."
    assert result["replacement_count"] == 0
    assert result["validation_issues"]
    assert any("timestamp" in issue for issue in result["validation_issues"])


def test_helper_does_not_mutate_input_scrub_key():
    scrub_key = _valid_scrub_key()
    original = deepcopy(scrub_key)

    reinsert_pdf_text_bytes(_minimal_text_pdf("[PERSOON_1]."), scrub_key)

    assert scrub_key == original


def test_limitations_are_reported():
    result = reinsert_pdf_text_bytes(_minimal_text_pdf("[PERSOON_1]."), _valid_scrub_key())

    assert result["limitations"] == PDF_TEXT_LIMITATIONS
    assert any("OCR" in limitation for limitation in result["limitations"])
    assert any("TXT" in limitation for limitation in result["limitations"])


def test_missing_pypdf_dependency_is_reported(monkeypatch):
    monkeypatch.setattr(pdf_reinsert, "PdfReader", None)
    monkeypatch.setattr(pdf_reinsert, "PYPDF_IMPORT_ERROR", ImportError("synthetic missing dependency"))

    result = pdf_reinsert.extract_text_from_pdf_bytes(b"%PDF-1.4")

    assert result["validation_issues"]
    assert PYPDF_MISSING_REASON in result["validation_issues"][0]
    assert result["ocr_used"] is False
    assert result["pdf_output"] is False


def test_examples_use_synthetic_values_only():
    result = reinsert_pdf_text_bytes(
        _minimal_text_pdf("[PERSOON_1] / [ZAAKNUMMER_1] / [ORGANISATIE_01]"),
        _valid_scrub_key(),
    )

    assert "BETROKKENE-TEST-A" in result["restored_text"]
    assert "ZAAK-TEST-2026-001" in result["restored_text"]
    assert "RECHTBANK TESTDAM" in result["restored_text"]
    assert "Jan Jansen" not in result["restored_text"]
    assert "Piet de Vries" not in result["restored_text"]
