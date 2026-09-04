# Assurance handover — SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION

Date/time: 2026-09-05 01:52 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Role: `governance_release_assurance`  
Issue: #117  
PR: #118

## Exact reviewed identity

- Frozen candidate head: `37de6859ed5b17f4767c463f6db73085ce0d4b56`
- Expected base: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`
- Fresh merge-base: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`
- Pre-merge `main`: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`
- Synthetic merge candidate inspected: `71d6329fa7df64393417a299aea51105c570eb32`
- Synthetic merge parents: exact base `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84` + exact candidate `37de6859ed5b17f4767c463f6db73085ce0d4b56`

Final pre-verdict PR readback was open, draft, unmerged and mergeable. Compare showed the candidate ahead of the exact expected base/merge-base with `behind_by=0` and 12 commits.

## Exact changed-file scope

Exactly nine files changed:

1. `CHANGELOG.md`
2. `DECISION_LOG.md`
3. `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`
4. `ROADMAP.md`
5. `WORKPACKAGES.md`
6. `handover/workpackages/20260905_0139_repository_convergence_validation_hierarchy_clarification.md`
7. `tests/test_repository_convergence_bootstrap_contracts.py`
8. `tests/test_repository_convergence_validation_hierarchy_contracts.py`
9. `workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION.md`

No application/runtime source, recognizer/profile, threshold, corpus, benchmark runner/report implementation, GitHub Actions workflow implementation, dependency, Docker, Scrub Key, review/export/reinsert, replacement-memory or external-AI implementation file changed.

## Validation hierarchy reconstruction

### Level 1 — release regression authority

`.github/workflows/tests.yml` is the current repository-wide regression gate used for consequential candidate/main evidence:

- triggers on pull requests and pushes to `main` and also supports explicit dispatch/current evidence-carrier routing;
- executes `python -m pytest -q tests`;
- runs the committed full `tests/` directory;
- PR exact-SHA/merge-candidate and post-merge exact-main runs are the machine evidence used by the governance flow.

No other current workflow forms a competing general merge authority. The remaining workflows are a narrow evidence carrier, a focused historical document-fidelity validator, an explicitly diagnostic recall-report workflow and GitHub→Hugging Face sync.

### Level 2 — capability regression evidence

Focused suites for Phase-6 synthetic E2E, Scrub Key, document hygiene/fidelity, Zorg, recognizer/candidate-scanner contracts and Premium Streamlit/AppTest/state remain first-class capability-level regression evidence inside the full `tests/` suite. D045 does not dismiss or downgrade them; it distinguishes them from a second general merge authority.

### Level 3 — supplemental diagnostic

`recall_benchmark_runner.py`, `recall_benchmark_report.py` and `.github/workflows/recall-benchmark-report.yml` are correctly classified as supplemental diagnostic evidence.

`recall_benchmark_report.py` declares exact metadata:

```text
status = diagnostic_only
synthetic_corpus = True
production_gate = False
thresholds_enforced = False
```

The report workflow may fail on technical/schema/integrity defects, but it does not enforce recall/precision score thresholds as release or production gates.

### Level 4 — supplemental / historical diagnostic

- `benchmark/run_recall_precision.py` scores supplied prediction JSON; it does not run recognizers and explicitly applies no CI/production threshold.
- `benchmark/build_entity_scorecard.py` is report-only/non-gating.
- `benchmark/build_residual_risk_report.py` is report-only/non-gating and states foundation/coverage limitations.

These remain useful evidence and are not represented as production-safety proof.

## Governance/current-truth review

D045 matches the actual repository and does not claim stronger authority than source supports:

- one current general release regression gate is identified;
- focused capability/domain evidence remains visible and first-class;
- diagnostic evidence remains useful but non-gating;
- no diagnostic score is promoted to merge/production authority;
- no new production recall/precision threshold is introduced;
- synthetic evidence does not prove production safety;
- mandatory human review remains binding;
- no second Evidence Framework is created.

D044 and prior still-binding product/privacy decisions remain present. `WORKPACKAGES.md` records WP-CONVERGENCE-02 as completed/merged/verified and WP-CONVERGENCE-03 as the single current executable package while preserving the shared Streamlit/review/export/runtime sequencing rule. The debt ledger remains temporary/non-authoritative, issue-state reconciliation and dormant patch-script retirement remain visible future convergence work, and Stage-2 persistence/external-AI cleanup was not pulled forward.

`RISK_REGISTER.md` continues to treat false negatives and Zorg under-detection/clinical over-masking as critical, Scrub Key leakage/mismatch as critical, human review as mandatory, and synthetic evidence as insufficient for production-safety claims. The pseudonymisation versus guaranteed-anonymisation boundary remains intact.

## Test-contract review

### New validation-hierarchy contracts

`tests/test_repository_convergence_validation_hierarchy_contracts.py` checks:

- the real full-suite pytest command plus binding D045 authority language;
- exact diagnostic metadata imported from the real module;
- WP22/WP23/WP24 self-described non-release roles;
- continued visibility of capability regression families and roadmap prohibitions on diagnostic-score merge gates/new production thresholds.

It introduces no numeric quality threshold and does not promote the diagnostic workflow to merge authority.

Non-blocking test-depth observation: the new Level-1 contract pins the full pytest command but does not separately assert the `pull_request` and `push main` trigger lines. Current workflow source and raw Actions evidence prove those triggers are present and operational; this is not a material release defect for this candidate.

### Updated bootstrap contracts

The initial red cycle exposed four stale/format-specific assertions. Final remediation is legitimate:

- the old literal `WP-CONVERGENCE-02..N` placeholder was replaced by semantic parsing that requires exactly one `— CURRENT` executable workpackage;
- the already-resolved Docker startup invocation is no longer required as unresolved debt, while the dormant historical patch scripts remain visible/classified;
- the no-new-Evidence-Framework prohibition is bound to canonical decision authority instead of duplicated prose in the temporary ledger;
- workflow-path validation no longer depends on Markdown backticks.

The underlying product, privacy, sequencing and source-of-truth invariants remain protected.

## Implementation failure history independently reconstructed

Initial candidate run:

```text
Tests run: 33930040668
job: 101206596706
result: 4 failed, 1264 passed in 14.74s
```

The four failures were the stale/current-state and formatting bindings described above. Their final remediation did not remove a material safety or product invariant.

## Raw exact-head Actions evidence

Frozen head `37de6859ed5b17f4767c463f6db73085ce0d4b56`:

- workflow: `Tests`
- run: `33930363272`
- job: `101207533835`
- conclusion: `SUCCESS`
- raw command: `python -m pytest -q tests`
- raw result: `1268 passed in 14.77s`
- synthetic merge candidate: `71d6329fa7df64393417a299aea51105c570eb32`
- synthetic merge parents: exact base + exact frozen candidate.

## Formal assurance verdict

`PASS`

No material correctness, privacy, product, governance, validation-authority, CI, test-contract or scope defect was found on the exact frozen pair.

A normal GitHub `APPROVE` submission was rejected because the connected GitHub identity is also the PR author (`Can not approve your own pull request`). The independent PASS was therefore registered as an exact-SHA `governance_release_assurance` review comment bound to `37de6859ed5b17f4767c463f6db73085ce0d4b56`; any head/base movement would have invalidated the verdict.

## Authorized merge administration

After PASS only:

- PR #118 was marked ready without candidate-head movement;
- merge was executed with `expected_head_sha=37de6859ed5b17f4767c463f6db73085ce0d4b56`;
- merge succeeded.

Actual merge/main SHA:

`268d967db95d923a73a3979ffce2d0cab586e499`

Actual merge parents:

1. `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`
2. `37de6859ed5b17f4767c463f6db73085ce0d4b56`

Fresh post-merge `main` readback equals exact merge SHA `268d967db95d923a73a3979ffce2d0cab586e499`.

## Exact-main Tests

On exact merged `main` `268d967db95d923a73a3979ffce2d0cab586e499`:

- workflow: `Tests`
- run: `33930953130`
- job: `101209253695`
- event: `push`
- conclusion: `SUCCESS`
- raw command: `python -m pytest -q tests`
- raw result: `1268 passed in 11.68s`.

## GitHub → Hugging Face sync / path-ignore evidence

On the same exact merged main SHA:

- workflow: `Sync to Hugging Face Space`
- run: `33930953103`
- job: `101209253746`
- event: `push`
- conclusion: `SUCCESS`
- checkout/readback before push: `268d967db95d923a73a3979ffce2d0cab586e499`
- remote target: `huggingface.co/spaces/solidprivacy/scrub`
- remote push acknowledgement: `7e4f549..268d967  HEAD -> main`.

Although most changed docs/tests paths are ignored by the HF workflow, `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md` is not in its `paths-ignore` list. Therefore this docs/tests-only package correctly triggered sync rather than being fully suppressed by path-ignore.

## App verification

Status: `N/A — no application/runtime/UI semantics changed by this package`.

The candidate changed only governance/documentation/tests and administrative artifacts. No user-visible app or runtime file changed, so a functional app retest is not required for this package.

## Issue closeout

Issue #117 was closed as `completed` only after:

- exact-pair assurance PASS;
- exact-head guarded merge;
- exact-main Tests SUCCESS;
- exact-main HF sync SUCCESS and remote exact-SHA push acknowledgement.

## Findings

No material findings.

Non-blocking observations:

1. The new Level-1 hierarchy contract does not independently pin the `pull_request`/`push main` trigger lines; current source and raw workflow executions nevertheless establish the intended semantics.
2. Historical/diagnostic coverage remains bounded and synthetic; D045 correctly preserves that limitation rather than converting benchmark quality into a safety claim.

## Residual risks / deliberate non-scope

1. False-negative/recall and Zorg risks remain current and require human review; no production recall guarantee exists.
2. Diagnostic benchmark coverage remains synthetic/bounded and supplemental.
3. Dormant historical Streamlit patch scripts remain separate evidence-based RETIRE candidates.
4. GitHub issue/state reconciliation remains later Stage-1 convergence work.
5. Scrub Private persistence, external-AI/content-egress and content-log cleanup remain Stage-2 scope unless a separate present defect requires earlier repair.
6. The temporary debt ledger remains non-authoritative and should eventually become historical evidence at convergence closeout.

## Next recommended step

Return authority to `implementation_operations` to derive the next bounded Repository Convergence package from current canonical state. The current documentation points toward issue/state reconciliation as a likely next evidence cluster, but this assurance role does not create or execute that package.
