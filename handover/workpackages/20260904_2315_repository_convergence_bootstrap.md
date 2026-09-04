# Handover — SCRUB-WP_REPOSITORY_CONVERGENCE_BOOTSTRAP

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Issue: #113  
PR: #114  
Branch: `wp/repository-convergence-bootstrap`  
Starting main: `54c73e0ebf5a3a3ed7039a50596fb57694add3cd`  
Status: `IMPLEMENTATION_REMEDIATED` — pre-final full regression green; final exact-head CI and fresh independent assurance still required.

## Summary

Started the approved Repository Convergence programme without changing Scrub runtime product behavior.

The package:

- preserved the exact pre-convergence baseline by SHA;
- confirmed exact-main `Tests` and GitHub→Hugging Face sync were green at package start;
- reconstructed current reachable architecture far enough to distinguish canonical capability, genuine debt candidates and variant-specific Private conflicts;
- replaced stale roadmap/workpackage routing with one current Repository Convergence line;
- aligned worker/governance documentation while preserving the two-role assurance model;
- converted DECISION_LOG and RISK_REGISTER from historical execution narratives into current-truth documents while preserving exact pre-convergence provenance;
- archived the complete pre-convergence CHANGELOG byte-for-byte and started a clean post-convergence changelog;
- added source-level contracts protecting the new current-truth model;
- received a fresh independent FAIL on the first candidate;
- remediated only the eight test/governance inconsistencies identified by that reviewer;
- restored full-suite green without restoring obsolete current queues or changing runtime behavior.

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

Canonical documentation/governance:

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `PROJECT_PROMPT.md`
- `PROJECT_PROMPT_SHORT.md`
- `AGENTS.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `CHANGELOG.md`

Governance/contract tests remediated after independent FAIL:

- `tests/test_repository_convergence_bootstrap_contracts.py`
- `tests/test_mvp_document_fidelity_pr_final_contracts.py`
- `tests/test_premium_core_flow_ui_realignment_plan.py`
- `tests/test_premium_staged_workspace_decision.py`
- `tests/test_reinsert_auto_flow_app_verify_closeout.py`

No runtime/product source file is changed by PR #114.

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

## Independent assurance history

Fresh blind assurance reviewed exact prior head:

```text
ea203abb04f008a7e583387242a6f4917c72e591
```

against base:

```text
54c73e0ebf5a3a3ed7039a50596fb57694add3cd
```

and returned:

```text
FAIL
```

Reviewer findings:

1. exact-head `Tests` run `33920335521` was red: `8 failed, 1256 passed`;
2. two new convergence tests encoded brittle string/prose placement instead of semantic governance contracts;
3. six legacy tests still required historical Premium/fidelity/reinsert state to remain in current ROADMAP/WORKPACKAGES/CHANGELOG positions.

The reviewer also independently found:

- scope integrity good;
- five-stage roadmap materially coherent/minimal;
- still-binding product semantics materially preserved;
- archived pre-convergence changelog preservation appropriate;
- no runtime/HF/product activation occurred.

No prior verdict transfers to a changed head.

## Remediation performed

Only tests/governance contracts were changed.

### New convergence-contract repair

- stage validation now parses formal `## Stage N — ...` headings and compares the exact ordered five-stage set;
- Evidence Framework prohibition now checks a stable semantic prohibition once instead of requiring duplicate prose in multiple files.

### Historical fidelity contract repair

- historical completion/no-duplicate evidence is read from `history/CHANGELOG_PRE_CONVERGENCE_20260904.md` and the historical handover;
- current supported DOCX scope is bound to D030 in `DECISION_LOG.md`;
- current WORKPACKAGES no longer needs to carry the historical fidelity package.

### Premium UI contract repair

- plan/decision artifacts still protect the implemented one-document/staged-workspace semantics;
- current authority is bound to D041/D043 and the current shared-surface sequencing rule;
- obsolete Premium package names/order are explicitly not required in the current queue.

### Reinsert contract repair

- historical app-verification evidence is read from the archived changelog/claim/handover;
- current document-first flow is bound to D031;
- current fail-closed document/key binding is bound to D037;
- old roadmap/workpackage placement is no longer release authority.

## Validation evidence

### Initial exact-head candidate — FAIL evidence

Head:

```text
ea203abb04f008a7e583387242a6f4917c72e591
```

Tests run:

```text
33920335521
```

Result:

```text
8 failed, 1256 passed in 12.64s
```

### Remediated pre-final candidate — GREEN

Head:

```text
dcdfb2c84bbaafe0beca79191bee509b9607b461
```

PR merge candidate checked out by Actions:

```text
ca222802fe5a5c21213df1ed71045fee0826c4ff
```

Tests run:

```text
33922952965
```

Job:

```text
101185112554
```

Raw result:

```text
1264 passed in 12.34s
```

This proves the reviewer-requested test/governance remediation is green.

### Final exact-head status

Administrative claim/handover/changelog/workpackage updates follow this green run and therefore change the branch head. A final exact-head full regression is still mandatory. The final frozen SHA and run must be recorded in the PR conversation without mutating the head again.

## Hugging Face sync status

- Baseline exact-main sync before this workpackage: success.
- PR #114 contains no runtime product change.
- No candidate deployment/app verification is required before merge for this docs/governance/test-only package.
- After authorized merge, verify exact-main Actions and HF sync/path-ignore behavior according to the runbook.

## App verification status

Not applicable for PR #114: no product/UI/runtime behavior changes.

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

- Final administrative head must complete the full `Tests` workflow successfully.
- A completely fresh independent assurance worker must review that exact new frozen SHA and return PASS before merge.
- Prior FAIL is correctly non-transferable to the new head, and any future PASS is likewise exact-head only.
- The later technical cleanup queue must remain audit-derived rather than pre-invented.
- Parent Premium live-verification state (#105/#96) is not yet proven closed.

## Next recommended step

1. Complete final administration without runtime changes.
2. Run full exact-head CI.
3. Freeze the exact final PR head and post the raw run/job/pass count to PR #114 without changing source.
4. Dispatch fresh blind `governance_release_assurance` on that exact SHA.
5. Merge only on PASS; verify exact-main Actions/HF sync handling.
6. Continue with evidence-backed convergence packages derived from the ledger.
