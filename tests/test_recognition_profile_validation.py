import json
from pathlib import Path

from recognition_profile_validation import build_recognition_profile_validation


VALIDATION_PATH = Path("output/validation/recognition_profile_configuration.json")


def test_recognition_profile_validation_preserves_current_live_options():
    report = build_recognition_profile_validation()

    assert report["schema_version"] == "1.0"
    assert report["profile_count"] == 4
    assert [item["label_nl"] for item in report["current_visible_options"]] == [
        "Juridische controle — streng",
        "Algemene Nederlandse controle",
        "Algemene internationale controle",
    ]
    assert [item["label_nl"] for item in report["target_streamlit_options"]] == [
        "Zorgcontrole — streng",
        "Juridische controle — streng",
        "Algemene Nederlandse controle",
        "Algemene internationale controle",
    ]
    assert [item["label_nl"] for item in report["desktop_short_options"]] == [
        "Algemeen NL",
        "Zorg",
        "Juridisch",
        "Internationaal",
    ]


def test_recognition_profile_validation_keeps_integration_gates_closed():
    report = build_recognition_profile_validation()

    assert report["exact_span_precedence_winner_count"] == 15
    assert report["live_ui_changed"] is False
    assert report["care_recognizers_registered"] is False
    assert report["production_ready"] is False
    assert report["human_review_required"] is True
    assert report["next_workpackage"] == "SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION"


def test_committed_recognition_profile_configuration_is_reproducible():
    committed = json.loads(VALIDATION_PATH.read_text(encoding="utf-8"))
    assert committed == build_recognition_profile_validation()
