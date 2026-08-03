# Handover — SCRUB-WP_CARE_PROFILE_APP_VERIFY

Repository: `solidprivacy-nl/scrub`  
Workpackage title: Zorgfilter v1 deployed app verification  
Status: technical deployment verified; coordinator/user app verification pending

## Summary

Opened the verification-only package after the Zorgfilter UI integration and cross-profile matrix were merged. An independent GitHub Actions workflow compared twelve relevant files between GitHub `main` at merge commit `cca4a25aaff28a7ba647c961d8e50f0e076921e2` and Hugging Face Space `solidprivacy/scrub`, verified the correctly scoped Zorgfilter markers and checked the live Streamlit health endpoint.

The technical deployment is verified. No product code was changed. Functional closeout remains blocked on coordinator/user verification of the visible app behavior.

## Files added

- `CARE_PROFILE_APP_VERIFICATION.md`
- `output/validation/care_profile_hf_sync_verification.json`
- `tests/test_care_profile_hf_sync_verification.py`
- `workpackage_claims/scrub_wp_care_profile_app_verify.md`
- `handover/workpackages/20260803_1912_care_profile_app_verify.md`

## Files changed

- `ROADMAP.md` — pending verification-status finalizer
- `WORKPACKAGES.md` — pending verification-status finalizer
- `CHANGELOG.md` — pending verification-status finalizer
- `RISK_REGISTER.md` — pending verification-status finalizer

## Tests

- Report schema and referenced GitHub/Hugging Face targets.
- Twelve exact byte matches and equal SHA-256 values.
- Correctly scoped Zorgfilter marker checks.
- Space health endpoint `HTTP 200 / ok`.
- Space root `HTTP 200`.
- Technical sync and deployment flags.
- Functional app verification intentionally remains false.
- No token, credential or real personal data in the evidence report.
- Full repository regression suite.

## Validation status

Initial verification report:
- all ten initially selected files were already exact byte matches;
- Space health was green;
- two marker groups were assigned to the wrong source modules, producing a false negative.

Corrected verification report:

```text
Files checked:                 12
Exact byte matches:          12/12
Correctly scoped markers:      all
Space health:            200 / ok
Space root:                    200
Sync verified:                true
Technical deployment:        true
Functional app verification: false / pending user
```

## GitHub Actions status

- PR #53 UI integration final clean run #1885: 986 tests passed.
- PR #54 cross-profile matrix final clean run #1906: 995 tests passed.
- Independent corrected Hugging Face verification passed its exact-file, marker and health assertions and wrote the committed evidence report.
- Verification-branch normal regression run: pending after PR creation.

## Hugging Face sync status

Verified independently:

- GitHub `main` commit: `cca4a25aaff28a7ba647c961d8e50f0e076921e2`;
- Hugging Face Space: `solidprivacy/scrub`;
- twelve relevant source files are byte-for-byte equal;
- all correctly scoped Zorgfilter markers are present;
- the live Space health endpoint is healthy.

## App verification status

Pending coordinator/user confirmation. Required visible checks are documented in `CARE_PROFILE_APP_VERIFICATION.md`.

## Remaining risks

- Generic NER is model-dependent and still requires observation in the running app.
- Visible profile selection, example count and review-status rendering require human verification.
- Historical legal benchmark observations remain recorded separately.
- Synthetic and technical deployment evidence does not establish production readiness.
- Human review remains mandatory.

## Next recommended step

Coordinator/user opens the deployed Space and follows `CARE_PROFILE_APP_VERIFICATION.md`. After confirmation, update the evidence status, complete governance closeout and merge the verification-only PR.