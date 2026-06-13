# Workpackage claim — WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2

status: completed; awaiting Actions/HF verification
repository: solidprivacy-nl/scrub
workpackage title: WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2 — Repair replacement-logic contract text failures after highlight toggle plan
started timestamp: 2026-06-13T16:58:00+02:00
completed timestamp: 2026-06-13T17:05:00+02:00
scope: narrow Actions repair for Tests #844 failures in replacement-logic documentation/contracts exposed after WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX

## Boundaries

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
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

## Final commit SHA or PR link

No PR was used. Changes were committed directly to `main` through the GitHub contents API.

Final handover commit before this claim close:

```text
9de0fc673046c77d4c8c29e3e3b8073cee62bf45
```

## Handover path

```text
handover/workpackages/20260613_1658_review_highlight_toggle_plan_actions_fix2.md
```

## Tests/checks

No shell/pytest execution was available through the GitHub connector.

Repair was based on the exact failure lines shown in coordinator screenshot for `Tests #844`:

- missing `does not write Scrub Key mappings` in `replacement_decision_panel_ui.py` renderer text;
- missing `WP_REPLACE_LOGIC_UI_CONTRACT_TESTS` in `REPLACE_LOGIC_UI_PLAN.md`.

Expected targeted checks:

```text
pytest tests/test_replace_logic_ui_patch.py tests/test_replace_logic_ui_plan.py
python -m pytest -q tests
```

## GitHub Actions status

Unknown at claim close. A new run is expected after the final fix commit.

## Hugging Face sync status

Unknown at claim close. This package does not change normal app runtime behavior.

## App verification status

Not applicable. No normal app UI/runtime behavior was intentionally changed.

## Next recommended step

Verify Tests and Sync for the final fix commit. Only after green evidence:

```text
WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS
```

Do not start `WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION` without separate coordinator approval.
