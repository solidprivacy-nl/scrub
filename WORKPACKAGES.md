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

Status: implemented; awaiting GitHub Actions and Hugging Face sync.

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

- `extract_text_from_pdf_bytes(content)` extracts selectable PDF text locally.
- `reinsert_pdf_text_bytes(content, scrub_key)` feeds extracted text into existing deterministic Scrub Key reinsert logic.
- Restored output is TXT/text only.
- No restored PDF bytes are produced.
- Blank/no-text PDFs are clearly marked unsupported.
- Audit includes local-only, no-AI, no-cloud, OCR-not-used and PDF-output-false fields.

Validation status:

- Syntax-level validation of the new helper and test file was performed in the Python environment.
- Repository pytest execution was not available in this connector session.
- Required tests to run in CI:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_pdf_text_reinsert.py`
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_document_reinsert.py`
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert.py`
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py`
- GitHub Actions: awaiting verification.
- Hugging Face sync: awaiting verification.
- App verification: not applicable because no UI behavior changed.

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

## Active / next recommended workpackage

WP16B — Text-based PDF extraction helper spike verification and closeout.

Recommended WP16B scope:

- verify GitHub Actions tests are green;
- verify Hugging Face sync is green;
- record that app verification is not applicable because no UI changed;
- close WP16 if validation is green;
- do not add UI yet.

Future implementation after WP16B, if desired:

- WP17 — PDF text extraction reinsert UI planning only.

Keep explicitly out of scope until separately approved:

- full restored PDF output;
- OCR;
- PDF-to-DOCX reconstruction;
- cloud PDF conversion;
- AI-based extraction;
- layout preservation promises.
