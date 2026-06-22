from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SIDE_BY_SIDE_UI = REPO_ROOT / "side_by_side_review_panel_ui.py"
SERIAL_REVIEW_UI = REPO_ROOT / "serial_review_panel_ui.py"
APP = REPO_ROOT / "presidio_streamlit.py"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_side_by_side_copy_is_clearer_and_still_says_table_is_leading() -> None:
    rendered = _text(SIDE_BY_SIDE_UI)

    assert "Vergelijk links de originele tekst met rechts de gecontroleerde versie." in rendered
    assert "De vervangtabel hieronder blijft leidend." in rendered
    assert "Deze weergave is alleen bedoeld om te vergelijken." in rendered
    assert "Pas beslissingen aan in de vervangtabel hieronder." in rendered
    assert "Visuele hulp bij het controleren" in rendered
    assert "De panelen scrollen samen." in rendered


def test_side_by_side_old_debug_like_copy_is_removed() -> None:
    rendered = _text(SIDE_BY_SIDE_UI)

    assert "Centrale side-by-side reviewweergave" not in rendered
    assert "Alleen visuele hulp. Controleer bij twijfel altijd" not in rendered
    assert "visuele uitlijning iets afwijken" not in rendered


def test_serial_review_copy_is_less_technical() -> None:
    rendered = _text(SERIAL_REVIEW_UI)

    assert '"unresolved": "Nog controleren"' in rendered
    assert '"high_risk": "Risico controleren"' in rendered
    assert '"high_risk_unresolved": "Open risico-items"' in rendered
    assert "Loop de gevonden gegevens één voor één na." in rendered
    assert "Deze hulpweergave verandert niets" in rendered
    assert "Geen extra context beschikbaar. Gebruik de vervangtabel als controlepunt." in rendered
    assert "Context uit de vervangtabel" in rendered
    assert 'metric("Dubbel"' in rendered
    assert 'st.button("Volgende open item"' in rendered


def test_serial_review_old_copy_is_removed() -> None:
    rendered = _text(SERIAL_REVIEW_UI)

    assert "Openstaande items" not in rendered
    assert "Risico-items" not in rendered
    assert "Context preview fallback" not in rendered
    assert "Volgende onopgeloste" not in rendered
    assert "Exact gelijk" not in rendered


def test_copy_polish_does_not_touch_export_or_scrub_key_flow() -> None:
    app_text = _text(APP)

    assert "export_text = apply_replacements_to_text(st_text, edited_replacements)" in app_text
    assert "scrub_key_rows = edited_replacements_df.copy()" in app_text
    assert "build_export_scrub_key(scrub_key_rows)" in app_text
    assert "reinsert_from_scrub_key" in app_text
    assert "reinsert_docx_bytes" in app_text
    assert "reinsert_txt_bytes" in app_text


def test_copy_polish_does_not_add_blocked_features() -> None:
    combined = (_text(SIDE_BY_SIDE_UI) + "\n" + _text(SERIAL_REVIEW_UI) + "\n" + _text(APP)).lower()

    for forbidden in [
        "cloud document processing",
        "custom document editor",
        "contextmenu",
        "right click",
        "click-to-mark",
        "full-document marking",
        "export gate",
        "benchmark gate",
    ]:
        assert forbidden not in combined
