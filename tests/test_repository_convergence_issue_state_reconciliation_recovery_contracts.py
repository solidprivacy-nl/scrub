from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def test_recovery_is_completed_and_fresh_wp04_is_current() -> None:
    workpackages = read("WORKPACKAGES.md")

    assert "WP-CONVERGENCE-04R — Governance sequencing recovery — COMPLETED" in workpackages
    assert "SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY" in workpackages
    assert "Issue: #121 — closed" in workpackages
    assert "14baceb97b274de6ef35c42ce48441c4e74c5f08" in workpackages
    assert "WP-CONVERGENCE-04 — GitHub issue/current-state reconciliation — CURRENT" in workpackages
    assert "Issue: #119 — open" in workpackages


def test_recovery_preserves_pre_action_assurance_boundary_as_history() -> None:
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
    assert "8565af4e9f579b3a975c6122668f6511a9df627a" in combined
    assert "14baceb97b274de6ef35c42ce48441c4e74c5f08" in combined
    assert "#74" in combined and "OPEN" in combined
    assert "no force reset" in combined.lower() or "no force-reset" in combined.lower()


def test_recovery_pass_does_not_become_wp04_action_authority() -> None:
    ledger = read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md")
    claim = read(
        "workpackage_claims/"
        "SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION.md"
    ).lower()

    assert "PR #122 recovery PASS is not WP04 assurance" in ledger
    assert "recovery pr #122 pass" in claim
    assert "reused as release authority" in claim
    assert "new candidate must earn its own exact-head" in claim


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
