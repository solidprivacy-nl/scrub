# SolidPrivacy Scrub — Product & Development Roadmap

This document is the central reference for future Scrub development.

Use it together with `CHANGELOG.md`:

- `ROADMAP.md` explains the bigger picture: direction, priorities, phases and why we are doing the current work.
- `CHANGELOG.md` records what has actually changed, when, and in which version/fase.

The roadmap should be updated whenever the product strategy or development sequence changes meaningfully.

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

The key promise:

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

Therefore Scrub must optimize for:

1. local processing;
2. context preservation;
3. human review;
4. consistent placeholders;
5. auditability;
6. domain-specific recognition;
7. safe export;
8. eventually desktop/offline deployment.

---

## 3. Strategic lessons from external products

Two external products shaped this roadmap:

- anonym.plus;
- CamoText.

### 3.1 Lessons from anonym.plus

Important concepts to learn from:

- offline-first as a main trust message;
- desktop installer as real product form;
- clear processing pipeline;
- multiple anonymization operators;
- presets/profiles;
- entity recognition catalogue;
- batch processing;
- local encrypted vault/settings;
- transparent security limitations;
- documentation and demos as part of the product.

Relevant product lesson:

```text
Do not sell only detection. Sell a trustworthy local workflow.
```

### 3.2 Lessons from CamoText

CamoText sharpened the roadmap further because it is focused on AI-safe document preparation.

Important concepts to learn from:

- position the product as an AI-safety workflow;
- desktop-first / offline-first;
- human-in-the-loop review;
- anonymization key / mapping file;
- reinsert original terms into AI output;
- priorities / categories / exclusions;
- category-level review actions;
- redaction mode as a clear export mode;
- metadata-free clean output;
- batch mode for folders;
- CLI/headless mode later;
- observable local-security validation.

Most important roadmap addition from CamoText:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

---

## 4. What differentiates Scrub

Scrub should not try to win as a generic international PII anonymizer.

The strongest differentiator is:

```text
Dutch domain-specific confidential document scrubbing.
```

For the first product line, this means:

```text
Dutch legal documents
Dutch legal identifiers
Dutch case/document references
Dutch process roles
legal context preservation
AI-ready readable output
```

Examples of context that must remain readable:

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

The product should mask or replace the sensitive value, not the legal meaning of the sentence.

---

## 5. Current status

Current development status at the time of this roadmap update:

```text
v9      Dutch Legal UI Layer                         completed
v9.1    UI polish                                    completed
v10     Regression test foundation                   completed
v11.1   Legal reference hardening / audit layer      completed
v11.2   Dutch recognizer integration tests           completed
v12.1   Review status model                          completed
v12.2   Review focus filters                         completed
v12.3   Review table simplification                  implemented; pending final verification after bugfix
```

Important recent bugfix:

```text
v12.3 introduced table configuration using pandas DataFrame columns.
A pandas Index cannot be boolean-tested.
This was fixed by converting available_columns explicitly to list/set.
```

Immediate verification before further work:

1. GitHub Actions `Tests` must be green.
2. GitHub → Hugging Face sync must be green.
3. Hugging Face app must reload successfully.
4. The same legal test example must no longer show the pandas Index truth-value error.

---

## 6. Development governance

From v10 onward, recognizer work must follow this sequence:

1. Add or update synthetic regression cases.
2. Add or update tests.
3. Change recognizer/scanner logic.
4. Verify GitHub Actions tests are green.
5. Let GitHub sync to Hugging Face automatically.
6. Test the app in Hugging Face.
7. Update `CHANGELOG.md`.
8. If the strategic roadmap changes, update `ROADMAP.md`.

For UI/UX-only work:

1. Add pure helper modules where possible.
2. Add tests for helper logic.
3. Patch UI.
4. Verify GitHub Actions tests.
5. Verify Hugging Face app.
6. Update changelog.

---

## 7. Current development line — v12 Review UX

The current line of work is v12: make the review workflow safer and easier for legal users.

### v12.1 — Review status model

Status: completed.

Added statuses:

- Automatisch vervangen;
- Controle nodig;
- Handmatig toegevoegd;
- Onthouden vervanging.

Purpose:

```text
Help users understand what each row means before export.
```

### v12.2 — Review focus filters

Status: completed.

Added filters:

- Toon alles;
- Alleen controle nodig;
- Alleen juridische referenties;
- Alleen namen/adressen;
- Alleen lage zekerheid.

Important design rule:

```text
Filters are focus views only. The full replacement table remains the source of truth.
```

### v12.3 — Review table simplification

Status: implemented; pending final verification after bugfix.

Main table should focus on:

- Meenemen;
- Onthouden;
- Status;
- Gevonden tekst;
- Vervangen door;
- Type gegeven;
- Zekerheid.

Technical fields should move to:

```text
Technische details bij de vervangtabel
```

---

## 8. Next immediate phase — finish v12

### v12.4 — Review guidance text

Goal:

```text
Make the review workflow self-explanatory.
```

Planned scope:

- explain that only checked rows are included in export;
- explain that `Controle nodig` rows are not automatically safe;
- explain the focus filter is only a view, not the export scope;
- explain technical details are for audit/debugging;
- add clearer guidance around AI usage: scrub first, then use AI.

Non-goals:

- no recognizer changes;
- no export semantics change;
- no desktop/MSI work.

### v12.5 — Final review summary

Goal:

```text
Show a final export readiness summary before downloads.
```

Planned summary:

- automatically detected rows;
- rows needing review;
- manually added rows;
- remembered replacements;
- checked rows included in export;
- unchecked rows excluded from export;
- open candidate warning.

### v12.6 — Export sanity checks

Goal:

```text
Warn users before exporting if risk remains.
```

Planned checks:

- warning if `Controle nodig` rows remain unchecked;
- warning if candidate rows exist but are not included;
- warning if no replacements are selected;
- warning if export mode implies redaction vs pseudonymization risk;
- reminder that user review remains required.

---

## 9. Next strategic phase — v13 Scrub Key / Reinsert

This is the most important strategic addition after the v12 review flow.

Inspired by CamoText’s anonymization-key and reinsert workflow.

### v13.1 — Scrub Key JSON export

Goal:

```text
Create a local mapping file for replacements.
```

A Scrub Key should contain:

- original value;
- placeholder;
- entity type;
- user-facing type label;
- source;
- review status;
- include/exclude state;
- timestamp;
- optional project/dossier label.

### v13.2 — Scrub Key import/reload

Goal:

```text
Allow users to reuse a previously saved mapping.
```

Use cases:

- consistent names across multiple documents;
- same client/case over several files;
- continue work later;
- reinsert AI output.

### v13.3 — AI-output reinsert

Goal:

```text
Paste AI-generated output back into Scrub and locally restore original terms.
```

Workflow:

1. scrub original document;
2. send scrubbed text to AI;
3. paste AI output back into Scrub;
4. load Scrub Key;
5. reinsert original values locally.

### v13.4 — Pseudonymization warnings

Goal:

```text
Make it clear that reversible mapping is pseudonymization, not true anonymization.
```

Warnings should explain:

- if a Scrub Key exists, the text may be reversible;
- key security matters;
- do not share the key with external parties unless intended.

---

## 10. v14 — Manual output review / highlight workflow

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

---

## 11. v15 — Document hygiene and metadata-clean export

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
- produce new clean output file.

PDF priorities:

- remove metadata where possible;
- support text-based PDF;
- warn when scanned/OCR content is not processed;
- explicitly state limitations.

This phase is strategically important because legal documents often contain hidden metadata.

---

## 12. v16 — Desktop/local proof of concept

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

---

## 13. v17 — Legal profiles / vertical profiles

Original order had legal profiles before Scrub Key, but after CamoText review the order changed:

```text
First: finish review workflow and Scrub Key.
Then: expand domain profiles.
```

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

---

## 14. v18 — Batch / dossiermap

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

---

## 15. v19 — CLI / automation

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

This is useful for:

- power users;
- IT-managed workflows;
- batch processing;
- future integrations;
- AI-agent workflows.

---

## 16. v20 — Broader vertical markets

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

Architecture:

```text
Scrub Core
  + profile: Legal
  + profile: Zorg
  + profile: HR/Arbo
  + profile: Claims
  + profile: Gemeente
  + profile: Finance
  + profile: Research
```

Each profile should add:

- recognizers;
- examples;
- false-positive guards;
- UI copy;
- exports/audit labels;
- tests.

---

## 17. Product architecture target

Current prototype architecture:

```text
Hugging Face Space
Streamlit UI
Presidio/spaCy recognizers
Dutch legal recognizers
Candidate scanner
Review table
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

The intermediate architecture can remain Streamlit-based while we validate workflow and recognizers.

---

## 18. Security and trust principles

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

## 19. Current next action

Before new roadmap work starts:

1. Verify the latest v12.3 pandas Index bugfix.
2. Confirm GitHub Actions `Tests` are green.
3. Confirm GitHub → Hugging Face sync is green.
4. Reload the app.
5. Confirm the simplified table and technical details expander work.

Then continue with:

```text
v12.4 — Review guidance text
```

---

## 20. Maintenance rule for this roadmap

Update this file when:

- the development sequence changes;
- external product research changes priorities;
- a new major phase is introduced;
- a phase is completed and its status changes;
- we decide to target a new vertical market;
- desktop/MSI direction changes.

Do not use this file for every small code change. Use `CHANGELOG.md` for implementation history.
