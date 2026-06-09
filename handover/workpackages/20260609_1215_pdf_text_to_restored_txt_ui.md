# Handover — WP18 — PDF text extraction to restored TXT UI implementation

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP18 — PDF text extraction to restored TXT UI implementation`

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

## Summary

WP18 exposes the existing WP16 PDF text helper safely in the UI as a TXT-only convenience workflow inside `Originele waarden terugzetten`.

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

This is not PDF reinsert. It does not reconstruct the original PDF.

## Files added

- `fix_streamlit_pdf_text_reinsert.py`
- `tests/test_pdf_text_reinsert_ui_patch.py`
- `handover/workpackages/20260609_1215_pdf_text_to_restored_txt_ui.md`

## Files changed

- `Dockerfile`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests added/updated

Added:

- `tests/test_pdf_text_reinsert_ui_patch.py`

Coverage includes:

- required PDF UI labels;
- required warnings;
- helper usage via `reinsert_pdf_text_bytes`;
- PDF-only upload;
- active Scrub Key requirement;
- restored TXT preview/download labels;
- audit fields;
- local/no-AI/no-cloud/no-OCR/no-PDF-output indicators;
- unsupported-case handling;
- no forbidden restored PDF/OCR/AI/cloud behavior.

## Validation status

- Repository pytest execution was not available in this connector session.
- Recommended commands:
  - `PYTHONPATH=. pytest -q tests/test_pdf_text_reinsert_ui_patch.py`
  - `PYTHONPATH=. pytest -q tests/test_two_mode_ui_patch.py`
  - `PYTHONPATH=. pytest -q tests/test_txt_reinsert_ui_patch.py`
  - `PYTHONPATH=. pytest -q tests/test_docx_reinsert_ui_patch.py`
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_pdf_text_reinsert.py`

## GitHub Actions status

Awaiting verification after WP18.

## Hugging Face sync status

Awaiting verification after WP18.

## App verification status

Required after Actions and Hugging Face sync are green, because UI behavior changed.

## Implementation notes

- The UI is added via `fix_streamlit_pdf_text_reinsert.py`, a second startup patch that runs after `fix_streamlit_nested_expanders.py`.
- `Dockerfile` now runs both startup patches.
- `Dockerfile` also installs `pypdf` in the runtime image so the existing WP16 helper dependency is available to the app.
- No direct edit was made to `presidio_streamlit.py`.
- No helper code was changed.

## Remaining risks

- The feature still depends on PDF selectable text extraction quality.
- Layout, visual order, tables, columns, headers and footers may be incomplete or changed.
- Scanned/image-only PDFs remain unsupported.
- App verification is required to confirm the section appears only in `Originele waarden terugzetten` and does not appear in `Anonimiseren`.

## Intentionally not changed

- No restored PDF output.
- No OCR.
- No PDF-to-DOCX reconstruction.
- No cloud PDF conversion.
- No AI-based extraction.
- No layout preservation promises.
- No batch PDF processing.
- No real-data PDF test cases.
- No automatic PDF rehydration.
- No existing pasted-text, TXT or DOCX reinsert semantics changed.
- No Scrub Key import/export behavior changed.
- No existing scrubbed export/download semantics changed.

## Next recommended step

Wait for GitHub Actions and Hugging Face sync evidence, then perform app verification.

Then run:

`WP18B — PDF text to restored TXT UI app verification closeout`

WP18B should be closeout-only.

## App verification checklist

Ask the coordinator/user to verify in the Hugging Face app that:

- `Originele waarden terugzetten` shows the new PDF-to-TXT section.
- `Anonimiseren` does not show the PDF reinsert section.
- A valid Scrub Key can be loaded.
- A text-based PDF with placeholders can be uploaded.
- The PDF text can be restored locally to TXT.
- The restored TXT preview appears.
- The restored TXT download appears.
- The audit report appears.
- The UI clearly says no OCR, no AI, no cloud and no PDF output.
- A scanned/image-only PDF is rejected or clearly marked unsupported.
- Existing pasted-text, TXT and DOCX reinsert still work.
- Existing anonymization/export behavior is unchanged.
