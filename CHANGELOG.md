# Changelog — SolidPrivacy Scrub

This file is the current implementation history from the Repository Convergence reset onward.

The exact pre-convergence changelog is preserved byte-for-byte at:

```text
history/CHANGELOG_PRE_CONVERGENCE_20260904.md
```

and remains recoverable from pre-convergence baseline:

```text
54c73e0ebf5a3a3ed7039a50596fb57694add3cd
```

The archived file is historical provenance only; it must not be interpreted as a current execution queue. Current work is defined by `WORKPACKAGES.md`.

---

## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION — FRESH RETRY

Status: `IMPLEMENTATION IN PROGRESS`; candidate reopened before assurance after live open-issue inventory exposed completed recovery-assurance issue #123 as stale OPEN administration.  
Role: `implementation_operations`  
Issue: #119 — open  
PR: #124 — open/draft  
Branch: `wp/repository-convergence-issue-state-reconciliation-v2`  
Exact starting main/base: `14baceb97b274de6ef35c42ce48441c4e74c5f08`

### Why this is a new candidate

The first WP04 candidate in PR #120 was not rejected for a material content defect, but its merge/issue mutation happened before the required independent assurance verdict. That release-ordering failure invalidated PR #120 as governed action authority.

Governed recovery PR #122 has now independently PASSed, merged, and been exact-main verified. The retry therefore starts from new exact main `14baceb...`; it may reuse evidence findings, but it may not reuse PR #120's candidate identity, merge, CI, or later FAIL as a pre-action PASS.

### Current-truth correction before assurance

The first frozen retry head `06198ec05907c32b41ecc2876d8ca1fb0d3554eb` had a green full suite (`1278 passed in 15.12s`) and issue #125 had been created as the fresh assurance dispatch. Before any independent verdict was recorded, implementation re-read the actual open issue inventory and found recovery-assurance issue #123 still OPEN.

That open state was truthful under #123's own PASS procedure, which explicitly required closing #121 and then stopping. But once recovery is complete, #123 is no longer current work. Because WP04's business objective is current GitHub issue-state reconciliation, leaving #123 open would make the candidate incomplete. The candidate was therefore intentionally unfrozen before assurance and the disposition changed from 17-close/1-keep to 18-close/1-keep.

Keep open:

```text
#96
```

Potential evidence-backed close set after the corrected candidate independently PASSes, merges, and exact-main verification succeeds:

```text
#74 #75 #76 #77
#79 #81 #84 #86 #88 #89
#98 #100 #105
#106 #107 #109 #112
#123
```

#123 is completed recovery-assurance administration; closing it later preserves its PASS provenance and does not make it WP04 assurance authority.

#96 remains excluded because the consolidated deployed live-app retest after PR #108 and PR #111 remains unproven.

### Stricter action ordering

The retry keeps the explicit governance fence:

```text
exact candidate
→ full Tests
→ fresh blind PASS
→ guarded merge
→ exact-main Tests + GitHub→HF verification
→ only then target issue mutation
→ issue-state readback
```

No product/runtime/UI/recognizer/review/export/Scrub Key/reinsert semantics are changed by this package.

---

## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY

Status: `PASS → MERGED → exact-main verified`.  
Role: `implementation_operations`  
Issue: #121 — closed  
Assurance issue: #123 — exact-head PASS recorded; intentionally left open by its explicit PASS stop rule  
PR: #122 — merged  
Reviewed frozen head: `8565af4e9f579b3a975c6122668f6511a9df627a`  
Merge/main SHA: `14baceb97b274de6ef35c42ce48441c4e74c5f08`

### Trigger

PR #120 was merged before the fresh blind `governance_release_assurance` verdict required by D042 and `SCRUB_RELEASE_ASSURANCE_CONTRACT_V1`. Issue #74 was then closed before that verdict. The later fresh assurance returned formal `FAIL` because independent assurance is a **pre-action ordering control** and cannot be supplied retroactively by green CI or a technically correct merge.

### Recovery outcome

- no force reset or history rewrite;
- issue #74 reopened with explicit governance-recovery provenance;
- accepted PR #118 / D045 truth preserved;
- failed PR #120 candidate-specific claim/test/handover removed from active recovery authority while Git retains provenance;
- #96 remained open and its consolidated deployed live-app retest remained unproven;
- no WP04 issue reconciliation was performed;
- fresh assurance PASS was recorded on exact PR #122 head before merge;
- PR #122 was guarded-merged without head movement;
- issue #121 was closed only after exact-main confirmation.

Exact-main recovery evidence:

```text
Tests run 33966351441 / job 101307057966
1272 passed in 14.44s
SUCCESS

GitHub → Hugging Face sync run 33966351286 / job 101307057815
SUCCESS
```

A new WP04 candidate must start from `14baceb...`; recovery assurance does not authorize WP04 issue mutation.

---

## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION — FAILED FIRST RELEASE SEQUENCE

Status: `GOVERNANCE FAIL — PREMATURE MERGE; RECOVERED BY WP-CONVERGENCE-04R`.  
Role: `implementation_operations`  
Issue: #119 — remains open for the fresh retry  
PR: #120 — prematurely merged  
Candidate base: `268d967db95d923a73a3979ffce2d0cab586e499`  
Frozen candidate head: `1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a`  
Premature merge/main SHA: `fd69294c67a59bb150f5d4a637daad2607c14077`

### Root cause addressed by the candidate

The live GitHub issue set exposed 18 historical/current Premium/governance tickets as open. Most describe candidate states later failed, superseded, independently PASSed, repaired or merged. The substantive reconstruction supported keeping #96 open and treating 17 others as future evidence-backed closure candidates.

### Candidate validation history

Three red CI cycles were retained as evidence:

```text
33931758642 / 101211615952
1 failed, 1271 passed in 8.98s
→ parser incorrectly included explanatory PR references in the keep-open set

33931829877 / 101211823357
1 failed, 1271 passed in 8.61s
→ residual-gate wording differed between current-control files

33931948111 / 101212181362
1 failed, 1271 passed in 14.43s
→ absence of live-retest proof was not yet encoded explicitly as `remains unproven`
```

Pre-final green:

```text
head b33b7e765ede9b9d99586b82b846035143d3782a
Tests run 33932036674
job 101212447162
1272 passed in 14.68s
SUCCESS
```

Final frozen candidate:

```text
head 1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a
Tests run 33932180435
job 101212872885
1272 passed in 16.24s
SUCCESS
```

The candidate content was later found materially sound, but that does not cure release ordering.

### Governance failure

Required order:

```text
exact candidate
→ fresh blind independent assurance
→ PASS
→ merge / issue mutation
```

Actual order:

```text
exact candidate
→ premature merge fd69294c67a59bb150f5d4a637daad2607c14077
→ issue #74 prematurely closed
→ fresh blind assurance
→ FAIL
```

Post-merge Tests and HF sync on `fd69294...` were technically green, but are not a substitute for the missing pre-action assurance gate.

Only #74 had been mutated when the FAIL stopped further reconciliation. #74 was then reopened by WP-CONVERGENCE-04R. #96 remained open. The remaining 16 intended closure issues were never closed by the failed action sequence.

---

## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION

Status: `PASS → MERGED → exact-main verified`.  
Role: `implementation_operations`  
Issue: #117 — closed  
PR: #118 — merged  
Reviewed frozen head: `37de6859ed5b17f4767c463f6db73085ce0d4b56`  
Merge/main SHA: `268d967db95d923a73a3979ffce2d0cab586e499`

### Root cause

The repository contains several generations of mature validation assets, but historical wording could make diagnostic benchmark/report paths look like competing release authorities.

Source reconstruction established that:

- `.github/workflows/tests.yml` runs the full committed `tests/` suite and is the exact-SHA regression gate used for consequential candidates and `main`;
- focused Phase-6, Scrub Key, document, Zorg, recognizer and Premium/AppTest suites provide capability-level regression evidence within that full gate;
- `recall_benchmark_report.py` explicitly identifies itself as `diagnostic_only`, with `production_gate=False` and `thresholds_enforced=False`;
- WP22 scores supplied predictions and does not invoke recognizers;
- WP23/WP24 are report-only/non-gating and retain coverage limitations.

### Smallest complete fix

- D045 records one release regression authority and subordinate evidence roles;
- ROADMAP validation wording is aligned to D045;
- the temporary convergence ledger classifies the evidence generations explicitly;
- one narrow contract test validates actual workflow/source metadata plus the binding decision;
- obsolete bootstrap tests were rebound to current semantic convergence invariants rather than stale wording/status placement;
- no runner, corpus, recognizer, threshold, workflow implementation or product/runtime behavior changed;
- no diagnostic score was promoted to a merge/production gate.

### Validation history

Initial candidate:

```text
Tests run 33930040668
job 101206596706
4 failed, 1264 passed in 14.74s
```

The four failures were stale governance/format contracts: the historical `WP-CONVERGENCE-02..N` placeholder, already-resolved Docker startup debt, duplicate Evidence-Framework prose in the temporary ledger, and a Markdown-format-specific workflow-path assertion. The underlying invariants were retained.

Corrected pre-final candidate:

```text
head 2147c854b344e628515076a624efc6176a74ca84
Tests run 33930216093
job 101207097941
1268 passed in 13.72s
SUCCESS
```

Final frozen head `37de6859ed5b17f4767c463f6db73085ce0d4b56` received fresh blind `PASS`.

Post-merge evidence on exact main `268d967db95d923a73a3979ffce2d0cab586e499`:

- `Tests` run `33930953130`: SUCCESS, `1268 passed in 11.68s`;
- GitHub→Hugging Face sync run `33930953103`: SUCCESS;
- HF remote acknowledged `7e4f549..268d967 HEAD -> main`;
- app verification: N/A because no application/runtime/UI behavior changed;
- issue #117 closed after PASS, guarded merge and post-merge evidence.

---

## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT

Status: `PASS → MERGED → exact-main verified`.  
Role: `implementation_operations`  
Issue: #115 — closed  
PR: #116 — merged  
Reviewed frozen head: `cbaaa1e4560670116c41ca788786d80d670dcf34`  
Merge/main SHA: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`

### Root cause

Docker still executed `fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py` before every Streamlit start even though current direct-source markers made both historical mutation paths unnecessary.

### Smallest complete fix

- Docker now launches `presidio_streamlit.py` directly through Streamlit;
- existing port/address/XSRF/CORS flags are unchanged;
- historical compatibility scripts remain for a later evidence-based retirement decision;
- four Docker-coupled tests were rebound from obsolete startup ordering to current direct-source/no-runtime-mutation invariants;
- no product/runtime semantics beyond obsolete startup invocation changed.

Final reviewed head `cbaaa1e4560670116c41ca788786d80d670dcf34` received fresh blind `PASS`.

Post-merge evidence on exact main `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`:

- `Tests` run `33929193443`: SUCCESS, `1264 passed in 15.15s`;
- GitHub→Hugging Face sync run `33929193466`: SUCCESS;
- HF remote confirmed `255cd61..7e4f549 HEAD -> main`;
- public Space health was Running/serving;
- functional app retest: N/A because no product/UI behavior changed.

---

## 2026-09-04/05 — SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP

Status: `PASS → MERGED → exact-main verified`.  
Role: `implementation_operations`  
Issue: #113 — closed  
PR: #114 — merged  
Reviewed frozen head: `8028643ed2f11b9f43bf32854e2d4cf86fb387f0`  
Merge/main SHA: `255cd619d5cf6eab32f9383940eaa4af362cb68c`

### Outcome

- exact pre-convergence baseline preserved at `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`;
- old full changelog preserved byte-identically in `history/CHANGELOG_PRE_CONVERGENCE_20260904.md`;
- five-stage roadmap adopted;
- WORKPACKAGES reduced to one current executable queue;
- D044 records Repository Convergence → Scrub Private direction;
- critical product risks retained and source-of-truth/runtime-mutation risks made explicit;
- temporary capability-level convergence ledger established;
- existing product/evidence architecture preserved rather than rebuilt.

Two earlier frozen heads received independent `FAIL` verdicts and were remediated without runtime/product changes. Final reviewed head `8028643ed2f11b9f43bf32854e2d4cf86fb387f0` received fresh blind `PASS`.

Post-merge evidence on exact main `255cd619d5cf6eab32f9383940eaa4af362cb68c`:

- `Tests` run `33925330688`: SUCCESS, `1264 passed`;
- GitHub→Hugging Face sync run `33925330710`: SUCCESS;
- app verification: N/A because the bootstrap changed no runtime/UI behavior.
