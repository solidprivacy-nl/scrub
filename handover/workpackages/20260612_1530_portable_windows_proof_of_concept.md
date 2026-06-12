# Handover — WP48 Portable Windows proof of concept

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP48 — Portable Windows proof of concept`

Status: completed Windows portable proof-of-concept launcher/docs/tests.

## Summary

WP48 added a minimal Windows PowerShell proof-of-concept wrapper around the existing local Python Streamlit launcher. The work validates a portable-folder direction without changing app behavior, Streamlit UI, upload/download/export/reinsert semantics, Docker/Hugging Face startup behavior, dependencies, telemetry, cloud document processing or real-data handling.

The proof-of-concept remains explicitly non-production: it is not a Windows installer, not an MSI, not PyInstaller packaging, not a signed executable, not an enterprise deployment, not a full offline guarantee and not network-traffic certification.

## Files added

- `scripts/run_windows_portable_poc.ps1`
- `WINDOWS_PORTABLE_POC.md`
- `tests/test_windows_portable_poc.py`
- `workpackage_claims/WP48_portable_windows_proof_of_concept.md`
- `handover/workpackages/20260612_1530_portable_windows_proof_of_concept.md`

## Files changed

- `LOCAL_RUN.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests added/updated

Added:

```text
tests/test_windows_portable_poc.py
```

The tests check that:

- the Windows wrapper delegates to `scripts/run_local_streamlit.py` instead of duplicating app startup behavior;
- the wrapper defaults to `127.0.0.1` and port `8501`;
- the wrapper does not add cloud, telemetry, packaging or installer behavior;
- the wrapper does not accept document, Scrub Key, secret, token or password arguments;
- `WINDOWS_PORTABLE_POC.md` records the proof-of-concept-only boundary and non-goals;
- `LOCAL_RUN.md` mentions WP48 and keeps no-production-installer/no-MSI/no-full-offline-guarantee boundaries.

## Tests/checks run

No tests were run in the live GitHub checkout because the ChatGPT GitHub connector does not provide shell execution in the checked-out repository.

Expected validation command:

```text
pytest tests/test_windows_portable_poc.py
```

Related local-runtime regression command:

```text
pytest tests/test_local_file_handling_privacy.py tests/test_windows_portable_poc.py
```

## Validation status

- Required repository/control context was read.
- Existing WP47 local launcher privacy tests and `LOCAL_RUN.md` were inspected.
- WP48 was checked for existing claims before work started.
- A WP48 claim was created before changing files.
- Implementation is limited to a Windows PowerShell wrapper, documentation and static tests.
- No real data was added.

## GitHub Actions status

- Pending / not verified through connector at handover time.
- The final commits should be validated by GitHub Actions.

## Hugging Face sync status

- Not applicable for app behavior. WP48 does not change Streamlit UI/runtime behavior in the Hugging Face Space.
- No app verification is required for this workpackage.

## App verification status

- Not applicable; no UI behavior changed.

## Remaining risks

- WP48 does not prove full offline operation.
- WP48 does not perform network packet capture or runtime traffic inspection.
- WP48 does not package dependencies into a portable Python distribution.
- WP48 does not create a signed executable, MSI or managed enterprise deployment.
- WP48 does not validate Windows machine compatibility in a real Windows environment through the connector.
- Desktop packaging architecture still needs a decision package.

## Next recommended step

- `WP49 — Desktop packaging decision`, only after WP48 CI/status is acceptable and the coordinator confirms the local-runtime line should continue.
- Active parallel Scrub Key UI line remains the already-claimed `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`.

## Intentionally not changed

- No Streamlit UI behavior changed.
- No upload/download/export/reinsert semantics changed.
- No Docker/Hugging Face startup behavior changed.
- No dependencies changed.
- No telemetry added.
- No cloud document processing added.
- No real data added.
- No production installer claim added.
- No MSI claim added.
- No PyInstaller package added.
- No signed executable added.
- No full offline guarantee or network-traffic certification added.
