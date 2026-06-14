# Changelog — SolidPrivacy Scrub

## WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY — Closeout/app verification for side-by-side review implementation

Status: completed verification/documentation-only closeout; no product code or UI code changed.

Files added:

- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY.md`
- `handover/workpackages/20260615_0015_side_by_side_review_implementation_verify.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY.md`

Summary:

- Closed out the first bounded side-by-side review implementation after coordinator evidence.
- Confirmed GitHub Actions green and Sync to Hugging Face Space green for the side-by-side/height/sync-scroll documentation sequence.
- Confirmed app screenshot evidence: side-by-side review visible, highlights visible, equal pane height visible, local processed-pane scrolling visible.
- Recorded that synchronized scroll is intentionally not implemented and is not a bug.
- Recorded the current MVP baseline as equal-height independent panes.

Validation status:

- Verification/documentation-only package.
- No shell/pytest execution was performed through the ChatGPT GitHub connector.
- Coordinator screenshots provided validation evidence for Actions, Hugging Face sync and app behavior.

Intentionally not changed:

- No product code.
- No UI code.
- No tests.
- No synchronized scroll implementation.
- No custom Streamlit component.
- No JavaScript injection.
- No review table behavior change.
- No replacement behavior change.
- No Scrub Key behavior change.
- No export/download behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real data.

Next recommended step:

- Continue MVP workflow simplification through separately approved packages.
- If synchronized scroll is still desired later: `WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_CONTRACT_TESTS` before any spike.

## WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY — Feasibility review for synchronized side-by-side scrolling

Status: completed documentation-only feasibility review; no implementation or runtime behavior changed.

Summary:

- Reviewed whether synchronized scrolling should be added to the side-by-side review surface.
- Recorded that synchronized scrolling is attractive for long-document comparison but risky because source and processed text are not guaranteed to align line-by-line or by scroll percentage after masking/replacement.
- Compared independent scroll panes, percentage-based custom component sync, anchor-based sync and selected-item focus.
- Recommended keeping equal-height independent panes as the MVP baseline.
- Recommended not implementing synchronized scroll in the current Streamlit MVP flow.
- Recommended contract tests and a separate approved spike only if the coordinator later still wants synchronized scroll.

## WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — Equal-height side-by-side review panes

Status: completed after Actions/HF/app verification.

Summary:

- Added a shared pane-height constant for the side-by-side review panes.
- The source text area and processed text area now use the same height value.
- The highlighted processed pane now has fixed height, max-height, min-height and local `overflow-y: auto` scrolling.
- This is not synchronized scrolling.
- No custom Streamlit component was added.

## WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — Small unified source/processed review surface

Status: completed after Actions/HF/app verification.

Summary:

- Added a bounded Streamlit side-by-side review surface in the existing review flow.
- The new visible section is `Controleer de tekst`.
- The left pane shows `Brontekst`.
- The right pane shows `Verwerkte tekst`.
- The `Markeringen tonen in verwerkte tekst` toggle is integrated into the right processed pane.
- Markers remain visual-only and do not change source text, review table state, export payloads, Scrub Key state or reinsert behavior.
- The review table remains source of truth and fallback.
- Serial review remains visible below the side-by-side surface.
- The old separate highlight-preview call was removed from `serial_review_panel_ui.py`; legacy highlight helper assets remain available for compatibility.
- The new panel avoids repeated visible per-highlight labels and uses one compact legend instead.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_ACTIONS_FIX — narrow test/wording repair after side-by-side implementation.
- WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — helper-only model for source/processed review panes.
- WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS_ACTIONS_FIX — contract wording repair.
- WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS — contract tests for unified side-by-side review UX.
- WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN — detailed plan for unified source/processed review surface.
- WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS — contract tests for intuitive replacement review redesign.
- WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR — unified side-by-side review UX direction.
- WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — closeout/app verification for hidden replacement helper panel.
- WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — simple masked-text highlight toggle implementation.
- WP39D — DOCX hygiene audit UI implementation.
