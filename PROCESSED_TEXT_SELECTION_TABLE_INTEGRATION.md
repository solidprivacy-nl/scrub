# Processed-text selection table integration

Status: implementation under validation  
Workpackage: `SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION`  
Repository: `solidprivacy-nl/scrub`  
Date: 2026-08-04 Europe/Amsterdam

## User flow

```text
select unmasked text in Verwerkte tekst
→ right-click, Shift+F10 or Masker selectie
→ server inspects the exact selection and impact
→ choose a broad type
→ server revalidates current document and table
→ append one normal document-scoped manual row
→ immediate rerun
→ preview and authoritative table show the result
```

Version one masks all safe exact occurrences. One-occurrence-only replacement remains out of scope.

## Production architecture

The local component remains transport-only. `processed_text_selection_integration.py` coordinates caller-owned document-scoped state and the pure action model. `presidio_streamlit.py` remains responsible for visible feedback and immediate reruns.

Events are rendered before the editable table but processed only after `st.data_editor` has returned the current rows. Processing occurs before serial review and every export control. This prevents an export from using a half-processed selection event.

A commit appends exactly one row to:

```text
st.session_state["manual_mask_rows"][document_scope_key]
```

The row is produced by the existing bound manual-row path and then naturally rejoins the existing preview, table, export, Scrub Key and reinsert mappings on the next rerun.

## Review authority and fallbacks

The full review table remains authoritative. The existing `Gemiste waarde toevoegen` form remains available. The previous static synchronized renderer remains available through:

```text
PROCESSED_TEXT_SELECTION_COMPONENT_ENABLED=false
```

A Python component-rendering exception also fails back to the static renderer and displays a warning. No selection event is applied when the component is unavailable.

## Hidden-marker safety

The visual `Markeringen tonen` control still governs what is shown. A separate server-only protected span set is calculated even when visual markers are hidden. Inspect/commit validation receives those protected spans, so hiding visual marks cannot make existing replacements selectable as safe unmarked text.

## Replay, stale state and mutation order

The integration preserves the action model's:

- bounded event replay history;
- single-use inspections;
- document-scope and document-binding checks;
- source, processed-text and replacement-table hashes;
- exact occurrence and collision revalidation;
- confirmation token for 6–20 occurrences.

Every accepted inspect or commit requests an immediate Streamlit rerun. Unknown and repeated events are ignored without mutation.

## Undo

`Ongedaan maken` is shown only when a selection-created action exists for the current document. Undo removes only that latest row when:

- the document scope matches;
- exactly one stored manual row has the action ID;
- the visible review-table row still matches protected fields from creation.

If the user changed include, remember, find, replacement, entity type, type label or source metadata in the table, automatic undo is blocked and the table remains unchanged.

## Explicitly unchanged

This integration does not change:

- replacement-table authority or editable columns;
- output formats, filenames, MIME types or download buttons;
- Scrub Key schema, digest, binding, warnings or lifecycle;
- reinsert semantics;
- recognizers, profiles, thresholds or replacement algorithms;
- Streamlit/dependency versions;
- network, analytics, browser persistence or cloud processing;
- occurrence-specific masking.

## Validation gates

Before merge:

- action/integration tests;
- source-order contract tests;
- full Python regression;
- standard workflow restored;
- exact merge-candidate regression green.

After merge:

- GitHub-to-Hugging-Face synchronization verification for all runtime-relevant files;
- Streamlit health check;
- live user verification of right-click, visible fallback, type selection, row appearance, all-exact behavior, undo, hidden-marker protection, manual fallback and unchanged exports.

## Next workpackage

Only after live app verification:

```text
SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION
```
