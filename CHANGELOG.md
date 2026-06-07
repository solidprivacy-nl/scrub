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

## v13.3 — Deterministic reinsert UI implementation

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Purpose:

- Add the deterministic local reinsert UI described in `REINSERT_UI_SPEC.md`.
- Let the user paste scrubbed or AI-generated text and locally restore mapped placeholders using a validated Scrub Key.
- Show restored text, an audit summary and a `.txt` download for restored text.
- Keep the step local and deterministic, with no AI calls and no cloud processing.

Files added or changed:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_reinsert_ui_patch.py`
- `tests/test_scrub_key_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1915_v13_3_reinsert_ui_implementation.md`

Main changes:

- Added import/wiring for the verified helper:
  - `from scrub_key_reinsert import reinsert_from_scrub_key`.
- Added the section `Originele waarden terugzetten` after the existing Scrub Key import/reload area.
- Added the input label `Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten`.
- Added the explicit action button `Zet originele waarden lokaal terug`.
- Added local helper call:
  - `reinsert_from_scrub_key(reinsert_input_text, active_reinsert_scrub_key)`.
- Added output label `Herstelde tekst`.
- Added `Download herstelde tekst (.txt)` with `text/plain` output.
- Added `Controleverslag terugzetten` audit summary.
- Added audit rendering for item count, active item count, excluded item count, replacement count, placeholders not found, unknown placeholders, duplicate placeholders, validation issues, local-only status, AI-processing status and cloud-processing status.
- Added visible warning that restored text may again contain personal or confidential information and must be reviewed before sharing.
- Added local/no-AI/no-cloud wording.
- Stores a successfully imported Scrub Key in `st.session_state["active_scrub_key"]` for local reinsert use.
- Falls back to the currently built Scrub Key from reviewed replacement rows if no imported key is active.

Testing and validation:

- Added `tests/test_scrub_key_reinsert_ui_patch.py`.
- Updated `tests/test_scrub_key_ui_patch.py` so it no longer forbids the intentionally added reinsert flow, while still guarding no-AI, no-cloud and no-automatic-document-rehydration boundaries.
- Local targeted validation on a reconstructed subset passed:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py tests/test_scrub_key_import.py tests/test_scrub_key_reinsert.py tests/test_scrub_key_reinsert_ui_patch.py tests/test_scrub_key_import_ui_patch.py tests/test_scrub_key_ui_patch.py` → 57 passed.
- Full repository test suite was not run from this connector environment.
- GitHub Actions are pending for WP8B commits.
- Hugging Face sync is pending for WP8B commits.
- App verification is pending because UI behavior changed.

Intentionally not changed:

- No direct edit to `presidio_streamlit.py`.
- No edit to `scrub_key_reinsert.py`.
- No edit to `scrub_key.py`.
- No edit to `scrub_key_import.py`.
- No AI calls.
- No cloud processing.
- No automatic document rehydration.
- No DOCX/PDF reinsert.
- No TXT, CSV, DOCX or PDF scrubbed export behavior changed.
- No Scrub Key JSON export behavior intentionally changed.
- No Scrub Key import/reload behavior intentionally changed except storing the validated imported key in session state for reinsert use.
- No silent overwrite of existing review rows.
- No secrets, tokens or real personal data.

Outcome:

- v13.3 deterministic local reinsert UI is implemented and awaits external verification and app testing.

---

## v13.3 — Deterministic reinsert UI planning

Status: implemented; reinsert UI implementation completed in WP8B and awaits verification.

Purpose:

- Plan deterministic local reinsert UI before changing Streamlit UI code.
- Define where the UI should appear, what labels it should use, what state it should rely on, and which warnings and audit fields it must show.
- Keep AI-output behavior separate unless explicitly approved.

Files added or changed:

- `REINSERT_UI_SPEC.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1900_v13_3_reinsert_ui_planning.md`

Main planning decisions:

- Future UI block should appear after the existing Scrub Key import/reload section near the download/export area.
- Suggested section label: `Originele waarden terugzetten`.
- Suggested input label: `Plak hier de tekst waarin u originele waarden lokaal wilt terugzetten`.
- Suggested action button: `Zet originele waarden lokaal terug`.
- Suggested output label: `Herstelde tekst`.
- Suggested download label: `Download herstelde tekst (.txt)`.
- Future UI should call `reinsert_from_scrub_key(text, scrub_key)` and render the helper result instead of duplicating reinsert logic.
- Future UI should use a validated Scrub Key from import/reload first, or a key built from the current reviewed replacement table if no imported key exists.
- Reinsertion must require a separate visible user action and must not happen automatically when a Scrub Key is loaded.
- First UI implementation should produce restored text and `.txt` download only; no DOCX/PDF rehydration in the first UI step.

Required warnings specified:

- Reinsertion restores original sensitive values.
- Restored text may again contain personal or confidential information.
- Restored output must be manually reviewed before sharing.
- A Scrub Key is reversible/pseudonymization, not full anonymization.
- The key must remain local and protected.
- No AI/cloud processing is involved in the local reinsert step.

Required audit summary specified:

- mapping item count;
- active item count;
- excluded item count;
- replacement count;
- placeholders not found;
- unknown placeholders;
- duplicate placeholders;
- validation issues;
- local-only status;
- no-AI status;
- no-cloud status.

Testing and validation:

- Tests: not applicable; planning/specification-only workpackage.
- App verification: not applicable; no UI behavior changed in WP8 planning.

Intentionally not changed in planning phase:

- No UI code changed.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No direct edit to `presidio_streamlit.py`.
- No tests added or changed.
- No AI calls.
- No cloud processing.
- No automatic document rehydration.
- No TXT, CSV, DOCX or PDF export behavior changed.
- No Scrub Key JSON export behavior changed.
- No Scrub Key import/reload behavior changed.
- No secrets, tokens or real personal data.

Outcome:

- v13.3 deterministic reinsert UI was planned and then implemented in WP8B.

---

## v13.3 — Deterministic reinsert helper verification reconciliation

Status: completed and formally closed after Actions/sync verification.

Purpose:

- Administratively reconcile the v13.3 deterministic reinsert helper after coordinator-provided verification evidence.
- Replace the previous `awaiting coordinator verification of Actions/sync` status with formal closeout.
- Confirm that the helper remains pure, local and deterministic.
- Preserve the boundary that no UI, AI-output flow, cloud processing or export/download behavior change was added.

Verification evidence:

- Tests #106 green — commit `5854dbf`.
- Sync to Hugging Face Space #120 green — commit `5854dbf`.
- Tests #107 green — commit `43ecad4`.
- Sync to Hugging Face Space #121 green — commit `43ecad4`.
- Tests #108 green — commit `6e4ec9b`.
- Sync to Hugging Face Space #122 green — commit `6e4ec9b`.
- Tests #109 green — commit `eaf036a`.
- Sync to Hugging Face Space #123 green — commit `eaf036a`.

Validation status:

- GitHub Actions: green based on coordinator evidence.
- Hugging Face sync: green based on coordinator evidence.
- App verification: not applicable, helper-only package.

Outcome:

- v13.3 deterministic reinsert helper is completed and formally closed.

---

## v13.2 — Scrub Key import/reload UI app verification closeout

Status: completed, app-verified and closed.

Purpose:

- Administratively close the v13.2 Scrub Key import/reload UI after app verification.
- Record that the implemented import/reload flow works in the Hugging Face app.
- Preserve the boundary that this phase is import/reload only and does not add AI-output reinsert.

Technical evidence already recorded:

- Tests #89 green — commit `83353e4`.
- Tests #90 green — commit `4a1ef55`.
- Sync to Hugging Face Space #104 green — commit `4a1ef55`.
- Tests #91 green — commit `4d8bfe9`.
- Sync to Hugging Face Space #105 green — commit `4d8bfe9`.
- Tests #92 green — commit `ff8321f`.
- Sync to Hugging Face Space #106 green — commit `ff8321f`.

App verification:

- Confirmed by coordinator/user.
- `Scrub Key laden` works.
- Scrub Key import/reload UI is visible.
- Upload/paste import flow works.
- Pseudonymization/reversibility warning is visible.
- Existing `Download Scrub Key (.json)` remains visible.
- Existing TXT, CSV, DOCX and PDF downloads remain available.

Outcome:

- v13.2 Scrub Key import/reload UI is completed, app-verified and closed.

---

## Earlier completed work

- v13.2 Scrub Key import/reload UI integration.
- v13.2 Scrub Key import/reload helper and tests.
- v13.1 Scrub Key JSON export UI closeout.
- v12.6 Export sanity checks closeout.
- v13.0 Scrub Key specification and pure model.
- v12.5 Final review summary.
- v12.4 Review guidance text.
- Project governance setup.
- v12.3 Review table simplification.
- v12.2 Review focus filters.
- v12.1 Review table status model.
- v11.2 Dutch recognizer integration tests.
- v11.1 Legal reference recognizer hardening.
- v10 Regression test layer.
- v9.1 UI polish and baseline stabilization.
- v9 Dutch Legal UI Layer.

---

## Planned later phase — v13 and beyond

Possible directions:

- Deterministic reinsert UI verification and closeout.
- AI-output reinsert workflow review.
- Further recognizer expansion by legal domain.
