# SolidPrivacy Scrub — Product & Development Roadmap

This document is the central roadmap for SolidPrivacy Scrub.

Use it together with:

- `WORKPACKAGES.md` for the active execution queue, dependencies and verification gates;
- `CHANGELOG.md` for the implementation history;
- `PROJECT_PROMPT.md` for worker rules and project governance.

Last roadmap status reconciliation: 2026-06-09 — WP17B.

---

## 1. Product vision

Scrub is evolving from a technical Presidio demo into a local-first professional document scrubber for confidential Dutch documents.

The primary starting market is:

```text
Scrub Legal
A local Dutch legal scrubber for process documents, case files and AI use.
```

The broader product direction is:

```text
A Dutch local-first privacy scrubber for professional confidential documents.
```

The long-term product should help professionals safely prepare documents for:

- AI use;
- external sharing;
- internal analysis;
- training examples;
- reporting;
- controlled publication.

The key promise remains:

```text
Sensitive information stays local.
The user remains in control.
The document stays readable.
```

---

## 2. Core product principle

The product is not just a generic anonymizer.

The real problem is:

```text
How can a professional safely use or share confidential documents without losing context, legal meaning or auditability?
```

Scrub must optimize for:

1. local processing;
2. context preservation;
3. human review;
4. consistent placeholders;
5. auditability;
6. domain-specific recognition;
7. safe export;
8. eventually desktop/offline deployment.

Legal context must be preserved. Scrub should replace sensitive values, not legal meaning.

Examples of legal context that must remain readable:

- slachtoffer;
- minderjarige;
- verzoeker;
- verweerder;
- eiser;
- gemachtigde;
- rechtbank;
- zaaknummer label;
- claim context;
- incident context.

---

## 3. Strategic workflow

The current product workflow direction is:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

This direction was strengthened by external product review of anonym.plus and CamoText.

Important retained lessons:

- do not sell only detection; sell a trustworthy local workflow;
- position Scrub as an AI-safety workflow for confidential documents;
- use human-in-the-loop review before export;
- support a reversible Scrub Key / mapping file for controlled pseudonymization;
- allow local reinsert into AI output;
- make pseudonymization risks explicit;
- keep the future desktop/offline path open.

---

## 4. Current implementation status

Current implementation status after WP17:

```text
v9       Dutch Legal UI Layer                                      completed
v9.1     UI polish                                                 completed
v10      Regression test foundation                                completed
v11.1    Legal reference hardening / audit layer                   completed
v11.2    Dutch recognizer integration tests                        completed
v12      Review UX line                                            completed
v13.1    Scrub Key JSON export                                     completed
v13.2    Scrub Key import/reload                                   completed
v13.3    Deterministic pasted-text reinsert                        completed/app-verified
v13.6    Two-mode UI: Anonimiseren / Originele waarden terugzetten completed/app-verified
v13.7    TXT reinsert upload/download UI                           completed/app-verified
v13.8    DOCX reinsert upload/download UI                          completed/app-verified
WP15     PDF text extraction reliability review                    completed review/specification only
WP16     Text-based PDF extraction helper spike                    completed after Actions/sync verification
WP16-FIX PDF helper test fix                                       completed after Actions/sync verification
WP16B    PDF helper verification closeout                          completed closeout-only
WP17     PDF text extraction reinsert UI planning                  completed planning/specification-only
WP17B    Roadmap current-status reconciliation after WP17           completed documentation-only
```

### 4.1 v12 Review UX line

The v12 line is no longer the active line. It delivered the safer review workflow foundation:

- review status model;
- review focus filters;
- simplified review table;
- review guidance text;
- final review summary;
- export sanity checks.

Export semantics were intentionally preserved: warnings and summaries advise the user but do not silently block or alter exports unless a later workpackage explicitly changes that policy.

### 4.2 v13 Scrub Key / Reinsert line

The v13 line delivered the core reversible pseudonymization workflow:

- Scrub Key JSON export;
- Scrub Key import/reload;
- deterministic local pasted-text reinsert;
- two-mode UI separation between `Anonimiseren` and `Originele waarden terugzetten`;
- TXT upload/download reinsert;
- DOCX upload/download reinsert;
- clear warnings that Scrub Key-based reinsert restores sensitive/confidential values;
- audit output for reinsert flows;
- local-only / no-AI / no-cloud positioning.

Current document-level reinsert support:

```text
Pasted text → restored text
TXT upload  → restored TXT
DOCX upload → restored DOCX, within documented helper limits
```

Known DOCX limitations remain:

- normal `word/document.xml` text and tables are supported;
- headers, footers, comments, tracked changes and metadata are not fully processed;
- placeholders split across Word runs may not be restored;
- no perfect formatting guarantee is made.

### 4.3 PDF review, helper and planning line

WP15 concluded:

- do not implement full PDF reinsert now;
- do not implement OCR now;
- restored PDF output remains out of scope;
- PDF-to-DOCX reconstruction remains out of scope;
- DOCX remains the preferred document-level reinsert path;
- a helper-only text-based PDF extraction route to restored TXT output may be evaluated.

WP16 implemented that helper-only spike:

```text
PDF bytes → local selectable-text extraction → existing Scrub Key reinsert → restored TXT/text output only
```

WP16 / WP16-FIX / WP16B status:

```text
Completed after Actions/sync verification; app verification not applicable because no UI behavior changed.
```

WP17 completed planning/specification-only. It specified that any future PDF UI must be limited to:

```text
PDF upload → local text extraction → restored TXT preview/download only
```

The PDF boundaries remain:

- no restored PDF output;
- no OCR;
- no PDF-to-DOCX reconstruction;
- no cloud PDF conversion;
- no AI-based extraction;
- no layout preservation promises;
- no batch PDF processing;
- no real-data PDF test cases;
- no automatic PDF rehydration.

---

## 5. Current next possible workpackage

The current next possible workpackage is:

```text
WP18 — PDF text extraction to restored TXT UI implementation
```

WP18 has **not** started.

WP18 must not start unless explicitly approved as a separate implementation workpackage.

If approved later, WP18 should remain limited to:

- `Originele waarden terugzetten` only;
- PDF upload;
- local text extraction via the WP16 helper;
- restored TXT preview;
- restored TXT download;
- audit report;
- strong warnings;
- no PDF output;
- no OCR;
- no AI/cloud behavior;
- no export/download semantic changes outside the approved PDF-to-TXT reinsert path.

---

## 6. PDF UI implementation boundaries for WP18

WP18, if explicitly approved, must preserve these boundaries:

- no restored PDF output;
- no OCR;
- no PDF-to-DOCX reconstruction;
- no cloud PDF conversion;
- no AI-based extraction;
- no layout preservation promises;
- no batch PDF processing;
- no real-data PDF test cases;
- no automatic PDF rehydration.

Required UX principles for a future PDF-to-TXT reinsert UI:

- explain that PDF extraction is not guaranteed complete;
- warn that formatting and layout are not preserved;
- warn that restored output contains sensitive/confidential values again;
- show local-only / no-AI / no-cloud;
- show unknown placeholders;
- show mapped placeholders not found;
- reject or clearly mark scanned/image-only PDFs as unsupported;
- do not imply that restored TXT equals a legally complete reconstruction of the PDF.

---

## 7. Upcoming strategic product phases

### v14 — Manual output review / highlight workflow

Goal:

```text
Allow users to manually mark text from the output/review area and replace it everywhere.
```

Planned scope:

- search in scrubbed output;
- manually add selected text to replacement table;
- choose replacement type;
- replace selected text everywhere;
- add manual replacement to Scrub Key.

Why this matters:

```text
Legal users often see missing sensitive terms while reading, not while editing a table.
```

### v15 — Document hygiene and metadata-clean export

Goal:

```text
Produce clean outputs that do not leak metadata or hidden document content.
```

DOCX priorities:

- remove document metadata;
- remove author information where possible;
- handle comments;
- handle tracked changes policy;
- include headers/footers in scrubbing;
- preserve basic layout where feasible;
- produce a clean output file.

PDF policy after WP15/WP16/WP17:

- text-based PDF extraction may be used only for restored TXT output unless a later approved workpackage changes that;
- scanned/OCR content remains unsupported;
- full PDF reinsert remains out of scope;
- restored PDF output remains out of scope;
- limitations must be explicit.

This phase is strategically important because legal documents often contain hidden metadata.

### v16 — Desktop/local proof of concept

Goal:

```text
Prove that Scrub can run locally outside Hugging Face.
```

Preferred direction:

- Python backend remains local;
- frontend can be Streamlit initially, then desktop wrapper;
- portable Windows build first;
- MSI later;
- no internet required for core processing.

Possible technical paths:

- Streamlit local launcher;
- Tauri + local Python service;
- Electron + local Python service;
- PyInstaller/Nuitka for local packaging experiments.

Success criteria:

- app starts locally;
- sample document can be scrubbed offline;
- no cloud calls required;
- Hugging Face no longer needed for real-world use.

### v17 — Legal profiles / vertical profiles

Planned Legal profiles:

- algemeen juridisch;
- familierecht;
- strafrecht;
- arbeidsrecht;
- bestuursrecht;
- vreemdelingenrecht;
- letselschade / verzekering;
- huurrecht / vastgoed;
- medisch-juridisch.

Each profile should have:

- own example texts;
- own recognizer emphasis;
- own false-positive guards;
- own review guidance;
- own regression tests.

### v18 — Batch / dossiermap

Goal:

```text
Process multiple documents or full case folders.
```

Planned scope:

- input folder;
- output folder;
- preserve folder structure;
- scrub keys per file or per dossier;
- summary report;
- ZIP export;
- later parallel processing.

Batch should not come before single-document flow is reliable.

### v19 — CLI / automation

Goal:

```text
Support headless and enterprise workflows.
```

Possible commands:

```text
scrublegal --input dossier.docx --output dossier_scrubbed.docx --profile arbeidsrecht
scrublegal --input-dir zaakmap --output-dir zaakmap_ai --key-dir keys
scrublegal --reinsert ai_output.docx --key zaak_key.json
```

### v20 — Broader vertical markets

Scrub Core should remain one engine, with vertical profiles on top.

Potential future verticals:

1. Scrub Legal;
2. Scrub Zorg;
3. Scrub HR / Arbo;
4. Scrub Claims / Verzekering;
5. Scrub Gemeente / Sociaal Domein;
6. Scrub Finance / Accountancy;
7. Scrub Research.

Do not build separate apps too early.

---

## 8. Product architecture target

Current prototype architecture:

```text
Hugging Face Space
Streamlit UI
Presidio/spaCy recognizers
Dutch legal recognizers
Candidate scanner
Review table
Scrub Key import/export
Pasted/TXT/DOCX reinsert
PDF text extraction helper
PDF text reinsert UI plan
Exports
GitHub Actions tests
GitHub → Hugging Face sync
```

Target architecture:

```text
Local desktop app
Local recognition engine
Local review workflow
Local Scrub Key vault/files
Local exports
Optional CLI
No required cloud processing
```

The intermediate architecture can remain Streamlit-based while we validate workflow, recognizers, document support and user experience.

---

## 9. Security and trust principles

For the final product:

- no document upload to third-party cloud;
- no model training on user documents;
- no telemetry containing document content;
- clear warning when using cloud AI outside Scrub;
- local-only processing as default;
- metadata-aware exports;
- audit report;
- clear distinction between anonymization, pseudonymization and redaction.

Future security validation should include:

- offline mode demonstration;
- network traffic check;
- clear file storage locations;
- local key storage explanation;
- user-controlled deletion.

---

## 10. Development governance

For recognizer work:

1. Add or update synthetic regression cases.
2. Add or update tests.
3. Change recognizer/scanner logic.
4. Verify GitHub Actions tests are green.
5. Let GitHub sync to Hugging Face automatically.
6. Test the app in Hugging Face when UI behavior changed.
7. Update `CHANGELOG.md`.
8. Update `WORKPACKAGES.md` when status or next steps change.
9. Update `ROADMAP.md` only when strategy, phase status or sequence changes.

For UI implementation work:

1. Prefer helper modules and tests before UI changes.
2. Keep UI workpackages small and sequential.
3. Do not silently change export/download semantics.
4. Ask for app verification whenever UI behavior changes.
5. Preserve local-only, no-AI and no-cloud boundaries unless explicitly approved otherwise.
