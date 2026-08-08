# Handover — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION state-preservation repair

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — repair Standard/Expert processing-state preservation`  
Status: `RELEASE_CANDIDATE_READY` subject to final exact-head CI and fresh blind assurance.

## Files added/changed in this repair cycle

Added:
- `tests/test_premium_presentation_state_preservation.py`
- this repair handover.

Changed:
- `premium_streamlit_state.py`
- `presidio_streamlit.py`
- `tests/test_premium_streamlit_state.py`
- `tests/test_care_profile_current_ui_integration_snapshot.py`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_premium_app_shell_implementation.md`

Temporary repair executor/workflow self-deleted and are not intended to be part of the persistent candidate diff.

## Repair implemented

- Hydrate Expert profile from the shared persisted profile instead of hard-coded index 1.
- Hydrate operator, threshold, entity selection, allow/deny lists and analyzer/model settings across Standard/Expert.
- Rehydrate the Standard profile widget when returning from Expert.
- Synchronize deterministic processing generation in both presentation modes.
- Preserve downstream lineage when only presentation changes.
- Invalidate downstream lineage fail-closed when processing-affecting settings actually change.
- Preserve the existing block against silently coercing Expert-only operators in Standard.

## Tests

Pre-administration full regression:

```text
GitHub Actions Tests #2229 / run 31263099583
job 93116829430
python -m pytest -q tests
1235 passed in 14.48s
conclusion: success
```

Focused new contracts include Standard Zorg → Expert → Standard preservation, operator/threshold/entity generation sensitivity and source-level hydration/synchronization assertions.

## Validation status

Functional repair validation: green before final administration.  
Final exact-head validation: required after this handover/administration commit.

## GitHub Actions status

Pre-administration candidate: `success` as above.  
Final candidate: pending a fresh exact-head full-suite run.

## Hugging Face sync status

Not run pre-merge. Runtime source changed, so exact GitHub → Hugging Face synchronization must be verified after an independently authorized merge.

## App verification status

Pending. UI behavior changed; coordinator live-app verification is mandatory after merge and successful synchronization/runtime health confirmation.

## Remaining risks

- Streamlit widget/session-state behavior must still receive independent source review and later live app verification.
- A fresh assurance worker must independently verify that presentation switching cannot alter processing settings or stale lineage.
- No later Premium Input/Review/Export package may start until this App Shell gate is passed, merged and post-merge/app-verified.

## Next recommended step

1. Run the complete regression suite on the final exact PR head after administration.
2. Freeze that head and record raw run/job/merge-candidate evidence in PR #85 and issue #84 metadata.
3. Open a new blind assurance issue for a fresh `governance_release_assurance` worker; do not reuse prior issue #90.
4. Merge only after independent PASS, then verify exact-main Actions, GitHub→Hugging Face sync/runtime health and live app behavior.
