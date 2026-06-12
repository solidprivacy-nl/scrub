from pathlib import Path

PLAN = Path("REPLACE_LOGIC_UI_PLAN.md").read_text(encoding="utf-8")


def test_plan_maps_ui_actions_to_helper_states():
    for marker in [
        "accepted",
        "edited",
        "ignored",
        "manual_added",
        "preserve_context",
        "unresolved",
    ]:
        assert marker in PLAN


def test_plan_keeps_scope_controls_conservative():
    for marker in [
        "this_occurrence",
        "all_exact",
        "all_normalized",
        "No fuzzy matching or guessed intent is allowed.",
        "Default scope is `this_occurrence`.",
    ]:
        assert marker in PLAN


def test_plan_keeps_scrub_key_and_export_boundaries():
    for marker in [
        "This UI plan does not approve export blocking.",
        "The first UI plan must not change Scrub Key behavior.",
        "changing Scrub Key schema",
        "changing placeholder format",
    ]:
        assert marker in PLAN


def test_plan_does_not_approve_streamlit_implementation():
    for marker in [
        "This plan does not change:",
        "presidio_streamlit.py",
        "fix_streamlit_nested_expanders.py",
        "review table behavior",
        "export/download behavior",
        "helper runtime behavior",
    ]:
        assert marker in PLAN


def test_plan_requires_contract_tests_before_ui_implementation():
    assert "WP_REPLACE_LOGIC_UI_CONTRACT_TESTS" in PLAN
    assert "Only after that should a small UI implementation package be considered." in PLAN
