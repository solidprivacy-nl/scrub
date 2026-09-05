# Assurance handover — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION

Date/time: 2026-09-05 12:28 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Role: `governance_release_assurance`  
Issue: #119  
PR: #120

## Exact reviewed identity

- Frozen candidate: `1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a`
- Expected base / merge-base / pre-merge main: `268d967db95d923a73a3979ffce2d0cab586e499`
- Fresh compare: `ahead_by=13`, `behind_by=0`, merge-base exact expected base.
- Final PR-run synthetic merge candidate: `9858345a9d5a7cfaabd1fd4f4634e94ccbd27a0e`, built from exact base + candidate.

## Exact candidate scope

Fresh compare showed exactly eight files:

1. `CHANGELOG.md`
2. `DECISION_LOG.md`
3. `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`
4. `RISK_REGISTER.md`
5. `WORKPACKAGES.md`
6. `handover/workpackages/20260905_0212_repository_convergence_issue_state_reconciliation.md`
7. `tests/test_repository_convergence_issue_state_reconciliation_contracts.py`
8. `workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION.md`

No product/runtime/UI, recognizer/profile, threshold, review/export, Scrub Key, reinsert, document-processing, replacement-memory, external-AI, dependency or workflow implementation file changed.

## Independent 18-issue disposition reconstruction

The substantive disposition encoded by the candidate is supported.

### KEEP OPEN

```text
#96
```

PR #104 V2 was independently PASSed and merged; PR #108 marker/compact repair was independently PASSed and merged; PR #111 Dutch-address precision repair was independently PASSed and merged. However, no evidence was found for one consolidated deployed live-app retest after the repaired PR #108 + PR #111 state. Therefore #96 remains the residual Premium/App-Shell gate: `TECHNICAL REPAIRS COMPLETE / CONSOLIDATED LIVE RETEST STILL REQUIRED`, status OPEN / UNPROVEN. CI and Hugging Face synchronization do not satisfy this live gate.

### CLOSE AFTER VALID PASS + MERGE + POST-MERGE EVIDENCE

```text
#74 #75 #76 #77
#79 #81 #84 #86 #88 #89
#98 #100 #105
#106 #107 #109 #112
```

Evidence summary:

- #74/#75/#76/#77: PR #73 had genuine failed/repaired assurance cycles followed by final fresh exact-head PASS and merge; the historical findings remain provenance but the issues are no longer current blockers.
- #79/#81: Premium contract/state work was independently assured and merged; later App-Shell work superseded it as current execution authority.
- #84/#86/#88/#89: staged-workspace/state/shell cycles are historical predecessors of the later App-Shell repair chain; they no longer represent independent current blockers.
- #98/#100: first repair candidate PR #99 closed unmerged and was superseded by V2.
- #105: PR #104 V2 independently PASSed and merged; later live defects were separated into targeted repairs, with residual live verification preserved in #96.
- #106/#109: PR #108 marker/compact repair independently PASSed and merged; no separate implementation defect remains under this pair.
- #107/#112: PR #111 Dutch-address repair independently PASSed and merged; no separate implementation defect remains under this pair.

Thus the exact 17-close / #96-keep classification is substantively correct.

## Repository current-truth review

Candidate source correctly marks WP-CONVERGENCE-03 completed, makes WP-CONVERGENCE-04 the one current executable package, records PR #118/D045 as independently assured/merged/exact-main verified, preserves shared Streamlit/review/export/runtime sequencing, keeps Stage 2 blocked, keeps D045 accepted rather than pending, records R6's live-app retest as unproven, preserves R8/R11/R12 current truth, and retains critical false-negative, Scrub Key and Zorg risks plus mandatory human review and the synthetic-evidence limitation.

The debt ledger remains explicitly temporary/non-authoritative, freezes the disposition only for assurance, excludes #96 from closure, explicitly says the consolidated deployed live-app retest `remains unproven`, and introduces no permanent issue-tracking framework.

## Contract-test review

`tests/test_repository_convergence_issue_state_reconciliation_contracts.py` is materially sound. It protects WP03 completion, exactly one current WP04, keep set `{96}`, the exact 17-close set, #96 exclusion, explicit live-app-retest/unproven wording, Stage-2 blocking, human review and no-new-permanent-framework boundaries. The parser reads explicit fenced disposition blocks, avoiding explanatory PR numbers being reinterpreted as issue IDs.

## CI reconstruction

Red cycle 1:

```text
head 0b1c47faf5b5f1b4f55385e970ed6f617a35a757
run 33931758642 / job 101211615952
1 failed, 1271 passed in 8.98s
```

Cause independently reproduced: explanatory PR refs leaked into keep-open parsing. Fenced-list parsing is a legitimate correction.

Red cycle 2:

```text
head 0d2e28ae713f725df9aec5abb1f253f642cae6ef
run 33931829877 / job 101211823357
1 failed, 1271 passed in 8.61s
```

Cause: canonical phrase `consolidated deployed live-app retest` was absent. Standardization improved residual-gate clarity.

Red cycle 3:

```text
head b259ba27f62163f013e9647ac0e7f894f4b9b95b
run 33931948111 / job 101212181362
1 failed, 1271 passed in 14.43s
```

Cause: the ledger described lack of proof but did not explicitly encode `remains unproven`. Adding it strengthened the safety invariant.

Final frozen candidate:

```text
head 1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a
Tests run 33932180435 / job 101212872885
SUCCESS
raw: 1272 passed in 16.24s
synthetic merge candidate 9858345a9d5a7cfaabd1fd4f4634e94ccbd27a0e
```

## Formal verdict

`FAIL`

## Finding F1 — pre-merge assurance gate bypassed

Severity: `HIGH`

Exact state/location: PR #120 release lifecycle / repository `main`; issue #74 administrative state.

Evidence:

- Binding governance required fresh independent assurance PASS before merge and before issue-state mutation.
- Fresh readback found PR #120 already closed/merged before this assurance verdict.
- Actual merge/main SHA: `fd69294c67a59bb150f5d4a637daad2607c14077`.
- Actual merge parents are exact expected base `268d967db95d923a73a3979ffce2d0cab586e499` and candidate `1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a`.
- Merge timestamp: 2026-09-05T09:15:25Z.
- Issue #74 was already closed at 2026-09-05T09:15:26Z, before this fresh assurance verdict.
- The implementation claim/handover, inspected only after the initial blind verdict, independently state the same required order: fresh assurance before merge or issue-state mutation.

Why it matters:

Independent assurance is an ordering control. Once the candidate is already merged and issue state has begun changing, this review cannot serve as the required pre-merge release decision. Correct candidate content, green exact-head CI, exact merge parents and post-merge success cannot retroactively restore that independence property.

Smallest complete remediation:

Return authority to implementation/coordination. Preserve history. Use a normal governed recovery/revert path rather than a force-reset: revert the premature PR #120 merge, restore partially mutated issue state such as #74 to truthful pre-reconciliation state, derive a fresh WP04 candidate from the recovered current `main`, freeze a new exact base/head pair, rerun full exact-head Tests, and dispatch genuinely fresh blind assurance before any new merge or issue-state mutation. Only a future PASS may authorize guarded merge and the 17-close / #96-keep reconciliation. #96 must remain open throughout.

## Post-merge technical evidence

The premature merged main is technically green, but this does not cure F1:

- exact main: `fd69294c67a59bb150f5d4a637daad2607c14077`;
- exact-main Tests run `33957487868`: SUCCESS;
- raw pytest: `1272 passed in 14.45s`;
- Hugging Face sync run `33957487866`: SUCCESS on the same main SHA.

## Final issue-state readback

At assurance closeout:

- #74: CLOSED / completed;
- #75 #76 #77 #79 #81 #84 #86 #88 #89 #98 #100 #105 #106 #107 #109 #112: OPEN;
- #96: OPEN; residual consolidated live-app verification remains unproven;
- #119: OPEN.

The reconciliation is therefore only partially applied. Nothing in this review claims #96's live test occurred.

## App verification

PR #120 itself: `N/A — governance/docs/tests only`.

This is not execution or satisfaction of #96. The consolidated deployed live-app retest remains unproven.

## Assurance-role actions

No implementation candidate repair was made. No issue was closed, reopened or edited. No PR was merged or reverted. No product/runtime/UI mutation was performed. This handover exists only on the separate assurance branch.

## Residual risks

- release-governance provenance remains inconsistent until the premature merge/state mutation is recovered explicitly;
- #96 remains a real deployed user-visible verification gate;
- issue state is internally inconsistent because #74 alone is closed while the other 16 intended closure candidates remain open;
- dormant historical Streamlit patch scripts remain separate RETIRE candidates;
- Stage-2 Scrub Private persistence/external-AI/content-log adaptation remains blocked pending truthful Repository Convergence closeout.

## Next recommended step

Implementation/coordination should execute only the smallest governed recovery for F1, then create a fresh WP04 release candidate and re-enter the exact-head assurance lifecycle. This assurance role must not perform that recovery or start the next implementation workpackage.
