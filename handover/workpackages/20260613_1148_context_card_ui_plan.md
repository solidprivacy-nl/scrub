# Handover — WP_CONTEXT_CARD_UI_PLAN

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_CONTEXT_CARD_UI_PLAN — Plan non-authoritative context-card panel near review table`

Status: completed planning/contract-only; awaiting GitHub Actions and Hugging Face sync evidence.

## Summary

Created a planning/contract document for a small context-card panel near the existing review table.

The plan uses the existing `context_cards.py` helper and preserves the table-first review workflow as the baseline/fallback. The panel is planned as context-assistive only: report-only, non-authoritative and non-mutating.

The plan explicitly avoids restarting the failed static-highlight/startup-mutation route and does not approve full-document marking, click-to-mark, an advanced editor or any Streamlit UI implementation.

## Files added

- `CONTEXT_CARD_UI_PLAN.md`
- `tests/test_context_card_ui_plan.py`
- `workpackage_claims/WP_CONTEXT_CARD_UI_PLAN.md`
- `handover/workpackages/20260613_1148_context_card_ui_plan.md`

## Files changed

- `CONTEXT_CARD_UI_PLAN.md` — tightened exact contract wording after static review.
- `WORKPACKAGES.md` — recorded completed planning/contract-only status and next recommended options.
- `workpackage_claims/WP_CONTEXT_CARD_UI_PLAN.md` — claim created and to be completed.

## Tests added/updated

Added `tests/test_context_card_ui_plan.py` covering that the plan contains:

- `context_cards.py`;
- `report-only`;
- `non-authoritative`;
- `table-first baseline`;
- `no startup source mutation`;
- `no click-to-mark`;
- `no advanced editor`;
- `no export blocking`;
- `no Scrub Key mutation`;
- `no reinsert behavior change`;
- `synthetic-only`;
- required card fields including `prefix_text`, `match_text`, `suffix_text`, `entity_type`, `review_state`, `replacement_preview`, `source`, `risk_flags`, `offset_valid`, `validation_errors`;
- serial-review relationship through `serial_review.py` and `current_item`;
- synthetic-only test values.

## Tests/checks run

Static contract review was completed against the created plan and tests.

The exact repository checkout could not be executed through the ChatGPT GitHub connector because it does not provide a checked-out repo shell/runtime.

Expected targeted command in a normal checkout:

```text
pytest tests/test_context_card_ui_plan.py
```

Expected combined helper check:

```text
pytest tests/test_context_card_ui_plan.py tests/test_context_cards.py
```

## Validation status

- Plan created and statically checked against the required contract language.
- Contract tests added but not executed in the exact GitHub checkout from this interface.
- `WORKPACKAGES.md` was re-fetched with the current SHA and updated successfully.
- `CHANGELOG.md` was re-fetched before central-doc update consideration, but the connector returned the full file in fragmented/truncated chunks. To avoid an unsafe partial overwrite, `CHANGELOG.md` was not updated in this package. Desired changelog status is recorded here.

Desired changelog entry:

```text
WP_CONTEXT_CARD_UI_PLAN — completed planning/contract-only. Added CONTEXT_CARD_UI_PLAN.md and tests/test_context_card_ui_plan.py. Planned a small report-only, non-authoritative context-card panel near the existing review table using context_cards.py. No Streamlit UI, no startup source mutation, no click-to-mark, no advanced editor, no export blocking, no Scrub Key mutation, no reinsert behavior change, no dependency change, no cloud processing and no real-data fixtures.
```

## GitHub Actions status

Unknown at handover time. A new run is expected after the final commits.

## Hugging Face sync status

Unknown at handover time. This package does not change app runtime/UI/dependencies, but sync status should still be checked if the workflow runs.

## App verification status

Not applicable. No Streamlit UI behavior changed.

## Intentionally not changed

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
- No real data.

## Commit evidence

- Claim created: `1f64969ad098b1c8745da577bb1aa3659edd12f8`
- Plan added: `41f610a778ad8627a232198318b19990277d2111`
- Contract tests added: `8a84ba3e33ea050337a2f47c6dd155f4bd278229`
- Plan wording tightened: `75d7cd6ac9fce1ef3ce2fec2acce890a8124d65d`
- Explicit no-UI wording added: `70788f63ae0077350e01293caf6c7b4931de0f65`
- Workpackages updated: `5b1afecfc0110cc93a6bfa1e53357587e4e36ccf`

## Remaining risks

- GitHub Actions and Hugging Face sync still need verification for the final commits.
- Contract tests were added but not executed in the exact repository checkout through this interface.
- `CHANGELOG.md` still needs coordinator-safe update if a worker with a full checkout can patch it without truncating the existing file.
- The plan is not a UI implementation; the context card is not visible in the app yet.

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
