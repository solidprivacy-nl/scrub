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

- Documentation and contract-test implementation prepared.
- Full GitHub Actions regression pending the planning PR.
- Hugging Face sync not functionally relevant because no runtime files change.
- App verification not applicable because this package changes no UI.

## GitHub Actions status

Pending.

## Hugging Face sync status

Not functionally applicable.

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