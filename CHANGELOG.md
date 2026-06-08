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

## WP12-FIX — v13.6 Two-mode UI content separation cleanup

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Purpose:

- Fix the WP12 app-verification issue where mode navigation existed but content was not separated enough.
- Ensure `Originele waarden terugzetten` does not show the full anonymization/review/export workflow above the reinsert flow.
- Keep `Anonimiseren` focused on the existing anonymization workflow.
- Keep `Originele waarden terugzetten` focused on Scrub Key load + local pasted-text reinsert.

Files added or changed:

- Changed `fix_streamlit_nested_expanders.py`.
- Changed `tests/test_two_mode_ui_patch.py`.
- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `handover/workpackages/20260608_0000_v13_6_two_mode_content_separation_cleanup.md`.

Main change:

- The earlier WP12 two-mode skeleton already existed, but only added visible mode navigation.
- WP12-FIX replaces skeleton-only rendering with conditional mode rendering using `solidprivacy_work_mode = st.radio(...)`.
- If the user selects `Originele waarden terugzetten`, the app renders only:
  - `Scrub Key laden`;
  - Scrub Key upload/paste validation;
  - pasted-text local reinsert;
  - restored-output warning;
  - local-only/no-AI/no-cloud text;
  - `Zet originele waarden lokaal terug`;
  - `Herstelde tekst`;
  - `Download herstelde tekst (.txt)`;
  - `Controleverslag terugzetten`.
- The existing anonymization workflow is rendered under the `Anonimiseren` branch.
- The anonymization/export review summary keeps Scrub Key JSON export, but no longer embeds Scrub Key import/reinsert inside the scrubbed export block.

Tests updated:

- `tests/test_two_mode_ui_patch.py` now checks:
  - both mode labels exist;
  - conditional work-mode rendering exists;
  - reinsert markers are associated with `Originele waarden terugzetten`;
  - anonymization markers are associated with the `Anonimiseren` branch;
  - reinsert flow is not embedded in the anonymization review/export summary block;
  - existing Scrub Key export/import labels remain;
  - existing scrubbed download markers remain;
  - no TXT upload reinsert UI was added;
  - no DOCX upload reinsert UI was added;
  - no PDF reinsert was added;
  - no AI/cloud/rehydration behavior was added;
  - `apply_replacements_to_text` was not altered.

Validation:

- Coordinator evidence for prior WP12 showed green Actions/sync, but app verification found the content separation issue:
  - `Tests #145 green — commit 5d879cc`;
  - `Sync #159 green — commit 5d879cc`;
  - `Tests #146 green — commit 79d771e`;
  - `Sync #160 green — commit 79d771e`;
  - `Tests #147 green — commit e106f7c`;
  - `Sync #161 green — commit e106f7c`.
- Local clone/test run for WP12-FIX could not be performed in the container because outbound GitHub DNS failed:
  - `Could not resolve host: github.com`.
- GitHub Actions: awaiting verification for WP12-FIX commits.
- Hugging Face sync: awaiting verification for WP12-FIX commits.
- App verification: required because UI behavior changed.

Intentionally not changed:

- `presidio_streamlit.py` was not directly edited.
- No TXT upload reinsert UI added.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download semantics intentionally changed inside `Anonimiseren`.
- No Scrub Key JSON export behavior intentionally changed inside `Anonimiseren`.
- No Scrub Key storage, secrets, tokens or real personal data added.

Outcome:

- WP12-FIX is implemented and awaits GitHub Actions, Hugging Face sync and app verification.
- Next recommended workpackage is `WP12-FIX-CLOSEOUT — v13.6 Two-mode content separation app verification closeout`.

---

## WP12 — v13.6 Two-mode UI skeleton and tab separation

Status: implemented; coordinator evidence showed Actions/sync green, but app verification found insufficient content separation.

Purpose:

- Implement the first two-mode UI structure with minimal risk.
- Make the two main user intents visible:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.
- Keep existing behavior working.
- Avoid a full landing-page refactor.

Outcome:

- WP12 created the first visible mode skeleton.
- App verification showed that content was not yet separated clearly enough.
- WP12-FIX was created to address this.

---

## WP11 — v13.5 Two-mode reinsert UI planning

Status: completed; planning/specification-only workpackage.

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

- WP12-FIX-CLOSEOUT app verification closeout.
- TXT reinsert upload/download UI.
- DOCX reinsert upload/download UI.
- PDF text extraction research only after separate reliability review.
- Further recognizer expansion by legal domain.
