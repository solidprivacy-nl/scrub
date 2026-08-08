## 2026-08-08 15:28 Europe/Amsterdam — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — release candidate prepared

Status: `RELEASE_CANDIDATE_READY`; final exact-head CI and fresh independent assurance required before merge.

Purpose:
- move the merged Premium staged-workspace architecture from helper/state primitives into the production Streamlit shell;
- make Standard behave as one persistent document workspace with `Toevoegen → Controleren → Downloaden` and exactly one dominant stage;
- preserve Expert and all existing processing/review/export/Scrub Key/reinsert/audit semantics.

Implemented:
- global `Anonimiseren | Terugzetten` and `Standaard | Expert` controls;
- persistent application-panel stage headers with active/completed/future states;
- compact completed summaries and passive future stages;
- primary `Document verwerken` and `Controle afronden` progression actions;
- explicit earlier-stage return;
- deterministic processing lineage and fail-closed downstream invalidation;
- current-generation analysis cache to prevent silent recognition reruns during stage navigation;
- cached review rows; reopening a completed Review invalidates Download until Review is explicitly completed again;
- Standard hides the permanent settings sidebar while Expert retains advanced controls;
- Standard does not silently modify Expert-only `highlight`/`synthesize` operator choices;
- legacy runtime source patch exits for the direct Premium shell, preventing the retired form/two-mode UI from being re-injected at startup.

Files added:
- `premium_streamlit_state.py`;
- `premium_streamlit_shell_ui.py`;
- `tests/test_premium_streamlit_state.py`;
- `tests/test_premium_app_shell_streamlit_integration.py`;
- implementation claim and handover.

Files changed:
- `premium_app_shell.py`;
- `presidio_streamlit.py`;
- `fix_streamlit_nested_expanders.py`;
- source-level UI contract tests updated where literal expectations described the retired shell;
- `WORKPACKAGES.md`, `CHANGELOG.md`, `RELEASE_NOTES.md` for closeout administration.

Validation:
- clean runtime/product head `0e1a5fbb3d6c3b8f8293779e598ececd6ea4aa1d`;
- GitHub Actions Tests #2200 / run `31259576962`, job `93108182555`;
- `python -m pytest -q tests` → `1225 passed in 12.55s`;
- final post-administration exact-head full regression still required before assurance;
- Hugging Face sync and live app verification are pending after PASS/merge because runtime UI changed.

Intentionally unchanged:
- recognizers/profile rules and threshold meaning;
- replacement/include authority and direct masking semantics;
- export bytes, filenames and MIME types;
- Scrub Key schema/binding/lifecycle;
- reinsert and audit semantics;
- dependencies and cloud/local-processing boundary;
- mandatory human review.

Next gate:
- freeze final exact head after this administrative closeout;
- full GitHub Actions regression;
- fresh blind `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_VERIFY`;
- no merge and no Input Stage work before independent PASS.

---

