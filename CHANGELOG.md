# Changelog — SolidPrivacy Scrub

## WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE — Inactive candidate file for collapsible review table

Status: completed as inactive candidate file; active app file unchanged.

Files added:

- `presidio_streamlit_collapsible_candidate.py`
- `tests/test_review_table_collapsible_candidate_file.py`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE.md`
- `handover/workpackages/20260615_1135_review_table_collapsible_candidate_file.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE.md`

Summary:

- Added a manually renameable candidate app file for testing a collapsible `Controleer gevonden gegevens` review table section.
- The active `presidio_streamlit.py` was not changed.
- The candidate keeps `3. Controleer gevonden gegevens` visible and places the editable `replacement_editor` table in a collapsed `Vervangtabel controleren — {item_count} items` expander.
- The candidate preserves `replacement_editor`, include, remember, find, replace_with and the Dutch table labels.
- Added static candidate-file contract tests to confirm the candidate exists, keeps the review table controls and preserves download labels.

Validation status:

- No shell/pytest execution was available through the ChatGPT GitHub connector.
- Expected targeted checks: `pytest tests/test_review_table_collapsible_candidate_file.py`; `pytest tests/test_review_table_collapsible_contract.py`; `pytest tests/test_side_by_side_review_ui_patch.py`; `pytest tests/test_side_by_side_review_consolidation_dutch_sample.py`.
- Expected compile check after manual promotion: `python -m py_compile presidio_streamlit.py`.

Important boundary:

- This is not yet a live app implementation.
- Manual promotion must happen on a branch or local clone by renaming the candidate file to `presidio_streamlit.py` after backing up the active file.
- Do not promote directly to main without a reversible backup/branch and tests.

## WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION — Takeover attempt blocked/released

Status: blocked/released after coordinator-approved takeover attempt.

Files added:

- `review_table_collapsible_ui.py`
- `handover/workpackages/20260615_1115_review_table_collapsible_implementation_takeover_blocked.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION.md`

Summary:

- The coordinator could not find the original active worker and approved a takeover attempt.
- The existing claim was reused and then released as blocked rather than creating a duplicate claim.
- The required safe implementation still needs a direct `presidio_streamlit.py` review-table patch.
- The ChatGPT GitHub connector could not safely complete that central full-file UI edit without risking an unsafe overwrite or hidden startup/monkeypatch behavior.
- A small helper artifact was added but is not wired into production UI.
- No runtime UI implementation was completed.

Next recommended step:

- Use the inactive candidate file for manual branch/local testing, or re-run the active implementation with a safe full-file edit environment.
- Do not use startup source mutation, global monkeypatching or hidden side effects for this UI change.

## WP_REVIEW_SURFACE_DUPLICATE_HEADING_CLEANUP — Remove duplicate central review heading

Status: completed after Actions/HF/app verification by coordinator screenshot evidence.

Files changed:

- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_SURFACE_DUPLICATE_HEADING_CLEANUP.md`

Files added:

- `handover/workpackages/20260615_0420_review_surface_duplicate_heading_cleanup.md`

Summary:

- Removed the internal `st.subheader("Controleer de tekst")` from the side-by-side review component.
- The outer app-level step heading `2. Controleer de tekst` remains the single heading for the review surface.
- The side-by-side explanatory copy still appears directly under the step heading.
- Brontekst, Verwerkte tekst, marker toggle and synchronized-scroll behavior are unchanged.
- Review table, export/download, Scrub Key, reinsert and replacement behavior are unchanged.

Validation status:

- Coordinator screenshot evidence showed green Tests and green Sync to Hugging Face Space for the duplicate heading cleanup claim.
- Coordinator app screenshot confirmed that only one `Controleer de tekst` heading appears above the side-by-side review surface.

Intentionally not changed:

- No `presidio_streamlit.py` change.
- No review table behavior change.
- No side-by-side functionality change.
- No marker logic change.
- No sync-scroll behavior change.
- No replacement behavior change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No click-to-mark.
- No advanced editor.
- No full-document marking.

## WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS — Contract tests for collapsible review table section

Status: completed after Actions/HF verification.

Files added:

- `REVIEW_TABLE_COLLAPSIBLE_CONTRACT.md`
- `tests/test_review_table_collapsible_contract.py`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS.md`
- `handover/workpackages/20260615_0230_review_table_collapsible_contract_tests.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS.md`
- `handover/workpackages/20260615_0230_review_table_collapsible_contract_tests.md`

Summary:

- Added documentation and contract tests for a future collapsible `Controleer gevonden gegevens` review table section.
- Locked the future heading shape `Controleer gevonden gegevens — {item_count} items`.
- Preserved the review table as source of truth and fallback.
- Contract tests verify that `replacement_editor`, `include`, `remember`, `find` and `replace_with` remain available.
- Contract tests verify that export/download labels remain present.
- Explicitly blocks export/download changes, export blocking, Scrub Key changes, reinsert changes, replacement behavior changes, click-to-mark, advanced editor and full-document marking.
- No production UI implementation was added.

Validation status:

- Earlier `Tests #1031` failed on stale review-surface assertions expecting old highlight label and visible `syncToggle`; this was outside the collapsible-contract package.
- `WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR` repaired those stale assertions.
- Coordinator screenshot evidence confirmed `Tests #1041` green and `Sync to Hugging Face Space #1053` green for commit `143a0fa`.

Next recommended step:

- `WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION` may start after coordinator approval, but must use a safe direct full-file/branch patch route.
- The implementation package must not run in parallel with other `presidio_streamlit.py` review-flow changes.

## WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR — Repair stale review surface control assertions

Status: completed after Actions/HF verification.

Summary:

- Repaired stale test assertions after the review surface control cleanup.
- Updated highlight-toggle contract expectations from `Markeringen tonen in verwerkte tekst` to the accepted shorter label `Markeringen tonen`.
- Updated sync-scroll production assertions to reflect D023: synchronized scrolling is active by default and no visible `syncToggle` checkbox exists in the production side-by-side renderer.
- Coordinator screenshot evidence confirmed `Tests #1041` green and `Sync to Hugging Face Space #1053` green for commit `143a0fa`.

## WP_REVIEW_SURFACE_CONTROL_CLEANUP — Simplify side-by-side review controls

Status: implemented; awaiting Actions, Hugging Face sync and app verification.

Summary:

- Marker toggle label shortened to `Markeringen tonen`.
- Marker toggle now defaults to on.
- Visible sync-scroll checkbox removed from the central side-by-side component.
- Synchronized scrolling remains active by default.
- A short sync-scroll explanation remains visible below the panes.
- Tests updated for the simplified control model.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_SIDE_BY_SIDE_REVIEW_CONSOLIDATION_DUTCH_SAMPLE — Consolidate preview surfaces and Dutch legal sample.
- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION — Production integration of synchronized side-by-side scrolling.
- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE — isolated working concept for synchronized side-by-side scrolling.
- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY — closeout/app verification for side-by-side review implementation.
- WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY — feasibility review for synchronized side-by-side scrolling.
- WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — equal-height side-by-side review panes.
- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — bounded Streamlit side-by-side review surface.
- WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — helper-only model for source/processed review panes.
- WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — contract tests for unified side-by-side review UX.
- WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — contract tests for intuitive replacement review redesign.
- WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — simple masked-text highlight toggle implementation.
- WP39D — DOCX hygiene audit UI implementation.
