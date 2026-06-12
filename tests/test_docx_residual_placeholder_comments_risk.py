from __future__ import annotations

from io import BytesIO
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

from scrub_key import build_scrub_key
from scrub_key_document_reinsert import DOCX_LIMITATIONS, reinsert_docx_bytes


REPO_ROOT = Path(__file__).resolve().parents[1]
TRIAGE_DOC = REPO_ROOT / "DOCX_RESIDUAL_PLACEHOLDER_COMMENTS_TRIAGE.md"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

SYNTHETIC_ROWS = [
    {
        "original_value": "BETROKKENE-TEST-A",
        "placeholder": "[PERSOON_1]",
        "entity_type": "PERSON",
        "type_label": "Naam",
        "source": "detected",
        "review_status": "auto_detected",
        "include": True,
        "timestamp": "2026-06-12T10:00:00Z",
    }
]


def _valid_scrub_key() -> dict:
    return build_scrub_key(SYNTHETIC_ROWS, document_label="WP36A synthetisch DOCX-risicodossier")


def _minimal_docx_with_comments(document_text: str, comment_text: str) -> bytes:
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/comments.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"/>
</Types>"""
    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""
    document_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}"><w:body><w:p><w:r><w:t>{document_text}</w:t></w:r></w:p></w:body></w:document>"""
    comments_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:comments xmlns:w="{W_NS}"><w:comment w:id="0" w:author="SYNTHETIC-REVIEWER"><w:p><w:r><w:t>{comment_text}</w:t></w:r></w:p></w:comment></w:comments>"""

    output = BytesIO()
    with ZipFile(output, "w") as docx:
        docx.writestr("[Content_Types].xml", content_types)
        docx.writestr("_rels/.rels", rels)
        docx.writestr("word/document.xml", document_xml)
        docx.writestr("word/comments.xml", comments_xml)
    return output.getvalue()


def _docx_texts(docx_bytes: bytes, part: str) -> list[str]:
    with ZipFile(BytesIO(docx_bytes), "r") as docx:
        xml = docx.read(part)
    root = ET.fromstring(xml)
    return [node.text or "" for node in root.iter(f"{{{W_NS}}}t")]


def test_docx_reinsert_leaves_residual_numbering_mismatch_placeholder_visible():
    docx_bytes = _minimal_docx_with_comments(
        document_text="Restplaceholder [PERSOON_01] blijft zichtbaar.",
        comment_text="SYNTHETIC-COMMENT-PERSOON-01 blijft buiten scope.",
    )

    result = reinsert_docx_bytes(docx_bytes, _valid_scrub_key())

    assert _docx_texts(result["docx_bytes"], "word/document.xml") == [
        "Restplaceholder [PERSOON_01] blijft zichtbaar."
    ]
    assert result["unknown_placeholders"] == ["[PERSOON_01]"]
    assert result["placeholders_not_found"] == ["[PERSOON_1]"]
    assert result["replacement_count"] == 0
    assert "BETROKKENE-TEST-A" not in result["text"]


def test_docx_comments_are_copied_through_unchanged_and_remain_outside_current_scope():
    synthetic_comment = "SYNTHETIC-COMMENT-PERSOON-01 blijft buiten huidige verwerking."
    docx_bytes = _minimal_docx_with_comments(
        document_text="Body [PERSOON_1] wordt wel teruggezet.",
        comment_text=synthetic_comment,
    )

    result = reinsert_docx_bytes(docx_bytes, _valid_scrub_key())

    assert _docx_texts(result["docx_bytes"], "word/document.xml") == [
        "Body BETROKKENE-TEST-A wordt wel teruggezet."
    ]
    assert _docx_texts(result["docx_bytes"], "word/comments.xml") == [synthetic_comment]
    assert result["replacement_count"] == 1
    assert result["limitations"] == DOCX_LIMITATIONS
    assert any("comments" in limitation.lower() for limitation in result["unsupported_parts"])


def test_triage_document_records_high_risk_and_no_fix_boundary():
    text = TRIAGE_DOC.read_text(encoding="utf-8")
    lowered = text.lower()

    assert "high-risk document hygiene issue" in lowered
    assert "[PERSOON_01]" in text
    assert "word/comments.xml" in text
    assert "kantlijncommentaren" in lowered or "margin comments" in lowered
    assert "no docx cleaner" in lowered or "does not implement a docx cleaner" in lowered
    assert "does not implement a fix" in lowered
    assert "no export semantics" in lowered or "change export semantics" in lowered
    assert "wp37" in lowered


def test_wp36a_uses_synthetic_values_only():
    exported_doc = TRIAGE_DOC.read_text(encoding="utf-8")
    synthetic_docx = _minimal_docx_with_comments(
        document_text="Restplaceholder [PERSOON_01].",
        comment_text="SYNTHETIC-COMMENT-PERSOON-01",
    )

    assert "SYNTHETIC" in synthetic_docx.decode("latin1", errors="ignore")
    assert "Jan Jansen" not in exported_doc
    assert "Piet de Vries" not in exported_doc
    assert "123456782" not in exported_doc
