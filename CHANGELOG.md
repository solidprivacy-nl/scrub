# Changelog — SolidPrivacy Scrub

## WP43 — Frontend architecture decision

Status: completed architecture/decision/documentation-only.

Files added:

- `FRONTEND_ARCHITECTURE_DECISION.md`
- `tests/test_frontend_architecture_decision.py`
- `workpackage_claims/WP43_frontend_architecture_decision.md`
- `handover/workpackages/20260612_2215_frontend_architecture_decision.md`

Files changed:

- `DECISION_LOG.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP43_frontend_architecture_decision.md`

Summary:

- Checked for an existing WP43 claim before starting; none existed.
- Decided to keep Streamlit as the MVP validation surface for now.
- Decided not to migrate to a separate frontend yet.
- Decided not to build a professional document editor yet.
- Kept the architecture helper-driven: reusable Python core, thin UI patch layer, contract tests before UI integration.
- Preserved the current review table as authoritative control/audit surface unless a later migration package changes that.
- Defined criteria for reconsidering a separate frontend later.
- Recorded D018 in `DECISION_LOG.md`.
- No UI implementation, Streamlit patch, review table behavior, export/download behavior, Scrub Key behavior, reinsert behavior, dependency, Docker/runtime behavior, cloud processing or real-data change was made.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Added decision tests should be validated by GitHub Actions.
- App verification: not applicable because no UI behavior changed.

Next recommended step:

- Coordinator/user evidence needed for WP42D Actions/HF sync and app verification.
- Alternative if coordinator wants non-UI planning: `WP39B — DOCX hygiene audit UI planning`.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- WP42D-VERIFY — Static highlight preview UI verification closeout.
- WP_REPLACE_LOGIC_UI_CONTRACT_TESTS — UI contract tests for replacement decision integration.
- WP42D — Static highlight preview UI integration.
- WP_REPLACE_LOGIC_UI_PLAN — UI plan for helper integration.
- WP42C — Static highlight preview UI planning.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
