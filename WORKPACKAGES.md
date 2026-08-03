## 2026-08-03 16:25 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_GAP_TRIAGE

Status: completed; all current care-corpus expectations classified.

Goal:
- Route every correct, missed or misclassified baseline value to a concrete follow-up mechanism before recognizer implementation.

Result:

```text
Expectations classified: 81/81
Reuse current recognizer: 14
Generic profile dependency: 13
Contextual care review recognizer: 36
Care-specific reclassification: 10
Dedicated care reference recognizer: 5
Care collision guard: 3
Unclassified: 0
```

Key decisions:
- keep address, BIG, BSN, date-of-birth and Dutch-phone recognizers;
- keep generic PERSON and e-mail in the generic local profile layer;
- split broad healthcare/legal references into care-specific policy entities;
- build a context-bound review layer for providers, organizations, locations, room/bed and care-event dates;
- require explicit AGB/BSN precedence and negative medical-number contracts;
- keep diagnosis, medication, dosages, lab values, observations and roles under preservation guards.

Evidence:
- `CARE_PROFILE_GAP_TRIAGE.md`
- `output/validation/care_profile_v1_gap_triage.json`

Active next package:
- `SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS`

Boundaries:
- no recognizer or UI implementation;
- no threshold, export, Scrub Key or reinsert change;
- synthetic data only;
- human review remains required;
- production readiness remains false.

## 2026-08-03 16:10 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE

Status: completed; corrected current-engine evidence baseline implemented and validated.

Goal:
- Measure the unchanged deterministic Dutch custom recognizers against the eight-document synthetic care corpus before dedicated Zorgfilter recognizers are added.

Result:

```text
Expected replace/review values: 81
Exact normalized spans found: 25 (30.86%)
Correct intended entity type: 14 (17.28%)
Misclassified values: 11
Missed values: 56
Protected clinical phrase overlaps: 0
```

Key evidence:
- strong bounded coverage for addresses, BIG numbers, BSN, dates of birth and Dutch telephone numbers;
- no bounded custom-rule coverage for generic PERSON names, care-provider names, care organizations, exact care-event dates, care locations or room/bed references;
- review-selected layer: 4/42 spans found and 3/42 correctly classified;
- one AGB code collided with BSN recognition;
- broad existing healthcare/legal references find several values but do not express the approved care policy;
- generic NER was excluded and the baseline is not a full-app or production-readiness measurement.

Evidence:
- `CARE_PROFILE_CURRENT_ENGINE_BASELINE.md`
- `output/validation/care_profile_v1_current_engine_baseline.json`

Active next package:
- `SCRUB-WP_CARE_PROFILE_GAP_TRIAGE`

Boundaries:
- synthetic data only;
- no recognizer behavior, UI, threshold, export, Scrub Key or reinsert change;
- human review remains required;
- production readiness remains false.

## 2026-08-03 15:31 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_V1_POLICY_AND_CORPUS_FOUNDATION

Status: completed; policy/corpus foundation implemented and validated.

Goal:
- Establish the approved Zorgfilter v1 policy and a fully synthetic, machine-readable care-document corpus before adding recognizers or UI.

Current package scope:
- roadmap, decision and risk alignment;
- pure care-profile action contract;
- eight synthetic care-document families;
- corpus contract tests;
- current custom-recognizer baseline helper and report generator.

Approved policy:
- date of birth and patient/client identity: replace;
- other exact care dates and provider identity: review, selected by default;
- diagnosis, medication, dosage, lab results and observations: preserve;
- rare-case re-identification: audit warning only.

Active next package:
1. `SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE`
2. `SCRUB-WP_CARE_PROFILE_GAP_TRIAGE`
3. `SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS`
4. `SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION`
5. `SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR`
6. `SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION`
7. `SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX`
8. `SCRUB-WP_CARE_PROFILE_APP_VERIFY`
9. `SCRUB-WP_CARE_PROFILE_DESKTOP_UX_CONTRACT`

Boundaries:
- no Streamlit change in this package;
- no recognizer behavior change yet;
- no export, Scrub Key, reinsert, cloud or dependency change;
- synthetic data only;
- current Phase 6 binding verification remains an independent active gate.

## 2026-08-03 14:47 Europe/Amsterdam — SCRUB-WP_AI_FIRST_DESKTOP_PACKAGING_ROADMAP_ALIGNMENT

Status: completed; documentation/strategy alignment only.

Summary:
- Added an AI-first execution model for the final local Windows desktop/offline packaging phase.
- Preserved the existing gate: installer implementation remains deferred until Phase 6 quality closeout and explicit coordinator approval.
- Refined the eventual target to a signed Tauri shell, bundled PyInstaller onedir Python/Presidio sidecar, setup.exe and MSI.
- Recorded planning assumptions that 60–70% of first-cycle development/integration labor and 75–90% of later repetitive release work may be agent-executed.
- Kept publisher identity, signing, public release, security claims, real-user acceptance and safety-critical semantic changes under human control.
- Added no product code, installer, runtime, dependency or UI change.

Next recommended step:
- Continue the active Phase 6 queue. Open the Phase 9 desktop distribution contract only after quality-gate closeout and explicit approval.

## 2026-07-28 00:52 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Status: implemented; full GitHub Actions passed; app verification pending.

Summary:
- Binding validation now gates every text, TXT, DOCX and PDF-to-TXT reinsert before replacement.
- Correct bound keys are verified; legacy v1.0 remains explicit unverified compatibility.
- Wrong, mixed, missing or corrupted bindings restore zero values.
- The existing three-step flow and final confidentiality acknowledgement remain unchanged.

Next recommended step:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY` after merge and sync.

## 2026-07-27 21:45 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION

Status: implemented; targeted validation pending.

Summary:
- Bound placeholder and schema-1.1 key creation is integrated into anonymization/export.
- Custom replacement text is preserved and cannot be silently represented as a verified bound mapping.
- Reinsert enforcement remains the active next package.

Next recommended step:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`.

## 2026-07-27 20:05 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION

Status: implemented; targeted validation passed; PR verification pending.

Summary:
- Added `scrub_key_binding.py` as a pure, Streamlit-free binding model.
- Implemented local binding-ID generation using ten random bytes and uppercase base32.
- Implemented strict binding-ID validation and automatic/manual bound placeholder build/parse helpers.
- Implemented strict document binding-ID extraction from bound placeholders.
- Implemented canonical mapping-digest payload and SHA-256 digest helpers matching the frozen fixture.
- Implemented bound Scrub Key structural, policy, item-binding, duplicate and digest validation.
- Implemented all eight frozen document/key statuses, including explicit legacy-v1.0 unbound compatibility.
- Enforced six fail-closed statuses before any later replacement integration.
- Preserved immutable inputs and stable result fields.
- Integrated nothing into current placeholder generation, export, reinsert or UI paths.

Validation boundaries:
- Contract fixture digest matched exactly.
- Targeted model, contract, legacy import/export and roundtrip tests passed.
- No Streamlit, network, AI, cloud or file-write behavior exists in the model.
- Production readiness: false.
- Human review remains required.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION`.

## 2026-07-27 19:38 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS

Status: completed; contract frozen; PR validation pending.

Summary:
- Added a versioned binding contract and synthetic fixture before any product implementation.
- Locked binding ID grammar `B[A-Z2-7]{16}` with an 80-bit random payload.
- Locked automatic placeholders as `[LABEL_BINDINGID_INDEX]` and manual placeholders as `[LABEL_BINDINGID_HANDMATIG_INDEX]`.
- Locked bound Scrub Key metadata direction as schema version `1.1`, binding version `1`, a document binding ID and canonical SHA-256 mapping digest.
- Locked eight binding statuses and six fail-closed statuses that must produce zero replacements.
- Locked explicit legacy-v1.0 unbound compatibility without silent upgrading.
- Preserved the existing three-step source → key → download UX and final confidential-download acknowledgement.
- Defined the pure helper responsibilities for model implementation.
- Changed no product helper, UI, placeholder generation, Scrub Key schema implementation, export or reinsert behavior.

Validation boundaries:
- Fixed synthetic digest: `516075e4970f0def6052aaac6885e12339e7cdbe012d4104aa7387c51a53faa3`.
- Mapping digest is accidental-corruption evidence, not authenticity or a signature.
- Malformed placeholders are never guessed or repaired.
- Production readiness: false.
- Human review remains required.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`.

## 2026-07-27 19:18 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE

Status: completed; targeted validation passed; PR verification pending.

Summary:
- Classified the critical same-placeholder wrong-key finding by accidental pairing, accidental corruption and malicious tampering.
- Rejected document labels, complete-content hashes, placeholder-list hashes, filenames, hidden metadata and extra sidecars as sufficient primary binding controls.
- Recommended a non-sensitive document binding ID carried in every automatic/manual placeholder and the corresponding Scrub Key.
- Recommended a canonical SHA-256 mapping digest as a complementary accidental-corruption control, not as an authenticity signature.
- Deferred signature/HMAC protection until a trusted local signing-key lifecycle exists.
- Preserved the three-step document-first reinsert flow without new confirmation buttons or checkboxes.
- Changed no product code, UI, schema, placeholders, export or reinsert semantics.

Approved sequential implementation line:
1. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`
2. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`
3. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION`
4. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`
5. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`

Optional later package:
- `SCRUB-WP_MVP_MALFORMED_PLACEHOLDER_DIAGNOSTIC_HARDENING`.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`.

## 2026-07-27 18:55 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION

Status: completed; deterministic validation passed; PR verification pending.

Summary:
- Added a versioned synthetic adversarial matrix with 15 Scrub Key and placeholder roundtrip scenarios.
- Verified intact, repeated, missing, unknown, translated, merged, malformed and changed placeholder behavior.
- Verified duplicate, incomplete, malformed, tampered and wrong Scrub Key behavior.
- Confirmed deterministic local execution with no AI or cloud processing.
- Changed no product code, UI, Scrub Key schema, export or reinsert semantics.

Validation result:
- Cases: 15.
- Failing cases: 0.
- Findings: 2.
- Critical findings: 1.
- Medium findings: 1.
- Production readiness: false.
- Human review remains required.

Critical evidence:
- A structurally valid wrong or tampered Scrub Key that reuses the same placeholder namespace can restore incorrect original values without a detectable mismatch.
- This requires separate triage because a safe solution may affect document/key binding, Scrub Key schema or export semantics.

Secondary evidence:
- Malformed tokens outside the strict placeholder grammar are reported indirectly through expected placeholders not found, rather than as explicit unknown malformed tokens.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE`.

## 2026-07-27 18:28 Europe/Amsterdam — SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Evidence:
- PR #38 merged as `390f381c1464883f220716655c5067dadd0bb4c9`.
- Final clean PR GitHub Actions run #1678 passed.
- The coordinator live-tested the deployed three-step workflow and confirmed it is working.
- The live result proves that the merged UI reached the Hugging Face Space.

Verified behavior:
- Step 1 begins with the source document or pasted text.
- Step 2 accepts and automatically validates the corresponding Scrub Key.
- Local deterministic reinsert starts automatically for one valid source/key pair.
- Redundant source/key acknowledgement checkboxes and execution buttons are absent.
- One confidentiality acknowledgement remains immediately before download.
- Existing output filenames, MIME types, audit reporting and DOCX/PDF boundaries remain intact.

Active next package:
- `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

## 2026-07-27 17:06 Europe/Amsterdam — SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION

Status: implemented; full suite passed; final PR validation pending.

Evidence:
- Live DOCX reinsert passed for body, table, header and footer.
- The same verification exposed a concrete interface-clarity blocker: uploaded source/key files still required hidden follow-up checkboxes and action buttons.

Summary:
- Reordered reinsert to source first, Scrub Key second and restored download third.
- Added pure helper orchestration for input normalisation, deterministic request signatures and dispatch to existing local helpers.
- Automatically validates a supplied Scrub Key and automatically runs reinsert for one valid source/key pair.
- Removed separate source/key processing acknowledgements and buttons.
- Retained one final confidentiality acknowledgement at the restored-output download boundary.
- Preserved TXT, DOCX, PDF-to-TXT and pasted-text paths, audit reporting, filenames, MIME types and safety boundaries.

Validation:
- Full repository suite: 797 passed.
- Final GitHub Actions pending after governance finalisation.
- Hugging Face sync and live app verification required after merge.
- Human review remains required; production readiness remains false.

Active next package after verification:
- `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

## 2026-07-17 22:30 Europe/Amsterdam — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Status: completed / ready for PR verification.

Summary:
- Extended deterministic DOCX reinsert from `word/document.xml` to existing `word/header*.xml` and `word/footer*.xml` text nodes.
- Preserved body/table behavior and unrelated OOXML package parts.
- Aligned existing DOCX reinsert copy with the supported body/table/header/footer scope without adding controls.
- Kept comments, tracked-change-only parts, footnotes/endnotes, text boxes, metadata and split placeholders explicitly unsupported.
- Resolved the DOCX header/footer finding and retained the PDF TXT-only/no-OCR boundary.

Validation:
- DOCX header/footer resolution: true.
- Resolved findings: 1.
- Remaining findings: 1.
- Production readiness: false.
- Human review remains required.
- Final clean-branch GitHub Actions validation required before merge.
- Hugging Face sync and live app verification required after merge.

Active next package after verification:
- `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

## 2026-07-17 11:45 Europe/Amsterdam — HF Space runtime incident closeout

Status: completed and app-verified.

Summary:
- Restored the Hugging Face Space and confirmed runtime stage `RUNNING`.
- Coordinator confirmed that the application opens again.
- Merged a conservative sync-churn guard so clearly non-runtime-only commits no longer rebuild the Space.
- Removed temporary recovery and probe workflows/triggers.
- No product behavior or privacy controls changed.

Active next package:
- Resume `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING` in PR #33.

## 2026-07-17 22:08 Europe/Amsterdam — SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE

Status: completed / ready for PR verification.

Summary:
- Classified all 2 evidence items from the Phase 6 synthetic matrix.
- Confirmed that the corrected matrix contains no reproducible false negative, misclassification or role-over-masking result that justifies recognizer changes.
- Routed the DOCX header/footer reinsert limitation and PDF restored-TXT-only boundary to `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.
- Recorded the `.invalid` fixture correction so it cannot reappear as a false product gap.
- No product code or behavior changed.

Validation:
- Machine-readable triage must match every evidence gap in the source report.
- Recognizer fix required: false.
- Production readiness: false.
- Human review remains required.
- GitHub Actions pending final PR validation.
- App verification not applicable.

Active next package:
- `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.

## 2026-07-17 20:20 Europe/Amsterdam — SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

Status: completed / ready for PR verification.

Summary:
- Added a versioned synthetic validation manifest with TXT, DOCX and text-based PDF cases.
- Added pure helper-driven validation for import, review rows, manual additions, replacements, Scrub Key, reinsert, export representation and DOCX hygiene evidence.
- Generated `output/validation/mvp_phase6_synthetic_validation_report.json` as the machine-readable Phase 6 baseline.
- Recorded existing DOCX header/footer reinsert and PDF TXT-only limitations as evidence rather than silently accepting or changing them.
- No UI, recognizer, export, Scrub Key, reinsert or document-processing semantics changed.

Validation:
- Cases: 3.
- Failing cases: 0.
- Evidence gaps: 3.
- Categories: false_negative_or_detection_gap, known_docx_reinsert_limitation, known_pdf_reinsert_limitation.
- Production-readiness claim: false.
- Human review remains required.
- GitHub Actions pending final PR validation.
- App verification not applicable.

Active next package:
- `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE`.

## 2026-07-17 20:12 Europe/Amsterdam — SCRUB-WP_MVP_PHASE6_ROADMAP_REALIGNMENT

Status: completed / ready for PR verification.

Summary:
- Closed the verified MVP UI simplification line as the default development focus.
- Made Phase 6 end-to-end workflow validation and trust hardening the active execution line.
- Added `MVP_PHASE6_EXECUTION_PLAN.md` with the ordered validation, triage, hardening, evidence and quality-gate packages.
- Preserved the Phase 7 pilot, local packaging and production-readiness gates.
- No product code, tests, UI, recognizers, replacement semantics, export, Scrub Key, reinsert, document processing, runtime or dependencies changed.

Validation:
- Documentation consistency checks required through PR review and GitHub Actions.
- Hugging Face sync not functionally relevant because no app code changed.
- App verification not applicable.

Active next package:
- `SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX`.

## 2026-07-16 23:43 Europe/Amsterdam — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Summary:
- Live Hugging Face app verification passed after PR #28 merge.
- The manual correction panel opens with one concise caption, a compact three-column input row and one full-width submit action.
- The duplicate internal heading is absent.
- Synthetic value `lantaarnbloem` was successfully added and is visible in the replacement table as `[WAARDE_HANDMATIG_01]` with status `Handmatig toegevoegd`.
- The screenshot confirms the merged UI reached the Hugging Face Space and no Script execution error is visible.
- No product code or behavioral semantics changed in this docs-only closeout.

Validation:
- PR #28 final GitHub Actions test run passed before merge.
- Hugging Face sync confirmed by live deployed UI.
- App verification passed.

Related package status:
- `SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION` — completed and app-verified.

Next recommended step:
- Use the simplified MVP UI with representative synthetic legal documents before approving another UI package.

## 2026-07-16 20:40 Europe/Amsterdam — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: completed / ready for app verification.

Summary:
- Converted the open manual correction form from a vertical stack to one compact three-column input row.
- Removed the duplicate internal `Gemiste waarde toevoegen` heading.
- Kept the expander collapsed by default and retained one full-width submit action.
- Preserved validation, session state, replacement-table integration and all export/Scrub Key/reinsert semantics.

Validation:
- Required worker validation passed.
- GitHub Actions pending after PR update.
- Hugging Face sync pending after merge.
- App verification required after sync.

Next recommended step:
- `SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_APP_VERIFY`.

## 2026-07-05 22:42 Europe/Amsterdam — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Summary:
- Recorded live app verification for the Review/Export vertical-density implementation.
- Confirmed the Export section is materially less tall and less form-like because TXT/DOCX/PDF downloads are shown in a compact row.
- Confirmed Review safety controls remain visible or accessible: Basiscontrole/Expertcontrole, Markeringen tonen, side-by-side review, Gemiste waarde toevoegen, vervangtabel and replacement status.
- Confirmed Scrub Key, audit/technical files and DOCX hygiene audit remain separate and accessible.
- No product code, tests, export payloads, filenames, MIME types, Scrub Key JSON, reinsert behavior or startup/runtime behavior changed in this closeout.

Validation:
- Coordinator live Hugging Face screenshot reviewed.
- GitHub Actions for PR #26 passed before merge.
- Live Hugging Face app shows the merged UI behavior.
- `git diff --check` required before PR.

Next recommended step:
- Decide whether the current MVP UI is good enough for this pass, or start a new separately approved small UI package.

Related package status:
- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_PLAN` — completed and merged.
- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_CONTRACT_TESTS` — completed and merged.
- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION` — completed and app-verified.

## 2026-07-05 22:13 Europe/Amsterdam — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / local validation passed.

Summary:
- Implemented the conservative Option B Review/Export density pass.
- Compressed repeated Review helper copy without hiding the main side-by-side review.
- Kept manual missed-value entry and the replacement table collapsed and accessible.
- Changed the primary TXT/DOCX/PDF document downloads from three stacked buttons into a compact three-column layout.
- Preserved export payloads, filenames, MIME types, Scrub Key JSON, reinsert behavior, recognition behavior and startup/runtime boundaries.

Validation:
- Local validation passed.
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required because visible UI behavior changed.

Next recommended step:
- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_APP_VERIFY`.

## 2026-07-05 01:13 Europe/Amsterdam — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / local validation passed.

Summary:
- Resumed the implementation branch after the connector-only worker was blocked before product edit.
- Grouped the existing upload, synthetic example selector and pasted/extracted text area into one input surface under the single `1. Voeg document of tekst toe` heading.
- Preserved existing input variables, input precedence, TXT/DOCX/PDF support, review/export/Scrub Key/reinsert/audit behavior and startup/runtime boundaries.
- Added a source-level implementation guard for the unified input surface.

Validation:
- Local validation passed.
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required after merge/sync because visible UI grouping changed.

Next recommended step:
- Run required guardrail tests, open PR, verify Actions, merge when green, verify Hugging Face sync, and request live app verification.

## 2026-07-04 23:18 Europe/Amsterdam — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS

Status: completed / PR validation pending.

Summary:
- Added source-level contract tests for the duplicate input-surface simplification line.
- Locked the intended single `1. Voeg document of tekst toe` input step before any implementation touches `presidio_streamlit.py`.
- Protected existing TXT/DOCX/PDF upload support, synthetic legal examples, pasted/extracted text area, input precedence, review controls, Scrub Key/export/audit surface and startup-patch boundaries.
- No product code, UI behavior, export semantics, Scrub Key semantics, reinsert behavior, recognizers, dependencies or startup/runtime patches changed.

Validation:
- Targeted and related source-level checks are expected through PR validation/GitHub Actions.
- Hugging Face sync is not applicable until merge.
- App verification is not applicable for this contract-test-only package because no UI behavior changed.

Next recommended step:
- Review PR validation. If green, merge and start `SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION` as the next narrow package.

## 2026-07-03 00:00 UTC — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / PR validation pending.

Summary:
- Calmer side-by-side review copy implemented in `side_by_side_review_panel_ui.py`.
- The review surface now refers more clearly to the safe download step while keeping the comparison report-only.
- Added `tests/test_review_surface_simplification_implementation.py`.
- Updated source-level copy tests for the calmer review surface.
- No replacement logic, export content, filenames, MIME types, Scrub Key JSON, reinsert behavior, recognizers, benchmarks, runtime/startup or dependency behavior changed.

Validation:
- Targeted and related tests are expected through PR validation/GitHub Actions.
- Hugging Face sync required after merge.
- Live app verification required after Actions and sync are green because visible UI copy changed.

Next recommended step:
- Review PR validation. If green, merge and request live app verification.

## 2026-06-23 20:52 Europe/Amsterdam — Full-suite validation update — SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

- Full suite passed: `python -m pytest tests -x -vv` → 647 passed in 108.30s.
- `git diff --check` passed.
- Local implementation validation complete.
- GitHub Actions, GitHub to Hugging Face sync and live app verification remain pending until PR/merge/sync.

## SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

Status: in_progress / implementation complete / full-suite validation pending

Scope completed:
- migrated reinsert UI to direct source via `reinsert_mode_ui.py`;
- simplified visible reinsert flow into four user-facing steps;
- kept `presidio_streamlit.py` change minimal;
- added startup no-op guard for direct-source reinsert UI;
- added source-level UI contract tests.

Validation so far:
- targeted reinsert simplification test passed;
- existing reinsert UI patch tests passed;
- warning/two-mode UI tests passed.

Remaining:
- run full test suite;
- commit and open PR;
- verify GitHub Actions;
- verify GitHub to Hugging Face sync;
- request live app verification.


# SolidPrivacy Scrub — Workpackages

Repository: `solidprivacy-nl/scrub`.

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

## Claim rule

Before starting a package, check `workpackage_claims/`. If a claim for the same workpackage is already `in_progress`, stop and report the collision. If no claim exists, create one before changing files. When done, update the claim with status, final commit, handover path, validation and next step.

## Current status

```text
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION — implemented / PR validation pending; visible review copy changed; live app verification required after Actions/HF sync.
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS — completed / merged to main / Actions + HF sync green.
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_PLAN — completed / merged to main / Actions + HF sync green.
SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_IMPLEMENTATION_RESTART — completed and verified; default UI flow simplified toward execution interface, secondary controls collapsed, no export/Scrub Key/reinsert/recognizer/benchmark/startup semantics changed.
SCRUB-WP_REVIEW_COPY_POLISH_IMPLEMENTATION — completed; small visible Dutch copy polish for side-by-side review and serial review labels, no product behavior or export semantics changed.
SCRUB-WP_MAIN_NOOP_CLEANUP — completed; accidental noop files and accidental copy-polish claim were removed from main.
SCRUB-WP_MVP_UI_APP_VERIFICATION_CLOSEOUT — completed; verification/closeout-only status recorded for the current MVP UI baseline, no product code or export semantics changed.
WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN — completed; MVP UI cleanup and export/download redesign route planned.
WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS — completed and verified; contract tests added for professional export/download UX redesign.
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION — superseded by direct repair after startup-patch app verification failed.
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR — completed and verified; export/download UX implemented directly in presidio_streamlit.py.
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN — completed; sharp interface cleanup plan added without adding a new review loop.
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION — completed and verified; step-by-step review collapsed by default, debug governance captions removed from primary UI, Actions/HF/app verified.
WP_MVP_FAST_MANUAL_MASK_ENTRY — completed and verified; simple manual entry for missed values is implemented in the existing review flow and live app verified.
WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY — completed and verified.
WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS — completed and verified.
WP_RECALL_PERSON_NAME_COVERAGE_TESTS — completed and verified.
WP_RECALL_BENCHMARK_THRESHOLDS_PLAN — completed.
WP_RECALL_BENCHMARK_REPORT_REVIEW_2 — completed.
WP_SERIAL_REVIEW_UI — completed and app-verified.
```

Earlier completed workpackages remain available in Git history and handover files.

## Active product line

```text
Import -> Scrub -> Review -> Handmatig aanvullen -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

## Review UX / frontend baseline

The review table remains source of truth and fallback. The normal app keeps one central side-by-side review surface, visible markers, a simple manual missed-value entry, the collapsible replacement table, optional step-by-step review, export/download and DOCX hygiene audit.

Current product direction remains MVP interface cleanup and fast anonymization workflow before more recall/benchmark follow-up.

## MVP UI/export redesign status

Planning, contract and implementation files:

```text
MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md
MVP_UI_APP_VERIFICATION_CLOSEOUT.md
EXPORT_DOWNLOAD_UX_CONTRACTS.md
tests/test_export_download_ux_contracts.py
EXPORT_DOWNLOAD_UX_IMPLEMENTATION.md
tests/test_export_download_ux_implementation.py
REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN.md
manual_mask_entry.py
presidio_streamlit.py
serial_review_panel_ui.py
side_by_side_review_panel_ui.py
tests/test_review_copy_polish_ui.py
REVIEW_SURFACE_SIMPLIFICATION_PLAN.md
REVIEW_SURFACE_SIMPLIFICATION_CONTRACTS.md
tests/test_review_surface_simplification_contracts.py
tests/test_review_surface_simplification_implementation.py
```

The failed startup-patch route was removed after live app verification showed the old export section. Direct implementation now lives in `presidio_streamlit.py` and is verified in the live app.

The review debug collapse implementation keeps the change interface-focused: the existing serial review renderer is collapsed by default and no new review/benchmark/safeguard loop is introduced. Verification shows the primary review UI no longer displays old debug/governance captions.

The fast manual mask entry implementation adds a simple MVP control near `2. Controleer resultaat` so a user can add a missed value to the existing replacement table. It does not add right-click, context menu, custom editor, export semantics, Scrub Key semantics, reinsert semantics or recognizer changes. Actions, Hugging Face sync and live app verification are complete.

The MVP UI app verification closeout records the current verified MVP UI baseline as an administrative checkpoint only. It does not change product code, UI behavior, export semantics, Scrub Key semantics, reinsert semantics, recognizer logic, benchmark logic or local packaging.

The review copy polish implementation improves visible Dutch helper text in the side-by-side review and serial review panel only. It does not change the review table, export construction, Scrub Key, reinsert, recognizers, benchmarks or local packaging.

The review surface simplification line protects and implements a calmer side-by-side review copy before broader review-flow implementation. Export, Scrub Key, reinsert and recognition behavior remain unchanged.

Contract and implementation protection covers:

```text
export/download grouping
Scrub Key separation and warning
primary document downloads vs audit downloads
no export semantics change
audit/technical details remain available
copy-cleanup direction
implementation route
manual missed-value entry through the existing replacement table
MVP UI verification closeout without product behavior change
copy polish without product behavior change
review-surface simplification boundaries before implementation
```

## Recall/benchmark status

Recall/benchmark follow-up packages are temporarily parked unless a concrete blocker appears.

## Active / next recommended execution queue

```text
1. SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX
2. SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE — only for reproducible gaps found by the matrix
3. SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING
4. SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION
5. SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE
6. SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT
```

The UI simplification baseline is completed and app-verified. Do not start another UI package by default; use evidence from Phase 6 validation to justify any future UI change.

## Boundaries

Do not start further UI implementation, export/download implementation, Scrub Key, reinsert, benchmark-gate, local packaging or broad architecture work without separate coordinator approval and a dedicated workpackage.

Do not run parallel edits to `presidio_streamlit.py`, review table flow or export/download flow.

## SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE — completed

Status: completed / ready for PR verification.

Summary:
- Reproduced DOCX side-by-side preview order issue with synthetic paragraph/table markers.
- Fixed DOCX plain-text extraction to preserve interleaved paragraph/table body order.
- No export, Scrub Key or reinsert semantics changed.

Validation:
- Targeted DOCX/reinsert/hygiene tests: 40 passed.
- Full suite: 649 passed in 102.51s.

## SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_PLAN — completed

Status: completed as planning/design-only; merged to main.

Summary:
- Added `REVIEW_SURFACE_SIMPLIFICATION_PLAN.md` for the next premium MVP review-surface simplification line.
- Target flow: `1. Voeg document toe` -> `2. Controleer resultaat` -> `3. Download veilig`.
- Keeps side-by-side review central, review table available as source of truth/fallback, and safety/audit controls available through calmer secondary layers.
- Defines `SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS` as the recommended next package before implementation touches `presidio_streamlit.py` or review flow.

Validation:
- Planning/design-only package; no product tests required.
- No app verification required because no UI behavior changed.
