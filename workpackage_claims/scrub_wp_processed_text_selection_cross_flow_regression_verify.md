# Workpackage claim — SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION_VERIFY

Status: completed  
Assurance decision: `PASS`  
Closeout status: `ACTION_EXECUTED_UNVERIFIED`

Claimed: 2026-08-06 21:23 Europe/Amsterdam  
Initial decision recorded: 2026-08-06 21:26 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Candidate PR: `#69`  
Candidate head: `41bf09abe3966ae40a51c526d162c57a824557e8`  
Tested merge candidate: `13d55b6d74ad6f31446e16bcad0794abea32f9e7`  
Merged commit: `07cf12d0cfa57dd81bd2c964cb081e5f8f8c4f71`  
Role: `governance_release_assurance`

## Blind-review boundary

The initial `PASS` was recorded on issue #70 before opening any file under `handover/workpackages/` or `workpackage_claims/`, and without relying on implementation conclusions in `CHANGELOG.md`, `WORKPACKAGES.md`, or the PR narrative.

## Independent evidence

The five synthetic tests use the production selection inspect/commit route and production export, Scrub Key, reinsert and audit helpers. They verify:

- one document-scoped included `manual_selection` row with `all_exact` scope and two occurrences;
- processed-text/TXT and original-DOCX replacement;
- schema-1.1 bound Scrub Key creation and validation;
- verified TXT and DOCX reinsert with exact source restoration;
- replacement CSV and scrub-report evidence;
- authoritative `include=false` omission;
- free custom replacement remaining document-exportable while verified bound-key generation fails closed;
- local-only, no-AI and no-cloud metadata.

The base/head comparison contained no production Python, Streamlit, frontend, runtime, dependency, workflow or deployment change. The only executable addition was the regression test.

## Administrative review after PASS

The implementation claim and handover were opened only after the initial decision. They were complete and disclosed no contradictory or hidden scope. Their stated supported DOCX limitations match the production helper boundaries.

## Action and validation

- PR #69 was merged without candidate repair or head modification.
- Actual merge commit parents exactly match the tested merge candidate parents.
- Actual merge tree `4c993cbed86eade252cec6799f7dae5919b84085` exactly matches the tested merge-candidate tree.
- Raw PR run #2105 executed `python -m pytest -q tests` on merge candidate `13d55b6d74ad6f31446e16bcad0794abea32f9e7` and returned `1165 passed in 12.41s`.
- A distinct GitHub Actions push run on merged SHA `07cf12d0cfa57dd81bd2c964cb081e5f8f8c4f71` was not yet observable when this claim was written; therefore `OUTCOME_CONFIRMED` is not claimed here.
- Hugging Face sync: not applicable because no runtime file changed and all changed paths are excluded from the sync workflow.
- App verification: not applicable because no UI behavior changed.

## Remaining risks

- The regression covers current supported TXT/DOCX surfaces and does not expand known DOCX limitations such as split placeholders, comments, tracked-change-only parts, footnotes/endnotes, text boxes or metadata.

## Next step

Record the separate verification handover, complete the documentation-only closeout PR, and promote to `OUTCOME_CONFIRMED` only when the required post-action evidence is available.