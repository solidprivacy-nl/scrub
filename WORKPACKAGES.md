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

Outcome:

- The app shows `Eindcontrole vóór download` before downloads.
- The summary is advisory and does not change export/download semantics.
- v12.5 is complete.

---

### WP3 — v12.6 Export sanity checks

Status: completed and formally closed.

Implemented files:

- `export_sanity.py`
- `tests/test_export_sanity.py`
- `tests/test_export_sanity_ui_patch.py`
- `fix_streamlit_nested_expanders.py`

Outcome:

- The app shows advisory `Extra exportcontrole` before downloads.
- Downloads are not blocked.
- TXT, CSV, DOCX and PDF export behavior is not changed.
- v12 Review UX line is complete from WP1 through WP3.

---

## Completed strategic / helper workpackages

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

Outcome:

- v13.1 Scrub Key JSON export is complete and app-verified.

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

Status: implemented; reinsert UI implementation completed in WP8B and app-verified in WP8C.

Implemented files:

- `REINSERT_UI_SPEC.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1900_v13_3_reinsert_ui_planning.md`

Outcome:

- v13.3 deterministic reinsert UI was planned before implementation.

---

### WP8B / WP8C — v13.3 Deterministic reinsert UI implementation and app verification closeout

Status: completed and app-verified after Actions/sync verification.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_reinsert_ui_patch.py`
- `tests/test_scrub_key_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1915_v13_3_reinsert_ui_implementation.md`
- `handover/workpackages/20260607_1930_v13_3_reinsert_ui_app_closeout.md`

Outcome:

- v13.3 deterministic local reinsert UI is completed, app-verified and formally closed.
- No AI calls, cloud processing, automatic document rehydration or DOCX/PDF reinsert were added.
- Existing scrubbed export/download behavior was not changed.

---

### WP9 — AI-output / document reinsert workflow UX and architecture review

Status: completed; review-only workpackage.

Added files:

- `AI_OUTPUT_REINSERT_WORKFLOW_REVIEW.md`
- `handover/workpackages/20260608_0000_ai_output_reinsert_workflow_review.md`

Changed files:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Outcome:

- Pasted-text reinsert remains a safe baseline and fallback, but is not sufficient as the final legal-document workflow.
- The first three obvious ideas were explicitly challenged:
  - keeping only pasted-text reinsert;
  - immediately adding broad PDF/DOCX upload reinsert;
  - placing anonymize and de-anonymize in one combined long screen.
- Recommended UX direction is a two-mode interface:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.
- Recommended implementation sequence is phased:
  - keep pasted text;
  - add TXT upload/download reinsert;
  - add DOCX reinsert helper and tests;
  - add DOCX reinsert UI;
  - investigate PDF text extraction only;
  - consider PDF output only after reliability review.
- Recommended architecture remains local-only, deterministic and helper-first.

Validation:

- Tests: not applicable; planning/review-only workpackage.
- App verification: not applicable; no UI behavior changed.

---

### WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests

Status: implemented; awaiting coordinator verification of Actions/sync.

Latest implementation commit checked by WP10B:

```text
eb0c1ed2397ec1a4dc256d6e7e615ac4c026c0ee
```

Added files:

- `scrub_key_document_reinsert.py`
- `tests/test_scrub_key_document_reinsert.py`
- `handover/workpackages/20260608_0000_v13_4_txt_docx_reinsert_foundation.md`

Changed files:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Implemented helper behavior:

- Added `reinsert_text_document(text, scrub_key)` for plain text document-level reinsert.
- Added `reinsert_txt_bytes(content, scrub_key, encoding="utf-8")` for TXT bytes input/output.
- Added `reinsert_docx_bytes(content, scrub_key)` for DOCX main-document text-node reinsert.
- Reuses existing deterministic `reinsert_from_scrub_key(...)` logic.
- Returns restored text / restored bytes plus audit summary fields.
- Reports `document_type`, `local_only=True`, `ai_processing=False` and `cloud_processing=False`.
- Keeps TXT/DOCX reinsert pure and side-effect free.
- Does not mutate the input Scrub Key.

DOCX foundation limitations:

- Processes only `word/document.xml` text nodes.
- Supports normal body paragraphs and tables in `word/document.xml`.
- Does not restore placeholders split across multiple Word runs/text nodes.
- Does not process headers, footers, comments, tracked changes or metadata.
- Does not claim perfect formatting preservation.

Validation status:

- Local reconstructed targeted validation:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert.py` → 12 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_document_reinsert.py` → 14 passed.
- Local reconstructed full available subset:
  - `PYTHONPATH=. pytest -q` → 32 passed.
- Repository clone via container was not possible because outbound GitHub DNS was unavailable, so validation was performed on reconstructed files from GitHub-fetched content plus the new helper/tests.

WP10B verification / closeout status:

- Commit metadata visible for `eb0c1ed2397ec1a4dc256d6e7e615ac4c026c0ee`.
- GitHub combined commit status returned an empty status list.
- GitHub workflow-runs query for the commit returned no visible workflow runs.
- GitHub Actions: not visible through connector.
- Hugging Face sync: not visible through connector.
- App verification: not applicable; helper-only package and no UI behavior changed.

Boundaries preserved:

- No UI files changed.
- No edit to `fix_streamlit_nested_expanders.py`.
- No edit to `presidio_streamlit.py`.
- No PDF reinsert implementation added.
- No AI calls added.
- No cloud processing added.
- No automatic app document rehydration added.
- Existing TXT, CSV, DOCX and PDF scrubbed export/download behavior was not changed.
- Scrub Key JSON export/import behavior was not changed.
- Synthetic test data only.

---

### WP10B — v13.4 TXT/DOCX reinsert foundation verification and closeout

Status: completed; Actions/sync not visible through connector, coordinator verification required.

Added files:

- `handover/workpackages/20260608_0000_v13_4_txt_docx_reinsert_foundation_closeout.md`

Changed files:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Outcome:

- WP10 closeout was performed without changing code.
- Actions/sync could not be verified through connector-visible status data.
- WP10 remains implemented and awaits coordinator verification of Actions/sync.
- App verification is not applicable because WP10 added helper/test logic only and no UI behavior.

---

## Active / next recommended workpackage

### WP11 — v13.5 Two-mode reinsert UI planning

Status: recommended next workpackage; not started here.

Goal:

- Plan the future `Anonimiseren` / `Originele waarden terugzetten` mode structure before Streamlit UI changes.
- Decide where TXT/DOCX reinsert upload should appear after the helper foundation.
- Preserve existing pasted-text reinsert as fallback.
- Keep UI integration sequential and avoid parallel edits to the patch-based UI flow.

Recommended scope:

- Planning/specification only.
- Do not edit `fix_streamlit_nested_expanders.py` or `presidio_streamlit.py` yet.
- Do not change export/download semantics.
- Do not add PDF reinsert.
- Do not add AI/cloud behavior.

---

## Recommended execution order

1. Coordinator verifies WP10 GitHub Actions and Hugging Face sync, because connector-visible status data was unavailable in WP10B.
2. Start WP11 as two-mode UI planning only.
3. After WP11, implement TXT/DOCX reinsert UI sequentially.
4. Keep PDF full reinsert out of scope until a separate reliability review.
5. Keep AI/cloud behavior out unless explicitly approved.
6. Preserve export/download and Scrub Key import/export semantics.
