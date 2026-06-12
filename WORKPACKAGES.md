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

## Required workpackage claim check

Before starting implementation or documentation changes, check:

```text
workpackage_claims/
```

If a claim file for the same workpackage exists with status `in_progress`, stop and report that another worker has already claimed the package.

If no claim exists, create a new claim file before changing code, tests, UI, export, schema or shared documentation. Use `GitHub.create_file` so a duplicate claim fails instead of silently overwriting another worker.

When done, update the same claim file to `completed` and include the final commit/PR, handover path, tests/checks and next step.

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
WP48 — Portable Windows proof of concept: completed Windows portable proof-of-concept launcher/docs/tests.
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

WP28C claim status:

```text
workpackage_claims/WP28C_mvp_scrub_key_warning_acknowledgement_ui.md — in_progress
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
WP48 — Portable Windows proof of concept: completed Windows portable proof-of-concept launcher/docs/tests.
```

WP48 files added/changed:

```text
scripts/run_windows_portable_poc.ps1
WINDOWS_PORTABLE_POC.md
tests/test_windows_portable_poc.py
LOCAL_RUN.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
workpackage_claims/WP48_portable_windows_proof_of_concept.md
handover/workpackages/20260612_1530_portable_windows_proof_of_concept.md
```

WP48 summary:

- Added a minimal Windows PowerShell proof-of-concept wrapper that delegates to the existing `scripts/run_local_streamlit.py` local launcher.
- Added `WINDOWS_PORTABLE_POC.md` documenting the portable-folder concept, privacy boundary, Windows command, non-goals and validation matrix.
- Added static tests to verify the wrapper delegates to the existing launcher, defaults to `127.0.0.1`/`8501`, does not add cloud/telemetry/package behavior, does not accept document/secret arguments, and that documentation records the proof-of-concept boundary.
- Updated `LOCAL_RUN.md` to describe WP48 and keep explicit no-production-installer/no-MSI/no-offline-guarantee boundaries.
- No Streamlit UI, upload/download/export/reinsert semantics, Docker/Hugging Face startup behavior, dependencies, telemetry, cloud document processing, real data, signed packaging or production installer behavior changed.

Next recommended local-runtime step:

```text
WP49 — Desktop packaging decision
```

Only start WP49 after WP48 CI/status is acceptable and the coordinator confirms the local-runtime line should proceed before other risk lines.

## Active / next recommended execution queue

The next recommended workpackage from the Scrub Key security line is:

```text
WP28C — MVP Scrub Key warning/acknowledgement UI implementation
```

Claimed/in progress:

```text
workpackage_claims/WP28C_mvp_scrub_key_warning_acknowledgement_ui.md
```

The next recommended workpackage from the local-runtime line is:

```text
WP49 — Desktop packaging decision
```

Other gated future work:

```text
Placeholder robustness — robust placeholder generation/compatibility implementation only after explicit schema/format approval.
DOCX hygiene — WP36 remains blocked until tighter metadata-only helper boundary is approved.
```

## Next workpackage definitions

### WP28C — MVP Scrub Key warning/acknowledgement UI implementation

Type: UI/security implementation.

Claim status:

```text
workpackage_claims/WP28C_mvp_scrub_key_warning_acknowledgement_ui.md — in_progress
```

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

### WP49 — Desktop packaging decision

Type: local runtime packaging decision.

Purpose:

- Decide the longer-term local desktop/package direction after WP45-WP48.
- Compare Streamlit/Python folder, PyInstaller, Tauri, Electron and managed enterprise deployment options.
- Define privacy/security requirements before any production packaging or installer claim.

Allowed direction:

- Documentation/decision only unless a separate implementation package is explicitly approved.
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
