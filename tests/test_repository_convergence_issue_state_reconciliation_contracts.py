from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def _first_fenced_text_block(text: str) -> str:
    return text.split("```text", 1)[1].split("```", 1)[0]


def test_wp04_is_completed_and_wp05_is_the_only_current_repository_convergence_package() -> None:
    workpackages = read("WORKPACKAGES.md")

    assert "WP-CONVERGENCE-04 — GitHub issue/current-state reconciliation — COMPLETED" in workpackages
    assert "Issue #119 closed" in workpackages
    assert "2d4ab0446c20f08ad07576af326ab4b0df0a2af7" in workpackages

    current_wp_headings = re.findall(
        r"^## (WP-CONVERGENCE-\d+[A-Z]? .+ — CURRENT)$",
        workpackages,
        flags=re.MULTILINE,
    )
    assert current_wp_headings == [
        "WP-CONVERGENCE-05 — Consolidated deployed live-app verification — CURRENT"
    ]
    assert "Issue: #96 — OPEN" in workpackages


def test_wp04_historical_disposition_is_exact_and_96_remains_open() -> None:
    workpackages = read("WORKPACKAGES.md")
    section = workpackages.split(
        "## WP-CONVERGENCE-04 — GitHub issue/current-state reconciliation — COMPLETED",
        1,
    )[1].split("## WP-CONVERGENCE-05", 1)[0]

    expected_closed = {
        74, 75, 76, 77, 79, 81, 84, 86, 88, 89,
        98, 100, 105, 106, 107, 109, 112, 123,
    }
    actual = {int(value) for value in re.findall(r"#(\d+)", section)}
    assert expected_closed.issubset(actual)
    assert 96 in actual
    assert "#96 is the sole remaining open product-facing issue" in section


def test_wp04_release_ordering_and_provenance_remain_historical_truth() -> None:
    changelog = read("CHANGELOG.md")
    ledger = read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md")
    claim = read(
        "workpackage_claims/"
        "SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION.md"
    )
    combined = "\n".join([changelog, ledger, claim]).lower()

    for marker in [
        "1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a",
        "fd69294c67a59bb150f5d4a637daad2607c14077",
        "14baceb97b274de6ef35c42ce48441c4e74c5f08",
        "ce021443303cfa11de12f3273f872b2d027da5db",
        "2d4ab0446c20f08ad07576af326ab4b0df0a2af7",
        "governance fail",
        "guarded merge",
    ]:
        assert marker in combined


def test_residual_live_gate_and_safety_boundaries_remain_binding() -> None:
    workpackages = read("WORKPACKAGES.md")
    risks = read("RISK_REGISTER.md")
    ledger = read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md")
    combined = "\n".join([workpackages, risks, ledger]).lower()

    assert "consolidated deployed live-app" in combined
    assert "remains unproven" in combined
    assert "#96" in combined
    assert "mandatory human review" in combined
    assert "stage 2 — scrub private application — blocked" in combined


def test_candidate_scope_excludes_product_runtime_changes() -> None:
    claim = read(
        "workpackage_claims/"
        "SCRUB-WP_REPOSITORY_CONVERGENCE_LIVE_APP_GATE_ALIGNMENT.md"
    ).lower()

    for marker in [
        "no runtime/product/ui/recognizer/review/export/scrub key/reinsert change",
        "no stage-2 persistence/egress work",
        "#96 remains open",
        "no new permanent evidence framework",
    ]:
        assert marker in claim
