# SolidPrivacy Scrub — Decision Log

This file records accepted strategic, product and architecture decisions.

---

## 2026-06-18 — D026 — Temporarily prioritize MVP UI cleanup and export/download redesign

Status: accepted product-direction decision

Decision:

```text
Pause new recall/benchmark follow-up packages temporarily and prioritize MVP UI cleanup/export redesign.
```

Reason:

```text
The app must move from a prototype/debug interface toward a professional MVP workflow.
```

Consequence:

```text
Next packages focus on export/download UX and hiding/collapsing debug details without weakening safety controls.
```

Implications:

- Recall/benchmark follow-up packages are parked unless a concrete blocker appears.
- Export/download UX is now the active next user-visible improvement line.
- Technical/audit details must remain available but move out of the primary flow where appropriate.
- Scrub Key must stay clearly separated and visibly sensitive.
- Export semantics must not change silently.
- The review table remains source of truth and fallback.
- No Streamlit implementation is approved by this planning decision; implementation requires separate workpackages.

---

## 2026-06-18 — D025 — PERSON-name implementation requires green contract tests first

Status: accepted tests/specification decision

Decision:

```text
PERSON-name recognizer implementation may only start after contract tests are green.
```

Reason:

```text
Value-only matching and role preservation are safety-critical.
```

Consequence:

```text
Implementation package must satisfy the contract fixture before benchmark review.
```

---

## 2026-06-18 — D024 — PERSON-name improvement proceeds test-first

Status: accepted planning/specification decision

Decision:

```text
PERSON-name improvement will proceed test-first.
```

Reason:

```text
Single-surname and role/context cases are high-risk for over-masking and legal/care meaning damage.
```

Consequence:

```text
Contract tests are required before recognizer implementation.
```

---

## 2026-06-15 — D023 — Synchronized scrolling is default review behavior, not a user-facing technical control

Status: accepted bounded UX refinement decision

Decision:

```text
In the central side-by-side review surface, synchronized scrolling should be on by default and should not be exposed as a visible checkbox.
```

Boundary:

This decision does not change replacement behavior, export/download behavior, Scrub Key behavior or reinsert behavior.

---

## 2026-06-15 — D022 — Bounded synchronized side-by-side scrolling approved after prototype review

Status: accepted bounded UX implementation decision; refined by D023 for visible control behavior

Decision:

```text
After visual review of the isolated synchronized-scroll prototype, bounded synchronized scrolling may be integrated into the existing side-by-side review surface.
```

Implementation boundaries:

- Keep synchronized scrolling bounded to the side-by-side review surface.
- Do not change replacement behavior.
- Do not mutate review table state.
- Do not write or change Scrub Key data.
- Do not change export/download behavior.
- Do not change reinsert behavior.
- Do not use real data.

---

## 2026-06-14 — D021 — Unified side-by-side review surface is the target review UX

Status: accepted product/UX direction

Decision:

```text
The review UX should move toward one unified side-by-side main review surface: source text on the left, processed/checked text on the right, with optional highlights integrated in the processed-text pane. The product should not keep adding separate helper panels or duplicate preview expanders for every review feature.
```

Implications:

- Future review UX work should centralize around source-vs-processed comparison.
- The review table remains source of truth and fallback.
- Serial review remains a guided review layer, not a replacement of the table.
- The old replacement decision helper panel must not return as normal user-facing UI.
- Do not start panel removal, click-to-mark, advanced editor, full-document marking, Scrub Key writes, export blocking or reinsert behavior changes without separate approved packages.

---

## Historical note

Older decisions remain available in Git history.
