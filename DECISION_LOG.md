# SolidPrivacy Scrub — Decision Log

This file records accepted strategic, product and architecture decisions.

---

## 2026-06-12 — D015 — Local installer is deferred until the final roadmap phase

Status: accepted roadmap sequencing decision

Decision:

```text
Local installer and production desktop packaging work must move to the end of the roadmap. Scrub should validate as much as possible through the online/web prototype and GitHub workflow first. Only after logic, interface, security and trustworthiness are acceptable should the project invest serious effort in local installer/MSI/desktop packaging.
```

Rationale:

Testing an installable app is much more labor-intensive than testing a web interface. Installer work introduces OS, antivirus, signing, dependency, update, rollback, temp-file, network, support and enterprise-management complexity. Starting packaging too early risks spending effort on distributing logic and UI that may still change. The Hugging Face/Streamlit prototype remains the fastest surface for synthetic and approved non-confidential validation of product behavior.

Implications:

- `ROADMAP.md` now places final local desktop/offline installer work after trust, review, document hygiene, online workflow validation, pilot validation and scale-readiness work.
- `WP48B` or `WP49B` are not default next workpackages; they require explicit coordinator approval.
- MSI, signed installer, auto-updater, Tauri/Electron implementation and production packaging claims remain blocked until late-phase evidence is strong.
- The local-first product promise remains the final trust target, but installer effort should not precede product-behavior validation.
- Workers must not start installer or packaging implementation as a side effect of local-runtime, UI or trust work.

---

## 2026-06-12 — D014 — Desktop packaging starts with portable Python folder, MSI later only

Status: accepted packaging decision

Decision:

```text
The first local MVP distribution form should remain a portable Python folder with the existing local Streamlit launcher. PyInstaller one-folder may be the next concrete packaging proof if explicitly approved. Tauri remains the preferred later professional desktop-shell direction if Scrub moves toward a document-centric frontend, with Electron as a later alternative. MSI is a future managed-deployment option only after packaging, signing, update, rollback, offline, network, temp-file and support boundaries have been validated.
```

Rationale:

A portable Python folder has the lowest current architecture and security risk. It reuses the current app, avoids installer/elevation behavior, avoids opaque executable bundling, remains inspectable for IT/security reviewers and fits the current WP46-WP48 local-runtime path. PyInstaller can later validate dependency/model bundling but should start with one-folder proof, not a production one-file executable claim. Tauri and Electron are desktop-shell decisions that should wait until the Python core and document-centric frontend needs are clearer. MSI is useful for legal/care organization deployment later, but it would create false production maturity if built before signing, update, rollback, storage and support policies exist.

Implications:

- WP49 is decision/documentation-only and does not implement packaging.
- No worker may build MSI, PyInstaller, Tauri or Electron artifacts as a side effect of unrelated work.
- The next packaging proof should be `WP48B` or `WP49B` only if the coordinator approves a concrete packaging proof.
- Preferred next proof is either portable Python folder hardening or PyInstaller one-folder packaging proof.
- One-file PyInstaller, signed installer, MSI/MSIX, auto-updater and managed enterprise deployment remain future gated work.
- Local-first boundaries remain: no telemetry, no cloud document processing, no real data in repo, no export/reinsert semantic changes.
- Production packaging requires reproducible build, dependency/model asset inventory, code signing plan, update/rollback policy, offline/network/temp-file validation and support model.

---

## 2026-06-10 — D013 — Scrub Key deletion remains explicit and user-controlled

Status: accepted security/lifecycle policy

Decision:

```text
Scrub Keys must be retained only as long as needed for a specific matter, project, AI roundtrip, review or reinsert purpose. Expiry is guidance-first in MVP. Deletion must remain explicit and user-controlled. Scrub must not silently delete Scrub Keys, mappings, restored output, audit context or external copies, and must not keep hidden recovery copies.
```

Rationale:

The Scrub Key is sensitive re-identification data, so unnecessary retention increases breach impact. At the same time, deleting or losing the key prevents deterministic reinsert. Silent deletion would create surprise data loss and could conflict with matter, project, legal-hold or organization retention requirements.

Implications:

- WP28 defines policy only and does not implement deletion behavior.
- MVP may warn, guide and request acknowledgement, but must not automatically delete keys.
- Future app-managed deletion requires explicit confirmation, non-sensitive audit events and clear limits about external copies.
- Future expiry metadata, reminders, protected storage, encrypted containers, vault behavior and recovery/escrow require separate approved implementation workpackages.
- No worker may add automatic Scrub Key deletion, hidden recovery copies or import/export behavior changes as a side effect of unrelated work.

---

## 2026-06-10 — D012 — Recommended future robust placeholder format

Status: accepted architecture recommendation; not implemented

Decision:

```text
The recommended future robust placeholder format direction is [[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]], for example [[SP_PERSON_0001_A7F3]]. This is an architecture recommendation only. It does not change current placeholder generation, Scrub Key schema, reinsert helper behavior or export behavior.
```

Rationale:

The recommended shape is ASCII-only, visually distinct, machine-detectable, copy/paste friendly and less likely than Dutch natural-language labels to be translated by an LLM. The `SP` prefix identifies the token as a SolidPrivacy control token. A stable technical entity code, zero-padded counter and short integrity component create a path for future validation.

Implications:

- Current legacy placeholders such as `[PERSOON_1]` remain supported until a separate compatibility/migration decision says otherwise.
- WP31 remains proposal-only and does not implement migration.
- WP32 should implement a placeholder checksum/validation helper behind tests before any generation change.
- The visible integrity token must not be derived directly from original sensitive values.
- Future robust placeholder support should be additive first, not a silent replacement of legacy placeholders.
- No worker may change placeholder format, reinsert behavior or Scrub Key schema as a side effect of unrelated work.

---

## 2026-06-10 — D011 — Local runtime starts with Streamlit launcher, later desktop shell

Status: accepted; superseded in sequence by D015

Decision:

```text
The MVP local runtime path should start with a minimal local Streamlit launcher, followed by local file-handling/privacy validation and a PyInstaller/portable Windows proof of concept. The later professional runtime path should evaluate a Tauri desktop shell with a reusable Python core, with Electron as an alternative if frontend requirements or team capability favor it.
```

Rationale:

A minimal local Streamlit launcher is the fastest, lowest-risk way to test the local-first trust promise while reusing the current Python/Streamlit prototype. PyInstaller can validate Windows packaging and offline asset handling before committing to a professional desktop architecture. Tauri is the preferred later professional direction because it can support a document-centric frontend with a smaller desktop footprint, while Electron remains viable for richer web-app frontend needs.

Implications:

- WP45 remains architecture/specification-only.
- WP46 should implement only a minimal local Streamlit launcher unless separately approved otherwise.
- WP47 should validate local file handling, temp-file behavior, logs and network expectations.
- WP48 should validate a portable Windows proof of concept before installer claims.
- WP49 should decide the longer-term packaging path across Streamlit/PyInstaller, Tauri and Electron.
- D015 now defers further installer/packaging investment until the end of the roadmap after online/web validation of product behavior.
- Hugging Face remains a demo/development environment and should not be positioned as the confidential production processing environment.

---

## 2026-06-10 — D010 — Scrub Key MVP lifecycle starts warning-first before encryption

Status: accepted

Decision:

```text
Scrub Key lifecycle must be specified before encryption implementation. The MVP may start with warning-only handling plus explicit lifecycle guidance and protected-local-file guidance, but encrypted key files, local vault behavior, key recovery and Scrub Key schema/container changes require separate implementation workpackages.
```

Rationale:

The Scrub Key is sensitive re-identification data. Adding encryption or vault behavior without a lifecycle policy can create new risks: surprise data loss, unclear passphrase recovery, hidden recovery copies, incompatible key formats, import/export confusion and unsupported security claims. A warning-first MVP preserves the current schema and behavior while making risk visible.

Implications:

- WP26 remains security/lifecycle-specification-only.
- WP27 should specify warning UX before user-facing lifecycle changes.
- WP28 should define expiry/delete policy before any automated deletion behavior.
- WP29 should add secure import/export tests before harder protection behavior.
- Scrub Key encryption implementation remains blocked until a separate approved implementation workpackage defines format, migration, passphrase behavior and tamper protection.
- Local vault / managed key-store behavior remains a later professional/local desktop option, not an MVP change.

---

## Earlier decisions

Earlier accepted decisions remain available in Git history and include:

- D001 — Roadmap becomes risk-driven.
- D002 — PDF support remains TXT-only unless separately approved.
- D003 — Scrub Key is sensitive re-identification data.
- D004 — Streamlit remains prototype/demo layer, not assumed final review UI.
- D005 — Documentation is split into internal and user-facing layers.
- D006 — Workers should self-check Actions/sync where possible.
- D007 — Scrub Key encryption and lifecycle require separate approved specification.
- D008 — Placeholder robustness must be additive and validation-led.
- D009 — WP58 next execution queue after parallel specifications.
