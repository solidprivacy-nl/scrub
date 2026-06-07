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

## v13.0 — Scrub Key specification and pure model

Status: implemented; pending GitHub Actions and Hugging Face sync confirmation.

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
- Added a deterministic pure helper model:
  - `build_scrub_key(rows, document_label=None)`;
  - `scrub_key_to_json(scrub_key)`;
  - `scrub_key_from_json(text)`;
  - `validate_scrub_key(scrub_key)`.
- Set the v13.0 excluded-row policy to `omitted`, so unchecked rows are not written into the key.
- Kept timestamp handling deterministic: the model does not create timestamps itself; validation catches missing timestamps.

Testing:

- Added `tests/test_scrub_key.py`.
- Local targeted validation passed: `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
- Tests cover valid key creation, excluded-row omission, required fields, JSON roundtrip, validation errors, and synthetic Dutch legal examples only.

Intentionally not changed:

- No direct edit to `presidio_streamlit.py`.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No export/download buttons.
- No reinsert UI.
- No cloud processing.
- No secret storage.
- No real personal data in tests or examples.
- No change to active review UI or export semantics.

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
- Added summary counts for:
  - total rows;
  - automatically detected rows;
  - rows needing review;
  - manually added rows;
  - remembered replacement rows;
  - checked rows included in export;
  - unchecked rows excluded from export;
  - open unchecked candidate rows.
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
- No direct edit to `fix_streamlit_nested_expanders.py` during closeout.
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

## v12.3 — Review table simplification

Status: completed and user-confirmed after pandas Index bugfix.

Purpose:

- Reduce visual noise in the replacement table.
- Keep the main review table focused on the columns legal users actually need to edit.
- Preserve technical/audit information in a separate details view.
- Keep recognizer and export semantics unchanged.

Files added or changed:

- `review_table_config.py`
- `tests/test_review_table_config.py`
- `fix_streamlit_nested_expanders.py`
- `CHANGELOG.md`

Main changes:

- Added a central table configuration module.
- Main editable review table now focuses on:
  - `Meenemen`
  - `Onthouden`
  - `Status`
  - `Gevonden tekst`
  - `Vervangen door`
  - `Type gegeven`
  - `Zekerheid`
- Technical and audit-oriented columns are moved out of the primary editing view.
- Added a separate `Technische details bij de vervangtabel` expander.
- Fixed pandas Index truth-value handling by explicitly converting available columns to list/set.

Important design decision:

- The full data remains present in the underlying dataframe.
- The main table is simplified visually, but exports and reports still use the available row data.
- The technical details remain accessible for debugging, auditability and future tuning.

Testing:

- Added unit tests for `review_table_config.py`.
- User confirmed the simplified review table and technical-details flow worked after the bugfix.

Intentionally not changed:

- No recognizer changes.
- No entity-type expansion.
- No export semantics change.
- No MSI/local installer work.
- No LLM/cloud feature.

---

## v12.2 — Review focus filters

Status: completed and green in GitHub Actions.

Purpose:

- Add practical focus filters on top of the v12.1 review-status model.
- Help the legal reviewer quickly inspect only the rows that matter for a specific task.
- Keep export semantics safe: the filter is an overview/focus tool, not the authoritative edited replacement table.

Files added or changed:

- `review_filters.py`
- `tests/test_review_filters.py`
- `fix_streamlit_nested_expanders.py`
- `CHANGELOG.md`

Main changes:

- Added pure filter helpers with Dutch filter labels.
- Added filter groups for legal/admin reference entity types, names and address-like data.
- Added low-confidence filtering based on either Dutch confidence label `Laag` or numeric score below `0.60`.
- Added tests for all filter modes.
- Extended the Streamlit startup patch so the review step gets a `Focusfilter voor controle` selectbox.
- When a focus filter is active, the app shows a read-only filtered overview above the full editable replacement table.

Important design decision:

- v12.2 does **not** filter the editable table itself.
- The full replacement table remains the source of truth for exports.
- This prevents hidden rows from being accidentally dropped from the final export.
- The focus filter is deliberately a safe review aid, not an edit-scope limiter.

Testing:

- Added unit tests for `review_filters.py`.
- GitHub Actions `Tests` passed.
- GitHub → Hugging Face sync passed.

Intentionally not changed:

- No recognizer changes.
- No entity-type expansion.
- No export semantics change.
- No MSI/local installer work.
- No LLM/cloud feature.

---

## v12.1 — Review table status model

Status: completed and green in GitHub Actions; user confirmed the Status column appears in Hugging Face.

Purpose:

- Start the v12 Review UX phase with a simple, explicit review-status model.
- Make it clearer to a legal user which rows are already applied, which need review, which are manual, and which come from remembered replacements.
- Keep recognizer logic unchanged.

Files added or changed:

- `review_status.py`
- `tests/test_review_status.py`
- `fix_streamlit_nested_expanders.py`
- `CHANGELOG.md`

Main changes:

- Added a pure review-status model with stable internal values:
  - `auto_detected`
  - `needs_review`
  - `manual`
  - `remembered`
- Added Dutch user-facing labels:
  - `Automatisch vervangen`
  - `Controle nodig`
  - `Handmatig toegevoegd`
  - `Onthouden vervanging`
- Added sorting order so rows needing review appear before automatically applied rows.
- Added tests for source-to-status mapping and ordering.
- Extended the existing Streamlit startup patch so the replacement table gets a visible `Status` column, internal status fields and a compact status summary above the editor.

Testing:

- Added unit tests for `review_status.py`.
- GitHub Actions `Tests` passed.
- GitHub → Hugging Face sync passed.
- User confirmed the Status column appeared correctly in the Hugging Face app.

Intentionally not changed:

- No recognizer changes.
- No new entity types.
- No MSI/local installer work.
- No LLM/cloud feature.

---

## v11.2 — Dutch recognizer integration tests

Status: completed and green in GitHub Actions.

Purpose:

- Prove that the real Dutch recognizer layer works, not only the candidate scanner / audit layer.
- Test recognizer output at value/span level.
- Confirm that context labels remain readable and are not swallowed into the sensitive span.

Files added or changed:

- `.github/workflows/tests.yml`
- `tests/test_dutch_recognizers_integration.py`

Main changes:

- Added lightweight recognizer integration tests using `get_dutch_recognizers()` directly.
- Verified that v11.1 legal reference values are detected by the actual recognizers.
- Verified expected entity types for representative court/case numbers, incident numbers, camera/video references, insurance claim references, repair numbers, immigration numbers, municipal references and KvK numbers.
- Verified value-only behavior so context labels remain readable.

Testing:

- GitHub Actions `Tests` passed.
- GitHub → Hugging Face sync passed.

Intentionally not changed:

- No UI changes.
- No MSI/local installer work.
- No new cloud dependency.

---

## v11.1 — Legal reference recognizer hardening

Status: completed and green in GitHub Actions.

Purpose:

- Harden recognition and review of Dutch legal/admin reference values.
- Move from isolated examples to category-level reference recognition.
- Preserve legal context while only selecting the sensitive value.

Files changed:

- `candidate_scanner.py`
- `test_cases/legal_regression_cases.py`
- `tests/test_candidate_scanner_regression.py`
- `tests/test_case_number_pattern_contract.py`

Main changes:

- Expanded the regression set with concrete Dutch legal/admin examples reported during testing.
- Added/validated cases for court/case numbers, incident numbers, camera/video references, insurance claim references, repair numbers, immigration numbers, municipal references and KvK numbers in labelled context.
- Added a lightweight KvK fallback to the candidate scanner.
- Kept the candidate scanner as a review/audit layer with candidates unchecked by default.
- Updated the case-reference contract test to use the broader contextual value regex instead of only the strict formal court-number regex.

Important design decision:

- Context can make a generic-looking reference legally relevant.
- Tests reflect contextual recognition, not only raw pattern recognition.

Testing:

- GitHub Actions `Tests` passed after the contextual-value test correction.
- GitHub → Hugging Face sync passed.

Intentionally not changed:

- No broad blind masking of every uppercase/digit code.
- No automatic masking of weak candidates without context.
- No masking of article references, dates, amounts, postcodes or document navigation references as legal reference numbers.

---

## v10 — Regression test layer

Status: completed and green in GitHub Actions.

Purpose:

- Stop relying only on manual interface testing.
- Create a repeatable regression safety net before further recognizer changes.
- Protect context preservation and false-positive behavior.

Files added or changed:

- `test_cases/legal_regression_cases.py`
- `tests/test_candidate_scanner_regression.py`
- `tests/test_context_preservation_contract.py`
- `tests/test_case_number_pattern_contract.py`
- `.github/workflows/tests.yml`

Main changes:

- Added synthetic Dutch legal regression cases.
- Added candidate scanner tests for expected reference-like values.
- Added false-positive guards for legal article references, dates and money/amount context.
- Added context preservation contract tests for words such as `Slachtoffer`, `minderjarige` and `Verzoeker`.
- Added a GitHub Actions workflow for Python regression tests.
- Fixed import path handling by setting `PYTHONPATH` to the repository root.
- Kept early tests lightweight to avoid unnecessary full Streamlit/Presidio/spaCy startup cost.

Testing:

- GitHub Actions `Tests` passed.
- GitHub → Hugging Face sync passed.

Intentionally not changed:

- No major recognizer changes in v10 itself.
- No UI redesign.

---

## v9.1 — UI polish and baseline stabilization

Status: completed and working in Hugging Face.

Purpose:

- Polish Dutch UI text after the v9 conversion.
- Keep the app stable before adding deeper regression infrastructure.

Files changed:

- `ui_texts_nl.py`

Main changes:

- Added `APP_VERSION = "v9.1"`.
- Corrected UI wording:
  - `clientreferenties` → `cliëntreferenties`.
- Kept recognizer behavior unchanged.

Testing:

- GitHub → Hugging Face sync passed.
- User confirmed the app was working.

Intentionally not changed:

- No recognizer changes.
- No major UX redesign.

---

## v9 — Dutch Legal UI Layer

Status: completed and working in Hugging Face after startup hotfix.

Purpose:

- Move the app away from a technical “Presidio demo” feel.
- Present it as a Dutch legal document scrubber.
- Keep the underlying recognition engine, but make the user workflow more understandable for legal users.

Files added or changed:

- `ui_texts_nl.py`
- `display_labels_nl.py`
- `presidio_streamlit.py`
- `fix_streamlit_nested_expanders.py`
- `Dockerfile`

Main changes:

- Added Dutch product language and workflow language such as `Scrub Legal`, `Lokale juridische documentcontrole`, `Controlemodus`, `Voeg document of tekst toe`, `Controleer gevonden gegevens`, `Mogelijke gemiste waarden` and `Download opgeschoonde bestanden`.
- Added a separate Dutch UI copy layer and Dutch display labels for technical entity types.
- Reworked the main Streamlit app to make the workflow more legal-user oriented.
- Restored/kept synthetic legal test example loading.
- Added a startup hotfix for Streamlit’s nested-expander limitation.

Known limitation:

- Some Streamlit-native widget labels remain English, such as upload button internals (`Browse files`, `Drag and drop file here`). These come from Streamlit itself and are not fully controlled by normal UI strings.

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
- Initial `huggingface/hub-sync` approach failed on SDK and API-rate issues.
- Replaced it with a simpler direct Git push workflow.
- Added concurrency handling to avoid overlapping sync runs.

Security/ops note:

- The workflow expects a GitHub Actions secret named `HF_TOKEN`.
- This should be a Hugging Face token with write access to `solidprivacy/scrub`.

---

## Pre-GitHub incremental development phase

Status: superseded by GitHub workflow, but historically important.

Purpose:

- Improve the Hugging Face app through manual file replacement while the GitHub workflow was not yet connected.

Main themes:

- Dutch/EU recognizer direction.
- Legal-profession focus.
- Local/offline strategy for confidentiality.
- Recognition of Dutch legal references, case numbers and administrative identifiers.
- Candidate scanner / audit-layer idea.
- Synthetic legal examples for testing.
- Context preservation principle: do not mask role words such as `slachtoffer`, `minderjarige`, `verzoeker`, `verweerder`; mask the person/value, not the legal meaning of the sentence.

Important design conclusions:

- A local deterministic scrubber is a better MVP path than relying on cloud LLMs.
- Local LLMs may be useful later, but they are not the best first layer for a fast legal scrubber.
- The MVP should combine deterministic recognizers, Dutch legal/admin taxonomy, review table, candidate scanner, regression tests and eventually local packaging.

---

## Planned later phase — v13 and beyond

Possible directions:

- Further recognizer expansion by legal domain: family law, criminal law, labour law, immigration law, administrative law, housing/real estate and insurance/personal injury.
- Local packaging research: Windows desktop app, local-only processing, MSI installer path and model/runtime size constraints.
- More advanced DOCX/PDF preservation.
- Better synthetic long-form legal test documents.
