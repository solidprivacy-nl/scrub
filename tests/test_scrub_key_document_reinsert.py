from __future__ import annotations

from copy import deepcopy
from io import BytesIO
from zipfile import ZipFile
import xml.etree.ElementTree as ET

from scrub_key import build_scrub_key
from scrub_key_document_reinsert import (
    DOCX_LIMITATIONS,
    reinsert_docx_bytes,
    reinsert_text_document,
    reinsert_txt_bytes,
)

VALID_SYNTHETIC_ROWS = [
    {
        "original_value": "BETROKKENE-TEST-A",
        "placeholder": "[PERSOON_1]",
        "entity_type": "PERSON",
        "type_label": "Naam",
        "source": "detected",
        "review_status": "auto_detected",
        "include": True,
        "timestamp": "2026-06-08T10:00:00Z",
    },
    {
        "original_value": "ZAAK-TEST-2026-001",
        "placeholder": "[ZAAKNUMMER_1]",
        "entity_type": "LEGAL_REFERENCE",
        "type_label": "Zaaknummer",
        "source": "manual",
        "review_status": "manual",
        "include": True,
        "timestamp": "2026-06-08T10:05:00Z",
    },
    {
        "original_value": "RECHTBANK TESTDAM",
        "placeholder": "[ORGANISATIE_01]",
        "entity_type": "ORGANIZATION",
        "type_label": "Organisatie",
        "source": "detected",
        "review_status": "auto_detected",
        "include": True,
        "timestamp": "2026-06-08T10:10:00Z",
    },
]

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def _valid_scrub_key():
    return build_scrub_key(VALID_SYNTHETIC_ROWS, document_label="Document reinsert testdossier")


def _minimal_docx(document_xml: str) -> bytes:
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""
    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""
    output = BytesIO()
    with ZipFile(output, "w") as docx:
        docx.writestr("[Content_Types].xml", content_types)
        docx.writestr("_rels/.rels", rels)
        docx.writestr("word/document.xml", document_xml)
    return output.getvalue()


def _document_xml_with_texts(texts: list[str]) -> str:
    paragraphs = "".join(
        f"<w:p><w:r><w:t>{text}</w:t></w:r></w:p>" for text in texts
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}"><w:body>{paragraphs}</w:body></w:document>"""


def _document_xml_with_table(text: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}"><w:body><w:tbl><w:tr><w:tc><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:body></w:document>"""


def _document_xml_with_split_run() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}"><w:body><w:p><w:r><w:t>[PERS</w:t></w:r><w:r><w:t>OON_1]</w:t></w:r></w:p></w:body></w:document>"""


def _docx_texts(docx_bytes: bytes) -> list[str]:
    with ZipFile(BytesIO(docx_bytes), "r") as docx:
        xml = docx.read("word/document.xml")
    root = ET.fromstring(xml)
    return [node.text or "" for node in root.iter(f"{{{W_NS}}}t")]


def test_txt_text_reinsert_with_one_placeholder():
    result = reinsert_text_document("Verzoeker [PERSOON_1] verschijnt.", _valid_scrub_key())

    assert result["text"] == "Verzoeker BETROKKENE-TEST-A verschijnt."
    assert result["content"] == result["text"]
    assert result["document_type"] == "txt"
    assert result["replacement_count"] == 1
    assert result["local_only"] is True


def test_txt_bytes_reinsert_with_multiple_placeholders():
    content = "[PERSOON_1] heeft zaak [ZAAKNUMMER_1].".encode("utf-8")

    result = reinsert_txt_bytes(content, _valid_scrub_key())

    assert result["text"] == "BETROKKENE-TEST-A heeft zaak ZAAK-TEST-2026-001."
    assert result["content_bytes"] == result["text"].encode("utf-8")
    assert result["encoding"] == "utf-8"
    assert result["replacement_count"] == 2


def test_txt_unknown_placeholder_remains_unchanged_and_is_reported():
    result = reinsert_text_document("Onbekend: [ONBEKEND_1].", _valid_scrub_key())

    assert result["text"] == "Onbekend: [ONBEKEND_1]."
    assert result["unknown_placeholders"] == ["[ONBEKEND_1]"]
    assert result["replacement_count"] == 0


def test_invalid_scrub_key_returns_validation_issues():
    scrub_key = _valid_scrub_key()
    scrub_key["items"][0]["timestamp"] = ""

    result = reinsert_text_document("Waarde [PERSOON_1].", scrub_key)

    assert result["text"] == "Waarde [PERSOON_1]."
    assert result["replacement_count"] == 0
    assert result["validation_issues"]
    assert any("timestamp" in issue for issue in result["validation_issues"])


def test_docx_reinsert_with_one_placeholder_in_paragraph():
    docx_bytes = _minimal_docx(_document_xml_with_texts(["Verzoeker [PERSOON_1] verschijnt."]))

    result = reinsert_docx_bytes(docx_bytes, _valid_scrub_key())

    assert result["document_type"] == "docx"
    assert result["replacement_count"] == 1
    assert _docx_texts(result["docx_bytes"]) == ["Verzoeker BETROKKENE-TEST-A verschijnt."]


def test_docx_reinsert_with_multiple_placeholders():
    docx_bytes = _minimal_docx(
        _document_xml_with_texts([
            "[PERSOON_1] heeft zaak [ZAAKNUMMER_1].",
            "Instantie: [ORGANISATIE_01].",
        ])
    )

    result = reinsert_docx_bytes(docx_bytes, _valid_scrub_key())

    texts = _docx_texts(result["docx_bytes"])
    assert texts == [
        "BETROKKENE-TEST-A heeft zaak ZAAK-TEST-2026-001.",
        "Instantie: RECHTBANK TESTDAM.",
    ]
    assert result["replacement_count"] == 3
    assert result["placeholders_not_found"] == []


def test_docx_reinsert_supports_table_text_in_main_document_xml():
    docx_bytes = _minimal_docx(_document_xml_with_table("Tabelwaarde [ZAAKNUMMER_1]."))

    result = reinsert_docx_bytes(docx_bytes, _valid_scrub_key())

    assert _docx_texts(result["docx_bytes"]) == ["Tabelwaarde ZAAK-TEST-2026-001."]
    assert result["replacement_count"] == 1


def test_docx_output_remains_a_valid_docx_zip_file():
    docx_bytes = _minimal_docx(_document_xml_with_texts(["Waarde [PERSOON_1]."]))

    result = reinsert_docx_bytes(docx_bytes, _valid_scrub_key())

    with ZipFile(BytesIO(result["docx_bytes"]), "r") as docx:
        assert "[Content_Types].xml" in docx.namelist()
        assert "_rels/.rels" in docx.namelist()
        assert "word/document.xml" in docx.namelist()
        ET.fromstring(docx.read("word/document.xml"))


def test_docx_paragraph_text_is_restored_correctly():
    docx_bytes = _minimal_docx(
        _document_xml_with_texts(["Eerste alinea [PERSOON_1].", "Tweede alinea [ZAAKNUMMER_1]."])
    )

    result = reinsert_docx_bytes(docx_bytes, _valid_scrub_key())

    assert _docx_texts(result["docx_bytes"]) == [
        "Eerste alinea BETROKKENE-TEST-A.",
        "Tweede alinea ZAAK-TEST-2026-001.",
    ]


def test_docx_helper_returns_audit_summary():
    docx_bytes = _minimal_docx(_document_xml_with_texts(["Waarde [PERSOON_1]."]))

    result = reinsert_docx_bytes(docx_bytes, _valid_scrub_key())

    for field in [
        "replacement_count",
        "item_count",
        "active_item_count",
        "excluded_item_count",
        "placeholders_not_found",
        "unknown_placeholders",
        "duplicate_placeholders",
        "validation_issues",
        "document_type",
        "local_only",
        "ai_processing",
        "cloud_processing",
    ]:
        assert field in result
    assert result["document_type"] == "docx"
    assert result["local_only"] is True
    assert result["ai_processing"] is False
    assert result["cloud_processing"] is False


def test_docx_unsupported_areas_or_limitations_are_documented():
    docx_bytes = _minimal_docx(_document_xml_with_split_run())

    result = reinsert_docx_bytes(docx_bytes, _valid_scrub_key())

    assert result["limitations"] == DOCX_LIMITATIONS
    assert result["unsupported_parts"] == DOCX_LIMITATIONS
    assert any("split" in limitation.lower() for limitation in result["limitations"])
    assert any("headers" in limitation.lower() for limitation in result["limitations"])
    assert _docx_texts(result["docx_bytes"]) == ["[PERS", "OON_1]"]
    assert result["replacement_count"] == 0


def test_helper_does_not_mutate_input_scrub_key():
    scrub_key = _valid_scrub_key()
    original = deepcopy(scrub_key)
    docx_bytes = _minimal_docx(_document_xml_with_texts(["Waarde [PERSOON_1]."]))

    reinsert_text_document("Waarde [PERSOON_1].", scrub_key)
    reinsert_txt_bytes(b"Waarde [PERSOON_1].", scrub_key)
    reinsert_docx_bytes(docx_bytes, scrub_key)

    assert scrub_key == original


def test_no_ai_or_cloud_behavior():
    txt_result = reinsert_text_document("Waarde [PERSOON_1].", _valid_scrub_key())
    docx_bytes = _minimal_docx(_document_xml_with_texts(["Waarde [PERSOON_1]."]))
    docx_result = reinsert_docx_bytes(docx_bytes, _valid_scrub_key())

    for result in [txt_result, docx_result]:
        assert result["local_only"] is True
        assert result["ai_processing"] is False
        assert result["cloud_processing"] is False


def test_examples_use_synthetic_values_only():
    result = reinsert_text_document(
        "[PERSOON_1] / [ZAAKNUMMER_1] / [ORGANISATIE_01]",
        _valid_scrub_key(),
    )

    assert "BETROKKENE-TEST-A" in result["text"]
    assert "ZAAK-TEST-2026-001" in result["text"]
    assert "RECHTBANK TESTDAM" in result["text"]
    assert "Jan Jansen" not in result["text"]
    assert "Piet de Vries" not in result["text"]
