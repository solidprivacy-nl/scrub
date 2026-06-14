# SolidPrivacy Scrub — Risk-driven Product & Development Roadmap

This document is the central roadmap for SolidPrivacy Scrub.

Use it together with:

- `WORKPACKAGES.md` for the active execution queue, dependencies and verification gates;
- `CHANGELOG.md` for internal implementation history;
- `RELEASE_NOTES.md` for user-facing product changes;
- `RISK_REGISTER.md` for trust, privacy and product risks;
- `DECISION_LOG.md` for accepted strategic and architecture decisions;
- `PROJECT_PROMPT.md` for worker rules and project governance.

Last roadmap strategy update: 2026-06-14 — unified side-by-side review UX direction anchored.

---

## 1. Product vision

Scrub is evolving from a technical Presidio demo into a trustworthy Dutch professional document scrubber for confidential legal and care documents.

The key promise remains:

```text
Sensitive information stays local in the final trust environment.
The user remains in control.
The document stays readable.
Residual risk is visible.
```

Current sequencing principle:

```text
Make the MVP workflow good before investing further in pilot operations, marketing, pricing, sales, promotion or installer work.
```

The active MVP workflow is:

```text
Import -> Scrub -> Review -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

---

## 2. Core product principle

The product is not just a generic anonymizer.

The real problem is:

```text
How can a professional safely use or share confidential documents without losing context, legal meaning, control or auditability?
```

Scrub must optimize for:

1. high recall for sensitive data;
2. context preservation;
3. human review;
4. easy and consistent replacement logic;
5. secure Scrub Key lifecycle;
6. reliable de-anonymization/reinsert;
7. document hygiene;
8. safe export;
9. audit and residual-risk reporting;
10. clear interface and workflow confidence.

Legal and professional context must be preserved. Scrub should replace sensitive values, not legal meaning.

---

## 3. Strategic workflow

The product workflow direction remains:

```text
Scrub -> Review -> Scrub Key -> AI -> Reinsert -> Export -> Audit
```

The roadmap is risk-driven rather than feature-driven.

Highest priority risks:

1. false negatives;
2. Scrub Key leakage or accidental sharing;
3. hidden document content and metadata leakage;
4. placeholder corruption during AI roundtrip;
5. review UX that is not document-centric enough;
6. confusing import/export/reinsert limitations;
7. installer/distribution effort before the product behavior is ready.

---

## 4. Current implementation status

Recent work completed or recorded:

```text
WP19-WP24 — recall/trust foundation.
WP25-WP29C — Scrub Key safety/test line.
WP30-WP34 — placeholder robustness helper/test line.
WP35-WP39 — DOCX hygiene line through clean-DOCX export policy and report-only audit UI.
WP40-WP43 — review UX/frontend decision line.
WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — product-rejected helper panel hidden and verified.
WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — replacement review redesigned around simple user choices.
WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR — unified side-by-side review UX direction anchored.
WP45-WP49 — local runtime/packaging decision line; installer deferred.
WP50-WP51 — pilot/ICP thinking artifacts; parked for now.
```

Important UX status:

```text
The review table remains source of truth and fallback.
The old replacement decision helper panel must not return as normal user-facing UI.
The long-term review target is one unified side-by-side main review surface, not more separate helper panels.
```

---

## 5. MVP product quality gate

Phase 7 follow-up is parked until the MVP is credible across:

- import;
- anonymization;
- review;
- replacement logic;
- Scrub Key handling;
- de-anonymization/reinsert;
- export;
- audit/residual-risk reporting;
- interface clarity.

WP50 and WP51 remain useful early thinking artifacts, but they are not the active execution line now.

Do not start WP52 by default.

---

## 6. Current phase order

The current phase order is:

```text
Phase 1 — Trust & recall foundation
Phase 2 — Scrub Key security and lifecycle
Phase 3 — Placeholder robustness for AI roundtrip
Phase 4 — Hidden content and document hygiene
Phase 5 — Document-centric review UX
Phase 6 — MVP workflow validation and trust hardening
Phase 7 — Pilot validation: Legal vs Zorg — parked until MVP quality gate passes
Phase 8 — Scale features: profiles, batch, CLI, enterprise
Phase 9 — Final local desktop/offline installer path
```

### Phase 5/6 — Review UX direction

The review UX target is now:

```text
Source text left | Processed/checked text right
                 | Optional highlights integrated in the processed text
```

This is governed by:

- `DECISION_LOG.md` D021;
- `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md`;
- `REPLACE_LOGIC_UI_REDESIGN_PLAN.md`.

UX principles:

- one main review surface before more helper panels;
- review table remains source of truth and fallback;
- serial review remains a guided review layer, not a table replacement;
- highlights are visual aid, not mutation mechanism;
- no repeated per-highlight `Gemarkeerd` labels as the long-term design;
- no click-to-mark, advanced editor or full-document marking in this phase;
- no Scrub Key/export/reinsert behavior changes from review UX work without separate approval.

### Phase 6 — MVP workflow validation and trust hardening

Goal:

```text
Use the online/web prototype and GitHub workflow to validate product behavior before pilot expansion or installer investment.
```

Focus:

- end-to-end workflow testing;
- import and export confidence;
- Scrub Key warning/acknowledgement verification;
- DOCX hygiene reporting;
- unified side-by-side review direction;
- easier replace/review logic;
- residual-risk and audit reporting;
- Hugging Face app verification after GitHub Actions/sync when UI changes.

### Phase 7 — parked pilot validation

WP50 and WP51 are recorded, but Phase 7 is not the active next line.

Phase 7 may reopen when the coordinator confirms the MVP product quality gate has been met.

---

## 7. Active next work direction

Current active priorities:

```text
1. Lock the side-by-side review UX direction with plan and contract tests.
2. Lock the redesigned replacement-review flow with contract tests.
3. Only then consider small UI implementation packages with separate explicit coordinator approval.
```

Do not implement UI directly from this roadmap step.

Do not start local packaging next steps such as `WP48B` or `WP49B` by default. They require explicit coordinator approval.

Do not start pilot follow-up such as `WP52` by default. It requires the MVP quality gate to pass first.

---

## 8. Parallelization strategy

Safe to do in parallel:

- helper modules with separate files;
- tests that do not touch the same UI flow;
- specifications;
- documentation;
- benchmark data design;
- risk reviews;
- non-UI architecture work;
- `WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN` and `WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS`, if both stay documentation/tests-only.

Do not run in parallel:

- multiple changes to `fix_streamlit_nested_expanders.py` or `presidio_streamlit.py`;
- multiple changes to the same Streamlit patch file;
- `serial_review_panel_ui.py` UI edits without coordination;
- `review_highlight_toggle_panel_ui.py` UI edits without coordination;
- export/download flow changes;
- review table flow changes;
- synchronized scroll implementation;
- custom HTML/component rendering implementation;
- Docker/runtime startup patch-order changes;
- installer/packaging work unless explicitly approved;
- Phase 7 follow-up while the MVP quality gate is not passed.

Use `workpackage_claims/` before starting a package.

---

## 9. Product architecture target

Current prototype architecture:

```text
Hugging Face Space
Streamlit UI
Presidio/spaCy recognizers
Dutch legal recognizers
Candidate scanner
Review table
Serial review / context aids
Side-by-side review UX direction
Scrub Key import/export
Pasted/TXT/DOCX/PDF-to-TXT reinsert
Exports
GitHub Actions tests
GitHub -> Hugging Face sync
```

Target architecture remains local-first, but installer work comes late:

```text
Validated online/web workflow first
Reusable Python core
Local recognition engine
Local benchmark/evaluation layer
Unified review workflow
Secure Scrub Key handling
Local exports
Residual-risk/audit reports
Final local desktop/offline packaging after validation
```

---

## 10. Security and trust principles

For the final product:

- no document upload to third-party cloud in the final trust environment;
- no model training on user documents;
- no telemetry containing document content;
- clear warning when using cloud AI outside Scrub;
- local-only processing as final production default;
- metadata-aware exports;
- audit report;
- residual-risk report;
- clear distinction between anonymization, pseudonymization and redaction;
- explicit Scrub Key lifecycle and deletion policy.

---

## 11. Development governance

For implementation work:

1. Add or update benchmark/gold-label cases where relevant.
2. Add or update tests.
3. Change logic/UI only within the approved package scope.
4. Verify GitHub Actions tests when possible.
5. Verify GitHub to Hugging Face sync when relevant.
6. Test the app in Hugging Face when UI behavior changed.
7. Update `CHANGELOG.md`.
8. Update `RELEASE_NOTES.md` for user-facing changes.
9. Update `WORKPACKAGES.md` when status or next steps change.
10. Update `ROADMAP.md` only when strategy, phase status or sequence changes.

For parked work:

1. Do not start WP52 by default.
2. Do not start installer/packaging work by default.
3. Require explicit coordinator approval to reopen parked lines.
