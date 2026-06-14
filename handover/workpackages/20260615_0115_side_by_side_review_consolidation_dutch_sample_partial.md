# Partial handover — WP_SIDE_BY_SIDE_REVIEW_CONSOLIDATION_DUTCH_SAMPLE

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_SIDE_BY_SIDE_REVIEW_CONSOLIDATION_DUTCH_SAMPLE — Consolidate preview surfaces and replace English demo text with Dutch synthetic legal text`

Status: partial only; not completed.

## What was completed

`demo_text.txt` was safely updated on `main` with a longer Dutch synthetic legal sample text.

Commit:

```text
693a630d4404da67af98339306fc7b28a51f04dd
```

The claim was updated to `in_progress_partial`.

Commit:

```text
f8e219051787699f4bd12f4b1a6ee6356fc6c734
```

## What was not completed

The UX consolidation is not implemented yet.

Still true on `main` at handover time:

- the old upper `Invoer` / `Directe voorbeeldweergave` still exists in `presidio_streamlit.py`;
- the lower side-by-side review surface still renders through `serial_review_panel_ui.py`;
- there is still more than one preview/review surface;
- tests for consolidation have not been added;
- `WORKPACKAGES.md`, `CHANGELOG.md` and `RELEASE_NOTES.md` have not been updated for completion;
- the workpackage claim is not completed.

## Important warning

A previous attempt used low-level GitHub tree/commit calls and created detached commit objects. The `main` branch was not moved to those commits, so they do not affect the app. Do not continue from those detached commits.

Continue only with small `GitHub.update_file` commits or a clean local patch workflow.

## Recommended continuation plan

1. Add/adjust tests first:
   - Dutch legal sample is present in `demo_text.txt`.
   - English demo sentence is no longer present.
   - old `Directe voorbeeldweergave` should be absent after implementation.
   - one central side-by-side review surface should be expected.
   - sync scroll and highlight toggle remain available.
   - review table remains source of truth.
   - no export/Scrub Key/reinsert behavior markers are changed.

2. Modify `serial_review_panel_ui.py`:
   - add a parameter such as `include_side_by_side: bool = True`;
   - render the side-by-side block only when that parameter is true;
   - preserve default behavior for compatibility until `presidio_streamlit.py` passes `False`.

3. Modify `presidio_streamlit.py` carefully:
   - import `render_side_by_side_review_panel`;
   - remove the old upper `Invoer` / `Directe voorbeeldweergave` two-column preview;
   - keep the input text area;
   - after default replacement rows are built and before the review table, render the central side-by-side review once;
   - call `render_serial_review_panel(..., include_side_by_side=False)` to avoid duplicate rendering;
   - do not change export/download, Scrub Key or reinsert behavior.

4. Update docs and closeout only after tests/Actions/HF/app verification.

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

## Validation status

Partial only. Demo text update is committed. UX consolidation remains open.

## GitHub Actions status

Unknown for the partial demo-text update at handover time.

## Hugging Face sync status

Unknown for the partial demo-text update at handover time.

## App verification status

Not applicable yet. UX consolidation not implemented.

## Remaining risks

- The duplicate preview problem still exists.
- If another worker assumes the package is completed, they may miss the still-open UI work.
- `presidio_streamlit.py` should be changed only in a small, reviewed patch.

## Next recommended step

Continue this same workpackage from the existing `in_progress_partial` claim, or create a clearly named repair/continue package that references this partial handover.
