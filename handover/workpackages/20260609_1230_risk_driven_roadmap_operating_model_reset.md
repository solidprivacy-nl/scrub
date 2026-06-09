# Handover — WP18R Risk-driven roadmap and operating model reset

Repository: solidprivacy-nl/scrub  
Status: completed documentation/governance-only update

## Summary

Implemented the accepted strategic review recommendations by shifting the roadmap from feature-led sequencing to risk-driven sequencing. Added explicit governance for risk tracking, decision logging, release notes and workflow status monitoring. No product code, tests, UI or dependencies were changed.

## Files added

- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `STATUS_MONITORING_RUNBOOK.md`
- `RELEASE_NOTES.md`
- `handover/workpackages/20260609_1230_risk_driven_roadmap_operating_model_reset.md`

## Files changed

- `PROJECT_PROMPT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- Tests not required; documentation/governance-only update.

## Validation

- GitHub Actions: not required unless documentation checks run automatically.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.

## Notes / risks

- WP18 remains implemented but not closed; GitHub Actions were red in coordinator evidence, so WP18-FIX remains the active required workpackage.
- New risk-driven roadmap prioritizes trust/recall, Scrub Key security, placeholder robustness, hidden document hygiene, document-centric review, local runtime and pilot validation before batch/CLI/scale features.
- `STATUS_MONITORING_RUNBOOK.md` defines how workers should check GitHub Actions and Hugging Face sync themselves where connector permissions allow.

## Next recommended step

- Continue with `WP18-FIX — Fix failing PDF text to TXT UI tests`.
- After WP18-FIX is green, perform WP18 app verification.
- Then run `WP18B — PDF text to restored TXT UI app verification closeout` as closeout-only.
- After WP18 closeout, safe parallel tracks are WP19, WP25, WP30, WP35, WP45, WP50, WP56 and WP57.
