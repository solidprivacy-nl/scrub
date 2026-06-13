# Changelog — SolidPrivacy Scrub

## WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — Strengthen replacement decision UI contract tests before implementation

Status: completed tests/documentation-only; no UI or product code changed.

Files added:

- `workpackage_claims/WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX.md`
- `handover/workpackages/20260613_1255_replace_logic_ui_contract_gap_fix.md`

Files changed:

- `REPLACE_LOGIC_UI_PLAN.md`
- `tests/test_replace_logic_ui_contract.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX.md`

Summary:

- Strengthened `REPLACE_LOGIC_UI_PLAN.md` with explicit staged-vs-applied contract language.
- Locked the existing review table as source of truth and fallback.
- Added view-only session-state key boundaries for a future non-mutating companion panel.
- Recorded that `creates_mapping`, `mapping_candidates` and `export_readiness` are advisory only.
- Recorded no review table mutation, no replacement mutation, no automatic replacement, no Scrub Key writes, no export/download calls, no reinsert changes, no fuzzy matching/guessed intent, and no first mutating `all_normalized` scope without separate explicit coordinator approval.
- Strengthened `tests/test_replace_logic_ui_contract.py` from 6 to 13 contract tests.

Validation status:

- Targeted local validation in an isolated workspace passed:

```text
PYTHONPATH=. pytest tests/test_replace_logic_ui_contract.py
```

- Result: `13 passed`.
- No app rebuild was run.
- No Hugging Face app verification is required because no UI/runtime behavior changed.

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

- `WP_REPLACE_LOGIC_UI_IMPLEMENTATION` only after separate explicit coordinator approval.

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

- `WP_REPLACE_LOGIC_UI_IMPLEMENTATION` only after separate explicit coordinator approval.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP39D — DOCX hygiene audit UI implementation.
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
