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
        "three-page wizard",
        "three separate core-flow pages: rejected for Standard",
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


def test_current_roadmap_preserves_staged_workspace_without_reactivating_old_gate() -> None:
    roadmap = ROADMAP.read_text(encoding="utf-8")
    decisions = DECISION_LOG.read_text(encoding="utf-8")

    assert "generation-bound Standard/Expert workflow state" in roadmap
    assert "Stage 1 — Repository Convergence — CURRENT" in roadmap
    assert "## D043" in decisions
    assert "single-page staged document workspace" in decisions
    assert "three routed pages" in decisions

    # Old implementation-gate prose is historical, not current strategy.
    assert "SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE — URGENT CURRENT PACKAGE" not in roadmap
    assert "production integration paused until package 3 is incorporated" not in roadmap
    assert "PR #85 is **amended, not discarded**" not in roadmap


def test_current_workpackages_preserve_shared_surface_sequencing_not_historical_package_order() -> None:
    workpackages = WORKPACKAGES.read_text(encoding="utf-8")
    decisions = DECISION_LOG.read_text(encoding="utf-8")

    assert "Shared Streamlit/review/export/runtime surfaces remain sequential" in workpackages
    assert "## D043" in decisions
    assert "single-page staged document workspace" in decisions
    assert "three separate routed screens" not in decisions
    assert "three routed pages" in decisions

    for obsolete_current_package in [
        "SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE",
        "SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION",
        "SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION",
        "SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION",
        "SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION",
        "SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION",
        "SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT",
    ]:
        assert obsolete_current_package not in workpackages
