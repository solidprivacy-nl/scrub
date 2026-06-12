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

```text
WP0-WP13B — completed.
WP14-WP18C — completed/app-verified or closeout as previously recorded.
WP19-WP24 — recall/trust line completed through report-only residual-risk reporting.
WP25-WP29C — Scrub Key security, policy, import/export and warning test scaffolding completed.
WP28C — MVP Scrub Key warning/acknowledgement UI implementation: implemented; blocked awaiting coordinator/user evidence for Actions/HF sync and app verification.
WP28C-VERIFY — verification attempted; connector returned no statuses or workflow runs.
WP30-WP34 — placeholder robustness line completed through synthetic AI-output corruption tests.
WP35 — DOCX hidden content risk review completed.
WP45-WP48 — local runtime line completed through portable Windows proof of concept.
WP58 — parallel specification consolidation completed.
```

## Scrub Key security line

Current Scrub Key status:

```text
WP25 — Scrub Key threat model: completed.
WP26 — Scrub Key encryption/lifecycle specification: completed.
WP27 — Scrub Key warning UX plan: completed.
WP28 — Scrub Key expiry/delete policy: completed.
WP28B — Scrub Key warning implementation planning: completed.
WP28C — MVP Scrub Key warning/acknowledgement UI implementation: implemented; blocked awaiting coordinator/user evidence.
WP28C-VERIFY — status checks attempted; Actions/HF sync unknown because connector returned no workflow runs/statuses.
WP29 — Scrub Key secure import/export tests: completed.
WP29B — Scrub Key import/export edge-case hardening: completed.
WP29C — Scrub Key warning UI regression test scaffolding: completed.
```

WP28C files added/changed:

```text
fix_streamlit_pdf_text_reinsert.py
tests/test_scrub_key_warning_acknowledgement_ui.py
RELEASE_NOTES.md
CHANGELOG.md
WORKPACKAGES.md
RISK_REGISTER.md
workpackage_claims/WP28C_mvp_scrub_key_warning_acknowledgement_ui.md
handover/workpackages/20260612_1545_mvp_scrub_key_warning_acknowledgement_ui.md
```

WP28C summary:

- Added MVP warning and acknowledgement gating for Scrub Key export/import, pasted-text reinsert, TXT reinsert, DOCX reinsert, PDF-to-TXT reinsert and restored-output downloads.
- Preserved Scrub Key JSON content, import behavior, reinsert helper behavior, restored output bytes, filenames and MIME types after acknowledgement.
- Added static regression tests for warning copy, acknowledgement keys, disabled buttons and non-change boundaries.
- No Scrub Key schema migration, encryption, automatic deletion, expiry blocking, hidden recovery, dependency change, real data or cloud processing was added.

WP28C-VERIFY findings:

- `get_commit_combined_status` returned no statuses for the WP28C final claim commit.
- `fetch_commit_workflow_runs` returned no workflow runs for the WP28C final claim commit.
- `get_commit_combined_status` returned no statuses for the WP28C-VERIFY claim commit.
- `fetch_commit_workflow_runs` returned no workflow runs for the WP28C-VERIFY claim commit.
- Therefore Actions and Hugging Face sync cannot be verified by this worker.
- App verification must wait until Actions and sync evidence is available.

Next Scrub Key step:

```text
Coordinator/user evidence needed — provide GitHub Actions and Hugging Face sync result for the WP28C commits. If green, perform app verification for the WP28C warning/acknowledgement UI.
```

Do not start further Scrub Key UI implementation until WP28C verification status is known.

## Completed recall/trust line

```text
WP19 — Recall benchmark specification.
WP20 — Synthetic messy Dutch legal/zorg benchmark corpus.
WP21 — Gold-label entity schema.
WP22 — Recall/precision test runner.
WP23 — Entity-class scorecard in CI.
WP24 — False-negative residual-risk report.
```

Remaining future work: complete gold-label sidecars, recognizer-backed baselines, approved thresholds and user-facing audit integration.

## Placeholder robustness line

```text
WP30 — Placeholder robustness review.
WP31 — LLM-resistant placeholder format proposal.
WP32 — Placeholder checksum/validation helper.
WP33 — Placeholder audit hardening.
WP34 — Synthetic AI-output placeholder corruption tests.
```

The placeholder robustness line is complete through synthetic AI-output corruption tests. Do not start robust placeholder generation, placeholder migration or Scrub Key schema work without a separate approved gated package.

## Local runtime line

```text
WP45 — Local runtime architecture plan.
WP46 — Minimal local Streamlit launcher.
WP47 — Local file handling/privacy test.
WP48 — Portable Windows proof of concept.
```

Next local-runtime step:

```text
WP49 — Desktop packaging decision
```

Only start WP49 after WP48 CI/status is acceptable and the coordinator confirms this line should continue before other risk lines.

## Active / next recommended execution queue

```text
1. Coordinator/user evidence needed for WP28C Actions/HF sync and app verification.
2. WP49 — Desktop packaging decision, only if the coordinator chooses to continue the local-runtime line.
```

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
