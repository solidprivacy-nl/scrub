# Handover — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_REVERIFY

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_REVERIFY — fresh blind assurance for repaired PR #85`  
Role: `governance_release_assurance`  
Status: `GOVERNANCE_FAIL`  
Initial assurance decision: `FAIL`  
Issue: `#92`  
Candidate PR: `#85`  
Candidate head: `6ccda2ec58be387de768661c64d0a2d12b8b406e`  
Base main: `2831da154e6c299b3616d62a37f151ebfa9c45f1`  
Tested PR merge candidate: `5cecf611b4a85a427753d6d5550446264671d5af`  
Decision recorded: 2026-08-08 18:02 Europe/Amsterdam

## Summary

Fresh independent release assurance returned `FAIL` for exact repaired PR #85 head `6ccda2ec58be387de768661c64d0a2d12b8b406e`.

The prior hard-coded Standard Zorg → Expert Juridisch profile reset is repaired. The exact candidate now persists/hydrates profile, operator, threshold, entity selection, allow/deny lists and analyzer/model configuration, and those values participate in deterministic processing generation.

However, the broader binding Standard↔Expert presentation-only state contract is still violated in the integrated Streamlit control flow.

## Blocking findings

### 1. Current Standard source is not deterministically hydrated into Expert

Standard caches the active source in `_premium_cached_text` when the Add stage is left. The exact source then defines:

```python
show_add_workspace = is_premium_expert or stage_is_active(premium_state, Stage.ADD)
```

so Expert always renders the Add workspace. But its input initialization uses `_premium_cached_text` only for Standard; the Expert branch initializes from the demo text:

```python
input_text = (
    st.session_state.get("_premium_cached_text", "".join(demo_text))
    if is_premium_standard
    else "".join(demo_text)
)
```

The Standard non-Add path explicitly uses `_premium_cached_text`. Therefore a presentation-only transition from completed Standard Review/Download into Expert has no deterministic hydration path from the authoritative current source. The resulting `st_text` feeds `processing_generation(...)`; a source reinitialization changes generation and causes `synchronize_processing_generation(...)` to invalidate processed/review/export lineage despite the user changing only presentation mode.

This violates the issue #92 preservation contract and the approved Premium rule that Standard↔Expert is presentation-only unless the user explicitly changes a processing-affecting setting.

### 2. Expert bypasses current-generation analysis reuse

The exact source only consults `get_cached_analysis_results(...)` under:

```python
if is_premium_standard and not stage_is_active(premium_state, Stage.ADD):
```

Expert therefore enters the analyzer path even when the same deterministic generation already has current cached analysis. Presentation switching can silently rerun recognition rather than reusing the current-generation result.

This conflicts with the App Shell no-silent-reprocessing/current-generation-cache requirement.

### 3. Authoritative completed Standard review rows are not explicitly restored into Expert

`_premium_cached_review_rows` is merged/restored only on Standard-specific paths. Expert rebuilds `replacement_editor_df` from analysis/default rows and does not explicitly hydrate the completed Standard review working set.

As a result, after Standard review completion a switch to Expert can present/reconstruct a different review/export working set while `CoreFlowState` can still report the reviewed/export generation as current. Include/exclude decisions, manual rows and edited replacement values are therefore not deterministically preserved across the presentation transition.

This violates the requirement to preserve current replacement decisions, authoritative review state and export lineage across presentation-only switching.

## Test coverage assessment

The repaired candidate adds useful pure state and source-contract tests, including Standard Zorg → Expert → Standard helper-level preservation and processing-generation sensitivity.

However, the new integration assertions are source-string/AST contracts. They do not execute the actual Streamlit sequence:

```text
Standard Add
→ process
→ Standard Review edits
→ Controle afronden
→ Standard Download
→ Expert
→ Standard
```

and therefore do not exercise source-widget hydration, current-generation analysis reuse or authoritative review-row restoration across that transition.

## Exact raw machine evidence

Independent raw GitHub Actions evidence inspected:

```text
workflow: Tests
run: #2236 / 31263232074
job: 93117154194
candidate head: 6ccda2ec58be387de768661c64d0a2d12b8b406e
checked-out PR merge ref: 5cecf611b4a85a427753d6d5550446264671d5af
merge parents: 2831da154e6c299b3616d62a37f151ebfa9c45f1 + 6ccda2ec58be387de768661c64d0a2d12b8b406e
command: python -m pytest -q tests
result: 1235 passed in 12.45s
conclusion: success
```

The full suite is valid and green but does not cover the blocking integrated presentation transition.

## Post-verdict implementation disclosure review

Only after recording the initial `FAIL`, the implementation claim and handovers were opened.

They disclose the intended repair and correctly require fresh assurance, but they also claim that presentation switching preserves downstream lineage and that current-generation analysis/review state is preserved. Those claims conflict with the exact integrated source paths above. This disclosure review does not alter the independently reached initial decision.

## Files added/changed by this assurance worker

Candidate PR #85: **none**.

Separate assurance administration branch `assurance/issue92-premium-app-shell-reverify-fail`:

- added `handover/workpackages/20260808_1802_premium_app_shell_implementation_reverify.md`;
- added `workpackage_claims/scrub_wp_premium_app_shell_implementation_reverify.md`.

No runtime, test, recognizer, review, export, Scrub Key, reinsert, audit, dependency or deployment file was modified by assurance.

## Tests

- Candidate raw GitHub Actions: `1235 passed in 12.45s`, run #2236 / job `93117154194`.
- No candidate code was changed or locally repaired by assurance.
- Assurance administration must receive its normal repository Actions validation before being merged as documentation-only evidence.

## Validation status

- Initial assurance: `FAIL`.
- Candidate identity immediately before decision: exact PR ref remained `6ccda2ec58be387de768661c64d0a2d12b8b406e`.
- Candidate merge: `NOT EXECUTED`.
- Post-merge validation for PR #85: `NOT APPLICABLE — FAIL / no merge`.

## GitHub Actions status

Candidate: `GREEN BUT INSUFFICIENT FOR PASS` because the exact source violates the presentation-state contract and the failing paths are not covered by executable integration tests.

Assurance administration: pending its own documentation-only PR validation at handover creation time.

## Hugging Face sync status

`NOT EXECUTED — FAIL / PR #85 not merged`.

No runtime candidate was authorized for synchronization.

## App verification status

`NOT EXECUTED — FAIL / PR #85 not merged`.

Live app verification remains required only after a future repaired candidate independently passes, merges, synchronizes and has runtime health evidence.

## Blind-review transparency

Before the initial verdict, one commit-metadata connector call unexpectedly included text from `workpackage_claims/scrub_wp_premium_app_shell_implementation.md`, a path prohibited by issue #92 before decision. That content was explicitly excluded from the evidence basis. The initial `FAIL` was derived from permitted exact source/test files, authoritative contracts/profile definitions and raw Actions evidence. After the verdict, the claim and handovers were opened normally for administrative comparison.

## Remaining risks

- Source/widget state across Standard↔Expert is not yet represented by an executable integration test.
- Expert currently does not deterministically hydrate the authoritative Standard source/review working set.
- Expert can rerun recognition despite a current-generation Standard cache.
- Until repaired, a presentation switch can cause processing/review/export state to diverge from the lineage recorded by the pure core-flow state model.
- The later `SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION` remains blocked.

## Next recommended step

Return PR #85 to `implementation_operations` and produce a new release candidate that:

1. makes the authoritative source cache presentation-independent;
2. reuses current-generation analysis in both Standard and Expert when processing inputs are unchanged;
3. makes the authoritative review-row cache presentation-independent and restores it before Expert review/export rendering;
4. adds executable integration regression for Standard Zorg process/review/download → Expert → Standard, including source, generation, analysis cache, include/exclude/manual/replacement rows and export-lineage assertions;
5. preserves existing fail-closed invalidation when the user explicitly changes profile/operator/threshold/entities/allow/deny/analyzer settings;
6. preserves the Expert-only operator guard;
7. runs the full suite on the new exact head;
8. requests a completely fresh blind assurance review.
