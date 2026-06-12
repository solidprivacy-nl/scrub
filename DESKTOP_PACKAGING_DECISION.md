# WP49 — Desktop packaging decision

Status: completed decision/documentation-only  
Repository: `solidprivacy-nl/scrub`

## 1. Decision update after roadmap adjustment

The packaging decision remains valid, but the roadmap sequence is now stricter:

```text
Validate logic, interface, security and trustworthiness online first. Delay local installer/MSI work until the core product behavior is acceptable.
```

This means the local installer is not a near-term default track. It belongs at the end of the roadmap.

The Hugging Face/Streamlit web prototype remains the preferred validation surface for synthetic and approved non-confidential testing because web-interface testing is faster and less labor-intensive than testing an installable desktop app.

## 2. Packaging decision

The recommended first local MVP distribution form, when local distribution is revisited, remains:

```text
Portable Python folder with the existing local Streamlit launcher
```

The recommended later professional desktop direction remains:

```text
Tauri shell with reusable Python core, unless team capability or frontend requirements make Electron preferable
```

A real MSI remains a future managed-deployment option only after:

- logic is acceptable;
- interface is acceptable;
- security and trustworthiness are acceptable;
- recall/residual-risk behavior is credible;
- DOCX hygiene and Scrub Key risks are visibly handled;
- online/web workflow validation is strong;
- packaging, signing, update, rollback, offline, network, temp-file and support boundaries have been validated.

## 3. Option comparison

| Option | Current role | Later role | Main risk |
| --- | --- | --- | --- |
| Portable Python folder | Final-phase MVP local distribution candidate | Controlled local pilot path | Dependency/setup support burden |
| PyInstaller | Not default next work | Later one-folder proof if approved | Bundling, temp files, antivirus/signing |
| Tauri | Too early now | Preferred later professional shell candidate | Frontend/Rust/backend integration complexity |
| Electron | Too early now | Later alternative if frontend/team needs require it | Larger dependency and security surface |
| MSI | Out of scope now | Future managed deployment option | False production maturity if premature |

## 4. Why installer work is deferred

Installer work is deferred because it creates extra validation load before the product behavior is stable:

- OS-specific setup and support;
- antivirus/endpoint behavior;
- signing and trust warnings;
- update and rollback policy;
- dependency/model bundling;
- temp-file and network validation;
- enterprise deployment expectations;
- support process for legal/care organizations.

Those concerns matter, but they should not consume capacity before Scrub's core logic, interface, security and trustworthiness are acceptable.

## 5. Proof-of-concept versus production installation

A proof-of-concept may show:

- the app starts locally;
- the app binds to `127.0.0.1`;
- Streamlit usage stats are disabled;
- documents are processed in the local Python process;
- no cloud document-processing endpoint is introduced by the launcher.

A proof-of-concept must not claim:

- production security certification;
- complete offline guarantee;
- managed deployment readiness;
- signed/trusted installer behavior;
- automatic update safety;
- protected key storage;
- enterprise support readiness.

A production installation needs:

- reproducible build pipeline;
- dependency and model asset inventory;
- code signing;
- installer/update/rollback policy;
- local storage policy;
- Scrub Key lifecycle/protection policy;
- logging/diagnostic policy with no real document snippets;
- network-traffic validation;
- endpoint/antivirus compatibility;
- support process for legal/care organizations;
- app verification with synthetic and approved pilot data.

## 6. What remains outside scope

This decision does not implement or approve:

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

## 7. Final recommendation

Recommended sequence:

```text
1. Keep validating logic/interface/security/trust online first.
2. Continue DOCX hygiene, Scrub Key verification, review UX and pilot workflow before installer investment.
3. Keep portable Python folder as the first local distribution candidate for the final phase.
4. Consider PyInstaller one-folder only as a later approved proof.
5. Keep Tauri as preferred later professional shell candidate.
6. Keep Electron as later alternative only.
7. Keep MSI as future enterprise deployment option, not current work.
```

This keeps Scrub aligned with the product promise:

```text
Sensitive information stays local in the final trust environment.
The user remains in control.
The document stays readable.
Residual risk is visible.
```
