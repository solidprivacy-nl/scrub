# Handover — WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — Readiness check before replacement decision UI implementation`

Status: completed readiness/specification/documentation-only.

## Summary

Completed a readiness review for future replacement decision UI implementation.

The conclusion is conservative:

```text
Replacement decision UI must not start automatically.
The helper and plans are sufficient for a small read-only/staged companion panel direction.
Mutating replacement actions require separate coordinator approval and stronger contract tests.
```

The readiness document answers the required questions about helper output, safe staged UI actions, mutating actions, integration with review table / serial review / context cards / Scrub Key / export / reinsert, existing contract tests, missing contract tests, smallest safe UI step and visible boundaries.

## Files added

- `REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS.md`
- `handover/workpackages/20260613_1240_replace_logic_ui_implementation_readiness.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS.md` — claim created as `in_progress`; final completion update follows this handover.

## Tests/checks run

No shell tests were run.

Reason:

```text
This is readiness/specification/documentation-only. No product code, UI code or runtime behavior changed.
```

Repository files were reviewed through the GitHub connector. The status check available through the connector returned no visible combined statuses for the latest documentation commit at handover time.

Optional checks if desired in CI:

```text
pytest tests/test_replace_logic_ui_contract.py
pytest tests/test_review_panel_view_model.py tests/test_serial_review_helper.py tests/test_context_cards.py
```

## Validation status

- Readiness document added.
- Central status updated in `WORKPACKAGES.md`.
- Changelog updated.
- Risk register updated under R6.
- No app rebuild required.
- No product tests required for this documentation-only package.

## GitHub Actions status

Unknown at handover time. `get_commit_combined_status` returned no visible statuses for the latest documentation commit checked through the connector.

## Hugging Face sync status

Unknown / not verified at handover time. This package does not require Hugging Face app verification because it does not change UI/runtime behavior.

## App verification status

Not applicable. No Streamlit UI, product code, startup/runtime behavior, review table behavior, export/download behavior, Scrub Key behavior or reinsert behavior changed.

## Readiness findings

### Ready / usable

- `replacement_decision.py` is pure and helper-first.
- It exposes useful decision fields: `occurrence_id`, `source_text`, `entity_type`, `display_label`, `suggested_replacement`, `final_replacement`, `review_state`, `scope`, `confidence`, `context_preview`, `origin`, `risk_flags`, `replacement_value`, `creates_mapping`.
- It exposes useful audit fields: `state_counts`, `mapping_candidates`, `unresolved_items`, `apply_to_same_value_actions`, `risk_flags`, `export_readiness`, `report_only`, `export_blocking`.
- Existing tests cover review states, scopes, exact/normalized matching and advisory export readiness.

### Not ready without stronger safeguards

- Mutating replacement decision UI is not ready to start automatically.
- There are no dedicated contract tests yet for staged-vs-applied UI state.
- There are no dedicated static tests yet proving a future replacement UI does not mutate table/session state, Scrub Key, export/download or reinsert behavior.
- `all_normalized` needs stronger confirmation or should be disabled in the first UI.
- `creates_mapping` must remain advisory and must not be used to write Scrub Key mappings.

## Intentionally not changed

- No Streamlit UI implementation.
- No changes to `presidio_streamlit.py`.
- No changes to `serial_review_panel_ui.py`.
- No product code changes.
- No review table behavior change.
- No replacement mutation implementation.
- No automatic replacement.
- No Scrub Key writes.
- No Scrub Key schema change.
- No export blocking.
- No export/download behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real data.
- No click-to-mark.
- No advanced editor.
- No full-document marking.

## Remaining risks

- A future replacement decision UI could accidentally duplicate or conflict with the existing editable replacement table if its staged/applied boundary is not explicit.
- A future implementation could accidentally treat `creates_mapping` as permission to write Scrub Key mappings. This must remain blocked.
- `all_normalized` is conservative but broader than exact matching; it should require stronger confirmation or remain unavailable in the first UI implementation.
- UI implementation should wait for explicit coordinator approval.

## Next recommended step

Recommended order:

1. `WP39D-VERIFY` if DOCX hygiene audit UI is ready for closeout/app verification.
2. `WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX` if stronger replacement UI contract coverage is desired.
3. `WP_REPLACE_LOGIC_UI_IMPLEMENTATION` only after separate explicit coordinator approval.

Do not start without separate approval:

- replacement decision UI implementation;
- click-to-mark;
- advanced editor;
- full-document marking;
- export blocking;
- Scrub Key schema/write behavior changes.
