# Handover — WP_REPLACE_LOGIC_UI_IMPLEMENTATION

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REPLACE_LOGIC_UI_IMPLEMENTATION — Small staged/read-only replacement decision companion panel`

Coordinator approval noted: explicit.

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

## Summary

Implemented the first small staged/read-only replacement decision companion panel.

The panel uses `replacement_decision.py` to show a preview/audit for a selected review item. It is rendered from the existing serial review area and remains advisory only. The existing review table remains the source of truth and fallback.

No replacement decision is applied. No existing review table rows are mutated. No Scrub Key mapping is written. Export/download behavior and reinsert behavior remain unchanged.

## Files added

- `replacement_decision_panel_ui.py`
- `tests/test_replace_logic_ui_patch.py`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_IMPLEMENTATION.md`
- `handover/workpackages/20260613_1505_replace_logic_ui_implementation.md`

## Files changed

- `serial_review_panel_ui.py`
- `tests/test_replace_logic_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_IMPLEMENTATION.md`

## Tests added/updated

Added `tests/test_replace_logic_ui_patch.py` with static coverage for:

- app reaches the panel through the existing serial review panel;
- renderer uses `build_replacement_decision`, `matching_occurrence_ids` and `build_replacement_audit` from `replacement_decision.py`;
- required visible boundary text:
  - `Replacement decision helper`;
  - `staged decision preview only`;
  - `staged decision state is not applied state`;
  - `existing review table remains source of truth and fallback`;
  - `no review table mutation`;
  - `no automatic replacement`;
  - `no Scrub Key writes`;
  - `no export blocking`;
  - `no reinsert behavior change`;
- Dutch boundary labels such as `Vervanghulp`, `Alleen voorbeeld / nog niet toegepast`, `Bestaande vervangtabel blijft leidend`, `Geen automatische vervanging`, `Geen Scrub Key wijziging`, `Export wordt niet geblokkeerd` and `Terugzetten/originele waarden blijft ongewijzigd`;
- advisory helper fields such as selected/source text, suggested replacement, decision state, scope, affected count, mapping candidates, export readiness, unresolved items and risk flags;
- only allowed view-only session/widget keys;
- no mutation of `edited_replacements_df`, review table or data-editor state;
- no export/download, Scrub Key or reinsert function calls;
- no fuzzy matching, guessed intent, startup source mutation, click-to-mark, advanced editor, full-document marking, cloud processing or real-data examples.

## Tests/checks run

No shell/pytest/py_compile execution was available through the ChatGPT GitHub connector.

Expected checks:

```text
python -m py_compile serial_review_panel_ui.py
python -m py_compile replacement_decision_panel_ui.py
pytest tests/test_replace_logic_ui_patch.py
pytest tests/test_replace_logic_ui_contract.py tests/test_replacement_decision.py
pytest
```

Static source checks through GitHub connector:

- `replacement_decision_panel_ui.py` was added.
- `serial_review_panel_ui.py` imports and renders `render_replacement_decision_panel(...)` from the existing serial review area.
- `presidio_streamlit.py` still calls `render_serial_review_panel(...)`; it was not changed in this package.
- No export/download files or Scrub Key/reinsert files were changed.

## Validation status

Implementation committed. Runtime validation pending.

Because this changes UI/runtime behavior, closeout requires:

```text
1. GitHub Actions green.
2. Sync to Hugging Face Space green.
3. Coordinator app verification screenshot.
```

## GitHub Actions status

Unknown at handover time. Must be checked for the final claim/implementation commit.

## Hugging Face sync status

Unknown at handover time. Must be checked after Actions.

## App verification status

Pending and required.

App verification should confirm:

- app starts without Script execution error;
- normal Scrub Legal interface remains visible;
- existing review table remains visible;
- serial review panel remains visible;
- replacement decision helper panel is visible;
- panel says clearly that it is staged/read-only/not applied;
- existing replacement table remains source of truth and fallback;
- no automatic replacement;
- no Scrub Key change;
- no export blocking;
- no reinsert change;
- no static-highlight startup error.

## Boundaries preserved

- No review table mutation.
- No `edited_replacements_df` mutation.
- No Streamlit data-editor state mutation.
- No automatic replacement.
- No Scrub Key writes.
- No Scrub Key schema change.
- No mapping persistence.
- No export blocking.
- No export/download calls or behavior change.
- No reinsert behavior change.
- No fuzzy matching or guessed intent.
- No click-to-mark.
- No advanced editor.
- No full-document marking.
- No dependency change.
- No cloud processing.
- No real data.

## Remaining risks

- The panel is preview-only and does not yet simplify actual table editing.
- Mutating replacement decision behavior remains blocked until a separate explicit approval and dedicated tests.
- The table-first review table remains the authoritative surface for actual replacement decisions and export.

## Next recommended step

```text
WP_REPLACE_LOGIC_UI_VERIFY — closeout/app verification for replacement decision helper panel after green Actions and Hugging Face sync.
```

Do not start without separate coordinator approval:

```text
mutating replacement decision implementation
automatic replacement
Scrub Key write behavior
export blocking
click-to-mark
advanced editor
full-document marking
```
