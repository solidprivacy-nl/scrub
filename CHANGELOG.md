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

## WP9 — AI-output / document reinsert workflow UX and architecture review

Status: completed; review-only workpackage.

Purpose:

- Decide what Scrub should do next for AI-output and document-level reinsert before implementation starts.
- Challenge whether pasted-text reinsert is enough.
- Challenge whether direct DOCX/PDF reinsert should be added immediately.
- Challenge whether anonymization and de-anonymization should remain in one combined long screen.
- Recommend a model architecture, product direction, tactical sequence, operational safety position and visual/UX direction.

Files added or changed:

- Added `AI_OUTPUT_REINSERT_WORKFLOW_REVIEW.md`.
- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `handover/workpackages/20260608_0000_ai_output_reinsert_workflow_review.md`.

Main recommendation:

- Keep pasted-text reinsert as a safe baseline and fallback, but do not treat it as the final legal-document workflow.
- Move toward a two-mode interface:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.
- Add document-level reinsert in phases.
- Prioritize TXT and DOCX before PDF.
- Keep PDF as investigation/reliability-review work only for now.
- Keep all reinsert behavior local-only, deterministic and helper-first.
- Do not add AI calls.
- Do not add cloud processing.

First three obvious ideas challenged:

1. `Keep only pasted-text reinsert` was limited: useful fallback, not enough for final legal-document workflow because of usability burden, formatting loss, legal workflow friction, incomplete-copy risk and poor DOCX/PDF fit.
2. `Add direct PDF/DOCX reinsert immediately` was rejected as too broad: DOCX is feasible but needs careful replacement; PDF is high-risk because of extraction, layout reconstruction, scanned documents, OCR and metadata hygiene.
3. `Add one combined screen for everything` was rejected as main UX direction: it creates cognitive overload and mixes anonymization with reversible de-anonymization risk.

Recommended implementation sequence:

1. Keep current text-paste reinsert and improve guidance when the UI is next touched.
2. Add TXT upload/download reinsert.
3. Add DOCX reinsert helper, pure helper + tests.
4. Add DOCX reinsert UI only after helper validation.
5. Investigate PDF text extraction only.
6. Consider PDF output only after a reliability review.

Next recommended implementation workpackage:

```text
WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests
```

Recommended WP10 boundaries:

- helper/test-first;
- no UI changes;
- no edit to `fix_streamlit_nested_expanders.py`;
- no edit to `presidio_streamlit.py`;
- no existing export/download behavior changes;
- no Scrub Key export/import behavior changes;
- no PDF reinsert implementation;
- no AI calls;
- no cloud processing;
- synthetic data only.

Testing and validation:

- Tests: not applicable; planning/review-only workpackage.
- App verification: not applicable; no UI behavior changed.
- GitHub Actions: not checked for this docs-only change at handover time.
- Hugging Face sync: not checked for this docs-only change at handover time.

Intentionally not changed:

- No code files changed.
- No tests changed.
- No UI changed.
- No export/download behavior changed.
- No Scrub Key export/import behavior changed.
- No TXT/DOCX/PDF reinsert implementation added.
- No AI calls added.
- No cloud processing added.
- No secrets, tokens or real personal data stored.

Outcome:

- WP9 is complete.
- Product direction for reinsert is now documented before implementation.

---

## v13.3 — Deterministic reinsert UI app verification closeout

Status: completed and app-verified after Actions/sync verification.

Purpose:

- Administratively close the v13.3 deterministic reinsert UI after technical verification and app verification.
- Record that local deterministic reinsert works in the Hugging Face app.
- Preserve the boundary that no AI calls, cloud processing, automatic document rehydration, DOCX/PDF reinsert or existing scrubbed export/download behavior changes were added.

Files added or changed in this closeout:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1930_v13_3_reinsert_ui_app_closeout.md`

Technical evidence:

- Local validation recorded in WP8B: 57 passed.
- Tests #120 green — commit `7725182`.
- Sync to Hugging Face Space #134 green — commit `7725182`.
- Tests #121 green — commit `84f5312`.
- Sync to Hugging Face Space #135 green — commit `84f5312`.
- Tests #122 green — commit `1a8e87e`.
- Sync to Hugging Face Space #136 green — commit `1a8e87e`.

App verification:

- Confirmed by coordinator/user.
- `Originele waarden terugzetten` is visible.
- Warning about sensitive/confidential information is visible.
- Local-only / no-AI / no-cloud text is visible.
- Text input works.
- Button `Zet originele waarden lokaal terug` works.
- Reinsert works with a valid Scrub Key.
- Placeholders are correctly restored.
- Result message appears: `37 waarde(n) lokaal teruggezet.`
- `Herstelde tekst` appears with restored original values.

Closeout notes:

- Restored output may contain sensitive/confidential information again.
- Existing Scrub Key export remains available.
- Existing Scrub Key import/reload remains available.
- Existing TXT, CSV, DOCX and PDF scrubbed downloads remain available based on prior verification and no intentional export changes.
- No AI calls were added.
- No cloud processing was added.
- No automatic document rehydration was added.
- No DOCX/PDF reinsert was added.
- No existing scrubbed export/download behavior was intentionally changed.

Intentionally not changed in this closeout:

- No code files changed.
- No tests changed.
- No edit to `fix_streamlit_nested_expanders.py`.
- No edit to `presidio_streamlit.py`.
- No edit to `scrub_key_reinsert.py`.
- No edit to `scrub_key.py`.
- No edit to `scrub_key_import.py`.
- No edit to `tests/*`.
- No UI changes.
- No AI calls.
- No cloud processing.
- No automatic document rehydration.
- No TXT, CSV, DOCX or PDF export/download behavior changed.
- No Scrub Key export/import behavior changed.
- No secrets, tokens or real personal data.

Outcome:

- v13.3 deterministic local reinsert UI is completed, app-verified and formally closed.

---

## v13.3 — Deterministic reinsert UI implementation

Status: completed and app-verified after Actions/sync verification.

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
- `handover/workpackages/20260607_1930_v13_3_reinsert_ui_app_closeout.md`

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
- GitHub Actions green based on coordinator evidence.
- Hugging Face sync green based on coordinator evidence.
- App verification confirmed by coordinator/user.

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

- v13.3 deterministic local reinsert UI is completed, app-verified and formally closed.

---

## v13.3 — Deterministic reinsert UI planning

Status: implemented; reinsert UI implementation completed in WP8B and app-verified in WP8C.

Purpose:

- Plan deterministic local reinsert UI before changing Streamlit UI code.
- Define where the UI should appear, what labels it should use, what state it should rely on, and which warnings and audit fields it must show.
- Keep AI-output behavior separate unless explicitly approved.

Outcome:

- v13.3 deterministic reinsert UI was planned and then implemented and app-verified.

---

## v13.3 — Deterministic reinsert helper verification reconciliation

Status: completed and formally closed after Actions/sync verification.

Purpose:

- Administratively reconcile the v13.3 deterministic reinsert helper after coordinator-provided verification evidence.
- Confirm that the helper remains pure, local and deterministic.
- Preserve the boundary that no UI, AI-output flow, cloud processing or export/download behavior change was added.

Outcome:

- v13.3 deterministic reinsert helper is completed and formally closed.

---

## v13.2 — Scrub Key import/reload UI app verification closeout

Status: completed, app-verified and closed.

Purpose:

- Administratively close the v13.2 Scrub Key import/reload UI after app verification.
- Record that the implemented import/reload flow works in the Hugging Face app.
- Preserve the boundary that this phase is import/reload only and does not add AI-output reinsert.

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

- TXT/DOCX document-level reinsert foundation.
- Two-mode UI planning for `Anonimiseren` and `Originele waarden terugzetten`.
- Further recognizer expansion by legal domain.
