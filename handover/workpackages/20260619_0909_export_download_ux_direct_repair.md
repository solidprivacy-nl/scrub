# Handover — WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR`

Status: completed and verified.

## Summary

The startup-patch route was removed after repeated live app checks showed the export UI stayed old.

The grouped export/download UI was implemented directly in `presidio_streamlit.py` in commit `a202c3f573f21129c5299a11c7fe0c8b93e08f54`.

A follow-up compatibility commit `371ee49` kept the direct export implementation compatible with the legacy regression suite by preserving expected labels and avoiding forbidden helper-call substrings in the normal-flow text scan.

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

## Files changed in direct repair line

- `Dockerfile`
- `EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md`
- `presidio_streamlit.py`
- `tests/test_export_download_ux_implementation.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Files deleted in direct repair line

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

Focused checks:

```text
tests/test_export_download_ux_contracts.py — 10 passed
tests/test_export_download_ux_implementation.py — 9 passed
tests/test_recall_person_name_recognizer_contracts.py — 9 passed
tests/test_recall_person_name_recognizer_implementation.py — 5 passed
py_compile presidio_streamlit.py — no error reported
git diff --check — no error reported
```

Full suite:

```text
608 passed
```

## Validation status

Completed and verified by coordinator screenshots.

## GitHub Actions status

Verified green from coordinator screenshot for Tests and Sync to Hugging Face Space through the final relevant commits.

## Hugging Face sync status

Verified green from coordinator screenshot.

## App verification status

Verified by live app screenshot showing:

```text
5. Exporteer resultaat
Document downloaden
Scrub Key
Audit en technische bestanden
```

No Script execution error was visible in the provided live app screenshot.

## Remaining risks

- Downloads should still receive normal smoke verification after future export changes.
- Review/debug labels elsewhere are still not cleaned up.
- Human review remains necessary.

## Next recommended step

```text
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN
```

Do not start follow-up work automatically.
