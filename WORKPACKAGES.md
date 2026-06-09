# SolidPrivacy Scrub — Workpackages

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Repository: `solidprivacy-nl/scrub`.

## Current status

WP0 through WP13B are complete.

## WP14 / WP14B / WP14C — v13.8 DOCX reinsert upload/download UI

Status: completed and app-verified after Actions/sync verification.

WP14 implemented controlled DOCX upload/download reinsert in `Originele waarden terugzetten`, using the existing local helper `reinsert_docx_bytes(content, scrub_key)`.

Existing pasted-text reinsert and TXT reinsert remain available.

## WP15 — PDF text extraction reliability review only

Status: completed review/specification only.

Review conclusion:

- Do not implement full PDF reinsert now.
- Do not implement OCR now.
- Restored PDF output remains out of scope.
- DOCX remains the preferred document-level reinsert path.
- A future helper-only spike may evaluate text-based PDF extraction to restored TXT output.

## WP16 — Text-based PDF extraction helper spike, restored TXT output only

Status: completed after Actions/sync verification; app verification not applicable because no UI behavior changed.

Added:

- `scrub_key_pdf_text_reinsert.py`
- `tests/test_scrub_key_pdf_text_reinsert.py`
- `handover/workpackages/20260609_0000_pdf_text_extraction_helper_spike.md`

Changed:

- `requirements.txt`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Dependency decision:

- Added `pypdf` as a local text-extraction dependency.
- `pypdf` is used only for local selectable-text extraction.
- No OCR dependency was added.
- No cloud PDF service was added.
- No AI extraction dependency was added.
- No PDF-to-DOCX or layout reconstruction dependency was added.

Implemented behavior:

- `extract_text_from_pdf_bytes(content)` extracts selectable PDF text locally when `pypdf` is installed.
- `reinsert_pdf_text_bytes(content, scrub_key)` feeds extracted text into existing deterministic Scrub Key reinsert logic.
- Restored output is TXT/text only.
- No restored PDF bytes are produced.
- Blank/no-text PDFs are clearly marked unsupported.
- Audit includes local-only, no-AI, no-cloud, OCR-not-used and PDF-output-false fields.

Verification closeout:

- WP16 added the helper-only text-based PDF extraction path.
- Tests are green based on coordinator evidence after WP16-FIX.
- Hugging Face sync is green based on coordinator evidence after WP16-FIX.
- App verification is not applicable because no UI changed.

## WP16-FIX — Fix failing PDF text helper tests

Status: completed after Actions/sync verification; app verification not applicable because no UI behavior changed.

Cause found:

- The GitHub Actions test workflow installs `pytest presidio-analyzer click==8.1.8` directly.
- It does not install `requirements.txt`.
- Therefore `pypdf` was not guaranteed to be present in the test job.
- The original helper/test module imported `pypdf` at module import time, which could fail before tests ran.

Fix applied:

- `scrub_key_pdf_text_reinsert.py` now imports `pypdf` optionally and remains import-safe when `pypdf` is unavailable.
- If `pypdf` is missing, the helper returns an explicit validation issue instead of failing module import.
- `tests/test_scrub_key_pdf_text_reinsert.py` now uses `pytest.importorskip("pypdf")` for PDF extraction tests.
- A test was added for the missing-`pypdf` path via monkeypatch.

Files changed in WP16-FIX:

- `scrub_key_pdf_text_reinsert.py`
- `tests/test_scrub_key_pdf_text_reinsert.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Handover added:

- `handover/workpackages/20260609_0015_pdf_text_helper_tests_fix.md`

Coordinator evidence after WP16-FIX:

```text
Tests #198 green — commit 4ccd79e
Sync to Hugging Face Space #212 green — commit 4ccd79e
Tests #199 green — commit 1fbdf48
Sync to Hugging Face Space #213 green — commit 1fbdf48
Tests #200 green — commit 410f04a
Sync to Hugging Face Space #214 green — commit 410f04a
Tests #201 green — commit 9354727
Sync to Hugging Face Space #215 green — commit 9354727
```

Verification closeout:

- WP16-FIX fixed the failing tests by making `pypdf` optional/import-safe.
- Tests are green based on coordinator evidence.
- Hugging Face sync is green based on coordinator evidence.
- App verification is not applicable because no UI changed.

Boundaries preserved:

- No UI files changed.
- No PDF reinsert UI added.
- No OCR added.
- No cloud processing added.
- No AI calls added.
- No PDF output added.
- No PDF-to-DOCX reconstruction added.
- Existing pasted-text, TXT and DOCX reinsert UI behavior unchanged.
- Existing scrubbed TXT/CSV/DOCX/PDF export/download behavior unchanged.
- Existing Scrub Key export/import behavior unchanged.
- Tests use synthetic values only.

## WP16C — Roadmap status reconciliation after v13.8 and PDF helper line

Status: completed documentation-only update.

Purpose:

- Refresh `ROADMAP.md` because it still described v12 as the current line and v13 as the next strategic phase.
- Align roadmap status with `WORKPACKAGES.md` and `CHANGELOG.md` after v13.8, WP15 and WP16/WP16-FIX.
- Preserve strategic direction while updating current phase status and next steps.

Files changed:

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Handover added:

- `handover/workpackages/20260609_0030_roadmap_status_reconciliation.md`

Validation:

- Tests: not applicable; documentation-only update.
- GitHub Actions: not required unless documentation checks run.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.

## WP16B — Text-based PDF extraction helper spike verification and closeout

Status: completed closeout-only.

Purpose:

- Formally close WP16 and WP16-FIX as verified after coordinator-supplied Actions/sync evidence.
- Record that app verification is not applicable because no UI behavior changed.
- Preserve all implementation, UI, dependency and export boundaries.

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Handover added:

- `handover/workpackages/20260609_1123_pdf_text_helper_verification_closeout.md`

Validation:

- Local tests: not required; closeout-only.
- GitHub Actions: green based on coordinator evidence.
- Hugging Face sync: green based on coordinator evidence.
- App verification: not applicable; no UI behavior changed.

## Active / next recommended workpackage

WP17 — PDF text extraction reinsert UI planning only.

WP17 must be planning/specification-only and must not start UI implementation directly.

Recommended WP17 planning scope:

- plan whether and how the WP16 helper can be exposed safely as PDF upload → local text extraction → restored TXT preview/download only;
- document warnings for incomplete PDF extraction, unsupported scanned/image-only PDFs, no layout preservation and sensitive-value restoration;
- keep restored PDF output, OCR, PDF-to-DOCX reconstruction, cloud PDF conversion, AI-based extraction and layout preservation promises out of scope unless separately approved.

Keep explicitly out of scope until separately approved:

- full restored PDF output;
- OCR;
- PDF-to-DOCX reconstruction;
- cloud PDF conversion;
- AI-based extraction;
- layout preservation promises.
