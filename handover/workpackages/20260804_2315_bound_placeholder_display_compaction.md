# Handover — SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION

Repository worked in: `solidprivacy-nl/scrub`
Workpackage title: Compact document-bound placeholders in review display
Status: completed; deployment synchronization and live app verification green

## Summary

Implemented a display-only compaction layer for strict schema-1.1 bound placeholders. The review UI now presents short aliases while retaining the complete source token, 80-bit document binding and exact UTF-16 offsets. Automatic placeholders display as `[LABEL_INDEX]`; manual selection placeholders display as `[LABEL_H_INDEX]`.

The interactive component renders source-backed segments and maps browser selections back to the unchanged processed text. Compact placeholders remain protected even with visual markers hidden. The static fallback uses the same strict, escaped display contract. Legacy, malformed and free replacement text remain unchanged.

## Files added

- `BOUND_PLACEHOLDER_DISPLAY_COMPACTION.md`
- `bound_placeholder_display.py`
- `tests/test_bound_placeholder_display.py`
- `tests/test_bound_placeholder_display_ui_integration.py`
- `tests/frontend/bound_placeholder_display.test.js`
- `workpackage_claims/scrub_wp_bound_placeholder_display_compaction.md`
- `handover/workpackages/20260804_2315_bound_placeholder_display_compaction.md`

## Files changed

- `frontend/processed_text_selection_component/component_core.js`
- `frontend/processed_text_selection_component/component.js`
- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

## Tests

New and updated tests cover:

- strict automatic and manual compact aliases;
- no rewrite of legacy, malformed or free values;
- complete source reconstruction from display segments;
- exact UTF-16 source offsets, including text after compact tokens;
- selection mapping within and after compact tokens;
- protected placeholder spans when visual markers are hidden;
- complete source token and hash retained in component arguments;
- escaped static fallback parity and full-token hover/accessibility metadata;
- explicit no-change declarations for binding entropy and key semantics.

## Validation status

- Dedicated frontend display tests passed.
- Existing processed-text component frontend tests passed.
- Standard PR run #2076: 1155 Python tests passed in 11.62s.
- Finalization workflow: both frontend suites passed and 1155 tests passed in 10.73s.
- Final standard merge-candidate run #2080: 1155 tests passed in 12.44s.
- Independent deployment run #2082: 4/4 runtime files exact, health `ok`, root HTTP 200, frontend tests passed and 1155 tests passed in 11.49s.
- Coordinator/user app verification confirmed shorter replacement codes are visible and working.

## GitHub Actions status

Green through final merge-candidate run #2080 and independent deployment run #2082.

## Hugging Face sync status

Green; 4/4 changed runtime files matched Hugging Face byte-for-byte in run #2082.

## App verification status

Confirmed by coordinator/user at 2026-08-05 10:49 Europe/Amsterdam.

## Remaining risks

- Live browser behavior must confirm compact aliases render consistently and direct selection after them still targets the correct full source offsets.
- Downloaded scrubbed documents must be checked to contain full bound tokens rather than compact aliases.
- Scrub Key validation and reinsert must be checked against those full exported tokens.
- The full token is available in hover/accessibility metadata; this is non-sensitive but should not create visual clutter.
- Cross-browser Edge, Chrome and Firefox behavior remains part of later broader validation.
- Human review remains mandatory; no production-readiness claim is made.

## Next recommended step

Merge only after the final standard PR regression is green. Then verify GitHub-to-Hugging-Face synchronization and perform focused app verification of compact aliases, marker-off behavior, direct selection after a compact token, full-token export and successful reinsert. Continue cross-flow regression only after that gate is green.
