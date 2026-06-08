# Handover — WP15 — PDF text extraction reliability review only

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP15 — PDF text extraction reliability review only`

Status: completed review/specification only.

## Summary

WP15 reviewed whether PDF input can be safely supported in the reinsert workflow.

Conclusion:

- Do not implement full PDF reinsert now.
- Do not implement OCR now.
- Restored PDF output remains out of scope.
- DOCX remains the preferred document-level reinsert path.
- A future helper-only spike may evaluate text-based PDF extraction to restored TXT output.

No code files were changed.

## Files added

- `PDF_TEXT_EXTRACTION_RELIABILITY_REVIEW.md`
- `handover/workpackages/20260608_0115_pdf_text_extraction_reliability_review.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

No tests were added or changed.

Tests are not applicable because WP15 is review/specification-only.

## Validation status

- Required start sequence: completed.
- Dependency check: WP14/WP14B/WP14C is closed as completed and app-verified after Actions/sync verification.
- Code changes: none.
- UI changes: none.
- Dependency changes: none.

## GitHub Actions status

Not required unless documentation checks exist.

## Hugging Face sync status

Not functionally relevant because no app behavior changed.

## App verification status

Not applicable because no UI behavior changed.

## Remaining risks

- PDF text extraction can still be incomplete or misleading even if text-based.
- Scanned/image-only PDFs require OCR and remain out of scope.
- Future PDF support must not imply layout or completeness guarantees.
- Future tests must use synthetic data only.

## Next recommended step

`WP16 — Text-based PDF extraction helper spike, restored TXT output only`

Recommended WP16 boundaries:

- pure helper only;
- text-based PDFs only;
- local extraction;
- restored TXT output only;
- synthetic tests;
- no UI;
- no OCR;
- no AI calls;
- no cloud processing;
- no restored PDF output;
- no Scrub Key import/export behavior change;
- no scrubbed export/download behavior change.
