# Handover — SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_IMPLEMENTATION

Repository: solidprivacy-nl/scrub  
Status: completed and app-verified

## Summary

Implemented and verified the first visible Basiscontrole / Expertcontrole split in the central side-by-side review surface. The selector defaults to `Basiscontrole` and stores UI state in `solidprivacy_review_mode`. The implementation is intentionally visibility-only: it does not change processing, replacement, export, Scrub Key, reinsert, recognizer, benchmark, runtime/startup or dependency semantics.

This is a restrained first implementation. It introduces the user-facing mode selector and explanatory copy. Deeper restructuring of all downstream secondary controls should remain a separate follow-up package.

## Files added

- `tests/test_basic_expert_review_mode_implementation.py`
- `handover/workpackages/20260703_0000_basic_expert_review_mode_implementation.md`

## Files changed

- `side_by_side_review_panel_ui.py`
- `workpackage_claims/scrub_wp_basic_expert_review_mode_implementation.md`

## Tests / checks

Added source-level implementation tests covering:

- visible `Basiscontrole` / `Expertcontrole` selector;
- default `Basiscontrole` index;
- session-state key `solidprivacy_review_mode`;
- visibility-only boundaries;
- Basic and Expert explanatory copy;
- side-by-side review and markers remain primary;
- existing processing/export/Scrub Key/reinsert paths remain present in app source;
- contract tests remain guardrail;
- no prohibited cloud/AI/OCR/restored-PDF/PDF-to-DOCX/click-to-mark/advanced-editor/full-document-marking/hidden-export-gate behavior added by the review-mode UI helper.

Validation evidence:

- PR #17 Tests passed.
- PR #17 merged to `main`.
- Hugging Face sync completed sufficiently for live Space verification.
- Coordinator live app screenshots verified the UI.

No manual full-suite run was performed in this connector session.

## Validation

- GitHub Actions: green for PR #17.
- Hugging Face sync: completed sufficiently for live Space verification.
- App verification: passed by coordinator screenshots.

## App verification evidence

Coordinator screenshots confirmed:

- App starts without Script execution error.
- `Controleweergave` is visible.
- `Basiscontrole` / `Expertcontrole` selector is visible.
- `Basiscontrole` is selected by default.
- `Expertcontrole` can be selected.
- Side-by-side review remains visible in both modes.
- `Markeringen tonen` remains visible.
- Manual missed-value entry remains reachable.
- Replacement table remains reachable.
- Scrub Key, document downloads, audit files, technical details and DOCX hygiene audit remain available.
- No visible export, Scrub Key, reinsert or recognizer regression observed in the verified path.

## Documentation sync note

A release-notes update was attempted but blocked by the connector safety layer during full-file replacement. Status is recorded in this handover and the claim file.

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

- This first implementation introduces the mode selector but does not yet fully restructure every downstream secondary control into separate Basic/Expert layouts.
- A deeper Basic-mode decluttering package should be separate and contract-tested.

## Next recommended step

Start a follow-up package to make Basiscontrole materially cleaner by moving lower-priority secondary controls behind a smaller `Details aanpassen` / `Meer bestanden` structure while keeping Expertcontrole fully available.
