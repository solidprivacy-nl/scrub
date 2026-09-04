# Handover — SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION

## Repository worked in

`solidprivacy-nl/scrub`

## Workpackage title

`SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION`

## Role

`implementation_operations`

## Issue / PR / branch

- Issue: #117
- PR: #118
- Branch: `wp/repository-convergence-validation-hierarchy`
- Exact starting main/base: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`

## Status

Implementation complete. Final exact-head regression is still required after this handover commit. Fresh independent `governance_release_assurance` is mandatory before merge.

## Business/root-cause objective

Remove ambiguity about validation authority without building a new validation framework or changing product/runtime behavior.

The repository contains multiple mature validation generations. Source inspection proved that they do not all have the same authority:

1. `.github/workflows/tests.yml` runs `python -m pytest -q tests` on pull requests and `main`; this is the current exact-SHA release regression gate.
2. Focused test families inside the full suite are capability-level regression evidence.
3. The recognizer-backed recall report is diagnostic: `recall_benchmark_report.py` declares `status=diagnostic_only`, `production_gate=False`, `thresholds_enforced=False`.
4. WP22 (`benchmark/run_recall_precision.py`) scores supplied prediction JSON and explicitly does not call recognizers.
5. WP23/WP24 scorecard/residual-risk helpers are report-only/non-gating and retain coverage limitations.

The previous documentation did not define these authority boundaries sharply enough, creating a risk that diagnostic reports could later be mistaken for release gates.

## Files added/changed

Expected final changed-file scope relative to starting main:

- `CHANGELOG.md`
- `DECISION_LOG.md`
- `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `tests/test_repository_convergence_bootstrap_contracts.py`
- `tests/test_repository_convergence_validation_hierarchy_contracts.py`
- `workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION.md`
- `handover/workpackages/20260905_0139_repository_convergence_validation_hierarchy_clarification.md`

No application/runtime/workflow implementation, corpus, recognizer, threshold, dependency, Scrub Key, review, export, reinsert, persistence or external-AI file is intentionally in scope.

## Decisions/materialization

### D045

Added D045 to `DECISION_LOG.md`:

- one release regression gate: `.github/workflows/tests.yml` → full `tests/` suite on exact candidate/main SHA;
- focused capability/domain suites remain first-class regression evidence but not competing merge authorities;
- recognizer-backed recall benchmark/report is supplemental diagnostic evidence;
- WP22/WP23/WP24 are supplemental/historical diagnostic evidence, not release authority;
- no diagnostic score becomes a merge/production gate;
- no production recall/precision threshold is introduced by convergence;
- synthetic evidence does not prove production safety or remove mandatory human review;
- no second Evidence Framework may be introduced merely to unify these assets.

### ROADMAP

Validation strategy now mirrors D045 and no longer implies that a diagnostic report path is a candidate release authority.

### WORKPACKAGES

- records WP-CONVERGENCE-02 / PR #116 as completed, independently PASSed, merged and exact-main/HF verified;
- makes WP-CONVERGENCE-03 current;
- keeps issue-state reconciliation as the next evidence-derived candidate package;
- keeps dormant patch-script retirement separate;
- keeps replacement-memory/external-AI Private adaptation behind the Stage-2 boundary.

### Temporary debt ledger

- records live Docker startup mutation invocation as resolved by accepted PR #116;
- classifies full Tests workflow as `CANONICAL RELEASE REGRESSION GATE`;
- classifies focused test families as `CANONICAL CAPABILITY REGRESSION EVIDENCE`;
- classifies recognizer-backed recall as `SUPPLEMENTAL DIAGNOSTIC`;
- classifies WP22/WP23/WP24 as `SUPPLEMENTAL / HISTORICAL DIAGNOSTIC`;
- remains explicitly temporary/non-authoritative after convergence.

## Tests added/changed

### New

`tests/test_repository_convergence_validation_hierarchy_contracts.py`

Protects:

- actual full Tests workflow command;
- D045 existence and hierarchy labels;
- exact `DIAGNOSTIC_METADATA` policy from `recall_benchmark_report.py`;
- WP22/WP23/WP24 self-described non-release roles;
- capability regression evidence remains subordinate rather than competing authority;
- roadmap prohibition on diagnostic-score merge gates/new production thresholds.

### Existing bootstrap contracts updated

`tests/test_repository_convergence_bootstrap_contracts.py`

Only stale convergence-placement assertions were rebound:

- one-current-queue invariant is now parsed semantically instead of requiring obsolete placeholder `WP-CONVERGENCE-02..N` text;
- already-resolved live startup invocation is no longer required to appear as unresolved debt;
- D045 is included among current binding decisions;
- the no-new-Evidence-Framework contract is bound to canonical D045 rather than requiring duplicate prose in the temporary debt ledger.

No product safety invariant was intentionally removed.

## Validation history

### Initial PR run — RED

- Tests run: `33930040668`
- Job: `101206596706`
- Merge candidate: `3c7080ececdcef9162d9c796536087b41a898541`
- Result: `4 failed, 1264 passed in 14.74s`

Failures:

1. old bootstrap test required literal `WP-CONVERGENCE-02..N` in current WORKPACKAGES;
2. old bootstrap test required the already-resolved live Docker startup invocation as a current ledger capability;
3. old bootstrap test required duplicate `no new framework` prose in the temporary ledger;
4. new hierarchy test required Markdown backticks around `.github/workflows/tests.yml`.

Assessment: all four were documentation/test-contract authority drift; none indicated runtime/product failure.

### Corrected pre-final run — GREEN

- Head: `2147c854b344e628515076a624efc6176a74ca84`
- Tests run: `33930216093`
- Job: `101207097941`
- Merge candidate: `ebeedfc2e0e874a739f7c0b9addbcbbae205e563`
- Result: `1268 passed in 13.72s`
- Conclusion: SUCCESS

The test count increased by four because the new validation-hierarchy contract file adds four tests.

## Validation status

Pre-final implementation validation: GREEN.

Final exact-head validation: PENDING because claim/changelog/handover commits were deliberately made after the pre-final run. No further implementation changes are intended. The resulting head must receive the full Tests workflow again and then be frozen.

## GitHub Actions status

- Initial candidate: FAIL as documented above.
- Corrected pre-final candidate: SUCCESS (`1268 passed`).
- Final handover-complete candidate: PENDING.

## Hugging Face sync status

Not applicable pre-merge. This package has no application/runtime changes, but repository governance requires post-merge GitHub→HF sync/path-ignore behavior to be verified where triggered.

## App verification status

Expected N/A: this workpackage changes validation authority documentation/tests only and no application/UI/runtime semantics.

## Remaining risks

- validation hierarchy remains candidate state until fresh blind independent assurance PASS and merge;
- open stale GitHub Premium/governance issue state remains unresolved and is the next likely convergence cluster;
- dormant historical Streamlit patch scripts remain separate RETIRE candidates;
- Scrub Private persistence/external-AI/content-log changes remain deliberately deferred to Stage 2 unless a present defect independently requires repair;
- diagnostic benchmark quality/coverage limitations remain visible; D045 does not turn them into production gates or assert production safety.

## Next recommended step

1. Run full exact-head `Tests` on the handover-complete candidate.
2. If green, freeze the exact branch SHA with no further mutations.
3. Record exact run/job/merge-candidate evidence in PR #118 conversation without changing the branch.
4. Dispatch a completely fresh blind-first `governance_release_assurance` reviewer for exactly that frozen SHA.
5. Only PASS may authorize exact-head guarded merge and post-merge exact-main Tests/HF verification.
6. After WP-CONVERGENCE-03 completes, derive the next package from current evidence; current leading candidate is GitHub issue/state reconciliation.
