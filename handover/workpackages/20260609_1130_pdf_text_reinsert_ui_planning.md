# Handover — WP17 — PDF text extraction reinsert UI planning only

Repository: solidprivacy-nl/scrub  
Status: completed planning/specification-only

## Summary

WP17 created a safe future UI specification for exposing the WP16 PDF text extraction helper.

Planning conclusion:

- PDF text extraction may be exposed only as text-based PDF extraction to restored TXT output.
- The future UI must be placed only in `Originele waarden terugzetten`.
- The future UI must not appear in `Anonimiseren`.
- DOCX remains the preferred document-level reinsert route.
- The future workflow should be PDF upload → local text extraction → restored TXT preview/download only.
- Strong warnings are required for incomplete PDF extraction, no layout preservation, restored sensitive values, unsupported scanned/image-only PDFs, no OCR and TXT-only output.
- Required audit fields and unsupported cases are specified.
- Full restored PDF output, OCR, PDF-to-DOCX reconstruction, cloud PDF conversion and AI-based extraction remain out of scope.

No UI, code, tests, dependencies or export behavior were changed.

## Files added

- `PDF_TEXT_REINSERT_UI_PLAN.md`
- `handover/workpackages/20260609_1130_pdf_text_reinsert_ui_planning.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- Tests: not applicable; planning-only.
- No tests were added.
- No tests were changed.
- No local tests were run.

## Validation

- Validation status: completed as planning/specification-only.
- GitHub Actions: not required unless documentation checks run.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.

## GitHub Actions status

Not required for WP17 unless documentation checks run.

## Hugging Face sync status

Not functionally relevant because no app behavior changed.

## App verification status

Not applicable because no UI behavior changed.

## Boundaries preserved

- No code changed.
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
- No existing TXT/DOCX/pasted-text reinsert behavior changed.
- No existing scrubbed TXT/CSV/DOCX/PDF export/download behavior changed.
- No Scrub Key import/export behavior changed.
- No secrets, tokens or real personal data stored.

## Remaining risks

- PDF text extraction remains inherently unreliable for layout, reading order, headers, footers, columns and tables.
- Scanned/image-only PDFs remain unsupported because OCR is out of scope.
- The future UI could still create false confidence if warnings are weakened during implementation.
- Future implementation must avoid any wording that implies restored PDF output or legal completeness.
- Future implementation must keep restored output clearly separated from scrubbed export/download controls.

## Next recommended step

- WP18 — PDF text extraction to restored TXT UI implementation.

WP18 must be explicitly approved as a separate implementation workpackage before starting.

Recommended WP18 scope:

```text
Originele waarden terugzetten only
PDF upload
local text extraction via WP16 helper
restored TXT preview
restored TXT download
audit report
strong warnings
no PDF output
no OCR
no AI/cloud
```

Still out of scope unless separately approved:

- full restored PDF output;
- OCR;
- PDF-to-DOCX reconstruction;
- cloud PDF conversion;
- AI-based extraction;
- layout preservation promises;
- batch PDF processing;
- real-data PDF test cases;
- automatic PDF rehydration.
