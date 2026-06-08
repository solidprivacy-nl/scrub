# Changelog — SolidPrivacy Scrub

## WP15 — PDF text extraction reliability review only

Status: completed review/specification only.

Purpose:

- Evaluate whether PDF input can be supported safely and reliably in the reinsert workflow.
- Challenge whether Scrub should support PDF reinsert at all.
- Keep this as review-only with no code, UI, dependency or export behavior changes.

Files added:

- `PDF_TEXT_EXTRACTION_RELIABILITY_REVIEW.md`
- `handover/workpackages/20260608_0115_pdf_text_extraction_reliability_review.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Review conclusion:

- Do not implement full PDF reinsert now.
- Do not implement OCR now.
- Restored PDF output remains out of scope.
- PDF-to-DOCX reconstruction remains out of scope.
- DOCX remains the preferred document-level reinsert path.
- A future helper-only package may evaluate text-based PDF extraction to restored TXT output.

Recommended next phase:

```text
WP16 — Text-based PDF extraction helper spike, restored TXT output only
```

Recommended WP16 boundaries:

- pure helper only;
- text-based PDFs only;
- local deterministic extraction;
- restored TXT output only;
- synthetic tests only;
- no UI;
- no OCR;
- no AI calls;
- no cloud processing;
- no restored PDF output;
- no Scrub Key import/export behavior change;
- no scrubbed export/download behavior change.

Validation:

- Tests: not applicable; review-only workpackage.
- GitHub Actions: not required unless documentation checks exist.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.

## WP14C — v13.8 DOCX reinsert upload/download UI final verification reconciliation

Status: completed.

WP14 DOCX reinsert UI is completed and app-verified after Actions/sync verification.

Technical verification and app verification were supplied by coordinator/user.

## WP14B — v13.8 DOCX reinsert upload/download UI app verification closeout

Status: superseded by WP14C final reconciliation.

## WP14 — v13.8 DOCX reinsert upload/download UI

Status: completed and app-verified after Actions/sync verification.

WP14 added controlled DOCX upload/download reinsert in `Originele waarden terugzetten` using `reinsert_docx_bytes(content, scrub_key)`.

Existing pasted-text reinsert and TXT reinsert remain available.

DOCX limitations remain visible in the UI.

## WP13B — v13.7 TXT reinsert upload/download UI app verification closeout

Status: completed and app-verified after Actions/sync verification.

## Earlier completed work

- v13.7 TXT reinsert upload/download UI.
- v13.6 two-mode UI.
- v13.3 deterministic reinsert UI.
- v13 Scrub Key foundation and import/export work.
- v12 Review UX line.
- Earlier Dutch Legal UI and recognizer work.

## Planned later phase

- WP16 — Text-based PDF extraction helper spike, restored TXT output only.
