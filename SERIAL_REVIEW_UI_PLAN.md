# WP_SERIAL_REVIEW_UI_PLAN — Contract for a future serial review panel

Status: planning/contract-only  
Repository: `solidprivacy-nl/scrub`

## 1. Purpose

This plan defines the UI contract for a future small serial review panel. It prepares `WP_SERIAL_REVIEW_UI`, but it does not implement UI.

The panel goal is:

```text
one finding at a time -> context -> suggested replacement -> safe explicit review action -> next item
```

The existing table-first baseline remains the working review baseline and fallback. The serial panel may assist review, but it must not replace the review table, mutate review rows, change export behavior, write Scrub Key mappings or change reinsert behavior.

## 2. Source helpers

The future panel may consume data from:

```text
serial_review.py
replacement_decision.py
context_cards.py
```

The first UI must treat `serial_review.py` as the queue/source-of-view helper. It may use `context_cards.py` only for safe escaped context snippets. It may use `replacement_decision.py` mappings only as a contract for future explicit review actions.

## 3. Serial helper output fields the UI may show

The future panel may show these `build_serial_review_queue` fields from `serial_review.py`:

```text
current_item
previous_item
next_item
unresolved_count
high_risk_count
duplicate_exact_value_count
same_value_occurrence_ids
report_only
mutation_allowed
```

For `current_item`, `previous_item` and `next_item`, the panel may show these item fields:

```text
occurrence_id
source_text
entity_type
suggested_replacement
review_state
confidence
context_preview
risk_flags
is_unresolved
is_high_risk
is_high_risk_unresolved
report_only
mutation_allowed
```

The first UI may display `audit_summary` as advisory status only. It must not use `audit_summary.review_readiness` to block export in this package.

## 4. Context display contract

The serial panel should show the selected finding in context.

Allowed context sources:

```text
current_item.context_preview
context_cards.py escaped prefix/match/suffix output
synthetic-only examples
```

Rendering safety:

- source text must be escaped before any HTML rendering;
- raw user text must not be rendered as raw HTML;
- invalid offsets from future context-card inputs must be shown as a report-only warning, not repaired by fuzzy matching;
- no source text should be logged from UI-only state.

## 5. Navigation labels

The future UI may use these navigation labels:

| UI label | Meaning |
|---|---|
| Vorige | Move to the previous available serial item. |
| Volgende | Move to the next available serial item. |
| Volgende onopgeloste | Move to the next unresolved item from `next_item` or helper navigation output. |

Navigation is view-state only. It must be non-destructive.

## 6. Review action labels and state mapping

The future UI may use these action labels:

| UI label | Helper state |
|---|---|
| Later controleren | `unresolved` |
| Vervangen | `accepted` |
| Vervanging aanpassen | `edited` |
| Zichtbaar houden | `ignored` |
| Als context behouden | `preserve_context` |

Additional state display values from `serial_review.py` may be displayed when they come from the helper:

```text
needs_review
manual_added
high_risk_unresolved
```

`manual_added` is display-only in this first serial panel contract because this package does not approve click-to-mark or manual document marking. `high_risk_unresolved` is a serial review risk state and should remain visible as a warning.

## 7. Scope labels and matching contract

The future UI may use these scope labels:

| UI label | Helper scope |
|---|---|
| Alleen deze plek | `this_occurrence` |
| Alle exact dezelfde waarden | `all_exact` |

Rules:

- default scope is `this_occurrence`;
- `all_exact` may only use `same_value_occurrence_ids` / exact same-value matching;
- show `duplicate_exact_value_count` before a future apply-to-same-value action;
- no fuzzy matching;
- no guessed intent;
- `all_normalized` from `replacement_decision.py` is not part of the first serial review panel contract.

## 8. Boundary language

The future serial review panel must keep these boundaries:

```text
table-first baseline
non-destructive
report-only until approved
no export blocking
no Scrub Key mutation
no reinsert behavior change
no startup source mutation
no click-to-mark
no advanced editor
synthetic-only boundary
```

Expanded meaning:

- the existing review table remains the authoritative control/audit surface and fallback;
- the panel is a helper-driven review aid, not the source of truth;
- until a later approved implementation changes this, the UI must preserve `report_only = True` and `mutation_allowed = False`;
- the panel must not block export;
- the panel must not write Scrub Key mappings or mutate Scrub Key schema/content;
- the panel must not change reinsert behavior;
- the panel must not mutate `presidio_streamlit.py` through startup source mutation;
- the panel must not implement click-to-mark;
- the panel must not implement an advanced editor;
- tests and examples must be synthetic-only and must not contain real personal data.

## 9. Placement and fallback

Recommended future placement:

```text
review guidance
small serial review panel
existing review table
export/audit summary
```

The review table remains visible or reachable as the table-first baseline. The serial review panel must not hide or replace the existing review table.

## 10. Explicit non-changes

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

## 11. Validation contract

Before any UI package, contract tests should verify:

- this plan exists;
- helper output fields are listed;
- UI labels are present;
- state mappings align with `serial_review.py` and `replacement_decision.py`;
- scope mappings align with `replacement_decision.py`;
- boundary language remains intact;
- synthetic-only examples are used.

## 12. Next recommended step

Only after coordinator approval:

```text
WP_SERIAL_REVIEW_UI — small non-destructive serial review panel in Streamlit.
```
