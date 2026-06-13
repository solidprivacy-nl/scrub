# WP43 — Frontend architecture decision

Status: completed architecture/decision/documentation-only  
Repository: `solidprivacy-nl/scrub`

## 1. Decision

The frontend architecture decision is:

```text
Keep Streamlit as the MVP validation surface for now.
Do not migrate to a separate frontend yet.
Do not build a professional document editor yet.
```

The project should continue using Streamlit for online/web validation of the MVP workflow while keeping the core logic in reusable Python helpers.

A separate frontend may become necessary later, but only after the MVP workflow is validated and the exact interaction requirements are clearer.

---

## 2. Why this decision now

The project currently needs validation of product behavior more than a new frontend stack.

Current priorities:

- import confidence;
- scrub/review reliability;
- replacement logic clarity;
- Scrub Key safety;
- reinsert reliability;
- DOCX hygiene visibility;
- export trust;
- audit/residual-risk reporting;
- online app verification before installer investment.

A frontend migration now would add complexity before the core workflow is trusted.

---

## 3. Accepted architecture path

Use this path for the MVP stage:

```text
Streamlit MVP UI
thin UI patch layer
reusable Python helper modules
contract tests before UI integration
small experimental panels only when approved
no broad UI rewrite
```

The UI should stay thin. Business rules and safety decisions should live in helper modules and tests wherever possible.

---

## 4. What Streamlit is approved for now

Streamlit remains approved for:

- current table-first review workflow;
- small, bounded review aids;
- experimental read-only preview panels only after helper/tests and explicit approval;
- synthetic online validation;
- user-facing workflow testing;
- Hugging Face demo validation with non-confidential/synthetic data;
- incremental MVP improvements after tests and approval.

The existing review table remains the authoritative control/audit surface unless a later approved package changes that.

---

## 5. What Streamlit is not approved for yet

Streamlit is not approved for:

- a broad professional document editor;
- click-to-mark sensitive text as an authoritative workflow;
- complex synchronized multi-pane editing;
- Word/PDF layout rendering;
- long-document virtualized review;
- export blocking based on UI-only state;
- direct Scrub Key mutation from new panels;
- replacing the current review table without a separate migration plan;
- startup source mutation of `presidio_streamlit.py` for preview, marking or editor work.

---

## 6. When to reconsider a separate frontend

A separate frontend may be reconsidered when at least one of these is true:

- document-centric review needs interaction beyond static/read-only aids;
- click-to-mark sensitive text becomes a priority;
- keyboard navigation, accessibility or large-document performance cannot be handled safely in Streamlit;
- users validate the need for a professional document-first review surface;
- MVP logic is stable enough that frontend migration risk is justified;
- the product moves toward scale features such as profiles, batch review or enterprise deployment.

---

## 7. Candidate later frontend path

If a separate frontend becomes necessary later, the preferred direction is:

```text
Python core remains source of truth
frontend consumes typed/audited helper outputs
API boundary is local-first
no cloud document processing
no hidden telemetry
review/export/Scrub Key actions stay explicit and auditable
```

Possible later options:

- lightweight web frontend around a local Python backend;
- desktop shell only after product behavior is stable;
- local-first document review UI after explicit architecture and security review.

No option is selected for implementation in WP43.

---

## 8. Required rules for future UI work

Future UI work must follow these rules:

1. helper/model and tests before UI integration;
2. no mutation from preview-only UI;
3. existing table remains fallback/control surface unless a migration package says otherwise;
4. no export semantic changes without explicit workpackage;
5. no Scrub Key schema or lifecycle changes without explicit workpackage;
6. no cloud document processing;
7. no real-data fixtures;
8. app verification required for UI behavior changes;
9. status evidence required before claiming UI success;
10. no startup source mutation of `presidio_streamlit.py` for preview/marking/editor work.

---

## 9. Relationship to WP42D after rollback closeout

WP42D added an experimental Streamlit static highlight preview UI, but that implementation route failed repeated runtime/startup verification and has been rolled back/parked.

The current accepted status is:

```text
The normal table-first Scrub interface is the working baseline and fallback.
The static-highlight startup mutation route is not approved for restart.
Future review improvements must start helper/model first and tests first.
```

WP43 remains valid at architecture level: keep Streamlit for MVP validation, keep UI thin, and defer a separate frontend/professional editor. D019 / WP42D-ROLLBACK-CLOSEOUT supersedes the earlier WP42D verification path.

Next review/frontend step:

```text
WP_SERIAL_REVIEW_HELPER — pure helper/tests for serial review queue.
```

Only after helper/tests and explicit approval should a small non-destructive UI package be considered.

---

## 10. Explicit non-changes in WP43

WP43 does not change:

- `presidio_streamlit.py`;
- `fix_streamlit_nested_expanders.py`;
- any Streamlit patch file;
- review table behavior;
- export/download behavior;
- Scrub Key behavior;
- reinsert behavior;
- helper runtime behavior;
- dependencies;
- Docker/runtime behavior;
- cloud processing;
- real-data fixtures.

---

## 11. Final decision

```text
Stay with Streamlit for MVP validation.
Keep UI thin and helper-driven.
Do not migrate frontend yet.
Do not restart startup source mutation for static highlights/marking/editor work.
Reconsider frontend migration only after MVP workflow evidence and user validation.
```
