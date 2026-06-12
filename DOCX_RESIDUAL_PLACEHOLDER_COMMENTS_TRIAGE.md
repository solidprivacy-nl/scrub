# WP36A — DOCX residual placeholder and comments risk triage

Status: completed triage/test/documentation-only  
Repository: `solidprivacy-nl/scrub`

This triage records an app-verification finding: DOCX reinsert can still leave residual placeholders in restored DOCX output, and Word comments / margin comments are outside the current scrub/reinsert processing scope.

This is a high-risk document hygiene issue. It affects privacy trust and must not be treated as a cosmetic bug.

---

## 1. Finding

During app verification, DOCX restore/reinsert was observed to work partly, but restored DOCX output could still contain placeholders such as:

```text
[PERSOON_01]
[PERSOON_02]
```

A second finding is that Word comments / margin comments are not currently processed. Sensitive names, references or other confidential information inside comment parts can remain outside the current scrub/reinsert path.

The current behavior is consistent with the documented foundation limitation: current DOCX reinsert processes only `word/document.xml` text nodes and does not process headers, footers, comments, tracked changes or metadata.

---

## 2. Why this is high risk

This is high risk because a user may open the restored DOCX and believe the document was fully restored or fully checked while:

- visible body text may still contain residual placeholders;
- placeholders may remain because the placeholder format differs, for example `[PERSOON_01]` versus `[PERSOON_1]`;
- placeholders may remain because Word split a placeholder across multiple runs/text nodes;
- Word comments / margin comments may still contain sensitive values;
- comment author/person metadata may still identify reviewers or staff;
- tracked changes may preserve deleted sensitive text;
- unsupported DOCX parts are copied through unchanged by the current foundation helper.

This directly affects privacy trust. It also affects legal and professional trust because the user may not notice the residual risk before sharing the document.

---

## 3. Current technical scope

Current DOCX reinsert foundation scope:

```text
DOCX package → word/document.xml → WordprocessingML text nodes → deterministic placeholder reinsert → restored DOCX package
```

Current support:

- normal body paragraphs in `word/document.xml`;
- table text in `word/document.xml`;
- deterministic exact placeholder replacement when a placeholder appears in a single text node and exists in the Scrub Key.

Current unsupported/high-risk areas:

- residual placeholders not present in the Scrub Key mapping;
- placeholders with numbering or formatting mismatch;
- placeholders split across multiple Word runs/text nodes;
- `word/comments.xml`;
- `word/commentsExtended.xml`;
- `word/person.xml`;
- tracked changes;
- headers and footers;
- document metadata;
- footnotes and endnotes;
- text boxes, drawings, charts and embedded objects;
- custom XML.

---

## 4. Residual placeholder scenarios

Residual placeholders can appear when:

| Scenario | Example | Current expected outcome |
| --- | --- | --- |
| Numbering mismatch | Scrub Key contains `[PERSOON_1]`, DOCX contains `[PERSOON_01]` | Placeholder remains visible and should be treated as unresolved. |
| Split Word runs | `[PERS` + `OON_1]` across two `w:t` nodes | Placeholder is not restored by exact per-node replacement. |
| Missing mapping | Placeholder exists in DOCX but not in Scrub Key | Placeholder remains visible and should be reported/audited. |
| Corrupted by editing/AI | `[Persoon 1]`, `[PERSOON - 1]`, translated label | Placeholder remains unresolved unless later placeholder-audit logic reports it. |
| Duplicate or ambiguous mapping | Same placeholder maps to multiple original values | Current helper excludes duplicate placeholders to avoid wrong reinsert. |

Residual placeholders should be visible to the user and audit, not silently repaired or guessed.

---

## 5. Comments / margin comments risk

Word comments are commonly stored in package parts such as:

```text
word/comments.xml
word/commentsExtended.xml
word/person.xml
```

These parts may contain:

- reviewer names;
- initials;
- staff or lawyer identities;
- internal legal strategy;
- care notes;
- old client names;
- BSN/client/matter references;
- comment author/person metadata.

In the current foundation helper, these parts are not processed and are copied through unchanged. That means a restored DOCX may still contain sensitive comment content even when body text was restored correctly.

---

## 6. Risk classification

Risk level:

```text
high
```

Reason:

- The problem can leave sensitive or operationally meaningful markers in the restored output.
- Comments can contain hidden or side-channel sensitive information.
- Users often overlook Word comments, tracked changes and metadata before sharing a document.
- This undermines trust in restored DOCX output and future clean-export claims.

This should be handled as a document hygiene issue, not as UI polish.

---

## 7. MVP policy boundary

WP36A does not implement a fix.

WP36A explicitly does not:

- implement a DOCX cleaner;
- process comments;
- remove comments;
- remove tracked changes;
- block export;
- change export semantics;
- change reinsert behavior;
- change Streamlit UI;
- change Scrub Key schema;
- add cloud processing;
- add real-data fixtures.

Existing behavior remains unchanged. The goal is to make the risk explicit and test-visible.

---

## 8. Test expectation added in WP36A

The WP36A regression test should show, with synthetic data only, that:

- a residual placeholder such as `[PERSOON_01]` remains if the loaded Scrub Key only contains `[PERSOON_1]`;
- the helper reports that the unmatched placeholder remains unresolved;
- comment parts such as `word/comments.xml` are not processed by current DOCX reinsert;
- comment content is copied through unchanged in the restored DOCX package;
- the triage document records this as high risk;
- no cleaner/export blocking/UI behavior is introduced.

---

## 9. Recommended next step

Recommended next workpackage:

```text
WP37 — Headers/footers/comments/tracked-changes extraction helper
```

Purpose:

- Detect and extract high-risk DOCX parts such as headers, footers, comments and tracked changes.
- Produce audit-visible signals before any cleaner or export-blocking policy is considered.
- Keep extraction local and synthetic-test-only.

Do not jump directly to comment removal or export blocking without extraction/audit tests and explicit policy.

---

## 10. Relationship to WP35

WP35 already documented that comments and tracked changes are high-risk hidden content. WP36A adds a concrete app-verification finding and locks it into tests/documentation so future work cannot treat it as cosmetic or already solved.

WP36A is narrower than a DOCX cleaner package. It is a risk triage and regression visibility package only.
