# Cleaned diagnostic recall benchmark report review

Status: review-only

Artifact: `diagnostic-recall-benchmark-report`

Workflow: `Diagnostic recall benchmark report`

Reviewed files uploaded by coordinator:

```text
recall_benchmark_report.json
recall_benchmark_summary.md
```

This review follows `WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX`.

---

## 1. Scope and boundaries

This review is documentation-only. It reviews the cleaned diagnostic recall benchmark artifact output after mapping, deduplication and benchmark-only email cleanup.

No product code was changed by this review.

Boundaries preserved:

- no product UI change;
- no recognizer change;
- no pattern fix;
- no runner/report code change;
- no workflow change;
- no export/download change;
- no Scrub Key change;
- no reinsert change;
- no threshold enforcement;
- no production gate;
- no product safety claim.

---

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

---

## 3. Summary values

| Metric | First artifact | Cleaned artifact | Change |
|---|---:|---:|---:|
| document_count | 7 | 7 | 0 |
| gold_label_count | 75 | 75 | 0 |
| prediction_count | 61 | 60 | -1 |
| required_label_count | 75 | 75 | 0 |
| matched_required_exact_count | 41 | 56 | +15 |
| matched_required_text_normalized_count | 41 | 57 | +16 |
| matched_required_overlap_count | 41 | 57 | +16 |
| missed_required_count | 34 | 18 | -16 |
| wrong_type_count | 11 | 1 | -10 |
| false_positive_candidate_count | 8 | 1 | -7 |
| preserve_term_hit_count | 0 | 0 | 0 |
| known_trap_hit_count | 1 | 1 | 0 |

Diagnostic interpretation:

- The cleanup materially reduced mapping/counting noise.
- Exact required matches improved from 41 to 56.
- Missed required labels dropped from 34 to 18.
- Wrong-type findings dropped from 11 to 1.
- False-positive candidates dropped from 8 to 1.
- Preserve-term hits remain 0.
- Known-trap hits remain 1 and are still a care-location review signal.

This is still diagnostic only and not a production safety claim.

---

## 4. Per-document findings

| document_id | domain | source_file | gold_label_count | prediction_count | matched_exact | missed_required_count | wrong_type_count | false_positive_candidate_count | preserve_term_hit_count | known_trap_hit_count |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| care_mixed_identifiers_seed_001 | care | corpus/care/care_mixed_identifiers_seed_001.txt | 12 | 10 | 9 | 3 | 0 | 1 | 0 | 1 |
| care_reference_seed_001 | care | corpus/care/care_reference_seed_001.txt | 9 | 6 | 6 | 3 | 0 | 0 | 0 | 0 |
| care_role_preservation_seed_001 | care | corpus/care/care_role_preservation_seed_001.txt | 10 | 7 | 7 | 3 | 0 | 0 | 0 | 0 |
| legal_false_positive_traps_seed_001 | legal | corpus/legal/legal_false_positive_traps_seed_001.txt | 7 | 5 | 5 | 2 | 0 | 0 | 0 | 0 |
| legal_mixed_identifiers_seed_001 | legal | corpus/legal/legal_mixed_identifiers_seed_001.txt | 15 | 13 | 11 | 3 | 1 | 0 | 0 | 0 |
| legal_reference_seed_001 | legal | corpus/legal/legal_reference_seed_001.txt | 19 | 18 | 17 | 2 | 0 | 0 | 0 | 0 |
| legal_role_preservation_seed_001 | legal | corpus/legal/legal_role_preservation_seed_001.txt | 3 | 1 | 1 | 2 | 0 | 0 | 0 | 0 |

Most remaining misses are now concentrated in:

- person-name coverage;
- care room/location references;
- one client-number value.

---

## 5. Missed required labels

Missed required labels by entity class:

| entity_class | count | examples |
|---|---:|---|
| PERSON | 14 | `Hassan El Amrani`; `Mila van Dijk`; `Ahmed El Idrissi`; `Bakker`; `Sara El Idrissi`; `Fatima Zahra`; `Lina de Vries`; `Omar Ben Salah`; `Nora El Yassini`; `Tariq de Jong`; `Noor van Dijk`; `Sami El Amrani`; `Jansen`; `Fatima El Amrani` |
| MEDICAL_OR_CARE_REFERENCE | 3 | `C-118`; `B-214`; `Magnolia 2` |
| CLIENT_NUMBER | 1 | `CL-HUUR-2026-0009` |

### PERSON — 14 missed

Likely classification:

```text
C. recognizer coverage issue
F. needs follow-up decision
```

Interpretation:

- Mapping cleanup worked for `NL_LEGAL_PARTY_NAME -> PERSON` when the recognizer finds the name.
- Many names are still simply not predicted by the current analyzer/helper path.
- This looks less like report noise and more like a real recall-coverage issue for person names in synthetic Dutch legal/care text.

### MEDICAL_OR_CARE_REFERENCE — 3 missed

Values:

```text
C-118
B-214
Magnolia 2
```

Likely classification:

```text
C. recognizer coverage issue
D. candidate-scanner coverage issue
F. needs follow-up decision
```

Interpretation:

- These are care room/department/location-style values.
- The taxonomy cleanup helped for `Rozenhof 3`, but these three values still are not detected.
- This is a concrete care-location/care-reference follow-up area.

### CLIENT_NUMBER — 1 missed

Value:

```text
CL-HUUR-2026-0009
```

Likely classification:

```text
C. recognizer coverage issue
D. candidate-scanner coverage issue
F. needs follow-up decision
```

Interpretation:

- The value is partly misread as `NL_LEGAL_PARTY_NAME` with text `CL-HUUR-`.
- This is no longer a broad mapping issue; it is a concrete client-reference recognition/candidate issue.

---

## 6. Wrong-type findings

Only one wrong-type finding remains.

| document_id | gold_class | gold_text | prediction_entity_type | prediction_text | diagnosis |
|---|---|---|---|---|---|
| legal_mixed_identifiers_seed_001 | CLIENT_NUMBER | `CL-HUUR-2026-0009` | `NL_LEGAL_PARTY_NAME` | `CL-HUUR-` | Concrete recognizer/candidate issue; no longer broad benchmark mapping noise. |

Interpretation:

- The cleanup reduced wrong-type findings from 11 to 1.
- Remaining wrong-type is specific and actionable.
- This should not block planning-only thresholds, but it should remain visible as an open recall/precision issue.

---

## 7. False-positive candidates

Only one false-positive candidate remains.

| document_id | text | entity_type | benchmark_class | source | interpretation |
|---|---|---|---|---|---|
| care_mixed_identifiers_seed_001 | `55667788` | `NL_BSN` | BSN | recognizer | Nested/overlapping false positive inside phone-like value `06 55667788`; concrete precision issue. |

Interpretation:

- False-positive candidates dropped from 8 to 1.
- Matched predictions are no longer broadly double-counted as false positives.
- Remaining false-positive looks like a real nested-value precision issue, not report-accounting noise.

---

## 8. Preserve-term hits

Preserve-term hits:

```text
preserve_term_hit_count = 0
```

Interpretation:

- Role/context terms were not directly hit in this cleaned artifact.
- This remains a positive diagnostic signal.
- It does not prove production safety.

Important role/context terms remain:

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

---

## 9. Known-trap hits

Known-trap hits:

| document_id | trap_text | trap_type | prediction | interpretation |
|---|---|---|---|---|
| care_mixed_identifiers_seed_001 | `afdeling Rozenhof 3` | `care_location_context_needs_review` | `Rozenhof 3` / `NL_ADDRESS` | Care-location review signal, not a hard product precision failure. |

Interpretation:

- Known-trap hit count remains 1.
- This is expected/reviewable care-location context.
- It should remain visible in future reports.

---

## 10. Cleanup effectiveness

The cleanup was effective.

Evidence:

- `NL_ADDRESS` now matches address/location/care-location labels where accepted.
- `NL_IBAN` now matches IBAN labels via normalized text.
- `NL_CASE_REFERENCE` now matches case-number labels.
- `NL_LEGAL_PARTY_NAME` now matches `PERSON` where the recognizer finds the name.
- `EMAIL_ADDRESS` / benchmark-only email predictions now match email labels.
- Duplicate-prediction accounting noise is substantially reduced.
- False-positive candidate count dropped to 1.
- Wrong-type count dropped to 1.

Remaining misses now look more like real coverage/taxonomy/product-risk questions than benchmark accounting bugs.

---

## 11. Threshold planning readiness

Threshold planning is now reasonable as a planning-only package.

Conditions:

- Threshold planning must not enforce gates.
- Threshold planning must not claim production safety.
- Threshold planning must explicitly separate:
  - exact match;
  - text-normalized match;
  - overlap diagnostic match;
  - missed required;
  - wrong type;
  - false positive;
  - preserve-term hit;
  - known-trap hit.
- Threshold planning must account for the remaining PERSON, care-location and client-number gaps.

Recommended next workpackage:

```text
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN
```

Scope must be planning-only:

```text
no CI gate
no production blocking
no threshold enforcement
no product claim
```

Backlog after threshold planning or in parallel after separate approval:

```text
WP_RECALL_PERSON_NAME_COVERAGE_REVIEW
WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN
WP_CLIENT_REFERENCE_COVERAGE_REVIEW
```

---

## 12. Non-claims

This review is diagnostic only.

This review does not prove production safety.

This review does not define accepted production thresholds.

This review does not create a production gate.

This review does not support the claim that all legal/care identifiers are always detected.
