# WP35 — DOCX hidden content risk review

Status: completed document-hygiene/specification-only.  
Repository: `solidprivacy-nl/scrub`.  
Scope: risk review and future specification only; no DOCX parser change, cleaner implementation, UI change, dependency change, test change or export semantics change.

---

## 1. Purpose

This review defines hidden DOCX content and metadata leakage risks for SolidPrivacy Scrub.

The core risk is:

```text
A DOCX file may still contain sensitive data outside the visible body text that Scrub currently processes or restores.
```

This matters because a professional user may believe a document is safe after visible text is scrubbed, while sensitive data remains in metadata, comments, tracked changes, headers, footers, footnotes, text boxes, custom XML or other package parts.

WP35 does not change behavior. It defines the policy boundary and the sequence for later workpackages.

---

## 2. Current DOCX support assumptions

The current document-level DOCX helper assumes a deliberately limited foundation scope:

```text
DOCX package → word/document.xml → WordprocessingML text nodes → deterministic placeholder reinsert → restored DOCX package
```

Current assumptions:

- processing is local;
- no AI or cloud processing is used;
- only `word/document.xml` text nodes are processed;
- normal body paragraphs in `word/document.xml` are covered;
- tables inside `word/document.xml` are covered because table text also uses WordprocessingML text nodes;
- the helper preserves the package structure by replacing only `word/document.xml` with a rewritten XML part;
- all other DOCX package parts are copied through unchanged;
- split-run placeholders are not restored if the placeholder text is divided across multiple Word runs/text nodes;
- headers, footers, comments, tracked changes and metadata are not processed in the current foundation version.

These assumptions are acceptable for the existing DOCX reinsert helper only because the UI and audit text already communicate limitations. They are not sufficient for future safe DOCX export or professional trust claims.

---

## 3. Policy distinction

Future DOCX hygiene work must keep these policies separate:

| Policy area | Meaning | Future behavior direction |
|---|---|---|
| Scrubbing visible body text | Detecting/replacing sensitive values in the main visible document body. | Supported first; must remain reviewable. |
| Scrubbing hidden document content | Detecting/replacing sensitive values in non-body parts such as headers, comments or footnotes. | Requires explicit extraction, review and audit support before claiming coverage. |
| Cleaning metadata | Removing or replacing package/core/custom properties and authoring metadata. | Separate cleaner helper; should not depend on recognizer accuracy alone. |
| Warning about unsupported content | Informing the user that unsupported parts may contain sensitive data. | Required when unsupported parts are present or cannot be inspected. |
| Blocking export when risk is too high | Preventing or requiring explicit confirmation before export. | Must be a separate policy decision; not silently changed in WP35. |

WP35 does not silently change export semantics. Any future blocking behavior must be introduced by a dedicated workpackage with tests, UI copy and explicit approval.

---

## 4. Normal document text coverage

Normal visible DOCX body text usually lives in:

```text
word/document.xml
```

Within that XML part, text is stored in `w:t` nodes. Current DOCX reinsert support can process these nodes.

Risk level: medium.

Reason:

- body text is the most visible and reviewable area;
- current helper covers straightforward paragraphs;
- however, Word may split values or placeholders across multiple runs because of formatting, spellcheck, track changes or copy/paste history.

Future requirements:

- audit how many `w:t` nodes were inspected;
- report whether placeholders were split across adjacent runs;
- avoid claiming full DOCX coverage when only `word/document.xml` was processed;
- keep value replacement separate from metadata cleaning.

---

## 5. Table coverage

Tables in the main document body are also stored in `word/document.xml`. Their text usually appears in `w:t` nodes within table structures.

Risk level: medium.

Current coverage:

- normal table text in `word/document.xml` is covered by the current helper;
- table layout, merged cells and visual reading order are not semantically interpreted;
- table text may be fragmented across many runs.

Future requirements:

- report table presence in the audit;
- report that table text was inspected as body text, not layout-reconstructed;
- test synthetic tables containing split placeholders and legal/care identifiers;
- avoid promising that visual table order equals extracted text order.

---

## 6. Headers and footers risk

Headers and footers commonly contain names, matter numbers, client numbers, version labels, office names and page-level confidentiality markings.

Typical DOCX parts:

```text
word/header*.xml
word/footer*.xml
```

Risk level: high.

Leakage examples:

- `Dossier: ARB-2026-00421` in every header;
- client name in a footer;
- law firm or care organization with matter reference;
- old case number in a template header.

Future requirements:

- detect and audit whether header/footer parts exist;
- extract their text for review before claiming full-document coverage;
- either scrub them or warn clearly that they are unsupported;
- never copy unsupported header/footer content into a supposedly clean export without visible risk reporting.

---

## 7. Comments risk

Comments may contain reviewer names, initials, client names, internal legal strategy, medical/care notes or unresolved review discussion.

Typical DOCX parts:

```text
word/comments.xml
word/commentsExtended.xml
word/person.xml
```

Risk level: high.

Leakage examples:

- lawyer comment: `Check BSN 123456782 with client`;
- care review note naming a resident;
- comment author metadata exposing employee names;
- old redline discussion preserved in comment history.

Future requirements:

- audit comment parts and comment author/person metadata;
- decide whether comments should be scrubbed, removed, or block export;
- treat comments as potentially sensitive even when not visible in body text;
- add synthetic tests before implementation.

Recommended policy direction:

```text
Before a cleaner exists, warn if comments are present.
For clean export later, remove comments by default unless a separate reviewed-comment export mode is approved.
```

---

## 8. Tracked changes risk

Tracked changes can preserve deleted text, inserted text, author names and timestamps. Sensitive data may remain even when it is visually deleted from the accepted document view.

Typical locations:

```text
word/document.xml
word/header*.xml
word/footer*.xml
word/footnotes.xml
word/endnotes.xml
```

Common XML elements include insertions and deletions such as `w:ins` and `w:del`.

Risk level: critical.

Leakage examples:

- deleted client name remains in a `w:delText` node;
- previous address remains in tracked deletion;
- author metadata reveals staff names;
- tracked edits in headers or footnotes contain old case details.

Future requirements:

- audit presence of tracked-change elements across all relevant XML parts;
- decide whether to accept, reject, remove, or block documents with tracked changes;
- surface this risk before export;
- do not rely only on visible text extraction.

Recommended policy direction:

```text
Tracked changes should usually block clean-export claims until a safe accept/remove policy exists.
```

---

## 9. Metadata risk

DOCX metadata may expose authors, last modified by, company, title, subject, keywords, template names, revision numbers, timestamps, custom properties and application-specific data.

Typical DOCX parts:

```text
docProps/core.xml
docProps/app.xml
docProps/custom.xml
```

Risk level: high.

Leakage examples:

- author name or employee account;
- client name in document title;
- law firm matter number in subject or keywords;
- care location in company/custom properties;
- template path or revision history.

Future requirements:

- create a metadata cleaner helper in WP36;
- define which fields are removed, replaced, or preserved;
- audit metadata before and after cleaning;
- avoid using cloud metadata services;
- avoid storing real metadata examples in tests.

Recommended policy direction:

```text
Clean export should remove or neutralize identifying metadata by default.
```

---

## 10. Custom XML risk

Custom XML parts can store hidden application data, form fields, add-in data, case-management metadata, document variables or copied source data.

Typical DOCX package areas:

```text
customXml/
word/_rels/*.rels
```

Risk level: high.

Leakage examples:

- client ID stored by a document automation system;
- case-management reference in custom XML;
- hidden structured data copied from a template;
- add-in data with user or organization identifiers.

Future requirements:

- audit the presence of `customXml/` parts;
- decide whether to remove custom XML by default for clean exports;
- warn if custom XML is present and no cleaner is active;
- preserve only parts required for a valid, intentionally supported output.

Recommended policy direction:

```text
For clean export, remove custom XML unless a specific safe-use case is documented and tested.
```

---

## 11. Footnotes and endnotes risk

Footnotes and endnotes can contain names, case citations, matter references, medical notes or source references that identify people or cases.

Typical DOCX parts:

```text
word/footnotes.xml
word/endnotes.xml
```

Risk level: high.

Leakage examples:

- footnote with client name;
- endnote containing a full ECLI and party details;
- medical/care reference in a note;
- previous draft note preserved outside the body.

Future requirements:

- detect footnote/endnote parts;
- extract note text for review if full-document coverage is claimed;
- report unsupported note content in audit;
- add tests before any helper implementation.

---

## 12. Text boxes and shapes risk

DOCX files can contain text in shapes, text boxes, SmartArt, drawing objects, charts or embedded objects. These may not be represented as ordinary body paragraphs.

Typical locations include XML under:

```text
word/document.xml
word/drawings/
word/charts/
word/embeddings/
```

Risk level: high.

Leakage examples:

- client name in a text box on a cover page;
- matter number in a watermark-like shape;
- organization chart with staff names;
- embedded spreadsheet or object containing real data.

Future requirements:

- audit presence of drawings, shapes, charts and embedded objects;
- identify text-bearing shapes where feasible;
- warn or block clean-export claims when unsupported embedded objects are present;
- keep embedded-object handling out of scope until separately specified.

---

## 13. Split-run placeholder risk

Word often splits text across multiple runs because of formatting, spellcheck, revision marks or copy/paste history. A placeholder like:

```text
[PERSOON_1]
```

may be stored as:

```text
w:t [PERS
w:t OON_1]
```

Risk level: high for reinsert reliability; medium-to-high for scrubbed output trust.

Current behavior:

- split-run placeholders are not restored by the current helper;
- audit may show placeholders not found because exact placeholder strings do not exist in a single text node;
- visible document text may look correct to a user while XML storage prevents deterministic replacement.

Future requirements:

- detect split-run placeholder candidates across adjacent text nodes;
- report them in audit as `split_placeholder_candidates` or similar;
- never silently guess original intent when the placeholder is ambiguous;
- coordinate with WP31/WP32 placeholder robustness work before changing placeholder format or repair logic.

---

## 14. Audit requirements

Future DOCX hygiene audit output should report at minimum:

| Audit field | Meaning |
|---|---|
| `docx_parts_seen` | Number/list of DOCX package parts inspected. |
| `body_text_processed` | Whether `word/document.xml` body text was processed. |
| `tables_detected` | Whether tables exist in `word/document.xml`. |
| `headers_detected` / `footers_detected` | Whether header/footer parts exist. |
| `comments_detected` | Whether comment/person metadata parts exist. |
| `tracked_changes_detected` | Whether tracked-change markers exist. |
| `metadata_detected` | Whether core/app/custom metadata exists. |
| `custom_xml_detected` | Whether `customXml/` parts exist. |
| `footnotes_detected` / `endnotes_detected` | Whether note parts exist. |
| `text_boxes_or_shapes_detected` | Whether drawings/shapes likely contain text. |
| `embedded_objects_detected` | Whether embedded package objects exist. |
| `split_placeholder_candidates` | Potential placeholder fragments across runs. |
| `unsupported_parts` | Parts not processed by current helper. |
| `cleaning_actions` | Metadata/content cleaning actions applied by future helper. |
| `warnings` | Non-blocking risks shown to the user. |
| `blocking_reasons` | Reasons export is blocked or requires explicit future policy. |

Audit output should be human-readable and machine-readable.

---

## 15. Safe extraction sequence

Future extraction should proceed in a conservative order:

1. Validate DOCX is a ZIP/OOXML package.
2. List all package parts.
3. Classify parts into supported, inspectable, cleanable and unsupported groups.
4. Extract normal body text from `word/document.xml`.
5. Extract table text from `word/document.xml` while reporting table presence.
6. Detect and extract headers and footers.
7. Detect comments and comment-person metadata.
8. Detect tracked-change elements across body, headers, footers, notes and comments.
9. Detect footnotes and endnotes.
10. Inspect metadata files under `docProps/`.
11. Detect custom XML parts.
12. Detect drawings, text boxes, charts and embedded objects.
13. Detect split-run placeholder candidates.
14. Produce an audit report before making clean-export claims.

Extraction should not call cloud services and should not persist real document content outside the local process.

---

## 16. Safe cleaning sequence

Future cleaning should be additive and explicit:

1. Preserve the original input bytes unchanged until the user requests output.
2. Create a new output package, never mutate the source package in place.
3. Scrub/reinsert supported visible body text only when already reviewed/approved.
4. Apply metadata cleaning according to a dedicated WP36 policy.
5. Remove comments only when a later policy says comments should be removed.
6. Accept/remove tracked changes only after a dedicated policy defines safe semantics.
7. Remove or warn about custom XML according to explicit policy.
8. Handle headers, footers, footnotes and endnotes only after extraction/review support exists.
9. Preserve package validity and relationships required for a readable DOCX.
10. Produce before/after audit fields showing what was cleaned, removed, preserved or unsupported.

No cleaning step should silently change legal meaning. Removing comments or tracked changes can alter document review history, so the user must understand the effect.

---

## 17. What should be blocked vs warned

WP35 does not implement blocking. This section defines a future policy direction only.

### Warning-first candidates

Warn the user when:

- headers or footers exist but are not processed;
- footnotes/endnotes exist but are not processed;
- metadata exists but no cleaner has run;
- custom XML exists but no cleaner has run;
- text boxes/shapes may contain text;
- split-run placeholders are possible but not confirmed;
- table layout may affect review confidence.

### Strong warning or future block candidates

Require strong warning or future export blocking when:

- tracked changes are present and no accept/remove policy exists;
- comments are present and no remove/review policy exists;
- embedded objects are present;
- macros or active content are present;
- unsupported package parts contain readable text that Scrub cannot review;
- hygiene audit cannot inspect the package safely;
- the user requests a clean/safe export claim while unsupported hidden content remains.

### Blocking policy rule

Blocking export is a product semantics change. It must be implemented only in a later approved workpackage with:

- explicit UX copy;
- tests;
- changelog entry;
- user-facing release notes if visible;
- rollback or override policy where appropriate.

---

## 18. What should remain out of scope

The following should remain out of scope until separately approved:

- OCR for images inside DOCX;
- cloud-based document conversion or inspection;
- AI-based hidden-content extraction;
- full fidelity DOCX reconstruction beyond controlled package editing;
- embedded object scrubbing;
- macro analysis or macro rewriting;
- guaranteed removal of every possible third-party add-in artifact;
- silent export blocking without explicit policy;
- real customer document test fixtures;
- changing existing DOCX reinsert behavior.

---

## 19. Recommended next workpackages

Recommended sequence:

1. `WP36 — DOCX metadata cleaner helper`.
2. `WP37 — Headers/footers/comments/tracked-changes extraction helper`.
3. `WP38 — DOCX hygiene audit report`.
4. `WP39 — Clean DOCX export policy`.

Coordination note:

After WP35, the coordinator should run:

```text
WP58 — Parallel specification consolidation and next execution queue
```

WP58 should reconcile WP19, WP25, WP30 and WP35 before implementation workpackages such as WP20, WP26, WP31 or WP36 start.

---

## 20. Intentionally not changed in WP35

- No DOCX cleaner implemented.
- No DOCX parser changed.
- No export semantics changed.
- No UI changed.
- No tests added or changed.
- No real documents added.
- No cloud processing added.
- No dependency changes made.
- No direct edit to `presidio_streamlit.py`.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No direct edit to `fix_streamlit_pdf_text_reinsert.py`.
