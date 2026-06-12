# SolidPrivacy Scrub — Workpackages

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Repository: `solidprivacy-nl/scrub`.

## Required workpackage claim check

Before starting implementation or documentation changes, check:

```text
workpackage_claims/
```

If a claim file for the same workpackage exists with status `in_progress`, stop and report that another worker has already claimed the package.

If no claim exists, create a new claim file before changing code, tests, UI, export, schema or shared documentation. Use `GitHub.create_file` so a duplicate claim fails instead of silently overwriting another worker.

When done, update the same claim file to `completed` and include the final commit/PR, handover path, tests/checks and next step.

## Current status

```text
WP28C — implemented; still needs coordinator evidence/app verification.
WP35-WP39 — DOCX hygiene line completed through clean-DOCX export policy.
WP40-WP42D — review UX line implemented through experimental static highlight preview UI; awaiting Actions/HF sync/app verification.
WP_REPLACE_LOGIC — easy replace/review logic simplification specification completed with artifact limitation.
WP_REPLACE_LOGIC_HELPER — replacement decision helper and tests implemented.
WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration completed.
WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration completed.
WP50-WP51 — pilot/ICP thinking artifacts completed, but Phase 7 is parked.
WP51B — MVP product quality gate recorded.
```

## MVP product quality gate

The active product priority is:

```text
Import -> Scrub -> Review -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

WP52 is parked until the MVP product quality gate is passed.

## Review UX line

```text
WP40 — Document-centric review UX specification: completed.
WP41 — Highlight-based review prototype decision: completed.
WP42 — Streamlit feasibility boundary review: completed.
WP42B — Static highlight preview helper and tests: completed.
WP42C — Static highlight preview UI planning: completed.
WP42D — Static highlight preview UI integration: implemented; awaiting Actions/HF sync/app verification.
```

WP42D artifacts:

```text
fix_streamlit_static_highlight_preview.py
tests/test_static_highlight_preview_ui_integration_patch.py
Dockerfile
WORKPACKAGES.md
CHANGELOG.md
RELEASE_NOTES.md
RISK_REGISTER.md
workpackage_claims/WP42D_static_highlight_preview_ui_integration.md
handover/workpackages/20260612_2130_static_highlight_preview_ui_integration.md
```

WP42D summary:

- Added a small post-patch Streamlit integration for an experimental read-only static highlight preview panel.
- The panel appears before the authoritative replacement table.
- It uses `build_static_highlight_preview(...)` and renders only helper-provided `escaped_text` inside trusted markup.
- It gates rendering on `safe_to_render`, `read_only`, `non_authoritative`, `mutation_allowed=False`, `export_blocking=False` and `scrub_key_changes=False`.
- It limits preview to small text and the first 40 rows.
- It does not mutate review rows, export/download state, Scrub Key data or reinsert behavior.

Next review UX step:

```text
WP42D-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout
```

## Replace/review logic line

```text
WP_REPLACE_LOGIC — completed with artifact limitation.
WP_REPLACE_LOGIC_HELPER — implemented helper/tests-only.
WP_REPLACE_LOGIC_UI_PLAN — completed planning/tests/documentation-only.
WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — completed tests/documentation-only.
```

WP_REPLACE_LOGIC_UI_CONTRACT_TESTS artifacts:

```text
tests/test_replace_logic_ui_contract.py
WORKPACKAGES.md
CHANGELOG.md
RISK_REGISTER.md
workpackage_claims/WP_REPLACE_LOGIC_UI_CONTRACT_TESTS_replacement_decision_integration.md
handover/workpackages/20260612_2145_replace_logic_ui_contract_tests.md
```

Summary:

- Added contract tests mapping planned Dutch UI labels to supported `replacement_decision.py` review states.
- Added contract tests mapping planned scope labels to supported helper scopes.
- Tested exact and normalized affected-occurrence behavior through `matching_occurrence_ids(...)`.
- Tested `build_replacement_audit(...)` report-only/export-readiness behavior.
- Locked boundaries from `REPLACE_LOGIC_UI_PLAN.md`: no UI implementation, no export blocking, no Scrub Key behavior change, no click-to-mark implementation, existing table remains fallback/control surface.
- Used synthetic values only.

Next replace/review logic step:

```text
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — only after coordinator explicitly approves UI work and after relevant contract tests are green.
```

Do not start replacement UI implementation until coordinator approves UI work.

## Active / next recommended execution queue

```text
1. WP42D-VERIFY — verify GitHub Actions, Hugging Face sync and app behavior for the static highlight preview UI.
2. Coordinator/user evidence still needed for WP28C Actions/HF sync and app verification if not already available.
3. WP39B — DOCX hygiene audit UI planning, if coordinator wants to continue DOCX hygiene first.
4. WP43 — Frontend architecture decision, if coordinator wants architecture before more UI implementation.
```

## Blocked work

Do not start yet without separate approval:

```text
WP36 — DOCX metadata cleaner helper
WP52 — Pilot intake and NDA process
WP_REPLACE_LOGIC_UI_IMPLEMENTATION — replacement decision UI implementation
```

Also blocked until separate approval or later specs:

- Scrub Key encryption implementation.
- Scrub Key JSON schema migration.
- Placeholder migration.
- Robust placeholder generation in product flow.
- Placeholder auto-repair or guessed placeholder intent.
- DOCX comment/tracked-change removal.
- Clean DOCX export blocking implementation.
- Restored PDF output.
- OCR.
- Cloud document processing.
- MSI implementation.
- PyInstaller/Tauri/Electron implementation.
- Broad document-centric Streamlit UI rewrite.
- Click-to-mark sensitive text implementation.
- Authoritative highlight-based review mutation.
