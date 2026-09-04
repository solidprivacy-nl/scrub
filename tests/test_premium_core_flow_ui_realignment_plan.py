from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md"
ROADMAP = ROOT / "ROADMAP.md"
WORKPACKAGES = ROOT / "WORKPACKAGES.md"
DECISIONS = ROOT / "DECISION_LOG.md"
CLAIM = ROOT / "workpackage_claims" / "scrub_wp_premium_core_flow_ui_realignment_plan.md"


def test_plan_freezes_single_task_app_shell_direction() -> None:
    text = PLAN.read_text(encoding="utf-8")

    for required in [
        "Long configuration form",
        "single-task document workspace",
        "1. Toevoegen",
        "2. Controleren",
        "3. Downloaden",
        "Only the active stage is expanded",
        "Standard view: no permanent configuration sidebar.",
        "Anonimiseren | Terugzetten",
        "Standaard",
        "Expert",
        "one recommended document download",
        "Standard view is lower cognitive load, not lower safety.",
    ]:
        assert required in text


def test_plan_preserves_safety_and_roundtrip_semantics() -> None:
    text = PLAN.read_text(encoding="utf-8")

    for required in [
        "weaken human review",
        "change export bytes, filenames, MIME types or eligibility",
        "change Scrub Key schema, binding, digest, warning or lifecycle",
        "change reinsert semantics",
        "introduce cloud document processing",
        "remove audit or technical evidence",
    ]:
        assert required in text


def test_current_strategy_preserves_implemented_ui_contract_without_reactivating_old_queue() -> None:
    roadmap = ROADMAP.read_text(encoding="utf-8")
    workpackages = WORKPACKAGES.read_text(encoding="utf-8")
    decisions = DECISIONS.read_text(encoding="utf-8")

    assert "generation-bound Standard/Expert workflow state" in roadmap
    assert "## D041" in decisions
    assert "## D043" in decisions
    assert "global `Standaard | Expert` presentation" in decisions
    assert "exactly one Standard stage is dominant at a time" in decisions
    assert "Shared Streamlit/review/export/runtime surfaces remain sequential" in workpackages

    # Historical implementation packages are evidence, not the current queue.
    for obsolete_current_package in [
        "SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT",
        "SCRUB-WP_PREMIUM_CORE_FLOW_STATE_MODEL",
        "SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION",
        "SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT",
    ]:
        assert obsolete_current_package not in workpackages


def test_decision_log_records_global_view_and_stage_model() -> None:
    text = DECISIONS.read_text(encoding="utf-8")

    assert "## D041" in text
    assert "global `Standaard | Expert` presentation" in text
    assert "presentation-only switching" in text
    assert "## D043" in text
    assert "exactly one Standard stage is dominant at a time" in text
    assert "Standard is lower cognitive load, not lower safety" in text


def test_claim_is_planning_only() -> None:
    text = CLAIM.read_text(encoding="utf-8")

    assert "completed planning/design-only" in text
    assert "No Streamlit or product-code changes" in text
    assert "SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT" in text
