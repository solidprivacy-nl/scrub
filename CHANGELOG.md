# Changelog — SolidPrivacy Scrub

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

## ROADMAP — Local installer deferred to final phase

Status: completed roadmap/strategy documentation-only.

Purpose:

- Defer local installer/MSI/desktop packaging work to the final roadmap phase.
- Make online/web validation of logic, interface, security and trustworthiness the default route before installer investment.
- Prevent packaging proofs from appearing as default next work.

Next recommended step:

- Continue online/web validation and trust hardening first.
- Keep WP28C verification, DOCX hygiene policy and pilot workflow ahead of installer work.

## Recent previous entries

Recent detailed changelog history remains available in Git history and includes:

- WP38 — DOCX hygiene audit report.
- WP51 — ICP and pricing hypothesis.
- WP37 — Headers/footers/comments/tracked-changes extraction helper.
- WP50 — Pilot design Legal vs Zorg.
- WP49 — Desktop packaging decision.
- WP28C / WP28C-VERIFY — Scrub Key warning acknowledgement UI implementation and verification attempt.
