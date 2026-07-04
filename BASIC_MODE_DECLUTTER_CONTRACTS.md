# SCRUB-WP_BASIC_MODE_DECLUTTER_CONTRACTS

Status: contract-tests-only boundary document.

Repository: `solidprivacy-nl/scrub`

## Purpose

This document defines the product and safety contracts for the next Basiscontrole declutter implementation.

The goal is to make `Basiscontrole` materially cleaner than the current first mode-split implementation while preserving `Expertcontrole` as the full review, audit and troubleshooting surface.

This package does not implement UI changes. A later implementation requires a separate workpackage.

## Product thesis

```text
Basiscontrole is not weaker review.
Basiscontrole is lower cognitive load with the same safety boundaries.
Expertcontrole preserves the full review/audit machinery.
```

Basiscontrole should reduce visible complexity. It must not weaken privacy, review, export, Scrub Key, reinsert, audit or document-hygiene controls.

## Basiscontrole target

Basiscontrole must remain the default selected review mode.

The mode state key must remain:

```text
solidprivacy_review_mode
```

The primary visible flow should remain:

```text
1. Voeg document of tekst toe
2. Controleer resultaat
3. Exporteer resultaat / Download veilig
```

Under `2. Controleer resultaat`, Basiscontrole should keep the practical essentials visible or near-visible:

- `Controleweergave`;
- `Basiscontrole` / `Expertcontrole`;
- side-by-side review;
- `Markeringen tonen`;
- short instruction copy;
- replacement count;
- `Gemiste waarde toevoegen`;
- one compact correction/detail path such as `Details aanpassen`;
- primary document downloads.

The replacement table remains the internal source of truth and fallback. It should remain reachable in Basiscontrole, but it should not dominate the default visual path.

## Basiscontrole declutter contract

Basiscontrole should avoid showing the full expert expander stack as equally prominent top-level controls.

The following should not all remain equally prominent in Basiscontrole:

- `Waarom controleren?`;
- `Extra controlehulpen`;
- `Mogelijk extra te controleren waarden`;
- `Geavanceerde details bij de vervangtabel`;
- `Stap voor stap controleren`;
- `Herbruikbare vervangingen`;
- `Technische informatie`;
- `Geavanceerde herkenningsdetails`.

Acceptable Basiscontrole approaches:

- show only a smaller correction path such as `Details aanpassen`;
- keep `Gemiste waarde toevoegen` visible or immediately reachable;
- keep `Vervangtabel controleren` reachable through the correction path;
- show candidate-warning controls only when candidate rows exist;
- keep Scrub Key and audit downloads available but secondary;
- keep technical/advanced details primarily in Expertcontrole.

## Expertcontrole preservation contract

When `Expertcontrole` is selected, the full detailed machinery must remain available:

- `Waarom controleren?`;
- `Gemiste waarde toevoegen`;
- `Extra controlehulpen`;
- `Mogelijk extra te controleren waarden`;
- `Vervangtabel controleren`;
- `Geavanceerde details bij de vervangtabel`;
- `Stap voor stap controleren`;
- `Herbruikbare vervangingen`;
- `Scrub Key downloaden`;
- `Audit en technische bestanden`;
- `DOCX hygiene audit`;
- `Technische informatie`;
- `Geavanceerde herkenningsdetails`.

Expertcontrole may remain more technical. It must not be stripped down as part of Basiscontrole decluttering.

## Mode-switch and session-state contract

Switching modes must not reset:

- uploaded text;
- uploaded file;
- recognized replacements;
- manual additions;
- replacement decisions;
- download outputs;
- session state needed for the active document.

A later implementation should capture the review-surface return value in `presidio_streamlit.py`, for example:

```python
side_by_side_review_state = render_side_by_side_review_panel(
    source_text=st_text,
    edited_replacements_df=replacement_editor_df,
)

review_mode = side_by_side_review_state.get("review_mode", "Basiscontrole")
is_expert_review = review_mode == "Expertcontrole"
```

The mode flag may control visibility and grouping only. It must not control recognition, replacement construction, export payloads, Scrub Key JSON, reinsert behavior or audit generation.

## Streamlit implementation constraints

Do not introduce nested expanders.

A later implementation must not put existing `st.expander(...)` blocks inside a parent `st.expander(...)`.

Allowed approaches:

- conditionally render fewer top-level expanders in Basiscontrole;
- rename a top-level expander in Basiscontrole, for example `Details aanpassen — vervangtabel`;
- keep expert-only controls as top-level expanders only when Expertcontrole is selected;
- use simple headings/captions above grouped controls;
- use tabs only if they do not introduce state loss or visual confusion.

Do not introduce a parent `Meer controleopties` expander containing other expanders.

## Safety boundaries

A later implementation must not change:

- replacement logic;
- review table data semantics;
- include/remember/find/replace_with meaning;
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

A later implementation must not introduce:

- cloud processing;
- AI processing;
- OCR;
- restored PDF promise;
- PDF-to-DOCX reconstruction;
- click-to-mark;
- advanced editor;
- full-document marking;
- hidden export gate;
- old replacement decision helper panel.

## Required app verification checklist for later implementation

When a later implementation changes UI behavior, live app verification must confirm:

1. App starts without Script execution error.
2. Basiscontrole is selected by default.
3. Basiscontrole is visibly cleaner than before.
4. Side-by-side review remains visible.
5. `Markeringen tonen` remains visible.
6. `Gemiste waarde toevoegen` remains reachable.
7. `Vervangtabel controleren` / `Details aanpassen` remains reachable.
8. Expertcontrole exposes the full detailed controls.
9. Step-by-step review remains reachable in Expertcontrole.
10. Scrub Key download remains separated and warning-protected.
11. Primary document downloads remain visible.
12. Audit/technical downloads remain available.
13. DOCX hygiene audit remains available when relevant.
14. No visible export, Scrub Key or reinsert regression appears.

## Next package

The next implementation package may be:

```text
SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION
```

Only start implementation after these contract tests are accepted and merged.
