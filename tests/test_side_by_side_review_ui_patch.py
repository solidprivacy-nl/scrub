from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP = REPO_ROOT / "presidio_streamlit.py"
SERIAL_PANEL = REPO_ROOT / "serial_review_panel_ui.py"
SIDE_BY_SIDE_PANEL = REPO_ROOT / "side_by_side_review_panel_ui.py"
SIDE_BY_SIDE_HELPER = REPO_ROOT / "side_by_side_review.py"
HIGHLIGHT_PANEL = REPO_ROOT / "review_highlight_toggle_panel_ui.py"


def _normal_review_flow_text() -> str:
    return "\n".join(
        [
            APP.read_text(encoding="utf-8"),
            SERIAL_PANEL.read_text(encoding="utf-8"),
            SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8"),
        ]
    )


def test_side_by_side_panel_is_connected_through_existing_review_route():
    app_text = APP.read_text(encoding="utf-8")
    serial_text = SERIAL_PANEL.read_text(encoding="utf-8")

    assert "from side_by_side_review_panel_ui import render_side_by_side_review_panel" in app_text
    assert "render_side_by_side_review_panel(" in app_text
    assert "from serial_review_panel_ui import render_serial_review_panel" in app_text
    assert "from side_by_side_review_panel_ui import render_side_by_side_review_panel" in serial_text


def test_side_by_side_panel_uses_helper_model_and_existing_preview_logic():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "from side_by_side_review import build_side_by_side_review_model" in text
    assert "from review_highlight_toggle_panel_ui import build_preview_text" in text
    assert "build_side_by_side_review_model(" in text
    assert "build_preview_text(" in text
    assert SIDE_BY_SIDE_HELPER.exists()


def test_central_step_heading_is_not_duplicated_inside_side_by_side_component():
    app_text = APP.read_text(encoding="utf-8")
    side_text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert 'st.subheader("2. Controleer resultaat")' in app_text
    assert 'st.subheader("Controleer de tekst")' not in side_text


def test_user_facing_side_by_side_copy_exists_and_controls_are_simplified():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    for phrase in [
        "Controleer links de brontekst en rechts de verwerkte tekst",
        "Selecteer rechts een gemiste waarde",
        "Brontekst",
        "Verwerkte tekst",
        "Markeringen tonen",
        "Geel = vervangen of gemaskeerde waarde",
        "Twijfel je over een waarde?",
        "Elke toevoeging blijft zichtbaar en aanpasbaar in de vervangtabel",
        "Masker selectie",
        "De panelen scrollen samen. Bij grote tekstverschillen kan de uitlijning iets afwijken.",
    ]:
        assert phrase in text

    assert "Markeringen tonen in verwerkte tekst" not in text
    assert "Synchroon scrollen" not in text
    assert "Sync uit: beide panelen scrollen onafhankelijk." not in text
    assert "Must not change source text" not in text


def test_side_by_side_panes_have_equal_height_and_static_fallback():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "SIDE_BY_SIDE_REVIEW_PANE_HEIGHT = 320" in text
    assert "SIDE_BY_SIDE_REVIEW_COMPONENT_HEIGHT = 410" in text
    assert "height: {SIDE_BY_SIDE_REVIEW_PANE_HEIGHT}px" in text
    assert "max-height: {SIDE_BY_SIDE_REVIEW_PANE_HEIGHT}px" in text
    assert "min-height: {SIDE_BY_SIDE_REVIEW_PANE_HEIGHT}px" in text
    assert "overflow-y: auto" in text
    assert "components.html(" in text
    assert "height=SIDE_BY_SIDE_REVIEW_COMPONENT_HEIGHT" in text
    assert '"pane_height": SIDE_BY_SIDE_REVIEW_PANE_HEIGHT' in text
    assert '"static_fallback_available": True' in text


def test_side_by_side_panel_keeps_bidirectional_sync_scroll_without_visible_toggle():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    for required in [
        "import streamlit.components.v1 as components",
        'id="sourcePane"',
        'id="processedPane"',
        "function scrollRatio(element)",
        "function setScrollRatio(element, ratio)",
        "function syncScroll(fromPane, toPane)",
        "sourcePane.addEventListener('scroll'",
        "processedPane.addEventListener('scroll'",
        "window.requestAnimationFrame",
        "element.scrollTop = ratio * maxScroll",
        '"synchronized_scroll_implementation": True',
        '"sync_scroll_percentage_based": True',
        '"sync_scroll_always_on": True',
        '"sync_scroll_visible_checkbox": False',
        '"uses_streamlit_components_html": static_fallback_used',
    ]:
        assert required in text

    assert 'id="syncToggle"' not in text
    assert "syncToggle.addEventListener" not in text


def test_marker_toggle_defaults_on_and_renderer_never_mutates_rows():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "side_by_side_review_show_markers" in text
    assert "value=True" in text
    assert '"report_only": False' in text
    assert '"visual_only": False' in text
    assert '"mutation_allowed": False' in text
    assert '"review_table_mutation": False' in text


def test_side_by_side_panel_escapes_static_fallback_and_uses_safe_component():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "source_html = escape(source_text)" in text
    assert "else escape(processed_text)" in text
    assert "_highlighted_processed_inner_html(" in text
    assert "render_processed_text_selection_component(" in text


def test_highlights_are_integrated_in_side_by_side_right_pane_not_old_duplicate_panel():
    serial_text = SERIAL_PANEL.read_text(encoding="utf-8")
    side_text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "render_review_highlight_toggle_panel(" not in serial_text
    assert "Voorbeeldtekst met optionele markeringen" not in serial_text
    assert "side_by_side_review_show_markers" in side_text
    assert "processed_pane" in side_text
    assert "highlight_spans" in side_text
