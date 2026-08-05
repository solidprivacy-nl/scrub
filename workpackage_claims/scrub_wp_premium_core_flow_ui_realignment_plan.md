# Workpackage claim — SCRUB-WP_PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN

Repository: `solidprivacy-nl/scrub`

Status: completed planning/design-only; implementation not started

Claimed at: 2026-08-05 10:49 Europe/Amsterdam

## Goal

Reassess the current interface after live user evidence and realign the roadmap from local decluttering toward a premium, app-like, single-task document workspace.

## Evidence

The coordinator/user confirmed that compact placeholder display is working, then reported that the interface still feels:

- too form-like;
- too website-like;
- too close to an MVP prototype;
- visually distracted by dropdowns, expanders, settings and download controls;
- insufficiently premium, client-grade and enterprise-grade.

The desired core flow is:

```text
Document uploaden of tekst plakken
→ verwerken
→ controleren
→ downloaden
```

## Scope

- Review existing roadmap, Basic/Expert work and current UI direction.
- Define the structural gap between local decluttering and a true app shell.
- Define a global Standard/Expert presentation model.
- Define one-active-stage flow for add, review and download.
- Define top-level separation of anonymize and reinsert workflows.
- Define progressive disclosure and source-aware export hierarchy.
- Update roadmap, workpackage sequence, decision log and risk framing.
- Record the successful compact-placeholder app verification.

## Boundaries

- Planning, governance and contract-test preparation only.
- No Streamlit or product-code changes.
- No export, Scrub Key, reinsert, recognizer, profile, runtime or dependency changes.
- Human review remains mandatory.
- Existing audit and expert controls remain available in the target architecture.
- Structural UI implementation remains sequential and test-first.

## Deliverable

`PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`

## Next recommended package

`SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION`, followed by `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT`.