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

## 2026-09-05 — SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT

Status: `IMPLEMENTATION IN PROGRESS`; independent assurance required before merge.  
Role: `implementation_operations`  
Issue: #115  
PR: #116  
Base: `255cd619d5cf6eab32f9383940eaa4af362cb68c`

### Root cause

Docker still executed `fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py` before every Streamlit start even though current direct-source markers make both scripts exit without mutation.

### Smallest complete fix

- Docker now launches `presidio_streamlit.py` directly through Streamlit;
- existing port/address/XSRF/CORS flags are unchanged;
- the historical compatibility scripts remain in the repository for a later evidence-based retirement decision;
- four Docker-coupled tests are rebound from the old invocation order to the current direct-source/no-runtime-mutation invariant;
- no `presidio_streamlit.py`, recognizer, review, export, Scrub Key, reinsert, persistence, external-AI or dependency behavior is changed.

### Validation history

The first implementation head exposed three additional legacy tests that still required the historical startup chain:

```text
3 failed, 1261 passed
```

Those failures were confined to Docker-order assertions in export, Scrub Key warning and static-highlight rollback tests. Their underlying product contracts were retained while the obsolete startup-placement assertions were removed.

A final exact-head full regression and fresh blind `governance_release_assurance` PASS remain mandatory before merge.

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
