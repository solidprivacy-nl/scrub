from __future__ import annotations

import pytest

import reinsert_auto_flow
from reinsert_auto_flow import (
    build_reinsert_request_signature,
    build_reinsert_source,
    run_reinsert_request,
)


def valid_scrub_key() -> dict:
    return {
        "schema": "solidprivacy.scrub_key",
        "schema_version": "1.0",
        "reversible": True,
        "privacy_model": "pseudonymization_not_full_anonymization",
        "excluded_rows_policy": "omitted",
        "item_count": 1,
        "items": [
            {
                "original_value": "Mila Voorbeeld",
                "placeholder": "[PERSOON_01]",
                "entity_type": "PERSON",
                "type_label": "Persoon",
                "source": "synthetic_test",
                "review_status": "verified",
                "include_state": "included",
                "timestamp": "2026-07-27T16:05:00+02:00",
            }
        ],
    }


def test_uploaded_file_takes_precedence_over_pasted_text() -> None:
    source = build_reinsert_source(
        file_name="voorbeeld.docx",
        file_bytes=b"docx-bytes",
        pasted_text="[PERSOON_01]",
    )

    assert source == {
        "source_type": "docx",
        "file_name": "voorbeeld.docx",
        "content_bytes": b"docx-bytes",
        "pasted_text_ignored": True,
    }


def test_pasted_text_is_supported_without_a_file() -> None:
    source = build_reinsert_source(pasted_text="Hallo [PERSOON_01]")

    assert source is not None
    assert source["source_type"] == "text"
    assert source["text"] == "Hallo [PERSOON_01]"


def test_empty_source_returns_none() -> None:
    assert build_reinsert_source() is None


def test_unsupported_file_type_fails_explicitly() -> None:
    with pytest.raises(ValueError, match="Ondersteund zijn TXT, DOCX"):
        build_reinsert_source(file_name="voorbeeld.rtf", file_bytes=b"rtf")


def test_request_signature_is_stable_and_sensitive_to_source_and_key() -> None:
    source = build_reinsert_source(file_name="voorbeeld.txt", file_bytes=b"[PERSOON_01]")
    assert source is not None
    key = valid_scrub_key()

    first = build_reinsert_request_signature(source, key)
    second = build_reinsert_request_signature(dict(source), dict(key))
    changed_source = build_reinsert_source(
        file_name="voorbeeld.txt",
        file_bytes=b"Gewijzigd [PERSOON_01]",
    )
    assert changed_source is not None
    changed_key = valid_scrub_key()
    changed_key["items"][0]["original_value"] = "Andere Waarde"

    assert first == second
    assert first != build_reinsert_request_signature(changed_source, key)
    assert first != build_reinsert_request_signature(source, changed_key)


def test_text_request_uses_existing_reinsert_semantics() -> None:
    source = build_reinsert_source(pasted_text="Hallo [PERSOON_01]")
    assert source is not None

    result = run_reinsert_request(source, valid_scrub_key())

    assert result["text"] == "Hallo Mila Voorbeeld"
    assert result["replacement_count"] == 1
    assert result["local_only"] is True
    assert result["ai_processing"] is False
    assert result["cloud_processing"] is False


@pytest.mark.parametrize(
    ("file_name", "source_type", "target_name", "expected_kwargs"),
    [
        ("voorbeeld.txt", "txt", "reinsert_txt_bytes", {"encoding": "utf-8"}),
        ("voorbeeld.docx", "docx", "reinsert_docx_bytes", {}),
        ("voorbeeld.pdf", "pdf", "reinsert_pdf_text_bytes", {}),
    ],
)
def test_file_requests_dispatch_to_existing_helpers(
    monkeypatch: pytest.MonkeyPatch,
    file_name: str,
    source_type: str,
    target_name: str,
    expected_kwargs: dict,
) -> None:
    captured: dict = {}

    def fake_helper(content_bytes: bytes, scrub_key: dict, **kwargs: object) -> dict:
        captured.update(
            content_bytes=content_bytes,
            scrub_key=scrub_key,
            kwargs=kwargs,
        )
        return {"source_type": source_type, "replacement_count": 1}

    monkeypatch.setattr(reinsert_auto_flow, target_name, fake_helper)
    source = build_reinsert_source(file_name=file_name, file_bytes=b"payload")
    assert source is not None

    result = run_reinsert_request(source, valid_scrub_key())

    assert result["source_type"] == source_type
    assert captured["content_bytes"] == b"payload"
    assert captured["scrub_key"] == valid_scrub_key()
    assert captured["kwargs"] == expected_kwargs
