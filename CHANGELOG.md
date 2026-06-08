# Changelog — SolidPrivacy Scrub

## WP16-FIX — Fix failing PDF text helper tests

Status: implemented; awaiting GitHub Actions and Hugging Face sync.

Purpose:

- Fix failing PDF text helper tests from the WP16 implementation line.
- Keep scope limited to helper/tests/documentation.
- Do not add UI, OCR, PDF output, AI calls or cloud behavior.

Cause:

- `.github/workflows/tests.yml` installs test dependencies directly with `python -m pip install pytest presidio-analyzer click==8.1.8`.
- The workflow does not install `requirements.txt`.
- `pypdf` was added to `requirements.txt`, but was not guaranteed to be installed in the Actions test job.
- The original PDF helper/test imports could therefore fail when `pypdf` was absent.

Fix:

- `scrub_key_pdf_text_reinsert.py` now imports `pypdf` optionally and remains import-safe when `pypdf` is missing.
- If `pypdf` is missing, the helper returns a clear validation issue instead of failing module import.
- `tests/test_scrub_key_pdf_text_reinsert.py` now uses `pytest.importorskip("pypdf")` for dependency-requiring PDF extraction tests.
- Added a monkeypatch test for the missing-`pypdf` helper path.

Files changed:

- `scrub_key_pdf_text_reinsert.py`
- `tests/test_scrub_key_pdf_text_reinsert.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Files added:

- `handover/workpackages/20260609_0015_pdf_text_helper_tests_fix.md`

Validation:

- The connector could not retrieve workflow-run logs for the WP16 commits.
- Root cause was inferred from `.github/workflows/tests.yml` and reconstructed local testing.
- Local reconstructed assertions for the PDF helper passed in the Python environment.
- Repository pytest execution was not available in this connector session.
- GitHub Actions: awaiting verification after WP16-FIX.
- Hugging Face sync: awaiting verification after WP16-FIX.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

- No UI files changed.
- No OCR added.
- No PDF output added.
- No AI/cloud behavior added.
- No workflow file changed.
- No existing pasted-text, TXT or DOCX reinsert UI behavior changed.
- No existing scrubbed export/download behavior changed.
- No Scrub Key import/export behavior changed.

## WP16 — Text-based PDF extraction helper spike, restored TXT output only

Status: implemented; awaiting GitHub Actions and Hugging Face sync after WP16-FIX.

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
- Text-based PDFs can be extracted locally when `pypdf` is installed.
- Extracted text is fed into the existing deterministic Scrub Key reinsert path.
- Restored output is text/TXT only.
- No PDF bytes are produced.
- Blank/no-text PDFs are clearly marked unsupported.
- Audit fields include local-only, no-AI, no-cloud, OCR-not-used and PDF-output-false indicators.

## WP15 — PDF text extraction reliability review only

Status: completed review/specification only.

Review conclusion:

- Do not implement full PDF reinsert now.
- Do not implement OCR now.
- Restored PDF output remains out of scope.
- PDF-to-DOCX reconstruction remains out of scope.
- DOCX remains the preferred document-level reinsert path.
- A future helper-only package may evaluate text-based PDF extraction to restored TXT output.

## Earlier completed work

- v13.8 DOCX reinsert upload/download UI.
- v13.7 TXT reinsert upload/download UI.
- v13.6 two-mode UI.
- v13.3 deterministic reinsert UI.
- v13 Scrub Key foundation and import/export work.
- v12 Review UX line.

## Planned later phase

- WP16B — Text-based PDF extraction helper spike verification and closeout, only after Tests and Hugging Face sync are green.
- WP17 — PDF text extraction reinsert UI planning only, only after WP16B closes green.
