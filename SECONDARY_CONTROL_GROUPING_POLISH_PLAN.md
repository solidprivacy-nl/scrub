# SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH — Plan

Status: planning/contract-test-first.

Repository: `solidprivacy-nl/scrub`

## Purpose

Make the secondary controls under `2. Controleer resultaat` calmer and less visually fragmented without weakening review, export, Scrub Key, reinsert, audit or privacy controls.

This is a small MVP UI-polish line. It should not become a new review architecture.

## Current user-visible issue

The primary review surface is now calmer, but the area below the side-by-side review still shows many separate collapsed controls in sequence, such as:

- `Waarom controleren?`
- `Gemiste waarde toevoegen`
- `Extra controlehulpen`
- `Mogelijk extra te controleren waarden`
- `Vervangtabel controleren — <items> items`
- `Geavanceerde details bij de vervangtabel`
- `Stap voor stap controleren`
- `Herbruikbare vervangingen`

All of these controls are useful, but the number of separate expanders makes the screen still feel more technical than necessary.

## Target direction

Keep the primary review path simple:

```text
2. Controleer resultaat
- side-by-side review visible
- Markeringen tonen visible
- short guidance
- one calmer secondary-control area
- replacement table remains reachable and source of truth
- manual missed-value entry remains reachable
```

A later implementation should reduce the visible secondary-control stack, preferably by introducing a single calmer secondary area such as:

```text
Meer controleopties
```

or another equivalent grouping that makes the review area feel less like a technical form.

## Important implementation constraint

Do not use nested Streamlit expanders.

The repository has a history of nested-expander issues. A later implementation may group controls by:

- using one parent expander and inline headings/tabs/sections inside it; or
- replacing multiple expanders with one or two top-level expanders; or
- using tabs/segments inside a single secondary-control area if safe;
- keeping some high-value controls top-level if grouping would reduce discoverability.

But the implementation must avoid `st.expander` inside another `st.expander`.

## Controls that must remain available

A later implementation must preserve:

- side-by-side review as the visible primary review surface;
- `Markeringen tonen`;
- manual missed-value entry / `Gemiste waarde toevoegen`;
- replacement table / `Vervangtabel controleren`;
- review table source-of-truth and fallback role;
- focus/filter review aid;
- Dutch legal candidate audit values when relevant;
- advanced/technical replacement details;
- serial review / `Stap voor stap controleren` as optional secondary aid;
- reusable replacements;
- Scrub Key separation and warning protection;
- export/download behavior and file semantics;
- audit and DOCX hygiene details.

## Non-goals

Do not change:

- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Do not introduce:

- cloud processing;
- AI processing;
- OCR;
- restored PDF;
- PDF-to-DOCX reconstruction;
- click-to-mark;
- advanced editor;
- full-document marking;
- hidden export gate;
- old replacement decision helper panel as normal user-facing UI.

## Implementation checklist for the next package

The implementation package should:

1. edit only the normal review-control grouping area;
2. avoid nested expanders;
3. preserve side-by-side review and `Markeringen tonen` above the secondary controls;
4. keep manual missed-value entry discoverable;
5. keep replacement table reachable and source-of-truth;
6. keep serial review and advanced details reachable but secondary;
7. add source-level tests proving the grouping and preserved controls;
8. use PR validation, Hugging Face sync and live app verification because visible UI behavior will change.

## App verification checklist for the implementation package

After implementation, verify in the live app:

- app starts without Script execution error;
- side-by-side review remains visible;
- `Markeringen tonen` remains visible;
- secondary controls are calmer and less visually fragmented;
- no nested-expander error appears;
- manual missed-value entry remains reachable;
- replacement table remains reachable and source of truth;
- step-by-step review remains reachable;
- candidate/audit/technical controls remain reachable;
- primary downloads, Scrub Key, audit downloads and DOCX hygiene audit remain available;
- no export, Scrub Key, reinsert, recognizer, benchmark or runtime semantics changed.

## Next package

Recommended next package:

```text
SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION
```
