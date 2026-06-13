# Handover — WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS — Contract tests for simple masked-text highlight toggle plan`

Status: completed tests/documentation-only; awaiting GitHub Actions and Hugging Face sync evidence.

## Summary

Added contract tests for `REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`.

The tests lock the planned simple masked-text highlight toggle as a small optional visual aid only. They do not implement UI.

## Files added

- `tests/test_review_highlight_toggle_plan.py`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS.md`
- `handover/workpackages/20260613_1745_review_highlight_toggle_contract_tests.md`

## Files changed

- `tests/test_review_highlight_toggle_plan.py`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS.md`

Attempted but not changed:

- `WORKPACKAGES.md` — update was blocked by connector safety checks; desired status is recorded below.

## Tests added/updated

Added `tests/test_review_highlight_toggle_plan.py` covering:

- `Markeringen tonen`;
- `Markeringen tonen in voorbeeldtekst`;
- off-state calm preview copy;
- on-state subtle marker copy;
- `read-only`;
- `visual-only`;
- `non-authoritative`;
- `non-mutating`;
- `table-first baseline`;
- existing review table as source of truth/fallback;
- simple product principles and no helper-internal panel;
- exact matching only;
- only already masked/replaced preview values;
- no guessing/fuzzy matching;
- no hidden/offscreen document content;
- no reinsert values;
- no replacement table mutation;
- no `edited_replacements_df` mutation;
- no automatic replacement;
- no Scrub Key writes/mappings/schema changes;
- no export/download changes;
- no export blocking;
- no reinsert changes;
- no old static-highlight startup mutation route;
- no click-to-mark;
- no advanced editor;
- no full-document marking;
- color not as only signal;
- raw HTML only if safely escaped and tested;
- synthetic-only/no-real-personal-data constraints;
- implementation gate remains separate coordinator approval.

## Tests/checks run

No shell/pytest execution was available through the GitHub connector.

Static review was performed against `REVIEW_HIGHLIGHT_TOGGLE_PLAN.md` after adding the test file. One too-strict wording expectation was corrected to match the existing plan wording:

```text
existing review table remains the source of truth and fallback
review table as source of truth
```

Expected targeted check in a normal checkout:

```text
pytest tests/test_review_highlight_toggle_plan.py
```

Expected full check:

```text
python -m pytest -q tests
```

## Validation status

- Contract tests added.
- No product code changed.
- No UI/runtime behavior changed.
- `CHANGELOG.md` updated.
- `WORKPACKAGES.md` update was attempted but blocked by connector safety checks.

Desired `WORKPACKAGES.md` status:

```text
WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS — completed tests/documentation-only; added tests/test_review_highlight_toggle_plan.py; awaiting Actions/HF verification.
```

Desired next queue entry:

```text
Verify GitHub Actions and Hugging Face sync for WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS before any implementation package.
```

## GitHub Actions status

Unknown at handover time. A new run is expected after the final commits.

## Hugging Face sync status

Unknown at handover time. This package does not change normal app runtime behavior.

## App verification status

Not applicable. No Streamlit UI/runtime behavior changed.

## Intentionally not changed

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `serial_review_panel_ui.py`.
- No product runtime behavior changes.
- No startup source mutation.
- No static-highlight startup patch.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No replacement table mutation.
- No automatic replacement.
- No Scrub Key writes.
- No export/download behavior changes.
- No export blocking.
- No reinsert behavior changes.
- No dependency changes.
- No cloud processing.
- No real data.

## Remaining risks

- Full suite still needs GitHub Actions verification.
- Hugging Face sync still needs verification.
- The highlight toggle remains planned/tested only; it is not visible in the app.
- Implementation still requires separate coordinator approval.

## Next recommended step

Verify:

```text
Tests — green
Sync to Hugging Face Space — green
```

Only after green evidence and separate coordinator approval should a future implementation package be considered:

```text
WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION
```
