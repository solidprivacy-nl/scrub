# SolidPrivacy Scrub — Workpackages

This file translates `ROADMAP.md` into executable workpackages.

Use:

- `ROADMAP.md` for product direction and phase order.
- `WORKPACKAGES.md` for immediate execution planning and parallelization.
- `CHANGELOG.md` for implementation history.

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

## Completed prerequisite

### WP0 — v12.3 stabilization check

Status: completed by user verification.

Evidence:

- GitHub Actions tests green.
- GitHub to Hugging Face sync green.
- App reloaded successfully.
- pandas Index truth-value error gone.
- Simplified review table working.
- Technical details available in separate expander.

Outcome:

- v12.3 can be treated as stable.
- Work may continue with v12.4.

---

## Active workpackage

### WP1 — v12.4 Review guidance text

Status: implemented; awaiting GitHub Actions and Hugging Face verification.

Goal:

- Make the review workflow self-explanatory for non-technical legal users.

Scope:

- Explain that only checked rows are included in export.
- Explain that `Controle nodig` rows require manual review.
- Explain that the focus filter is a viewing aid, not the export scope.
- Explain that technical details are mainly for audit/debugging.
- Add AI-use guidance: scrub first, then use AI.

Files:

- `review_guidance.py`
- `tests/test_review_guidance.py`
- `fix_streamlit_nested_expanders.py`

Verification:

- GitHub Actions tests must pass.
- GitHub to Hugging Face sync must pass.
- Hugging Face app must show guidance around the review step.

---

## Next sequential UI workpackages

### WP2 — v12.5 Final review summary

Status: planned.

Goal:

- Show export readiness before downloads.

Planned helper module:

- `review_summary.py`

Planned tests:

- `tests/test_review_summary.py`

Expected summary values:

- automatically detected rows;
- rows needing review;
- manually added rows;
- remembered replacements;
- checked rows included in export;
- unchecked rows excluded from export;
- open candidate warning.

Dependency:

- UI integration after WP1 verification.

Parallelization:

- Helper and tests can be prepared in parallel with WP1 verification.
- UI integration should wait.

---

### WP3 — v12.6 Export sanity checks

Status: planned.

Goal:

- Warn users before export if review risk remains.

Planned helper module:

- `export_sanity.py`

Planned tests:

- `tests/test_export_sanity.py`

Checks:

- `Controle nodig` rows remain unchecked;
- candidate rows exist but are not included;
- no replacements selected;
- reminder that user review remains required.

Dependency:

- Best after WP2 because it can reuse summary counts.

Parallelization:

- Helper and tests can be prepared early.
- UI integration should wait until WP2 UI is stable.

---

## Parallel strategic workpackage

### WP4 — v13.0 Scrub Key specification and pure model

Status: planned.

Goal:

- Prepare the strategic v13 Scrub Key / Reinsert phase without touching the active review UI yet.

Planned files:

- `SCRUB_KEY_SPEC.md`
- `scrub_key.py`
- `tests/test_scrub_key.py`

Initial Scrub Key fields:

- original value;
- placeholder;
- entity type;
- type label;
- source;
- review status;
- include state;
- timestamp;
- optional document/project/dossier label.

Parallelization:

- Safe to start while v12 UI work continues.
- Do not integrate into UI until v12.4–v12.6 are stable.

---

## Recommended execution order

1. Verify WP1 / v12.4 in GitHub Actions and Hugging Face.
2. Prepare WP2 helper and tests.
3. Integrate WP2 UI.
4. Prepare WP3 helper and tests.
5. Integrate WP3 UI.
6. In parallel, start WP4 Scrub Key spec and pure tests.
7. After v12 is complete, begin v13 UI integration.
