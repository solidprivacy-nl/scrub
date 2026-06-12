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
WP35 — DOCX hidden content risk review: completed document-hygiene/specification-only.
WP45 — Local runtime architecture plan: completed architecture/specification-only.
WP46 — Minimal local Streamlit launcher: completed minimal local runtime implementation.
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

WP28B artifacts:

```text
SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md
handover/workpackages/20260612_1415_scrub_key_warning_implementation_planning.md
```

WP28B summary:

- Translated WP27 warning UX and WP28 expiry/delete policy into exact future implementation locations, acknowledgement states and Dutch copy inventory.
- Mapped warning placement to the current Streamlit patch surface: `review_summary_block`, `scrub_key_import_ui_block`, `two_mode_selection_block`, `reinsert_ui_block`, `txt_reinsert_ui_block`, `docx_reinsert_ui_block` and future PDF-to-TXT reinsert scope.
- Defined MVP acknowledgement states for Scrub Key export/import, pasted-text reinsert, TXT reinsert, DOCX reinsert, PDF-to-TXT reinsert if present, and restored output downloads.
- Defined guidance-only MVP warnings for Downloads/local storage, shared-computer risk, expiry/delete guidance, loss-of-key, DOCX/PDF limitations and audit mismatch guidance.
- Defined later blocking candidates without implementing blocking.
- No UI implementation, Streamlit patch, helper logic, schema migration, import/export behavior change, reinsert behavior change, encryption, automatic deletion, expiry blocking, dependency change, real data or cloud processing was added.

WP29 artifacts:

```text
tests/test_scrub_key_secure_import_export.py
handover/workpackages/20260612_0000_scrub_key_secure_import_export_tests.md
handover/workpackages/20260612_0715_scrub_key_secure_import_export_tests_closeout.md
handover/workpackages/20260612_1330_scrub_key_secure_import_export_edge_case_hardening.md
```

WP29B files changed:

```text
scrub_key.py
tests/test_scrub_key_secure_import_export.py
```

WP29 / WP29B summary:

- WP29 added focused secure import/export tests for the current Scrub Key helper surface.
- WP29B expanded edge-case coverage for missing schema marker, unsupported schema version, empty/no-usable mappings, not-found placeholder audit behavior and validation-error non-leakage.
- WP29B added a minimal validation hardening so unsupported `schema_version` values are reported instead of accepted.
- No encryption, automatic deletion, expiry enforcement, Scrub Key schema migration, UI change, export/reinsert semantic change, dependency change, real data or cloud processing was added.

Next recommended Scrub Key step:

```text
WP28C — MVP Scrub Key warning/acknowledgement UI implementation
```

Alternative if the coordinator wants more test scaffolding before UI work:

```text
WP29C — Scrub Key warning UI regression test scaffolding
```

## Placeholder robustness line

```text
WP30 — Placeholder robustness review: completed architecture/specification-only.
WP31 — LLM-resistant placeholder format proposal: completed architecture/proposal-only.
WP32 — Placeholder checksum/validation helper: completed helper/tests-only.
WP33 — Placeholder audit hardening: completed audit/helper hardening-only.
```

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

## Active / next recommended execution queue

The next recommended workpackage from the Scrub Key security line is:

```text
WP28C — MVP Scrub Key warning/acknowledgement UI implementation
```

Alternative Scrub Key test scaffolding package:

```text
WP29C — Scrub Key warning UI regression test scaffolding
```

The next recommended workpackage from the placeholder robustness line is:

```text
WP34 — Synthetic AI-output placeholder corruption tests
```

The next recommended workpackage from the local-runtime line is:

```text
WP47 — Local file handling/privacy test
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

Validation expectations:

```text
pytest tests/test_scrub_key_ui_patch.py
pytest tests/test_two_mode_ui_patch.py
pytest tests/test_txt_reinsert_ui_patch.py
pytest tests/test_docx_reinsert_ui_patch.py
pytest tests -k "scrub_key or reinsert"
```

Because WP28C changes UI behavior, app verification is required after GitHub Actions and Hugging Face sync are green.

### WP29C — Scrub Key warning UI regression test scaffolding

Type: test scaffolding only.

Purpose:

- Add tests that lock down the warning-copy and acknowledgement requirements from `SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md` before WP28C implementation.
- Keep behavior unchanged.

Allowed direction:

- Tests only.
- No UI implementation.
- No helper logic.
- No schema/import/export/reinsert behavior changes.

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
