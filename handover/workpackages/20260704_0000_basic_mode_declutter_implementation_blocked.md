# Handover — SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION

Repository: solidprivacy-nl/scrub  
Status: blocked / implementation not started

## Summary

The precondition for implementation is satisfied because `SCRUB-WP_BASIC_MODE_DECLUTTER_CONTRACT_TESTS` was merged via PR #18. The implementation branch already exists and the claim was created. The current review/export code path in `presidio_streamlit.py` was inspected.

Implementation did not proceed because the required change must patch `presidio_streamlit.py`, while the available GitHub write operation in this connector session can only replace the full file. A generated full-file replacement of this large, safety-critical UI/export file would create unnecessary risk of accidental product-code drift. No runtime/startup patch, CSS hack, wrapper approach, or broad rewrite was introduced.

## Files added

- `handover/workpackages/20260704_0000_basic_mode_declutter_implementation_blocked.md`

## Files changed

- `workpackage_claims/scrub_wp_basic_mode_declutter_implementation.md`

## Product files changed

None.

## Tests / checks

- Required project documents were read.
- Precondition verified: `SCRUB-WP_BASIC_MODE_DECLUTTER_CONTRACT_TESTS` is merged.
- Existing branch inspected: `scrub-basic-mode-declutter-implementation`.
- Existing claim inspected and updated to blocked.
- `presidio_streamlit.py` review/export area inspected.
- No source-level tests were added because implementation did not start.
- No product tests were run.

## Validation status

- GitHub Actions: not applicable; no implementation PR opened.
- Hugging Face sync: not applicable.
- App verification: not applicable because no UI behavior changed.

## Intended implementation that remains to be done

A follow-up worker with patch/local-git capability should apply the small intended patch:

- capture `side_by_side_review_state = render_side_by_side_review_panel(...)`;
- derive `review_mode` and `is_expert_review`;
- keep `Gemiste waarde toevoegen`, replacement count, document downloads, Scrub Key downloads, audit downloads and DOCX hygiene available;
- show `Waarom controleren?`, `Extra controlehulpen`, `Geavanceerde details bij de vervangtabel`, `render_serial_review_panel`, `Herbruikbare vervangingen`, `Technische informatie` and `Geavanceerde herkenningsdetails` only in `Expertcontrole`;
- show candidate audit values in Basiscontrole only when candidate rows exist;
- use the calmer Basiscontrole table label `Details aanpassen — vervangtabel (...)`;
- avoid nested expanders;
- add `tests/test_basic_mode_declutter_implementation.py`.

## Intentionally not changed

- `presidio_streamlit.py`;
- `side_by_side_review_panel_ui.py`;
- replacement logic;
- review table data semantics;
- include/remember/find/replace_with meaning;
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

- `Basiscontrole` is not yet materially decluttered beyond the earlier mode selector.
- The branch contains only status/handover changes for this package.
- The implementation still requires a safe patch-capable workflow.

## Next recommended step

Continue this package with a worker/tooling setup that can apply a small unified diff to `presidio_streamlit.py` safely. Do not use a generated full-file rewrite or runtime/startup patch.
