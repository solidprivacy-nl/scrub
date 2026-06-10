# WP45 — Local runtime architecture plan

Status: completed architecture/specification-only.  
Repository: `solidprivacy-nl/scrub`.  
Scope: architecture plan only; no packaging implementation, runtime code, UI, dependency, Docker/runtime startup or cloud-processing change.

---

## 1. Purpose

WP45 defines a local runtime architecture direction for SolidPrivacy Scrub.

The goal is to address the trust gap between:

```text
current Hugging Face demo/development environment
```

and the intended product promise:

```text
local-first processing for confidential Dutch professional documents
```

This plan compares local runtime paths and recommends a phased architecture approach without implementing packaging or runtime changes.

---

## 2. Current Hugging Face demo role

The Hugging Face Space remains useful as:

- a public demo surface;
- a rapid development and review environment;
- a way to show the workflow to stakeholders;
- a place to validate UI behavior on non-confidential synthetic documents;
- a synced deployment target for early prototype testing.

The Hugging Face Space should not be positioned as the trust environment for confidential production documents.

Policy:

```text
Use the cloud demo for synthetic/demo data.
Use local runtime for confidential legal and care documents once available.
```

The demo can remain in parallel with local runtime development, but the product promise should move toward local-first/offline-capable use.

---

## 3. Why local-first matters

SolidPrivacy Scrub processes professional documents that may contain:

- names;
- addresses;
- case numbers;
- client numbers;
- medical/care references;
- e-mail addresses;
- phone numbers;
- financial references;
- Scrub Keys that can re-identify scrubbed text.

For legal and care users, trust depends not only on recognizer quality but also on where documents are processed.

Local-first matters because it supports:

- reduced document exposure;
- no required third-party cloud upload;
- better alignment with confidentiality expectations;
- clearer data control for the user;
- offline operation for sensitive environments;
- easier positioning for professional desktop/enterprise use;
- future audit and residual-risk reporting tied to local artifacts.

Local-first does not remove all risk. It must still be paired with high recall, human review, secure Scrub Key lifecycle, document hygiene and clear warnings.

---

## 4. Runtime options compared

| Option | Privacy | Complexity | Windows friendliness | Installer effort | Offline support | Future frontend flexibility | Maintainability |
|---|---|---|---|---|---|---|---|
| Local Streamlit launcher | High if bound to localhost and no telemetry/cloud calls are used. Browser UI still local. | Low. Reuses current Python/Streamlit app. | Medium. Requires Python/runtime bundling or managed install path. | Low to medium. Can start as scripts, later simple launcher. | Good if dependencies/models are local. | Limited. Still Streamlit-first. | High for current codebase because it reuses existing app. |
| PyInstaller | High if packaged app remains local and dependencies are bundled correctly. | Medium. Python packaging, model assets and native deps can be tricky. | High for single-machine Windows distribution once stabilized. | Medium. Requires build pipeline, signing and installer decisions. | Good if package contains all needed assets. | Limited to current Python/Streamlit or small wrapper. | Medium. Packaging failures can be environment-specific. |
| Tauri | High. Small native shell with local backend; good local-app posture. | High. Requires Rust/webview/frontend architecture decisions. | High. Good Windows desktop direction after design work. | Medium to high. Requires signing, update channel and frontend build. | Good when backend/assets are local. | High. Enables document-centric frontend later. | Medium to high if frontend/backend split is clean. |
| Electron | High if local-only and network controls are clear, but larger attack/update surface. | High. Requires Node/desktop packaging and frontend/backend bridge. | High. Mature Windows app ecosystem. | High. Installer, signing and update handling are well-known but heavier. | Good when packaged assets are local. | Very high. Rich frontend capabilities. | Medium. Larger dependency surface and security upkeep. |

---

## 5. Minimal local Streamlit launcher option

Description:

```text
Run the existing Streamlit app locally on the user's machine, usually bound to localhost only.
```

Benefits:

- fastest path from current prototype to local-first proof;
- reuses existing Streamlit workflow;
- no frontend rewrite;
- good bridge between Hugging Face demo and local desktop direction;
- allows local file-handling validation early;
- supports care/legal pilot conversations without waiting for a full desktop shell.

Risks:

- still feels like a developer/prototype app unless wrapped well;
- local Python/model setup can be fragile;
- browser-based local UI may confuse users unless clearly explained;
- packaging can become messy if not separated from app logic;
- Streamlit remains a limitation for document-centric review UX.

Recommended use:

```text
MVP local runtime path.
```

This should be the first implementation step because it tests the local-first trust promise with the least architectural change.

---

## 6. PyInstaller option

Description:

```text
Package the Python application and dependencies into a Windows-friendly executable or bundled app folder.
```

Benefits:

- closer to a one-click local product;
- can hide Python setup complexity from users;
- supports offline distribution if all models/assets are bundled;
- aligns with a future MSI/Windows installer path.

Risks:

- NLP, Presidio, spaCy and document libraries may have packaging edge cases;
- executable size may be large;
- antivirus false positives can occur with packaged Python apps;
- model asset paths must be handled carefully;
- Streamlit/browser launch still needs a clean UX wrapper;
- updates and code signing need a policy.

Recommended use:

```text
Second local runtime step after the minimal local launcher proves file handling and offline behavior.
```

PyInstaller is useful for an early Windows proof of concept, but should not be the final architecture decision until dependency packaging is validated.

---

## 7. Tauri option

Description:

```text
Use a lightweight native desktop shell with a web frontend and local backend integration.
```

Benefits:

- strong professional desktop direction;
- smaller footprint than Electron in many cases;
- good path toward a document-centric review UI;
- can keep Python core as local backend if designed carefully;
- supports future local file-handling controls and app-level UX.

Risks:

- introduces Rust/Tauri build complexity;
- requires frontend architecture work;
- Python backend integration must be designed, not improvised;
- installer, signing and update channel still need decisions;
- may be premature before local Python core boundaries stabilize.

Recommended use:

```text
Recommended later professional runtime path, especially if a document-centric frontend becomes a priority.
```

Tauri should be considered after the local Streamlit/PyInstaller phase has clarified local file handling, offline assets and core Python boundaries.

---

## 8. Electron option

Description:

```text
Use a mature desktop shell with a web frontend and local backend bridge.
```

Benefits:

- mature Windows packaging ecosystem;
- very flexible frontend capabilities;
- many developers know the stack;
- strong option for complex document review interfaces.

Risks:

- heavier runtime footprint;
- larger dependency and security surface;
- update mechanism and signing require operational discipline;
- local backend bridge must be designed securely;
- may be overkill for the first local-first proof.

Recommended use:

```text
Alternative later professional runtime path if team skills or frontend needs favor Electron over Tauri.
```

Electron should not be the MVP path unless the project decides to prioritize a full frontend rewrite earlier than planned.

---

## 9. Windows desktop considerations

Windows is the primary packaging target for early professional use.

Considerations:

- code signing to reduce security warnings;
- predictable install location;
- local-only data directory;
- clear user-controlled output locations;
- no silent upload or telemetry;
- explicit version number in app and audit output;
- uninstaller behavior;
- local model asset storage;
- Windows Defender / antivirus false-positive risk;
- corporate endpoint restrictions;
- running without administrator rights where possible;
- future MSI or managed deployment option for organizations.

For MVP, a simple local launcher can be acceptable if the limitations are clear. For professional use, a signed installer and update policy become important.

---

## 10. Local file handling

Local runtime must preserve the product principle:

```text
The user remains in control of source document, scrubbed output, Scrub Key, restored output and audit report.
```

Expectations:

- process files locally;
- do not upload document content by default;
- avoid persistent temporary files where possible;
- if temporary files are needed, keep them in a predictable local temp area and remove them after use;
- keep original files unchanged unless user explicitly saves an output;
- clearly separate source file, scrubbed output, Scrub Key, restored output and audit report;
- do not store real document snippets in logs;
- use synthetic examples only in repository tests/fixtures.

Future helper work should define a local file-handling/privacy test.

---

## 11. Offline expectations

The local runtime should aim for:

- app starts without internet;
- recognizers and local NLP assets are available offline;
- no required cloud API calls;
- no remote model loading at runtime;
- no dependency download during normal app use;
- no telemetry dependency for core functions;
- clear error if an optional online feature is ever introduced later.

For the first MVP, offline expectations may be validated in a controlled test rather than fully guaranteed by installer packaging.

---

## 12. Telemetry and network expectations

Default policy:

```text
No document-content telemetry.
No required outbound network calls for core processing.
No silent cloud document processing.
```

Expected future validation:

- network-traffic check during local scrub/review/reinsert flows;
- document content absent from logs and telemetry;
- clear list of any allowed update/check endpoints if an updater exists later;
- user-facing explanation that Hugging Face demo and local runtime are different trust environments.

If telemetry is introduced later, it must be opt-in, non-content, transparent and separately approved.

---

## 13. Secrets handling

The local runtime should not store:

- API keys;
- access tokens;
- Scrub Key values in logs;
- passphrases;
- encryption keys;
- document content in telemetry;
- hidden debug exports with real content.

Future encrypted/protected key handling belongs to the Scrub Key lifecycle/security line and must align with `SCRUB_KEY_LIFECYCLE_SPEC.md`.

---

## 14. Scrub Key local storage expectations

The Scrub Key is sensitive re-identification data.

MVP expectations:

- user explicitly downloads/saves the Scrub Key;
- UI/copy should warn that it can restore sensitive values;
- local runtime should not silently store additional key copies;
- logs should never include full mappings;
- import/reload should be local;
- deletion remains user-controlled unless a later lifecycle feature is implemented.

Later professional expectations:

- protected local file or encrypted key container;
- tamper/integrity checks;
- clear expiry/delete policy;
- possible local vault / managed key store;
- audit events that record counts and state, not original values.

---

## 15. Installer and update considerations

For MVP:

- avoid overbuilding an installer before local behavior is validated;
- document manual local launch steps or provide a simple local launcher;
- keep dependency list clear;
- keep app version visible.

For professional runtime:

- signed Windows installer;
- update channel policy;
- rollback policy;
- offline installation option;
- integrity verification;
- changelog/release notes separation;
- enterprise deployment considerations;
- clear support matrix for Windows versions.

Updates must not silently change export semantics, Scrub Key behavior or document-processing boundaries.

---

## 16. Supportability

Supportability depends on keeping layers clear:

1. Python core detection/reinsert/export logic.
2. Local runtime launcher.
3. Packaging/installer layer.
4. UI/frontend layer.
5. Local storage and audit layer.

Support requirements:

- reproducible local startup instructions;
- versioned dependencies;
- clear troubleshooting for model assets;
- synthetic diagnostic bundle for support;
- no request for users to share confidential documents;
- app logs should be safe to share because they contain no document content or Scrub Key mappings.

---

## 17. Recommended MVP local runtime path

Recommended MVP path:

```text
Minimal local Streamlit launcher → local file-handling/privacy test → PyInstaller proof of concept
```

Rationale:

- fastest path to local-first proof;
- lowest architecture risk;
- reuses current app and Python code;
- validates offline/local expectations before desktop-shell complexity;
- keeps Hugging Face available as demo/development environment;
- avoids premature frontend rewrite.

The MVP should not claim full professional desktop maturity. It should claim a controlled local prototype once verified.

---

## 18. Recommended later professional runtime path

Recommended later path:

```text
Tauri desktop shell with reusable Python core, unless team capability or frontend requirements make Electron preferable.
```

Rationale:

- future professional review likely needs document-centric UX beyond Streamlit;
- local app shell can better handle files, state, warnings, updates and audit output;
- Tauri can provide a smaller professional desktop footprint;
- Electron remains a viable alternative if mature web tooling and team familiarity outweigh footprint concerns.

The later runtime decision should be revisited after:

- local Streamlit proof;
- PyInstaller packaging spike;
- document-centric review UX specification;
- local file-handling/privacy tests;
- pilot feedback.

---

## 19. Implementation phases

Recommended phases:

### Phase A — Local launcher specification and minimal implementation

Future workpackage: `WP46 — Minimal local Streamlit launcher`.

Scope:

- local launch script or documented launcher;
- localhost-only binding expectations;
- no cloud processing;
- no installer yet;
- no UI changes unless explicitly approved.

### Phase B — Local file-handling/privacy validation

Future workpackage: `WP47 — Local file handling/privacy test`.

Scope:

- verify source files stay local;
- verify no document snippets in logs;
- verify temp-file handling;
- verify no required outbound calls during core flows where practical.

### Phase C — Windows packaging proof of concept

Future workpackage: `WP48 — Portable Windows proof of concept`.

Scope:

- test PyInstaller or similar packaging path;
- validate model assets and dependencies;
- no production installer claim.

### Phase D — Desktop packaging decision

Future workpackage: `WP49 — Desktop packaging decision`.

Scope:

- decide whether to continue Streamlit/PyInstaller, move toward Tauri, or use Electron;
- define installer/signing/update requirements.

### Phase E — Professional runtime implementation

Later workpackage after UX and packaging decisions.

Scope:

- signed installer;
- local storage policy;
- update policy;
- document-centric frontend if approved.

---

## 20. Recommended next workpackages

Immediate next step:

```text
WP46 — Minimal local Streamlit launcher
```

Then:

```text
WP47 — Local file handling/privacy test
WP48 — Portable Windows proof of concept
WP49 — Desktop packaging decision
```

Related parallel work that should remain coordinated:

- `WP21 — Gold-label entity schema` for recall/trust;
- `WP27 — Scrub Key warning UX plan` for local key-handling warnings;
- `WP31 — LLM-resistant placeholder format proposal` for AI roundtrip reliability;
- document-centric review UX work before choosing a final desktop shell.

---

## 21. Intentionally not changed in WP45

- No packaging implementation.
- No installer created.
- No runtime code changed.
- No UI changed.
- No Docker/runtime startup changes.
- No dependency changes.
- No telemetry implementation.
- No cloud processing added.
- No real data added.
- No export/reinsert behavior changed.
