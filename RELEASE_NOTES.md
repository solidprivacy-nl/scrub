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
- scanned/image-only PDFs are unsupported;
- the UI must clearly show no OCR, no AI, no cloud and no PDF output.

---

## Known important limitations

- The Hugging Face Space is a demo/development environment, not the final local confidential processing environment.
- The final product direction is local-first/offline capable.
- The Scrub Key is sensitive because it can re-identify scrubbed content.
- UI acknowledgements are safety prompts, not encryption, automatic deletion, expiry enforcement or managed key storage.
- DOCX metadata, comments, tracked changes, headers and footers require further document-hygiene work.
- Detection quality needs formal recall/precision benchmarking before strong trust claims can be made.
- PDF text extraction depends on a usable selectable-text layer and may lose layout, tables, columns, headers, footers and visual reading order.

---

## Upcoming focus

After the verified PDF-to-restored-TXT UI line, the roadmap prioritizes:

1. recall and trust benchmarking;
2. Scrub Key security and lifecycle;
3. placeholder robustness for AI roundtrip;
4. hidden document content and metadata hygiene;
5. document-centric review UX;
6. local-first runtime;
7. pilot validation for Legal and Zorg.
