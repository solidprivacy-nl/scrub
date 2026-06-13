# Handover — WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK — Hide non-intuitive replacement helper panel from main UI`

Coordinator feedback:

```text
Replacement decision helper werkt, maar is niet een intuïtieve gebruiksvriendelijke functionaliteit. Het maakt het eerder onoverzichtelijker en complexer dan dat het de verwerking intuïtiever maakt.
```

Status: completed product rollback/hide; awaiting GitHub Actions, Hugging Face sync and app verification because UI/runtime behavior changed.

## Summary

The technically working replacement decision helper panel is no longer considered a successful user-facing feature. It has been removed from the normal Scrub Legal UI flow.

The helper and contract assets are preserved for a later redesign:

- `replacement_decision.py`
- `REPLACE_LOGIC_UI_PLAN.md`
- `tests/test_replace_logic_ui_contract.py`
- `replacement_decision_panel_ui.py` as parked/unused technical helper UI code

The review table remains the source of truth and fallback. The serial review UI remains visible.

## Files added

- `workpackage_claims/WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK.md`
- `handover/workpackages/20260613_1525_replace_logic_ui_product_rollback.md`

## Files changed

- `serial_review_panel_ui.py`
- `tests/test_replace_logic_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK.md`

## Tests added/updated

Updated `tests/test_replace_logic_ui_patch.py` so it now verifies:

- replacement helper and contract assets still exist;
- `presidio_streamlit.py` still renders the serial review panel;
- `serial_review_panel_ui.py` no longer imports or calls the replacement decision helper panel;
- the normal Scrub flow no longer contains `Replacement decision helper` or `replacement_decision_preview`;
- serial review remains available and table-first;
- parked `replacement_decision_panel_ui.py` still documents non-mutating boundaries;
- no Scrub Key, export/download or reinsert calls are introduced from the normal flow;
- no automatic replacement, click-to-mark, advanced editor or full-document marking was added;
- no startup source mutation, cloud processing or real-data fixture was added.

## Tests/checks run

No shell/pytest/py_compile execution was available through the ChatGPT GitHub connector.

Expected checks:

```text
python -m py_compile presidio_streamlit.py
python -m py_compile serial_review_panel_ui.py
pytest tests/test_replace_logic_ui_patch.py
pytest tests/test_replace_logic_ui_contract.py tests/test_replacement_decision.py
pytest
```

Source checks through GitHub connector:

- `serial_review_panel_ui.py` now only imports `build_review_panel_view_model`; it no longer imports `replacement_decision_panel_ui`.
- The serial review current-item/context rendering remains intact.
- The call to `render_replacement_decision_panel(...)` has been removed.
- `presidio_streamlit.py` was read and not changed.
- `replacement_decision_panel_ui.py` remains present but is parked/unused in the normal user flow.

## Validation status

Rollback/hide committed. Runtime validation pending.

Because this changes UI/runtime behavior, required follow-up evidence is:

```text
1. GitHub Actions green.
2. Sync to Hugging Face Space green.
3. Coordinator app verification screenshot.
```

## GitHub Actions status

Unknown at handover time. Must be checked for the final claim/rollback commit.

## Hugging Face sync status

Unknown at handover time. Must be checked after Actions.

## App verification status

Pending and required because UI/runtime behavior changed.

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- review table remains visible;
- serial review panel remains visible;
- replacement decision helper panel is not visible in the normal flow;
- export/download remains visible;
- DOCX hygiene audit remains visible;
- no static-highlight startup error.

## Boundaries preserved

- No new replacement UI design or implementation.
- No mutating replacement decision implementation.
- No automatic replacement.
- No review table behavior change.
- No serial review behavior change except hiding/removing the helper panel.
- No Scrub Key writes or schema change.
- No export blocking.
- No export/download behavior change.
- No reinsert behavior change.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No dependency change.
- No cloud processing.
- No real data.

## Remaining risks

- Replacement UX is still not solved; the first helper-internals panel was product-rejected.
- Future replacement UX needs a redesign based on user intuition rather than exposing raw helper/audit internals.
- Any mutating replacement behavior remains blocked until separate approval and stronger tests.

## Next recommended step

```text
Verify GitHub Actions and Hugging Face sync for WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK.
```

Then request app verification screenshot.

After that, the next design package can be considered only with separate coordinator approval:

```text
WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — design a genuinely intuitive replacement review flow.
```

Do not start without separate coordinator approval:

```text
new replacement UI implementation
mutating replacement decisions
automatic replacement
Scrub Key writes
export blocking
click-to-mark
advanced editor
full-document marking
```
