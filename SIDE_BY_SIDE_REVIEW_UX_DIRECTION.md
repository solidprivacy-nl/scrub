# Side-by-side review UX direction — unified main review surface

Status: roadmap/specification/documentation-only  
Repository: `solidprivacy-nl/scrub`

## 1. Product decision summary

The review interface should move toward one unified main review surface instead of adding a new expander or helper panel for every review feature.

Target direction:

```text
Source text left | Processed/checked text right
                 | Optional highlights integrated in the processed text
```

The user should be able to compare source and processed output in the main review area, with optional visual support. Highlighting should not live primarily in a separate highlight-only panel.

## 2. Why this direction is needed

The current interface has grown by adding separate surfaces for separate concerns:

- source text;
- preview text;
- review table;
- serial review panel;
- highlight toggle / marked preview;
- DOCX hygiene audit;
- previous replacement helper panel, now product-rejected and hidden.

This creates a risk that every new function becomes another panel, which makes the product less intuitive. The main review experience should become simpler, not wider.

## 3. New review UX principle

The main review task is:

```text
Compare what came in with what will go out, understand what changed, then review exceptions.
```

Therefore, the review UX should be organized around:

1. source text;
2. processed/checked text;
3. optional highlights;
4. simple replacement decisions near the current item when needed;
5. review table as source of truth and fallback.

## 4. Side-by-side review target

The desired main review view is:

```text
┌──────────────────────────────┬──────────────────────────────┐
│ Brontekst                    │ Verwerkte tekst               │
│                              │ [optionele highlights]        │
│                              │                              │
└──────────────────────────────┴──────────────────────────────┘
```

Above or near this pair:

```text
[ ] Markeringen tonen
```

The toggle should affect the processed/checked text in the main comparison surface. It should not create another separate copy of the preview text elsewhere as the long-term UX.

## 5. Synchronized scrolling

Synchronized scrolling is a valid UX goal:

```text
when the user scrolls the source text, the processed text follows, and vice versa
```

However, synchronized scrolling may require custom HTML/component work in Streamlit. It must be planned and tested separately because previous review-highlight attempts showed that fragile UI rendering can destabilize the app.

The first implementation should not jump directly to a broad custom editor. It should start with a bounded proof of a side-by-side review surface.

## 6. Highlight behavior

Highlights should be visual support inside the main processed-text pane.

Rules:

- highlights are visual only;
- highlights are not a mutation mechanism;
- no click-to-mark in this phase;
- no full-document marking;
- no advanced editor;
- source/user text must be escaped if HTML rendering is used;
- no raw unsafe user-text HTML;
- no fuzzy matching or guessed intent;
- no automatic replacement.

## 7. Remove redundant per-highlight labels

The current repeated per-highlight label such as `Gemarkeerd` is not needed as a long-term design.

Reason:

```text
The color/marker already communicates that the segment is highlighted. Repeating the same label on every segment adds noise but no decision value.
```

Preferred design:

- no repeated inline `Gemarkeerd` label;
- optionally one compact legend above the preview, for example:

```text
Geel = vervangen waarde
```

Only use a label when it adds a real distinction, not when every highlight has the same meaning.

## 8. Relationship to replacement review

The replacement redesign should plug into the unified side-by-side review surface, not become a separate technical helper panel.

The replacement flow remains task-oriented:

```text
Gevonden waarde -> Context -> Voorgestelde vervanging -> Wat wil je doen?
```

Allowed first user choices remain:

```text
Vervangen
Zichtbaar houden
Aanpassen
Later controleren
```

Allowed first scope choices remain:

```text
Alleen deze plek
Alle exact dezelfde waarden
```

The normal UI must not show helper/audit internals such as:

- `creates_mapping`;
- `mapping_candidates`;
- `export_readiness`;
- raw decision states;
- raw audit fields.

## 9. Relationship to current panels

### Review table

The review table remains source of truth and fallback.

It may become visually less dominant later, but it remains the authoritative control/audit surface until a separately approved package changes that.

### Serial review

Serial review remains a guided review layer, not a replacement for the table.

It may become part of the side-by-side review experience, but it should not multiply into many helper panels.

### Highlight toggle

Highlighting should be integrated into the main processed-text pane.

The existing separate highlight-only panel is not the desired end-state.

### Replacement helper panel

The old replacement decision helper panel must not return as the normal user-facing UI.

### DOCX hygiene audit

DOCX hygiene audit may remain a separate report-only export-adjacent panel because it concerns file hygiene and export risk, not core text comparison.

## 10. Explicit non-goals and blocked behavior

This direction does not approve:

- Streamlit UI implementation;
- custom synchronized scroll implementation;
- replacing the review table;
- removing existing working UI code;
- review table behavior changes;
- mutation behavior;
- automatic replacement;
- Scrub Key writes;
- Scrub Key schema changes;
- export blocking;
- export/download behavior changes;
- reinsert behavior changes;
- click-to-mark;
- advanced editor;
- full-document marking;
- dependency changes;
- cloud processing;
- real-data fixtures.

## 11. Follow-up workpackage sequence

Recommended sequence:

```text
1. WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN
2. WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS
3. WP_SIDE_BY_SIDE_REVIEW_PROTOTYPE_HELPER
4. WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — only after explicit coordinator approval
```

Related replacement-flow line:

```text
WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS
```

The replacement-flow tests can run in parallel with the side-by-side planning/tests because they are documentation/contract-only and should not touch UI code.

## 12. Parallelization guidance

Safe to run in parallel:

- `WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN` with replacement redesign contract tests;
- documentation-only risk/decision refinements;
- contract tests for redesign documents.

Do not run in parallel without explicit coordination:

- any edits to `presidio_streamlit.py`;
- any edits to `serial_review_panel_ui.py`;
- any edits to `review_highlight_toggle_panel_ui.py`;
- any removal/hiding of existing panels;
- any synchronized scroll implementation;
- any custom HTML rendering implementation;
- any export/download/reinsert/Scrub Key changes.

## 13. Required future contract tests

Before implementation, contract tests should verify:

1. this direction document exists;
2. the main review target is side-by-side source and processed text;
3. highlight toggle belongs near/in the main side-by-side review surface;
4. no long-term separate highlight-only duplicate preview is the target;
5. no repeated per-highlight `Gemarkeerd` label as long-term UI copy;
6. review table remains source of truth and fallback;
7. serial review remains a guided layer, not table replacement;
8. old replacement helper panel remains blocked from normal user-facing flow;
9. synchronized scrolling requires separate planning/approval/testing;
10. no click-to-mark, advanced editor or full-document marking;
11. no Scrub Key/export/reinsert behavior change;
12. source text escaping is required for any HTML-based rendering.
