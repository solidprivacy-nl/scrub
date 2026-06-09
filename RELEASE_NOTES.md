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

### Reinsert

Supported reinsert paths:

```text
Pasted text → restored text
TXT upload  → restored TXT
DOCX upload → restored DOCX, within documented helper limits
PDF upload  → restored TXT only, pending WP18 verification
```

PDF support is intentionally limited:

- no restored PDF output;
- no OCR;
- no PDF-to-DOCX reconstruction;
- no layout preservation guarantee;
- scanned/image-only PDFs are unsupported;
- PDF-to-TXT UI is pending WP18 test/app verification.

---

## Known important limitations

- The Hugging Face Space is a demo/development environment, not the final local confidential processing environment.
- The final product direction is local-first/offline capable.
- The Scrub Key is sensitive because it can re-identify scrubbed content.
- DOCX metadata, comments, tracked changes, headers and footers require further document-hygiene work.
- Detection quality needs formal recall/precision benchmarking before strong trust claims can be made.

---

## Upcoming focus

After WP18 is fixed and verified, the roadmap prioritizes:

1. recall and trust benchmarking;
2. Scrub Key security and lifecycle;
3. placeholder robustness for AI roundtrip;
4. hidden document content and metadata hygiene;
5. document-centric review UX;
6. local-first runtime;
7. pilot validation for Legal and Zorg.
