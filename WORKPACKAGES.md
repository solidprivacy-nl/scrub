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

Status: implemented; awaiting formal WP16B closeout after green evidence.

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

## WP16-FIX — Fix failing PDF text helper tests

Status: implemented; green evidence supplied by coordinator; awaiting formal WP16B closeout.

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

App verification: not applicable because no UI behavior changed.

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

## Active / next recommended workpackage

WP16B — Text-based PDF extraction helper spike verification and closeout.

WP16B can now use coordinator evidence already supplied for:

- green GitHub Actions tests after WP16-FIX;
- green Hugging Face sync after WP16-FIX;
- app verification not applicable because no UI changed.

Recommended WP16B scope:

- close WP16/WP16-FIX as Actions/sync verified;
- record that app verification is not applicable;
- do not add UI;
- do not change code or tests.

Future implementation after WP16B, if desired:

- WP17 — PDF text extraction reinsert UI planning only.

Keep explicitly out of scope until separately approved:

- full restored PDF output;
- OCR;
- PDF-to-DOCX reconstruction;
- cloud PDF conversion;
- AI-based extraction;
- layout preservation promises.
