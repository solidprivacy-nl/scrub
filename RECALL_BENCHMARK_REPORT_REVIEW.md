# Diagnostic recall benchmark report review

Status: review-only

Artifact: `diagnostic-recall-benchmark-report`

Workflow: `Diagnostic recall benchmark report`

Source commit/run: `a3df5c7 — Diagnostic recall benchmark report #1` according to coordinator screenshot evidence.

Uploaded artifact files reviewed:

```text
recall_benchmark_report.json
recall_benchmark_summary.md
```

## 1. Scope and boundaries

This review is documentation-only. It reviews the first diagnostic recall benchmark artifact output.

No product code was changed.

Boundaries preserved:

- no product UI change;
- no recognizer change;
- no pattern fix;
- no export/download change;
- no Scrub Key change;
- no reinsert change;
- no threshold enforcement;
- no production gate;
- no product safety claim.

## 2. Artifact integrity

Artifact integrity passed.

Metadata:

```text
metadata.status = diagnostic_only
metadata.synthetic_corpus = true
metadata.production_gate = false
metadata.thresholds_enforced = false
```

Report structure:

```text
report.summary exists
report.documents exists
document_count = 7
gold_label_count = 75
JSON report present
Markdown summary present
```

The Markdown summary explicitly states:

```text
Status: diagnostic only
Generated from synthetic corpus
No production threshold
No product safety claim
```

## 3. Summary values

| document_count | gold_label_count | prediction_count | required_label_count | matched_required_exact_count | matched_required_text_normalized_count | matched_required_overlap_count | missed_required_count | wrong_type_count | false_positive_candidate_count | preserve_term_hit_count | known_trap_hit_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | 75 | 61 | 75 | 41 | 41 | 41 | 34 | 11 | 8 | 0 | 1 |

Diagnostic interpretation:

- 41 of 75 required gold labels have exact/text-normalized/overlap matches in the current report.
- 34 required labels are currently reported as missed.
- 11 wrong-type findings are reported.
- 8 false-positive candidates are reported.
- 0 preserve-term hits are reported, which is good for the current role/context preservation fixtures.
- 1 known-trap hit is reported.
- These values are diagnostic only and must not be treated as accepted thresholds.

## 4. Per-document findings

| document_id | domain | source_file | gold_label_count | prediction_count | missed_required_count | wrong_type_count | preserve_term_hit_count | known_trap_hit_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| care_mixed_identifiers_seed_001 | care | corpus/care/care_mixed_identifiers_seed_001.txt | 12 | 10 | 6 | 2 | 0 | 1 |
| care_reference_seed_001 | care | corpus/care/care_reference_seed_001.txt | 9 | 6 | 5 | 1 | 0 | 0 |
| care_role_preservation_seed_001 | care | corpus/care/care_role_preservation_seed_001.txt | 10 | 6 | 6 | 2 | 0 | 0 |
| legal_false_positive_traps_seed_001 | legal | corpus/legal/legal_false_positive_traps_seed_001.txt | 7 | 5 | 3 | 0 | 0 | 0 |
| legal_mixed_identifiers_seed_001 | legal | corpus/legal/legal_mixed_identifiers_seed_001.txt | 15 | 13 | 6 | 3 | 0 | 0 |
| legal_reference_seed_001 | legal | corpus/legal/legal_reference_seed_001.txt | 19 | 20 | 5 | 2 | 0 | 0 |
| legal_role_preservation_seed_001 | legal | corpus/legal/legal_role_preservation_seed_001.txt | 3 | 1 | 3 | 1 | 0 | 0 |

Highest-risk diagnostic concentration:

- `legal_role_preservation_seed_001`: 3/3 missed and 1 wrong-type; role-name detection/mapping needs follow-up.
- `care_role_preservation_seed_001`: 6/10 missed and 2 wrong-type; care role/name and care client-reference taxonomy need follow-up.
- `care_mixed_identifiers_seed_001`: 6/12 missed, 2 wrong-type and 1 known-trap hit; care location/reference taxonomy needs follow-up.
- `legal_mixed_identifiers_seed_001`: 6/15 missed and 3 wrong-type; runner mapping issues are visible for address/IBAN/client reference.
- `legal_reference_seed_001`: 5/19 missed and 2 wrong-type; case/address mapping and person/email coverage need follow-up.

## 5. Missed required labels

Missed required labels by entity class:

| entity_class | count | examples |
| --- | --- | --- |
| PERSON | 16 | care_mixed_identifiers_seed_001: `Hassan El Amrani`; care_mixed_identifiers_seed_001: `Mila van Dijk`; care_reference_seed_001: `Ahmed El Idrissi` |
| MEDICAL_OR_CARE_REFERENCE | 7 | care_mixed_identifiers_seed_001: `C-118`; care_mixed_identifiers_seed_001: `Rozenhof 3`; care_mixed_identifiers_seed_001: `ZORG-CL-2026-88990` |
| EMAIL | 6 | care_mixed_identifiers_seed_001: `hassan.elamrani@example.test`; care_reference_seed_001: `ahmed.elidrissi@example.test`; care_role_preservation_seed_001: `sara.elidrissi@example.test` |
| ADDRESS | 2 | legal_mixed_identifiers_seed_001: `Laan van Meerdervoort 100, 2517 AS Den Haag`; legal_reference_seed_001: `Parklaan 188, 3512 ZX Utrecht` |
| CLIENT_NUMBER | 1 | legal_mixed_identifiers_seed_001: `CL-HUUR-2026-0009` |
| IBAN | 1 | legal_mixed_identifiers_seed_001: `NL91 ABNA 0417 1643 00` |
| CASE_NUMBER | 1 | legal_reference_seed_001: `ZK-WOON-55091` |

Interpretation by group:

### PERSON — 16 missed

Likely cause:

```text
C. recognizer coverage issue
B. runner mapping issue for NL_LEGAL_PARTY_NAME -> PERSON
F. needs follow-up decision
```

Many synthetic personal names are missed. Some are detected as `NL_LEGAL_PARTY_NAME` but not accepted/mapped as `PERSON`, so part of the miss count may be a runner/benchmark mapping problem rather than pure recognizer failure.

### MEDICAL_OR_CARE_REFERENCE — 7 missed

Likely cause:

```text
A. corpus/gold-label taxonomy issue
C. recognizer coverage issue
D. candidate-scanner coverage issue
F. needs follow-up decision
```

Care room/department references such as `C-118`, `B-214`, `Magnolia 2` and care-client values such as `ZORG-CL-2026-00441` need a clearer benchmark decision: should they be measured as care references, locations, client references or candidate rows?

### EMAIL — 6 missed

Likely cause:

```text
B. runner/report issue
C. recognizer coverage issue
F. needs follow-up decision
```

The current runner/report path appears not to surface email predictions in the artifact even though the corpus contains reserved synthetic `@example.test` emails. This should be investigated before threshold planning.

### ADDRESS — 2 missed

Likely cause:

```text
B. runner mapping issue
F. needs follow-up decision
```

Address text is detected as `NL_ADDRESS`, but the benchmark mapping/acceptable entity types do not currently accept that as `ADDRESS` or `LOCATION` in the reviewed artifact. This likely inflates missed/wrong-type counts.

### CLIENT_NUMBER / IBAN / CASE_NUMBER — 1 missed each

Likely cause:

```text
B. runner mapping issue
C. recognizer coverage issue
F. needs follow-up decision
```

Examples include `CL-HUUR-2026-0009`, `NL91 ABNA 0417 1643 00` and `ZK-WOON-55091`. The artifact shows several cases where a recognizer produced a near-correct or exact semantic type (`NL_IBAN`, `NL_CASE_REFERENCE`) but the runner mapping did not accept it.

## 6. Wrong-type findings

| document_id | gold_class | gold_text | prediction_entity_types | acceptable_entity_types | diagnosis |
| --- | --- | --- | --- | --- | --- |
| care_mixed_identifiers_seed_001 | MEDICAL_OR_CARE_REFERENCE | `Rozenhof 3` | NL_ADDRESS×3 | LOCATION, ORGANIZATION, NL_HEALTHCARE_REFERENCE | B/F: runner mapping/acceptable-types issue likely; detected as address but not accepted/mapped. |
| care_mixed_identifiers_seed_001 | MEDICAL_OR_CARE_REFERENCE | `ZORG-CL-2026-88990` | NL_CLIENT_REFERENCE×3 | NL_HEALTHCARE_REFERENCE, NL_SUSPICIOUS_REFERENCE_CANDIDATE | A/F: care client reference taxonomy/acceptable-types needs decision. |
| care_reference_seed_001 | MEDICAL_OR_CARE_REFERENCE | `ZORG-CL-2026-00441` | NL_CLIENT_REFERENCE×3 | NL_HEALTHCARE_REFERENCE, NL_SUSPICIOUS_REFERENCE_CANDIDATE | A/F: care client reference taxonomy/acceptable-types needs decision. |
| care_role_preservation_seed_001 | PERSON | `Youssef Ait Ben` | NL_LEGAL_PARTY_NAME×3 | PERSON | B/F: legal-party name mapping to PERSON needs decision. |
| care_role_preservation_seed_001 | MEDICAL_OR_CARE_REFERENCE | `ZORG-CL-2026-77881` | NL_CLIENT_REFERENCE×3 | NL_HEALTHCARE_REFERENCE, NL_SUSPICIOUS_REFERENCE_CANDIDATE | A/F: care client reference taxonomy/acceptable-types needs decision. |
| legal_mixed_identifiers_seed_001 | CLIENT_NUMBER | `CL-HUUR-2026-0009` | NL_LEGAL_PARTY_NAME×1 | NL_CLIENT_REFERENCE, NL_SUSPICIOUS_REFERENCE_CANDIDATE | B/F: legal-party name mapping to PERSON needs decision. |
| legal_mixed_identifiers_seed_001 | IBAN | `NL91 ABNA 0417 1643 00` | NL_IBAN×2 | IBAN_CODE, IBAN | B: runner mapping issue likely; NL_IBAN should probably map to IBAN. |
| legal_mixed_identifiers_seed_001 | ADDRESS | `Laan van Meerdervoort 100, 2517 AS Den Haag` | NL_ADDRESS×3, NL_POSTCODE×1 | LOCATION, ADDRESS | B/F: runner mapping/acceptable-types issue likely; detected as address but not accepted/mapped. |
| legal_reference_seed_001 | CASE_NUMBER | `ZK-WOON-55091` | NL_CASE_REFERENCE×3 | NL_LEGAL_CASE_NUMBER, NL_SUSPICIOUS_REFERENCE_CANDIDATE | B: runner mapping issue likely; case reference detected but not mapped/accepted. |
| legal_reference_seed_001 | ADDRESS | `Parklaan 188, 3512 ZX Utrecht` | NL_ADDRESS×3, NL_POSTCODE×1 | LOCATION, ADDRESS | B/F: runner mapping/acceptable-types issue likely; detected as address but not accepted/mapped. |
| legal_role_preservation_seed_001 | PERSON | `Sami El Amrani` | NL_LEGAL_PARTY_NAME×3 | PERSON | B/F: legal-party name mapping to PERSON needs decision. |

Main wrong-type pattern:

1. `NL_ADDRESS` is not mapped/accepted as address/location in the current report.
2. `NL_IBAN` is not mapped/accepted as `IBAN`.
3. `NL_CASE_REFERENCE` is not mapped/accepted as `CASE_NUMBER`.
4. `NL_LEGAL_PARTY_NAME` is not mapped/accepted as `PERSON`.
5. `NL_CLIENT_REFERENCE` for `ZORG-CL-*` care client references needs a taxonomy decision.

This means several wrong-type findings are probably benchmark/runner mapping issues, not necessarily product detection failures.

## 7. Preserve-term hits

Preserve-term hits:

```text
preserve_term_hit_count = 0
```

Interpretation:

- No role/context terms were directly hit by predictions in this artifact.
- That is a positive diagnostic signal for role/context preservation.
- It does not prove production safety because this is a synthetic corpus and no thresholds exist.

Role/context terms that remain important for future checks include:

```text
slachtoffer
arts
getuige
eiser
verweerder
minderjarige
cliënt
zorgmedewerker
verpleegkundige
behandelaar
mantelzorger
kamer
afdeling
```

## 8. Known-trap hits

| document_id | trap_text | trap_type | prediction | interpretation |
| --- | --- | --- | --- | --- |
| care_mixed_identifiers_seed_001 | `afdeling Rozenhof 3` | care_location_context_needs_review | `Rozenhof 3` / NL_ADDRESS | Care-location review signal; not a product precision claim. |

Interpretation:

- The only known-trap hit is `afdeling Rozenhof 3`, where `Rozenhof 3` was predicted as `NL_ADDRESS`.
- The trap type is `care_location_context_needs_review`, not a hard “must not detect” false positive.
- This should be treated as a care-location taxonomy/review-policy decision, not as a product claim failure.

## 9. Diagnosis classification

### A. corpus/gold-label issue

Potential corpus/taxonomy decisions:

- Care client references such as `ZORG-CL-*` are currently labeled as `MEDICAL_OR_CARE_REFERENCE` but detected as `NL_CLIENT_REFERENCE`.
- Care room/department values need a clearer taxonomy: sensitive location, care reference or context requiring review.
- Some labels may need broader `acceptable_entity_types`.

### B. runner/report issue

Likely runner/report mapping issues:

- Map or accept `NL_ADDRESS` for address/location gold labels.
- Map or accept `NL_IBAN` for IBAN gold labels.
- Map or accept `NL_CASE_REFERENCE` for case-number gold labels.
- Decide whether `NL_LEGAL_PARTY_NAME` should count as a `PERSON` match in this benchmark.
- Dedupe repeated predictions so wrong-type and false-positive counts are not inflated.

### C. recognizer coverage issue

Likely recognizer coverage issues:

- Many `PERSON` labels have no accepted match.
- `EMAIL` labels have no accepted match in this artifact.
- Some care-location/care-reference values are not detected unless they fit existing candidate patterns.

### D. candidate-scanner coverage issue

Likely candidate-scanner follow-ups:

- Care room references such as `C-118` and `B-214` are not surfaced.
- Some care client/reference patterns are not surfaced as care-specific candidates.
- Candidate output is still intentionally review-candidate visibility, not automatic masking proof.

### E. expected limitation / accepted diagnostic finding

Expected limitations:

- The current corpus is synthetic and small.
- Candidate-scanner rows are ambiguous by design.
- Overlap matching is diagnostic, not strict recall.
- The artifact does not enforce thresholds.

### F. needs follow-up decision

Follow-up decisions needed before thresholds:

1. Should runner mapping be repaired before threshold planning?
2. Should `NL_LEGAL_PARTY_NAME` count as `PERSON` in this benchmark?
3. Should `NL_ADDRESS` count as `ADDRESS`/`LOCATION`?
4. Should `NL_IBAN` count as `IBAN`?
5. Should `NL_CASE_REFERENCE` count as `CASE_NUMBER`?
6. Should care `ZORG-CL-*` values be measured as care reference or client reference?
7. Should email detection be added through built-in Presidio entities in the runner, or should the corpus expectation be adjusted?

## 10. Recommended next step

Do not start threshold planning yet.

The artifact is useful and structurally valid, but the first content review shows the raw counts are currently inflated by mapping/taxonomy/deduplication issues. Starting threshold planning now would risk setting thresholds against noisy metrics.

Recommended next workpackage:

```text
WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX
```

Suggested narrow scope:

- review and repair runner mapping for `NL_ADDRESS`, `NL_IBAN`, `NL_CASE_REFERENCE`, and possibly `NL_LEGAL_PARTY_NAME`;
- dedupe repeated predictions before wrong-type/false-positive reporting;
- clarify care-reference acceptable types for `ZORG-CL-*`;
- investigate why `EMAIL_ADDRESS` predictions are absent;
- keep output diagnostic only;
- no product UI, recognizer/pattern product changes, thresholds or production gate.

Only after that, consider:

```text
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN
```

## 11. Non-claims

This review is diagnostic only.

This review does not prove production safety.

This review does not define accepted thresholds.

This review does not create a production gate.

This review does not support the claim that all legal/care identifiers are always detected.
