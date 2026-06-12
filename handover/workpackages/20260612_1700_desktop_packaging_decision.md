# Handover — WP49 Desktop packaging decision

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP49 — Desktop packaging decision`

Status: completed decision/documentation-only.

Files added:

- `DESKTOP_PACKAGING_DECISION.md`
- `workpackage_claims/WP49_desktop_packaging_decision.md`
- `handover/workpackages/20260612_1700_desktop_packaging_decision.md`

Files changed:

- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP49_desktop_packaging_decision.md`

Summary:

- Decided that first MVP local distribution remains a portable Python folder with the local Streamlit launcher.
- PyInstaller one-folder may be the next proof only if explicitly approved.
- Tauri remains the preferred later professional shell candidate.
- Electron remains a later alternative.
- MSI remains future managed-deployment work only after packaging, signing, update, rollback, offline, network, temp-file and support boundaries are validated.

Tests/checks run:

- No tests run; documentation/decision-only.

Validation status:

- Required start files read.
- Claim checked and created before work.
- Local runtime documents, risk register and decision log reviewed.
- `ROADMAP.md` not changed because strategy/phase order did not change.
- No installer, MSI, PyInstaller, Tauri, Electron, Docker/Hugging Face startup, Streamlit UI, runtime behavior, telemetry, cloud processing, dependency or real-data change.

GitHub Actions status: unknown at handover time.

Hugging Face sync status: unknown at handover time; no app/runtime change made.

App verification status: not applicable; no UI changed.

Remaining risks:

- No production installer exists.
- No full offline demonstration exists.
- No runtime packet/network inspection exists.
- No code signing/update/rollback policy implemented.
- MSI remains gated future work.

Next recommended step:

`WP48B — Portable Python folder hardening proof` or `WP49B — PyInstaller one-folder packaging proof`, only if the coordinator approves a concrete packaging proof.
