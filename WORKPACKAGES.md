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
WP36A — DOCX residual placeholder and comments risk triage completed.
WP37 — Headers/footers/comments/tracked-changes extraction helper completed.
WP45-WP49 — local runtime line completed through desktop packaging decision.
WP50 — Pilot design Legal vs Zorg completed planning-only with artifact limitation.
WP51 — ICP and pricing hypothesis completed business/design/documentation-only.
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

## DOCX hygiene line

```text
WP35 — DOCX hidden content risk review.
WP36A — DOCX residual placeholder and comments risk triage.
WP37 — Headers/footers/comments/tracked-changes extraction helper.
```

Next DOCX hygiene step:

```text
WP38 — DOCX hygiene audit report
```

Blocked until separate approval:

```text
WP36 — DOCX metadata cleaner helper
```

## Local runtime line

```text
WP45 — Local runtime architecture plan.
WP46 — Minimal local Streamlit launcher.
WP47 — Local file handling/privacy test.
WP48 — Portable Windows proof of concept.
WP49 — Desktop packaging decision.
```

Next local-runtime step:

```text
WP48B or WP49B only if coordinator approves a concrete packaging proof.
```

## Pilot validation line

```text
WP50 — Pilot design Legal vs Zorg.
WP51 — ICP and pricing hypothesis.
```

WP51 files added/changed:

```text
ICP_AND_PRICING_HYPOTHESIS.md
WORKPACKAGES.md
CHANGELOG.md
RISK_REGISTER.md
workpackage_claims/WP51_icp_and_pricing_hypothesis.md
handover/workpackages/20260612_1815_icp_and_pricing_hypothesis.md
```

WP51 summary:

- Defined first ICP hypothesis for Scrub Legal and Scrub Zorg.
- Compared Legal and Zorg users, buyers, approvers/blockers, workflows, willingness-to-pay drivers and risks.
- Compared demo/discovery, paid pilot, consultancy-assisted pilot, subscription, local desktop license and enterprise/support models.
- Recommended consultancy-assisted paid pilot as the first paid-offer hypothesis.
- Recorded what must not be sold or claimed yet, including full automation, production certification, complete anonymization without review, complete hidden-content handling, OCR/restored-PDF output and guaranteed detection.
- No sales campaign, customer outreach, code, UI, runtime behavior or cloud document processing was added.

Next pilot-validation step:

```text
WP52 — Pilot intake and NDA process
```

## Active / next recommended execution queue

```text
1. Coordinator/user evidence needed for WP28C Actions/HF sync and app verification.
2. WP38 — DOCX hygiene audit report, if coordinator wants to continue DOCX hygiene line.
3. WP52 — Pilot intake and NDA process, if coordinator wants to continue pilot-validation line.
4. WP48B or WP49B — only if coordinator approves a concrete packaging proof.
```

## Blocked work

Do not start yet without separate approval:

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
- MSI implementation.
- PyInstaller/Tauri/Electron implementation.
- Production installer claim.
