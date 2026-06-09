# Handover — WP18-FIX — Fix failing PDF text to TXT UI tests

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP18-FIX — Fix failing PDF text to TXT UI tests`

Status: implemented; awaiting GitHub Actions and Hugging Face sync.

## Root cause

WP18 implemented the PDF-to-restored-TXT UI, but GitHub Actions tests were red in coordinator evidence.

`STATUS_MONITORING_RUNBOOK.md` was read and followed where connector permissions allowed. However:

- commit-to-workflow lookup returned no workflow runs for the relevant WP18 commits;
- visible run numbers #220–#223 were not accepted by the connector as workflow run IDs;
- visible run numbers #220–#223 were also not accepted as job IDs;
- failing job logs could therefore not be fetched via connector.

The failure was reconstructed from the current repository files. The likely failing assertion was in `tests/test_pdf_text_reinsert_ui_patch.py`, around the brittle triple-quoted `else:` insertion marker expectation.

## Fix applied

Updated `tests/test_pdf_text_reinsert_ui_patch.py` so the test asserts the actual real-newline `else:` marker form present in `fix_streamlit_pdf_text_reinsert.py`.

No product behavior changed.

## Files added

- `handover/workpackages/20260609_1245_pdf_text_to_txt_ui_tests_fix.md`

## Files changed

- `tests/test_pdf_text_reinsert_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests added/updated

Updated:

- `tests/test_pdf_text_reinsert_ui_patch.py`

The update keeps the existing coverage for:

- `PDF-tekst terugzetten naar TXT`;
- `Upload een PDF-bestand met placeholders`;
- `Zet PDF-tekst lokaal terug`;
- `Herstelde TXT-tekst uit PDF`;
- `Download herstelde TXT uit PDF (.txt)`;
- `Controleverslag PDF-tekst terugzetten`;
- `reinsert_pdf_text_bytes`;
- `local_only`;
- `ai_processing`;
- `cloud_processing`;
- `ocr_used`;
- `pdf_output`;
- `unsupported_reason`;
- no OCR behavior;
- no PDF output behavior;
- no AI/cloud behavior.

## Validation status

Repository pytest execution was not available in this connector session.

Recommended commands:

```bash
PYTHONPATH=. pytest -q tests/test_pdf_text_reinsert_ui_patch.py
PYTHONPATH=. pytest -q tests/test_two_mode_ui_patch.py
PYTHONPATH=. pytest -q tests/test_txt_reinsert_ui_patch.py
PYTHONPATH=. pytest -q tests/test_docx_reinsert_ui_patch.py
PYTHONPATH=. pytest -q tests/test_scrub_key_pdf_text_reinsert.py
```

## GitHub Actions status

Awaiting verification after WP18-FIX.

## Hugging Face sync status

Awaiting verification after WP18-FIX.

Coordinator evidence before this fix stated that Hugging Face sync for WP18 commits was green, but the new WP18-FIX commit still needs sync verification.

## App verification status

Blocked until GitHub Actions and Hugging Face sync are green.

WP18 changed UI behavior, so app verification remains required after Actions/sync are green.

## Remaining risks

- The connector could not fetch the exact failing Actions log, so the fix is based on repository inspection and reconstructed failure.
- If Actions remain red, the next worker should fetch the actual run/job logs if connector access permits or ask for the run/job URL.
- App verification must still confirm the PDF-to-TXT section appears only in `Originele waarden terugzetten` and not in `Anonimiseren`.

## Intentionally not changed

- No `presidio_streamlit.py` direct edit.
- No `fix_streamlit_pdf_text_reinsert.py` functional change.
- No `Dockerfile` change.
- No helper code changed.
- No dependency change.
- No OCR.
- No restored PDF output.
- No PDF-to-DOCX reconstruction.
- No AI/cloud extraction.
- No layout reconstruction.
- No batch PDF processing.
- No real-data tests.
- No automatic PDF rehydration.
- No existing pasted-text/TXT/DOCX reinsert semantics changed.
- No existing anonymization/export semantics changed.
- No Scrub Key import/export behavior changed.

## Next recommended step

Check GitHub Actions and Hugging Face sync for the WP18-FIX commit.

Only when both are green:

1. Perform WP18 app verification.
2. Then run `WP18B — PDF text to restored TXT UI app verification closeout`.

WP18B must be closeout-only.
