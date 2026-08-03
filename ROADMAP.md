# SolidPrivacy Scrub — Risk-driven Product & Development Roadmap

This document is the central roadmap for SolidPrivacy Scrub.

Use it together with:

- `WORKPACKAGES.md` for the active execution queue, dependencies and verification gates;
- `CHANGELOG.md` for internal implementation history;
- `RELEASE_NOTES.md` for user-facing product changes;
- `RISK_REGISTER.md` for trust, privacy and product risks;
- `DECISION_LOG.md` for accepted strategic and architecture decisions;
- `PROJECT_PROMPT.md` for worker rules and project governance.

Last roadmap strategy update: 2026-08-03 — Phase 9 local desktop packaging remains gated, with an AI-first implementation model and explicit human signing, release, security-claim and UX-acceptance gates.

---

## 1. Product vision

Scrub is evolving from a technical Presidio demo into a trustworthy Dutch professional document scrubber for confidential legal and care documents.

The key promise remains:

```text
Sensitive information stays local in the final trust environment.
The user remains in control.
The document stays readable.
Residual risk is visible.
```

Current sequencing principle:

```text
Make the MVP workflow good before investing further in pilot operations, marketing, pricing, sales, promotion or installer work.
```

The active MVP workflow is:

```text
Import -> Scrub -> Review -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

---

## 2. Core product principle

The product is not just a generic anonymizer.

The real problem is:

```text
How can a professional safely use or share confidential documents without losing context, legal meaning, control or auditability?
```

Scrub must optimize for:

1. high recall for sensitive data;
2. context preservation;
3. human review;
4. easy and consistent replacement logic;
5. secure Scrub Key lifecycle;
6. reliable de-anonymization/reinsert;
7. document hygiene;
8. safe export;
9. audit and residual-risk reporting;
10. clear interface and workflow confidence.

Legal and professional context must be preserved. Scrub should replace sensitive values, not legal meaning.

---

## 3. Strategic workflow

The product workflow direction remains:

```text
Scrub -> Review -> Scrub Key -> AI -> Reinsert -> Export -> Audit
```

The roadmap is risk-driven rather than feature-driven.

Highest priority risks:

1. false negatives;
2. Scrub Key leakage or accidental sharing;
3. hidden document content and metadata leakage;
4. placeholder corruption during AI roundtrip;
5. review UX that is not document-centric enough;
6. confusing import/export/reinsert limitations;
7. installer/distribution effort before the product behavior is ready.

---

## 4. Current implementation status

Recent work completed or recorded:

```text
WP19-WP24 — recall/trust foundation.
WP25-WP29C — Scrub Key safety/test line.
WP30-WP34 — placeholder robustness helper/test line.
WP35-WP39 — DOCX hygiene line through clean-DOCX export policy and report-only audit UI.
WP40-WP43 — review UX/frontend decision line.
WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — product-rejected helper panel hidden and verified.
WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — replacement review redesigned around simple user choices.
WP_SIDE_BY_SIDE_REVIEW_ROADMAP_ANCHOR — unified side-by-side review UX direction anchored.
WP45-WP49 — local runtime/packaging decision line; installer deferred.
WP50-WP51 — pilot/ICP thinking artifacts; parked for now.
WP_RECALL_PERSON_NAME_* — diagnostic, contract and helper-level PERSON-name work completed; benchmark follow-up temporarily parked unless a concrete blocker appears.
SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_* through SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_* — the current MVP UI simplification line is completed, synchronized and live-app verified.
SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING — merged, synchronized and live-app verified for DOCX body, table, header and footer restoration.
SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION — completed, synchronized and live-app verified.
SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION — completed with 15/15 cases passing and a critical document/key-binding gap routed to triage.
SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE — completed with a bound-placeholder plus mapping-digest recommendation and a test-first implementation sequence.
SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS — completed with frozen placeholder, digest, legacy and fail-closed model contracts.
SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION — completed with pure binding-ID, placeholder, digest, bound-key and document/key validation helpers.
SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION — completed with bound placeholders and schema-1.1 key export.
SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION — implemented with dual-read import, fail-closed binding enforcement and explicit legacy compatibility; app verification pending.
SCRUB-WP_AI_FIRST_DESKTOP_PACKAGING_ROADMAP_ALIGNMENT — completed as a documentation-only Phase 9 execution-model refinement; installer implementation remains gated.
```

Important UX status:

```text
The review table remains source of truth and fallback.
The old replacement decision helper panel must not return as normal user-facing UI.
The unified side-by-side review, manual missed-value entry and compact export flow form the verified MVP UI baseline.
Further UI work is not the default next line and requires a separately approved package tied to evidence from Phase 6 validation.
```

---

## 5. MVP product quality gate

Phase 7 follow-up is parked until the MVP is credible across:

- import;
- anonymization;
- review;
- replacement logic;
- Scrub Key handling;
- de-anonymization/reinsert;
- export;
- audit/residual-risk reporting;
- interface clarity.

WP50 and WP51 remain useful early thinking artifacts, but they are not the active execution line now.

Do not start WP52 by default.

---

## 6. Current phase order

The current phase order is:

```text
Phase 1 — Trust & recall foundation
Phase 2 — Scrub Key security and lifecycle
Phase 3 — Placeholder robustness for AI roundtrip
Phase 4 — Hidden content and document hygiene
Phase 5 — Document-centric review UX
Phase 6 — MVP workflow validation and trust hardening
Phase 7 — Pilot validation: Legal vs Zorg — parked until MVP quality gate passes
Phase 8 — Scale features: profiles, batch, CLI, enterprise
Phase 9 — Final local desktop/offline installer path
```

### Phase 5/6 — Review UX direction

The review UX target is now:

```text
Source text left | Processed/checked text right
                 | Optional highlights integrated in the processed text
```

This is governed by:

- `DECISION_LOG.md` D021;
- `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md`;
- `REPLACE_LOGIC_UI_REDESIGN_PLAN.md`;
- `MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md`.

UX principles:

- one main review surface before more helper panels;
- review table remains source of truth and fallback;
- serial review remains a guided review layer, not a table replacement;
- highlights are visual aid, not mutation mechanism;
- no repeated per-highlight `Gemarkeerd` labels as the long-term design;
- no click-to-mark, advanced editor or full-document marking in this phase;
- no Scrub Key/export/reinsert behavior changes from review UX work without separate approval;
- technical/debug-like details should move to secondary audit/advanced layers, not disappear.

### Phase 6 — MVP workflow validation and trust hardening

Goal:

```text
Use the online/web prototype and GitHub workflow to validate product behavior before pilot expansion or installer investment.
```

Focus:

- end-to-end workflow testing;
- import and export confidence;
- Scrub Key warning/acknowledgement verification;
- DOCX hygiene reporting;
- unified side-by-side review direction;
- easier replace/review logic;
- residual-risk and audit reporting;
- MVP interface clarity;
- professional export/download flow;
- Hugging Face app verification after GitHub Actions/sync when UI changes.

### Phase 7 — parked pilot validation

WP50 and WP51 are recorded, but Phase 7 is not the active next line.

Phase 7 may reopen when the coordinator confirms the MVP product quality gate has been met.

---

## 7. Active next work direction

The verified MVP UI baseline is now stable enough to move the active line into Phase 6 validation and trust hardening.

Current execution queue:

```text
1. SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX — completed
2. SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE — completed
3. SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING — completed and app-verified
4. SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION — completed and app-verified
5. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION — completed
6. SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE — completed
7. SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS — completed
8. SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION — completed
9. SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION — completed
10. SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION — implemented
11. SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY — active
12. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE
13. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT
```

Execution principles:

- use synthetic data only;
- validate the full supported workflow before adding new features;
- create recognizer or document-processing fixes only from reproducible evidence;
- preserve legal meaning and keep human review mandatory;
- do not reopen broad UI work unless validation reveals a concrete usability or safety blocker;
- do not make production-readiness claims from prototype evidence.

Recall/benchmark work is reopened only where the synthetic validation matrix exposes a concrete false-negative, misclassification or over-masking gap.

Do not start local packaging next steps such as `WP48B` or `WP49B` by default. They require explicit coordinator approval.

Do not start pilot follow-up such as `WP52` by default. It remains gated by `SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT` and explicit coordinator approval.

---

## 8. Parallelization strategy

Safe to do in parallel:

- helper modules with separate files;
- tests that do not touch the same UI flow;
- specifications;
- documentation;
- benchmark data design;
- risk reviews;
- non-UI architecture work.

Do not run in parallel:

- multiple changes to `fix_streamlit_nested_expanders.py` or `presidio_streamlit.py`;
- multiple changes to the same Streamlit patch file;
- `serial_review_panel_ui.py` UI edits without coordination;
- `review_highlight_toggle_panel_ui.py` UI edits without coordination;
- export/download flow changes;
- review table flow changes;
- synchronized scroll implementation;
- custom HTML/component rendering implementation;
- Docker/runtime startup patch-order changes;
- installer/packaging work unless explicitly approved;
- Phase 7 follow-up while the MVP quality gate is not passed.

Use `workpackage_claims/` before starting a package.

---

## 9. Product architecture target

Current prototype architecture:

```text
Streamlit app + helper modules + GitHub Actions + Hugging Face Space demo.
```

MVP architecture target:

```text
Thin Streamlit UI, helper-driven behavior, tested safety boundaries, local-first direction, and clear export/audit workflow.
```

Do not migrate frontend, add a full document editor, introduce cloud document processing, or alter export/Scrub Key/reinsert semantics without a dedicated approved package.

---

## 10. Phase 9 — AI-first local desktop/offline packaging execution model

The final trust environment remains a local Windows desktop installation for confidential documents. Hosting migration and local desktop distribution are separate concerns:

```text
Hugging Face / web prototype = synthetic and approved non-confidential validation
Local signed desktop runtime = confidential production-oriented trust environment
```

Phase 9 remains gated by Phase 6 quality closeout and explicit coordinator approval. This roadmap update authorizes no installer implementation by itself.

### Target end-user distribution

The preferred end-user direction is:

```text
one signed setup.exe for low-friction installation
+ one signed MSI for managed organizational deployment
+ Tauri Windows shell
+ bundled local Python/Presidio engine as a PyInstaller onedir sidecar
+ all required models and assets available locally
+ loopback-only communication on the same PC
+ no required cloud calls, runtime downloads or document telemetry
```

A portable Python folder remains an internal technical validation path, not the intended premium end-user product. A PyInstaller onefile runtime is not the default because extraction to temporary executable directories increases startup, antivirus, cleanup and diagnostic risk. The user may receive one installer file even when the installed application contains multiple controlled runtime files.

### AI-first execution assumption

Phase 9 should be implemented AI-first where the work is deterministic, testable and reversible. Planning assumptions:

```text
First installer implementation:
- 60–70% of development and integration labor may be agent-executed.
- expected development/integration budget after agent substitution: approximately EUR 8,000–24,000.
- agent/build-compute allowance: approximately EUR 1,000–4,000.

Subsequent release cycles:
- 75–90% of repetitive build, test, packaging and release-candidate preparation may be automated.
```

These are budgeting assumptions, not supplier quotations or production-readiness claims. Independent security review, code-signing identity, final release approval and real user acceptance remain separate costs and responsibilities.

### Agent-autonomous scope

Within isolated workstations or disposable Windows test VMs, scoped agents may autonomously:

- install approved build SDKs and packaging dependencies;
- inventory and pin Python packages, native libraries and model assets;
- build and debug PyInstaller onedir bundles;
- build the Tauri shell and local sidecar lifecycle;
- create setup.exe and MSI release candidates;
- implement loopback binding, health checks and shutdown cleanup;
- run offline, install, upgrade, uninstall, Defender and synthetic document tests;
- inspect network, process, filesystem, logging and temporary-file evidence;
- maintain CI, checksums, SBOMs, release notes and handovers;
- open pull requests and prepare unsigned release candidates.

All test documents and Scrub Keys must remain synthetic. Agents must not weaken review, Scrub Key, export or privacy controls to make packaging easier.

### Human-controlled gates

The following responsibilities must not be delegated as an unreviewed autonomous chain:

- legal publisher identity and long-lived code-signing authority;
- final production signing and public release;
- acceptance of privacy and security claims;
- approval of export, Scrub Key or document-processing semantic changes;
- acceptance testing by non-technical users on real managed Windows environments;
- independent security validation where a strong local-only product claim is made.

No single agent should simultaneously hold unrestricted repository-write, signing-identity and public-release authority. Use protected environments, least-privilege identities and an explicit human release gate.

### Indicative external and retained costs

Costs that remain materially external or human-controlled include:

```text
- managed Windows code signing: approximately EUR 120–300 per year;
- build/CI/test infrastructure: usually limited, depending on runner and artifact use;
- physical or managed Windows test devices: approximately EUR 0–1,500 initially;
- targeted independent desktop/privacy security review: approximately EUR 5,000–15,000;
- broader penetration testing and retest, if required: approximately EUR 15,000–30,000;
- human packaging/security/release oversight: retained even with extensive agent autonomy.
```

### Phase 9 execution sequence

When the phase is explicitly opened, use small sequential workpackages:

```text
1. Desktop distribution and local-only security contract
2. Offline dependency, native-library and model inventory
3. PyInstaller onedir engine-sidecar packaging spike
4. Tauri shell and sidecar lifecycle proof
5. Network, temp-file, logging, crash and endpoint-security validation
6. Signed setup.exe and MSI release candidate
7. Managed Windows pilot, upgrade, rollback and uninstall validation
8. Independent security review and quality-gate closeout
```

Do not collapse signing, release and security acceptance into the same autonomous worker. Do not make a production/local-only claim from successful packaging alone.
