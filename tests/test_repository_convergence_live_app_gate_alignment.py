from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def test_wp05_is_exactly_one_current_repository_convergence_package() -> None:
    workpackages = read("WORKPACKAGES.md")

    current = re.findall(
        r"^## (WP-CONVERGENCE-\d+[A-Z]? .+ — CURRENT)$",
        workpackages,
        flags=re.MULTILINE,
    )
    assert current == [
        "WP-CONVERGENCE-05 — Consolidated deployed live-app verification — CURRENT"
    ]
    assert "Issue: #96 — OPEN" in workpackages
    assert "2d4ab0446c20f08ad07576af326ab4b0df0a2af7" in workpackages


def test_wp05_freezes_the_exact_residual_live_behavior_contract() -> None:
    workpackages = read("WORKPACKAGES.md")
    section = workpackages.split(
        "## WP-CONVERGENCE-05 — Consolidated deployed live-app verification — CURRENT",
        1,
    )[1].split("## Candidate later package", 1)[0].lower()

    for marker in [
        "staged standard/expert core flow",
        "leading whitespace/newlines",
        "strict document-bound placeholders render compactly",
        "polderweg 8",
        "source/review/export lineage remains fail-closed",
        "human review remains required",
        "exact deployed git sha",
        "test date",
    ]:
        assert marker in section


def test_live_gate_cannot_be_closed_from_ci_or_hf_sync_alone() -> None:
    workpackages = read("WORKPACKAGES.md").lower()
    risks = read("RISK_REGISTER.md").lower()
    combined = workpackages + "\n" + risks

    assert "do not close #96 from ci/hf sync alone" in combined
    assert "remains unproven" in combined
    assert "sync" in combined
    assert "live-app" in combined


def test_stage2_and_product_safety_boundaries_remain_blocked() -> None:
    workpackages = read("WORKPACKAGES.md")
    risks = read("RISK_REGISTER.md").lower()

    assert "Stage 2 — Scrub Private Application — BLOCKED" in workpackages
    assert "mandatory human review" in risks
    assert "Impact: `critical`" in read("RISK_REGISTER.md")


def test_alignment_claim_is_docs_only_and_does_not_claim_live_pass() -> None:
    claim = read(
        "workpackage_claims/"
        "SCRUB-WP_REPOSITORY_CONVERGENCE_LIVE_APP_GATE_ALIGNMENT.md"
    ).lower()

    for marker in [
        "governance/docs/contracts only",
        "does not claim the live app already passes",
        "no runtime/product/ui/recognizer/review/export/scrub key/reinsert change",
        "#96 remains open",
        "fresh independent governance assurance",
    ]:
        assert marker in claim
