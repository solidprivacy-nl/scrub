# TWO_MODE_UI_SPEC — v13.5 Two-mode reinsert UI planning

Status: planning/specification only.  
Workpackage: WP11 — v13.5 Two-mode reinsert UI planning.  
Repository: `solidprivacy-nl/scrub`.  
Date: 2026-06-08.

This document plans the future two-mode user interface before changing Streamlit UI code.

No UI code, export behavior, Scrub Key behavior, AI calls, cloud processing, TXT/DOCX reinsert UI, or PDF reinsert is implemented by this document.

---

## 1. Executive recommendation

Scrub should move to a clear two-mode interface:

```text
1. Anonimiseren
2. Originele waarden terugzetten
```

The first implementation should use two main Streamlit tabs or two clearly separated mode panels, not a large landing-page refactor yet.

Recommended first implementation direction:

```text
Use tabs first:

Tab 1: Anonimiseren
Tab 2: Originele waarden terugzetten
```

Reason:

- tabs are the lowest-risk way to create explicit mode separation in the current patch-based Streamlit app;
- they reduce confusion between scrubbing and restoring;
- they preserve the current working anonymization/export flow;
- they allow the reinsert flow to move out of the long export section gradually;
- they avoid a full navigation refactor before the UI code is ready.

Longer-term product direction:

```text
Landing choice with two large cards/buttons
```

The landing-card design is the better mature product experience, but it should come after the current patch-based UI has been simplified or replaced.

---

## 2. Required planning questions answered

### 1. Should the app start with a mode choice?

Yes.

The user should immediately understand whether they are:

```text
making content safer by anonymizing/pseudonymizing it
```

or:

```text
restoring original sensitive values with a Scrub Key
```

These are different privacy states and different user intents.

### 2. Should the modes be tabs, a landing choice, or separate sections?

Recommended near-term implementation:

```text
Streamlit tabs or two very clear mode panels.
```

Recommended long-term product design:

```text
Landing choice with two large cards/buttons.
```

Not recommended as the next step:

```text
Separate pages or full navigation refactor.
```

Separate pages may become useful later, but are too large for the next small workpackage.

### 3. How should `Anonimiseren` work from start to finish?

The `Anonimiseren` mode should contain the existing source-document workflow:

1. User uploads or pastes source text/document.
2. Scrub detects sensitive values locally.
3. User reviews detected replacements in the replacement table.
4. User keeps legal meaning readable by deciding which replacements are included.
5. User downloads currently supported scrubbed outputs:
   - TXT;
   - CSV where available;
   - DOCX where available;
   - PDF where available.
6. User optionally downloads a Scrub Key JSON.
7. UI warns that the Scrub Key makes the text reversible and is pseudonymization, not full anonymization.
8. User keeps the Scrub Key local and protected.

### 4. How should `Originele waarden terugzetten` work from start to finish?

The `Originele waarden terugzetten` mode should contain only restoration/reinsert actions:

1. User loads or pastes a Scrub Key.
2. App validates the Scrub Key locally.
3. User chooses input type:
   - paste text;
   - upload TXT;
   - upload DOCX.
4. User explicitly clicks a restore action.
5. App reinserts original values locally using deterministic helpers.
6. App shows restored output.
7. App shows an audit summary.
8. App warns that restored output may contain personal or confidential information again.
9. User downloads restored TXT or restored DOCX where supported.

The app must not automatically restore values when a key is loaded.

### 5. Where should TXT/DOCX document-level reinsert fit?

TXT/DOCX reinsert belongs only inside:

```text
Originele waarden terugzetten
```

It should not be placed inside the normal anonymization/export section because restored output has the opposite privacy meaning from scrubbed output.

Recommended order inside the reinsert mode:

```text
1. Scrub Key laden
2. Invoer kiezen
   - tekst plakken
   - TXT uploaden
   - DOCX uploaden
3. Originele waarden lokaal terugzetten
4. Controleverslag terugzetten
5. Download herstelde uitvoer
```

### 6. How should pasted-text reinsert remain available?

Pasted-text reinsert should remain the first and simplest reinsert option.

It should be labelled clearly as:

```text
Tekst plakken
```

Use cases:

- AI chat output;
- short email snippets;
- copied plain text;
- debugging/review;
- fallback when document upload is not suitable.

Pasted-text reinsert should not be removed when TXT/DOCX upload is added.

### 7. How should Scrub Key import/export be presented safely?

Scrub Key export belongs in `Anonimiseren` because the key is created from reviewed replacements.

Scrub Key import belongs in `Originele waarden terugzetten` because the key is needed to restore original values.

Both modes must use strong warning language:

```text
Een Scrub Key maakt vervangen waarden lokaal herleidbaar.
Dit is pseudonimisering, geen volledige anonimisering.
Bewaar de sleutel lokaal en beveiligd.
Deel de Scrub Key niet met AI-diensten of derden tenzij dat bewust en toegestaan is.
```

The UI should make this distinction clear:

```text
Anonimiseren: Download Scrub Key (.json)
Originele waarden terugzetten: Upload/plak Scrub Key (.json)
```

### 8. How should the app avoid users confusing anonymization with de-anonymization?

Use explicit mode labels and privacy-state captions:

```text
Anonimiseren
Maak tekst of documenten veiliger voor AI of delen.
Uitvoer: opgeschoonde tekst/documenten.

Originele waarden terugzetten
Gebruik een Scrub Key om placeholders lokaal terug te zetten.
Uitvoer: herstelde tekst/documenten met mogelijk weer gevoelige waarden.
```

Do not place restored downloads next to scrubbed downloads without clear separation.

Use separate labels:

```text
Download opgeschoonde tekst/document
Download herstelde tekst/document
```

### 9. Which UI changes should be made first?

First implementation should be:

```text
WP12 — v13.6 Two-mode UI skeleton and tab separation
```

Scope:

- add two clear tabs/panels;
- keep current anonymization workflow in `Anonimiseren`;
- place current Scrub Key load + pasted-text reinsert flow under `Originele waarden terugzetten` if feasible;
- preserve existing exports and download labels;
- add patch-level UI tests for the mode labels and no-AI/no-cloud boundaries;
- ask for app verification because UI behavior changes.

### 10. Which UI changes should explicitly not be made yet?

Do not build yet:

- full landing-card refactor;
- separate multi-page navigation;
- TXT upload reinsert UI in the same first skeleton phase;
- DOCX upload reinsert UI in the same first skeleton phase;
- PDF reinsert;
- OCR;
- AI calls;
- cloud processing;
- server-side Scrub Key storage;
- metadata-clean DOCX promises;
- batch folder reinsert;
- automatic reinsertion after key upload;
- changes to existing scrubbed export/download semantics.

---

## 3. Model architecture perspective

### 3.1 Separate pipelines

Scrub should show two pipelines as separate user modes.

```text
Pipeline 1 — Anonymization
source text/document
-> local recognition
-> human review
-> scrubbed output
-> optional Scrub Key export
-> audit/export

Pipeline 2 — Reinsert
Scrub Key + AI output / scrubbed output
-> local validation
-> deterministic placeholder replacement
-> restored output
-> audit/download
```

The pipelines may share helper modules, but UI state should stay explicit and auditable.

### 3.2 Scrub Key as reversible local mapping

The Scrub Key is not a normal settings file. It is a sensitive reversible mapping between placeholders and original values.

It must be treated as:

```text
local
protected
reversible
pseudonymization, not full anonymization
```

The UI should not encourage users to upload a Scrub Key to external AI services.

### 3.3 Text reinsert versus document reinsert

Text reinsert remains the core deterministic logic.

Existing helper:

```python
reinsert_from_scrub_key(text, scrub_key) -> dict
```

Document-level reinsert should wrap this logic, not create a competing replacement engine.

Current WP10 helper foundation:

```python
reinsert_text_document(text, scrub_key) -> dict
reinsert_txt_bytes(content, scrub_key, encoding="utf-8") -> dict
reinsert_docx_bytes(content, scrub_key) -> dict
```

### 3.4 TXT/DOCX helper from WP10

WP10 added a local helper/test foundation for TXT and DOCX reinsert.

TXT support:

- accepts text and bytes;
- decodes bytes locally;
- returns restored text/bytes;
- reports audit fields.

DOCX support:

- processes `word/document.xml` text nodes only;
- supports normal body paragraphs and tables in `word/document.xml`;
- returns restored DOCX bytes;
- reports limitations.

DOCX limitations must remain visible when the UI is added.

### 3.5 PDF excluded for now

PDF reinsert should remain out of implementation scope.

Reasons:

- text extraction can be unreliable;
- layout reconstruction is non-trivial;
- scanned PDFs may require OCR;
- OCR raises accuracy, privacy and dependency questions;
- restored PDF output could falsely imply document fidelity.

A later workpackage may investigate text-based PDF extraction only, without full restored PDF output.

### 3.6 No AI calls inside Scrub

Scrub should not call AI in the reinsert workflow.

The product role is:

```text
scrub before AI
restore after AI
```

The AI step happens outside Scrub.

### 3.7 Local-only design

The mode split should reinforce local-only processing:

- no AI provider calls;
- no cloud document conversion;
- no server-side Scrub Key storage;
- no durable vault unless explicitly approved later;
- no real personal data in tests/docs.

---

## 4. UX / visual structure

### Option A — Current single-scroll workflow

Description:

The app keeps one long page where upload, recognition, review, export, Scrub Key, import and reinsert live in sequence.

Pros:

- already works;
- lowest immediate implementation cost;
- avoids restructuring the patch-based Streamlit flow.

Cons:

- users may miss the difference between scrubbed output and restored output;
- reinsert is buried near export/download controls;
- restored downloads can feel like normal scrubbed downloads;
- cognitive load grows as TXT/DOCX reinsert is added;
- privacy state is not explicit enough.

Assessment:

```text
Acceptable temporarily, but not suitable for the next growth step.
```

### Option B — Streamlit tabs

Description:

The app uses two top-level tabs:

```text
Anonimiseren
Originele waarden terugzetten
```

Pros:

- low-to-medium implementation risk in Streamlit;
- clear mode separation;
- preserves existing one-page app structure;
- avoids immediate full navigation refactor;
- makes future TXT/DOCX reinsert placement obvious;
- supports patch-level UI tests for labels and boundaries.

Cons:

- tabs may still share session state if implementation is careless;
- current patch-based flow may need careful wrapping;
- less polished than a landing-card product experience.

Assessment:

```text
Recommended first implementation direction.
```

### Option C — Landing choice with two large cards/buttons

Description:

The app starts with two large choices:

```text
[Anonimiseren]
Maak tekst of documenten veilig voor AI of delen.

[Originele waarden terugzetten]
Gebruik een Scrub Key om placeholders lokaal terug te zetten.
```

Pros:

- best mental model;
- strongest privacy-state separation;
- good for desktop/offline product later;
- feels like a mature product, not a demo page.

Cons:

- larger refactor;
- requires stronger routing/state design;
- more risk in the current patch-based UI layer;
- could slow down the next incremental implementation.

Assessment:

```text
Best long-term product direction, but not the first implementation step.
```

### Visual recommendation

Use tabs first, landing cards later.

Recommended near-term layout:

```text
Titel: SolidPrivacy Scrub
Caption: Kies eerst wat u wilt doen.

Tab 1 — Anonimiseren
Tab 2 — Originele waarden terugzetten
```

Recommended mode captions:

```text
Anonimiseren
Maak tekst of documenten veiliger voor AI of delen. Controleer altijd de vervangingen vóór export.

Originele waarden terugzetten
Gebruik een Scrub Key om placeholders lokaal terug te zetten. De uitvoer kan weer gevoelige informatie bevatten.
```

---

## 5. Strategic product direction

### 5.1 Reinsert is a separate user intent

Anonymization and reinsert are not two versions of the same action.

Anonymization reduces exposure risk by replacing sensitive values.

Reinsert increases sensitivity again by restoring original values.

The UI should therefore treat them as separate user intents.

### 5.2 Legal users need privacy-state clarity

Legal users work with confidential process documents, case files and AI outputs. They need to know whether a document is:

```text
source/confidential
scrubbed/pseudonymized
scrubbed and reversible with key
restored/confidential again
```

The two-mode UI should make this status visible.

### 5.3 Restored output is sensitive again

The reinsert mode must warn clearly:

```text
Terugzetten herstelt originele gevoelige waarden. De uitvoer kan weer persoonsgegevens of vertrouwelijke informatie bevatten. Controleer het resultaat zorgvuldig voordat u het deelt.
```

This warning should appear before the restore action and near the output/download.

### 5.4 Document-level reinsert matters for real AI workflows

Pasted text is useful, but real legal work often produces DOCX outputs and sometimes PDFs.

Document-level reinsert matters because users want to receive a restored document rather than manually rebuild formatting after copy/paste.

The product should support this carefully:

```text
text paste first
TXT upload second
DOCX upload third
PDF later only after reliability review
```

### 5.5 PDF remains later

PDF should remain out of implementation scope until a separate reliability review.

The product should not imply reliable PDF rehydration while only text extraction or partial replacement is possible.

---

## 6. Tactical implementation plan

### Phase 1 — Add two-mode UI skeleton / navigation only

Recommended next implementation workpackage:

```text
WP12 — v13.6 Two-mode UI skeleton and tab separation
```

Scope:

- add two top-level tabs or mode panels;
- keep `Anonimiseren` as the main existing workflow;
- create a clearly labelled `Originele waarden terugzetten` area;
- keep current pasted-text reinsert available;
- do not add TXT/DOCX upload reinsert yet;
- do not add PDF;
- do not change export/download semantics.

Validation:

- add patch-level UI tests for mode labels;
- verify existing download markers remain;
- verify no AI/cloud text or imports were added;
- app verification required.

### Phase 2 — Move current anonymization workflow under `Anonimiseren`

This may be combined with Phase 1 if technically simple, but should be treated as a clear implementation concern.

Requirements:

- current upload/paste flow remains available;
- current review table remains source of truth;
- current scrubbed TXT/CSV/DOCX/PDF downloads remain unchanged;
- Scrub Key export remains available after review/export controls.

### Phase 3 — Move existing Scrub Key load + pasted-text reinsert under `Originele waarden terugzetten`

Requirements:

- Scrub Key import/reload appears in the reinsert mode;
- pasted-text reinsert appears in the reinsert mode;
- active Scrub Key state remains explicit;
- no silent overwrite of review rows;
- no automatic restoration after key loading;
- restored `.txt` download remains labelled as restored output.

### Phase 4 — Add TXT reinsert upload/download UI

Recommended after Phase 1-3 are app-verified.

Use WP10 helper:

```python
reinsert_txt_bytes(content, scrub_key, encoding="utf-8")
```

UI should add:

```text
Upload TXT met AI-output of scrubbed tekst
Download herstelde tekst (.txt)
```

This phase is lower risk than DOCX because no layout needs to be preserved.

### Phase 5 — Add DOCX reinsert upload/download UI using WP10 helper

Recommended after TXT upload UI is stable.

Use WP10 helper:

```python
reinsert_docx_bytes(content, scrub_key)
```

UI must show DOCX limitations clearly:

- only `word/document.xml` text nodes are processed;
- body paragraphs and tables are supported;
- split-run placeholders may not be restored;
- headers, footers, comments, tracked changes and metadata are not processed;
- output must be manually reviewed.

Download label:

```text
Download hersteld DOCX-document (.docx)
```

### Phase 6 — Research PDF text extraction only, no full PDF output

Recommended later only.

Scope:

- research only;
- no PDF output;
- no OCR;
- no cloud conversion;
- no promise of layout preservation.

---

## 7. Operational safety

### 7.1 Avoid parallel UI edits

Future UI implementation must not run in parallel with any other work that edits:

- `fix_streamlit_nested_expanders.py`;
- `presidio_streamlit.py`;
- review table flow;
- export/download flow;
- shared session state.

### 7.2 Test strategy

For the first UI implementation, add patch-level tests that check:

- `Anonimiseren` appears;
- `Originele waarden terugzetten` appears;
- pasted-text reinsert remains available;
- Scrub Key import/reload remains available;
- Scrub Key export remains available;
- existing scrubbed download labels remain;
- restored download labels remain separate;
- no PDF reinsert UI is added;
- no AI/cloud imports or wording are added;
- reinsertion still requires an explicit button action.

Suggested targeted validation after UI implementation:

```bash
PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert_ui_patch.py
PYTHONPATH=. pytest -q tests/test_scrub_key_import_ui_patch.py
PYTHONPATH=. pytest -q tests/test_scrub_key_ui_patch.py
```

If feasible:

```bash
PYTHONPATH=. pytest -q
```

### 7.3 App verification requirements

App verification is required for any future UI implementation because mode selection changes user navigation.

Verify at least:

- both modes are visible;
- anonymization still works;
- existing downloads still appear;
- Scrub Key export still works;
- Scrub Key import still works;
- pasted-text reinsert still works;
- no PDF reinsert UI appears;
- no AI/cloud processing is introduced.

### 7.4 Preserve export/download semantics

Existing scrubbed downloads must not change.

Restored downloads must be clearly separated and labelled:

```text
opgeschoond = safer/scrubbed output
hersteld = original values restored, sensitive again
```

### 7.5 No silent overwrite

The reinsert mode must not silently overwrite:

- review rows;
- scrubbed output;
- imported Scrub Key rows;
- existing export state.

Any restoration must require an explicit user action.

### 7.6 No key storage or real data

Do not add:

- server-side Scrub Key storage;
- durable key vault;
- secrets;
- tokens;
- real personal data;
- real legal case data.

Use synthetic test data only.

### 7.7 Metadata risks for DOCX

When DOCX reinsert UI is added, the UI must state that metadata hygiene is not yet solved.

Do not claim that restored DOCX is metadata-clean.

Document hygiene remains a later phase.

---

## 8. Required UI journeys

### Mode 1 — Anonimiseren

Ideal journey:

1. User chooses `Anonimiseren`.
2. User uploads or pastes source text/document.
3. App recognizes candidate sensitive values locally.
4. User reviews detected replacements in the replacement table.
5. User decides which rows are included.
6. User downloads currently supported scrubbed output:
   - TXT;
   - CSV where available;
   - DOCX where available;
   - PDF where available.
7. User optionally downloads Scrub Key JSON.
8. App warns:

```text
Een Scrub Key maakt deze tekst omkeerbaar. Dit is pseudonimisering, geen volledige anonimisering. Bewaar de sleutel lokaal en beveiligd.
```

9. User manually checks the output before sharing or using it in AI.

### Mode 2 — Originele waarden terugzetten

Ideal journey:

1. User chooses `Originele waarden terugzetten`.
2. User loads or pastes Scrub Key JSON.
3. App validates the key locally.
4. User chooses input type:
   - paste text;
   - upload TXT;
   - upload DOCX.
5. App shows applicable limitations:
   - text/TXT: plain-text behavior;
   - DOCX: foundation-level support and unsupported areas.
6. User explicitly clicks restore action.
7. App reinserts original values locally.
8. App shows audit summary:
   - mapping item count;
   - active item count;
   - excluded item count;
   - replacement count;
   - placeholders not found;
   - unknown placeholders;
   - duplicate placeholders;
   - validation issues;
   - local-only status;
   - no-AI status;
   - no-cloud status;
   - document limitations where applicable.
9. App warns restored output may contain sensitive/confidential data again.
10. User downloads restored TXT or DOCX.
11. User manually reviews restored output before sharing or filing.

---

## 9. Final recommendation answers

### 1. Should the app move to a two-mode interface?

Yes.

The modes should be:

```text
Anonimiseren
Originele waarden terugzetten
```

### 2. Should the first implementation be tabs or another structure?

Use Streamlit tabs or two clear mode panels first.

Do not start with a large landing-page or separate-page refactor.

### 3. Should pasted-text reinsert remain?

Yes.

It should remain the simplest reinsert path and fallback.

### 4. Should TXT upload reinsert be implemented before DOCX UI?

Yes.

TXT upload is simpler, validates the document-upload flow, and avoids DOCX layout risk.

### 5. Should DOCX upload reinsert be implemented in the same phase or later?

Later.

Add DOCX UI after the two-mode skeleton and TXT upload reinsert are stable and app-verified.

### 6. Should PDF reinsert remain excluded?

Yes.

PDF reinsert should remain excluded from implementation until a separate reliability review. PDF research may later investigate text extraction only.

### 7. What is the next implementation workpackage after this planning WP?

Recommended next implementation workpackage:

```text
WP12 — v13.6 Two-mode UI skeleton and tab separation
```

Recommended WP12 boundaries:

- UI skeleton/navigation only;
- use two tabs or clear mode panels;
- keep current anonymization workflow working;
- keep pasted-text reinsert available;
- no TXT upload reinsert yet;
- no DOCX upload reinsert yet;
- no PDF reinsert;
- no AI/cloud behavior;
- no export/download semantics change;
- add patch-level UI tests;
- require app verification.

---

## 10. Non-goals for the next implementation

Do not include in WP12:

- TXT upload reinsert UI;
- DOCX upload reinsert UI;
- PDF reinsert;
- OCR;
- AI calls;
- cloud processing;
- metadata cleaning;
- batch mode;
- durable Scrub Key vault;
- server-side Scrub Key storage;
- separate pages;
- full landing-card refactor;
- export/download semantics changes.

---

## 11. Done criteria for future WP12

WP12 should be done only when:

- `Anonimiseren` and `Originele waarden terugzetten` are clearly visible;
- existing anonymization flow still works;
- existing scrubbed downloads remain visible and unchanged;
- Scrub Key export remains visible and unchanged;
- Scrub Key import/reload remains visible;
- pasted-text reinsert remains visible and requires explicit action;
- restored text download remains clearly labelled as restored output;
- no TXT/DOCX upload reinsert UI is added yet;
- no PDF UI is added;
- no AI/cloud behavior is added;
- targeted UI patch tests pass;
- app verification is requested and completed.
