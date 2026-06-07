from review_summary import (
    build_review_summary,
    review_summary_lines,
    review_summary_markdown,
    review_summary_readiness_label,
)


def test_review_summary_counts_expected_status_groups_and_export_scope():
    rows = [
        {"include": True, "review_status": "auto_detected", "source": "detected"},
        {"include": False, "review_status": "needs_review", "source": "candidate"},
        {"include": True, "review_status": "manual", "source": "manual"},
        {"include": True, "review_status": "remembered", "source": "remembered"},
    ]

    summary = build_review_summary(rows)

    assert summary["total_rows"] == 4
    assert summary["automatically_detected_rows"] == 1
    assert summary["rows_needing_review"] == 1
    assert summary["manually_added_rows"] == 1
    assert summary["remembered_replacement_rows"] == 1
    assert summary["checked_rows_included_in_export"] == 3
    assert summary["unchecked_rows_excluded_from_export"] == 1
    assert summary["open_candidate_warning"] is True
    assert summary["open_candidate_rows"] == 1


def test_review_summary_infers_status_from_dutch_labels_and_source_fallbacks():
    rows = [
        {"include": "ja", "review_status_label": "Automatisch vervangen"},
        {"include": "nee", "review_status_label": "Controle nodig"},
        {"include": "true", "source": "manual"},
        {"include": 1, "entity_type": "REMEMBERED"},
        {"include": 0, "source": "unknown"},
    ]

    summary = build_review_summary(rows)

    assert summary["automatically_detected_rows"] == 1
    assert summary["rows_needing_review"] == 2
    assert summary["manually_added_rows"] == 1
    assert summary["remembered_replacement_rows"] == 1
    assert summary["checked_rows_included_in_export"] == 3
    assert summary["unchecked_rows_excluded_from_export"] == 2


def test_review_summary_ready_label_warns_when_candidates_are_open():
    summary = build_review_summary([
        {"include": True, "review_status": "auto_detected"},
        {"include": False, "review_status": "needs_review"},
    ])

    assert review_summary_readiness_label(summary) == "Controle nodig voor export"
    assert summary["readiness_label"] == "Controle nodig voor export"


def test_review_summary_ready_label_handles_empty_and_unselected_states():
    empty_summary = build_review_summary([])
    unselected_summary = build_review_summary([
        {"include": False, "review_status": "auto_detected"},
    ])

    assert review_summary_readiness_label(empty_summary) == "Geen vervangregels gevonden"
    assert review_summary_readiness_label(unselected_summary) == "Niet klaar voor export"


def test_review_summary_lines_and_markdown_are_user_facing_dutch():
    summary = build_review_summary([
        {"include": True, "review_status": "auto_detected"},
        {"include": False, "review_status": "needs_review"},
    ])

    lines = review_summary_lines(summary)
    markdown = review_summary_markdown(summary)

    assert "Totaal aantal regels: 2" in lines
    assert "Meegenomen in export: 1" in lines
    assert "Niet meegenomen in export: 1" in lines
    assert any("Let op:" in line for line in lines)
    assert "- Controle nodig: 1" in markdown
