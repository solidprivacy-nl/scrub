# Changelog — SolidPrivacy Scrub

## WP17B — Roadmap current-status reconciliation after WP17

Status: completed documentation-only update.

Purpose:

- Reconcile stale `ROADMAP.md` wording after WP17.
- Align `ROADMAP.md`, `WORKPACKAGES.md` and `CHANGELOG.md` with the current source-of-truth status.
- Record that WP16 / WP16-FIX / WP16B are completed after Actions/sync verification, with app verification not applicable.
- Record that WP17 is completed planning/specification-only.
- Record that WP18 is the current next possible workpackage, but only after explicit approval.

Files changed:

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Files added:

- `handover/workpackages/20260609_1200_roadmap_status_reconciliation_after_wp17.md`

Validation:

- Tests: not required; documentation-only update.
- GitHub Actions: not required unless documentation checks run automatically.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.
- Edited files were manually checked for internal consistency.

Intentionally not changed:

- No code files changed.
- No tests changed.
- No dependencies changed.
- No UI changed.
- No OCR added.
- No PDF output added.
- No PDF-to-DOCX reconstruction added.
- No cloud PDF conversion added.
- No AI-based extraction added.
- No layout preservation promises added.
- No batch PDF processing added.
- No real-data PDF test cases added.
- No automatic PDF rehydration added.
- No export/download semantics changed.
- No Scrub Key import/export behavior changed.

Next recommended step:

- WP18 — PDF text extraction to restored TXT UI implementation.
- WP18 has not started.
- WP18 must not start unless explicitly approved as a separate implementation workpackage.

## WP17 — PDF text extraction reinsert UI planning only

Status: completed planning/specification-only.

Purpose:

- Create a safe future UI specification for exposing the WP16 PDF text extraction helper.
- Decide whether PDF support should appear in the UI and under which boundaries.
- Keep implementation, UI changes, code changes, tests and dependencies out of scope.

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

Validation:

- Tests: not applicable; planning-only.
- GitHub Actions: not required unless documentation checks run.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.

Intentionally not changed:

- No code files changed.
- No tests changed.
- No UI changed.
- No dependencies changed.
- No OCR added.
- No PDF output added.
- No PDF-to-DOCX reconstruction added.
- No cloud PDF conversion added.
- No AI-based extraction added.
- No layout preservation promises added.
- No batch PDF processing added.
- No real-data PDF test cases added.
- No automatic PDF rehydration added.
- No existing export/download semantics changed.
- No existing scrubbed TXT/CSV/DOCX/PDF export/download behavior changed.
- No existing pasted-text, TXT or DOCX reinsert behavior changed.
- No Scrub Key import/export behavior changed.

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

Purpose:

- Refresh `ROADMAP.md` because it still described v12 as the current line and v13 as the next strategic phase.
- Align roadmap status with `WORKPACKAGES.md` and `CHANGELOG.md` after v13.8, WP15 and WP16/WP16-FIX.

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

## Planned later phase

- WP18 — PDF text extraction to restored TXT UI implementation, only if explicitly approved as a separate implementation workpackage.
