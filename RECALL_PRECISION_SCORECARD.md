# Recall / Precision Scorecard — Dutch legal and care benchmark refresh

Status: refreshed after Dutch legal pattern fixes, gold-label corpus expansion, diagnostic runner/report artifact, artifact cleanup, cleaned artifact review, planning-only threshold design, PERSON-name coverage review, PERSON-name diagnostic tests, PERSON-name recognizer planning, PERSON-name recognizer contract tests and helper-level PERSON-name recognition implementation.  
Repository: `solidprivacy-nl/scrub`.  
Scope: benchmark/helper/tests/documentation. No product UI, export, Scrub Key or reinsert behavior is changed by this document.

---

## 1. Current evidence status

This scorecard records the current evidence after:

```text
WP_DUTCH_LEGAL_RECALL_GAP_TESTS
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY
WP_RECALL_SCORECARD_REFRESH
WP_RECALL_GOLD_LABEL_CORPUS_SEED
WP_RECALL_GOLD_LABEL_CORPUS_EXPAND
WP_RECALL_BENCHMARK_RUNNER_MINIMAL
WP_RECALL_BENCHMARK_REPORT_ARTIFACT
WP_RECALL_BENCHMARK_REPORT_REVIEW
WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX
WP_RECALL_BENCHMARK_REPORT_REVIEW_2
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN
WP_RECALL_PERSON_NAME_COVERAGE_REVIEW
WP_RECALL_PERSON_NAME_COVERAGE_TESTS
WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN
WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS
WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY
```

Current evidence:

- Diagnostic benchmark artifacts and reviews exist.
- Cleaned artifact output is substantially less noisy than the first artifact.
- Planning-only threshold policy exists.
- PERSON gaps are classified in `RECALL_PERSON_NAME_COVERAGE_REVIEW.md`.
- PERSON gap inventory is covered by diagnostic tests in `tests/test_recall_person_name_coverage_diagnostics.py`.
- PERSON-name recognition has a safe planning/specification document in `RECALL_PERSON_NAME_RECOGNIZER_PLAN.md`.
- Contract fixture and tests define future PERSON-name recognizer behavior.
- `person_name_recognizer_helper.py` now implements contract-backed, value-only role/title PERSON-name matching for helper-level use.
- `tests/test_recall_person_name_recognizer_implementation.py` validates the helper against contract-backed positive, negative, single-surname and candidate-only boundary cases.
- No app UI changes were made.
- No registered app recognizer changes were made in `dutch_recognizers.py`.
- No recognizer changes were made to the existing app-registered Dutch recognizer setup.
- No candidate scanner changes were made.
- No runner/report changes were made.
- No threshold enforcement exists.
- No production gate exists.
- No product claim is supported.

---

## 2. Current cleaned benchmark baseline

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

Remaining diagnostic gaps before helper implementation review:

```text
14 missed PERSON labels
3 missed MEDICAL_OR_CARE_REFERENCE care room/location labels
1 missed/wrong CLIENT_NUMBER
1 nested false-positive BSN-like hit inside a phone-like value
1 known-trap care-location review signal
```

The helper implementation targets only contract-backed role/title PERSON-name examples. It does not yet prove benchmark recall improvement in the artifact report.

---

## 3. PERSON-name helper implementation status

`WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY` completed helper/recognizer implementation + tests.

Implementation:

```text
person_name_recognizer_helper.py
```

Tests:

```text
tests/test_recall_person_name_recognizer_implementation.py
```

Implemented scope:

- contract-backed value-only role/title PERSON-name matching;
- strong-context single-surname handling for examples like `arts Bakker` and `Arts Jansen`;
- negative cases remain unmatched as PERSON-name values;
- candidate-only weak contexts remain not automatic.

Not changed:

```text
No UI/export/Scrub Key/reinsert change.
No registered app recognizer change in dutch_recognizers.py.
No candidate scanner change.
No runner/report change.
No threshold enforcement.
No production gate.
No product claim.
```

Recommended next:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_BENCHMARK_REVIEW
```

---

## 4. PERSON-name recognizer contract test status

`WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS` completed tests/specification-only.

The contract layer includes:

```text
tests/fixtures/person_name_recognizer_contract_cases.json
tests/test_recall_person_name_recognizer_contracts.py
PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md
```

The contract fixture and tests define future behavior for:

- positive future hard-recognizer cases;
- candidate-only weak-context cases;
- negative cases that must not become PERSON matches;
- single-surname policy;
- preserve-term policy;
- no product-claim/no threshold/no gate boundaries.

---

## 5. PERSON-name recognizer planning status

`WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN` completed planning/specification-only.

The plan records:

- safe recognition design principles;
- role/context preservation requirements;
- single-surname ambiguity policy;
- three possible recognition strategies;
- contract-test requirements before implementation;
- review-table/source-of-truth boundaries;
- product-claim boundaries.

---

## 6. Threshold planning status

`WP_RECALL_BENCHMARK_THRESHOLDS_PLAN` completed planning-only.

Status remains:

```text
No accepted production thresholds.
No CI gate.
No production blocking.
No threshold enforcement.
No product claim.
```

PERSON threshold impact:

- `PERSON` exact/text-normalized match should become high over time.
- With remaining PERSON misses, a hard PERSON threshold is still too early.
- Helper-level implementation must be followed by benchmark review before threshold reconsideration.

---

## 7. Current coverage status

| Area | Current state | Risk status |
|---|---|---|
| Dutch legal reference baseline | Present and normal assertions after pattern fix | Reduced for listed samples |
| Role-word preservation | Cleaned artifact shows 0 preserve-term hits | Diagnostically measurable, not production-proof |
| Care references | Remaining room/location gaps | Open coverage risk |
| Person names | Gaps classified, diagnostic tests added, plan added, contract tests added, helper implementation added | Partially mitigated for contract-backed role/title examples |
| Email | Benchmark-only email predictions now match email labels | Improved diagnostic runner behavior, not product recognizer proof |
| Address/IBAN/case reference mapping | Mapping cleanup effective | Improved diagnostic mapping |
| Client references | 1 missed/wrong client reference `CL-HUUR-2026-0009` | Open coverage risk |
| Diagnostic runner/report | Present and cleaned | Improves measurement, not trust claim |
| Threshold planning | Planning-only policy exists | No enforcement; risk remains open |
| Production safety claim | Not supported | Must remain blocked |

---

## 8. Open scorecard risks

Open risks:

- No formal accepted recall threshold exists.
- No formal accepted precision threshold exists.
- No production benchmark gate exists.
- Runner/report metrics remain diagnostic only.
- Helper-level recognition is not the same as production-readiness proof.
- Candidate rows require human review and are not automatically applied.
- Corpus coverage is expanded but still synthetic and not exhaustive.
- PERSON-name false-negative risk is only partially mitigated for contract-backed role/title cases.
- App-registered recognizer behavior and diagnostic report artifact impact still need review.
- DOCX metadata, comments, tracked changes, headers and footers remain separate document-hygiene risks.

Allowed wording:

```text
The PERSON-name helper implements contract-backed value-only role/title matching for synthetic examples.
Human review remains necessary.
```

Disallowed wording:

```text
Alle persoonsnamen worden altijd gevonden.
Alle persoonsgegevens worden altijd gevonden.
De app is veilig zonder menselijke review.
De benchmark bewijst production readiness.
```

---

## 9. Recommendation

Recommended next workpackage after green tests/HF sync/app smoke:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_BENCHMARK_REVIEW
```

Other backlog candidates:

```text
WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN
WP_CLIENT_REFERENCE_COVERAGE_REVIEW
WP_RECALL_BENCHMARK_THRESHOLDS_CONTRACT_TESTS
```

No follow-up package should start automatically.
