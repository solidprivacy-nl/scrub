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

Status: `IMPLEMENTATION_IN_PROGRESS` / candidate preparation; independent assurance required before merge.

Role: `implementation_operations`  
Issue: #113  
Branch: `wp/repository-convergence-bootstrap`  
Starting main: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`

### Purpose

- preserve the exact mature pre-convergence product state;
- stop stale ROADMAP/WORKPACKAGES/issues from routing new work incorrectly;
- reconstruct current reachable capability before deleting or rebuilding anything;
- establish Repository Convergence as the active stage before Scrub Private adaptation;
- distinguish genuine technical debt from valid but Private-incompatible variant functionality;
- keep the existing validation framework and identify its current release-authority hierarchy rather than building another one.

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

- `ROADMAP.md` — reduced to five strategic stages: Repository Convergence → Scrub Private Application → Private Service → External Product & Service Assurance → Pilot;
- `WORKPACKAGES.md` — replaced multiple historical current-status overrides with one active convergence queue;
- `PROJECT_PROMPT.md` — preserved governance/safety rules while aligning product direction and current-stage routing;
- `PROJECT_PROMPT_SHORT.md` — aligned bootstrap worker instructions;
- `AGENTS.md` — aligned claim/worker routing and convergence/refactor discipline;
- `DECISION_LOG.md` — added D044 and retained concise still-binding Premium, Zorg, review, Scrub Key, reinsert and DOCX decisions; detailed prior history remains at the pre-convergence SHA;
- `RISK_REGISTER.md` — preserved critical product risks and added explicit current risks for Private retention/egress, source-of-truth drift and legacy startup mutation;
- `CHANGELOG.md` — started the post-convergence log after preserving the exact historical file.

### Audit findings captured without runtime changes

- current Premium staged workspace/generation state is mature current capability and should not be rebuilt from stale queue entries;
- review authority/direct correction, Scrub Key binding/reinsert, Legal/Zorg recognizers and supported document handling are current canonical capability;
- persistent replacement memory is valid full-feature/possible Local functionality but is `VARIANT-SPECIFIC` and conflicts with the future Scrub Private no-content-persistence boundary;
- Azure AI Language and OpenAI/Azure synthesis are `VARIANT-SPECIFIC` external-processing paths that conflict with the Scrub Private no-third-party-document-processing baseline;
- the synthesis helper currently prints a content-bearing prompt, a future Private logging blocker;
- Docker still invokes legacy Streamlit mutation scripts, while current Premium/direct-source markers make both scripts exit without mutating source; this is a `RETIRE` candidate to verify in an isolated technical package;
- multiple evidence generations exist; recognizer-backed recall workflow, Phase-6 E2E, Zorg evidence, Scrub Key/document tests and Premium AppTests must be classified into a clear current validation hierarchy rather than replaced;
- several open GitHub issues describe candidate states that have already PASSed/merged, while the final parent Premium deployed retest remains unproven and must not be falsely closed.

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

### Validation required before merge

- source-level convergence contract tests;
- full exact-head GitHub Actions regression;
- exact diff/scope review confirming docs/governance/tests/administration only;
- fresh blind `governance_release_assurance` PASS;
- exact-main Actions after authorized merge;
- HF sync/path-ignore verification as applicable;
- no app verification required for this package because product behavior is unchanged.
