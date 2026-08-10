# SCRUB-WP_DUTCH_ADDRESS_SPAN_PRECISION_REPAIR

Role: `implementation_operations`
Issue: #107
Candidate PR: #111

## Claim

Repair the deployed Dutch address overcapture without disabling address recognition or weakening fail-closed privacy behavior.

## Implementation

- retain the existing recall-oriented `NL_ADDRESS` recognizer;
- add a downstream precision resolver that acts only on already-recognized `NL_ADDRESS` results;
- narrow a broad result only when a stricter street + house-number subspan is provable inside it;
- preserve the original broad result unchanged when no strict internal address can be established;
- prevent a spaced short Dutch word after a house number from being consumed as a generic house-number suffix;
- preserve explicit prefix-street addresses, postcode/city forms and ordinary suffix streets;
- leave non-address entities unchanged.

## Synthetic regression

Dedicated tests reproduce every live #107 `Polderweg 8` adjacent-context example and cover legitimate address forms, fail-safe unknown shapes and non-address preservation.

## Evidence

Initial integrated PR run before administration finalization:
- source head: `3b0bcd04caa06d0c64b2350bb4869cb6dec153ba`;
- tested PR merge candidate: `51b8db10018dd2819feb39bbb02ea5808538d5ad`;
- Tests run: `31356019220`;
- job: `93355748290`;
- command: `python -m pytest -q tests`;
- result: `1253 passed in 14.19s`;
- conclusion: `success`.

This administration commit intentionally moves the PR head. Final release-candidate identity and exact-head CI must therefore be recorded after this claim/handover is committed.

## Exclusions

No UI redesign, profile/threshold policy, export payload/name/MIME, Scrub Key, reinsert, audit, cloud-processing boundary or unrelated recognizer semantics are intentionally changed.

## Governance

Implementation does not self-certify or self-merge. Because `NL_ADDRESS` result semantics change, the final frozen exact head requires full CI and a completely fresh independent `governance_release_assurance` decision before merge/deploy.
