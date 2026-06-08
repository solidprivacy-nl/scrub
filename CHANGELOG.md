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

## WP11 — v13.5 Two-mode reinsert UI planning

Status: completed; planning/specification-only workpackage.

Purpose:

- Plan the future two-mode UI before changing Streamlit UI code.
- Clearly separate `Anonimiseren` from `Originele waarden terugzetten`.
- Decide where pasted-text, TXT and DOCX reinsert should fit.
- Compare current single-scroll workflow, tabs and landing-card options.
- Define the next safe UI implementation workpackage.

Files added or changed:

- Added `TWO_MODE_UI_SPEC.md`.
- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `handover/workpackages/20260608_0000_v13_5_two_mode_ui_planning.md`.

Main recommendation:

- Move Scrub toward a two-mode interface:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.
- Use Streamlit tabs or two clear mode panels as the first implementation step.
- Treat a landing choice with two large cards/buttons as the better long-term product direction, but not the next patch-based implementation step.
- Keep pasted-text reinsert available as the simplest and safest fallback.
- Add TXT upload/download reinsert UI after the mode skeleton is verified.
- Add DOCX upload/download reinsert UI later using the WP10 helper.
- Keep PDF reinsert excluded until a separate reliability review.

Options compared:

1. Current single-scroll workflow:
   - lowest short-term cost;
   - too much cognitive load;
   - weak separation between scrubbed and restored privacy states.
2. Streamlit tabs:
   - recommended first step;
   - clear mode separation;
   - lower implementation risk in current app structure.
3. Landing choice with two large cards/buttons:
   - best mature product UX;
   - higher refactor risk;
   - better later after the patch-based UI has been simplified.

Specified user journeys:

- `Anonimiseren`:
  - upload/paste source text or document;
  - review detected replacements;
  - download currently supported scrubbed TXT/DOCX/PDF outputs;
  - optionally download Scrub Key JSON;
  - show warning that Scrub Key is reversible/pseudonymization.
- `Originele waarden terugzetten`:
  - load/paste Scrub Key;
  - choose paste text, upload TXT or upload DOCX;
  - validate key locally;
  - reinsert original values locally;
  - show audit summary;
  - warn restored output may contain sensitive/confidential data again;
  - download restored TXT or DOCX where supported.

Recommended implementation sequence:

1. `WP12 — v13.6 Two-mode UI skeleton and tab separation`.
2. `WP13 — v13.7 TXT reinsert upload/download UI`.
3. `WP14 — v13.8 DOCX reinsert upload/download UI`.
4. `WP15 — PDF text extraction reliability review only`.

Validation:

- Tests: not applicable; planning/specification-only workpackage.
- App verification: not applicable; no UI behavior changed.
- GitHub Actions: not required for planning-only documentation change.
- Hugging Face sync: not required for planning-only documentation change.

Intentionally not changed:

- No UI code changed.
- No edit to `fix_streamlit_nested_expanders.py`.
- No edit to `presidio_streamlit.py`.
- No edit to `scrub_key_document_reinsert.py`.
- No edit to `scrub_key_reinsert.py`.
- No edit to `scrub_key.py`.
- No edit to `scrub_key_import.py`.
- No edit to `tests/*`.
- No TXT/DOCX reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download behavior changed.
- No Scrub Key export/import behavior changed.
- No secrets, tokens or real personal data stored.

Outcome:

- WP11 planning is complete.
- Next recommended implementation workpackage is `WP12 — v13.6 Two-mode UI skeleton and tab separation`.

---

## WP10B — v13.4 TXT/DOCX reinsert foundation verification and closeout

Status: completed; Actions/sync not visible through connector, coordinator verification required.

Purpose:

- Verify and formally close, or pending-close, WP10.
- Check GitHub Actions and Hugging Face sync visibility for implementation commit `eb0c1ed2397ec1a4dc256d6e7e615ac4c026c0ee`.
- Update control files without changing code.

Verification result:

- Commit metadata was visible for `eb0c1ed2397ec1a4dc256d6e7e615ac4c026c0ee`.
- GitHub combined commit status returned an empty status list.
- GitHub workflow-runs query for the commit returned no visible workflow runs.
- GitHub Actions: not visible through connector.
- Hugging Face sync: not visible through connector.
- App verification: not applicable; WP10 was helper/test-only and added no UI behavior.

Outcome:

- WP10B closeout is complete.
- Coordinator should verify Actions/sync externally before marking WP10 formally closed.
- Next recommended workpackage remains WP11 — v13.5 Two-mode reinsert UI planning.

---

## WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests

Status: implemented; awaiting coordinator verification of Actions/sync.

Purpose:

- Prepare document-level reinsert without changing UI first.
- Add pure helper/test foundation for TXT and DOCX reinsert.
- Reuse the existing deterministic Scrub Key reinsert logic.
- Keep PDF, UI, AI calls and cloud processing out of scope.

Outcome:

- WP10 helper/test foundation is implemented.
- WP10 awaits coordinator verification of GitHub Actions and Hugging Face sync.
- Next recommended workpackage is WP11 — v13.5 Two-mode reinsert UI planning.

---

## WP9 — AI-output / document reinsert workflow UX and architecture review

Status: completed; review-only workpackage.

Purpose:

- Decide what Scrub should do next for AI-output and document-level reinsert before implementation starts.
- Challenge whether pasted-text reinsert is enough.
- Challenge whether direct DOCX/PDF reinsert should be added immediately.
- Challenge whether anonymization and de-anonymization should remain in one combined long screen.
- Recommend a model architecture, product direction, tactical sequence, operational safety position and visual/UX direction.

Outcome:

- WP9 is complete.
- Product direction for reinsert is documented before implementation.

---

## v13.3 — Deterministic reinsert UI app verification closeout

Status: completed and app-verified after Actions/sync verification.

Outcome:

- v13.3 deterministic local reinsert UI is completed, app-verified and formally closed.

---

## v13.3 — Deterministic reinsert UI implementation

Status: completed and app-verified after Actions/sync verification.

Outcome:

- v13.3 deterministic local reinsert UI is completed, app-verified and formally closed.

---

## v13.3 — Deterministic reinsert UI planning

Status: implemented; reinsert UI implementation completed in WP8B and app-verified in WP8C.

Outcome:

- v13.3 deterministic reinsert UI was planned and then implemented and app-verified.

---

## v13.3 — Deterministic reinsert helper verification reconciliation

Status: completed and formally closed after Actions/sync verification.

Outcome:

- v13.3 deterministic reinsert helper is completed and formally closed.

---

## v13.2 — Scrub Key import/reload UI app verification closeout

Status: completed, app-verified and closed.

Outcome:

- v13.2 Scrub Key import/reload UI is completed, app-verified and closed.

---

## Earlier completed work

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

- Coordinator verification of WP10 Actions/sync.
- Two-mode UI skeleton and tab separation.
- TXT reinsert upload/download UI.
- DOCX reinsert upload/download UI.
- PDF text extraction research only after separate reliability review.
- Further recognizer expansion by legal domain.
