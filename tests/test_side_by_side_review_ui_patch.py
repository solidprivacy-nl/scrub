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


def test_side_by_side_panel_is_connected_through_existing_serial_review_route():
    app_text = APP.read_text(encoding="utf-8")
    serial_text = SERIAL_PANEL.read_text(encoding="utf-8")

    assert "from serial_review_panel_ui import render_serial_review_panel" in app_text
    assert "render_serial_review_panel(" in app_text
    assert "from side_by_side_review_panel_ui import render_side_by_side_review_panel" in serial_text
    assert "render_side_by_side_review_panel(" in serial_text


def test_side_by_side_panel_uses_helper_model_and_existing_preview_logic():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "from side_by_side_review import build_side_by_side_review_model" in text
    assert "from review_highlight_toggle_panel_ui import build_preview_text" in text
    assert "build_side_by_side_review_model(" in text
    assert "build_preview_text(" in text
    assert SIDE_BY_SIDE_HELPER.exists()


def test_user_facing_side_by_side_copy_exists():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    for phrase in [
        "Controleer de tekst",
        "Vergelijk links de brontekst met rechts de verwerkte tekst",
        "Brontekst",
        "Verwerkte tekst",
        "Markeringen tonen in verwerkte tekst",
        "Geel = vervangen of gemaskeerde waarde",
        "De vervangtabel blijft leidend",
        "Alleen visuele hulp",
        "Must not change source text, review table state, export payloads, Scrub Key state or reinsert behavior",
    ]:
        assert phrase in text


def test_side_by_side_panes_have_equal_height_and_local_processed_scroll():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "SIDE_BY_SIDE_REVIEW_PANE_HEIGHT = 320" in text
    assert "height: {SIDE_BY_SIDE_REVIEW_PANE_HEIGHT}px" in text
    assert "max-height: {SIDE_BY_SIDE_REVIEW_PANE_HEIGHT}px" in text
    assert "min-height: {SIDE_BY_SIDE_REVIEW_PANE_HEIGHT}px" in text
    assert "overflow-y: auto" in text
    assert "height=SIDE_BY_SIDE_REVIEW_PANE_HEIGHT" in text
    assert '"pane_height": SIDE_BY_SIDE_REVIEW_PANE_HEIGHT' in text
    assert '"processed_pane_scrolls_independently": True' in text


def test_highlights_are_integrated_in_side_by_side_right_pane_not_old_duplicate_panel():
    serial_text = SERIAL_PANEL.read_text(encoding="utf-8")
    side_text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "render_review_highlight_toggle_panel(" not in serial_text
    assert "Voorbeeldtekst met optionele markeringen" not in serial_text
    assert "side_by_side_review_show_markers" in side_text
    assert "processed_pane" in side_text
    assert "highlight_spans" in side_text
    assert "right_column" in side_text


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
    assert "serial review — experimentele reviewhulp" in text
    assert "table-first baseline" in text
    assert "no scrub key mutation" in text
    assert "no export blocking" in text
    assert "no reinsert behavior change" in text
    assert "side-by-side review" in text


def test_side_by_side_panel_does_not_add_blocked_behaviors_or_flow_mutations():
    text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8").lower()

    forbidden = [
        "streamlit.components",
        "components.html",
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
        "synchronized scroll implementation",
        "click-to-mark",
        "advanced editor",
        "full-document marking",
        "automatic_replacement = true",
        "review_table_mutation = true",
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
        '"synchronized_scroll_implementation": False',
        '"custom_component_rendering": False',
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
