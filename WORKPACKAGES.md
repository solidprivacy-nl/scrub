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
- No recognizer logic, runner, CI gate, UI, dependency, export/reinsert behavior, real data or cloud processing was added.

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

- Verified the WP21 schema artifact and completed central closeout documentation.
- Confirmed the schema covers gold-label sidecar format, zero-based inclusive/exclusive offsets, source file references, entity class mapping, label IDs, entity IDs, expected text spans, normalization guidance, preserve-term labels, known-trap labels, partial-overlap guidance, validation expectations and future WP22 runner expectations.
- Updated `benchmark/gold/README.md` from WP20 placeholder language to WP21 schema foundation status.
- No recognizer logic, benchmark runner, CI scorecard, production gate, UI, dependency, export/reinsert behavior, real data or cloud processing was added.

Next recommended step from WP21:

```text
WP22 — Recall/precision test runner
```

### WP22 — Recall/precision test runner

Status: completed report-only benchmark runner implementation.

Files added:

```text
benchmark/run_recall_precision.py
tests/test_recall_precision_runner.py
handover/workpackages/20260612_1200_recall_precision_test_runner.md
```

Files changed:

```text
WORKPACKAGES.md
CHANGELOG.md
```

Summary:

- Added a deterministic local recall/precision runner for synthetic WP21 gold-label sidecars and supplied prediction JSON.
- The runner validates source-file references, synthetic-only sidecars, zero-based inclusive/exclusive offsets and `text == source_text[start:end]` before scoring.
- The runner reports exact and value-normalized recall/precision, per-domain metrics, per-entity-class metrics, false negatives, false positives, preserve-term failures, known-trap failures and diagnostic-only partial overlaps.
- The runner does not call recognizers, Presidio, Streamlit, AI or cloud services.
- The runner applies no CI threshold and no production-blocking gate.

Validation:

```text
python -m json.tool benchmark/gold/schema/gold_label_schema.json
pytest tests/test_recall_precision_runner.py
```

Intentionally not changed:

- No recognizer logic changed.
- No Streamlit UI changed.
- No CI scorecard or production test gate added.
- No dependency changes.
- No export/reinsert behavior changed.
- No real data added.
- No cloud processing added.

Next recommended step from WP22:

```text
WP23 — Entity-class scorecard in CI
```

## Other completed risk-driven packages

### Scrub Key security line

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

### Placeholder robustness line

```text
WP30 — Placeholder robustness review: completed architecture/specification-only.
WP31 — LLM-resistant placeholder format proposal: completed architecture/proposal-only.
```

Next recommended placeholder step:

```text
WP32 — Placeholder checksum/validation helper
```

### DOCX hygiene line

```text
WP35 — DOCX hidden content risk review: completed document-hygiene/specification-only.
```

Blocked until tighter helper boundary is approved:

```text
WP36 — DOCX metadata cleaner helper
```

### Local runtime line

```text
WP45 — Local runtime architecture plan: completed architecture/specification-only.
WP46 — Minimal local Streamlit launcher: completed minimal local runtime implementation.
```

Next recommended local-runtime step:

```text
WP47 — Local file handling/privacy test
```

### Planning / consolidation

```text
WP58 — Parallel specification consolidation and next execution queue: completed documentation/planning-only.
```

## Active / next recommended execution queue

The next recommended workpackage for the recall/trust line is:

```text
WP23 — Entity-class scorecard in CI
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
WP22 made recall/precision measurable but report-only. WP23 should add entity-class scorecard integration in CI without creating misleading product safety claims. WP28 defined Scrub Key expiry/delete policy, so the Scrub Key line can proceed to secure import/export tests or warning implementation planning. WP31 accepted the robust placeholder format direction, so the placeholder line can proceed to validation helpers. WP46 added the minimal local launcher, so the local-runtime line can proceed to local file handling and privacy validation.
```

## Next workpackage definitions

### WP23 — Entity-class scorecard in CI

Type: benchmark CI/report integration.

Purpose:

- Add CI-visible scorecard output for the WP22 recall/precision runner.
- Keep the first CI integration report-only unless later thresholds are explicitly approved.
- Make per-entity class gaps visible without claiming production safety.

Allowed direction:

- Synthetic corpus only.
- No recognizer logic changes unless separately approved.
- No production-blocking threshold yet unless separately approved.
- No UI changes.
- No export/reinsert changes.
- No real data.
- No cloud processing.

Likely files:

```text
benchmark/reports/...
tools or workflow/report-only integration if approved
tests/... for scorecard/report behavior
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_entity_class_scorecard_ci.md
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

### WP32 — Placeholder checksum/validation helper

Type: helper/test implementation.

Purpose:

- Add validation/checksum helper foundation for the WP31 robust placeholder proposal.
- Do not migrate placeholder generation or reinsert behavior yet.

Allowed direction:

- Helper and tests only.
- No placeholder migration.
- No Scrub Key schema migration.
- No UI changes.
- No export/reinsert behavior changes.
- No real data.
- No cloud processing.

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
- Unknown/changed placeholder audit hardening before the format proposal is stable.
- DOCX comment/tracked-change removal.
- Clean DOCX export blocking.
- Restored PDF output.
- OCR.
- Cloud document processing.
