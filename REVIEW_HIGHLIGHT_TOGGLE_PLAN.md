# WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN — Simple masked-text highlight toggle planning

Status: planning/specification-only  
Repository: `solidprivacy-nl/scrub`

## 1. Purpose

This plan describes a simple non-mutating review aid:

```text
[ ] Markeringen tonen
```

Alternative label:

```text
[ ] Markeringen tonen in voorbeeldtekst
```

When the toggle is off, the preview text stays calm and normally readable. When the toggle is on, values that have already been masked or replaced get a subtle visual marker in the preview text.

This is not a full-document editor, not click-to-mark, not an authoritative highlight workflow and not a restart of the failed WP42D route.

## 2. Product goal

The feature should make the review interface simpler.

It should help the user answer one basic question faster:

```text
Welke tekstdelen zijn al vervangen of gemaskeerd?
```

It should not add a new decision layer, show helper internals, expose audit fields, or make the workflow more technical.

## 3. Placement in the review flow

Recommended future placement:

```text
2. Controleer gevonden gegevens
Bestaande review/vervangtabel
Serial review — experimentele reviewhulp
Voorbeeld op basis van de gecontroleerde vervangtabel
[ ] Markeringen tonen in voorbeeldtekst
```

The safest first placement is inside or directly above the existing preview section:

```text
Voorbeeld op basis van de gecontroleerde vervangtabel
```

The existing review table remains the source of truth and fallback. The toggle must not replace the table, serial review panel or export summary.

## 4. Dutch UI copy

Recommended label:

```text
Markeringen tonen
```

More explicit label:

```text
Markeringen tonen in voorbeeldtekst
```

Short helper text:

```text
Toont subtiel welke waarden in de voorbeeldtekst zijn vervangen of gemaskeerd.
```

Safety text:

```text
Markeringen zijn alleen een visuele hulp.
Ze wijzigen niets aan de vervangtabel.
Ze wijzigen niets aan export.
Ze wijzigen niets aan Scrub Key.
```

Empty-state text:

```text
Geen gemarkeerde vervangingen beschikbaar in deze voorbeeldtekst.
```

## 5. On/off behavior

### Toggle off

Default state should be off or quietly off for users who prefer a calm preview.

Expected behavior:

```text
De voorbeeldtekst blijft rustig en normaal leesbaar.
```

The existing text preview remains unchanged.

### Toggle on

Expected behavior:

```text
Vervangen/gemaskeerde waarden krijgen een subtiele visuele markering.
```

The marker should help visual scanning, not dominate the page.

The toggle only changes display style in the preview area. It must not change replacement data, export payloads or Scrub Key state.

## 6. Values that may be highlighted

A later implementation may highlight only values that are already represented by the current reviewed replacement state.

Allowed input sources:

- rows from the existing review/replacement table after user review;
- included rows where `find` and `replace_with` are both non-empty;
- values that appear exactly in the preview or generated output text;
- serial-review `current_item` only for selecting/focusing an item, not for applying decisions.

Allowed highlighted text:

```text
already masked/replaced values in the preview text
exact placeholders or replacement values already present in the preview
```

Use exact matching only.

## 7. Values that must not be highlighted

Do not highlight values by guessing.

Not allowed:

- fuzzy matches;
- inferred personal data;
- hidden/offscreen document content;
- non-included table rows;
- candidate rows that the user did not include;
- ignored rows;
- unresolved rows unless a later contract explicitly marks them as advisory-only and visually distinct;
- Scrub Key mappings not present in the current preview;
- reinsert values;
- document bytes or raw Word/PDF layout content.

The toggle must not turn into a detector, scanner, editor or click-to-mark tool.

## 8. Safety boundaries

This future feature must remain:

```text
read-only
visual-only
non-authoritative
non-mutating
table-first baseline
```

It must not:

- mutate the replacement table;
- change `edited_replacements_df`;
- apply replacements;
- perform automatic replacement;
- write Scrub Key mappings;
- change Scrub Key schema;
- change export/download behavior;
- block export;
- change reinsert behavior;
- introduce startup source mutation;
- patch `presidio_streamlit.py` at startup;
- use unsafe raw HTML with document text;
- use cloud processing;
- use real-data fixtures;
- add dependencies.

Required warning against old route:

```text
Do not restart static-highlight startup source mutation.
Do not patch presidio_streamlit.py at startup.
Do not implement click-to-mark.
Do not implement an advanced editor.
Do not implement full-document marking.
```

## 9. Accessibility and visual design

The highlight must be subtle and calm.

Requirements:

- Color must not be the only signal.
- Use a secondary indicator such as a light border, underline, label, or text marker pattern if technically feasible.
- Avoid a crowded interface.
- Avoid high-contrast warning colors for normal replaced values.
- Do not make all text look alarming.
- Keep the normal preview available without markers.
- Avoid raw HTML unless all user/document text is safely escaped and this is covered by tests.

Preferred visual tone:

```text
quiet, review aid, not warning-heavy
```

## 10. Relationship with serial review and context cards

The serial review panel may remain a small non-destructive review aid.

A future implementation may use the serial review current item only to focus the preview on the same value. It must not use serial review navigation to mutate the table.

Context cards may provide local context, but the highlight toggle should not expose context-card helper internals or validation fields to normal users.

The feature should feel like a simple display option, not a technical helper panel.

## 11. Relationship with replacement decision helpers

`replacement_decision.py` and `REPLACE_LOGIC_UI_PLAN.md` remain useful design assets.

However, the product rollback of the replacement helper panel shows that exposing helper/audit internals can make the interface less intuitive.

This toggle must therefore avoid showing internal helper fields such as:

- `mapping_candidates`;
- `export_readiness`;
- `creates_mapping`;
- `scope` internals;
- risk/audit counters unless already shown elsewhere.

The user-facing concept is only:

```text
Show me what is already masked/replaced in this preview.
```

## 12. Test expectations for a later contract-test package

Next package should add contract tests for this plan.

Minimum expected tests:

- plan contains `Markeringen tonen`;
- plan contains `Markeringen tonen in voorbeeldtekst`;
- toggle is described as read-only / visual-only;
- plan preserves table-first baseline;
- plan says the review table remains source of truth;
- plan forbids table mutation;
- plan forbids `edited_replacements_df` mutation;
- plan forbids automatic replacement;
- plan forbids Scrub Key writes;
- plan forbids export/download changes;
- plan forbids export blocking;
- plan forbids reinsert changes;
- plan forbids startup source mutation;
- plan forbids static-highlight startup patch;
- plan forbids click-to-mark;
- plan forbids advanced editor;
- plan forbids full-document marking;
- plan forbids raw unsafe HTML;
- plan requires escaping if HTML is ever used;
- plan requires color not to be the only signal;
- plan requires synthetic-only tests and no real personal data.

## 13. Implementation route after this plan

Recommended sequence:

```text
1. WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS
2. WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION only after separate coordinator approval
3. Actions and Hugging Face sync verification
4. App verification because UI behavior would change
```

Do not implement the toggle in this package.

## 14. Final recommendation

The highlight toggle should be a small optional display aid in the existing preview text. It should make it easier to see which values are already masked/replaced, while keeping the review table as source of truth.

It must stay far away from the old static-highlight startup mutation route, click-to-mark, advanced editing and full-document marking.
