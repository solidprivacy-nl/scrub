# Benchmark gold labels — README

Status: WP20 corpus-first placeholder documentation.  
Scope: explanation only; no gold-label schema, runner, CI gate or production benchmark exists yet.

## Synthetic-only rule

All benchmark source documents under `benchmark/corpus/` must be synthetic.

Do not add:

- real case files;
- real client data;
- real care records;
- real names from actual cases;
- real BSNs;
- real IBANs;
- real customer examples;
- copied confidential documents.

If a fixture looks realistic, it must clearly say that it is synthetic.

## Future gold-label direction

A later workpackage, expected as `WP21 — Gold-label entity schema`, should define the final schema.

The future gold labels should follow the direction in `RECALL_BENCHMARK_SPEC.md`:

- one sidecar file per synthetic source document;
- zero-based character offsets;
- `start` as inclusive offset;
- `end` as exclusive offset;
- `text` must equal `source_text[start:end]`;
- labels must map to canonical benchmark entity classes;
- labels should point to the sensitive value span, not the surrounding label, unless the label itself is identifying.

## Canonical entity classes

Gold labels should use the canonical classes from `RECALL_BENCHMARK_SPEC.md`, including:

```text
PERSON
ADDRESS
EMAIL
PHONE
BSN
IBAN
DATE
NL_POSTCODE
CASE_NUMBER
DOSSIER_NUMBER
CLIENT_NUMBER
CLAIM_NUMBER
INCIDENT_NUMBER
ECLI
ORGANIZATION
MEDICAL_OR_CARE_REFERENCE
ROLE_OR_CONTEXT_TERM_TO_PRESERVE
```

Implementation-specific recognizer labels can be mapped later by the benchmark runner. WP20 does not define that mapping.

## WP20 boundary

WP20 is corpus-first and runner-free.

It creates messy synthetic Dutch legal, zorg and mixed professional text fixtures only. It does not add:

- full gold-label sidecars;
- offset validation;
- benchmark runner;
- CI scorecard;
- production test gate;
- recognizer logic changes;
- UI changes;
- dependency changes.

## Next expected step

`WP21 — Gold-label entity schema` should define the sidecar format and validation expectations before `WP22` implements a recall/precision runner.
