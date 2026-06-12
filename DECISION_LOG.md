# SolidPrivacy Scrub — Decision Log

This file records accepted strategic, product and architecture decisions.

---

## 2026-06-12 — D016 — Highlight-based review starts as bounded read-only prototype after feasibility review

Status: accepted prototype decision

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

---

## 2026-06-12 — D015 — Local installer is deferred until the final roadmap phase

Status: accepted roadmap sequencing decision

Decision:

```text
Local installer and production desktop packaging work must move to the end of the roadmap. Scrub should validate as much as possible through the online/web prototype and GitHub workflow first. Only after logic, interface, security and trustworthiness are acceptable should the project invest serious effort in local installer/MSI/desktop packaging.
```

Rationale:

Testing an installable app is much more labor-intensive than testing a web interface. Installer work introduces OS, antivirus, signing, dependency, update, rollback, temp-file, network, support and enterprise-management complexity. Starting packaging too early risks spending effort on distributing logic and UI that may still change. The Hugging Face/Streamlit prototype remains the fastest surface for synthetic and approved non-confidential validation of product behavior.

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
