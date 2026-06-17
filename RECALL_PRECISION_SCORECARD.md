# Recall / Precision Scorecard — Dutch legal and care benchmark refresh

Status: refreshed after Dutch legal pattern fixes, gold-label corpus expansion, minimal diagnostic runner and diagnostic report artifact.  
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
```

Current evidence:

- Dutch legal recall gap tests exist and cover documented legal reference values and role-word preservation.
- The first pattern-fix round improved `candidate_scanner.py` only.
- Coordinator evidence confirmed GitHub Actions `Tests #1115`, `Sync to Hugging Face Space #1116` and live Hugging Face smoke check for the pattern-fix verify closeout.
- A synthetic gold-label corpus seed was added and then expanded.
- A minimal diagnostic benchmark runner exists.
- A diagnostic report artifact workflow now exists.
- The runner compares sidecars with recognizer/candidate-scanner output and reports exact, text-normalized and overlap diagnostics.
- Runner output can now be generated as JSON and Markdown and uploaded as a CI artifact.
- Quantitative recall/precision remains diagnostic only until thresholds and gates are separately planned and approved.

Important interpretation:

```text
Improved candidate surfacing != complete automatic recognizer guarantee.
Gold-label corpus + diagnostic runner + report artifact != production quality gate.
```

---

## 2. Corpus, runner and report inventory

Current corpus/report inventory:

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
Report artifact: diagnostic-recall-benchmark-report
```

Artifact files:

```text
output/recall_benchmark/recall_benchmark_report.json
output/recall_benchmark/recall_benchmark_summary.md
```

---

## 3. Runner and artifact status

The minimal diagnostic runner:

- loads all `.gold.json` sidecars under `corpus/`;
- validates source offsets for labels and preserve terms;
- collects predictions from Dutch recognizers and the candidate scanner when available;
- safely falls back to an empty diagnostic prediction set if optional analyzer dependencies are unavailable;
- compares labels and predictions using exact span, text-normalized and overlap diagnostic matching;
- reports missed required labels, wrong-type hits, false-positive candidates, preserve-term hits and known-trap hits;
- returns a JSON-serializable report with per-document and summary sections;
- does not start Streamlit;
- does not change product behavior;
- does not enforce thresholds or gates.

The diagnostic report helper:

- wraps runner output with diagnostic metadata;
- writes `recall_benchmark_report.json`;
- writes `recall_benchmark_summary.md`;
- validates schema/integrity in strict mode only;
- does not fail on low recall/precision;
- does not create a production gate.

Report command:

```bash
python recall_benchmark_report.py --corpus corpus --output output/recall_benchmark --strict
```

---

## 4. Dutch legal reference coverage

| Value/risk group | Coverage status | Evidence | Scorecard interpretation |
|---|---|---|---|
| `10598721 / UE VERZ 26-441` | baseline + gold sidecar + runner/report-readable | `test_rechtspraak_like_rolnummers_are_detectable`; `legal_reference_seed_001.gold.json` | Reduced known rolnummer gap; measurable by runner/artifact. |
| `ARN 26/4412` | baseline + gold sidecar + runner/report-readable | `test_rechtspraak_like_rolnummers_are_detectable`; `legal_reference_seed_001.gold.json` | Reduced Rechtspraak-like reference gap; measurable by runner/artifact. |
| `ZK-WOON-55091`, `ZK-ARBEID-2026-0007`, `ZK-HUUR-2026-8831` | baseline + expanded corpus + runner/report-readable | legal reference, false-positive and mixed identifier sidecars | Better measurable case-number coverage. |
| dossier references | baseline + expanded corpus + runner/report-readable | `DOS-2026-778899`, `DOS-ARBEID-2026-9911`, `DOS-HUUR-2026-1200` | Better measurable dossier-number coverage. |
| client references | baseline + expanded corpus + runner/report-readable | `CL-FAM-55201`, `CLNT-2026-0042`, `CL-HUUR-2026-0009` | Better measurable client-reference coverage. |
| claim references | baseline + expanded corpus + runner/report-readable | `CLM-2026-112233`, `CLM-2026-778899` | CLM/phone confusion can now be diagnosed across more than one sample. |
| ECLI values | expanded corpus + runner/report-readable | three synthetic ECLI values | Better measurable ECLI coverage. |
| legal false-positive traps | expanded corpus + runner/report-readable | articles, page, attachment, production, date, time, money amount | Better precision trap measurability. |

---

## 5. Role words / over-masking

The runner and report can now surface preserve-term hits when predictions overlap context terms such as:

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

Role/name combinations represented in the corpus include:

```text
arts Jansen
getuige Fatima El Amrani
de minderjarige Sami El Amrani
arts Bakker
verpleegkundige Sara El Idrissi
cliënt Youssef Ait Ben
mantelzorger Fatima Zahra
```

Risk update:

- Role-word over-masking is now diagnostically measurable and visible in a report artifact.
- Legal/care meaning must remain readable.
- Names next to role words should be detected as `PERSON`, while role words remain context.

---

## 6. Care coverage

The expanded care corpus, runner and report improve measurability for:

- care client numbers;
- zorgdossier references;
- MIC incident references;
- room and department context;
- medication/admin codes;
- device references;
- BIG-like numbers;
- care role words;
- care role/name combinations;
- person, phone and email direct identifiers.

---

## 7. Review/export regression boundaries

The runner/report workflow does not execute or change the app, review table, export, Scrub Key or reinsert behavior.

Existing boundary tests remain relevant:

```text
tests/test_review_table_collapsible_contract.py
tests/test_side_by_side_review_ui_patch.py
tests/test_side_by_side_review_consolidation_dutch_sample.py
```

Coverage summary:

- `replacement_editor` remains the review table source of truth and fallback.
- Download labels and export/download surfaces remain contract-tested.
- Side-by-side review remains report/visual only.
- No Scrub Key writes are introduced.
- No reinsert behavior change is introduced.
- Runner/report tests do not start Streamlit or export flows.

---

## 8. Open scorecard risks

Open risks:

- No formal recall threshold exists.
- No formal precision threshold exists.
- No production-blocking benchmark gate exists.
- Runner/report metrics are diagnostic only.
- Helper-level candidate surfacing is not the same as automatic recognition.
- Candidate rows require human review and are not automatically applied.
- Corpus coverage is expanded but still not exhaustive.
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

## 9. Recommendation

No immediate `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2` should start unless runner output or later app/user testing demonstrates concrete misses.

Recommended next options:

```text
WP_RECALL_BENCHMARK_REPORT_REVIEW — review first artifact output and decide whether corpus/runner/threshold planning needs adjustment.
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN — plan thresholds without enforcing them.
WP_RECALL_GOLD_LABEL_CORPUS_EXPAND — add more synthetic documents if coverage is thin.
WP_DOCX_HYGIENE_RECALL_FOLLOWUP — if document/export risks now dominate.
```

Most useful next benchmark step:

```text
Review the first diagnostic artifact before planning thresholds or gates.
```

---

## 10. Current scorecard status

| Area | Current state | Risk status |
|---|---|---|
| Dutch legal reference baseline | Present and normal assertions after pattern fix | Reduced for listed samples |
| CLM / phone confusion | Baseline assertion plus multiple gold sidecar labels | Reduced for documented samples |
| Role-word preservation | Baseline assertions plus legal/care preserve terms | Diagnostically measurable and report-visible |
| Over-masking role structure | Baseline assertion and expanded role seeds | Diagnostically measurable and report-visible |
| Legal false-positive traps | Expanded corpus includes legal articles, dates, times, money, page/attachment labels | Diagnostically measurable and report-visible |
| Care references | Expanded corpus includes client, dossier, incident, BIG-like, room/department, medication and device examples | Diagnostically measurable and report-visible |
| Review/export regression | Covered by existing contract tests | Guarded, CI remains source of truth |
| Gold-label corpus sidecars | 7 synthetic sidecars present | Improved measurability |
| Diagnostic runner | Present | Improves measurement, not trust claim |
| Diagnostic report artifact | Present | Improves evidence visibility, not trust claim |
| Quantitative recall | Diagnostic only until thresholds exist | Open |
| Quantitative precision | Diagnostic only until thresholds exist | Open |
| Production safety claim | Not supported | Must remain blocked |
