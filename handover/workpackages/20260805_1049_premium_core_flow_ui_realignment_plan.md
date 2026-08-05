# Handover — SCRUB-WP_PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: Realign the interface toward a premium single-task document workspace

Status: completed planning/design-only

## Summary

Reviewed the current roadmap, the implemented Basiscontrole/Expertcontrole split, the basic-mode declutter work and the latest live app evidence. Confirmed that earlier work reduced local density but did not solve the structural long-form Streamlit page. Defined a new target architecture around separate anonymize/reinsert workflows, a global Standard/Expert view, one active stage at a time, one primary action per stage and progressive disclosure of settings, Scrub Key, alternative formats and audit details.

## Files added

- `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`
- `tests/test_premium_core_flow_ui_realignment_plan.py`
- `workpackage_claims/scrub_wp_premium_core_flow_ui_realignment_plan.md`
- `handover/workpackages/20260805_1049_premium_core_flow_ui_realignment_plan.md`

## Files changed

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- the compact-placeholder implementation claim and handover, to record successful live app verification.

## Tests

Added source-level planning contract tests for:

- one-active-stage app-shell direction;
- Standard/Expert global visibility model;
- anonymize/reinsert top-level workflow separation;
- sidebar policy;
- recommended-download hierarchy;
- preservation of export, Scrub Key, reinsert, audit and human-review boundaries;
- roadmap, workpackage and decision-log alignment.

## Validation status

- The self-cleaning finalization workflow updated the definitive governance tree and removed its temporary workflow, script and trigger.
- Finalization workflow run #6: 1160 tests passed in 11.55s on commit `1132fce8fa0767c044caf5b4b81c7e1fc42c191c`.
- Standard PR merge-candidate run #2093: 1160 tests passed in 11.90s on commit `9994804feeb7219b1d75d9abbc0551d8d76e3655`.
- This final evidence-only handover commit receives one last standard regression before merge.
- Hugging Face sync is not functionally relevant because no runtime files change.
- App verification is not applicable because this package changes no UI.

## GitHub Actions status

Green through finalization run #6 and standard PR run #2093; final evidence-only regression pending.

## Hugging Face sync status

Not functionally applicable; no runtime product files changed.

## App verification status

Not applicable for planning-only work.

## Remaining risks

- Streamlit can materially improve information architecture but may not deliver every aspect of native desktop polish.
- An explicit `Document controleren` action changes visible execution state and requires a pure state-model contract before UI integration.
- A source-aware primary download must preserve exact existing payload, filename, MIME and eligibility semantics.
- Shared Streamlit input, review and export flows must remain sequential, not parallel.
- Expert parity must be proven so decluttering does not hide or lose safety controls.

## Next recommended step

Complete `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION` as the frozen safety baseline. Then start `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT`.
