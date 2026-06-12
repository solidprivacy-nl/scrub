# Changelog — SolidPrivacy Scrub

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
- Tests assert that malformed, truncated, integrity-failed and unknown placeholder-like tokens are reported without repair or guessing.
- Tests confirm existing legacy reinsert still restores exact preserved placeholders.
- The fixture states that it is synthetic and uses no real personal data.

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
- Active non-placeholder next step remains `WP28C — MVP Scrub Key warning/acknowledgement UI implementation` or `WP47 — Local file handling/privacy test`, depending on coordinator priority.

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

## WP29-CLOSEOUT — Scrub Key secure import/export tests closeout

Status: completed documentation/status closeout after PR/Actions verification.

Purpose:

- Close out WP29 after PR #2 was merged into `main` and GitHub Actions passed.
- Record that WP29 added secure import/export regression tests for the current Scrub Key helper surface.
- Move the Scrub Key security line to `WP28B — Scrub Key warning implementation planning`, with `WP29B — Scrub Key import/export edge-case hardening` as an alternative.

Files added:

- `handover/workpackages/20260612_0715_scrub_key_secure_import_export_tests_closeout.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

WP29 artifacts recorded:

- `tests/test_scrub_key_secure_import_export.py`
- `handover/workpackages/20260612_0000_scrub_key_secure_import_export_tests.md`

Main closeout points:

- WP29 is completed helper/tests-only after PR/Actions verification.
- The tests cover deterministic Scrub Key JSON export, required policy markers, valid import/reload warning and result shape, malformed JSON, non-object JSON, missing required item fields, invalid `items` structure, wrong privacy/reversible/excluded-row policy markers, duplicate placeholder tampering, unknown placeholder mismatch, old timestamp non-blocking behavior, no hidden recovery/deletion/expiry state, no-mutation behavior, local deterministic no-AI/no-cloud reinsert behavior and synthetic-only examples.
- PR #2 merged the WP29 test and handover into `main`.
- GitHub Actions for PR #2 passed before merge.
- No helper logic, UI, Scrub Key schema, import/export behavior, reinsert behavior, encryption, automatic deletion, expiry blocking, dependency, real-data or cloud-processing changes were made.

Validation status:

- GitHub Actions: green for WP29 PR #2 / head commit `88759004ae534b73d0af63f7ff3c214832dd8e58`.
- PR merge commit recorded by GitHub: `e1f23c6565e271e702fea17934f1a4f81711db30`.
- No local pytest was run in ChatGPT web/GitHub connector environment.
- This closeout is documentation/status only.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No code changed.
- No tests changed in this closeout.
- No helper logic changed.
- No Streamlit UI changed.
- No Scrub Key schema migration.
- No import/export behavior change.
- No reinsert behavior change.
- No encryption implemented.
- No automatic deletion implemented.
- No expiry blocking implemented.
- No dependency change.
- No real data added.
- No cloud processing added.
- No roadmap change because strategy and phase order did not change.

Next recommended step:

- `WP28B — Scrub Key warning implementation planning`.
- Alternative if the security-test line should continue first: `WP29B — Scrub Key import/export edge-case hardening`.

## WP33-CLOSEOUT — Placeholder audit hardening central docs repair

Status: completed documentation/coordination-only.

Purpose:

- Complete central documentation for WP33 after the audit helper and tests were added.
- Record the additive placeholder audit hardening status without changing code, tests, UI, reinsert, export or Scrub Key schema behavior.
- Move the placeholder robustness line to WP34.

Files added:

- `handover/workpackages/20260612_0105_placeholder_audit_hardening_closeout.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

WP33 artifacts recorded:

- `placeholder_audit.py`
- `tests/test_placeholder_audit.py`
- `handover/workpackages/20260612_0045_unknown_changed_placeholder_audit_hardening.md`

Main closeout points:

- WP33 is completed audit/helper hardening only.
- The helper adds pure placeholder audit classification on top of WP32 validation.
- The helper classifies placeholder-like tokens without changing reinsert behavior.
- Existing legacy placeholder reinsert remains compatible.
- Unknown, malformed, truncated and failed-integrity placeholder-like tokens are made visible in helper audit output.
- Unknown/malformed tokens are not automatically repaired.
- No placeholder migration, robust placeholder generation, Scrub Key schema change, Streamlit UI change, export/reinsert behavior change, dependency change or AI/cloud processing was added.
- Only synthetic test values were used.

Validation status:

- Documentation/coordination repair only.
- Prior WP33 checks were recorded as passed: `python -m py_compile placeholder_validation.py placeholder_audit.py scrub_key.py scrub_key_reinsert.py tests/test_placeholder_audit.py`.
- Prior WP33 targeted pytest was recorded as passed: `PYTHONPATH=. pytest -q tests/test_placeholder_validation.py tests/test_placeholder_audit.py tests/test_scrub_key_reinsert.py` with 34 passed.
- Prior WP33 broader selected pytest was recorded as passed: `PYTHONPATH=. pytest -q tests -k "placeholder or scrub_key or reinsert"` with 34 passed.
- No code or test files were changed in this closeout.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No code changed.
- No tests changed.
- No placeholder migration.
- No robust placeholder generation in product flow.
- No Scrub Key schema migration.
- No reinsert behavior change.
- No Streamlit UI change.
- No export behavior change.
- No dependency change.
- No AI/cloud integration.
- No real data added.
- No roadmap change because strategy and phase order did not change.

Next recommended step:

- `WP34 — Synthetic AI-output placeholder corruption tests`.

## WP24 — False-negative residual-risk report

Status: completed report-only false-negative residual-risk report foundation.

Purpose:

- Make remaining false-negative and coverage risks explicit after WP19/WP20/WP21/WP22/WP23.
- Provide a report-only residual-risk helper for internal/support risk communication.
- Keep the work synthetic-only and avoid any production safety claim, threshold or gate.

Files added:

- `benchmark/build_residual_risk_report.py`
- `tests/test_residual_risk_report.py`
- `handover/workpackages/20260612_1300_false_negative_residual_risk_report.md`

Files changed:

- `benchmark/reports/README.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Added `benchmark/build_residual_risk_report.py`, a pure-stdlib report-only helper that consumes a WP23 scorecard or builds one through the existing WP22/WP23 helpers.
- The helper can write `benchmark/reports/false_negative_residual_risk_report.json` and `benchmark/reports/false_negative_residual_risk_report.md`.
- The report includes synthetic-only warning, report-only/no-production-safety policy, current benchmark coverage status, schema-example limitation, supplied-prediction limitation, overall false-negative risk, per-domain residual risk, per-entity-class residual risk, preserve-term risk, known-trap/false-positive risk, partial-overlap/near-miss diagnostics, unsupported/not-yet-baselined classes and recommended next work.
- The report explicitly records `thresholds_applied: false`, `production_gate: false` and `safe_for_production_claim: false`.
- Added `tests/test_residual_risk_report.py` for policy fields, coverage limitations, risk summaries, unsupported/not-yet-baselined classes, Markdown rendering and output writing.
- Updated `benchmark/reports/README.md` to document generated residual-risk report artifacts and the no-real-data/no-production-claim boundary.

Validation status:

- `python -m py_compile benchmark/build_residual_risk_report.py` passed in the ChatGPT execution sandbox against the authored helper.
- `pytest -q tests/test_residual_risk_report.py` passed in the ChatGPT execution sandbox against the authored tests: 4 passed.
- `pytest tests/test_recall_precision_runner.py` and `pytest tests/test_entity_scorecard.py` were requested but could not be run in a live GitHub checkout through the ChatGPT GitHub connector.
- `python -m json.tool benchmark/gold/schema/gold_label_schema.json` was requested but could not be run in a live GitHub checkout through the ChatGPT GitHub connector. The schema was fetched and inspected through GitHub.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No recognizer logic changed.
- No Presidio integration changed.
- No Streamlit UI changed.
- No recall/precision threshold added.
- No production-blocking gate added.
- No production safety claim added.
- No dependency changes.
- No export/reinsert behavior changed.
- No real data added.
- No cloud processing added.

Next recommended step:

- `WP29 — Scrub Key secure import/export tests`.

## Earlier completed work

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
