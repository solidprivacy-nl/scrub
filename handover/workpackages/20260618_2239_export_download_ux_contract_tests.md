# Handover — WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS — Add contract tests for professional export/download UX redesign`

Status: completed and verified.

## Summary

Added contract tests and documentation for the professional export/download UX redesign.

The tests lock the planning contract before implementation: grouped document exports, separated Scrub Key area, secondary audit/technical downloads, no export semantics change, no Scrub Key/reinsert changes and no product claim.

A follow-up wording fix now expects `No production gate`, which is the wording used by the contract docs. This does not weaken the boundary; it aligns the test with the actual approved non-goal text.

## Files added

- `EXPORT_DOWNLOAD_UX_CONTRACTS.md`
- `tests/test_export_download_ux_contracts.py`
- `handover/workpackages/20260618_2239_export_download_ux_contract_tests.md`
- `workpackage_claims/WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `tests/test_export_download_ux_contracts.py`
- `handover/workpackages/20260618_2239_export_download_ux_contract_tests.md`
- `workpackage_claims/WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS.md`

## Product-code changes

None.

## Streamlit code changes

None.

No changes were made to:

- `presidio_streamlit.py`
- `serial_review_panel_ui.py`
- `docx_hygiene_audit_panel_ui.py`
- `fix_streamlit_nested_expanders.py`

## Export semantics changes

None.

No filenames, MIME types, payloads, export eligibility, Scrub Key contents or report contents were changed.

## Scrub Key/reinsert changes

None.

## Recognizer/benchmark changes

None.

## Tests added/updated

Added:

```text
tests/test_export_download_ux_contracts.py
```

The tests verify:

- `MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md` exists;
- target labels such as `Exporteer resultaat`, `Document downloaden`, `Scrub Key` and `Audit en technische bestanden` are present;
- Scrub Key is separated from normal document exports;
- primary document outputs and secondary audit outputs are specified;
- export semantics changes are explicitly blocked;
- Scrub Key safety remains visible;
- audit/technical details remain available as secondary layers;
- debug/prototype copy cleanup is planned;
- follow-up workpackage route is locked;
- this package does not approve implementation or semantic changes;
- the contract test file does not import Streamlit or mutate runtime app state.

Follow-up test fix:

- `test_this_package_does_not_approve_implementation_or_semantic_changes` now uses `No production gate`, matching the contract documentation.

Documentation added:

```text
EXPORT_DOWNLOAD_UX_CONTRACTS.md
```

## Tests/checks run

Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.

Coordinator screenshot evidence showed the earlier attempt failed on gate wording. The test now follows the contract document wording.

Coordinator screenshot evidence now confirms:

```text
Tests #1318 for commit 359447f — green
Sync to Hugging Face Space #1326 for commit 359447f — green
Hugging Face Space app — running without Script execution error
```

## Validation status

Verified by coordinator screenshot evidence.

## GitHub Actions status

Verified green by coordinator screenshot evidence.

```text
Tests #1318 for commit 359447f — green
```

## Hugging Face sync status

Verified green by coordinator screenshot evidence.

```text
Sync to Hugging Face Space #1326 for commit 359447f — green
```

## App verification status

Verified healthy by coordinator screenshot evidence. The Hugging Face Space is running without Script execution error.

No app behavior changed.

## Remaining risks

- Export/download UX is contract-protected but not implemented yet.
- Current app still has loose download buttons until implementation.
- Audit/technical details still need professional grouping in a later package.
- Scrub Key must remain visibly sensitive in implementation.
- Export semantics must remain unchanged in implementation.
- Human review remains necessary.

## Next recommended step

After green tests and sync:

```text
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION
```

Do not start follow-up work automatically.
