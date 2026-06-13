# Handover — WP_CONTEXT_CARD_HELPER

Repository: solidprivacy-nl/scrub  
Workpackage title: WP_CONTEXT_CARD_HELPER — Safe context-card helper for document-centric review  
Status: completed helper/tests-only implementation; pending remote Actions/Hugging Face visibility.

## Summary

Implemented a pure Python helper for safe context cards around detected values. The helper builds prefix/match/suffix snippets around exact offsets in the displayed text, provides escaped rendering fields, preserves review metadata as data, and locks report-only/non-mutating boundaries.

This package intentionally replaces the failed full-document marking direction with a smaller helper-first path. It does not add Streamlit UI, full-document marking, click-to-mark, an advanced editor, startup mutation, export changes, Scrub Key changes, reinsert changes, dependencies, cloud processing or real-data fixtures.

## Files added

- `context_cards.py`
- `tests/test_context_cards.py`
- `handover/workpackages/20260613_1115_context_card_helper.md`

## Files changed

- `workpackage_claims/WP_CONTEXT_CARD_HELPER.md` — claim created as `in_progress`; final completion update follows this handover.
- `CHANGELOG.md` — intended update for implementation history.
- `WORKPACKAGES.md` — intended update for current status / next step.

## Tests added/updated

- Added `tests/test_context_cards.py` with coverage for:
  - valid context card;
  - match at beginning of text;
  - match at end of text;
  - context window truncation;
  - invalid offsets;
  - label/source mismatch;
  - HTML escaping with synthetic `<script>` value;
  - risk flags preserved as data;
  - report-only and mutation boundaries;
  - synthetic-only test values.

## Tests/checks run

Executed locally in an isolated workspace assembled from the new helper/tests and the existing highlight preview helper/tests:

```text
pytest tests/test_context_cards.py
```

Result:

```text
10 passed
```

Also executed:

```text
pytest tests/test_context_cards.py tests/test_highlight_preview.py
```

Result:

```text
16 passed
```

A full repository `pytest` was not run because the ChatGPT GitHub connector does not provide a full checked-out repo shell/runtime. The local Python runtime also emitted an unrelated spreadsheet warmup warning after pytest; pytest itself passed.

## Validation status

- Helper behavior: locally validated with focused pytest.
- Offset behavior: exact displayed-text offset matching only; invalid offsets return invalid cards without crashing.
- HTML safety: escaped fields provided for all snippet parts and source/replacement preview values.
- Mutation boundary: locked with `report_only=True`, `mutation_allowed=False`, `export_blocking=False`, `scrub_key_changes=False`, plus no automatic replacement/fuzzy matching/editor-state flags.

## GitHub Actions status

- Checked commit workflow runs for the first helper/test commits through the connector.
- No workflow runs were visible at the time of checking.
- Final status: unknown / not yet visible through connector.

## Hugging Face sync status

- Unknown / not verified through connector.
- No UI or runtime startup behavior changed in this package.

## App verification status

- Not applicable for this package because no Streamlit UI, startup, export, Scrub Key or reinsert behavior changed.

## Remaining risks

- The helper is not yet integrated into a UI panel.
- Context cards are only as reliable as the caller-provided displayed text and offsets.
- Remote CI/Hugging Face status still needs normal pipeline visibility after GitHub updates.
- Future UI must remain non-authoritative unless a separate approved package changes that boundary.

## Next recommended step

- `WP_CONTEXT_CARD_UI_PLAN` — plan a small non-authoritative context-card panel near the review table.
- Only after coordinator approval: `WP_SERIAL_REVIEW_UI` — combine serial review queue with context cards in a small Streamlit panel.
