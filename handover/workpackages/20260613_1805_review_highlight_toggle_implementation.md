# Handover — WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — Simple masked-text highlight toggle implementation`

Status: completed after Tests/app verification; Hugging Face final sync retry required.

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
- `handover/workpackages/20260613_1805_review_highlight_toggle_implementation.md`

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

Coordinator screenshot evidence:

```text
Tests #878 — green for commit 60750c0
```

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
- GitHub Actions tests are green by coordinator screenshot evidence: `Tests #878`, commit `60750c0`.
- App verification is positive by coordinator screenshot: app starts, review table remains visible, serial review remains visible, `Voorbeeldtekst met optionele markeringen` is visible, `Markeringen tonen in voorbeeldtekst` is visible, and subtle highlight markers are shown.
- No startup mutation was introduced.
- No export/download behavior was changed.
- No Scrub Key behavior was changed.
- No reinsert behavior was changed.
- No dependency was added.
- No cloud processing or real data was introduced.

## GitHub Actions status

Green by coordinator screenshot evidence: `Tests #878` for commit `60750c0`.

## Hugging Face sync status

Final sync not green yet.

Coordinator screenshot evidence:

```text
Sync to Hugging Face Space #890 — failed for commit 60750c0
fatal: unable to access 'https://huggingface.co/spaces/solidprivacy/scrub/': The requested URL returned error: 429
```

This appears to be an external/rate-limit sync failure, not a code or test failure.

The provided app screenshot shows the feature visible in the Hugging Face Space, so implementation code appears deployed, but the final workflow evidence remains red and should be retried.

## App verification status

Positive by coordinator screenshot.

Confirmed visually:

- app starts without Script execution error;
- normal Scrub Legal flow remains visible;
- review table remains visible;
- serial review panel remains visible;
- `Voorbeeldtekst met optionele markeringen` is visible in the review area;
- `Markeringen tonen in voorbeeldtekst` toggle is visible;
- toggle on shows subtle markers for already masked/replaced values;
- export/download remains visible;
- no static-highlight startup error;
- no click-to-mark/advanced editor/full-document marking was shown.

## Remaining risks

- Final Hugging Face sync evidence is red due `429`; retry is required before marking fully completed after Actions/HF/app verification.
- Because the feature uses `st.markdown(..., unsafe_allow_html=True)` for marker rendering, safety depends on the helper escaping raw document text first. Tests cover the escaping contract.
- App screenshot is positive, but final administrative sync run is still red.

## Next recommended step

Rerun or wait/retry:

```text
Sync to Hugging Face Space #890
```

Expected final status after a successful retry:

```text
WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — completed after Actions/HF/app verification
```

Do not start broader document marking, click-to-mark, advanced editor or replacement UI redesign without separate coordinator approval.
