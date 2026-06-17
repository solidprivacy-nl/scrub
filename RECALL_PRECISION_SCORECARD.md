# Recall / Precision Scorecard — Dutch legal and care benchmark refresh

Status: refreshed after Dutch legal pattern fixes, gold-label corpus expansion, diagnostic runner/report artifact, artifact cleanup, cleaned artifact review and planning-only threshold design.  
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
```

Current evidence:

- Dutch legal recall gap tests exist and cover documented legal reference values and role-word preservation.
- The first pattern-fix round improved `candidate_scanner.py` only.
- A synthetic gold-label corpus seed was added and then expanded.
- A minimal diagnostic benchmark runner exists.
- A diagnostic report artifact workflow exists and was coordinator-verified green.
- The first diagnostic report artifact output was reviewed.
- Diagnostic artifact mapping/counting cleanup was implemented.
- The cleaned diagnostic artifact output was reviewed.
- `RECALL_BENCHMARK_THRESHOLDS_PLAN.md` now defines a planning-only threshold policy direction.
- No thresholds are enforced.
- No production gate exists.
- No product claim is supported.

Important interpretation:

```text
Improved candidate surfacing != complete automatic recognizer guarantee.
Gold-label corpus + diagnostic runner + report artifact + cleanup + threshold plan != production quality gate.
```

---

## 2. Corpus, runner, report and review inventory

```text
Legal documents: 4
Care documents: 3
Gold sidecars: 7
Validator: tests/test_recall_gold_label_corpus_seed.py
Runner: recall_benchmark_runner.py
Runner tests: tests/test_recall_benchmark_runner_minimal.py
Runner docs: RECALL_BENCHMARK_RUNNER_MINIMAL.md
Report helper: recall_benchmark_report.py
Report tests: tests/test_recall_benchmark_report_artifact.py
Report workflow: .github/workflows/recall-benchmark-report.yml
Report docs: RECALL_BENCHMARK_REPORT_ARTIFACT.md
First report review: RECALL_BENCHMARK_REPORT_REVIEW.md
Report cleanup docs: RECALL_BENCHMARK_REPORT_ARTIFACT_FIX.md
Cleaned report review: RECALL_BENCHMARK_REPORT_REVIEW_2.md
Threshold plan: RECALL_BENCHMARK_THRESHOLDS_PLAN.md
Report artifact: diagnostic-recall-benchmark-report
```

---

## 3. Artifact review progression

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

- Mapping/counting cleanup materially improved benchmark signal quality.
- The cleaned artifact is structurally valid and substantially less noisy.
- Remaining misses now look more like real coverage/taxonomy/product-risk questions than report-accounting bugs.
- Planning-only threshold design is now documented.
- No accepted thresholds or gates exist yet.

---

## 4. Threshold planning status

`WP_RECALL_BENCHMARK_THRESHOLDS_PLAN` completed planning-only.

Status:

```text
No thresholds enforced.
No production gate created.
No release blocking added.
No product safety claim added.
Cleaned artifact supports planning-only threshold design.
```

The plan defines:

- metric meanings;
- hard versus soft diagnostic interpretation;
- planning baseline, warning threshold, release review threshold and future blocking threshold categories;
- class-specific planning for person names, legal references, care references, client numbers, email, phone, IBAN, BSN, address/location, preserve terms and known traps;
- mandatory conditions before any future gate.

A future blocking gate is explicitly not allowed until a separate approved workpackage.

---

## 5. Current coverage status

| Area | Current state | Risk status |
|---|---|---|
| Dutch legal reference baseline | Present and normal assertions after pattern fix | Reduced for listed samples |
| CLM / phone confusion | Baseline assertion plus multiple gold sidecar labels | Reduced for documented samples |
| Role-word preservation | Cleaned artifact shows 0 preserve-term hits | Diagnostically measurable, not production-proof |
| Over-masking role structure | Baseline assertion and expanded role seeds | Diagnostically measurable, not production-proof |
| Legal false-positive traps | Expanded corpus includes legal articles, dates, times, money, page/attachment labels | Diagnostically measurable |
| Care references | Expanded corpus includes client, dossier, incident, BIG-like, room/department, medication and device examples | Measurable; remaining room/location gaps |
| Person names | 14 remaining missed person labels in cleaned artifact | Open recognizer/corpus coverage risk |
| Email | Benchmark-only email predictions now match email labels | Improved diagnostic runner behavior, not product recognizer |
| Address/IBAN/case reference mapping | Mapping cleanup effective | Improved diagnostic mapping |
| Client references | 1 remaining missed/wrong client reference `CL-HUUR-2026-0009` | Open coverage risk |
| Diagnostic runner | Present and cleaned | Improves measurement, not trust claim |
| Diagnostic report artifact | Present and reviewed twice | Improves evidence visibility, not trust claim |
| Threshold planning | Planning-only policy exists | No enforcement; risk remains open |
| Quantitative recall | Planning-only thresholds possible later | Open |
| Quantitative precision | Planning-only thresholds possible later | Open |
| Production safety claim | Not supported | Must remain blocked |

---

## 6. Review/export regression boundaries

The runner/report cleanup, artifact reviews and threshold planning do not execute or change the app, review table, export, Scrub Key or reinsert behavior.

Existing boundary tests remain relevant:

```text
tests/test_review_table_collapsible_contract.py
tests/test_side_by_side_review_ui_patch.py
tests/test_side_by_side_review_consolidation_dutch_sample.py
```

Boundaries still preserved:

- `replacement_editor` remains the review table source of truth and fallback;
- download labels and export/download surfaces remain contract-tested;
- side-by-side review remains report/visual only;
- no Scrub Key writes are introduced;
- no reinsert behavior change is introduced;
- runner/report tests do not start Streamlit or export flows.

---

## 7. Open scorecard risks

Open risks:

- No formal accepted recall threshold exists.
- No formal accepted precision threshold exists.
- No production-blocking benchmark gate exists.
- Runner/report metrics remain diagnostic only.
- Helper-level candidate surfacing is not the same as automatic recognition.
- Candidate rows require human review and are not automatically applied.
- Corpus coverage is expanded but still not exhaustive.
- Remaining misses are concentrated in person names, care room/location references and one client-number example.
- DOCX metadata, comments, tracked changes, headers and footers remain separate document-hygiene risks.
- The app must not claim: `alle juridische nummers worden altijd herkend`.

Allowed wording:

```text
De diagnostische benchmark helpt regressies zichtbaar te maken op een synthetische corpus.
De output ondersteunt engineeringbeslissingen, maar vervangt geen menselijke review.
```

Disallowed wording:

```text
Alle persoonsgegevens worden altijd gevonden.
Alle juridische nummers worden altijd herkend.
De app is veilig voor productie zonder menselijke review.
De benchmark bewijst production readiness.
```

---

## 8. Recommendation

Recommended next workpackage after separate approval:

```text
WP_RECALL_PERSON_NAME_COVERAGE_REVIEW
```

Alternative next packages depending on coordinator priority:

```text
WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN
WP_CLIENT_REFERENCE_COVERAGE_REVIEW
WP_RECALL_BENCHMARK_THRESHOLDS_CONTRACT_TESTS
```

No follow-up package should start automatically.

A future gate path may be planned later, but only as a separate planning package first:

```text
WP_RECALL_BENCHMARK_GATE_PLAN
```

`WP_RECALL_BENCHMARK_GATE_PLAN` is still planning, not gate implementation.
