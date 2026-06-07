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

## Completed UI workpackages

### WP1 — v12.4 Review guidance text

Status: implemented; GitHub Actions and Hugging Face sync confirmed green by coordinator; app guidance visually confirmed earlier by user.

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

- GitHub Actions tests passed.
- GitHub to Hugging Face sync passed.
- Hugging Face app showed guidance around the review step.

---

### WP2 — v12.5 Final review summary

Status: completed and formally closed after verification.

Goal:

- Show export readiness before downloads.

Implemented helper module:

- `review_summary.py`

Implemented tests:

- `tests/test_review_summary.py`
- `tests/test_review_summary_ui_patch.py`

Implemented summary values:

- automatically detected rows;
- rows needing review;
- manually added rows;
- remembered replacements;
- checked rows included in export;
- unchecked rows excluded from export;
- open candidate warning;
- Dutch readiness label and markdown lines.

UI integration:

- `fix_streamlit_nested_expanders.py` imports the review summary helpers.
- The app shows `Eindcontrole vóór download` immediately above the download/export section.
- The summary is advisory and does not change export/download semantics.

Verification evidence:

- Latest implementation handover commit before closeout: `ab1c926dfb6a1587f1ec57c3f895d1a5211fd645`.
- Coordinator reported GitHub Actions tests green for the v12.5 review summary line.
- Coordinator reported GitHub to Hugging Face sync green for the v12.5 review summary line.
- Hugging Face app was visually verified by the coordinator/user.
- The app showed `Eindcontrole vóór download` before the download section.
- Downloads were reported as still working after visual verification: text, CSV, DOCX and PDF.

Outcome:

- v12.5 is complete.
- No export semantics were changed.
- WP3 can continue as the next active workpackage.

---

## Active workpackage

### WP3 — v12.6 Export sanity checks

Status: helper implemented; local targeted tests passed; GitHub Actions and Hugging Face sync not independently confirmed by this worker.

Goal:

- Warn users before export if review risk remains.

Implemented helper module:

- `export_sanity.py`

Implemented tests:

- `tests/test_export_sanity.py`

Implemented checks:

- `Controle nodig` rows remain unchecked;
- candidate rows exist but are not included;
- no replacements selected;
- user review remains required;
- export is advisory and not guaranteed anonymization.

Validation:

- Local targeted validation passed in the WP3 handover: `PYTHONPATH=. pytest -q tests/test_export_sanity.py tests/test_review_summary.py` → 12 passed.
- Latest WP3 handover commit checked: `4d721e3aed3bf28cfdaeb096c0e9cd227885f1a6`.
- Connector check attempted for WP3 commits `5342e0eef663817036e91f823b4389b338b9223c`, `704ae03788702ce33263343743a69f8139f16319`, `869e3804edf04e0cbdf7ab69b034e7bc707de8c3`, and `4d721e3aed3bf28cfdaeb096c0e9cd227885f1a6`.
- GitHub combined status returned `statuses: []` for checked WP3 commits.
- Commit workflow-run lookup returned `workflow_runs: []` for checked WP3 commits.
- Therefore this worker could not independently confirm green GitHub Actions or Hugging Face sync from the connector.

Boundaries preserved:

- No UI files changed.
- No export/download behavior changed.
- Downloads are not blocked.
- No Scrub Key logic added.

Next step:

- Coordinator should verify the GitHub Actions `Tests` and GitHub to Hugging Face sync status in the GitHub UI for the WP3/WP4 commit line.
- Integrate WP3 warnings into the export UI only after external Actions/sync verification is green.

---

## Parallel strategic workpackage

### WP4 — v13.0 Scrub Key specification and pure model

Status: implemented; local targeted tests passed; GitHub Actions and Hugging Face sync not independently confirmed by this worker.

Goal:

- Prepare the strategic v13 Scrub Key / Reinsert phase without touching the active review UI yet.

Implemented files:

- `SCRUB_KEY_SPEC.md`
- `scrub_key.py`
- `tests/test_scrub_key.py`
- `handover/workpackages/20260607_1342_v13_0_scrub_key_spec_model.md`

Implemented Scrub Key fields:

- original value;
- placeholder;
- entity type;
- user-facing type label;
- source;
- review status;
- include state;
- timestamp;
- optional document/project/dossier label.

Implemented safety/spec decisions:

- A Scrub Key makes scrubbed text reversible.
- This is pseudonymization, not full anonymization.
- The key must stay local and protected.
- Users should not share the key with external AI services unless explicitly intended and allowed.
- Scrub Key export/import must not silently change document meaning.
- v13.0 excluded-row policy is `omitted`.
- The pure model does not generate timestamps itself; timestamps must be supplied by the caller and validation catches missing timestamps.

Implemented helper functions:

- `build_scrub_key(rows, document_label=None) -> dict`
- `scrub_key_to_json(scrub_key) -> str`
- `scrub_key_from_json(text) -> dict`
- `validate_scrub_key(scrub_key) -> list[str]`

Validation:

- Local targeted validation passed: `PYTHONPATH=. pytest -q tests/test_scrub_key.py` → 6 passed.
- Full local test run not performed because the container could not clone the full repository.
- Latest WP4 target/head commit checked: `d65364373e4d3612044d8688ac17e11de81c07e5`.
- GitHub combined status returned `statuses: []` for `d65364373e4d3612044d8688ac17e11de81c07e5`.
- Commit workflow-run lookup returned `workflow_runs: []` for `d65364373e4d3612044d8688ac17e11de81c07e5`.
- Therefore this worker could not independently confirm green GitHub Actions or Hugging Face sync from the connector.

Boundaries respected:

- No edit to `presidio_streamlit.py`.
- No edit to `fix_streamlit_nested_expanders.py`.
- No export/download buttons added.
- No reinsert UI added.
- No cloud processing introduced.
- No secrets or real personal data stored.

Parallelization:

- Safe to continue non-UI v13 model/spec work if needed.
- Do not integrate into UI until v12.4–v12.6 are stable.

---

## Recommended execution order

1. Coordinator verifies GitHub Actions `Tests` and GitHub to Hugging Face sync in the GitHub UI for WP3/WP4, because the connector returned no check-run evidence.
2. Integrate WP3 UI only after helper tests and external Actions/sync verification are green.
3. After v12 is complete, begin v13 UI integration for Scrub Key JSON export.
