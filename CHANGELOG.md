# Changelog — SolidPrivacy Scrub

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

## WP42B — Static highlight preview helper and tests

Status: completed helper/tests/documentation-only.

Next recommended step:

- `WP42C — Static highlight preview UI planning`.
- Alternative: `WP43 — Frontend architecture decision`.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- WP42 — Streamlit feasibility boundary review.
- WP_REPLACE_LOGIC — Easy replace/review logic simplification specification.
- WP41 — Highlight-based review prototype decision.
- WP40 — Document-centric review UX specification.
- WP39 — Clean DOCX export policy.
- WP38 — DOCX hygiene audit report.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
