# SolidPrivacy Scrub — Premium Core Flow UI Contract

Workpackage: `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT`  
Issue: #79  
Role: `implementation_operations`  
Status: `IMPLEMENTATION_CANDIDATE`  
Base: `e9ad2df16cdb03591d7d2521d2c5509ad648a400`

## 1. Purpose

Freeze the product-facing interaction contract for the premium Scrub workspace before state-model and Streamlit implementation begins.

The product target is a single-task professional document workspace rather than a long configuration form.

```text
Add document or text
→ inspect the protected result
→ download the result
```

This contract governs presentation, stage progression and disclosure only. It does not authorize any change to processing semantics.

## 2. Top-level application model

### Workflows

The application exposes two top-level user goals:

```text
Anonimiseren | Terugzetten
```

They are navigation destinations, not a form question inside the workspace. Each goal owns its own focused stage state.

### Presentation mode

The global presentation switch is:

```text
Standaard | Expert
```

`Standaard` is the normal product experience. `Expert` exposes complete inspection, tuning, audit and troubleshooting. The switch changes visibility and grouping only; it never weakens privacy, review or validation behavior.

## 3. Standard anonymization stages

The Standard anonymization workflow contains exactly three primary stages:

```text
1. Toevoegen
2. Controleren
3. Downloaden
```

Exactly one stage is the dominant expanded workspace at a time. Completed stages collapse to compact summaries with an explicit action to return or edit.

Example summaries:

```text
✓ Document toegevoegd — contract.docx — Wijzigen
✓ 17 vervangingen gecontroleerd — Terug naar controle
```

A stage may not be marked complete unless its required state is valid for the current source document and current processing generation.

## 4. Stage 1 — Toevoegen

### Primary contract

Only one input method is active and visually dominant at a time:

```text
Bestand uploaden | Tekst plakken
```

Default: `Bestand uploaden`.

Visible in Standard:

- one large file dropzone or one paste surface;
- compact active profile/domain identity;
- concise local-processing/file support information;
- one dominant primary action: `Document controleren`;
- one secondary text action: `Voorbeeld gebruiken`.

Not simultaneously exposed in Standard:

- unused input alternative;
- recognition internals and entity lists;
- thresholds and advanced detection settings;
- replacement-method configuration;
- long prototype/product explanations.

### Transition invariant

`Document controleren` creates an explicit processing boundary. The UI may only move to `Controleren` after a valid current processing result exists. A new source, source edit, profile change that affects processing, or explicit reprocess invalidates downstream review/export state according to the later state-model contract.

## 5. Stage 2 — Controleren

Visible in Standard:

- compact result summary such as `17 waarden afgeschermd · 1 controle nodig`;
- unified source-versus-processed review surface;
- compact marker/highlight control;
- direct masking of a missed value from processed text;
- one secondary disclosure action: `Details aanpassen`;
- one dominant completion action: `Controle afronden` / `Naar downloaden`.

Secondary or Expert-only presentation:

- complete replacement table;
- serial review;
- candidate/audit detail when not contextually needed;
- reusable replacement internals;
- technical recognition evidence;
- engineering/governance explanatory text.

### Authority invariant

The existing authoritative review-table/include state remains the source of truth. The premium review surface is a presentation and interaction layer over that authority, not a replacement data model.

Direct missed-value masking must continue to create a normal authoritative manual review row and must retain existing undo/export/Scrub-Key/reinsert behavior.

## 6. Stage 3 — Downloaden

Standard presents one recommended cleaned-document action as the dominant export control:

```text
Download opgeschoond document
```

The recommended file is source-aware:

- source DOCX → recommend the existing eligible cleaned DOCX;
- source TXT/plain text → recommend the existing eligible text download;
- source PDF → recommend only an already-supported safe cleaned output according to existing export eligibility; this contract creates no new PDF mutation semantics;
- when the preferred source-preserving format is not eligible, use the existing safe fallback already produced by Scrub and explain that choice concisely.

This recommendation changes visual priority only. Existing file bytes, filenames, MIME types and eligibility rules remain unchanged.

Secondary groups:

### Andere formaten

Contains other already-supported document/text exports. No new format is created by this package.

### Later terugzetten

Contains the Scrub Key with explicit sensitivity treatment. The Scrub Key must never visually compete with the normal cleaned-document download or appear as an ordinary companion file.

### Controlebewijs en details

Contains existing evidence such as:

- scrub report;
- replacement table/CSV;
- document-hygiene audit;
- technical recognition/audit evidence.

## 7. Standard sidebar policy

Standard has no permanent configuration sidebar.

The application header may show:

- SolidPrivacy Scrub identity;
- current workflow;
- compact active profile/domain selector or badge;
- one `Instellingen` entry;
- `Standaard / Expert` switch;
- required compact prototype warning.

Less-used configuration opens through one secondary settings surface.

## 8. Expert contract

Expert retains full current capability, including:

- profile and recognition configuration;
- replacement method/entity controls;
- full replacement table;
- correction/candidate layers;
- serial review;
- all eligible document formats;
- Scrub Key detail;
- audit and technical evidence;
- document-hygiene detail.

Expert still uses the same stage model. It must not become an unstructured dump of all controls.

## 9. State-preservation invariants

Switching `Standaard ↔ Expert` must preserve, without silent recomputation or reset:

- uploaded/pasted source identity;
- active workflow;
- active profile unless explicitly changed by the user;
- current authoritative replacement decisions;
- review include/exclude state;
- manual correction rows;
- current stage when still valid;
- export eligibility and generated-result identity;
- Scrub Key/reinsert semantics.

Changing presentation mode must not:

- trigger recognition;
- mutate replacements;
- generate a new Scrub Key;
- reset review state;
- change document bytes;
- change profile or threshold values;
- make stale exports appear current.

## 10. Freshness / stale-state contract for next package

The following must be explicitly represented in `SCRUB-WP_PREMIUM_CORE_FLOW_STATE_MODEL`:

1. source generation identity;
2. processed-result generation identity;
3. review-valid-for generation identity;
4. export-valid-for generation identity;
5. active stage;
6. presentation mode;
7. active workflow;
8. invalidation rules for source/profile/processing changes.

Minimum rule:

```text
current export generation == current reviewed processing generation == current source generation lineage
```

The UI must fail closed to an earlier stage whenever that lineage no longer holds.

## 11. Prohibited semantic changes

This contract does not authorize changes to:

- recognizers or entity coverage;
- confidence thresholds;
- profile meaning;
- replacement semantics;
- review-table authority;
- placeholder grammar or binding strength;
- Scrub Key schema, binding or encryption/storage behavior;
- TXT/DOCX reinsert semantics;
- document hygiene behavior;
- output bytes, names, MIME types or eligibility;
- audit semantics;
- local-only/privacy guarantees;
- dependencies, deployment or hosting.

Any such change requires a separate consequential workpackage.

## 12. Acceptance tests required from the next state-model package

The state-model candidate must provide pure/synthetic tests proving at minimum:

1. initial Standard anonymization state opens at `Toevoegen`;
2. selecting `Expert` preserves source and all authoritative processing/review state;
3. returning to `Standaard` preserves the same state;
4. valid processing advances `Toevoegen → Controleren`;
5. invalid/stale processing cannot advance;
6. completed review advances `Controleren → Downloaden` only for the current generation;
7. source replacement invalidates review and download stage state;
8. processing-affecting profile changes invalidate downstream state;
9. presentation-only settings do not invalidate processing;
10. manual review rows and include/exclude decisions survive Standard/Expert switching;
11. source-aware recommended download selection is presentation-only and returns only an already-eligible existing output;
12. Scrub Key remains secondary and unchanged;
13. top-level `Anonimiseren ↔ Terugzetten` navigation cannot leak stale cross-workflow state;
14. no stage transition mutates recognizer/replacement/export semantics.

## 13. Governance / next gate

This document is an implementation candidate for the contract package only.

Required sequence:

```text
contract candidate
→ independent governance_release_assurance
→ PASS
→ SCRUB-WP_PREMIUM_CORE_FLOW_STATE_MODEL
```

No Streamlit/UI integration is authorized by this contract candidate itself.
