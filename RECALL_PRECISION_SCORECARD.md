# Recall / Precision Scorecard — Dutch legal and care benchmark refresh

Status: refreshed after Dutch legal pattern fixes, gold-label corpus expansion, minimal diagnostic runner, diagnostic report artifact, first artifact review and report artifact cleanup.  
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
```

Current evidence:

- Dutch legal recall gap tests exist and cover documented legal reference values and role-word preservation.
- The first pattern-fix round improved `candidate_scanner.py` only.
- A synthetic gold-label corpus seed was added and then expanded.
- A minimal diagnostic benchmark runner exists.
- A diagnostic report artifact workflow exists and was coordinator-verified green.
- The first diagnostic report artifact output was reviewed in `RECALL_BENCHMARK_REPORT_REVIEW.md`.
- Diagnostic artifact mapping/counting cleanup is now implemented.
- Quantitative recall/precision remains diagnostic only until thresholds and gates are separately planned and approved.

Important interpretation:

```text
Improved candidate surfacing != complete automatic recognizer guarantee.
Gold-label corpus + diagnostic runner + report artifact + cleanup != production quality gate.
```

---

## 2. Corpus, runner, report and cleanup inventory

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
Report cleanup docs: RECALL_BENCHMARK_REPORT_ARTIFACT_FIX.md
Report artifact: diagnostic-recall-benchmark-report
```

---

## 3. First artifact review summary

The first reviewed artifact had valid metadata and structure:

```text
metadata.status = diagnostic_only
metadata.synthetic_corpus = true
metadata.production_gate = false
metadata.thresholds_enforced = false
document_count = 7
gold_label_count = 75
```

Raw values from the first reviewed artifact:

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

Diagnostic interpretation from the review:

- The artifact is useful for engineering review.
- Raw counts were not suitable for threshold planning yet.
- Several missed/wrong-type findings appeared to be caused by runner mapping, acceptable-entity taxonomy or duplicate prediction reporting.
- The artifact does not support any production accuracy claim.

---

## 4. Diagnostic cleanup completed

Cleanup completed in `WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX`:

### Mapping cleanup

The diagnostic runner now maps/accepts:

```text
NL_ADDRESS -> ADDRESS
NL_IBAN -> IBAN
NL_CASE_REFERENCE -> CASE_NUMBER
NL_LEGAL_PARTY_NAME -> PERSON
EMAIL_ADDRESS -> EMAIL
```

This is benchmark/report mapping only and does not change product recognition behavior.

### Care taxonomy cleanup

Selected care sidecars now accept benchmark-compatible implementation outputs:

```text
ZORG-CL-* care references -> NL_CLIENT_REFERENCE accepted where appropriate
care department/location references -> NL_ADDRESS accepted where appropriate
care role/person labels -> NL_LEGAL_PARTY_NAME accepted as person-name output where appropriate
```

This is benchmark taxonomy cleanup only. Spans and source text are unchanged.

### Dedup/counting cleanup

The runner now deduplicates predictions for diagnostic accounting using:

```text
text
entity_type
start
end
source
```

Deduplication applies before document comparison and to wrong-type, preserve-term, known-trap and false-positive accounting.

### Email behavior

The runner now adds benchmark-only `EMAIL_ADDRESS` predictions for synthetic email fixtures. These predictions use source:

```text
benchmark_builtin
```

This is not a product recognizer and does not change app behavior.

---

## 5. Current coverage status

| Area | Current state | Risk status |
|---|---|---|
| Dutch legal reference baseline | Present and normal assertions after pattern fix | Reduced for listed samples |
| CLM / phone confusion | Baseline assertion plus multiple gold sidecar labels | Reduced for documented samples |
| Role-word preservation | Baseline assertions plus legal/care preserve terms; first artifact showed 0 preserve-term hits | Diagnostically measurable, not production-proof |
| Over-masking role structure | Baseline assertion and expanded role seeds | Diagnostically measurable, not production-proof |
| Legal false-positive traps | Expanded corpus includes legal articles, dates, times, money, page/attachment labels | Diagnostically measurable |
| Care references | Expanded corpus includes client, dossier, incident, BIG-like, room/department, medication and device examples | Measurable; taxonomy cleanup added |
| Person names | `NL_LEGAL_PARTY_NAME` now maps to `PERSON` in benchmark | Improved diagnostic mapping, not product claim |
| Email | Benchmark-only email predictions added | Improved diagnostic runner behavior, not product recognizer |
| Address/IBAN/case reference mapping | Mapping cleanup added | Improved diagnostic mapping |
| Diagnostic runner | Present and cleaned | Improves measurement, not trust claim |
| Diagnostic report artifact | Present and reviewed | Improves evidence visibility, not trust claim |
| Quantitative recall | Diagnostic only until thresholds exist | Open |
| Quantitative precision | Diagnostic only until thresholds exist | Open |
| Production safety claim | Not supported | Must remain blocked |

---

## 6. Review/export regression boundaries

The runner/report cleanup does not execute or change the app, review table, export, Scrub Key or reinsert behavior.

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
- Runner/report metrics remain diagnostic only.
- Helper-level candidate surfacing is not the same as automatic recognition.
- Candidate rows require human review and are not automatically applied.
- Corpus coverage is expanded but still not exhaustive.
- A cleaned artifact still needs to be generated and reviewed before threshold planning.
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

Recommended next workpackage after separate approval:

```text
WP_RECALL_BENCHMARK_REPORT_REVIEW_2
```

Purpose:

- review the cleaned artifact output;
- confirm whether mapping/dedup/taxonomy cleanup reduced noise;
- decide whether threshold planning is now reasonable.

Only after a cleaned artifact review should `WP_RECALL_BENCHMARK_THRESHOLDS_PLAN` be considered.
