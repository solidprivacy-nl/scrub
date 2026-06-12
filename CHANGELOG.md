# Changelog — SolidPrivacy Scrub

## WP38 — DOCX hygiene audit report

Status: completed helper/tests/documentation-only.

Purpose:

- Add a report-only DOCX hygiene audit helper on top of the WP37 hidden-content extraction helper.
- Convert hidden-content extraction into structured severity, counts, findings and recommended-action text.
- Preserve current DOCX reinsert behavior, export semantics and UI behavior.

Files added:

- `docx_hygiene_audit.py`
- `DOCX_HYGIENE_AUDIT_REPORT.md`
- `tests/test_docx_hygiene_audit.py`
- `workpackage_claims/WP38_docx_hygiene_audit_report.md`
- `handover/workpackages/20260612_1840_docx_hygiene_audit_report.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Added `build_docx_hygiene_audit_report(content: bytes) -> dict`.
- Added `render_docx_hygiene_audit_markdown(report: dict) -> str`.
- Reports `low`, `medium` or `high` severity for DOCX hygiene risk.
- Marks headers, footers, comments/person metadata and tracked-change markers as high-risk findings.
- Reports invalid DOCX inspection as medium unknown-risk finding.
- Keeps explicit boundaries: `report_only: true`, `extraction_only: true`, `cleaning_applied: false`, `export_blocking: false`, `export_semantics_changed: false` and `safe_to_claim_clean: false`.
- Added synthetic tests for high-risk findings, no-supported-findings-not-clean guarantee, invalid DOCX, Markdown rendering and synthetic-only boundaries.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Added tests should be validated by GitHub Actions.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

- No DOCX cleaner implemented.
- No comments/tracked-changes removal implemented.
- No export blocking.
- No export semantics changed.
- No DOCX reinsert behavior changed.
- No Streamlit UI changed.
- No Scrub Key schema changed.
- No dependency change.
- No real data added.
- No cloud processing added.
- No roadmap change because strategy and phase order did not change.

Next recommended step:

- `WP39 — Clean DOCX export policy`.

## WP51 — ICP and pricing hypothesis

Status: completed business/design/documentation-only.

Purpose:

- Define the first ICP and pricing hypothesis after WP50.
- Compare Scrub Legal and Scrub Zorg as early validation tracks.
- Keep the work hypothesis-only without sales activity or product-behavior changes.

Files added:

- `ICP_AND_PRICING_HYPOTHESIS.md`
- `workpackage_claims/WP51_icp_and_pricing_hypothesis.md`
- `handover/workpackages/20260612_1815_icp_and_pricing_hypothesis.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP51_icp_and_pricing_hypothesis.md`

Main changes:

- Defined first ICP hypothesis for Scrub Legal and Scrub Zorg.
- Compared likely users, buyers, approvers/blockers, workflows, willingness-to-pay drivers and sales risks.
- Compared pricing models: demo/discovery, paid pilot, consultancy-assisted pilot, per-user subscription, per-organization subscription, local desktop license and enterprise/support model.
- Recommended a consultancy-assisted paid pilot as the most sensible first paid offer, while keeping final prices as hypotheses only.
- Defined what may not yet be sold or claimed, including production certification, full automation, full anonymization without review, complete DOCX hidden-content handling, OCR/restored PDF output and guaranteed detection.
- Added validation questions and go/no-go criteria for interviews and controlled pilot work.

Validation status:

- Documentation/business-design only.
- No tests run because no code, tests, UI, runtime behavior, dependency or product behavior changed.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

- No sales campaign started.
- No customer outreach started.
- No real data added.
- No UI changed.
- No code changed.
- No runtime behavior changed.
- No cloud document processing added.
- No production, compliance or safety guarantee added.

Next recommended step:

- `WP52 — Pilot intake and NDA process`.

## WP37 — Headers/footers/comments/tracked-changes extraction helper

Status: completed helper/tests/documentation-only.

Purpose:

- Add a pure local DOCX extraction helper for headers, footers, comments/kantlijncommentaren and tracked-change signals.
- Make high-risk hidden DOCX content audit-visible before any cleaner, removal or export-blocking policy is implemented.
- Preserve current DOCX reinsert behavior and export semantics.

Files added:

- `docx_hidden_content_extractor.py`
- `DOCX_HIDDEN_CONTENT_EXTRACTION_HELPER.md`
- `tests/test_docx_hidden_content_extractor.py`
- `workpackage_claims/WP37_headers_footers_comments_tracked_changes_extraction_helper.md`
- `handover/workpackages/20260612_1735_headers_footers_comments_tracked_changes_extraction_helper.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Added `inspect_docx_hidden_content(content: bytes) -> dict`, a side-effect-free helper that inspects DOCX bytes in memory.
- Detects and extracts text from `word/header*.xml`, `word/footer*.xml`, `word/comments.xml`, `word/commentsExtended.xml` and `word/person.xml` where parseable.
- Detects tracked-change markers such as `w:ins`, `w:del`, `w:delText`, `w:moveFrom` and `w:moveTo` across `word/*.xml` parts.
- Returns audit-oriented fields including `docx_parts_seen`, `headers`, `footers`, `comments`, `tracked_changes`, `detected`, `warnings`, `extraction_only`, `cleaning_applied: false` and `export_blocking: false`.
- Added synthetic tests for extraction, absence reporting, invalid input and synthetic-only boundaries.
- Added helper documentation that explicitly records extraction-only non-goals.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Added tests should be validated by GitHub Actions.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

- No DOCX cleaner implemented.
- No comments/tracked-changes removal implemented.
- No export blocking.
- No export semantics changed.
- No DOCX reinsert behavior changed.
- No Streamlit UI changed.
- No Scrub Key schema changed.
- No dependency change.
- No real data added.
- No cloud processing added.
- No roadmap change because strategy and phase order did not change.

Next recommended step:

- `WP38 — DOCX hygiene audit report`.

## WP50 — Pilot design Legal vs Zorg

Status: completed planning-only with artifact limitation.

Files added:

- `workpackage_claims/WP50_pilot_design_legal_vs_zorg.md`
- `handover/workpackages/20260612_1715_pilot_design_legal_vs_zorg.md`

Files changed:

- `workpackage_claims/WP50_pilot_design_legal_vs_zorg.md`
- `CHANGELOG.md`

Main changes:

- Created and completed the WP50 claim.
- Recorded the WP50 design summary in the claim file because repeated attempts to create the intended standalone design file were blocked by platform safety checks.
- Covered Legal vs Zorg validation direction, target groups, selection criteria, measurement themes, stop criteria, agreement boundaries, residual-risk reporting role and demo/pilot/production distinction at summary level.

Validation status:

- Documentation-only.
- No tests were run.
- App verification: not applicable.

Intentionally not changed:

- No pilot started.
- No code changed.
- No UI changed.
- No runtime behavior changed.

Next recommended step:

- `WP51 — ICP and pricing hypothesis`.

## Earlier entries

Previous changelog detail remains available in Git history. This WP38 entry records the latest DOCX hygiene audit report while preserving recent WP51, WP37 and WP50 entries below.
