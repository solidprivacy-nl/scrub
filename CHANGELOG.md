# Changelog — SolidPrivacy Scrub

## WP47 — Local file handling/privacy test

Status: completed local runtime privacy validation.

Purpose:

- Validate the WP46 minimal local Streamlit launcher against local-runtime privacy expectations.
- Make the Hugging Face demo boundary and local runtime limitations explicit in `LOCAL_RUN.md`.
- Keep the work test/documentation-only: no UI behavior, upload/download/export/reinsert semantics, cloud processing, telemetry or packaging changes.

Files added:

- `tests/test_local_file_handling_privacy.py`
- `handover/workpackages/20260612_1500_local_file_handling_privacy_test.md`

Files changed:

- `LOCAL_RUN.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Added static/monkeypatch tests for `scripts/run_local_streamlit.py`.
- Tests verify default loopback binding `127.0.0.1`, default port `8501`, `--browser.gatherUsageStats false`, no cloud/AI/telemetry endpoints in launcher arguments, and no document content or synthetic filenames in launcher command arguments.
- Tests verify the launcher source does not write logs, create temp files, open files, or introduce installer/packaging behavior.
- Tests verify `LOCAL_RUN.md` documents Hugging Face demo boundaries, local-only limitations, no-real-data rules, temp/runtime expectations, no telemetry/cloud-processing claim and no installer/packaging claim.
- Updated `LOCAL_RUN.md` with explicit Hugging Face demo warning, runtime privacy expectations, temporary/runtime file expectations and no-telemetry/no-cloud-processing clarification.

Validation status:

- `python -m py_compile scripts/run_local_streamlit.py` passed in the ChatGPT execution sandbox against the authored files. The sandbox emitted an unrelated spreadsheet runtime warmup warning before Python execution, but the command returned success.
- `pytest -q tests/test_local_file_handling_privacy.py` passed in the ChatGPT execution sandbox against the authored tests: 6 passed.
- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository. GitHub Actions should validate the committed final files.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

- No Streamlit UI changed.
- No upload/download/export/reinsert semantics changed.
- No cloud document processing added.
- No telemetry added.
- No installer/packaging added.
- No Docker/Hugging Face startup behavior changed.
- No dependency changes.
- No real data added.

Next recommended step:

- `WP48 — Portable Windows proof of concept`, only if the coordinator wants to continue the local-runtime line after CI/status is acceptable.
- Other active risk-line option: `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`.

## WP28B — Scrub Key warning implementation planning

Status: completed UI/security implementation-planning-only.

Purpose:

- Translate WP27 Scrub Key warning UX and WP28 expiry/delete policy into exact future implementation locations before editing Streamlit UI.
- Define MVP warning and acknowledgement placement for Scrub Key creation, export/download, import/reload, reinsert mode and restored output downloads.
- Preserve existing Scrub Key schema, helper logic, import/export behavior, reinsert behavior, encryption/deletion/expiry boundaries and UI behavior.

Files added:

- `SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md`
- `handover/workpackages/20260612_1415_scrub_key_warning_implementation_planning.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Added a UI/security implementation plan for future MVP Scrub Key warnings and acknowledgements.
- Mapped warning placement to current Streamlit patch locations.
- Defined Dutch copy inventory for Scrub Key creation, export/download, import/reload, reinsert, restored output downloads, Downloads/local storage, shared-computer risk, e-mail/AI upload risk, loss-of-key and tampering/mismatch warnings.
- Defined MVP acknowledgement states and later blocking candidates without implementing blocking.

Validation status:

- Documentation/planning-only.
- No tests were run because no code, tests, UI, helper, dependency or behavior changed.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No UI implementation.
- No Streamlit patch change.
- No helper logic change.
- No tests changed.
- No Scrub Key schema migration.
- No import/export behavior change.
- No reinsert behavior change.
- No encryption implementation.
- No automatic deletion implementation.
- No expiry blocking.
- No hidden recovery.
- No dependency change.
- No real data added.
- No cloud processing added.
- No roadmap change because strategy and phase order did not change.

Next recommended step:

- `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`.
- Alternative if the coordinator wants tests before UI edits: `WP29C — Scrub Key warning UI regression test scaffolding`.

## WP34 — Synthetic AI-output placeholder corruption tests

Status: completed synthetic fixtures/tests-only.

Purpose:

- Add synthetic AI-output-style placeholder corruption fixtures and tests after WP33.
- Cover translation, summarization/deletion, markdown/HTML, spacing, punctuation, truncation, integrity failure and placeholder deletion/merge scenarios.
- Keep the work synthetic-only and report/audit focused without changing product behavior.

Files added:

- `tests/fixtures/placeholder_corruption/ai_output_corruption_cases.json`
- `tests/test_placeholder_corruption_scenarios.py`
- `handover/workpackages/20260612_0140_synthetic_ai_placeholder_corruption_tests.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Added a synthetic fixture set with expected placeholders and corrupted AI-output-style examples.
- Added tests for exact legacy placeholder preservation with punctuation, translated placeholder label, summarization/deletion, markdown/HTML wrapping, HTML split token, spacing mutation, robust placeholder truncation, robust integrity mismatch, placeholder merge/deletion and invented curly placeholder-like token.
- Tests assert that missing expected placeholders remain visible through `placeholder_audit.audit_placeholders`.
- Tests confirm existing legacy reinsert still restores exact preserved placeholders.

Validation status:

- `python -m py_compile placeholder_validation.py placeholder_audit.py scrub_key.py scrub_key_reinsert.py tests/test_placeholder_corruption_scenarios.py` passed in the ChatGPT execution sandbox against the authored fixture/test draft.
- `PYTHONPATH=. pytest -q tests/test_placeholder_corruption_scenarios.py` passed in the ChatGPT execution sandbox against the authored WP34 test draft: 11 passed.
- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector. GitHub Actions should validate the committed final files.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No helper logic changed.
- No Streamlit UI changed.
- No export behavior changed.
- No reinsert behavior changed.
- No Scrub Key schema migration.
- No placeholder migration.
- No robust placeholder generation in product flow.
- No dependency change.
- No real data added.
- No AI/cloud integration.

Next recommended step:

- Placeholder robustness line: later gated robust placeholder generation and compatibility implementation only after schema/format policy is explicitly approved.

## WP29B — Scrub Key import/export edge-case hardening

Status: completed helper/tests-only edge-case validation hardening.

Purpose:

- Extend the already-completed WP29 secure import/export regression coverage for the current Scrub Key helper surface.
- Make unsupported Scrub Key schema versions visible as validation issues.
- Preserve existing Scrub Key schema, UI, import/export behavior and reinsert behavior.

Files changed:

- `scrub_key.py`
- `tests/test_scrub_key_secure_import_export.py`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `CHANGELOG.md`

Files added:

- `handover/workpackages/20260612_1330_scrub_key_secure_import_export_edge_case_hardening.md`

Main changes:

- `validate_scrub_key` now reports unsupported `schema_version` values instead of accepting any non-empty version marker.
- Expanded `tests/test_scrub_key_secure_import_export.py` with coverage for missing schema marker, unsupported schema version, empty/no-usable mappings, tampered item count, unknown placeholder and not-found placeholder audit behavior, validation error non-leakage and valid synthetic roundtrip.
- Kept old timestamp behavior guidance-only: old keys are not expiry-blocked or deleted by helpers.
- Confirmed helpers do not add hidden recovery, deletion or expiry state.
- Confirmed reinsert remains deterministic, local-only, no-AI and no-cloud for valid synthetic keys.

Validation status:

- `python -m py_compile scrub_key.py scrub_key_import.py scrub_key_reinsert.py tests/test_scrub_key_secure_import_export.py` passed in the ChatGPT execution sandbox against the authored helper/test draft.
- `pytest -q tests/test_scrub_key_secure_import_export.py` passed in the ChatGPT execution sandbox against the authored WP29 edge-case test draft: 10 passed.
- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector. GitHub Actions should validate the committed final file.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No encryption implemented.
- No automatic deletion implemented.
- No expiry enforcement implemented.
- No Scrub Key schema migration.
- No Streamlit UI change.
- No import/export semantic change.
- No reinsert semantic change.
- No dependency change.
- No real data added.
- No cloud processing added.

Next recommended step:

- `WP28B — Scrub Key warning implementation planning`.

## Earlier completed work

- WP29-CLOSEOUT — Scrub Key secure import/export tests closeout.
- WP33-CLOSEOUT — Placeholder audit hardening central docs repair.
- WP24 — False-negative residual-risk report.
- WP23 — Entity-class scorecard in CI.
- WP32-CLOSEOUT — Placeholder validation helper central docs repair.
- WP22 — Recall/precision test runner.
- WP28-REPAIR — Scrub Key expiry/delete policy artifact repair.
- WP21-CLOSEOUT — Gold-label schema handover and central docs repair.
- WP28 — Scrub Key expiry/delete policy.
- WP46 — Minimal local Streamlit launcher.
- WP31 — LLM-resistant placeholder format proposal.
- WP27 — Scrub Key warning UX plan.
- WP45 — Local runtime architecture plan.
- WP20 — Synthetic messy Dutch legal/zorg benchmark corpus.
- WP26 — Scrub Key encryption/lifecycle specification.
- WP58 — Parallel specification consolidation and next execution queue.
- WP35 — DOCX hidden content risk review.
- WP30 — Placeholder robustness review.
- WP25 — Scrub Key threat model.
- WP19 — Recall benchmark specification.
- WP18C — Add Codex worker governance instructions.
