# Handover — WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY — Feasibility review for synchronized side-by-side scrolling`

Status: completed documentation-only feasibility review.

## Summary

Added `SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY.md`.

The review concludes:

```text
Do not implement synchronized scrolling in the current Streamlit MVP flow.
Keep equal-height independent panes as the safe baseline.
```

Reason:

```text
Source and processed text are not guaranteed to align line-by-line or by scroll percentage after masking/replacement. Naive synchronized scrolling could create false visual alignment.
```

The document compares:

- equal-height independent scroll panes;
- percentage-based synchronized scroll with custom component;
- anchor-based synchronized scroll;
- selected-item focus as a lower-risk alternative.

## Files added

- `SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY.md`
- `handover/workpackages/20260615_0005_side_by_side_review_sync_scroll_feasibility.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY.md`

## Tests/checks run

No shell/git diff execution was available through the ChatGPT GitHub connector.

No product tests were required because this package changed no product code, UI code or runtime behavior.

## Validation status

Completed by documentation review and central-document updates.

Validated against:

- `PROJECT_PROMPT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md`
- `side_by_side_review_panel_ui.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

## GitHub Actions status

Not applicable / not required for this documentation-only feasibility package.

## Hugging Face sync status

Not applicable / not required for this documentation-only feasibility package.

## App verification status

Not applicable.

## Remaining risks

- Synchronized scrolling remains unimplemented.
- If still desired, it requires contract tests and a separately approved spike.
- A future implementation must avoid cloud processing, unsafe raw HTML, review table mutation, Scrub Key changes, export/download changes and reinsert behavior changes.
- Current side-by-side implementation and height fix still need normal closeout after green Actions/HF sync and app screenshot.

## Next recommended step

Immediate:

```text
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY
```

Only if the coordinator still wants synchronized scroll after that:

```text
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_CONTRACT_TESTS
```

Do not start without separate coordinator approval:

```text
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_SPIKE
synchronized scroll implementation
custom Streamlit component rendering
JavaScript injection
click-to-mark
advanced editor
full-document marking
export blocking
Scrub Key writes
```
