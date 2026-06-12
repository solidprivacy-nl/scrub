"""DOCX hidden-content extraction helpers for SolidPrivacy Scrub.

WP37 adds local, read-only inspection of DOCX package parts that are outside the
current foundation DOCX reinsert path. The helper detects and extracts text from
headers, footers and comments, and reports tracked-change signals. It does not
clean, remove, rewrite, block export, change reinsert behavior, call AI/cloud
services, persist files or process real-data fixtures.
"""

from __future__ import annotations

from io import BytesIO
from typing import Any
from zipfile import BadZipFile, ZipFile
import re
import xml.etree.ElementTree as ET

WORDPROCESSINGML_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
DOCX_MAIN_DOCUMENT = "word/document.xml"

HEADER_PATTERN = re.compile(r"^word/header\d*\.xml$")
FOOTER_PATTERN = re.compile(r"^word/footer\d*\.xml$")
COMMENT_PARTS = {
    "word/comments.xml",
    "word/commentsExtended.xml",
    "word/person.xml",
}
TRACKED_CHANGE_TAGS = {
    "ins",
    "del",
    "delText",
    "moveFrom",
    "moveTo",
    "moveFromRangeStart",
    "moveFromRangeEnd",
    "moveToRangeStart",
    "moveToRangeEnd",
}


def _local_name(tag: str) -> str:
    """Return the XML local name for a namespaced or plain tag."""
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def _text_nodes(root: ET.Element) -> list[str]:
    """Extract WordprocessingML text node values from an XML root."""
    values: list[str] = []
    for node in root.iter():
        if _local_name(node.tag) in {"t", "delText", "instrText"} and node.text:
            values.append(node.text)
    return values


def _joined(values: list[str]) -> str:
    return "\n".join(value for value in values if value)


def _parse_xml_part(part_name: str, data: bytes) -> dict[str, Any]:
    """Parse one XML part and return text/tracked-change diagnostics."""
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        return {
            "part_name": part_name,
            "text_fragments": [],
            "text": "",
            "parse_error": str(exc),
            "tracked_changes": [],
        }

    tracked_changes: list[dict[str, str]] = []
    for element in root.iter():
        tag_name = _local_name(element.tag)
        if tag_name in TRACKED_CHANGE_TAGS:
            fragments = _text_nodes(element)
            tracked_changes.append({
                "part_name": part_name,
                "element": tag_name,
                "text": _joined(fragments),
            })

    fragments = _text_nodes(root)
    return {
        "part_name": part_name,
        "text_fragments": fragments,
        "text": _joined(fragments),
        "parse_error": "",
        "tracked_changes": tracked_changes,
    }


def _comment_authors(part_name: str, data: bytes) -> list[str]:
    """Extract synthetic-safe comment/person author-like metadata where present."""
    if part_name not in COMMENT_PARTS:
        return []
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return []

    authors: list[str] = []
    for element in root.iter():
        for attr_name, attr_value in element.attrib.items():
            if _local_name(attr_name) in {"author", "initials", "name"} and attr_value:
                authors.append(attr_value)
    return sorted(set(authors))


def inspect_docx_hidden_content(content: bytes) -> dict[str, Any]:
    """Inspect high-risk DOCX hidden-content parts without changing the file.

    The returned structure is intentionally audit-oriented. It reports whether
    headers, footers, comments and tracked-change markers exist, and extracts
    their text where possible. The helper is side-effect free and does not make
    clean-export claims.
    """
    if not isinstance(content, (bytes, bytearray)):
        return {
            "document_type": "docx",
            "valid_docx": False,
            "validation_issues": ["DOCX content must be bytes."],
            "local_only": True,
            "ai_processing": False,
            "cloud_processing": False,
            "extraction_only": True,
            "cleaning_applied": False,
            "export_blocking": False,
            "docx_parts_seen": [],
            "headers": [],
            "footers": [],
            "comments": [],
            "tracked_changes": [],
            "detected": {},
            "warnings": ["DOCX content could not be inspected because it was not bytes."],
        }

    original_content = bytes(content)
    try:
        with ZipFile(BytesIO(original_content), "r") as package:
            part_names = sorted(package.namelist())
            parsed_parts: list[dict[str, Any]] = []
            headers: list[dict[str, Any]] = []
            footers: list[dict[str, Any]] = []
            comments: list[dict[str, Any]] = []
            tracked_changes: list[dict[str, str]] = []

            for part_name in part_names:
                is_header = bool(HEADER_PATTERN.match(part_name))
                is_footer = bool(FOOTER_PATTERN.match(part_name))
                is_comment = part_name in COMMENT_PARTS
                should_scan_for_tracked_changes = part_name.startswith("word/") and part_name.endswith(".xml")

                if not (is_header or is_footer or is_comment or should_scan_for_tracked_changes):
                    continue

                data = package.read(part_name)
                parsed = _parse_xml_part(part_name, data)
                parsed_parts.append(parsed)
                tracked_changes.extend(parsed["tracked_changes"])

                if is_header:
                    headers.append(parsed)
                if is_footer:
                    footers.append(parsed)
                if is_comment:
                    comment_info = dict(parsed)
                    comment_info["authors"] = _comment_authors(part_name, data)
                    comments.append(comment_info)
    except BadZipFile:
        return {
            "document_type": "docx",
            "valid_docx": False,
            "validation_issues": ["DOCX content is not a valid OOXML package."],
            "local_only": True,
            "ai_processing": False,
            "cloud_processing": False,
            "extraction_only": True,
            "cleaning_applied": False,
            "export_blocking": False,
            "docx_parts_seen": [],
            "headers": [],
            "footers": [],
            "comments": [],
            "tracked_changes": [],
            "detected": {},
            "warnings": ["DOCX content is not a valid OOXML package."],
        }

    detected = {
        "headers_detected": bool(headers),
        "footers_detected": bool(footers),
        "comments_detected": bool(comments),
        "tracked_changes_detected": bool(tracked_changes),
    }
    warnings: list[str] = []
    if headers:
        warnings.append("DOCX headers were detected and extracted for audit; they are not cleaned by this helper.")
    if footers:
        warnings.append("DOCX footers were detected and extracted for audit; they are not cleaned by this helper.")
    if comments:
        warnings.append("DOCX comments/person metadata were detected and extracted for audit; they are not cleaned by this helper.")
    if tracked_changes:
        warnings.append("DOCX tracked-change markers were detected; no accept/remove/blocking policy is applied by this helper.")

    return {
        "document_type": "docx",
        "valid_docx": True,
        "validation_issues": [],
        "local_only": True,
        "ai_processing": False,
        "cloud_processing": False,
        "extraction_only": True,
        "cleaning_applied": False,
        "export_blocking": False,
        "docx_parts_seen": part_names,
        "headers": headers,
        "footers": footers,
        "comments": comments,
        "tracked_changes": tracked_changes,
        "detected": detected,
        "warnings": warnings,
    }
