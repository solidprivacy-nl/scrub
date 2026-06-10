# Handover — WP46 Minimal local Streamlit launcher

Repository: `solidprivacy-nl/scrub`

Workpackage title: `WP46 — Minimal local Streamlit launcher`

Status: completed minimal local runtime implementation.

## Summary

WP46 added the smallest safe local runtime path recommended by WP45.

The new launcher starts the existing Streamlit app locally by running the same existing startup patch scripts used by the container startup path, then launching `presidio_streamlit.py` through Streamlit on `127.0.0.1:8501` by default.

`LOCAL_RUN.md` documents how to run Scrub locally, the Python version assumption, dependency installation, the exact command executed, local-only warning, no-real-data-in-repo warning, which files are processed locally, what is not guaranteed yet and the next validation step.

## Files added

- `scripts/run_local_streamlit.py`
- `LOCAL_RUN.md`
- `handover/workpackages/20260610_1828_minimal_local_streamlit_launcher.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests / checks

- `python -m py_compile scripts/run_local_streamlit.py`
- `python scripts/run_local_streamlit.py --help`

## Validation status

- Script syntax validation: passed.
- Launcher CLI help: passed.
- Full app launch: not run.
- Full local file-handling/privacy validation: not run; belongs to WP47.

## GitHub Actions status

- Unknown / no statuses returned by connector for final WP46 commit.

## Hugging Face sync status

- Unknown / no workflow runs returned by connector for final WP46 commit.

## App verification status

- Not applicable. No UI feature changed.

## Remaining risks

- Local runtime has not yet been validated for temp-file behavior, logs, network traffic or offline operation.
- This is not an installer, PyInstaller build, Tauri/Electron app or signed Windows package.
- Local dependency installation still requires a developer/user setup step.
- No claim is made that all optional models and assets are already available offline.

## Next recommended step

- `WP47 — Local file handling/privacy test`.

## Intentionally not changed

- No installer.
- No PyInstaller packaging.
- No Tauri/Electron implementation.
- No Docker startup change.
- No Streamlit UI feature change.
- No export/reinsert behavior change.
- No dependency change.
- No telemetry implementation.
- No cloud processing added.
- No real data added.
