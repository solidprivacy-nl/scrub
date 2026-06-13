# Changelog — SolidPrivacy Scrub

## WP28C-CLOSEOUT — Scrub Key warning/reinsert evidence closeout

Status: completed verification/documentation-only closeout.

Files added:

- `workpackage_claims/WP28C_CLOSEOUT.md`
- `handover/workpackages/20260613_1305_wp28c_closeout.md`
- `handover/workpackages/20260613_1315_wp28c_closeout.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP28C_CLOSEOUT.md`

Summary:

- Closed out WP28C after coordinator screenshots showed green Tests, green Hugging Face sync and the running app in `Originele waarden terugzetten` mode.
- The app evidence shows Scrub Key loading, warning text, acknowledgement checkbox and original-values reinsert sections.
- Pasted-text, TXT, DOCX and PDF-to-TXT reinsert warning/acknowledgement surfaces are visible.
- DOCX restored-output success/download evidence and reinsert statistics/audit output are visible.
- UI acknowledgements remain safety prompts only; no encryption, protected storage, automatic deletion, expiry enforcement, key recovery or managed vault was added.

Validation status:

- Verification/documentation-only; no product code changed.
- No tests changed.
- Coordinator screenshots are recorded as the verification source for Actions, Hugging Face sync and app behavior.

Intentionally not changed:

- No UI changes in this closeout.
- No export/download behavior change.
- No Scrub Key schema or behavior change.
- No reinsert semantic change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

Next recommended step:

- `WP39B — DOCX hygiene audit UI planning`, if coordinator wants to continue DOCX hygiene.
- `WP_REPLACE_LOGIC_UI_IMPLEMENTATION` only after separate explicit coordinator approval.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_SERIAL_REVIEW_UI_VERIFY — closeout/app verification for non-destructive serial review panel.
- WP_SERIAL_REVIEW_UI — small non-destructive serial review panel in Streamlit.
- WP_SERIAL_REVIEW_UI_CONTRACT_STATUS_RECONCILE — central status reconciliation for serial review UI contract tests.
- WP_CONTEXT_CARD_STATUS_RECONCILE — central status reconciliation for the context-card helper.
- WP_ACTIONS_FIX_FRONTEND_DECISION_CONTRACT — restored WP43/WP42D contract phrase.
- WP_SERIAL_REVIEW_HELPER — serial review queue helper and tests.
- WP42D-ROLLBACK-CLOSEOUT — working table-first interface restored after failed static highlight preview.
- WP42D-ROLLBACK-REPAIR — static preview source cleanup / HF startup repair.
- WP_ACTIONS_FIX_REPLACE_LOGIC_TESTS — repair failing replacement logic and DOCX triage tests.
- WP42D-FIX4 — static highlight preview stale-block cleanup repair.
