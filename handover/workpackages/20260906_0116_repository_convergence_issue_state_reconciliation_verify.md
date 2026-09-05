# Governance Release Assurance Handover — Repository Convergence Issue-State Reconciliation

- Repository: `solidprivacy-nl/scrub`
- Role: `governance_release_assurance`
- Workpackage: `SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION`
- Assurance dispatch: issue #126
- Candidate PR: #124
- Formal verdict: `SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_VERIFY: PASS`

## Exact reviewed identity

- Frozen candidate head: `ce021443303cfa11de12f3273f872b2d027da5db`
- Reviewed base: `14baceb97b274de6ef35c42ce48441c4e74c5f08`
- Merge-base: `14baceb97b274de6ef35c42ce48441c4e74c5f08`
- Pre-merge main: `14baceb97b274de6ef35c42ce48441c4e74c5f08`
- Geometry: `ahead_by=19`, `behind_by=0`

Exact persistent changed-file set:

1. `CHANGELOG.md`
2. `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`
3. `RISK_REGISTER.md`
4. `WORKPACKAGES.md`
5. `handover/workpackages/20260905_1525_repository_convergence_issue_state_reconciliation.md`
6. `tests/test_repository_convergence_issue_state_reconciliation_contracts.py`
7. `tests/test_repository_convergence_issue_state_reconciliation_recovery_contracts.py`
8. `workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION.md`
9. `workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY.md`

No product/runtime/UI/recognizer/profile/review/export/Scrub Key/reinsert/dependency/workflow implementation file changed.

## Blind-first boundary

The initial correctness reconstruction was completed before opening any file under `handover/workpackages/` or `workpackage_claims/`. Generic PR metadata unexpectedly exposed the PR body during identity verification; that narrative was immediately treated as contaminated metadata and excluded from the initial verdict evidence.

The formal PASS was recorded before the denied implementation administration was read. Those files were subsequently inspected only for disclosure/administrative completeness and introduced no blocker. Their pre-final CI wording was consistent with the intentional workflow: the handover was the final candidate mutation and final exact-head CI was recorded externally afterward.

## Reconstructed governance provenance

### Premature PR #120 sequence

PR #120 was independently reconstructed as the governance-invalid first WP04 attempt:

- reviewed candidate lineage ultimately merged as `fd69294c67a59bb150f5d4a637daad2607c14077`;
- merge parents were exact pre-merge main `268d967db95d923a73a3979ffce2d0cab586e499` and candidate `1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a`;
- issue #74 was closed one second after that merge and before the required fresh independent assurance verdict;
- later fresh assurance therefore correctly returned FAIL for release-ordering bypass;
- that FAIL remains historical truth and was not retroactively converted into PASS.

### Governed recovery PR #122

Recovery PR #122 was independently reconstructed as correctly sequenced:

- exact recovery head `8565af4e9f579b3a975c6122668f6511a9df627a`;
- base `fd69294c67a59bb150f5d4a637daad2607c14077`;
- fresh exact-SHA PASS preceded merge;
- recovery merged as `14baceb97b274de6ef35c42ce48441c4e74c5f08` with exact parents `fd69294c67a59bb150f5d4a637daad2607c14077` and `8565af4e9f579b3a975c6122668f6511a9df627a`;
- exact-main Tests and GitHub→Hugging Face sync were confirmed;
- #74 was restored OPEN, #96 and #119 remained OPEN, and no WP04 issue reconciliation occurred.

Issue #123 remained open after recovery because its own PASS procedure explicitly required closing #121 and then stopping. It was therefore correctly classified by WP04 as completed historical recovery-assurance administration, not residual current work and not reusable WP04 release authority.

Superseded assurance dispatch #125 was independently confirmed `closed/not_planned`, with zero verdict authority.

## Pre-action issue inventory and disposition reconstruction

Before the initial verdict and before any corrected-retry mutation, all 18 reviewed closure targets were OPEN:

`#74 #75 #76 #77 #79 #81 #84 #86 #88 #89 #98 #100 #105 #106 #107 #109 #112 #123`

Also OPEN: `#96`, `#119`, `#126`.

The historical implementation/repair/assurance clusters were reconstructed from GitHub rather than age or candidate narrative. The evidence supported administrative closure of those 18 historical/completed/superseded tickets while preserving one residual live product gate:

- PR #104 V2 technical state repair independently PASSed, merged, and exact-main/sync evidence completed;
- PR #108 marker/compact-placeholder repair independently PASSed, merged, and synchronized;
- PR #111 Dutch-address span-precision repair independently PASSed, merged, and synchronized;
- the consolidated deployed live-app retest after both PR #108 and PR #111 remained unproven.

Therefore #96 had to remain OPEN. Closing #105 was not interpreted as proof that its historical live gate passed; residual live authority was explicitly consolidated into #96.

## Candidate contract review

The candidate materially froze:

- exactly one current executable Repository Convergence package: WP-CONVERGENCE-04;
- WP-CONVERGENCE-04R as completed recovery provenance;
- exact close set of 18 and keep-open set `{96}`;
- explicit wording that the consolidated deployed live-app retest `remains unproven`;
- required causal action order: exact candidate → full exact-head Tests → fresh blind PASS → guarded merge → exact-main Tests + GitHub→HF verification → only then issue mutation → issue-state readback → #119 closeout → assurance-dispatch closeout;
- Stage 2 blocked;
- D045 accepted;
- R1 false negatives, R2 Scrub Key and R10 Zorg remain critical;
- mandatory human review remains binding;
- no force-reset/history-rewrite mechanism.

The generalized current-workpackage regex `\d+[A-Z]?` did not weaken the exactly-one invariant because the hard `len(current_wp_headings) == 1` assertion remained present.

## Exact-head machine evidence

Final PR exact-head run:

- Tests run: `33996982852`
- Job: `101389126133`
- Frozen head: `ce021443303cfa11de12f3273f872b2d027da5db`
- Base: `14baceb97b274de6ef35c42ce48441c4e74c5f08`
- Synthetic merge: `8a8ebd9b917afb09f3270e6c3351767720986878`
- Synthetic merge parents: exact base + frozen candidate
- Command: `python -m pytest -q tests`
- Result: `1279 passed in 13.91s`
- Conclusion: SUCCESS

## Formal verdict and guarded merge

Formal exact-SHA PASS was registered on PR #124 before merge as review ID `5123337398`, bound to the exact frozen head and base.

PR #124 was marked ready without head movement and merged only with hard `expected_head_sha=ce021443303cfa11de12f3273f872b2d027da5db`.

Actual merge/main SHA:

`2d4ab0446c20f08ad07576af326ab4b0df0a2af7`

Exact parents:

1. `14baceb97b274de6ef35c42ce48441c4e74c5f08`
2. `ce021443303cfa11de12f3273f872b2d027da5db`

## Post-merge exact-main verification

### Tests

- Run: `33997889522`
- Job: `101391497463`
- Head/main: `2d4ab0446c20f08ad07576af326ab4b0df0a2af7`
- Event: push
- Command: `python -m pytest -q tests`
- Result: `1279 passed in 14.51s`
- Conclusion: SUCCESS

### GitHub → Hugging Face

- Run: `33997889554`
- Job: `101391497663`
- Exact checkout: `2d4ab0446c20f08ad07576af326ab4b0df0a2af7`
- Target: `huggingface.co/spaces/solidprivacy/scrub`
- Push: `git push --force huggingface HEAD:main`
- Remote acknowledgement: `14baceb..2d4ab04  HEAD -> main`
- Conclusion: SUCCESS

This is exact deployment-sync evidence, not live-app behavioral proof.

## App verification status

For PR #124 itself: `N/A` because the PR changed only governance/docs/tests/administration and no product/runtime source.

For the residual Premium/App-Shell product outcome: NOT complete. Issue #96 remains OPEN because the consolidated deployed live-app retest after PR #108 and PR #111 remains unproven.

## Final administrative reconciliation

Only after both post-merge gates were green, the following 18 issues were closed as `completed`, each with evidence-aware provenance that preserves earlier FAIL/PASS/superseded history:

`#74 #75 #76 #77 #79 #81 #84 #86 #88 #89 #98 #100 #105 #106 #107 #109 #112 #123`

Issue #96 body was updated to current truth and left OPEN. It now explicitly states that PR #104/#108/#111 repair chains are complete but the consolidated deployed live-app retest remains unproven.

A fresh open-issue readback after reconciliation contained only `#96`, `#119`, and `#126`; therefore none of the 18 reviewed closure targets remained open.

Issue #119 was then closed `completed` only after that readback confirmed the WP04 administrative outcome.

## Remaining risks / boundaries

1. #96 remains the sole current Premium/App-Shell live verification gate. CI and HF synchronization do not substitute for that live test.
2. Private Stage-2 persistence/egress work remains blocked/deferred; WP04 did not alter that boundary.
3. Historical failed/superseded assurance cycles remain intentionally visible in Git/issues; administrative closure must not be read as retroactive validation of rejected heads.
4. This assurance performed no next implementation workpackage.

## Next recommended step

After closing assurance dispatch #126, return execution authority to the normal implementation/coordinator lane. Do not start a new implementation package from the assurance role. The only remaining product-facing gate identified by this reconciliation is the explicit live-app verification recorded in OPEN issue #96.
