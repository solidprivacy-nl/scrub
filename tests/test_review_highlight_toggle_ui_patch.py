from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SERIAL_RENDERER = REPO_ROOT / "serial_review_panel_ui.py"
TOGGLE_RENDERER = REPO_ROOT / "review_highlight_toggle_panel_ui.py"
SIDE_BY_SIDE_RENDERER = REPO_ROOT / "side_by_side_review_panel_ui.py"
HELPER = REPO_ROOT / "review_highlight_toggle.py"
APP = REPO_ROOT / "presidio_streamlit.py"


def _combined_text() -> str:
    return "\n".join(
        [
            SERIAL_RENDERER.read_text(encoding="utf-8"),
            TOGGLE_RENDERER.read_text(encoding="utf-8"),
            SIDE_BY_SIDE_RENDERER.read_text(encoding="utf-8"),
            HELPER.read_text(encoding="utf-8"),
        ]
    )


def test_review_highlight_toggle_is_now_reached_through_side_by_side_panel():
    serial_text = SERIAL_RENDERER.read_text(encoding="utf-8")
    side_by_side_text = SIDE_BY_SIDE_RENDERER.read_text(encoding="utf-8")

    assert "from side_by_side_review_panel_ui import render_side_by_side_review_panel" in serial_text
    assert "render_side_by_side_review_panel(" in serial_text
    assert "render_review_highlight_toggle_panel(" not in serial_text
    assert "Markeringen tonen in verwerkte tekst" in side_by_side_text
    assert "side_by_side_review_show_markers" in side_by_side_text
    assert "review_highlight_toggle_show_markers" not in APP.read_text(encoding="utf-8")


def test_legacy_review_highlight_toggle_renderer_assets_are_preserved():
    text = TOGGLE_RENDERER.read_text(encoding="utf-8")

    assert "Voorbeeldtekst met optionele markeringen" in text
    assert "Markeringen tonen in voorbeeldtekst" in text
    assert "review_highlight_toggle_show_markers" in text
    assert "Gecontroleerde voorbeeldtekst" in text
    assert "Geen gemarkeerde vervangingen beschikbaar in deze voorbeeldtekst." in text
    assert "def build_preview_text(" in text


def test_review_highlight_toggle_visible_boundaries_exist():
    text = _combined_text().lower()

    for required in [
        "alleen een visuele hulp",
        "niets aan de vervangtabel",
        "niets aan export",
        "niets aan scrub key",
        "read-only",
        "visual-only",
        "non-mutating",
        "table-first baseline",
        "no scrub key writes",
        "no export/download changes",
        "no reinsert behavior change",
    ]:
        assert required in text


def test_review_highlight_toggle_uses_safe_escaped_html_helper():
    text = _combined_text()
    lowered = text.lower()

    assert "build_highlighted_preview_html" in text
    assert "html.escape" in text
    assert "unsafe_allow_html=True" in text
    assert "raw document text is never inserted into html unescaped" in lowered
    assert "unsafe raw html" not in lowered


def test_review_highlight_toggle_does_not_add_mutating_or_blocked_behavior():
    lowered = _combined_text().lower()

    for forbidden in [
        "fix_streamlit_static_highlight_preview.py",
        "click-to-mark",
        "advanced editor",
        "full-document marking",
        "export_blocking = true",
        "scrub_key_mapping_written = true",
        "st.download_button",
        "save_remembered_replacements",
        "clear_remembered_replacements",
    ]:
        assert forbidden not in lowered


def test_review_highlight_toggle_return_contract_is_report_only():
    text = TOGGLE_RENDERER.read_text(encoding="utf-8")

    for required in [
        '"report_only": True',
        '"visual_only": True',
        '"mutation_allowed": False',
        '"table_mutation": False',
        '"scrub_key_writes": False',
        '"export_download_changes": False',
        '"reinsert_behavior_change": False',
    ]:
        assert required in text


def test_review_highlight_toggle_ui_tests_use_synthetic_values_only():
    rendered = _combined_text() + "\n" + Path(__file__).read_text(encoding="utf-8")
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]

    assert "synthetic" in rendered.lower()
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
