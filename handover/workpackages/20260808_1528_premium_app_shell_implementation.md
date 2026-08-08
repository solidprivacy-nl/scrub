# Handover — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION

Repository: `solidprivacy-nl/scrub`  
Workpackage title: `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — integrate premium staged workspace`  
Role: `implementation_operations`  
Status: `RELEASE_CANDIDATE_READY — independent assurance pending`

## Summary

Implemented the first production Premium Core Flow shell in Streamlit under the merged staged-workspace decision:

```text
One document. One workspace. Three stages. One active task.
Toevoegen → Controleren → Downloaden
```

The Standard flow is now orchestrated as one persistent workspace with exactly one dominant stage, compact completed-stage summaries, passive future stages, explicit return, automatic processing/review progression and fail-closed lineage invalidation. Expert remains available for advanced controls. Reinsert remains a separate top-level workflow.

This workpackage intentionally stops at the shared shell. It does not claim that the separate Input, Review or Export stage simplification workpackages are complete.

## Files added

- `premium_streamlit_state.py`
- `premium_streamlit_shell_ui.py`
- `tests/test_premium_streamlit_state.py`
- `tests/test_premium_app_shell_streamlit_integration.py`
- `workpackage_claims/scrub_wp_premium_app_shell_implementation.md`
- this handover

## Files changed

- `premium_app_shell.py`
- `presidio_streamlit.py`
- `fix_streamlit_nested_expanders.py`
- selected source-level UI contract tests whose literal expectations described the retired form/two-mode shell:
  - `tests/test_care_profile_current_ui_integration_snapshot.py`
  - `tests/test_duplicate_input_surface_simplification_contracts.py`
  - `tests/test_export_sanity_ui_patch.py`
  - `tests/test_premium_app_shell.py`
  - `tests/test_reinsert_interface_simplification_ui.py`
  - `tests/test_review_export_vertical_density_contracts.py`
- `CHANGELOG.md`, `WORKPACKAGES.md`, and `RELEASE_NOTES.md` are finalized in the administrative closeout commit after this handover is written.

## Main implementation

- global `Anonimiseren | Terugzetten` workflow choice;
- global `Standaard | Expert` presentation choice;
- Standard starts with the permanent sidebar collapsed/absent as the primary interaction surface;
- persistent stage headers for Add, Review and Download;
- one active Standard stage at a time;
- completed-stage summaries and passive future-stage status;
- `Document verwerken` as Add progression action;
- `Controle afronden` as Review progression action;
- explicit return through completed-stage `Openen` actions;
- deterministic source/processing generation tracking;
- fail-closed invalidation on processing-affecting changes;
- reopening completed Review invalidates Download until Review is completed again;
- current-generation analysis is cached so stage navigation does not silently re-run recognition;
- current Review rows are cached so return/navigation does not silently reconstruct a different review state;
- Expert-only `highlight` / `synthesize` modes are not silently converted when Standard is selected;
- the legacy runtime source patch exits early when the direct Premium shell is present, preventing startup from restoring the retired form UI.

## Tests

Added/expanded pure state, staged-shell and source integration contracts covering:

- active/completed/future stage semantics;
- exactly one active stage;
- compact summaries;
- Add → Review and Review → Download transitions;
- return-to-Add lineage preservation;
- return-to-Review fail-closed export invalidation;
- deterministic processing generation;
- analysis cache lifecycle;
- workflow/presentation state changes;
- no three-page routing;
- no nested expander shell;
- no permanent Standard sidebar;
- no hidden re-analysis on navigation;
- no silent Expert-only operator mutation;
- legacy runtime patch bypass;
- unchanged export and Scrub Key payload markers.

Normal GitHub Actions evidence on the clean runtime/product head before administrative finalization:

```text
Head: 0e1a5fbb3d6c3b8f8293779e598ececd6ea4aa1d
Tests run #2200 / ID 31259576962
Job: 93108182555
Command: python -m pytest -q tests
Result: 1225 passed in 12.55s
Conclusion: success
```

A fresh full regression on the final post-administration PR head remains mandatory because the administrative closeout commits change candidate identity.

## Validation status

- GitHub Actions: `GREEN` on clean runtime/product head; final exact-head administrative candidate run pending.
- Hugging Face sync: `PENDING AFTER MERGE`; runtime UI changed, so exact merged candidate must be synchronized and verified.
- App verification: `PENDING AFTER MERGE/DEPLOYMENT`; required because UI behavior changed.
- Independent governance assurance: `PENDING`; implementation cannot self-certify.

## Intentionally unchanged

- recognizers and profile rules;
- threshold meaning/recognizer processing semantics;
- authoritative review-table/include state;
- direct masking semantics;
- export bytes, filenames and MIME types;
- Scrub Key schema, binding and lifecycle;
- reinsert semantics;
- audit semantics;
- dependencies;
- cloud/local-processing boundary;
- mandatory human review.

## Remaining risks

- Live Streamlit/Hugging Face behavior still requires exact deployment verification; source and regression tests cannot establish subjective UX quality or browser interaction fidelity.
- This App Shell exposes the staged architecture but does not complete the subsequent dedicated Input, Review and Export visual simplification packages.
- Exact-head assurance must check the larger `presidio_streamlit.py` integration independently rather than trusting implementation conclusions.

## Next recommended step

1. complete administrative closeout without further runtime changes;
2. run the full suite on the final exact PR head;
3. freeze candidate identity;
4. fresh blind `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_VERIFY` by `governance_release_assurance`;
5. if PASS, merge unchanged;
6. verify exact-main Actions and GitHub → Hugging Face sync;
7. request coordinator live-app verification;
8. only after closeout, start `SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION`.
