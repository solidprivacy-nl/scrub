"""Pure document-level Scrub Key reinsert helpers for SolidPrivacy Scrub.

The helpers in this module wrap the existing deterministic text reinsert logic
for TXT and DOCX inputs. They deliberately avoid Streamlit UI integration,
PDF handling, AI calls, remote processing, file-system persistence and export
semantic changes.

DOCX support is intentionally limited in this foundation version:
- only `word/document.xml` text nodes are processed;
- normal body paragraphs and tables in `word/document.xml` are covered;
- placeholders split across multiple Word runs/text nodes are not restored;
- headers, footers, comments, tracked changes and metadata are not processed.
"""

from __future__ import annotations

from io import BytesIO
from typing import Any
from zipfile import ZIP_DEFLATED, BadZipFile, ZipFile
import xml.etree.ElementTree as ET

from scrub_key_reinsert import reinsert_from_scrub_key

DOCX_MAIN_DOCUMENT = "word/document.xml"
WORDPROCESSINGML_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"

DOCX_LIMITATIONS = [
    "DOCX helper processes only word/document.xml text nodes in this foundation version.",
    "Normal body paragraphs and tables in word/document.xml are supported.",
    "Placeholders split across multiple Word runs/text nodes are not restored in this version.",
    "Headers, footers, comments, tracked changes and metadata are not processed in this version.",
]

ET.register_namespace("w", WORDPROCESSINGML_NS)
ET.register_namespace("xml", XML_NS)


def _with_document_metadata(result: dict[str, Any], document_type: str) -> dict[str, Any]:
    """Return a copy of a text reinsert result with document-level metadata."""
    return {
        **dict(result),
        "document_type": document_type,
        "local_only": True,
        "ai_processing": False,
        "cloud_processing": False,
    }


def reinsert_text_document(text: str, scrub_key: dict[str, Any]) -> dict[str, Any]:
    """Reinsert placeholders in plain text and return restored text plus audit.

    This is a document-level wrapper around ``reinsert_from_scrub_key`` for plain
    text/TXT use cases. It does not mutate the supplied Scrub Key.
    """
    result = _with_document_metadata(reinsert_from_scrub_key(text, scrub_key), "txt")
    result["content"] = result.get("text", "")
    result["limitations"] = []
    return result


def reinsert_txt_bytes(
    content: bytes,
    scrub_key: dict[str, Any],
    encoding: str = "utf-8",
) -> dict[str, Any]:
    """Decode TXT bytes, reinsert placeholders and return restored text/bytes.

    Decoding is strict by default so invalid input is reported instead of being
    silently changed. No file-system writes are performed.
    """
    if not isinstance(content, (bytes, bytearray)):
        result = reinsert_text_document("", scrub_key)
        result["validation_issues"] = ["TXT content must be bytes."]
        result["content_bytes"] = b""
        result["encoding"] = encoding
        return result

    try:
        text = bytes(content).decode(encoding)
    except UnicodeDecodeError as exc:
        result = reinsert_text_document("", scrub_key)
        result["validation_issues"] = [f"TXT content could not be decoded as {encoding}: {exc}"]
        result["content_bytes"] = b""
        result["encoding"] = encoding
        return result

    result = reinsert_text_document(text, scrub_key)
    result["content_bytes"] = result.get("text", "").encode(encoding)
    result["encoding"] = encoding
    return result


def _docx_validation_result(content: bytes, message: str) -> dict[str, Any]:
    return {
        "text": "",
        "content": "",
        "docx_bytes": bytes(content) if isinstance(content, (bytes, bytearray)) else b"",
        "replacement_count": 0,
        "item_count": 0,
        "active_item_count": 0,
        "excluded_item_count": 0,
        "placeholders_not_found": [],
        "unknown_placeholders": [],
        "duplicate_placeholders": [],
        "validation_issues": [message],
        "reinserted": False,
        "document_type": "docx",
        "local_only": True,
        "ai_processing": False,
        "cloud_processing": False,
        "limitations": list(DOCX_LIMITATIONS),
        "unsupported_parts": list(DOCX_LIMITATIONS),
    }


def _word_text_nodes(root: ET.Element) -> list[ET.Element]:
    return list(root.iter(f"{{{WORDPROCESSINGML_NS}}}t"))


def _serialize_package_with_document_xml(content: bytes, document_xml: bytes) -> bytes:
    output = BytesIO()
    with ZipFile(BytesIO(content), "r") as source_package, ZipFile(output, "w", ZIP_DEFLATED) as target_package:
        for entry in source_package.infolist():
            data = document_xml if entry.filename == DOCX_MAIN_DOCUMENT else source_package.read(entry.filename)
            target_package.writestr(entry, data)
    return output.getvalue()


def reinsert_docx_bytes(content: bytes, scrub_key: dict[str, Any]) -> dict[str, Any]:
    """Reinsert placeholders in the main body of a DOCX document.

    This foundation helper processes ``word/document.xml`` text nodes only. That
    covers normal paragraphs and tables in the main document body, while leaving
    headers, footers, comments, tracked changes and metadata untouched. It returns
    restored DOCX bytes and an audit summary. The input bytes and Scrub Key are
    not mutated.
    """
    if not isinstance(content, (bytes, bytearray)):
        return _docx_validation_result(b"", "DOCX content must be bytes.")

    original_content = bytes(content)

    try:
        with ZipFile(BytesIO(original_content), "r") as docx_package:
            names = set(docx_package.namelist())
            if DOCX_MAIN_DOCUMENT not in names:
                return _docx_validation_result(
                    original_content,
                    "DOCX package is missing word/document.xml.",
                )
            document_xml = docx_package.read(DOCX_MAIN_DOCUMENT)
    except BadZipFile:
        return _docx_validation_result(original_content, "DOCX content is not a valid OOXML package.")

    try:
        root = ET.fromstring(document_xml)
    except ET.ParseError as exc:
        return _docx_validation_result(original_content, f"DOCX document.xml could not be parsed: {exc}")

    text_nodes = _word_text_nodes(root)
    original_text = "\n".join(node.text or "" for node in text_nodes)
    audit_result = _with_document_metadata(reinsert_from_scrub_key(original_text, scrub_key), "docx")

    if not audit_result.get("validation_issues"):
        for node in text_nodes:
            node_result = reinsert_from_scrub_key(node.text or "", scrub_key)
            node.text = node_result.get("text", "")

    restored_document_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    restored_docx = _serialize_package_with_document_xml(original_content, restored_document_xml)

    audit_result["text"] = "\n".join(node.text or "" for node in text_nodes)
    audit_result["content"] = audit_result["text"]
    audit_result["docx_bytes"] = restored_docx
    audit_result["limitations"] = list(DOCX_LIMITATIONS)
    audit_result["unsupported_parts"] = list(DOCX_LIMITATIONS)
    return audit_result
