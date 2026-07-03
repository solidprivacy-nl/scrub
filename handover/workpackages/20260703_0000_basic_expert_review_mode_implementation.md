# Handover — SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_IMPLEMENTATION

Repository: solidprivacy-nl/scrub  
Status: implemented / PR validation pending

## Summary

Implemented the first visible Basiscontrole / Expertcontrole split in the central side-by-side review surface. The selector defaults to `Basiscontrole` and stores UI state in `solidprivacy_review_mode`. The implementation is intentionally visibility-only: it does not change processing, replacement, export, Scrub Key, reinsert, recognizer, benchmark, runtime/startup or dependency semantics.

This is a restrained first implementation. It introduces the user-facing mode selector and explanatory copy. Deeper restructuring of all downstream secondary controls should remain a separate follow-up package if needed.

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

Targeted validation expected in PR/GitHub Actions:

```text
python -m pytest -q tests/test_basic_expert_review_mode_contracts.py tests/test_basic_expert_review_mode_implementation.py
python -m pytest -q tests/test_review_surface_simplification_implementation.py tests/test_side_by_side_review_ui_patch.py tests/test_review_copy_polish_ui.py
```

No manual full-suite run was performed in this connector session.

## Validation

- GitHub Actions: pending after PR.
- Hugging Face sync: pending after merge.
- App verification: required after merge/sync because visible UI behavior changed.

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

- PR validation still needs to complete.
- Live app verification is required after Actions and Hugging Face sync are green.
- This first implementation introduces the mode selector but does not yet fully restructure every downstream secondary control into separate Basic/Expert layouts.

## Next recommended step

Open PR and validate. If green, merge, verify Hugging Face sync, then ask the coordinator for live app verification around `2. Controleer resultaat`:

```text
1. App starts without Script execution error.
2. `Basiscontrole` / `Expertcontrole` selector is visible.
3. `Basiscontrole` is selected by default.
4. Side-by-side review remains visible.
5. `Markeringen tonen` remains visible.
6. Manual missed-value entry remains reachable.
7. Replacement table remains reachable.
8. Scrub Key, downloads, audit files and DOCX hygiene audit remain available.
9. Export/Scrub Key/reinsert/recognizer behavior appears unchanged.
```
