## 2026-06-23 20:43 Europe/Amsterdam — Reinsert interface simplified

## 2026-06-23 — SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE

- Fixed DOCX plain-text extraction order for side-by-side preview.
- DOCX body paragraphs and tables are now read in document XML order instead of all paragraphs first and all tables afterwards.
- Added synthetic regression coverage for interleaved paragraph/table order.
- Preserved DOCX export, Scrub Key and reinsert semantics.
- Validation: `python -m pytest tests -x -vv` → 649 passed in 102.51s.

- The “Originele waarden terugzetten” workflow is now presented as a clearer four-step flow:
  1. Voeg Scrub Key toe
  2. Voeg tekst of document toe
  3. Controleer herstelrapport
  4. Download herstelde output
- Existing safety controls remain in place: Scrub Key warnings, acknowledgement gates and restored-output warnings.
- Existing restored output semantics remain unchanged: filenames, MIME types and supported output types are preserved.
- PDF reinsert remains TXT-only: no restored PDF, no OCR, no cloud processing and no AI processing.


# SolidPrivacy Scrub — Release Notes

## Execution interface simplification

- The default Scrub flow is calmer and more execution-oriented: add document/text, check result, export result.
- Secondary controls remain available but are collapsed by default.
- Primary document downloads remain visible; Scrub Key and audit downloads are separated into optional sections.
- No export, Scrub Key, reinsert or recognition behavior was changed.


This file is the user-facing product changelog.

For internal workpackage history, see `CHANGELOG.md` and `handover/workpackages/`.

---

## Current prototype capabilities

### Scrub / anonymize

- Upload and process supported document text flows in the Streamlit prototype.
- Review detected replacement candidates before export.
- Add a missed value manually with `Gemiste waarde toevoegen` so it enters the existing replacement table before export.
- Preserve legal/professional context where possible.
- Nederlandse juridische referenties zoals dossier-, zaak-, cliënt- en administratieve referentiecodes worden beter als review-kandidaat zichtbaar gemaakt wanneer automatische herkenning ze mist.
- Juridische rolwoorden blijven beter behouden als juridische context; Scrub doet geen claim dat alle juridische nummers altijd automatisch worden herkend.
- Export scrubbed outputs according to existing app behavior.

### Review

- The review flow has one central side-by-side review surface near the top of the review workflow.
- The side-by-side review surface uses one section heading: `2. Controleer resultaat`.
- `Brontekst` appears on the left and `Verwerkte tekst` on the right.
- The side-by-side panes use equal visual height.
- The side-by-side panes scroll together by default.
- The side-by-side helper text is shorter and clearer: it says that this view is for comparison and that decisions are still made in the replacement table.
- Markers are on by default and can be hidden with `Markeringen tonen`.
- Users can add a missed value manually near `2. Controleer resultaat`; it is added to the same replacement table used for export.
- The detailed replacement-table section is visually quieter: the replacement table is now under a collapsed `Vervangtabel controleren — <items> items` section.
- The replacement table remains the source of truth and fallback for review decisions and export construction.
- Serial review remains available as a small read-only review aid below the replacement table, with clearer Dutch labels for open items, risk items, duplicate values and next open item.
- Markers are visual-only. They do not change the replacement table, export, Scrub Key or reinsert behavior.

### Export

- Improved the export/download section by grouping document downloads, Scrub Key and audit/technical files more clearly.
- Existing export content, filenames and file types remain unchanged.
- The Scrub Key remains sensitive because it can restore original values.

### Scrub Key

- Export a Scrub Key JSON mapping file.
- Import/reload a Scrub Key for controlled reinsert.
- Clear warnings are shown because the Scrub Key can restore confidential values.
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
- UI acknowledgements are safety prompts, not managed key storage.
- Side-by-side synchronized scrolling is percentage-based and can still create imperfect alignment when source and processed text differ structurally.
- The review table remains the source of truth and fallback.
- The side-by-side review surface does not implement direct marking in the document text, an advanced editor or full-document marking.
- DOCX metadata, comments, tracked changes, headers and footers require further document-hygiene work.
- Detection quality needs formal recall/precision benchmarking before strong trust claims can be made.

---

## Upcoming focus

The roadmap prioritizes MVP product quality across:

```text
Import → Scrub → Review → Handmatig aanvullen → Replace → Scrub Key → Reinsert → Export → Audit
```

Local installer work remains later, after the core workflow is good enough.