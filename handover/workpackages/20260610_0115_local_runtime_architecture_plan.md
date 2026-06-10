# Handover — WP45 Local runtime architecture plan

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP45 — Local runtime architecture plan`

Status: completed architecture/specification-only.

## Summary

WP45 created the local runtime architecture plan for SolidPrivacy Scrub. The plan compares local Streamlit launcher, PyInstaller, Tauri and Electron, defines local-first trust requirements, and recommends a phased path from the current Hugging Face demo/development environment toward a local-first professional runtime.

The recommendation is:

```text
MVP: minimal local Streamlit launcher → local file-handling/privacy validation → PyInstaller/portable Windows proof of concept
Later professional path: Tauri desktop shell with reusable Python core, with Electron as an alternative if frontend/team requirements favor it
```

## Files added

- `LOCAL_RUNTIME_ARCHITECTURE_PLAN.md`
- `handover/workpackages/20260610_0115_local_runtime_architecture_plan.md`

## Files changed

- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- No tests added.
- No tests changed.
- No tests run, because WP45 is architecture/specification-only and no code or test files were changed.

## Validation status

- Required start files read: `AGENTS.md`, `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Required supporting files read: `RISK_REGISTER.md`, `DECISION_LOG.md`, `STATUS_MONITORING_RUNBOOK.md`, `RELEASE_NOTES.md`, `PARALLEL_SPEC_CONSOLIDATION_WP58.md`.
- Context-only files inspected: `Dockerfile`, `requirements.txt`, `presidio_streamlit.py`.
- Architecture plan reviewed against WP58 boundaries: no packaging implementation, no runtime code, no UI, no Docker/runtime startup changes, no dependency changes and no cloud processing.

Note: the architecture plan file was created before all required context-only files were inspected. The remaining required reads and context inspection were completed before the decision, risk, workpackage, changelog and handover updates were made. The created file stayed within the allowed file set and no runtime/code behavior was changed.

## GitHub Actions status

- To be checked after this final handover commit.

## Hugging Face sync status

- To be checked after this final handover commit.

## App verification status

- Not applicable. No UI behavior changed.

## Remaining risks

- No local runtime implementation exists yet.
- No minimal local Streamlit launcher exists yet.
- No offline-mode demonstration exists yet.
- No network-traffic validation exists yet.
- No local file-handling/privacy test exists yet.
- No Windows packaging proof of concept exists yet.
- No final desktop packaging decision has been made.
- Hugging Face remains useful for demo/development, but should not be used as the trust environment for confidential real-world documents.

## Next recommended step

- `WP46 — Minimal local Streamlit launcher`.
