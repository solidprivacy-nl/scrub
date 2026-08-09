# Handover — SCRUB-WP_REVIEW_MARKER_COMPACTION_LIVE_REGRESSION_REPAIR

Repository: `solidprivacy-nl/scrub`  
Role: `implementation_operations`  
Issue: #106  
PR: #108  
Status: implemented; functional PR CI green; administrative finalization and final exact-head CI pending

## Summary

Coordinator live verification after the independently PASSed and deployed Premium App Shell V2 exposed visibly shifted yellow masking/replacement markers in the processed-text pane. The same shifted boundaries fragmented full document-bound placeholders and caused the previously verified compact display (`[LABEL_NN]`) to fall back to visible full binding tokens.

The root cause was confirmed in `review_highlight_toggle.py`: full processed document text was passed through `.strip()` before exact highlight offsets were computed, while those offsets were subsequently applied to the original untrimmed processed text. Leading DOCX/PDF whitespace therefore shifted every marker left.

The repair separates raw document text from scalar review-cell normalization. Processed text now retains all leading/trailing whitespace for highlight coordinate calculation; review-cell values still use the existing trimmed normalization. No authoritative placeholder token is shortened or mutated.

## Files added

- `tests/test_review_marker_compaction_live_regression.py`
- `workpackage_claims/scrub_wp_review_marker_compaction_live_regression_repair.md`
- this handover

## Files changed

- `review_highlight_toggle.py`
- `CHANGELOG.md` — administration finalization step
- `RELEASE_NOTES.md` — administration finalization step
- `WORKPACKAGES.md` — administration finalization step

## Tests

New regression coverage proves with synthetic data that:

- leading newlines/spaces do not shift processed highlight offsets;
- every highlighted slice equals the complete authoritative full bound placeholder token;
- exact marker boundaries allow the existing display segmenter to render `[ORGANISATIE_02]` and `[LOCATIE_01]` while keeping full source tokens internally;
- marker-off display still compacts strict bound placeholders correctly.

Functional candidate evidence before administration:

- head: `a9e977b2ad21ff4f5c86d405d56ebce60cafe3ec`
- base: `d5586f07b4225c3eef50a8eaee9f0590c60c3298`
- tested PR merge candidate: `5b9af3a09519128d40b842b50fe1421b289ea2bd`
- Tests #2279 / run `31337824222`
- job `93306469803`
- Streamlit `1.61.1`
- command: `python -m pytest -q tests`
- result: `1247 passed in 12.80s`
- conclusion: success

Final exact-head CI remains mandatory after administration is complete.

## Validation

- GitHub Actions: functional candidate green; final administrative head pending exact-head rerun
- Hugging Face sync: not yet applicable; candidate is not merged
- App verification: prior deployed App Shell build failed live verification; fresh verification required after this repair and the separate address precision repair are independently assured, merged and synchronized

## Protected semantics / intentionally unchanged

- recognizers, profiles and threshold meaning;
- Dutch address detection (tracked separately in issue #107);
- review include/replacement authority;
- authoritative full bound placeholder value;
- export bytes, filenames and MIME types;
- Scrub Key schema, document binding and lifecycle;
- reinsert and audit semantics;
- local/cloud processing boundary;
- mandatory human review.

## Governance transparency

During preparation of this repair, an empty `operator_triggers/.keep` file was accidentally created directly on `main` twice. Each accidental add was immediately neutralized by a fast-forward cleanup commit restoring the exact pre-existing repository tree `9ba64fd0cc7994bc2859d910ebddf08605de1339`. The add/cleanup pairs are visible in commit history, but the final tree delta is zero and `operator_triggers/**` is excluded from Hugging Face synchronization. No runtime/product file was changed by those accidental commits.

Relevant cleanup history:

- accidental add `6ad8444a444ed6d22d0e5eaf7b92c3d51e14c718` → clean-tree commit `77d7fedb5eca2248b4985342bec4883b1b911379`;
- accidental add `f76b500f44063cbdaea9190aded69896d999c817` → clean-tree commit `d5586f07b4225c3eef50a8eaee9f0590c60c3298`.

## Remaining risks / follow-up

- issue #107 remains open for the independent Dutch address-span precision defect seen with repeated `Polderweg 8` variants;
- issue #105 and parent #96 remain open because the live app gate failed;
- Premium Input Stage remains blocked;
- this candidate requires fresh independent `governance_release_assurance` before merge.

## Next recommended step

1. Finish branch administration and freeze a final #108 head.
2. Run full exact-head GitHub Actions.
3. Obtain fresh blind assurance for #108.
4. Merge/sync only after PASS.
5. Execute issue #107 separately.
6. Ask the coordinator to re-run the same live document only after both fixes are deployed.
