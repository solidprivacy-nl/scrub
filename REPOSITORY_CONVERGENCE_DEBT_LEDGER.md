# SolidPrivacy Scrub — Repository Convergence Debt Ledger

> **TEMPORARY EXECUTION ARTIFACT — NON-AUTHORITATIVE AFTER CONVERGENCE**
>
> This ledger supports `SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP` and later convergence work. It is not a new permanent source of product truth. At convergence closeout, accepted decisions belong in `DECISION_LOG.md`, current risks in `RISK_REGISTER.md`, execution state in `WORKPACKAGES.md`, and implementation history in `CHANGELOG.md`.

Date: 2026-09-04  
Repository: `solidprivacy-nl/scrub`  
Pre-convergence baseline: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`

## Classification model

- `CANONICAL` — supported current behavior; retain, test and document accurately.
- `RECONCILE` — valid responsibility whose implementation, tests, configuration, documentation or status does not match current reality.
- `RETIRE` — superseded, dead, contradictory or unnecessarily active path; remove only after evidence shows it is safe to do so.
- `VARIANT-SPECIFIC` — potentially valid functionality whose requirements conflict with Scrub Private; preserve recoverability through Git but exclude from the Private line unless explicitly re-approved.

Classification applies to capabilities/contracts/runtime paths, not mechanically to whole files.

## Current capability/path ledger

| Capability / path | Current role and evidence | Classification | Target | Protecting evidence / tests | Risk | Smallest next action |
|---|---|---|---|---|---|---|
| Premium staged workspace and generation-bound state (`premium_core_flow_state.py`, Premium Streamlit helpers, current `presidio_streamlit.py`) | Current main contains `Anonimiseren | Terugzetten`, `Standaard | Expert`, staged `Toevoegen → Controleren → Downloaden`, generation-bound analysis/review state and fail-closed export eligibility. | `CANONICAL` | Retain as current UI/state architecture. | Premium state/AppTest/integration suites. | Rebuilding from stale workpackages could reintroduce already-fixed state defects. | Preserve; do not restart old Input/Review/Export packages without current evidence. |
| Human review authority, review table and direct correction | Review/include state remains authoritative; direct masking/manual additions feed normal replacement rows rather than bypassing review/export authority. | `CANONICAL` | Retain mandatory human review and authoritative review state. | Review/direct-selection/manual-row/cross-flow tests. | Privacy control could be weakened by UI simplification or alternate mutation paths. | Preserve. |
| Scrub Key binding and reinsert | Current architecture has bound placeholders, schema-1.1 keys, mapping digest, fail-closed wrong/mixed binding checks and controlled reinsert with explicit legacy handling. | `CANONICAL` | Retain; no redesign without evidence of a concrete flaw. | Scrub Key binding, import/export, TXT/DOCX/PDF-to-TXT reinsert and roundtrip suites. | Re-identification material is safety-critical. | Preserve. |
| Legal recognition / Dutch deterministic recognition | Current runtime uses deterministic Dutch recognizers plus generic NER and Legal profile behavior. Latest main includes Dutch address-span precision repair. | `CANONICAL` | Retain current behavior; future fixes remain evidence-driven. | Legal/custom-recognizer, recall, address-span and cross-profile tests. | False negatives remain product-critical. | Preserve and verify through canonical validation path. |
| Zorg profile, policy and recognizers | Dedicated Zorg policy/recognizers, synthetic corpus, baseline, gap triage and cross-profile evidence exist and are integrated. | `CANONICAL` | Retain; preserve clinical meaning and human review. | Care policy/corpus/recognizer/cross-profile/long-form tests. | Under-detection or clinical over-masking remains critical. | Preserve. |
| TXT/DOCX/text-PDF document handling and DOCX hygiene/fidelity | Supported import/export/reinsert/hygiene paths exist; PDF remains text-based with explicit limitations. | `CANONICAL` | Retain supported boundaries; do not add OCR/restored-PDF merely during cleanup. | Document tools, hygiene, Phase-6 E2E and fidelity tests. | Hidden content and unsupported-format assumptions. | Preserve. |
| Recognizer-backed recall benchmark (`recall_benchmark_runner.py`, `recall_benchmark_report.py`, `.github/workflows/recall-benchmark-report.yml`, `corpus/**`) | Current workflow executes corpus/runner/report tests and runs the actual recognition stack to produce JSON/Markdown diagnostic artifacts. | `CANONICAL` candidate | Treat as primary current recognizer-backed diagnostic release evidence unless later audit finds a newer equivalent. | Recall benchmark corpus/runner/report tests and workflow. | Competing benchmark generations can confuse release evidence. | Document release role and compare older scorecard/residual-risk helpers before de-authorizing anything. |
| Older entity-scorecard / residual-risk helper generation (`benchmark/build_entity_scorecard.py`, `benchmark/build_residual_risk_report.py`) | Useful report-only/supplied-prediction diagnostics explicitly state coverage limits and no production gate. | `RECONCILE` | Keep as supplemental diagnostic if still useful; do not present as equivalent to recognizer-backed corpus execution. | Scorecard/residual-risk tests. | Different generations may appear to be competing sources of accuracy truth. | Classify canonical vs supplemental in a narrow validation-hierarchy package; no new framework. |
| Phase-6 synthetic E2E validation | Exercises TXT/DOCX/PDF workflow, manual additions, Scrub Key, export/reinsert and known limitations. | `CANONICAL` | Retain as workflow-level product evidence complementary to recognizer benchmarks. | `tests/test_mvp_phase6_*` and committed validation artifacts. | Could be mistaken for complete production readiness. | Preserve limitations and human-review boundary. |
| Persistent replacement memory (`replacement_memory.py` + Expert UI) | Current code deliberately persists original/replacement/entity values to `/data/replacement_memory.json` when persistent storage exists and exposes save/load/clear controls. | `VARIANT-SPECIFIC` | Preserve recoverability for possible Local use; Scrub Private must not persist these mappings server-side. | Existing replacement-memory tests plus future Private no-persistence contract. | Direct conflict with Private content-plane retention boundary. | Do not change in bootstrap. After clean baseline, remove/exclude from Private in a separate consequential package. |
| Azure AI Language document recognition | Current Expert analyzer list still includes Azure AI Language and current helper can construct Azure recognizer clients. | `VARIANT-SPECIFIC` | Exclude from Scrub Private baseline; Private document processing stays local. | Current analyzer-selection tests; future Private no-egress tests. | Third-party document-content egress conflicts with intended service trust boundary. | Do not change in bootstrap. Remove/exclude after clean baseline. |
| OpenAI/Azure OpenAI synthesis operator | Current Expert operator includes `synthesize`; helper sends document-bearing prompt to external provider. | `VARIANT-SPECIFIC` | Exclude from Scrub Private baseline unless explicitly approved later. | Current operator/state tests; future Private no-egress tests. | External content processing and unnecessary trust-boundary complexity. | Do not change in bootstrap. Remove/exclude after clean baseline. |
| Content-bearing prompt print in `create_fake_data()` | Current helper prints the generated synthesis prompt before external call. | `RECONCILE` for current full-feature line; Private blocker | No document text/prompts in ordinary application logs. | Future narrow no-content-log regression. | Sensitive content can enter logs. | Remove with Private external-synthesis cleanup; do not build a logging framework. |
| Legacy startup patch script invocation in Dockerfile | Docker CMD still runs `fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py`. Current Premium/direct-source markers make both scripts exit without mutating source. | `RETIRE` candidate | Production/current runtime should not invoke obsolete no-op source mutation machinery. | Patch-script contract tests, Premium source markers, full suite and runtime startup tests. | Hidden startup complexity and future accidental mutation. | Prove both current no-op paths are unnecessary, then remove invocation/scripts in isolated package. |
| `fix_streamlit_nested_expanders.py` historical mutation implementation | Contains large historical patch logic but exits immediately on current Premium source. | `RETIRE` candidate | Remove after startup-path proof; Git history retains implementation. | Existing patch tests and Premium regression suites. | Dead complex code can be accidentally reactivated or mistaken for current UI authority. | Isolated technical package after bootstrap. |
| `fix_streamlit_pdf_text_reinsert.py` historical mutation implementation | Current direct-source marker makes script exit without mutation. | `RETIRE` candidate | Remove after startup-path proof. | Reinsert direct-source/patch tests. | Dead startup code and duplicate authority. | Isolated technical package after bootstrap. |
| Docker/runtime production hardening | Current Dockerfile uses Python 3.10 base, build tools, legacy startup patch calls and permissive Streamlit XSRF/CORS flags. This is not itself evidence of a current HF product defect. | `RECONCILE` / later service work | Keep convergence scoped; production immutability, least privilege, egress and secure server config belong primarily to Private Service stage. | Runtime/startup tests and later service security evidence. | Premature hardening work can derail functional convergence; leaving insecure production config later would be unacceptable. | Record only; defer major hardening until Private Service unless a current safety defect is demonstrated. |
| `openai` and `azure-ai-textanalytics` dependencies | Required only by current variant-specific external processing paths. | `RECONCILE` | Remove when the corresponding Private-incompatible runtime paths are removed; do not leave unused dependencies. | Full dependency/import/runtime suite. | Unused attack/maintenance surface. | Defer to the same Private cleanup package as external processing. |
| `PROJECT_PROMPT.md` product-direction section | Governance/safety rules are current, but bottom section still says broader direction is local-first and old sequencing. | `RECONCILE` | Preserve operating rules; align strategic direction to convergence → Private service, HF synthetic reference, Local deferred. | New convergence contract tests. | Workers can follow obsolete strategy. | Fix in bootstrap. |
| `AGENTS.md` product-direction section | Claim/governance discipline remains useful; product direction still encodes local-first path. | `RECONCILE` | Preserve claim/governance rules; align strategic direction. | New convergence contract tests. | Agent workers can start obsolete packages. | Fix in bootstrap. |
| `ROADMAP.md` | Current file mixes current strategy, long implementation history and old nine-phase/local-installer path. | `RECONCILE` | Replace with concise five-stage strategic roadmap. | New convergence contract tests. | Strategy and implementation history compete as current truth. | Fix in bootstrap. |
| `WORKPACKAGES.md` | Multiple stacked dated `Current execution status override` sections and superseded Premium queues coexist. | `RECONCILE` | Replace with one current Repository Convergence queue. Historical execution remains in CHANGELOG/handovers/Git. | New convergence contract tests. | Workers can execute stale blockers/packages. | Fix in bootstrap. |
| `CHANGELOG.md` | Large historical implementation record. Some old entries are stale as current claims but belong as history. | `CANONICAL` history | Preserve history; prepend new convergence entries rather than rewriting past entries. | File-history discipline. | Rewriting history would destroy provenance. | Add bootstrap entry only. |
| `DECISION_LOG.md` | D043/D042 etc. capture accepted historical/current architecture; newest strategic direction not yet recorded. | `RECONCILE` | Add Repository Convergence + Scrub Private decision without erasing existing decisions. | Governance/document tests. | Future workers lack authoritative record of strategic pivot. | Add D044 in bootstrap. |
| `RISK_REGISTER.md` | Live critical risks exist, but register contains extensive historical execution narrative and R5 still assumes local-first final trust environment. | `RECONCILE` | Keep all live risks/claim boundaries; align hosted-service and source-of-truth risks. Final condensation may occur after technical convergence. | Risk/claim contract tests. | Stale narrative obscures current risk picture or weakens active risk continuity. | Narrow bootstrap alignment; final cleanup later. |
| Open GitHub issues #112/#109/#107/#106 and earlier Premium/governance cycle issues | Several describe candidates that have since PASSed/merged; open state does not match main. #105/#96 additionally require a final consolidated deployed live retest after their child repairs. | `RECONCILE` | Reconstruct each against current main; close stale completed issues, preserve/consolidate any still-unverified live gate. | Raw PR/Actions/assurance comments + current runtime evidence. | Issue state can misroute future work. | Reconcile after bootstrap candidate is accepted; do not falsely claim unperformed live verification. |
| Hugging Face role in project docs | Historically cloud demo versus local-first. | `RECONCILE` | Define HF as synthetic/approved reference application-validation surface; not confidential-production assurance. | HF sync + synthetic app verification. | Overclaiming provider-level retention/security. | Fix strategic wording in bootstrap. |
| Local/offline installer programme | Valuable prior planning exists but is not current delivery path after approved Private/VPS direction. | `VARIANT-SPECIFIC` / deferred | Preserve history; do not execute installer programme unless future business requirement reopens it. | Historical decision/packaging docs. | Maintaining two active delivery lines creates distraction and duplicated architecture. | Demote from active roadmap in bootstrap. |

## Current issue-reconciliation notes

These notes are findings, not closure authority by themselves.

- #112: independent assurance for PR #111 recorded PASS; PR #111 is merged into current main; exact-main Tests and HF sync are green. Issue is stale as an active candidate gate.
- #109: independent assurance for PR #108 recorded PASS; PR #108 is merged. Issue is stale as an active candidate gate.
- #107/#106: implementation issues whose corresponding repairs are merged; active issue state requires reconciliation.
- #105/#96: their original App Shell state defect was repaired, but live verification later exposed marker/address defects. Those child defects were subsequently repaired by PR #108/#111. Evidence found so far does **not** prove the final consolidated deployed live retest required by the parent issues was completed. Do not close that residual gate as verified without evidence.
- Earlier #74–#100 Premium/governance repair/assurance issues are historical candidate cycles and should be checked for stale open state, not treated as current implementation direction.

## Current validation-hierarchy hypothesis

Subject to a narrow follow-up verification:

### Candidate canonical release/product evidence

- full `python -m pytest -q tests` regression;
- recognizer-backed `recall_benchmark_runner.py` / `recall_benchmark_report.py` corpus workflow;
- Zorg baseline/recognizer/cross-profile evidence where domain-specific;
- Phase-6 synthetic E2E workflow validation;
- Scrub Key security/roundtrip tests;
- document hygiene/fidelity tests;
- Premium AppTest/state tests.

### Supplemental diagnostic evidence

- entity scorecard and older report-only residual-risk builders when used within their explicit coverage limits.

### Explicit non-claim

None of the above alone proves production safety or removes the mandatory human-review requirement.

## Bootstrap boundary

This ledger authorizes no runtime change by itself. The bootstrap package may only reset current strategy/execution documentation and contract tests. Technical changes must be split into evidence-backed consequential workpackages and receive normal independent assurance.
