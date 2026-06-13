# Changelog — SolidPrivacy Scrub

## WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX3 — Restore exact replacement UI plan sequencing phrase

Status: completed after Actions/HF verification; app verification not applicable.

Files added:

- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX3.md`
- `handover/workpackages/20260613_1718_review_highlight_toggle_plan_actions_fix3.md`

Files changed:

- `REPLACE_LOGIC_UI_PLAN.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX3.md`
- `handover/workpackages/20260613_1718_review_highlight_toggle_plan_actions_fix3.md`

Summary:

- Coordinator screenshot for `Tests #851` showed the exact missing plan sentence in `REPLACE_LOGIC_UI_PLAN.md`.
- Restored: `Only after that should a small UI implementation package be considered.`
- Coordinator screenshot evidence later confirmed `Tests #855` green and `Sync to Hugging Face Space #867` green for commit `c9b5201`.
- No product code, UI/runtime behavior, export/download behavior, Scrub Key behavior, reinsert behavior, dependency, cloud processing or real-data behavior changed.

Next recommended step:

- `WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS`.
- `WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION` remains blocked without separate coordinator approval.

## WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2 — Repair replacement-logic contract text failures

Status: completed narrow Actions repair; later superseded by green FIX3 closeout evidence.

Files added:

- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2.md`
- `handover/workpackages/20260613_1658_review_highlight_toggle_plan_actions_fix2.md`

Files changed:

- `replacement_decision_panel_ui.py`
- `REPLACE_LOGIC_UI_PLAN.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2.md`

Summary:

- Coordinator screenshot for `Tests #844` showed two exact contract failures in existing replacement-logic tests.
- Restored exact renderer phrase `does not write Scrub Key mappings` in the parked replacement decision renderer while keeping the panel out of the normal Scrub Legal flow.
- Restored exact `WP_REPLACE_LOGIC_UI_CONTRACT_TESTS` reference in `REPLACE_LOGIC_UI_PLAN.md`.
- Preserved `_safe_text` runtime behavior after the text patch.
- No Streamlit UI implementation, normal-flow rendering, replacement table mutation, automatic replacement, Scrub Key write, export/download change, export blocking, reinsert change, dependency change, cloud processing or real-data fixture was introduced.

## WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX — Repair stale workflow-status risk wording

Status: completed narrow documentation repair; later superseded by green FIX3 closeout evidence.

Files added:

- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX.md`
- `handover/workpackages/20260613_1634_review_highlight_toggle_plan_actions_fix.md`

Files changed:

- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX.md`

Summary:

- Coordinator screenshot showed red `Tests #838` on `WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN` claim close while sync was green.
- Connector could not fetch workflow logs for the push-triggered run.
- The likely stale contract issue was in `RISK_REGISTER.md` R8, which still claimed there was no formal monitoring runbook and no standard status states.
- `STATUS_MONITORING_RUNBOOK.md` exists and defines standard status states, so R8 was corrected to mark the risk as mitigating and to describe the remaining connector-run lookup limitation instead.
- No product code, UI, tests, export, Scrub Key, reinsert, dependency, cloud processing or real-data behavior changed.

## WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN — Simple masked-text highlight toggle planning

Status: completed planning/specification-only; no UI or product code changed.

Files added:

- `REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`
- `handover/workpackages/20260613_1605_review_highlight_toggle_plan.md`

Summary:

- Planned a simple optional review toggle: `Markeringen tonen` / `Markeringen tonen in voorbeeldtekst`.
- Goal is to show subtle visual markers for values already masked/replaced in the preview text.
- The planned toggle remains visual-only, read-only, non-authoritative and non-mutating.
- The review table remains the source of truth and fallback.
- Explicitly blocks the old WP42D static-highlight startup mutation route, startup patching of `presidio_streamlit.py`, click-to-mark, advanced editor behavior, full-document marking, raw unsafe HTML, Scrub Key writes, export/download changes and reinsert changes.

## WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK

Status: completed product rollback/hide.

Summary:

- Product feedback rejected the technically working replacement helper panel as not intuitive enough for the normal user flow.
- The panel is no longer rendered from the normal Scrub Legal flow.
- Helper and contract assets remain available for later redesign.
- No replacement behavior, export behavior, Scrub Key behavior or reinsert behavior changed.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_REPLACE_LOGIC_UI_IMPLEMENTATION — staged/read-only replacement decision companion panel, technically implemented but product-rejected.
- WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — strengthened replacement decision UI contract tests before implementation.
- WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — readiness check before replacement decision UI implementation.
- WP39D — DOCX hygiene audit UI implementation.
- WP39C — DOCX hygiene audit UI contract tests.
- WP39B — DOCX hygiene audit UI planning.
