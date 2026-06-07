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

### WP3 — v12.6 Export sanity checks

Status: completed and formally closed after coordinator closeout instruction.

Goal:

- Warn users before export if review risk remains.

Implemented helper module:

- `export_sanity.py`

Implemented tests:

- `tests/test_export_sanity.py`
- `tests/test_export_sanity_ui_patch.py`

Implemented checks:

- `Controle nodig` rows remain unchecked;
- candidate rows exist but are not included;
- no replacements selected;
- user review remains required;
- export is advisory and not guaranteed anonymization.

UI integration:

- `fix_streamlit_nested_expanders.py` imports `build_export_sanity_checks` and `export_sanity_warnings`.
- The app shows `Extra exportcontrole` near `Eindcontrole vóór download` before the download/export section.
- The warning block is advisory only and explicitly says downloads remain available and export settings remain unchanged.
- Downloads are not blocked.
- TXT, CSV, DOCX and PDF export behavior is not changed.

Validation evidence:

- Helper verification was reconciled externally by coordinator: `Tests #58` green and `Sync to Hugging Face Space #72` green for commit `b0bf8ae`.
- UI integration commits:
  - `c60b9b4bfa8944e620546ca26a4fe42c287edaa0` — Integrate export sanity warnings into UI patch.
  - `f5158c9faf8e7676cb8403da0b42b0465539acfa` — Add export sanity UI patch tests.
  - `7d043d13096518d5dca6a5f187189fa3a8471627` — Update workpackage status for export sanity UI.
  - `4a84ddb7ca2b298ce2dcdcc5daf8b9f1cc055023` — Add export sanity UI handover.
- WP3C closeout was requested by the coordinator as administrative closeout only, with no further code changes.

Boundaries preserved:

- No direct edit to `presidio_streamlit.py`.
- No additional code changes in WP3C.
- No export/download behavior changed.
- Downloads are not blocked.
- No Scrub Key logic added in WP3.
- No cloud processing introduced.

Outcome:

- v12.6 is closed.
- v12 Review UX line is complete from WP1 through WP3.
- Next UI phase can move to v13 Scrub Key JSON export after coordinator approval.

---

## Active workpackage

### WP4B — v13.1 Scrub Key JSON export UI integration

Status: implemented; awaiting GitHub Actions, Hugging Face sync and app verification.

Goal:

- Add a local Scrub Key JSON download option after review, without adding import, reload, reinsert or AI-output flows.

Implemented foundation from WP4:

- `SCRUB_KEY_SPEC.md`
- `scrub_key.py`
- `tests/test_scrub_key.py`

Implemented UI integration:

- `fix_streamlit_nested_expanders.py` imports `build_scrub_key`, `scrub_key_to_json` and `validate_scrub_key`.
- The app shows `Scrub Key (JSON)` near the existing final review/download section.
- The app shows a warning that a Scrub Key is pseudonymization, not full anonymization.
- The app warns users not to share the key with AI services or third parties unless consciously intended and allowed.
- The app offers `Download Scrub Key (.json)` with filename `solidprivacy_scrub_key.json`.
- The UI layer adds timestamps at export time, preserving the pure model decision that `scrub_key.py` does not create timestamps itself.

Implemented tests:

- `tests/test_scrub_key_ui_patch.py`

Boundaries preserved:

- No direct edit to `presidio_streamlit.py`.
- No Scrub Key import/reload.
- No reinsert UI.
- No AI-output flow.
- No cloud processing.
- No secret storage.
- No real personal data.
- No change to TXT, CSV, DOCX or PDF export/download behavior.

Validation status:

- Local pytest not run from this connector environment.
- GitHub Actions pending for commits:
  - `a9011ccc3fdb981c3101490fdc8b8996696f75e3` — Integrate Scrub Key JSON export into UI patch.
  - `adb676000d07e6f00b39a378da40adfa9701e0d1` — Add Scrub Key UI patch tests.

Next step:

- Verify GitHub Actions and Hugging Face sync.
- Ask the user/coordinator to verify in the Hugging Face app that `Download Scrub Key (.json)` appears and that existing TXT/CSV/DOCX/PDF downloads still work.

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
- No edit to `fix_streamlit_nested_expanders.py` for v13.0.
- No export/download buttons added for v13.0.
- No reinsert UI added.
- No cloud processing introduced.
- No secrets or real personal data stored.

---

## Recommended execution order

1. Verify GitHub Actions `Tests` and GitHub to Hugging Face sync for WP4B.
2. Ask the user/coordinator to verify the Hugging Face app shows `Download Scrub Key (.json)` and the pseudonymization warning.
3. Confirm TXT/CSV/DOCX/PDF downloads still work.
4. After v13.1 is verified, plan v13.2 Scrub Key import/reload as a separate sequential UI workpackage.
