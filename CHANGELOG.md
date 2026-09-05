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

## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_ISSUE_STATE_RECONCILIATION

Status: `IMPLEMENTATION IN PROGRESS`; independent assurance required before merge or issue-state mutation.  
Role: `implementation_operations`  
Issue: #119  
Branch: `wp/repository-convergence-issue-state-reconciliation`  
Base: `268d967db95d923a73a3979ffce2d0cab586e499`

### Root cause

The live GitHub issue set still exposes 18 historical/current Premium/governance tickets as open. Most describe candidate states that were later failed, superseded, independently PASSed, repaired or merged. This stale issue state competes with accepted `main` and the one-current-queue convergence model.

### Evidence-derived target

Repository/issue/PR reconstruction supports one narrow current end-state, subject to fresh independent assurance before any issue mutation:

- keep #96 open as the single residual Premium/App-Shell deployed live-verification gate;
- close #74/#75/#76/#77, #79/#81/#84/#86/#88/#89, #98/#100/#105, #106/#107/#109/#112 as completed or historical/superseded cycles with evidence-aware closeout comments;
- update #96 so the old source-state PASS/FAIL conflict is no longer presented as current: PR #104 V2 independently PASSed and merged; PR #108 marker/compact-display repair independently PASSed and merged; PR #111 Dutch-address precision repair independently PASSed and merged;
- preserve the only unproven requirement: one consolidated deployed live-app retest after both live-regression repairs.

No product/runtime code is changed and no final live verification is claimed by this package.

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

Final frozen head:

```text
37de6859ed5b17f4767c463f6db73085ce0d4b56
```

received fresh blind `PASS`.

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
- the historical compatibility scripts remain in the repository for a later evidence-based retirement decision;
- four Docker-coupled tests were rebound from obsolete startup ordering to current direct-source/no-runtime-mutation invariants;
- no `presidio_streamlit.py`, recognizer, review, export, Scrub Key, reinsert, persistence, external-AI or dependency behavior changed.

### Validation history

The implementation exposed two useful CI cycles before the final candidate:

```text
3 failed, 1261 passed
2 failed, 1262 passed
```

The first identified historical Docker-order assertions. The second correctly detected that a still-binding shared-surface sequencing rule had been dropped during WORKPACKAGES condensation; that rule was restored rather than weakening the tests.

Final reviewed head:

```text
cbaaa1e4560670116c41ca788786d80d670dcf34
```

received fresh blind `PASS`.

Post-merge evidence on exact main `7e4f5491fa6616f9f1b08649a4ed9dfd80de0d84`:

- `Tests` run `33929193443`: SUCCESS, `1264 passed in 15.15s`;
- GitHub→Hugging Face sync run `33929193466`: SUCCESS;
- HF remote confirmed `255cd61..7e4f549 HEAD -> main`;
- public Space health was `Running` and serving the Streamlit app;
- functional app retest: N/A because the removed startup scripts were semantically obsolete and no product/UI behavior changed.

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

### Assurance history

Two earlier frozen heads received independent `FAIL` verdicts: first for eight red governance/document-location tests, then for stale present-tense debt-ledger rows. Both were remediated without runtime/product changes.

Final reviewed head:

```text
8028643ed2f11b9f43bf32854e2d4cf86fb387f0
```

received fresh blind `PASS`.

Post-merge evidence on exact main `255cd619d5cf6eab32f9383940eaa4af362cb68c`:

- `Tests` run `33925330688`: SUCCESS, `1264 passed`;
- GitHub→Hugging Face sync run `33925330710`: SUCCESS;
- app verification: N/A because the bootstrap changed no runtime/UI behavior.
