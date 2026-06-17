# Recall benchmark corpus

This directory contains synthetic benchmark corpus material for future recall/precision measurement.

The seed corpus is intentionally small. It is not a product accuracy claim and not a production benchmark threshold.

Rules:

- Use synthetic data only.
- Store each plain-text source beside a `.gold.json` sidecar.
- Gold labels point to sensitive value spans, not labels such as `zaaknummer` or `dossiernummer`.
- Preserve legal/care context terms through `preserve_terms`.
- Record traps such as legal articles, money amounts and generic role words in `known_traps`.
- Offsets are zero-based and exclusive at `end`.
- Every label must satisfy `source_text[start:end] == text`.
- Every preserve term must satisfy `source_text[start:end] == term`.

Current seed files:

```text
corpus/legal/legal_reference_seed_001.txt
corpus/legal/legal_reference_seed_001.gold.json
corpus/legal/legal_role_preservation_seed_001.txt
corpus/legal/legal_role_preservation_seed_001.gold.json
corpus/care/care_reference_seed_001.txt
corpus/care/care_reference_seed_001.gold.json
```

This corpus enables a later runner to compare analyzer/helper output against gold labels. No runner is implemented by this seed package.
