from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def test_recovery_is_current_and_issue_reconciliation_is_blocked() -> None:
    workpackages = read("WORKPACKAGES.md")

    assert "WP-CONVERGENCE-04R — Governance sequencing recovery — CURRENT" in workpackages
    assert "SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY" in workpackages
    assert "Issue: #121" in workpackages
    assert "WP-CONVERGENCE-04 — GitHub issue/current-state reconciliation — BLOCKED ON 04R" in workpackages
    assert "Issue: #119 — open" in workpackages


def test_recovery_preserves_pre_action_assurance_boundary() -> None:
    combined = "\n".join(
        [
            read("WORKPACKAGES.md"),
            read("CHANGELOG.md"),
            read("RISK_REGISTER.md"),
            read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md"),
        ]
    )

    assert "fd69294c67a59bb150f5d4a637daad2607c14077" in combined
    assert "GOVERNANCE FAIL" in read("CHANGELOG.md")
    assert "before" in combined.lower() and "independent" in combined.lower()
    assert "#74 has been reopened" in combined or "issue #74 has been reopened" in combined
    assert "no force reset" in combined.lower()


def test_failed_wp04_artifacts_are_not_active_authority() -> None:
    assert not (ROOT / "tests" / "test_repository_convergence_issue_state_reconciliation_contracts.py").exists()
    assert not (
        ROOT
        / "workpackage_claims"
        / "SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION.md"
    ).exists()
    assert not (
        ROOT
        / "handover"
        / "workpackages"
        / "20260905_0212_repository_convergence_issue_state_reconciliation.md"
    ).exists()

    ledger = read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md")
    assert "not current action authority" in ledger
    assert "new WP04 candidate" in ledger


def test_valid_pre_wp04_truth_and_residual_live_gate_are_preserved() -> None:
    decisions = read("DECISION_LOG.md")
    risks = read("RISK_REGISTER.md")
    workpackages = read("WORKPACKAGES.md")

    assert "accepted, independently assured and merged validation-authority direction" in decisions
    assert "268d967db95d923a73a3979ffce2d0cab586e499" in workpackages
    assert "consolidated deployed live-app retest" in risks
    assert "remains unproven" in risks
    assert "#96" in workpackages
    assert "do not close #96" in workpackages.lower()
    assert "Stage 2 — Scrub Private Application — BLOCKED" in workpackages
    assert "mandatory human review" in risks.lower()
