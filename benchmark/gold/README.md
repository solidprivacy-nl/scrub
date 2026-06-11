# Benchmark gold labels — README

Status: WP21 schema foundation completed.
Scope: gold-label sidecar schema and documentation only; no benchmark runner, CI scorecard, production gate or recognizer logic exists yet.

## Synthetic-only rule

All benchmark source documents under `benchmark/corpus/` and all future gold-label sidecars must be synthetic.

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

## Schema artifact

The WP21 gold-label sidecar schema is:

```text
benchmark/gold/schema/gold_label_schema.json
```

The schema defines the future sidecar contract for synthetic benchmark documents. It is a schema/specification artifact only. It does not implement validation tooling, a recall/precision runner, a CI gate or recognizer changes.

Existing example sidecars under `benchmark/gold/examples/` are examples only. Files marked with:

```text
"completeness": "schema_example_only"
```

must not be treated as full benchmark gold labels.

## Sidecar shape

Future complete gold-label sidecars should be one JSON file per synthetic source document.

Required top-level concepts include:

- `schema_version`;
- `document_id`;
- `domain`;
- `language`;
- `source_file`;
- `source_text_encoding`;
- `synthetic`;
- `labels`;
- `preserve_terms`;
- `known_traps`;
- optional `normalization`;
- optional `runner_expectations`.

The `source_file` field must point to a synthetic plain-text source under:

```text
benchmark/corpus/legal/
benchmark/corpus/zorg/
benchmark/corpus/mixed/
```

## Offset convention

Offsets are defined against the UTF-8-decoded source text.

Rules:

1. `start` is zero-based and inclusive.
2. `end` is zero-based and exclusive.
3. `text` must equal `source_text[start:end]`.
4. Labels must point to the sensitive value span, not the surrounding label, unless the label itself is uniquely identifying.
5. Repeated occurrences must have distinct `label_id` values. They may share the same `entity_id` when they represent the same synthetic value.

Future WP22 runner validation should fail malformed offsets and report text/span mismatches clearly.

## Canonical entity classes

Gold labels must use the canonical classes from `RECALL_BENCHMARK_SPEC.md` and the schema enum:

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

Implementation-specific recognizer labels can be mapped later by the WP22 runner through fields such as `acceptable_entity_mappings`. The gold schema remains canonical and product-neutral.

## Gold labels

Each sensitive value label should include:

- `label_id`;
- `entity_id`;
- `entity_class`;
- expected `text`;
- `start`;
- `end`;
- `sensitivity`;
- `required`;
- optional normalization, mapping and failure-class hints.

The `required` field means a later runner should count a miss as a false negative.

## Normalization guidance

The schema supports normalization guidance without implementing matching behavior.

Supported concepts include:

- exact matching;
- casefolding;
- whitespace collapse;
- stripping outer punctuation;
- ignoring separators for classes such as phone, IBAN and matter references;
- class-specific normalization profiles such as `phone_digits_normalized` and `iban_compact_uppercase`.

WP22 should report exact and value-normalized results separately. Normalized matching must not hide missed sensitive values.

## Preserve terms

`preserve_terms` are labels for legal or care context terms that should normally remain readable.

Examples:

```text
cliënt
minderjarige
verzoeker
verweerder
eiser
rechtbank
arts
zorgmedewerker
```

The schema uses `ROLE_OR_CONTEXT_TERM_TO_PRESERVE` and expected behavior values such as:

```text
must_remain_readable
may_be_sensitive_only_with_identifying_context
```

The future runner should report context-preservation failures separately from recall failures.

## Known traps

`known_traps` define false-positive traps that should not be counted as sensitive values or should not map to a specific entity class.

Examples:

- dates that must not be treated as BSN or phone;
- legal article references that must not be treated as case numbers;
- times that must not be treated as phone numbers;
- money amounts that must not be treated as references;
- generic role words that must not be treated as person names;
- labels such as `Dossiernummer` where only the value should be detected.

These traps prepare precision and context-preservation reporting for WP22.

## Partial overlap guidance

The schema includes `partial_overlap_policy` for future runner behavior.

Recommended default:

```text
diagnostic_only
```

Overlap can help diagnose near-misses, but exact and value-normalized matching should remain the main reporting tiers. Partial overlap must not be used to hide false negatives in safety reporting.

## WP22 runner expectations

The future WP22 runner should:

1. Load sidecars that conform to `gold_label_schema.json`.
2. Read `source_file` as UTF-8 text.
3. Validate offsets before scoring.
4. Assert `text == source_text[start:end]`.
5. Map recognizer outputs to canonical entity classes.
6. Report exact and value-normalized recall/precision separately.
7. Report preserve-term failures.
8. Report known-trap false positives.
9. Keep partial-overlap results diagnostic unless a later policy changes this.
10. Use synthetic data only.

## Current boundary

WP21 is complete as schema/closeout work.

Still not implemented:

- complete gold-label sidecars for the corpus;
- automated offset validation;
- benchmark runner;
- CI scorecard;
- production test gate;
- recognizer logic changes;
- UI changes;
- dependency changes.

## Next expected step

```text
WP22 — Recall/precision test runner
```
