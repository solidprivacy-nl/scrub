from __future__ import annotations

from io import BytesIO
from zipfile import ZipFile

from docx_hygiene_audit import (
    build_docx_hygiene_audit_report,
    render_docx_hygiene_audit_markdown,
)


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


def _body(text: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}"><w:body><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:body></w:document>"""


def _single_text_root(root_tag: str, text: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:{root_tag} xmlns:w="{W_NS}"><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:{root_tag}>"""


def _comments(text: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:comments xmlns:w="{W_NS}"><w:comment w:id="0" w:author="SYNTHETIC-REVIEWER"><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:comment></w:comments>"""


def _tracked_body() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}"><w:body><w:p><w:del><w:r><w:delText>SYNTHETIC-DELETED-RISK</w:delText></w:r></w:del><w:ins><w:r><w:t>SYNTHETIC-INSERTED-RISK</w:t></w:r></w:ins></w:p></w:body></w:document>"""


def test_hygiene_audit_reports_high_risk_findings_without_cleaning_or_blocking():
    docx_bytes = _minimal_docx({
        "word/document.xml": _tracked_body(),
        "word/header1.xml": _single_text_root("hdr", "SYNTHETIC-HEADER-RISK"),
        "word/footer1.xml": _single_text_root("ftr", "SYNTHETIC-FOOTER-RISK"),
        "word/comments.xml": _comments("SYNTHETIC-COMMENT-RISK"),
    })

    report = build_docx_hygiene_audit_report(docx_bytes)

    assert report["audit_type"] == "docx_hygiene_audit"
    assert report["local_only"] is True
    assert report["ai_processing"] is False
    assert report["cloud_processing"] is False
    assert report["report_only"] is True
    assert report["extraction_only"] is True
    assert report["cleaning_applied"] is False
    assert report["export_blocking"] is False
    assert report["export_semantics_changed"] is False
    assert report["summary"]["severity"] == "high"
    assert report["summary"]["safe_to_claim_clean"] is False
    assert report["summary"]["high_risk_findings"] == 4
    assert {finding["id"] for finding in report["findings"]} == {
        "headers_detected",
        "footers_detected",
        "comments_detected",
        "tracked_changes_detected",
    }
    assert report["counts"] == {
        "headers": 1,
        "footers": 1,
        "comments": 1,
        "tracked_changes": 3,
    }


def test_hygiene_audit_no_supported_findings_is_not_a_clean_docx_claim():
    docx_bytes = _minimal_docx({"word/document.xml": _body("SYNTHETIC-BODY-ONLY")})

    report = build_docx_hygiene_audit_report(docx_bytes)

    assert report["valid_docx"] is True
    assert report["summary"]["severity"] == "low"
    assert report["findings"] == []
    assert report["summary"]["safe_to_claim_clean"] is False
    assert "not a clean-DOCX guarantee" in report["summary"]["message"]
    assert "future work" in report["unsupported_scope_note"]


def test_hygiene_audit_invalid_docx_reports_unknown_risk_without_throwing():
    report = build_docx_hygiene_audit_report(b"not a zip")

    assert report["valid_docx"] is False
    assert report["summary"]["severity"] == "medium"
    assert report["findings"][0]["id"] == "invalid_docx"
    assert report["validation_issues"] == ["DOCX content is not a valid OOXML package."]
    assert report["cleaning_applied"] is False
    assert report["export_blocking"] is False


def test_markdown_rendering_includes_report_only_boundaries():
    docx_bytes = _minimal_docx({
        "word/document.xml": _body("SYNTHETIC-BODY"),
        "word/comments.xml": _comments("SYNTHETIC-COMMENT-RISK"),
    })

    report = build_docx_hygiene_audit_report(docx_bytes)
    markdown = render_docx_hygiene_audit_markdown(report)

    assert "# DOCX hygiene audit report" in markdown
    assert "Severity: `high`" in markdown
    assert "Comments and margin notes" in markdown or "DOCX comments" in markdown
    assert "No DOCX cleaner was applied." in markdown
    assert "No comments or tracked changes were removed." in markdown
    assert "No export blocking was applied." in markdown
    assert "not a clean-DOCX guarantee" in markdown


def test_hygiene_audit_uses_synthetic_values_only():
    docx_bytes = _minimal_docx({
        "word/document.xml": _body("SYNTHETIC-DOCX-HYGIENE-AUDIT-001"),
        "word/comments.xml": _comments("SYNTHETIC-COMMENT-AUDIT-001"),
    })

    report = build_docx_hygiene_audit_report(docx_bytes)
    rendered = repr(report)

    assert "SYNTHETIC" in rendered
    assert "Jan Jansen" not in rendered
    assert "Piet de Vries" not in rendered
    assert "123456782" not in rendered
