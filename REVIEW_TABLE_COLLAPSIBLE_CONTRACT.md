# WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS — Collapsible review table contract

Status: contract/documentation-only  
Repository: `solidprivacy-nl/scrub`

## Purpose

This contract defines the future UX for making the `Controleer gevonden gegevens` section visually quieter by allowing it to become collapsible.

This document does not implement UI.

## Future heading

Recommended future heading:

```text
3. Controleer gevonden gegevens — 34 items
```

The heading may include the current review item count.

Acceptable variants:

```text
Controleer gevonden gegevens
Controleer gevonden gegevens — {item_count} items
```

## Required table role

The review table remains:

```text
source of truth
fallback
de plek waar include/remember/find/replace_with wordt gecontroleerd
```

User-facing Dutch copy inside or near the section must preserve:

```text
De vervangtabel blijft leidend voor beslissingen en export.
```

## Required table controls

The review table must remain present and must keep the existing Streamlit data editor key:

```text
replacement_editor
```

The following table columns/fields must remain available:

```text
include
remember
find
replace_with
```

These fields represent the user-controlled replacement audit surface. Making the section collapsible must not remove or bypass them.

## Relationship to central side-by-side review

The central side-by-side review surface is the main visual comparison surface.

The review table is still authoritative for applied replacement decisions and export construction.

A collapsible table may reduce visual weight, but it must not hide the table permanently, remove the table, or replace it with side-by-side markers, serial review, context cards or a replacement helper panel.

## Boundaries

This contract does not approve:

- production UI implementation;
- editing `presidio_streamlit.py` in this package;
- export/download behavior changes;
- export blocking;
- Scrub Key writes;
- Scrub Key schema changes;
- reinsert behavior changes;
- replacement behavior changes;
- click-to-mark;
- advanced editor;
- full-document marking;
- dependency changes;
- cloud processing;
- real-data fixtures.

## Export/download boundary

Existing export/download labels must remain available after a later implementation:

```text
Download opgeschoonde tekst (.txt)
Download vervangtabel (.csv)
Download scrubrapport (.txt)
Download opgeschoond Word-bestand (.docx)
Download opgeschoonde PDF (.pdf)
```

## Future implementation gate

A future implementation package may be considered only after these contract tests are green:

```text
WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION
```

That implementation package must not run in parallel with other `presidio_streamlit.py` review-flow changes.
