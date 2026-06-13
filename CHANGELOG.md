# Changelog — SolidPrivacy Scrub

## WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX2 — Repair replacement-logic contract text failures

Status: completed narrow Actions repair; awaiting GitHub Actions and Hugging Face sync evidence.

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

Validation status:

- Repair is based on the exact failure lines shown in coordinator screenshot for `Tests #844`.
- Expected verification: GitHub Actions green and Hugging Face sync green for the final fix commit.
- App verification is not applicable because the normal app UI/runtime behavior was not intentionally changed.

## WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN_ACTIONS_FIX — Repair stale workflow-status risk wording

Status: completed narrow documentation repair; awaiting GitHub Actions and Hugging Face sync evidence.

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

Validation status:

- Documentation/status repair only.
- Expected verification: GitHub Actions green and Hugging Face sync green for the final fix commit.
- App verification is not applicable because no Streamlit UI/runtime behavior changed.

## WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN — Simple masked-text highlight toggle planning

Status: completed planning/specification-only; no UI or product code changed.

Files added:

- `REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`
- `handover/workpackages/20260613_1605_review_highlight_toggle_plan.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REVIEW_HIGHLIGHT_TOGGLE_PLAN.md`

Summary:

- Planned a simple optional review toggle: `Markeringen tonen` / `Markeringen tonen in voorbeeldtekst`.
- Goal is to show subtle visual markers for values already masked/replaced in the preview text.
- The planned toggle remains visual-only, read-only, non-authoritative and non-mutating.
- The review table remains the source of truth and fallback.
- Explicitly blocks the old WP42D static-highlight startup mutation route, startup patching of `presidio_streamlit.py`, click-to-mark, advanced editor behavior, full-document marking, raw unsafe HTML, Scrub Key writes, export/download changes and reinsert changes.
- Next recommended package: `WP_REVIEW_HIGHLIGHT_TOGGLE_CONTRACT_TESTS`.

Validation status:

- Documentation/planning-only.
- No tests were added or run.
- App verification is not applicable because no Streamlit UI/runtime behavior changed.

## WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK

Status: completed product rollback/hide.

Files added:

- `workpackage_claims/WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK.md`
- `handover/workpackages/20260613_1525_replace_logic_ui_product_rollback.md`

Files changed:

- `serial_review_panel_ui.py`
- `tests/test_replace_logic_ui_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `workpackage_claims/WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK.md`

Summary:

- Product feedback rejected the technically working replacement helper panel as not intuitive enough for the normal user flow.
- The panel is no longer rendered from the normal Scrub Legal flow.
- Helper and contract assets remain available for later redesign.
- No replacement behavior, export behavior, Scrub Key behavior or reinsert behavior changed.

Validation status:

- No shell or pytest execution was available through the ChatGPT GitHub connector.
- UI/runtime changed, so Actions, Hugging Face sync and app verification are still required.

Next recommended step:

- Verify Actions and sync, then request app verification.
- Later: `WP_REPLACE_LOGIC_UI_REDESIGN_PLAN`, only after separate coordinator approval.

## Recent previous entries

Detailed recent history remains available in Git history and includes:

- WP_REPLACE_LOGIC_UI_IMPLEMENTATION — staged/read-only replacement decision companion panel, technically implemented but product-rejected.
- WP_REPLACE_LOGIC_UI_CONTRACT_GAP_FIX — strengthened replacement decision UI contract tests before implementation.
- WP_REPLACE_LOGIC_UI_IMPLEMENTATION_READINESS — readiness check before replacement decision UI implementation.
- WP39D — DOCX hygiene audit UI implementation.
- WP39C — DOCX hygiene audit UI contract tests.
- WP39B — DOCX hygiene audit UI planning.
