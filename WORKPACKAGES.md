# SolidPrivacy Scrub — Workpackages

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Repository: `solidprivacy-nl/scrub`.

Also read when relevant:

- `AGENTS.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `STATUS_MONITORING_RUNBOOK.md`
- `RELEASE_NOTES.md`

## Current status

WP0 through WP13B are complete.

Recent completed line:

```text
WP14 / WP14B / WP14C — v13.8 DOCX reinsert upload/download UI: completed and app-verified.
WP15 — PDF text extraction reliability review only: completed review/specification-only.
WP16 — Text-based PDF extraction helper spike: completed after Actions/sync verification.
WP16-FIX — PDF helper test fix: completed after Actions/sync verification.
WP16B — PDF helper verification closeout: completed closeout-only.
WP17 — PDF text extraction reinsert UI planning: completed planning/specification-only.
WP17B — Roadmap current-status reconciliation after WP17: completed documentation-only.
WP18 — PDF text extraction to restored TXT UI implementation: completed and app-verified after Actions/sync verification.
WP18R — Risk-driven roadmap and operating model reset: completed documentation/governance-only.
WP18-FIX — Fix failing PDF text to TXT UI tests: completed after Actions/sync verification; WP18 app verification completed.
WP18B — PDF text to restored TXT UI app verification closeout: completed closeout-only.
WP18C — Add Codex worker governance instructions: completed documentation/governance-only.
WP19 — Recall benchmark specification: completed specification-only.
WP25 — Scrub Key threat model: completed security/specification-only.
WP30 — Placeholder robustness review: completed architecture/specification-only.
WP35 — DOCX hidden content risk review: completed document-hygiene/specification-only.
```

## Closed UI line: WP18 PDF text to restored TXT

### WP18 — PDF text extraction to restored TXT UI implementation

Status: completed and app-verified after Actions/sync verification.

Implemented workflow:

```text
Originele waarden terugzetten
→ PDF upload
→ local selectable-text extraction via WP16 helper
→ deterministic Scrub Key reinsert
→ restored TXT preview
→ restored TXT download
→ audit report
```

Preserved boundaries:

- no OCR;
- no restored PDF output;
- no PDF-to-DOCX reconstruction;
- no AI/cloud extraction;
- no layout reconstruction;
- no batch PDF processing;
- no real-data tests;
- no automatic PDF rehydration;
- no changes to existing pasted-text/TXT/DOCX reinsert semantics;
- no changes to existing anonymization/export semantics.

### WP18-FIX — Fix failing PDF text to TXT UI tests

Status: completed after Actions/sync verification; WP18 app verification completed.

Fix summary:

- Updated `tests/test_pdf_text_reinsert_ui_patch.py` only.
- Corrected a brittle test expectation around the triple-quoted `else:` insertion marker.
- No UI code, Dockerfile behavior, helper code, dependencies or feature behavior were changed.

Verification note:

- Connector status lookup for the WP18-FIX commit returned no statuses and no workflow runs.
- WP18B was approved by the coordinator/user as closeout-only after external verification.
- This closeout records coordinator/user evidence that Actions/sync and app verification gates are satisfied.

### WP18B — PDF text to restored TXT UI app verification closeout

Status: completed closeout-only.

Closeout evidence recorded:

- GitHub Actions: green based on coordinator/user closeout approval.
- Hugging Face sync: green based on coordinator/user closeout approval.
- App verification: confirmed by coordinator/user closeout approval.

App verification scope covered:

- `Originele waarden terugzetten` shows the new PDF-to-TXT section;
- `Anonimiseren` does not show the PDF reinsert section;
- a valid Scrub Key can be loaded;
- a text-based PDF with placeholders can be uploaded;
- PDF text can be restored locally to TXT;
- restored TXT preview appears;
- restored TXT download appears;
- audit report appears;
- UI clearly says no OCR, no AI, no cloud and no PDF output;
- scanned/image-only PDFs are rejected or clearly marked unsupported;
- existing pasted-text, TXT and DOCX reinsert still work;
- existing anonymization/export behavior is unchanged.

Files changed in WP18B:

```text
WORKPACKAGES.md
CHANGELOG.md
RELEASE_NOTES.md
handover/workpackages/20260609_1315_pdf_text_to_txt_ui_app_closeout.md
```

No code, tests, dependencies or UI files were changed.

## Governance setup: WP18C Codex worker governance

### WP18C — Add Codex worker governance instructions

Status: completed documentation/governance-only.

Purpose:

- Add repository-level Codex/agent worker instructions.
- Make handover-by-file the default workflow for parallel Codex workers.
- Avoid full handover copy-paste into the coordinator chat when the handover is committed to GitHub.

Files added:

```text
AGENTS.md
handover/workpackages/20260609_1330_codex_worker_governance.md
```

Files changed:

```text
WORKPACKAGES.md
CHANGELOG.md
```

No code, tests, UI, dependencies, runtime behavior or product behavior were changed.

Codex worker rule:

```text
Workers must write full handovers to handover/workpackages/.
Coordinator chat only needs handover path, commit/PR, status and short summary unless commit failed or GitHub access is unavailable.
```

## Phase 1: Trust & recall foundation

### WP19 — Recall benchmark specification

Status: completed specification-only.

Purpose:

- Define a benchmark for measuring recall/precision on messy synthetic Dutch legal and care texts.
- Define entity classes, scoring rules, minimum metrics and reporting format.
- Make false negatives / missed sensitive data measurable before benchmark implementation.

Files added:

```text
RECALL_BENCHMARK_SPEC.md
handover/workpackages/20260609_2200_recall_benchmark_spec.md
```

Files changed:

```text
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
```

Main specification decisions:

- Benchmark classes include `PERSON`, `ADDRESS`, `EMAIL`, `PHONE`, `BSN`, `IBAN`, `DATE`, `NL_POSTCODE`, `CASE_NUMBER`, `DOSSIER_NUMBER`, `CLIENT_NUMBER`, `CLAIM_NUMBER`, `INCIDENT_NUMBER`, `ECLI`, `ORGANIZATION`, `MEDICAL_OR_CARE_REFERENCE` and `ROLE_OR_CONTEXT_TERM_TO_PRESERVE`.
- Gold labels should use zero-based character offsets against synthetic plain text.
- Recall and precision should be reported overall, per domain and per entity class.
- Context terms such as `slachtoffer`, `minderjarige`, `verzoeker`, `verweerder`, `eiser`, `rechtbank`, `arts`, `cliënt` and `zorgmedewerker` should normally remain readable unless identifying context makes them sensitive.
- CI should start report-only, then move toward malformed-label failures, regression gates and later per-entity thresholds.

Intentionally not changed:

- No recognizer logic changed.
- No benchmark runner implemented.
- No tests added or changed.
- No UI changed.
- No dependencies changed.
- No real data added.
- No export or reinsert behavior changed.

Next recommended step:

- WP20 — Synthetic messy Dutch legal/zorg benchmark corpus.

## Phase 2: Scrub Key security and lifecycle

### WP25 — Scrub Key threat model

Status: completed security/specification-only.

Purpose:

- Treat Scrub Key as sensitive re-identification data.
- Define leakage, accidental sharing, lifecycle, expiry/delete and encryption risks.
- Make clear that Scrub Key-based output is pseudonymized, not fully anonymized, as long as the key exists.

Files added:

```text
SCRUB_KEY_THREAT_MODEL.md
handover/workpackages/20260609_2258_scrub_key_threat_model.md
```

Files changed:

```text
RISK_REGISTER.md
DECISION_LOG.md
WORKPACKAGES.md
CHANGELOG.md
```

Main security findings:

- The Scrub Key contains original confidential values and placeholder mappings, so it can re-identify scrubbed content.
- Accidental sharing, download-folder retention, e-mail/AI uploads, shared computers, unmanaged local storage and long retention are critical risks.
- Loss of the key prevents deterministic reinsert; tampering or malformed keys can cause incorrect or unsafe reinsert.
- Encryption, lifecycle, expiry/delete and tamper protection require a separate approved specification before implementation.

Intentionally not changed:

- No helper logic changed.
- No Scrub Key JSON schema migration.
- No import/export behavior changed.
- No reinsert behavior changed.
- No UI changed.
- No encryption implemented.
- No dependencies changed.
- No tests added or changed.
- No secrets or real data stored.

Next recommended step:

- WP26 — Scrub Key encryption/lifecycle specification.

## Phase 3: Placeholder robustness for AI roundtrip

### WP30 — Placeholder robustness review

Status: completed architecture/specification-only.

Purpose:

- Review how placeholders survive AI rewriting, translation, summarization and formatting changes.
- Document current placeholder format and deterministic reinsert assumptions.
- Identify corruption risks and candidate future validation directions before any implementation.

Files added:

```text
PLACEHOLDER_ROBUSTNESS_REVIEW.md
handover/workpackages/20260609_2310_placeholder_robustness_review.md
```

Files changed:

```text
RISK_REGISTER.md
DECISION_LOG.md
WORKPACKAGES.md
CHANGELOG.md
```

Main architecture findings:

- Current placeholders such as `[PERSOON_1]`, `[ZAAKNUMMER_1]` and `[ADRES_1]` are readable and deterministic, but fragile under AI translation, summarization, punctuation changes, markdown/HTML formatting and document conversion.
- Current reinsert depends on exact placeholder strings from the Scrub Key mapping.
- Existing audit reporting for unknown, duplicate and not-found placeholders is a useful foundation but does not yet detect checksum failures, near-misses or semantic placeholder merges.
- Candidate robust formats such as `[[SP_PERSON_0001_A7F3]]` should remain proposal-only until WP31.
- Checksum design must avoid leaking original sensitive values.
- Backward compatibility with legacy placeholders is mandatory.

Intentionally not changed:

- No placeholder migration.
- No Scrub Key schema change.
- No reinsert helper change.
- No UI change.
- No AI/cloud integration.
- No tests added or changed.
- No export behavior change.
- No final placeholder format mandated.

Next recommended step:

- WP31 — LLM-resistant placeholder format proposal.

## Phase 4: Hidden content and document hygiene

### WP35 — DOCX hidden content risk review

Status: completed document-hygiene/specification-only.

Purpose:

- Review DOCX metadata, comments, tracked changes, headers, footers, footnotes, text boxes, custom XML and hidden document parts as leakage risks.
- Define current DOCX support assumptions and distinguish visible body-text scrubbing, hidden-content scrubbing, metadata cleaning, unsupported-content warnings and future export blocking.
- Define safe extraction and cleaning sequences before helper implementation.

Files added:

```text
DOCX_HIDDEN_CONTENT_RISK_REVIEW.md
handover/workpackages/20260609_2325_docx_hidden_content_risk_review.md
```

Files changed:

```text
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
```

Main risk findings:

- Current DOCX support covers `word/document.xml` text nodes, including normal body paragraphs and tables, but not full package hygiene.
- Headers, footers, comments, tracked changes, metadata, custom XML, footnotes/endnotes, text boxes/shapes and embedded objects can contain sensitive values outside visible body text.
- Tracked changes are a critical leakage risk because deleted text and author/timestamp data can remain in XML.
- Metadata and custom XML should be treated as separate cleaning problems, not as normal visible-text scrubbing.
- Blocking export is a product semantics change and must not be introduced silently.

Intentionally not changed:

- No DOCX cleaner implemented.
- No DOCX parser changed.
- No export semantics changed.
- No UI changed.
- No tests added or changed.
- No real documents added.
- No cloud processing added.
- No dependency changes made.
- No direct edit to `presidio_streamlit.py`.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No direct edit to `fix_streamlit_pdf_text_reinsert.py`.

Next recommended step:

- WP58 — Parallel specification consolidation and next execution queue.
- After WP58 reconciliation, WP36 — DOCX metadata cleaner helper.

## Active / next recommended workpackages

The WP18 UI line is closed. WP19, WP25, WP30 and WP35 are complete.

The coordinator should now run:

```text
WP58 — Parallel specification consolidation and next execution queue
```

WP58 must reconcile WP19, WP25, WP30 and WP35 before implementation packages such as WP20, WP26, WP31 or WP36 start.

The following workpackages can also be prepared and run in parallel because they do not touch the same UI flow:

### WP45 — Local runtime architecture plan

Type: architecture/specification.

Purpose:

- Bring local-first runtime earlier in the roadmap.
- Compare minimal local Streamlit launcher, PyInstaller, Tauri and Electron paths.

Likely files:

```text
LOCAL_RUNTIME_ARCHITECTURE_PLAN.md
DECISION_LOG.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_local_runtime_architecture_plan.md
```

No packaging implementation in WP45.

### WP50 — Pilot design: Legal vs Zorg

Type: validation/GTM specification.

Purpose:

- Compare first pilot route: Scrub Legal versus Scrub Zorg.
- Define ICP, pilot documents, consent/NDA process, metrics and decision criteria.

Likely files:

```text
PILOT_VALIDATION_PLAN.md
DECISION_LOG.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_pilot_validation_plan.md
```

No real customer data or real documents in repo.

### WP56 — User-facing release notes split and documentation hygiene

Type: documentation.

Purpose:

- Keep `CHANGELOG.md` as internal workpackage log.
- Keep `RELEASE_NOTES.md` as user-facing product capability log.

Likely files:

```text
RELEASE_NOTES.md
CHANGELOG.md
WORKPACKAGES.md
handover/workpackages/YYYYMMDD_HHMM_release_notes_split.md
```

### WP57 — Workflow status monitoring runbook and checks

Type: operations/documentation, optional helper later.

Purpose:

- Reduce dependence on coordinator screenshots.
- Define how workers check GitHub Actions and Hugging Face sync status themselves.
- Define status states and when app verification can start.

Likely files:

```text
STATUS_MONITORING_RUNBOOK.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_status_monitoring_runbook.md
```

No GitHub workflow changes unless separately approved.

## Parallelization rules

Safe in parallel after WP18B closeout:

```text
WP45, WP50, WP56, WP57
```

Do not run in parallel:

- multiple edits to Docker startup patch order;
- multiple edits to `presidio_streamlit.py` or `fix_streamlit_nested_expanders.py`;
- multiple changes to export/download flow;
- implementation work that depends on unresolved specs.

## Documentation model

- `ROADMAP.md`: strategy, risk-driven phase order and architecture.
- `WORKPACKAGES.md`: active queue and dependencies.
- `CHANGELOG.md`: internal workpackage implementation log.
- `RELEASE_NOTES.md`: user-facing product changes.
- `DECISION_LOG.md`: accepted strategic/architecture/product decisions.
- `RISK_REGISTER.md`: active privacy/product/security risks and mitigations.
- `handover/workpackages/`: worker handovers.
