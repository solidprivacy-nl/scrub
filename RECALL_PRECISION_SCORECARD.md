# Recall / Precision Scorecard — Dutch legal and care benchmark refresh

Status: refreshed after Dutch legal pattern fixes, gold-label corpus expansion, minimal diagnostic runner, diagnostic report artifact and first artifact review.  
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
```

Current evidence:

- Dutch legal recall gap tests exist and cover documented legal reference values and role-word preservation.
- The first pattern-fix round improved `candidate_scanner.py` only.
- A synthetic gold-label corpus seed was added and then expanded.
- A minimal diagnostic benchmark runner exists.
- A diagnostic report artifact workflow exists and was coordinator-verified green.
- The first diagnostic report artifact output has now been reviewed in `RECALL_BENCHMARK_REPORT_REVIEW.md`.
- The artifact is structurally valid and contains diagnostic JSON and Markdown outputs.
- Quantitative recall/precision remains diagnostic only until thresholds and gates are separately planned and approved.

Important interpretation:

```text
Improved candidate surfacing != complete automatic recognizer guarantee.
Gold-label corpus + diagnostic runner + report artifact + review != production quality gate.
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
Report review: RECALL_BENCHMARK_REPORT_REVIEW.md
Report artifact: diagnostic-recall-benchmark-report
```

Artifact files reviewed:

```text
recall_benchmark_report.json
recall_benchmark_summary.md
```

---

## 3. First artifact review summary

Artifact integrity passed:

```text
metadata.status = diagnostic_only
metadata.synthetic_corpus = true
metadata.production_gate = false
metadata.thresholds_enforced = false
report.summary exists
report.documents exists
document_count = 7
gold_label_count = 75
```

Summary values from the reviewed artifact:

| Metric | Value |
|---|---:|
| document_count | 7 |
| gold_label_count | 75 |
| prediction_count | 61 |
| required_label_count | 75 |
| matched_required_exact_count | 41 |
| matched_required_text_normalized_count | 41 |
| matched_required_overlap_count | 41 |
| missed_required_count | 34 |
| wrong_type_count | 11 |
| false_positive_candidate_count | 8 |
| preserve_term_hit_count | 0 |
| known_trap_hit_count | 1 |

Diagnostic interpretation:

- The artifact is useful for engineering review.
- The current raw counts are not yet suitable for threshold planning.
- Several missed/wrong-type findings appear to be caused by runner mapping, acceptable-entity taxonomy or duplicate prediction reporting.
- The artifact does not support any production accuracy claim.

---

## 4. Main artifact review findings

### 4.1 Positive findings

- Artifact metadata correctly blocks production-gate interpretation.
- Corpus and report structure are present.
- 41 required labels are matched exactly/text-normalized/overlap in the current diagnostic report.
- `preserve_term_hit_count = 0`, so the reviewed artifact did not show direct role/context-term over-masking.
- Legal/care references are now measurable and visible in a CI artifact.

### 4.2 Diagnostic concerns

- `missed_required_count = 34`.
- `wrong_type_count = 11`.
- `false_positive_candidate_count = 8`.
- `known_trap_hit_count = 1`.

Main likely causes:

- runner mapping does not accept `NL_ADDRESS` as address/location;
- runner mapping does not accept `NL_IBAN` as IBAN;
- runner mapping does not accept `NL_CASE_REFERENCE` as case number;
- `NL_LEGAL_PARTY_NAME` may need a benchmark decision for person-name matching;
- care `ZORG-CL-*` references are detected as `NL_CLIENT_REFERENCE` but gold labels expect care-reference classes;
- repeated predictions inflate wrong-type and false-positive counts;
- email labels are missed in the reviewed artifact and need investigation.

---

## 5. Dutch legal and care coverage status

| Area | Current state | Risk status |
|---|---|---|
| Dutch legal reference baseline | Present and normal assertions after pattern fix | Reduced for listed samples |
| CLM / phone confusion | Baseline assertion plus multiple gold sidecar labels | Reduced for documented samples |
| Role-word preservation | Baseline assertions plus legal/care preserve terms; artifact showed 0 preserve-term hits | Diagnostically measurable, not production-proof |
| Over-masking role structure | Baseline assertion and expanded role seeds | Diagnostically measurable, not production-proof |
| Legal false-positive traps | Expanded corpus includes legal articles, dates, times, money, page/attachment labels | Diagnostically measurable |
| Care references | Expanded corpus includes client, dossier, incident, BIG-like, room/department, medication and device examples | Measurable, but taxonomy/mapping needs cleanup |
| Person names | Many missed in artifact | Open recognizer/mapping risk |
| Email | Missed in artifact | Open runner/coverage risk |
| Address/IBAN/case reference mapping | Detected values currently reported as wrong/missed in some cases | Open runner mapping risk |
| Diagnostic runner | Present | Improves measurement, not trust claim |
| Diagnostic report artifact | Present and reviewed | Improves evidence visibility, not trust claim |
| Quantitative recall | Diagnostic only until thresholds exist | Open |
| Quantitative precision | Diagnostic only until thresholds exist | Open |
| Production safety claim | Not supported | Must remain blocked |

---

## 6. Review/export regression boundaries

The runner/report workflow and artifact review do not execute or change the app, review table, export, Scrub Key or reinsert behavior.

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

- No formal recall threshold exists.
- No formal precision threshold exists.
- No production-blocking benchmark gate exists.
- Runner/report metrics are diagnostic only.
- Helper-level candidate surfacing is not the same as automatic recognition.
- Candidate rows require human review and are not automatically applied.
- Corpus coverage is expanded but still not exhaustive.
- First artifact review shows raw metrics are noisy because of mapping/taxonomy/deduplication issues.
- DOCX metadata, comments, tracked changes, headers and footers remain separate document-hygiene risks.
- The app must not claim: `alle juridische nummers worden altijd herkend`.

Allowed wording:

```text
De diagnostische runner vergelijkt huidige analyzer/helper-output met de synthetische gold-label corpus en maakt dat zichtbaar als CI-artifact.
```

Disallowed wording:

```text
Alle juridische nummers worden altijd herkend.
```

---

## 8. Recommendation

Do not start threshold planning yet.

The reviewed artifact is structurally valid and useful, but its current raw counts are too noisy for threshold planning because several findings likely come from runner mapping, benchmark taxonomy or duplicate prediction accounting.

Recommended next workpackage after separate approval:

```text
WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX
```

Suggested scope:

- review/repair runner mapping for `NL_ADDRESS`, `NL_IBAN`, `NL_CASE_REFERENCE`, and possibly `NL_LEGAL_PARTY_NAME`;
- dedupe repeated predictions before wrong-type/false-positive reporting;
- clarify care-reference acceptable types for `ZORG-CL-*` values;
- investigate absent `EMAIL_ADDRESS` predictions;
- keep the report diagnostic only;
- do not add product UI, recognizer/pattern product changes, thresholds or gates.

Only after that should `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN` be considered.
