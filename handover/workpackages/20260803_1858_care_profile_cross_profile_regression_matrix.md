# Handover — SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX

Repository: `solidprivacy-nl/scrub`  
Workpackage title: Zorgfilter v1 cross-profile regression matrix  
Status: completed and regression-green; governance closeout and merge pending

## Summary

Built a pure deterministic cross-profile matrix for Care, Legal, General Dutch and International profiles. It runs the repository's Dutch custom recognizers across eight synthetic care-document families and twelve existing synthetic legal examples. The matrix confirms that the Zorgfilter integration preserves profile isolation, Care/International and Legal/International parity, all dedicated Care expectations and protected clinical text.

## Files added

- `care_profile_cross_profile_matrix.py`
- `CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX.md`
- `tests/test_care_profile_cross_profile_matrix.py`
- `output/validation/care_profile_cross_profile_matrix.json`
- `workpackage_claims/scrub_wp_care_profile_cross_profile_regression_matrix.md`
- `handover/workpackages/20260803_1858_care_profile_cross_profile_regression_matrix.md`

## Files changed

- `ROADMAP.md` — pending governance finalizer
- `WORKPACKAGES.md` — pending governance finalizer
- `CHANGELOG.md` — pending governance finalizer
- `RISK_REGISTER.md` — pending governance finalizer

## Tests

- Four-profile entity composition and isolation.
- Dedicated Care entities only in Care and International.
- Dedicated Legal entities only in Legal and International.
- Shared Dutch identity entities available in all four profiles.
- All 108 dedicated Care expectations found across Care and International.
- Care/International dedicated-type parity for every care document.
- Legal/International dedicated-type parity for every legal example.
- Care replace versus review-selected policy alignment.
- Zero overlap with protected clinical phrases.
- International all-supported scope remains explicit.
- Full observation set from historical legal metadata reproduced in the committed JSON snapshot.
- Helper-purity guard: no Streamlit, cloud or network dependency.

## Validation status

- Run #1887: 992 passed, 2 failed; exposed that historical legal metadata was being treated incorrectly as a pure hard contract.
- Run #1888: diagnostic failure list confirmed 16 legacy metadata gaps and 4 negative observations, with no Zorg or clinical-preservation failure.
- Run #1890: corrected methodology passed with 994 tests.
- Run #1897: 993 passed, 2 failed because the evidence snapshot contained the wrong legal-example count (`10` instead of `12`).
- Run #1899: **995 tests passed in 9.56s** after correcting the snapshot count.
- Final clean run after governance finalization: pending.

## Matrix result

```text
Care document families:                 8
Legal examples:                        12
Dedicated Care expectations:      108/108
Hard profile failures:                  0
Protected clinical overlaps:            0
Historical legal metadata:        132/148
Recorded historical gaps:              16
Recorded negative observations:         4
```

## GitHub Actions status

- PR #54 is open.
- Latest validated run: #1899, green, 995 tests.

## Hugging Face sync status

Not applicable to this pure helper/test package itself. The preceding user-visible UI integration was merged in PR #53, but its GitHub-to-Hugging-Face sync has not yet been independently verified through the available connector.

## App verification status

Pending. App verification must not start until deployment sync is confirmed. Generic NER behavior is intentionally deferred to deployed-app observation.

## Remaining risks

- Generic NER is model-dependent and not covered by this deterministic matrix.
- Historical legal metadata still contains 16 deterministic gaps and 4 negative observations; these are recorded rather than hidden.
- The deployed Care selector, examples and review statuses still require live verification.
- Synthetic evidence does not establish production recall or precision.
- Human review remains mandatory.

## Next recommended step

Finalize governance, run one clean full regression and merge PR #54. Then start `SCRUB-WP_CARE_PROFILE_APP_VERIFY` only after GitHub-to-Hugging-Face sync for the merged UI integration can be confirmed.
