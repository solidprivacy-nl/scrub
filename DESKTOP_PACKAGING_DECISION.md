# WP49 — Desktop packaging decision

Status: completed decision/documentation-only  
Repository: `solidprivacy-nl/scrub`

## 1. Decision

The recommended first local MVP distribution form is:

```text
Portable Python folder with the existing local Streamlit launcher
```

This means Scrub is distributed as a controlled local folder containing the repository/app code, documented dependency setup and a Windows-oriented launcher wrapper. The user or IT operator starts the app locally, bound to `127.0.0.1`, and opens the local browser UI.

The recommended next concrete packaging proof, only if the coordinator approves it, is:

```text
WP48B or WP49B — concrete portable/PyInstaller packaging proof
```

The recommended later professional desktop direction is:

```text
Tauri shell with reusable Python core, unless team capability or frontend requirements make Electron preferable
```

A real MSI remains a future managed-deployment option only after packaging, signing, update, rollback, offline, network, temp-file and support boundaries have been validated.

## 2. Why portable Python folder first?

A portable Python folder is the best first local MVP distribution form because it has the lowest architecture and security risk at this stage.

It:

- reuses the current Python/Streamlit app;
- avoids a frontend rewrite;
- avoids an opaque executable bundle during early privacy validation;
- avoids installer/elevation/admin behavior;
- keeps files and dependencies easier to inspect;
- matches the WP46/WP47/WP48 local runtime path;
- supports local confidential-processing validation without claiming production maturity.

For a professional privacy product, this is important: the first serious claim should be that the app can run locally and that the local boundary is understandable and testable. It should not prematurely claim to be a finished secure desktop product.

## 3. Suitability for jurists and care organizations

### Controlled MVP / pilot

For early legal and care pilots, the best fit is:

```text
Portable Python folder managed by the coordinator or local IT
```

Reason:

- IT can inspect the folder and command before use;
- no installer rights are required by the app packaging itself;
- no production installer claim is made;
- no automatic update channel is introduced;
- confidential-processing instructions can stay explicit;
- local-only behavior can be validated before organizational rollout.

This is suitable for:

- small internal pilots;
- trusted testers;
- local-first workflow validation;
- demonstrations with synthetic or approved non-confidential data;
- IT/security review of the local runtime boundary.

It is not suitable yet as a broad unmanaged end-user deployment.

### Professional organizational deployment

For jurists and care organizations at production scale, the likely future need is:

```text
signed managed installer or enterprise deployment package
```

But this should come later. Before production deployment, the project needs decisions on:

- code signing;
- update policy;
- rollback policy;
- offline dependency/model assets;
- local storage location;
- Scrub Key protection model;
- logging and diagnostics;
- endpoint management restrictions;
- support process without sharing real documents;
- managed deployment and uninstall behavior.

## 4. Option comparison

| Option | Fit for first MVP | Fit for professional future | Security / management risk | Main reason |
| --- | --- | --- | --- | --- |
| Portable Python folder | Best | Limited but useful for controlled pilots | Lowest current risk | Transparent, inspectable, no installer/elevation, reuses current app |
| PyInstaller | Good next proof, not first default | Possible bridge to Windows distribution | Medium | Hides Python setup, but can create dependency, antivirus, temp-file and signing issues |
| Tauri | Too early for MVP | Best later professional shell candidate | Medium, after architecture work | Smaller desktop shell, good for future document-centric frontend, but requires Rust/frontend/backend design |
| Electron | Too early for MVP | Viable later alternative | Higher | Mature and flexible, but heavier footprint and larger dependency/security surface |
| MSI later | Out of scope now | Likely enterprise option after proof | High if premature; acceptable after signing/update policy | Managed deployment needs packaging maturity, signing, update/rollback and IT review |

## 5. Portable Python folder

Description:

```text
A local folder with the existing app, Python dependency setup, and launcher scripts.
```

Recommended role:

```text
First MVP local distribution and controlled pilot path.
```

Benefits:

- fastest route from current codebase to local-first validation;
- easiest to inspect and debug;
- no hidden packaging layer;
- no installer behavior;
- no admin/elevation requirement from packaging itself;
- no new runtime framework;
- no Streamlit UI changes;
- no Docker/Hugging Face startup changes;
- no cloud document processing.

Risks:

- less polished for non-technical users;
- dependency setup can be fragile;
- support burden remains higher than a signed installer;
- does not prove full offline behavior by itself;
- not ideal for broad unmanaged distribution.

Decision:

```text
Use this as the first local MVP distribution form.
```

## 6. PyInstaller

Description:

```text
Bundle Python app/dependencies into a Windows-friendly folder or executable.
```

Recommended role:

```text
Next approved packaging proof, not automatic production packaging.
```

Benefits:

- hides Python setup from end users;
- can produce a more recognizable Windows launch experience;
- can help validate bundled dependencies and local assets;
- can be a bridge toward a future signed installer.

Risks:

- NLP/document/PDF dependencies may be hard to bundle;
- model/data asset paths need careful testing;
- one-file mode may create temp-file behavior that requires privacy validation;
- antivirus false positives are possible;
- signing and update policies remain unresolved;
- still does not solve final professional UX if Streamlit remains the UI.

Decision:

```text
Use only as a separately approved proof package, preferably one-folder first. Do not jump directly to one-file or production installer claims.
```

## 7. Tauri

Description:

```text
Native desktop shell with web frontend and local backend integration.
```

Recommended role:

```text
Preferred later professional desktop direction if Scrub moves beyond Streamlit into a document-centric review interface.
```

Benefits:

- good fit for a polished desktop product;
- smaller desktop-shell posture than Electron in many cases;
- can support a future document-centric review UI;
- can give better control over local file dialogs, windows and user flow;
- can keep Python core local if backend boundaries are designed carefully.

Risks:

- requires frontend architecture work;
- requires Rust/Tauri build capability;
- Python backend/sidecar integration must be designed securely;
- installer/signing/update policies are still needed;
- premature adoption could slow privacy/core validation.

Decision:

```text
Keep as preferred later professional shell candidate, not MVP packaging.
```

## 8. Electron

Description:

```text
Desktop shell using Chromium/Node with a web frontend and local backend bridge.
```

Recommended role:

```text
Later alternative to Tauri if team skills, frontend requirements or ecosystem needs outweigh footprint and dependency concerns.
```

Benefits:

- mature desktop packaging ecosystem;
- strong frontend flexibility;
- many developers know web/Electron tooling;
- good fit for rich document-centric interfaces.

Risks:

- heavier runtime footprint;
- larger dependency/security surface;
- Node/backend bridge requires strict security design;
- update/signing policy still required;
- overkill for the first local MVP.

Decision:

```text
Do not use Electron for the first MVP. Reconsider later only if Tauri is not practical or frontend needs clearly require Electron.
```

## 9. MSI later

Description:

```text
Managed Windows installer/deployment package for organizational rollout.
```

Recommended role:

```text
Future enterprise deployment option only.
```

Benefits:

- familiar for Windows IT teams;
- supports managed deployment patterns;
- can support install/uninstall and versioning expectations;
- can fit legal/care organizational rollout.

Risks:

- premature MSI creates false production maturity;
- signing, update, rollback and support policy are required;
- installer may need admin or endpoint management review;
- wrong defaults could store sensitive runtime data in unmanaged locations;
- MSI does not itself solve privacy, offline, Scrub Key or telemetry risks.

Decision:

```text
Do not build MSI now. Treat MSI as a later packaging/distribution layer after the app, local storage, key lifecycle, update policy and support model are mature.
```

## 10. Proof-of-concept versus production installation

### Proof-of-concept

A proof-of-concept may show:

- the app starts locally;
- the app binds to `127.0.0.1`;
- Streamlit usage stats are disabled;
- documents are processed in the local Python process;
- no cloud document-processing endpoint is introduced by the launcher;
- the local run path is understandable to IT/security reviewers.

A proof-of-concept must not claim:

- production security certification;
- complete offline guarantee;
- managed deployment readiness;
- signed/trusted installer behavior;
- automatic update safety;
- protected key storage;
- enterprise support readiness.

### Production installation

A production installation needs additional decisions and evidence:

- reproducible build pipeline;
- dependency lock and asset inventory;
- code signing;
- installer/update/rollback policy;
- local storage policy;
- Scrub Key lifecycle/protection policy;
- logging/diagnostic policy with no real document snippets;
- network-traffic validation;
- endpoint/antivirus compatibility;
- support process for legal/care organizations;
- app verification with synthetic and approved pilot data.

## 11. Least security-/management-risk option

For the next MVP step, the least security-/management-risk option is:

```text
Portable Python folder with documented local launcher
```

Reason:

- no installer elevation;
- no new desktop framework;
- no opaque executable bundling;
- no automatic updater;
- no additional packaging temp-file behavior;
- easier IT review;
- easiest rollback: delete/replace the folder;
- easiest to keep Hugging Face and local runtime boundaries separate.

For later organizational deployment, the least long-term management risk may become a signed managed installer, but only after the packaging proof and security model are mature.

## 12. What remains outside scope

WP49 does not implement or approve:

- MSI;
- PyInstaller build;
- Tauri app;
- Electron app;
- production installer;
- signed executable;
- auto-updater;
- telemetry;
- cloud document processing;
- Docker/Hugging Face startup changes;
- Streamlit UI changes;
- Scrub Key schema changes;
- encryption or local vault behavior;
- automatic deletion or expiry blocking;
- real-data packaging tests.

## 13. What comes before a real MSI?

Before a real MSI, Scrub needs at least one approved concrete packaging proof package.

Recommended next packaging proof options:

```text
WP48B — Portable Python folder hardening proof
```

or:

```text
WP49B — PyInstaller one-folder packaging proof
```

The proof should validate:

- reproducible local build steps;
- dependency and model asset inventory;
- local-only launch behavior;
- no document-content logging;
- temp-file behavior;
- network-traffic behavior;
- Windows Defender/endpoint behavior;
- supportable folder layout;
- app version display;
- synthetic diagnostics only;
- no real data;
- no cloud processing;
- no change to export/reinsert semantics.

Only after that should the project decide on:

- code signing;
- MSI/MSIX/installer format;
- update channel;
- rollback;
- enterprise deployment;
- managed storage;
- helpdesk/support process;
- professional desktop shell migration.

## 14. Final recommendation

Recommended sequence:

```text
1. Keep portable Python folder as first MVP local distribution.
2. Run WP48B or WP49B only if the coordinator approves a concrete packaging proof.
3. Prefer PyInstaller one-folder before any one-file executable.
4. Keep Tauri as preferred later professional shell candidate.
5. Keep Electron as later alternative only.
6. Keep MSI as future enterprise deployment option, not current implementation.
```

This keeps Scrub aligned with the product promise:

```text
Sensitive information stays local.
The user remains in control.
The document stays readable.
Residual risk is visible.
```
