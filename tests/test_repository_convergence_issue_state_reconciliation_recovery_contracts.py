from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def test_recovery_and_wp04_are_completed_before_wp05() -> None:
    workpackages = read("WORKPACKAGES.md")

    assert "WP-CONVERGENCE-04R — Governance sequencing recovery — COMPLETED" in workpackages
    assert "Issue #121 closed" in workpackages
    assert "14baceb97b274de6ef35c42ce48441c4e74c5f08" in workpackages
    assert "WP-CONVERGENCE-04 — GitHub issue/current-state reconciliation — COMPLETED" in workpackages
    assert "Issue #119 closed" in workpackages
    assert "2d4ab0446c20f08ad07576af326ab4b0df0a2af7" in workpackages
    assert "WP-CONVERGENCE-05 — Consolidated deployed live-app verification — CURRENT" in workpackages


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
    assert "no force reset" in combined.lower() or "no force-reset" in combined.lower()


def test_recovery_pass_did_not_become_wp04_or_wp05_action_authority() -> None:
    ledger = read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md").lower()
    wp04_claim = read(
        "workpackage_claims/"
        "SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION.md"
    ).lower()
    wp05_claim = read(
        "workpackage_claims/"
        "SCRUB-WP_REPOSITORY_CONVERGENCE_LIVE_APP_GATE_ALIGNMENT.md"
    ).lower()

    assert "recovery pass is not wp04 assurance" in ledger
    assert "recovery pr #122 pass" in wp04_claim
    assert "reused as release authority" in wp04_claim
    assert "pr #122" in wp05_claim
    assert "does not authorize" in wp05_claim


def test_residual_live_gate_and_safety_truth_are_preserved() -> None:
    decisions = read("DECISION_LOG.md")
    risks = read("RISK_REGISTER.md")
    workpackages = read("WORKPACKAGES.md")

    assert "accepted, independently assured and merged validation-authority direction" in decisions
    assert "268d967db95d923a73a3979ffce2d0cab586e499" in workpackages
    assert "consolidated deployed live-app" in risks
    assert "remains unproven" in risks
    assert "Issue: #96 — OPEN" in workpackages
    assert "Stage 2 — Scrub Private Application — BLOCKED" in workpackages
    assert "mandatory human review" in risks.lower()
