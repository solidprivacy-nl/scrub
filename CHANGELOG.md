# Changelog — SolidPrivacy Scrub

## WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES — Improve Dutch legal reference detection

Status: completed as a targeted helper-level detection improvement.

Files changed:

- `candidate_scanner.py`
- `tests/test_dutch_legal_recall_gap_baseline.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES.md`
- `handover/workpackages/20260616_2211_dutch_legal_recall_pattern_fixes.md`

Summary:

- Improved the Dutch Legal candidate scanner for reference-like values that should be surfaced in the review/replacement table when recognizers miss them.
- Added context-bound case-number scanning for values with spaces, including numeric court role references and `ARN 26/4412`-style references.
- Broadened safe context cues for `client`, `cliënt`, `camera`, `incident`, `reparatie`, `rolnummer` and `rolnr`.
- Converted the Dutch legal recall baseline from `xfail(strict=False)` gap documentation to direct helper-level passing assertions for the first fixed round.
- Kept role-word preservation tests for `slachtoffer`, `arts`, `getuige`, `eiser`, `verweerder` and `minderjarige`.

Validation status:

- Local tests were attempted but could not run in this environment because the container still cannot resolve `github.com` for a local clone.
- GitHub Actions/Hugging Face sync must be used as final execution proof.

Intentionally not changed:

- No `presidio_streamlit.py` change.
- No UI change.
- No review-table layout change.
- No side-by-side or marker change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No placeholder-format change.
- No Docker/startup/dependency change.
- No cloud processing.
- No real personal data.
- No broad refactor.

Next recommended step:

- Do not automatically continue into another pattern round.
- Recommended next package after separate coordinator approval: `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY`.

## WP_DUTCH_LEGAL_RECALL_GAP_TESTS — Add tests for known Dutch legal recall gaps

Status: completed as tests/documentation-only baseline.

Files added:

- `tests/test_dutch_legal_recall_gap_baseline.py`
- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_GAP_TESTS.md`
- `handover/workpackages/20260616_2209_dutch_legal_recall_gap_tests.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_GAP_TESTS.md`

Summary:

- Added a tests-only baseline for known Dutch legal recall and precision gaps.
- Used synthetic legal text only.
- Captured known gaps for legal reference numbers, Rechtspraak-like rolnummers, client/dossier/zaak numbers, legal-code misclassification, role-word preservation and over-masking risk.
- Used `pytest.mark.xfail(..., strict=False)` for current known gaps so CI can remain green while the shortcomings stay visible.
- Added two normal fixture coverage tests for the synthetic legal-reference and role-word baselines.

Validation status:

- Local shell/pytest execution was not available in this environment because GitHub access from the container is restricted; connector/static checks verified the added file content.
- GitHub Actions/Hugging Face sync should be used as the source of truth for final test execution.

Intentionally not changed:

- No product code change.
- No `presidio_streamlit.py` change.
- No recognizer or pattern fix.
- No UI change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No placeholder-format change.
- No Docker/startup/dependency change.
- No cloud processing.
- No real personal data.

Next recommended step:

- Do not automatically start recognizer fixes.
- Likely next package after separate coordinator approval: `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES`.

## WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP — Remove temporary candidate artifacts

Status: completed as repo-hygiene cleanup after verified promotion.

Files removed:

- `presidio_streamlit_collapsible_candidate.py`
- `tests/test_review_table_collapsible_candidate_file.py`
- `review_table_collapsible_ui.py`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP.md`
- `handover/workpackages/20260616_2108_review_table_collapsible_artifact_cleanup.md`

Summary:

- Removed temporary candidate/helper files after the collapsible review table was promoted, tested and app-verified.
- Active app behavior is unchanged.
- The collapsible review-table behavior remains in `presidio_streamlit.py`.
- The active app still keeps `3. Controleer gevonden gegevens` visible and places the editable table under `Vervangtabel controleren — <items> items` with `expanded=False`.
- Review table source-of-truth controls remain preserved: `include`, `remember`, `find`, `replace_with`, `Meenemen`, `Onthouden`, `Gevonden tekst`, `Vervangen door`.

Validation status:

- GitHub contents check confirmed the temporary files were present before cleanup and removed afterward.
- Active `presidio_streamlit.py` was not changed in this package.
- Local shell/pytest execution was not available in this environment because the repository could not be cloned from GitHub due DNS/network restriction; GitHub Actions/Hugging Face sync were checked from GitHub after push where connector visibility allowed.

Intentionally not changed:

- No `presidio_streamlit.py` change.
- No active Streamlit UI change.
- No review table behavior change.
- No side-by-side behavior change.
- No marker/sync-scroll behavior change.
- No replacement behavior change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No Docker CMD change.
- No startup patch.
- No monkeypatch.
- No dependency change.
- No cloud processing.
- No real data.

Next recommended step:

- Do not start a new review-UX feature automatically.
- Coordinator can separately choose detection/recall gap tests, serial review compacting, or temporary review-UX freeze with recall/document hygiene focus.

## WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY — Promoted and verified collapsible review table

Status: completed after coordinator promotion, local test evidence, GitHub Actions evidence and app verification screenshot.

Files added:

- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY.md`
- `handover/workpackages/20260615_1210_review_table_collapsible_promote_verify.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY.md`

Summary:

- Verified that the previously inactive collapsible review-table candidate has been promoted into the live app.
- Verified active `presidio_streamlit.py` now keeps `3. Controleer gevonden gegevens` visible while the editable replacement table sits in a collapsed `Vervangtabel controleren — {items} items` expander.
- Verified the expander uses `expanded=False` and preserves `key="replacement_editor"`.
- Verified required review-table fields and labels remain present: `include`, `remember`, `find`, `replace_with`, `Meenemen`, `Onthouden`, `Gevonden tekst`, `Vervangen door`.
- Verified export/download labels remain present.
- Recorded coordinator app verification showing side-by-side review, marker toggle, collapsed review table, serial review, export/download and DOCX hygiene audit remain visible without Script execution error.

Evidence:

- Branch used by coordinator: `test/collapsible-review-table`.
- Promotion commit: `15f5173c893668566e9d62524ef4d0b5449f37b8` — `Promote collapsible review table candidate`.
- GitHub Actions: `Tests #1074` completed successfully for the promotion commit.
- Coordinator local checks:
  - `python -m py_compile presidio_streamlit.py`
  - `python -m pytest -q tests/test_review_table_collapsible_candidate_file.py` — 5 passed
  - `python -m pytest -q tests/test_review_table_collapsible_contract.py` — 11 passed
  - `python -m pytest -q tests/test_side_by_side_review_ui_patch.py` — 15 passed
  - `python -m pytest -q tests/test_side_by_side_review_consolidation_dutch_sample.py` — 7 passed
  - `python -m pytest -q tests` — 545 passed
- Coordinator app verification screenshot confirms the live app shows collapsed `Vervangtabel controleren — 16 items` while the rest of the review/export flow remains visible.

Validation status:

- Completed/app-verified by coordinator evidence.
- No new product UI was built in this verification package.

Intentionally not changed:

- No `presidio_streamlit.py` change in this verification package.
- No review table behavior change in this verification package.
- No side-by-side behavior change.
- No marker/sync-scroll behavior change.
- No replacement behavior change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No startup patch.
- No Docker CMD change.
- No monkeypatch.
- No dependency change.
- No cloud processing.
- No real data.
- No click-to-mark, advanced editor or full-document marking.

Next recommended step:

- Do not start a new feature automatically.
- Possible next UX step only after separate coordinator approval: make Serial review compacter/collapsible.
- Alternative: freeze review UX temporarily and return to detection/recall issues.

## WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE — Inactive candidate file for collapsible review table

Status: completed as inactive candidate file and later promoted through `WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY`.

Summary:

- Added a manually renameable candidate app file for testing a collapsible `Controleer gevonden gegevens` review table section.
- The candidate kept `3. Controleer gevonden gegevens` visible and placed the editable `replacement_editor` table in a collapsed `Vervangtabel controleren — {item_count} items` expander.
- The candidate preserved `replacement_editor`, include, remember, find, replace_with and the Dutch table labels.
- Static candidate-file contract tests confirmed the candidate existed, kept the review table controls and preserved download labels.
- The candidate was later promoted and verified by coordinator evidence.
- The temporary candidate file and its static candidate-file test were removed by `WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP` after verified promotion.

## WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION — Takeover attempt blocked/released

Status: superseded by candidate promotion/verification route.

Summary:

- The coordinator could not find the original active worker and approved a takeover attempt.
- The existing claim was reused and then released as blocked rather than creating a duplicate claim.
- The ChatGPT GitHub connector could not safely complete that central full-file UI edit without risking an unsafe overwrite or hidden startup/monkeypatch behavior.
- A small helper artifact was added but was not wired into production UI.
- The later candidate-file route and coordinator promotion verified the collapsible review table in the live app.
- The temporary helper artifact was removed by `WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP` after verified promotion.

## WP_REVIEW_SURFACE_DUPLICATE_HEADING_CLEANUP — Remove duplicate central review heading

Status: completed after Actions/HF/app verification by coordinator screenshot evidence.

Summary:

- Removed the internal `st.subheader("Controleer de tekst")` from the side-by-side review component.
- The outer app-level step heading `2. Controleer de tekst` remains the single heading for the review surface.
- The side-by-side explanatory copy still appears directly under the step heading.
- Brontekst, Verwerkte tekst, marker toggle and synchronized-scroll behavior are unchanged.
- Review table, export/download, Scrub Key, reinsert and replacement behavior are unchanged.

## WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS — Contract tests for collapsible review table section

Status: completed after Actions/HF verification.

Summary:

- Added documentation and contract tests for a future collapsible `Controleer gevonden gegevens` review table section.
- Locked the future heading shape `Controleer gevonden gegevens — {item_count} items`.
- Preserved the review table as source of truth and fallback.
- Contract tests verify that `replacement_editor`, `include`, `remember`, `find` and `replace_with` remain available.
- Contract tests verify that export/download labels remain present.
- Explicitly blocks export/download changes, export blocking, Scrub Key changes, reinsert changes, replacement behavior changes, click-to-mark, advanced editor and full-document marking.

## WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR — Repair stale review surface control assertions

Status: completed after Actions/HF verification.

Summary:

- Repaired stale test assertions after the review surface control cleanup.
- Updated highlight-toggle contract expectations from `Markeringen tonen in verwerkte tekst` to the accepted shorter label `Markeringen tonen`.
- Updated sync-scroll production assertions to reflect D023: synchronized scrolling is active by default and no visible `syncToggle` checkbox exists in the production side-by-side renderer.
- Coordinator screenshot evidence confirmed `Tests #1041` green and `Sync to Hugging Face Space #1053` green for commit `143a0fa`.

## WP_REVIEW_SURFACE_CONTROL_CLEANUP — Simplify side-by-side review controls

Status: completed after later verification evidence.

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
