# Handover — WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION — Implement professional grouped export/download UX without changing export semantics`

Status: completed, pending GitHub Actions/HF/app verification after marker-based patch fix.

## Summary

Implemented grouped export/download UX through a small startup patch:

```text
fix_streamlit_export_download_ux.py
```

The Hugging Face startup command runs the existing startup patches first and then runs this export UX patch before Streamlit starts. The patch changes only export/download presentation and copy.

The export section should become:

```text
5. Exporteer resultaat
```

with visible groups:

```text
Document downloaden
Scrub Key
Audit en technische bestanden
```

Follow-up fixes:

- Dockerfile startup-order fix moved the export UX patch after `fix_streamlit_pdf_text_reinsert.py`, preserving the legacy tested startup substring while still running the export patch before Streamlit.
- App verification then showed the live app still had the old export section, indicating the exact-block patch did not match the runtime-mutated app source.
- `fix_streamlit_export_download_ux.py` was changed from exact-block replacement to marker-based replacement, from the old export-section header to the `elif st_operator == "synthesize"` branch marker.

## Files added

- `fix_streamlit_export_download_ux.py`
- `tests/test_export_download_ux_implementation.py`
- `EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md`
- `handover/workpackages/20260618_2341_export_download_ux_implementation.md`
- `workpackage_claims/WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md`

## Files changed

- `Dockerfile`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `RELEASE_NOTES.md`
- `fix_streamlit_export_download_ux.py`
- `workpackage_claims/WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md`
- `handover/workpackages/20260618_2341_export_download_ux_implementation.md`

## Product-code changes

Added and refined a startup patch that modifies the Streamlit app source at container startup.

The patch replaces only the export/download UI block. It does not change export payload helpers or document processing helpers.

## Streamlit code changes

No direct edit to `presidio_streamlit.py` was made through the GitHub contents API.

Runtime behavior changes because Docker runs:

```text
python fix_streamlit_nested_expanders.py && python fix_streamlit_pdf_text_reinsert.py && python fix_streamlit_export_download_ux.py && streamlit run presidio_streamlit.py
```

The patch keeps the DOCX hygiene audit outside a nested expander.

## Export semantics changes

None intended.

Unchanged by design:

- download data/bytes;
- filenames;
- MIME types;
- TXT/DOCX/PDF/CSV/report generation helpers;
- Scrub Key JSON helper functions;
- export eligibility.

## Scrub Key/reinsert changes

No reinsert changes.

Scrub Key is visually separated in the export area with this warning:

```text
De Scrub Key kan originele waarden herstellen. Bewaar dit bestand veilig.
```

Scrub Key JSON content is still built by the existing helpers.

## Tests added/updated

Added:

```text
tests/test_export_download_ux_implementation.py
```

The tests verify:

- patched app source has `5. Exporteer resultaat`;
- export groups exist;
- Scrub Key warning exists;
- existing downloads remain available;
- filenames and MIME concepts remain present;
- no bundled/combined export wording was introduced;
- DOCX hygiene audit remains available;
- Docker runs the startup patch;
- implementation test and patch module do not import Streamlit or `presidio_streamlit.py`.

Existing contract tests remain:

```text
tests/test_export_download_ux_contracts.py
```

## Tests/checks run

Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.

Coordinator screenshot evidence showed two Dockerfile regression tests failed because the export patch was inserted between the existing nested-expander and PDF text reinsert startup patches.

The Dockerfile was fixed to preserve the expected tested startup substring:

```text
python fix_streamlit_nested_expanders.py && python fix_streamlit_pdf_text_reinsert.py
```

and then run:

```text
python fix_streamlit_export_download_ux.py
```

before Streamlit starts.

Coordinator app screenshot evidence then showed the live app still had the old export section. The export patch was therefore changed to marker-based replacement.

Required checks after marker-based fix:

```text
python -m pytest -q tests/test_export_download_ux_contracts.py
python -m pytest -q tests/test_export_download_ux_implementation.py
python -m pytest -q tests/test_recall_person_name_recognizer_contracts.py
python -m pytest -q tests/test_recall_person_name_recognizer_implementation.py
python -m py_compile presidio_streamlit.py
python -m py_compile fix_streamlit_export_download_ux.py
git diff --check
```

Recommended broader check:

```text
python -m pytest -q
```

## Validation status

Implemented and documented. Dockerfile startup-order fix applied. Marker-based export patch fix applied. Awaiting GitHub Actions/HF/app verification.

## GitHub Actions status

Pending/unknown after marker-based patch fix.

## Hugging Face sync status

Pending/unknown after marker-based patch fix.

## App verification status

Required and pending because visible UI behavior changes.

Coordinator should verify:

```text
Section title says "5. Exporteer resultaat"
Document downloaden group is visible
Scrub Key group is visible and separated
Audit en technische bestanden group is visible
Existing TXT/DOCX/PDF/CSV/report downloads remain available
No Script execution error
No unexpected export behavior change
```

## Remaining risks

- Runtime startup patch must apply cleanly in Hugging Face.
- Grouped export UI must be verified visually in the live app.
- Export semantics are intended unchanged, but app verification should confirm downloads remain available.
- Review/debug labels elsewhere are still not cleaned up; those are later packages.
- Human review remains necessary.

## Next recommended step

After green Actions, HF sync and app verification:

```text
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN
```

Do not start follow-up work automatically.
