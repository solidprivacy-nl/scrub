# Windows portable proof of concept — WP48

Status: proof-of-concept only  
Repository: `solidprivacy-nl/scrub`

WP48 validates a minimal Windows/Python portable-folder direction after WP47 local file-handling/privacy validation.

This is not a production packaging decision and not a finished desktop distribution. It does not change Streamlit UI behavior, upload/download/export/reinsert semantics, Docker/Hugging Face startup behavior, dependencies, telemetry, cloud document processing or real-data handling.

---

## 1. Goal

The goal is to validate whether the current local launcher can be started from a Windows-oriented repository folder using a small PowerShell wrapper while keeping the same privacy boundary as WP46/WP47:

```text
local browser → 127.0.0.1 Streamlit → local Python process
```

The proof-of-concept delegates to the existing Python launcher:

```text
scripts/run_local_streamlit.py
```

The Windows wrapper is:

```text
scripts/run_windows_portable_poc.ps1
```

---

## 2. Explicit non-goals

WP48 does not add or claim:

- a Windows installer;
- an MSI package;
- PyInstaller packaging;
- a signed executable;
- enterprise deployment management;
- a production desktop app;
- a complete offline guarantee;
- network-traffic certification;
- protected local storage;
- encrypted Scrub Key containers;
- local vault behavior;
- automatic deletion or expiry blocking;
- UI changes;
- export or reinsert semantic changes;
- telemetry;
- cloud document processing;
- real-data test fixtures.

---

## 3. POC folder assumption

The portable proof-of-concept assumes a local Windows folder containing the repository and a local Python environment prepared by the user or coordinator.

Example folder shape:

```text
SolidPrivacy-Scrub-POC/
  scrub/
    scripts/
      run_local_streamlit.py
      run_windows_portable_poc.ps1
    presidio_streamlit.py
    fix_streamlit_nested_expanders.py
    fix_streamlit_pdf_text_reinsert.py
    LOCAL_RUN.md
```

The PowerShell wrapper does not copy documents, create document caches, write logs, build packages, download models or install dependencies. It starts the existing local launcher from the repository root.

---

## 4. Windows run command

From the repository root on Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run_windows_portable_poc.ps1
```

The wrapper defaults to:

```text
address = 127.0.0.1
port    = 8501
```

Open:

```text
http://127.0.0.1:8501
```

To select another local port:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run_windows_portable_poc.ps1 -Port 8502
```

Do not bind the app to a public interface for confidential documents unless a later security review explicitly approves that mode.

---

## 5. Dependency setup boundary

The existing dependency setup remains documented in `LOCAL_RUN.md`.

Recommended development setup still uses Python 3.10 and Poetry. WP48 does not replace that setup with a packaging system.

A future package may decide whether to use:

- portable Python folder distribution;
- PyInstaller;
- Tauri shell with Python core;
- Electron shell with Python core;
- managed enterprise deployment;
- MSI or another installer format.

That decision belongs to WP49 or a later packaging decision package, not WP48.

---

## 6. Privacy boundary

The wrapper passes only runtime options to the existing launcher:

```text
scripts/run_local_streamlit.py --address <address> --port <port>
```

It must not pass:

- source document content;
- source document filenames;
- Scrub Key values;
- restored output;
- audit content;
- client or matter labels;
- secrets or tokens.

The local Streamlit app still processes selected files in the local Python process. Browser caches, Streamlit upload handling, Python package caches and OS-level temporary/runtime behavior remain outside the proof-of-concept guarantee and require later validation before production claims.

---

## 7. Validation matrix

| Expectation | WP48 POC status |
| --- | --- |
| Uses existing local Python launcher | Yes |
| Defaults to `127.0.0.1` | Yes |
| Defaults to port `8501` | Yes |
| Disables Streamlit usage stats through delegated launcher | Yes, via `scripts/run_local_streamlit.py` |
| Adds cloud processing | No |
| Adds telemetry | No |
| Adds packaging/installer behavior | No |
| Changes UI behavior | No |
| Changes export/reinsert semantics | No |
| Stores real data in repo | No |
| Proves full offline operation | No |
| Proves network-traffic behavior | No |

---

## 8. Recommended next step

Recommended next package:

```text
WP49 — Desktop packaging decision
```

Purpose:

- Decide whether the next serious local runtime path should be Streamlit/Python folder, PyInstaller, Tauri, Electron or another managed packaging approach.
- Define the security and operational requirements before any production installer claim.
- Keep Hugging Face clearly separated as a demo/development environment.

Do not start production packaging until WP49 or a later package explicitly approves the target architecture and security boundary.
