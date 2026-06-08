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

## WP12B — v13.6 Two-mode UI app verification closeout

Status: completed and app-verified after Actions/sync verification.

Purpose:

- Administratively close WP12, WP12-FIX and WP12-FIX2 after successful technical verification and app verification.
- Record that v13.6 two-mode UI is now complete.
- Confirm that no further closeout blocker remains before WP13.

Implementation sequence closed:

- WP12 introduced the two-mode UI skeleton.
- WP12-FIX cleaned up content separation.
- WP12-FIX2 fixed the indentation/runtime error.
- WP12B records successful Actions/sync and app verification.

Technical verification evidence:

```text
Tests #155 green — commit b27d115
Sync to Hugging Face Space #169 green — commit b27d115

Tests #156 green — commit 0e357bb
Sync to Hugging Face Space #170 green — commit 0e357bb

Tests #157 green — commit 268234d
Sync to Hugging Face Space #171 green — commit 268234d
```

Latest verified WP12-FIX2 commit:

```text
268234d9d1aeb9c82658c4c30702f51cfdd58c96
```

App verification confirmed:

- The app starts without Script execution error.
- No `IndentationError` appears.
- `Anonimiseren` mode remains available.
- `Originele waarden terugzetten` mode remains available and selectable.
- `Originele waarden terugzetten` now focuses on Scrub Key load + local pasted-text reinsert.
- The full anonymization workflow is no longer shown as the main content inside the reinsert mode.
- Existing anonymization workflow remains available in `Anonimiseren`.
- Existing Scrub Key export/import remains available.
- Existing pasted-text reinsert remains available.
- `Scrub Key laden` is visible.
- Scrub Key upload/paste is visible.
- `Valideer en laad Scrub Key` is visible.
- Local pasted-text reinsert section is visible.
- Warning about restored sensitive/confidential values is visible.
- Local-only / no-AI / no-cloud text is visible.
- Text field for reinsert is visible.
- Button `Zet originele waarden lokaal terug` is visible.

Files added or changed:

- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `handover/workpackages/20260608_0000_v13_6_two_mode_ui_app_closeout.md`.

Tests:

- No new tests were added because WP12B is closeout-only.
- Existing validation is based on coordinator evidence:
  - GitHub Actions green;
  - GitHub to Hugging Face sync green;
  - app verification confirmed.

Intentionally not changed:

- No code files were changed in WP12B.
- `fix_streamlit_nested_expanders.py` was not changed in WP12B.
- `presidio_streamlit.py` was not changed.
- No test files were changed.
- No TXT upload reinsert UI added.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download behavior intentionally changed.
- No Scrub Key JSON export/import behavior intentionally changed.
- No Scrub Key storage, secrets, tokens or real personal data added.

Outcome:

- v13.6 two-mode UI is closed as completed and app-verified.
- Next recommended workpackage is `WP13 — v13.7 TXT reinsert upload/download UI`.

---

## WP12-FIX2 — v13.6 Two-mode indentation/runtime hotfix

Status: completed and app-verified through WP12B closeout.

Purpose:

- Fix the blocking Hugging Face runtime failure introduced by WP12-FIX.
- Restore app startup.
- Preserve the two-mode behavior:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.

Blocking runtime error fixed:

```text
File "/home/user/app/presidio_streamlit.py", line 380
    st.markdown("**Scrub Key laden**")
    ^
IndentationError: unexpected indent
```

Outcome:

- Generated indentation around `Scrub Key laden` and the local reinsert UI block was corrected.
- GitHub Actions and Hugging Face sync were later verified green by the coordinator.
- App verification confirmed the script execution error is gone.

---

## WP12-FIX — v13.6 Two-mode UI content separation cleanup

Status: completed through WP12B closeout after WP12-FIX2 runtime hotfix.

Purpose:

- Fix the WP12 app-verification issue where mode navigation existed but content was not separated enough.
- Ensure `Originele waarden terugzetten` does not show the full anonymization/review/export workflow above the reinsert flow.
- Keep `Anonimiseren` focused on the existing anonymization workflow.
- Keep `Originele waarden terugzetten` focused on Scrub Key load + local pasted-text reinsert.

Outcome:

- WP12-FIX separated the intended content paths conceptually.
- WP12-FIX2 corrected the runtime indentation issue.
- WP12B confirmed app verification.

---

## WP12 — v13.6 Two-mode UI skeleton and tab separation

Status: completed and app-verified through WP12B closeout.

Outcome:

- WP12 created the first visible mode skeleton.
- WP12-FIX improved actual content separation.
- WP12-FIX2 fixed the runtime indentation error.
- WP12B closed v13.6 after Actions/sync and app verification.

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

- v13.6 two-mode UI implementation and app verification closeout.
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

- WP13 — v13.7 TXT reinsert upload/download UI.
- WP14 — v13.8 DOCX reinsert upload/download UI.
- PDF text extraction research only after separate reliability review.
- Further recognizer expansion by legal domain.
