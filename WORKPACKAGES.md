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

## Completed prerequisite and UI workpackages

### WP0 — v12.3 stabilization check

Status: completed by user verification.

Evidence:

- GitHub Actions tests green.
- GitHub to Hugging Face sync green.
- App reloaded successfully.
- pandas Index truth-value error gone.
- Simplified review table working.
- Technical details available in separate expander.

### WP1 — v12.4 Review guidance text

Status: completed.

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

### WP4B / WP4B-FIX — v13.1 Scrub Key JSON export UI and mapping hotfix

Status: completed and app-verified.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_ui_patch.py`

### WP5 — v13.2 Scrub Key import/reload helper and tests

Status: completed.

Implemented files:

- `scrub_key_import.py`
- `tests/test_scrub_key_import.py`

### WP6 — v13.2 Scrub Key import/reload UI integration

Status: completed and app-verified.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_import_ui_patch.py`

### WP7A / WP7B / WP7B-FINAL — v13.3 Deterministic reinsert helper

Status: completed and formally closed after Actions/sync verification.

Implemented files:

- `scrub_key_reinsert.py`
- `tests/test_scrub_key_reinsert.py`

### WP8 — v13.3 Deterministic reinsert UI planning

Status: implemented; reinsert UI implementation completed in WP8B and app-verified in WP8C.

Implemented files:

- `REINSERT_UI_SPEC.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1900_v13_3_reinsert_ui_planning.md`

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

### WP9 — AI-output / document reinsert workflow UX and architecture review

Status: completed; review-only workpackage.

Added files:

- `AI_OUTPUT_REINSERT_WORKFLOW_REVIEW.md`
- `handover/workpackages/20260608_0000_ai_output_reinsert_workflow_review.md`

Outcome:

- Recommended two-mode direction: `Anonimiseren` and `Originele waarden terugzetten`.
- Recommended keeping pasted-text reinsert as fallback.
- Recommended controlled TXT/DOCX phases before PDF.
- Recommended local-only, deterministic, helper-first architecture.

### WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests

Status: implemented; awaiting coordinator verification of Actions/sync.

Added files:

- `scrub_key_document_reinsert.py`
- `tests/test_scrub_key_document_reinsert.py`
- `handover/workpackages/20260608_0000_v13_4_txt_docx_reinsert_foundation.md`

Outcome:

- Added `reinsert_text_document(text, scrub_key)`.
- Added `reinsert_txt_bytes(content, scrub_key, encoding="utf-8")`.
- Added `reinsert_docx_bytes(content, scrub_key)`.
- Reuses existing deterministic `reinsert_from_scrub_key(...)` logic.
- No UI, PDF, AI, cloud, or export/download behavior change.

Validation status:

- Local reconstructed targeted validation:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert.py` → 12 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_document_reinsert.py` → 14 passed.
- Local reconstructed full available subset:
  - `PYTHONPATH=. pytest -q` → 32 passed.
- Repository clone via container was not possible because outbound GitHub DNS was unavailable.

### WP10B — v13.4 TXT/DOCX reinsert foundation verification and closeout

Status: completed; Actions/sync not visible through connector, coordinator verification required.

Added files:

- `handover/workpackages/20260608_0000_v13_4_txt_docx_reinsert_foundation_closeout.md`

Outcome:

- WP10 closeout was performed without changing code.
- Actions/sync could not be verified through connector-visible status data.
- WP10 remains implemented and awaits coordinator verification of Actions/sync.

### WP11 — v13.5 Two-mode reinsert UI planning

Status: completed; planning/specification-only workpackage.

Added files:

- `TWO_MODE_UI_SPEC.md`
- `handover/workpackages/20260608_0000_v13_5_two_mode_ui_planning.md`

Outcome:

- Recommended moving Scrub to a two-mode interface:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.
- Compared current single-scroll workflow, Streamlit tabs, and landing cards.
- Recommended Streamlit tabs or clear mode panels as first implementation.
- Recommended landing cards as longer-term product direction.
- Planned TXT/DOCX reinsert UI phasing and kept PDF out of implementation scope.

### WP12 / WP12-FIX / WP12-FIX2 / WP12B — v13.6 Two-mode UI implementation and app verification closeout

Status: completed and app-verified after Actions/sync verification.

Implementation sequence:

- WP12 introduced the two-mode UI skeleton.
- WP12-FIX cleaned up content separation so `Originele waarden terugzetten` no longer shows the full anonymization workflow as its main content.
- WP12-FIX2 fixed the generated indentation/runtime error around `Scrub Key laden`.
- WP12B administratively closed the v13.6 two-mode UI line after successful technical verification and app verification.

Technical verification evidence:

```text
Tests #155 green — commit b27d115
Sync to Hugging Face Space #169 green — commit b27d115

Tests #156 green — commit 0e357bb
Sync to Hugging Face Space #170 green — commit 0e357bb

Tests #157 green — commit 268234d
Sync to Hugging Face Space #171 green — commit 268234d
```

Latest verified WP12-FIX2 commit:

```text
268234d9d1aeb9c82658c4c30702f51cfdd58c4c30702f51cfdd58c96
```

App verification confirmed:

- The app starts without Script execution error.
- No `IndentationError` appears.
- `Anonimiseren` mode remains available.
- `Originele waarden terugzetten` mode remains available and selectable.
- In `Originele waarden terugzetten`, the full anonymization workflow is no longer shown above the reinsert flow.
- `Scrub Key laden` is visible.
- Scrub Key upload/paste is visible.
- `Valideer en laad Scrub Key` is visible.
- Local pasted-text reinsert is visible.
- Warning about restored sensitive/confidential values is visible.
- Local-only / no-AI / no-cloud text is visible.
- Text field for reinsert is visible.
- Button `Zet originele waarden lokaal terug` is visible.
- No TXT upload reinsert UI appears.
- No DOCX upload reinsert UI appears.
- No PDF reinsert appears.
- No AI/cloud behavior appears.

Boundaries preserved:

- No code files changed in WP12B.
- No TXT upload reinsert UI added.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No existing scrubbed TXT/CSV/DOCX/PDF export/download behavior intentionally changed.
- No Scrub Key export/import behavior intentionally changed.
- No secrets, tokens or real personal data stored.

Closeout files:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260608_0000_v13_6_two_mode_ui_app_closeout.md`

---

## Current implementation workpackages

### WP13 — v13.7 TXT reinsert upload/download UI

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Changed files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_two_mode_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Added files:

- `tests/test_txt_reinsert_ui_patch.py`
- `handover/workpackages/20260608_0000_v13_7_txt_reinsert_upload_download_ui.md`

Implemented behavior:

- Added controlled TXT upload/download support inside `Originele waarden terugzetten`.
- Added section label `TXT-bestand terugzetten`.
- Added TXT upload label `Upload een TXT-bestand met placeholders`.
- Added action button `Zet TXT-bestand lokaal terug`.
- Added output label `Herstelde TXT-tekst`.
- Added download label `Download hersteld TXT-bestand (.txt)`.
- TXT reinsert uses existing deterministic local helper:
  - `reinsert_txt_bytes(content, scrub_key, encoding="utf-8")`.
- TXT reinsert requires a loaded Scrub Key before running.
- Existing pasted-text reinsert remains available as fallback.
- Existing Scrub Key load/import remains available.
- Existing anonymization workflow remains under `Anonimiseren`.
- Restored TXT audit summary includes document type, mapping counts, replacement count, missing/unknown/duplicate placeholders, validation issues, local-only, AI and cloud status.

Validation status:

- Added `tests/test_txt_reinsert_ui_patch.py` to verify:
  - TXT helper import/use;
  - TXT labels;
  - `.txt` upload-only configuration;
  - Scrub Key requirement;
  - TXT placement inside reinsert mode only;
  - pasted-text reinsert remains;
  - anonymization/export markers remain;
  - audit fields remain;
  - no DOCX upload reinsert UI;
  - no PDF reinsert;
  - no AI/cloud behavior;
  - no alteration of `apply_replacements_to_text` or existing scrubbed downloads.
- Updated `tests/test_two_mode_ui_patch.py` so TXT reinsert is allowed in the reinsert mode while DOCX/PDF/AI/cloud remain forbidden.
- Local clone/test run could not be performed in the container because outbound GitHub DNS was unavailable:
  - `Could not resolve host: github.com`.
- GitHub Actions: awaiting verification.
- Hugging Face sync: awaiting verification.
- App verification: required because UI behavior changed.

Boundaries preserved:

- `presidio_streamlit.py` was not directly edited.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration beyond TXT local reinsert added.
- No existing scrubbed TXT/CSV/DOCX/PDF export/download behavior intentionally changed.
- No Scrub Key JSON export behavior intentionally changed.
- No Scrub Key import/reload behavior intentionally changed except reusing the loaded key for TXT reinsert.
- No secrets, tokens or real personal data stored.

---

## Active / next recommended workpackage

### WP13-CLOSEOUT — v13.7 TXT reinsert upload/download UI app verification closeout

Status: recommended next workpackage after coordinator evidence.

Goal:

- Verify GitHub Actions tests.
- Verify GitHub to Hugging Face sync.
- App-verify TXT reinsert upload/download behavior.
- Close WP13 only after evidence confirms the UI works safely.

Required app verification:

In `Anonimiseren`:

- anonymization workflow remains available;
- source text/file input remains visible;
- review table remains visible;
- scrubbed TXT/CSV/DOCX/PDF downloads remain available;
- Scrub Key JSON export remains available;
- TXT reinsert upload UI is not presented as part of the anonymization workflow.

In `Originele waarden terugzetten`:

- `Scrub Key laden` remains visible;
- Scrub Key upload/paste validation remains visible;
- pasted-text reinsert remains visible;
- `TXT-bestand terugzetten` is visible;
- TXT upload accepts `.txt`;
- `Zet TXT-bestand lokaal terug` works with a valid Scrub Key;
- restored TXT text appears;
- `Download hersteld TXT-bestand (.txt)` works;
- audit summary appears;
- warning about restored sensitive/confidential data is visible;
- local-only / no-AI / no-cloud text is visible.

Also confirm:

- no DOCX upload reinsert UI appears yet;
- no PDF reinsert appears;
- no AI/cloud behavior appears;
- existing Scrub Key export/import remains available.

Recommended later workpackages:

```text
WP14 — v13.8 DOCX reinsert upload/download UI
WP15 — PDF text extraction reliability review only
```

---

## Recommended execution order

1. Verify WP13 GitHub Actions and Hugging Face sync.
2. Verify TXT reinsert upload/download behavior in the app.
3. Close WP13 through closeout if verification is green.
4. After TXT UI is verified, implement DOCX reinsert upload/download UI.
5. Keep PDF full reinsert out of scope until a separate reliability review.
6. Keep AI/cloud behavior out unless explicitly approved.
7. Preserve export/download and Scrub Key import/export semantics.
