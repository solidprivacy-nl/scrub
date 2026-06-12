# Handover — WP28C-VERIFY warning acknowledgement UI closeout

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP28C-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout`

Status: verification attempted; blocked awaiting coordinator/user evidence.

## Summary

Performed the WP28C verification closeout attempt using the GitHub connector status tools available in this ChatGPT webinterface session.

The connector returned no commit statuses and no workflow runs for the relevant WP28C commits, so GitHub Actions and Hugging Face sync cannot be confirmed by this worker.

Because WP28C changed UI behavior, app verification is required, but under `STATUS_MONITORING_RUNBOOK.md` it should only be requested after Actions and Hugging Face sync are confirmed green.

## Files added

- `workpackage_claims/WP28C_VERIFY_warning_acknowledgement_ui_closeout.md`
- `handover/workpackages/20260612_1605_wp28c_warning_acknowledgement_ui_verify.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP28C_VERIFY_warning_acknowledgement_ui_closeout.md`

## Tests/checks run

No tests were run.

Connector checks performed:

```text
get_commit_combined_status(7be73b8aabb8b3677995e153f64148eaf42648e7)
fetch_commit_workflow_runs(7be73b8aabb8b3677995e153f64148eaf42648e7)
get_commit_combined_status(ec52353d3425d409ce46990c1d3a97d71a4b4941)
fetch_commit_workflow_runs(ec52353d3425d409ce46990c1d3a97d71a4b4941)
```

Results:

```text
combined statuses: []
workflow_runs: []
```

## Validation status

- Required start files read: `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- `STATUS_MONITORING_RUNBOOK.md` read.
- WP28C-VERIFY claim created before closeout edits.
- No code changed.
- No tests changed.
- No Streamlit UI changed.
- No helper logic changed.
- No Scrub Key schema changed.
- No import/export behavior changed.
- No reinsert behavior changed.
- No dependency changed.
- No real data added.
- No cloud processing added.

## GitHub Actions status

Unknown.

The connector returned no statuses or workflow runs for the checked commits.

## Hugging Face sync status

Unknown.

The connector returned no workflow/check evidence for `Sync to Hugging Face Space`.

## App verification status

Required but pending.

Not requested as confirmed because Actions/sync are not known green from connector evidence.

## Remaining risks

- WP28C UI behavior is implemented but not verified in the deployed app.
- GitHub Actions and Hugging Face sync status require coordinator/user evidence or another status source.
- If Actions are red, a narrow WP28C-FIX package may be needed.
- If Actions and sync are green, coordinator/user should perform app verification.

## Next recommended step

Coordinator/user should provide GitHub Actions and Hugging Face sync evidence for WP28C. If green, verify the app behavior:

- Scrub Key JSON download disabled until export acknowledgement is checked.
- Scrub Key import/load disabled until import acknowledgement is checked.
- Pasted-text/TXT/DOCX/PDF-to-TXT reinsert buttons disabled until acknowledgement is checked.
- Restored output downloads disabled until download acknowledgement is checked.
- After acknowledgement, JSON/restored content, filenames and MIME types remain unchanged.
- Existing anonymization/export flow still works.
