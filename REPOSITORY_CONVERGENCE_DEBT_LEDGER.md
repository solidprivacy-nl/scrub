# SolidPrivacy Scrub — Repository Convergence Debt Ledger

> **TEMPORARY EXECUTION ARTIFACT — NON-AUTHORITATIVE AFTER CONVERGENCE**
>
> This ledger supports Stage 1 execution. It is not a permanent source of product truth. Accepted decisions belong in `DECISION_LOG.md`, current risks in `RISK_REGISTER.md`, current execution in `WORKPACKAGES.md`, and implementation history in `CHANGELOG.md`.

Date: 2026-09-06  
Repository: `solidprivacy-nl/scrub`  
Pre-convergence baseline: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Governed post-WP04 main: `2d4ab0446c20f08ad07576af326ab4b0df0a2af7`

## Classification model

- `CANONICAL` — supported current behavior; retain, test and document accurately.
- `RECONCILE` — valid responsibility whose active implementation, test, configuration or authority needs current-truth alignment.
- `RETIRE` — superseded, dead, contradictory or unnecessarily active path; remove only after evidence shows it is safe.
- `VARIANT-SPECIFIC` — potentially valid functionality whose requirements conflict with Scrub Private; preserve recoverability through Git but exclude from the Private line unless explicitly re-approved.

Classification applies to capabilities/contracts/runtime paths, not mechanically to whole files.

## Accepted convergence history

### Bootstrap/current-truth reset — resolved

PR #114 received fresh blind PASS and merged as `255cd619d5cf6eab32f9383940eaa4af362cb68c` with green exact-main Tests and GitHub→Hugging Face sync.

Accepted current truth includes:

- Repository Convergence → Scrub Private Application → Private Service → External Assurance → Pilot;
- five-stage roadmap;
- one current executable workpackage queue;
- D044 as strategic direction;
- Hugging Face as synthetic/approved application-validation surface, not confidential-production infrastructure assurance;
- Local/offline work deferred as recoverable variant-specific history.

### Runtime startup authority — resolved

PR #116 received fresh blind PASS and merged as `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`.

Docker no longer invokes `fix_streamlit_nested_expanders.py` or `fix_streamlit_pdf_text_reinsert.py` before startup. Streamlit starts `presidio_streamlit.py` directly. The scripts remain dormant RETIRE candidates only.

### Validation authority — resolved

PR #118 received fresh blind PASS and merged as `268d967db95d923a73a3979ffce2d0cab586e499`.

D045 remains accepted validation authority:

```text
RELEASE REGRESSION GATE
.github/workflows/tests.yml
→ python -m pytest -q tests
→ exact candidate/main SHA evidence
```

Focused capability suites remain regression evidence inside the full suite. Recognizer-backed recall and WP22/WP23/WP24 remain supplemental diagnostics; no production score threshold or new Evidence Framework was introduced.

## WP-CONVERGENCE-04 governance history — resolved

The first WP04 candidate was prepared in PR #120 at frozen head:

```text
1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a
```

It was prematurely merged as:

```text
fd69294c67a59bb150f5d4a637daad2607c14077
```

and issue #74 mutated before fresh independent assurance. The later assurance correctly returned `GOVERNANCE FAIL`. Green CI and deployment did not cure the ordering defect.

Governed recovery PR #122 then received fresh PASS before merge and produced:

```text
recovery reviewed head
8565af4e9f579b3a975c6122668f6511a9df627a

recovery merge/main
14baceb97b274de6ef35c42ce48441c4e74c5f08
```

The recovery PASS is not WP04 assurance and does not authorize later reconciliation or the #96 live outcome.

Fresh WP04 PR #124 then followed the required sequence:

```text
reviewed head
ce021443303cfa11de12f3273f872b2d027da5db

fresh blind PASS before merge
→ guarded merge
2d4ab0446c20f08ad07576af326ab4b0df0a2af7
→ exact-main Tests 33997889522 / 1279 passed in 14.51s
→ GitHub→HF sync 33997889554 / SUCCESS
→ only then issue-state reconciliation
```

WP04 administrative outcome:

- #74 #75 #76 #77 #79 #81 #84 #86 #88 #89 #98 #100 #105 #106 #107 #109 #112 #123 closed as completed/historical/superseded;
- #119 closed only after readback;
- assurance #126 closed after its own procedure;
- historical PASS/FAIL/INDETERMINATE provenance remains in GitHub/Git;
- #96 remains OPEN because the consolidated deployed live-app retest remains unproven.

## WP-CONVERGENCE-05 — current residual evidence gate

The only current product-facing Repository Convergence gate is issue #96.

Underlying repair chains are already accepted at source/deployment level:

- PR #104 V2 — Standard↔Expert source/analysis/review-state preservation;
- PR #108 — exact processed-text marker offsets and compact bound-placeholder display;
- PR #111 — Dutch address-span precision repair.

Required remaining evidence is the **consolidated deployed live-app verification**. It must verify the actual Hugging Face user flow with synthetic/approved material and record the exact deployed SHA/date/results.

Required behaviors:

- staged Standard/Expert flow operates on current authoritative state;
- leading whitespace/newlines do not shift marker/highlight offsets;
- strict bound placeholders stay internally intact but render compactly in review;
- full binding tokens do not leak or fragment in the review display;
- `Polderweg 8` and representative legitimate Dutch address forms do not absorb adjacent ordinary words;
- review/export lineage remains fail-closed;
- mandatory human review remains explicit.

CI and GitHub→Hugging Face sync are necessary evidence but cannot substitute for this live behavior proof.

## Current capability/path ledger

| Capability / path | Current role / evidence | Classification | Smallest next action |
|---|---|---|---|
| Premium staged workspace and generation-bound state | Current app implements `Anonimiseren | Terugzetten`, `Standaard | Expert`, staged `Toevoegen → Controleren → Downloaden`, shared authoritative state and fail-closed export eligibility. | `CANONICAL` | Preserve; verify deployed integrated behavior under WP05. |
| Human review authority and direct/manual correction | Review/include state remains authoritative; direct/manual missed-value paths feed normal review/export authority. | `CANONICAL` | Preserve mandatory human review. |
| Scrub Key binding and reinsert | Bound placeholders, schema-1.1 keys, mapping digest, document binding and fail-closed mismatch handling remain tested. | `CANONICAL` | Preserve; redesign only for a proven defect. |
| Legal / Dutch recognition | Deterministic recognizers plus generic NER and Legal profile are current; address-span repair is merged. | `CANONICAL` | Preserve; verify deployed `Polderweg 8` behavior in WP05. |
| Zorg policy and recognizers | Dedicated Zorg policy/recognizers, synthetic corpus, gap triage and cross-profile evidence are integrated. | `CANONICAL` | Preserve clinical meaning and human review. |
| TXT/DOCX/text-PDF handling and DOCX hygiene/fidelity | Supported import/export/reinsert/hygiene behavior exists with explicit PDF and unsupported-content boundaries. | `CANONICAL` | Preserve; no OCR/restored-PDF expansion during convergence. |
| Full `.github/workflows/tests.yml` regression | Runs `python -m pytest -q tests` for pull requests and `main`. | `CANONICAL RELEASE REGRESSION GATE` | Preserve alongside independent assurance. |
| Focused Phase-6, Scrub Key, document, Zorg, recognizer and Premium/AppTest suites | Capability-specific regression evidence inside the full suite. | `CANONICAL CAPABILITY REGRESSION EVIDENCE` | Preserve; no competing merge authority. |
| Recognizer-backed recall benchmark | Synthetic/gold recognizer diagnostic with explicit non-gating metadata. | `SUPPLEMENTAL DIAGNOSTIC` | Preserve diagnostic value. |
| WP22/WP23/WP24 evidence chain | Supplied-prediction/report-only historical diagnostics with known limits. | `SUPPLEMENTAL / HISTORICAL DIAGNOSTIC` | Retain while useful; not release authority. |
| Persistent replacement memory | Deliberately persists original/replacement/entity values when persistent storage exists. | `VARIANT-SPECIFIC` | Exclude/remove from Scrub Private only in Stage 2. |
| Azure AI Language document recognition | Optional Expert path can send document content to Azure. | `VARIANT-SPECIFIC` | Exclude from Scrub Private in Stage 2. |
| OpenAI/Azure OpenAI synthesis operator | Optional Expert path can send document-bearing prompts externally. | `VARIANT-SPECIFIC` | Exclude from Scrub Private in Stage 2 unless explicitly re-approved. |
| Content-bearing prompt print in `create_fake_data()` | Synthesis helper prints content-bearing prompt. | `RECONCILE` / Private blocker | Remove with Stage-2 external-synthesis cleanup; add no-content-log contract. |
| `fix_streamlit_nested_expanders.py` | Dormant after PR #116. | `RETIRE` candidate | Separate evidence-based retirement only. |
| `fix_streamlit_pdf_text_reinsert.py` | Dormant after PR #116. | `RETIRE` candidate | Separate evidence-based retirement only. |
| GitHub issue/current-state reconciliation | WP04 completed; all reviewed historical issues closed; only #96 remains product-facing. | `RECONCILE` — nearly resolved | Complete WP05 live verification, then final canonical alignment. |
| HF workflow path-ignore churn | Governance-only changes can trigger unnecessary but successful HF sync. | `RECONCILE` / low priority | Address only if repeated churn creates real cost. |

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

This temporary ledger does not authorize implementation or issue mutation by itself. Consequential repository changes require an exact candidate and fresh independent assurance before merge. The #96 live gate must not close from CI/HF sync alone. At convergence closeout this file becomes historical/non-authoritative evidence.
