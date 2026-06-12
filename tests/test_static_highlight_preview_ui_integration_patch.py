from __future__ import annotations

from pathlib import Path

PATCH = Path("fix_streamlit_static_highlight_preview.py")
DOCKERFILE = Path("Dockerfile")


def _patch_text() -> str:
    return PATCH.read_text(encoding="utf-8")


def test_static_highlight_preview_patch_exists_and_is_bounded():
    text = _patch_text()

    assert "WP42D" in text
    assert "read-only Streamlit preview panel" in text
    assert "does not mutate review rows" in text
    assert "change export/download behavior" in text
    assert "change Scrub Key behavior" in text
    assert "change reinsert" in text
    assert "call cloud services" in text
    assert "real-data fixtures" in text


def test_static_highlight_preview_patch_imports_helper_once_with_fallback_guard():
    text = _patch_text()

    assert "from highlight_preview import build_static_highlight_preview" in text
    assert "if 'from highlight_preview import build_static_highlight_preview\\n' not in text" in text
    assert "from scrub_key_pdf_text_reinsert import reinsert_pdf_text_bytes" in text
    assert "from scrub_key_document_reinsert import reinsert_docx_bytes, reinsert_txt_bytes" in text


def test_static_highlight_preview_patch_inserts_before_authoritative_editor():
    text = _patch_text()

    assert "Documentvoorbeeld met markeringen — experimenteel" in text
    assert "De vervangtabel blijft leidend" in text
    assert "edited_replacements_df = st.data_editor(" in text
    assert text.index("static_highlight_preview_block") < text.index("APP_FILE.write_text")


def test_static_highlight_preview_patch_uses_helper_gates_before_rendering():
    text = _patch_text()

    required_gates = [
        'highlight_preview_result.get("safe_to_render") is True',
        'highlight_preview_result.get("read_only") is True',
        'highlight_preview_result.get("non_authoritative") is True',
        'highlight_preview_result.get("mutation_allowed") is False',
        'highlight_preview_result.get("export_blocking") is False',
        'highlight_preview_result.get("scrub_key_changes") is False',
    ]
    for gate in required_gates:
        assert gate in text


def test_static_highlight_preview_patch_renders_escaped_text_only():
    text = _patch_text()

    assert 'highlight_preview_segment.get("escaped_text", "")' in text
    assert "unsafe_allow_html=True" in text
    assert 'highlight_preview_segment.get("text"' not in text
    assert "external JavaScript" not in text


def test_static_highlight_preview_patch_keeps_preview_non_authoritative():
    text = _patch_text()

    assert "Niet bepalend voor export" in text
    assert "Static preview only; the review table remains authoritative." in text
    assert "use_container_width" not in text or "st.dataframe" not in text
    assert "download_button" not in text
    assert "scrub_key_to_json" not in text
    assert "reinsert_from_scrub_key" not in text
    assert "st.session_state[" not in text


def test_dockerfile_runs_highlight_patch_after_existing_patches_before_streamlit():
    text = DOCKERFILE.read_text(encoding="utf-8")

    nested = "python fix_streamlit_nested_expanders.py"
    pdf = "python fix_streamlit_pdf_text_reinsert.py"
    highlight = "python fix_streamlit_static_highlight_preview.py"
    streamlit = "streamlit run presidio_streamlit.py"

    assert nested in text
    assert pdf in text
    assert highlight in text
    assert streamlit in text
    assert text.index(nested) < text.index(pdf) < text.index(highlight) < text.index(streamlit)
