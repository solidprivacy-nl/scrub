# Handover — WP47 Local file handling/privacy test

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP47 — Local file handling/privacy test`

Status: completed local runtime privacy validation.

## Summary

WP47 adds local runtime privacy/file-handling tests for the minimal local Streamlit launcher introduced in WP46 and clarifies `LOCAL_RUN.md` boundaries.

The work verifies launcher/documentation expectations only. It does not implement a full network-traffic capture, offline certification, installer, packaging, UI behavior change, telemetry feature or cloud-processing feature.

## Files added

- `tests/test_local_file_handling_privacy.py`
- `handover/workpackages/20260612_1500_local_file_handling_privacy_test.md`

## Files changed

- `LOCAL_RUN.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests added/updated

- `tests/test_local_file_handling_privacy.py`

Coverage added:

- local launcher defaults to `127.0.0.1`;
- local launcher defaults to port `8501`;
- local launcher starts Streamlit with `--browser.gatherUsageStats false`;
- local launcher command does not add cloud/AI/telemetry endpoints;
- local launcher command does not include document content or synthetic filenames;
- launcher source does not write logs, create temp files, open files or introduce installer/packaging behavior;
- `LOCAL_RUN.md` warns that Hugging Face is demo/development only and must not be used for confidential real documents;
- `LOCAL_RUN.md` explains local-only limitations, no-real-data rules, temp/runtime expectations, no-telemetry/no-cloud-processing boundary and no installer/packaging claim.

## Tests/checks run

- `python -m py_compile scripts/run_local_streamlit.py` — passed in the ChatGPT execution sandbox against the authored files. The sandbox emitted an unrelated spreadsheet runtime warmup warning before Python execution, but the command returned success.
- `pytest -q tests/test_local_file_handling_privacy.py` — passed in the ChatGPT execution sandbox against the authored tests; 6 passed. The sandbox emitted the same unrelated spreadsheet runtime warmup warning, but pytest returned success.
- `pytest tests -k "local or privacy or streamlit"` — requested as relevant if executable, but not run in a live GitHub checkout through the ChatGPT GitHub connector.

## Validation status

- Launcher command defaults and privacy-relevant flags are covered by tests.
- Launcher argument construction is tested without starting Streamlit by monkeypatching `run_checked`.
- Launcher source is tested for absence of logging/temp-file/file-open/packaging behavior.
- Documentation now explicitly separates Hugging Face demo/development use from local confidential-processing validation.
- Documentation states that WP47 is not a full offline or network-traffic guarantee.
- No Streamlit UI changed.
- No upload/download/export/reinsert semantics changed.
- No cloud document processing added.
- No telemetry added.
- No installer or packaging added.
- No Docker/Hugging Face startup behavior changed.
- No dependency changes.
- No real data added.

## GitHub Actions status

To be checked after final handover commit.

## Hugging Face sync status

To be checked after final handover commit. No app behavior changed.

## App verification status

Not applicable. No UI behavior changed.

## Remaining risks

- WP47 validates launcher and documentation boundaries only; it is not full runtime packet/network inspection.
- No full offline demonstration yet.
- No portable Windows proof of concept yet.
- No final desktop packaging decision yet.
- No production security certification is supported.

## Next recommended step

- `WP48 — Portable Windows proof of concept`, only if the coordinator wants to continue the local-runtime line after CI/status is acceptable.
- Other active risk-line option: `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`.
