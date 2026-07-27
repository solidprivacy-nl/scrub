"""Pure orchestration helpers for the automatic local reinsert flow.

The helpers keep Streamlit state and presentation outside this module. They only
normalise one source input, build a deterministic request signature, and dispatch
to the existing local reinsert helpers without changing their semantics.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from scrub_key_document_reinsert import reinsert_docx_bytes, reinsert_txt_bytes
from scrub_key_pdf_text_reinsert import reinsert_pdf_text_bytes
from scrub_key_reinsert import reinsert_from_scrub_key


SUPPORTED_FILE_TYPES = {
    ".txt": "txt",
    ".docx": "docx",
    ".pdf": "pdf",
}


def build_reinsert_source(
    *,
    file_name: str | None = None,
    file_bytes: bytes | bytearray | None = None,
    pasted_text: str = "",
) -> dict[str, Any] | None:
    """Return one normalised source, giving an uploaded file precedence.

    ``None`` means that the user has not supplied a source yet. The Streamlit
    uploader already limits file extensions, but this helper still rejects an
    unsupported suffix so callers cannot silently route an unknown document.
    """

    clean_name = str(file_name or "").strip()
    if clean_name and file_bytes is not None:
        suffix = Path(clean_name).suffix.lower()
        source_type = SUPPORTED_FILE_TYPES.get(suffix)
        if source_type is None:
            raise ValueError(
                "Ondersteund zijn TXT, DOCX en tekstgebaseerde PDF-bestanden."
            )
        return {
            "source_type": source_type,
            "file_name": clean_name,
            "content_bytes": bytes(file_bytes),
            "pasted_text_ignored": bool(str(pasted_text or "").strip()),
        }

    text = str(pasted_text or "")
    if text.strip():
        return {
            "source_type": "text",
            "file_name": None,
            "text": text,
            "pasted_text_ignored": False,
        }

    return None


def build_reinsert_request_signature(
    source: Mapping[str, Any],
    scrub_key: Mapping[str, Any],
) -> str:
    """Build a deterministic signature for one source/key combination."""

    digest = hashlib.sha256()
    source_type = str(source.get("source_type") or "")
    digest.update(source_type.encode("utf-8"))
    digest.update(b"\0")

    if source_type == "text":
        digest.update(str(source.get("text") or "").encode("utf-8"))
    else:
        digest.update(bytes(source.get("content_bytes") or b""))

    digest.update(b"\0")
    digest.update(
        json.dumps(
            dict(scrub_key),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    )
    return digest.hexdigest()


def run_reinsert_request(
    source: Mapping[str, Any],
    scrub_key: Mapping[str, Any],
) -> dict[str, Any]:
    """Dispatch one normalised request to the existing local helpers."""

    source_type = str(source.get("source_type") or "")
    if source_type == "text":
        return reinsert_from_scrub_key(str(source.get("text") or ""), scrub_key)
    if source_type == "txt":
        return reinsert_txt_bytes(
            bytes(source.get("content_bytes") or b""),
            scrub_key,
            encoding="utf-8",
        )
    if source_type == "docx":
        return reinsert_docx_bytes(
            bytes(source.get("content_bytes") or b""),
            scrub_key,
        )
    if source_type == "pdf":
        return reinsert_pdf_text_bytes(
            bytes(source.get("content_bytes") or b""),
            scrub_key,
        )
    raise ValueError(f"Onbekend brontype voor terugzetten: {source_type or 'leeg'}.")
