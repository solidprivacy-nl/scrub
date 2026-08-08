# Handover — SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_ASSURANCE_CONFLICT

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: `SCRUB-WP_PREMIUM_APP_SHELL_POST_MERGE_ASSURANCE_CONFLICT — reconcile exact-head PASS/FAIL before downstream work`  
Role: `governance_release_assurance`  
Status: `POST_MERGE_ASSURANCE_CONFLICT / INDETERMINATE`  
Date/time: 2026-08-08 18:40 Europe/Amsterdam  
Reconciliation issue: #96  
Affected PR: #85  
Exact candidate head: `6ccda2ec58be387de768661c64d0a2d12b8b406e`  
Runtime merge commit: `5a68f4cc8a8b4aa5052caed8810084a659496718`

## Summary

A repeated request to execute issue #92 in the same already-exposed conversation could not satisfy issue #92's fresh-blind independence rule and was correctly recorded as `INDETERMINATE` for that repeated invocation.

During the governance-only closeout, PR #85 was concurrently merged by another action. This assurance reviewer did not execute or authorize that runtime merge.

Subsequent provenance reconstruction found two contradictory assurance decisions for the **same exact candidate head**:

- issue #93 records `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_VERIFY: PASS` for `6ccda2ec58be387de768661c64d0a2d12b8b406e`;
- issue #92 records the later `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_REVERIFY: FAIL` for that exact same head, with concrete integrated Standard↔Expert source/analysis/review-state findings and an explicit no-merge instruction.

Under `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`, contradictory assurance evidence must not be silently interpreted as PASS. Therefore the App Shell is not `OUTCOME_CONFIRMED` despite green post-merge machine evidence. Issue #96 is the controlling reconciliation gate and the Premium Input Stage remains blocked.

## Files added/changed

Added in this governance conflict closeout:

- `handover/workpackages/20260808_1840_premium_app_shell_post_merge_assurance_conflict.md`

No product/runtime/test/deployment source is changed.

Related persistent records already on `main` include:

- `handover/workpackages/20260808_1802_premium_app_shell_implementation_reverify.md` — issue #92 exact-head FAIL;
- `handover/workpackages/20260808_1829_premium_app_shell_reverify_repeat_indeterminate.md` — repeated same-session procedural INDETERMINATE;
- `handover/workpackages/20260808_1655_premium_app_shell_state_preservation_repair.md` — implementation repair handover.

No corresponding issue #93 PASS handover was found in the current `handover/workpackages/` directory or visible assurance branches during this review. Issue #93 itself remains evidence that a PASS decision was recorded; the missing persistent handover is an administrative provenance gap, not by itself a technical invalidation of that decision.

## Tests

### Runtime merge commit

GitHub Actions:

```text
merge commit: 5a68f4cc8a8b4aa5052caed8810084a659496718
Tests run: #2240 / 31267172276
job: 93127094017
checkout: exact 5a68f4cc8a8b4aa5052caed8810084a659496718
command: python -m pytest -q tests
result: 1235 passed in 14.14s
conclusion: success
```

### Governance-only repeated-invocation handover main

```text
main commit before this handover: 69d660b6ba856222c274afba2d537cbb5c1a6dcd
Tests run: #2242 / 31267228323
job: 93127235434
checkout: exact 69d660b6ba856222c274afba2d537cbb5c1a6dcd
result: 1235 passed in 10.91s
conclusion: success
```

This conflict-handover branch must receive the normal repository regression workflow before administrative merge.

## Validation status

- Candidate identity: exact runtime candidate was `6ccda2ec58be387de768661c64d0a2d12b8b406e`.
- PR #85 runtime merge: completed externally as `5a68f4cc8a8b4aa5052caed8810084a659496718`.
- Exact-main runtime Tests: **GREEN**.
- Assurance state: **CONTRADICTORY / NOT OUTCOME_CONFIRMED** because issue #93 PASS and later issue #92 FAIL address the same exact candidate.
- Earlier issue #92 concrete integrated state findings: **UNRESOLVED** until executable evidence disproves them or a repair/new candidate closes them.
- Downstream Premium Input Stage: **BLOCKED**.

## GitHub Actions status

Runtime merge exact-main Tests are green as documented above.

The later governance-only `69d660...` main also passed the full suite. No machine failure is currently known; the blocker is assurance contradiction and unresolved integrated behavior, not basic CI health.

## Hugging Face sync status

GitHub→Hugging Face synchronization for runtime merge `5a68f4cc8a8b4aa5052caed8810084a659496718` is confirmed:

```text
workflow run: 31267172284
job: 93127094283
checkout: exact 5a68f4cc8a8b4aa5052caed8810084a659496718
remote: huggingface.co/spaces/solidprivacy/scrub
push result: d54eb06..5a68f4c  HEAD -> main
conclusion: success
```

The later governance-only handover commit does not alter runtime code and correctly did not require a new HF deployment.

## App verification status

`PENDING / BLOCKED`.

The public Hugging Face Space was reachable and reported `Running`, which is only a runtime smoke signal. Live behavior of the disputed Standard Review/Download → Expert → Standard state transition has not been independently closed. The project runbook does not permit green deployment evidence to substitute for required UI verification.

Do not request coordinator acceptance of a build whose exact-head assurance remains contradictory until issue #96 resolves whether the issue #92 integrated findings are real or disproven.

## Remaining risks

1. Same exact runtime candidate has contradictory PASS/FAIL assurance records.
2. The later FAIL contains concrete integrated state-integrity findings not covered by the green source-level/pure-state suite.
3. Issue #93 PASS lacks a persistent handover in the current repository evidence found by this reviewer, reducing administrative traceability.
4. Runtime is already deployed to Hugging Face, so the conflict is post-merge rather than pre-release administrative only.
5. `WORKPACKAGES.md` contains historical/current-status text that has not yet been reconciled to this unexpected concurrent merge and conflict; issue #96 and this handover are the controlling current governance records until central status administration is safely updated.

## Next recommended step

1. Keep issue #96 open and block `SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION`.
2. Independently execute the actual integrated Standard Review/Download → Expert → Standard transition against the merged runtime/state logic, specifically source identity, deterministic generation, current-generation analysis, authoritative include/exclude/manual review rows, and export lineage.
3. If issue #92 findings reproduce, route repair to `implementation_operations`, create a new candidate identity, run full exact-head CI, and obtain fresh blind assurance before treating App Shell as closed.
4. If issue #92 findings are disproven without code changes, persist executable integrated evidence and obtain a fresh release-assurance reconciliation closeout for the already-merged state.
5. Only after assurance conflict resolution, runtime health, and required live UI verification are all closed may the App Shell become `OUTCOME_CONFIRMED` and the Premium Input Stage start.

No rollback, runtime repair, export-semantic change, privacy-control change, or downstream release authorization is performed by this assurance handover.