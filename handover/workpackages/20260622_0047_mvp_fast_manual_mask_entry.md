# Handover — WP_MVP_FAST_MANUAL_MASK_ENTRY

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_MVP_FAST_MANUAL_MASK_ENTRY`

Status: completed_pending_verification.

## Summary

Implemented a small MVP improvement that lets a user add a missed value manually from the review flow. The manual row is added to the existing replacement table and therefore uses the existing replacement/export path.

The package keeps the existing review table as source of truth and does not change export, Scrub Key, reinsert, recognizer, benchmark, Docker or runtime behavior.

## Files added

- `manual_mask_entry.py`
- `tests/test_manual_mask_entry.py`
- `tests/test_mvp_fast_manual_mask_entry_ui.py`
- `workpackage_claims/WP_MVP_FAST_MANUAL_MASK_ENTRY.md`
- `handover/workpackages/20260622_0047_mvp_fast_manual_mask_entry.md`

## Files changed

- `presidio_streamlit.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `RELEASE_NOTES.md`

## Product-code changes

- Added `manual_mask_entry.py` with Streamlit-free helper functions for manual replacement rows.
- Added a `Gemiste waarde toevoegen` form near `3. Controleer gevonden gegevens`.
- Added manual rows to the existing replacement table data before rendering the table.
- Scoped manual rows to the current text using `manual_mask_document_key`.
- Kept existing export/download/Scrub Key/reinsert paths unchanged.

## Tests

Coordinator Codespaces focused tests:

```text
python -m pytest -q tests/test_manual_mask_entry.py — 11 passed
python -m pytest -q tests/test_mvp_fast_manual_mask_entry_ui.py — 8 passed
python -m pytest -q tests/test_replace_logic_ui_patch.py — 7 passed
python -m pytest -q tests/test_review_table_collapsible_contract.py — 11 passed
python -m pytest -q tests/test_side_by_side_review_consolidation_dutch_sample.py — 8 passed
python -m pytest -q tests/test_export_download_ux_contracts.py tests/test_export_download_ux_implementation.py — 19 passed
python -m py_compile presidio_streamlit.py serial_review_panel_ui.py side_by_side_review_panel_ui.py manual_mask_entry.py — no error reported
git diff --check — no error reported
git status — clean after d57cec4
```

## Validation status

Local/focused validation passed. GitHub Actions validation is pending/unknown after the final governance commits.

## GitHub Actions status

Pending/unknown.

## Hugging Face sync status

Pending/unknown.

## App verification status

Pending.

Required live app checks:

```text
Geen Script execution error
1. Voeg document of tekst toe werkt
2. Controleer de tekst blijft zichtbaar
3. Controleer gevonden gegevens blijft zichtbaar
Gemiste waarde toevoegen is zichtbaar en simpel
Een handmatig toegevoegde waarde verschijnt in de vervangtabel
De waarde wordt toegepast in de verwerkte tekst/export
Stap voor stap controleren blijft ingeklapt
Geavanceerde details blijven ingeklapt
5. Exporteer resultaat blijft zichtbaar
Download opgeschoonde tekst werkt
Scrub Key-waarschuwing blijft zichtbaar
```

## Remaining risks

- Live app verification is still required.
- Human review remains necessary.
- The manual entry path helps with false negatives but does not prove detection quality.
- Further UI simplification should remain small and separately approved.

## Next recommended step

```text
Verify GitHub Actions, Hugging Face sync and live app for WP_MVP_FAST_MANUAL_MASK_ENTRY.
```

After verification only:

```text
Mark WP_MVP_FAST_MANUAL_MASK_ENTRY completed_verified.
```

Do not start follow-up work automatically.
