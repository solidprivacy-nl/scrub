from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LAUNCHER_PATH = REPO_ROOT / "scripts" / "run_local_streamlit.py"
LOCAL_RUN_PATH = REPO_ROOT / "LOCAL_RUN.md"

SYNTHETIC_FILENAME = "synthetic_confidential_fixture.txt"
SYNTHETIC_CONTENT = "SYNTHETIC-BETROKKENE-TEST-LOCAL-001"


def load_launcher_module():
    spec = importlib.util.spec_from_file_location("run_local_streamlit_under_test", LAUNCHER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_local_launcher_defaults_to_loopback_and_expected_port():
    launcher = load_launcher_module()

    args = launcher.parse_args([])

    assert args.address == "127.0.0.1"
    assert args.port == "8501"


def test_local_launcher_streamlit_command_disables_usage_stats_and_has_no_cloud_endpoint(monkeypatch):
    launcher = load_launcher_module()
    commands: list[list[str]] = []

    def fake_run_checked(command: list[str]) -> None:
        commands.append(command)

    monkeypatch.setattr(launcher, "run_checked", fake_run_checked)

    assert launcher.main([]) == 0

    assert commands[:2] == [
        [sys.executable, "fix_streamlit_nested_expanders.py"],
        [sys.executable, "fix_streamlit_pdf_text_reinsert.py"],
    ]
    streamlit_command = commands[-1]
    command_text = " ".join(streamlit_command).lower()

    assert streamlit_command[:5] == [sys.executable, "-m", "streamlit", "run", "presidio_streamlit.py"]
    assert streamlit_command[streamlit_command.index("--server.address") + 1] == "127.0.0.1"
    assert streamlit_command[streamlit_command.index("--server.port") + 1] == "8501"
    assert streamlit_command[streamlit_command.index("--server.headless") + 1] == "true"
    assert streamlit_command[streamlit_command.index("--browser.gatherUsageStats") + 1] == "false"

    forbidden_fragments = [
        "0.0.0.0",
        "huggingface.co",
        "api.openai.com",
        "http://",
        "https://",
        "telemetry",
        "analytics",
        "cloud",
    ]
    assert not any(fragment in command_text for fragment in forbidden_fragments)


def test_launcher_command_does_not_include_document_content_or_file_names(monkeypatch):
    launcher = load_launcher_module()
    commands: list[list[str]] = []

    def fake_run_checked(command: list[str]) -> None:
        commands.append(command)

    monkeypatch.setattr(launcher, "run_checked", fake_run_checked)

    launcher.main(["--port", "8502"])

    command_text = " ".join(" ".join(command) for command in commands)
    assert SYNTHETIC_FILENAME not in command_text
    assert SYNTHETIC_CONTENT not in command_text


def test_launcher_source_does_not_write_logs_temp_files_or_packaging_behavior():
    source = LAUNCHER_PATH.read_text(encoding="utf-8")
    lowered = source.lower()

    forbidden_source_fragments = [
        "logging",
        "print(",
        ".write_text",
        ".write_bytes",
        "open(",
        "tempfile",
        "namedtemporaryfile",
        "pyinstaller",
        "tauri",
        "electron",
        "msi",
        "installer",
    ]
    assert not any(fragment in lowered for fragment in forbidden_source_fragments)


def test_local_run_documentation_contains_privacy_boundaries():
    doc = LOCAL_RUN_PATH.read_text(encoding="utf-8")
    lowered = doc.lower()

    assert "hugging face" in lowered
    assert "do not process confidential real documents" in lowered
    assert "127.0.0.1" in doc
    assert "--browser.gatherUsageStats false" in doc
    assert "no real data" in lowered
    assert "synthetic examples" in lowered
    assert "local-only" in lowered or "local runtime" in lowered


def test_local_run_documentation_covers_temp_runtime_limits_and_no_packaging_claim():
    doc = LOCAL_RUN_PATH.read_text(encoding="utf-8")
    lowered = doc.lower()

    assert "runtime privacy expectations" in lowered
    assert "should not pass source document content" in lowered
    assert "should not create application-managed temporary files" in lowered
    assert "write document-content logs" in lowered
    assert "does not add ai processing" in lowered
    assert "cloud document processing" in lowered
    assert "does not prove a full offline or network-traffic guarantee" in lowered
    assert "no installer" in lowered
    assert "pyinstaller" in lowered
    assert "tauri" in lowered
    assert "electron" in lowered
    assert "msi" in lowered
