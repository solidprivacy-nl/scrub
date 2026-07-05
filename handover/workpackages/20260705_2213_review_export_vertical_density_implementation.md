# Handover — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION — Reduce Review/Export vertical density

## Status

Completed and app-verified.

## Files added

- `handover/workpackages/20260705_2213_review_export_vertical_density_implementation.md`

## Files changed

- `presidio_streamlit.py`
- `side_by_side_review_panel_ui.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_implementation.md`

## Tests

Passed locally:

- `python -m pytest -q tests/test_review_export_vertical_density_contracts.py` → 9 passed.
- Related narrow Review/Export guardrail suite → 40 passed.
- `git diff --check` passed.


## Validation status

Local validation passed.

## GitHub Actions status

PR #26 validation passed after the narrow side-by-side copy contract repair.

## Hugging Face sync status

Verified indirectly by the live Hugging Face app showing the merged UI change.

## App verification status

Passed by coordinator live Hugging Face screenshot after PR #26 merge/deployment.

## Remaining risks

- Live app verification must confirm the page is shorter and less form-like.
- Review safety controls must remain discoverable: side-by-side review, marker toggle, missed-value entry and replacement table.
- Export semantics must remain unchanged: payloads, filenames and MIME types.
- Scrub Key and audit files must remain separate from normal document downloads.

## Next recommended step

Run local validation, open PR, verify GitHub Actions, merge when green, verify Hugging Face sync, then request live app verification.


## App verification evidence

2026-07-05 22:42 Europe/Amsterdam: coordinator live Hugging Face screenshot verified the Review/Export density implementation.

Confirmed:
- App starts without Script execution error.
- One coherent input section remains.
- `2. Controleer resultaat` remains visible.
- Basiscontrole and Expertcontrole remain visible and selectable.
- `Markeringen tonen` remains visible.
- Side-by-side review remains visible.
- `Gemiste waarde toevoegen` remains accessible.
- Vervangtabel remains accessible.
- Replacement count/status remains understandable.
- `3. Exporteer resultaat` remains visible.
- TXT/DOCX/PDF downloads are visible in a compact row.
- Scrub Key remains accessible and separate.
- Audit and technical files remain accessible.
- DOCX hygiene audit remains accessible.
- No export filenames, MIME types, payloads, Scrub Key JSON or reinsert behavior changed.
