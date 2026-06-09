# Changelog — SolidPrivacy Scrub

## WP18R — Risk-driven roadmap and operating model reset

Status: completed documentation/governance-only update.

Purpose:

- Implement the accepted strategic review recommendations.
- Convert the roadmap from feature-led sequencing to risk-driven sequencing.
- Add explicit governance for risk tracking, decision logging, release notes and workflow status monitoring.
- Prepare parallel future workpackages after WP18-FIX without starting new functional work.

Files added:

- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `STATUS_MONITORING_RUNBOOK.md`
- `RELEASE_NOTES.md`
- `handover/workpackages/20260609_1230_risk_driven_roadmap_operating_model_reset.md`

Files changed:

- `PROJECT_PROMPT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main changes:

- Roadmap now prioritizes trust/recall, Scrub Key security, placeholder robustness, hidden document hygiene, document-centric review, local runtime and pilot validation before scale features.
- `RISK_REGISTER.md` now records false negatives, Scrub Key leakage, placeholder corruption, hidden document content, cloud-demo trust gap, Streamlit review UX ceiling, PDF limitation risk and status-monitoring dependency.
- `DECISION_LOG.md` now records accepted decisions around risk-driven sequencing, PDF TXT-only scope, Scrub Key sensitivity, Streamlit as prototype layer, documentation split and worker self-monitoring.
- `STATUS_MONITORING_RUNBOOK.md` defines how workers should check GitHub Actions and Hugging Face sync before asking for app verification.
- `RELEASE_NOTES.md` separates user-facing product capability notes from internal workpackage history.
- `WORKPACKAGES.md` now lists WP18-FIX as the active required next workpackage and identifies safe parallel work after WP18-FIX is green.

Validation:

- Tests: not required; documentation/governance-only update.
- GitHub Actions: not required unless documentation checks run automatically.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.

Intentionally not changed:

- No product code changed.
- No tests changed.
- No dependencies changed.
- No UI changed.
- No OCR added.
- No PDF output added.
- No AI/cloud behavior added.
- No export/download semantics changed.
- No Scrub Key import/export behavior changed.

Next recommended step:

- Continue with `WP18-FIX — Fix failing PDF text to TXT UI tests`.
- After WP18-FIX is green, perform WP18 app verification and then WP18B closeout.
- After WP18 is closed, safe parallel tracks are WP19, WP25, WP30, WP35, WP45, WP50, WP56 and WP57.

## WP18 — PDF text extraction to restored TXT UI implementation

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Purpose:

- Expose the existing WP16 PDF text helper safely in the UI.
- Add only PDF upload → local selectable-text extraction → deterministic Scrub Key reinsert → restored TXT preview/download.
- Keep the feature inside `Originele waarden terugzetten` only.
- Keep `Anonimiseren` unchanged.
- Preserve all PDF boundaries: no restored PDF output, no OCR, no PDF-to-DOCX reconstruction, no cloud PDF conversion and no AI-based extraction.

Files added:

- `fix_streamlit_pdf_text_reinsert.py`
- `tests/test_pdf_text_reinsert_ui_patch.py`
- `handover/workpackages/20260609_1215_pdf_text_to_restored_txt_ui.md`

Files changed:

- `Dockerfile`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main changes:

- Added a second startup patch that runs after `fix_streamlit_nested_expanders.py`.
- The patch imports and uses `reinsert_pdf_text_bytes(content, scrub_key)` from the existing WP16 helper.
- Added a new UI section titled `PDF-tekst terugzetten naar TXT` inside `Originele waarden terugzetten`.
- Added PDF uploader with label `Upload een PDF-bestand met placeholders`.
- Added action button `Zet PDF-tekst lokaal terug`.
- Added restored TXT preview label `Herstelde TXT-tekst uit PDF`.
- Added download button label `Download herstelde TXT uit PDF (.txt)`.
- Added audit section `Controleverslag PDF-tekst terugzetten`.
- Added visible local/no-AI/no-cloud/no-OCR/no-PDF-output indicators.
- Added clear unsupported-case handling for no usable selectable text.
- Download is shown only when there are no validation issues, no unsupported reason and restored text is available.
- `Dockerfile` now runs both startup patches and installs `pypdf` in the runtime image so the existing WP16 helper dependency is available to the app.

Tests:

- Added `tests/test_pdf_text_reinsert_ui_patch.py`.
- Test coverage includes helper usage, UI labels, warnings, audit fields, local/no-AI/no-cloud/no-OCR/no-PDF-output indicators, PDF-only upload, required Scrub Key, unsupported-case handling and no forbidden PDF/OCR/AI/cloud behavior.

Validation:

- Repository pytest execution was not available in this connector session.
- Recommended tests after commit:
  - `PYTHONPATH=. pytest -q tests/test_pdf_text_reinsert_ui_patch.py`
  - `PYTHONPATH=. pytest -q tests/test_two_mode_ui_patch.py`
  - `PYTHONPATH=. pytest -q tests/test_txt_reinsert_ui_patch.py`
  - `PYTHONPATH=. pytest -q tests/test_docx_reinsert_ui_patch.py`
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_pdf_text_reinsert.py`
- GitHub Actions: awaiting verification.
- Hugging Face sync: awaiting verification.
- App verification: required after Actions/sync are green because UI behavior changed.

Intentionally not changed:

- No direct edit to `presidio_streamlit.py`.
- No change to `scrub_key_pdf_text_reinsert.py`.
- No change to `scrub_key_reinsert.py`.
- No change to `scrub_key_import.py`.
- No change to `requirements.txt`.
- No change to `PDF_TEXT_REINSERT_UI_PLAN.md`.
- No restored PDF output added.
- No OCR added.
- No PDF-to-DOCX reconstruction added.
- No cloud PDF conversion added.
- No AI-based extraction added.
- No layout preservation promises added.
- No batch PDF processing added.
- No real-data PDF test cases added.
- No automatic PDF rehydration added.
- No existing pasted-text, TXT or DOCX reinsert semantics changed.
- No Scrub Key import/export behavior changed.
- No existing scrubbed export/download semantics changed.

Next recommended step:

- Continue with `WP18-FIX — Fix failing PDF text to TXT UI tests`.

## WP17B — Roadmap current-status reconciliation after WP17

Status: completed documentation-only update.

Purpose:

- Reconcile stale `ROADMAP.md` wording after WP17.
- Align `ROADMAP.md`, `WORKPACKAGES.md` and `CHANGELOG.md` with the current source-of-truth status.
- Record that WP16 / WP16-FIX / WP16B are completed after Actions/sync verification, with app verification not applicable.
- Record that WP17 is completed planning/specification-only.
- Record that WP18 is the current next possible workpackage, but only after explicit approval.

## WP17 — PDF text extraction reinsert UI planning only

Status: completed planning/specification-only.

Planning conclusion:

- PDF text extraction may be exposed in the future UI only as text-based PDF extraction to restored TXT output.
- The future UI must live only in `Originele waarden terugzetten`.
- The PDF text workflow must not appear in `Anonimiseren`.
- DOCX remains the preferred document-level reinsert route.
- The future workflow should be PDF upload → local text extraction → restored TXT preview/download only.
- Strong PDF limitation warnings are required.
- The future UI must warn that restored output may contain sensitive/confidential values again.
- Scanned/image-only PDFs remain unsupported because OCR is not available.
- Scrub must not offer restored PDF output.
- Unsupported PDF cases must show clear messages and must not silently succeed.
- Required audit fields are specified in `PDF_TEXT_REINSERT_UI_PLAN.md`.

## WP16B — Text-based PDF extraction helper spike verification and closeout

Status: completed closeout-only.

Closeout result:

- WP16 / WP16-FIX is verified.
- WP16 added the helper-only text-based PDF extraction path.
- WP16-FIX fixed the failing tests by making `pypdf` optional/import-safe.
- Tests #198–#201 are green based on coordinator evidence.
- Sync #212–#215 is green based on coordinator evidence.
- App verification is not applicable because no UI behavior changed.

## WP16C — Roadmap status reconciliation after v13.8 and PDF helper line

Status: completed documentation-only update.

## WP16-FIX — Fix failing PDF text helper tests

Status: completed after Actions/sync verification; app verification not applicable.

## WP16 — Text-based PDF extraction helper spike, restored TXT output only

Status: completed after Actions/sync verification; app verification not applicable.

Implemented behavior:

- Added `extract_text_from_pdf_bytes(content)`.
- Added `reinsert_pdf_text_bytes(content, scrub_key)`.
- Text-based PDFs can be extracted locally when `pypdf` is installed.
- Extracted text is fed into the existing deterministic Scrub Key reinsert path.
- Restored output is text/TXT only.
- No PDF bytes are produced.
- Blank/no-text PDFs are clearly marked unsupported.
- Audit fields include local-only, no-AI, no-cloud, OCR-not-used and PDF-output-false indicators.

## WP15 — PDF text extraction reliability review only

Status: completed review/specification only.

Review conclusion:

- Do not implement full PDF reinsert now.
- Do not implement OCR now.
- Restored PDF output remains out of scope.
- PDF-to-DOCX reconstruction remains out of scope.
- DOCX remains the preferred document-level reinsert path.
- A future helper-only package may evaluate text-based PDF extraction to restored TXT output.

## Earlier completed work

- v13.8 DOCX reinsert upload/download UI.
- v13.7 TXT reinsert upload/download UI.
- v13.6 two-mode UI.
- v13.3 deterministic reinsert UI.
- v13 Scrub Key foundation and import/export work.
- v12 Review UX line.
