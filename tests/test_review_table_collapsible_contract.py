from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP = REPO_ROOT / "presidio_streamlit.py"
CONTRACT = REPO_ROOT / "REVIEW_TABLE_COLLAPSIBLE_CONTRACT.md"
SIDE_BY_SIDE_TEST = REPO_ROOT / "tests" / "test_side_by_side_review_consolidation_dutch_sample.py"


def _app_text() -> str:
    return APP.read_text(encoding="utf-8")


def _contract_text() -> str:
    return CONTRACT.read_text(encoding="utf-8")


def test_contract_defines_collapsible_review_table_heading_with_count_support():
    text = _contract_text()

    assert "Controleer gevonden gegevens" in text
    assert "3. Controleer gevonden gegevens — 34 items" in text
    assert "Controleer gevonden gegevens — {item_count} items" in text
    assert "item count" in text.lower()


def test_contract_preserves_review_table_source_of_truth_and_fallback():
    text = _contract_text().lower()

    for required in [
        "source of truth",
        "fallback",
        "de plek waar include/remember/find/replace_with wordt gecontroleerd",
        "the review table is still authoritative",
        "must not remove or bypass them",
    ]:
        assert required in text


def test_contract_requires_table_and_key_fields_to_remain_available():
    text = _contract_text()

    for required in [
        "replacement_editor",
        "include",
        "remember",
        "find",
        "replace_with",
    ]:
        assert required in text


def test_current_review_table_surface_still_exists_in_app():
    text = _app_text()

    assert 'st.subheader(\"2. Controleer resultaat\")' in text


    assert 'with st.expander(f\"Vervangtabel controleren — {len(replacement_editor_df.index)} items\", expanded=False)' in text
    assert "De vervangtabel blijft leidend" in text
    assert "st.data_editor(" in text
    assert "replacement_editor" in text


def test_current_review_table_keeps_required_columns_and_column_config():
    text = _app_text()

    for required in [
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


def test_export_download_labels_remain_present_in_app():
    text = _app_text()

    for required in [
        "Download opgeschoonde tekst (.txt)",
        "Download vervangtabel (.csv)",
        "Download scrubrapport (.txt)",
        "Download opgeschoond Word-bestand (.docx)",
        "Download opgeschoonde PDF (.pdf)",
    ]:
        assert required in text


def test_contract_forbids_scrub_key_reinsert_export_and_replacement_changes():
    text = _contract_text().lower()

    for required in [
        "export/download behavior changes",
        "export blocking",
        "scrub key writes",
        "scrub key schema changes",
        "reinsert behavior changes",
        "replacement behavior changes",
    ]:
        assert required in text


def test_contract_forbids_editor_and_marking_expansion():
    text = _contract_text().lower()

    for required in [
        "click-to-mark",
        "advanced editor",
        "full-document marking",
    ]:
        assert required in text


def test_contract_requires_future_implementation_gate_and_no_parallel_review_flow_edits():
    text = _contract_text()

    assert "WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION" in text
    assert "must not run in parallel with other `presidio_streamlit.py` review-flow changes" in text


def test_side_by_side_review_contract_still_preserves_table_fallback():
    text = SIDE_BY_SIDE_TEST.read_text(encoding="utf-8")

    assert "replacement_editor" in text
    assert "De vervangtabel blijft leidend" in text
    assert "review table" in text.lower() or "vervangtabel" in text.lower()


def test_no_real_data_fixture_added_for_collapsible_table_contract():
    rendered = "\n".join(
        [
            _contract_text(),
            Path(__file__).read_text(encoding="utf-8"),
        ]
    )
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]

    assert "real-data fixtures" in rendered.lower()
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
