# Changelog — SolidPrivacy Scrub

This changelog records meaningful product, architecture, workflow and recognizer changes for the Scrub legal document scrubber.

Conventions:

- Keep this file explicit and human-readable.
- Group changes by project phase / version.
- Record what changed, why it changed, and what is intentionally not changed.
- Do not use this as a substitute for tests; every recognizer hardening step should also add or update regression tests.

---

## Current development rule

From v10 onward, recognizer work follows this order:

1. Add or update synthetic regression cases.
2. Add or update tests.
3. Change recognizer / scanner logic.
4. Verify GitHub Actions tests are green.
5. Let GitHub sync to Hugging Face automatically.
6. Test the app in Hugging Face.

For UI/UX-only work, prefer pure helper modules and tests before touching Streamlit UI flow.

---

## v13.2 — Scrub Key import/reload UI app verification closeout

Status: completed, app-verified and closed.

Purpose:

- Administratively close the v13.2 Scrub Key import/reload UI after app verification.
- Record that the implemented import/reload flow works in the Hugging Face app.
- Preserve the boundary that this phase is import/reload only and does not add AI-output reinsert.

Files added or changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1730_v13_2_scrub_key_import_ui_app_closeout.md`

Technical evidence already recorded:

- Tests #89 green — commit `83353e4`.
- Tests #90 green — commit `4a1ef55`.
- Sync to Hugging Face Space #104 green — commit `4a1ef55`.
- Tests #91 green — commit `4d8bfe9`.
- Sync to Hugging Face Space #105 green — commit `4d8bfe9`.
- Tests #92 green — commit `ff8321f`.
- Sync to Hugging Face Space #106 green — commit `ff8321f`.

App verification:

- Confirmed by coordinator/user.
- `Scrub Key laden` works.
- Scrub Key import/reload UI is visible.
- Upload/paste import flow works.
- Pseudonymization/reversibility warning is visible.
- Existing `Download Scrub Key (.json)` remains visible.
- Existing TXT, CSV, DOCX and PDF downloads remain available.

Closeout notes:

- GitHub Actions tests were green based on coordinator evidence.
- GitHub to Hugging Face sync was green based on coordinator evidence.
- Import/reload remains local and uses the existing helper logic.
- The key remains pseudonymization/reversible and must be protected.
- No AI-output reinsert behavior was added.
- No automatic document rehydration was added.
- No export/download behavior was intentionally changed.

Intentionally not changed in this app-verification closeout:

- No code files changed.
- No tests changed.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No direct edit to `presidio_streamlit.py`.
- No edit to `scrub_key.py`.
- No edit to `scrub_key_import.py`.
- No edit to `tests/*`.
- No AI-output reinsert behavior.
- No automatic document rehydration.
- No change to TXT, CSV, DOCX or PDF export/download behavior.
- No cloud processing.
- No secrets, tokens or real personal data.

Outcome:

- v13.2 Scrub Key import/reload UI is completed, app-verified and closed.

---

## v13.2 — Scrub Key import/reload UI integration

Status: implemented; Actions/sync verified green in closeout; app verification completed in app closeout.

Purpose:

- Integrate the existing Scrub Key import/reload helper into the Streamlit startup patch flow.
- Let the user upload or paste a previously exported Scrub Key JSON.
- Validate imported Scrub Keys before loading mappings into the current review/replacement table.
- Keep import/reload local and separate from deterministic reinsert or AI-output workflows.

Files added or changed:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_import_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1645_v13_2_scrub_key_import_ui.md`

Main changes:

- Added the `Scrub Key laden` UI section near the existing `Scrub Key (JSON)` export block.
- Added upload support for Scrub Key JSON files.
- Added paste support for Scrub Key JSON text.
- Reused the existing `build_scrub_key_import_result(...)` helper instead of duplicating parsing or validation logic.
- Added visible validation feedback before mapping rows are loaded.
- Added warnings that a Scrub Key makes values locally reversible and is pseudonymization, not full anonymization.
- Added warning text that the key must stay local and protected and should not be shared with AI services or third parties unless consciously intended and allowed.
- Loaded validated mapping rows into the current replacement table only after the visible `Valideer en laad Scrub Key` user action.
- Kept the existing `Download Scrub Key (.json)` export block.

Testing:

- Added `tests/test_scrub_key_import_ui_patch.py`.
- Local targeted validation on the reconstructed connector subset passed:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_import.py` → 8 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_import_ui_patch.py` → 9 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_ui_patch.py` → 12 passed.
  - `PYTHONPATH=. pytest -q` on the available subset → 35 passed.
- Coordinator evidence after implementation confirmed green tests and sync for commits `83353e4`, `4a1ef55`, `4d8bfe9` and `ff8321f`.

Intentionally not changed:

- No direct edit to `presidio_streamlit.py`.
- No deterministic reinsert behavior.
- No AI-output flow.
- No automatic document rehydration.
- No silent replacement of review rows without a visible user action.
- No change to TXT, CSV, DOCX or PDF export behavior.
- No change to existing Scrub Key JSON export behavior.
- No cloud processing.
- No server-side Scrub Key storage.
- No secrets, tokens or real personal data.

---

## v13.2 — Scrub Key import/reload helper and tests

Status: completed.

Purpose:

- Prepare reliable import/reload of a previously saved Scrub Key JSON file.
- Keep this work pure and helper-only before UI integration.
- Prepare future mapping reuse, session continuation and deterministic reinsert work.
- Preserve local-only handling and warning language for sensitive Scrub Keys.

Files added or changed:

- `scrub_key_import.py`
- `tests/test_scrub_key_import.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1605_v13_2_scrub_key_import_helper.md`

Main changes:

- Added `scrub_key_import.py` as a pure helper module.
- Added `validate_scrub_key_import_text(json_text)` for safe validation errors.
- Added `normalise_scrub_key_items(scrub_key)` to convert Scrub Key items into review-table-like mapping rows.
- Added `build_scrub_key_import_result(json_text)` with a UI-friendly result shape:
  - `ok`;
  - `errors`;
  - `warnings`;
  - `scrub_key`;
  - `mapping_rows`;
  - `item_count`;
  - `reversible`;
  - `privacy_model`;
  - `document_label`.
- Reused the existing `scrub_key_from_json(...)` and `validate_scrub_key(...)` model helpers.
- Added safe Dutch user-facing errors for empty input, invalid JSON syntax, invalid top-level structure and invalid Scrub Key content.
- Added a local-only privacy warning explaining that imported Scrub Keys make replacements locally reversible and should not be shared with AI services or third parties unless consciously intended and allowed.

Testing:

- Added `tests/test_scrub_key_import.py`.
- Tests cover valid Scrub Key JSON import, normalized row mapping, privacy warning, empty JSON text, invalid JSON syntax, invalid top-level format, structural validation errors, no input mutation and synthetic Dutch legal values only.
- Coordinator evidence supplied for green checks before UI integration:
  - Tests #83 green;
  - Tests #84 green;
  - Sync to Hugging Face Space #98 green;
  - Tests #85 green;
  - Sync to Hugging Face Space #99 green;
  - Tests #86 green;
  - Sync to Hugging Face Space #100 green.

Intentionally not changed in helper phase:

- No UI changes.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No direct edit to `presidio_streamlit.py`.
- No edit to existing Scrub Key export UI.
- No reinsert behavior.
- No AI-output flow.
- No cloud processing.
- No server-side Scrub Key storage.
- No real personal data in tests.
- No change to TXT, CSV, DOCX or PDF download behavior.

---

## v13.1 — Scrub Key JSON export UI closeout

Status: completed and app verified after mapping hotfix.

Purpose:

- Close v13.1 after confirming that the local Scrub Key JSON export works in the Hugging Face app.
- Record that the earlier `original_value` validation error was fixed.
- Preserve the boundary that Scrub Key import/reload and reinsert are not implemented yet.

Files added or changed in the full v13.1 line:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1535_v13_1_scrub_key_json_export_ui.md`
- `handover/workpackages/20260607_1535_v13_1_scrub_key_ui_mapping_hotfix.md`
- `handover/workpackages/20260607_1550_v13_1_scrub_key_json_export_closeout.md`

Main changes:

- Added a `Scrub Key (JSON)` section to the download/export flow.
- Added a `Download Scrub Key (.json)` button.
- Added warning text explaining that the Scrub Key makes replaced values locally reversible.
- Added warning text that this is pseudonymization, not full anonymization.
- Added warning text not to share the key with AI services or third parties unless consciously intended and allowed.
- Added timestamp creation in the UI/export layer so the pure `scrub_key.py` model remains deterministic and side-effect free.
- Added the mapping hotfix so app review-table rows are converted into Scrub Key model rows before calling `build_scrub_key(...)`.

Mapping hotfix:

- `find` → `original_value`
- `replace_with` → `placeholder`
- `entity_type` → `entity_type`
- `type_label` → `type_label`
- `source` → `source`
- `review_status` → `review_status`
- `include` → `include`

Testing and verification:

- Initial v13.1 UI implementation:
  - `Tests #73` green for commit `9d349bb`.
  - `Sync to Hugging Face Space #87` green for commit `9d349bb`.
- Mapping hotfix:
  - `Tests #78` green for commit `8d33941`.
  - `Sync to Hugging Face Space #92` green for commit `8d33941`.
- User verified in the Hugging Face app:
  - `Scrub Key (JSON)` section is visible.
  - pseudonymization / reversibility warning is visible.
  - `Item has empty required field: original_value` is gone.
  - `Download Scrub Key (.json)` is visible.
  - Scrub Key JSON download works.

Intentionally not changed:

- No edit to `scrub_key.py` in the mapping hotfix.
- No direct edit to `presidio_streamlit.py`.
- No Scrub Key import/reload.
- No reinsert UI.
- No AI-output flow.
- No cloud processing.
- No server-side Scrub Key storage.
- No change to TXT, CSV, DOCX or PDF download behavior.
- No change to existing replacement/export semantics.
- No `st.stop()` or export blocking behavior added.

Outcome:

- v13.1 Scrub Key JSON export is complete.

---

## v12.6 — Export sanity checks closeout

Status: completed and administratively closed after coordinator closeout instruction.

Purpose:

- Close the v12.6 export sanity workpackage after helper and UI integration were completed.
- Record that the UI warning block is advisory only.
- Preserve the documented boundary that export/download behavior was not changed.

Files added or changed in the full v12.6 line:

- `export_sanity.py`
- `tests/test_export_sanity.py`
- `tests/test_export_sanity_ui_patch.py`
- `fix_streamlit_nested_expanders.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1405_v12_6_export_sanity_helper.md`
- `handover/workpackages/20260607_1445_v12_6_export_sanity_ui.md`
- `handover/workpackages/20260607_1515_v12_6_export_sanity_closeout.md`

Main changes:

- Added pure helper logic for advisory export readiness checks.
- Added Dutch user-facing warning text for unchecked `Controle nodig` rows, candidate rows not included, no replacements selected, required user review and export not guaranteeing full anonymization.
- Integrated the existing `export_sanity.py` helper into the Streamlit startup patch flow.
- Added UI text for `Extra exportcontrole` near the existing v12.5 `Eindcontrole vóór download` block.
- Added patch-level tests to guard that the export sanity helper is wired into the UI patch.
- Administratively closed WP3C without changing code files.

Testing and verification:

- Helper validation recorded in WP3A handover: `PYTHONPATH=. pytest -q tests/test_export_sanity.py tests/test_review_summary.py` → 12 passed.
- Coordinator reconciled helper verification: `Tests #58` green, `Sync to Hugging Face Space #72` green, commit `b0bf8ae`.
- WP3C was administrative closeout only; no new local pytest run was performed by that worker.

Intentionally not changed:

- No code files changed in WP3C closeout.
- No direct edit to `presidio_streamlit.py`.
- No export/download blocking.
- No change to which rows are included in export.
- No change to TXT, CSV, DOCX or PDF download logic.
- No Scrub Key logic added in v12.6.
- No reinsert workflow added in v12.6.
- No cloud processing introduced.

Outcome:

- v12.6 is closed.
- v12 Review UX is complete through guidance, final review summary and export sanity warnings.

---

## Earlier completed work

- v13.0 Scrub Key specification and pure model.
- v12.5 Final review summary.
- v12.4 Review guidance text.
- Project governance setup.
- v12.3 Review table simplification.
- v12.2 Review focus filters.
- v12.1 Review table status model.
- v11.2 Dutch recognizer integration tests.
- v11.1 Legal reference recognizer hardening.
- v10 Regression test layer.
- v9.1 UI polish and baseline stabilization.
- v9 Dutch Legal UI Layer.

---

## Planned later phase — v13 and beyond

Possible directions:

- Deterministic reinsert helper.
- AI-output reinsert.
- Further recognizer expansion by legal domain.
