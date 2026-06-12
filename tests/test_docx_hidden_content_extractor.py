from __future__ import annotations

from io import BytesIO
from zipfile import ZipFile

from docx_hidden_content_extractor import inspect_docx_hidden_content


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def _minimal_docx(parts: dict[str, str]) -> bytes:
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
        for part_name, xml in parts.items():
            docx.writestr(part_name, xml)
    return output.getvalue()


def _text_part(text: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}"><w:body><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:body></w:document>"""


def _header_or_footer(text: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:hdr xmlns:w="{W_NS}"><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:hdr>"""


def _comments(text: str, author: str = "SYNTHETIC-REVIEWER") -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:comments xmlns:w="{W_NS}"><w:comment w:id="0" w:author="{author}" w:initials="SR"><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:comment></w:comments>"""


def _tracked_changes() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}"><w:body><w:p><w:del><w:r><w:delText>OUDE-SYNTHETISCHE-WAARDE</w:delText></w:r></w:del><w:ins><w:r><w:t>NIEUWE-SYNTHETISCHE-WAARDE</w:t></w:r></w:ins></w:p></w:body></w:document>"""


def test_extracts_headers_footers_comments_and_tracked_changes_without_cleaning():
    docx_bytes = _minimal_docx({
        "word/document.xml": _tracked_changes(),
        "word/header1.xml": _header_or_footer("SYNTHETIC-HEADER-DOSSIER-001"),
        "word/footer1.xml": _header_or_footer("SYNTHETIC-FOOTER-CLIENT-001"),
        "word/comments.xml": _comments("SYNTHETIC-COMMENT-RISK-001"),
    })

    result = inspect_docx_hidden_content(docx_bytes)

    assert result["valid_docx"] is True
    assert result["local_only"] is True
    assert result["ai_processing"] is False
    assert result["cloud_processing"] is False
    assert result["extraction_only"] is True
    assert result["cleaning_applied"] is False
    assert result["export_blocking"] is False
    assert result["detected"] == {
        "headers_detected": True,
        "footers_detected": True,
        "comments_detected": True,
        "tracked_changes_detected": True,
    }
    assert result["headers"][0]["text"] == "SYNTHETIC-HEADER-DOSSIER-001"
    assert result["footers"][0]["text"] == "SYNTHETIC-FOOTER-CLIENT-001"
    assert result["comments"][0]["text"] == "SYNTHETIC-COMMENT-RISK-001"
    assert result["comments"][0]["authors"] == ["SR", "SYNTHETIC-REVIEWER"]
    assert {change["element"] for change in result["tracked_changes"]} >= {"del", "delText", "ins"}
    assert any("OUDE-SYNTHETISCHE-WAARDE" in change["text"] for change in result["tracked_changes"])


def test_header_footer_comment_absence_is_reported_without_warnings():
    docx_bytes = _minimal_docx({"word/document.xml": _text_part("Alleen synthetische bodytekst.")})

    result = inspect_docx_hidden_content(docx_bytes)

    assert result["detected"] == {
        "headers_detected": False,
        "footers_detected": False,
        "comments_detected": False,
        "tracked_changes_detected": False,
    }
    assert result["headers"] == []
    assert result["footers"] == []
    assert result["comments"] == []
    assert result["tracked_changes"] == []
    assert result["warnings"] == []


def test_invalid_docx_is_reported_without_side_effects():
    result = inspect_docx_hidden_content(b"not a zip")

    assert result["valid_docx"] is False
    assert result["validation_issues"] == ["DOCX content is not a valid OOXML package."]
    assert result["local_only"] is True
    assert result["ai_processing"] is False
    assert result["cloud_processing"] is False
    assert result["cleaning_applied"] is False
    assert result["export_blocking"] is False


def test_non_bytes_input_is_rejected_safely():
    result = inspect_docx_hidden_content("not bytes")

    assert result["valid_docx"] is False
    assert result["validation_issues"] == ["DOCX content must be bytes."]
    assert result["headers"] == []
    assert result["footers"] == []
    assert result["comments"] == []
    assert result["tracked_changes"] == []


def test_extractor_uses_synthetic_values_only():
    docx_bytes = _minimal_docx({
        "word/document.xml": _text_part("SYNTHETIC-DOCX-INSPECTION-001"),
        "word/comments.xml": _comments("SYNTHETIC-COMMENT-ONLY"),
    })

    result = inspect_docx_hidden_content(docx_bytes)
    rendered = repr(result)

    assert "SYNTHETIC" in rendered
    assert "Jan Jansen" not in rendered
    assert "Piet de Vries" not in rendered
    assert "123456782" not in rendered
