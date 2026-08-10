# Handover — SCRUB-WP_DUTCH_ADDRESS_SPAN_PRECISION_REPAIR

Date: 2026-08-10
Role: `implementation_operations`
Issue: #107
PR: #111

## Live defect reproduced

The deployed app generated multiple near-duplicate `Adres` rows around the same privacy-sensitive address `Polderweg 8`, because the broad Dutch address recognizer could absorb ordinary words before the street token and could also treat a short separated Dutch word after the house number as a generic suffix.

## Repair design

The base `NL_ADDRESS` recognizer remains unchanged and recall-oriented. A separate fail-safe precision resolver is applied to analyzer output:

1. inspect only an already-recognized `NL_ADDRESS` result;
2. search inside its existing span for a stricter Dutch street + house-number expression;
3. if proven, shallow-copy the result and narrow only `start`/`end`;
4. if no strict subspan is proven, preserve the original broad result unchanged;
5. never delete an ambiguous address result merely to improve precision.

The strict grammar supports explicit street-prefix names such as `Laan van Meerdervoort 55, 2517 AM Den Haag`, ordinary suffix streets such as `Polderweg 8`, common Dutch street descriptors, attached house-number letter suffixes and numeric subdivisions. It does not treat arbitrary spaced 1–3 letter words after a house number as part of the address.

## Files

- `dutch_address_span_precision.py` — fail-safe resolver;
- `presidio_helpers.py` — resolver wired into the normal analyzer result path;
- `tests/test_dutch_address_span_precision.py` — synthetic reproduction and safety regressions;
- `workpackage_claims/scrub_wp_dutch_address_span_precision_repair.md`;
- this handover.

## Validation before final administration commit

Source head `3b0bcd04caa06d0c64b2350bb4869cb6dec153ba` was tested as PR merge candidate `51b8db10018dd2819feb39bbb02ea5808538d5ad` in Tests run `31356019220`, job `93355748290`:

`python -m pytest -q tests` → `1253 passed in 14.19s` → success.

Because claim/handover persistence changes the candidate head, this result is supporting implementation evidence only. Freeze and assurance must use the final post-administration head and its own exact PR CI.

## Safety / exclusions

No intentional change to UI architecture, review/include authority, profile/threshold policy, export bytes/names/MIME, Scrub Key schema or binding, reinsert, audit, local/cloud processing boundary, or non-address entity semantics. Human review remains mandatory.

## Required next gate

After this administration is persisted:
- identify final exact PR #111 head/base/merge candidate;
- require successful full exact-head CI;
- freeze the head;
- route to a completely fresh independent `governance_release_assurance` reviewer;
- do not merge before PASS;
- after pinned merge, verify exact-main Tests and GitHub→Hugging Face sync/runtime;
- only then request the consolidated live retest required by parent issues #105/#96.
