# Handover — WP39B DOCX hygiene audit UI planning

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP39B — DOCX hygiene audit UI planning`

Status: completed planning/documentation-only.

## Summary

Created `DOCX_HYGIENE_AUDIT_UI_PLAN.md`, a planning document for a later small report-only UI surface for the existing DOCX hygiene audit helper.

The plan is based on WP37, WP38 and WP39:

- `docx_hidden_content_extractor.py` extracts supported hidden DOCX content locally and read-only.
- `docx_hygiene_audit.py` turns that extraction into a report-only audit.
- `CLEAN_DOCX_EXPORT_POLICY.md` states that current DOCX output must not be claimed as clean DOCX and that export blocking/clean-export semantics need separate approval.

No product code, Streamlit UI, tests, export/download behavior, Scrub Key behavior, reinsert behavior, dependencies, cloud processing or real-data fixtures were changed.

## Files added

- `DOCX_HYGIENE_AUDIT_UI_PLAN.md`
- `workpackage_claims/WP39B_docx_hygiene_audit_ui_planning.md`
- `handover/workpackages/20260613_1330_docx_hygiene_audit_ui_planning.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP39B_docx_hygiene_audit_ui_planning.md`

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

Documentation/source checks performed:

- Required start files read: `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Relevant DOCX hygiene files read:
  - `DOCX_HIDDEN_CONTENT_EXTRACTION_HELPER.md`
  - `DOCX_HYGIENE_AUDIT_REPORT.md`
  - `CLEAN_DOCX_EXPORT_POLICY.md`
  - `docx_hygiene_audit.py`
  - `tests/test_docx_hygiene_audit.py`
- Risk/decision context read:
  - `RISK_REGISTER.md`
  - `DECISION_LOG.md`
- Claim checked and created with `GitHub.create_file` before documentation changes.

## Validation status

Planning/documentation-only package completed.

The plan explicitly preserves these boundaries:

- report-only;
- no clean-DOCX guarantee;
- no DOCX cleaning/removal;
- no export blocking;
- no export/download behavior change;
- no Scrub Key change;
- no reinsert behavior change;
- no dependency change;
- no cloud processing;
- no real data.

## GitHub Actions status

Unknown/not required for product runtime validation because this package is planning/documentation-only. GitHub Actions may still run for documentation commits.

## Hugging Face sync status

Unknown/not required for app verification because this package does not change runtime/UI behavior. Hugging Face sync may still run for documentation commits.

## App verification status

Not applicable. No UI/runtime behavior changed.

## Remaining risks

- Product UI still does not consume the DOCX hygiene audit report.
- No DOCX cleaner exists.
- No clean-DOCX export claim is allowed.
- No approved export-blocking implementation exists.
- Unsupported DOCX parts remain future work, including metadata, footnotes, endnotes, text boxes, shapes, charts, embedded objects and custom XML.

## Next recommended step

```text
WP39C — DOCX hygiene audit UI contract tests
```

Only after contract tests are green and coordinator approval is explicit should a later package implement a small report-only UI surface:

```text
WP39D — DOCX hygiene audit UI implementation
```
