# Workpackage claim — WP_CONTEXT_CARD_UI_PLAN

status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_CONTEXT_CARD_UI_PLAN — Plan non-authoritative context-card panel near review table
started timestamp: 2026-06-13T11:48:00+02:00
completed timestamp: 2026-06-13T11:55:00+02:00
scope: planning/contract-only plan for a small non-authoritative context-card panel near the existing review table using `context_cards.py`

## Boundaries

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `fix_streamlit_nested_expanders.py`.
- No startup source mutation.
- No full-document marking.
- No click-to-mark.
- No advanced editor.
- No review table mutation.
- No export/download changes.
- No Scrub Key changes.
- No reinsert changes.
- No dependency changes.
- No cloud processing.
- Synthetic data only.

## Final commit SHA / PR link

No PR was used; changes were committed directly to `main` through the GitHub contents API.

Final implementation/docs commit before this claim-close update:

```text
3a2c01d455466970b7f39db662e4524db2b61121
```

Note: the exact claim-close commit SHA is returned by the GitHub update call that writes this completed claim state.

## Handover path

```text
handover/workpackages/20260613_1148_context_card_ui_plan.md
```

## Tests/checks

Added contract tests:

```text
tests/test_context_card_ui_plan.py
```

Static contract review completed against `CONTEXT_CARD_UI_PLAN.md` and `tests/test_context_card_ui_plan.py`.

Expected follow-up in a normal checkout:

```text
pytest tests/test_context_card_ui_plan.py
pytest tests/test_context_card_ui_plan.py tests/test_context_cards.py
```

## GitHub Actions status

Unknown at claim close. A new run is expected after final commits.

## Hugging Face sync status

Unknown at claim close. This package does not change app runtime/UI/dependencies.

## App verification status

Not applicable. No Streamlit UI behavior changed.

## Next recommended step

Recommended next package:

```text
WP_CONTEXT_CARD_UI_CONTRACT_TESTS — optional next contract-test package for labels, fields and boundaries.
```

Alternative helper-first package:

```text
WP_REVIEW_PANEL_VIEW_MODEL_HELPER — combine serial review queue + context-card data into a pure view model before UI.
```

Do not start Streamlit UI implementation without explicit coordinator approval.
