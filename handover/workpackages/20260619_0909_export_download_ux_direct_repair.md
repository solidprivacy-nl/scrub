# Handover — WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR`

Status: completed, pending GitHub Actions/HF/app verification.

## Summary

The startup-patch route was removed after repeated live app checks showed the export UI stayed old.

The grouped export/download UI was implemented directly in `presidio_streamlit.py` in commit `a202c3f573f21129c5299a11c7fe0c8b93e08f54`.

Target live UI:

```text
5. Exporteer resultaat
Document downloaden
Scrub Key
Audit en technische bestanden
```

## Files added

- `handover/workpackages/20260619_0909_export_download_ux_direct_repair.md`
- `workpackage_claims/WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR.md`

## Files changed in direct repair commit

- `Dockerfile`
- `EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md`
- `presidio_streamlit.py`
- `tests/test_export_download_ux_implementation.py`

## Files deleted in direct repair commit

- `fix_streamlit_export_download_ux.py`

## Product-code changes

Direct grouped export/download UI in `presidio_streamlit.py`.

## Streamlit code changes

Yes. The export/download section was changed directly in `presidio_streamlit.py`.

## Dockerfile/startup changes

The failed export startup patch was removed from the Docker command.

## Export semantics changes

None intended. The change is UI grouping/copy only.

## Reinsert/recognizer/benchmark changes

None.

## Tests/checks run in Codespaces by coordinator

```text
tests/test_export_download_ux_contracts.py — 10 passed
tests/test_export_download_ux_implementation.py — 9 passed
tests/test_recall_person_name_recognizer_contracts.py — 9 passed
tests/test_recall_person_name_recognizer_implementation.py — 5 passed
py_compile presidio_streamlit.py — no error reported
git diff --check — no error reported
```

## Validation status

Code committed and pushed by coordinator. Awaiting GitHub Actions, HF sync and live app verification.

## GitHub Actions status

Pending/unknown after metadata commit.

## Hugging Face sync status

Pending/unknown after metadata commit.

## App verification status

Required and pending because visible UI changed.

Required live checks:

```text
No Script execution error
Section title says "5. Exporteer resultaat"
Document downloaden group is visible
Scrub Key group is visible and separated
Audit en technische bestanden group is visible
TXT/DOCX/PDF/CSV/report downloads remain available
DOCX hygiene audit remains available
Technical information remains available
```

## Remaining risks

- Live app must prove the grouped export UI is visible.
- Downloads should be checked after grouping.
- Review/debug labels elsewhere are still not cleaned up.
- Human review remains necessary.

## Next recommended step

After green Actions/HF/app verification:

```text
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN
```

Do not start follow-up work automatically.
