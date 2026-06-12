from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WINDOWS_POC_SCRIPT = REPO_ROOT / "scripts" / "run_windows_portable_poc.ps1"
WINDOWS_POC_DOC = REPO_ROOT / "WINDOWS_PORTABLE_POC.md"
LOCAL_RUN_DOC = REPO_ROOT / "LOCAL_RUN.md"

SYNTHETIC_FILENAME = "synthetic_windows_case_file.docx"
SYNTHETIC_CONTENT = "SYNTHETIC-WINDOWS-PORTABLE-POC-001"


def test_windows_portable_script_delegates_to_existing_local_launcher():
    source = WINDOWS_POC_SCRIPT.read_text(encoding="utf-8")

    assert "scripts/run_local_streamlit.py" in source
    assert "presidio_streamlit.py" not in source
    assert "fix_streamlit_nested_expanders.py" not in source
    assert "fix_streamlit_pdf_text_reinsert.py" not in source


def test_windows_portable_script_defaults_to_loopback_and_expected_port():
    source = WINDOWS_POC_SCRIPT.read_text(encoding="utf-8")

    assert "127.0.0.1" in source
    assert "8501" in source
    assert "0.0.0.0" not in source


def test_windows_portable_script_has_no_cloud_telemetry_or_packaging_behavior():
    source = WINDOWS_POC_SCRIPT.read_text(encoding="utf-8").lower()

    forbidden_fragments = [
        "huggingface.co",
        "api.openai.com",
        "http://",
        "https://",
        "telemetry",
        "analytics",
        "pyinstaller",
        "tauri",
        "electron",
        "msi",
        "installer",
        "downloadstring",
        "invoke-webrequest",
        "start-bitstransfer",
    ]
    assert not any(fragment in source for fragment in forbidden_fragments)


def test_windows_portable_script_does_not_accept_document_or_secret_arguments():
    source = WINDOWS_POC_SCRIPT.read_text(encoding="utf-8")
    lowered = source.lower()

    assert SYNTHETIC_FILENAME not in source
    assert SYNTHETIC_CONTENT not in source
    assert "document" not in lowered
    assert "scrub_key" not in lowered
    assert "secret" not in lowered
    assert "token" not in lowered
    assert "password" not in lowered


def test_windows_portable_doc_records_proof_of_concept_non_goals():
    doc = WINDOWS_POC_DOC.read_text(encoding="utf-8")
    lowered = doc.lower()

    assert "proof-of-concept only" in lowered
    assert "not a production packaging decision" in lowered
    assert "windows installer" in lowered
    assert "msi" in lowered
    assert "pyinstaller" in lowered
    assert "no real data" in lowered or "real-data" in lowered
    assert "telemetry" in lowered
    assert "cloud document processing" in lowered
    assert "no ui" in lowered or "ui changes" in lowered
    assert "export or reinsert semantic changes" in lowered


def test_windows_portable_doc_preserves_local_runtime_privacy_boundary():
    doc = WINDOWS_POC_DOC.read_text(encoding="utf-8")
    lowered = doc.lower()

    assert "127.0.0.1" in doc
    assert "scripts/run_local_streamlit.py" in doc
    assert "scripts/run_windows_portable_poc.ps1" in doc
    assert "source document content" in lowered
    assert "scrub key values" in lowered
    assert "restored output" in lowered
    assert "audit content" in lowered
    assert "does not prove" in lowered or "outside the proof-of-concept guarantee" in lowered


def test_local_run_documentation_mentions_wp48_windows_poc():
    doc = LOCAL_RUN_DOC.read_text(encoding="utf-8")
    lowered = doc.lower()

    assert "wp48" in lowered
    assert "windows portable proof of concept" in lowered
    assert "scripts\\run_windows_portable_poc.ps1" in doc
    assert "not a production installer" in lowered
    assert "not an msi" in lowered
    assert "not a full offline guarantee" in lowered
