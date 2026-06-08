# Changelog — SolidPrivacy Scrub

## WP16 — Text-based PDF extraction helper spike, restored TXT output only

Status: implemented; awaiting GitHub Actions and Hugging Face sync.

Purpose:

- Add a pure helper spike for text-based PDF extraction.
- Restore Scrub Key placeholders into extracted PDF text using existing deterministic reinsert logic.
- Return restored TXT/text output only.
- Keep full PDF reinsert, OCR, UI and cloud/AI behavior out of scope.

Files added:

- `scrub_key_pdf_text_reinsert.py`
- `tests/test_scrub_key_pdf_text_reinsert.py`
- `handover/workpackages/20260609_0000_pdf_text_extraction_helper_spike.md`

Files changed:

- `requirements.txt`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Dependency decision:

- Added `pypdf`.
- Reason: `pypdf` provides local selectable-text extraction for PDFs and does not require OCR, AI, cloud services, PDF-to-DOCX conversion or layout reconstruction.
- This dependency is used only for helper-level text extraction.

Implemented behavior:

- Added `extract_text_from_pdf_bytes(content)`.
- Added `reinsert_pdf_text_bytes(content, scrub_key)`.
- Text-based PDFs can be extracted locally.
- Extracted text is fed into the existing deterministic Scrub Key reinsert path.
- Restored output is text/TXT only.
- No PDF bytes are produced.
- Blank/no-text PDFs are clearly marked unsupported.
- Audit fields include local-only, no-AI, no-cloud, OCR-not-used and PDF-output-false indicators.

Tests added:

- `tests/test_scrub_key_pdf_text_reinsert.py`

Test coverage includes:

- text-based PDF with one placeholder;
- text-based PDF with multiple placeholders;
- deterministic reinsert reuse;
- restored output is TXT/text only;
- no PDF bytes are produced;
- unknown placeholders remain unchanged and are reported;
- mapped placeholders not found are reported;
- blank/no-text PDF is unsupported;
- local-only/no-AI/no-cloud audit fields;
- `ocr_used=False`;
- `pdf_output=False`;
- invalid Scrub Key returns validation issues;
- helper does not mutate input Scrub Key;
- synthetic values only.

Validation:

- Syntax-level validation of the new helper and test file was performed in the Python environment.
- Repository pytest execution was not available in this connector session.
- GitHub Actions: awaiting verification.
- Hugging Face sync: awaiting verification.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

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

## WP15 — PDF text extraction reliability review only

Status: completed review/specification only.

Review conclusion:

- Do not implement full PDF reinsert now.
- Do not implement OCR now.
- Restored PDF output remains out of scope.
- PDF-to-DOCX reconstruction remains out of scope.
- DOCX remains the preferred document-level reinsert path.
- A future helper-only package may evaluate text-based PDF extraction to restored TXT output.

## WP14C — v13.8 DOCX reinsert upload/download UI final verification reconciliation

Status: completed.

WP14 DOCX reinsert UI is completed and app-verified after Actions/sync verification.

## Earlier completed work

- v13.8 DOCX reinsert upload/download UI.
- v13.7 TXT reinsert upload/download UI.
- v13.6 two-mode UI.
- v13.3 deterministic reinsert UI.
- v13 Scrub Key foundation and import/export work.
- v12 Review UX line.
- Earlier Dutch Legal UI and recognizer work.

## Planned later phase

- WP16B — Text-based PDF extraction helper spike verification and closeout.
- WP17 — PDF text extraction reinsert UI planning only, only after WP16B closes green.
