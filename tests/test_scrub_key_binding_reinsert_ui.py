from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "reinsert_mode_ui.py"
STATUS_HELPER = ROOT / "scrub_key_binding_reinsert_status.py"


def _ui_text() -> str:
    return UI.read_text(encoding="utf-8")


def test_ui_uses_pure_binding_status_model() -> None:
    text = _ui_text()

    assert "from scrub_key_binding_reinsert_status import binding_status_notice" in text
    assert "binding_notice = binding_status_notice(result)" in text
    assert "binding_notice.get('status_label')" in text
    assert 'binding_notice.get("message")' in text
    assert 'binding_notice.get("level")' in text


def test_binding_audit_fields_remain_visible_in_existing_report() -> None:
    text = _ui_text()

    for marker in [
        "Document-/sleutelstatus",
        "Documentmatch geverifieerd",
        "Legacy sleutel zonder binding",
        "Documentcodes in document",
        "Documentcode in sleutel",
        "Mapping-controlewaarde geldig",
        "Bindingwaarschuwingen",
    ]:
        assert marker in text


def test_bound_legacy_and_blocked_statuses_use_existing_feedback_surfaces() -> None:
    text = _ui_text()

    assert 'if binding_notice.get("level") == "success":' in text
    assert 'elif binding_notice.get("level") == "warning":' in text
    assert 'elif binding_notice.get("level") == "error":' in text
    assert "st.success(binding_notice.get(\"message\"))" in text
    assert "st.warning(binding_notice.get(\"message\"))" in text
    assert "st.error(binding_notice.get(\"message\"))" in text


def test_three_step_flow_and_only_final_confidential_acknowledgement_remain() -> None:
    text = _ui_text()

    assert 'st.subheader("1. Voeg het bestand toe dat je wilt herstellen")' in text
    assert 'st.subheader("2. Voeg de bijbehorende Scrub Key toe")' in text
    assert 'st.subheader("3. Download het herstelde resultaat")' in text
    assert "run_reinsert_request(source, active_key)" in text
    assert text.count("st.checkbox(") == 1
    assert "ack_auto_reinsert_download_confidential" in text
    assert "Scrub Key valideren" not in text
    assert "bestand lokaal terugzetten" not in text.lower()


def test_status_helper_and_ui_add_no_cloud_ai_ocr_or_new_output_type() -> None:
    combined = (_ui_text() + "\n" + STATUS_HELPER.read_text(encoding="utf-8")).lower()

    for forbidden in [
        "cloud document processing",
        "ai processing",
        "ocr processing",
        "restored pdf",
        "pdf-to-docx",
        "hmac",
        "signing key",
    ]:
        assert forbidden not in combined
