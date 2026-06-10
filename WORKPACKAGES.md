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
WP20 — Synthetic messy Dutch legal/zorg benchmark corpus: completed benchmark-corpus-only.
WP25 — Scrub Key threat model: completed security/specification-only.
WP26 — Scrub Key encryption/lifecycle specification: completed security/lifecycle-specification-only.
WP30 — Placeholder robustness review: completed architecture/specification-only.
WP35 — DOCX hidden content risk review: completed document-hygiene/specification-only.
WP58 — Parallel specification consolidation and next execution queue: completed documentation/planning-only.
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

### WP18B — PDF text to restored TXT UI app verification closeout

Status: completed closeout-only.

Closeout evidence recorded:

- GitHub Actions: green based on coordinator/user closeout approval.
- Hugging Face sync: green based on coordinator/user closeout approval.
- App verification: confirmed by coordinator/user closeout approval.

### WP18C — Add Codex worker governance instructions

Status: completed documentation/governance-only.

Codex worker rule:

```text
Workers must write full handovers to handover/workpackages/.
Coordinator chat only needs handover path, commit/PR, status and short summary unless commit failed or GitHub access is unavailable.
```

## Completed risk-driven specification and benchmark packages

### WP19 — Recall benchmark specification

Status: completed specification-only.

Files added:

```text
RECALL_BENCHMARK_SPEC.md
handover/workpackages/20260609_2200_recall_benchmark_spec.md
```

Summary:

- Defined recall/precision benchmark requirements for messy synthetic Dutch legal and care documents.
- Made false negatives / missed sensitive data measurable before recognizer changes.
- Defined entity classes, context-preservation expectations, gold-label requirements and future reporting/CI sequence.

Next recommended step from WP19:

```text
WP20 — Synthetic messy Dutch legal/zorg benchmark corpus
```

### WP20 — Synthetic messy Dutch legal/zorg benchmark corpus

Status: completed benchmark-corpus-only.

Files added:

```text
benchmark/corpus/README.md
benchmark/corpus/legal/legal_process_messy_001.txt
benchmark/corpus/zorg/care_operations_messy_001.txt
benchmark/corpus/mixed/legal_care_mixed_messy_001.txt
benchmark/gold/README.md
handover/workpackages/20260610_0045_synthetic_messy_benchmark_corpus.md
```

Summary:

- Created a first synthetic messy corpus foundation with legal, zorg and mixed professional text fixtures.
- Covered case numbers, client numbers, dossier numbers, claim/incident references, names, addresses, emails, phone numbers, synthetic BSN-like and IBAN-like values, Dutch postcodes, dates, organizations, medical/care references and role/context terms to preserve.
- Added `benchmark/gold/README.md` explaining that full gold labels, zero-based offsets and schema validation belong to WP21.

Intentionally not changed:

- No recognizer logic changed.
- No benchmark runner implemented.
- No CI gate added.
- No UI changed.
- No tests added or changed.
- No dependencies changed.
- No export/reinsert behavior changed.
- No real data added.
- No cloud processing added.

Next recommended step from WP20:

```text
WP21 — Gold-label entity schema
```

### WP25 — Scrub Key threat model

Status: completed security/specification-only.

Files added:

```text
SCRUB_KEY_THREAT_MODEL.md
handover/workpackages/20260609_2258_scrub_key_threat_model.md
```

Summary:

- Treats the Scrub Key as sensitive re-identification data.
- Clarifies that Scrub Key-based output is pseudonymized, not fully anonymized, as long as the key exists.
- Defines leakage, accidental sharing, retention, loss-of-key, tampering, malformed-key and import/export risks.

Next recommended step from WP25:

```text
WP26 — Scrub Key encryption/lifecycle specification
```

### WP26 — Scrub Key encryption/lifecycle specification

Status: completed security/lifecycle-specification-only.

Files added:

```text
SCRUB_KEY_LIFECYCLE_SPEC.md
handover/workpackages/20260610_0015_scrub_key_lifecycle_spec.md
```

Files changed:

```text
DECISION_LOG.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
```

Summary:

- Defines Scrub Key lifecycle states from creation, download/export, local storage, import/reload and active use through sharing risk, expiry and deletion.
- Defines loss-of-key, tampering, password/passphrase, key recovery, metadata and audit/logging expectations.
- Compares warning-only, protected local file, encrypted local file and local vault / managed key store options.
- Recommends warning-only plus explicit lifecycle/protected-local-file guidance for MVP.
- Recommends encrypted files, vault/managed key stores and integrity protection only for later professional/local desktop versions after separate implementation workpackages.

Intentionally not changed:

- No encryption implemented.
- No Scrub Key JSON schema migration.
- No helper logic changed.
- No import/export behavior changed.
- No reinsert behavior changed.
- No UI changed.
- No tests or dependencies changed.
- No secrets or real data added.

Next recommended step from WP26:

```text
WP27 — Scrub Key warning UX plan
```

Alternative next step depending on consolidation:

```text
WP29 — Scrub Key secure import/export tests
```

### WP30 — Placeholder robustness review

Status: completed architecture/specification-only.

Files added:

```text
PLACEHOLDER_ROBUSTNESS_REVIEW.md
handover/workpackages/20260609_2310_placeholder_robustness_review.md
```

Summary:

- Reviews how placeholders survive AI rewriting, translation, summarization and formatting changes.
- Documents current exact-match reinsert assumptions and placeholder corruption risks.
- Defines candidate robust format direction, checksum ideas, validation/audit ideas, migration risks and backward compatibility concerns.

Next recommended step from WP30:

```text
WP31 — LLM-resistant placeholder format proposal
```

### WP35 — DOCX hidden content risk review

Status: completed document-hygiene/specification-only.

Files added:

```text
DOCX_HIDDEN_CONTENT_RISK_REVIEW.md
handover/workpackages/20260609_2325_docx_hidden_content_risk_review.md
```

Summary:

- Reviews DOCX metadata, comments, tracked changes, headers, footers, footnotes, text boxes, custom XML and hidden document parts as leakage risks.
- Defines current DOCX support assumptions, audit requirements, safe extraction and cleaning sequences, and warning/blocking policy boundaries.
- Confirms that blocking export is a product semantics change and must not be introduced silently.

Next recommended step after WP58:

```text
WP36 remains blocked until a tighter metadata-cleaner helper boundary is approved.
```

### WP58 — Parallel specification consolidation and next execution queue

Status: completed documentation/planning-only.

Files added:

```text
PARALLEL_SPEC_CONSOLIDATION_WP58.md
handover/workpackages/20260609_2345_parallel_spec_consolidation_wp58.md
```

Files changed:

```text
DECISION_LOG.md
WORKPACKAGES.md
CHANGELOG.md
```

Consolidation decisions:

- WP20, WP26, WP31 and WP45 may run in parallel now.
- WP20 is the highest priority if only one worker is available, because false negatives remain the highest product risk.
- WP26 can run in parallel with WP20 because Scrub Key lifecycle/specification is separate from detection benchmarking.
- WP31 can run in parallel with WP20 and WP26 because placeholder format proposal is specification-only and must not implement migration.
- WP45 can run in parallel as architecture/planning because it addresses the cloud-demo trust gap without touching UI/runtime implementation.
- WP36 is blocked until a tighter metadata-only/helper-only/no-export-semantics boundary is approved.
- WP50, WP56 and WP57 remain lower-risk optional parallel candidates if worker capacity exists.

Intentionally not changed:

- No code changed.
- No tests added or changed.
- No UI changed.
- No dependencies changed.
- No recognizer logic changed.
- No Scrub Key encryption implemented.
- No placeholder migration.
- No DOCX cleaner implemented.
- No export behavior changed.
- No real data added.
- No cloud processing added.
- No roadmap change made.
- No release notes change made.

## Active / next recommended execution queue

The next recommended workpackage for the recall/trust line is:

```text
WP21 — Gold-label entity schema
```

Other workpackages from the WP58/WP26 parallel set may continue independently if not already completed:

```text
WP27 — Scrub Key warning UX plan
WP31 — LLM-resistant placeholder format proposal
WP45 — Local runtime architecture plan
```

Reason:

```text
WP20 created source corpus fixtures only. Gold-label schema and offset validation are still needed before a runner or CI scorecard can be useful.
```

## Next workpackage definitions

### WP21 — Gold-label entity schema

Type: benchmark schema/specification artifacts.

Purpose:

- Define the sidecar schema for benchmark gold labels.
- Define zero-based offset rules, entity class mapping, preserve terms and known traps.
- Prepare validation expectations before the runner is implemented.

Allowed direction:

- Schema/specification only unless separately approved.
- Synthetic corpus only.
- No recognizer logic changes.
- No runner implementation.
- No CI gate.
- No UI changes.
- No export/reinsert changes.

Likely files:

```text
benchmark/gold/README.md
benchmark/gold/schema...
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_gold_label_entity_schema.md
```

### WP27 — Scrub Key warning UX plan

Type: UX/security specification.

Purpose:

- Convert WP25/WP26 Scrub Key threat and lifecycle findings into a user-facing warning plan.
- Define warning text, placement and acknowledgement expectations for export/download, import/reload, reinsert, deletion/expiry and shared-computer/storage-risk moments.

Allowed direction:

- Specification/UX plan only.
- No UI implementation.
- No Scrub Key schema migration.
- No import/export behavior change.
- No reinsert behavior change.
- No encryption implementation.
- No secrets or real data.

Likely files:

```text
SCRUB_KEY_WARNING_UX_PLAN.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_scrub_key_warning_ux_plan.md
```

### WP31 — LLM-resistant placeholder format proposal

Type: architecture/specification.

Purpose:

- Propose and compare candidate LLM-resistant placeholder formats.
- Define backward compatibility and validation/checksum direction.

Allowed direction:

- Proposal only.
- No placeholder migration.
- No reinsert helper change.
- No Scrub Key schema change.
- No UI change.
- No export behavior change.

Likely files:

```text
PLACEHOLDER_FORMAT_PROPOSAL.md
DECISION_LOG.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_placeholder_format_proposal.md
```

### WP45 — Local runtime architecture plan

Type: architecture/specification.

Purpose:

- Compare local Streamlit launcher, PyInstaller, Tauri and Electron paths.
- Define local file-handling, offline and trust requirements.

Allowed direction:

- Architecture/specification only.
- No packaging implementation.
- No Docker/runtime startup changes.
- No UI changes.
- No cloud processing.

Likely files:

```text
LOCAL_RUNTIME_ARCHITECTURE_PLAN.md
DECISION_LOG.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_local_runtime_architecture_plan.md
```

## Optional safe parallel candidates

These can also be prepared if worker capacity exists:

```text
WP50 — Pilot design: Legal vs Zorg
WP56 — User-facing release notes split and documentation hygiene
WP57 — Workflow status monitoring runbook and checks
```

Constraints:

- WP50 must not use real customer documents or real personal data in the repo.
- WP56 must not rewrite technical history in a way that breaks worker traceability.
- WP57 must not change GitHub workflows unless separately approved.

## Blocked work

Do not start yet:

```text
WP36 — DOCX metadata cleaner helper
```

Reason:

```text
WP36 may affect document/export semantics. It must wait until a tighter metadata-only/helper-only/no-export-semantics boundary is approved.
```

Also blocked until separate approval or later specs:

- Scrub Key encryption implementation.
- Scrub Key JSON schema migration.
- Placeholder migration.
- Placeholder checksum/validation helper implementation before WP31 is accepted.
- Unknown/changed placeholder audit hardening before the format proposal is stable.
- DOCX comment/tracked-change removal.
- Clean DOCX export blocking.
- Restored PDF output.
- OCR.
- Cloud document processing.
- Real-data benchmark fixtures.
- Batch/CLI scale features before single-document trust/security/review/local-runtime foundations are credible.

## Parallelization rules

Safe in parallel now:

```text
WP27, WP31, WP45
```

Optional safe parallel candidates:

```text
WP50, WP56, WP57
```

Do not run in parallel:

- multiple edits to Docker startup patch order;
- multiple edits to `presidio_streamlit.py` or `fix_streamlit_nested_expanders.py`;
- multiple changes to export/download flow;
- implementation work that depends on unresolved specs;
- DOCX cleaner/export semantics work before WP36 boundary approval.

## Documentation model

- `ROADMAP.md`: strategy, risk-driven phase order and architecture.
- `WORKPACKAGES.md`: active queue and dependencies.
- `CHANGELOG.md`: internal workpackage implementation log.
- `RELEASE_NOTES.md`: user-facing product changes.
- `DECISION_LOG.md`: accepted strategic/architecture/product decisions.
- `RISK_REGISTER.md`: active privacy/product/security risks and mitigations.
- `handover/workpackages/`: worker handovers.
