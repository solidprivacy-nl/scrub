# Workpackage claim — SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT

Status: implementation complete; pre-final regression green; final exact-head regression and independent assurance pending  
Role: `implementation_operations`  
Issue: #115  
PR: #116  
Branch: `wp/repository-convergence-startup-invocation-retirement`  
Starting main: `255cd619d5cf6eab32f9383940eaa4af362cb68c`  
Started: 2026-09-05 Europe/Amsterdam

## Objective

Remove the obsolete Docker pre-start invocation of the two legacy Streamlit source-patch scripts after source inspection proved that both scripts exit without mutating the current direct-source application.

## Root-cause evidence

Current `presidio_streamlit.py` directly imports:

- `premium_streamlit_shell_ui`, which causes `fix_streamlit_nested_expanders.py` to exit immediately;
- `render_reinsert_mode` from `reinsert_mode_ui`, which causes `fix_streamlit_pdf_text_reinsert.py` to exit immediately.

Accepted-main Docker nevertheless executed both historical mutation scripts before launching Streamlit.

## Implemented scope

- Docker `CMD` now launches `presidio_streamlit.py` directly through Streamlit;
- existing `--server.port=7860`, `--server.address=0.0.0.0`, XSRF and CORS flags are preserved unchanged;
- four Docker-coupled tests were rebound from obsolete patch-order requirements to current direct-source/no-runtime-mutation invariants;
- `WORKPACKAGES.md`, `CHANGELOG.md`, `RISK_REGISTER.md` and the temporary convergence debt ledger were aligned to current truth;
- the still-binding shared Streamlit/review/export/runtime sequencing invariant remains explicit in WORKPACKAGES.

The two historical patch scripts themselves remain present and are not retired by this package.

## Validation history

Initial implementation run:

```text
Tests run: 33926348414
job: 101195603271
result: 3 failed, 1261 passed in 14.42s
```

All three failures were legacy Docker-order assertions in export, Scrub Key warning and static-highlight rollback tests. Their product semantics were retained while the obsolete runtime-order requirement was removed.

Second run:

```text
Tests run: 33926636459
job: 101196486677
result: 2 failed, 1262 passed in 14.30s
```

Both failures correctly detected that a still-binding shared-surface sequencing rule had been dropped while condensing WORKPACKAGES. The tests were not weakened; the invariant was restored.

Pre-final green run:

```text
branch head: aa6c03a4a3123cec702da9728fa3636ef6cb813a
Tests run: 33926738278
job: 101196791909
merge candidate: e06ecb69a592fd3624e02ccae5fd58228df7627b
result: 1264 passed in 14.76s
conclusion: SUCCESS
```

Because this claim update and the mandatory handover occur after that run, a new final exact-head full regression is required before freezing the candidate.

## Explicit non-scope

No changes to:

- `presidio_streamlit.py` product/UI behavior;
- recognizers, profiles or thresholds;
- review/include/export semantics;
- Scrub Key or reinsert semantics;
- persistent replacement memory;
- Azure/OpenAI processing paths;
- dependencies;
- unrelated Docker hardening/security settings;
- historical patch-script deletion;
- mass retirement of historical `*_ui_patch.py` tests.

## Remaining gates

1. Write the mandatory implementation handover.
2. Run full exact-head `python -m pytest -q tests` after all branch-mutating administration.
3. Freeze that exact SHA and make no further branch mutations.
4. Obtain fresh blind `governance_release_assurance`: `PASS | FAIL | INDETERMINATE`.
5. Merge only on PASS.
6. Verify post-merge exact-main Tests and GitHub→Hugging Face sync.
7. App verification is N/A unless assurance identifies an actual user-visible behavior change; this package removes no-op startup commands only.
