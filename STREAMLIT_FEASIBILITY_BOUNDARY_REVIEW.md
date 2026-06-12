# WP42 — Streamlit feasibility boundary review

Status: completed specification/decision/documentation-only  
Repository: `solidprivacy-nl/scrub`

This review decides the safe Streamlit boundary for the document-centric/highlight review direction from WP40 and WP41.

WP42 does not implement UI, does not edit Streamlit patch files, does not change the review table, does not change export/download behavior, does not change Scrub Key behavior, does not add dependencies, does not add cloud processing and does not add real data.

---

## 1. Decision

Streamlit is feasible for a **small static read-only highlight review preview**.

Streamlit is **not yet feasible as the long-term professional document-centric review interface** and should not be used now for:

- a broad document UI rewrite;
- click-to-mark sensitive text;
- multi-pane synchronized editing;
- Word/PDF layout rendering;
- mutation of review decisions from highlights;
- export blocking based on highlight state;
- high-volume long-document review as the primary interface.

Approved next prototype boundary:

```text
static/read-only highlight preview
synthetic text or extracted main text only
no mutation
no export semantics change
current review table remains authoritative audit/control surface
```

---

## 2. Rationale

Streamlit is fast for online MVP validation, but its model is rerun/session-state oriented. Document-centric review requires stable marker identity, selection state, keyboard navigation, safe rendering and eventual synchronization with the review table.

That is feasible for a read-only proof, but risky for authoritative review editing.

The current codebase also uses Streamlit patch files. Broad document UI changes in this layer could destabilize existing flows such as:

- review table flow;
- Scrub Key export/import;
- reinsert;
- export/download;
- PDF-to-TXT restored output;
- DOCX restored output.

Therefore the next implementation should be small and isolated.

---

## 3. Approved Streamlit prototype boundary

A later prototype package may implement:

- synthetic plain text highlight preview;
- extracted DOCX main text preview, if already available as text;
- read-only highlighted spans;
- a separate finding detail area;
- table/audit row references shown as labels or ids;
- warning summary for unresolved findings;
- color plus text labels, not color-only marking;
- escaped user text rendering;
- no mutation of source review rows.

The prototype may use a separate helper/model file before touching UI.

The prototype should be separate from the production review table and clearly labelled as experimental/non-authoritative.

---

## 4. Not approved in Streamlit yet

Do not implement these in the next Streamlit package:

- click-to-mark new sensitive values;
- inline editing of highlights;
- drag/drop marker editing;
- changing include/replace decisions from the highlight pane;
- direct mutation of Scrub Key rows;
- clean-DOCX export state changes;
- export blocking;
- raw Word layout rendering;
- PDF layout rendering;
- OCR;
- comments/tracked changes editing;
- broad replacement of the review table.

These require later decision packages.

---

## 5. Rendering safety requirements

If highlighted text is rendered with HTML, the implementation must:

- escape source document text before rendering;
- avoid rendering user text as raw HTML;
- generate markup only from trusted code;
- keep span offsets tied to the displayed text;
- fail visibly if offsets are invalid;
- avoid storing source text in logs;
- use synthetic fixtures in tests;
- not use external JavaScript or cloud assets.

---

## 6. State boundary

The first Streamlit prototype may store only non-authoritative view state, such as:

```text
selected_span_id
selected_row_id
preview_filter
```

It must not store or mutate:

```text
final include/exclude decision
replace_with value
Scrub Key content
export eligibility
review table source of truth
```

The production review table remains the control/audit surface.

---

## 7. Performance boundary

First prototype limits:

```text
synthetic or small extracted text
bounded number of highlights
no full DOCX/PDF layout reconstruction
no long-document virtualized editor
```

If larger documents cause performance issues, the prototype should degrade to:

- summary list;
- section/chunk preview;
- table-only review;
- warning that highlight preview is unavailable for long text.

---

## 8. Accessibility boundary

The prototype must not rely on color alone.

Minimum requirements:

- visible label for marker category;
- selected marker text label;
- contrast-conscious default styling;
- keyboard-accessible fallback through finding list/table;
- unresolved-risk summary;
- no dense visual overload for long documents.

---

## 9. Data model boundary

The first prototype should use a non-sensitive span model:

```text
span_id
row_id
start_offset
end_offset
label
entity_type
status
source
replacement_preview
reason
context_before
context_after
```

Rules:

- offsets are zero-based;
- offsets refer to the exact displayed text;
- span text must equal displayed_text[start_offset:end_offset];
- invalid offsets must be reported and skipped;
- no original real personal data in fixtures;
- replacement preview must be synthetic or already placeholder-safe.

---

## 10. Recommended next step

Recommended next workpackage:

```text
WP42B — Static highlight preview helper and tests
```

Scope:

- build a pure helper/model for safe highlighted text rendering inputs;
- validate offsets, escaped text and category labels;
- use synthetic fixtures only;
- no Streamlit UI change yet unless explicitly approved.

After WP42B, a later UI package may add a small experimental Streamlit preview panel if tests and boundary remain stable.

Alternative next step:

```text
WP43 — Frontend architecture decision
```

Choose WP43 first if the coordinator wants to decide the long-term frontend before any Streamlit preview proof.

---

## 11. Explicit non-changes in WP42

WP42 did not change:

- `presidio_streamlit.py`;
- `fix_streamlit_nested_expanders.py`;
- any other Streamlit patch file;
- review table behavior;
- export/download behavior;
- Scrub Key behavior;
- reinsert behavior;
- DOCX hygiene behavior;
- dependencies;
- runtime behavior;
- cloud processing;
- real-data fixtures.
