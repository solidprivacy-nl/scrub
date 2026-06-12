# Handover — Local installer deferred to final phase

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `ROADMAP — Defer local installer to final phase`

Status: completed roadmap/strategy documentation-only.

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

Tests/checks run:

- No tests run; documentation/strategy-only.

Validation status:

- No code, tests, UI, runtime behavior, installer, MSI, PyInstaller, Tauri, Electron, Docker/Hugging Face startup, telemetry, cloud processing or real data changed.
- Roadmap now says online/web validation comes before installer investment.
- Installer/packaging is no longer default active work.

GitHub Actions status: unknown.

Hugging Face sync status: unknown; no app/runtime change made.

App verification status: not applicable.

Remaining risks:

- Final local installer still does not exist.
- Future installer work still needs offline, network, temp-file, signing, update, rollback and support validation.
- `CHANGELOG.md` was compacted because a fuller update was blocked by connector safety checks; detailed prior history remains in Git history.

Next recommended step:

Continue online/web validation and trust hardening first. Keep WP28C verification, DOCX hygiene policy and pilot workflow ahead of installer work.
