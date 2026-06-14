# Handover — WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN — Detailed plan for unified source/processed review surface`

Status: completed planning/design/documentation-only.

## Summary

Added `SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md`, a detailed UX plan for the unified side-by-side review surface.

The plan expands the anchored direction:

```text
Brontekst links | Verwerkte/gecontroleerde tekst rechts
                | Optionele markeringen geïntegreerd in de verwerkte tekst
```

It defines the desired main review layout, placement of the highlight toggle, the long-term relationship to the existing highlight preview, review table fallback, serial review, replacement review, desired and unwanted copy, the smallest safe first implementation and required pre-implementation contract tests.

This package did not implement UI and did not change product code or tests.

## Files added

- `SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md`
- `handover/workpackages/20260614_2205_side_by_side_review_redesign_plan.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md`

## Tests/checks run

No shell access was available through the ChatGPT GitHub connector.

Expected check, not run here:

```text
git diff --check
```

No product tests were run because this was planning/design/documentation-only and changed no product code, UI code or runtime behavior.

## Validation status

Completed by repository document review and central-document updates.

Validated against:

- `PROJECT_PROMPT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `RELEASE_NOTES.md`
- `REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`
- `review_highlight_toggle.py`
- `review_highlight_toggle_panel_ui.py`
- `serial_review.py`
- `serial_review_panel_ui.py`
- `review_panel_view_model.py`
- `REPLACE_LOGIC_UI_REDESIGN_PLAN.md`
- `REPLACE_LOGIC_UI_PLAN.md`
- `presidio_streamlit.py`
- `handover/workpackages/20260614_2130_side_by_side_review_roadmap_anchor.md`

## GitHub Actions status

Not applicable / not required for this planning-only package.

No product code, UI code or tests changed.

## Hugging Face sync status

Not applicable / not required for this planning-only package.

No app rebuild or app verification is required.

## App verification status

Not applicable.

## Remaining risks

- The current app still has multiple review surfaces until a future approved implementation changes it.
- The existing highlight-only duplicate preview is not the desired long-term UX but remains an intermediate safe implementation.
- Repeated per-highlight labels such as `Gemarkeerd` remain implementation debt for future refinement.
- Synchronized scrolling is desirable but must be planned/tested separately because it may require custom rendering.
- Side-by-side implementation remains blocked until contract tests and separate coordinator approval.

## Next recommended step

```text
WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS
```

If that is already completed by another worker, move to:

```text
WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER
```

Do not start without separate coordinator approval:

```text
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION
synchronized scroll implementation
custom HTML/component rendering
click-to-mark
advanced editor
full-document marking
replacement UI implementation
export blocking
Scrub Key writes
```
