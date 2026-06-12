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

Future placement should be close to the current review table:

```text
Review guidance
Optional static preview / context area
Replacement decision panel
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

## 11. Static preview relationship

If the future static highlight preview exists, the replacement decision panel may use the selected item from that preview.

Boundary:

```text
Highlight preview remains read-only and non-authoritative.
Replacement table / decision model remains the authoritative decision surface.
```

No click-to-mark implementation is approved by this plan.

## 12. Minimum implementation sequence

Recommended sequence:

```text
1. Add UI contract tests around labels/states/scopes.
2. Add a non-mutating decision panel prototype behind an expander.
3. Use synthetic examples only.
4. Keep the existing table flow as fallback.
5. Verify Actions and Hugging Face sync.
6. Ask for app verification because UI behavior changed.
```

## 13. Explicit non-changes

This plan does not change:

- `presidio_streamlit.py`;
- `fix_streamlit_nested_expanders.py`;
- review table behavior;
- export/download behavior;
- Scrub Key behavior;
- reinsert behavior;
- helper runtime behavior;
- dependencies;
- cloud processing;
- real-data fixtures.

## 14. Next recommended step

Recommended next package:

```text
WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration
```

Only after that should a small UI implementation package be considered.
