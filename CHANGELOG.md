# Changelog — SolidPrivacy Scrub

## WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY — Verify Dutch legal recall pattern fixes

Status: completed after coordinator Actions/HF/app verification evidence.

Files added:

- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY.md`
- `handover/workpackages/20260617_0032_dutch_legal_recall_pattern_fixes_verify.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY.md`
- `handover/workpackages/20260617_0032_dutch_legal_recall_pattern_fixes_verify.md`

Summary:

- Confirmed prerequisite `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES` is completed.
- Verified the implementation scope by comparing the pattern-fix commit range: product/helper code change is limited to `candidate_scanner.py`; tests changed in `tests/test_dutch_legal_recall_gap_baseline.py`; no `presidio_streamlit.py` product-code change was part of the pattern-fix range.
- Verified the candidate scanner keeps the new case-number-shaped scan context-bound and value-only.
- Verified the Dutch legal recall baseline now contains normal assertions for legal references, client/dossier/zaak references, CLM reference not as phone, role-word preservation and over-masking prevention.
- Verified existing review/export contract tests still assert preservation of `replacement_editor`, download labels, side-by-side boundaries and no export/Scrub Key/reinsert mutations.
- Added coordinator verification evidence for Actions, Hugging Face sync and app flow.

Tests/checks:

- Local clone/test execution failed because the container could not resolve `github.com`.
- GitHub connector static checks and commit comparisons were completed.
- Coordinator screenshot evidence shows `Tests #1115` green for commit `e1e44b3`.
- Coordinator screenshot evidence shows `Sync to Hugging Face Space #1116` green for commit `e1e44b3`.
- Earlier `Sync to Hugging Face Space #1112` for commit `ca5cb3f` was red, but this was superseded by later successful sync evidence.

App verification:

- Coordinator app screenshot confirms the Hugging Face Space is running without Script execution error.
- Screenshot confirms `2. Controleer de tekst` and side-by-side review remain visible.
- Screenshot confirms `3. Controleer gevonden gegevens` remains visible.
- Screenshot confirms collapsed `Vervangtabel controleren — 16 items` remains visible.
- Screenshot confirms Serial review, export/download buttons and DOCX hygiene audit remain visible.

Intentionally not changed:

- No product code change in this verify package.
- No recognizer or pattern change in this verify package.
- No `presidio_streamlit.py` change.
- No UI change.
- No review table layout change.
- No side-by-side or marker change.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No DOCX/PDF flow change.
- No Docker/startup/dependency change.
- No cloud processing.
- No real personal data.

Remaining gaps:

- The first pattern-fix round improves candidate visibility; it does not prove complete automatic recognizer classification for every Dutch legal reference type.
- Broader recall/precision scorecard and gold-label corpus work remain future work.

Next recommended step:

- Do not automatically continue into another pattern round.
- No immediate extra pattern round is required based on current coordinator verification evidence.
- If remaining gaps appear in later app/user testing, consider `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2` after separate approval.

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

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY — verified promoted collapsible review table.
- WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS — contract tests for collapsible review table section.
- WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR — repaired stale review surface control assertions.
- WP_REVIEW_SURFACE_CONTROL_CLEANUP — simplified side-by-side review controls.
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
