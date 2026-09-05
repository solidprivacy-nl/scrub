# SolidPrivacy Scrub — Repository Convergence Debt Ledger

> **TEMPORARY EXECUTION ARTIFACT — NON-AUTHORITATIVE AFTER CONVERGENCE**
>
> This ledger supports Stage 1 execution. It is not a permanent source of product truth. Accepted decisions belong in `DECISION_LOG.md`, current risks in `RISK_REGISTER.md`, current execution in `WORKPACKAGES.md`, and implementation history in `CHANGELOG.md`.

Date: 2026-09-05  
Repository: `solidprivacy-nl/scrub`  
Pre-convergence baseline: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Accepted convergence main at start of WP-CONVERGENCE-04: `268d967db95d923a73a3979ffce2d0cab586e499`

## Classification model

- `CANONICAL` — supported current behavior; retain, test and document accurately.
- `RECONCILE` — valid responsibility whose active implementation, test, configuration or authority needs current-truth alignment.
- `RETIRE` — superseded, dead, contradictory or unnecessarily active path; remove only after evidence shows it is safe.
- `VARIANT-SPECIFIC` — potentially valid functionality whose requirements conflict with Scrub Private; preserve recoverability through Git but exclude from the Private line unless explicitly re-approved.

Classification applies to capabilities/contracts/runtime paths, not mechanically to whole files.

## Bootstrap/current-truth debt already resolved

PR #114 received fresh blind PASS and merged as `255cd619d5cf6eab32f9383940eaa4af362cb68c` with green exact-main Tests and GitHub→Hugging Face sync.

The following are **not current cleanup tasks anymore**:

- `PROJECT_PROMPT.md` and `AGENTS.md` route through Repository Convergence → Scrub Private;
- `ROADMAP.md` contains the five strategic stages;
- `WORKPACKAGES.md` contains one current executable queue;
- root `CHANGELOG.md` is post-reset history and the pre-convergence changelog is preserved byte-identically under `history/`;
- D044 records the accepted convergence/private direction;
- `RISK_REGISTER.md` carries current critical risks plus source-of-truth/runtime-mutation risk;
- Hugging Face is bounded to synthetic/approved application validation;
- Local/offline installer work is deferred variant-specific history, not an active delivery line.

Do not reopen these items without fresh evidence of a current defect.

## Runtime startup debt already resolved

PR #116 received fresh blind PASS and merged as `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84` with green exact-main Tests and GitHub→Hugging Face sync.

Resolved current-runtime finding:

- Docker no longer invokes `fix_streamlit_nested_expanders.py` or `fix_streamlit_pdf_text_reinsert.py` before Streamlit startup;
- Streamlit starts `presidio_streamlit.py` directly with the pre-existing server flags unchanged;
- the historical patch-script files remain separate dormant RETIRE candidates and are not current runtime startup authority.

Do not describe live Docker startup as source-mutating after this accepted main.

## Validation-authority debt already resolved

PR #118 received fresh blind PASS and merged as `268d967db95d923a73a3979ffce2d0cab586e499`; exact-main Tests passed `1268` tests and GitHub→Hugging Face sync succeeded.

D045 is therefore current accepted validation authority, not a pending candidate:

```text
RELEASE REGRESSION GATE
.github/workflows/tests.yml
→ python -m pytest -q tests
→ exact candidate/main SHA evidence
```

Focused capability suites remain product/domain regression evidence inside the full suite. Recognizer-backed recall reporting and WP22/WP23/WP24 remain supplemental diagnostics, not release/production score gates.

## Current capability/path ledger

| Capability / path | Current role / evidence | Classification | Current target / smallest next action |
|---|---|---|---|
| Premium staged workspace and generation-bound state | Current app implements `Anonimiseren | Terugzetten`, `Standaard | Expert`, staged `Toevoegen → Controleren → Downloaden`, shared authoritative state and fail-closed export eligibility. | `CANONICAL` | Preserve; do not rebuild from historical workpackages. |
| Human review authority and direct/manual correction | Review/include state remains authoritative; direct and manual missed-value paths feed normal review/export authority. | `CANONICAL` | Preserve mandatory human review. |
| Scrub Key binding and reinsert | Bound placeholders, schema-1.1 keys, mapping digest, document binding and fail-closed mismatch handling are covered by dedicated tests. | `CANONICAL` | Preserve; redesign only for a proven defect. |
| Legal / Dutch recognition | Deterministic recognizers plus generic NER and Legal profile are current, with address-span repair on accepted main. | `CANONICAL` | Preserve and validate through current evidence paths. |
| Zorg policy and recognizers | Dedicated Zorg policy/recognizers, synthetic corpus, gap triage and cross-profile evidence are integrated. | `CANONICAL` | Preserve clinical meaning and human review. |
| TXT/DOCX/text-PDF handling and DOCX hygiene/fidelity | Supported import/export/reinsert/hygiene behavior exists with explicit PDF and unsupported-content boundaries. | `CANONICAL` | Preserve; no OCR/restored-PDF expansion during convergence. |
| Full `.github/workflows/tests.yml` regression | Runs `python -m pytest -q tests` for pull requests and `main`, and is used for exact-candidate/exact-main verification in the two-role release process. | `CANONICAL RELEASE REGRESSION GATE` | Preserve as the single current regression merge/main authority alongside independent assurance. |
| Focused Phase-6, Scrub Key, document, Zorg, recognizer and Premium/AppTest suites | Exercise specific workflow/product/security/domain contracts and are included in the full regression suite. | `CANONICAL CAPABILITY REGRESSION EVIDENCE` | Preserve; may run independently for diagnosis but do not create competing merge authority. |
| Recognizer-backed recall benchmark (`recall_benchmark_runner.py`, `recall_benchmark_report.py`, diagnostic workflow) | Runs recognizer/candidate-scanner diagnostics against synthetic/gold material; metadata explicitly says diagnostic-only, no production gate and no enforced thresholds. | `SUPPLEMENTAL DIAGNOSTIC` | Preserve diagnostic value; do not present scores as release/production gates. |
| WP22 supplied-prediction runner (`benchmark/run_recall_precision.py`) | Scores supplied prediction JSON and explicitly does not call recognizers or apply CI thresholds. | `SUPPLEMENTAL / HISTORICAL DIAGNOSTIC` | Retain while useful for analysis/history; not release authority. |
| WP23 entity scorecard / WP24 residual-risk report | Report-only wrappers over WP22 with no production gate; residual-risk builder records foundation-only/coverage limitations. | `SUPPLEMENTAL / HISTORICAL DIAGNOSTIC` | Retain within explicit limits; no threshold promotion during convergence. |
| Persistent replacement memory (`replacement_memory.py` + Expert UI) | Deliberately persists original/replacement/entity values when persistent storage exists. | `VARIANT-SPECIFIC` | Preserve shared-baseline recoverability; remove/exclude from Scrub Private only in Stage 2. |
| Azure AI Language document recognition | Current optional Expert path can send document content to Azure AI Language. | `VARIANT-SPECIFIC` | Exclude from Scrub Private in Stage 2; do not build a proxy/broker. |
| OpenAI/Azure OpenAI synthesis operator | Current optional Expert path can send document-bearing prompts to an external provider. | `VARIANT-SPECIFIC` | Exclude from Scrub Private in Stage 2 unless explicitly re-approved. |
| Content-bearing prompt print in `create_fake_data()` | Synthesis helper prints a content-bearing prompt. | `RECONCILE` / Private blocker | Remove with Private external-synthesis cleanup; add a narrow no-content-log contract, not a logging framework. |
| `fix_streamlit_nested_expanders.py` historical mutation implementation | Historical compatibility code remains in repository and is no longer invoked by Docker startup after PR #116. | `RETIRE` candidate | Decide later whether diagnostic/history value justifies keeping it; do not mass-delete tests blindly. |
| `fix_streamlit_pdf_text_reinsert.py` historical mutation implementation | Historical compatibility code remains in repository and is no longer invoked by Docker startup after PR #116. | `RETIRE` candidate | Treat separately from completed runtime invocation retirement. |
| Docker/runtime production hardening | Python 3.10 base/build tools and permissive Streamlit XSRF/CORS settings remain. PR #116 deliberately did not change these. | `RECONCILE` / later service work | Defer major hardening to Private Service unless a current safety defect is proven. |
| `openai` and `azure-ai-textanalytics` dependencies | Used only by current variant-specific external-processing paths. | `RECONCILE` | Remove when those Private-incompatible paths are removed; do not leave unused dependencies. |
| GitHub issue state from Premium/governance cycles | 18 pre-WP04 historical/current issues are open although most candidate cycles are completed/superseded. | `RECONCILE` | Close only evidence-backed stale cycles after independent WP04 assurance; keep #96 as residual live gate. |
| HF workflow path-ignore churn | Governance-only changes can trigger unnecessary but successful HF sync when convergence/history paths are not ignored. | `RECONCILE` / low operational priority | Consider only if repeated churn creates real operational cost; do not mix with product/runtime packages. |

## WP-CONVERGENCE-04 reviewed issue-disposition candidate

This section freezes the proposed administrative action for independent assurance; it is not itself issue-closure authority.

### Keep open

```text
#96
```

Reason: PR #104 V2 independently PASSed and merged, technically superseding the old PR #85 exact-head PASS/FAIL conflict. PR #108 independently PASSed and merged the marker/compact-placeholder repair. PR #111 independently PASSed and merged the Dutch-address precision repair. **No evidence reconstructed in WP04 proves the required consolidated deployed live-app retest after both repairs.** #96 therefore remains the single current Premium/App-Shell live-verification gate.

### Close after WP04 independent PASS

```text
#74 #75 #76 #77
#79 #81 #84 #86 #88 #89
#98 #100 #105
#106 #107 #109 #112
```

Evidence basis:

- #74/#75/#76 are superseded PR #73 review/repair dispatches; #77 records final exact-head PASS and merge authorization for the PR #73 head that subsequently merged;
- #79/#81 contract and assurance cycle is implemented/merged and no longer an open execution gate;
- #84/#86/#88/#89 are historical Premium App Shell/staged-workspace candidate cycles superseded by later integrated repairs and current canonical Premium source;
- #98/#100 are the first App Shell state-repair/assurance cycle; PR #99 was closed unmerged after failure and superseded by V2 PR #104;
- #105 contains the fresh V2 PASS plus later live-regression discovery; PR #104 merged and its remaining live findings were split into #106/#107, so #105 should not compete with #96 as a second current parent gate;
- #106/#109 marker/compact-display implementation/assurance are complete and PR #108 merged;
- #107/#112 Dutch-address implementation/assurance are complete and PR #111 merged.

Closure must preserve provenance in issue comments/Git and must not claim the missing #96 live-app retest occurred.

## Current validation hierarchy

### Release regression authority

```text
.github/workflows/tests.yml
→ python -m pytest -q tests
→ exact candidate/main SHA evidence
```

### Capability regression evidence

- Phase-6 synthetic E2E workflow validation;
- Scrub Key security/roundtrip tests;
- document hygiene/fidelity tests;
- Zorg recognizer/profile/cross-profile tests;
- recognizer/candidate-scanner contracts;
- Premium Streamlit/AppTest/state tests;
- other focused tests included in the full suite.

### Supplemental diagnostic evidence

- recognizer-backed recall corpus/report workflow;
- WP22 supplied-prediction recall/precision runner;
- WP23 entity scorecard;
- WP24 residual-risk report.

### Explicit non-claims

- no diagnostic score is a merge or production gate;
- no production recall/precision threshold is introduced by convergence;
- synthetic validation does not prove production safety;
- mandatory human review remains binding.

## Execution boundary

This temporary ledger does not authorize implementation or issue mutation by itself. Technical or consequential administrative changes require a claimed evidence-backed workpackage, full validation appropriate to the change, and independent assurance before merge/action. At convergence closeout this file becomes historical/non-authoritative evidence.
