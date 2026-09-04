# Workpackage claim — SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION

Status: release candidate ready; independent assurance required  
Role: `implementation_operations`  
Issue: #117  
PR: #118  
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

## Scope delivered

- D045 records one binding validation-authority hierarchy in `DECISION_LOG.md`;
- `ROADMAP.md` describes one release regression gate plus subordinate capability/diagnostic evidence;
- `WORKPACKAGES.md` records WP-CONVERGENCE-02 completed and WP-CONVERGENCE-03 current;
- the temporary convergence ledger classifies the validation generations explicitly;
- one narrow validation-hierarchy contract test is added;
- obsolete bootstrap tests are rebound to current semantic convergence invariants rather than old placement/status prose;
- `CHANGELOG.md` and the mandatory handover record implementation and validation history.

No runner, workflow implementation, corpus, recognizer, threshold or product/runtime behavior is changed.

## CI history before final freeze

Initial PR candidate:

```text
Tests run 33930040668
4 failed, 1264 passed
```

The four failures were contract/current-truth mismatches only:

- old bootstrap test still required `WP-CONVERGENCE-02..N` literal wording;
- old bootstrap test still required the already-resolved live Docker startup finding as current ledger content;
- old bootstrap test required duplicate `no new framework` prose in the temporary ledger;
- the new hierarchy test incorrectly required Markdown backticks around the workflow path.

Remediation preserved the underlying invariants and removed only obsolete/format-specific assertions.

Corrected pre-final candidate:

```text
head 2147c854b344e628515076a624efc6176a74ca84
Tests run 33930216093
job 101207097941
1268 passed in 13.72s
SUCCESS
```

The mandatory handover and this claim closeout are committed after that pre-final run, so the resulting final head must receive one more complete exact-head regression before it is frozen for independent assurance.

## Acceptance

1. One release regression gate is unambiguous: exact-SHA full `Tests` workflow.
2. Capability/domain tests remain first-class regression evidence but not competing merge authority.
3. Recognizer-backed recall report is explicitly supplemental diagnostic evidence, consistent with its source metadata.
4. WP22/WP23/WP24 scorecard/residual-risk chain is classified supplemental/historical diagnostic and not release authority.
5. No new threshold or production-safety claim is introduced.
6. Full final exact-head `python -m pytest -q tests` is green.
7. Fresh independent `governance_release_assurance` returns PASS before merge.
8. Post-merge exact-main Tests and GitHub→Hugging Face sync are verified where applicable.
