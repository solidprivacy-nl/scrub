# Changelog — SolidPrivacy Scrub

## WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration

Status: completed planning/tests/documentation-only.

Files added:

- `REPLACE_LOGIC_UI_PLAN.md`
- `tests/test_replace_logic_ui_plan.py`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_PLAN_helper_integration.md`
- `handover/workpackages/20260612_1925_replace_logic_ui_plan.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_PLAN_helper_integration.md`

Summary:

- Checked for an existing WP_REPLACE_LOGIC_UI_PLAN claim before starting; none existed.
- Planned how `replacement_decision.py` can later be integrated into the review UI.
- Mapped simple Dutch UI actions to helper states.
- Defined conservative scope controls and affected-count confirmation expectations.
- Kept export readiness advisory only.
- Kept Scrub Key schema and behavior unchanged.
- Added static tests for the plan boundaries.
- No Streamlit UI, review table behavior, export/download behavior, Scrub Key behavior, reinsert behavior, helper runtime behavior, dependency, cloud processing or real data changed.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Added plan tests should be validated by GitHub Actions.
- App verification: not applicable because no UI behavior changed.

Next recommended step:

- `WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration`.

## WP42C — Static highlight preview UI planning

Status: completed planning/tests/documentation-only.

Files added:

- `STATIC_HIGHLIGHT_PREVIEW_UI_PLAN.md`
- `tests/test_static_highlight_preview_ui_plan.py`
- `workpackage_claims/WP42C_static_highlight_preview_ui_planning.md`
- `handover/workpackages/20260612_2110_static_highlight_preview_ui_planning.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP42C_static_highlight_preview_ui_planning.md`

Summary:

- Planned a future experimental read-only Streamlit panel for static highlight preview.
- Required the current replacement table to remain authoritative.
- Required rendering only `escaped_text`, not raw user text as HTML.
- Added static tests for the plan boundaries.
- No Streamlit UI, review table, export/download, Scrub Key, reinsert, helper runtime behavior, dependency, cloud processing or real data changed.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Added plan tests should be validated by GitHub Actions.
- App verification: not applicable because no UI behavior changed.

Next recommended step:

- `WP42D — Static highlight preview UI integration`, only if coordinator explicitly approves UI work.
- Alternative: `WP43 — Frontend architecture decision`.

## WP_REPLACE_LOGIC_HELPER — replacement decision helper and tests

Status: implemented helper/tests-only; awaiting GitHub Actions verification.

Next recommended step:

- `WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration`.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- WP42B — Static highlight preview helper and tests.
- WP42 — Streamlit feasibility boundary review.
- WP_REPLACE_LOGIC — Easy replace/review logic simplification specification.
- WP41 — Highlight-based review prototype decision.
- WP40 — Document-centric review UX specification.
- WP39 — Clean DOCX export policy.
- WP38 — DOCX hygiene audit report.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
