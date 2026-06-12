# WP40 — Document-centric review UX specification

Status: completed specification-only  
Repository: `solidprivacy-nl/scrub`

## 1. Purpose

The current review workflow is table-first. It gives users a replacement table, review status, focus filters, guidance and export sanity checks. That is useful, but it does not fully match how legal and care professionals review documents.

Professional users review meaning in context. They need to see the document text, the surrounding sentence, the role of a term and whether removing or replacing it changes legal or care meaning.

WP40 defines a future document-centric review UX direction without implementing UI.

## 2. Decision boundary

This workpackage is specification-only.

It does not change:

- Streamlit UI;
- review table implementation;
- export/download behavior;
- Scrub Key behavior;
- recognizer logic;
- helper logic;
- dependencies;
- cloud processing;
- real data.

## 3. UX problem

A table-first review creates several risks:

- users lose the sentence or paragraph context around a finding;
- role words such as `eiser`, `verweerder`, `slachtoffer`, `minderjarige`, `arts` or `gemachtigde` may be misunderstood as values to remove;
- duplicate values across a document are hard to reason about;
- hidden misses are hard to spot because the user reviews rows rather than the document;
- users may approve a replacement without seeing whether legal meaning remains intact;
- long documents become tiring to review in a table.

The table should remain useful, but it should not be the only review surface.

## 4. Product principle

The target review experience should be:

```text
Document first, table second, audit always visible.
```

The document view should help the user answer:

- What was found?
- Where was it found?
- Why was it considered sensitive?
- What will it become after scrubbing?
- What remains in the text?
- What needs human attention?
- What limitations still apply?

## 5. Future review layout

A future document-centric review screen should have three coordinated zones.

### 5.1 Document pane

The document pane shows the user the text or document representation with visible markers.

Marker types:

- confirmed sensitive value;
- candidate/maybe missed value;
- manual user mark;
- preserved legal/care context term;
- warning/high-risk span;
- hidden-content warning where applicable.

The document pane should support:

- click a marker to inspect details;
- highlight all occurrences of the same value;
- navigate previous/next finding;
- show paragraph/sentence context;
- show replacement preview;
- show unresolved warnings.

### 5.2 Detail pane

The detail pane shows one selected finding.

Minimum fields:

- original text;
- replacement/placeholder;
- entity type;
- source: detected, candidate, manual, remembered, Scrub Key;
- confidence/score where available;
- reason;
- surrounding sentence/paragraph;
- review status;
- actions: accept, ignore, edit replacement, mark as context term, add manual sensitive value.

### 5.3 Review table pane

The table remains available for bulk review and audit.

Recommended role:

- sort/filter findings;
- batch inspect similar entities;
- edit replacement text;
- compare detected/candidate/manual rows;
- export/audit sanity view.

The table should not replace document review.

## 6. Review states

The future UX should use explicit states:

```text
needs_review
accepted
ignored
edited
manual_added
preserve_context
high_risk_unresolved
```

Rules:

- high-risk unresolved items should remain visible before export;
- ignored items should remain auditable;
- manual additions should be clearly distinct from recognizer detections;
- preserve-context decisions should be visible to avoid accidental later masking.

## 7. Document-centric actions

Future actions should include:

### Accept finding

User confirms that a span should be replaced.

### Ignore finding

User says the span should remain as-is.

### Edit replacement

User changes the placeholder/replacement label.

### Mark as context term

User marks a term as meaningful context, not sensitive value.

Examples:

- `eiser`;
- `verweerder`;
- `slachtoffer`;
- `minderjarige`;
- `arts`;
- `gemachtigde`;
- `zorgverlener`.

### Add missed sensitive value

User selects text in the document and marks it as sensitive.

### Apply to all same values

User can apply a decision to identical occurrences, with a warning if context differs.

## 8. Safety and trust requirements

The document-centric review must keep current safety boundaries:

- no cloud document processing;
- no silent export semantic changes;
- no automatic removal of hidden content without explicit future policy;
- no Scrub Key schema change as part of review UX;
- no real data in tests or fixtures;
- preserve legal and care meaning;
- make residual risk visible.

The future UI should clearly separate:

- anonymization claims;
- pseudonymization with Scrub Key;
- redaction/removal;
- hidden-content audit warnings;
- residual-risk warnings.

## 9. MVP document-centric review concept

The first MVP should not try to render perfect DOCX layout.

Recommended MVP shape:

```text
Text-based document preview with inline markers + synchronized detail/table panes.
```

Supported first inputs:

- plain text;
- extracted DOCX main text where available;
- synthetic legal/care examples.

Out of initial MVP scope:

- exact Word layout rendering;
- PDF layout rendering;
- OCR;
- automatic clean-DOCX export;
- comments/tracked-change editing;
- production frontend migration.

## 10. Streamlit feasibility questions

Before implementation, WP42 should evaluate whether Streamlit can support:

- clickable span markers;
- stable synchronized document/detail/table state;
- large document performance;
- keyboard navigation;
- accessible color/marker design;
- safe state management;
- side-by-side panes without fragile patching.

If Streamlit is too limited, the future frontend decision should move toward a separate document-centric UI while keeping the Python core reusable.

## 11. Relation to current review table

The current table-first flow should not be removed.

It should become:

```text
an audit/control surface beside the document view
```

Current assets that should be reused:

- review status labels;
- focus filters;
- review guidance;
- export sanity checks;
- replacement table columns;
- Scrub Key export based on reviewed rows;
- residual-risk/audit messages.

## 12. Validation plan

Future validation should use synthetic documents only.

Recommended test cases:

- legal paragraph with names, role terms and case numbers;
- care paragraph with client number, staff names and role terms;
- repeated same value in different contexts;
- candidate missed values;
- manual selection of a missed value;
- ignored context term;
- high-risk unresolved item before export;
- DOCX hygiene warning surfaced beside document review.

Usability checks:

- user can find all high-risk items;
- user understands difference between sensitive value and context term;
- user can add a missed value from the document text;
- user can see what remains unresolved before export;
- user can still use the table for bulk control.

## 13. Recommended next workpackages

Recommended sequence:

```text
WP41 — Highlight-based review prototype decision
WP42 — Streamlit feasibility boundary review
WP43 — Frontend architecture decision
WP44 — Click-to-mark sensitive text prototype
```

Do not implement a broad document-centric UI before WP41/WP42 clarify the prototype boundary.

## 14. Final recommendation

The review UX should move toward:

```text
Document-first review with inline markers, synchronized detail pane, table audit/control and explicit residual-risk status.
```

This is the right direction for online/web validation before installer work, because it improves user trust where the actual product risk lives: reviewing confidential document meaning before export or AI use.
