# Changelog — SolidPrivacy Scrub

## WP39B — DOCX hygiene audit UI planning

Status: completed planning/documentation-only.

Files added:

- `DOCX_HYGIENE_AUDIT_UI_PLAN.md`
- `workpackage_claims/WP39B_docx_hygiene_audit_ui_planning.md`
- `handover/workpackages/20260613_1330_docx_hygiene_audit_ui_planning.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP39B_docx_hygiene_audit_ui_planning.md`

Summary:

- Planned a small future UI surface for the existing report-only DOCX hygiene audit helper.
- The plan uses `docx_hygiene_audit.py` and `render_docx_hygiene_audit_markdown(...)` as the future helper surface.
- The plan defines placement near DOCX upload/export and restored DOCX reinsert/download controls.
- The plan defines severity behavior for low, medium and high findings.
- The plan preserves the WP39 policy that current DOCX output must not be called clean DOCX.
- The plan recommends `WP39C — DOCX hygiene audit UI contract tests` before implementation.

Validation status:

- Planning/documentation-only; no app rebuild was run.
- No shell/pytest execution was available through the ChatGPT GitHub connector.
- Existing WP37/WP38/WP39 documents and helper/test files were read and used as source material.

Intentionally not changed:

- No product code changes.
- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `fix_streamlit_nested_expanders.py`.
- No changes to `docx_hygiene_audit.py`.
- No tests changed.
- No export/download behavior change.
- No export blocking.
- No DOCX cleaning/removal.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

Next recommended step:

- `WP39C — DOCX hygiene audit UI contract tests`.
- `WP39D — DOCX hygiene audit UI implementation` only after contract tests and explicit coordinator approval.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP28C-CLOSEOUT — Scrub Key warning/reinsert evidence closeout.
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
