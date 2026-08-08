# Handover — SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE

Repository: `solidprivacy-nl/scrub`  
Workpackage title: `SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE — bind single-page three-stage workspace`  
Role: `implementation_operations`  
Status: `RELEASE_CANDIDATE_READY — independent governance_release_assurance required before merge`

## Summary

The coordinator-approved Premium Standard interaction decision has been translated into a binding architecture specification, roadmap realignment, authoritative execution queue, decision-log record and regression contract.

The governing principle is:

```text
One document. One workspace. Three stages. One active task.

Toevoegen → Controleren → Downloaden
```

For Standard anonymization, the three stages remain represented in one persistent page/workspace. Exactly one stage is expanded/dominant at a time. Completed stages collapse to compact summaries, future stages remain visible but passive, successful completion auto-advances, explicit return to an earlier stage is allowed, and processing-affecting earlier changes invalidate downstream state fail-closed.

Three separate routed core-flow pages and a generic nested-expander form hierarchy are explicitly rejected for Standard.

This package deliberately intervenes before active PR #85 enters production `presidio_streamlit.py` integration. PR #85 is amended, not discarded: its existing pure `premium_app_shell.py` and test work remains reusable, but the production shell must first incorporate this staged-workspace contract.

## Files added

- `PREMIUM_STAGED_WORKSPACE_DECISION.md`
- `tests/test_premium_staged_workspace_decision.py`
- `workpackage_claims/scrub_wp_premium_staged_workspace_decision_freeze.md`
- `handover/workpackages/20260808_1255_premium_staged_workspace_decision_freeze.md`

## Files changed

- `ROADMAP.md`
  - Premium staged workspace made the explicit strategic UI direction;
  - Premium UI made the dominant execution line;
  - new urgent architecture gate inserted before production PR #85 integration;
  - current governance/contract/state-model status aligned with merged PRs #73, #80 and #82.
- `WORKPACKAGES.md`
  - authoritative current Premium execution queue prepended without deleting historical workpackage records;
  - detailed sequential packages and acceptance criteria frozen.
- `CHANGELOG.md`
  - architecture-candidate entry added.
- `DECISION_LOG.md`
  - D043 records the single-page staged workspace decision and rejected alternatives.

Issue #84 and PR #85 also contain binding comments pointing to issue #86 / PR #87.

## Tests added / updated

Added `tests/test_premium_staged_workspace_decision.py` covering:

- one persistent document workspace;
- `Toevoegen | Controleren | Downloaden` stage contract;
- exactly one expanded/dominant stage;
- compact completed-stage summaries;
- passive future-stage visibility;
- automatic progression;
- rejection of three routed core-flow pages;
- rejection of nested core-flow accordion hierarchy;
- preservation of review/export/Scrub Key/reinsert/human-review safety boundaries;
- roadmap urgency and exact workpackage execution order;
- D043 decision-log binding.

One initial new-test assertion was overly literal about Markdown emphasis (`not a three-page wizard` versus `**not** a three-page wizard`). Raw run #2143 therefore produced `1 failed, 1189 passed`. The assertion was narrowed to the durable semantic contract without weakening the routed-page/nested-expander prohibitions.

Pre-final administrative candidate validation:

```text
GitHub Actions Tests run #2145 / ID 31253772414
python -m pytest -q tests
1190 passed in 12.23s
conclusion: success
```

After that green run, a scope-cleanup commit only restored unrelated historical ROADMAP status wording and removed its temporary self-cleaning workflow. No product/runtime code changed.

The final handover/claim commits intentionally move the PR head once more. A fresh full `Tests` run on that final exact head is required before the candidate is handed to assurance. No further candidate edits are permitted after that exact-head run unless the candidate returns to implementation for repair.

## Validation status

- GitHub Actions: `GREEN` on pre-final administrative candidate (`1190 passed in 12.23s`); fresh exact-final-head run required after this handover/claim commit.
- Hugging Face sync: `NOT APPLICABLE` — no runtime/deployment/Hugging Face product files are changed.
- App verification: `NOT APPLICABLE` — this package changes architecture/roadmap/contracts only; it does not change the live UI.
- Production Streamlit integration: deliberately not included.

## GitHub Actions status

Pre-final green evidence:

- workflow: `Tests`
- run: #2145 / `31253772414`
- tested branch head: `6c72d87700683215bacf7115c82f72418d6da38e`
- tested PR merge candidate: `d72686b585a137adb9000c4457b262eecb0679e6`
- command: `python -m pytest -q tests`
- raw result: `1190 passed in 12.23s`
- conclusion: `success`

The exact final PR head and its fresh run must be recorded in PR #87 / issue #86 after this file and the final claim are committed.

## Hugging Face sync status

`NOT APPLICABLE`.

This workpackage contains no production/runtime file intended for Hugging Face synchronization.

## App verification status

`NOT APPLICABLE` for this package.

Actual staged-workspace behavior must be verified later in `SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT` after the App Shell, Input, Review and Export implementation packages have been independently assured, merged and synchronized.

## Remaining risks

1. **Independent assurance not yet completed.** Implementation may not certify or merge its own PR #87.
2. **PR #85 must remain aligned.** Its current helpers are reusable, but production integration must not proceed using three routed pages or a generic nested-expander hierarchy.
3. **Streamlit implementation risk remains future work.** The staged workspace must feel like application panels, not cosmetically renamed `st.expander` form sections.
4. **Standard must not become less safe.** Review-table/include authority, direct masking, Scrub Key, export, reinsert, audit and mandatory human review remain binding.
5. **Final exact-head evidence is still required after this administrative closeout commit.** A failure returns to implementation; no inference of PASS is allowed.

## Next recommended step

1. Commit the final claim with `RELEASE_CANDIDATE_READY` status.
2. Run/observe the normal full GitHub Actions `Tests` workflow on the exact final PR #87 head.
3. If and only if that exact-head run is green, freeze the candidate and route PR #87 to a fresh independent `governance_release_assurance` reviewer for `PASS | FAIL | INDETERMINATE`.
4. On independent PASS, merge PR #87 unchanged.
5. Only then resume `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION` in PR #85 under the new staged-workspace contract.
6. Continue sequentially: App Shell → Input → Review → Export → Expert parity → live app verification.

Implementation must not self-merge PR #87 and must not claim live Premium UI completion from this architecture package.