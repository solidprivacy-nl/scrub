# SolidPrivacy Scrub — Decision Log

This file records accepted strategic, product and architecture decisions.

---

## 2026-06-15 — D022 — Bounded synchronized side-by-side scrolling approved after prototype review

Status: accepted bounded UX implementation decision

Decision:

```text
After visual review of the isolated synchronized-scroll prototype, bounded synchronized scrolling may be integrated into the existing side-by-side review surface.
```

Rationale:

The coordinator confirmed that the isolated prototype looked good and may be integrated into the production environment. The integration must remain bounded: source and processed panes stay in the review surface, the review table remains source of truth and fallback, and synchronized scrolling remains a visual/navigation aid only.

Implementation boundaries:

- Use local escaped HTML/JS inside the app.
- Keep a visible sync on/off fallback.
- Do not change replacement behavior.
- Do not mutate review table state.
- Do not write or change Scrub Key data.
- Do not change export/download behavior.
- Do not change reinsert behavior.
- Do not add dependencies.
- Do not use cloud processing.
- Do not use real data.
- Preserve the warning that percentage-based sync can be imperfect when source and processed text differ structurally.

Verification requirement:

```text
GitHub Actions green -> Hugging Face sync green -> coordinator app screenshot.
```

---

## 2026-06-14 — D021 — Unified side-by-side review surface is the target review UX

Status: accepted product/UX direction

Decision:

```text
The review UX should move toward one unified side-by-side main review surface: source text on the left, processed/checked text on the right, with optional highlights integrated in the processed-text pane. The product should not keep adding separate helper panels or duplicate preview expanders for every review feature.
```

Rationale:

The current interface risks becoming less intuitive because each new review function can become another expander/panel. The coordinator feedback is that a simpler professional workflow should let the user compare source and processed output directly, with visual support in the same main review area. A separate highlight-only preview and repeated inline labels such as `Gemarkeerd` add cognitive noise when the highlight color already communicates the marker.

Implications:

- Add `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md` as the central direction document for this UX line.
- Future review UX work should centralize around source-vs-processed comparison.
- The highlight toggle should belong near/in the main side-by-side review surface, not primarily as a separate duplicate preview panel.
- Repeated per-highlight labels such as `Gemarkeerd` should not be the long-term design when the marker itself is sufficient.
- Synchronized scrolling is a valid UX goal but requires separate planning/testing because it may need custom HTML/component work.
- D022 records the later approved bounded implementation route for synchronized scrolling after prototype review.
- The review table remains source of truth and fallback.
- Serial review remains a guided review layer, not a replacement of the table.
- The old replacement decision helper panel must not return as normal user-facing UI.
- Do not start panel removal, click-to-mark, advanced editor, full-document marking, Scrub Key writes, export blocking or reinsert behavior changes without separate approved packages.

---

## 2026-06-13 — D020 — Do not expose replacement helper internals as a user-facing panel

Status: accepted UX rollback decision

Decision:

```text
Do not expose replacement_decision helper internals as a user-facing panel in the normal Scrub Legal flow. The technically working replacement decision helper panel is parked/hidden because coordinator product feedback found it not intuitive enough and too complex for normal users.
```

Rationale:

The replacement decision helper and contract tests remain useful as business-logic foundations, but the first user-facing panel exposed too much helper/audit structure. It made the review flow less clear instead of more intuitive.

Implications:

- Keep `replacement_decision.py`, `REPLACE_LOGIC_UI_PLAN.md` and the contract tests as redesign assets.
- Do not treat WP_REPLACE_LOGIC_UI_IMPLEMENTATION as a successful user-facing feature.
- The normal Scrub Legal flow must not show the replacement decision helper panel.
- The review table remains the source of truth and fallback.
- The serial review panel may remain visible as a non-destructive review aid.
- Future replacement UX must be redesigned around a genuinely intuitive review flow, not raw helper/audit internals.
- Do not start a new replacement UI implementation, mutating decision behavior, automatic replacement, Scrub Key writes, export blocking, click-to-mark, advanced editor or full-document marking without separate coordinator approval.

---

## 2026-06-13 — D019 — Table-first baseline restored; static-highlight startup mutation parked

Status: accepted rollback/implementation-route decision

Decision:

```text
The working table-first Scrub interface is the current baseline and fallback. The failed static-highlight/marking route based on startup source mutation is fully rolled back and parked. Future document-context, marking or editor improvements must be redesigned through helper/model code first, tests first and small approved non-destructive UI panels only after the contracts are stable.
```

Rationale:

The WP42D static highlight preview attempt repeatedly destabilized Hugging Face runtime startup and required rollback/repair work. The product direction remains document-first review with context, better replacement decisions and later marking/editor capabilities, but the implementation route must not depend on mutating `presidio_streamlit.py` at container startup or on quick UI patch fixes without app-start verification.

Implications:

- Do not restart the old static highlight preview startup mutation route.
- Do not patch `presidio_streamlit.py` through container startup for preview, marking or editor work.
- Keep the table-first review workflow as the authoritative working baseline/fallback.
- Future review improvements should start with pure helper/model modules and tests.
- UI work should be small, non-destructive and explicitly approved after helper/contract tests are stable.
- The next recommended work is `WP_SERIAL_REVIEW_HELPER`, followed later by `WP_SERIAL_REVIEW_UI` only after helper/tests and explicit approval.
- Click-to-mark and advanced editor work remain later-stage candidates requiring separate decisions.

---

## 2026-06-12 — D018 — Stay with Streamlit for MVP validation and defer frontend migration

Status: accepted frontend architecture decision; implementation-route superseded where it conflicts with D019/D021/D022

Decision:

```text
Keep Streamlit as the MVP validation surface for now. Do not migrate to a separate frontend yet. Do not build a professional document editor yet.
```

Rationale:

The project currently needs validation of product behavior more than a new frontend stack. Streamlit remains the fastest surface for online MVP validation with synthetic and approved non-confidential test data. A frontend migration now would add architecture, security, testing and synchronization complexity before the core workflow is trusted.

Implications:

- Continue using Streamlit for MVP validation.
- Keep UI thin and helper-driven.
- Put business rules and safety decisions in reusable Python helpers and tests where possible.
- Do not replace the current review table without a separate migration package.
- Do not start click-to-mark, professional document editing, long-document virtualized review or Word/PDF layout rendering yet.
- Reconsider frontend migration only after MVP workflow evidence and user validation.
- WP42D is no longer pending preview verification; it is rolled back/parked and closed out through D019/WP42D-ROLLBACK-CLOSEOUT.

---

## 2026-06-12 — D017 — Streamlit is feasible only for a bounded read-only highlight preview

Status: accepted feasibility boundary decision; any implementation route using startup source mutation is superseded by D019/D021/D022

Decision:

```text
Streamlit may be used for a small static/read-only highlight review preview using synthetic text or extracted main text only. It must not become the long-term professional document-centric review interface yet, and it must not implement click-to-mark, review mutation, export blocking, Scrub Key mutation, Word/PDF layout rendering or broad review-table replacement.
```

Rationale:

Streamlit is fast for online MVP validation, but clickable markers, synchronized panes, raw HTML rendering, accessibility, long-document performance and state synchronization are high-risk in the current patch-based UI architecture. A bounded read-only prototype can validate whether document context improves review comprehension without destabilizing the current table-first workflow.

Implications:

- `STREAMLIT_FEASIBILITY_BOUNDARY_REVIEW.md` remains a historical feasibility boundary, but D019 governs the route after the failed WP42D startup-mutation attempt and D021/D022 govern the unified side-by-side review target.
- The old static-highlight startup source mutation route must not be restarted.
- Future UI preview work may be considered only after helper/model tests and explicit approval.
- Click-to-mark sensitive text remains blocked until later decision/implementation packages.
- The production review table remains the authoritative audit/control surface.
- Any HTML rendering must escape source text and avoid raw user-text HTML.

---

## 2026-06-12 — D016 — Highlight-based review starts as bounded read-only prototype after feasibility review

Status: accepted prototype decision; implementation route superseded where it conflicts with D019/D021/D022

Decision:

```text
Build a small, read-only proof-of-concept for visual review of scrubbed output using highlighted placeholders before considering any broader document-editor direction.
```
