# Assurance handover — SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT

Date/time: 2026-09-05 01:25 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Role: `governance_release_assurance`  
Issue: #115  
PR: #116

## Exact reviewed identity

- Frozen candidate head: `cbaaa1e4560670116c41ca788786d80d670dcf34`
- Expected base: `255cd619d5cf6eab32f9383940eaa4af362cb68c`
- Fresh merge-base: `255cd619d5cf6eab32f9383940eaa4af362cb68c`
- Pre-merge `main`: `255cd619d5cf6eab32f9383940eaa4af362cb68c`
- Synthetic merge candidate inspected: `c98a7075a72c9514b7c7c4f1bf242358cacbbaf1`
- Synthetic merge parents: exact base `255cd619d5cf6eab32f9383940eaa4af362cb68c` + exact candidate `cbaaa1e4560670116c41ca788786d80d670dcf34`

The fresh PR readback before verdict was open, draft, unmerged and mergeable. Compare showed the candidate directly ahead of the exact expected base/merge-base with no behind commits. The PR contained 13 commits; no one-commit constraint exists for this workpackage.

## Exact changed-file scope

Exactly 11 files changed:

1. `CHANGELOG.md`
2. `Dockerfile`
3. `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`
4. `RISK_REGISTER.md`
5. `WORKPACKAGES.md`
6. `handover/workpackages/20260905_0045_repository_convergence_startup_invocation_retirement.md`
7. `tests/test_export_download_ux_implementation.py`
8. `tests/test_pdf_text_reinsert_ui_patch.py`
9. `tests/test_scrub_key_warning_acknowledgement_ui.py`
10. `tests/test_static_highlight_preview_ui_integration_patch.py`
11. `workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT.md`

No `presidio_streamlit.py`, recognizer/profile, review/export/Scrub-Key/reinsert runtime, replacement-memory, OpenAI/Azure implementation, dependency file or Hugging Face runtime configuration changed.

## Blind-first root-cause reconstruction

Canonical governance and current source were inspected before implementation claims or handover narrative.

Current direct source already contains the two markers that make the historical compatibility scripts stop before their legacy mutation paths:

- `presidio_streamlit.py` contains `premium_streamlit_shell_ui`;
- `presidio_streamlit.py` imports `render_reinsert_mode` from `reinsert_mode_ui`.

`fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py` both read `presidio_streamlit.py`, detect their respective current-source marker, write the same content back, and then exit successfully before historical mutation logic. Therefore they are semantic startup no-ops on this source state, although the early-exit path still performs a same-content filesystem write.

The accepted-main Dockerfile nevertheless invoked both scripts before every Streamlit start. Removing those invocations removes obsolete runtime mutation authority without changing current app semantics.

## Docker/runtime result

Candidate Docker launches Streamlit directly:

```text
streamlit run presidio_streamlit.py --server.port=7860 --server.address=0.0.0.0 --server.enableXsrfProtection=false --server.enableCORS=false
```

The prior server flags are unchanged. Neither historical compatibility script is invoked by Docker startup. Both script files remain present for a separate evidence-based retirement decision.

## Test-contract review

The four changed tests were inspected individually. Their product/privacy contracts remain intact; only obsolete Docker-order/compatibility-invocation assertions were rebound to the direct-source/no-runtime-mutation invariant.

Still-binding invariants preserved include review/export behavior, Scrub Key warning/acknowledgement and fail-closed mismatch handling, PDF reinsert warnings and boundaries, static-highlight rollback safety, file names/MIME/data contracts, local-processing boundaries and the current shared-surface sequencing rule.

The second implementation test cycle correctly caught loss of the governance invariant:

```text
Shared Streamlit/review/export/runtime surfaces remain sequential
```

The catching tests were not weakened. The literal invariant was restored to current `WORKPACKAGES.md`, and the unchanged Premium plan/decision tests continue to assert it.

## Failure/repair history cross-check

Machine/administrative evidence preserves both relevant pre-final red cycles:

- initial: `3 failed, 1261 passed`; failures were obsolete Docker-order requirements;
- second: `2 failed, 1262 passed`; failures detected the accidentally dropped shared-surface sequencing rule.

Root `CHANGELOG.md` narrates the first cycle but not the full second cycle. This was assessed as a non-material documentation observation, not a release defect, because it does not falsely claim an exhaustive clean history; the exact second cycle is preserved in the workpackage claim and implementation handover, while the governing sequencing invariant is restored and machine-tested.

## Exact-head pre-merge Actions evidence

Exact frozen head `cbaaa1e4560670116c41ca788786d80d670dcf34`:

- workflow: `Tests`
- run: `33926913276`
- job: `101197324584`
- conclusion: `SUCCESS`
- raw command: `python -m pytest -q tests`
- raw result: `1264 passed in 17.18s`
- synthetic merge candidate: `c98a7075a72c9514b7c7c4f1bf242358cacbbaf1`
- synthetic parents: exact base + exact candidate.

## Formal assurance verdict

`PASS`

No material correctness, privacy, product, runtime, governance, sequencing, CI, or scope defect was found on the exact frozen pair.

A formal `governance_release_assurance` PASS was registered on PR #116 and bound explicitly to the exact reviewed head/base pair. Any candidate/base movement would have invalidated that PASS.

## Authorized merge administration

After PASS only:

- PR #116 was marked ready for review without candidate-head movement;
- merge was executed with `expected_head_sha=cbaaa1e4560670116c41ca788786d80d670dcf34`;
- merge succeeded.

Actual merge/main SHA:

`7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`

Actual merge parents:

1. `255cd619d5cf6eab32f9383940eaa4af362cb68c`
2. `cbaaa1e4560670116c41ca788786d80d670dcf34`

Fresh post-merge `main` readback equals exact merge SHA `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`.

## Exact-main Tests

On exact merged `main` `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`:

- workflow: `Tests`
- run: `33929193443`
- job: `101204143720`
- event: `push`
- conclusion: `SUCCESS`
- raw command: `python -m pytest -q tests`
- raw result: `1264 passed in 15.15s`.

## GitHub → Hugging Face sync / deployment evidence

On the same exact merged main SHA:

- workflow: `Sync to Hugging Face Space`
- run: `33929193466`
- job: `101204143901`
- event: `push`
- conclusion: `SUCCESS`
- checkout/readback before push: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`
- target remote: `huggingface.co/spaces/solidprivacy/scrub`
- remote push acknowledgement: `255cd61..7e4f549  HEAD -> main`.

Separate target-health verification observed the public `solidprivacy/scrub` Hugging Face Space in `Running` state and its `solidprivacy-scrub.hf.space` endpoint serving the Streamlit application shell.

This establishes that the exact merged tree containing the Dockerfile startup cleanup reached the intended HF `main` and that the Space is serving after the sync. It does not claim a content-hash readback of the remote Dockerfile beyond the exact Git push acknowledgement.

## App verification

Status: `N/A — no user-visible product/UI semantics changed by this package`.

Reason: no app/runtime product source was modified; the only runtime change removes two compatibility invocations proven to be semantic no-ops on current direct source. Deployment health was nevertheless smoke-verified separately via HF Running state and the live Streamlit endpoint.

## Issue closeout

Issue #115 was closed as `completed` only after:

- exact-pair assurance PASS;
- exact-head guarded merge;
- exact-main Tests SUCCESS;
- exact-main HF sync SUCCESS;
- target-space health verification.

## Residual risks / deliberate non-scope

1. `fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py` remain dormant historical mutation implementations. They are separate convergence/RETIRE candidates and must not be mass-deleted without fresh evidence.
2. Historical patch-oriented tests remain numerous; only assertions directly contradicting this proven startup cleanup were rebound.
3. R12 is reduced because live Docker invocation is gone, but dormant source can still be mistaken for current authority or reintroduced.
4. Private persistence/egress risks — replacement memory, Azure/OpenAI processing and content-bearing prompt logging — remain deliberately untouched and belong to later Private work unless a current safety defect forces reprioritization.
5. Existing Streamlit XSRF/CORS flags were deliberately preserved; hardening them is separate service/security scope rather than an incidental cleanup side effect.

## Next step

Return authority to `implementation_operations` for selection of the next bounded, evidence-derived Repository Convergence package from current canonical state. This assurance role does not create or execute that next implementation package.
