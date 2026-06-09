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

Implemented behavior:

- `extract_text_from_pdf_bytes(content)` extracts selectable PDF text locally when `pypdf` is installed.
- `reinsert_pdf_text_bytes(content, scrub_key)` feeds extracted text into existing deterministic Scrub Key reinsert logic.
- Restored output is TXT/text only.
- No restored PDF bytes are produced.
- Blank/no-text PDFs are clearly marked unsupported.
- Audit includes local-only, no-AI, no-cloud, OCR-not-used and PDF-output-false fields.

## WP16-FIX — Fix failing PDF text helper tests

Status: completed after Actions/sync verification; app verification not applicable because no UI behavior changed.

Fix applied:

- `scrub_key_pdf_text_reinsert.py` imports `pypdf` optionally and remains import-safe when `pypdf` is unavailable.
- If `pypdf` is missing, the helper returns an explicit validation issue instead of failing module import.
- `tests/test_scrub_key_pdf_text_reinsert.py` uses `pytest.importorskip("pypdf")` for PDF extraction tests.

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

Planning conclusion:

- PDF text extraction may be exposed only as text-based PDF extraction to restored TXT output.
- Future placement must be only in `Originele waarden terugzetten`.
- The UI must not appear in `Anonimiseren`.
- DOCX remains the preferred document-level reinsert route.
- The future workflow should be PDF upload → local text extraction → restored TXT preview/download only.
- Strong warnings must explain incomplete PDF extraction, no layout preservation, restored sensitive values, unsupported scanned/image-only PDFs and TXT-only output.
- Unsupported cases must not silently succeed.

## WP17B — Roadmap current-status reconciliation after WP17

Status: completed documentation-only update.

Purpose:

- Reconcile stale `ROADMAP.md` wording that still pointed to WP16B/WP17 as the active next steps.
- Align `ROADMAP.md`, `WORKPACKAGES.md` and `CHANGELOG.md` after WP17.
- Record that WP18 is the current next possible workpackage, but only after explicit approval.

## WP18 — PDF text extraction to restored TXT UI implementation

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Purpose:

- Expose the existing WP16 PDF text helper safely in the UI.
- Add only PDF upload → local selectable-text extraction → deterministic Scrub Key reinsert → restored TXT preview/download.
- Keep the feature inside `Originele waarden terugzetten` only.
- Keep `Anonimiseren` unchanged.

Implemented workflow:

```text
Originele waarden terugzetten
→ PDF upload
→ local selectable-text extraction via WP16 helper
→ existing deterministic Scrub Key reinsert
→ restored TXT preview
→ restored TXT download
→ audit report
```

Files added:

- `fix_streamlit_pdf_text_reinsert.py`
- `tests/test_pdf_text_reinsert_ui_patch.py`
- `handover/workpackages/20260609_1215_pdf_text_to_restored_txt_ui.md`

Files changed:

- `Dockerfile`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Implementation notes:

- `fix_streamlit_pdf_text_reinsert.py` runs after `fix_streamlit_nested_expanders.py` and adds the PDF-to-restored-TXT UI section.
- `Dockerfile` now runs both startup patches.
- `Dockerfile` also installs `pypdf` in the runtime image so the existing WP16 local PDF parser dependency is available to the app.
- No new PDF extraction library was introduced beyond the already approved WP16 `pypdf` dependency.
- No changes were made to `requirements.txt` or helper modules.

Validation status:

- UI patch tests added for the PDF-to-restored-TXT section.
- Repository pytest execution was not available in this connector session.
- GitHub Actions: awaiting verification.
- Hugging Face sync: awaiting verification.
- App verification: required after Actions/sync are green because UI behavior changed.

Intentionally not changed:

- No `presidio_streamlit.py` direct edit.
- No `scrub_key_pdf_text_reinsert.py` helper change.
- No `scrub_key_reinsert.py` change.
- No `scrub_key_import.py` change.
- No `requirements.txt` change.
- No `PDF_TEXT_REINSERT_UI_PLAN.md` change.
- No restored PDF output.
- No OCR.
- No PDF-to-DOCX reconstruction.
- No cloud PDF conversion.
- No AI-based extraction.
- No layout preservation promises.
- No batch PDF processing.
- No real-data PDF test cases.
- No automatic PDF rehydration.
- No existing TXT/DOCX/pasted reinsert semantics changed.
- No Scrub Key import/export behavior changed.
- No existing scrubbed export/download semantics changed.

## Active / next recommended workpackage

WP18B — PDF text to restored TXT UI app verification closeout.

Do not start WP18B until:

- GitHub Actions tests are green after WP18;
- Hugging Face sync is green after WP18;
- coordinator/user has verified the Hugging Face app behavior.

App verification must confirm:

- `Originele waarden terugzetten` shows the new PDF-to-TXT section;
- `Anonimiseren` does not show the PDF reinsert section;
- a valid Scrub Key can be loaded;
- a text-based PDF with placeholders can be uploaded;
- PDF text can be restored locally to TXT;
- restored TXT preview appears;
- restored TXT download appears;
- audit report appears;
- UI clearly says no OCR, no AI, no cloud and no PDF output;
- scanned/image-only PDFs are rejected or clearly marked unsupported;
- existing pasted-text, TXT and DOCX reinsert still work;
- existing anonymization/export behavior is unchanged.
