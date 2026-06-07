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

Status: completed and formally closed.

Implemented files:

- `export_sanity.py`
- `tests/test_export_sanity.py`
- `tests/test_export_sanity_ui_patch.py`
- `fix_streamlit_nested_expanders.py`

Implemented behavior:

- The app shows `Extra exportcontrole` near `Eindcontrole vóór download` before the download/export section.
- The warning block is advisory only.
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

Outcome:

- v13.0 model/spec is complete.

---

### WP4B / WP4B-FIX — v13.1 Scrub Key JSON export UI and mapping hotfix

Status: completed and app-verified.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_ui_patch.py`

Implemented behavior:

- The app shows a `Scrub Key (JSON)` section in the download/export flow.
- The app shows a pseudonymization / reversibility warning.
- The app shows `Download Scrub Key (.json)`.
- The Scrub Key JSON download works after the mapping hotfix.

Outcome:

- v13.1 Scrub Key JSON export is complete.

---

### WP5 — v13.2 Scrub Key import/reload helper and tests

Status: completed.

Implemented files:

- `scrub_key_import.py`
- `tests/test_scrub_key_import.py`

Outcome:

- v13.2 helper layer was ready for UI integration and is now part of the completed v13.2 import/reload flow.

---

### WP6 — v13.2 Scrub Key import/reload UI integration

Status: completed and app-verified.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_import_ui_patch.py`

Implemented behavior:

- Adds a `Scrub Key laden` section near the existing `Scrub Key (JSON)` export block.
- Allows upload of a Scrub Key `.json` file or pasted Scrub Key JSON.
- Validates the imported key using `build_scrub_key_import_result(...)` before loading.
- Shows pseudonymization/reversibility and local-protection warnings.
- Preserves the existing `Download Scrub Key (.json)` export block.

Outcome:

- v13.2 Scrub Key import/reload UI is completed, app-verified and closed.

---

### WP7A / WP7B / WP7B-FINAL — v13.3 Deterministic reinsert helper

Status: completed and formally closed after Actions/sync verification.

Implemented files:

- `scrub_key_reinsert.py`
- `tests/test_scrub_key_reinsert.py`

Implemented helper behavior:

- Added `detect_placeholders(text)`.
- Added `build_reinsert_mapping(scrub_key)`.
- Added `reinsert_from_scrub_key(text, scrub_key)`.
- Reuses existing `validate_scrub_key(...)` validation.
- Reports validation issues, mapping item count, active item count, excluded item count, replacement count, missing placeholders, unknown placeholders and duplicate placeholders.
- Reports `local_only=True`, `ai_processing=False` and `cloud_processing=False`.

Validation evidence:

- Local targeted validation: `PYTHONPATH=. pytest -q tests/test_scrub_key.py tests/test_scrub_key_import.py tests/test_scrub_key_reinsert.py` → 25 passed.
- Coordinator verification evidence confirmed Tests #106-#109 and Sync #120-#123 green.

Outcome:

- v13.3 deterministic reinsert helper is completed and formally closed.

---

### WP8 — v13.3 Deterministic reinsert UI planning

Status: implemented; reinsert UI implementation can start as a separate sequential workpackage.

Implemented files:

- `REINSERT_UI_SPEC.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1900_v13_3_reinsert_ui_planning.md`

Outcome:

- v13.3 deterministic reinsert UI is planned and ready for implementation.

---

### WP8B — v13.3 Deterministic reinsert UI implementation

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_reinsert_ui_patch.py`
- `tests/test_scrub_key_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1915_v13_3_reinsert_ui_implementation.md`

Implemented behavior:

- Adds `Originele waarden terugzetten` after the existing `Scrub Key laden` / Scrub Key area.
- Lets the user paste scrubbed or AI-generated text into `Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten`.
- Requires explicit button action: `Zet originele waarden lokaal terug`.
- Calls `reinsert_from_scrub_key(reinsert_input_text, active_reinsert_scrub_key)`.
- Shows `Herstelde tekst`.
- Adds `Download herstelde tekst (.txt)`.
- Shows `Controleverslag terugzetten` with mapping item count, active item count, excluded item count, replacement count, placeholders not found, unknown placeholders, duplicate placeholders, validation issues, local-only status, no-AI status and no-cloud status.
- Shows warning that restored text can again contain personal or confidential information and must be reviewed before sharing.
- Uses the imported validated Scrub Key from session state when available, otherwise the current Scrub Key built from reviewed replacement rows.

Validation status:

- Local targeted validation on a reconstructed subset passed:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py tests/test_scrub_key_import.py tests/test_scrub_key_reinsert.py tests/test_scrub_key_reinsert_ui_patch.py tests/test_scrub_key_import_ui_patch.py tests/test_scrub_key_ui_patch.py` → 57 passed.
- GitHub Actions: pending for WP8B commits.
- Hugging Face sync: pending for WP8B commits.
- App verification: pending because UI behavior changed.

Boundaries preserved:

- No direct edit to `presidio_streamlit.py`.
- No AI calls.
- No cloud processing.
- No automatic document rehydration.
- No DOCX/PDF reinsert added.
- No TXT, CSV, DOCX or PDF scrubbed export behavior changed.
- No Scrub Key JSON export behavior intentionally changed.
- No Scrub Key import/reload behavior intentionally changed except storing the validated imported key in session state for reinsert use.
- No silent overwrite of existing review rows.
- No secrets, tokens or real personal data stored.

Outcome:

- v13.3 deterministic local reinsert UI is implemented and awaits external verification and app testing.

---

## Active / next recommended workpackage

### WP8C — v13.3 Deterministic reinsert UI verification and closeout

Status: recommended next workpackage; not started here.

Goal:

- Verify GitHub Actions and Hugging Face sync for WP8B.
- Ask coordinator/user to verify the Hugging Face app shows the local reinsert UI and can restore mapped placeholders.
- Confirm existing Scrub Key export/import and TXT/CSV/DOCX/PDF scrubbed downloads remain available.

Boundaries:

- Closeout/status-only unless app verification reveals a bug.
- Do not add AI calls.
- Do not add cloud processing.
- Do not change export/download behavior.

---

## Recommended execution order

1. Verify GitHub Actions tests for WP8B.
2. Verify GitHub to Hugging Face sync for WP8B.
3. Ask for app verification because UI behavior changed.
4. Close WP8B through WP8C if verification is green.
5. Keep AI-output workflow separate and explicitly reviewed before AI-specific UI behavior.
