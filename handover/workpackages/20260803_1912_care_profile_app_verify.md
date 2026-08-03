# Handover — SCRUB-WP_CARE_PROFILE_APP_VERIFY

Repository: `solidprivacy-nl/scrub`  
Workpackage title: Zorgfilter v1 deployed app verification  
Status: completed, merged and app-verified after technical deployment verification

## Summary

Opened the verification-only package after the Zorgfilter UI integration and cross-profile matrix were merged. An independent GitHub Actions workflow compared twelve relevant files between GitHub `main` at merge commit `cca4a25aaff28a7ba647c961d8e50f0e076921e2` and Hugging Face Space `solidprivacy/scrub`, verified the correctly scoped Zorgfilter markers and checked the live Streamlit health endpoint.

The technical deployment is verified. No product code was changed. The coordinator/user confirmed `alles groen` at 2026-08-03 20:35 Europe/Amsterdam, completing the functional closeout. Verification-only PR #55 was merged to `main` as `bd89398ace9d12934ff0516999d5716a9dd72b88`.

## Files added

- `CARE_PROFILE_APP_VERIFICATION.md`
- `output/validation/care_profile_hf_sync_verification.json`
- `tests/test_care_profile_hf_sync_verification.py`
- `workpackage_claims/scrub_wp_care_profile_app_verify.md`
- `handover/workpackages/20260803_1912_care_profile_app_verify.md`

## Files changed

- `ROADMAP.md` — current-web Zorgfilter line marked completed and app-verified
- `WORKPACKAGES.md` — package and downstream gates closed
- `CHANGELOG.md` — final CI and user verification recorded
- `RISK_REGISTER.md` — R10 mitigation evidence updated without closing production risk
- `CARE_PROFILE_APP_VERIFICATION.md` — visible verification result recorded
- `output/validation/care_profile_hf_sync_verification.json` — functional verification fields completed
- `tests/test_care_profile_hf_sync_verification.py` — closeout evidence assertions updated
- `workpackage_claims/scrub_wp_care_profile_app_verify.md` — claim marked completed

## Tests

- Report schema and referenced GitHub/Hugging Face targets.
- Twelve exact byte matches and equal SHA-256 values.
- Correctly scoped Zorgfilter marker checks.
- Space health endpoint `HTTP 200 / ok`.
- Space root `HTTP 200`.
- Technical sync and deployment flags.
- Functional app verification and all nine documented visible checks are true.
- Human-review and non-production-readiness boundaries remain true.
- No token, credential or real personal data in the evidence report.
- Full repository regression suite.

## Validation status

Initial verification report:
- all ten initially selected files were already exact byte matches;
- Space health was green;
- two marker groups were assigned to the wrong source modules, producing a false negative.

Corrected and completed verification report:

```text
Files checked:                 12
Exact byte matches:          12/12
Correctly scoped markers:      all
Space health:            200 / ok
Space root:                    200
Sync verified:                true
Technical deployment:        true
Functional app verification: true / confirmed_all_green
Production ready:             false
Human review required:        true
```

## GitHub Actions status

- PR #53 UI integration final clean run #1885: 986 tests passed.
- PR #54 cross-profile matrix final clean run #1906: 995 tests passed.
- Independent corrected Hugging Face verification passed its exact-file, marker and health assertions and wrote the committed evidence report.
- PR #55 verification-only run #1908: 998 tests passed in 10.07s.
- PR #55 pre-closeout run #1909: 998 tests passed in 10.45s.
- PR #55 confirmed-evidence closeout run #1917: 998 tests passed in 9.87s.
- PR #55 final clean run #1918: 998 tests passed in 10.02s.
- PR #55 post-recording run #1919: 998 tests passed in 10.05s.

## Hugging Face sync status

Verified independently for the underlying runtime integration:

- GitHub `main` commit: `cca4a25aaff28a7ba647c961d8e50f0e076921e2`;
- Hugging Face Space: `solidprivacy/scrub`;
- twelve relevant source files are byte-for-byte equal;
- all correctly scoped Zorgfilter markers are present;
- the live Space health endpoint is healthy.

PR #55 changed verification evidence, tests and governance only; it introduced no new runtime or UI behavior requiring renewed functional app verification.

## App verification status

Confirmed. The coordinator/user reported `alles groen` at 2026-08-03 20:35 Europe/Amsterdam; all documented visible checks passed.

## Remaining risks

- Generic NER remains model-dependent; bounded synthetic and app evidence does not establish full production recall or precision.
- Historical legal benchmark observations remain recorded separately.
- Rare-case clinical re-identification and over-masking risk are not eliminated by this closeout.
- Synthetic and technical deployment evidence does not establish production readiness.
- Human review remains mandatory.

## Next recommended step

Continue with the active risk-driven Phase 6 queue defined in `WORKPACKAGES.md`. Do not automatically open desktop UX or installer work; those remain separately gated by Phase 9 and explicit coordinator approval.