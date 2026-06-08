# Handover — WP16 — Text-based PDF extraction helper spike

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP16 — Text-based PDF extraction helper spike, restored TXT output only`

Status: implemented; awaiting GitHub Actions and Hugging Face sync.

## Summary

WP16 added a pure helper spike for local text-based PDF extraction and Scrub Key reinsert to restored TXT/text output only.

The helper does not add UI, OCR, AI calls, cloud processing, PDF output, PDF-to-DOCX conversion, layout reconstruction or export behavior changes.

## Files added

- `scrub_key_pdf_text_reinsert.py`
- `tests/test_scrub_key_pdf_text_reinsert.py`
- `handover/workpackages/20260609_0000_pdf_text_extraction_helper_spike.md`

## Files changed

- `requirements.txt`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

Added:

- `tests/test_scrub_key_pdf_text_reinsert.py`

Coverage includes:

- text-based PDF extraction;
- one and multiple placeholders;
- existing deterministic Scrub Key reinsert path;
- restored TXT/text output only;
- no PDF bytes output;
- unknown placeholders reported and preserved;
- mapped placeholders not found reported;
- no-text PDF marked unsupported;
- local-only/no-AI/no-cloud fields;
- `ocr_used=False`;
- `pdf_output=False`;
- invalid Scrub Key validation issues;
- no mutation of input Scrub Key;
- synthetic data only.

## Validation status

- Syntax-level validation of the new helper and test file was performed in the Python environment.
- Repository pytest execution was not available in this connector session.

Recommended validation:

```bash
PYTHONPATH=. pytest -q tests/test_scrub_key_pdf_text_reinsert.py
PYTHONPATH=. pytest -q tests/test_scrub_key_document_reinsert.py
PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert.py
PYTHONPATH=. pytest -q tests/test_scrub_key.py
```

If feasible:

```bash
PYTHONPATH=. pytest -q
```

## GitHub Actions status

Awaiting verification.

## Hugging Face sync status

Awaiting verification.

## App verification status

Not applicable because no UI behavior changed.

## Dependency decision

Added `pypdf` to `requirements.txt`.

Justification:

- local PDF selectable-text extraction only;
- no OCR;
- no cloud service;
- no AI extraction;
- no PDF-to-DOCX conversion;
- no layout reconstruction dependency.

## Remaining risks

- PDF text extraction can be incomplete or have incorrect reading order.
- Scanned/image-only PDFs remain unsupported because OCR is not used.
- This helper must not be presented as full PDF reinsert.
- UI should not be added until WP16B verifies Actions/sync and a separate UI planning package is approved.

## Next recommended step

`WP16B — Text-based PDF extraction helper spike verification and closeout`

Recommended WP16B scope:

- verify GitHub Actions tests are green;
- verify Hugging Face sync is green;
- record app verification as not applicable;
- close WP16 if validation is green;
- do not add UI yet.
