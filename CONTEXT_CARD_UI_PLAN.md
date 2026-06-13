# WP_CONTEXT_CARD_UI_PLAN — Non-authoritative context-card panel near review table

Status: planning/contract-only  
Repository: `solidprivacy-nl/scrub`

## 1. Purpose

This plan defines a small, non-authoritative context-card panel near the existing review table.

The panel may later consume `context_cards.py` to show a local prefix/match/suffix context card for one selected review item. It must help reviewers see document context without restarting the failed full-document marking/editor route.

This plan does not implement UI.

The current table-first baseline remains the working baseline and fallback.

## 2. Governing boundary

This plan follows the post-rollback route:

```text
helper/model first -> contract tests first -> small approved non-destructive UI panel later
```

It must not reintroduce:

- startup source mutation;
- full-document marking;
- click-to-mark;
- advanced editor behavior;
- broad document-centric Streamlit rewrite;
- review table mutation;
- export/download behavior changes;
- Scrub Key mutation;
- reinsert behavior change;
- dependency changes;
- cloud processing;
- real-data fixtures.

Contract wording:

```text
no Streamlit UI implementation
no startup source mutation
no full-document marking
no click-to-mark
no advanced editor
no review table mutation
no export blocking
no Scrub Key mutation
no reinsert behavior change
no dependency changes
no cloud processing
synthetic-only
```

The future panel is context-assistive only. It is report-only, non-authoritative and synthetic-only in tests.

## 3. Placement

Recommended placement in the existing review workflow:

```text
Review guidance / warnings
Optional serial review controls
Context-card panel — non-authoritative, report-only
Existing review table — authoritative audit/control surface
Export / Scrub Key / reinsert areas remain separate
```

Preferred first UI shape, if later approved:

- a compact panel above the existing review table; or
- a narrow side/detail panel directly beside the selected table row area; or
- a collapsed/expandable context card immediately before the table.

The panel should be close enough to the review table that the user understands it belongs to the currently selected row. It must not replace the table and must not claim to be the source of truth.

Required visible placement message:

```text
Table-first baseline: the review table remains the authoritative control and fallback.
```

## 4. Panel labels

The panel must show clear safety labels:

```text
Alleen contextweergave
Niet autoritatief
Wijzigt geen Scrub Key
Blokkeert geen export
Geen document editor
```

English contract wording for tests and handover:

```text
context-only display
non-authoritative
no Scrub Key mutation
no export blocking
no document editor
```

## 5. Data source and helper contract

The future panel may consume the existing helper:

```text
context_cards.py
build_context_card
build_context_cards
```

The helper output is already bounded as:

```text
report-only
mutation_allowed = False
export_blocking = False
scrub_key_changes = False
raw_html_allowed = False
automatic_replacement = False
fuzzy_matching = False
document_editor_state = False
```

The panel must treat those helper outputs as display data only.

It must not write decisions, mappings, Scrub Key data, export eligibility or reinsert state.

## 6. Required fields

The context-card panel must be able to display these fields from a helper output or compatible view model:

```text
prefix_text
match_text
suffix_text
entity_type
review_state
replacement_preview
source
risk_flags
offset_valid
validation_errors
```

Recommended display order:

1. safety labels;
2. `prefix_text` + emphasized `match_text` + `suffix_text`;
3. `entity_type`, `review_state`, `replacement_preview`;
4. `source`, `risk_flags`;
5. offset status: `offset_valid` and `validation_errors`.

If `offset_valid` is false, the panel should show the validation errors and should not try to guess the intended text.

## 7. Review states

The context card may reflect review states already present in the existing review data or serial review helper:

```text
needs_review
accepted
edited
ignored
manual_added
preserve_context
unresolved
high_risk_unresolved
```

The panel may use state labels to help the user understand why an item still needs attention.

It must not change the state.

## 8. Relationship with serial_review.py

A future serial review panel may use `serial_review.py` as the driver for one selected item.

Allowed relationship:

```text
serial_review.py current_item -> occurrence_id / source_text / entity_type / review_state / replacement_preview -> context_cards.py -> context-card panel
```

Rules:

- `current_item` from `serial_review.py` can select which context card to show.
- next/previous review stays helper-driven by `serial_review.py`.
- the context card mutates nothing.
- the context card is report-only.
- the context card is non-authoritative.
- the review table remains the source of truth for decisions until a later approved package changes that.

The context card may show `same_value_occurrence_ids` or duplicate warnings from serial review as labels only. It must not apply a decision to same-value occurrences.

## 9. Invalid offsets and safety behavior

The panel must not perform fuzzy matching or guessed intent.

If offsets are invalid:

```text
offset_valid = False
validation_errors are shown
no automatic replacement
no click-to-mark fallback
no hidden mutation
```

Invalid cards should degrade to an error/warning card beside the table, not to a full document editor.

## 10. Accessibility and clarity

The panel should not rely on color alone.

Minimum requirements for a future UI package:

- visible text labels for review state and risk flags;
- clear warning for invalid offsets;
- short context window to prevent overload;
- table row / occurrence id reference;
- fallback to table-only review if context is unavailable.

## 11. Not-goals

This plan explicitly does not approve:

- Streamlit UI implementation;
- changes to `presidio_streamlit.py`;
- changes to `fix_streamlit_nested_expanders.py`;
- startup source mutation;
- full-document marking;
- click-to-mark;
- inline editing;
- advanced editor;
- Word/PDF layout rendering;
- export blocking;
- Scrub Key mutation;
- reinsert behavior change;
- review table mutation;
- dependency changes;
- cloud processing;
- real-data fixtures.

Additional explicit contract wording:

```text
no inline editing
no Word/PDF layout rendering
```

## 12. Implementation sequence after this plan

Recommended next packages:

```text
1. WP_CONTEXT_CARD_UI_CONTRACT_TESTS — lock labels, fields and boundaries.
2. WP_REVIEW_PANEL_VIEW_MODEL_HELPER — optional pure helper combining serial queue + context card view model.
3. A later explicitly approved UI package — small non-destructive context-card panel near the review table.
```

Do not start Streamlit UI implementation without explicit coordinator approval.

## 13. Validation approach

Contract validation should check that this plan contains:

```text
context_cards.py
report-only
non-authoritative
table-first baseline
no startup source mutation
no full-document marking
no click-to-mark
no advanced editor
no export blocking
no Scrub Key mutation
no reinsert behavior change
synthetic-only
```

Tests must use synthetic-only text and must not include real personal data.

## 14. Final recommendation

The safest next review UX step is not a full document editor. It is a small context-card panel beside the current review table, driven by helpers and explicitly labelled as context-only, report-only and non-authoritative.

This provides document context while preserving the current stable table-first baseline.
