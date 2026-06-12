# Changelog — SolidPrivacy Scrub

## WP42D — Static highlight preview UI integration

Status: implemented UI patch/tests; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

- `fix_streamlit_static_highlight_preview.py`
- `tests/test_static_highlight_preview_ui_integration_patch.py`
- `workpackage_claims/WP42D_static_highlight_preview_ui_integration.md`
- `handover/workpackages/20260612_2130_static_highlight_preview_ui_integration.md`

Files changed:

- `Dockerfile`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP42D_static_highlight_preview_ui_integration.md`

Summary:

- Added a new post-patch script that injects an experimental read-only static highlight preview panel before the authoritative replacement table.
- The panel uses `build_static_highlight_preview(...)` and renders only helper-provided `escaped_text` inside trusted markup.
- The panel is gated by helper safety flags and is explicitly non-authoritative.
- The existing review table remains authoritative for include/exclude/replacement decisions, Scrub Key and export.
- Added static tests for patch boundaries and Docker startup order.
- No export/download, Scrub Key, reinsert, helper runtime behavior, dependency, cloud processing or real data changed.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Expected checks: `pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py`.
- App verification required after Actions and Hugging Face sync because UI behavior changed.

Next recommended step:

- `WP42D-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout`.

## WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration

Status: completed planning/tests/documentation-only.

Next recommended step:

- `WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration`.

## WP42C — Static highlight preview UI planning

Status: completed planning/tests/documentation-only.

Next recommended step:

- `WP42D — Static highlight preview UI integration`, only if coordinator explicitly approves UI work.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- WP_REPLACE_LOGIC_HELPER — replacement decision helper and tests.
- WP42B — Static highlight preview helper and tests.
- WP42 — Streamlit feasibility boundary review.
- WP_REPLACE_LOGIC — Easy replace/review logic simplification specification.
- WP41 — Highlight-based review prototype decision.
- WP40 — Document-centric review UX specification.
- WP39 — Clean DOCX export policy.
- WP38 — DOCX hygiene audit report.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
