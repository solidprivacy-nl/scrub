# Changelog — SolidPrivacy Scrub

## WP50 — Pilot design Legal vs Zorg

Status: completed planning-only with artifact limitation.

Files added:

- `workpackage_claims/WP50_pilot_design_legal_vs_zorg.md`
- `handover/workpackages/20260612_1715_pilot_design_legal_vs_zorg.md`

Files changed:

- `workpackage_claims/WP50_pilot_design_legal_vs_zorg.md`
- `CHANGELOG.md`

Main changes:

- Created and completed the WP50 claim.
- Recorded the WP50 design summary in the claim file because repeated attempts to create the intended standalone design file were blocked by platform safety checks.
- Covered Legal vs Zorg validation direction, target groups, selection criteria, measurement themes, stop criteria, agreement boundaries, residual-risk reporting role and demo/pilot/production distinction at summary level.

Validation status:

- Documentation-only.
- No tests were run.
- App verification: not applicable.

Intentionally not changed:

- No pilot started.
- No code changed.
- No UI changed.
- No runtime behavior changed.

Next recommended step:

- `WP51 — ICP and pricing hypothesis`.

## WP49 — Desktop packaging decision

Status: completed decision/documentation-only.

Purpose:

- Decide the future local desktop packaging direction after WP45-WP48.
- Compare portable Python folder, PyInstaller, Tauri, Electron and MSI as a later future option.
- Preserve the local-first privacy boundary without implementing packaging.

Files added:

- `DESKTOP_PACKAGING_DECISION.md`
- `workpackage_claims/WP49_desktop_packaging_decision.md`
- `handover/workpackages/20260612_1700_desktop_packaging_decision.md`

Files changed:

- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main changes:

- Decided that the first local MVP distribution form should remain a portable Python folder with the existing local Streamlit launcher.
- Decided that PyInstaller one-folder may be the next concrete packaging proof only if explicitly approved.
- Kept Tauri as the preferred later professional desktop-shell candidate if Scrub moves toward a document-centric frontend.
- Kept Electron as a later alternative if frontend requirements or team capability favor it.
- Kept MSI as a future managed-deployment option only after packaging, signing, update, rollback, offline, network, temp-file and support boundaries are validated.
- Added D014 to `DECISION_LOG.md`.
- Updated R5 in `RISK_REGISTER.md` so the desktop-packaging decision is no longer a gap, while production packaging remains gated.

Validation status:

- Documentation/decision-only.
- No tests run because no code, tests, UI, runtime behavior, dependency or packaging implementation changed.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

- No installer built.
- No MSI built.
- No PyInstaller package built.
- No Tauri or Electron implementation.
- No Docker/Hugging Face startup change.
- No Streamlit UI change.
- No runtime behavior change.
- No telemetry added.
- No cloud document processing added.
- No real data added.
- No roadmap change because the strategy did not change.

Next recommended step:

- `WP48B — Portable Python folder hardening proof` or `WP49B — PyInstaller one-folder packaging proof`, only if the coordinator approves a concrete packaging proof.

## WP36A — DOCX residual placeholder and comments risk triage

Status: completed triage/test/documentation-only.

Purpose:

- Record the app-verification finding that DOCX restored output can still contain residual placeholders such as `[PERSOON_01]`.
- Record that Word comments/kantlijncommentaren are outside the current DOCX scrub/reinsert flow.
- Treat this as a high-risk document hygiene issue, not as a cosmetic bug.

Files added:

- `DOCX_RESIDUAL_PLACEHOLDER_COMMENTS_TRIAGE.md`
- `tests/test_docx_residual_placeholder_comments_risk.py`
- `workpackage_claims/WP36A_docx_residual_placeholder_comments_risk_triage.md`
- `handover/workpackages/20260612_1625_docx_residual_placeholder_comments_risk_triage.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Added a triage document explaining residual DOCX placeholders, numbering mismatches, split-run placeholders and comments/kantlijncommentaren risk.
- Added synthetic tests showing that `[PERSOON_01]` remains visible when the Scrub Key contains `[PERSOON_1]` and that `word/comments.xml` is copied through unchanged by the current DOCX reinsert helper.
- Updated `RISK_REGISTER.md` to reflect the app-verification finding under R4 hidden document content and metadata leakage.
- Updated `WORKPACKAGES.md` so the DOCX hygiene line records WP36A and points to WP37 as the next extraction/audit-oriented step.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Added tests should be validated by GitHub Actions.
- App verification finding was supplied by the coordinator/user and recorded in triage.

Intentionally not changed:

- No DOCX cleaner implemented.
- No comments/tracked-changes removal implemented.
- No export blocking.
- No export semantics changed.
- No Streamlit UI changed.
- No helper behavior changed.
- No Scrub Key schema changed.
- No real data added.
- No cloud processing added.
- No roadmap change because strategy and phase order did not change.

Next recommended step:

- `WP37 — Headers/footers/comments/tracked-changes extraction helper`.

## WP28C-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout

Status: verification attempted; blocked awaiting coordinator/user evidence.

Purpose:

- Check WP28C implementation status through connector-supported GitHub status tools.
- Record whether GitHub Actions and Hugging Face sync can be verified before app verification.
- Avoid starting further Scrub Key UI work until WP28C verification status is known.

Files added:

- `workpackage_claims/WP28C_VERIFY_warning_acknowledgement_ui_closeout.md`
- `handover/workpackages/20260612_1605_wp28c_warning_acknowledgement_ui_verify.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP28C_VERIFY_warning_acknowledgement_ui_closeout.md`

Main findings:

- `get_commit_combined_status` returned no statuses for `7be73b8aabb8b3677995e153f64148eaf42648e7`.
- `fetch_commit_workflow_runs` returned no workflow runs for `7be73b8aabb8b3677995e153f64148eaf42648e7`.
- `get_commit_combined_status` returned no statuses for `ec52353d3425d409ce46990c1d3a97d71a4b4941`.
- `fetch_commit_workflow_runs` returned no workflow runs for `ec52353d3425d409ce46990c1d3a97d71a4b4941`.
- Actions/Hugging Face sync cannot be verified by this worker from connector data.
- App verification cannot be requested yet under `STATUS_MONITORING_RUNBOOK.md` because Actions/sync are not confirmed green.

Validation status:

- Verification/closeout-only.
- No tests run.
- No code, tests, UI, helper logic, schema, export, reinsert, dependency, real-data or cloud-processing files changed.

Next recommended step:

- Coordinator/user should provide GitHub Actions and Hugging Face sync evidence for WP28C. If green, perform WP28C app verification.

## Earlier entries

Previous changelog detail remains available in Git history. This WP50 entry records the latest pilot design status while preserving recent WP49, WP36A and WP28C verification entries below.
