# Handover — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION

Repository: solidprivacy-nl/scrub  
Status: implemented / PR validation pending

## Summary

Implemented the secondary-control grouping polish as a narrow visible UI cue: `Meer controleopties` now appears below the side-by-side review, before the existing secondary controls. This gives the stack of collapsed controls a clearer grouping point without using a parent expander and therefore avoids nested Streamlit expander risk.

The implementation keeps side-by-side review central and does not change replacement logic, export, Scrub Key, reinsert, recognizers, benchmarks, runtime/startup or dependencies.

## Files added

- `tests/test_secondary_control_grouping_polish_implementation.py`
- `handover/workpackages/20260703_0000_secondary_control_grouping_polish_implementation.md`

## Files changed

- `side_by_side_review_panel_ui.py`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/scrub_wp_secondary_control_grouping_polish_implementation.md`

## Tests / checks

Added source-level implementation tests covering:

- visible `Meer controleopties` grouping cue;
- no parent `Meer controleopties` expander and no nested expander implementation;
- side-by-side review and `Markeringen tonen` remain above the grouping cue;
- existing secondary controls remain reachable in source;
- review table and manual missed-value entry remain source-of-truth paths;
- export, Scrub Key, reinsert, audit and DOCX hygiene controls remain visible;
- blocked feature boundaries remain unchanged.

Targeted validation expected in PR/GitHub Actions:

```text
python -m pytest -q tests/test_secondary_control_grouping_polish_contracts.py tests/test_secondary_control_grouping_polish_implementation.py
python -m pytest -q tests/test_review_surface_simplification_implementation.py tests/test_mvp_fast_manual_mask_entry_ui.py tests/test_review_table_collapsible_contract.py tests/test_export_download_ux_contracts.py tests/test_export_download_ux_implementation.py
```

No manual full-suite run was performed outside GitHub Actions.

## Validation

- GitHub Actions: pending after PR.
- Hugging Face sync: pending after merge.
- App verification: pending after Actions and sync are green because visible UI changed.

## Intentionally not changed

- `presidio_streamlit.py`;
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
- This is a restrained grouping cue rather than a full rewrite of the secondary controls. A deeper restructure should remain a separate package if needed.

## Next recommended step

Open PR, review GitHub Actions, merge if green, verify Hugging Face sync, then ask the coordinator to verify the live app.
