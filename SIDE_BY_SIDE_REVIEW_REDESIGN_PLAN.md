# WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN — Unified source/processed review surface

Status: planning/design/documentation-only  
Repository: `solidprivacy-nl/scrub`

## 1. Executive summary

Scrub should move toward one clear main review surface instead of adding a separate helper panel for every review function.

Target review layout:

```text
Brontekst links | Verwerkte/gecontroleerde tekst rechts
                | Optionele markeringen geïntegreerd in de verwerkte tekst
```

The user should be able to compare the original source text and the checked/processed output directly. Optional highlights should support that comparison inside the right-side processed pane, not as a separate duplicate preview.

This plan does not implement UI, does not change product code and does not change tests.

## 2. Why one main review surface is needed

The current prototype has grown from several safe incremental additions:

- original text input/preview;
- direct processed preview;
- review table;
- serial review panel;
- optional highlight preview;
- DOCX hygiene audit;
- replacement helper assets, with the old helper panel now product-rejected and hidden.

Each individual step was defensible, but together they risk a crowded interface. The user should not have to decide which panel is the real review surface.

The main review question is simple:

```text
Wat kwam erin, wat gaat eruit, en wat moet ik nog controleren?
```

A unified side-by-side review surface gives the user one primary mental model:

```text
links = origineel / bron
rechts = gecontroleerde versie / wat straks gebruikt of geëxporteerd wordt
```

Everything else should support this comparison, not compete with it.

## 3. Desired layout

### 3.1 Main layout

The target main review area should look conceptually like this:

```text
┌──────────────────────────────┬──────────────────────────────┐
│ Brontekst                    │ Verwerkte tekst               │
│ Originele inhoud             │ Gecontroleerde/vervangen tekst│
│                              │ Optionele markeringen         │
└──────────────────────────────┴──────────────────────────────┘
```

### 3.2 Left column: Brontekst

The left column shows the source text extracted from the uploaded or pasted document.

Purpose:

- preserve source context;
- help the user compare legal/professional meaning;
- help spot values that may still need review;
- make the app feel document-based instead of table-only.

The source column should not be editable in the first implementation.

### 3.3 Right column: Verwerkte/gecontroleerde tekst

The right column shows the processed or checked text based on the current review table state.

Purpose:

- show what the user is moving toward as scrubbed output;
- show replacement results in context;
- host optional visual highlights;
- support final confidence before export.

The right column is the primary place for visual review support.

### 3.4 Column headers

Recommended labels:

```text
Brontekst
Verwerkte tekst
```

More explicit alternative:

```text
Originele tekst
Gecontroleerde tekst
```

Avoid technical labels such as:

```text
input buffer
processed buffer
render target
replacement output
highlight engine
```

## 4. Placement of the toggle

The toggle belongs near the right column, above the processed text.

Recommended label:

```text
Markeringen tonen
```

More explicit label:

```text
Markeringen tonen in verwerkte tekst
```

Short helper text:

```text
Toont subtiel welke waarden zijn vervangen of gemaskeerd.
```

Safety copy, if shown, should stay compact:

```text
Alleen visuele hulp. Wijzigt niets aan de vervangtabel of export.
```

Contract/safety note:

```text
only visual aid. Must not change source text, review table state, export payloads, Scrub Key state or reinsert behavior.
```

The toggle affects only the right column. It should not change source text, review table state, export payloads, Scrub Key state or reinsert behavior.

## 5. What happens to the existing separate highlight preview?

The current separate highlight-only duplicate preview is useful as a safe intermediate step, but it is not the desired long-term UX.

Long-term direction:

```text
Do not show a separate highlight-only duplicate preview as the main review pattern.
Integrate highlights into the processed-text right column.
```

The existing highlight implementation can remain until a safe side-by-side implementation replaces or absorbs it. Future implementation must not remove working UI abruptly without contract tests and coordinator approval.

## 6. Review table as source of truth and fallback

The review table remains authoritative.

Principle:

```text
The side-by-side view explains and visualizes the current review state.
The review table remains the source of truth and fallback.
```

The side-by-side surface must not silently replace table semantics.

The review table continues to own:

- include/exclude decisions;
- find/replace values;
- manual corrections;
- remembered replacement choices where applicable;
- export-driving replacement data;
- audit/fallback control.

A future implementation may visually de-emphasize the table, collapse it by default, or move it below the side-by-side review surface, but only if the table remains accessible and authoritative.

Allowed future wording:

```text
De vervangtabel blijft leidend. Controleer bij twijfel de tabel hieronder.
```

Not allowed:

```text
Deze weergave vervangt de vervangtabel.
```

## 7. Relationship to serial review

Serial review remains a guided review layer. It is not a replacement for the review table.

In the target UX, serial review should become a navigation/attention aid for the side-by-side surface:

```text
serial item selected -> source and processed panes show relevant context -> user reviews in one main surface
```

Serial review may later help the user move through items one by one, but it should not multiply into more helper panels.

Recommended direction:

- keep serial review compact;
- keep current item, context and next/previous navigation;
- connect it conceptually to the side-by-side surface;
- avoid exposing internal queue/audit details in the main interface.

Serial review should answer:

```text
Welk item vraagt nu aandacht?
```

It should not become:

```text
another full review surface with separate duplicate output text
```

## 8. Relationship to replacement review

Replacement review should plug into the side-by-side review surface, not return as the old helper/audit panel.

The replacement review should stay task-oriented:

```text
Gevonden waarde -> Context -> Voorgestelde vervanging -> Wat wil je doen?
```

Preferred first actions:

```text
Vervangen
Zichtbaar houden
Aanpassen
Later controleren
```

Preferred first scope choices:

```text
Alleen deze plek
Alle exact dezelfde waarden
```

Where it fits:

- the current item/context may be shown near the side-by-side view;
- replacement actions may later appear close to the selected item;
- details should stay compact and optional;
- the review table remains fallback and audit source.

Do not expose helper/audit internals as main UI:

```text
creates_mapping
mapping_candidates
export_readiness
raw decision states
state_counts
apply_to_same_value_actions
```

The old replacement decision helper panel must not return as the normal user-facing panel.

## 9. Desired labels and copy

### Main review section

Recommended title:

```text
Controleer de tekst
```

Alternative:

```text
Vergelijk bron en verwerkte tekst
```

### Column labels

```text
Brontekst
Verwerkte tekst
```

or:

```text
Originele tekst
Gecontroleerde tekst
```

### Highlight toggle

```text
Markeringen tonen
Markeringen tonen in verwerkte tekst
```

### Compact legend

If a legend is needed, use one compact line above the processed text:

```text
Geel = vervangen of gemaskeerde waarde
```

Alternative:

```text
Gemarkeerd = waarde die door de vervangtabel is vervangen
```

Use a single compact legend, not repeated labels on every highlight.

### Table fallback copy

```text
De vervangtabel blijft leidend. Controleer bij twijfel de tabel hieronder.
```

### Replacement action copy

```text
Wat wil je doen met deze waarde?
Vervangen
Zichtbaar houden
Aanpassen
Later controleren
```

## 10. Unwanted labels and copy

Avoid technical/helper labels in the main interface:

```text
Replacement decision helper
Decision state
Scope selector
Affected count
Creates mapping
Mapping candidates
Export readiness
Audit fields
state_counts
apply_to_same_value_actions
all_normalized
creates_mapping
mapping_candidates
```

Avoid repeated per-highlight labels in the long-term design:

```text
Gemarkeerd
Gemarkeerd
Gemarkeerd
```

Repeated labels add noise when every highlight has the same meaning. Use one compact legend instead.

Avoid alarm language for normal replaced values:

```text
Waarschuwing
Gevaar
Fout
Risico
```

Those words should be reserved for actual risk states, not normal visual markers.

## 11. Smallest safe first implementation

The smallest safe first implementation should be a bounded side-by-side read-only surface.

It should:

- render source text left;
- render processed/checked text right;
- include the existing highlight toggle near the right pane;
- keep highlights visual-only;
- keep the review table unchanged and available below or nearby;
- keep serial review available;
- avoid synchronized scrolling in the first implementation;
- avoid custom components in the first implementation unless explicitly approved;
- avoid replacement action mutation;
- avoid changing export, Scrub Key or reinsert behavior.

Recommended safe first implementation shape:

```text
Section: Controleer de tekst
[Brontekst] [Verwerkte tekst]
            [ ] Markeringen tonen

Below:
Bestaande serial review / review table remains available.
```

The first implementation may reuse existing helper functions for safe text generation and highlighting, but must be covered by contract tests first.

## 12. Explicitly blocked behavior

This plan does not approve:

- Streamlit UI implementation;
- changes to `presidio_streamlit.py`;
- changes to `serial_review_panel_ui.py`;
- changes to `review_highlight_toggle_panel_ui.py`;
- custom HTML/component implementation;
- synchronized scroll implementation;
- review table behavior changes;
- replacement behavior changes;
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
- real-data fixtures;
- raw unsafe document HTML;
- fuzzy matching or guessed intent;
- automatic replacement.

Synchronized scrolling is desirable, but must be a separate package with separate tests because it may require custom rendering.

## 13. Contract tests required before implementation

`WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS` should verify at minimum:

1. `SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN.md` exists.
2. The plan requires one main side-by-side review surface.
3. The plan states source/brontekst is on the left.
4. The plan states processed/checked text is on the right.
5. The plan states optional highlights are integrated into the right processed pane.
6. The plan includes `Markeringen tonen` or `Markeringen tonen in verwerkte tekst`.
7. The plan says highlights are visual-only and non-mutating.
8. The plan says the separate highlight-only duplicate preview is not the long-term target.
9. The plan rejects repeated per-highlight `Gemarkeerd` labels as the long-term design.
10. The plan allows at most one compact legend above the processed text.
11. The plan says the review table remains source of truth and fallback.
12. The plan says serial review remains a guided layer, not a table replacement.
13. The plan says replacement review must be task-oriented and must not expose helper/audit internals as main UI.
14. The plan includes preferred replacement actions: `Vervangen`, `Zichtbaar houden`, `Aanpassen`, `Later controleren`.
15. The plan blocks `all_normalized` as a first normal user-facing scope.
16. The plan blocks synchronized scroll implementation in the first package and requires separate planning/testing.
17. The plan blocks custom HTML/component implementation unless separately approved.
18. The plan blocks `presidio_streamlit.py`, `serial_review_panel_ui.py` and `review_highlight_toggle_panel_ui.py` changes in this planning package.
19. The plan blocks review table mutation, replacement mutation, automatic replacement, Scrub Key writes, export/download changes and reinsert changes.
20. The plan blocks click-to-mark, advanced editor and full-document marking.
21. The plan requires escaping if any HTML-based rendering is later used.
22. The plan requires synthetic-only test data and no real personal data.

## 14. Later implementation package

Next package after this plan:

```text
WP_SIDE_BY_SIDE_REVIEW_CONTRACT_TESTS
```

Only after contract tests and separate coordinator approval should implementation be considered:

```text
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION
```

Separate later packages are required for:

```text
synchronized scroll implementation
custom HTML/component rendering
replacement UI implementation
click-to-mark
advanced editor
full-document marking
export blocking
Scrub Key writes
```

Do not start these automatically.

## 15. Final recommendation

The review UX should now move from multiple additive panels toward one calm main comparison surface.

The user should see:

```text
Brontekst links. Verwerkte tekst rechts. Markeringen optioneel.
```

The product should avoid exposing internal helper/audit concepts as normal UI. The next safe step is contract tests for this plan, not implementation.
