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

## WP12-FIX2 — v13.6 Two-mode indentation/runtime hotfix

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Purpose:

- Fix the blocking Hugging Face runtime failure introduced by WP12-FIX.
- Restore app startup.
- Preserve the two-mode behavior:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.

Blocking runtime error:

```text
File "/home/user/app/presidio_streamlit.py", line 380
    st.markdown("**Scrub Key laden**")
    ^
IndentationError: unexpected indent
```

Files added or changed:

- Changed `fix_streamlit_nested_expanders.py`.
- Changed `tests/test_two_mode_ui_patch.py`.
- Changed `WORKPACKAGES.md`.
- Changed `CHANGELOG.md`.
- Added `handover/workpackages/20260608_0000_v13_6_two_mode_indentation_hotfix.md`.

Main change:

- Corrected generated indentation around `Scrub Key laden` and the local reinsert UI block.
- Reinsert branch blocks now start with one branch indentation level under:
  - `if solidprivacy_work_mode == "Originele waarden terugzetten":`.
- The anonymization branch still uses `indent_block(anonymization_flow)` under `else:`.
- No feature scope was added.

Tests updated:

- `tests/test_two_mode_ui_patch.py` now includes a compile guard that reconstructs the generated two-mode source snippet and calls:
  - `compile(..., "generated_two_mode_source.py", "exec")`.
- This guards against:
  - `IndentationError`;
  - `SyntaxError`;
  - the specific unexpected-indent failure at `st.markdown("**Scrub Key laden**")`.
- The tests also assert that the reinsert block strings start with exactly one branch indentation level, not two.

Validation:

- Prior WP12-FIX technical evidence was:
  - `Tests #150 green — commit de01c0b`;
  - `Sync #164 green — commit de01c0b`;
  - `Tests #151 green — commit 911e093`;
  - `Sync #165 green — commit 911e093`.
- App verification then failed with the runtime `IndentationError` shown above.
- Local clone/test run for WP12-FIX2 could not be performed in the container because outbound GitHub DNS failed:
  - `Could not resolve host: github.com`.
- GitHub Actions: awaiting verification for WP12-FIX2 commits.
- Hugging Face sync: awaiting verification for WP12-FIX2 commits.
- App verification: required because this was a blocking runtime failure.

Intentionally not changed:

- `presidio_streamlit.py` was not directly edited.
- No TXT upload reinsert UI added.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No existing TXT, CSV, DOCX or PDF scrubbed export/download semantics intentionally changed.
- No Scrub Key JSON export/import semantics intentionally changed except fixing generated runtime validity.
- No Scrub Key storage, secrets, tokens or real personal data added.

Outcome:

- WP12-FIX2 is implemented and awaits GitHub Actions, Hugging Face sync and app verification.
- Next recommended workpackage is `WP12-FIX2-CLOSEOUT — v13.6 Two-mode indentation/runtime app verification closeout`.

---

## WP12-FIX — v13.6 Two-mode UI content separation cleanup

Status: implemented; produced a blocking runtime indentation error and required WP12-FIX2.

Purpose:

- Fix the WP12 app-verification issue where mode navigation existed but content was not separated enough.
- Ensure `Originele waarden terugzetten` does not show the full anonymization/review/export workflow above the reinsert flow.
- Keep `Anonimiseren` focused on the existing anonymization workflow.
- Keep `Originele waarden terugzetten` focused on Scrub Key load + local pasted-text reinsert.

Outcome:

- WP12-FIX separated the intended content paths conceptually.
- App verification showed the generated Python source was syntactically invalid because the reinsert branch block indentation was too deep.
- WP12-FIX2 was created as the blocking runtime hotfix.

---

## WP12 — v13.6 Two-mode UI skeleton and tab separation

Status: implemented; coordinator evidence showed Actions/sync green, but app verification found insufficient content separation.

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

- WP12-FIX2-CLOSEOUT app verification closeout.
- TXT reinsert upload/download UI.
- DOCX reinsert upload/download UI.
- PDF text extraction research only after separate reliability review.
- Further recognizer expansion by legal domain.
