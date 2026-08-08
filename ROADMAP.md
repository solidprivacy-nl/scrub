# SolidPrivacy Scrub — Risk-driven Product & Development Roadmap

This document is the central roadmap for SolidPrivacy Scrub.

Use it together with:

- `WORKPACKAGES.md` for the active execution queue, dependencies and verification gates;
- `CHANGELOG.md` for internal implementation history;
- `RELEASE_NOTES.md` for user-facing product changes;
- `RISK_REGISTER.md` for trust, privacy and product risks;
- `DECISION_LOG.md` for accepted strategic and architecture decisions;
- `PROJECT_PROMPT.md` for worker rules and project governance.

Last roadmap strategy update: 2026-08-08 — the Premium UI direction is now explicitly frozen as a **single-page staged document workspace**: `Toevoegen → Controleren → Downloaden` remain persistently represented in one workspace, exactly one stage is expanded at a time, completed stages collapse to compact summaries, future stages remain passive, and successful completion auto-advances. Three separate routed pages for these core stages are rejected for Standard. This urgent decision intervenes before production Streamlit integration in PR #85 and preserves its reusable pure helper work.

---

## Operational governance — implementation and blind release assurance

Consequential Scrub work follows the canonical cross-project two-role standard used by the Weekly ETF donor architecture:

```text
implementation_operations
→ identifiable release candidate
→ governance_release_assurance blind reconstruction
→ PASS / FAIL / INDETERMINATE
→ authorized action
→ independent post-action confirmation
```

The user remains the single coordinator-facing principal. Implementation cannot certify its own candidate, and governance cannot silently repair it. Scrub adds a blind-review boundary: before its initial decision, governance may inspect source, criteria and raw machine evidence but not implementation handovers, self-assessments or conclusions.

The current maturity is `LEVEL_1_CHECKLIST`, with a later target of `LEVEL_2_MACHINE_EVIDENCE`.

The governance/cross-flow gate that previously blocked the Premium UI line is closed. Issue #70 is closed, PR #73 is merged, the Premium UI contract is merged through PR #80, and the pure Premium core-flow state model is merged through PR #82. The active line is therefore Premium UI implementation, subject to independent assurance for each consequential candidate.

Governed by:
- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`;
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`;
- `DECISION_LOG.md` D042.

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
SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION — independently assured and governance gate closed through issue #70/#73 recovery.
SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT — merged through PR #80; contract only, no production UI behavior.
SCRUB-WP_PREMIUM_CORE_FLOW_STATE_MODEL — merged through PR #82; pure state model only, no production UI behavior.
SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — active in draft PR #85; current candidate contains reusable presentation primitives/tests but production `presidio_streamlit.py` integration has not started.
SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE — urgent architecture/queue intervention approved by the coordinator on 2026-08-08; must be incorporated before PR #85 proceeds to production UI integration.
```

Important UX status:

```text
The review table remains source of truth and fallback.
The old replacement decision helper panel must not return as normal user-facing UI.
The unified side-by-side review, manual missed-value entry, compact placeholder display and grouped export flow form the verified functional baseline.
Direct live-app evidence confirms that this baseline still presents too much of the workflow as one long form.
The Premium Standard target is one document workspace with three persistent stages and one active task, not another isolated expander-cleanup pass and not three routed core-flow pages.
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
- `MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md`;
- `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`;
- `PREMIUM_STAGED_WORKSPACE_DECISION.md`.

UX principles:

- one main review surface before more helper panels;
- review table remains source of truth and fallback;
- serial review remains a guided review layer, not a table replacement;
- highlights are visual aid, not mutation mechanism;
- no repeated per-highlight `Gemarkeerd` labels as the long-term design;
- no click-to-mark, advanced editor or full-document marking in this phase;
- no Scrub Key/export/reinsert behavior changes from review UX work without separate approval;
- technical/debug-like details should move to secondary audit/advanced layers, not disappear.

### Premium core-flow UI realignment — binding staged-workspace decision

Direct coordinator/user evidence on 2026-08-05 established that the remaining interface problem is structural:

```text
The app still behaves visually as one long Streamlit form.
Input, settings, review, corrections, downloads, Scrub Key and audit controls compete on the same page.
```

The approved target remains:

```text
Top-level workflow: Anonimiseren | Terugzetten
Global presentation: Standaard | Expert
Core stages: Toevoegen → Controleren → Downloaden
One primary action per active stage
Progressive and conditional disclosure for settings, other formats, Scrub Key and audit evidence
```

On 2026-08-08 the coordinator explicitly chose how those three core stages must be presented. The Standard anonymization flow is a **single-page staged document workspace**, not three separate routed screens.

Binding interaction model:

```text
One document
→ one persistent workspace
→ three persistent stage headers
→ exactly one expanded/active stage
→ completed stages collapse to compact summaries
→ future stages remain visible but passive
→ successful completion auto-opens the next stage
→ explicit return to an earlier stage is allowed
→ processing-affecting earlier changes invalidate downstream state fail-closed
```

The first-principles reason is that Scrub is an iterative document-review workflow rather than a strictly linear checkout wizard. The interface should represent the **state of one document** rather than force the user to navigate separate pages. A staged workspace keeps the cognitive benefit of one task at a time while preserving context, progress, confidence and easy return from review to input.

The rejected Standard pattern is:

```text
Toevoegen page → Controleren page → Downloaden page
```

The rejected implementation shortcut is also:

```text
classic long Streamlit form
+ multiple independent/nested expanders
```

Stage sections must read as application panels, not as a FAQ/settings accordion. There must be no default nested core-flow expander hierarchy in Standard.

`Standaard` is lower cognitive load, not lower safety. `Expert` preserves full inspection, tuning, audit and troubleshooting. The permanent settings sidebar is not part of the Standard target. Completed stages show only compact orientation/trust summaries rather than full controls.

Target progression example:

```text
Initial:
▼ 1 Toevoegen
  2 Controleren — beschikbaar na verwerking
  3 Downloaden — beschikbaar na controle

After processing:
✓ 1 Toevoegen — contract.docx · Juridisch
▼ 2 Controleren
  3 Downloaden — beschikbaar na controle

After review:
✓ 1 Toevoegen — contract.docx · Juridisch
✓ 2 Controleren — 14 gecontroleerd · 1 handmatig toegevoegd
▼ 3 Downloaden
```

The implementation remains within Streamlit first, but must approximate a single-task application shell. It must not change recognizers, replacement decisions, export bytes, filenames, MIME types, Scrub Key semantics, reinsert behavior, audit evidence or the human-review requirement.

The detailed decision, alternative comparison, interaction rules, safety invariants and acceptance criteria are frozen in `PREMIUM_STAGED_WORKSPACE_DECISION.md`.

### Premium execution sequence — urgent realignment

The previous Premium sequence is amended before production UI integration in PR #85:

```text
0. SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION — completed / gate closed
1. SCRUB-WP_PREMIUM_CORE_FLOW_UI_CONTRACT — completed / PR #80 merged
2. SCRUB-WP_PREMIUM_CORE_FLOW_STATE_MODEL — completed / PR #82 merged
3. SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE — URGENT CURRENT PACKAGE
4. SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — active draft PR #85; production integration paused until package 3 is incorporated
5. SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION
6. SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION
7. SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION
8. SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION
9. SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT
```

PR #85 is **amended, not discarded**. Its current pure `premium_app_shell.py` helpers/tests are consistent with the one-active-stage direction and may be retained. Before production `presidio_streamlit.py` integration, the candidate must additionally freeze/test active/completed/future stage presentation, compact completed summaries, passive future stages, explicit return/edit affordances, auto-progression hooks and the no-three-page-routing rule.

Do not combine input, review and export restructuring into one patch. Do not run shared Streamlit UI packages in parallel. Each consequential production UI candidate receives separate `governance_release_assurance` under the enforced contract.

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

The coordinator has explicitly prioritized the Premium interface. The Premium staged-workspace line is therefore the dominant execution queue until its live closeout, unless a privacy/safety blocker requires interruption.

Current dominant queue:

```text
1. SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE — current; architecture/roadmap/workpackage binding
2. SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — draft PR #85; resume production integration only after #1 is incorporated
3. SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION
4. SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION
5. SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION
6. SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION
7. SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT
```

The earlier Phase 6 trust-hardening packages remain part of project history and may be reopened when required by evidence, but they are not allowed to dilute the current Premium UI focus by default.

Execution principles:

- use synthetic data only;
- preserve legal meaning and keep human review mandatory;
- the Premium shell is presentation/state orchestration, not a license to change recognition or export semantics;
- one document, one workspace, three persistent stages, one active task;
- no three routed pages for `Toevoegen → Controleren → Downloaden` in Standard;
- no nested-expander recreation of the current long form;
- create recognizer or document-processing fixes only from reproducible safety evidence;
- live UI work must be sequential where it touches shared Streamlit/review/export surfaces;
- do not make production-readiness claims from prototype evidence.

### Candidate document-centric manual-correction line

Direct usability evidence supports correction in the main processed-text pane:

```text
select an unmasked value
→ right-click
→ choose a masking type
→ add through the existing manual replacement path
```

The first version is bounded to all exact occurrences of the selected value. It creates a normal document-scoped manual row, keeps the replacement table authoritative and preserves current bound export, Scrub Key and reinsert semantics. Occurrence-specific replacement, a rich editor and a combined Streamlit upgrade are excluded.

The sequence was:

```text
1. SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT
2. SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL
3. SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE
4. SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION
5. SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION
6. SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY
```

The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract, action model, component and production table integration are complete. GitHub-to-Hugging-Face synchronization and live app verification are green. Display-only placeholder compaction is deployed and app-verified without changing binding grammar, entropy, export, Scrub Key or reinsert semantics. The cross-flow safety/governance gate is now closed and no longer blocks Premium UI work.

Recall/benchmark work is reopened only where reproducible safety evidence requires it.

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
Thin helper-driven Streamlit application shell;
one persistent document workspace;
three core Standard stages with exactly one active at a time;
global Standard/Expert presentation;
tested safety/state boundaries;
local-first direction;
and a clear primary export with secondary restore/audit layers.
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

## 11. Zorgfilter v1 — evidence-driven care profile

Approved: 2026-08-03 15:31 Europe/Amsterdam

The first product wedge already identifies Legal and Zorg as the most relevant Dutch professional domains. Zorg now receives an explicit profile line rather than remaining an incidental subset of general and legal recognition.

### Approved policy

```text
Geboortedatum: vervangen
Overige exacte zorgdata: controleren en standaard geselecteerd
Patiënt- en cliëntidentificatie: vervangen
Zorgverleneridentificatie: controleren en standaard geselecteerd
Diagnose, medicatie, dosering, labwaarden en observaties: behouden
Zeldzame-casus-herleidbaarheid: auditwaarschuwing, niet blind maskeren
```

The core product rule is:

```text
Remove identity and patient-specific administrative references while preserving clinical meaning.
```

Zorgfilter v1 is not a generic medical-word filter. It must not make care records clinically unreadable.

### Initial document scope

- daily nursing/care reports;
- care plans and evaluations;
- nursing transfers;
- medical specialist discharge letters;
- GP referrals and consultation letters;
- medication overviews or administration lists;
- laboratory reports;
- MIC/MIM/VIM care-incident reports.

### Architecture and sequencing

The first packages are pure helper, policy, corpus and evidence work. They may proceed without reopening the shared Streamlit review/export flow. The future current-UI integration is permitted by explicit coordinator approval, but only after the corpus baseline, gap triage, recognizer contracts and recognizer implementation are green and no parallel worker is editing the same UI surface.

Preferred helper direction:

```text
care_profile_policy.py
care_test_examples.py
care_profile_baseline.py
care_reference_taxonomy.py
dutch_care_recognizers.py
recognition_profiles.py
```

The existing broad `NL_HEALTHCARE_REFERENCE` category must be assessed and split. Patient numbers, referral references, insurance identifiers and DBC/clinical codes do not share one safe default action.

Current-engine baseline evidence is now recorded: 25 of 81 expected replace/review values were found as exact normalized spans, only 14 under the intended entity type, 11 were misclassified and 56 were missed. The bounded custom-rule baseline produced zero overlaps with the designated clinical preserve passages. Generic NER was excluded, so PERSON and e-mail results are not full-app measurements.

The dedicated pure recognizer implementation is now green but remains unregistered: sixteen care entities pass 37/37 positive contracts, 16/16 negative/collision contracts and all 54 dedicated expectations in the eight-document corpus, with zero protected-clinical overlaps. The next gate is central profile composition and AGB/BSN precedence before any visible Zorg profile is added.

Central profile configuration is now implemented without changing the live UI. The current three options remain exact, while future Streamlit and desktop four-profile orders, thresholds, entity groups, care policy actions and fifteen exact-span precedence winners are frozen. Care recognizer registration and visible UI integration remain the next gated package.

The current Streamlit integration is now implemented and regression-green. `Zorgcontrole — streng` is added without silently becoming the default; the existing Legal profile remains initially selected. Sixteen care recognizers, central entity composition, exact-span precedence, eight synthetic examples and conservative unchecked care candidates are wired into the current flow. Review-selected care detections remain selected but show `Controle nodig`. Export, Scrub Key and reinsert semantics are unchanged. The next gates are cross-profile regression, deployment sync and live app verification.

The deterministic cross-profile regression matrix is now green. Across eight care document families and twelve legal examples, Care and International retain all 108 dedicated care expectations, Care/International and Legal/International dedicated-type parity hold, no dedicated Care or Legal entities leak into the wrong profiles, and no protected clinical phrase is overlapped. The historical legal metadata remains visible as 132/148 deterministic expectations, sixteen recorded gaps and four negative observations; these are existing benchmark observations, not hidden or reclassified as Zorg success. Generic NER remains outside this matrix. GitHub-to-Hugging-Face synchronization and deployed app behavior were confirmed on 2026-08-03; the current-web Zorgfilter line is completed and app-verified. Desktop UX work remains separately gated by Phase 9 and explicit approval.

GitHub-to-Hugging-Face synchronization is now independently verified for merge commit `cca4a25aaff28a7ba647c961d8e50f0e076921e2`: twelve relevant source files match byte-for-byte, all correctly scoped Zorg markers are present, the Streamlit health endpoint returns `200 / ok` and the Space root returns HTTP 200. The initial sync check produced a false negative because two marker groups were assigned to the wrong modules; the hashes were already equal and the corrected verification passed. The remaining gate is coordinator/user confirmation of the visible app behavior and generic-NER observation.

### Current and final interface direction

Current prototype after test-gated integration:

```text
Zorgcontrole — streng
Juridische controle — streng
Algemene Nederlandse controle
Algemene internationale controle
```

Final desktop workspace:

```text
[ Algemeen NL ] [ Zorg ] [ Juridisch ] [ Internationaal ]
```

The active profile remains visible in the document toolbar and never changes silently.

### Sequential workpackages

```text
1. SCRUB-WP_CARE_PROFILE_V1_POLICY_AND_CORPUS_FOUNDATION
2. SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE
3. SCRUB-WP_CARE_PROFILE_GAP_TRIAGE
4. SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS
5. SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION
6. SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR
7. SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION
8. SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX
9. SCRUB-WP_CARE_PROFILE_APP_VERIFY
10. SCRUB-WP_CARE_PROFILE_DESKTOP_UX_CONTRACT
```

Safety boundaries:

- synthetic data only;
- no blind masking of clinical meaning;
- no change to Scrub Key, export or reinsert semantics without a separate package;
- human review remains required;
- corpus or benchmark success does not prove production readiness;
- no cloud document processing is introduced.