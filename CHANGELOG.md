# Changelog — SolidPrivacy Scrub

This changelog records meaningful product, architecture, workflow and recognizer changes for the Scrub legal document scrubber.

Conventions:

- Keep this file explicit and human-readable.
- Group changes by project phase / version.
- Record what changed, why it changed, and what is intentionally not changed.
- Do not use this as a substitute for tests; every recognizer hardening step should also add or update regression tests.

---

## Current development rule

From v10 onward, recognizer work follows this order:

1. Add or update synthetic regression cases.
2. Add or update tests.
3. Change recognizer / scanner logic.
4. Verify GitHub Actions tests are green.
5. Let GitHub sync to Hugging Face automatically.
6. Test the app in Hugging Face.

For UI/UX-only work, prefer pure helper modules and tests before touching Streamlit UI flow.

---

## WP12 — v13.6 Two-mode UI skeleton and tab separation

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Purpose:

- Implement the first two-mode UI structure with minimal risk.
- Make the two main user intents visible:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.
- Keep existing behavior working.
- Avoid a full landing-page refactor.

Files added or changed:

- Changed `fix_streamlit_nested_expanders.py`.
- Added `tests/test_two_mode_ui_patch.py`.
- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `handover/workpackages/20260608_0000_v13_6_two_mode_ui_skeleton.md`.

Main change:

- Added an idempotent startup patch that injects a small two-mode skeleton near the top of the app after the local-processing note.
- The skeleton uses Streamlit tabs:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.
- Each tab contains a short caption explaining the mode intent.
- The existing anonymization/scrub flow is left available.
- The existing pasted-text reinsert flow is left available.
- This is a navigation/skeleton step only; it does not move all app content into tabs yet.

Tests added:

- `tests/test_two_mode_ui_patch.py` checks:
  - `Anonimiseren` is present;
  - `Originele waarden terugzetten` is present;
  - `st.tabs` and named tab variables are present;
  - existing Scrub Key export/import labels remain;
  - existing pasted-text reinsert labels remain;
  - existing anonymization/download markers remain;
  - existing scrubbed download behavior markers are not rewired;
  - no TXT upload reinsert UI was added;
  - no DOCX upload reinsert UI was added;
  - no PDF reinsert was added;
  - no AI/cloud/rehydration behavior was added;
  - `apply_replacements_to_text` was not altered.

Validation:

- Local clone/test run could not be performed in the container because outbound GitHub DNS failed:
  - `Could not resolve host: github.com`.
- GitHub Actions: awaiting verification.
- Hugging Face sync: awaiting verification.
- App verification: required because UI behavior changed.

Intentionally not changed:

- `presidio_streamlit.py` was not directly edited.
- No TXT upload reinsert UI added.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download semantics intentionally changed.
- No Scrub Key export/import behavior intentionally changed.
- No secrets, tokens or real personal data stored.

Outcome:

- WP12 is implemented and awaits GitHub Actions, Hugging Face sync and app verification.
- Next recommended workpackage is `WP12B — v13.6 Two-mode UI skeleton app verification closeout`.

---

## WP11 — v13.5 Two-mode reinsert UI planning

Status: completed; planning/specification-only workpackage.

Purpose:

- Plan the future two-mode UI before changing Streamlit UI code.
- Clearly separate `Anonimiseren` from `Originele waarden terugzetten`.
- Decide where pasted-text, TXT and DOCX reinsert should fit.
- Compare current single-scroll workflow, tabs and landing-card options.
- Define the next safe UI implementation workpackage.

Outcome:

- WP11 planning is complete.
- Next recommended implementation workpackage was `WP12 — v13.6 Two-mode UI skeleton and tab separation`.

---

## WP10B — v13.4 TXT/DOCX reinsert foundation verification and closeout

Status: completed; Actions/sync not visible through connector, coordinator verification required.

Outcome:

- WP10B closeout is complete.
- Coordinator should verify Actions/sync externally before marking WP10 formally closed.

---

## WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests

Status: implemented; awaiting coordinator verification of Actions/sync.

Outcome:

- WP10 helper/test foundation is implemented.
- WP10 awaits coordinator verification of GitHub Actions and Hugging Face sync.

---

## WP9 — AI-output / document reinsert workflow UX and architecture review

Status: completed; review-only workpackage.

Outcome:

- WP9 is complete.
- Product direction for reinsert is documented before implementation.

---

## v13.3 — Deterministic reinsert UI app verification closeout

Status: completed and app-verified after Actions/sync verification.

Outcome:

- v13.3 deterministic local reinsert UI is completed, app-verified and formally closed.

---

## Earlier completed work

- v13.3 deterministic reinsert UI implementation.
- v13.3 deterministic reinsert UI planning.
- v13.3 deterministic reinsert helper verification reconciliation.
- v13.2 Scrub Key import/reload UI app verification closeout.
- v13.2 Scrub Key import/reload UI integration.
- v13.2 Scrub Key import/reload helper and tests.
- v13.1 Scrub Key JSON export UI closeout.
- v12.6 Export sanity checks closeout.
- v13.0 Scrub Key specification and pure model.
- v12.5 Final review summary.
- v12.4 Review guidance text.
- Project governance setup.
- v12.3 Review table simplification.
- v12.2 Review focus filters.
- v12.1 Review table status model.
- v11.2 Dutch recognizer integration tests.
- v11.1 Legal reference recognizer hardening.
- v10 Regression test layer.
- v9.1 UI polish and baseline stabilization.
- v9 Dutch Legal UI Layer.

---

## Planned later phase — v13 and beyond

Possible directions:

- WP12B app verification closeout.
- TXT reinsert upload/download UI.
- DOCX reinsert upload/download UI.
- PDF text extraction research only after separate reliability review.
- Further recognizer expansion by legal domain.
