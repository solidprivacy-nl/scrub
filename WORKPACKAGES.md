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

Outcome:

- v12.3 can be treated as stable.

---

## Completed UI workpackages

### WP1 — v12.4 Review guidance text

Status: completed.

Evidence:

- GitHub Actions tests passed.
- GitHub to Hugging Face sync passed.
- Hugging Face app showed guidance around the review step.

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

Verification evidence:

- Coordinator reported GitHub Actions tests green for the v12.5 review summary line.
- Coordinator reported GitHub to Hugging Face sync green for the v12.5 review summary line.
- Hugging Face app was visually verified by the coordinator/user.
- Downloads were reported as still working: text, CSV, DOCX and PDF.

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

Validation evidence:

- Helper verification was reconciled externally by coordinator: `Tests #58` green and `Sync to Hugging Face Space #72` green for commit `b0bf8ae`.
- UI integration and closeout were completed.
- User visually confirmed `Extra exportcontrole` in the Hugging Face app.

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
- Added pure helpers:
  - `build_scrub_key(rows, document_label=None) -> dict`
  - `scrub_key_to_json(scrub_key) -> str`
  - `scrub_key_from_json(text) -> dict`
  - `validate_scrub_key(scrub_key) -> list[str]`
- Preserved the v13.0 excluded-row policy: unchecked rows are omitted.
- Kept timestamp handling deterministic: timestamps must be supplied by the caller.

Validation evidence:

- Local targeted validation passed: `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
- Coordinator later showed `Tests #56` green and `Sync #70` green for commit `d653643`.

Outcome:

- v13.0 model/spec is complete.

---

### WP4B / WP4B-FIX — v13.1 Scrub Key JSON export UI and mapping hotfix

Status: completed and formally closed after hotfix verification.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
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

- Initial v13.1 UI implementation:
  - `Tests #73` green for commit `9d349bb`.
  - `Sync to Hugging Face Space #87` green for commit `9d349bb`.
- Mapping hotfix:
  - `Tests #78` green for commit `8d33941`.
  - `Sync to Hugging Face Space #92` green for commit `8d33941`.
- User verified in the Hugging Face app:
  - Scrub Key section is visible.
  - pseudonymization warning is visible.
  - `original_value` validation error is gone.
  - `Download Scrub Key (.json)` is visible.
  - Scrub Key JSON download works.

Boundaries preserved:

- No edit to `scrub_key.py` in the mapping hotfix.
- No direct edit to `presidio_streamlit.py`.
- No Scrub Key import/reload.
- No reinsert UI.
- No AI-output flow.
- No cloud processing.
- No server-side Scrub Key storage.
- No change to TXT, CSV, DOCX or PDF export/download behavior.
- No `st.stop()` or export blocking behavior added.

Outcome:

- v13.1 Scrub Key JSON export is complete.
- The next phase can start with v13.2 Scrub Key import/reload.

---

## Active workpackage

### WP5 — v13.2 Scrub Key import/reload helper and tests

Status: planned; not started.

Goal:

- Allow the app/model layer to reliably read a previously saved Scrub Key JSON file.
- Prepare future workflows for reusing mappings across sessions and documents.
- Keep this as helper/test work first before any UI integration.

Planned files:

- `scrub_key_import.py` or extension helpers in `scrub_key.py` if the existing model is the cleaner fit.
- `tests/test_scrub_key_import.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/YYYYMMDD_HHMM_v13_2_scrub_key_import_helper.md`

Planned scope:

- Validate JSON structure from uploaded/imported Scrub Key text.
- Reuse `validate_scrub_key(...)` where possible.
- Return safe user-facing validation errors for invalid or incomplete keys.
- Produce normalized mapping rows suitable for later UI/reinsert work.

Boundaries:

- Do not add UI yet unless explicitly approved as a separate workpackage.
- Do not add reinsert behavior.
- Do not add AI-output flow.
- Do not introduce cloud processing.
- Do not store keys server-side.

---

## Recommended execution order

1. Start WP5 — v13.2 Scrub Key import/reload helper and tests.
2. After helper validation is green, plan v13.2 UI import/reload as a separate sequential UI workpackage.
3. After import/reload is stable, implement deterministic reinsert helper.
4. Only after deterministic reinsert is stable, consider AI-output reinsert UI.
