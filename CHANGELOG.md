# Changelog — SolidPrivacy Scrub

## WP32-CLOSEOUT — Placeholder validation helper central docs repair

Status: completed documentation/coordination-only.

Purpose:

- Complete central documentation for WP32 after the helper and tests were added.
- Record the additive placeholder validation helper status without changing code, tests, UI, reinsert, export or Scrub Key schema behavior.
- Move the placeholder robustness line to WP33.

Files added:

- `handover/workpackages/20260612_0030_placeholder_validation_helper_closeout.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

WP32 artifacts recorded:

- `placeholder_validation.py`
- `tests/test_placeholder_validation.py`
- `handover/workpackages/20260612_0015_placeholder_checksum_validation_helper.md`

Main closeout points:

- WP32 is completed helper/tests-only.
- The helper recognizes and validates the future robust placeholder form `[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]`.
- The helper parses entity type, counter and integrity token.
- The helper generates deterministic integrity tokens from non-sensitive placeholder metadata.
- Integrity tokens are not derived directly from original sensitive values.
- Legacy placeholders remain a separate compatibility mode.
- No placeholder migration, robust placeholder generation, Scrub Key schema change, reinsert behavior change, UI/export/dependency change or AI/cloud processing was added.

Validation status:

- Documentation/coordination repair only.
- Prior WP32 targeted checks were recorded as passed: `python -m py_compile placeholder_validation.py tests/test_placeholder_validation.py` and `PYTHONPATH=. pytest tests/test_placeholder_validation.py -q` with 12 passed.
- The broader command `pytest tests -k "placeholder or scrub_key or reinsert"` was not run in the prior WP32 worker because a full repository checkout was unavailable in the ChatGPT runtime.
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

- `WP33 — Unknown/changed placeholder audit hardening`.

## WP22 — Recall/precision test runner

Status: completed report-only benchmark runner implementation.

Purpose:

- Make synthetic benchmark detection quality measurable after WP19/WP20/WP21.
- Add a deterministic local runner for WP21 gold-label sidecars and supplied prediction JSON.
- Keep the first runner report-only with no recognizer logic changes, no Streamlit UI changes, no CI gate and no production-blocking threshold.

Files added:

- `benchmark/run_recall_precision.py`
- `tests/test_recall_precision_runner.py`
- `handover/workpackages/20260612_1200_recall_precision_test_runner.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Added `benchmark/run_recall_precision.py`, a pure-stdlib deterministic runner.
- The runner loads WP21 sidecars, validates `synthetic: true`, verifies source file references and checks `text == source_text[start:end]` for labels, preserve terms and known traps.
- The runner accepts optional prediction JSON and reports exact and value-normalized recall/precision.
- Metrics include overall summary, per-domain metrics, per-entity-class metrics, false negatives, false positives, preserve-term failures, known-trap failures and diagnostic-only partial overlaps.
- Partial overlap is explicitly diagnostic-only and does not hide false negatives.
- Schema-example sidecars are included by default with warnings so current examples can be used for runner validation without implying full benchmark coverage.
- Added `tests/test_recall_precision_runner.py` covering exact/normalized scoring, preserve/trap failure reporting, malformed gold-label offset rejection and CLI JSON output.

Validation status:

- `python -m py_compile benchmark/run_recall_precision.py` passed in the ChatGPT execution sandbox against the authored runner.
- `pytest -q tests/test_recall_precision_runner.py` passed in the ChatGPT execution sandbox against the authored tests: 3 passed.
- `python -m json.tool benchmark/gold/schema/gold_label_schema.json` was requested; the schema was fetched and inspected through GitHub, but the GitHub connector does not provide a shell in the repository checkout. The runner itself parses JSON sidecars with Python stdlib.
- GitHub Actions: to be checked after final handover commit.
- Hugging Face sync: to be checked after final handover commit.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No recognizer logic changed.
- No Presidio integration changed.
- No Streamlit UI changed.
- No CI scorecard or production test gate added.
- No production-blocking threshold added.
- No dependency changes.
- No export/reinsert behavior changed.
- No real data added.
- No cloud processing added.

Next recommended step:

- `WP23 — Entity-class scorecard in CI`.

## WP28-REPAIR — Scrub Key expiry/delete policy artifact repair

Status: completed documentation-repair-only.

Purpose:

- Verify that the completed WP28 central documentation is backed by the required policy artifact.
- Confirm that `SCRUB_KEY_EXPIRY_DELETE_POLICY.md` is present and covers the required expiry, retention and deletion policy topics.
- Create a repair handover for the artifact consistency check.

Files added:

- `handover/workpackages/20260611_2135_scrub_key_expiry_delete_policy_repair.md`

Files changed:

- `CHANGELOG.md`

Files verified:

- `SCRUB_KEY_EXPIRY_DELETE_POLICY.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Validation status:

- Documentation/artifact repair review only.
- `SCRUB_KEY_EXPIRY_DELETE_POLICY.md` is present at the expected path.
- Policy coverage was checked against the WP28 required topics and aligned with WP25, WP26, WP27, `SCRUB_KEY_SPEC.md`, WP58, `RISK_REGISTER.md` and `DECISION_LOG.md`.
- No tests run; no code or test files were changed.
- App verification: not applicable because no UI changed.

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
- No cloud processing added.

Next recommended step:

- `WP29 — Scrub Key secure import/export tests`.
- Alternative if warning implementation planning should precede tests: `WP28B — Scrub Key warning implementation planning`.

## WP21-CLOSEOUT — Gold-label schema handover and central docs repair

Status: completed documentation/schema-closeout-only.

Purpose:

- Complete WP21 closeout after the gold-label schema artifact was created.
- Verify that `benchmark/gold/schema/gold_label_schema.json` covers the required sidecar schema concepts.
- Repair central status documentation and create the missing handover.

Files added:

- `handover/workpackages/20260610_1900_gold_label_entity_schema_closeout.md`

Files changed:

- `benchmark/gold/README.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Schema artifact verified:

- `benchmark/gold/schema/gold_label_schema.json`

Verification summary:

- The schema covers gold-label sidecar format, zero-based character offsets, inclusive `start` and exclusive `end`, source file reference, canonical entity class mapping, label ID, entity ID, expected text span, normalization guidance, preserve-term labels, known-trap labels, partial-overlap guidance, validation expectations and future WP22 runner expectations.
- The schema aligns with the canonical entity classes in `RECALL_BENCHMARK_SPEC.md`.
- `benchmark/gold/README.md` now reflects WP21 schema foundation status instead of WP20 future-schema placeholder language.
- No schema defect was found, so `benchmark/gold/schema/gold_label_schema.json` was intentionally not modified.

Validation status:

- Documentation/schema closeout review only.
- `python -m json.tool benchmark/gold/schema/gold_label_schema.json` passed in the prior closeout worker environment.
- Required benchmark context files were read.
- No tests run; no code or test files were changed.
- App verification: not applicable because no UI changed.

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

Next recommended step:

- `WP22 — Recall/precision test runner`.

## WP28 — Scrub Key expiry/delete policy

Status: completed security/lifecycle-policy-only.

Purpose:

- Define expiry, retention and deletion policy for Scrub Keys after the warning UX plan.
- Clarify user-controlled deletion, matter/project retention guidance, Downloads/shared-computer risk, loss-of-key consequences, tampering/mismatch consequences and audit expectations.
- Keep the package policy-only with no UI, deletion automation, schema migration, encryption or behavior changes.

Files added:

- `SCRUB_KEY_EXPIRY_DELETE_POLICY.md`
- `handover/workpackages/20260610_1826_scrub_key_expiry_delete_policy.md`

Files changed:

- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main policy decisions:

- Scrub Keys should be retained only as long as needed for a specific matter, project, AI roundtrip, review or reinsert purpose.
- MVP expiry is guidance-only; Scrub must not add expiry metadata, block import by age or automatically delete old keys.
- Deletion must remain explicit and user-controlled.
- Scrub must not silently delete Scrub Keys, mappings, restored output, audit context, browser Downloads files, synced copies, backups or future app-managed vault entries.
- Scrub must not keep hidden recovery copies.
- Future app-managed deletion, expiry reminders, protected storage, encrypted containers, vault behavior and recovery/escrow require separate approved implementation workpackages.
- Dutch user-facing policy copy examples are included for future warning/planning work.

Validation status:

- Documentation/security lifecycle-policy review only.
- Required control files plus Scrub Key context files were read.
- Context-only helper/UI files were inspected.
- No tests run; no code or test files were changed.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No UI implementation.
- No Streamlit patch changed.
- No helper logic changed.
- No automatic deletion.
- No Scrub Key JSON schema migration.
- No encryption implementation.
- No import/export behavior changed.
- No reinsert behavior changed.
- No tests added or changed.
- No dependencies changed.
- No secrets or real data stored.
- No cloud processing added.

Next recommended step:

- `WP29 — Scrub Key secure import/export tests`.
- Alternative if UI planning should precede tests: `WP28B — Scrub Key warning implementation planning`.

## WP46 — Minimal local Streamlit launcher

Status: completed minimal local runtime implementation.

Purpose:

- Add the smallest safe local launcher path recommended by WP45.
- Allow a developer/user to run the existing Streamlit app locally for non-cloud confidential-processing validation.
- Document local setup, launch command, local-only warnings and current limits without changing app behavior.

Files added:

- `scripts/run_local_streamlit.py`
- `LOCAL_RUN.md`
- `handover/workpackages/20260610_1828_minimal_local_streamlit_launcher.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main changes:

- Added a minimal Python launcher that runs the existing startup patch scripts and then starts `presidio_streamlit.py` through Streamlit.
- The launcher binds to `127.0.0.1` by default, uses port `8501` by default and disables Streamlit usage stats for this local launcher path.
- Added local run documentation covering Python setup, dependency installation, exact launch command, local-only warning, no-real-data-in-repo warning, locally processed files, current non-guarantees and the next validation step.

Validation status:

- `python -m py_compile scripts/run_local_streamlit.py` passed in the implementation worker environment.
- Full app launch was not run.
- App verification: not applicable because no UI feature changed.

Intentionally not changed:

- No installer.
- No PyInstaller packaging.
- No Tauri/Electron implementation.
- No Docker startup change.
- No Streamlit UI feature change.
- No export/reinsert behavior change.
- No dependency change.
- No telemetry implementation.
- No cloud processing added.
- No real data added.

Next recommended step:

- `WP47 — Local file handling/privacy test`.

## WP31 — LLM-resistant placeholder format proposal

Status: completed architecture/proposal-only.

Purpose:

- Propose and compare placeholder formats that are more resistant to AI rewriting, translation, summarization and formatting changes.
- Select a future robust placeholder direction without implementing migration or changing reinsert behavior.
- Define compatibility, validation and phased implementation requirements after WP30.

Files added:

- `PLACEHOLDER_FORMAT_PROPOSAL.md`
- `handover/workpackages/20260610_0035_placeholder_format_proposal.md`
- `handover/workpackages/20260610_1824_placeholder_format_proposal.md`

Files changed:

- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main proposal decisions:

- Recommended future format direction: `[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]`.
- Example: `[[SP_PERSON_0001_A7F3]]`.
- Legacy placeholders such as `[PERSOON_1]` remain backward-compatible.
- Future robust support should be additive first and must not silently replace legacy placeholders.
- Visible checksum/integrity values must not be derived directly from original sensitive data.
- WP32 should implement validation/checksum helpers before any generation, migration or schema change.

Validation status:

- Documentation/architecture review only.
- Required context files were read.
- No tests run; no code or test files were changed.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No placeholder migration.
- No reinsert helper change.
- No Scrub Key schema change.
- No UI change.
- No export behavior change.
- No tests added or changed.
- No AI/cloud integration.
- No dependencies changed.

Next recommended step:

- `WP32 — Placeholder checksum/validation helper`.

## Earlier completed work

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
- Earlier UI, PDF helper, Scrub Key, reinsert and Review UX work as recorded in repository history.
