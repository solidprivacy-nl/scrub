# Handover — WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS — Add contract tests for professional export/download UX redesign`

Status: completed, pending GitHub Actions/HF verification after wording fix.

## Summary

Added contract tests and documentation for the professional export/download UX redesign.

The tests lock the planning contract before implementation: grouped document exports, separated Scrub Key area, secondary audit/technical downloads, no export semantics change, no Scrub Key/reinsert changes and no product claim.

A follow-up wording fix made the benchmark-gate assertion accept both singular and plural wording (`no benchmark gate` / `no benchmark gates`). This does not weaken the boundary; it only avoids brittle wording failure.

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

- `test_this_package_does_not_approve_implementation_or_semantic_changes` now accepts both `no benchmark gate` and `no benchmark gates` wording.

Documentation added:

```text
EXPORT_DOWNLOAD_UX_CONTRACTS.md
```

## Tests/checks run

Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.

Coordinator screenshot evidence showed the first attempt failed on exact singular wording `No benchmark gate` while the docs used plural/equivalent wording.

Required checks after fix:

```text
python -m pytest -q tests/test_export_download_ux_contracts.py
python -m pytest -q tests/test_recall_person_name_recognizer_contracts.py
python -m pytest -q tests/test_recall_person_name_recognizer_implementation.py
python -m py_compile presidio_streamlit.py
git diff --check
```

Recommended broader check:

```text
python -m pytest -q
```

## Validation status

Implemented as tests/documentation-only. Wording fix added. Awaiting GitHub Actions verification.

## GitHub Actions status

Pending/unknown after wording fix.

## Hugging Face sync status

Pending/unknown after wording fix.

## App verification status

Not required. No app behavior changed.

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
