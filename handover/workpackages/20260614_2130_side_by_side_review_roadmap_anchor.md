# Handover — WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR — Anchor unified side-by-side review UX direction and workpackage sequence`

Status: completed roadmap/specification/documentation-only.

## Summary

Anchored the new UX direction: one unified side-by-side main review surface instead of adding separate helper panels for every review feature.

Target direction:

```text
Source text left | Processed/checked text right
                 | Optional highlights integrated in the processed text
```

The direction also records that the separate highlight-only duplicate preview is not the desired long-term UX and that repeated per-highlight labels such as `Gemarkeerd` are not the long-term design.

## Files added

- `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md`
- `handover/workpackages/20260614_2130_side_by_side_review_roadmap_anchor.md`

## Files changed

- `DECISION_LOG.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR.md`

## Tests/checks run

No shell tests were run. This was roadmap/specification/documentation-only. No product code, UI code, tests or runtime behavior changed.

## Validation status

- New direction document added.
- D021 added to decision log.
- Roadmap updated.
- Workpackages structured.
- Risk register updated.
- Changelog updated.

## GitHub Actions status

Unknown. Connector combined-status lookup returned no visible statuses for the latest documentation commit.

## Hugging Face sync status

Unknown / not verified. Not required because no UI/runtime behavior changed.

## App verification status

Not applicable.

## Remaining risks

- Side-by-side UX is now anchored but not yet planned/tested in detail.
- Synchronized scrolling may require custom rendering and must be planned/tested separately.
- Existing UI still has separate review surfaces until a future approved implementation changes it.

## Next recommended step

```text
WP_SIDE_BY_SIDE_REVIEW_REDESIGN_PLAN
```

Parallel candidate if kept documentation/tests-only:

```text
WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS
```
