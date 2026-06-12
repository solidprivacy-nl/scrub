# Changelog — SolidPrivacy Scrub

## WP39 — Clean DOCX export policy

Status: completed policy/tests/documentation-only.

Purpose:

- Define when Scrub may warn, report, block or eventually claim a DOCX export is clean.
- Record that current DOCX output must not be described as clean DOCX export.
- Preserve current export behavior while setting boundaries for future clean-export claims.

Files added:

- `CLEAN_DOCX_EXPORT_POLICY.md`
- `tests/test_clean_docx_export_policy.py`
- `workpackage_claims/WP39_clean_docx_export_policy.md`
- `handover/workpackages/20260612_1915_clean_docx_export_policy.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Main changes:

- Defined allowed current labels: DOCX output with limitations, restored DOCX output with hygiene warnings and DOCX hygiene audit.
- Forbid current claims such as clean DOCX, safe DOCX, fully cleaned DOCX, metadata-free DOCX, comments removed and tracked changes removed.
- Defined warning/report policy for no-supported-findings, headers/footers, comments/kantlijncommentaren, tracked changes and invalid/uninspectable DOCX.
- Defined future export-blocking candidates without implementing blocking.
- Defined minimum requirements before any future clean-DOCX claim.
- Added policy tests that lock the no-clean-claim, no-export-semantic-change, no-blocking and no-real-data boundaries.

Validation status:

- The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.
- Added policy tests should be validated by GitHub Actions.
- App verification: not applicable because no UI behavior changed.

Intentionally not changed:

- No DOCX cleaner implemented.
- No comments/tracked-changes removal implemented.
- No export blocking implemented.
- No export semantics changed.
- No DOCX reinsert behavior changed.
- No Streamlit UI changed.
- No Scrub Key schema changed.
- No dependency change.
- No real data added.
- No cloud processing added.
- No roadmap change because strategy and phase order did not change.

Next recommended step:

- `WP40 — Document-centric review UX specification`.
- Alternative DOCX-specific follow-up: `WP39B — DOCX hygiene audit UI planning`.

## ROADMAP — Local installer deferred to final phase

Status: completed roadmap/strategy documentation-only.

Purpose:

- Defer local installer/MSI/desktop packaging work to the final roadmap phase.
- Make online/web validation of logic, interface, security and trustworthiness the default route before installer investment.
- Prevent packaging proofs from appearing as default next work.

Files added:

- `workpackage_claims/ROADMAP_local_installer_deferral.md`
- `handover/workpackages/20260612_1900_local_installer_deferral.md`

Files changed:

- `ROADMAP.md`
- `DECISION_LOG.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `DESKTOP_PACKAGING_DECISION.md`
- `CHANGELOG.md`
- `workpackage_claims/ROADMAP_local_installer_deferral.md`

Validation status:

- Documentation/strategy-only.
- No tests run.
- App verification not applicable.
- No code, UI, runtime behavior, dependency, installer, MSI, PyInstaller, Tauri, Electron, telemetry, cloud processing or real data changed.

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
