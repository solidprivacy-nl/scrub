# Changelog — SolidPrivacy Scrub

## WP42 — Streamlit feasibility boundary review

Status: completed specification/decision/documentation-only.

Files added:

- `STREAMLIT_FEASIBILITY_BOUNDARY_REVIEW.md`
- `tests/test_streamlit_feasibility_boundary_review.py`
- `workpackage_claims/WP42_streamlit_feasibility_boundary_review.md`
- `handover/workpackages/20260612_2030_streamlit_feasibility_boundary_review.md`

Files changed:

- `DECISION_LOG.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Summary:

- Checked for an existing WP42 claim before starting; none existed.
- Created a WP42 claim before changing shared docs.
- Decided Streamlit is feasible only for a small static/read-only highlight preview using synthetic text or extracted main text.
- Decided Streamlit is not yet feasible as the long-term professional document-centric review interface.
- Blocked broad document UI rewrite, click-to-mark sensitive text, synchronized editing, Word/PDF layout rendering, review-decision mutation from highlights, Scrub Key mutation and export blocking based on highlight state.
- Required escaped rendering, non-authoritative view state, color-plus-label accessibility and bounded performance scope.
- Recorded D017 in `DECISION_LOG.md`.
- Added static tests that lock the boundary review.
- No Streamlit UI, review table, export/download, Scrub Key, reinsert, helper runtime behavior, dependency, cloud processing or real-data change was made.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Added static tests should be validated by GitHub Actions.
- App verification: not applicable because no UI behavior changed.

Next recommended step:

- `WP42B — Static highlight preview helper and tests`.
- Alternative: `WP43 — Frontend architecture decision`.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- WP_REPLACE_LOGIC — Easy replace/review logic simplification specification.
- WP41 — Highlight-based review prototype decision.
- WP40 — Document-centric review UX specification.
- WP39 — Clean DOCX export policy.
- ROADMAP — Local installer deferred to final phase.
- WP38 — DOCX hygiene audit report.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
