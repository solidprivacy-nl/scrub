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

Status: implemented; awaiting GitHub Actions and Hugging Face sync after WP16-FIX.

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

Status: implemented; awaiting GitHub Actions and Hugging Face sync.

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

Validation status:

- The connector could not retrieve workflow-run logs for the WP16 commits.
- Root cause was inferred from `.github/workflows/tests.yml` and reconstructed local testing.
- Local reconstructed assertions for the PDF helper passed in the Python environment.
- Repository pytest execution was not available in this connector session.
- GitHub Actions: awaiting verification after WP16-FIX.
- Hugging Face sync: awaiting verification after WP16-FIX.
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

Do not start WP16B until:

- Tests are green after WP16-FIX.
- Hugging Face sync is green after WP16-FIX.

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
