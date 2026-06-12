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
WP28B — Scrub Key warning implementation planning: completed UI/security implementation-planning-only.
WP29 — Scrub Key secure import/export tests: completed helper/tests-only after PR/Actions verification.
WP29B — Scrub Key import/export edge-case hardening: completed helper/tests-only with minimal unsupported-version validation hardening.
WP30 — Placeholder robustness review: completed architecture/specification-only.
WP31 — LLM-resistant placeholder format proposal: completed architecture/proposal-only.
WP32 — Placeholder checksum/validation helper: completed helper/tests-only.
WP33 — Placeholder audit hardening: completed audit/helper hardening-only.
WP34 — Synthetic AI-output placeholder corruption tests: completed synthetic fixtures/tests-only.
WP35 — DOCX hidden content risk review: completed document-hygiene/specification-only.
WP45 — Local runtime architecture plan: completed architecture/specification-only.
WP46 — Minimal local Streamlit launcher: completed minimal local runtime implementation.
WP47 — Local file handling/privacy test: completed local runtime privacy validation.
WP58 — Parallel specification consolidation and next execution queue: completed documentation/planning-only.
```

## Completed recall/trust line

```text
WP19 — Recall benchmark specification.
WP20 — Synthetic messy Dutch legal/zorg benchmark corpus.
WP21 — Gold-label entity schema.
WP22 — Recall/precision test runner.
WP23 — Entity-class scorecard in CI.
WP24 — False-negative residual-risk report.
```

The recall/trust line is now report-only complete through residual-risk reporting. Remaining future work: complete gold-label sidecars, recognizer-backed baselines, approved thresholds and user-facing audit integration.

## Scrub Key security line

```text
WP25 — Scrub Key threat model: completed security/specification-only.
WP26 — Scrub Key encryption/lifecycle specification: completed security/lifecycle-specification-only.
WP27 — Scrub Key warning UX plan: completed UX/security specification-only.
WP28 — Scrub Key expiry/delete policy: completed security/lifecycle-policy-only.
WP28B — Scrub Key warning implementation planning: completed UI/security implementation-planning-only.
WP29 — Scrub Key secure import/export tests: completed helper/tests-only after PR/Actions verification.
WP29B — Scrub Key import/export edge-case hardening: completed helper/tests-only.
```

Next recommended Scrub Key step:

```text
WP28C — MVP Scrub Key warning/acknowledgement UI implementation
```

Alternative Scrub Key test scaffolding package:

```text
WP29C — Scrub Key warning UI regression test scaffolding
```

## Placeholder robustness line

```text
WP30 — Placeholder robustness review: completed architecture/specification-only.
WP31 — LLM-resistant placeholder format proposal: completed architecture/proposal-only.
WP32 — Placeholder checksum/validation helper: completed helper/tests-only.
WP33 — Placeholder audit hardening: completed audit/helper hardening-only.
WP34 — Synthetic AI-output placeholder corruption tests: completed synthetic fixtures/tests-only.
```

The placeholder robustness line is complete through synthetic AI-output corruption tests. Do not start robust placeholder generation, placeholder migration or Scrub Key schema work without a separate approved gated package.

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
WP47 — Local file handling/privacy test: completed local runtime privacy validation.
```

WP47 files added/changed:

```text
tests/test_local_file_handling_privacy.py
LOCAL_RUN.md
handover/workpackages/20260612_1500_local_file_handling_privacy_test.md
```

WP47 summary:

- Added local launcher privacy/file-handling tests for default loopback binding, default port, Streamlit usage-stats disabling, absence of cloud/AI/telemetry endpoints in the launcher command, absence of document content or filenames in launcher arguments, no launcher logging/temp-file/packaging behavior, and LOCAL_RUN privacy-boundary documentation.
- Updated `LOCAL_RUN.md` with Hugging Face demo boundary, runtime privacy expectations, temporary/runtime file expectations, no-telemetry/no-cloud-processing clarification and no installer/packaging claim.
- No Streamlit UI, upload/download/export/reinsert semantics, cloud document processing, telemetry, installer/packaging, Docker/startup behavior, dependency, real data or app behavior changed.

Next recommended local-runtime step:

```text
WP48 — Portable Windows proof of concept
```

Only start WP48 after WP47 CI/status is acceptable and coordinator confirms this local-runtime line should proceed before other risk lines.

## Active / next recommended execution queue

The next recommended workpackage from the Scrub Key security line is:

```text
WP28C — MVP Scrub Key warning/acknowledgement UI implementation
```

The next recommended workpackage from the local-runtime line is:

```text
WP48 — Portable Windows proof of concept
```

Other gated future work:

```text
Placeholder robustness — robust placeholder generation/compatibility implementation only after explicit schema/format approval.
DOCX hygiene — WP36 remains blocked until tighter metadata-only helper boundary is approved.
```

## Next workpackage definitions

### WP28C — MVP Scrub Key warning/acknowledgement UI implementation

Type: UI/security implementation.

Purpose:

- Implement the MVP Scrub Key warning and acknowledgement placements defined in `SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md`.
- Add clear Dutch warnings for Scrub Key creation, export/download, import/reload, reinsert, restored output download, Downloads/local storage, shared-computer risk, e-mail/AI upload risk, loss-of-key and tampering/mismatch risk.
- Add/update UI patch regression tests for warning placement and acknowledgement gating.

Allowed direction:

- Edit `fix_streamlit_nested_expanders.py` only unless a test requires a narrow related patch file update.
- Add/update tests for Streamlit patch output.
- Acknowledgement gating may disable high-risk buttons until the user checks the relevant checkbox.
- Preserve exported JSON content, import behavior, reinsert behavior and file download semantics after acknowledgement.
- No Scrub Key schema migration.
- No encryption.
- No automatic deletion.
- No expiry blocking.
- No hidden recovery.
- No cloud processing.
- No real data.

Likely files:

```text
fix_streamlit_nested_expanders.py
tests/test_scrub_key_ui_patch.py
tests/test_two_mode_ui_patch.py
tests/test_txt_reinsert_ui_patch.py
tests/test_docx_reinsert_ui_patch.py
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_mvp_scrub_key_warning_acknowledgement_ui.md
```

Because WP28C changes UI behavior, app verification is required after GitHub Actions and Hugging Face sync are green.

### WP48 — Portable Windows proof of concept

Type: local runtime packaging proof of concept.

Purpose:

- Validate a minimal portable Windows/Python packaging direction after WP47 local privacy boundaries.
- Keep this as proof-of-concept only unless a separate packaging decision approves broader implementation.

Allowed direction:

- No MSI claim unless explicitly approved.
- No production installer claim.
- No cloud document processing.
- No telemetry.
- No real data.
- No Streamlit UI behavior changes.
- No export/reinsert semantic changes.

## Blocked work

Do not start yet:

```text
WP36 — DOCX metadata cleaner helper
```

Also blocked until separate approval or later specs:

- Scrub Key encryption implementation.
- Scrub Key JSON schema migration.
- Placeholder migration.
- Robust placeholder generation in product flow.
- Placeholder auto-repair or guessed placeholder intent.
- DOCX comment/tracked-change removal.
- Clean DOCX export blocking.
- Restored PDF output.
- OCR.
- Cloud document processing.
