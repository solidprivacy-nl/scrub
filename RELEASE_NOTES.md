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
- Experimental marked document preview: for small texts, the app can show a read-only context preview before the replacement table.
- The marked preview is not authoritative. Users still make decisions in the replacement table.
- A visibility repair was added for the experimental marked preview after app verification showed the panel was not visible.

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
- The marked document preview is read-only and does not replace the replacement table.
- The marked preview still needs fresh app verification after the visibility repair is synced.
- DOCX metadata, comments, tracked changes, headers and footers require further document-hygiene work.
- Detection quality needs formal recall/precision benchmarking before strong trust claims can be made.

---

## Upcoming focus

The roadmap prioritizes MVP product quality across:

```text
Import → Scrub → Review → Replace → Scrub Key → Reinsert → Export → Audit
```

Local installer work remains later, after the core workflow is good enough.
