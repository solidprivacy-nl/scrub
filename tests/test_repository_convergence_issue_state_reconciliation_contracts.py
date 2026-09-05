from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def _first_fenced_block(text: str) -> str:
    return text.split("```text", 1)[1].split("```", 1)[0]


def test_validation_hierarchy_package_is_recorded_as_completed() -> None:
    workpackages = read("WORKPACKAGES.md")
    changelog = read("CHANGELOG.md")
    decisions = read("DECISION_LOG.md")

    assert "WP-CONVERGENCE-03 — Validation hierarchy clarification — COMPLETED" in workpackages
    assert "268d967db95d923a73a3979ffce2d0cab586e499" in workpackages
    assert "33930953130" in workpackages
    assert "33930953103" in workpackages

    validation_section = changelog.split(
        "## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION",
        1,
    )[1].split("\n---\n", 1)[0]
    assert "PASS → MERGED → exact-main verified" in validation_section
    assert "37de6859ed5b17f4767c463f6db73085ce0d4b56" in validation_section

    d045 = decisions.split("## D045", 1)[1].split("\n---\n", 1)[0]
    assert "accepted, independently assured and merged" in d045
    assert "subject to independent assurance" not in d045


def test_issue_reconciliation_is_the_only_current_workpackage() -> None:
    workpackages = read("WORKPACKAGES.md")

    current_wp_headings = re.findall(
        r"^## (WP-CONVERGENCE-\d+ .+ — CURRENT)$",
        workpackages,
        flags=re.MULTILINE,
    )
    assert current_wp_headings == [
        "WP-CONVERGENCE-04 — GitHub issue/current-state reconciliation — CURRENT"
    ]
    assert "Issue: #119" in workpackages
    assert "SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION" in workpackages


def test_issue_disposition_keeps_exactly_one_residual_premium_gate() -> None:
    workpackages = read("WORKPACKAGES.md")
    ledger = read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md")
    risks = read("RISK_REGISTER.md")

    expected_close = {
        74,
        75,
        76,
        77,
        79,
        81,
        84,
        86,
        88,
        89,
        98,
        100,
        105,
        106,
        107,
        109,
        112,
    }

    disposition = ledger.split("## WP-CONVERGENCE-04 reviewed issue-disposition candidate", 1)[1]
    keep_section = disposition.split("### Keep open", 1)[1].split("### Close after", 1)[0]
    close_section = disposition.split("### Close after WP04 independent PASS", 1)[1].split(
        "Evidence basis:", 1
    )[0]

    kept_numbers = {int(value) for value in re.findall(r"#(\d+)", _first_fenced_block(keep_section))}
    close_numbers = {int(value) for value in re.findall(r"#(\d+)", _first_fenced_block(close_section))}

    assert kept_numbers == {96}
    assert close_numbers == expected_close
    assert 96 not in close_numbers

    assert "consolidated deployed live-app retest" in disposition
    assert "consolidated deployed live-app retest" in workpackages
    assert "consolidated deployed live-app retest" in risks
    assert "remains unproven" in disposition


def test_issue_reconciliation_does_not_claim_live_gate_or_change_product_line() -> None:
    combined = "\n".join(
        [
            read("WORKPACKAGES.md"),
            read("CHANGELOG.md"),
            read("RISK_REGISTER.md"),
            read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md"),
        ]
    )

    assert "do not close #96 without actual live post-repair evidence" in combined.lower()
    assert "Stage 2 — Scrub Private Application — BLOCKED" in read("WORKPACKAGES.md")
    assert "mandatory human review" in combined.lower()
    assert "no new permanent issue ledger" in combined.lower()
