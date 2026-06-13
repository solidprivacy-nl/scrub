# WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — Readiness check before replacement decision UI implementation

Status: completed readiness/specification/documentation-only  
Repository: `solidprivacy-nl/scrub`

## 1. Purpose

This readiness check decides whether the existing replacement-decision helper, UI plan and contract tests are ready for a later replacement decision UI implementation.

This package does **not** implement UI and does **not** change product code.

## 2. Executive conclusion

Replacement decision UI is **not approved to start automatically** from this readiness check.

The foundation is useful and mostly ready for a small first UI step, but only after explicit coordinator approval. The safest first UI step is:

```text
read-only / staged replacement-decision companion panel near the existing review table or serial review panel
```

It may show helper-derived decisions, suggested replacement, advisory mapping eligibility and advisory audit status. It must not write decisions back to the table, Scrub Key, export state or reinsert state.

If the coordinator wants mutating replacement actions such as `Vervangen`, `Zichtbaar houden`, `Vervanging aanpassen`, `Als context behouden` or apply-to-same-value to update the actual review table, a separate implementation package is required with explicit approval and stronger tests.

## 3. Files reviewed

Core control files reviewed:

- `PROJECT_PROMPT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Replacement/review files reviewed:

- `replacement_decision.py`
- `tests/test_replacement_decision.py`
- `REPLACE_LOGIC_UI_PLAN.md`
- `tests/test_replace_logic_ui_contract.py`
- `serial_review.py`
- `review_panel_view_model.py`
- `serial_review_panel_ui.py`
- `CONTEXT_CARD_UI_PLAN.md`
- `SERIAL_REVIEW_UI_PLAN.md`
- `presidio_streamlit.py`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `STATUS_MONITORING_RUNBOOK.md`

## 4. Current architecture state

The current review stack is now:

```text
existing review table = source of truth and fallback
serial_review.py = report-only queue helper
context_cards.py = safe context display helper
review_panel_view_model.py = combined non-mutating view model
serial_review_panel_ui.py = small non-destructive Streamlit panel
replacement_decision.py = pure decision/audit helper, not wired into mutating UI
```

`presidio_streamlit.py` currently imports and renders `serial_review_panel_ui.py` after the editable replacement table. It still applies exports from the edited replacement table, not from `replacement_decision.py` decisions.

## 5. Readiness question 1 — helper output already usable for UI

The following `replacement_decision.py` helper outputs are usable for a future UI:

### Per-decision fields

```text
occurrence_id
source_text
entity_type
display_label
suggested_replacement
final_replacement
review_state
scope
confidence
context_preview
origin
risk_flags
replacement_value
creates_mapping
```

Useful UI interpretation:

- `source_text`: what was found.
- `entity_type`: technical/category label.
- `display_label`: user-facing label.
- `suggested_replacement`: current proposed placeholder/replacement.
- `final_replacement`: future edited value, if separately approved.
- `review_state`: current intended decision state.
- `scope`: one occurrence vs same-value scope.
- `replacement_value`: derived value that would be used if applied.
- `creates_mapping`: advisory Scrub Key mapping eligibility only; it must not write a Scrub Key entry.

### Audit fields

```text
total_decisions
state_counts
ignored_items
manual_additions
context_preserved
mapping_candidates
unresolved_items
apply_to_same_value_actions
risk_flags
export_readiness
report_only
export_blocking
```

Useful UI interpretation:

- show unresolved items;
- show ignored/context-preserved items;
- show mapping candidates as advisory;
- show `export_readiness` as advisory only;
- show risk flags as warnings.

## 6. Readiness question 2 — UI actions safe as read-only or staged

Safe as read-only/staged actions:

| UI concept | Safe first behavior |
|---|---|
| `Vervangen` | Show what state would be: `accepted`; do not apply. |
| `Vervanging aanpassen` | Show a staged edited value preview; do not write to table. |
| `Zichtbaar houden` | Show what state would be: `ignored`; do not apply. |
| `Als context behouden` | Show what state would be: `preserve_context`; do not apply. |
| `Later controleren` | Show unresolved advisory state; do not apply. |
| `Alleen deze plek` | Show `this_occurrence` scope preview. |
| `Alle exact dezelfde waarden` | Show exact affected ids/count before any future apply. |
| `Alle genormaliseerde gelijke waarden` | Advisory only; requires stronger confirmation in a later package. |
| Mapping candidates | Show only; do not write Scrub Key. |
| Export readiness | Advisory only; do not block export. |

## 7. Readiness question 3 — mutating actions requiring separate approval

These are mutating and must remain blocked without a separate approved workpackage:

- changing `include` in the existing review table;
- changing `replace_with` in the existing review table;
- writing `review_status` back to table/session state;
- applying a staged `ReplacementDecision` to exports;
- applying `all_exact` or `all_normalized` to multiple rows;
- writing Scrub Key mappings;
- changing Scrub Key schema/content/lifecycle;
- changing export eligibility;
- blocking export;
- changing reinsert behavior;
- adding click-to-mark/manual document marking;
- adding advanced editor or full-document marking behavior.

## 8. Readiness question 4 — integration relationships

### Existing review table

The review table remains the source of truth. Replacement decision UI may only read from it or show staged previews until a separate package approves mutation.

Safe attachment point:

```text
existing data_editor replacement table -> staged decision preview panel -> existing table/export remains authoritative
```

### Serial review panel

The serial review panel already shows one item at a time and is non-destructive. Replacement decision UI can fit beside or below the current item area as a staged decision companion.

Safe attachment point:

```text
serial_review_panel_ui.py current_item -> build_replacement_decision(...) -> display staged decision/audit output
```

Do not change `serial_review_panel_ui.py` in this readiness package.

### Context cards

Context cards provide safe local context. Replacement decision UI should show decision controls only near current context, not as a full document editor.

Safe relationship:

```text
context card shows what/where -> replacement decision preview shows what would happen -> review table remains source of truth
```

### Scrub Key

`creates_mapping` and `mapping_candidates` are advisory only. They may be shown as “may become mapping candidate later,” but the UI must not write mappings.

Blocked without separate package:

- Scrub Key schema mutation;
- Scrub Key mapping writes;
- direct Scrub Key save from replacement decision UI;
- automatic placeholder repair.

### Export

`export_readiness` is advisory only. The future UI may show:

```text
ready_for_export
review_recommended
high_risk_unresolved
```

It must not block export or change download behavior without a separate approved package.

### Reinsert

No replacement decision UI should change reinsert behavior. Reinsert depends on existing Scrub Key/export semantics and must remain separate.

## 9. Readiness question 5 — existing contract tests

Existing tests cover useful foundations:

- `tests/test_replacement_decision.py` covers helper states, replacement value derivation, invalid state/scope/confidence rejection, exact/normalized scope matching, advisory export readiness and no Streamlit/Scrub Key dependency.
- `tests/test_replace_logic_ui_contract.py` covers label-to-state mappings, scope-to-helper mappings, plan labels, advisory export readiness, report-only audit, no export blocking, no Scrub Key behavior change, no click-to-mark approval, and synthetic-only fixtures.
- `tests/test_serial_review_helper.py`, `tests/test_review_panel_view_model.py` and serial review UI tests provide a safer one-item-at-a-time context in which a future replacement decision companion could live.

## 10. Readiness question 6 — contract tests still missing

Recommended missing contract tests before any mutating replacement decision UI:

1. `WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX` should add tests that the first implementation package cannot mutate table/session state unless explicitly approved.
2. Add static tests that a future replacement decision UI module does not write Scrub Key mappings.
3. Add static tests that it does not change export/download behavior or call export functions directly.
4. Add tests that staged decisions are clearly separated from applied table decisions.
5. Add tests for integration with `serial_review_panel_ui.py` or a future replacement panel renderer, verifying visible safety labels:
   - table-first baseline;
   - staged only / not applied;
   - no Scrub Key write;
   - no export blocking;
   - no reinsert change.
6. Add tests around `all_normalized` requiring stronger confirmation or being disabled in the first UI implementation.
7. Add tests that `creates_mapping` is shown as advisory and never used as direct persistence.
8. Add tests for `ReplacementDecision.as_dict()` to expose explicit `report_only` / `mutation_allowed` fields, or document why only the audit has those fields.

## 11. Readiness question 7 — smallest safe first UI step

Smallest safe first UI step:

```text
WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX
```

Then, only after explicit coordinator approval:

```text
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — read-only/staged replacement decision companion panel
```

The first UI implementation should:

- sit near the existing review table / serial review panel;
- build `ReplacementDecision` objects from the selected row/current item;
- display suggested state, scope, replacement value and mapping eligibility;
- show audit/readiness labels as advisory;
- not write anything back;
- not add apply buttons that mutate state;
- not affect export, Scrub Key or reinsert.

## 12. Readiness question 8 — visible user boundaries

The future UI must visibly keep these boundaries:

```text
table-first baseline
staged preview only
not applied to export
no Scrub Key write
no export blocking
no reinsert behavior change
no fuzzy matching
no guessed intent
no click-to-mark
no advanced editor
no full-document marking
```

Suggested Dutch labels:

```text
Vervangtabel blijft leidend
Voorvertoning — nog niet toegepast
Wijzigt geen Scrub Key
Blokkeert geen export
Wijzigt terugplaatsen niet
Geen document-editor
```

## 13. Readiness verdict

| Area | Status | Notes |
|---|---|---|
| Helper-first foundation | Ready for read-only/staged UI | `replacement_decision.py` is pure and reusable. |
| UI plan | Mostly ready | Still predates completed serial review UI; readiness document updates placement guidance. |
| Contract tests | Sufficient for plan-level safety | Not sufficient yet for a mutating UI implementation. |
| Integration point | Available | Best near serial review panel/current review row, not export/Scrub Key/reinsert. |
| Mutating decisions | Not ready | Requires separate approval and stronger tests. |
| Scrub Key writes | Blocked | Must remain separate. |
| Export blocking | Blocked | Must remain separate. |
| Reinsert changes | Blocked | Must remain separate. |

Final verdict:

```text
Do not start replacement decision UI implementation automatically.
First run WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX if the coordinator wants stronger safeguards.
Only after explicit coordinator approval may WP_REPLACE_LOGIC_UI_IMPLEMENTATION start, and the first version should be read-only/staged.
```

## 14. Explicit non-changes in this package

This readiness package did not change:

- Streamlit UI;
- `presidio_streamlit.py`;
- `serial_review_panel_ui.py`;
- review table behavior;
- replacement mutation behavior;
- automatic replacement behavior;
- Scrub Key behavior;
- Scrub Key schema;
- Scrub Key mapping writes;
- export/download behavior;
- export blocking;
- reinsert behavior;
- dependencies;
- cloud processing;
- real-data fixtures;
- click-to-mark;
- advanced editor;
- full-document marking.

## 15. Recommended next steps

1. `WP39D-VERIFY` if DOCX hygiene audit UI is ready for closeout/app verification.
2. `WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX` if the coordinator wants stronger contract tests before UI implementation.
3. `WP_REPLACE_LOGIC_UI_IMPLEMENTATION` only after separate explicit coordinator approval.

Do not start these without separate approval:

- replacement decision UI implementation;
- click-to-mark;
- advanced editor;
- full-document marking;
- export blocking;
- Scrub Key schema/write behavior changes.
