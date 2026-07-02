# SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACTS

Status: contract-tests-only boundary document.

Repository: `solidprivacy-nl/scrub`

## Purpose

This document defines the safety and product boundaries for a later review-surface simplification implementation. It is derived from `REVIEW_SURFACE_SIMPLIFICATION_PLAN.md` and exists so the next implementation package can simplify the primary MVP review surface without weakening privacy, review, export or audit controls.

This package does not implement UI changes. A future implementation requires a separate workpackage.

## Target user-visible direction

The normal anonymization flow should move toward one calmer primary path:

```text
1. Voeg document toe
2. Controleer resultaat
3. Download veilig
```

The target is a less form-like, more premium execution flow. The user should see upload/input, review and download as the dominant path, while secondary controls remain reachable.

## Protected safety controls

The following controls and boundaries must remain protected:

- The review table remains source of truth and fallback for replacement decisions and export construction.
- The side-by-side review remains the primary/central review surface.
- Manual missed-value entry remains available, including the user-facing `Gemiste waarde toevoegen` path and the underlying `manual_mask_entry` helper path into the replacement table.
- Export/download semantics must not change.
- Download filenames must not change.
- Download MIME types must not change.
- Export content must not change.
- Scrub Key JSON semantics must not change.
- Audit downloads must remain available.
- Scrub Key must remain visually separated from normal document downloads and warning-protected.
- Technical/audit details may be collapsed or secondary, but not removed.
- DOCX hygiene and audit details must remain reachable.

## Explicit non-goals

Review-surface simplification must not introduce or endorse:

- cloud processing;
- AI processing;
- OCR;
- restored PDF output;
- PDF-to-DOCX reconstruction;
- direct click-to-mark in document text;
- advanced editor;
- full-document marking;
- export blocking based on a new hidden gate;
- recognizer behavior changes;
- benchmark behavior changes;
- Scrub Key behavior or schema changes;
- reinsert behavior changes;
- runtime or startup behavior changes;
- dependency changes.

The old replacement decision helper panel must not return as normal user-facing UI.

## Implementation boundaries

A later implementation may:

- make the primary path calmer and less form-like;
- group secondary review controls under one clear secondary layer;
- make the replacement table reachable but less visually dominant by default;
- keep audit/technical details available in secondary/collapsed sections;
- improve visible copy and grouping.

A later implementation must not:

- change review table data semantics;
- change replacement logic;
- change export content;
- change download filenames;
- change download MIME types;
- change Scrub Key JSON semantics;
- change reinsert behavior;
- remove audit or DOCX hygiene access;
- hide review controls without a fallback;
- add cloud, AI, OCR, restored-PDF or PDF-to-DOCX behavior.

## Required app verification checklist for later implementation

When a later implementation package changes UI behavior, the live app verification checklist must confirm:

- primary flow is calmer and less form-like;
- upload/input, review and download are clearly discoverable;
- side-by-side review remains visible;
- replacement table remains reachable and source of truth;
- manual missed-value entry remains reachable;
- Scrub Key remains separated and warning-protected;
- audit/technical details remain available;
- no export semantics changed;
- no reinsert semantics changed;
- no Scrub Key semantics changed;
- no cloud, AI, OCR, restored-PDF or PDF-to-DOCX behavior appears;
- no Script execution error appears.

## Next package

The next implementation package may be:

```text
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION
```

Only start that implementation after these contract tests are accepted and the coordinator explicitly approves UI implementation.
