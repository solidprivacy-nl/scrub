# Workpackage claim — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY

Status: `IMPLEMENTATION_IN_PROGRESS`  
Role: `implementation_operations`  
Issue: #121  
Branch: `wp/repository-convergence-issue-state-reconciliation-governance-recovery`  
Starting main: `fd69294c67a59bb150f5d4a637daad2607c14077`  
Started: 2026-09-05 Europe/Amsterdam

## Trigger

Fresh blind `governance_release_assurance` for PR #120 returned `FAIL` because PR #120 had already merged and issue #74 had already been closed before the required independent pre-action verdict.

This is a release-ordering/governance defect. The reviewed eight-file PR #120 content was not found materially defective.

## Exact recovery objective

Restore a truthful pre-reconciliation authority state without rewriting Git history or force-resetting `main`:

1. restore the prematurely mutated issue #74 to open state with explicit recovery provenance;
2. remove prematurely adopted WP04 candidate-specific claim/test/handover artifacts from the active tree while preserving them in Git history;
3. keep independently proven PR #118 / D045 validation-authority facts current;
4. represent this recovery package as the single current executable Repository Convergence workpackage;
5. record the premature PR #120 merge and assurance FAIL as current/history facts;
6. leave #96 open and explicitly unproven;
7. do not perform any further issue reconciliation until a new WP04 candidate later receives a fresh independent PASS.

## Proven current state at claim start

```text
pre-WP04 governance-valid main:
268d967db95d923a73a3979ffce2d0cab586e499

premature PR #120 head:
1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a

premature merge / current main:
fd69294c67a59bb150f5d4a637daad2607c14077
```

PR #120 merge parents are exactly the pre-WP04 main and frozen candidate above.

Issue #74 was prematurely closed as `completed` after the merge. It has been reopened with a recovery note before repository recovery implementation continued.

## Scope

Authorized:

- update `WORKPACKAGES.md`, `CHANGELOG.md`, `RISK_REGISTER.md` and the temporary convergence debt ledger to truthful recovery state;
- preserve the accepted D045 status in `DECISION_LOG.md` unchanged;
- remove the prematurally adopted WP04-specific test/claim/handover from the active tree;
- minimally generalize the existing one-current-workpackage contract to accept the explicit recovery suffix `04R` while retaining the exactly-one invariant;
- add this recovery claim and mandatory recovery handover;
- open a draft recovery PR and run full exact-head Tests.

Not authorized:

- force-reset or force-push `main`;
- alter product/runtime/UI/recognizer/review/export/Scrub Key/reinsert behavior;
- close any of the 17 historical issue candidates;
- close or weaken #96;
- perform the final consolidated live-app retest;
- start Stage 2;
- merge the recovery candidate before fresh blind independent PASS.

## Acceptance

1. Issue #74 is open again with truthful recovery provenance.
2. Git history still records the premature PR #120 merge and later FAIL.
3. Exactly one current executable workpackage exists: WP-CONVERGENCE-04R recovery.
4. PR #118/D045 remains represented as independently PASSed, merged and exact-main verified.
5. The failed PR #120 issue-disposition model is no longer executable current authority.
6. #96 remains the explicit residual unproven deployed live-app gate.
7. Full exact-head `Tests` is green.
8. Fresh blind `governance_release_assurance` PASSes the recovery candidate before any recovery merge.
9. Only after guarded recovery merge and exact-main verification may a new WP04 issue-reconciliation candidate be created from the new main.
