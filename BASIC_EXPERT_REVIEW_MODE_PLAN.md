# SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_PLAN

Status: completed planning/design-only.

Repository: `solidprivacy-nl/scrub`

## 1. Purpose

Scrub is moving from a technical prototype toward a professional document-control product. Recent UI work made the review surface calmer, but the interface still exposes too many expert controls in the normal path.

The next product-level simplification is a clear distinction between two review modes:

```text
Basiscontrole
Expertcontrole
```

The user should not be forced through all technical controls to complete a safe scrub. The goal is a true less-is-more MVP path for normal use, with expert controls still available for inspection, tuning, audit and troubleshooting.

Product thesis:

```text
Basiscontrole is not weaker review.
Basiscontrole is lower cognitive load with the same safety boundaries.
Expertcontrole is full inspection, tuning, audit and troubleshooting.
```

Basiscontrole should become the default user-facing MVP flow. Expertcontrole should expose the current detailed machinery.

## 2. Recommended naming

Evaluated naming options:

| Option | Strength | Weakness |
| --- | --- | --- |
| `Basis / Expert` | Short and easy to scan. | `Basis` alone can sound too casual or incomplete for legal/privacy review. |
| `Basiscontrole / Expertcontrole` | Keeps both modes framed as control/review workflows. Makes clear that basic mode is still serious. | Slightly longer labels. |
| `Standaard / Expert` | Familiar software pattern. | `Standaard` says less about review responsibility and may sound like a setting rather than a workflow. |
| `Snel controleren / Uitgebreid controleren` | Action-oriented and user-friendly. | “Snel” can imply speed over safety, which is undesirable for legal/privacy work. |

Recommendation:

```text
Basiscontrole
Expertcontrole
```

Reason:

Even the basic mode remains a legal/privacy control workflow. `Basiscontrole` communicates lower visual complexity without implying weaker safeguards. `Expertcontrole` communicates that full inspection and tuning controls are one step away.

## 3. Basiscontrole principles

Basiscontrole means:

- minimal primary path;
- no spreadsheet-first feeling;
- side-by-side review visible;
- simple correction available;
- safe download visible;
- advanced details collapsed or moved out;
- context-specific disclosure only when relevant;
- same safety semantics as Expertcontrole.

Basiscontrole should show the user the essential task:

```text
Add document -> check result -> download safely
```

It should not make the user decide whether every technical expander matters.

Basiscontrole must keep human review explicit. It may hide or collapse technical details, but it must not imply that the document is automatically safe without manual checking.

## 4. Expertcontrole principles

Expertcontrole is the place for full inspection, tuning, audit and troubleshooting.

It should expose:

- full replacement table;
- include/remember/find/replace_with review;
- candidate audit values;
- recognition details;
- thresholds/settings;
- Scrub Key details;
- audit downloads;
- DOCX hygiene audit;
- serial review;
- troubleshooting and legal/privacy audit work.

Expertcontrole may look more technical. That is acceptable because its purpose is full control and explainability.

## 5. Basiscontrole visible default

Basiscontrole should default to:

```text
1. Voeg document toe
2. Controleer resultaat
3. Download veilig
```

### 1. Voeg document toe

Visible by default:

- upload/dropzone;
- paste text or example;
- one short safety note.

Not visually dominant in Basiscontrole:

- profile internals;
- recognition/entity details;
- thresholds;
- advanced settings;
- long explanations about recognizers.

### 2. Controleer resultaat

Visible by default:

- side-by-side review;
- `Markeringen tonen`;
- replacement count, for example `16 vervanging(en) worden toegepast op de exports`;
- `Gemiste waarde toevoegen`;
- one collapsed correction/detail entry, for example `Details aanpassen`.

The review table remains the internal source of truth and fallback, but Basiscontrole should not feel spreadsheet-first.

### 3. Download veilig

Visible by default:

- primary scrubbed text download;
- Word download if available;
- PDF download if available;
- short warning that manual review remains required.

The primary download path should be easy to find. Scrub Key and audit downloads remain reachable but should not visually compete with normal document downloads.

## 6. Basiscontrole reachable but secondary

These controls remain reachable in Basiscontrole but should not dominate the main screen:

- `Vervangtabel controleren`;
- `Stap voor stap controleren`;
- `Mogelijk extra te controleren waarden`;
- `Herbruikbare vervangingen`;
- `Scrub Key downloaden`;
- `Audit en technische bestanden`;
- `DOCX hygiene audit`;
- `Technische informatie`;
- `Geavanceerde herkenningsdetails`.

Recommended Basiscontrole grouping:

```text
Details aanpassen
- Gemiste waarde toevoegen
- Vervangtabel controleren
- Stap voor stap controleren
- Mogelijk extra te controleren waarden
- Herbruikbare vervangingen

Meer bestanden
- Scrub Key downloaden
- Audit en technische bestanden
- DOCX hygiene audit

Expertcontrole
- Technische informatie
- Geavanceerde herkenningsdetails
- recognition/entity settings
- advanced replacement details
```

This keeps corrective controls close to the review task, while moving audit and technical controls away from the main path.

## 7. Expertcontrole visible default

Expertcontrole should expose the current complete interface more directly.

It should include:

- current sidebar control mode/profile options;
- recognition/entity settings;
- full replacement table;
- advanced replacement details;
- all audit/technical sections;
- Scrub Key controls;
- serial review;
- candidate audit review.

Expertcontrole can preserve most of the current detail-rich interface, but it should still avoid duplicate previews, debug-like copy and unsupported feature promises.

## 8. Mode switch behavior

Recommended mode switch behavior:

- A clear control near the top of the normal app flow.
- Default: `Basiscontrole`.
- `Expertcontrole` is one click away.
- Switching modes must not reset uploaded text, replacement decisions or session state.
- Switching modes changes visibility/grouping only.

The mode switch must not change:

- recognizer behavior;
- replacement logic;
- export output;
- Scrub Key JSON;
- reinsert behavior;
- audit generation.

Mode selection should be treated as UI state, not processing state.

## 9. Conditional disclosure

Basiscontrole should use contextual disclosure rather than showing every possible control at all times.

Recommended conditional behavior:

- DOCX hygiene audit only appears for DOCX or DOCX-derived flows;
- PDF limitations only appear for PDF input;
- candidate audit values only appear when candidates exist;
- Scrub Key warning appears when the Scrub Key section is opened or the key download is requested;
- audit downloads sit under a secondary file/details section;
- recognition details are primarily in Expertcontrole.

This is part of the less-is-more philosophy: if a control is not relevant to the current document or flow, it should not compete for attention.

## 10. Safety boundaries

The Basiscontrole / Expertcontrole plan must preserve:

- legal/professional context;
- review table as source of truth internally;
- manual missed-value correction;
- export/download semantics;
- Scrub Key warning protection;
- local-only/no-cloud/no-AI boundary;
- no OCR;
- no restored PDF promise;
- no PDF-to-DOCX reconstruction;
- no hidden export gate;
- no advanced editor;
- no click-to-mark implementation;
- no full-document marking.

Basiscontrole may simplify visibility and grouping. It must not weaken privacy, review, export, Scrub Key, reinsert, audit or document-hygiene controls.

## 11. Implementation sequencing

Recommended next packages:

```text
SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_CONTRACT_TESTS
SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_IMPLEMENTATION
SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_APP_VERIFY_CLOSEOUT
```

Implementation must not start until contract tests are merged.

The contract-test package should protect:

- Basiscontrole default;
- Expertcontrole one click away;
- mode switch is visibility-only;
- side-by-side review remains visible in Basiscontrole;
- manual missed-value correction remains reachable in Basiscontrole;
- replacement table remains reachable in Basiscontrole and visible in Expertcontrole;
- Scrub Key remains separate and warning-protected;
- downloads remain visible and unchanged;
- audit/technical details remain available;
- no export/Scrub Key/reinsert/recognizer/benchmark/runtime semantics changed.

## 12. Future implementation checklist

The later implementation package should verify:

- Basiscontrole is default;
- Basiscontrole is visually cleaner than the current interface;
- Expertcontrole exposes full controls;
- switching mode does not reset session state;
- side-by-side review remains visible in Basiscontrole;
- manual missed-value entry remains reachable in Basiscontrole;
- replacement table remains reachable in Basiscontrole and visible in Expertcontrole;
- Scrub Key remains separate and warning-protected;
- downloads remain visible and unchanged;
- audit/technical details remain available;
- no Script execution error;
- no export/Scrub Key/reinsert/recognizer/benchmark/runtime semantics changed.

## 13. Non-goals for the planning package

This planning package does not:

- change product code;
- implement a Streamlit UI switch;
- edit `presidio_streamlit.py`;
- edit side-by-side, serial review or manual mask helpers;
- change export/download behavior;
- change Scrub Key behavior or schema;
- change reinsert behavior;
- change recognizers or benchmark logic;
- change runtime/startup behavior;
- change dependencies.

## 14. Decision to record

Recommended product decision:

```text
Use Basiscontrole / Expertcontrole as the planning names for the two normal review-mode layers.
Basiscontrole is the default MVP path.
Expertcontrole exposes the full inspection/audit machinery.
Mode switching changes visibility only, not processing or export semantics.
```
