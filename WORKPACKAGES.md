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
WP16 / WP16-FIX / WP16B — PDF helper line: completed after Actions/sync verification.
WP17 / WP17B — PDF text extraction reinsert UI planning/status reconciliation: completed.
WP18 / WP18-FIX / WP18B / WP18C — PDF text to restored TXT UI and governance line: completed and app-verified where applicable.
WP19 — Recall benchmark specification: completed specification-only.
WP20 — Synthetic messy Dutch legal/zorg benchmark corpus: completed benchmark-corpus-only.
WP21 — Gold-label entity schema: completed benchmark schema/closeout-only.
WP22 — Recall/precision test runner: completed report-only benchmark runner implementation.
WP23 — Entity-class scorecard in CI: completed report-only CI/entity-class scorecard foundation.
WP24 — False-negative residual-risk report: completed report-only residual-risk report foundation.
WP25 — Scrub Key threat model: completed security/specification-only.
WP26 — Scrub Key encryption/lifecycle specification: completed security/lifecycle-specification-only.
WP27 — Scrub Key warning UX plan: completed UX/security specification-only.
WP28 — Scrub Key expiry/delete policy: completed security/lifecycle-policy-only.
WP30 — Placeholder robustness review: completed architecture/specification-only.
WP31 — LLM-resistant placeholder format proposal: completed architecture/proposal-only.
WP32 — Placeholder checksum/validation helper: completed helper/tests-only.
WP33 — Placeholder audit hardening: completed audit/helper hardening-only.
WP35 — DOCX hidden content risk review: completed document-hygiene/specification-only.
WP45 — Local runtime architecture plan: completed architecture/specification-only.
WP46 — Minimal local Streamlit launcher: completed minimal local runtime implementation.
WP58 — Parallel specification consolidation and next execution queue: completed documentation/planning-only.
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

### WP21 — Gold-label entity schema

Status: completed benchmark schema/closeout-only.

Files added:

```text
benchmark/gold/schema/gold_label_schema.json
benchmark/gold/examples/legal_process_messy_001.gold.example.json
benchmark/gold/examples/care_operations_messy_001.gold.example.json
handover/workpackages/20260610_1900_gold_label_entity_schema_closeout.md
```

### WP22 — Recall/precision test runner

Status: completed report-only benchmark runner implementation.

Files added:

```text
benchmark/run_recall_precision.py
tests/test_recall_precision_runner.py
handover/workpackages/20260612_1200_recall_precision_test_runner.md
```

Summary:

- Added a deterministic local recall/precision runner for synthetic WP21 gold-label sidecars and supplied prediction JSON.
- Reports exact and value-normalized recall/precision, per-domain metrics, per-entity-class metrics, false negatives, false positives, preserve-term failures, known-trap failures and diagnostic-only partial overlaps.
- No recognizer logic, UI, CI threshold, dependency, export/reinsert behavior, real data or cloud processing was added.

### WP23 — Entity-class scorecard in CI

Status: completed report-only CI/entity-class scorecard foundation.

Files added:

```text
benchmark/build_entity_scorecard.py
benchmark/reports/README.md
tests/test_entity_scorecard.py
handover/workpackages/20260612_1230_entity_class_scorecard_ci.md
```

Summary:

- Added a report-only entity-class scorecard wrapper around the WP22 runner.
- Scorecard artifacts explicitly record `synthetic_only`, `report_only`, `thresholds_applied: false`, `production_gate: false` and `safe_for_production_claim: false`.
- No recognizer logic, UI, CI threshold, dependency, export/reinsert behavior, real data or cloud processing was added.

### WP24 — False-negative residual-risk report

Status: completed report-only false-negative residual-risk report foundation.

Files added:

```text
benchmark/build_residual_risk_report.py
tests/test_residual_risk_report.py
handover/workpackages/20260612_1300_false_negative_residual_risk_report.md
```

Files changed:

```text
benchmark/reports/README.md
WORKPACKAGES.md
CHANGELOG.md
RISK_REGISTER.md
```

Summary:

- Added a report-only residual-risk helper that consumes a WP23 scorecard or builds one from WP22/WP23 inputs.
- The report shows synthetic-only warning, report-only/no-production-safety policy, benchmark coverage status, residual false-negative risks, unsupported/not-yet-baselined classes and recommended next work.
- No recognizer logic, UI, production threshold, production gate, dependency, export/reinsert behavior, real data or cloud processing was added.

## Scrub Key security line

```text
WP25 — Scrub Key threat model: completed security/specification-only.
WP26 — Scrub Key encryption/lifecycle specification: completed security/lifecycle-specification-only.
WP27 — Scrub Key warning UX plan: completed UX/security specification-only.
WP28 — Scrub Key expiry/delete policy: completed security/lifecycle-policy-only.
```

Next recommended Scrub Key step:

```text
WP29 — Scrub Key secure import/export tests
```

Alternative Scrub Key sequencing if UI planning should precede tests:

```text
WP28B — Scrub Key warning implementation planning
```

## Placeholder robustness line

```text
WP30 — Placeholder robustness review: completed architecture/specification-only.
WP31 — LLM-resistant placeholder format proposal: completed architecture/proposal-only.
WP32 — Placeholder checksum/validation helper: completed helper/tests-only.
WP33 — Placeholder audit hardening: completed audit/helper hardening-only.
```

WP32 files added:

```text
placeholder_validation.py
tests/test_placeholder_validation.py
handover/workpackages/20260612_0015_placeholder_checksum_validation_helper.md
handover/workpackages/20260612_0030_placeholder_validation_helper_closeout.md
```

WP33 files added:

```text
placeholder_audit.py
tests/test_placeholder_audit.py
handover/workpackages/20260612_0045_unknown_changed_placeholder_audit_hardening.md
handover/workpackages/20260612_0105_placeholder_audit_hardening_closeout.md
```

WP33 summary:

- Added a pure placeholder audit helper using WP32 validation output.
- Classifies legacy, robust, malformed robust, truncated robust, integrity-failed and unknown placeholder-like tokens.
- Reports audit fields such as `placeholder_format_summary`, `observed_placeholder_like_tokens`, `legacy_placeholders`, `robust_placeholders`, `malformed_robust_placeholders`, `integrity_failed_placeholders`, `unknown_placeholder_like_tokens`, `missing_placeholders` and `placeholder_validation_issues`.
- Leaves unknown, malformed and failed-integrity tokens unchanged and does not silently repair or guess placeholder intent.
- Existing legacy reinsert semantics remain compatible.
- No placeholder migration, robust placeholder generation, Scrub Key schema change, UI/export behavior change, dependency change or AI/cloud integration was added.

Next recommended placeholder step:

```text
WP34 — Synthetic AI-output placeholder corruption tests
```

## DOCX hygiene line

```text
WP35 — DOCX hidden content risk review: completed document-hygiene/specification-only.
```

Blocked until tighter helper boundary is approved:

```text
WP36 — DOCX metadata cleaner helper
```

## Local runtime line

```text
WP45 — Local runtime architecture plan: completed architecture/specification-only.
WP46 — Minimal local Streamlit launcher: completed minimal local runtime implementation.
```

Next recommended local-runtime step:

```text
WP47 — Local file handling/privacy test
```

## Planning / consolidation

```text
WP58 — Parallel specification consolidation and next execution queue: completed documentation/planning-only.
```

## Active / next recommended execution queue

The next recommended workpackage from the Scrub Key security line is:

```text
WP29 — Scrub Key secure import/export tests
```

Alternative Scrub Key sequencing if UI planning should precede tests:

```text
WP28B — Scrub Key warning implementation planning
```

The next recommended workpackage from the placeholder robustness line is:

```text
WP34 — Synthetic AI-output placeholder corruption tests
```

The next recommended workpackage from the local-runtime line is:

```text
WP47 — Local file handling/privacy test
```

Reason:

```text
WP24 completed the first report-only false-negative residual-risk report foundation for the recall/trust line. The recall/trust line still needs complete gold-label sidecars, recognizer-backed prediction baselines and later approved thresholds. WP33 completed additive placeholder audit helper hardening, so the placeholder line can proceed to synthetic AI-output corruption tests without migration or generation changes. WP46 added the minimal local launcher, so the local-runtime line can proceed to local file handling and privacy validation.
```

## Next workpackage definitions

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
RISK_REGISTER.md
handover/workpackages/YYYYMMDD_HHMM_scrub_key_secure_import_export_tests.md
```

### WP34 — Synthetic AI-output placeholder corruption tests

Type: synthetic corruption tests.

Purpose:

- Add synthetic AI-output-style placeholder corruption fixtures and tests after WP33.
- Cover translation, summarization, markdown/HTML, spacing, punctuation, truncation, integrity failure and placeholder deletion/merge scenarios.
- Keep tests synthetic and report/audit focused.

Allowed direction:

- Tests and synthetic fixtures only unless a narrow helper defect is discovered.
- No placeholder migration.
- No robust placeholder generation in product flow.
- No Scrub Key schema migration.
- No UI feature change.
- No export behavior change.
- No AI/cloud integration.
- No real data.

### WP47 — Local file handling/privacy test

Type: local runtime privacy validation.

Purpose:

- Validate local file handling, temp-file behavior, logs and network expectations after WP46.
- Keep the Hugging Face demo separate from the future confidential-processing trust environment.

Allowed direction:

- Tests and documentation only unless a narrow helper is explicitly required.
- No UI feature changes.
- No cloud document processing.
- No real data.
- No installer or packaging implementation.

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
- Placeholder auto-repair or guessed placeholder intent.
- DOCX comment/tracked-change removal.
- Clean DOCX export blocking.
- Restored PDF output.
- OCR.
- Cloud document processing.
