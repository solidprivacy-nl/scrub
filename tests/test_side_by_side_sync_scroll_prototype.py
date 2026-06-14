from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROTOTYPE = REPO_ROOT / "prototypes" / "side_by_side_sync_scroll_prototype.html"
NOTE = REPO_ROOT / "SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE.md"
APP = REPO_ROOT / "presidio_streamlit.py"
SERIAL_PANEL = REPO_ROOT / "serial_review_panel_ui.py"
SIDE_BY_SIDE_PANEL = REPO_ROOT / "side_by_side_review_panel_ui.py"


def _prototype_text() -> str:
    return PROTOTYPE.read_text(encoding="utf-8")


def test_sync_scroll_prototype_file_exists_and_is_isolated_html():
    text = _prototype_text()

    assert PROTOTYPE.exists()
    assert "<!doctype html>" in text.lower()
    assert "Side-by-side synchronized scroll prototype" in text
    assert "Prototype-only" in text
    assert "Niet gekoppeld aan de normale Scrub Legal-flow" in text


def test_sync_scroll_prototype_has_two_panes_and_toggle():
    text = _prototype_text()

    for required in [
        'id="sourcePane"',
        'id="processedPane"',
        'id="syncToggle"',
        "Synchroon scrollen",
        "Brontekst",
        "Verwerkte tekst",
        "Geel = vervangen of gemaskeerde waarde",
    ]:
        assert required in text


def test_sync_scroll_prototype_contains_bidirectional_percentage_sync():
    text = _prototype_text()

    for required in [
        "function scrollRatio(element)",
        "function setScrollRatio(element, ratio)",
        "function syncScroll(fromPane, toPane)",
        "sourcePane.addEventListener('scroll'",
        "processedPane.addEventListener('scroll'",
        "window.requestAnimationFrame",
        "element.scrollTop = ratio * maxScroll",
    ]:
        assert required in text


def test_sync_scroll_prototype_has_fallback_and_risk_warning():
    text = _prototype_text()

    for required in [
        "Sync uit: beide panelen scrollen onafhankelijk.",
        "kan valse uitlijning geven",
        "werkend concept, geen productiefeature",
        "Fallback: zet sync uit",
    ]:
        assert required in text


def test_sync_scroll_prototype_uses_synthetic_content_only():
    text = _prototype_text()

    assert "SYNTHETIC_DAMAGE_001" in text
    assert "[PERSOON_01]" in text
    assert "synthetische" in text.lower()

    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "Fatima " + "El " + "Amrani",
        "Peter " + "Bakker",
        "123" + "456" + "782",
    ]
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in text


def test_sync_scroll_prototype_file_is_not_loaded_by_normal_app_flow():
    prototype_path = "prototypes/side_by_side_sync_scroll_prototype.html"
    production_text = "\n".join(
        [
            APP.read_text(encoding="utf-8"),
            SERIAL_PANEL.read_text(encoding="utf-8"),
            SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8"),
        ]
    )

    assert prototype_path not in production_text


def test_sync_scroll_concept_is_now_integrated_through_safe_renderer_not_prototype_file():
    production_text = SIDE_BY_SIDE_PANEL.read_text(encoding="utf-8")

    assert "syncToggle" not in production_text
    assert "sync_scroll_always_on" in production_text
    assert "sync_scroll_visible_checkbox" in production_text
    assert "sourcePane.addEventListener('scroll'" in production_text
    assert "processedPane.addEventListener('scroll'" in production_text
    assert "_side_by_side_sync_scroll_html" in production_text
    assert "prototypes/side_by_side_sync_scroll_prototype.html" not in production_text


def test_sync_scroll_prototype_does_not_touch_production_behavior_markers():
    text = _prototype_text().lower()

    forbidden = [
        "scrub_key_to_json(",
        "build_scrub_key(",
        "reinsert_from_scrub_key(",
        "reinsert_docx_bytes(",
        "reinsert_txt_bytes(",
        "st.download_button",
        "download_button(",
        "save_remembered_replacements(",
        "clear_remembered_replacements(",
        "apply_replacements_to_text(",
    ]
    for marker in forbidden:
        assert marker not in text


def test_sync_scroll_prototype_note_records_boundary():
    note = NOTE.read_text(encoding="utf-8")

    assert "prototype-only" in note
    assert "not connected to the normal Scrub Legal app flow" in note
    assert "It uses only synthetic content" in note
    assert "does not prove that source and processed passages always match semantically" in note
