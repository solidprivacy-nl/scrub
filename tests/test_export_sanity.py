from copy import deepcopy

from export_sanity import (
    build_export_sanity_checks,
    export_sanity_ready_label,
    export_sanity_warnings,
)


def test_export_sanity_all_rows_selected_and_no_candidates_open():
    rows = [
        {"include": True, "review_status": "auto_detected", "source": "detected"},
        {"include": "ja", "review_status": "manual", "source": "manual"},
    ]

    summary = build_export_sanity_checks(rows)
    warnings = export_sanity_warnings(summary)

    assert summary["unchecked_control_needed_rows"] == 0
    assert summary["candidate_rows_not_included"] == 0
    assert summary["no_replacements_selected"] is False
    assert summary["blocks_export"] is False
    assert summary["changes_export_semantics"] is False
    assert export_sanity_ready_label(summary) == "Klaar voor export na gebruikerscontrole"
    assert not any("Controle nodig' staan niet aangevinkt" in warning for warning in warnings)
    assert any("Gebruikerscontrole blijft nodig" in warning for warning in warnings)
    assert any("geen garantie op volledige anonimisering" in warning for warning in warnings)


def test_export_sanity_warns_about_unchecked_control_needed_rows():
    rows = [
        {"include": True, "review_status": "auto_detected"},
        {"include": False, "review_status_label": "Controle nodig"},
    ]

    summary = build_export_sanity_checks(rows)
    warnings = export_sanity_warnings(summary)

    assert summary["unchecked_control_needed_rows"] == 1
    assert export_sanity_ready_label(summary) == "Controle nodig vóór export"
    assert any("1 regel(s) met 'Controle nodig'" in warning for warning in warnings)


def test_export_sanity_warns_about_candidate_rows_not_included():
    rows = [
        {"include": True, "review_status": "auto_detected", "source": "detected"},
        {"include": False, "review_status": "needs_review", "source": "candidate"},
    ]

    summary = build_export_sanity_checks(rows)
    warnings = export_sanity_warnings(summary)

    assert summary["candidate_rows_not_included"] == 1
    assert any("1 mogelijke kandidaatwaarde(n)" in warning for warning in warnings)
    assert any("Niet-aangevinkte kandidaten" in warning for warning in warnings)


def test_export_sanity_warns_when_no_selected_replacements():
    rows = [
        {"include": False, "review_status": "auto_detected"},
        {"include": "nee", "review_status": "manual"},
    ]

    summary = build_export_sanity_checks(rows)
    warnings = export_sanity_warnings(summary)

    assert summary["checked_rows_included_in_export"] == 0
    assert summary["no_replacements_selected"] is True
    assert export_sanity_ready_label(summary) == "Geen vervangingen geselecteerd"
    assert any("geen vervangingen geselecteerd" in warning.lower() for warning in warnings)


def test_export_sanity_handles_empty_table():
    summary = build_export_sanity_checks([])
    warnings = export_sanity_warnings(summary)

    assert summary["total_rows"] == 0
    assert summary["no_replacements_selected"] is True
    assert export_sanity_ready_label(summary) == "Geen vervangregels gevonden — controleer handmatig"
    assert any("geen vervangingen geselecteerd" in warning.lower() for warning in warnings)
    assert any("Downloaden blijft mogelijk" in warning for warning in warnings)


def test_export_sanity_warning_text_is_dutch_and_user_facing():
    rows = [
        {"include": False, "review_status_label": "Controle nodig", "source": "candidate"},
    ]

    warnings = export_sanity_warnings(rows)
    joined = " ".join(warnings)

    assert "Let op" in joined
    assert "Controleer" in joined or "controleer" in joined
    assert "Gebruikerscontrole blijft nodig" in joined
    assert "geen garantie op volledige anonimisering" in joined
    assert "export" in joined.lower()
    assert "blocks_export" not in joined
    assert "review_status" not in joined


def test_export_sanity_does_not_mutate_input_rows():
    rows = [
        {"include": False, "review_status_label": "Controle nodig", "source": "candidate"},
        {"include": True, "review_status": "manual", "source": "manual"},
    ]
    original = deepcopy(rows)

    build_export_sanity_checks(rows)
    export_sanity_warnings(rows)
    export_sanity_ready_label(rows)

    assert rows == original
