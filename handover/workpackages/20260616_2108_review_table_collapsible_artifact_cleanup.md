# Handover — WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP — Remove temporary collapsible review table candidate artifacts after verified promotion`

Status: completed; temporary candidate/helper artifacts removed after verified promotion. Active app behavior unchanged.

## Summary

Removed the temporary collapsible review-table candidate/helper artifacts that were no longer needed after the promoted app behavior was verified. The active implementation remains in `presidio_streamlit.py`; this package did not edit product UI, review behavior, export/download, Scrub Key, reinsert, startup, Docker or dependencies.

## Files removed

- `presidio_streamlit_collapsible_candidate.py`
- `tests/test_review_table_collapsible_candidate_file.py`
- `review_table_collapsible_ui.py`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP.md` pending final closeout update after this handover file

## Files added

- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP.md`
- `handover/workpackages/20260616_2108_review_table_collapsible_artifact_cleanup.md`

## Tests / checks run

Required local shell commands requested by the workpackage:

```text
python -m py_compile presidio_streamlit.py
python -m pytest -q tests/test_review_table_collapsible_contract.py
python -m pytest -q tests/test_side_by_side_review_ui_patch.py
python -m pytest -q tests/test_side_by_side_review_consolidation_dutch_sample.py
python -m pytest -q tests
```

Result: not runnable in this environment. Attempted to clone `https://github.com/solidprivacy-nl/scrub.git` locally, but the container returned `Could not resolve host: github.com`. No local pytest execution was therefore possible.

Static repository checks completed through the GitHub connector:

- Confirmed the cleanup claim did not exist before starting, then created it.
- Read the required control files: `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Read the required review/promote evidence files: `RELEASE_NOTES.md`, `RISK_REGISTER.md`, `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY.md`, `handover/workpackages/20260615_1210_review_table_collapsible_promote_verify.md`.
- Read the temporary artifacts before deletion: `presidio_streamlit_collapsible_candidate.py`, `review_table_collapsible_ui.py`, `tests/test_review_table_collapsible_candidate_file.py`.
- Read `tests/test_review_table_collapsible_contract.py`.
- Checked active `presidio_streamlit.py` still contains the promoted review-table implementation.
- Confirmed removed files now return 404 through `fetch_file`:
  - `presidio_streamlit_collapsible_candidate.py`
  - `tests/test_review_table_collapsible_candidate_file.py`
  - `review_table_collapsible_ui.py`

## Active app validation

Active `presidio_streamlit.py` was not changed.

Confirmed the active file still contains:

- `st.subheader("3. Controleer gevonden gegevens")`
- `Vervangtabel controleren`
- `expanded=False`
- `key="replacement_editor"`
- `include`
- `remember`
- `find`
- `replace_with`
- `Meenemen`
- `Onthouden`
- `Gevonden tekst`
- `Vervangen door`

Validation status: cleanup completed; active review-table behavior remains in `presidio_streamlit.py`; removed artifacts are no longer present.

## GitHub Actions status

Connector status: unknown / not exposed.

Details:

- `get_commit_combined_status` for cleanup documentation commit `0ccbe9972175359f8b5824dfffd877417c59a54f` returned no statuses.
- `fetch_commit_workflow_runs` returned an empty workflow run list for the cleanup commits checked.
- The connector documentation notes that commit workflow-run lookup may filter to pull-request-triggered runs, so push-triggered Actions may not be visible through this tool.

## Hugging Face sync status

Connector status: unknown / not exposed for this cleanup commit.

Expected app impact: no visible app change because active product code was not changed and only unused candidate/helper artifacts were removed.

## App verification status

Not required by scope unless Actions/Hugging Face showed unexpected behavior. No app behavior was intentionally changed.

Previous promoted UI app verification remains the source of truth for the live collapsible review table:

- `WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY`
- coordinator screenshot showed collapsed `Vervangtabel controleren — 16 items`, no Script execution error, side-by-side review, serial review, export/download and DOCX hygiene audit visible.

## Remaining risks

- Local pytest could not be run from this environment due GitHub DNS/network restriction in the container.
- GitHub Actions and Hugging Face sync were not visible through the connector for the cleanup commits.
- Existing product risks remain unchanged: detection/recall gaps, document hygiene gaps and review UX limits.
- The top docstring in active `presidio_streamlit.py` still describes a candidate copy, but this package was explicitly forbidden from editing `presidio_streamlit.py`; no product code cleanup was attempted.

## Next recommended step

Do not start a new review-UX feature automatically.

The review-table-collapsible line is now cleanup-complete. Next content direction requires separate coordinator choice:

- detection/recall gap tests for Dutch legal recognition;
- or serial review compacter/collapsible;
- or freeze review UX temporarily and return to recall/document hygiene.
