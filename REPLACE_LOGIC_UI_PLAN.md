# WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration

Status: planning/documentation-only  
Repository: `solidprivacy-nl/scrub`

## 1. Purpose

This plan defines how the `replacement_decision.py` helper may later be integrated into the review UI.

It does not implement UI.

The goal is to make replacement review easier while preserving the current safety boundaries:

```text
found item -> suggested replacement -> user decision -> scope -> audit
```

## 2. Current helper contract

The future UI may consume helper concepts from `replacement_decision.py`:

```text
ReplacementDecision
build_replacement_decision
matching_occurrence_ids
build_replacement_audit
```

Important helper fields:

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

Important helper states:

```text
needs_review
accepted
edited
ignored
manual_added
preserve_context
unresolved
```

Important helper scopes:

```text
this_occurrence
all_exact
all_normalized
```

## 3. Design principle

The first UI integration should simplify decisions, not add a complex editor.

The user-facing flow should be:

```text
1. See the item in context.
2. See the suggested replacement.
3. Choose Replace, Keep, Edit, Add missed item or Mark as context.
4. Choose scope only when needed.
5. See unresolved items before export.
```

The UI must keep legal/professional context readable and must not imply that output is automatically risk-free.

## 4. Recommended placement

Future placement should be close to the current review table and, now that the serial review panel exists, may also sit close to the current serial review item:

```text
Review guidance
Serial review / context card area
Replacement decision companion panel — staged preview only
Existing replacement table as audit/control fallback
```

Do not place replacement-decision controls in:

- Scrub Key export/import flow;
- reinsert flow;
- export/download flow;
- PDF-to-TXT reinsert flow;
- DOCX restored-output flow.

## 5. User-facing actions

Recommended first visible actions:

```text
Vervangen
Zichtbaar houden
Vervanging aanpassen
Toepassen op exact dezelfde waarde
Handmatig gemiste waarde toevoegen
Als context behouden
Later controleren
```

Mapping to helper states:

| UI action | Helper state |
|---|---|
| Vervangen | `accepted` |
| Vervanging aanpassen | `edited` |
| Zichtbaar houden | `ignored` |
| Handmatig gemiste waarde toevoegen | `manual_added` |
| Als context behouden | `preserve_context` |
| Later controleren | `unresolved` |

## 6. Scope controls

Scope controls should be hidden by default and shown only when the user chooses to apply a decision beyond one occurrence.

Recommended labels:

| UI label | Helper scope |
|---|---|
| Alleen deze plek | `this_occurrence` |
| Alle exact dezelfde waarden | `all_exact` |
| Alle genormaliseerde gelijke waarden | `all_normalized` |

Safety rules:

- Default scope is `this_occurrence`.
- `all_exact` must show affected count before applying.
- `all_normalized` must require a stronger confirmation.
- No fuzzy matching or guessed intent is allowed.
- `all_normalized` is not available as a first mutating UI scope without separate explicit coordinator approval.
- A first UI may show `all_normalized` as disabled/advisory only, or omit it entirely.

## 7. Decision panel fields

For one selected item, show:

```text
Context preview
Detected label
Suggested replacement
Final replacement editor
Decision state
Scope selector
Affected count
Risk flags / notes
```

Advanced technical fields should stay in a collapsible details area.

## 8. Audit panel

The future UI may display helper audit output:

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
```

The audit panel is report-only. It must not block export in this package.

## 9. Export readiness language

Use careful advisory wording:

| Helper value | Suggested UI meaning |
|---|---|
| `ready_for_export` | Review decisions are complete, but output still needs normal human confidence check. |
| `review_recommended` | Some items still need review. |
| `high_risk_unresolved` | Important unresolved items remain; do not treat the result as final. |

This UI plan does not approve export blocking.

`export_readiness` is advisory only. It must not call export/download functions, change export eligibility, disable export buttons or alter download payloads.

## 10. Scrub Key boundary

The first UI plan must not change Scrub Key behavior.

Allowed future UI behavior:

- show which accepted/edited/manual decisions may become mapping candidates;
- show that ignored/context items do not need mappings;
- show unresolved decisions before export.

Not allowed in this plan:

- changing Scrub Key schema;
- writing mappings directly from a new UI panel;
- auto-repairing duplicate placeholders;
- changing placeholder format.

`creates_mapping` is advisory only. It does not authorize a Scrub Key write.

`mapping_candidates` are advisory only. They do not authorize Scrub Key persistence.

## 11. Static preview relationship

If the future static highlight preview exists, the replacement decision panel may use the selected item from that preview.

Boundary:

```text
Highlight preview remains read-only and non-authoritative.
Replacement table / decision model remains the authoritative decision surface.
```

No click-to-mark implementation is approved by this plan.

## 12. Staged-vs-applied contract

A future replacement decision UI must separate staged UI intent from applied product state.

Contract language:

```text
staged decision preview only
staged decision state is not applied state
existing review table remains source of truth and fallback
no review table mutation
no replacement mutation
no automatic replacement
no export/download calls
no reinsert behavior change
no Scrub Key writes
```

The first implementation may build `ReplacementDecision` objects for display, but it must not write those decisions back to:

- the existing review table;
- `edited_replacements_df`;
- Streamlit data-editor state;
- Scrub Key memory or files;
- export payloads;
- reinsert payloads.

If later approved, mutating behavior must be implemented in a separate package with explicit coordinator approval and dedicated tests.

## 13. Session-state contract

A future non-mutating replacement decision companion panel may use only view-only session-state keys.

Allowed view-only session keys:

```text
replacement_decision_selected_occurrence_id
replacement_decision_preview_state
replacement_decision_preview_scope
replacement_decision_preview_text
replacement_decision_panel_expanded
```

These keys are allowed only for temporary UI selection and preview state. They must not be treated as applied replacement state.

Forbidden session-state behavior:

- no mutation of `replacement_editor`;
- no mutation of `edited_replacements_df`;
- no mutation of review table rows;
- no mutation of export state;
- no mutation of Scrub Key state;
- no mutation of reinsert state.

## 14. Minimum implementation sequence

Required pre-implementation contract package:

```text
WP_REPLACE_LOGIC_UI_CONTRACT_TESTS
```

Recommended sequence:

```text
1. Add UI contract tests around labels/states/scopes and staged-vs-applied boundaries.
2. Add a non-mutating decision panel prototype behind an expander only after separate explicit coordinator approval.
3. Use synthetic examples only.
4. Keep the existing table flow as fallback.
5. Verify Actions and Hugging Face sync.
6. Ask for app verification because UI behavior changed.
```

## 15. Explicit non-changes

This plan does not change:

- `presidio_streamlit.py`;
- `serial_review_panel_ui.py`;
- `fix_streamlit_nested_expanders.py`;
- review table behavior;
- replacement mutation behavior;
- export/download behavior;
- Scrub Key behavior;
- reinsert behavior;
- helper runtime behavior;
- dependencies;
- cloud processing;
- real-data fixtures.

This plan does not approve:

- Streamlit UI implementation;
- automatic replacement;
- review table mutation;
- replacement mutation;
- Scrub Key writes;
- Scrub Key schema changes;
- export blocking;
- export/download calls;
- reinsert behavior changes;
- click-to-mark;
- advanced editor;
- full-document marking.

## 16. Next recommended step

Recommended next package after this gap-fix:

```text
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — only after separate explicit coordinator approval.
```

Do not start implementation automatically. A later implementation must begin as a small staged/read-only companion panel unless a separate approved package explicitly allows mutation.
