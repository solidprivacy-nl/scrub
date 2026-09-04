from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def test_roadmap_has_only_the_five_current_macro_stages() -> None:
    roadmap = read("ROADMAP.md")

    stages = [
        "Stage 1 — Repository Convergence",
        "Stage 2 — Scrub Private Application",
        "Stage 3 — Private Service",
        "Stage 4 — External Product & Service Assurance",
        "Stage 5 — Pilot",
    ]
    for stage in stages:
        assert roadmap.count(stage) == 1, stage

    for milestone in [
        "SCRUB_REPOSITORY_CONVERGED",
        "SCRUB_HF_APPLICATION_COMPLETE",
        "SCRUB_PRIVATE_SERVICE_CANDIDATE",
    ]:
        assert milestone in roadmap

    assert "Phase 9 — Final local desktop/offline installer path" not in roadmap
    assert "active draft PR #85" not in roadmap
    assert "The broader direction is a local-first" not in roadmap


def test_workpackages_contains_one_current_queue_not_historical_overrides() -> None:
    workpackages = read("WORKPACKAGES.md")

    assert "# SolidPrivacy Scrub — Current Workpackages" in workpackages
    assert "Repository Convergence" in workpackages
    assert "SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP" in workpackages
    assert "Current execution status override" not in workpackages
    assert "WP-CONVERGENCE-02..N" in workpackages
    assert "DERIVED, NOT PRE-INVENTED" in workpackages
    assert "SCRUB_REPOSITORY_CONVERGED" in workpackages


def test_project_prompt_preserves_start_governance_and_safety_contracts() -> None:
    prompt = read("PROJECT_PROMPT.md")

    ordered = [
        "1. `PROJECT_PROMPT.md`",
        "2. `ROADMAP.md`",
        "3. `WORKPACKAGES.md`",
        "4. `CHANGELOG.md`",
    ]
    positions = [prompt.index(marker) for marker in ordered]
    assert positions == sorted(positions)

    for marker in [
        "implementation_operations",
        "governance_release_assurance",
        "PASS`, `FAIL` or `INDETERMINATE",
        "Scrub Private",
        "Repository Convergence",
        "human review",
        "false negatives",
        "GitHub→Hugging Face",
        "handover/workpackages/YYYYMMDD_HHMM_<workpackage_slug>.md",
    ]:
        assert marker in prompt

    assert "Immediate line: v12 Review UX" not in prompt
    assert "broader direction is a local-first" not in prompt


def test_short_prompt_routes_workers_to_the_same_current_direction() -> None:
    short = read("PROJECT_PROMPT_SHORT.md")

    for marker in [
        "Repository Convergence",
        "Scrub Private Application",
        "Private Service",
        "External Product & Service Assurance",
        "Pilot",
        "governance_release_assurance",
        "synthetic/approved-test application-validation",
    ]:
        assert marker in short

    assert "Immediate line: v12 Review UX" not in short


def test_agents_routes_claims_and_execution_to_convergence() -> None:
    agents = read("AGENTS.md")

    for marker in [
        "Repository Convergence",
        "SCRUB_REPOSITORY_CONVERGED",
        "implementation_operations",
        "governance_release_assurance",
        "workpackage_claims/",
        "Do not refactor for aesthetics",
    ]:
        assert marker in agents

    assert "local-first" not in agents.lower()


def test_temporary_ledger_is_explicitly_non_authoritative_and_capability_level() -> None:
    ledger = read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md")

    assert "TEMPORARY EXECUTION ARTIFACT — NON-AUTHORITATIVE AFTER CONVERGENCE" in ledger
    assert "54c73e0ebf5a3a3ed7039a50596fb57694add3cd" in ledger

    for classification in [
        "CANONICAL",
        "RECONCILE",
        "RETIRE",
        "VARIANT-SPECIFIC",
    ]:
        assert classification in ledger

    for capability in [
        "Persistent replacement memory",
        "Azure AI Language document recognition",
        "OpenAI/Azure OpenAI synthesis operator",
        "Legacy startup patch script invocation in Dockerfile",
        "Recognizer-backed recall benchmark",
    ]:
        assert capability in ledger

    assert "new Evidence Framework" in ledger


def test_decision_log_keeps_current_binding_decisions_and_adds_d044() -> None:
    decisions = read("DECISION_LOG.md")

    for marker in [
        "D044 — 2026-09-04 — Repository Convergence",
        "D043",
        "D042",
        "D041",
        "D040",
        "D039",
        "D037",
        "D036",
        "D034",
        "54c73e0ebf5a3a3ed7039a50596fb57694add3cd",
    ]:
        assert marker in decisions

    assert "main` becomes the active Scrub Private development line" in decisions


def test_risk_register_keeps_critical_product_risks_and_adds_current_truth_risks() -> None:
    risks = read("RISK_REGISTER.md")

    assert "R1 — False negatives / missed sensitive data" in risks
    assert "R2 — Scrub Key leakage, mismatch or misuse" in risks
    assert "R10 — Zorg under-detection and clinical over-masking" in risks
    assert "R11 — Repository/source-of-truth drift" in risks
    assert "R12 — Legacy runtime mutation / hidden startup authority" in risks

    # R1, R2 and R10 must remain explicitly critical.
    for heading in [
        "R1 — False negatives / missed sensitive data",
        "R2 — Scrub Key leakage, mismatch or misuse",
        "R10 — Zorg under-detection and clinical over-masking",
    ]:
        start = risks.index(heading)
        section = risks[start : start + 700]
        assert "Impact: `critical`" in section, heading

    assert "R5 — Scrub Private content-retention / external-egress trust boundary" in risks
    r5 = risks[risks.index("R5 — Scrub Private") : risks.index("R6 — Review UX")]
    assert "Impact: `critical`" in r5
    assert "replacement_memory.py" in r5
    assert "Azure AI Language" in r5


def test_bootstrap_does_not_redefine_hugging_face_as_production_assurance() -> None:
    combined = "\n".join(
        [
            read("ROADMAP.md"),
            read("PROJECT_PROMPT.md"),
            read("WORKPACKAGES.md"),
        ]
    ).lower()

    assert "hugging face" in combined
    assert "application-validation" in combined or "application validation" in combined
    assert "not the final confidential-production trust environment" in combined
    assert "zero retention" not in combined


def test_bootstrap_does_not_authorize_source_cloning_or_a_new_evidence_framework() -> None:
    roadmap = read("ROADMAP.md")
    ledger = read("REPOSITORY_CONVERGENCE_DEBT_LEDGER.md")

    assert "no source-tree clone" in roadmap
    assert "No separate Evidence Framework" in roadmap
    assert "/app_v2" not in roadmap
    assert "/scrub-new" not in roadmap
    assert "Do not build a new Evidence Framework" not in ledger  # ledger records 'no new' but is not a new framework itself
