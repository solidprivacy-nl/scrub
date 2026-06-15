# Handover — WP_REVIEW_SURFACE_DUPLICATE_HEADING_CLEANUP

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_SURFACE_DUPLICATE_HEADING_CLEANUP`

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

## Files added

- `handover/workpackages/20260615_0420_review_surface_duplicate_heading_cleanup.md`
- `workpackage_claims/WP_REVIEW_SURFACE_DUPLICATE_HEADING_CLEANUP.md`

## Files changed

- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/WP_REVIEW_SURFACE_DUPLICATE_HEADING_CLEANUP.md`

## What changed

- Removed the duplicate internal `st.subheader("Controleer de tekst")` from the central side-by-side review component.
- Kept the outer app-level step heading `2. Controleer de tekst` in `presidio_streamlit.py` unchanged.
- Kept side-by-side explanatory copy directly under the step heading.
- Kept Brontekst / Verwerkte tekst panes unchanged.
- Kept marker toggle and default-on marker behavior unchanged.
- Kept synchronized scrolling behavior unchanged.

## Tests added/updated

Updated:

- `tests/test_side_by_side_review_ui_patch.py`

The test now explicitly checks that:

- the central app step heading `st.subheader("2. Controleer de tekst")` remains;
- the side-by-side component does not render its own duplicate `st.subheader("Controleer de tekst")`.

Attempted but not changed:

- `tests/test_side_by_side_review_consolidation_dutch_sample.py`; the update was blocked by the connector safety layer. The existing test remains compatible with this cleanup.

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

Expected checks:

```text
pytest tests/test_side_by_side_review_ui_patch.py
pytest tests/test_side_by_side_review_consolidation_dutch_sample.py
python -m pytest -q tests
```

## Validation status

Implemented on `main`; runtime validation pending.

## GitHub Actions status

Pending / unknown at handover time.

## Hugging Face sync status

Pending / unknown at handover time.

## App verification status

Pending and required because UI copy/layout changed.

Expected app verification:

- app starts without Script execution error;
- `2. Controleer de tekst` is visible;
- there is no second standalone `Controleer de tekst` heading inside the side-by-side component;
- Brontekst is visible on the left;
- Verwerkte tekst is visible on the right;
- Markeringen tonen is visible;
- no visible sync-scroll checkbox is shown;
- review table remains visible;
- export/download remains visible.

## Remaining risks

- Runtime UI needs coordinator app verification after Actions and Hugging Face sync.
- This cleanup does not implement review-table collapsibility.

## Next recommended step

Verify GitHub Actions and Hugging Face sync. Then request coordinator app verification screenshot.
