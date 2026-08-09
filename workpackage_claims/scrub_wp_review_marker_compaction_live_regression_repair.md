# Workpackage Claim — SCRUB-WP_REVIEW_MARKER_COMPACTION_LIVE_REGRESSION_REPAIR

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Issue: #106  
PR: #108  
Status: `IMPLEMENTATION_IN_PROGRESS` pending final exact-head CI and fresh independent assurance

## Claimed implementation scope

- preserve exact raw processed-text whitespace while computing highlight coordinates;
- prevent marker offsets from drifting when document extraction starts with newlines/spaces;
- keep strict full bound-placeholder tokens intact across marker segmentation so existing compact visual aliases remain available;
- preserve scalar review-cell trimming separately from document-text coordinate handling;
- add synthetic regression coverage for marker-on and marker-off compact display.

## Explicit exclusions

No intended change to recognizers, profile rules, threshold semantics, Dutch address recognition, review include/replacement authority, authoritative bound placeholder tokens, export bytes/names/MIME, Scrub Key schema/binding, reinsert, audit, dependencies, local/cloud processing or mandatory human review.

## Functional evidence before administration

Tests #2279 / run `31337824222`, job `93306469803`; exact PR merge candidate `5b9af3a09519128d40b842b50fe1421b289ea2bd`; Streamlit `1.61.1`; `python -m pytest -q tests` → `1247 passed in 12.80s`.

This claim is administrative evidence only. A final exact-head full-suite run after administration and a fresh blind `governance_release_assurance` verdict are mandatory before merge.
