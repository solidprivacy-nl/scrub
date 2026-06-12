# WP41 — Highlight-based review prototype decision

Status: completed decision/documentation-only  
Repository: `solidprivacy-nl/scrub`

## 1. Decision

The recommended next prototype direction is:

```text
A small text-based highlight review prototype, not a broad document UI rewrite.
```

The prototype should start with synthetic plain text and extracted DOCX main text only. It should show highlighted spans, selected finding details and table/audit linkage, but it must not change the current production review table, export/download behavior or Scrub Key behavior.

The recommended immediate next step is:

```text
WP42 — Streamlit feasibility boundary review
```

WP42 should decide whether this highlight prototype can safely be built in Streamlit or whether a separate frontend path is needed later.

## 2. Why not implement immediately?

Highlight review touches a risky UI area:

- document text rendering;
- clickable markers;
- synchronized state between document, detail pane and table;
- possible raw HTML rendering;
- accessibility and color meaning;
- large-document performance;
- export trust expectations.

Starting with a broad UI change would risk destabilizing the current table-first workflow. The safer next move is to decide the prototype boundary first, then review Streamlit feasibility, then implement a small prototype only after that boundary is clear.

## 3. Prototype goal

The goal of the future prototype is to answer:

```text
Can users review sensitive findings more reliably when they see them in document context instead of only in a table?
```

The prototype should test whether users can:

- see detected values in context;
- understand why a value was marked;
- distinguish sensitive values from legal/care context terms;
- identify missed sensitive values;
- inspect high-risk unresolved findings before export;
- still use the table as audit/control surface.

## 4. Recommended prototype scope

The first highlight prototype should support only:

- synthetic plain text;
- synthetic extracted DOCX main text;
- deterministic highlight spans from existing review rows or synthetic fixtures;
- read-only highlight display at first;
- a selected-finding detail panel;
- linkage back to table/audit rows;
- explicit unresolved-risk summary.

The first prototype should not support:

- exact Word layout rendering;
- PDF layout rendering;
- OCR;
- editing Word comments or tracked changes;
- automatic clean-DOCX export;
- export blocking;
- Scrub Key schema changes;
- real documents in repo;
- cloud document processing.

## 5. Highlight categories

The prototype should distinguish marker categories visually and textually.

Recommended categories:

```text
confirmed_sensitive
needs_review
candidate_missed_value
manual_added
preserve_context
high_risk_unresolved
hidden_content_warning
```

The UI must not rely on color alone. Each marker type should also have a label or icon/text cue.

## 6. Minimum interaction model

The first interactive version should be minimal:

1. Click or select a highlight.
2. Show the finding in a detail panel.
3. Show original text, proposed placeholder, entity type, source, reason and surrounding context.
4. Show linked table/audit row.
5. Allow no mutation in the first proof unless a later implementation package explicitly allows it.

The first proof should therefore be review-assistive, not authoritative.

## 7. Data model expectation

The prototype should use a simple non-sensitive span model:

```text
span_id
start_offset
end_offset
text
entity_type
source
review_status
replacement_preview
reason
context_before
context_after
```

Offsets must be zero-based and must refer to the text shown in the prototype. If text normalization changes offsets, the prototype must report that offsets are not reliable.

## 8. Security and privacy boundaries

The prototype must preserve current safety boundaries:

- no real data in fixtures;
- no cloud document processing;
- no telemetry;
- no hidden document upload;
- no silent export semantic change;
- no Scrub Key schema change;
- no automatic removal or cleaning;
- no claim that highlighted output is fully anonymized.

If HTML rendering is used, WP42 must address escaping/sanitization and whether user text can ever be rendered as raw HTML.

## 9. Accessibility requirements

The prototype should be usable without relying only on color.

Minimum requirements:

- text label for marker type;
- keyboard navigation expectation;
- readable contrast target;
- clear selected-marker state;
- warning summary for unresolved high-risk findings;
- no dense visual overload for long documents.

## 10. Options considered

### Option A — Static read-only highlighted text preview

Decision:

```text
Preferred first prototype shape.
```

Pros:

- smallest implementation surface;
- safest for online validation;
- avoids mutation logic;
- easier to test with synthetic text;
- lets users validate whether highlights improve review comprehension.

Cons:

- cannot yet add missed values by clicking;
- still needs later interaction design.

### Option B — Interactive click-to-review highlights in Streamlit

Decision:

```text
Candidate after WP42 feasibility review.
```

Pros:

- closer to desired UX;
- can synchronize document, detail pane and table;
- useful for online workflow testing.

Cons:

- may require fragile HTML/session-state handling;
- may not scale well for long documents;
- risks UI complexity in current Streamlit patch setup.

### Option C — Separate frontend prototype

Decision:

```text
Later candidate if Streamlit feasibility is poor.
```

Pros:

- better long-term document UX potential;
- stronger interaction model possible.

Cons:

- bigger architecture step;
- premature before Streamlit feasibility is reviewed;
- not suitable as the immediate next step.

## 11. Recommendation

Recommended sequence:

```text
1. WP42 — Streamlit feasibility boundary review.
2. If feasible: small static/read-only highlight prototype with synthetic text.
3. Only after that: controlled click-to-mark prototype.
4. If not feasible: frontend architecture decision before implementation.
```

This keeps the project aligned with the new roadmap rule: validate product logic and interface online first, but do not destabilize core workflow or start installer work too early.

## 12. Non-goals

WP41 does not implement:

- UI changes;
- clickable highlights;
- click-to-mark behavior;
- frontend migration;
- export/download changes;
- review table changes;
- Scrub Key behavior changes;
- DOCX cleaning;
- cloud processing;
- real-data fixtures.

## 13. Final decision

The project should pursue highlight-based review, but only as a small, bounded prototype after a Streamlit feasibility review.

The first prototype should be:

```text
read-only, text-based, synthetic, highlight-and-detail oriented, table-linked, and explicitly non-authoritative.
```

The next workpackage should be:

```text
WP42 — Streamlit feasibility boundary review
```
