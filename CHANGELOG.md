# Changelog — SolidPrivacy Scrub

## WP17 — PDF text extraction reinsert UI planning only

Status: completed planning/specification-only.

Purpose:

- Create a safe future UI specification for exposing the WP16 PDF text extraction helper.
- Decide whether PDF support should appear in the UI and under which boundaries.
- Keep implementation, UI changes, code changes, tests and dependencies out of scope.

Files added:

- `PDF_TEXT_REINSERT_UI_PLAN.md`
- `handover/workpackages/20260609_1130_pdf_text_reinsert_ui_planning.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Planning conclusion:

- PDF text extraction may be exposed in the future UI only as text-based PDF extraction to restored TXT output.
- The future UI must live only in `Originele waarden terugzetten`.
- The PDF text workflow must not appear in `Anonimiseren`.
- DOCX remains the preferred document-level reinsert route.
- The future workflow should be PDF upload → local text extraction → restored TXT preview/download only.
- Strong PDF limitation warnings are required.
- The future UI must warn that restored output may contain sensitive/confidential values again.
- Scanned/image-only PDFs remain unsupported because OCR is not available.
- Scrub must not offer restored PDF output.
- Unsupported PDF cases must show clear messages and must not silently succeed.
- Required audit fields are specified in `PDF_TEXT_REINSERT_UI_PLAN.md`.

Validation:

- Tests: not applicable; planning-only.
- GitHub Actions: not required unless documentation checks run.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.

Intentionally not changed:

- No code files changed.
- No tests changed.
- No UI changed.
- No dependencies changed.
- No OCR added.
- No PDF output added.
- No PDF-to-DOCX reconstruction added.
- No cloud PDF conversion added.
- No AI-based extraction added.
- No layout preservation promises added.
- No batch PDF processing added.
- No real-data PDF test cases added.
- No automatic PDF rehydration added.
- No existing export/download semantics changed.
- No existing scrubbed TXT/CSV/DOCX/PDF export/download behavior changed.
- No existing pasted-text, TXT or DOCX reinsert behavior changed.
- No Scrub Key import/export behavior changed.

Next recommended step:

- WP18 — PDF text extraction to restored TXT UI implementation.
- WP18 must be explicitly approved as a separate implementation workpackage before starting.
- Recommended WP18 scope: `Originele waarden terugzetten` only, PDF upload, local text extraction via WP16 helper, restored TXT preview, restored TXT download, audit report, strong warnings, no PDF output, no OCR and no AI/cloud.

## WP16B — Text-based PDF extraction helper spike verification and closeout

Status: completed closeout-only.

Purpose:

- Formally close WP16 and WP16-FIX as verified after coordinator-supplied GitHub Actions and Hugging Face sync evidence.
- Record that app verification is not applicable because no UI behavior changed.
- Preserve all code, test, UI, dependency and export boundaries.

Closeout result:

- WP16 / WP16-FIX is now verified.
- WP16 added the helper-only text-based PDF extraction path.
- WP16-FIX fixed the failing tests by making `pypdf` optional/import-safe.
- Tests #198–#201 are green based on coordinator evidence.
- Sync #212–#215 is green based on coordinator evidence.
- App verification is not applicable because no UI behavior changed.

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Files added:

- `handover/workpackages/20260609_1123_pdf_text_helper_verification_closeout.md`

Validation:

- Local tests: not required; closeout-only.
- GitHub Actions: green based on coordinator evidence.
- Hugging Face sync: green based on coordinator evidence.
- App verification: not applicable; no UI behavior changed.

Intentionally not changed:

- No code files changed.
- No tests changed.
- No UI changed.
- No dependencies changed.
- No OCR added.
- No PDF output added.
- No PDF-to-DOCX reconstruction added.
- No AI/cloud behavior added.
- No existing export/download semantics changed.
- No existing scrubbed TXT/CSV/DOCX/PDF export/download behavior changed.
- No existing pasted-text, TXT or DOCX reinsert behavior changed.
- No Scrub Key import/export behavior changed.

Next recommended step:

- WP17 — PDF text extraction reinsert UI planning only.
- WP17 must plan whether and how the helper from WP16 can be exposed safely as PDF upload → local text extraction → restored TXT preview/download only.
- Full restored PDF output, OCR, PDF-to-DOCX reconstruction, cloud PDF conversion, AI-based extraction and layout preservation promises remain out of scope unless separately approved.

## WP16C — Roadmap status reconciliation after v13.8 and PDF helper line

Status: completed documentation-only update.

Purpose:

- Refresh `ROADMAP.md` because it still described v12 as the current line and v13 as the next strategic phase.
- Align roadmap status with `WORKPACKAGES.md` and `CHANGELOG.md` after v13.8, WP15 and WP16/WP16-FIX.
- Preserve the strategic direction while updating current phase status and next steps.

Files changed:

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Files added:

- `handover/workpackages/20260609_0030_roadmap_status_reconciliation.md`

Main changes:

- Roadmap now records v12 Review UX as completed rather than current.
- Roadmap now records v13 Scrub Key / Reinsert line as implemented through pasted-text, TXT and DOCX reinsert.
- Roadmap now records WP15 PDF reliability review conclusion.
- Roadmap now records WP16 PDF text helper line and WP16-FIX green coordinator evidence.
- Roadmap now names WP16B as the active next closeout step.
- Roadmap now positions WP17 as PDF text extraction reinsert UI planning only, after WP16B.

Validation:

- Tests: not applicable; documentation-only update.
- GitHub Actions: not required unless documentation checks run.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.

Intentionally not changed:

- No code files changed.
- No tests changed.
- No UI changed.
- No OCR added.
- No PDF output added.
- No AI/cloud behavior added.
- No existing scrubbed export/download behavior changed.
- No Scrub Key import/export behavior changed.

## WP16-FIX — Fix failing PDF text helper tests

Status: implemented; green evidence supplied by coordinator; awaiting formal WP16B closeout.

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

Validation:

- Root cause was inferred from `.github/workflows/tests.yml` and reconstructed local testing.
- Local reconstructed assertions for the PDF helper passed in the Python environment.
- GitHub Actions: green based on coordinator evidence after WP16-FIX.
- Hugging Face sync: green based on coordinator evidence after WP16-FIX.
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

Status: implemented; awaiting formal WP16B closeout after green evidence.

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

- WP18 — PDF text extraction to restored TXT UI implementation, only if explicitly approved as a separate implementation workpackage.
