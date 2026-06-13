# Handover — WP42D-ROLLBACK-CLOSEOUT Working table-first interface restored after failed static highlight preview

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP42D-ROLLBACK-CLOSEOUT — Working table-first interface restored after failed static highlight preview`

Status: completed documentation-only closeout.

## Summary

This closeout records that the Hugging Face app is back on the stable table-first Scrub interface after the failed static highlight preview / marking attempt. The old implementation route based on startup source mutation is fully rolled back and parked.

The product direction remains:

```text
Document-first review with context, better replacement decisions, later marking/editor.
```

The implementation route is now explicitly:

```text
helper/model first -> tests/contracts first -> small approved non-destructive UI panels later
```

The table-first review workflow remains the current working baseline and fallback.

## Files added

- `workpackage_claims/WP42D_ROLLBACK_CLOSEOUT.md`
- `handover/workpackages/20260613_1116_wp42d_rollback_closeout.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `FRONTEND_ARCHITECTURE_DECISION.md`
- `workpackage_claims/WP42D_ROLLBACK_CLOSEOUT.md`

## Tests/checks run

No shell or pytest execution was available through the ChatGPT GitHub connector for the checked-out repository.

Documentation/textual checks performed through GitHub connector:

- Required start files read in order: `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Required review/frontend/risk/decision files read: `DOCUMENT_CENTRIC_REVIEW_UX_SPEC.md`, `HIGHLIGHT_BASED_REVIEW_PROTOTYPE_DECISION.md`, `STREAMLIT_FEASIBILITY_BOUNDARY_REVIEW.md`, `FRONTEND_ARCHITECTURE_DECISION.md`, `RISK_REGISTER.md`, `DECISION_LOG.md`, `STATUS_MONITORING_RUNBOOK.md`.
- Recent relevant handovers reviewed where accessible: `handover/workpackages/20260613_0030_wp42d_rollback_source_cleanup_repair.md` and `handover/workpackages/20260612_2340_static_highlight_preview_cleanup_repair.md`.
- Claim check performed: `workpackage_claims/WP42D_ROLLBACK_CLOSEOUT.md` did not exist before claim; created with `GitHub.create_file`.
- Textual planning check: updated central planning so it no longer recommends verifying/restarting the old static highlight preview startup mutation route.
- Repository search checks for old visible preview wording / stale fix-verification wording returned no results through the connector search.

## Validation status

- Documentation-only package; no app rebuild run.
- No product code changed.
- No runtime/UI behavior changed.
- No dependency changed.
- The closeout relies on coordinator/user-provided evidence in the workpackage instruction that the app is working again on the stable table-first interface.
- `WORKPACKAGES.md` now lists `WP_SERIAL_REVIEW_HELPER` as the next review/frontend step, not the old static-highlight startup mutation route.

## GitHub Actions status

Unknown / not required for runtime validation in this documentation-only closeout. GitHub workflow tools returned no workflow runs for the initial claim commit at handover time. If documentation commits trigger Actions, status should be checked from GitHub UI or workflow tools after runs appear.

## Hugging Face sync status

Unknown / not required for app verification in this documentation-only closeout because no runtime/UI code changed. If documentation commits trigger sync workflows, status should be checked from GitHub UI after runs appear.

## App verification status

Not applicable for this closeout commit because no code/runtime/UI changed. The closeout records the coordinator/user-provided state that the Hugging Face app is already back on the working table-first interface.

## Remaining risks

- The table-first review interface is stable again but still has the original document-context limitations.
- Serial review queue helper/UI has not been implemented yet.
- Replacement decision helper is not wired into the UI yet.
- Advanced editor and click-to-mark remain later-stage candidates requiring separate decisions.
- Historical static-highlight planning artifacts remain useful as background, but D019 / WP42D-ROLLBACK-CLOSEOUT governs the implementation route after the failed startup-mutation attempt.

## Next recommended step

```text
WP_SERIAL_REVIEW_HELPER — pure helper/tests for serial review queue
```

Then, only after helper/tests and explicit approval:

```text
WP_SERIAL_REVIEW_UI — small non-destructive serial review panel
```
