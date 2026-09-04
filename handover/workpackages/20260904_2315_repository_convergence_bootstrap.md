# Handover — SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Issue: #113  
Branch: `wp/repository-convergence-bootstrap`  
Starting main: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Status: `IMPLEMENTATION_IN_PROGRESS` — candidate administration prepared; exact-head CI and fresh independent assurance pending.

## Summary

Started the approved Repository Convergence programme without changing Scrub runtime product behavior.

The package:

- preserved the exact pre-convergence baseline by SHA;
- confirmed exact-main `Tests` and GitHub→Hugging Face sync were green at package start;
- reconstructed current reachable architecture far enough to distinguish canonical capability, genuine debt candidates and variant-specific Private conflicts;
- replaced stale roadmap/workpackage routing with one current Repository Convergence line;
- aligned worker/governance documentation while preserving the two-role assurance model;
- converted DECISION_LOG and RISK_REGISTER from historical execution narratives into current-truth documents while preserving the exact pre-convergence state in Git;
- archived the full pre-convergence CHANGELOG byte-for-byte and started a clean post-convergence changelog;
- added source-level contracts protecting the new current-truth model.

## Baseline preservation

Authoritative pre-convergence SHA:

```text
54c73e0ebf5a3a3ed7039a50596fb57694add3cd
```

At package start:

- GitHub main: exact SHA above;
- Tests workflow: success on exact main;
- Sync to Hugging Face Space: success on exact main.

No source clone (`app_v2`, `scrub-new`, duplicate Streamlit main) was created.

## Files added

- `REPOSITORY_CONVERGENCE_DEBT_LEDGER.md`
- `tests/test_repository_convergence_bootstrap_contracts.py`
- `workpackage_claims/SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP.md`
- `handover/workpackages/20260904_2315_repository_convergence_bootstrap.md`
- `history/CHANGELOG_PRE_CONVERGENCE_20260904.md` — exact pre-convergence CHANGELOG blob, historical/non-authoritative.

## Files changed

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `PROJECT_PROMPT.md`
- `PROJECT_PROMPT_SHORT.md`
- `AGENTS.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `CHANGELOG.md`

## Current audit findings

### Canonical capability to preserve

- Premium staged workspace and generation-bound source/analysis/review/export state;
- mandatory review authority, review table and direct/manual correction;
- bound Scrub Key + mapping digest + fail-closed reinsert validation;
- Legal/Dutch and Zorg recognition/profile policy;
- TXT/DOCX/text-PDF handling and DOCX hygiene/fidelity boundaries;
- existing recognizer benchmark, domain evidence, Phase-6 E2E, Scrub Key/document suites and Premium AppTests.

### Variant-specific / Private-incompatible capability

- persistent remembered replacements (`replacement_memory.py` and Expert UI);
- Azure AI Language external document recognition;
- OpenAI/Azure synthesis;
- content-bearing synthesis prompt logging.

These are recorded but intentionally not changed in this Stage-1 bootstrap. Their Private disposition belongs after the clean baseline unless current evidence proves an immediate reference-environment safety defect.

### Retire candidates

- Docker still invokes `fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py` even though current Premium/direct-source markers make both exit without mutating source.

This requires an isolated proof/retirement package, not deletion in the bootstrap.

### Evidence-authority reconciliation

- current recognizer-backed recall workflow appears to be the primary automated recognition diagnostic path;
- older entity-scorecard/residual-risk helpers remain useful within explicit report-only limitations;
- Phase-6 E2E, Zorg, Scrub Key/document and Premium AppTest evidence are complementary;
- a narrow hierarchy package should classify existing paths as canonical release validation, supplemental diagnostic or historical/superseded without building a new framework or inventing thresholds.

### GitHub issue truth

- #112 and #109 contain independent PASS evidence for PR #111/#108, both of which are merged; these are stale as active candidate gates;
- #107/#106 correspond to merged child repairs and require stale-state reconciliation;
- #105/#96 additionally required a final consolidated deployed live retest after those repairs. No evidence found in this implementation session proves that final retest occurred. Do not falsely close it as verified.

## Tests

Added:

```text
tests/test_repository_convergence_bootstrap_contracts.py
```

Contracts cover:

- exactly five strategic roadmap stages;
- one current WORKPACKAGES queue without historical overrides;
- preserved worker start/governance/safety rules;
- current Repository Convergence / Scrub Private routing;
- temporary/non-authoritative debt-ledger semantics;
- retained still-binding review/Zorg/Scrub Key/reinsert/document decisions;
- critical R1/R2/R10 continuity plus new current R5/R11/R12 risks;
- archived pre-convergence changelog preservation;
- bounded HF application-assurance wording;
- rejection of source cloning/new Evidence Framework.

## Validation

- Local execution: unavailable in the connector-only implementation environment.
- Candidate diff at pre-CI review: documentation/governance/tests/administration only; no runtime product source changed.
- GitHub Actions: pending exact-head PR run.
- Hugging Face sync: runtime behavior unchanged; final path-ignore/sync status to be checked after authorized merge.
- App verification: not applicable for this package because no product/UI/runtime behavior changes.
- Independent assurance: pending fresh `governance_release_assurance` after exact-head CI.

## Intentionally unchanged

- recognizers/profile/threshold semantics;
- review/include/replacement authority;
- export payloads, filenames and MIME types;
- Scrub Key schema/binding/lifecycle;
- reinsert behavior;
- document-processing behavior;
- runtime dependencies;
- Docker/Streamlit runtime product behavior;
- current replacement-memory/external-provider functionality;
- mandatory human review.

## Remaining risks / blockers

- Exact-head GitHub Actions must pass.
- A fresh independent assurance worker must issue PASS before merge; implementation cannot self-certify.
- The later technical cleanup queue must remain audit-derived rather than pre-invented.
- Parent Premium live-verification state (#105/#96) is not yet proven closed.

## Next recommended step

1. Open the bootstrap PR and run exact-head full CI.
2. Fix only concrete CI/contract defects, if any.
3. Freeze the exact final head and update this handover/claim to `RELEASE_CANDIDATE_READY` with raw CI evidence.
4. Dispatch a fresh blind `governance_release_assurance` review.
5. Merge only on PASS; verify exact-main Actions/HF sync handling.
6. Continue autonomously with the evidence-backed convergence packages derived from the ledger.
