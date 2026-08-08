from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DECISION = ROOT / "PREMIUM_STAGED_WORKSPACE_DECISION.md"
ROADMAP = ROOT / "ROADMAP.md"
WORKPACKAGES = ROOT / "WORKPACKAGES.md"
DECISION_LOG = ROOT / "DECISION_LOG.md"


def test_decision_freezes_one_document_one_workspace_model() -> None:
    text = DECISION.read_text(encoding="utf-8")

    for required in [
        "single-page staged document workspace",
        "One document. One workspace. Three stages. One active task.",
        "1. Toevoegen",
        "2. Controleren",
        "3. Downloaden",
        "Exactly one of those stages is expanded and dominant",
        "completed prior stage collapses into a compact summary",
        "Future stages remain visible",
        "After successful processing",
        "Controleren opens automatically",
        "After explicit review completion",
        "Downloaden opens automatically",
    ]:
        assert required in text


def test_decision_rejects_routed_pages_and_nested_form_accordion() -> None:
    text = DECISION.read_text(encoding="utf-8")

    for required in [
        "not a three-page wizard",
        "Do not implement the Standard core flow as three isolated routed pages/screens",
        "No nested core-flow accordion hierarchy",
        "Do not build an accordion inside an accordion",
        "Stage panels, not generic Streamlit expanders",
    ]:
        assert required in text


def test_decision_preserves_state_safety_and_product_semantics() -> None:
    text = DECISION.read_text(encoding="utf-8")

    for required in [
        "review-table authority",
        "export bytes, filenames or MIME types",
        "Scrub Key schema, binding, warning or lifecycle",
        "reinsert semantics",
        "human-review requirement",
        "processed lineage invalid",
        "reviewed lineage invalid",
        "export lineage invalid",
    ]:
        assert required in text


def test_roadmap_makes_staged_workspace_the_urgent_premium_gate() -> None:
    text = ROADMAP.read_text(encoding="utf-8")

    assert "PREMIUM_STAGED_WORKSPACE_DECISION.md" in text
    assert "SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE — URGENT CURRENT PACKAGE" in text
    assert "production integration paused until package 3 is incorporated" in text
    assert "PR #85 is **amended, not discarded**" in text
    assert "one persistent document workspace" in text
    assert "no three routed pages" in text


def test_workpackages_and_decision_log_bind_the_execution_order() -> None:
    workpackages = WORKPACKAGES.read_text(encoding="utf-8")
    decisions = DECISION_LOG.read_text(encoding="utf-8")

    assert "SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE" in workpackages
    assert "SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION" in workpackages
    assert "SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION" in workpackages
    assert "SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION" in workpackages
    assert "SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION" in workpackages
    assert "SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION" in workpackages
    assert "SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT" in workpackages
    assert "do not run the shared Streamlit UI packages in parallel" in workpackages

    assert "D043" in decisions
    assert "single-page staged document workspace" in decisions
    assert "three separate routed screens" in decisions
