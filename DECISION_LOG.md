# SolidPrivacy Scrub — Decision Log

This file records accepted strategic, product and architecture decisions.

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

Status: accepted frontend architecture decision; implementation-route superseded where it conflicts with D019

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

Status: accepted feasibility boundary decision; any implementation route using startup source mutation is superseded by D019

Decision:

```text
Streamlit may be used for a small static/read-only highlight review preview using synthetic text or extracted main text only. It must not become the long-term professional document-centric review interface yet, and it must not implement click-to-mark, review mutation, export blocking, Scrub Key mutation, Word/PDF layout rendering or broad review-table replacement.
```

Rationale:

Streamlit is fast for online MVP validation, but clickable markers, synchronized panes, raw HTML rendering, accessibility, long-document performance and state synchronization are high-risk in the current patch-based UI architecture. A bounded read-only prototype can validate whether document context improves review comprehension without destabilizing the current table-first workflow.

Implications:

- `STREAMLIT_FEASIBILITY_BOUNDARY_REVIEW.md` remains a historical feasibility boundary, but D019 governs the route after the failed WP42D startup-mutation attempt.
- The old static-highlight startup source mutation route must not be restarted.
- Future UI preview work may be considered only after helper/model tests and explicit approval.
- Click-to-mark sensitive text remains blocked until later decision/implementation packages.
- The production review table remains the authoritative audit/control surface.
- Any HTML rendering must escape source text and avoid raw user-text HTML.

---

## 2026-06-12 — D016 — Highlight-based review starts as bounded read-only prototype after feasibility review

Status: accepted prototype decision; implementation route superseded where it conflicts with D019

Decision:

```text
Highlight-based document review should be pursued, but only as a small bounded prototype after Streamlit feasibility is reviewed. The first prototype should be read-only, text-based, synthetic, highlight-and-detail oriented, table-linked and explicitly non-authoritative. It must not change review table behavior, export/download behavior, Scrub Key behavior or runtime behavior.
```

Rationale:

Document context is needed for trustworthy review, but clickable highlights and synchronized panes touch fragile UI/state areas. A broad UI rewrite now would risk destabilizing the current workflow. The safer route is WP42 first, then a small synthetic text-based highlight proof if feasible.

Implications:

- WP41 is decision/documentation-only.
- WP42 should decide whether Streamlit can safely support the prototype.
- No worker should implement broad document-centric UI before WP42.
- Raw HTML/highlight rendering must consider escaping, accessibility, color-not-alone design and state safety.
- Current review table remains the audit/control surface.
- D019 supersedes any interpretation that would restart static-highlight startup source mutation.

---

## 2026-06-12 — D015 — Local installer is deferred until the final roadmap phase

Status: accepted roadmap sequencing decision

Decision:

```text
Local installer and production desktop packaging work must move to the end of the roadmap. Scrub should validate as much as possible through the online/web prototype and GitHub workflow first. Only after logic, interface, security and trustworthiness are acceptable should the project invest serious effort in local installer/MSI/desktop packaging.
```

Rationale:

Testing an installable app is much more labor-intensive than testing a web interface. Installer work introduces OS, antivirus, signing, dependency, update, rollback, offline, network, temp-file, support and enterprise-management complexity. Starting packaging too early risks spending effort on distributing logic and UI that may still change. The Hugging Face/Streamlit prototype remains the fastest surface for synthetic and approved non-confidential validation of product behavior.

Implications:

- `ROADMAP.md` now places final local desktop/offline installer work after trust, review, document hygiene, online workflow validation, pilot validation and scale-readiness work.
- `WP48B` or `WP49B` are not default next workpackages; they require explicit coordinator approval.
- MSI, signed installer, auto-updater, Tauri/Electron implementation and production packaging claims remain blocked until late-phase evidence is strong.
- The local-first product promise remains the final trust target, but installer effort should not precede product-behavior validation.
- Workers must not start installer or packaging implementation as a side effect of local-runtime, UI or trust work.

---

## Earlier active decisions

Earlier detailed decisions remain available in Git history and include:

- D014 — Desktop packaging starts with portable Python folder, MSI later only.
- D013 — Scrub Key deletion remains explicit and user-controlled.
- D012 — Recommended future robust placeholder format.
- D011 — Local runtime starts with Streamlit launcher, later desktop shell; superseded in sequence by D015.
- D010 — Scrub Key MVP lifecycle starts warning-first before encryption.
- D001-D009 — Earlier roadmap, PDF, Scrub Key, review UI, documentation and parallelization decisions.
