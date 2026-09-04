from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_reinsert_auto_flow_closeout_history_and_current_contract_are_preserved() -> None:
    archived_changelog = (
        ROOT / "history" / "CHANGELOG_PRE_CONVERGENCE_20260904.md"
    ).read_text(encoding="utf-8")
    decisions = (ROOT / "DECISION_LOG.md").read_text(encoding="utf-8")
    claim = (
        ROOT
        / "workpackage_claims"
        / "scrub_wp_mvp_reinsert_auto_flow_simplification_implementation.md"
    ).read_text(encoding="utf-8")
    handover = (
        ROOT
        / "handover"
        / "workpackages"
        / "20260727_1706_mvp_reinsert_auto_flow_simplification_implementation.md"
    ).read_text(encoding="utf-8")

    assert "coordinator reported `getest en werkend`" in archived_changelog
    assert "Status: completed and app-verified" in claim
    assert "Completed and app-verified." in handover

    # Current authority lives in accepted decisions, not old roadmap/workpackage slots.
    assert "## D031" in decisions
    assert "source document/text" in decisions
    assert "corresponding Scrub Key" in decisions
    assert "deterministic validation/reinsert" in decisions
    assert "meaningful confidentiality acknowledgement" in decisions
    assert "## D037" in decisions
    assert "fails closed with zero replacements" in decisions


def test_closeout_preserves_product_boundaries() -> None:
    closeout = (
        ROOT
        / "handover"
        / "workpackages"
        / "20260727_1828_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md"
    ).read_text(encoding="utf-8")

    assert "One final confidentiality acknowledgement remains" in closeout
    assert "PDF remains restored TXT only" in closeout
    assert "Human review remains mandatory" in closeout
    assert "no production-readiness claim" in closeout


def test_temporary_closeout_files_are_absent() -> None:
    assert not (ROOT / ".github/workflows/reinsert_auto_flow_closeout_finalizer.yml").exists()
    assert not (ROOT / "scripts/finalize_reinsert_auto_flow_app_verify_closeout.py").exists()
