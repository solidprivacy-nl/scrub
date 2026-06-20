from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP = REPO_ROOT / "presidio_streamlit.py"
RENDERER = REPO_ROOT / "serial_review_panel_ui.py"
DOCKERFILE = REPO_ROOT / "Dockerfile"


def _combined_ui_text() -> str:
    return APP.read_text(encoding="utf-8") + "\n" + RENDERER.read_text(encoding="utf-8")


def test_presidio_uses_safe_serial_review_panel_renderer_and_view_model():
    app_text = APP.read_text(encoding="utf-8")
    renderer_text = RENDERER.read_text(encoding="utf-8")

    assert "from serial_review_panel_ui import render_serial_review_panel" in app_text
    assert "render_serial_review_panel(" in app_text
    assert "from review_panel_view_model import build_review_panel_view_model" in renderer_text
    assert "build_review_panel_view_model(" in renderer_text


def test_serial_review_panel_visible_text_and_safety_message_exist():
    text = _combined_ui_text()

    assert "Stap voor stap controleren" in text
    assert "expanded=False" in text
    assert "Controleer gevonden gegevens één voor één" in text
    assert "De vervangtabel blijft leidend voor beslissingen en export" in text
    assert "Gevonden waarde" in text
    assert "Voorgestelde vervanging" in text
    assert "Status" in text
    assert "Risico’s" in text
    assert "Context" in text

    assert "Serial review — experimentele reviewhulp" not in text
    assert "Alleen-lezen hulpweergave" not in text
    assert "De bestaande vervangtabel blijft leidend" not in text


def test_serial_review_panel_navigation_labels_exist():
    text = _combined_ui_text()

    assert "Vorige" in text
    assert "Volgende" in text
    assert "Volgende onopgeloste" in text
    assert "serial_review_current_index" in text
    assert "serial_review_current_occurrence_id" in text
    assert "serial_review_filter_mode" in text
    assert "Filter voor stap-voor-stap controle" in text


def test_serial_review_panel_boundary_contract_remains_in_code_but_not_primary_caption():
    text = _combined_ui_text()
    renderer_text = RENDERER.read_text(encoding="utf-8")

    assert "table-first baseline" not in text
    assert "no Scrub Key mutation" not in text
    assert "no export blocking" not in text
    assert "no reinsert behavior change" not in text

    for phrase in [
        "does not mutate review",
        "does not write Scrub Key mappings",
        "block export",
        "change reinsert behavior",
    ]:
        assert phrase in renderer_text


def test_serial_review_ui_does_not_reintroduce_static_highlight_startup_mutation():
    docker_text = DOCKERFILE.read_text(encoding="utf-8")
    app_text = APP.read_text(encoding="utf-8")

    assert "fix_streamlit_static_highlight_preview.py" not in docker_text
    assert "Documentvoorbeeld met markeringen" not in app_text
    assert "static highlight preview" not in app_text.lower()


def test_serial_review_ui_does_not_implement_blocked_editor_or_marking_features():
    renderer_text = RENDERER.read_text(encoding="utf-8").lower()

    assert "click-to-mark" not in renderer_text
    assert "advanced editor" not in renderer_text
    assert "unsafe_allow_html" not in renderer_text
    assert "export_blocking = true" not in renderer_text
    assert "scrub_key_mapping_written = true" not in renderer_text


def test_serial_review_ui_tests_use_synthetic_boundaries_only():
    rendered = RENDERER.read_text(encoding="utf-8") + "\n" + Path(__file__).read_text(encoding="utf-8")
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]

    assert "SYNTHETIC" in rendered or "synthetic" in rendered.lower()
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
