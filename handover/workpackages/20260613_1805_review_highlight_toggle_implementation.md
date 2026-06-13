# Handover — WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — Simple masked-text highlight toggle implementation`

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

## Summary

Implemented a small optional review highlight toggle after coordinator approval and after green contract-test evidence.

The toggle appears in the review area as:

```text
Markeringen tonen in voorbeeldtekst
```

It is rendered from the serial review panel through a separate renderer:

```text
review_highlight_toggle_panel_ui.py
```

The feature builds a read-only checked preview from the current replacement table values and can show subtle markers for exact replacement values that are already present in that preview.

The helper escapes document text before wrapping matched values in static marker HTML.

## Files added

- `review_highlight_toggle.py`
- `review_highlight_toggle_panel_ui.py`
- `tests/test_review_highlight_toggle.py`
- `tests/test_review_highlight_toggle_ui_patch.py`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION.md`
- `handover/workpackages/20260613_1805_review_highlight_toggle_implementation.md`

## Files changed

- `serial_review_panel_ui.py`
- `RELEASE_NOTES.md`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION.md`

## Tests added/updated

Added:

```text
tests/test_review_highlight_toggle.py
tests/test_review_highlight_toggle_ui_patch.py
```

Covered:

- exact matching only;
- include-only replacement terms;
- de-duplication and longest-first term order;
- escaping of raw document text before HTML rendering;
- no fuzzy matching;
- no table/export/Scrub Key/reinsert mutation metadata in output;
- UI label and helper text;
- connection from `serial_review_panel_ui.py` to the new renderer;
- visible read-only/visual-only/non-mutating boundaries;
- no startup source mutation;
- no click-to-mark;
- no advanced editor;
- no full-document marking;
- no export/download calls in the new toggle renderer;
- synthetic-only values.

## Tests/checks run

No shell/pytest execution was available through the GitHub connector.

Expected targeted checks:

```text
pytest tests/test_review_highlight_toggle.py tests/test_review_highlight_toggle_ui_patch.py tests/test_review_highlight_toggle_plan.py
```

Expected full check:

```text
python -m pytest -q tests
```

## Validation status

- Contract tests were green before implementation by coordinator screenshot evidence: `Tests #865`, `Sync #877`, commit `07b7581`.
- Implementation completed after explicit coordinator approval.
- No startup mutation was introduced.
- No export/download behavior was changed.
- No Scrub Key behavior was changed.
- No reinsert behavior was changed.
- No dependency was added.
- No cloud processing or real data was introduced.

## GitHub Actions status

Unknown at handover time. A new run is expected after the implementation commits.

## Hugging Face sync status

Unknown at handover time. A new sync run is expected after the implementation commits.

## App verification status

Required after green Actions and Hugging Face sync because UI behavior changed.

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal flow remains visible;
- review table remains visible;
- serial review panel remains visible;
- `Voorbeeldtekst met optionele markeringen` is visible in the review area;
- `Markeringen tonen in voorbeeldtekst` toggle is visible;
- toggle off shows normal calm preview text;
- toggle on shows subtle markers for already masked/replaced values;
- export/download remains visible and unchanged;
- DOCX hygiene audit remains visible;
- no static-highlight startup error;
- no click-to-mark/advanced editor/full-document marking.

## Remaining risks

- Full Actions test suite still needs verification.
- Hugging Face sync still needs verification.
- App verification still needs coordinator screenshot.
- Because the feature uses `st.markdown(..., unsafe_allow_html=True)` for marker rendering, safety depends on the helper escaping raw document text first. Tests cover the escaping contract.

## Next recommended step

Verify:

```text
Tests — green
Sync to Hugging Face Space — green
```

Then request app verification screenshot for the toggle.

Do not start broader document marking, click-to-mark, advanced editor or replacement UI redesign without separate coordinator approval.
