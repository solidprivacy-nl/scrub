# Handover — WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER — Helper-only model for source/processed review panes`

Status: completed helper/tests-only; awaiting GitHub Actions verification.

## Summary

Added a pure helper model for the future unified side-by-side review surface:

```text
source/brontekst left | processed/checked text right
                      | optional highlights integrated in processed pane
```

The helper does not render Streamlit UI and does not change product runtime behavior. It prepares safe data structures for future UI work:

- source pane metadata;
- processed pane metadata;
- optional processed-pane highlight terms and exact spans;
- compact single legend metadata;
- review table source-of-truth/fallback metadata;
- serial review guided-layer relationship metadata;
- replacement review future task-oriented relationship metadata;
- synchronized scrolling desired-later but not implemented metadata;
- explicit no-mutation/no-export/no-Scrub-Key/no-reinsert boundary flags.

## Files added

- `side_by_side_review.py`
- `tests/test_side_by_side_review_prototype.py`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER.md`
- `handover/workpackages/20260614_2250_side_by_side_review_prototype_helper.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER.md`

## Tests added/updated

Added `tests/test_side_by_side_review_prototype.py`.

The tests cover:

- source pane left and processed pane right;
- user-facing labels `Brontekst` and `Verwerkte tekst`;
- highlight spans only in processed pane;
- highlight toggle is visual-only and non-mutating;
- compact single legend without repeated inline `Gemarkeerd` labels;
- review table source-of-truth/fallback fields;
- serial review as guided layer, not table replacement;
- replacement review as future task-oriented layer;
- blocked user-facing helper internals such as `all_normalized`;
- synchronized scrolling desired later but not implemented;
- no review table/replacement/Scrub Key/export/reinsert mutation;
- no Streamlit import or UI calls;
- synthetic-only test values.

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

Expected checks:

```text
pytest tests/test_side_by_side_review_prototype.py
pytest tests/test_side_by_side_review_prototype.py tests/test_side_by_side_review_contract.py tests/test_review_highlight_toggle.py
pytest
```

## Validation status

Repository source updated and static source review completed through GitHub reads.

No app verification is required because this package changes no UI/runtime behavior.

## GitHub Actions status

Unknown at handover time. Verify Actions for the final helper commit before starting an implementation package.

## Hugging Face sync status

Not required for this helper-only package. No UI/runtime behavior changed.

## App verification status

Not applicable.

## Remaining risks

- The helper does not implement the side-by-side UI.
- The current app still has multiple review surfaces until a future approved implementation changes it.
- Synchronized scrolling remains only a desired-later field and still requires separate planning/testing.
- Custom HTML/component rendering remains blocked until separately approved.
- Side-by-side review implementation remains blocked until separate explicit coordinator approval.

## Next recommended step

```text
Verify GitHub Actions for WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER.
```

Then, only after separate explicit coordinator approval:

```text
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION
```

Do not start without separate coordinator approval:

```text
synchronized scroll implementation
custom HTML/component rendering
replacement UI implementation
click-to-mark
advanced editor
full-document marking
export blocking
Scrub Key writes
```
