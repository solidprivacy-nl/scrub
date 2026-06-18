# Recall / Precision Scorecard — Dutch legal and care benchmark refresh

Status: refreshed after Dutch legal pattern fixes, gold-label corpus expansion, diagnostic runner/report artifact, artifact cleanup, cleaned artifact review, planning-only threshold design, PERSON-name coverage review, PERSON-name diagnostic tests, PERSON-name recognizer planning and PERSON-name recognizer contract tests.  
Repository: `solidprivacy-nl/scrub`.  
Scope: benchmark/tests/documentation-only. No product UI, export, Scrub Key or reinsert behavior is changed by this document.

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
```

Current evidence:

- Diagnostic benchmark artifacts and reviews exist.
- Cleaned artifact output is substantially less noisy than the first artifact.
- Planning-only threshold policy exists.
- PERSON gaps are classified in `RECALL_PERSON_NAME_COVERAGE_REVIEW.md`.
- PERSON gap inventory is covered by diagnostic tests in `tests/test_recall_person_name_coverage_diagnostics.py`.
- PERSON-name recognition has a safe planning/specification document in `RECALL_PERSON_NAME_RECOGNIZER_PLAN.md`.
- Contract fixture and tests now define future PERSON-name recognizer behavior.
- No recognizer implementation was added.
- No candidate scanner implementation was added.
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

Remaining diagnostic gaps:

```text
14 missed PERSON labels
3 missed MEDICAL_OR_CARE_REFERENCE care room/location labels
1 missed/wrong CLIENT_NUMBER
1 nested false-positive BSN-like hit inside a phone-like value
1 known-trap care-location review signal
```

---

## 3. PERSON-name recognizer contract test status

`WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS` completed tests/specification-only.

The new contract layer includes:

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

No changes:

```text
No recognizer implementation.
No candidate scanner implementation.
No runner/report changes.
No threshold enforcement.
No production gate.
No product claim.
```

Recommended next:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY
```

---

## 4. PERSON-name recognizer planning status

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

## 5. PERSON-name coverage diagnostics status

`WP_RECALL_PERSON_NAME_COVERAGE_TESTS` completed tests/documentation-only.

Diagnostic tests cover:

- the PERSON gap inventory;
- the underlying synthetic corpus/source grounding;
- PERSON gold sidecar label expectations;
- context category examples;
- non-claim boundaries;
- no enforcement/gate boundary for PERSON coverage.

The tests do not require current recognizers to pass all PERSON examples. They keep the known risk visible for future planning.

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
- With remaining PERSON misses, a hard PERSON threshold is too early.
- Coverage tests, recognizer planning and contract tests now exist.
- Helper-only implementation should come before any threshold reconsideration.

---

## 7. Current coverage status

| Area | Current state | Risk status |
|---|---|---|
| Dutch legal reference baseline | Present and normal assertions after pattern fix | Reduced for listed samples |
| Role-word preservation | Cleaned artifact shows 0 preserve-term hits | Diagnostically measurable, not production-proof |
| Care references | Remaining room/location gaps | Open coverage risk |
| Person names | Gaps classified, diagnostic tests added, plan added, contract tests added | Open direct-identifier risk |
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
- Helper-level candidate surfacing is not the same as automatic recognition.
- Candidate rows require human review and are not automatically applied.
- Corpus coverage is expanded but still synthetic and not exhaustive.
- PERSON-name false-negative risk now has diagnostic and contract test coverage, but no implementation.
- DOCX metadata, comments, tracked changes, headers and footers remain separate document-hygiene risks.

Allowed wording:

```text
The PERSON-name recognizer contracts define future safe behavior for synthetic examples.
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

Recommended next workpackage after separate approval:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY
```

Then consider:

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
