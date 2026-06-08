# Handover — WP16-FIX — Fix failing PDF text helper tests

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP16-FIX — Fix failing PDF text helper tests`

Status: implemented; awaiting GitHub Actions and Hugging Face sync.

## Summary

WP16-FIX addressed the failing PDF text helper test line without changing UI, OCR, PDF output, AI/cloud behavior, Scrub Key import/export behavior or existing export/download semantics.

The likely failure cause was dependency availability in GitHub Actions: the workflow installs test dependencies directly and does not install `requirements.txt`, so `pypdf` was not guaranteed to be present.

## Files added

- `handover/workpackages/20260609_0015_pdf_text_helper_tests_fix.md`

## Files changed

- `scrub_key_pdf_text_reinsert.py`
- `tests/test_scrub_key_pdf_text_reinsert.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

Updated:

- `tests/test_scrub_key_pdf_text_reinsert.py`

Test adjustment:

- PDF extraction tests now use `pytest.importorskip("pypdf")` when the optional PDF dependency is unavailable.
- Added a monkeypatch test for the missing-`pypdf` helper path.

## Validation status

- The connector could not retrieve workflow-run logs for the WP16 commits.
- Root cause was inferred from `.github/workflows/tests.yml` and reconstructed local testing.
- Local reconstructed assertions for the PDF helper passed in the Python environment.
- Repository pytest execution was not available in this connector session.

## GitHub Actions status

Awaiting verification after WP16-FIX.

## Hugging Face sync status

Awaiting verification after WP16-FIX.

## App verification status

Not applicable because no UI behavior changed.

## Dependency decision

No dependency was added or removed in WP16-FIX.

The earlier WP16 dependency decision remains:

- `pypdf` in `requirements.txt` for local selectable-text extraction only.
- No OCR dependency.
- No AI/cloud dependency.
- No PDF-to-DOCX or layout reconstruction dependency.

WP16-FIX made the helper import-safe if `pypdf` is not installed.

## Remaining risks

- If GitHub Actions should actively run the PDF extraction tests instead of skipping them, the workflow will need a separate approved change to install `requirements.txt` or `pypdf` in the test job.
- PDF text extraction remains limited to selectable text layers.
- No scanned/image-only PDF OCR support exists or should be implied.

## Next recommended step

Wait for GitHub Actions and Hugging Face sync evidence for WP16-FIX.

Then run:

`WP16B — Text-based PDF extraction helper spike verification and closeout`

Do not start WP16B until Tests and Sync are green after WP16-FIX.
