# SolidPrivacy Scrub — Repository Convergence Debt Ledger

> **TEMPORARY EXECUTION ARTIFACT — NON-AUTHORITATIVE AFTER CONVERGENCE**
>
> This ledger supports Stage 1 execution. It is not a permanent source of product truth. Accepted decisions belong in `DECISION_LOG.md`, current risks in `RISK_REGISTER.md`, current execution in `WORKPACKAGES.md`, and implementation history in `CHANGELOG.md`.

Date: 2026-09-05  
Repository: `solidprivacy-nl/scrub`  
Pre-convergence baseline: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Accepted bootstrap main: `255cd619d5cf6eab32f9383940eaa4af362cb68c`

## Classification model

- `CANONICAL` — supported current behavior; retain, test and document accurately.
- `RECONCILE` — valid responsibility whose active implementation, test, configuration or authority needs current-truth alignment.
- `RETIRE` — superseded, dead, contradictory or unnecessarily active path; remove only after evidence shows it is safe.
- `VARIANT-SPECIFIC` — potentially valid functionality whose requirements conflict with Scrub Private; preserve recoverability through Git but exclude from the Private line unless explicitly re-approved.

Classification applies to capabilities/contracts/runtime paths, not mechanically to whole files.

## Bootstrap debt already resolved

PR #114 received fresh blind PASS and merged as `255cd619d5cf6eab32f9383940eaa4af362cb68c` with green exact-main Tests and GitHub→Hugging Face sync.

The following are **not current cleanup tasks anymore**:

- `PROJECT_PROMPT.md` and `AGENTS.md` now route through Repository Convergence → Scrub Private;
- `ROADMAP.md` now contains the five strategic stages only;
- `WORKPACKAGES.md` contains one current executable queue;
- root `CHANGELOG.md` is post-reset history and the pre-convergence changelog is preserved byte-identically under `history/`;
- D044 records the accepted convergence/private direction;
- `RISK_REGISTER.md` carries current critical risks plus source-of-truth/runtime-mutation risk;
- Hugging Face is bounded to synthetic/approved application validation;
- Local/offline installer work is deferred variant-specific history, not an active delivery line.

Do not reopen these items without fresh evidence of a current defect.

## Current capability/path ledger

| Capability / path | Current role / evidence | Classification | Current target / smallest next action |
|---|---|---|---|
| Premium staged workspace and generation-bound state | Current app implements `Anonimiseren | Terugzetten`, `Standaard | Expert`, staged `Toevoegen → Controleren → Downloaden`, shared authoritative state and fail-closed export eligibility. | `CANONICAL` | Preserve; do not rebuild from historical workpackages. |
| Human review authority and direct/manual correction | Review/include state remains authoritative; direct and manual missed-value paths feed normal review/export authority. | `CANONICAL` | Preserve mandatory human review. |
| Scrub Key binding and reinsert | Bound placeholders, schema-1.1 keys, mapping digest, document binding and fail-closed mismatch handling are covered by dedicated tests. | `CANONICAL` | Preserve; redesign only for a proven defect. |
| Legal / Dutch recognition | Deterministic recognizers plus generic NER and Legal profile are current, with address-span repair on accepted main. | `CANONICAL` | Preserve and validate through current evidence paths. |
| Zorg policy and recognizers | Dedicated Zorg policy/recognizers, synthetic corpus, gap triage and cross-profile evidence are integrated. | `CANONICAL` | Preserve clinical meaning and human review. |
| TXT/DOCX/text-PDF handling and DOCX hygiene/fidelity | Supported import/export/reinsert/hygiene behavior exists with explicit PDF and unsupported-content boundaries. | `CANONICAL` | Preserve; no OCR/restored-PDF expansion during convergence. |
| Recognizer-backed recall benchmark (`recall_benchmark_runner.py`, `recall_benchmark_report.py`, corpus workflow) | Executes the actual recognition stack against synthetic/gold material and produces diagnostic JSON/Markdown. | `CANONICAL` candidate | Confirm its release role in the validation-hierarchy package. |
| Phase-6 synthetic E2E validation | Exercises TXT/DOCX/PDF workflow, manual additions, Scrub Key, export/reinsert and known limitations. | `CANONICAL` | Keep as workflow-level evidence complementary to recognizer benchmarks. |
| Older entity-scorecard / residual-risk builders | Useful supplied-prediction/report-only diagnostics with explicit coverage limitations. | `RECONCILE` | Classify as supplemental or historical; **no new framework** and no arbitrary production threshold. |
| Persistent replacement memory (`replacement_memory.py` + Expert UI) | Deliberately persists original/replacement/entity values when persistent storage exists. | `VARIANT-SPECIFIC` | Preserve shared-baseline recoverability; remove/exclude from Scrub Private only in Stage 2. |
| Azure AI Language document recognition | Current optional Expert path can send document content to Azure AI Language. | `VARIANT-SPECIFIC` | Exclude from Scrub Private in Stage 2; do not build a proxy/broker. |
| OpenAI/Azure OpenAI synthesis operator | Current optional Expert path can send document-bearing prompts to an external provider. | `VARIANT-SPECIFIC` | Exclude from Scrub Private in Stage 2 unless explicitly re-approved. |
| Content-bearing prompt print in `create_fake_data()` | Synthesis helper prints a content-bearing prompt. | `RECONCILE` / Private blocker | Remove with Private external-synthesis cleanup; add a narrow no-content-log contract, not a logging framework. |
| Legacy startup patch script invocation in Dockerfile | Pre-WP finding: accepted main `255cd619…` invokes `fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py`, although current direct-source markers make both exit without mutation. PR #116 candidate removes only those runtime invocations and starts Streamlit directly with existing server flags unchanged. | `RECONCILE — RESOLVED IN PR #116 CANDIDATE` | Require full exact-head regression + fresh independent PASS. Do not reintroduce runtime source mutation. |
| `fix_streamlit_nested_expanders.py` historical mutation implementation | Historical compatibility code remains in repository and exits immediately on current Premium source. | `RETIRE` candidate | **Still unresolved after PR #116.** Decide later whether diagnostic/history value justifies keeping it; do not mass-delete tests blindly. |
| `fix_streamlit_pdf_text_reinsert.py` historical mutation implementation | Historical compatibility code remains in repository and exits immediately on current direct-source reinsert marker. | `RETIRE` candidate | **Still unresolved after PR #116.** Treat separately from runtime invocation retirement. |
| Docker/runtime production hardening | Python 3.10 base/build tools and permissive Streamlit XSRF/CORS settings remain. PR #116 does not change these. | `RECONCILE` / later service work | Defer major hardening to Private Service unless a current safety defect is proven. |
| `openai` and `azure-ai-textanalytics` dependencies | Used only by current variant-specific external-processing paths. | `RECONCILE` | Remove when those Private-incompatible paths are removed; do not leave unused dependencies. |
| Open GitHub issues from Premium/governance repair cycles | Several describe candidate states already PASSed/merged; parent #105/#96 still lack proven final consolidated deployed retest. | `RECONCILE` | Reconstruct against current main; close stale cycles only with evidence and preserve unperformed live gate. |
| HF workflow path-ignore churn | Governance-only bootstrap changes triggered an otherwise unnecessary but successful HF sync because some convergence/history paths are not ignored. | `RECONCILE` / low operational priority | Consider only if repeated churn creates real operational cost; do not mix with product/runtime packages. |

## Current issue-reconciliation notes

These notes are findings, not closure authority:

- #112: PR #111 independently PASSed and merged; exact-main Tests/HF sync were green. Open issue state is stale.
- #109: PR #108 independently PASSed and merged. Open issue state is stale.
- #107/#106: corresponding repairs are merged; current issue state requires evidence-based reconciliation.
- #105/#96: child marker/address defects were repaired by later PRs, but evidence found so far does **not** prove the final consolidated deployed live retest required by the parent issues. Do not close that residual gate as verified without evidence.
- Earlier Premium/governance candidate cycles should be checked for stale open state, not treated as current implementation direction.

## Current validation-hierarchy hypothesis

Subject to a narrow follow-up verification:

### Candidate canonical release/product evidence

- full `python -m pytest -q tests` regression;
- recognizer-backed recall corpus/report workflow;
- Zorg baseline/recognizer/cross-profile evidence where domain-specific;
- Phase-6 synthetic E2E workflow validation;
- Scrub Key security/roundtrip tests;
- document hygiene/fidelity tests;
- Premium AppTest/state tests.

### Supplemental diagnostic evidence

- entity scorecard and older report-only residual-risk builders when used within their explicit coverage limits.

### Explicit non-claim

None of the above alone proves production safety or removes the mandatory human-review requirement.

## Execution boundary

This temporary ledger does not authorize implementation by itself. Technical changes require a claimed evidence-backed workpackage, full validation appropriate to the change, and independent assurance before merge. At convergence closeout this file becomes historical/non-authoritative evidence.
