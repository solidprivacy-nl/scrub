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

## v13.3 — Deterministic reinsert helper verification reconciliation

Status: completed and formally closed after Actions/sync verification.

Purpose:

- Administratively reconcile the v13.3 deterministic reinsert helper after coordinator-provided verification evidence.
- Replace the previous `awaiting coordinator verification of Actions/sync` status with formal closeout.
- Confirm that the helper remains pure, local and deterministic.
- Preserve the boundary that no UI, AI-output flow, cloud processing or export/download behavior change was added.

Files added or changed in this reconciliation:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1845_v13_3_reinsert_helper_verification_reconciliation.md`

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

Intentionally not changed in this reconciliation:

- No code files changed.
- No tests changed.
- No UI added.
- No direct edit to `scrub_key_reinsert.py`.
- No direct edit to `tests/test_scrub_key_reinsert.py`.
- No direct edit to `presidio_streamlit.py`.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No edit to `scrub_key.py`.
- No edit to `scrub_key_import.py`.
- No edit to `tests/*`.
- No AI calls.
- No cloud processing.
- No automatic document rehydration.
- No change to TXT, CSV, DOCX or PDF export behavior.
- No change to Scrub Key export behavior.
- No change to Scrub Key import UI behavior.
- No secrets, tokens or real personal data.

Outcome:

- v13.3 deterministic reinsert helper is completed and formally closed.

---

## v13.3 — Deterministic reinsert helper closeout

Status: completed and formally closed after Actions/sync verification.

Purpose:

- Verify and close out the v13.3 deterministic reinsert helper workpackage.
- Record that the helper remains pure, local and deterministic.
- Preserve the boundary that no UI, AI-output flow, cloud processing or export/download behavior change was added.

Files added or changed in the full v13.3 helper line:

- `scrub_key_reinsert.py`
- `tests/test_scrub_key_reinsert.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1745_v13_3_reinsert_helper.md`
- `handover/workpackages/20260607_1815_v13_3_reinsert_helper.md`
- `handover/workpackages/20260607_1830_v13_3_reinsert_helper_closeout.md`
- `handover/workpackages/20260607_1845_v13_3_reinsert_helper_verification_reconciliation.md`

Main changes:

- Added `detect_placeholders(text)` for conservative placeholder-token detection.
- Added `build_reinsert_mapping(scrub_key)` to build a deterministic placeholder-to-original mapping from included Scrub Key items.
- Added `reinsert_from_scrub_key(text, scrub_key)` to return reinserted text and an audit summary.
- Reused existing `validate_scrub_key(...)` validation.
- Invalid Scrub Keys return validation issues and do not modify the input text.
- Duplicate placeholder entries are detected and excluded from reinsertion to avoid ambiguity.
- Excluded Scrub Key items are ignored even if malformed/imported data contains them.
- Audit output includes item count, active item count, excluded item count, replacement count, placeholders not found, unknown placeholders, duplicate placeholders and validation issues.
- Audit output explicitly records local/no-AI/no-cloud behavior through `local_only=True`, `ai_processing=False` and `cloud_processing=False`.

Testing and verification:

- Added `tests/test_scrub_key_reinsert.py`.
- Tests cover valid reinsert, multiple placeholders, repeated placeholders, missing placeholders, unknown placeholders, invalid Scrub Key validation issues, duplicate placeholder detection, excluded rows not being reinserted, synthetic values only, input immutability and no-AI/no-cloud flags.
- Local targeted validation recorded by the implementation worker on the available/reconstructed subset:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py tests/test_scrub_key_import.py tests/test_scrub_key_reinsert.py` → 25 passed.
- Coordinator verification evidence confirms Actions and sync green:
  - Tests #106 green — commit `5854dbf`.
  - Sync to Hugging Face Space #120 green — commit `5854dbf`.
  - Tests #107 green — commit `43ecad4`.
  - Sync to Hugging Face Space #121 green — commit `43ecad4`.
  - Tests #108 green — commit `6e4ec9b`.
  - Sync to Hugging Face Space #122 green — commit `6e4ec9b`.
  - Tests #109 green — commit `eaf036a`.
  - Sync to Hugging Face Space #123 green — commit `eaf036a`.
- App verification is not applicable because this is a helper-only package.

Intentionally not changed:

- No code files changed in WP7B-FINAL reconciliation.
- No UI added.
- No direct edit to `presidio_streamlit.py`.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No edit to `scrub_key.py`.
- No edit to `scrub_key_import.py`.
- No AI calls.
- No cloud processing.
- No automatic document rehydration.
- No change to TXT, CSV, DOCX or PDF export behavior.
- No change to Scrub Key export behavior.
- No change to Scrub Key import UI behavior.
- No secrets, tokens or real personal data.

Outcome:

- v13.3 deterministic reinsert helper is implemented, verified and formally closed.

---

## v13.2 — Scrub Key import/reload UI app verification closeout

Status: completed, app-verified and closed.

Purpose:

- Administratively close the v13.2 Scrub Key import/reload UI after app verification.
- Record that the implemented import/reload flow works in the Hugging Face app.
- Preserve the boundary that this phase is import/reload only and does not add AI-output reinsert.

Files added or changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1730_v13_2_scrub_key_import_ui_app_closeout.md`

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

Closeout notes:

- GitHub Actions tests were green based on coordinator evidence.
- GitHub to Hugging Face sync was green based on coordinator evidence.
- Import/reload remains local and uses the existing helper logic.
- The key remains pseudonymization/reversible and must be protected.
- No AI-output reinsert behavior was added.
- No automatic document rehydration was added.
- No export/download behavior was intentionally changed.

Intentionally not changed in this app-verification closeout:

- No code files changed.
- No tests changed.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No direct edit to `presidio_streamlit.py`.
- No edit to `scrub_key.py`.
- No edit to `scrub_key_import.py`.
- No edit to `tests/*`.
- No AI-output reinsert behavior.
- No automatic document rehydration.
- No change to TXT, CSV, DOCX or PDF export/download behavior.
- No cloud processing.
- No secrets, tokens or real personal data.

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

- Deterministic reinsert UI after verification.
- AI-output reinsert.
- Further recognizer expansion by legal domain.
