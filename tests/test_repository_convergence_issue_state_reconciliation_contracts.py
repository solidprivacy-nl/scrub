from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def _first_fenced_text_block(text: str) -> str:
    return text.split("```text", 1)[1].split("```", 1)[0]


def test_wp04_is_the_only_current_repository_convergence_package() -> None:
    workpackages = read("WORKPACKAGES.md")

    current_wp_headings = re.findall(
        r"^## (WP-CONVERGENCE-\d+[A-Z]? .+ — CURRENT)$",
        workpackages,
        flags=re.MULTILINE,
    )
    assert current_wp_headings == [
        "WP-CONVERGENCE-04 — GitHub issue/current-state reconciliation — CURRENT"
    ]
    assert "Exact starting main/base: `14baceb97b274de6ef35c42ce48441c4e74c5f08`" in workpackages
    assert "Branch: `wp/repository-convergence-issue-state-reconciliation-v2`" in workpackages


def test_fresh_wp04_disposition_is_exact_and_excludes_96_from_closure() -> None:
    ledger = read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md")

    section = ledger.split("## Fresh WP-CONVERGENCE-04 retry — current evidence candidate", 1)[1]
    keep_section = section.split("### Keep open", 1)[1].split("### Close only after", 1)[0]
    close_section = section.split(
        "### Close only after new WP04 PASS + guarded merge + exact-main verification",
        1,
    )[1].split("Evidence basis:", 1)[0]

    kept = {int(value) for value in re.findall(r"#(\d+)", _first_fenced_text_block(keep_section))}
    closed = {int(value) for value in re.findall(r"#(\d+)", _first_fenced_text_block(close_section))}

    assert kept == {96}
    assert closed == {
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
    assert kept.isdisjoint(closed)


def test_wp04_requires_pass_merge_and_exact_main_verification_before_issue_mutation() -> None:
    workpackages = read("WORKPACKAGES.md")
    claim = read(
        "workpackage_claims/"
        "SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION.md"
    )
    combined = workpackages + "\n" + claim

    required_fragments = [
        "fresh blind governance_release_assurance",
        "PASS",
        "guarded merge",
        "exact-main Tests",
        "GitHub→HF",
        "only then",
        "issue mutation",
    ]
    for fragment in required_fragments:
        assert fragment.lower() in combined.lower()

    assert "zero target issue mutations" in claim

    action_block = claim.split("Required action order:", 1)[1].split("```", 2)[1].lower()
    ordered_markers = [
        "exact candidate",
        "full tests",
        "fresh blind pass",
        "guarded merge",
        "exact-main tests",
        "only then",
        "close the 17 reviewed issues",
        "readback",
    ]
    positions = [action_block.index(marker) for marker in ordered_markers]
    assert positions == sorted(positions)


def test_residual_live_gate_and_safety_boundaries_remain_binding() -> None:
    workpackages = read("WORKPACKAGES.md")
    risks = read("RISK_REGISTER.md")
    ledger = read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md")
    combined = "\n".join([workpackages, risks, ledger]).lower()

    assert "consolidated deployed live-app retest" in combined
    assert "remains unproven" in combined
    assert "do not close #96" in combined
    assert "mandatory human review" in combined
    assert "stage 2 — scrub private application — blocked" in combined
    assert "no new permanent issue ledger" in workpackages.lower()


def test_recovery_and_failed_pr120_are_provenance_not_reused_assurance() -> None:
    changelog = read("CHANGELOG.md")
    ledger = read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md")
    claim = read(
        "workpackage_claims/"
        "SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION.md"
    )
    claim_lower = claim.lower()

    assert "1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a" in changelog
    assert "14baceb97b274de6ef35c42ce48441c4e74c5f08" in ledger
    assert "not WP04 assurance" in ledger
    assert "reused as release authority" in claim_lower
    for historical_authority in [
        "pr #120 candidate identity",
        "pr #120 merge",
        "pr #120 ci",
        "recovery pr #122 pass",
    ]:
        assert historical_authority in claim_lower


def test_candidate_scope_claim_explicitly_excludes_product_runtime_changes() -> None:
    claim = read(
        "workpackage_claims/"
        "SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION.md"
    ).lower()

    for marker in [
        "product/runtime/ui/recognizer/profile/review/export/scrub key/reinsert changes",
        "stage-2 persistence/external-ai/logging work",
        "closing or weakening #96",
        "new permanent issue ledger/framework",
    ]:
        assert marker in claim
