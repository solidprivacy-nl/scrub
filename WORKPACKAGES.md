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
WP21 — Gold-label entity schema: completed benchmark schema/closeout-only.
WP25 — Scrub Key threat model: completed security/specification-only.
WP26 — Scrub Key encryption/lifecycle specification: completed security/lifecycle-specification-only.
WP27 — Scrub Key warning UX plan: completed UX/security specification-only.
WP28 — Scrub Key expiry/delete policy: completed security/lifecycle-policy-only.
WP30 — Placeholder robustness review: completed architecture/specification-only.
WP31 — LLM-resistant placeholder format proposal: completed architecture/proposal-only.
WP35 — DOCX hidden content risk review: completed document-hygiene/specification-only.
WP45 — Local runtime architecture plan: completed architecture/specification-only.
WP46 — Minimal local Streamlit launcher: completed minimal local runtime implementation.
WP58 — Parallel specification consolidation and next execution queue: completed documentation/planning-only.
```

## Closed UI line: WP18 PDF text to restored TXT

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

### WP21 — Gold-label entity schema

Status: completed benchmark schema/closeout-only.

Files added:

```text
benchmark/gold/schema/gold_label_schema.json
benchmark/gold/examples/legal_process_messy_001.gold.example.json
benchmark/gold/examples/care_operations_messy_001.gold.example.json
handover/workpackages/20260610_1900_gold_label_entity_schema_closeout.md
```

Files changed:

```text
benchmark/gold/README.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
```

Summary:

- Verified the existing WP21 schema artifact and completed central closeout documentation.
- Confirmed the schema covers gold-label sidecar format, zero-based inclusive/exclusive offsets, source file references, entity class mapping, label IDs, entity IDs, expected text spans, normalization guidance, preserve-term labels, known-trap labels, partial-overlap guidance, validation expectations and future WP22 runner expectations.
- Updated `benchmark/gold/README.md` from WP20 placeholder language to WP21 schema foundation status.
- No schema change was needed.

Intentionally not changed:

- No recognizer logic changed.
- No benchmark runner implemented.
- No CI scorecard added.
- No production test gate added.
- No UI changed.
- No dependency changes.
- No export/reinsert behavior changed.
- No real data added.
- No cloud processing added.

Next recommended step from WP21:

```text
WP22 — Recall/precision test runner
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

### WP27 — Scrub Key warning UX plan

Status: completed UX/security specification-only.

Files added:

```text
SCRUB_KEY_WARNING_UX_PLAN.md
handover/workpackages/20260610_0145_scrub_key_warning_ux_plan.md
```

Files changed:

```text
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
```

Summary:

- Converts WP25/WP26 Scrub Key threat and lifecycle findings into a user-facing warning and acknowledgement plan.
- Defines severity levels: informational, warning, critical and blocking candidate for later policy.
- Defines warning and acknowledgement expectations for Scrub Key creation, export/download, local storage, import/reload, reinsert mode, restored output download, deletion/expiry guidance, shared-computer risk, e-mail/AI upload risk, loss-of-key and tampering/mismatch warnings.
- Provides proposed Dutch UI copy without implementing it.
- Clarifies MVP warning expectations versus later secure/local desktop warning and blocking candidates.

Intentionally not changed:

- No UI implementation.
- No Streamlit patch changed.
- No helper logic changed.
- No Scrub Key schema migration.
- No encryption implementation.
- No import/export behavior changed.
- No reinsert behavior changed.
- No tests added or changed.
- No secrets or real data added.

Next recommended step from WP27:

```text
WP28 — Scrub Key expiry/delete policy
```

### WP28 — Scrub Key expiry/delete policy

Status: completed security/lifecycle-policy-only.

Files added:

```text
SCRUB_KEY_EXPIRY_DELETE_POLICY.md
handover/workpackages/20260610_1826_scrub_key_expiry_delete_policy.md
```

Files changed:

```text
DECISION_LOG.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
```

Summary:

- Defines Scrub Key retention principles, user-controlled deletion, matter/project retention guidance, Downloads risk, shared-computer risk, expiry guidance, manual deletion guidance, loss-of-key consequences, tampering/mismatch consequences and audit/logging expectations.
- Establishes that MVP expiry is guidance-only: no automatic deletion, no schema migration, no import/export behavior change and no reinsert behavior change.
- Records the accepted policy decision that Scrub must not silently delete Scrub Keys, mappings, restored output, audit context or external copies, and must not keep hidden recovery copies.
- Provides Dutch user-facing policy copy examples for future warning/planning work.

Intentionally not changed:

- No UI implementation.
- No Streamlit patch changed.
- No helper logic changed.
- No automatic deletion.
- No Scrub Key schema migration.
- No encryption implementation.
- No import/export behavior changed.
- No reinsert behavior changed.
- No tests added or changed.
- No secrets or real data added.

Next recommended step from WP28:

```text
WP29 — Scrub Key secure import/export tests
```

Alternative sequencing if the coordinator wants UI planning before tests:

```text
WP28B — Scrub Key warning implementation planning
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

### WP31 — LLM-resistant placeholder format proposal

Status: completed architecture/proposal-only.

Files added:

```text
PLACEHOLDER_FORMAT_PROPOSAL.md
handover/workpackages/20260610_0035_placeholder_format_proposal.md
handover/workpackages/20260610_1824_placeholder_format_proposal.md
```

Files changed:

```text
DECISION_LOG.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
```

Summary:

- Compares `[PERSOON_1]`, `[[SP_PERSON_0001_A7F3]]`, `{{SP:PERSON:0001:A7F3}}` and `⟦SP_PERSON_0001_A7F3⟧`.
- Recommends the future architecture direction `[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]`, for example `[[SP_PERSON_0001_A7F3]]`.
- Defines entity naming, counter format, integrity-token direction, human readability, LLM robustness, copy/paste robustness, TXT/DOCX/PDF compatibility, Scrub Key compatibility, backward compatibility, migration risks, audit/validation requirements and implementation phases.
- Explicitly warns that visible checksum/integrity values must not be derived directly from original sensitive data.

Intentionally not changed:

- No placeholder migration.
- No reinsert helper change.
- No Scrub Key schema change.
- No UI change.
- No export behavior change.
- No tests added or changed.
- No AI/cloud integration.
- No dependency changes.

Next recommended step from WP31:

```text
WP32 — Placeholder checksum/validation helper
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

### WP45 — Local runtime architecture plan

Status: completed architecture/specification-only.

Files added:

```text
LOCAL_RUNTIME_ARCHITECTURE_PLAN.md
handover/workpackages/20260610_0115_local_runtime_architecture_plan.md
```

Files changed:

```text
DECISION_LOG.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
```

Summary:

- Defines the current Hugging Face role as demo/development environment, not the trust environment for confidential production documents.
- Defines why local-first matters for Dutch legal and care workflows.
- Compares local Streamlit launcher, PyInstaller, Tauri and Electron across privacy, complexity, Windows friendliness, installer effort, offline support, frontend flexibility and maintainability.
- Defines local file handling, offline, telemetry/network, secrets, Scrub Key local storage, installer/update and supportability expectations.
- Recommends the MVP path: minimal local Streamlit launcher, local file-handling/privacy test and PyInstaller/portable Windows proof of concept.
- Recommends the later professional path: Tauri desktop shell with reusable Python core, with Electron as alternative depending on frontend/team requirements.

Intentionally not changed:

- No packaging implementation.
- No installer created.
- No runtime code changed.
- No UI changed.
- No Docker/runtime startup change.
- No dependency change.
- No cloud processing added.
- No telemetry implementation.
- No real data added.

Next recommended step from WP45:

```text
WP46 — Minimal local Streamlit launcher
```

### WP46 — Minimal local Streamlit launcher

Status: completed minimal local runtime implementation.

Files added:

```text
scripts/run_local_streamlit.py
LOCAL_RUN.md
handover/workpackages/20260610_1828_minimal_local_streamlit_launcher.md
```

Files changed:

```text
WORKPACKAGES.md
CHANGELOG.md
```

Summary:

- Added a minimal local Python launcher for the existing Streamlit app.
- The launcher runs the same existing startup patch scripts used by the container startup path, then starts `presidio_streamlit.py` locally through Streamlit.
- Default bind address is `127.0.0.1`, default port is `8501` and Streamlit usage stats are disabled for this local launcher path.
- Added `LOCAL_RUN.md` with Python 3.10 assumption, dependency installation, exact launch command, local-only warning, no-real-data-in-repo warning, locally processed files, current non-guarantees and next validation step.

Intentionally not changed:

- No installer.
- No PyInstaller packaging.
- No Tauri/Electron implementation.
- No Docker startup change.
- No Streamlit UI feature change.
- No export/reinsert behavior change.
- No dependency change.
- No cloud processing added.
- No real data added.

Validation:

```text
python -m py_compile scripts/run_local_streamlit.py
```

Next recommended step from WP46:

```text
WP47 — Local file handling/privacy test
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

The next recommended workpackage for the recall/trust line remains:

```text
WP22 — Recall/precision test runner
```

The next recommended workpackage from the Scrub Key security line is:

```text
WP29 — Scrub Key secure import/export tests
```

Alternative Scrub Key sequencing if UI planning should precede tests:

```text
WP28B — Scrub Key warning implementation planning
```

The next recommended workpackage from the local-runtime line is:

```text
WP47 — Local file handling/privacy test
```

Other workpackages from the WP58 parallel set may continue independently if not already completed:

```text
WP32 — Placeholder checksum/validation helper
```

Reason:

```text
WP21 completed the gold-label sidecar schema foundation, so the recall/trust line can proceed to the first recall/precision runner. WP28 defined the Scrub Key expiry/delete policy, so the Scrub Key line can proceed to secure import/export tests or warning implementation planning. WP31 accepted the robust placeholder format direction, so the placeholder line can proceed to validation helpers. WP46 added the minimal local launcher, so the local-runtime line can proceed to local file handling and privacy validation.
```

## Next workpackage definitions

### WP22 — Recall/precision test runner

Type: benchmark runner implementation.

Purpose:

- Implement the first runner that reads synthetic corpus files and WP21 gold-label sidecars.
- Validate sidecar offsets and expected text spans before scoring.
- Produce report-only recall/precision output for exact and value-normalized matching.

Allowed direction:

- Synthetic corpus only.
- No recognizer logic changes.
- Report-only runner; no CI failure gate yet.
- No UI changes.
- No export/reinsert changes.
- No real data.

Likely files:

```text
benchmark/run_recall_precision.py or benchmark/runner...
benchmark/reports/...
tests/... if scoped to synthetic runner behavior
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_recall_precision_test_runner.md
```

### WP29 — Scrub Key secure import/export tests

Type: security regression tests.

Purpose:

- Add focused tests for Scrub Key import/export safety expectations after WP25-WP28.
- Verify malformed, wrong-policy, missing-marker and unsafe/tampered key cases are handled visibly and without leaking original values.
- Preserve existing Scrub Key schema and import/export behavior unless a test exposes a bug that requires a separate fix package.

Allowed direction:

- Tests only unless a failing test proves a narrow helper bug and the coordinator approves a fix package.
- Synthetic data only.
- No UI implementation.
- No automatic deletion.
- No encryption implementation.
- No schema migration.
- No export/reinsert behavior change.

Likely files:

```text
tests/test_scrub_key_import.py
tests/test_scrub_key.py
tests/test_scrub_key_reinsert.py
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_scrub_key_secure_import_export_tests.md
```

### WP28B — Scrub Key warning implementation planning

Type: UI/security implementation planning only.

Purpose:

- Translate WP27 warning UX and WP28 expiry/delete policy into exact implementation locations, acknowledgement states and copy inventory before editing Streamlit UI.
- Keep behavior unchanged until a later implementation package is approved.

Allowed direction:

- Planning/specification only.
- No UI implementation.
- No Streamlit patch changes.
- No automatic deletion.
- No schema migration.
- No import/export or reinsert behavior change.

Likely files:

```text
SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_scrub_key_warning_implementation_planning.md
```

### WP32 — Placeholder checksum/validation helper

Type: helper/tests implementation, gated by WP31.

Purpose:

- Implement validation helpers for the recommended robust placeholder shape.
- Keep validation separate from placeholder generation and migration.
- Preserve legacy placeholder support as a separate compatibility mode.

Allowed direction:

- Helper and tests only.
- No placeholder migration.
- No generation of robust placeholders in product flow.
- No reinsert behavior change unless explicitly limited to validation reporting.
- No Scrub Key schema change.
- No UI change.
- No export behavior change.
- No AI/cloud integration.

Likely files:

```text
placeholder_validation.py
tests/test_placeholder_validation.py
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_placeholder_validation_helper.md
```

### WP47 — Local file handling/privacy test

Type: local runtime validation.

Purpose:

- Validate that the minimal local Streamlit runtime handles files in line with the local-first privacy expectations.
- Check source-file handling, Scrub Key handling, restored output handling, audit output handling, logs, temporary files and network behavior where practical.

Allowed direction:

- Validation/tests/checks only.
- No installer.
- No PyInstaller packaging.
- No Tauri/Electron implementation.
- No UI feature changes.
- No export/reinsert behavior changes.
- No cloud processing.
- No telemetry implementation.
- No real data.

Likely files:

```text
local runtime privacy validation file(s), to be specified in the WP47 task
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_local_file_handling_privacy_test.md
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
- Robust placeholder generation in product flow.
- Unknown/changed placeholder audit hardening before the validation helper is stable.
- DOCX comment/tracked-change removal.
- Clean DOCX export blocking.
- Restored PDF output.
- OCR.
- Cloud document processing.
