"""Pure document-level Scrub Key reinsert helpers for SolidPrivacy Scrub.

The helpers in this module wrap the existing deterministic text reinsert logic
for TXT and DOCX inputs. They deliberately avoid Streamlit UI integration,
PDF handling, AI calls, remote processing, file-system persistence and export
semantic changes.

DOCX support covers text nodes in:
- ``word/document.xml``;
- ``word/header*.xml``;
- ``word/footer*.xml``.

Normal body paragraphs, body tables and header/footer text are restored. The
helper still does not restore placeholders split across multiple Word text
nodes, comments, tracked-change-only parts, footnotes/endnotes, text boxes or
metadata.
"""

from __future__ import annotations

from io import BytesIO
from typing import Any
from zipfile import ZIP_DEFLATED, BadZipFile, ZipFile
import re
import xml.etree.ElementTree as ET

from scrub_key_reinsert import reinsert_from_scrub_key

DOCX_MAIN_DOCUMENT = "word/document.xml"
DOCX_HEADER_RE = re.compile(r"^word/header[^/]*\.xml$")
DOCX_FOOTER_RE = re.compile(r"^word/footer[^/]*\.xml$")
WORDPROCESSINGML_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"

DOCX_LIMITATIONS = [
    "DOCX helper processes word/document.xml plus word/header*.xml and word/footer*.xml text nodes.",
    "Normal body paragraphs, body tables and header/footer text are supported.",
    "Placeholders split across multiple Word runs/text nodes are not restored in this version.",
    "Comments, tracked-change-only parts, footnotes/endnotes, text boxes and metadata are not processed in this version.",
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
    """Reinsert placeholders in plain text and return restored text plus audit."""
    result = _with_document_metadata(reinsert_from_scrub_key(text, scrub_key), "txt")
    result["content"] = result.get("text", "")
    result["limitations"] = []
    return result


def reinsert_txt_bytes(
    content: bytes,
    scrub_key: dict[str, Any],
    encoding: str = "utf-8",
) -> dict[str, Any]:
    """Decode TXT bytes, reinsert placeholders and return restored text/bytes."""
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
        "processed_parts": [],
        "processed_part_count": 0,
        "part_texts": {},
    }


def _word_text_nodes(root: ET.Element) -> list[ET.Element]:
    return list(root.iter(f"{{{WORDPROCESSINGML_NS}}}t"))


def _supported_docx_xml_parts(names: set[str]) -> list[str]:
    parts = [DOCX_MAIN_DOCUMENT]
    parts.extend(sorted(name for name in names if DOCX_HEADER_RE.match(name)))
    parts.extend(sorted(name for name in names if DOCX_FOOTER_RE.match(name)))
    return parts


def _serialize_package_with_xml_parts(
    content: bytes,
    replacement_parts: dict[str, bytes],
) -> bytes:
    output = BytesIO()
    with ZipFile(BytesIO(content), "r") as source_package, ZipFile(
        output,
        "w",
        ZIP_DEFLATED,
    ) as target_package:
        for entry in source_package.infolist():
            data = replacement_parts.get(entry.filename)
            if data is None:
                data = source_package.read(entry.filename)
            target_package.writestr(entry, data)
    return output.getvalue()


def _parse_supported_parts(
    package: ZipFile,
    part_names: list[str],
) -> tuple[dict[str, ET.Element], str | None]:
    roots: dict[str, ET.Element] = {}
    for part_name in part_names:
        try:
            roots[part_name] = ET.fromstring(package.read(part_name))
        except ET.ParseError as exc:
            return {}, f"DOCX {part_name} could not be parsed: {exc}"
    return roots, None


def reinsert_docx_bytes(content: bytes, scrub_key: dict[str, Any]) -> dict[str, Any]:
    """Reinsert placeholders in supported DOCX body/header/footer text nodes.

    The input bytes and Scrub Key are not mutated. All supported OOXML parts are
    validated before any output package is produced. Audit counts and unresolved
    placeholders cover the combined supported text surface.
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
            part_names = _supported_docx_xml_parts(names)
            roots, parse_issue = _parse_supported_parts(docx_package, part_names)
    except BadZipFile:
        return _docx_validation_result(
            original_content,
            "DOCX content is not a valid OOXML package.",
        )

    if parse_issue:
        return _docx_validation_result(original_content, parse_issue)

    part_nodes = {
        part_name: _word_text_nodes(root)
        for part_name, root in roots.items()
    }
    original_part_texts = {
        part_name: "\n".join(node.text or "" for node in nodes)
        for part_name, nodes in part_nodes.items()
    }
    combined_original_text = "\n".join(
        original_part_texts[part_name]
        for part_name in part_names
    )
    audit_result = _with_document_metadata(
        reinsert_from_scrub_key(combined_original_text, scrub_key),
        "docx",
    )

    if not audit_result.get("validation_issues"):
        for nodes in part_nodes.values():
            for node in nodes:
                node_result = reinsert_from_scrub_key(node.text or "", scrub_key)
                node.text = node_result.get("text", "")

    restored_part_texts = {
        part_name: "\n".join(node.text or "" for node in part_nodes[part_name])
        for part_name in part_names
    }
    restored_xml_parts = {
        part_name: ET.tostring(
            roots[part_name],
            encoding="utf-8",
            xml_declaration=True,
        )
        for part_name in part_names
    }
    restored_docx = _serialize_package_with_xml_parts(
        original_content,
        restored_xml_parts,
    )
    combined_restored_text = "\n".join(
        restored_part_texts[part_name]
        for part_name in part_names
    )

    audit_result["text"] = combined_restored_text
    audit_result["content"] = combined_restored_text
    audit_result["docx_bytes"] = restored_docx
    audit_result["limitations"] = list(DOCX_LIMITATIONS)
    audit_result["unsupported_parts"] = list(DOCX_LIMITATIONS)
    audit_result["processed_parts"] = list(part_names)
    audit_result["processed_part_count"] = len(part_names)
    audit_result["part_texts"] = restored_part_texts
    return audit_result
