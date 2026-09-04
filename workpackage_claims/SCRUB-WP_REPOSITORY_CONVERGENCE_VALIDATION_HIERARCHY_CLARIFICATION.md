# Workpackage claim — SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION

Status: implementation in progress  
Role: `implementation_operations`  
Issue: #117  
Branch: `wp/repository-convergence-validation-hierarchy`  
Starting main: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`  
Started: 2026-09-05 Europe/Amsterdam

## Objective

Remove ambiguity about validation authority without creating another framework or changing any product/runtime behavior.

## Source-derived finding

Current evidence has three different roles that historical documents sometimes blur:

1. `.github/workflows/tests.yml` runs the complete committed `tests/` suite on pull requests and `main`; this is the current exact-SHA regression gate.
2. Capability/domain suites inside `tests/` (Phase-6 E2E, Scrub Key, document fidelity/hygiene, Zorg, Premium/AppTest, recognizer contracts) provide specific product-regression evidence as part of that full suite.
3. Recall/precision/report helpers are diagnostic evidence, not merge/production gates: `recall_benchmark_report.py` explicitly sets `diagnostic_only`, `production_gate=False`, `thresholds_enforced=False`; WP22 scores supplied predictions and does not invoke recognizers; WP23/WP24 are report-only and non-gating.

## Scope

Authorized:

- record one binding validation-authority decision in `DECISION_LOG.md`;
- align the validation strategy wording in `ROADMAP.md`;
- advance `WORKPACKAGES.md` from the merged WP-CONVERGENCE-02 to this package;
- align the temporary convergence debt ledger;
- update `CHANGELOG.md`;
- add one narrow contract test that validates workflow/source metadata and the binding decision;
- write the mandatory handover.

Not authorized:

- new Evidence Framework or validation subsystem;
- changes to corpus data, recognizers, thresholds or product/runtime code;
- making diagnostic recall/precision scores release-blocking;
- production-safety or perfect-recall claims;
- deleting historical validation helpers merely because they are non-authoritative;
- issue-state cleanup unrelated to this validation-authority cluster.

## Acceptance

1. One release regression gate is unambiguous: exact-SHA full `Tests` workflow.
2. Capability/domain tests remain first-class regression evidence but not competing merge authority.
3. Recognizer-backed recall report is explicitly supplemental diagnostic evidence, consistent with its source metadata.
4. WP22/WP23/WP24 scorecard/residual-risk chain is classified supplemental/historical diagnostic and not release authority.
5. No new threshold or production-safety claim is introduced.
6. Full exact-head `python -m pytest -q tests` is green.
7. Fresh independent `governance_release_assurance` returns PASS before merge.
8. Post-merge exact-main Tests and GitHub→Hugging Face sync are verified where applicable.
