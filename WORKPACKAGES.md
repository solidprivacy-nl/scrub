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

## WP16B — Text-based PDF extraction helper spike verification and closeout

Status: completed closeout-only.

Purpose:

- Formally close WP16 and WP16-FIX as verified after coordinator-supplied Actions/sync evidence.
- Record that app verification is not applicable because no UI behavior changed.
- Preserve all implementation, UI, dependency and export boundaries.

## WP17 — PDF text extraction reinsert UI planning only

Status: completed planning/specification-only.

Purpose:

- Specify whether and how the WP16 PDF text helper may be exposed safely in the future UI.
- Keep implementation out of scope.
- Preserve all current code, tests, UI behavior, dependencies and export semantics.

Planning conclusion:

- PDF text extraction may be exposed only as text-based PDF extraction to restored TXT output.
- Future placement must be only in `Originele waarden terugzetten`.
- The UI must not appear in `Anonimiseren`.
- DOCX remains the preferred document-level reinsert route.
- The future workflow should be PDF upload → local text extraction → restored TXT preview/download only.
- Strong warnings must explain incomplete PDF extraction, no layout preservation, restored sensitive values, unsupported scanned/image-only PDFs and TXT-only output.
- The future UI must show audit fields for document type, extracted text length, restored value count, mapping counts, placeholder issues, validation issues, unsupported reason, local-only status, AI/cloud status, OCR-used status and PDF-output status.
- Unsupported cases must not silently succeed.

## WP17B — Roadmap current-status reconciliation after WP17

Status: completed documentation-only update.

Purpose:

- Reconcile stale `ROADMAP.md` wording that still pointed to WP16B/WP17 as the active next steps.
- Align `ROADMAP.md`, `WORKPACKAGES.md` and `CHANGELOG.md` after WP17.
- Record that WP18 is the current next possible workpackage, but only after explicit approval.

Files changed:

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Handover added:

- `handover/workpackages/20260609_1200_roadmap_status_reconciliation_after_wp17.md`

Validation:

- Tests: not required; documentation-only update.
- GitHub Actions: not required unless documentation checks run automatically.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.

Intentionally not changed:

- No code changed.
- No tests changed.
- No UI changed.
- No dependencies changed.
- No OCR added.
- No PDF output added.
- No PDF-to-DOCX reconstruction added.
- No AI/cloud behavior added.
- No export/download semantics changed.

## Active / next possible workpackage

WP18 — PDF text extraction to restored TXT UI implementation.

WP18 must not start unless explicitly approved as a separate implementation workpackage.

Recommended WP18 scope if approved:

- `Originele waarden terugzetten` only;
- PDF upload;
- local text extraction via WP16 helper;
- restored TXT preview;
- restored TXT download;
- audit report;
- strong warnings;
- no PDF output;
- no OCR;
- no AI/cloud.

Keep explicitly out of scope until separately approved:

- full restored PDF output;
- OCR;
- PDF-to-DOCX reconstruction;
- cloud PDF conversion;
- AI-based extraction;
- layout preservation promises;
- batch PDF processing;
- real-data PDF test cases;
- automatic PDF rehydration.
