# Handover — SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT

Date/time: 2026-09-05 00:45 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Issue: #115  
PR: #116  
Branch: `wp/repository-convergence-startup-invocation-retirement`  
Starting main/base: `255cd619d5cf6eab32f9383940eaa4af362cb68c`

## Workpackage title

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT
```

## Status

Implementation complete. Pre-final full regression is green. This handover is the final branch-mutating administrative artifact; one new full exact-head regression must run after this commit. The resulting head must then be frozen and independently reviewed by `governance_release_assurance` before merge.

## Business / engineering outcome

The current app already contains the Premium shell and direct reinsert UI in source, while Docker still executed two historical source-patch scripts before every Streamlit start. Both scripts exit immediately on current direct-source markers, so the live runtime dependency was obsolete.

The smallest complete fix removes only those runtime invocations and starts Streamlit directly. Historical patch scripts remain in the repository for a later evidence-based retirement decision; this package does not perform a broad cleanup.

## Root-cause evidence

Current `presidio_streamlit.py` contains/imports the markers that make both compatibility scripts exit without mutation:

- `premium_streamlit_shell_ui` → `fix_streamlit_nested_expanders.py` exits;
- `from reinsert_mode_ui import render_reinsert_mode` → `fix_streamlit_pdf_text_reinsert.py` exits.

Before this package Docker ran:

```text
python fix_streamlit_nested_expanders.py &&
python fix_streamlit_pdf_text_reinsert.py &&
streamlit run presidio_streamlit.py ...
```

Candidate Docker now runs Streamlit directly with the prior server flags unchanged.

## Files added

- `workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT.md`
- `handover/workpackages/20260905_0045_repository_convergence_startup_invocation_retirement.md`

## Files changed

- `Dockerfile`
- `tests/test_pdf_text_reinsert_ui_patch.py`
- `tests/test_export_download_ux_implementation.py`
- `tests/test_scrub_key_warning_acknowledgement_ui.py`
- `tests/test_static_highlight_preview_ui_integration_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`

No `presidio_streamlit.py`, recognizer, profile, review, export, Scrub Key, reinsert, persistence, external-AI or dependency file is changed.

## Test / validation history

### Initial implementation run

```text
Tests run: 33926348414
job: 101195603271
result: 3 failed, 1261 passed in 14.42s
```

The three failures were obsolete Docker-order assertions in:

- export-download implementation test;
- Scrub Key warning/acknowledgement test;
- static-highlight rollback test.

Their underlying product contracts were preserved. Only the requirement that the two no-op compatibility scripts remain in Docker startup was retired.

### Second run

```text
Tests run: 33926636459
job: 101196486677
result: 2 failed, 1262 passed in 14.30s
```

Both failures protected a still-binding governance invariant:

```text
Shared Streamlit/review/export/runtime surfaces remain sequential
```

The tests were not changed. The invariant was restored to `WORKPACKAGES.md`.

### Pre-final green run

```text
branch head: aa6c03a4a3123cec702da9728fa3636ef6cb813a
Tests run: 33926738278
job: 101196791909
merge candidate: e06ecb69a592fd3624e02ccae5fd58228df7627b
result: 1264 passed in 14.76s
conclusion: SUCCESS
```

This run predates the final claim/handover commits and therefore is not the final release evidence.

## Validation status

- root-cause source proof: COMPLETE;
- focused Docker/direct-source contracts: covered by full regression;
- full pre-final regression: GREEN;
- final exact-head regression after this handover: PENDING;
- independent exact-head assurance: PENDING;
- merge: PROHIBITED until independent PASS.

## GitHub Actions status

Pre-final `Tests` run `33926738278`: SUCCESS, `1264 passed in 14.76s`.

A new final exact-head `Tests` run is mandatory after this handover commit.

## Hugging Face sync status

Pre-merge: N/A / not authoritative for this candidate.  
Required after an independently authorized merge: verify exact-main GitHub→Hugging Face sync and record the actual run/head.

## App verification status

N/A for this implementation candidate. The package does not change UI/product semantics; it removes startup invocations that are proven no-ops on current direct source. If independent assurance finds evidence of a user-visible runtime difference, this status must be reconsidered.

## Privacy / safety validation

Unchanged by scope:

- human review remains mandatory;
- recognition/profile thresholds unchanged;
- Scrub Key and reinsert behavior unchanged;
- export bytes/names/MIME unchanged;
- document processing unchanged;
- persistent replacement memory unchanged;
- Azure/OpenAI paths unchanged;
- Streamlit server XSRF/CORS flags intentionally remain unchanged and are later Private Service hardening scope, not silently altered here.

## Remaining risks

1. `fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py` remain dormant historical mutation implementations. They are separate RETIRE candidates and should not be mass-deleted without evidence.
2. Historical patch-oriented tests remain numerous; only Docker-order assertions directly contradicted by this root-cause fix were rebound.
3. R12 is reduced by removing live runtime invocation, but dormant code can still be mistaken for current authority or accidentally reintroduced.
4. Private persistence/egress risks (replacement memory, Azure/OpenAI, content-bearing prompt logging) remain deliberately untouched and belong to later Stage 2 unless a current safety defect forces earlier action.
5. Validation-hierarchy ambiguity and stale GitHub issue state remain unresolved Stage 1 packages.

## Next recommended step

1. Read the new PR #116 head after this handover commit.
2. Run/verify the full exact-head `Tests` workflow and raw pytest result.
3. Freeze that exact SHA; make no further implementation/admin branch commits.
4. Dispatch a completely fresh blind-first `governance_release_assurance` review on that SHA against base `255cd619d5cf6eab32f9383940eaa4af362cb68c`.
5. On PASS only: merge the exact reviewed head, verify exact-main Tests and GitHub→HF sync, close #115, and then return to `implementation_operations` for the next evidence-derived convergence package.
