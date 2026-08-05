# SolidPrivacy Scrub — Premium core-flow UI realignment plan

Workpackage: `SCRUB-WP_PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN`

Repository: `solidprivacy-nl/scrub`

Status: completed planning/design-only.

Date: 2026-08-05 10:49 Europe/Amsterdam

## 1. Why this realignment is needed

The existing UI simplification work was useful and should be preserved:

- `Basiscontrole / Expertcontrole` was introduced and app-verified;
- Basiscontrole was materially decluttered;
- duplicate input presentation was reduced;
- side-by-side review became the central review surface;
- review and export density were reduced;
- secondary audit and correction controls were collapsed;
- direct masking from processed text was integrated;
- bound placeholders now display compactly in review.

The remaining problem is structural rather than local.

The current app still presents most of the workflow as one long Streamlit page. Input, profile controls, explanations, work-mode radios, settings, review controls, status messages, correction sections, multiple download buttons, Scrub Key controls and audit sections remain visible in the same vertical document.

That creates a form and website feeling even when individual blocks are collapsed.

The required product shift is:

```text
Long configuration form
→ single-task document workspace
```

The target is a polished, customer-grade and enterprise-credible application with a clear purpose and minimal distraction.

## 2. Product thesis

The standard workflow must communicate one simple promise:

```text
Add document or text
→ inspect the protected result
→ download the result
```

Everything else is supporting functionality.

Supporting functionality remains available, but it must not compete visually with the primary task.

This means:

- one active stage at a time;
- one dominant primary action per stage;
- progressive and conditional disclosure;
- no spreadsheet-first or settings-first opening state;
- no permanent technical sidebar in the standard view;
- no equal visual weight for normal document download, Scrub Key, audit files and technical details;
- no weakening of privacy, review, export, Scrub Key, reinsert or audit controls.

## 3. Where the earlier Basic/Expert discussion stands

The repository already contains and has implemented the `Basiscontrole / Expertcontrole` direction.

That work solved a narrower problem: it changed visibility inside the review area and made the normal review path calmer.

It did not yet turn the whole application into two coherent presentation layers. The current mode selector is still another form control inside the page, while global profile settings, input alternatives, workflow mode, audit controls and downloads remain distributed across the sidebar and main page.

The next version therefore elevates the concept from a review-local switch to an application-wide view model.

Recommended user-facing labels:

```text
Standaard
Expert
```

Reason:

- `Standaard` describes the intended normal product experience without implying weaker privacy control;
- `Expert` remains familiar for full inspection and troubleshooting;
- `Basiscontrole` sounds review-specific and does not describe input, export and reinsert presentation;
- the switch controls visibility and grouping only, never processing safety.

The final naming must be frozen in the contract package before UI implementation.

## 4. Target application architecture

### 4.1 Top-level workflows

The current inline work-mode radio should become top-level application navigation:

```text
Anonimiseren | Terugzetten
```

These are separate user goals and should not be presented as a question inside a long form.

Each workflow keeps its own focused stages and state.

### 4.2 Global app header

The standard application header should contain only:

- SolidPrivacy Scrub identity;
- active workflow: `Anonimiseren` or `Terugzetten`;
- active domain/profile as one compact badge or selector, for example `Juridisch` or `Zorg`;
- a compact `Instellingen` entry;
- a `Standaard / Expert` view switch;
- a compact public-prototype warning where required.

Long product explanations, `Over deze app` and recognition internals move to Help/About or Expert settings.

### 4.3 One active stage at a time

The anonymization workspace has three visible stages:

```text
1. Toevoegen
2. Controleren
3. Downloaden
```

Only the active stage is expanded as the main workspace.

Completed stages collapse into compact summaries, for example:

```text
✓ Document toegevoegd — contract.docx — Wijzigen
✓ 17 vervangingen gecontroleerd — Terug naar controle
```

This is the primary structural change needed to stop the interface feeling like a web form.

## 5. Standard view target

### Stage 1 — Toevoegen

The standard view should not display a file uploader, example selector and large text area simultaneously.

Use one source-method choice:

```text
Bestand uploaden | Tekst plakken
```

Default to `Bestand uploaden`.

Visible content:

- one large dropzone or one paste area;
- current profile shown compactly;
- one primary action: `Document controleren`;
- one secondary text action: `Voorbeeld gebruiken`;
- concise file/type and local-processing information.

Moved out of the primary surface:

- detailed profile explanation;
- replacement-method dropdown;
- recognized entity-type list;
- thresholds and advanced recognition settings;
- long prototype description;
- simultaneously visible unused input alternatives.

An explicit processing action is the preferred target because it creates a clear stage transition and avoids the feeling that every field immediately recomputes a form. This changes visible execution state and therefore requires a dedicated state-model contract before implementation. It must never permit stale review or export state.

### Stage 2 — Controleren

Visible content:

- compact result summary, for example `17 waarden afgeschermd · 1 controle nodig`;
- the unified source-versus-processed review surface;
- compact marker toggle;
- direct masking of a missed value from processed text;
- one secondary entry: `Details aanpassen`;
- one primary action: `Naar downloaden` or `Controle afronden`.

Moved behind `Details aanpassen` or Expert view:

- full replacement table;
- serial review;
- candidate/audit details when no candidate exists;
- reusable replacement internals;
- technical recognition details;
- review-governance explanations;
- multiple status paragraphs.

Safety messages should be short, contextual and actionable. Engineering governance remains in tests, documentation and audit details rather than normal-page captions.

### Stage 3 — Downloaden

The standard view should present one recommended document download rather than three equal primary buttons.

Target:

```text
[Primary] Download opgeschoond document
Andere formaten ▾
```

The recommended format is source-aware and must be frozen in a contract before implementation. Existing bytes, filenames, MIME types and eligibility remain unchanged.

Secondary groups:

```text
Later terugzetten
- Scrub Key with explicit sensitivity warning

Controlebewijs en details
- scrub report
- replacement table
- document-hygiene audit
- technical recognition evidence
```

The Scrub Key is not a normal companion download. It remains reachable but does not visually compete with the primary cleaned document.

## 6. Expert view target

Expert view provides complete inspection, tuning, audit and troubleshooting.

It may expose:

- profile and recognition configuration;
- replacement method and entity controls;
- full replacement table;
- all correction and candidate layers;
- serial review;
- all document formats;
- Scrub Key details;
- audit and technical files;
- DOCX hygiene details;
- technical recognition evidence.

Expert view should still use the same stage model and application shell. It must not revert to an unstructured dump of every control.

Switching between Standard and Expert:

- must preserve uploaded input;
- must preserve current replacement decisions;
- must preserve review state;
- must preserve exports and Scrub Key semantics;
- must not trigger silent profile or recognition changes;
- must not reset session state.

## 7. Sidebar policy

The current sidebar is one of the strongest sources of the configuration-form feeling.

Target policy:

```text
Standard view: no permanent configuration sidebar.
Expert view: sidebar or settings drawer may expose full controls.
```

In Standard view, the active profile appears as a compact badge or selector in the header. Less-used settings open through one settings surface rather than several sidebar dropdowns and help expanders.

## 8. Progressive and conditional disclosure

Only show controls that are relevant to the current document and stage.

Examples:

- DOCX hygiene controls only for DOCX-related flows;
- PDF limitations only for PDF input/output;
- candidate review only when candidates exist;
- undo only immediately after a reversible action;
- Scrub Key warning when the restore option is opened or requested;
- audit files only under the audit/details entry;
- recognition settings primarily in Expert view;
- reinsert controls only inside the `Terugzetten` workflow.

Conditional disclosure should reduce visual noise, not hide important warnings at the moment they matter.

## 9. Visual language

The first implementation remains inside Streamlit, but should approximate an application shell rather than a webpage.

Principles:

- one centered work canvas with controlled maximum width;
- strong whitespace and clear typographic hierarchy;
- few borders and containers;
- one primary button per active stage;
- secondary actions as text buttons, menus or compact links;
- status chips instead of repeated explanatory paragraphs;
- completed-stage summaries instead of keeping all stages open;
- no deep stacks of nested expanders;
- no debug, prototype-governance or implementation vocabulary in the primary flow;
- no external asset, telemetry or cloud dependency required.

A later Tauri desktop shell can improve native chrome and distribution, but the web prototype should first reach a credible client-grade information architecture.

## 10. Existing elements: target treatment

| Current element | Standard target | Expert target |
| --- | --- | --- |
| Sidebar control profile | compact header badge/settings | fully available |
| `Wat doet deze controlemodus?` | tooltip/help | available in settings |
| Replacement method dropdown | hidden default | visible |
| Advanced settings/entity types | settings only | visible |
| Inline `Anonimiseren / Terugzetten` radio | top-level workflow navigation | same navigation |
| `Over deze app` | help/about menu | help/about menu |
| Upload + example + textarea together | one source method at a time | all methods available but structured |
| Review-mode radio inside review | global view switch | global view switch |
| Long review guidance | concise contextual copy | detailed guidance available |
| Full replacement table | `Details aanpassen` | visible/reachable directly |
| Three equal document download buttons | one recommended download + other formats | all formats visible |
| Scrub Key download | separate restore option | full details visible |
| Audit/technical expanders | one secondary audit entry | full audit stack |

## 11. Safety and semantic boundaries

This realignment must not:

- weaken human review;
- hide unresolved warnings when action is required;
- change recognizer behavior or active profile silently;
- change replacement rows or inclusion decisions;
- change export bytes, filenames, MIME types or eligibility without separate approval;
- change Scrub Key schema, binding, digest, warning or lifecycle;
- change reinsert semantics;
- introduce cloud document processing, telemetry or browser persistence;
- remove audit or technical evidence;
- imply production readiness.

Standard view is lower cognitive load, not lower safety.

## 12. Implementation sequence

The UI line remains sequential because the same Streamlit workflow surfaces are shared.

Recommended sequence:

```text
0. SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION
   Freeze the currently live selection/export/Scrub-Key/reinsert safety baseline before structural UI changes.

1. SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT
   Freeze stage model, global view behavior, top-level workflow navigation, primary/secondary hierarchy and semantic non-change boundaries.

2. SCRUB-WP_PREMIUM_CORE_FLOW_STATE_MODEL
   Implement pure state-transition helpers for input → review → export, stale-state invalidation and back/edit behavior before Streamlit integration.

3. SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION
   Add the global header, Standard/Expert view state, top-level Anonymize/Reinsert navigation and one-active-stage shell.

4. SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION
   Make file upload versus pasted text mutually exclusive in Standard view and move profile/settings details to the secondary settings surface.

5. SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION
   Keep summary, side-by-side review, marker toggle and direct correction primary; move the detailed review machinery to `Details aanpassen` or Expert view.

6. SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION
   Add one source-aware recommended download, move other formats to a secondary menu and separate Scrub Key plus audit evidence without changing payload semantics.

7. SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION
   Prove all current controls and outputs remain available and state-preserving in Expert view.

8. SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT
   Verify Actions, Hugging Face synchronization and the live app with focused Standard and Expert scenarios.
```

Do not implement input, review and export restructuring in one large patch. Do not run parallel changes to `presidio_streamlit.py`, the side-by-side review flow or export flow.

## 13. Definition of done

The interface line is complete when a normal user can:

1. open Scrub and immediately understand the task;
2. choose or drop one document without confronting irrelevant settings;
3. start one clear control action;
4. review the result in one focused workspace;
5. correct a missed value without leaving the document context;
6. continue through one clear primary action;
7. download one recommended cleaned document;
8. find other formats, Scrub Key and audit evidence without those elements dominating the screen;
9. switch to Expert without state loss;
10. complete the same supported workflow with unchanged safety and export semantics.

The target is not merely fewer controls. The target is a coherent, confident and polished document-control application.