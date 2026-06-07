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

Hotfix:

- Fixed app-row-to-Scrub-Key-row mapping:
  - `find` → `original_value`
  - `replace_with` → `placeholder`
  - `entity_type` → `entity_type`
  - `type_label` → `type_label`
  - `source` → `source`
  - `review_status` → `review_status`
  - `include` → `include`
- Fixed the app-visible validation error:
  - `Item has empty required field: original_value`

Validation evidence:

- Initial v13.1 UI implementation: `Tests #73` and `Sync #87` green for commit `9d349bb`.
- Mapping hotfix: `Tests #78` and `Sync #92` green for commit `8d33941`.
- User verified in the Hugging Face app that the Scrub Key JSON download works.

Outcome:

- v13.1 Scrub Key JSON export is complete.

---

## Active workpackage

### WP5 — v13.2 Scrub Key import/reload helper and tests

Status: helper and tests implemented; awaiting GitHub Actions and Hugging Face sync confirmation.

Goal:

- Allow the model/helper layer to reliably read a previously saved Scrub Key JSON file.
- Prepare future workflows for reusing mappings across sessions and documents.
- Keep this as helper/test work before any UI integration.

Implemented files:

- `scrub_key_import.py`
- `tests/test_scrub_key_import.py`

Implemented helper behavior:

- Parse Scrub Key JSON text.
- Validate structure using the existing `validate_scrub_key(...)` model helper.
- Return safe Dutch user-facing validation errors for empty, invalid JSON or invalid Scrub Key content.
- Return an import result with `ok`, `errors`, `warnings`, `scrub_key`, `mapping_rows`, `item_count`, `reversible`, `privacy_model` and `document_label`.
- Normalize Scrub Key items to review-table-like mapping rows with both model fields and app-style fields:
  - `original_value` and `find`
  - `placeholder` and `replace_with`
  - `entity_type`
  - `type_label`
  - `source`
  - `review_status`
  - `include` / `include_state`
  - `timestamp`
  - `document_label`
- Preserve local-only privacy warning for imported keys.

Implemented tests:

- Valid Scrub Key JSON import.
- Normalized row mapping.
- Privacy warning.
- Empty JSON text.
- Invalid JSON syntax.
- Invalid top-level format.
- Structural validation errors.
- No input mutation.
- Synthetic Dutch legal values only.

Boundaries preserved:

- No UI changes.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No direct edit to `presidio_streamlit.py`.
- No reinsert behavior.
- No AI-output flow.
- No cloud processing.
- No server-side Scrub Key storage.

Validation required:

- `PYTHONPATH=. pytest -q tests/test_scrub_key.py`
- `PYTHONPATH=. pytest -q tests/test_scrub_key_import.py`
- preferably `PYTHONPATH=. pytest -q`

---

## Next planned UI workpackage

### WP5B — v13.2 Scrub Key import/reload UI integration

Status: planned; do not start until WP5 helper/tests are green.

Goal:

- Add UI support for loading a previously downloaded Scrub Key JSON file.

Boundaries:

- Do not add deterministic reinsert yet.
- Do not add AI-output flow.
- Do not store keys server-side.
- Keep import warnings visible.

---

## Recommended execution order

1. Verify GitHub Actions and Hugging Face sync for WP5 helper/tests.
2. After WP5 is green, close out WP5 helper if desired.
3. Then plan WP5B — v13.2 Scrub Key import/reload UI integration.
4. After import/reload is stable, implement deterministic reinsert helper.
5. Only after deterministic reinsert is stable, consider AI-output reinsert UI.
