# AI-output / document reinsert workflow review

Status: completed recommendation.  
Workpackage: WP9 — AI-output / document reinsert workflow UX and architecture review.  
Repository: `solidprivacy-nl/scrub`.  
Date: 2026-06-08.

This review decides what Scrub should do next for AI-output and document-level reinsert before implementation starts.

No code, UI, export behavior, Scrub Key behavior, AI calls or cloud processing are changed by this document.

---

## 1. Decision summary

Pasted-text reinsert is useful and should remain available, but it is not sufficient as the final legal-document workflow.

Recommended direction:

```text
Use a two-mode interface:

1. Anonimiseren
2. Originele waarden terugzetten

Keep pasted-text reinsert as the simplest path.
Add document-level reinsert in controlled phases.
Prioritize TXT and DOCX before PDF.
Do not implement full PDF reinsert yet.
Do not add AI calls.
Do not add cloud processing.
```

The next implementation should not be a broad UI refactor or full document rehydration. It should be helper-first and test-first.

Recommended next implementation workpackage:

```text
WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests
```

Goal of WP10:

```text
Prepare document-level reinsert without changing UI yet:
- add pure TXT reinsert input/output helper behavior;
- add a pure DOCX placeholder replacement helper design/implementation if feasible;
- add synthetic tests;
- keep PDF out of scope;
- keep AI/cloud out of scope;
- keep export semantics unchanged.
```

---

## 2. Current baseline

The implemented v13.3 reinsert flow is:

```text
User pastes text into the reinsert area.
User loads or provides a Scrub Key.
Scrub restores mapped placeholders locally.
User can download restored text as TXT.
```

This is a safe baseline because it is deterministic, local and simple. It also avoids prematurely claiming that Scrub can reliably rehydrate every Word or PDF document.

However, the current baseline is only a text-level workflow. It does not yet match the natural workflow of a legal professional who receives or produces AI output as DOCX or PDF.

---

## 3. The first three obvious ideas challenged

### Idea 1 — Keep only pasted-text reinsert

Question:

```text
Is copying AI-output text from a PDF/DOCX and pasting it into Scrub good enough?
```

Decision:

```text
Limit this idea. Keep pasted-text reinsert, but do not treat it as the final product workflow.
```

Critique:

- Usability burden: legal users should not have to manually copy text from a generated document, paste it into Scrub, then manually reconstruct the output.
- Loss of formatting: copy/paste loses headings, tables, numbering, footnotes, page structure and sometimes line breaks.
- Legal-document workflow friction: lawyers and legal support staff often work in Word/PDF outputs, not plain text boxes.
- Risk of incomplete copying: a user may accidentally omit a header, footer, table cell, footnote, exhibit label or final paragraph.
- Poor fit for DOCX/PDF outputs: if the AI result is returned as a Word document or PDF, a plain text reinsert result creates extra manual work and extra error risk.

Why it still matters:

Pasted text is still the safest fallback and should remain available. It is useful for quick AI chat output, email snippets, short summaries and debugging. It should be positioned as the simple path, not the only path.

---

### Idea 2 — Add direct PDF/DOCX reinsert immediately

Question:

```text
Should Scrub immediately support upload of any AI-output PDF or Word document and return a de-anonymized document?
```

Decision:

```text
Reject as an immediate broad implementation. Split DOCX and PDF, and start with DOCX helper work only after TXT helper behavior is stable.
```

Critique:

- DOCX is feasible, but needs careful placeholder replacement across paragraphs, runs, tables, headers and footers.
- Word placeholders may be split across runs. A naïve string replacement can miss placeholders or damage formatting.
- PDF is harder than DOCX because it may require text extraction, layout reconstruction, font handling, coordinates or OCR.
- Scanned PDFs are high-risk because text may not exist as selectable text. OCR would add accuracy, privacy and dependency questions.
- Preserving formatting and metadata hygiene is non-trivial.
- Scrub must not silently claim reliable document restoration if only text extraction/replacement is actually supported.

Recommended interpretation:

Document-level reinsert should be built, but not as one big feature. DOCX should be handled before PDF. PDF should first be investigated as text extraction only, with explicit limitation warnings.

---

### Idea 3 — Add one combined screen for everything

Question:

```text
Should anonymize and de-anonymize live in the same long workflow?
```

Decision:

```text
Reject as the main UX direction. Use explicit modes instead.
```

Critique:

- Cognitive overload: the existing workflow already includes upload, recognition, review, Scrub Key export/import, reinsert and downloads.
- Users may confuse scrub/anonymize with reinsert/de-anonymize.
- The reversible Scrub Key flow has different risks from anonymization. It can restore sensitive values and therefore needs its own mental model.
- Privacy state must be explicit: `opgeschoond`, `omkeerbaar met sleutel`, and `hersteld met originele waarden` are different states.
- A single-scroll Streamlit flow makes it too easy to miss where the user is in the privacy lifecycle.

Recommended interpretation:

The UI should start with a mode choice. The current single-scroll flow can continue temporarily while helpers mature, but the product direction should be two visible modes.

---

## 4. Model architecture perspective

### 4.1 Scrub Key as reversible mapping layer

The Scrub Key is the reversible mapping layer between original values and placeholders.

Conceptually:

```text
original sensitive value <-> placeholder
```

The Scrub Key must remain a separate security object from the scrubbed document. The scrubbed document may be safe enough for AI or external processing after review. The Scrub Key can restore sensitive values and must stay local and protected.

This means Scrub Key support is pseudonymization, not full anonymization.

### 4.2 Text-level reinsert versus document-level reinsert

Text-level reinsert is the simplest architecture:

```text
text + Scrub Key -> restored text + audit summary
```

It is already implemented and should remain the core deterministic operation.

Document-level reinsert should wrap the same core operation rather than create a second replacement engine.

Preferred architecture:

```text
TXT/DOCX/PDF intake
-> extract replaceable text units
-> call deterministic placeholder replacement logic
-> rebuild output where safe
-> return restored output + audit summary
```

The pure text replacement logic should remain authoritative.

### 4.3 DOCX placeholder replacement helper as likely next pure helper

DOCX is the most realistic next document format because Word documents are common in legal drafting and review.

The next DOCX helper should be pure and testable. It should not start in Streamlit UI.

The helper should consider:

- paragraphs;
- tables;
- headers and footers where feasible;
- run-splitting risk;
- preservation of basic formatting;
- output as a new restored DOCX file, not overwrite input;
- audit summary: replaced placeholders, unknown placeholders, missing placeholders, unsupported areas.

A first DOCX helper may explicitly limit scope if needed. It is better to support a smaller reliable DOCX subset than claim full document fidelity.

### 4.4 PDF reinsert as later/high-risk

PDF should not be implemented as full document reinsert yet.

Recommended PDF path:

1. Investigate text-based PDF extraction only.
2. Report whether placeholders are found.
3. Provide restored plain text if reliable enough.
4. Do not reconstruct a restored PDF until a reliability review proves that layout, metadata and scanning limitations are acceptable.

Scanned PDFs and OCR should remain out of scope until explicitly approved.

### 4.5 Separate anonymization and reinsert pipelines

Scrub should maintain two separate pipelines:

```text
Pipeline 1 — Anonymization
Input document/text -> recognition -> review -> scrubbed output -> Scrub Key -> export

Pipeline 2 — Reinsert
AI output / scrubbed output + Scrub Key -> restored output -> audit -> export
```

The pipelines can share the Scrub Key model and deterministic replacement helper, but they should not share UI state in a way that silently mutates review rows or export behavior.

### 4.6 No AI calls inside Scrub

Reinsert must not call AI.

Scrub’s role is:

```text
prepare safe text/documents for AI
restore original values locally after AI use
```

The AI step is external to Scrub. Scrub should never need the user’s AI provider credentials for this workflow.

### 4.7 Local-only processing

All reinsert processing should remain local-first. No Scrub Key, original values or restored output should be sent to cloud services by Scrub.

The Hugging Face demo may still run as a hosted prototype, but the product architecture must be compatible with the long-term desktop/offline direction.

---

## 5. Strategic perspective

### 5.1 Product promise

Scrub’s product promise is:

```text
Sensitive information stays local.
The user remains in control.
The document stays readable.
```

Document-level reinsert supports the third part of that promise. A restored plain text box is not enough when the professional deliverable is a formatted legal document.

### 5.2 Legal-professional workflow

A realistic legal workflow is:

1. A user uploads or pastes a source document.
2. Scrub anonymizes/pseudonymizes the document.
3. The user reviews replacements.
4. The user exports scrubbed content and a Scrub Key.
5. The user uses scrubbed content in an AI tool or external process.
6. The user receives AI output, often as text, DOCX or PDF.
7. The user returns to Scrub to restore original values locally.
8. The user reviews the restored output before sharing or filing.

This makes reinsert a separate product capability, not just a small extra textbox.

### 5.3 Positioning: Anonimiseren, Terugzetten, Controle/Audit

The product should eventually present three clear concepts:

```text
Anonimiseren
Originele waarden terugzetten
Controle / Audit
```

For the next UI direction, the first two should be primary modes:

```text
1. Anonimiseren
2. Originele waarden terugzetten
```

`Controle / Audit` can be a supporting layer inside both modes at first. It does not need to be a separate top-level mode yet.

### 5.4 When document-level reinsert becomes strategically important

Document-level reinsert becomes strategically important when Scrub is used for real legal AI workflows. Professionals will expect to upload an AI-output file and receive a restored file, not manually copy/paste text and rebuild formatting.

However, trust is more important than breadth. A reliable DOCX-first workflow is strategically better than a broad but unreliable DOCX/PDF promise.

---

## 6. Tactical perspective — phased implementation sequence

Recommended sequence:

### Phase A — Keep current text-paste reinsert, improve guidance

Status:

```text
Keep as current baseline.
```

Purpose:

- Keep simple pasted-text reinsert available.
- Clarify that this is best for plain text / AI chat output.
- Explain that restored text may again contain confidential information.

Implementation risk:

- Low.

### Phase B — Add TXT upload/download reinsert

Status:

```text
Recommended next small implementation layer.
```

Purpose:

- Let users upload a `.txt` AI-output file plus a Scrub Key.
- Use the same deterministic reinsert helper.
- Return restored text as `.txt`.

Why before DOCX:

- Very testable.
- No layout complexity.
- Validates document-upload flow without changing reinsert semantics.

### Phase C — Add DOCX reinsert helper, pure helper + tests

Status:

```text
Recommended after TXT helper/path is stable.
```

Purpose:

- Build a helper that opens DOCX, replaces placeholders, and writes a new restored DOCX.
- Keep it outside Streamlit at first.
- Use synthetic DOCX fixtures only.

Required guardrails:

- Do not overwrite uploaded files.
- Report unsupported document parts.
- Preserve basic formatting where feasible.
- Test paragraphs, runs, tables and simple headers/footers if feasible.
- Document limitations clearly.

### Phase D — Add DOCX reinsert UI

Status:

```text
Only after Phase C tests are stable.
```

Purpose:

- Add `.docx` upload in `Originele waarden terugzetten` mode.
- Return restored `.docx` and audit summary.
- Ask for app verification because UI/download behavior changes.

### Phase E — Investigate PDF text extraction only

Status:

```text
Research/contract phase only.
```

Purpose:

- Determine whether text-based PDFs with placeholders can be extracted reliably.
- Report scanned/image-only PDFs as unsupported.
- Avoid OCR initially.

### Phase F — Consider PDF output only after reliability review

Status:

```text
Do not build yet.
```

Purpose:

- Only consider restored PDF output if layout, metadata, text extraction and limitation messaging are reliable enough.

---

## 7. Operational perspective

### 7.1 Testability

All document-level reinsert behavior should start with pure helpers and synthetic tests.

Recommended tests:

- TXT input with placeholders;
- TXT input with unknown placeholders;
- TXT input with missing key placeholders;
- DOCX paragraph replacement;
- DOCX table replacement;
- DOCX split-run placeholder behavior;
- DOCX no-placeholder behavior;
- invalid Scrub Key behavior;
- duplicate placeholder behavior;
- no AI/cloud markers remain true/false as expected.

### 7.2 Helper-first implementation

Do not start by editing the Streamlit UI.

Recommended order:

```text
pure helper -> tests -> specification update -> UI wiring -> app verification
```

This avoids fragile parallel edits to `fix_streamlit_nested_expanders.py`.

### 7.3 Synthetic data only

Use only synthetic Dutch legal placeholders and values. Do not commit real client names, real case data, real BSNs, real addresses or real Scrub Keys.

### 7.4 Metadata risks

Document-level reinsert can reintroduce sensitive values and can also carry document metadata.

DOCX/PDF output should eventually align with document hygiene work:

- remove or warn about metadata;
- avoid hidden content leakage;
- avoid tracked changes surprises;
- avoid comments containing sensitive values.

This review does not implement metadata cleaning. It flags the risk so future document-level work does not silently expand the product promise.

### 7.5 Export/download semantics

Existing scrubbed TXT, CSV, DOCX and PDF downloads must not change.

Reinsert downloads should be separate from anonymized/scrubbed downloads and clearly labelled as restored output.

Suggested naming distinction:

```text
Download opgeschoonde tekst/document
Download herstelde tekst/document
```

### 7.6 App verification requirements

No app verification is required for this WP9 review because no UI behavior changed.

Future UI work must request app verification when:

- mode choice is added;
- TXT upload is added;
- DOCX restored download is added;
- any export/download UI is changed.

### 7.7 Avoiding parallel edits

Future UI work should not run in parallel with other work that edits:

- `fix_streamlit_nested_expanders.py`;
- `presidio_streamlit.py`;
- review table flow;
- export/download flow;
- shared session state.

### 7.8 No cloud processing

Document reinsert must not introduce cloud processing. OCR, external converters or AI-based document reconstruction must not be added without explicit approval.

### 7.9 Audit summary requirements

Every reinsert result should include an audit summary:

- file type;
- mapping item count;
- active mapping count;
- replacement count;
- unknown placeholders;
- missing placeholders;
- duplicate placeholders;
- validation issues;
- local-only status;
- AI processing status;
- cloud processing status;
- unsupported document areas if applicable.

---

## 8. Visual / UX perspective

### 8.1 Interface options compared

#### Option A — Tabs

Pros:

- Simple in Streamlit.
- Clear separation between `Anonimiseren` and `Originele waarden terugzetten`.
- Lower implementation complexity than separate pages.

Cons:

- Tabs can still share too much session state if not carefully handled.
- Users may not notice mode-level warnings if tabs are visually too light.

Assessment:

```text
Good near-term direction.
```

#### Option B — Landing page with two large choices

Pros:

- Best mental model.
- Strong privacy-state separation.
- Works well for future desktop product.
- Reduces confusion between scrubbing and restoring.

Cons:

- Larger UI change.
- Needs careful implementation in current patch-based Streamlit setup.

Assessment:

```text
Best target direction, but implement carefully after helper foundation.
```

#### Option C — Accordion/stepper

Pros:

- Fits current single-page Streamlit style.
- Can show workflow sequence.

Cons:

- Still risks becoming one long mixed workflow.
- Reinsert may feel like a sub-step of anonymization rather than a separate capability.

Assessment:

```text
Acceptable temporary bridge, not the ideal long-term structure.
```

#### Option D — Separate pages

Pros:

- Strong separation.
- Good for mature product.

Cons:

- More refactor work.
- Risky while UI is still patch-based.

Assessment:

```text
Good later, not the next small step.
```

#### Option E — Current single-scroll Streamlit flow

Pros:

- Already implemented.
- Lowest short-term risk.

Cons:

- Poor scalability.
- Hard to explain privacy state.
- Reinsert is buried after export/Scrub Key controls.
- Does not clearly answer: am I anonymizing or restoring?

Assessment:

```text
Keep temporarily, but do not continue expanding it indefinitely.
```

### 8.2 Recommended visual direction

Yes, the UI should start with a mode choice.

Recommended target:

```text
Welkom bij Scrub

Wat wilt u doen?

[Anonimiseren]
Maak tekst of documenten veilig voor AI of delen.

[Originele waarden terugzetten]
Gebruik een Scrub Key om placeholders lokaal terug te zetten in AI-output of scrubbed output.
```

Near-term Streamlit implementation can be tabs:

```text
Tab 1: Anonimiseren
Tab 2: Originele waarden terugzetten
```

Longer-term product implementation can become a landing page or separate pages.

### 8.3 Ideal user journey — Anonimiseren

1. User chooses `Anonimiseren`.
2. User uploads DOCX/PDF/TXT or pastes text.
3. Scrub detects sensitive values locally.
4. User reviews replacements.
5. User downloads scrubbed output.
6. User downloads Scrub Key if reversible workflow is needed.
7. UI warns that the Scrub Key must remain protected.

### 8.4 Ideal user journey — Originele waarden terugzetten

1. User chooses `Originele waarden terugzetten`.
2. User uploads or pastes a Scrub Key.
3. User provides AI-output or scrubbed output:
   - paste text now;
   - TXT upload next;
   - DOCX upload later;
   - PDF later only if supported.
4. Scrub validates the key and detects placeholders.
5. User clicks an explicit restore action.
6. Scrub restores original values locally.
7. UI shows restored output and audit summary.
8. User downloads restored output.
9. UI warns that restored output may again contain confidential information.

---

## 9. Required recommendation answers

### 1. Is pasted-text reinsert enough for now?

Yes, it is enough as the current safe baseline and fallback.

No, it is not enough as the final legal-document workflow.

### 2. Should document upload reinsert be supported?

Yes, but phased and helper-first.

Start with TXT, then DOCX, then only investigate PDF.

### 3. Should DOCX be prioritized before PDF?

Yes.

DOCX is closer to normal legal drafting workflows and is more feasible to handle with controlled helper logic. PDF should remain later and high-risk.

### 4. Should anonymization and de-anonymization be separated visually?

Yes.

The UI should move toward a two-mode structure:

```text
1. Anonimiseren
2. Originele waarden terugzetten
```

### 5. What should be the next implementation workpackage?

```text
WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests
```

Recommended scope:

- no UI first;
- add pure TXT document-level reinsert helper behavior;
- add or design DOCX placeholder replacement helper;
- add synthetic regression tests;
- keep PDF out of scope;
- keep AI/cloud out of scope;
- do not change existing export/download behavior.

### 6. What should explicitly not be built yet?

Do not build yet:

- full PDF reinsert;
- OCR for scanned PDFs;
- AI-based document reconstruction;
- cloud conversion;
- automatic AI calls;
- server-side Scrub Key storage;
- automatic document rehydration without explicit user action;
- a broad UI refactor in parallel with other UI work;
- metadata-clean document promises until document hygiene work is explicitly scoped;
- changes to existing scrubbed export/download semantics.

---

## 10. Final recommendation

Scrub should keep pasted-text reinsert, but treat it as the simple/manual path.

The product should move toward a two-mode UX:

```text
Anonimiseren
Originele waarden terugzetten
```

Document-level reinsert should be supported, because legal professionals work with documents, not only copied text. But the implementation should be cautious:

```text
TXT first.
DOCX second.
PDF later only after reliability review.
```

The next workpackage should build the helper/test foundation, not immediately change the UI.

This keeps the product aligned with the core promise:

```text
local-first
user control
readable documents
safe auditability
```
