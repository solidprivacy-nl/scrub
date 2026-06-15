from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ACTIVE_APP = REPO_ROOT / "presidio_streamlit.py"
CANDIDATE_APP = REPO_ROOT / "presidio_streamlit_collapsible_candidate.py"


def _active_text() -> str:
    return ACTIVE_APP.read_text(encoding="utf-8")


def _candidate_text() -> str:
    return CANDIDATE_APP.read_text(encoding="utf-8")


def test_candidate_file_exists_without_replacing_active_app():
    assert CANDIDATE_APP.exists()
    assert ACTIVE_APP.exists()
    assert CANDIDATE_APP.name != ACTIVE_APP.name


def test_candidate_keeps_review_table_heading_and_collapsible_editor():
    text = _candidate_text()

    assert 'st.subheader("3. Controleer gevonden gegevens")' in text
    assert 'st.expander(f"Vervangtabel controleren — {len(replacement_editor_df.index)} items", expanded=False)' in text
    assert 'key="replacement_editor"' in text
    assert 'st.data_editor(' in text


def test_candidate_preserves_review_table_source_of_truth_copy_and_columns():
    text = _candidate_text()

    for required in [
        "De vervangtabel blijft leidend voor beslissingen en export.",
        '"include"',
        '"remember"',
        '"find"',
        '"replace_with"',
        '"Meenemen"',
        '"Onthouden"',
        '"Gevonden tekst"',
        '"Vervangen door"',
    ]:
        assert required in text


def test_candidate_does_not_change_active_runtime_startup_or_forbidden_features():
    text = _candidate_text().lower()
    active_text = _active_text().lower()

    assert "docker" not in text
    assert "fix_streamlit_nested_expanders" not in text
    assert "monkeypatch" not in text
    assert "click-to-mark" not in text
    assert "advanced editor" not in text
    assert "full-document marking" not in text
    assert 'st.subheader("3. controleer gevonden gegevens")' in active_text


def test_candidate_preserves_download_labels():
    text = _candidate_text()

    for required in [
        "Download opgeschoonde tekst (.txt)",
        "Download vervangtabel (.csv)",
        "Download scrubrapport (.txt)",
        "Download opgeschoond Word-bestand (.docx)",
        "Download opgeschoonde PDF (.pdf)",
    ]:
        assert required in text
