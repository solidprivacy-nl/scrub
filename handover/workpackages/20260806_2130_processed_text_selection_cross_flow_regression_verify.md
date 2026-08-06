# Handover — SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION_VERIFY

Repository: `solidprivacy-nl/scrub`  
Role: `governance_release_assurance`  
Initial assurance decision: `PASS`  
Closeout status: `ACTION_EXECUTED_UNVERIFIED`

## Summary

Independently verified PR #69's synthetic processed-text selection cross-flow regression. The initial decision was recorded before implementation handovers, claims or implementation conclusions were opened. No candidate repair was performed. After PASS, the administrative implementation records were checked and found complete. PR #69 was then merged unchanged.

## Candidate identity

- Base: `1cc0aa110d9aa33ca43fe423b94200c1dff08f6d`
- Head: `41bf09abe3966ae40a51c526d162c57a824557e8`
- Tested merge candidate: `13d55b6d74ad6f31446e16bcad0794abea32f9e7`
- Actual merge commit: `07cf12d0cfa57dd81bd2c964cb081e5f8f8c4f71`
- Actual/tested tree: `4c993cbed86eade252cec6799f7dae5919b84085`

## Decision evidence

The added tests exercise the real production helper chain and prove:

- one normal document-scoped included `manual_selection` row;
- `all_exact` scope with the exact two-occurrence impact;
- processed-text/TXT replacement and original-DOCX replacement;
- one valid schema-1.1 bound Scrub Key mapping;
- verified TXT and DOCX reinsert with exact source restoration;
- replacement CSV and scrub-report audit evidence;
- authoritative `include=false` omission;
- document-exportable custom replacement with fail-closed verified bound-key validation;
- local-only, no-AI and no-cloud metadata.

The exact candidate diff contains no production Python, Streamlit, frontend, runtime, dependency, workflow or deployment changes.

## Files added by this verification closeout

- `workpackage_claims/scrub_wp_processed_text_selection_cross_flow_regression_verify.md`
- `handover/workpackages/20260806_2130_processed_text_selection_cross_flow_regression_verify.md`

## Files changed by this verification closeout

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests and machine evidence

- Raw workflow: Tests run #2105 / run ID `31091265208`
- Tested object: merge candidate `13d55b6d74ad6f31446e16bcad0794abea32f9e7`
- Command: `python -m pytest -q tests`
- Result: `1165 passed in 12.41s`
- Workflow conclusion: success
- Actual merge and tested merge candidate have identical parents and identical tree.

## Validation

- Initial governance decision: `PASS`
- Candidate repair: none
- Candidate merge: completed as `07cf12d0cfa57dd81bd2c964cb081e5f8f8c4f71`
- GitHub Actions on actual merged SHA: no distinct push run observable at handover time
- Post-action status: `ACTION_EXECUTED_UNVERIFIED`; `OUTCOME_CONFIRMED` deliberately not claimed
- Hugging Face sync: not applicable; no runtime files changed and changed paths are ignored by the sync workflow
- App verification: not applicable; no UI behavior changed

## Remaining risks

- Current DOCX limitations remain unchanged: split placeholders, comments, tracked-change-only parts, footnotes/endnotes, text boxes and metadata are outside the supported reinsert surface.
- The missing distinct post-merge run prevents the stricter `OUTCOME_CONFIRMED` status at this point.

## Next recommended step

- Complete the documentation-only closeout PR.
- Confirm the required post-action evidence before promoting this package to `OUTCOME_CONFIRMED`.
- Once confirmed, the regression gate no longer blocks `SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT`.