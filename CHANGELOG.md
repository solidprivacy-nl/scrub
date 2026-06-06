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

This prevents one-off fixes and protects existing behaviour.

---

## v12.1 — Review table status model

Status: implemented; awaiting GitHub Actions and Hugging Face verification.

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
- Extended the existing Streamlit startup patch so the replacement table gets:
  - a visible `Status` column;
  - hidden/internal `review_status` and `review_order` fields;
  - a compact status summary above the editor;
  - status values included in report rows where supported by downstream exports.

Important design decision:

- This phase deliberately does not add filters yet.
- v12.1 only introduces the status model and visible status column.
- Filters and further table simplification are planned for v12.2 and v12.3.

Testing:

- Added unit tests for `review_status.py`.
- GitHub Actions status still needs to be checked after this changelog update.
- Hugging Face app should be checked after sync.

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
- Verified expected entity types for values such as:
  - `10598721 / UE VERZ 26-441` → `NL_LEGAL_CASE_NUMBER`
  - `INC-2026-0912` → `NL_INCIDENT_NUMBER`
  - `CAM-MAAS-2026-0518` → `NL_OTHER_REFERENCE`
  - `CLM-2026-112233` → `NL_CLAIM_NUMBER`
  - `REP-2026-4410` → `NL_OTHER_REFERENCE`
  - `ARN 26/4412` → `NL_LEGAL_CASE_NUMBER`
  - `NL26.12345` → `NL_LEGAL_CASE_NUMBER`
  - `GEM-HLM-2026-2210` → `NL_LEGAL_CASE_NUMBER`
  - `200.345.678/01 OK` → `NL_LEGAL_CASE_NUMBER`
  - `76543210` after KvK context → `NL_KVK_NUMBER`
- Verified value-only behavior:
  - context such as `Zaaknummer:` must remain readable;
  - context such as `intern incidentnummer` must remain readable;
  - context such as `Claimreferentie verzekeraar:` must remain readable;
  - context such as `KvK-nummer vennootschap:` must remain readable.

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
- Added/validated cases for:
  - court / case numbers;
  - incident numbers;
  - camera/video references;
  - insurance claim references;
  - repair numbers;
  - administrative law case numbers;
  - immigration case numbers;
  - municipal case references;
  - enterprise chamber / appellate style case numbers;
  - KvK numbers in labelled context.
- Added a lightweight KvK fallback to the candidate scanner:
  - `KvK-nummer vennootschap: 76543210` now yields value-only candidate `76543210` as `NL_KVK_NUMBER` when not already detected.
- Kept the candidate scanner as a review/audit layer:
  - candidates remain unchecked by default in the UI;
  - the user decides whether to include them.
- Updated the case-reference contract test to use the broader contextual value regex instead of only the strict formal court-number regex.

Important design decision:

- `GEM-HLM-2026-2210` is not a classic court-number format by itself.
- It becomes a legal case number because it appears near context such as `zaaknummer`.
- Therefore the test should reflect contextual recognition, not only raw pattern recognition.

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
- Added false-positive guards for:
  - legal article references, e.g. `7:669 BW`;
  - dates, e.g. `15-12-2025`;
  - money/amount context, e.g. `EUR 1.250,00`.
- Added context preservation contract tests:
  - `Slachtoffer` must stay readable;
  - `minderjarige` must stay readable;
  - `Verzoeker` must stay readable;
  - role/context words must not be swallowed into the replacement span.
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

- Added Dutch product language:
  - `Scrub Legal`
  - `Lokale juridische documentcontrole`
  - `Controlemodus`
  - `Manier van vervangen`
  - `Voeg document of tekst toe`
  - `Controleer gevonden gegevens`
  - `Mogelijke gemiste waarden`
  - `Download opgeschoonde bestanden`
- Added a separate Dutch UI copy layer in `ui_texts_nl.py`.
- Added Dutch display labels for technical entity types in `display_labels_nl.py`.
- Reworked the main Streamlit app to make the workflow more legal-user oriented.
- Kept technical settings under advanced sections.
- Kept technical recognizer labels available, but made them less central in the interface.
- Restored/kept synthetic legal test example loading in the interface.
- Added a startup hotfix for Streamlit’s nested-expander limitation.

Important bug fixed:

- Streamlit does not allow an expander inside another expander.
- The first v9 implementation nested `Woordenlijsten` inside `Geavanceerde instellingen`.
- Added `fix_streamlit_nested_expanders.py` and updated the Docker startup command to patch this before Streamlit starts.

Testing:

- GitHub → Hugging Face sync passed.
- User confirmed app startup and interface were working.

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
- Replaced it with a simpler direct Git push workflow:
  - checkout GitHub repo;
  - add Hugging Face Space as remote;
  - force-push `HEAD:main` to the Space.
- Added concurrency handling to avoid overlapping sync runs.

Problems encountered and fixed:

- Missing or insufficient Hugging Face token caused initial `Space not found` / authentication behavior.
- Space SDK mismatch was corrected from `streamlit` to `docker`.
- API `429 Too Many Requests` from `huggingface/hub-sync` was avoided by switching to direct Git push.

Testing:

- Sync workflow passed repeatedly after direct Git push implementation.

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
- Context preservation principle:
  - do not mask role words such as `slachtoffer`, `minderjarige`, `verzoeker`, `verweerder`;
  - mask the person/value, not the legal meaning of the sentence.

Important design conclusions:

- A local deterministic scrubber is a better MVP path than relying on cloud LLMs.
- Local LLMs may be useful later, but they are not the best first layer for a fast legal scrubber.
- The MVP should combine:
  - deterministic recognizers;
  - Dutch legal/admin taxonomy;
  - review table;
  - candidate scanner;
  - regression tests;
  - eventually local packaging.

---

## Planned next phase — v12.2 Review filters

Status: planned, not yet implemented.

Goal:

- Add filters on top of the v12.1 status model.

Planned scope:

- Show all.
- Show only `Controle nodig`.
- Show only legal references.
- Show only names/addresses.
- Show only low-confidence items.
- Keep technical columns hidden by default where possible.

Non-goals for v12.2:

- No recognizer changes.
- No MSI/local desktop packaging yet.
- No LLM integration.

---

## Planned later phase — v13 and beyond

Possible directions:

- Further recognizer expansion by legal domain:
  - family law;
  - criminal law;
  - labour law;
  - immigration law;
  - administrative law;
  - housing/real estate;
  - insurance / personal injury.
- Local packaging research:
  - Windows desktop app;
  - local-only processing;
  - MSI installer path;
  - model/runtime size constraints.
- More advanced DOCX/PDF preservation.
- Better synthetic long-form legal test documents.
