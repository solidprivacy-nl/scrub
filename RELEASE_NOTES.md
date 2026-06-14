# SolidPrivacy Scrub — Release Notes

This file is the user-facing product changelog.

For internal workpackage history, see `CHANGELOG.md` and `handover/workpackages/`.

---

## Current prototype capabilities

### Scrub / anonymize

- Upload and process supported document text flows in the Streamlit prototype.
- Review detected replacement candidates before export.
- Preserve legal/professional context where possible.
- Export scrubbed outputs according to existing app behavior.

### Review

- Review table and review guidance are available.
- Final review summary and export sanity checks help users understand remaining risk.
- The review area now includes a first side-by-side review surface: `Brontekst` on the left and `Verwerkte tekst` on the right.
- The side-by-side source and processed panes now use equal visual height.
- Long processed/highlighted text scrolls inside its own pane; synchronized scrolling is not implemented.
- The replacement table remains the source of truth and fallback.
- Serial review remains available as a small read-only review aid below the side-by-side comparison.
- The right-side processed pane includes an optional `Markeringen tonen in verwerkte tekst` toggle.
- When the toggle is off, the processed text remains calm and normally readable.
- When the toggle is on, already masked/replaced values can receive subtle visual markers in the processed pane.
- These markers are visual-only. They do not change the replacement table, export, Scrub Key or reinsert behavior.

### Scrub Key

- Export a Scrub Key JSON mapping file.
- Import/reload a Scrub Key for controlled reinsert.
- Clear warnings are shown because the Scrub Key can restore sensitive/confidential values.
- Scrub Key export and import now require an explicit acknowledgement before the high-risk action button is active.

### Reinsert

Supported reinsert paths:

```text
Pasted text → restored text
TXT upload  → restored TXT
DOCX upload → restored DOCX, within documented helper limits
PDF upload  → restored TXT only
```

- Pasted-text, TXT, DOCX and PDF-to-TXT reinsert actions now require acknowledgement that restored output is confidential again.
- Restored output download buttons now show an additional warning and acknowledgement before download.
- The restored output content, filenames and file types are unchanged after acknowledgement.

PDF support is intentionally limited:

- restored output is TXT only;
- no restored PDF output;
- no OCR;
- no PDF-to-DOCX reconstruction;
- no layout preservation guarantee;
- scanned/image-only PDFs are unsupported.

---

## Known important limitations

- The Hugging Face Space is a demo/development environment, not the final local confidential processing environment.
- The final product direction is local-first/offline capable.
- The Scrub Key is sensitive because it can re-identify scrubbed content.
- UI acknowledgements are safety prompts, not encryption, automatic deletion, expiry enforcement or managed key storage.
- The side-by-side review surface is a first bounded implementation and still needs app verification after Actions and Hugging Face sync are green.
- The side-by-side review surface does not implement synchronized scrolling, click-to-mark, an advanced editor or full-document marking.
- The review table remains the source of truth and fallback.
- DOCX metadata, comments, tracked changes, headers and footers require further document-hygiene work.
- Detection quality needs formal recall/precision benchmarking before strong trust claims can be made.

---

## Upcoming focus

The roadmap prioritizes MVP product quality across:

```text
Import → Scrub → Review → Replace → Scrub Key → Reinsert → Export → Audit
```

Local installer work remains later, after the core workflow is good enough.
