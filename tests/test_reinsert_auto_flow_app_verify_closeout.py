from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_reinsert_auto_flow_closeout_is_recorded() -> None:
    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    workpackages = (ROOT / "WORKPACKAGES.md").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
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

    assert "completed and app-verified" in roadmap
    assert "SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION — active" in roadmap
    assert "SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_APP_VERIFY_CLOSEOUT" in workpackages
    assert "coordinator reported `getest en werkend`" in changelog
    assert "Status: completed and app-verified" in claim
    assert "Completed and app-verified." in handover


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
