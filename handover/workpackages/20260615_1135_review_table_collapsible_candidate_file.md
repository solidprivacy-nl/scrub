# Handover — WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE — Create inactive candidate file for collapsible review table`

Status: completed as inactive candidate file; active app file unchanged.

## Purpose

The coordinator asked for a candidate copy that can be manually promoted after the direct runtime implementation was blocked by safe full-file edit constraints.

This package creates a candidate file without changing active `presidio_streamlit.py`.

## Files added

- `presidio_streamlit_collapsible_candidate.py`
- `tests/test_review_table_collapsible_candidate_file.py`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE.md`
- `handover/workpackages/20260615_1135_review_table_collapsible_candidate_file.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE.md`

## Implementation summary

`presidio_streamlit_collapsible_candidate.py` is an inactive candidate app file.

It keeps `3. Controleer gevonden gegevens` visible and places the editable review table in a collapsed Streamlit expander labelled `Vervangtabel controleren — {item_count} items`.

The candidate keeps the existing review-table source-of-truth role and preserves:

- `replacement_editor`
- `include`
- `remember`
- `find`
- `replace_with`
- `Meenemen`
- `Onthouden`
- `Gevonden tekst`
- `Vervangen door`

The active app file `presidio_streamlit.py` was not changed.

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

Static candidate tests were added in `tests/test_review_table_collapsible_candidate_file.py`.

Expected checks for a full worker/local environment:

- `python -m py_compile presidio_streamlit_collapsible_candidate.py`
- `pytest tests/test_review_table_collapsible_candidate_file.py`
- `pytest tests/test_review_table_collapsible_contract.py`
- `pytest tests/test_side_by_side_review_ui_patch.py`
- `pytest tests/test_side_by_side_review_consolidation_dutch_sample.py`
- `python -m pytest -q tests`

After manual promotion to active app file, run `python -m py_compile presidio_streamlit.py` and the targeted pytest checks again.

## Validation status

Static validation only through file creation and candidate contract-test content.

No runtime validation has been performed.

## GitHub Actions status

Pending / unknown at handover time.

## Hugging Face sync status

Pending / unknown at handover time.

Because the candidate file is inactive, Hugging Face app behavior should remain unchanged unless the candidate is manually promoted.

## App verification status

Not applicable for active app yet.

App verification is required only after manual promotion, and should confirm:

- app starts without Script execution error;
- `2. Controleer de tekst` remains visible;
- side-by-side review remains visible;
- `Markeringen tonen` remains visible;
- no duplicate `Controleer de tekst` heading;
- `3. Controleer gevonden gegevens` remains visible;
- review table is collapsed or visually quieter;
- review table opens and shows required columns;
- export/download remains visible;
- DOCX hygiene audit remains visible.

## Manual promotion instructions

Use a branch or local clone. Do not promote directly to main without a backup.

Recommended manual flow:

1. Back up the active `presidio_streamlit.py`.
2. Copy `presidio_streamlit_collapsible_candidate.py` to `presidio_streamlit.py`.
3. Compile the active app file.
4. Run the targeted pytest checks.
5. Run the app and verify the UI.

## Remaining risks

- Candidate file has not been executed in the Hugging Face runtime.
- The active app is unchanged until manual promotion.
- Existing startup compatibility patches may still run when the candidate is promoted to `presidio_streamlit.py`; this must be checked in the promoted branch/local test.
- `review_table_collapsible_ui.py` remains as a non-runtime helper artifact from the earlier blocked takeover and is not used by the active app.

## Next recommended step

1. Wait for GitHub Actions on this candidate-file package.
2. If green, manually promote the candidate on a branch/local clone.
3. Run targeted tests and app verification.
4. If successful, close out with a separate verify/promote package.
