# Recall benchmark corpus

This directory contains synthetic benchmark corpus material for future recall/precision measurement.

The corpus is intentionally synthetic and controlled. It is not a product accuracy claim and not a production benchmark threshold.

Rules:

- Use synthetic data only.
- Store each plain-text source beside a `.gold.json` sidecar.
- Gold labels point to sensitive value spans, not labels such as `zaaknummer` or `dossiernummer`.
- Preserve legal/care context terms through `preserve_terms`.
- Record traps such as legal articles, money amounts, dates, generic role words, page/attachment labels and ambiguous care-location references in `known_traps`.
- Offsets are zero-based and exclusive at `end`.
- Every label must satisfy `source_text[start:end] == text`.
- Every preserve term must satisfy `source_text[start:end] == term`.

Current corpus files:

```text
corpus/legal/legal_reference_seed_001.txt
corpus/legal/legal_reference_seed_001.gold.json
corpus/legal/legal_role_preservation_seed_001.txt
corpus/legal/legal_role_preservation_seed_001.gold.json
corpus/legal/legal_false_positive_traps_seed_001.txt
corpus/legal/legal_false_positive_traps_seed_001.gold.json
corpus/legal/legal_mixed_identifiers_seed_001.txt
corpus/legal/legal_mixed_identifiers_seed_001.gold.json
corpus/care/care_reference_seed_001.txt
corpus/care/care_reference_seed_001.gold.json
corpus/care/care_role_preservation_seed_001.txt
corpus/care/care_role_preservation_seed_001.gold.json
corpus/care/care_mixed_identifiers_seed_001.txt
corpus/care/care_mixed_identifiers_seed_001.gold.json
```

Current coverage:

- Legal reference samples.
- Legal role preservation samples.
- Legal false-positive traps for legal articles, pages, attachments, productions, dates, times and money amounts.
- Legal mixed identifiers including case, role/court reference, dossier, client, claim, invoice, IBAN, BSN, ECLI, person, phone, email and address values.
- Care reference samples.
- Care role preservation samples, including care-role/name combinations.
- Care mixed identifiers including room, department, incident, client, care dossier, medication, device, BIG-like, person, phone and email values.

This corpus enables a later runner to compare analyzer/helper output against gold labels. No runner is implemented by the corpus seed or expansion packages.

Do not use this corpus as a product claim. Quantitative recall/precision still requires a benchmark runner, matching rules and accepted thresholds.
