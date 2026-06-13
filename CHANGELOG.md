# Changelog — SolidPrivacy Scrub

## WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — Readiness check before replacement decision UI implementation

Status: completed readiness/specification/documentation-only; no UI or product code changed.

Files added:

- `REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS.md`
- `handover/workpackages/20260613_1240_replace_logic_ui_implementation_readiness.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS.md`

Summary:

- Reviewed `replacement_decision.py`, helper tests, UI plan, UI contract tests, serial review helper/UI, review panel view model, context-card and serial-review plans, `presidio_streamlit.py`, risk/decision docs and the status monitoring runbook.
- Concluded that the replacement-decision foundation is suitable for a small read-only/staged companion panel, but mutating replacement decision UI must not start automatically.
- Recorded that the existing review table remains the source of truth and fallback.
- Recorded that `creates_mapping`, `mapping_candidates` and `export_readiness` are advisory only and must not write Scrub Key mappings or block export.
- Recommended `WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX` before any mutating UI implementation.
- Reaffirmed that `WP_REPLACE_LOGIC_UI_IMPLEMENTATION` requires separate explicit coordinator approval.

Validation status:

- Documentation/readiness-only; no app rebuild was run.
- No shell/pytest execution was available through the ChatGPT GitHub connector in a checked-out repository.
- Product tests were not required because no product code, UI code or runtime behavior changed.

Intentionally not changed:

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `serial_review_panel_ui.py`.
- No product code changes.
- No review table behavior change.
- No replacement mutation implementation.
- No automatic replacement.
- No Scrub Key writes.
- No Scrub Key schema change.
- No export blocking.
- No export/download behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.
- No click-to-mark.
- No advanced editor.
- No full-document marking.

Next recommended step:

- `WP39D-VERIFY` if DOCX hygiene audit UI is ready for closeout/app verification.
- `WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX` if stronger replacement UI contract coverage is desired.
- `WP_REPLACE_LOGIC_UI_IMPLEMENTATION` only after separate explicit coordinator approval.

## WP39D — DOCX hygiene audit UI implementation

Status: implemented with explicit coordinator approval; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `docx_hygiene_audit_panel_ui.py`
- `tests/test_docx_hygiene_audit_ui_patch.py`
- `workpackage_claims/WP39D_docx_hygiene_audit_ui_implementation.md`
- `handover/workpackages/20260613_1405_docx_hygiene_audit_ui_implementation.md`

Files changed:

- `presidio_streamlit.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP39D_docx_hygiene_audit_ui_implementation.md`

Summary:

- Added `docx_hygiene_audit_panel_ui.py`, a small report-only Streamlit renderer for the existing `docx_hygiene_audit.py` helper.
- Integrated the panel into `presidio_streamlit.py` near the existing DOCX download button.
- The panel shows DOCX hygiene severity, finding count, affected areas, warnings and manual review guidance.
- The panel explicitly says: DOCX hygiene audit, Alleen rapportage, Geen clean-DOCX garantie, Export wordt niet geblokkeerd, Controleer metadata/opmerkingen/revisies/verborgen inhoud, and Bestaande export blijft ongewijzigd.
- Added `tests/test_docx_hygiene_audit_ui_patch.py` with static guards for UI text, helper use and non-mutating boundaries.

Validation status:

- No shell/pytest execution was available through the ChatGPT GitHub connector.
- Expected checks: `python -m py_compile presidio_streamlit.py`, `python -m py_compile docx_hygiene_audit_panel_ui.py`, `pytest tests/test_docx_hygiene_audit_ui_patch.py`, `pytest tests/test_docx_hygiene_audit.py tests/test_docx_hygiene_audit_ui_plan.py tests/test_docx_hygiene_audit_ui_patch.py`, then full `pytest`.
- This changes UI/runtime behavior, so Actions, Hugging Face sync and coordinator app verification are required before closeout.

Intentionally not changed:

- No DOCX cleaner implementation.
- No comments removal.
- No tracked changes removal.
- No metadata removal.
- No clean-DOCX claim.
- No export blocking.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.
- No startup source mutation.
- No full-document marking.
- No click-to-mark.
- No advanced editor.
- No broad UI rewrite.

Next recommended step:

- `WP39D-VERIFY — closeout/app verification for DOCX hygiene audit UI after green Actions and Hugging Face sync`.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP39C — DOCX hygiene audit UI contract tests.
- WP39B — DOCX hygiene audit UI planning.
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
