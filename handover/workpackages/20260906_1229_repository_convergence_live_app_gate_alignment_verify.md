# Assurance handover — SCRUB-WP_REPOSITORY_CONVERGENCE_LIVE_APP_GATE_ALIGNMENT_VERIFY

## Repository

`solidprivacy-nl/scrub`

## Role

`governance_release_assurance`

## Workpackage

`SCRUB-WP_REPOSITORY_CONVERGENCE_LIVE_APP_GATE_ALIGNMENT`

## Pull request

PR #127

## Exact reviewed identity

```text
frozen head: 763d21e2c8da8acf5334219ad1d63d811558c06d
base:        2d4ab0446c20f08ad07576af326ab4b0df0a2af7
merge-base:  2d4ab0446c20f08ad07576af326ab4b0df0a2af7
ahead_by:    12
behind_by:   0
changed:     10 files
```

The frozen branch and pre-merge `main` were re-read immediately before verdict and still matched the reviewed pair.

## Exact changed-file set

```text
CHANGELOG.md
REPOSITORY_CONVERGENCE_DEBT_LEDGER.md
RISK_REGISTER.md
WORKPACKAGES.md
handover/workpackages/20260906_0133_repository_convergence_live_app_gate_alignment.md
tests/test_repository_convergence_issue_state_reconciliation_contracts.py
tests/test_repository_convergence_issue_state_reconciliation_recovery_contracts.py
tests/test_repository_convergence_live_app_gate_alignment.py
workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION.md
workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_LIVE_APP_GATE_ALIGNMENT.md
```

No runtime/product/UI/recognizer/profile/review/export/Scrub Key/reinsert/document-processing/dependency/workflow implementation file changed.

## Blind-first sources

Before current PR body/comments, implementation handover or workpackage claim were used, assurance read the frozen candidate in this order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`
5. `RISK_REGISTER.md`
6. `DECISION_LOG.md`
7. `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`
8. `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`
9. canonical Execution & Engineering Constitution

Then GitHub object identity, full compare/diff, historical WP04 lifecycle, issue #96, relevant tests and raw Actions were reconstructed independently.

## Reconstructed WP04 provenance

PR #124 reviewed head:
`ce021443303cfa11de12f3273f872b2d027da5db`

WP04 merge/main:
`2d4ab0446c20f08ad07576af326ab4b0df0a2af7`

Fresh reconstruction established the required causal order:

1. independent `governance_release_assurance` PASS was recorded before merge;
2. guarded merge used exact reviewed head;
3. exact-main Tests run `33997889522` succeeded with `1279 passed in 14.51s`;
4. GitHub → Hugging Face sync run `33997889554` succeeded with `14baceb..2d4ab04 HEAD -> main`;
5. issue-state reconciliation occurred only afterwards;
6. #119 and #126 were closed after those post-merge gates.

Historical governance provenance remains intact. PR #120 merge commit `fd69294c67a59bb150f5d4a637daad2607c14077` remains an ancestor of recovery PR #122 merge `14baceb97b274de6ef35c42ce48441c4e74c5f08`, and that recovery remains an ancestor of the WP04 baseline. Current governance files continue to record PR #120's governance FAIL and PR #122 recovery; no force reset/history rewrite or retroactive FAIL→PASS reinterpretation was found.

## Issue #96 state and WP05 contract

Before verdict, #96 was OPEN and explicitly stated that consolidated deployed live-app verification after PR #108 + PR #111 remained unproven. CI/HF synchronization was explicitly non-substitutive.

The candidate makes exactly one current Repository Convergence package:

`WP-CONVERGENCE-05 — Consolidated deployed live-app verification — CURRENT`

WP04 is completed history, not CURRENT.

WP05 acceptance requires at least:

- staged Standard/Expert state coherence on authoritative state;
- exact marker/highlight offsets including leading whitespace/newlines;
- compact rendering of strict bound placeholders;
- no full binding-token leakage or token fragmentation;
- Dutch address precision around `Polderweg 8` and representative legitimate forms;
- fail-closed source/review/export lineage;
- explicit mandatory human review;
- exact deployed Git SHA;
- test date;
- concrete live outcomes.

`WP-CONVERGENCE-FINAL` remains blocked on WP05, `WP-CONVERGENCE-VERIFY` remains blocked on FINAL, and Stage 2 remains blocked on `SCRUB_REPOSITORY_CONVERGED`.

## Safety / debt

R1 false negatives, R2 Scrub Key and R10 Zorg remain critical. Mandatory human review remains binding. The candidate does not claim perfect anonymisation, perfect recall or production safety from synthetic/live spot checks.

`REPOSITORY_CONVERGENCE_DEBT_LEDGER.md` remains explicitly temporary/non-authoritative. Stage-2 blockers including persistent replacement memory, external AI processing and content-bearing logging remain visible. `fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py` still exist and remain separate dormant evidence-based RETIRE candidates; PR #127 neither deletes nor activates them.

## Regression history

### Red cycle

```text
head: f7be406bc2b1288e75cd51c809be53c6c8b382e5
Tests run: 33998778220
job: 101393810800
result: 1 failed, 1281 passed in 10.33s
```

The sole failure was the pre-existing bootstrap contract marker `Runtime startup debt already resolved`. The next remediation changed only the temporary ledger heading back to that existing marker. No test was weakened.

### Pre-handover green

```text
head: 566ad9a84ea8fcebb6def343114b5a47c344e5a6
Tests run: 33998886890
job: 101394093622
result: SUCCESS — 1282 passed in 14.82s
```

### Final frozen exact-head

```text
head: 763d21e2c8da8acf5334219ad1d63d811558c06d
Tests run: 33998972304
job: 101394319453
synthetic merge candidate: d4c928d91dc32b00b6a2d551c12beb01022a0449
result: SUCCESS — 1282 passed in 10.25s
```

Raw checkout proved:

`Merge 763d21e2c8da8acf5334219ad1d63d811558c06d into 2d4ab0446c20f08ad07576af326ab4b0df0a2af7`

## Formal verdict

`SCRUB-WP_REPOSITORY_CONVERGENCE_LIVE_APP_GATE_ALIGNMENT_VERIFY: PASS`

No material candidate finding remained.

## Governance / merge status

An exact-SHA PASS comment was registered on PR #127 before mutation. PR #127 was then marked ready without head movement and guarded-merged using hard `expected_head_sha=763d21e2c8da8acf5334219ad1d63d811558c06d`.

Actual merge SHA:
`a0fe29306a1f6875058d511466513f7ddb550760`

Exact parents:

```text
parent 1: 2d4ab0446c20f08ad07576af326ab4b0df0a2af7
parent 2: 763d21e2c8da8acf5334219ad1d63d811558c06d
```

Final `main` readback equals the merge SHA.

## Exact-main Actions

Tests:

```text
run: 34027429725
job: 101470788209
head: a0fe29306a1f6875058d511466513f7ddb550760
conclusion: SUCCESS
raw pytest: 1282 passed in 12.72s
```

GitHub → Hugging Face sync:

```text
run: 34027429743
job: 101470788494
head: a0fe29306a1f6875058d511466513f7ddb550760
conclusion: SUCCESS
raw push: 2d4ab04..a0fe293 HEAD -> main
```

The sync workflow ignores most governance/docs/tests paths but does not ignore `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`, so this governance merge legitimately triggered a sync. That is deployment/synchronization evidence only.

## Post-merge #96 administrative incident

Fresh post-merge readback detected that #96 had unexpectedly been closed at `2026-09-06T10:26:31Z`, two seconds after merge. Assurance did not request or perform that closure. GitHub issue events show a close event under the linked `market-predictions` identity at merge time, followed by a reference from merge commit `a0fe293...`; no live-app verification evidence accompanied it.

Because the reviewed current truth, issue body and assurance procedure all require #96 to remain OPEN until actual consolidated deployed live evidence exists, assurance administratively reopened #96 and recorded the correction on the issue. This did not modify the implementation candidate or `main`.

Final #96 readback after correction: OPEN / `state_reason=reopened`.

## App verification status

**NOT COMPLETE — #96 remains unproven.**

No deployed browser/live-app verification was performed from this assurance role. Exact-main CI and HF synchronization do not constitute WP05 live behavioral PASS.

## Findings

No material defect in the exact frozen candidate.

Post-merge administrative incident: #96 was transiently closed at merge time without live evidence and was restored to OPEN. Treat this as an issue-link/merge-administration hazard for future governance PR prose; avoid GitHub closing-keyword patterns around issues that must remain open.

## Remaining risks

1. #96 remains the real product-facing Repository Convergence gate.
2. Consolidated deployed behavior for marker offsets, compact placeholders, Dutch address precision, staged Standard/Expert state and fail-closed lineage remains unproven.
3. R1/R2/R10 remain critical.
4. Stage-2 persistence/external-AI/content-log work remains blocked.
5. Dormant startup patch scripts remain separate RETIRE candidates.
6. Governance authors should avoid accidental GitHub issue-closing keyword syntax in PR metadata when an issue is explicitly meant to remain open.

## Next recommended step

Return to `implementation_operations` / the separately governed WP05 live-app verification flow. Perform the consolidated deployed Hugging Face verification on synthetic/approved material, record exact deployed SHA/date/concrete outcomes, and obtain the required independent assurance before #96 may close. Do not start Stage 2 until Repository Convergence reaches its defined final gates.
