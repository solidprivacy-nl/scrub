# Changelog — SolidPrivacy Scrub

## WP42B — Static highlight preview helper and tests

Status: completed helper/tests/documentation-only.

Files added:

- `highlight_preview.py`
- `tests/test_highlight_preview.py`
- `workpackage_claims/WP42B_static_highlight_preview_helper_tests.md`
- `handover/workpackages/20260612_2045_static_highlight_preview_helper_tests.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Summary:

- Checked for an existing WP42B claim before starting; none existed.
- Added a pure helper/model for static read-only highlight preview rendering inputs.
- Validates span ids, zero-based offsets, category labels, duplicate ids, unsupported categories, overlapping spans and label-to-displayed-text consistency.
- Builds escaped text/highlight segments with Dutch category labels and accessibility labels.
- Keeps explicit non-authoritative flags: read-only, no mutation, no export blocking, no Scrub Key changes and no UI requirement.
- Added synthetic tests for escaping, invalid offsets, label mismatch, duplicate ids, unsupported categories, overlapping spans, category labels, non-string text and no-real-data boundaries.
- No Streamlit UI, review table mutation, export/download behavior, Scrub Key behavior, reinsert behavior, dependency, cloud processing or real-data change was made.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Added helper tests should be validated by GitHub Actions.
- App verification: not applicable because no UI behavior changed.

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
