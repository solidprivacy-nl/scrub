# Recall / Precision Scorecard — Dutch legal and care benchmark refresh

Status: refreshed after Dutch legal pattern fixes, gold-label corpus expansion, diagnostic runner/report artifact, artifact cleanup, cleaned artifact review, planning-only threshold design and PERSON-name coverage review.  
Repository: `solidprivacy-nl/scrub`.  
Scope: benchmark/documentation-only. No product UI, export, Scrub Key or reinsert behavior is changed by this document.

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
```

Current evidence:

- Diagnostic benchmark artifacts and reviews exist.
- Cleaned artifact output is substantially less noisy than the first artifact.
- Planning-only threshold policy exists.
- PERSON gaps are now classified in `RECALL_PERSON_NAME_COVERAGE_REVIEW.md`.
- No recognizer changes were made.
- No thresholds are enforced.
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

## 3. PERSON-name coverage review status

`WP_RECALL_PERSON_NAME_COVERAGE_REVIEW` completed review/planning-only.

Findings:

- The 14 remaining missed `PERSON` labels are classified.
- Common gap categories include Arabic/Moroccan-style multi-token names, Dutch names with tussenvoegsels, names after care/legal roles, names after professional titles and single surnames.
- The issue now looks mostly like recognizer coverage and candidate-design work, not benchmark mapping noise.
- Single-surname cases such as `Bakker` and `Jansen` require careful design because broad matching could over-mask normal words.

No changes:

```text
No recognizer changes.
No candidate scanner changes.
No runner/report changes.
No thresholds enforced.
No production gate.
No product claim.
```

---

## 4. Threshold planning status

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
- With 14 remaining misses, a hard PERSON threshold is too early.
- Coverage tests should come before recognizer/candidate planning.

---

## 5. Current coverage status

| Area | Current state | Risk status |
|---|---|---|
| Dutch legal reference baseline | Present and normal assertions after pattern fix | Reduced for listed samples |
| Role-word preservation | Cleaned artifact shows 0 preserve-term hits | Diagnostically measurable, not production-proof |
| Care references | Remaining room/location gaps | Open coverage risk |
| Person names | 14 missed labels classified | Open direct-identifier risk |
| Email | Benchmark-only email predictions now match email labels | Improved diagnostic runner behavior, not product recognizer proof |
| Address/IBAN/case reference mapping | Mapping cleanup effective | Improved diagnostic mapping |
| Client references | 1 missed/wrong client reference `CL-HUUR-2026-0009` | Open coverage risk |
| Diagnostic runner/report | Present and cleaned | Improves measurement, not trust claim |
| Threshold planning | Planning-only policy exists | No enforcement; risk remains open |
| Production safety claim | Not supported | Must remain blocked |

---

## 6. Open scorecard risks

Open risks:

- No formal accepted recall threshold exists.
- No formal accepted precision threshold exists.
- No production benchmark gate exists.
- Runner/report metrics remain diagnostic only.
- Helper-level candidate surfacing is not the same as automatic recognition.
- Candidate rows require human review and are not automatically applied.
- Corpus coverage is expanded but still synthetic and not exhaustive.
- PERSON-name false-negative risk is analyzed but not fixed.
- DOCX metadata, comments, tracked changes, headers and footers remain separate document-hygiene risks.

Allowed wording:

```text
De diagnostische benchmark laat zien welke synthetische persoonsnamen nog gemist worden.
Deze analyse helpt vervolgtests en herkenningslogica te plannen.
Menselijke review blijft noodzakelijk.
```

Disallowed wording:

```text
Alle persoonsnamen worden altijd gevonden.
Alle persoonsgegevens worden altijd gevonden.
De app is veilig zonder menselijke review.
De benchmark bewijst production readiness.
```

---

## 7. Recommendation

Recommended next workpackage after separate approval:

```text
WP_RECALL_PERSON_NAME_COVERAGE_TESTS
```

Alternative next package if design should come first:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN
```

Other backlog candidates:

```text
WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN
WP_CLIENT_REFERENCE_COVERAGE_REVIEW
WP_RECALL_BENCHMARK_THRESHOLDS_CONTRACT_TESTS
```

No follow-up package should start automatically.
