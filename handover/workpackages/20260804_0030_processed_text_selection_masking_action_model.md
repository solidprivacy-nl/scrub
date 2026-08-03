# Handover — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: Implement the pure processed-text selection masking action model  
Status: completed; GitHub Actions green

## Summary

Implemented the Streamlit-free and browser-free action model behind direct masking from a selection in `Verwerkte tekst`.

The model now provides:

- strict inspect/commit event parsing;
- UTF-16 browser-offset conversion with split-surrogate rejection;
- selection, placeholder, marked-range and source-presence validation;
- non-overlapping exact occurrence counting;
- Unicode-aware embedded-token collision blocking;
- exact/nested replacement-rule conflict blocking;
- ready / confirmation-required / blocked impact classification;
- bounded replay state and opaque single-use inspections;
- commit-time revalidation of document, binding, source, processed text, table and impact;
- existing document-bound manual-row creation;
- stable action records and fail-closed one-step undo.

The visible Streamlit form options remain unchanged. The extra quick-type labels are internal mappings for the later component/integration line.

## Files added

- `selection_mask_action.py`
- `tests/test_selection_mask_action.py`
- `PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL.md`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_action_model.md`
- `handover/workpackages/20260804_0030_processed_text_selection_masking_action_model.md`

## Files changed

- `manual_mask_entry.py`
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests

The new tests cover:

- no Streamlit/component dependency;
- event envelope and payload limits;
- UTF-16 conversion for BMP, accents, combining marks and supplementary characters;
- split-surrogate, negative and out-of-range offsets;
- exact non-overlapping and case-sensitive occurrences;
- Unicode token continuation and punctuation boundaries;
- embedded values such as `Jan` in `Jansen`, `Jan-Willem`, `O'Neil` and `AB123C`;
- duplicate and nested replacement conflicts;
- selection length, control, newline, placeholder and marked-range rules;
- 1–5, 6–20 and >20 impact bands;
- stale document, processed text, source, binding and table state;
- event replay and bounded history;
- all eight quick types and bound placeholders;
- confirmation tokens;
- single-use inspections;
- stable action IDs and safe undo;
- deterministic replacement-state hashes.

## Validation status

- Initial PR run #1957: failed because one validated `event_id` was not assigned locally and one test rejected an explanatory use of the word `JavaScript`; the remaining failures cascaded from the missing ID.
- Corrected run #1961: **1106 tests passed in 10.66s**.
- Governance updates are applied, the standard workflow is restored and temporary operators are removed.
- Clean standard PR run #1970: **1106 tests passed in 10.71s**.
- Hugging Face sync: not functionally relevant; the helper is not connected to runtime/UI yet.
- App verification: not applicable; no UI behavior changed.

## GitHub Actions status

Green. Corrected implementation run #1961 passed 1106 tests in 10.66s; clean standard PR run #1970 passed 1106 tests in 10.71s. One final status-only regression follows this closeout update.

## Hugging Face sync status

Not functionally relevant in this package.

## App verification status

Not applicable.

## Remaining risks

- The helper is not yet connected to a browser component or Streamlit session state.
- Browser-side text-node walking must produce offsets that match this UTF-16 contract.
- The component must preserve selection/menu state across Streamlit reruns without replaying events.
- Highlight ranges supplied to the server must use the agreed processed-text coordinate system.
- The current manual form and static renderer remain required fallbacks.
- Occurrence-specific masking remains explicitly out of scope.

## Next recommended step

After merge, claim:

```text
SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE
```

Keep the spike non-mutating. Do not integrate with the replacement table or `presidio_streamlit.py` until the component proof is green.
