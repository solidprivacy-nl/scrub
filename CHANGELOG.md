## 2026-07-05 — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Purpose:

- Record live app verification for `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION`.
- Close the Review/Export vertical-density implementation line after PR #26 merge and live Hugging Face verification.
- Add concise closeout notes for the related plan and contract-test packages that were previously missing from `CHANGELOG.md`.

Verification evidence:

- Coordinator live Hugging Face screenshot reviewed.
- The app starts without Script execution error.
- The input section remains coherent.
- `2. Controleer resultaat` remains visible.
- Basiscontrole / Expertcontrole remain visible.
- `Markeringen tonen` and side-by-side review remain visible.
- `Gemiste waarde toevoegen` and the vervangtabel remain accessible.
- `3. Exporteer resultaat` remains visible.
- TXT/DOCX/PDF downloads are visible in a compact row.
- Scrub Key, audit/technical files and DOCX hygiene audit remain separate and accessible.

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_implementation.md`
- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_app_verify_closeout.md`
- `handover/workpackages/20260705_2213_review_export_vertical_density_implementation.md`
- `handover/workpackages/20260705_2242_review_export_vertical_density_app_verify_closeout.md`

Intentionally not changed:

- product code;
- tests;
- recognizer logic;
- replacement logic;
- export payloads;
- download filenames;
- MIME types;
- Scrub Key JSON;
- reinsert behavior;
- startup/runtime behavior.

Related package closeout:

- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_PLAN` — completed and merged; planning-only.
- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_CONTRACT_TESTS` — completed and merged; source-level guardrails only.

Next recommended step:

- Decide whether the current MVP UI is good enough for this pass, or start a new separately approved small UI package.

---

## 2026-07-05 — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / local validation passed.

Purpose:

- Reduce vertical density in the Review and Export areas after plan and contract-test packages were merged.
- Compress repeated Review helper copy while keeping side-by-side review, marker toggle, manual missed-value entry and replacement table accessible.
- Put the three primary document downloads in a compact three-column layout.
- Keep Scrub Key, audit/technical files and DOCX hygiene audit separate and accessible.

Files changed:

- `presidio_streamlit.py`
- `side_by_side_review_panel_ui.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_implementation.md`

Files added:

- `handover/workpackages/20260705_2213_review_export_vertical_density_implementation.md`

Validation status:

- Local validation passed.
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required after sync because visible UI behavior changed.

Intentionally not changed:

- recognizer logic;
- replacement logic;
- review table semantics;
- export payloads;
- download filenames;
- MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- DOCX/PDF parsing;
- startup/runtime behavior;
- dependencies;
- benchmark or recall logic.

Next recommended step:

- Open PR, verify GitHub Actions, merge when green, verify Hugging Face sync, then request live app verification.

---

## 2026-07-05 — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / local validation passed.

Purpose:

- Resume the duplicate input surface implementation after the connector-only worker was blocked.
- Keep one visible `1. Voeg document of tekst toe` step and group upload, synthetic example selection and pasted/extracted text into one input surface.
- Preserve TXT/DOCX/PDF upload support, synthetic legal examples, pasted/extracted text handling and input precedence.
- Preserve review, export/download, Scrub Key, reinsert, audit and DOCX hygiene behavior.

Files changed:

- `presidio_streamlit.py`
- `tests/test_duplicate_input_surface_simplification_contracts.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/scrub_wp_duplicate_input_surface_simplification_implementation.md`

Files added:

- `handover/workpackages/20260705_0113_duplicate_input_surface_implementation.md`

Validation status:

- Local validation passed:
  - `python -m pytest -q tests/test_duplicate_input_surface_simplification_contracts.py`
  - related UI/export guardrail tests
  - `git diff --check`
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required after merge/sync because visible UI grouping changed.

Intentionally not changed:

- document parsing behavior;
- upload backend;
- recognizer logic;
- replacement logic;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- reinsert behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Open PR, verify GitHub Actions, merge when green, verify Hugging Face sync, and request live app verification.

---

## 2026-07-04 — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS

Status: completed / PR validation pending.

Purpose:

- Lock the single-input-surface contract before the duplicate input implementation touches `presidio_streamlit.py`.
- Preserve existing TXT/DOCX/PDF upload support, synthetic legal example support, pasted/extracted text handling and input precedence.
- Preserve review, replacement table, Scrub Key, export/download, audit and DOCX hygiene surfaces.
- Block duplicate-input runtime/startup patching and prohibited scope expansion.

Files added:

- `tests/test_duplicate_input_surface_simplification_contracts.py`
- `workpackage_claims/scrub_wp_duplicate_input_surface_simplification_contract_tests.md`
- `handover/workpackages/20260704_2318_duplicate_input_surface_contract_tests.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Validation status:

- Source-level contract tests added.
- GitHub Actions pending after PR.
- Hugging Face sync not applicable until merge.
- App verification not applicable because this package changes no UI behavior.

Intentionally not changed:

- product implementation code;
- Streamlit UI behavior;
- document ingestion behavior;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Review PR validation.
- If green, merge this contract-test package.
- Then start `SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION` as the next narrow implementation package.

---

## 2026-07-03 — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION

Status: implemented / PR validation pending.

Purpose:

- Make the secondary review controls under `2. Controleer resultaat` calmer and easier to understand.
- Add a clear `Meer controleopties` grouping cue below the side-by-side review without introducing nested Streamlit expanders.
- Preserve side-by-side review, manual missed-value entry, replacement table, serial review, Scrub Key, export/download, audit and DOCX hygiene controls.

Files changed:

- `side_by_side_review_panel_ui.py`
- `RELEASE_NOTES.md`
- `CHANGELOG.md`
- `workpackage_claims/scrub_wp_secondary_control_grouping_polish_implementation.md`

Files added:

- `tests/test_secondary_control_grouping_polish_implementation.py`
- `handover/workpackages/20260703_0000_secondary_control_grouping_polish_implementation.md`

Validation status:

- Source-level implementation tests added.
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required after merge/sync because visible UI behavior changed.

Intentionally not changed:

- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Review PR validation.
- If green, merge and verify Hugging Face sync.
- Then request coordinator live app verification for the new `Meer controleopties` grouping cue.

---

## 2026-07-03 — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH

Status: implemented planning/contract-tests-only; PR validation pending.

Purpose:

- Prepare the final small UI-polish step for calmer grouping of secondary review controls.
- Avoid nested Streamlit expanders before touching `presidio_streamlit.py`.
- Preserve side-by-side review, manual missed-value entry, replacement table, serial review, Scrub Key, export/download, audit and DOCX hygiene controls.

Files added:

- `SECONDARY_CONTROL_GROUPING_POLISH_PLAN.md`
- `tests/test_secondary_control_grouping_polish_contracts.py`
- `workpackage_claims/scrub_wp_secondary_control_grouping_polish.md`
- `handover/workpackages/20260703_0000_secondary_control_grouping_polish.md`

Validation status:

- Source-level contract tests added.
- GitHub Actions pending after PR.
- Hugging Face sync not applicable until merge.
- App verification not applicable because no UI behavior changed in this planning/contract step.

Intentionally not changed:

- product code;
- Streamlit UI;
- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Run PR validation for the contract tests.
- If green, merge this plan/contract package.
- Then start `SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION` as the actual narrow UI implementation.

---

## 2026-07-03 — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Status: completed and app-verified.

Purpose:

- Make the side-by-side review surface calmer and less form-like.
- Keep the source-vs-processed comparison central while pointing users toward the safe download step.
- Preserve review table, manual missed-value entry, serial review, Scrub Key, export/download and audit controls.

Files changed:

- `side_by_side_review_panel_ui.py`
- `tests/test_review_copy_polish_ui.py`
- `tests/test_side_by_side_review_consolidation_dutch_sample.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/scrub_wp_review_surface_simplification_implementation.md`

Files added:

- `tests/test_review_surface_simplification_implementation.py`
- `handover/workpackages/20260703_0000_review_surface_simplification_implementation.md`

Validation status:

- Source-level implementation tests added.
- Related copy-polish and side-by-side tests updated.
- PR #12 initially failed on stale copy expectations; a narrow test-expectation fix was applied.
- PR #12 Tests passed after the narrow fix.
- PR #12 merged to `main`.
- Main Tests for commit `41cf304` passed.
- GitHub to Hugging Face sync for commit `41cf304` passed.
- App verification passed by coordinator screenshot.

Intentionally not changed:

- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Do not start broader UI/reinsert/export work without a dedicated workpackage.
- Decide whether further secondary-control grouping is desired as a separate small package, or return to recall/benchmark follow-up if product UI is good enough for the current MVP pass.

---

## 2026-06-23 20:52 Europe/Amsterdam — Full-suite validation update — SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

## 2026-06-23 — SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE

- Fixed DOCX plain-text extraction order for side-by-side preview.
- DOCX body paragraphs and tables are now read in document XML order instead of all paragraphs first and all tables afterwards.
- Added synthetic regression coverage for interleaved paragraph/table order.
- Preserved DOCX export, Scrub Key and reinsert semantics.
- Validation: `python -m pytest tests -x -vv` → 649 passed in 102.51s.

- Full suite passed: `python -m pytest tests -x -vv` → 647 passed in 108.30s.
- `git diff --check` passed.
- Local implementation validation complete.
- GitHub Actions, GitHub to Hugging Face sync and live app verification remain pending until PR/merge/sync.

## 2026-06-23 20:43 Europe/Amsterdam — SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

- Implemented direct-source reinsert interface simplification.
- Added `reinsert_mode_ui.py` with the visible four-step reinsert flow:
  1. Voeg Scrub Key toe
  2. Voeg tekst of document toe
  3. Controleer herstelrapport
  4. Download herstelde output
- Added a minimal direct hook in `presidio_streamlit.py`.
- Added a no-op guard to `fix_streamlit_pdf_text_reinsert.py` so startup does not mutate the direct-source reinsert UI.
- Preserved Scrub Key warnings, acknowledgement gates, restored download filenames, MIME types and local-only/no-AI/no-cloud/no-OCR/no-restored-PDF boundaries.
- Added `tests/test_reinsert_interface_simplification_ui.py`.

Validation so far:
- `tests/test_reinsert_interface_simplification_ui.py`: 8 passed
- reinsert patch tests: 39 passed
- warning/two-mode UI tests: 23 passed


# Changelog — SolidPrivacy Scrub

## SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_IMPLEMENTATION_RESTART — Execution interface simplification

Status: completed and verified on `main` via PR #6 (`a34700c`).

Summary:

- Simplified the default Scrub flow toward `1. Voeg document of tekst toe`, `2. Controleer resultaat`, `3. Exporteer resultaat`.
- Edited `presidio_streamlit.py` directly; no startup patch, runtime hook, sitecustomize hook or Dockerfile startup change was added.
- Collapsed secondary controls by default while keeping them available:
  - control-mode explanation;
  - recognition details;
  - review guidance;
  - manual missed-value entry;
  - focus filter / extra control helpers;
  - candidate audit values;
  - replacement table;
  - technical replacement details;
  - step-by-step review;
  - reusable replacements;
  - Scrub Key download;
  - audit/technical downloads.
- Kept side-by-side review visible as the main review surface.
- Kept the replacement table as source of truth and export input.
- Kept primary document downloads visible.

Tests:

- `tests/test_execution_interface_simplification_ui.py` — 6 passed.
- Side-by-side, serial review and replace logic UI tests — 37 passed.
- Export/download contract and implementation tests — 19 passed.
- `git diff --check` — passed.
- Full local test suite — 639 passed.
- PR #6 checks — green.
- Main Tests — green.
- GitHub to Hugging Face sync — green.
- Live app verification — passed by coordinator screenshot on 2026-06-23.

Intentionally not changed:

- export semantics;
- download file contents;
- download filenames;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark thresholds;
- document processing behavior;
- cloud processing;
- local packaging;
- Dockerfile startup behavior;
- runtime mutation behavior;
