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

    assert 'st.subheader("2. Controleer de tekst")' in app_text
    assert 'st.subheader("Controleer de tekst")' not in side_text


def test_user_facing_side_by_side_copy_exists_and_controls_are_simplified():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    for phrase in [
        "Vergelijk links de brontekst met rechts de verwerkte tekst",
        "Brontekst",
        "Verwerkte tekst",
        "Markeringen tonen",
        "Geel = vervangen of gemaskeerde waarde",
        "De vervangtabel blijft leidend",
        "Alleen visuele hulp",
        "Controleer bij twijfel altijd de vervangtabel hieronder",
        "De panelen scrollen synchroon. Bij grote tekstverschillen kan de visuele uitlijning iets afwijken.",
    ]:
        assert phrase in text

    assert "Markeringen tonen in verwerkte tekst" not in text
    assert "Synchroon scrollen" not in text
    assert "Sync uit: beide panelen scrollen onafhankelijk." not in text
    assert "Must not change source text" not in text


def test_side_by_side_panes_have_equal_height_and_sync_scroll_component():
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
        '"uses_streamlit_components_html": True',
    ]:
        assert required in text

    assert 'id="syncToggle"' not in text
    assert "syncToggle.addEventListener" not in text


def test_marker_toggle_defaults_on_and_stays_report_only():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "side_by_side_review_show_markers" in text
    assert "value=True" in text
    assert '"report_only": True' in text
    assert '"visual_only": True' in text
    assert '"mutation_allowed": False' in text


def test_side_by_side_panel_escapes_document_text_before_component_rendering():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "source_html = escape(source_text)" in text
    assert "else escape(model[\"processed_pane\"][\"text\"])" in text
    assert "_highlighted_processed_inner_html(" in text


def test_highlights_are_integrated_in_side_by_side_right_pane_not_old_duplicate_panel():
    serial_text = SERIAL_PANEL.read_text(encoding="utf-8")
    side_text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "render_review_highlight_toggle_panel(" not in serial_text
    assert "Voorbeeldtekst met optionele markeringen" not in serial_text
    assert "side_by_side_review_show_markers" in side_text
    assert "processed_pane" in side_text
    assert "highlight_spans" in side_text
    assert "processedPane" in side_text


def test_side_by_side_panel_avoids_repeated_visible_gemarkeerd_labels():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert ">Gemarkeerd<" not in text
    assert "Gemarkeerd:</" not in text
    assert "::before" not in text
    assert "compact_legend" in text
    assert "aria-label=\"gemarkeerde vervanging\"" in text


def test_side_by_side_panel_preserves_existing_review_table_and_serial_review_boundaries():
    text = _normal_review_flow_text().lower()

    assert "replacement_editor" in text
    assert "stap voor stap controleren" in text
    assert "expanded=false" in text
    assert "controleer gevonden gegevens één voor één" in text
    assert "side-by-side review" in text

    assert "serial review — experimentele reviewhulp" not in text
    assert "table-first baseline" not in text
    assert "no scrub key mutation" not in text
    assert "no export blocking" not in text
    assert "no reinsert behavior change" not in text


def test_side_by_side_panel_does_not_add_blocked_flow_mutations():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8").lower()

    forbidden = [
        "st.download_button",
        "download_button(",
        "scrub_key_to_json(",
        "build_scrub_key(",
        "validate_scrub_key(",
        "reinsert_from_scrub_key(",
        "reinsert_docx_bytes(",
        "reinsert_txt_bytes(",
        "apply_replacements_to_text(",
        "save_remembered_replacements(",
        "clear_remembered_replacements(",
        "click-to-mark",
        "advanced editor",
        "full-document marking",
        "automatic_replacement = true",
        "review_table_mutation = true",
        "fetch(",
        "xmlhttprequest",
        "localstorage",
        "sessionstorage",
    ]
    for marker in forbidden:
        assert marker not in text


def test_side_by_side_panel_returns_report_only_contract():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    for required in [
        '"report_only": True',
        '"visual_only": True',
        '"mutation_allowed": False',
        '"review_table_mutation": False',
        '"replacement_mutation": False',
        '"scrub_key_writes": False',
        '"export_download_behavior_change": False',
        '"reinsert_behavior_change": False',
    ]:
        assert required in text


def test_existing_highlight_panel_helper_assets_are_preserved_for_compatibility():
    text = HIGHLIGHT_PANEL.read_text(encoding="utf-8")

    assert "def build_preview_text(" in text
    assert "def render_review_highlight_toggle_panel(" in text
    assert "build_highlighted_preview_html" in text


def test_side_by_side_ui_patch_tests_use_synthetic_values_only():
    rendered = Path(__file__).read_text(encoding="utf-8")
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
        "Fatima " + "El " + "Amrani",
        "Peter " + "Bakker",
    ]

    assert "synthetic" in rendered.lower()
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
