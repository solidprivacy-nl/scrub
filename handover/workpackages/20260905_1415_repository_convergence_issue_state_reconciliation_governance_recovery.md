# Handover — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY

## Repository worked in

`solidprivacy-nl/scrub`

## Workpackage title

`SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY`

Role: `implementation_operations`  
Issue: #121  
PR: #122  
Branch: `wp/repository-convergence-issue-state-reconciliation-governance-recovery`  
Exact starting main/base: `fd69294c67a59bb150f5d4a637daad2607c14077`

## Status

**IMPLEMENTATION RECOVERY PREPARED — final exact-head full regression and fresh blind `governance_release_assurance` required before merge.**

The exact assurance candidate is the PR #122 branch head after this handover commit. Assurance must read that SHA directly from GitHub and independently verify the final full-suite evidence tied to it.

## Trigger and root cause

PR #120 was technically green but violated the mandatory release sequence. Its frozen head `1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a` merged as `fd69294c67a59bb150f5d4a637daad2607c14077` before the required fresh independent assurance verdict. Issue #74 was then closed before that verdict.

The later fresh blind `governance_release_assurance` returned formal `FAIL` because independent assurance is a pre-action ordering control. Correct merge parents, green exact-main Tests and successful HF synchronization cannot retroactively satisfy it.

## Administrative recovery already performed

Issue #74 was reopened before repository recovery implementation continued. A comment records that reopening only undoes the unauthorized reconciliation mutation; it does not alter the historical PR #73 assurance evidence or assert that #74 is substantively current work.

No other historical issue was closed or reopened by recovery. Issue #96 remains open.

## Repository recovery implemented

The recovery deliberately does **not** force-reset or pretend PR #120 never happened.

Current candidate:

- records PR #120 as `GOVERNANCE FAIL — PREMATURE MERGE; RECOVERY REQUIRED` in `CHANGELOG.md`;
- preserves accepted PR #118 / D045 validation-authority truth;
- makes `WP-CONVERGENCE-04R — Governance sequencing recovery` the sole current executable workpackage;
- blocks a new WP04 reconciliation candidate until recovery PASS + normal merge + exact-main verification;
- removes the prematurely adopted PR #120-specific claim, contract test and implementation handover from the active tree while Git history retains them;
- replaces the old executable WP04 ledger disposition with a recovery record and evidence-only future disposition finding;
- updates R11 with the release-ordering/source-of-truth risk;
- preserves R1/R2/R5/R10 criticality, mandatory human review, and the unresolved #96 deployed live-app gate;
- adds one narrow recovery contract plus a minimal regex generalization so `04R` can still satisfy the exactly-one-current-workpackage invariant.

## Files added/changed/removed relative to recovery base

Expected recovery PR scope before this handover:

```text
CHANGELOG.md
REPOSITORY_CONVERGENCE_DEBT_LEDGER.md
RISK_REGISTER.md
WORKPACKAGES.md
tests/test_repository_convergence_bootstrap_contracts.py
tests/test_repository_convergence_issue_state_reconciliation_recovery_contracts.py
workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY.md

removed from active tree:
handover/workpackages/20260905_0212_repository_convergence_issue_state_reconciliation.md
tests/test_repository_convergence_issue_state_reconciliation_contracts.py
workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION.md
```

This recovery handover is the additional final implementation artifact.

No application/runtime/UI/recognizer/profile/review/export/Scrub Key/reinsert/document-processing/Docker/dependency/workflow implementation file is intentionally changed.

## Tests

Pre-handover recovery candidate:

```text
head dd73077e1fadba4bae876335b30ac1bf99190b6b
Tests run 33965249347
job 101304111851
synthetic merge candidate 8409ba5dcec69b7b8382948e515dd39ba007d6e4
result SUCCESS — 1272 passed in 15.67s
```

This verifies the recovery/current-authority contracts before the handover. Because the claim/handover commits follow that run, a fresh complete `Tests` run on the final handover-complete head is mandatory before assurance.

## Validation status

- #74 restored open: verified in live GitHub issue state.
- PR #120 premature merge/main identity: verified as `fd69294c67a59bb150f5d4a637daad2607c14077` with parents `268d967...` and `1c5ff96...`.
- PR #120 assurance verdict: FAIL supplied by fresh independent assurance.
- D045 accepted PR #118 truth: preserved.
- #96 residual live-app gate: preserved as open/unproven in current controls.
- Product/runtime behavior: unchanged by candidate scope.
- Pre-handover full regression: green.
- Final handover-complete exact-head regression: pending immediately after this commit.
- Independent governance assurance for PR #122: pending.

## GitHub Actions status

Pre-handover full Tests is green as recorded above.

Final frozen-head Tests must be independently inspected by assurance and must be green before any merge authorization.

## Hugging Face sync status

No recovery merge has occurred. Post-merge HF sync/path-ignore behavior is therefore pending and must only be checked after an independently authorized recovery merge.

Because this is governance/docs/tests only, any HF sync would be synchronization evidence, not product-function proof.

## App verification status

**N/A for PR #122** because the recovery changes no application/runtime/UI behavior.

This does not satisfy issue #96. The consolidated deployed live-app retest after the marker/address repairs remains a separate unproven requirement.

## Remaining risks/blockers

1. Fresh independent assurance is mandatory before recovery merge; repeating PR #120 ordering would invalidate the recovery.
2. `main` remains on the prematurely merged PR #120 state until a properly assured recovery merge occurs; Git history must remain intact.
3. #119 remains open and issue reconciliation must not resume until recovery is exact-main verified.
4. #96 remains the genuine user-visible Premium/App-Shell verification gate.
5. Dormant historical patch scripts remain later RETIRE candidates.
6. Scrub Private persistence/external-egress/content-log adaptation remains Stage 2 and is not part of recovery.

## Next recommended step

1. Run full `Tests` on the handover-complete exact PR #122 head.
2. If green, freeze that exact SHA and make no further branch changes.
3. Independently reconstruct base, merge-base, exact changed-file scope, #74 live state, #96 boundary and raw Actions evidence.
4. Run a fresh blind `governance_release_assurance` for PR #122 only.
5. Only on PASS: guarded recovery merge using the exact reviewed head, then exact-main Tests and HF sync/path-ignore verification.
6. Only after recovery outcome is confirmed: create a **new** WP04 issue-reconciliation candidate from the new exact main; do not reuse PR #120 as its pre-action assurance.
