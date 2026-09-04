# Workpackage claim — SCRUB-WP_REPOSITORY_CONVERGENCE_STARTUP_INVOCATION_RETIREMENT

Status: implementation in progress  
Role: `implementation_operations`  
Issue: #115  
Branch: `wp/repository-convergence-startup-invocation-retirement`  
Starting main: `255cd619d5cf6eab32f9383940eaa4af362cb68c`  
Started: 2026-09-05 Europe/Amsterdam

## Objective

Remove the obsolete Docker pre-start invocation of the two legacy Streamlit source-patch scripts after source inspection proved that both scripts exit without mutating the current direct-source application.

## Evidence before implementation

Current `presidio_streamlit.py` directly imports:

- `premium_streamlit_shell_ui`, which causes `fix_streamlit_nested_expanders.py` to exit immediately;
- `render_reinsert_mode` from `reinsert_mode_ui`, which causes `fix_streamlit_pdf_text_reinsert.py` to exit immediately.

Current Docker startup nevertheless executes both scripts before launching Streamlit.

This creates a live runtime dependency on historical mutation machinery even though current product behavior is already direct source.

## Scope

Authorized:

- change the Docker `CMD` so Streamlit launches directly with all existing port/address/XSRF/CORS flags preserved;
- update only test assertions that specifically require the obsolete startup invocation;
- add a narrow current-runtime contract if needed;
- align `WORKPACKAGES.md`, `CHANGELOG.md` and the temporary convergence debt ledger;
- write the mandatory handover.

Not authorized:

- changing `presidio_streamlit.py` product/UI behavior;
- changing recognizers, profiles, review/export/Scrub Key/reinsert semantics;
- removing persistent replacement memory or external AI paths;
- changing unrelated Docker hardening/security settings;
- deleting the historical patch scripts in this workpackage;
- mass-retiring historical `*_ui_patch.py` tests.

## Acceptance

1. Docker starts `presidio_streamlit.py` directly through Streamlit.
2. Neither `fix_streamlit_nested_expanders.py` nor `fix_streamlit_pdf_text_reinsert.py` is invoked at runtime startup.
3. Existing Streamlit port/address/XSRF/CORS flags remain unchanged.
4. Tests protect current direct-source behavior rather than requiring the obsolete invocation.
5. Full exact-head `python -m pytest -q tests` is green.
6. Changed-file scope contains no user-visible product behavior change.
7. Fresh independent `governance_release_assurance` returns PASS before merge.
8. After merge, exact-main Tests and GitHub→Hugging Face sync are verified.
