# SolidPrivacy Scrub — Repository Convergence Debt Ledger

> **TEMPORARY EXECUTION ARTIFACT — NON-AUTHORITATIVE AFTER CONVERGENCE**
>
> This ledger supports Stage 1 execution. It is not a permanent source of product truth. Accepted decisions belong in `DECISION_LOG.md`, current risks in `RISK_REGISTER.md`, current execution in `WORKPACKAGES.md`, and implementation history in `CHANGELOG.md`.

Date: 2026-09-05  
Repository: `solidprivacy-nl/scrub`  
Pre-convergence baseline: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Last governance-valid pre-WP04 main: `268d967db95d923a73a3979ffce2d0cab586e499`  
Premature PR #120 merge: `fd69294c67a59bb150f5d4a637daad2607c14077`  
Governed recovery main / fresh WP04 base: `14baceb97b274de6ef35c42ce48441c4e74c5f08`

## Classification model

- `CANONICAL` — supported current behavior; retain, test and document accurately.
- `RECONCILE` — valid responsibility whose active implementation, test, configuration or authority needs current-truth alignment.
- `RETIRE` — superseded, dead, contradictory or unnecessarily active path; remove only after evidence shows it is safe.
- `VARIANT-SPECIFIC` — potentially valid functionality whose requirements conflict with Scrub Private; preserve recoverability through Git but exclude from the Private line unless explicitly re-approved.

Classification applies to capabilities/contracts/runtime paths, not mechanically to whole files.

## Bootstrap/current-truth debt already resolved

PR #114 received fresh blind PASS and merged as `255cd619d5cf6eab32f9383940eaa4af362cb68c` with green exact-main Tests and GitHub→Hugging Face sync.

The following remain accepted current truth:

- `PROJECT_PROMPT.md` and `AGENTS.md` route through Repository Convergence → Scrub Private;
- `ROADMAP.md` contains the five strategic stages;
- `WORKPACKAGES.md` contains one current executable queue;
- root `CHANGELOG.md` is post-reset history and pre-convergence history is preserved under `history/`;
- D044 records the accepted convergence/private direction;
- Hugging Face is bounded to synthetic/approved application validation;
- Local/offline installer work is deferred variant-specific history, not an active delivery line.

## Runtime startup debt already resolved

PR #116 received fresh blind PASS and merged as `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84` with green exact-main Tests and GitHub→Hugging Face sync.

Resolved current-runtime finding:

- Docker no longer invokes `fix_streamlit_nested_expanders.py` or `fix_streamlit_pdf_text_reinsert.py` before Streamlit startup;
- Streamlit starts `presidio_streamlit.py` directly with the pre-existing server flags unchanged;
- historical patch-script files remain separate dormant RETIRE candidates.

Do not describe live Docker startup as source-mutating after this accepted work.

## Validation-authority debt already resolved

PR #118 received fresh blind PASS and merged as `268d967db95d923a73a3979ffce2d0cab586e499`; exact-main Tests passed `1268` tests and GitHub→Hugging Face sync succeeded.

D045 is therefore accepted validation authority:

```text
RELEASE REGRESSION GATE
.github/workflows/tests.yml
→ python -m pytest -q tests
→ exact candidate/main SHA evidence
```

Focused capability suites remain product/domain regression evidence inside the full suite. Recognizer-backed recall reporting and WP22/WP23/WP24 remain supplemental diagnostics, not release/production score gates.

## WP-CONVERGENCE-04 governance sequencing failure and governed recovery

The first WP04 candidate was prepared in PR #120 at frozen head:

```text
1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a
```

but the required lifecycle was violated. PR #120 merged as:

```text
fd69294c67a59bb150f5d4a637daad2607c14077
```

and issue #74 was closed before the fresh independent assurance verdict. The later fresh blind assurance returned `FAIL` because independent assurance is a pre-action ordering control and cannot be retroactively supplied by green post-merge CI.

Governed recovery PR #122 then followed the correct lifecycle:

```text
recovery frozen head
8565af4e9f579b3a975c6122668f6511a9df627a

fresh PASS before merge
→ guarded merge
14baceb97b274de6ef35c42ce48441c4e74c5f08
→ exact-main Tests 33966351441 / 1272 passed
→ exact-main GitHub→HF sync 33966351286 / SUCCESS
```

Recovery outcome:

- issue #74 is OPEN/reopened with explicit governance-recovery provenance;
- #96 remains OPEN;
- #119 remains OPEN;
- issue #121 is closed/completed;
- issue #123 contains the successful recovery assurance and remains OPEN only because that issue's explicit PASS procedure required closing #121 and then stopping;
- failed PR #120 candidate-specific active authority was removed while Git history remains intact;
- no WP04 issue reconciliation was executed during recovery;
- PR #122 recovery PASS is not WP04 assurance and cannot substitute for a new WP04 exact-head review.

Because WP04 now reconciles the live GitHub issue inventory, completed recovery-assurance issue #123 is historical administration and belongs in the WP04 closure candidate. Closing #123 after new WP04 PASS/merge/exact-main confirmation does not alter or reuse its assurance verdict.

## Fresh WP-CONVERGENCE-04 retry — current evidence candidate

A new WP04 implementation candidate starts from exact governed recovery main:

```text
14baceb97b274de6ef35c42ce48441c4e74c5f08
```

The earlier substantive reconstruction remains useful evidence, but the action authority must be newly earned.

### Keep open

```text
#96
```

Reason: PR #104 V2 independently PASSed and merged, PR #108 independently PASSed and merged the marker/compact-placeholder repair, and PR #111 independently PASSed and merged the Dutch-address precision repair. The required consolidated deployed live-app retest after both repairs **remains unproven**. #96 therefore remains the residual current Premium/App-Shell live-verification gate.

### Close only after new WP04 PASS + guarded merge + exact-main verification

```text
#74 #75 #76 #77
#79 #81 #84 #86 #88 #89
#98 #100 #105
#106 #107 #109 #112
#123
```

Evidence basis:

- #74/#75/#76 are superseded PR #73 review/repair dispatches; #77 records the final exact-head PASS/authorization cycle for the PR #73 head that subsequently merged;
- #79/#81 contract and assurance cycle is implemented/merged and no longer current work;
- #84/#86/#88/#89 are historical Premium App Shell/staged-workspace candidate cycles superseded by later integrated repairs/current source;
- #98/#100 are the first App Shell state-repair/assurance cycle; their failed/unmerged state was superseded by V2 PR #104;
- #105 contains the V2 PASS plus later live-regression discovery; the technical repairs were split into #106/#107 and later independently assured/merged;
- #106/#109 marker/compact-display implementation/assurance are complete and PR #108 merged;
- #107/#112 Dutch-address implementation/assurance are complete and PR #111 merged;
- #123 is the completed PR #122 recovery-assurance dispatch; its open state is procedural residue from the explicit stop rule, not a current unresolved gate.

This candidate does not execute those closures. Required action order is:

```text
new exact candidate
→ full Tests
→ fresh blind PASS
→ guarded merge
→ exact-main Tests + GitHub→HF verification
→ then issue mutation
→ readback
```

No target issue mutation is authorized before the exact-main verification step completes.

The active assurance-dispatch issue for the final frozen WP04 candidate is procedural current work and must close itself only after its own PASS/post-merge administrative closeout; it is not part of the pre-verdict historical close set.

## Current capability/path ledger

| Capability / path | Current role / evidence | Classification | Current target / smallest next action |
|---|---|---|---|
| Premium staged workspace and generation-bound state | Current app implements `Anonimiseren | Terugzetten`, `Standaard | Expert`, staged `Toevoegen → Controleren → Downloaden`, shared authoritative state and fail-closed export eligibility. | `CANONICAL` | Preserve; do not rebuild from historical workpackages. |
| Human review authority and direct/manual correction | Review/include state remains authoritative; direct and manual missed-value paths feed normal review/export authority. | `CANONICAL` | Preserve mandatory human review. |
| Scrub Key binding and reinsert | Bound placeholders, schema-1.1 keys, mapping digest, document binding and fail-closed mismatch handling are covered by dedicated tests. | `CANONICAL` | Preserve; redesign only for a proven defect. |
| Legal / Dutch recognition | Deterministic recognizers plus generic NER and Legal profile are current, with address-span repair on accepted main. | `CANONICAL` | Preserve and validate through current evidence paths. |
| Zorg policy and recognizers | Dedicated Zorg policy/recognizers, synthetic corpus, gap triage and cross-profile evidence are integrated. | `CANONICAL` | Preserve clinical meaning and human review. |
| TXT/DOCX/text-PDF handling and DOCX hygiene/fidelity | Supported import/export/reinsert/hygiene behavior exists with explicit PDF and unsupported-content boundaries. | `CANONICAL` | Preserve; no OCR/restored-PDF expansion during convergence. |
| Full `.github/workflows/tests.yml` regression | Runs `python -m pytest -q tests` for pull requests and `main`. | `CANONICAL RELEASE REGRESSION GATE` | Preserve as current regression authority alongside independent assurance. |
| Focused Phase-6, Scrub Key, document, Zorg, recognizer and Premium/AppTest suites | Capability-specific regression evidence inside the full suite. | `CANONICAL CAPABILITY REGRESSION EVIDENCE` | Preserve; no competing merge authority. |
| Recognizer-backed recall benchmark | Recognizer/candidate-scanner diagnostic over synthetic/gold material with `diagnostic_only`, no production gate and no enforced thresholds. | `SUPPLEMENTAL DIAGNOSTIC` | Preserve diagnostic value. |
| WP22 supplied-prediction runner | Scores supplied prediction JSON and does not call recognizers or apply CI thresholds. | `SUPPLEMENTAL / HISTORICAL DIAGNOSTIC` | Retain while useful; not release authority. |
| WP23 entity scorecard / WP24 residual-risk report | Report-only/non-gating chain with coverage limitations. | `SUPPLEMENTAL / HISTORICAL DIAGNOSTIC` | Retain within explicit limits. |
| Persistent replacement memory (`replacement_memory.py` + Expert UI) | Deliberately persists original/replacement/entity values when persistent storage exists. | `VARIANT-SPECIFIC` | Exclude/remove from Scrub Private only in Stage 2. |
| Azure AI Language document recognition | Optional Expert path can send document content to Azure AI Language. | `VARIANT-SPECIFIC` | Exclude from Scrub Private in Stage 2. |
| OpenAI/Azure OpenAI synthesis operator | Optional Expert path can send document-bearing prompts externally. | `VARIANT-SPECIFIC` | Exclude from Scrub Private in Stage 2 unless explicitly re-approved. |
| Content-bearing prompt print in `create_fake_data()` | Synthesis helper prints content-bearing prompt. | `RECONCILE` / Private blocker | Remove with Stage-2 external-synthesis cleanup; add narrow no-content-log contract. |
| `fix_streamlit_nested_expanders.py` historical mutation implementation | Dormant after PR #116. | `RETIRE` candidate | Evidence-based later retirement only. |
| `fix_streamlit_pdf_text_reinsert.py` historical mutation implementation | Dormant after PR #116. | `RETIRE` candidate | Evidence-based later retirement only. |
| GitHub issue state from Premium/governance cycles | Substantive disposition is reconstructed and recovery is complete; the retry still requires a new exact-head PASS and ordered action. | `RECONCILE` | Finish fresh WP04 candidate/assurance, then mutate issues only after exact-main verification. |
| HF workflow path-ignore churn | Governance-only changes can trigger unnecessary but successful HF sync. | `RECONCILE` / low operational priority | Address only if repeated churn creates real cost. |

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

This temporary ledger does not authorize implementation or issue mutation by itself. Consequential changes or administrative mutations require an exact candidate, full validation appropriate to the change, and fresh independent assurance before merge/action. For the WP04 retry, exact-main post-merge verification is an additional explicit prerequisite before the reviewed issue mutations. At convergence closeout this file becomes historical/non-authoritative evidence.
