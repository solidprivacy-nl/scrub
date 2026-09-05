# Workpackage claim — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION

Status: `RELEASE_CANDIDATE_READY — final handover-complete exact-head Tests still required`  
Role: `implementation_operations`  
Issue: #119  
PR: #124  
Branch: `wp/repository-convergence-issue-state-reconciliation-v2`  
Exact starting main/base: `14baceb97b274de6ef35c42ce48441c4e74c5f08`  
Started: 2026-09-05 Europe/Amsterdam

## Objective

Reconcile stale Premium/governance issue state against governed current `main` while preserving the one genuinely unproven deployed live-app gate and enforcing a release order that cannot repeat PR #120's governance failure.

## Fresh-candidate boundary

This is a new candidate lifecycle from post-recovery main.

Historical PR #120 evidence may inform the substantive issue reconstruction, but none of the following are reused as release authority:

- PR #120 candidate identity;
- PR #120 merge;
- PR #120 CI;
- the later PR #120 assurance FAIL;
- recovery PR #122 PASS.

The new candidate must earn its own exact-head full-suite evidence and fresh blind `governance_release_assurance` verdict.

## Exact issue-disposition candidate

### Keep open

```text
#96
```

Reason: PR #104 V2, PR #108 and PR #111 technical repair chains are independently PASSed/merged, but the consolidated deployed live-app retest after both live regressions remains unproven.

### Close only after PASS + guarded merge + exact-main verification

```text
#74 #75 #76 #77
#79 #81 #84 #86 #88 #89
#98 #100 #105
#106 #107 #109 #112
```

The closures mean those individual candidate/repair/assurance cycles are no longer current open work. They do not erase historical PASS/FAIL/INDETERMINATE provenance and do not claim #96's live verification occurred.

## Required action fence

Implementation and pre-verdict assurance perform **zero target issue mutations**.

Required action order:

```text
exact candidate on 14baceb...
→ full Tests
→ fresh blind PASS
→ guarded merge exact reviewed head
→ exact-main Tests + GitHub→HF verification
→ only then close the 17 reviewed issues and reconcile #96 body while keeping it OPEN
→ readback all issue states
→ close #119 only after confirmed administrative outcome
```

The post-merge exact-main verification prerequisite is intentionally stronger than merely requiring PASS before issue mutation. It prevents the same ordering class from recurring.

## Repository scope

Authorized:

- align `WORKPACKAGES.md` from completed recovery to fresh WP04 current state;
- record recovery completion and fresh retry in `CHANGELOG.md`;
- align R11 in `RISK_REGISTER.md` to governed recovery/current retry;
- align `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md` to the new base and exact disposition candidate;
- close the stale recovery claim to factual PASS/merged/verified state;
- update the recovery contract from `04R CURRENT` to `04R COMPLETED / WP04 CURRENT`;
- add a narrow fresh WP04 contract test;
- add this claim and mandatory implementation handover.

Not authorized:

- product/runtime/UI/recognizer/profile/review/export/Scrub Key/reinsert changes;
- Stage-2 persistence/external-AI/logging work;
- any target issue closure/update before fresh PASS + merge + exact-main verification;
- closing or weakening #96;
- claiming the consolidated deployed live-app retest occurred;
- creating a new permanent issue ledger/framework.

## Validation history

The fresh retry deliberately retained two red contract-hardening cycles instead of hiding them.

### Red cycle 1 — wording-coupled policy assertions

```text
head: 4f9e85d87a4040b78b64f6689e23bfb8a67d179d
Tests run: 33968392839
job: 101312453646
result: 3 failed, 1275 passed in 14.22s
```

The three failures were in the newly added governance tests. They required exact prose fragments even though the candidate already encoded the intended sequencing and non-reuse semantics. No product/runtime code or issue disposition was changed. The tests were rebound to semantic invariants and explicit action ordering.

### Red cycle 2 — action parser used an abstract label absent from the fenced action block

```text
head: b654a287dd38d46eab6b974766cb68bdb1e031c8
Tests run: 33968545987
job: 101312859816
result: 1 failed, 1277 passed in 15.25s
```

The remaining test looked for the abstract phrase `issue mutation` inside the fenced action-order block, while the block deliberately names the concrete action `close the 17 reviewed issues`. The parser was tightened to the concrete action. The governance fence itself was not weakened.

### Pre-handover green

```text
head: bd44baaebd5a800fe38151495d7591db4eab78ac
Tests run: 33968625302
job: 101313068109
synthetic merge candidate: c1d9df47f91bc08eb2559d606e25d528fcada162
result: SUCCESS — 1278 passed in 14.88s
```

The mandatory implementation handover is committed after this pre-handover green run. Therefore one final complete `Tests` run on the handover-complete exact PR head remains mandatory before assurance dispatch. That final head must not move after the run.

## Acceptance

1. Exact base is `14baceb97b274de6ef35c42ce48441c4e74c5f08`.
2. Recovery PR #122 is factual completed history, not current execution authority.
3. Exactly one current executable package is WP-CONVERGENCE-04.
4. Contract freezes exactly keep `{96}` and close `{74,75,76,77,79,81,84,86,88,89,98,100,105,106,107,109,112}`.
5. #96 is excluded from closures and `remains unproven` is explicit.
6. Stage 2 stays blocked and mandatory human review remains preserved.
7. No runtime/product path is changed.
8. Full final exact-head `Tests` is green.
9. Fresh blind assurance PASS precedes merge.
10. Exact-main Tests/HF evidence is confirmed after guarded merge and before target issue mutation.
11. Final issue readback confirms 17 closures and #96 OPEN/current residual wording.
