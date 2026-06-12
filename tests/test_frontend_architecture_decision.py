from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DECISION = REPO_ROOT / "FRONTEND_ARCHITECTURE_DECISION.md"


def _text() -> str:
    return DECISION.read_text(encoding="utf-8")


def test_wp43_keeps_streamlit_for_mvp_and_rejects_frontend_migration_now():
    text = _text().lower()

    assert "keep streamlit as the mvp validation surface for now" in text
    assert "do not migrate to a separate frontend yet" in text
    assert "do not build a professional document editor yet" in text
    assert "stay with streamlit for mvp validation" in text


def test_wp43_requires_thin_ui_and_helper_first_architecture():
    text = _text().lower()

    assert "thin ui patch layer" in text
    assert "reusable python helper modules" in text
    assert "contract tests before ui integration" in text
    assert "helper/model and tests before ui integration" in text
    assert "the ui should stay thin" in text


def test_wp43_blocks_unapproved_professional_document_editor_features():
    text = _text().lower()

    for required in [
        "a broad professional document editor",
        "click-to-mark sensitive text as an authoritative workflow",
        "complex synchronized multi-pane editing",
        "word/pdf layout rendering",
        "long-document virtualized review",
        "export blocking based on ui-only state",
        "direct scrub key mutation from new panels",
        "replacing the current review table without a separate migration plan",
    ]:
        assert required in text


def test_wp43_sets_frontend_reconsideration_criteria():
    text = _text().lower()

    assert "when to reconsider a separate frontend" in text
    assert "document-centric review needs interaction beyond static/read-only aids" in text
    assert "users validate the need" in text
    assert "mvp logic is stable enough" in text
    assert "profiles, batch review or enterprise deployment" in text


def test_wp43_preserves_privacy_and_local_first_boundaries():
    text = _text().lower()

    for required in [
        "python core remains source of truth",
        "api boundary is local-first",
        "no cloud document processing",
        "no hidden telemetry",
        "review/export/scrub key actions stay explicit and auditable",
        "no real-data fixtures",
    ]:
        assert required in text


def test_wp43_does_not_close_wp42d_verification_or_change_ui():
    text = _text().lower()

    assert "wp43 does not validate or close wp42d" in text
    assert "wp42d remains pending" in text
    for required in [
        "does not change:",
        "presidio_streamlit.py",
        "fix_streamlit_nested_expanders.py",
        "any streamlit patch file",
        "review table behavior",
        "export/download behavior",
        "scrub key behavior",
        "reinsert behavior",
        "helper runtime behavior",
        "dependencies",
        "docker/runtime behavior",
        "cloud processing",
        "real-data fixtures",
    ]:
        assert required in text
