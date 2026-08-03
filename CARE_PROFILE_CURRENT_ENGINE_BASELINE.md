# Zorgfilter v1 — current-engine baseline

Status: completed evidence baseline  
Workpackage: `SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE`  
Corpus: eight fully synthetic Dutch care documents

## Purpose

Measure what the existing deterministic Dutch custom recognizers detect before dedicated Zorgfilter recognizers are added.

This baseline deliberately excludes generic NER-model and cloud results. It therefore isolates the current rule-based Dutch recognizer layer and is not a complete measurement of the live app.

## Headline result

```text
Expected replace/review values:        81
Exact value spans found:               25  (30.86%)
Found under the correct entity type:   14  (17.28%)
Found but misclassified:               11
Missed:                                56
Protected clinical phrase overlaps:     0
```

These values are evidence for gap triage. They are not production thresholds or a production-readiness claim.

## Policy-level result

| Policy bucket | Expected | Found span | Correct entity | Misclassified | Missed |
| --- | ---: | ---: | ---: | ---: | ---: |
| Replace by default | 39 | 21 | 11 | 10 | 18 |
| Review, selected by default | 42 | 4 | 3 | 1 | 38 |

The current rules perform materially better on direct Dutch numeric identifiers than on contextual care identifiers. The review-selected layer is almost absent and requires dedicated care-aware recognition.

## Strong current coverage

The bounded corpus shows exact correct-entity coverage for:

- Dutch addresses: 2/2;
- BIG numbers: 3/3;
- BSN: 2/2;
- dates of birth: 4/4;
- Dutch telephone numbers: 3/3.

This does not prove production precision or recall outside the synthetic corpus.

## Principal care gaps

The current custom recognizers found none of the expected:

- patient, client or relative names represented as generic `PERSON`: 0/11;
- care-provider names: 0/10;
- care organizations: 0/9;
- exact care-event dates: 0/7;
- care location/team/department references: 0/6;
- room or bed references: 0/4;
- EPD/ECD numbers: 0/2;
- e-mail addresses: 0/2 in this custom-rule-only baseline.

The PERSON and e-mail gaps must not be read as full-app results because generic NER recognition was intentionally excluded.

## Existing broad recognition and misclassification

Several care values are already found as spans, but under a broader or wrong entity:

- patient numbers are found as `NL_HEALTHCARE_REFERENCE`;
- care client numbers are found as `NL_CLIENT_REFERENCE`;
- medical record numbers are found as `NL_DOSSIER_NUMBER` or `NL_HEALTHCARE_REFERENCE`;
- referral and treatment references are found as `NL_HEALTHCARE_REFERENCE`;
- a MIC number is found as `NL_INCIDENT_NUMBER`;
- one AGB code is incorrectly found as `NL_BSN`.

The AGB/BSN collision is especially important: eight-digit context-bound provider codes must not be treated as a BSN merely because the numeric checksum or shape appears plausible. Care-aware context and exact entity policy are required.

## Clinical-context preservation

No current deterministic custom recognizer overlapped the corpus phrases that must be preserved, including:

- diagnoses;
- medication and dosages;
- laboratory results and units;
- observations and functional status;
- vital signs;
- allergies;
- care goals and treatment meaning.

This is a useful starting signal, but generic NER models and future care recognizers still require explicit negative tests before UI integration.

## Case results

| Document family | Expected | Found | Correct entity | Misclassified | Missed |
| --- | ---: | ---: | ---: | ---: | ---: |
| Daily nursing report | 13 | 5 | 4 | 1 | 8 |
| Care plan and evaluation | 10 | 2 | 0 | 2 | 8 |
| Nursing transfer | 13 | 4 | 4 | 0 | 9 |
| Specialist discharge letter | 11 | 3 | 1 | 2 | 8 |
| GP referral | 9 | 4 | 2 | 2 | 5 |
| Medication overview | 8 | 3 | 2 | 1 | 5 |
| Laboratory report | 6 | 1 | 0 | 1 | 5 |
| MIC/MIM/VIM report | 11 | 3 | 1 | 2 | 8 |

## Required next triage

The next workpackage must classify each evidence gap into:

1. dedicated care-pattern recognizer;
2. generic NER/profile dependency;
3. contextual candidate/review scanner;
4. entity-policy mapping of an already-found span;
5. false-positive prevention;
6. document or UI behavior outside recognizer scope;
7. intentionally preserved clinical content.

No recognizer should be implemented merely to improve the aggregate percentage. Each change must preserve exact spans, role/context words and clinical meaning.

## Evidence files

- `output/validation/care_profile_v1_current_engine_baseline.json`
- `care_profile_baseline.py`
- `care_profile_baseline_summary.py`
- `care_test_examples.py`

## Boundaries

- synthetic data only;
- deterministic Dutch custom recognizers only;
- generic NER excluded;
- no product behavior changed;
- human review remains required;
- production readiness remains false.
