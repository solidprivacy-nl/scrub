# Bound placeholder display compaction

Status: approved narrow implementation contract

## Problem

Schema-1.1 placeholders repeat one 80-bit document binding in every token. That binding protects against applying a valid Scrub Key to the wrong document, but makes the review pane unnecessarily difficult to scan.

Example full token:

```text
[LOCATIE_BSK732WYQ424ZIEQ6_02]
```

## Decision

Compact only the visible review representation:

```text
[LOCATIE_BSK732WYQ424ZIEQ6_02]          -> [LOCATIE_02]
[EMAIL_BSK732WYQ424ZIEQ6_HANDMATIG_03] -> [EMAIL_H_03]
```

The complete source token remains unchanged and remains the only token used by server validation, replacement rows, exported documents, Scrub Key mappings and reinsert.

## Frozen boundaries

- Binding grammar remains `B` plus sixteen uppercase RFC 4648 base32 characters.
- Binding entropy remains 80 bits.
- Compaction applies only to strict schema-1.1 bound placeholders.
- Legacy placeholders, free replacement text and malformed near-placeholders remain visually unchanged.
- Every display segment retains its exact source UTF-16 start and end offsets.
- A selection after any compact placeholder resolves to the original source offset.
- A selection intersecting a compact placeholder remains blocked.
- Full tokens may be exposed as non-mutating hover/accessibility metadata.
- No export, Scrub Key, reinsert, filename, MIME, recognizer, profile, dependency or cloud-processing change.
- The review table remains source of truth.
- The static fallback follows the same display rule but remains non-interactive.

## Validation gates

1. Pure Python display-helper tests.
2. Pure frontend core tests, including UTF-16 offsets after compact tokens.
3. Existing component and full Python regression.
4. GitHub-to-Hugging-Face byte equality and Space health.
5. Focused live app verification because the review UI changes.
