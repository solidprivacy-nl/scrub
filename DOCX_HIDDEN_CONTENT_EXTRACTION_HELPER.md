# WP37 — DOCX hidden content extraction helper

Status: completed helper/tests/documentation-only  
Repository: `solidprivacy-nl/scrub`

WP37 adds a pure local, read-only helper for detecting and extracting text from high-risk DOCX package parts that are outside the current DOCX reinsert foundation scope.

The helper is:

```text
docx_hidden_content_extractor.py
```

Primary function:

```text
inspect_docx_hidden_content(content: bytes) -> dict
```

---

## 1. Purpose

The helper makes hidden-content risk audit-visible before any cleaner, removal policy or export-blocking policy is implemented.

It focuses on:

- headers;
- footers;
- comments / kantlijncommentaren;
- comment author/person-like metadata where present;
- tracked-change markers such as insertions, deletions and move markers.

This directly follows WP35 and WP36A.

---

## 2. What the helper reports

The helper returns an audit-oriented dictionary with fields such as:

```text
valid_docx
validation_issues
local_only
ai_processing
cloud_processing
extraction_only
cleaning_applied
export_blocking
docx_parts_seen
headers
footers
comments
tracked_changes
detected
warnings
```

Detection flags include:

```text
headers_detected
footers_detected
comments_detected
tracked_changes_detected
```

---

## 3. Supported extraction scope

The helper inspects these DOCX package patterns:

```text
word/header*.xml
word/footer*.xml
word/comments.xml
word/commentsExtended.xml
word/person.xml
word/*.xml for tracked-change markers
```

It extracts text from WordprocessingML text nodes and reports parse errors per part where applicable.

Tracked-change markers include:

```text
w:ins
w:del
w:delText
w:moveFrom
w:moveTo
w:moveFromRangeStart
w:moveFromRangeEnd
w:moveToRangeStart
w:moveToRangeEnd
```

---

## 4. Explicit non-goals

WP37 does not:

- clean DOCX files;
- remove comments;
- remove or accept tracked changes;
- remove metadata;
- block export;
- change export semantics;
- change DOCX reinsert behavior;
- change Scrub Key schema;
- change Streamlit UI;
- add dependencies;
- add cloud processing;
- add real-data fixtures.

The helper is deliberately extraction/audit-only.

---

## 5. Privacy boundary

The helper is local and side-effect free:

- no file-system persistence;
- no network calls;
- no AI calls;
- no cloud processing;
- no mutation of source bytes;
- no export package writing;
- no real-data test fixtures.

It accepts bytes and returns an in-memory audit dictionary.

---

## 6. Recommended next step

Recommended next package:

```text
WP38 — DOCX hygiene audit report
```

Purpose:

- Convert the extraction helper output into a user/support-facing hygiene audit structure.
- Keep it warning/report-only unless a later approved package defines export-blocking semantics.

Do not start comment removal, tracked-change removal or export blocking before the audit policy is explicit and tested.
