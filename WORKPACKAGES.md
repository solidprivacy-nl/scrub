# SolidPrivacy Scrub — Workpackages

This file translates `ROADMAP.md` into executable workpackages.

Use:

- `PROJECT_PROMPT.md` for full worker instructions and operating rules.
- `PROJECT_PROMPT_SHORT.md` for the compact ChatGPT Project Instructions version.
- `ROADMAP.md` for product direction and phase order.
- `WORKPACKAGES.md` for immediate execution planning and parallelization.
- `CHANGELOG.md` for implementation history.

---

## Mandatory worker start sequence

Every worker must start by reading, in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

If the active repository is not `solidprivacy-nl/scrub`, stop and report the mismatch.

Every worker must end with a handover summary and write that summary to:

```text
handover/workpackages/
```

Filename format:

```text
handover/workpackages/YYYYMMDD_HHMM_<workpackage_slug>.md
```

---

## Current execution principle

Avoid parallel edits to the same Streamlit UI patch area.

Parallel work is safe for:

- pure helper modules;
- tests;
- specifications;
- documentation;
- non-UI architecture work.

Parallel work is risky for:

- `presidio_streamlit.py`;
- `fix_streamlit_nested_expanders.py`;
- export/download UI blocks;
- shared replacement table flow.

UI integration should therefore happen sequentially.

---

## Completed prerequisite and UI workpackages

### WP0 — v12.3 stabilization check

Status: completed by user verification.

Evidence:

- GitHub Actions tests green.
- GitHub to Hugging Face sync green.
- App reloaded successfully.
- pandas Index truth-value error gone.
- Simplified review table working.
- Technical details available in separate expander.

### WP1 — v12.4 Review guidance text

Status: completed.

### WP2 — v12.5 Final review summary

Status: completed and formally closed after verification.

Implemented files:

- `review_summary.py`
- `tests/test_review_summary.py`
- `tests/test_review_summary_ui_patch.py`
- `fix_streamlit_nested_expanders.py`

Outcome:

- The app shows `Eindcontrole vóór download` before downloads.
- The summary is advisory and does not change export/download semantics.

### WP3 — v12.6 Export sanity checks

Status: completed and formally closed.

Implemented files:

- `export_sanity.py`
- `tests/test_export_sanity.py`
- `tests/test_export_sanity_ui_patch.py`
- `fix_streamlit_nested_expanders.py`

Outcome:

- The app shows advisory `Extra exportcontrole` before downloads.
- Downloads are not blocked.
- TXT, CSV, DOCX and PDF export behavior is not changed.
- v12 Review UX line is complete from WP1 through WP3.

---

## Completed strategic / helper workpackages

### WP4 — v13.0 Scrub Key specification and pure model

Status: completed.

Implemented files:

- `SCRUB_KEY_SPEC.md`
- `scrub_key.py`
- `tests/test_scrub_key.py`

### WP4B / WP4B-FIX — v13.1 Scrub Key JSON export UI and mapping hotfix

Status: completed and app-verified.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_ui_patch.py`

### WP5 — v13.2 Scrub Key import/reload helper and tests

Status: completed.

Implemented files:

- `scrub_key_import.py`
- `tests/test_scrub_key_import.py`

### WP6 — v13.2 Scrub Key import/reload UI integration

Status: completed and app-verified.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_import_ui_patch.py`

### WP7A / WP7B / WP7B-FINAL — v13.3 Deterministic reinsert helper

Status: completed and formally closed after Actions/sync verification.

Implemented files:

- `scrub_key_reinsert.py`
- `tests/test_scrub_key_reinsert.py`

### WP8 — v13.3 Deterministic reinsert UI planning

Status: implemented; reinsert UI implementation completed in WP8B and app-verified in WP8C.

Implemented files:

- `REINSERT_UI_SPEC.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1900_v13_3_reinsert_ui_planning.md`

### WP8B / WP8C — v13.3 Deterministic reinsert UI implementation and app verification closeout

Status: completed and app-verified after Actions/sync verification.

Implemented files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_reinsert_ui_patch.py`
- `tests/test_scrub_key_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `handover/workpackages/20260607_1915_v13_3_reinsert_ui_implementation.md`
- `handover/workpackages/20260607_1930_v13_3_reinsert_ui_app_closeout.md`

Outcome:

- v13.3 deterministic local reinsert UI is completed, app-verified and formally closed.
- No AI calls, cloud processing, automatic document rehydration or DOCX/PDF reinsert were added.
- Existing scrubbed export/download behavior was not changed.

### WP9 — AI-output / document reinsert workflow UX and architecture review

Status: completed; review-only workpackage.

Added files:

- `AI_OUTPUT_REINSERT_WORKFLOW_REVIEW.md`
- `handover/workpackages/20260608_0000_ai_output_reinsert_workflow_review.md`

Outcome:

- Recommended two-mode direction: `Anonimiseren` and `Originele waarden terugzetten`.
- Recommended keeping pasted-text reinsert as fallback.
- Recommended controlled TXT/DOCX phases before PDF.
- Recommended local-only, deterministic, helper-first architecture.

### WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests

Status: implemented; awaiting coordinator verification of Actions/sync.

Added files:

- `scrub_key_document_reinsert.py`
- `tests/test_scrub_key_document_reinsert.py`
- `handover/workpackages/20260608_0000_v13_4_txt_docx_reinsert_foundation.md`

Outcome:

- Added `reinsert_text_document(text, scrub_key)`.
- Added `reinsert_txt_bytes(content, scrub_key, encoding="utf-8")`.
- Added `reinsert_docx_bytes(content, scrub_key)`.
- Reuses existing deterministic `reinsert_from_scrub_key(...)` logic.
- No UI, PDF, AI, cloud, or export/download behavior change.

Validation status:

- Local reconstructed targeted validation:
  - `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_reinsert.py` → 12 passed.
  - `PYTHONPATH=. pytest -q tests/test_scrub_key_document_reinsert.py` → 14 passed.
- Local reconstructed full available subset:
  - `PYTHONPATH=. pytest -q` → 32 passed.
- Repository clone via container was not possible because outbound GitHub DNS was unavailable.

### WP10B — v13.4 TXT/DOCX reinsert foundation verification and closeout

Status: completed; Actions/sync not visible through connector, coordinator verification required.

Added files:

- `handover/workpackages/20260608_0000_v13_4_txt_docx_reinsert_foundation_closeout.md`

Outcome:

- WP10 closeout was performed without changing code.
- Actions/sync could not be verified through connector-visible status data.
- WP10 remains implemented and awaits coordinator verification of Actions/sync.

### WP11 — v13.5 Two-mode reinsert UI planning

Status: completed; planning/specification-only workpackage.

Added files:

- `TWO_MODE_UI_SPEC.md`
- `handover/workpackages/20260608_0000_v13_5_two_mode_ui_planning.md`

Outcome:

- Recommended moving Scrub to a two-mode interface:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.
- Compared current single-scroll workflow, Streamlit tabs, and landing cards.
- Recommended Streamlit tabs or clear mode panels as first implementation.
- Recommended landing cards as longer-term product direction.
- Planned TXT/DOCX reinsert UI phasing and kept PDF out of implementation scope.

---

## Current implementation workpackages

### WP12 — v13.6 Two-mode UI skeleton and tab separation

Status: implemented; coordinator evidence showed Actions/sync green, but app verification found insufficient content separation.

Coordinator evidence:

```text
Tests #145 green — commit 5d879cc
Sync #159 green — commit 5d879cc
Tests #146 green — commit 79d771e
Sync #160 green — commit 79d771e
Tests #147 green — commit e106f7c
Sync #161 green — commit e106f7c
```

Outcome:

- The visual mode navigation existed.
- App verification showed the full anonymization workflow still appeared above the reinsert flow when using `Originele waarden terugzetten`.
- This required WP12-FIX.

### WP12-FIX — v13.6 Two-mode UI content separation cleanup

Status: implemented; produced a blocking runtime indentation error in Hugging Face and required WP12-FIX2.

Coordinator evidence:

```text
Tests #150 green — commit de01c0b
Sync #164 green — commit de01c0b
Tests #151 green — commit 911e093
Sync #165 green — commit 911e093
```

Runtime failure:

```text
File "/home/user/app/presidio_streamlit.py", line 380
    st.markdown("**Scrub Key laden**")
    ^
IndentationError: unexpected indent
```

Outcome:

- WP12-FIX separated the intended content paths conceptually.
- The generated Python source was syntactically invalid because the reinsert branch block indentation was too deep.
- Do not start closeout from WP12-FIX; use WP12-FIX2 instead.

### WP12-FIX2 — v13.6 Two-mode indentation/runtime hotfix

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Changed files:

- `fix_streamlit_nested_expanders.py`
- `tests/test_two_mode_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Added files:

- `handover/workpackages/20260608_0000_v13_6_two_mode_indentation_hotfix.md`

Implemented behavior:

- Corrected the generated indentation for `Scrub Key laden` and the reinsert UI block under:
  - `if solidprivacy_work_mode == "Originele waarden terugzetten":`.
- Reinsert branch injected blocks now start with a single branch indentation level.
- The anonymization branch still uses `indent_block(anonymization_flow)` under `else:`.
- Two-mode behavior remains:
  - `Anonimiseren` shows the anonymization/review/export workflow;
  - `Originele waarden terugzetten` shows Scrub Key load + local pasted-text reinsert.

Validation status:

- Updated `tests/test_two_mode_ui_patch.py` with a compile guard that reconstructs the generated two-mode source snippet and calls:
  - `compile(..., "generated_two_mode_source.py", "exec")`.
- The test specifically guards against:
  - `IndentationError`;
  - `SyntaxError`;
  - the known `st.markdown("**Scrub Key laden**")` unexpected-indent failure.
- The test also asserts that reinsert block strings start with exactly one branch indentation level, not two.
- Local clone/test run could not be performed in the container because outbound GitHub DNS failed:
  - `Could not resolve host: github.com`.
- GitHub Actions: awaiting verification.
- Hugging Face sync: awaiting verification.
- App verification: required because this was a blocking runtime failure.

Boundaries preserved:

- `presidio_streamlit.py` was not directly edited.
- No TXT upload reinsert UI added.
- No DOCX upload reinsert UI added.
- No PDF reinsert added.
- No AI calls added.
- No cloud processing added.
- No automatic document rehydration added.
- No existing scrubbed export/download semantics intentionally changed.
- No Scrub Key JSON export/import semantics intentionally changed beyond fixing generated runtime validity.
- No secrets, tokens or real personal data stored.

---

## Active / next recommended workpackage

### WP12-FIX2-CLOSEOUT — v13.6 Two-mode indentation/runtime app verification closeout

Status: recommended next closeout workpackage after coordinator evidence.

Goal:

- Verify GitHub Actions tests.
- Verify GitHub to Hugging Face sync.
- Verify the Hugging Face app starts without script execution error.
- Verify app behavior for both modes.
- Close WP12-FIX2 only after evidence confirms the runtime error is gone.

Required app verification:

- No script execution error appears.
- No `IndentationError` appears.
- No `SyntaxError` appears.
- `Anonimiseren` mode is visible.
- `Originele waarden terugzetten` mode is visible.
- `Anonimiseren` shows the anonymization flow.
- `Originele waarden terugzetten` shows Scrub Key load + pasted-text reinsert only.
- Reinsert still works.
- Existing downloads remain available.
- No TXT/DOCX upload reinsert UI appears yet.
- No PDF reinsert appears.
- No AI/cloud behavior appears.

Recommended later workpackages:

```text
WP13 — v13.7 TXT reinsert upload/download UI
WP14 — v13.8 DOCX reinsert upload/download UI
WP15 — PDF text extraction reliability review only
```

---

## Recommended execution order

1. Verify WP12-FIX2 GitHub Actions and Hugging Face sync.
2. Verify the Hugging Face app starts without script execution error.
3. Verify the actual two-mode content separation in the app.
4. Close WP12-FIX2 through closeout if verification is green.
5. After WP12-FIX2 is app-verified, implement TXT reinsert upload/download UI.
6. After TXT UI is verified, implement DOCX reinsert upload/download UI.
7. Keep PDF full reinsert out of scope until a separate reliability review.
8. Keep AI/cloud behavior out unless explicitly approved.
9. Preserve export/download and Scrub Key import/export semantics.
