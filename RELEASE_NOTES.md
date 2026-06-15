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

- The review flow has one central side-by-side review surface near the top of the review workflow.
- The side-by-side review surface uses one section heading: `2. Controleer de tekst`.
- `Brontekst` appears on the left and `Verwerkte tekst` on the right.
- The side-by-side panes use equal visual height.
- The side-by-side panes scroll together by default.
- A short note explains that visual alignment can differ when source and processed text differ structurally.
- Markers are on by default and can be hidden with `Markeringen tonen`.
- The section `Controleer gevonden gegevens` is visually quieter: the replacement table is now under a collapsed `Vervangtabel controleren — <items> items` section.
- The replacement table remains the source of truth and fallback for review decisions and export construction.
- Serial review remains available as a small read-only review aid below the replacement table.
- Markers are visual-only. They do not change the replacement table, export, Scrub Key or reinsert behavior.

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
- Side-by-side synchronized scrolling is percentage-based and can still create imperfect alignment when source and processed text differ structurally.
- The review table remains the source of truth and fallback.
- The side-by-side review surface does not implement click-to-mark, an advanced editor or full-document marking.
- DOCX metadata, comments, tracked changes, headers and footers require further document-hygiene work.
- Detection quality needs formal recall/precision benchmarking before strong trust claims can be made.

---

## Upcoming focus

The roadmap prioritizes MVP product quality across:

```text
Import → Scrub → Review → Replace → Scrub Key → Reinsert → Export → Audit
```

Local installer work remains later, after the core workflow is good enough.
