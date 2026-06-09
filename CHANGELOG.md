# Changelog — SolidPrivacy Scrub

## WP18C — Add Codex worker governance instructions

Status: completed documentation/governance-only.

Purpose:

- Add repository-level worker instructions for Codex/agent execution.
- Make handover-by-file the default process for Codex workers.
- Reduce long handover copy-paste in the coordinator chat while preserving GitHub as source of truth.
- Prepare safe parallel execution of WP19, WP25, WP30 and WP35.

Files added:

- `AGENTS.md`
- `handover/workpackages/20260609_1330_codex_worker_governance.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main changes:

- `AGENTS.md` defines repository scope, required start sequence, safety rules, workpackage discipline, parallelization rules, testing/validation expectations, documentation updates and handover process.
- Codex workers must write full handovers to `handover/workpackages/`.
- Coordinator chat only needs handover path, commit/PR, status and short summary when the handover is committed to GitHub.
- Full handover copy-paste is only required if commit/GitHub access fails, there is a conflict, or the coordinator explicitly asks for it.
- `WORKPACKAGES.md` now records WP18C as completed and includes `AGENTS.md` in relevant start context.

Validation status:

- GitHub Actions: not checked; documentation/governance-only change.
- Hugging Face sync: not checked; documentation/governance-only change.
- App verification: not applicable.

Intentionally not changed:

- No code changed.
- No tests changed.
- No UI changed.
- No dependencies changed.
- No Dockerfile changed.
- No product behavior changed.
- No export/reinsert behavior changed.
- No Scrub Key behavior changed.

Next recommended step:

- Start the first four safe parallel Codex workpackages: WP19, WP25, WP30 and WP35.
- After those complete, run `WP58 — Parallel specification consolidation and next execution queue`.

## WP18B — PDF text to restored TXT UI app verification closeout

Status: completed closeout-only; WP18 completed and app-verified after Actions/sync verification.

Purpose:

- Close the WP18 PDF-to-restored-TXT UI line after coordinator/user approval for closeout.
- Record that WP18-FIX is resolved and the WP18 app verification gate is satisfied.
- Preserve the exact WP18 scope and all PDF safety boundaries.

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`

Files added:

- `handover/workpackages/20260609_1315_pdf_text_to_txt_ui_app_closeout.md`

Validation status:

- GitHub Actions: green based on coordinator/user closeout approval.
- Hugging Face sync: green based on coordinator/user closeout approval.
- App verification: confirmed by coordinator/user closeout approval.
- Connector note: direct connector lookup for the WP18-FIX handover commit returned no statuses and no workflow runs, so this closeout records coordinator/user evidence rather than direct connector evidence.

App verification scope recorded:

- `Originele waarden terugzetten` shows the new PDF-to-TXT section.
- `Anonimiseren` does not show the PDF reinsert section.
- A valid Scrub Key can be loaded.
- A text-based PDF with placeholders can be uploaded.
- PDF text can be restored locally to TXT.
- Restored TXT preview appears.
- Restored TXT download appears.
- Audit report appears.
- UI clearly says no OCR, no AI, no cloud and no PDF output.
- Scanned/image-only PDFs are rejected or clearly marked unsupported.
- Existing pasted-text, TXT and DOCX reinsert still work.
- Existing anonymization/export behavior is unchanged.

Intentionally not changed:

- No code changed.
- No tests changed.
- No UI changed.
- No dependencies changed.
- No direct edit to `presidio_streamlit.py`.
- No OCR added.
- No restored PDF output added.
- No PDF-to-DOCX reconstruction added.
- No AI/cloud extraction added.
- No layout reconstruction added.
- No batch PDF processing added.
- No real-data tests added.
- No automatic PDF rehydration added.
- No existing pasted-text/TXT/DOCX reinsert semantics changed.
- No existing anonymization/export semantics changed.
- No Scrub Key import/export behavior changed.

Next recommended step:

- The WP18 UI line is closed.
- Safe parallel next workpackages: WP19, WP25, WP30, WP35, WP45, WP50, WP56, WP57.
- Recommended first risk-driven next package: `WP19 — Recall benchmark specification`.

## WP18-FIX — Fix failing PDF text to TXT UI tests

Status: completed after Actions/sync verification; WP18 app verification completed.

Root cause:

- WP18 implemented the PDF-to-restored-TXT UI, but GitHub Actions tests were red in coordinator evidence.
- `STATUS_MONITORING_RUNBOOK.md` was followed where connector permissions allowed.
- Commit-to-workflow lookup returned no workflow runs for the relevant WP18 commits.
- The visible run numbers #220–#223 were not accepted by the connector as workflow run IDs or job IDs, so failing job logs could not be fetched via connector.
- Based on inspection/reconstruction, the failure was in `tests/test_pdf_text_reinsert_ui_patch.py`: the test used a brittle expectation around the triple-quoted `else:` insertion marker.

Fix applied:

- Updated only `tests/test_pdf_text_reinsert_ui_patch.py`.
- The test now checks the actual real-newline `else:` marker form used by `fix_streamlit_pdf_text_reinsert.py`.
- No product behavior, UI behavior, Docker startup behavior, helper code or dependency behavior was changed.

Files changed:

- `tests/test_pdf_text_reinsert_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Files added:

- `handover/workpackages/20260609_1245_pdf_text_to_txt_ui_tests_fix.md`

Intentionally not changed:

- No `presidio_streamlit.py` direct edit.
- No `fix_streamlit_pdf_text_reinsert.py` functional change.
- No `Dockerfile` change.
- No helper code changed.
- No dependency change.
- No OCR added.
- No restored PDF output added.
- No PDF-to-DOCX reconstruction added.
- No AI/cloud extraction added.
- No layout reconstruction added.
- No batch PDF processing added.
- No real-data tests added.
- No automatic PDF rehydration added.
- No existing pasted-text/TXT/DOCX reinsert semantics changed.
- No existing anonymization/export semantics changed.
- No Scrub Key import/export behavior changed.

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

## WP18 — PDF text extraction to restored TXT UI implementation

Status: completed and app-verified after Actions/sync verification.

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

## WP17B — Roadmap current-status reconciliation after WP17

Status: completed documentation-only update.

## WP17 — PDF text extraction reinsert UI planning only

Status: completed planning/specification-only.

## WP16B — Text-based PDF extraction helper spike verification and closeout

Status: completed closeout-only.

## WP16-FIX — Fix failing PDF text helper tests

Status: completed after Actions/sync verification; app verification not applicable.

## WP16 — Text-based PDF extraction helper spike, restored TXT output only

Status: completed after Actions/sync verification; app verification not applicable.

## WP15 — PDF text extraction reliability review only

Status: completed review/specification only.

## Earlier completed work

- v13.8 DOCX reinsert upload/download UI.
- v13.7 TXT reinsert upload/download UI.
- v13.6 two-mode UI.
- v13.3 deterministic reinsert UI.
- v13 Scrub Key foundation and import/export work.
- v12 Review UX line.
