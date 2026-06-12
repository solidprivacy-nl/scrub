# WP38 — DOCX hygiene audit report

Status: completed helper/tests/documentation-only  
Repository: `solidprivacy-nl/scrub`

WP38 adds a report-only DOCX hygiene audit helper on top of the WP37 hidden-content extractor.

Helper:

```text
docx_hygiene_audit.py
```

Primary functions:

```text
build_docx_hygiene_audit_report(content: bytes) -> dict
render_docx_hygiene_audit_markdown(report: dict) -> str
```

---

## 1. Purpose

The audit report converts hidden DOCX content detection into a structured risk report.

It makes these findings visible:

- headers detected;
- footers detected;
- comments / kantlijncommentaren detected;
- comment/person metadata detected;
- tracked-change markers detected;
- invalid DOCX / unknown hygiene risk.

This helper is designed for future audit/report integration. It is not a cleaner and does not change product behavior.

---

## 2. Report fields

The report includes:

```text
document_type
audit_type
synthetic_safe_structure
local_only
ai_processing
cloud_processing
report_only
extraction_only
cleaning_applied
export_blocking
export_semantics_changed
valid_docx
validation_issues
summary
detected
counts
findings
warnings
recommended_next_step
unsupported_scope_note
source_extraction
```

Important fixed safety fields:

```text
report_only: true
extraction_only: true
cleaning_applied: false
export_blocking: false
export_semantics_changed: false
safe_to_claim_clean: false
```

---

## 3. Severity model

The MVP severity model is intentionally conservative:

| Situation | Severity |
| --- | --- |
| Invalid DOCX / cannot inspect | `medium` |
| No WP37-supported findings | `low` |
| Headers, footers, comments or tracked changes detected | `high` |

A `low` result is not a clean-DOCX guarantee. It only means no WP37-supported hidden-content parts were detected.

---

## 4. Findings

Current finding ids:

```text
headers_detected
footers_detected
comments_detected
tracked_changes_detected
invalid_docx
```

Each finding includes:

```text
id
severity
count
title
risk
recommended_action
```

---

## 5. Explicit non-goals

WP38 does not:

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

---

## 6. Unsupported scope note

The helper explicitly states that it is based on WP37-supported parts only.

Still future work:

- footnotes;
- endnotes;
- document metadata;
- custom XML;
- text boxes;
- shapes;
- charts;
- embedded objects;
- product UI integration;
- export-blocking policy.

---

## 7. Recommended next step

Recommended next package:

```text
WP39 — Clean DOCX export policy
```

Purpose:

- Define when warnings are enough, when export should be blocked, and when a future clean-DOCX export may be claimed.
- Keep policy separate from cleaner/removal implementation.

Do not start comment removal, tracked-change removal, metadata cleaning or export blocking before the policy is explicit and tested.
