from __future__ import annotations

from pathlib import Path

PATCH = Path("fix_streamlit_static_highlight_preview.py")
DOCKERFILE = Path("Dockerfile")


def _patch_text() -> str:
    return PATCH.read_text(encoding="utf-8")


def test_static_highlight_preview_startup_patch_is_disabled_noop():
    text = _patch_text()

    assert "WP42D-ROLLBACK" in text
    assert "intentionally a no-op" in text
    assert "Static highlight preview startup patch disabled" in text
    assert "presidio_streamlit.py" in text
    assert "mutating" in text


def test_static_highlight_preview_patch_no_longer_mutates_app_source():
    text = _patch_text()

    forbidden = [
        "APP_FILE.write_text",
        "replace_once(",
        "build_static_highlight_preview",
        "st.markdown",
        "with st.expander",
        "unsafe_allow_html=True",
        "edited_replacements_df = st.data_editor",
        "Documentvoorbeeld met markeringen — experimenteel",
    ]
    for phrase in forbidden:
        assert phrase not in text


def test_dockerfile_does_not_run_static_highlight_preview_patch():
    text = DOCKERFILE.read_text(encoding="utf-8")

    assert "python fix_streamlit_nested_expanders.py" in text
    assert "python fix_streamlit_pdf_text_reinsert.py" in text
    assert "python fix_streamlit_static_highlight_preview.py" not in text
    assert "streamlit run presidio_streamlit.py" in text


def test_rollback_preserves_runtime_boundaries():
    docker_text = DOCKERFILE.read_text(encoding="utf-8")
    patch_text = _patch_text()

    assert "WP42D-ROLLBACK" in docker_text
    assert "restore" not in patch_text.lower()
    assert "export" not in patch_text.lower()
    assert "Scrub Key" not in patch_text
    assert "reinsert" not in patch_text.lower()
    assert "cloud" not in patch_text.lower()
    assert "real" not in patch_text.lower()
