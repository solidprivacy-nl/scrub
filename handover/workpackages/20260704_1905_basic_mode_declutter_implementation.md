# Handover — SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION — Make Basiscontrole materially cleaner while preserving Expertcontrole

## Status

Completed / merged / app-verified.

## Merge

- PR: #19 — SCRUB-WP basic mode declutter implementation
- Merge SHA: c68129b3b179fb2f4e0284a57678b96f9fa64ed7
- Closeout status commit: fb0ba13a4ab435462a719d4edc8e551011a1c18e

## Files added

- tests/test_basic_mode_declutter_implementation.py
- handover/workpackages/20260704_1905_basic_mode_declutter_implementation.md

## Files changed

- presidio_streamlit.py
- tests/test_execution_interface_simplification_ui.py
- tests/test_review_table_collapsible_contract.py
- workpackage_claims/scrub_wp_basic_mode_declutter_implementation.md
- handover/workpackages/20260704_1905_basic_mode_declutter_implementation.md

## Tests/checks

Local patch-capable worker validation passed:

- python -m py_compile presidio_streamlit.py
- git diff --check
- targeted pytest set: 74 passed

PR validation:

- Initial PR Actions found two stale source-level assertions for the old inline replacement-table expander string.
- Tests were updated to assert the new `replacement_table_label` source shape and both labels:
  - `Vervangtabel controleren —`
  - `Details aanpassen — vervangtabel`
- PR GitHub Actions Tests passed after the stale assertions were updated.

## Validation status

Validated and merged.

## GitHub Actions status

PR GitHub Actions Tests passed before merge.

## Hugging Face sync status

Live Hugging Face Space running updated app after merge.

## App verification status

Completed by coordinator screenshots on 2026-07-04.

Verification confirmed:

- app starts without Script execution error;
- Basiscontrole is selected by default;
- side-by-side review remains visible;
- Markeringen tonen remains visible;
- Basiscontrole is visibly cleaner than the pre-WP expert stack;
- Gemiste waarde toevoegen remains reachable;
- Details aanpassen — vervangtabel remains reachable;
- Expertcontrole exposes full detailed controls;
- primary downloads remain visible;
- Scrub Key download remains separated;
- audit downloads remain available;
- DOCX hygiene audit remains available.

## Remaining risks

- There is still a broader interface simplification opportunity outside this workpackage: the page still shows duplicate `1. Voeg document of tekst toe` surfaces in the verified screenshot. This was not changed in this WP.
- No automated visual regression exists; final UI clarity still depends on manual screenshots.

## Next recommended step

Proceed with the next small UI simplification workpackage focused on reducing duplicate upload/input presentation and further tightening the default flow without touching export, Scrub Key, reinsert or recognition semantics.
