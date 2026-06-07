# SolidPrivacy Scrub — Workpackages

This file translates `ROADMAP.md` into executable workpackages.

Use:

- `PROJECT_PROMPT.md` for full worker instructions and operating rules.
- `PROJECT_PROMPT_SHORT.md` for the compact ChatGPT Project Instructions version.
- `ROADMAP.md` for product direction and phase order.
- `WORKPACKAGES.md` for immediate execution planning and parallelization.
- `CHANGELOG.md` for implementation history.

---

## Mandatory worker start sequence

Every worker must start by reading, in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

If the active repository is not `solidprivacy-nl/scrub`, stop and report the mismatch.

Every worker must end with a handover summary and write that summary to:

```text
handover/workpackages/
```

Filename format:

```text
handover/workpackages/YYYYMMDD_HHMM_<workpackage_slug>.md
```

---

## Current execution principle

Avoid parallel edits to the same Streamlit UI patch area.

Parallel work is safe for:

- pure helper modules;
- tests;
- specifications;
- documentation;
- non-UI architecture work.

Parallel work is risky for:

- `presidio_streamlit.py`;
- `fix_streamlit_nested_expanders.py`;
- export/download UI blocks;
- shared replacement table flow.

UI integration should therefore happen sequentially.

---

## Completed prerequisite

### WP0 — v12.3 stabilization check

Status: completed by user verification.

Evidence:

- GitHub Actions tests green.
- GitHub to Hugging Face sync green.
- App reloaded successfully.
- pandas Index truth-value error gone.
- Simplified review table working.
- Technical details available in separate expander.

---

## Completed UI workpackages

### WP1 — v12.4 Review guidance text

Status: completed.

Outcome:

- Review workflow guidance is visible.
- Export semantics were not changed.

---

### WP2 — v12.5 Final review summary

Status: completed and formally closed after verification.

Implemented files:

- `review_summary.py`
- `tests/test_review_summary.py`
- `tests/test_review_summary_ui_patch.py`
- `fix_streamlit_nested_expanders.py`

Implemented behavior:

- The app shows `Eindcontrole vóór download` before the download/export section.
- The summary is advisory and does not change export/download semantics.

Outcome:

- v12.5 is complete.

---

### WP3 — v12.6 Export sanity checks

Status: completed and formally closed after coordinator closeout instruction.

Implemented files:

- `export_sanity.py`
- `tests/test_export_sanity.py`
- `tests/test_export_sanity_ui_patch.py`
- `fix_streamlit_nested_expanders.py`
- `handover/workpackages/20260607_1515_v12_6_export_sanity_closeout.md`

Implemented behavior:

- The app shows `Extra exportcontrole` near `Eindcontrole vóór download` before the download/export section.
- The warning block is advisory only and explicitly says downloads remain available and export settings remain unchanged.
- Downloads are not blocked.
- TXT, CSV, DOCX and PDF export behavior is not changed.

Outcome:

- v12.6 is closed.
- v12 Review UX line is complete from WP1 through WP3.

---

## Completed strategic workpackages

### WP4 — v13.0 Scrub Key specification and pure model

Status: completed.

Implemented files:

- `SCRUB_KEY_SPEC.md`
- `scrub_key.py`
- `tests/test_scrub_key.py`
- `handover/workpackages/20260607_1342_v13_0_scrub_key_spec_model.md`

Implemented behavior/model:

- Defined the local Scrub Key mapping file concept.
- Added pure helpers: `build_scrub_key`, `scrub_key_to_json`, `scrub_key_from_json`, `validate_scrub_key`.
- Preserved the v13.0 excluded-row policy: unchecked rows are omitted.

Outcome:

- v13.0 model/spec is complete.

---

### WP4B / WP4B-FIX — v13.1 Scrub Key JSON export UI and mapping hotfix

Status: completed and formally closed after hotfix verification.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_ui_patch.py`
- `handover/workpackages/20260607_1535_v13_1_scrub_key_json_export_ui.md`
- `handover/workpackages/20260607_1535_v13_1_scrub_key_ui_mapping_hotfix.md`
- `handover/workpackages/20260607_1550_v13_1_scrub_key_json_export_closeout.md`

Implemented behavior:

- The app shows a `Scrub Key (JSON)` section in the download/export flow.
- The app shows a pseudonymization / reversibility warning.
- The app shows `Download Scrub Key (.json)`.
- The Scrub Key JSON download works after the mapping hotfix.

Validation evidence:

- Initial v13.1 UI implementation: `Tests #73` and `Sync #87` green for commit `9d349bb`.
- Mapping hotfix: `Tests #78` and `Sync #92` green for commit `8d33941`.
- User verified in the Hugging Face app that the Scrub Key JSON download works.

Outcome:

- v13.1 Scrub Key JSON export is complete.

---

### WP5 — v13.2 Scrub Key import/reload helper and tests

Status: helper and tests implemented; coordinator evidence reported green checks before UI integration.

Implemented files:

- `scrub_key_import.py`
- `tests/test_scrub_key_import.py`

Implemented helper behavior:

- Parse Scrub Key JSON text.
- Validate structure using the existing `validate_scrub_key(...)` model helper.
- Return safe Dutch user-facing validation errors for empty, invalid JSON or invalid Scrub Key content.
- Return an import result with `ok`, `errors`, `warnings`, `scrub_key`, `mapping_rows`, `item_count`, `reversible`, `privacy_model` and `document_label`.
- Normalize Scrub Key items to review-table-like mapping rows with both model fields and app-style fields.
- Preserve local-only privacy warning for imported keys.

Boundaries preserved:

- No UI changes in the helper workpackage.
- No direct edit to `presidio_streamlit.py`.
- No reinsert behavior.
- No AI-output flow.
- No cloud processing.
- No server-side Scrub Key storage.

Outcome:

- v13.2 helper layer is ready for UI integration.

---

## Active workpackage

### WP6 — v13.2 Scrub Key import/reload UI integration

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Goal:

- Add UI support for loading a previously downloaded Scrub Key JSON file.
- Validate imported keys before loading their mappings into the current replacement/review workflow.
- Keep import/reload local and separate from deterministic reinsert or AI-output workflows.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_import_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1645_v13_2_scrub_key_import_ui.md`

Implemented behavior:

- Adds a `Scrub Key laden` section near the existing `Scrub Key (JSON)` export block.
- Allows upload of a Scrub Key `.json` file or pasted Scrub Key JSON.
- Validates the imported key using the existing `build_scrub_key_import_result(...)` helper before loading.
- Shows pseudonymization/reversibility and local-protection warnings.
- Loads validated mapping rows into the current replacement table only after the visible `Valideer en laad Scrub Key` user action.
- Preserves the existing `Download Scrub Key (.json)` export block.

Validation:

- Local targeted validation on the reconstructed connector subset passed:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_import.py` → 8 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_import_ui_patch.py` → 9 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_ui_patch.py` → 12 passed.
  - `PYTHONPATH=. pytest -q` on the available subset → 35 passed.
- GitHub Actions status pending after latest commits.
- GitHub to Hugging Face sync status pending after latest commits.
- Hugging Face app verification pending.

Boundaries preserved:

- No direct edit to `presidio_streamlit.py`.
- No AI-output reinsert.
- No automatic document rehydration.
- No silent replacement of current review rows without a visible user action.
- No change to TXT, CSV, DOCX or PDF export behavior.
- No change to existing Scrub Key JSON export behavior.
- No cloud processing.
- No secret, token or real personal data storage.

---

## Recommended execution order

1. Verify GitHub Actions and Hugging Face sync for WP6.
2. Ask the coordinator/user to verify that `Scrub Key laden` is visible and can load a valid exported key.
3. After import/reload is stable, implement a deterministic reinsert helper.
4. Only after deterministic reinsert is stable, consider AI-output reinsert UI.
