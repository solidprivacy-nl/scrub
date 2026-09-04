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

## 2026-09-04 — SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP

Status: `IMPLEMENTATION_REMEDIATED`; final exact-head CI and fresh independent assurance required before merge.

Role: `implementation_operations`  
Issue: #113  
PR: #114  
Branch: `wp/repository-convergence-bootstrap`  
Starting main: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`

### Purpose

- preserve the exact mature pre-convergence product state;
- stop stale ROADMAP/WORKPACKAGES/issues from routing new work incorrectly;
- reconstruct current reachable capability before deleting or rebuilding anything;
- establish Repository Convergence as the active stage before Scrub Private adaptation;
- distinguish genuine technical debt from valid but Private-incompatible variant functionality;
- keep the existing validation systems and identify their current release-authority hierarchy rather than building another one.

### Baseline evidence

At package start:

- GitHub `main` = `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`;
- exact-main `Tests` workflow = success;
- exact-main `Sync to Hugging Face Space` = success;
- no duplicate source tree/application clone was created;
- exact SHA is the recovery authority.

### Files added

- `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md` — temporary/non-authoritative capability-level audit ledger;
- `tests/test_repository_convergence_bootstrap_contracts.py` — source-level contracts for current-truth routing;
- `workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP.md`;
- `history/CHANGELOG_PRE_CONVERGENCE_20260904.md` — exact archived pre-convergence changelog blob.

### Files changed

Canonical documentation/governance:

- `ROADMAP.md` — reduced to five strategic stages: Repository Convergence → Scrub Private Application → Private Service → External Product & Service Assurance → Pilot;
- `WORKPACKAGES.md` — replaced multiple historical current-status overrides with one active convergence queue;
- `PROJECT_PROMPT.md` — preserved governance/safety rules while aligning product direction and current-stage routing;
- `PROJECT_PROMPT_SHORT.md` — aligned bootstrap worker instructions;
- `AGENTS.md` — aligned claim/worker routing and convergence/refactor discipline;
- `DECISION_LOG.md` — added D044 and retained concise still-binding Premium, Zorg, review, Scrub Key, reinsert and DOCX decisions; detailed prior history remains at the pre-convergence SHA;
- `RISK_REGISTER.md` — preserved critical product risks and added explicit current risks for Private retention/egress, source-of-truth drift and legacy startup mutation;
- `CHANGELOG.md` — started the post-convergence log after preserving the exact historical file.

Governance/contract tests remediated after independent FAIL:

- `tests/test_repository_convergence_bootstrap_contracts.py`;
- `tests/test_mvp_document_fidelity_pr_final_contracts.py`;
- `tests/test_premium_core_flow_ui_realignment_plan.py`;
- `tests/test_premium_staged_workspace_decision.py`;
- `tests/test_reinsert_auto_flow_app_verify_closeout.py`.

### Audit findings captured without runtime changes

- current Premium staged workspace/generation state is mature current capability and should not be rebuilt from stale queue entries;
- review authority/direct correction, Scrub Key binding/reinsert, Legal/Zorg recognizers and supported document handling are current canonical capability;
- persistent replacement memory is valid full-feature/possible Local functionality but is `VARIANT-SPECIFIC` and conflicts with the future Scrub Private no-content-persistence boundary;
- Azure AI Language and OpenAI/Azure synthesis are `VARIANT-SPECIFIC` external-processing paths that conflict with the Scrub Private no-third-party-document-processing baseline;
- the synthesis helper currently prints a content-bearing prompt, a future Private logging blocker;
- Docker still invokes legacy Streamlit mutation scripts, while current Premium/direct-source markers make both scripts exit without mutating source; this is a `RETIRE` candidate to verify in an isolated technical package;
- multiple evidence generations exist; recognizer-backed recall workflow, Phase-6 E2E, Zorg evidence, Scrub Key/document tests and Premium AppTests must be classified into a clear current validation hierarchy rather than replaced;
- several open GitHub issues describe candidate states that have already PASSed/merged, while the final parent Premium deployed retest remains unproven and must not be falsely closed.

### Independent assurance FAIL and remediation

Fresh blind assurance on exact head:

```text
ea203abb04f008a7e583387242a6f4917c72e591
```

returned `FAIL`.

Blocking evidence:

- `Tests` run `33920335521` → `8 failed, 1256 passed in 12.64s`;
- two new convergence tests encoded brittle global-string/prose-placement requirements;
- six legacy tests still required historical Premium/fidelity/reinsert status to remain in current ROADMAP/WORKPACKAGES/CHANGELOG locations.

The independent reviewer otherwise found scope integrity good, the five-stage roadmap coherent/minimal, important still-binding product semantics materially preserved, and archived historical provenance appropriate.

Implementation remediated only test/governance contracts:

- formal roadmap stage headings are parsed semantically instead of counted as arbitrary global strings;
- one stable semantic Evidence Framework prohibition replaces duplicated-prose authority;
- historical fidelity/reinsert completion evidence is read from archived history/handovers;
- current fidelity/reinsert contracts are bound to D030/D031/D037;
- current Premium Standard/Expert/staged-workspace semantics are bound to D041/D043 and shared-surface sequencing instead of superseded package order.

No runtime/product source changed.

Pre-final green evidence after remediation:

```text
branch head: dcdfb2c84bbaafe0beca79191bee509b9607b461
Tests run: 33922952965
job: 101185112554
merge candidate: ca222802fe5a5c21213df1ed71045fee0826c4ff
result: 1264 passed in 12.34s
```

Administrative closeout commits follow this run, so final exact-head regression remains required before the candidate is frozen and sent to a new blind reviewer.

### Intentionally not changed

This bootstrap package changes no runtime product semantics:

- no recognizer/profile/threshold change;
- no review/include/replacement semantics change;
- no export bytes, filenames or MIME change;
- no Scrub Key schema/binding/lifecycle change;
- no reinsert behavior change;
- no document-processing behavior change;
- no dependency/Docker/Streamlit runtime change;
- no Hugging Face product behavior change;
- no weakening of mandatory human review or privacy controls.

### Final validation required before merge

- full exact-head GitHub Actions regression after final administration;
- exact diff/scope review confirming docs/governance/tests/administration only;
- completely fresh blind `governance_release_assurance` PASS on that exact new head;
- exact-main Actions after authorized merge;
- HF sync/path-ignore verification as applicable;
- no app verification required for this package because product behavior is unchanged.
