# Assurance handover — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY_VERIFY

Date/time: 2026-09-05 14:36 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Role: `governance_release_assurance`  
Assurance issue: #123  
Recovery implementation issue: #121  
PR: #122

## Formal verdict

`SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY_VERIFY: PASS`

The initial verdict was recorded before opening any candidate `handover/workpackages/` or `workpackage_claims/` file. PR #122 body narrative exposed by the metadata endpoint during identity inspection was treated as contaminated narrative and excluded from correctness evidence.

## Exact reviewed identity

- Frozen candidate: `8565af4e9f579b3a975c6122668f6511a9df627a`
- Expected base / merge-base / pre-recovery main: `fd69294c67a59bb150f5d4a637daad2607c14077`
- Fresh compare: `ahead_by=12`, `behind_by=0`, merge-base exact expected base.
- Candidate changed paths: exactly 11, all governance/docs/tests/claim-handover recovery scope; no product/runtime/UI/recognizer/review/export/Scrub Key/reinsert/dependency/workflow implementation change.
- Final pre-merge synthetic merge candidate: `588ec49394a7ef8a8e06f220b9d59ede0ce00b45`, with parents exact base then exact frozen candidate.

## Blind-first independent findings

### PR #120 sequencing defect was real

Before reviewing implementation administration, GitHub current/history evidence independently established:

- last governance-valid pre-WP04 main: `268d967db95d923a73a3979ffce2d0cab586e499`;
- PR #120 candidate: `1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a`;
- premature PR #120 merge/current recovery base: `fd69294c67a59bb150f5d4a637daad2607c14077`;
- merge parents are exactly `268d967...` and `1c5ff96...`;
- PR #120 merged at 2026-09-05T09:15:25Z;
- issue #74 was closed at 2026-09-05T09:15:26Z, before the later independent assurance verdict;
- issue #74 was subsequently reopened with explicit recovery provenance, without rewriting historical PR #73 assurance semantics.

This is a release-ordering defect, not a product-code defect.

### Recovery current authority is correctly bounded

The candidate establishes `WP-CONVERGENCE-04R — Governance sequencing recovery` as the sole current executable Repository Convergence package and keeps WP04 / issue #119 blocked until recovery PASS, normal merge and exact-main confirmation.

It preserves independently accepted PR #118 / D045 validation authority and does not force-reset or rewrite Git history. The prematurely adopted PR #120-specific claim/test/handover are removed from active current authority while retained in Git history.

The former 17-close / 1-keep issue-disposition is evidence for a future retry only and is not current mutation authority.

### #96 safety boundary remains intact

Issue #96 remains OPEN. Independent evidence confirms PR #104 V2, PR #108 and PR #111 technical repair chains were assured/merged, but no evidence proves the required consolidated deployed live-app retest after the PR #108 + PR #111 repaired state. That live gate therefore remains explicitly unproven. CI and Hugging Face synchronization do not satisfy it.

### Contract-test review

`tests/test_repository_convergence_issue_state_reconciliation_recovery_contracts.py` materially protects:

- 04R as current authority;
- WP04/#119 blocked state;
- exact PR #120 recovery identities and governance-failure language;
- #74 reopening / no force reset;
- old PR #120 candidate-specific active artifacts removed;
- old issue disposition not current action authority;
- D045 / PR #118 accepted truth;
- #96 live-app retest still unproven;
- Stage 2 blocked;
- mandatory human review retained.

The only bootstrap-contract generalization changes the workpackage heading matcher from `\d+` to `\d+[A-Z]?` so an explicit recovery suffix such as `04R` can be represented. The existing `assert len(current_wp_headings) == 1` remains unchanged, so exactly-one-current-workpackage semantics are not weakened.

## Pre-merge machine evidence

Pre-handover recovery run:

```text
head dd73077e1fadba4bae876335b30ac1bf99190b6b
Tests run 33965249347
job 101304111851
synthetic merge 8409ba5dcec69b7b8382948e515dd39ba007d6e4
1272 passed in 15.67s
SUCCESS
```

Final exact frozen head:

```text
head 8565af4e9f579b3a975c6122668f6511a9df627a
base fd69294c67a59bb150f5d4a637daad2607c14077
Tests run 33965354552
job 101304393076
synthetic merge 588ec49394a7ef8a8e06f220b9d59ede0ce00b45
1272 passed in 14.19s
SUCCESS
```

## Post-verdict administration check

After the initial PASS only, the recovery implementation claim and recovery handover were inspected. They were administratively complete and consistent with the independently reconstructed scope, safety boundaries and sequencing. The prior PR #120 FAIL assurance handover was also read only after the initial verdict; it records the same HIGH ordering defect independently reconstructed during this review.

## Authorized PASS actions executed

1. Exact-SHA PASS comment registered on PR #122 (comment id `5551841623`).
2. Draft PR #122 marked ready without head movement; head remained `8565af4e9f579b3a975c6122668f6511a9df627a`.
3. Guarded merge executed with `expected_head_sha=8565af4e9f579b3a975c6122668f6511a9df627a`.
4. Actual merge/main SHA: `14baceb97b274de6ef35c42ce48441c4e74c5f08`.
5. Actual merge parents verified exactly:
   - `fd69294c67a59bb150f5d4a637daad2607c14077`
   - `8565af4e9f579b3a975c6122668f6511a9df627a`
6. Exact-main post-merge Tests and Hugging Face sync independently verified.
7. State fence re-read before recovery closeout: #74 OPEN/reopened, #96 OPEN, #119 OPEN.
8. Recovery issue #121 received evidence-aware closeout comment id `5551859115` and was then closed as `completed`.

No WP04 historical issue reconciliation was performed. #74, #96 and #119 were not closed or edited by this assurance closeout.

## Exact-main post-merge evidence

### Tests

```text
main 14baceb97b274de6ef35c42ce48441c4e74c5f08
Tests run 33966351441
job 101307057966
conclusion SUCCESS
checkout exact 14baceb97b274de6ef35c42ce48441c4e74c5f08
python -m pytest -q tests
1272 passed in 14.44s
```

### GitHub → Hugging Face sync

```text
main 14baceb97b274de6ef35c42ce48441c4e74c5f08
sync run 33966351286
job 101307057815
conclusion SUCCESS
checkout exact 14baceb97b274de6ef35c42ce48441c4e74c5f08
push: fd69294..14baceb HEAD -> main
```

The sync workflow did run for this governance/docs/tests recovery; current path-ignore behavior did not suppress it. That successful sync is operational synchronization evidence only, not product/runtime or live-app verification.

## Final issue state

At assurance closeout:

- #74: OPEN / reopened;
- #96: OPEN; consolidated deployed live-app retest remains unproven;
- #119: OPEN; future WP04 reconciliation remains separate work;
- #121: CLOSED / completed after successful recovery merge and exact-main verification.

## App verification

`N/A` for PR #122 itself: this recovery changes no application/runtime/UI behavior.

This does not satisfy or narrow issue #96. The separate consolidated deployed live-app retest remains required.

## Residual boundaries / next step

The governance sequencing recovery is outcome-confirmed. This assurance role stops here.

A separate `implementation_operations` worker may now create a **new** WP04 issue-reconciliation candidate from exact current main `14baceb97b274de6ef35c42ce48441c4e74c5f08`. PR #120 must not be reused as pre-action assurance evidence, and no historical issue closure may occur until that new candidate completes its own fresh exact-head assurance lifecycle.

Do not start Stage 2. Do not close #96 without real consolidated live-app evidence.
