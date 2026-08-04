# Handover — SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: Integrate direct processed-text masking with the authoritative review table  
Status: completed, synchronized and live-app verified

## Summary

Integrated the approved processed-text selection flow into the production review architecture while retaining the review table, current manual entry and static renderer as authoritative fallbacks.

The component emits bounded inspect/commit-intent events. After the editable review table returns its current state, `presidio_streamlit.py` processes those events through the pure action model and document-scoped integration adapter. A successful commit appends exactly one normal bound row to the existing `manual_mask_rows` bucket and reruns before serial review or export.

## Files added

- `processed_text_selection_integration.py`
- `tests/test_processed_text_selection_integration.py`
- `tests/test_processed_text_selection_table_integration_contract.py`
- `PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION.md`
- `workpackage_claims/scrub_wp_processed_text_selection_table_integration.md`
- `handover/workpackages/20260804_0134_processed_text_selection_table_integration.md`

## Files changed

- `processed_text_selection_component.py`
- `side_by_side_review_panel_ui.py`
- `presidio_streamlit.py`
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

## Tests

New tests cover:

- document-scoped inspect state, inspection results, scroll restore and feedback;
- no row creation during inspect;
- exactly one bound row on commit;
- replayed inspect/commit events produce no duplicate mutation;
- blocked commit adds no row;
- isolation between documents;
- undo of only the latest unchanged selection row;
- undo refusal after visible table edits;
- event processing after `st.data_editor` and before serial review/export;
- immediate rerun after state mutation;
- static renderer environment/exception fallback;
- protected spans while visual markers are hidden;
- existing manual form and authoritative table retention;
- no export, Scrub Key or reinsert behavior in the new layers.

## Validation status

- Cleanup run #2044: frontend component tests passed; two obsolete phase-status assertions failed in Python only.
- Final clean PR run #2047: 1146 Python tests passed in 11.97s.
- Evidence-finalization run #2049: 1146 Python tests passed in 11.74s.
- Final standard merge-candidate run #2051: 1146 Python tests passed in 11.59s.
- Independent deployment run #2064 matched 11/11 runtime/component files, returned Space health `ok` and HTTP 200, passed frontend tests, and passed 1146 Python tests in 11.47s.
- Coordinator/user live app verification confirmed `Het werkt.` at 2026-08-04 22:22 Europe/Amsterdam.

## GitHub Actions status

Green. Frontend component tests passed in cleanup run #2044. Final clean PR run #2047 passed 1146 Python tests in 11.97s, evidence-finalization run #2049 passed 1146 tests in 11.74s, and final standard run #2051 passed 1146 tests in 11.59s.

## Hugging Face sync status

Green through independent run #2064: 11/11 files exact, health `ok`, root HTTP 200.

## App verification status

Confirmed by the coordinator/user: selection masking and undo work in the deployed app; existing review/export/Scrub Key/reinsert surfaces remain present.

## Remaining risks

- Browser rerun/focus behavior requires live deployed verification.
- Component rendering errors must demonstrably fall back to the static renderer.
- Hidden visual markers must still block selection through server-protected spans.
- Existing table edits must remain authoritative over undo.
- Export, Scrub Key and reinsert must be verified after a selection-created row.
- Cross-browser Edge, Chrome and Firefox verification remains after integration.
- Occurrence-specific masking remains out of scope.

## Next recommended step

Implement the separately scoped display-only bound-placeholder compaction without changing binding entropy or export/Scrub Key/reinsert semantics, then continue with cross-flow regression.
