# Workpackage claim — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_REVERIFY

Repository: `solidprivacy-nl/scrub`  
Role: `governance_release_assurance`  
Status: `GOVERNANCE_FAIL`  
Assurance decision: `FAIL`  
Issue: `#92`  
Candidate PR: `#85`  
Candidate head: `6ccda2ec58be387de768661c64d0a2d12b8b406e`  
Base main: `2831da154e6c299b3616d62a37f151ebfa9c45f1`  
Tested merge candidate: `5cecf611b4a85a427753d6d5550446264671d5af`  
Decision recorded: 2026-08-08 18:02 Europe/Amsterdam

## Blind-review boundary

The initial `FAIL` was recorded on issue #92 before intentionally opening implementation handovers, implementation claims or implementation completion conclusions.

Permitted evidence used for the decision:

- issue #92 requested outcome and acceptance criteria;
- `PROJECT_PROMPT.md`;
- `ROADMAP.md` for authoritative direction only;
- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`;
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`;
- `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`;
- `PREMIUM_STAGED_WORKSPACE_DECISION.md`;
- merged `premium_core_flow_state.py`;
- exact candidate `premium_app_shell.py`, `premium_streamlit_state.py`, `premium_streamlit_shell_ui.py`, `presidio_streamlit.py`, `fix_streamlit_nested_expanders.py` and relevant tests;
- exact recognition-profile definitions;
- raw GitHub Actions run/job/log evidence.

One pre-decision commit-metadata connector response unexpectedly exposed content from the prohibited implementation claim path. That content was excluded from the evidence basis and the exposure was disclosed before continuing blind review.

## Independent decision evidence

The prior profile-index blocker is repaired: Expert now hydrates persisted profile/operator/threshold/entity/list/analyzer settings, and deterministic processing generation contains the required processing-affecting values.

The repaired candidate nevertheless fails the broader presentation-state contract:

1. Expert always renders Add but initializes its input branch from demo text rather than the authoritative `_premium_cached_text` used by non-active Standard stages. A Standard Review/Download → Expert presentation-only switch therefore lacks deterministic source hydration and can change processing generation/invalidate downstream lineage without an explicit processing edit.
2. Expert does not consult the current-generation analysis cache and therefore can silently rerun recognition when only presentation changed.
3. Completed Standard `_premium_cached_review_rows` are not explicitly restored into Expert. Expert rebuilds review rows from analysis while pure `CoreFlowState` can still report reviewed/export lineage as current, so include/exclude/manual/replacement decisions and the export working set are not deterministically preserved.
4. The new tests validate pure helpers and source-string contracts but do not execute the actual Streamlit Standard Review/Download → Expert → Standard transition.

These are blocking violations of the issue #92 Standard↔Expert preservation criteria and the approved Premium state model. Missing or contradictory state preservation cannot be inferred as passing.

## Raw machine evidence

```text
workflow: Tests
run: #2236 / 31263232074
job: 93117154194
candidate head: 6ccda2ec58be387de768661c64d0a2d12b8b406e
PR merge candidate checked out: 5cecf611b4a85a427753d6d5550446264671d5af
merge parents: 2831da154e6c299b3616d62a37f151ebfa9c45f1 + 6ccda2ec58be387de768661c64d0a2d12b8b406e
command: python -m pytest -q tests
result: 1235 passed in 12.45s
conclusion: success
```

The raw suite is valid and green but does not exercise the blocking integrated presentation transition.

## Post-verdict administration

After the initial decision, the implementation claim and handovers were opened. They are administratively detailed and disclose that widget/session-state behavior still required independent source review, but their stronger claims that presentation switching preserves downstream lineage/current review state conflict with the exact integrated control flow found independently.

Findings were returned to implementation issue #84 and PR #85. No repair was performed by assurance.

## Action and validation

- PR #85 merge: `NOT EXECUTED`.
- Candidate source/test repair: `NONE BY ASSURANCE`.
- Exact-head candidate Actions: `GREEN BUT DOES NOT SUPPORT PASS`.
- GitHub→Hugging Face sync: `NOT EXECUTED` because the runtime candidate failed assurance.
- Runtime health/smoke: `NOT EXECUTED`.
- Live app verification: `NOT EXECUTED`.
- `SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION`: remains blocked.

## Required next step

Implementation must produce a new exact head that makes source, current-generation analysis and authoritative review rows presentation-independent, adds executable cross-mode integration coverage, runs full exact-head regression and receives a fresh blind `governance_release_assurance` decision.
