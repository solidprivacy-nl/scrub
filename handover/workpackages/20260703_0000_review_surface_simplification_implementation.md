# Handover — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Repository: solidprivacy-nl/scrub  
Status: implemented / PR validation pending

## Summary

Implemented a restrained review-surface simplification focused on calmer side-by-side review copy. The review surface now gives shorter guidance, keeps the source-vs-processed comparison central, and explicitly points users toward the safe download step without changing review-table, export, Scrub Key or reinsert semantics.

This implementation follows the merged planning and contract-test line and keeps the change narrow: no broad `presidio_streamlit.py` rewrite, no startup patch, no second review flow and no export/reinsert behavior change.

## Files added

- `tests/test_review_surface_simplification_implementation.py`
- `handover/workpackages/20260703_0000_review_surface_simplification_implementation.md`

## Files changed

- `side_by_side_review_panel_ui.py`
- `tests/test_review_copy_polish_ui.py`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/scrub_wp_review_surface_simplification_implementation.md`

## Tests / checks

Added source-level implementation tests covering:

- three-step flow markers/equivalent safe-download copy;
- side-by-side review visibility;
- review table reachability and source-of-truth wording;
- manual missed-value entry reachability;
- serial review secondary availability;
- Scrub Key separation and warning protection;
- export/download label and MIME/filename markers;
- audit/technical/DOCX hygiene access;
- absence of prohibited new review-surface behavior.

Updated existing side-by-side copy tests to reflect the calmer copy.

Targeted test commands expected in PR validation:

```text
python -m pytest -q tests/test_review_surface_simplification_contracts.py tests/test_review_surface_simplification_implementation.py
python -m pytest -q tests/test_review_copy_polish_ui.py tests/test_mvp_fast_manual_mask_entry_ui.py tests/test_review_table_collapsible_contract.py tests/test_export_download_ux_contracts.py tests/test_export_download_ux_implementation.py
```

No manual full-suite run was performed in this connector session.

## Validation

- GitHub Actions: pending after PR.
- Hugging Face sync: pending after merge.
- App verification: pending after Actions and sync are green because visible UI copy changed.

## Intentionally not changed

- `presidio_streamlit.py` business logic;
- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

## Remaining risks

- PR validation still needs to complete.
- Live app verification is required after merge and Hugging Face sync.
- The implementation is intentionally restrained; broader grouping of all secondary review expanders should be a separate package if desired.
- `CHANGELOG.md` still needs a small documentation-sync update if the connector blocks full-file replacement.

## Next recommended step

Open PR, review GitHub Actions, merge if green, verify Hugging Face sync, then ask the coordinator to verify the live app:

```text
1. App starts without Script execution error.
2. Normal anonymization flow is calmer and less form-like.
3. Side-by-side review remains visible.
4. Markeringen tonen remains visible.
5. Manual missed-value entry remains reachable.
6. Replacement table remains reachable and source of truth.
7. Step-by-step review remains reachable as optional secondary aid.
8. Scrub Key remains separate and warning-protected.
9. Primary document downloads remain visible.
10. Audit/technical downloads and DOCX hygiene audit remain available.
```
