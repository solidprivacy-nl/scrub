# SolidPrivacy Scrub — Workpackages

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Repository: `solidprivacy-nl/scrub`.

## Current status

WP0 through WP13B are complete.

## WP14 / WP14B / WP14C — v13.8 DOCX reinsert upload/download UI

Status: completed and app-verified after Actions/sync verification.

WP14 implemented controlled DOCX upload/download reinsert in `Originele waarden terugzetten`, using the existing local helper `reinsert_docx_bytes(content, scrub_key)`.

Existing pasted-text reinsert and TXT reinsert remain available.

WP14B was recorded cautiously because explicit verification evidence was not available to that worker at the time.

WP14C reconciles the status after coordinator/user evidence was supplied.

## Technical verification evidence for WP14

Coordinator evidence:

```text
Tests #177 green — commit 22b7066
Sync to Hugging Face Space #191 green — commit 22b7066
Tests #178 green — commit 68379c6
Sync to Hugging Face Space #192 green — commit 68379c6
Tests #179 green — commit 03fd2cd
Sync to Hugging Face Space #193 green — commit 03fd2cd
Tests #180 green — commit 8651fc7
Sync to Hugging Face Space #194 green — commit 8651fc7
```

Latest WP14 implementation commit:

```text
8651fc7520cebc321b4b893557fce57afc314fe4
```

## App verification evidence for WP14

Coordinator/user evidence confirms DOCX reinsert upload/download works with a valid Scrub Key inside documented helper limits.

Also confirmed:

- No PDF reinsert appears.
- No AI/cloud behavior appears.
- Existing pasted-text reinsert remains available.
- Existing TXT reinsert remains available.
- Existing Scrub Key import/export remains available.
- Existing scrubbed export/download semantics remain unchanged.

## WP15 — PDF text extraction reliability review only

Status: completed review/specification only.

Added:

- `PDF_TEXT_EXTRACTION_RELIABILITY_REVIEW.md`
- `handover/workpackages/20260608_0115_pdf_text_extraction_reliability_review.md`

Changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Review conclusion:

- Do not implement full PDF reinsert now.
- Do not implement OCR now.
- Restored PDF output remains out of scope.
- DOCX remains the preferred document-level reinsert path.
- A future helper-only spike may evaluate text-based PDF extraction to restored TXT output.

Validation:

- Tests: not applicable; review-only workpackage.
- GitHub Actions: not required unless documentation checks exist.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.

## Active / next recommended workpackage

WP16 — Text-based PDF extraction helper spike, restored TXT output only.

Recommended WP16 scope:

- choose and justify a local PDF text extraction dependency;
- add a pure helper only;
- support text-based PDFs only;
- reject or clearly mark scanned/image-only PDFs as unsupported;
- feed extracted text into existing deterministic reinsert logic;
- output restored TXT only;
- add synthetic tests;
- do not add UI yet;
- do not add OCR;
- do not output PDF.

Keep explicitly out of scope:

- full restored PDF output;
- PDF-to-DOCX reconstruction;
- OCR;
- cloud PDF conversion;
- AI-based extraction;
- UI upload controls for PDF reinsert;
- automatic PDF rehydration;
- layout preservation promises;
- batch PDF processing;
- real-data PDF test cases.
