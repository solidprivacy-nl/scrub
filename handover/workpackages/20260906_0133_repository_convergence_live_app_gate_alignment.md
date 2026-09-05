# Handover — SCRUB-WP_REPOSITORY_CONVERGENCE_LIVE_APP_GATE_ALIGNMENT

## Repository worked in

`solidprivacy-nl/scrub`

## Workpackage title

`SCRUB-WP_REPOSITORY_CONVERGENCE_LIVE_APP_GATE_ALIGNMENT`

Role: `implementation_operations`  
Parent live gate: #96  
PR: #127  
Branch: `wp/repository-convergence-live-app-gate-alignment`  
Exact starting main/base: `2d4ab0446c20f08ad07576af326ab4b0df0a2af7`

## Status

**RELEASE_CANDIDATE_READY subject to one mandatory final full `Tests` run on the handover-complete exact head and subsequent fresh blind independent assurance.**

This handover is the final intended implementation file. The candidate must be frozen after the final green exact-head run.

## Business/current-truth outcome

WP04 is no longer current work. It independently PASSed, guarded-merged and completed its ordered administrative reconciliation.

The factual post-WP04 baseline is:

```text
WP04 reviewed head:
ce021443303cfa11de12f3273f872b2d027da5db

WP04 merge/current main at this package start:
2d4ab0446c20f08ad07576af326ab4b0df0a2af7

exact-main Tests:
33997889522
1279 passed in 14.51s
SUCCESS

GitHub → Hugging Face sync:
33997889554
SUCCESS
```

The 18 reviewed historical issues plus #119 and assurance #126 are closed. Issue #96 is the sole remaining open product-facing Repository Convergence gate.

This package aligns canonical repository truth to that state. It does **not** perform or claim the #96 deployed live-app verification.

## Current executable gate after this alignment

```text
WP-CONVERGENCE-05 — Consolidated deployed live-app verification — CURRENT
Issue #96 — OPEN
```

The remaining live evidence must verify on the deployed Hugging Face app with synthetic/approved material:

1. staged Standard/Expert state coherence;
2. exact marker/highlight offsets with leading whitespace/newlines;
3. compact bound-placeholder display with no long binding-token leakage or token fragmentation;
4. exact Dutch address span around `Polderweg 8` and representative legitimate Dutch address forms;
5. fail-closed source/review/export lineage;
6. explicit mandatory human review;
7. exact deployed Git SHA, date and concrete results.

CI and synchronization are not substitutes for this live verification.

## Files added/changed

Expected handover-complete PR #127 scope relative to base:

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

No application/runtime/UI/recognizer/profile/review/export/Scrub Key/reinsert/document-processing/dependency/workflow implementation file is intentionally changed.

## Implementation summary

- `WORKPACKAGES.md` now records WP04R and WP04 as completed and WP05/#96 as the sole current executable Repository Convergence package.
- `CHANGELOG.md` records factual WP04 completion and the narrow current-truth alignment package.
- `RISK_REGISTER.md` keeps R1/R2/R10 critical and updates R11 to the exact post-WP04 state; R6 still states the consolidated deployed live-app retest remains unproven.
- `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md` is advanced to post-WP04 truth while remaining explicitly temporary/non-authoritative; unresolved Private-line persistence/egress and dormant patch debt remain visible.
- the WP04 claim is closed to factual `OUTCOME_CONFIRMED` state rather than remaining a release candidate.
- the new WP05 alignment claim explicitly excludes product/runtime changes and does not claim live PASS.
- existing WP04/recovery tests were rebound from stale `WP04 CURRENT` assertions to factual historical WP04 completion and WP05 current-state invariants.
- a narrow new WP05 contract test freezes the exact residual live behavior and prevents #96 closure from CI/HF sync alone.

## Tests

### Red cycle

```text
head: f7be406bc2b1288e75cd51c809be53c6c8b382e5
run: 33998778220
job: 101393810800
result: 1 failed, 1281 passed in 10.33s
```

The only failure was the preserved bootstrap contract requiring the exact temporary-ledger marker `Runtime startup debt already resolved`. The ledger contained the same substantive PR #116 truth under a renamed heading. The fix restored the marker in the ledger rather than weakening the existing test.

### Pre-handover green

```text
head: 566ad9a84ea8fcebb6def343114b5a47c344e5a6
run: 33998886890
job: 101394093622
synthetic merge candidate: 5c94831274511607923eb68b1b541b13e4dd9159
result: SUCCESS — 1282 passed in 14.82s
```

A final full `Tests` run on the handover-complete PR head is mandatory after this file and the release-candidate claim are committed.

## Validation status

- WP04 factual completion: aligned and contract-checked;
- exactly one current Repository Convergence package = WP05: contract-checked;
- #96 remains OPEN/unproven in candidate documentation: contract-checked;
- marker/compact/address/lineage/human-review live acceptance contract: recorded and contract-checked;
- Stage 2: blocked;
- mandatory human review: preserved;
- product/runtime behavior: unchanged by intended scope;
- final handover-complete exact-head full regression: pending immediately after this commit;
- fresh independent governance assurance: pending.

## GitHub Actions status

Pre-handover full Tests: SUCCESS (`33998886890`, `1282 passed in 14.82s`).

Final exact frozen-head Tests must be read from the new PR head after this handover commit. Assurance must independently inspect the raw run/job/log.

## Hugging Face sync status

No accepted-main deployment exists for PR #127 before merge. The package changes governance/docs/tests only. A future PASS/merge should still verify actual GitHub→HF path-ignore/sync behavior for the exact merge SHA rather than assuming it.

## App verification status

**NOT COMPLETE — issue #96 remains OPEN and the consolidated deployed live-app retest remains unproven.**

This alignment candidate neither changes application behavior nor claims the live gate has passed.

The current monitoring runbook still distinguishes app verification from Actions/HF synchronization.

## Remaining risks

1. #96 remains a real user-visible live verification gate despite merged source repairs.
2. Marker/highlight, compact-placeholder and Dutch-address behavior must be verified together on the actual deployed app.
3. R1 false negatives, R2 Scrub Key and R10 Zorg remain critical.
4. Stage-2 Private persistence/external-AI/content-log work remains blocked until Repository Convergence is independently closed.
5. Dormant historical patch scripts remain separate evidence-based RETIRE candidates, not current work.
6. This implementation worker cannot self-certify PR #127.

## Next recommended step

1. Read PR #127 handover-complete exact head/base/merge-base and changed-file set.
2. Require a complete green `Tests` workflow on that exact head and inspect raw pytest output.
3. Freeze the exact candidate with no further implementation mutations.
4. Dispatch a genuinely fresh blind-first `governance_release_assurance` reviewer for PR #127 only.
5. PASS may authorize guarded merge of only the unchanged reviewed head.
6. After merge, verify exact-main Tests and GitHub→Hugging Face path-ignore/sync behavior.
7. Do **not** close #96 from this alignment package.
8. Return to WP05 live-app verification only after the canonical current-truth transition is confirmed.
