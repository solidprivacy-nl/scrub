# Changelog — SolidPrivacy Scrub

## WP51B — Park pilot line and restore MVP product quality gate

Status: completed roadmap/governance documentation-only.

Purpose:

- Park Phase 7 follow-up until the MVP product flow is credible enough.
- Keep WP50 and WP51 as recorded early thinking artifacts, not the active execution line.
- Restore the active queue to MVP product-quality work.

Files added:

- `MVP_PRODUCT_QUALITY_GATE.md`
- `workpackage_claims/WP51B_park_pilot_line_mvp_quality_gate.md`
- `handover/workpackages/20260612_1835_park_pilot_line_mvp_quality_gate.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP51B_park_pilot_line_mvp_quality_gate.md`

Main changes:

- Added the MVP product quality gate.
- Recorded the active product priority as `Import -> Scrub -> Review -> Replace -> Scrub Key -> Reinsert -> Export -> Audit`.
- Parked WP52 as a default next step.
- Updated the active queue to focus on WP28C evidence/app verification, WP41, easy replace/review logic specification and optional WP39B.
- Preserved concurrent worker updates showing WP38, WP39 and WP40 as completed.

Validation status:

- Documentation/governance-only.
- No tests run.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

- No code changed.
- No UI changed.
- No tests changed.
- No runtime behavior changed.
- No import, scrub, review, replace, Scrub Key, reinsert, export or audit behavior changed.
- No cloud processing added.
- No real data added.

Notes:

- Attempts to update `DECISION_LOG.md` were blocked by platform safety checks. The decision is recorded in `MVP_PRODUCT_QUALITY_GATE.md`, `WORKPACKAGES.md`, `CHANGELOG.md` and the handover.

Next recommended step:

- `WP41 — Highlight-based review prototype decision` or `WP_REPLACE_LOGIC — Easy replace/review logic simplification specification`.

## WP40 — Document-centric review UX specification

Status: completed specification/documentation-only.

Purpose:

- Define the future document-centric review UX direction.
- Move review thinking from table-only toward document-first review with table audit/control.
- Support online/web validation and trust hardening before installer work.

Files added:

- `DOCUMENT_CENTRIC_REVIEW_UX_SPEC.md`
- `workpackage_claims/WP40_document_centric_review_ux_specification.md`
- `handover/workpackages/20260612_1930_document_centric_review_ux_specification.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP40_document_centric_review_ux_specification.md`

Main changes:

- Defined a future document-first review model with document pane, detail pane and table audit/control pane.
- Defined review states such as `needs_review`, `accepted`, `ignored`, `edited`, `manual_added`, `preserve_context` and `high_risk_unresolved`.
- Defined future actions: accept, ignore, edit replacement, mark as context term, add missed sensitive value and apply to all same values.
- Kept current review table as a future audit/control surface rather than the only review surface.
- Updated R6 from open to mitigating because a document-centric specification now exists.

Validation status:

- Documentation/specification-only.
- No tests run.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

- No Streamlit UI changed.
- No review table implementation changed.
- No export/download behavior changed.
- No Scrub Key behavior changed.
- No helper logic changed.
- No dependency change.
- No cloud processing added.
- No real data added.

Next recommended step:

- `WP41 — Highlight-based review prototype decision`.

## WP39 — Clean DOCX export policy

Status: completed policy/tests/documentation-only.

Purpose:

- Define when Scrub may warn, report, block or eventually claim a DOCX export is clean.
- Record that current DOCX output must not be described as clean DOCX export.
- Preserve current export behavior while setting boundaries for future clean-export claims.

Next recommended step:

- `WP40 — Document-centric review UX specification`.
- Alternative DOCX-specific follow-up: `WP39B — DOCX hygiene audit UI planning`.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- ROADMAP — Local installer deferred to final phase.
- WP38 — DOCX hygiene audit report.
- WP51 — ICP and pricing hypothesis.
- WP37 — Headers/footers/comments/tracked-changes extraction helper.
- WP50 — Pilot design Legal vs Zorg.
- WP49 — Desktop packaging decision.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
