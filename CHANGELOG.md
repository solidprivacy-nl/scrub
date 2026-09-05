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

## 2026-09-06 — SCRUB-WP_REPOSITORY_CONVERGENCE_LIVE_APP_GATE_ALIGNMENT

Status: `IMPLEMENTATION IN PROGRESS — current-truth alignment candidate; #96 live outcome remains unproven`.  
Role: `implementation_operations`  
Parent live gate: #96 — OPEN  
Branch: `wp/repository-convergence-live-app-gate-alignment`  
Exact starting main/base: `2d4ab0446c20f08ad07576af326ab4b0df0a2af7`

### Trigger

WP04 has now fully completed, but its merged canonical control files still described WP04/#119 as current/open because those files were intentionally frozen before the independent PASS/merge/post-merge administrative sequence.

The actual governed state after issue #126 is:

- PR #124 independently PASSed exact head `ce021443303cfa11de12f3273f872b2d027da5db` before merge;
- guarded merge/main `2d4ab0446c20f08ad07576af326ab4b0df0a2af7`;
- exact-main Tests run `33997889522`: `1279 passed in 14.51s`, SUCCESS;
- GitHub→Hugging Face sync run `33997889554`: SUCCESS on the same SHA;
- the reviewed 18 historical issues are closed;
- #119 and assurance #126 are closed after readback;
- #96 is the sole remaining open product-facing gate.

### Smallest complete alignment

- mark WP-CONVERGENCE-04 completed with exact evidence;
- make WP-CONVERGENCE-05 / #96 consolidated deployed live-app verification the sole current Repository Convergence package;
- rebind convergence tests from stale `WP04 CURRENT` assertions to factual `WP04 COMPLETED / WP05 CURRENT` invariants;
- align R11 and the temporary convergence ledger;
- close the WP04 implementation claim to factual outcome-confirmed state;
- add one narrow WP05 alignment claim/test/handover;
- change no runtime/product/UI/recognizer/review/export/Scrub Key/reinsert semantics.

The actual #96 live verification is not claimed by this package. CI/HF sync do not substitute for it.

---

## 2026-09-05/06 — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION — COMPLETED FRESH RETRY

Status: `PASS → GUARDED MERGE → exact-main verified → issue-state reconciliation confirmed`.  
Role: `implementation_operations`  
Issue: #119 — closed  
Assurance: #126 — closed  
PR: #124 — merged  
Reviewed frozen head: `ce021443303cfa11de12f3273f872b2d027da5db`  
Merge/main SHA: `2d4ab0446c20f08ad07576af326ab4b0df0a2af7`

### Why the retry existed

The first WP04 candidate in PR #120 was materially sound in content but governance-invalid as action authority because it merged and issue #74 mutated before the required independent assurance verdict. Governed recovery PR #122 restored a valid release lifecycle and created exact main `14baceb97b274de6ef35c42ce48441c4e74c5f08`.

The first fresh-retry freeze `06198ec05907c32b41ecc2876d8ca1fb0d3554eb` was green, but before any assurance verdict implementation reconstructed the live issue inventory and found completed recovery-assurance issue #123 still open. That freeze was deliberately broken and #123 was added to the historical/completed closure set.

### Final governed outcome

The corrected candidate received fresh independent PASS before merge. The guarded merge used exact reviewed head `ce021443303cfa11de12f3273f872b2d027da5db` only.

Post-merge:

```text
Tests run 33997889522
1279 passed in 14.51s
SUCCESS

GitHub → Hugging Face sync run 33997889554
SUCCESS
14baceb..2d4ab04 HEAD -> main
```

Only after both post-merge gates were green were these 18 issues closed as historical/completed/superseded:

```text
#74 #75 #76 #77
#79 #81 #84 #86 #88 #89
#98 #100 #105
#106 #107 #109 #112
#123
```

#96 remained OPEN because the consolidated deployed live-app retest remains unproven. #119 closed only after state readback, and assurance #126 closed last.

Historical PR #120 FAIL, PR #122 recovery PASS and all earlier PASS/FAIL/INDETERMINATE provenance remain intact.

---

## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION_GOVERNANCE_RECOVERY

Status: `PASS → MERGED → exact-main verified`.  
Role: `implementation_operations`  
Issue: #121 — closed  
Assurance issue: #123 — later closed as completed historical administration by WP04  
PR: #122 — merged  
Reviewed frozen head: `8565af4e9f579b3a975c6122668f6511a9df627a`  
Merge/main SHA: `14baceb97b274de6ef35c42ce48441c4e74c5f08`

### Trigger

PR #120 was merged before the fresh blind `governance_release_assurance` verdict required by D042 and `SCRUB_RELEASE_ASSURANCE_CONTRACT_V1`. Issue #74 was then closed before that verdict. The later fresh assurance returned formal `FAIL` because independent assurance is a pre-action ordering control and cannot be supplied retroactively by green CI or a technically correct merge.

### Recovery outcome

- no force reset or history rewrite;
- issue #74 reopened with explicit governance-recovery provenance;
- accepted PR #118 / D045 truth preserved;
- failed PR #120 candidate-specific active authority removed while Git retained provenance;
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

Recovery assurance did not authorize the later WP04 issue reconciliation.

---

## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION — FAILED FIRST RELEASE SEQUENCE

Status: `GOVERNANCE FAIL — PREMATURE MERGE; RECOVERED BY WP-CONVERGENCE-04R`.  
Role: `implementation_operations`  
PR: #120 — prematurely merged  
Candidate base: `268d967db95d923a73a3979ffce2d0cab586e499`  
Frozen candidate head: `1c5ff96f5551e7d82c8ab9c01a80ffa9c97c195a`  
Premature merge/main SHA: `fd69294c67a59bb150f5d4a637daad2607c14077`

### Candidate validation history

```text
33931758642 / 101211615952
1 failed, 1271 passed in 8.98s

33931829877 / 101211823357
1 failed, 1271 passed in 8.61s

33931948111 / 101212181362
1 failed, 1271 passed in 14.43s

pre-final green:
33932036674 / 101212447162
1272 passed in 14.68s

final frozen candidate:
33932180435 / 101212872885
1272 passed in 16.24s
```

The content was later found materially sound, but release ordering remained invalid.

Required order was:

```text
exact candidate
→ fresh blind independent assurance
→ PASS
→ merge / issue mutation
```

Actual order was:

```text
exact candidate
→ premature merge fd69294c67a59bb150f5d4a637daad2607c14077
→ issue #74 prematurely closed
→ fresh blind assurance
→ FAIL
```

Post-merge Tests and HF sync were technically green but did not cure the missing pre-action assurance gate.

---

## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_VALIDATION_HIERARCHY_CLARIFICATION

Status: `PASS → MERGED → exact-main verified`.  
Role: `implementation_operations`  
Issue: #117 — closed  
PR: #118 — merged  
Reviewed frozen head: `37de6859ed5b17f4767c463f6db73085ce0d4b56`  
Merge/main SHA: `268d967db95d923a73a3979ffce2d0cab586e499`

D045 established one release regression authority and subordinate evidence roles without changing product/runtime behavior or creating a new Evidence Framework.

Post-merge evidence:

- Tests run `33930953130`: SUCCESS, `1268 passed in 11.68s`;
- GitHub→Hugging Face sync run `33930953103`: SUCCESS;
- app verification: N/A because no application/runtime/UI behavior changed.

---

## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT

Status: `PASS → MERGED → exact-main verified`.  
Role: `implementation_operations`  
Issue: #115 — closed  
PR: #116 — merged  
Reviewed frozen head: `cbaaa1e4560670116c41ca788786d80d670dcf34`  
Merge/main SHA: `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`

Docker now launches `presidio_streamlit.py` directly. Historical compatibility scripts remain separate dormant RETIRE candidates.

Post-merge evidence:

- Tests run `33929193443`: SUCCESS, `1264 passed in 15.15s`;
- GitHub→Hugging Face sync run `33929193466`: SUCCESS;
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

Outcome:

- exact pre-convergence baseline preserved at `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`;
- old full changelog preserved byte-identically in `history/CHANGELOG_PRE_CONVERGENCE_20260904.md`;
- five-stage roadmap adopted;
- WORKPACKAGES reduced to one current executable queue;
- D044 records Repository Convergence → Scrub Private direction;
- critical product risks retained;
- temporary capability-level convergence ledger established;
- existing product/evidence architecture preserved rather than rebuilt.

Post-merge evidence:

- Tests run `33925330688`: SUCCESS, `1264 passed`;
- GitHub→Hugging Face sync run `33925330710`: SUCCESS;
- app verification: N/A because the bootstrap changed no runtime/UI behavior.
