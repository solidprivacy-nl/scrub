# Changelog — SolidPrivacy Scrub

This changelog records meaningful product, architecture, workflow and recognizer changes for the Scrub legal document scrubber.

Conventions:

- Keep this file explicit and human-readable.
- Group changes by project phase / version.
- Record what changed, why it changed, and what is intentionally not changed.
- Do not use this as a substitute for tests; every recognizer hardening step should also add or update regression tests.

---

## Current development rule

From v10 onward, recognizer work follows this order:

1. Add or update synthetic regression cases.
2. Add or update tests.
3. Change recognizer / scanner logic.
4. Verify GitHub Actions tests are green.
5. Let GitHub sync to Hugging Face automatically.
6. Test the app in Hugging Face.

For UI/UX-only work, prefer pure helper modules and tests before touching Streamlit UI flow.

---

## v12.6 — Export sanity checks UI integration

Status: UI integration implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Purpose:

- Show advisory export sanity warnings near the final review/download section.
- Make remaining review risk visible before the user downloads files.
- Preserve existing export/download behavior.
- Keep the warnings advisory only.

Files added or changed:

- `fix_streamlit_nested_expanders.py`
- `tests/test_export_sanity_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1445_v12_6_export_sanity_ui.md`

Main changes:

- Integrated the existing `export_sanity.py` helper into the Streamlit startup patch flow.
- Added UI text for `Extra exportcontrole` near the existing v12.5 `Eindcontrole vóór download` block.
- The UI can show advisory warnings for:
  - unchecked `Controle nodig` rows;
  - candidate rows not included;
  - no replacements selected;
  - user review still required;
  - export not guaranteeing full anonymization.
- Added a patch-level test file to guard that the export sanity helper is wired into the UI patch.

Testing and verification:

- `tests/test_export_sanity_ui_patch.py` was added.
- The WP3B worker could not run pytest locally from the connector environment.
- Earlier helper validation was reconciled by the coordinator: `Tests #58` green and `Sync to Hugging Face Space #72` green for commit `b0bf8ae`.
- GitHub Actions and Hugging Face sync for the UI integration commits still need coordinator verification.
- Hugging Face app verification is still required: confirm `Extra exportcontrole` appears before downloads and downloads remain available.

Intentionally not changed:

- No direct edit to `presidio_streamlit.py`.
- No export/download blocking.
- No change to which rows are included in export.
- No change to TXT, CSV, DOCX or PDF download logic.
- No Scrub Key logic added.
- No reinsert workflow added.
- No cloud processing introduced.

---

## WP Status Reconciliation — WP3/WP4 verification evidence

Status: reconciliation completed; GitHub Actions and Hugging Face sync could not be independently confirmed through the connector.

Purpose:

- Verify and reconcile status for:
  - v12.6 export sanity commits;
  - v13.0 Scrub Key commits, especially `d65364373e4d3612044d8688ac17e11de81c07e5`.
- Update project control files without changing code or UI behavior.

Recorded repo evidence:

- WP3 handover records local targeted validation:
  - `PYTHONPATH=. pytest -q tests/test_export_sanity.py tests/test_review_summary.py` → 12 passed.
- WP4 changelog records local targeted validation:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.

Intentionally not changed:

- No code files.
- No UI files.
- No tests.
- No export semantics.
- No Hugging Face app behavior.

---

## v13.0 — Scrub Key specification and pure model

Status: implemented; coordinator later showed `Tests #56` green and `Sync #70` green for commit `d653643`.

Purpose:

- Prepare the v13 Scrub Key / Reinsert phase without touching the active review UI.
- Define the local mapping file concept for future reversible workflows.
- Add a pure Python model with validation and JSON roundtrip support.
- Make pseudonymization safety boundaries explicit before UI/export work starts.

Files added or changed:

- `SCRUB_KEY_SPEC.md`
- `scrub_key.py`
- `tests/test_scrub_key.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1342_v13_0_scrub_key_spec_model.md`

Main changes:

- Added a Scrub Key specification for the future workflow:
  - `Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit`.
- Defined required mapping fields:
  - original value;
  - placeholder;
  - entity type;
  - user-facing type label;
  - source;
  - review status;
  - include state;
  - timestamp;
  - optional document/project/dossier label.
- Added required safety language explaining that a Scrub Key makes scrubbed text reversible.
- Explicitly classified the Scrub Key model as pseudonymization, not full anonymization.
- Added local/protected key handling guidance and external-AI sharing warning.
- Added deterministic pure helpers:
  - `build_scrub_key(rows, document_label=None)`;
  - `scrub_key_to_json(scrub_key)`;
  - `scrub_key_from_json(text)`;
  - `validate_scrub_key(scrub_key)`.
- Set the v13.0 excluded-row policy to `omitted`, so unchecked rows are not written into the key.
- Kept timestamp handling deterministic: the model does not create timestamps itself; validation catches missing timestamps.

Testing:

- Added `tests/test_scrub_key.py`.
- Local targeted validation passed: `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
- Coordinator evidence later confirmed GitHub Actions and Hugging Face sync green for `d653643`.

Intentionally not changed:

- No direct edit to `presidio_streamlit.py`.
- No direct edit to `fix_streamlit_nested_expanders.py` for v13.
- No export/download buttons for Scrub Key yet.
- No reinsert UI.
- No cloud processing.
- No secret storage.
- No real personal data in tests or examples.
- No change to active review UI or export semantics.

---

## v12.6 — Export sanity checks helper and tests

Status: helper implemented; coordinator reconciled helper verification as green before UI integration.

Purpose:

- Prepare advisory export sanity-check logic before UI integration.
- Warn users when review risk remains.
- Preserve existing export semantics and download behavior.

Files added or changed:

- `export_sanity.py`
- `tests/test_export_sanity.py`
- `WORKPACKAGES.md`
- `handover/workpackages/20260607_1405_v12_6_export_sanity_helper.md`

Main changes:

- Added pure helper logic for advisory export readiness checks.
- Added Dutch user-facing warning text for:
  - unchecked `Controle nodig` rows;
  - candidate rows not included;
  - no replacements selected;
  - user review still required;
  - export not guaranteeing full anonymization.
- Added readiness labels:
  - `Geen vervangregels gevonden — controleer handmatig`;
  - `Geen vervangingen geselecteerd`;
  - `Controle nodig vóór export`;
  - `Klaar voor export na gebruikerscontrole`.
- Explicitly preserved helper flags:
  - `blocks_export = False`;
  - `changes_export_semantics = False`.
- Reused review-summary normalization logic where helpful.

Testing:

- Added `tests/test_export_sanity.py`.
- Local targeted validation passed in the WP3 handover:
  - `PYTHONPATH=. pytest -q tests/test_export_sanity.py tests/test_review_summary.py` → 12 passed.
- Coordinator later reconciled helper verification: `Tests #58` green and `Sync to Hugging Face Space #72` green for commit `b0bf8ae`.

Intentionally not changed:

- No direct edit to `presidio_streamlit.py`.
- No direct edit to `fix_streamlit_nested_expanders.py` in the helper-only phase.
- No change to `review_summary.py`.
- No export/download blocking.
- No change to which rows are included in export.
- No Scrub Key or reinsert implementation.
- No LLM/cloud feature.

---

## v12.5 — Final review summary

Status: completed and app verified.

Purpose:

- Show final export readiness before downloads.
- Make export scope clear before the user downloads files.
- Warn when candidate rows still need attention.
- Preserve existing replacement and export semantics.

Files added or changed:

- `review_summary.py`
- `tests/test_review_summary.py`
- `tests/test_review_summary_ui_patch.py`
- `fix_streamlit_nested_expanders.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1345_v12_5_review_summary_closeout.md`

Main changes:

- Added a pure helper that accepts review rows as dictionaries or DataFrame-like records.
- Added summary counts for automatically detected rows, rows needing review, manual rows, remembered rows, checked rows, unchecked rows and open candidate warnings.
- Added conservative include-flag parsing for boolean, numeric and Dutch/string values.
- Added status inference from stable status values, Dutch status labels, source fields and manual/remembered entity markers.
- Added Dutch readiness labels and markdown summary lines.
- Integrated the summary into the existing startup UI patch so the app shows `Eindcontrole vóór download` immediately above the download section.
- Kept the summary advisory only: it displays counts and readiness labels but does not block or alter downloads.
- Formally closed v12.5 after coordinator/user verification.

Testing and verification:

- Added unit tests for `review_summary.py`.
- Added a UI patch contract test to verify that the summary helper is imported and displayed before downloads.
- Local targeted validation before UI integration passed: `PYTHONPATH=. pytest -q tests/test_review_summary.py` → 5 passed.
- Coordinator reported GitHub Actions tests green for the v12.5 review summary line.
- Coordinator reported GitHub to Hugging Face sync green for the v12.5 review summary line.
- Hugging Face app was visually verified and showed `Eindcontrole vóór download` before the download section.
- Downloads were reported as still working after verification: text, CSV, DOCX and PDF.

Intentionally not changed:

- No direct edit to `presidio_streamlit.py` during closeout.
- No recognizer changes.
- No entity-type expansion.
- No export/download blocking.
- No change to which rows are included in export.
- No Scrub Key or reinsert implementation.
- No LLM/cloud feature.

---

## v12.4 — Review guidance text

Status: implemented; GitHub Actions and Hugging Face sync confirmed green by coordinator; app visually confirmed by user.

Purpose:

- Make the review workflow self-explanatory for non-technical legal users.
- Explain that only checked rows are included in export.
- Explain that `Controle nodig` rows require manual review.
- Explain that the focus filter is a viewing aid, not the export scope.
- Explain that technical details are mainly for audit/debugging.
- Add AI-use guidance: scrub first, then use AI.

Files added or changed:

- `review_guidance.py`
- `tests/test_review_guidance.py`
- `fix_streamlit_nested_expanders.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main changes:

- Added short Dutch review guidance strings.
- Added markdown helper for guidance bullets.
- Patched the review flow to show guidance near the replacement table and export step.
- Kept the guidance advisory only; it does not alter replacement selection or export behavior.

Testing:

- Added unit tests for guidance text coverage.
- User visually confirmed the guidance block appeared correctly in Hugging Face.
- Coordinator confirmed latest Actions and Hugging Face sync green for the helper/governance commits through `fffd27b`.

Intentionally not changed:

- No recognizer changes.
- No export semantics change.
- No desktop/MSI work.
- No LLM/cloud feature.

---

## Project governance setup

Status: implemented; Actions/sync confirmed green by coordinator through latest governance/helper handover commits.

Purpose:

- Make GitHub the operational source of truth for SolidPrivacy Scrub workpackages.
- Establish a central project prompt, roadmap, workpackage plan and handover convention.
- Prepare continuation across fresh chats/workers.

Files added or changed:

- `PROJECT_PROMPT.md`
- `PROJECT_PROMPT_SHORT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `handover/workpackages/20260607_1057_project_prompt_governance_handover.md`

Main changes:

- Added a full worker prompt with repository boundaries, source-of-truth rules, testing/sync rules and handover discipline.
- Added a short project prompt for ChatGPT Project Instructions.
- Added the central roadmap and executable workpackage plan.
- Established `handover/workpackages/` as the coordinator-readable handover directory.

---

## Earlier completed work

### v12.3 — Review table simplification

Status: completed and user-confirmed after pandas Index bugfix.

Summary:

- Added `review_table_config.py` and tests.
- Simplified the main editable review table to the legal-user fields.
- Moved technical/audit fields to `Technische details bij de vervangtabel`.
- Fixed pandas Index truth-value handling.
- Preserved export semantics.

### v12.2 — Review focus filters

Status: completed and green in GitHub Actions.

Summary:

- Added `review_filters.py` and tests.
- Added safe focus filters such as `Toon alles`, `Alleen controle nodig`, `Alleen juridische referenties`, `Alleen namen/adressen` and `Alleen lage zekerheid`.
- Kept the full editable table as the source of truth for exports.

### v12.1 — Review table status model

Status: completed and green in GitHub Actions; user confirmed the Status column appears in Hugging Face.

Summary:

- Added `review_status.py` and tests.
- Added Dutch review statuses: `Automatisch vervangen`, `Controle nodig`, `Handmatig toegevoegd`, `Onthouden vervanging`.
- Added review status fields and status ordering in the review table.

### v11.2 — Dutch recognizer integration tests

Status: completed and green in GitHub Actions.

Summary:

- Added recognizer integration tests using `get_dutch_recognizers()`.
- Verified Dutch legal/admin references at value/span level.
- Verified value-only behavior so context labels remain readable.

### v11.1 — Legal reference recognizer hardening

Status: completed and green in GitHub Actions.

Summary:

- Hardened Dutch legal/admin reference detection.
- Expanded synthetic regression cases.
- Added/validated court/case numbers, incident numbers, camera/video references, insurance claim references, repair numbers, immigration numbers, municipal references and KvK numbers in labelled context.
- Preserved context words and legal meaning.

### v10 — Regression test layer

Status: completed and green in GitHub Actions.

Summary:

- Added synthetic Dutch legal regression cases and candidate scanner tests.
- Added false-positive guards for legal article references, dates and money/amount context.
- Added context preservation tests.
- Added GitHub Actions test workflow.

### v9.1 — UI polish and baseline stabilization

Status: completed and working in Hugging Face.

Summary:

- Added `APP_VERSION = "v9.1"`.
- Corrected Dutch UI wording.
- Kept recognizer behavior unchanged.

### v9 — Dutch Legal UI Layer

Status: completed and working in Hugging Face after startup hotfix.

Summary:

- Moved the app away from a technical Presidio demo feel.
- Added Dutch legal product language and workflow labels.
- Added `ui_texts_nl.py`, `display_labels_nl.py`, updates to `presidio_streamlit.py`, `fix_streamlit_nested_expanders.py` and `Dockerfile`.
- Added a startup hotfix for Streamlit nested expander limitations.

---

## GitHub → Hugging Face automation

Status: completed and working.

Purpose:

- Replace manual download/upload file replacement workflow.
- Make GitHub the source of truth.
- Automatically sync `solidprivacy-nl/scrub` to the Hugging Face Space `solidprivacy/scrub`.

Files added or changed:

- `.github/workflows/sync-to-huggingface.yml`

Main changes:

- Added a GitHub Actions workflow for syncing to Hugging Face.
- Replaced an initial hub-sync approach with a simpler direct Git push workflow.
- Added concurrency handling to avoid overlapping sync runs.

---

## Pre-GitHub incremental development phase

Status: superseded by GitHub workflow, but historically important.

Summary:

- Dutch/EU recognizer direction.
- Legal-profession focus.
- Local/offline strategy for confidentiality.
- Recognition of Dutch legal references, case numbers and administrative identifiers.
- Candidate scanner / audit-layer idea.
- Synthetic legal examples for testing.
- Context preservation principle: mask the person/value, not the legal meaning of the sentence.

---

## Planned later phase — v13 and beyond

Possible directions:

- Scrub Key JSON export UI.
- Scrub Key import/reload.
- AI-output reinsert.
- Further recognizer expansion by legal domain.
- Local packaging research.
- More advanced DOCX/PDF preservation.
- Better synthetic long-form legal test documents.
