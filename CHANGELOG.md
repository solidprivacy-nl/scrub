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
