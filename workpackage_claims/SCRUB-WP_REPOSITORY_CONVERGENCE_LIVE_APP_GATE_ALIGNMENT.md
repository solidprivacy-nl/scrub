# Workpackage claim — SCRUB-WP_REPOSITORY_CONVERGENCE_LIVE_APP_GATE_ALIGNMENT

Status: `RELEASE_CANDIDATE_READY — mandatory final handover-complete exact-head Tests still required`  
Role: `implementation_operations`  
Parent live gate: #96  
PR: #127  
Branch: `wp/repository-convergence-live-app-gate-alignment`  
Exact starting main/base: `2d4ab0446c20f08ad07576af326ab4b0df0a2af7`  
Started: 2026-09-06 Europe/Amsterdam

## Objective

Restore canonical current truth immediately after the independently PASSed WP04 reconciliation by marking WP04 completed and making the still-unproven consolidated deployed live-app gate #96 the sole current Repository Convergence package.

This package changes governance/docs/contracts only. It does not claim the live app already passes.

## Proven starting truth

WP04 / PR #124:

```text
reviewed head: ce021443303cfa11de12f3273f872b2d027da5db
merge/main:     2d4ab0446c20f08ad07576af326ab4b0df0a2af7
Tests:          33997889522 — 1279 passed in 14.51s
HF sync:        33997889554 — SUCCESS
```

The 18 reviewed historical issues and #119/#126 are closed. #96 remains open. PR #122 recovery evidence is historical provenance and does not authorize this package or the #96 live outcome.

## Current live gate

#96 remains open because repository regression and GitHub→Hugging Face synchronization do not prove the final deployed user-facing flow.

Required deployed verification includes:

- Standard/Expert staged-flow state coherence;
- exact marker/highlight offsets with leading whitespace/newlines;
- compact review display for strict bound placeholders without full-token leakage or fragmentation;
- exact Dutch address span for `Polderweg 8` and representative legitimate address forms;
- fail-closed source/review/export lineage;
- explicit mandatory human review.

## Scope

Authorized:

- update `WORKPACKAGES.md` to mark WP04 completed and WP05 current;
- update `CHANGELOG.md`, `RISK_REGISTER.md` and temporary convergence ledger to current post-WP04 truth;
- close the WP04 implementation claim to factual post-merge state;
- update/rebind convergence governance tests from old WP04-current assertions to WP04-completed/WP05-current invariants;
- add a narrow WP05 alignment claim/test/handover.

Explicit exclusions:

- no runtime/product/UI/recognizer/review/export/Scrub Key/reinsert change;
- no Stage-2 persistence/egress work;
- #96 remains open until actual deployed live evidence exists;
- no new permanent evidence framework;
- no browser automation platform, service or generalized live-test subsystem is introduced by this alignment package.

## Safety boundary

- mandatory human review remains binding;
- R1 false negatives, R2 Scrub Key and R10 Zorg remain critical;
- synthetic or deployed spot verification does not prove perfect anonymisation, perfect recall or production safety;
- Hugging Face remains an application-validation surface, not confidential-production infrastructure assurance.

## Validation history

### Red cycle — preserved bootstrap marker

```text
head: f7be406bc2b1288e75cd51c809be53c6c8b382e5
Tests run: 33998778220
job: 101393810800
result: 1 failed, 1281 passed in 10.33s
```

The only failure was the existing bootstrap contract requiring the exact ledger marker `Runtime startup debt already resolved`. The rewritten ledger preserved the same substantive PR #116 truth but had renamed that heading. The implementation restored the existing marker in the temporary ledger instead of weakening the bootstrap test.

### Pre-handover green

```text
head: 566ad9a84ea8fcebb6def343114b5a47c344e5a6
Tests run: 33998886890
job: 101394093622
synthetic merge candidate: 5c94831274511607923eb68b1b541b13e4dd9159
result: SUCCESS — 1282 passed in 14.82s
```

The mandatory implementation handover is committed after this green run. Therefore one final complete `Tests` run on the handover-complete exact PR head remains mandatory before assurance dispatch. The final reviewed head must not move after that run.

## Acceptance

1. WP04 is completed in canonical current docs using exact reviewed/merge evidence.
2. WP05/#96 is exactly the one current Repository Convergence package.
3. #96 is described as OPEN and `remains unproven` until real deployed verification occurs.
4. Stage 2 remains blocked.
5. Historical PR #120 governance FAIL and PR #122 recovery provenance remain intact.
6. No runtime/product path changes.
7. Full exact-head Tests are green.
8. Fresh independent governance assurance is required before merging this canonical current-truth transition.
