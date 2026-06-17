# Recall benchmark thresholds plan

Workpackage: `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN`

Repository: `solidprivacy-nl/scrub`

Status: planning/documentation-only.

This document plans how diagnostic recall/precision thresholds could be designed later. It does not enforce thresholds, does not create a CI gate, does not block releases and does not support a product safety claim.

---

## 1. Goal and non-goals

Goal:

```text
Define which diagnostic recall/precision metrics matter, how thresholds could later be selected, which risks remain open and which conditions are required before any real gate is considered.
```

Non-goals:

```text
This is a planning document.
This does not define accepted production thresholds.
This does not activate a CI gate.
This does not block a release.
This does not prove product safety.
This does not change product behavior.
This does not change recognizers, candidate scanner, UI, export, Scrub Key or reinsert behavior.
```

---

## 2. Current diagnostic benchmark baseline

The cleaned artifact reviewed in `RECALL_BENCHMARK_REPORT_REVIEW_2.md` is the current planning baseline:

```text
document_count = 7
gold_label_count = 75
prediction_count = 60
required_label_count = 75
matched_required_exact_count = 56
matched_required_text_normalized_count = 57
matched_required_overlap_count = 57
missed_required_count = 18
wrong_type_count = 1
false_positive_candidate_count = 1
preserve_term_hit_count = 0
known_trap_hit_count = 1
```

Improvement from the first artifact:

```text
matched_required_exact_count: 41 -> 56
missed_required_count: 34 -> 18
wrong_type_count: 11 -> 1
false_positive_candidate_count: 8 -> 1
preserve_term_hit_count: 0 -> 0
known_trap_hit_count: 1 -> 1
```

Important limits:

```text
The corpus is synthetic.
The corpus is small.
The corpus is useful for regression and trend measurement.
The corpus is not production certification.
```

Planning conclusion:

```text
The cleaned benchmark output is useful enough for planning thresholds.
It is not suitable for enforcing thresholds yet.
```

---

## 3. Metric definitions

| Metric | Meaning | Planning interpretation | Hard/soft status |
|---|---|---|---|
| `required_label_count` | Number of gold labels that should be found. | Denominator for recall-style planning. | Hard inventory metric. |
| `matched_required_exact_count` | Predictions with exact start/end and acceptable class. | Strictest useful recall indicator. | Hardest match metric. |
| `matched_required_text_normalized_count` | Predictions where normalized text equals the gold value. | Useful for Dutch formatting differences in phone, IBAN and references. | Useful secondary metric. |
| `matched_required_overlap_count` | Predictions overlapping the gold span with acceptable class. | Diagnostic help only; should not hide missed values. | Soft diagnostic metric. |
| `missed_required_count` | Required gold labels with no acceptable match. | Main false-negative indicator. | Critical safety metric. |
| `wrong_type_count` | Gold value detected with an unacceptable entity type. | Recall/precision and mapping risk. | High-signal diagnostic metric. |
| `false_positive_candidate_count` | Prediction not used by an accepted gold-label match. | Precision/review-load risk. | Review-load metric. |
| `preserve_term_hit_count` | Prediction overlaps a role/context term that should remain readable. | Legal/care meaning risk. | Strong warning metric. |
| `known_trap_hit_count` | Prediction overlaps a known trap. | Review signal; not automatically wrong. | Soft diagnostic/review signal. |

Recommended metric interpretation:

```text
exact match = strictest usable recall indicator
text-normalized match = useful for formatting differences
overlap match = diagnostic help, not suitable as primary threshold
missed_required = main false-negative indicator
wrong_type = recall/precision risk
false_positive_candidate = precision/review-load risk
preserve_term_hit = legal meaning/context risk
known_trap_hit = review signal, not automatically wrong
```

---

## 4. Threshold category model

No threshold is enforced by this plan. The categories below describe later governance stages only.

### 4.1 Planning baseline

Purpose:

- record current trend;
- compare future report artifacts;
- identify noisy metrics and entity classes;
- no release block;
- no CI failure.

Current status:

```text
Allowed now.
Already useful.
No enforcement.
```

### 4.2 Warning threshold

Purpose:

- signal meaningful regression;
- trigger review discussion;
- document why the metric moved;
- no automatic block.

Example future use:

```text
If missed_required_count rises materially from the current baseline, open a review item.
```

### 4.3 Release review threshold

Purpose:

- require a human review before release/promotion if diagnostic metrics regress;
- still no automatic block;
- requires a written exception or follow-up package.

Example future use:

```text
If preserve_term_hit_count becomes non-zero, require legal/care context review before release promotion.
```

### 4.4 Future blocking threshold

Purpose:

- only after separate approval;
- only after larger corpus;
- only after stable metric definitions;
- only after false-negative and false-positive policy approval;
- implemented in a separate workpackage.

Current status:

```text
Not allowed yet.
No blocking threshold exists.
No CI gate exists.
```

---

## 5. Candidate threshold direction

These are planning candidates only. They are not accepted product thresholds and may not fail CI.

Candidate direction:

```text
preserve_term_hit_count should remain 0
wrong_type_count should remain very low
false_positive_candidate_count should remain low
missed_required_count should trend down
matched_required_exact_count should trend up
matched_required_text_normalized_count should trend up or remain stable
overlap matches should stay diagnostic-only
known_trap_hit_count should be reviewed by trap category, not treated as automatically wrong
```

Current cleaned artifact baseline:

```text
preserve_term_hit_count = 0
wrong_type_count = 1
false_positive_candidate_count = 1
missed_required_count = 18
matched_required_exact_count = 56
matched_required_text_normalized_count = 57
known_trap_hit_count = 1
```

Explicit non-enforcement:

```text
These values are not accepted product thresholds.
These values may not fail CI yet.
These values do not create a production gate.
These values do not prove safety.
```

---

## 6. Class-specific planning

### 6.1 PERSON

Current status:

```text
14 missed PERSON labels in the cleaned artifact.
```

Risk:

- direct identifier false negatives;
- especially relevant in legal/care role-name context.

Planning candidate:

- do not set a hard PERSON threshold yet;
- use current misses as a baseline for coverage review;
- prioritize trend reduction.

Open follow-up:

```text
WP_RECALL_PERSON_NAME_COVERAGE_REVIEW
```

### 6.2 LEGAL_REFERENCE / CASE_NUMBER

Current status:

- mapping cleanup improved `NL_CASE_REFERENCE -> CASE_NUMBER`;
- no broad mapping-noise issue remains in the cleaned artifact.

Risk:

- legal matter references can be missed or partially detected.

Planning candidate:

- exact/text-normalized detection should remain stable;
- wrong-type count for case/reference values should remain near zero.

Open follow-up:

- monitor through the next artifact;
- only create a narrow pattern package if cleaned reports show concrete missed legal references.

### 6.3 CLIENT_NUMBER

Current status:

```text
1 missed/wrong CLIENT_NUMBER: CL-HUUR-2026-0009.
```

Risk:

- client identifiers are high-risk false negatives.

Planning candidate:

- client-number misses should trend toward zero before any future gate;
- current value should be tracked as a named diagnostic gap.

Open follow-up:

```text
WP_CLIENT_REFERENCE_COVERAGE_REVIEW
```

### 6.4 MEDICAL_OR_CARE_REFERENCE

Current status:

```text
3 missed care room/location values: C-118, B-214, Magnolia 2.
```

Risk:

- room/department references can identify care context or individuals depending on local setting;
- over-aggressive detection can also damage meaning.

Planning candidate:

- separate care-location references from stronger care identifiers;
- avoid hard threshold until taxonomy is clearer.

Open follow-up:

```text
WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN
```

### 6.5 EMAIL

Current status:

- benchmark-only email mapping now prevents synthetic email labels from being missed in the runner;
- this is not a product recognizer claim.

Risk:

- direct identifier false negatives if product path differs from benchmark-only behavior.

Planning candidate:

- email should remain a high-recall class in future threshold planning;
- document distinction between benchmark-only detection and product behavior.

Open follow-up:

- later verify product analyzer coverage separately if needed.

### 6.6 PHONE

Current status:

- mostly covered in the cleaned artifact;
- one nested false positive remains: `55667788` as `NL_BSN` inside a phone-like value.

Risk:

- phone values are direct identifiers;
- nested BSN false positives can increase review load and confusion.

Planning candidate:

- phone recall should be high;
- nested false positives should be tracked under precision/review-load.

Open follow-up:

- include nested-phone/BSN trap in threshold planning and later precision review.

### 6.7 IBAN

Current status:

- improved by normalized `NL_IBAN -> IBAN` mapping.

Risk:

- direct financial identifier.

Planning candidate:

- IBAN should have high exact/text-normalized match expectations once corpus grows.

Open follow-up:

- add more IBAN variants before any gate.

### 6.8 BSN

Current status:

- one nested false-positive candidate remains inside a phone-like value.

Risk:

- BSN is high-sensitivity;
- false positives can confuse review, while false negatives would be critical.

Planning candidate:

- distinguish BSN recall and BSN false-positive traps;
- do not set hard thresholds until corpus contains valid/invalid BSN examples and phone/date traps.

Open follow-up:

- expand BSN trap fixtures later if threshold work proceeds.

### 6.9 ADDRESS / LOCATION

Current status:

- improved by `NL_ADDRESS -> ADDRESS` mapping;
- care-location known trap remains visible.

Risk:

- addresses are direct identifiers;
- care location can be sensitive depending on context.

Planning candidate:

- keep address/location threshold separate from care-location review signals;
- review known-trap category manually.

Open follow-up:

- care-location candidate planning.

### 6.10 ROLE_OR_CONTEXT_TERMS_TO_PRESERVE

Current status:

```text
preserve_term_hit_count = 0
```

Risk:

- masking legal/care role terms can damage meaning.

Planning candidate:

```text
preserve_term_hit_count should remain 0 as a warning/release-review candidate.
```

Open follow-up:

- keep preserve-term checks in future artifacts.

### 6.11 KNOWN_TRAPS

Current status:

```text
known_trap_hit_count = 1
```

Current known hit:

```text
afdeling Rozenhof 3 -> Rozenhof 3 / NL_ADDRESS, care_location_context_needs_review
```

Risk:

- known traps may be precision risks or expected review signals depending on trap type.

Planning candidate:

- do not treat all known-trap hits as failures;
- classify by trap type;
- require review explanation if count increases.

Open follow-up:

- define trap severity classes in a later contract/spec package.

---

## 7. Conditions before any real gate

A real gate may only be considered after all of these are true:

```text
larger corpus
stable metric definitions
at least two reviewed artifacts after cleanup
clear per-class minimums
approved false-negative policy
approved false-positive/review-load policy
explicit coordinator approval
separate workpackage for gate implementation
```

Additional recommended preconditions:

- per-class trend history across multiple commits;
- known-trap severity classification;
- explicit treatment of overlap matches as diagnostic-only;
- separate handling for legal, care and mixed-professional corpora;
- documented exception process for threshold regressions.

---

## 8. Recommended follow-up packages

Recommended next package:

```text
WP_RECALL_PERSON_NAME_COVERAGE_REVIEW
```

Alternative next packages depending on coordinator priority:

```text
WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN
WP_CLIENT_REFERENCE_COVERAGE_REVIEW
WP_RECALL_BENCHMARK_THRESHOLDS_CONTRACT_TESTS
WP_RECALL_BENCHMARK_GATE_PLAN
```

Important boundary:

```text
WP_RECALL_BENCHMARK_GATE_PLAN is still planning.
No gate implementation.
```

No follow-up package should start automatically.

---

## 9. Product-claim policy

Disallowed claims:

```text
Alle persoonsgegevens worden altijd gevonden.
Alle juridische nummers worden altijd herkend.
De app is veilig voor productie zonder menselijke review.
De benchmark bewijst production readiness.
```

Allowed internal wording:

```text
De diagnostische benchmark helpt regressies zichtbaar te maken op een synthetische corpus.
De output ondersteunt engineeringbeslissingen, maar vervangt geen menselijke review.
```

Allowed user-facing caution if needed later:

```text
De benchmark is een hulpmiddel voor kwaliteitsbewaking; controleer het resultaat altijd handmatig.
```

---

## 10. Expected end state of this plan

After this plan:

```text
We know which metrics can be used later.
We know which gaps need attention first.
We have not accepted product thresholds.
We have not built a gate.
```
