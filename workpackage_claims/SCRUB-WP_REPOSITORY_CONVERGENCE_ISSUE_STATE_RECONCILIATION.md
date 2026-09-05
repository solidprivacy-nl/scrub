# Workpackage claim — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION

Status: implementation in progress  
Role: `implementation_operations`  
Issue: #119  
Branch: `wp/repository-convergence-issue-state-reconciliation`  
Starting main: `268d967db95d923a73a3979ffce2d0cab586e499`  
Started: 2026-09-05 Europe/Amsterdam

## Objective

Reconcile stale open GitHub issues against accepted `main` without erasing assurance history or falsely closing the one remaining deployed live-app verification gate.

## Source-derived finding

At package start GitHub returned 18 open historical/current Premium/governance issues:

```text
#74 #75 #76 #77
#79 #81 #84 #86 #88 #89
#96 #98 #100 #105
#106 #107 #109 #112
```

The issue set does not represent 18 current blockers.

Independent evidence already present in GitHub shows:

- final PR #73 recovery head received blind PASS in #77 and PR #73 merged; #74/#75/#76 are prior failed/repaired dispatch states;
- Premium contract/state/staged-workspace lines were merged and later App-Shell defects were repaired by newer candidates;
- fresh issue #105 assurance ultimately PASSed PR #104 V2 and PR #104 merged, technically superseding the old #93 PASS / #92 FAIL source-state conflict;
- issue #109 records blind PASS for PR #108 marker/compact-placeholder repair and PR #108 is merged;
- issue #112 records blind PASS for PR #111 Dutch-address precision repair and PR #111 is merged;
- issue #96 explicitly remained open after those technical repairs because the required consolidated deployed live-app retest was not yet proven.

## Reviewed disposition candidate

No issue mutation is authorized by implementation alone. The intended action after fresh independent PASS is:

### Keep open

```text
#96
```

#96 becomes the single residual current Premium/App-Shell gate. Its current description must state that PR #104, PR #108 and PR #111 are repaired/assured/merged and that the remaining requirement is one consolidated deployed live retest after both live-regression repairs.

### Close with evidence-aware comments

```text
#74 #75 #76 #77
#79 #81 #84 #86 #88 #89
#98 #100 #105
#106 #107 #109 #112
```

These closures mean the individual candidate/repair/assurance cycles are no longer current open work. They do **not** rewrite historical FAIL/INDETERMINATE/PASS outcomes and do **not** claim #96's final live test occurred.

## Repository scope

Authorized:

- update `WORKPACKAGES.md` so WP-CONVERGENCE-03 is completed and WP-CONVERGENCE-04 is the one current package;
- update `CHANGELOG.md` with actual PR #118 PASS/merge/exact-main evidence and this package;
- update D045 status from pending candidate language to independently assured/merged;
- update R6/R11/R12 current risk wording to actual merged state;
- update the temporary convergence ledger with accepted main, resolved validation authority and the exact reviewed issue-disposition candidate;
- add one narrow contract test for current queue and disposition invariants;
- write the mandatory handover.

Not authorized:

- product/runtime/UI/recognizer/review/export/Scrub Key/reinsert changes;
- Stage-2 persistence/AI-egress changes;
- a new permanent issue ledger/framework;
- closing #96 without actual live evidence;
- claiming the final live retest was performed;
- mutating GitHub issue state before fresh independent assurance.

## Acceptance

1. Exactly one current executable workpackage: WP-CONVERGENCE-04.
2. PR #118/D045 is represented as PASSed/merged/exact-main verified.
3. The reviewed disposition contains exactly 17 closure candidates and exactly one retained Premium gate, #96.
4. #96 is absent from the closure set.
5. The unresolved consolidated deployed live-app retest remains explicit in WORKPACKAGES, RISK_REGISTER and the temporary ledger.
6. Existing product-risk and human-review boundaries remain unchanged.
7. Full exact-head `Tests` is green.
8. Fresh blind `governance_release_assurance` PASSes exact candidate before merge or issue mutation.
9. After authorized merge, exact-main Tests/HF sync/path-ignore behavior is independently verified before applying/confirming issue closeout.
