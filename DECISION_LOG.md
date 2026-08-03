## 2026-08-04 — D040 — Use a two-stage server-authoritative protocol for direct masking from processed text

Status: accepted product, UX and implementation-sequence decision

Decision:

```text
Allow a user to select an unmasked value in Verwerkte tekst, invoke a right-click or visible/keyboard masking action, inspect the server-validated exact-occurrence impact, choose a broad type and create one normal manual replacement row. Version one masks all safe exact occurrences only.
```

Protocol:

```text
inspect_selection
→ server validates UTF-16 offsets, text, document scope, processed hash, collisions and occurrence count
→ ready / confirmation_required / blocked inspection result
→ commit_manual_mask with a current single-use inspection ID
→ server revalidates and creates the bound manual row
```

Safety boundaries:
- one to five safe exact occurrences are ready;
- six to twenty require explicit confirmation;
- more than twenty are blocked from the quick path;
- embedded substrings, nested included replacement terms, marked-range intersections, duplicates, stale views and replays fail closed;
- the review table remains source of truth and `Gemiste waarde toevoegen` remains fallback;
- browser code never creates placeholders, mutates the table, writes a Scrub Key or builds an export;
- no external assets, telemetry, browser persistence or cloud processing;
- no occurrence-specific replacement, rich editor or Streamlit upgrade in this line.

Reason:
- direct correction where a false negative is noticed reduces navigation friction and copying mistakes;
- a server-derived impact step is required because browser-supplied counts and types are untrusted;
- all-exact behavior matches current replacement/export/Scrub Key/reinsert semantics;
- occurrence-specific behavior would require a separate span-aware architecture.

Approved sequence:
1. `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT`
2. `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL`
3. `SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE`
4. `SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION`
5. `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION`
6. `SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY`

Evidence:
- coordinator/user approval at 2026-08-04 00:09 Europe/Amsterdam;
- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`;
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`;
- `test_cases/processed_text_selection_masking/contract.json`.

## 2026-08-03 — D039 — Add Zorgfilter v1 with clinical-context preservation

Status: accepted product and implementation-sequence decision

Decision:

```text
Add an explicit Dutch Zorg profile. Replace date of birth and patient/client identity by default. Show other exact care dates, provider identity, BIG/AGB, organizations and locations for review and select them by default. Preserve diagnosis, medication, dosage, laboratory results and observations. Surface rare-case indirect re-identification as residual-risk evidence rather than blindly masking clinical meaning.
```

Implementation sequence:
- policy and fully synthetic corpus first;
- current-engine baseline and gap triage second;
- recognizer contracts and pure recognizer implementation before UI;
- central profile configuration before adding the fourth Streamlit profile;
- cross-profile regression and live app verification before closeout.

Reason:
- Care documents contain both direct identifiers and essential clinical meaning.
- A broad medical-word filter would destroy usability and potentially clinical/legal context.
- The current `NL_HEALTHCARE_REFERENCE` category combines values with different privacy policies and must be split through evidence-driven work.
- A fourth UI label without dedicated detection evidence would be cosmetic and unsafe.

Boundaries:
- synthetic data only;
- human review remains required;
- no production-readiness claim from corpus or benchmark results;
- no silent profile switching;
- no cloud document processing;
- no export, Scrub Key or reinsert semantic change in the foundation package.

## 2026-08-03 — D038 — Use AI-first execution with human-controlled signing, security and release gates for Phase 9 desktop packaging

Status: accepted roadmap and execution-model decision; implementation remains gated

Decision:

```text
When the final local desktop/offline installer phase is explicitly opened, use scoped AI agents for deterministic packaging, CI, synthetic testing and release-candidate preparation. Target a signed Tauri Windows shell with a bundled PyInstaller onedir Python/Presidio sidecar, a low-friction setup.exe and a managed-deployment MSI. Retain human control over publisher identity, production signing, public release, security claims, real-user acceptance and safety-critical semantic changes.
```

Planning assumptions:
- 60–70% of first-cycle development/integration labor may be agent-executed;
- 75–90% of repetitive later release work may be automated;
- post-agent development/integration planning range: approximately EUR 8,000–24,000;
- independent security review, test hardware, signing and human release oversight remain retained costs.

Boundaries:
- Phase 9 remains gated by Phase 6 quality closeout and explicit coordinator approval.
- No installer, runtime, UI, dependency, export, Scrub Key, reinsert or cloud behavior changes in this decision package.
- Synthetic data only.
- No single agent receives unrestricted repository-write, signing-identity and public-release authority.
- Successful packaging alone does not justify a production-readiness or local-only security claim.

## 2026-07-28 — D037 — Validate document/key binding before every reinsert replacement

Status: accepted reinsert-integration decision

Decision:

```text
Validate the complete supported text surface against the supplied Scrub Key before any original value is restored. Permit verified bound matches and explicit legacy-v1.0 compatibility only. All mismatch, mixed-binding, missing-binding, invalid-digest and invalid-bound-key states fail closed with zero replacements and no partial DOCX output.
```

Reason:

- Structural key validity alone cannot prove that a key belongs to a document.
- Applying a wrong but valid key can silently restore incorrect confidential values.
- Validation must happen before mutation so document-level helpers cannot produce partial output.
- Legacy compatibility remains necessary, but it must never be presented as a verified document match.
- The document-first three-step UX remains simpler and does not require new execution gates.

---

## 2026-07-27 — D036 — Preserve custom replacement text and fail verified key export rather than silently rewriting it

Status: accepted export-integration decision

Decision:

```text
Generate document-bound placeholders by default. Rebind only recognised placeholder tokens. Never silently replace arbitrary user-chosen replacement text with a placeholder. When any included mapping remains unbound, keep the document export behavior but block schema-1.1 Scrub Key download with a visible validation warning.
```

Reason:

- Review choices remain source of truth.
- Silent rewriting would change legal/readability semantics and user intent.
- A bound key must not claim verified document matching for an unbound mapping.
- Fail-visible key export is safer than a false binding claim.

---

# SolidPrivacy Scrub — Decision Log

This file records accepted strategic, product and architecture decisions.

---

## 2026-07-27 — D035 — Keep binding-model implementation pure until sequential export and reinsert integration

Status: accepted implementation decision

Decision:

```text
Implement document/Scrub-Key binding as a new pure helper module first. Do not alter current placeholder creation, Scrub Key export/import, deterministic replacement or Streamlit behavior in the model package. Export integration creates bound artifacts in the next package; reinsert integration enforces binding only after bound export is proven.
```

Reason:

- Placeholder generation, key export and reinsert are shared safety-critical surfaces.
- Pure helpers can be validated completely against the frozen contract without silently changing current output semantics.
- Sequential integration preserves explicit migration and rollback boundaries.

Implemented model boundaries:

- local random/injected binding-ID generation;
- strict bound placeholder build/parse and document-ID extraction;
- canonical SHA-256 mapping digest;
- bound key validation;
- eight stable document/key statuses and six fail-closed statuses;
- explicit legacy-v1.0 unbound compatibility;
- no UI, export or reinsert integration;
- no cloud, AI, file persistence, signing or secret storage.

Evidence:

- `scrub_key_binding.py`
- `tests/test_scrub_key_binding_model.py`
- `output/validation/mvp_scrub_key_binding_model_validation.json`

---

## 2026-07-27 — D034 — Freeze the bound-placeholder and mapping-digest contract before model implementation

Status: accepted test/specification decision; model implementation may proceed

Decision:

```text
Freeze binding IDs as B plus sixteen uppercase RFC 4648 base32 characters, automatic placeholders as [LABEL_BINDINGID_INDEX], manual placeholders as [LABEL_BINDINGID_HANDMATIG_INDEX], and the bound-key direction as schema version 1.1 with binding version 1 and a canonical SHA-256 mapping digest. Preserve explicit legacy-v1.0 unbound compatibility and require all bound mismatch, mixed-ID, missing-binding, invalid-digest and invalid-bound-key states to fail closed before replacement.
```

Reason:

- Exact grammar and canonicalization are required before multiple shared placeholder, export and reinsert surfaces change.
- A fixed synthetic digest fixture makes implementation independently testable.
- Bound and legacy statuses must not be conflated.
- UI simplification must survive the security change without new source/key execution gates.

Boundaries:

- Contract/tests only in this package; no product behavior change.
- Mapping digest is not authenticity or a signature.
- No automatic placeholder repair or legacy upgrade.
- Preserve the three-step document-first reinsert flow and final confidential-download acknowledgement.
- Model implementation remains pure and Streamlit-free.
- Export and reinsert integration require later sequential packages.
- Human review remains mandatory; no production-readiness claim.

Evidence:

- `SCRUB_KEY_BINDING_CONTRACT.md`
- `test_cases/mvp_phase6/scrub_key_binding_contract.json`
- `tests/test_mvp_scrub_key_binding_contracts.py`
- `output/validation/mvp_scrub_key_binding_contract_validation.json`

---

## 2026-07-27 — D033 — Bind new Scrub Keys through document-specific placeholder namespaces

Status: accepted planning/architecture decision; implementation requires green contract tests

Decision:

```text
For new bound Scrub Keys, carry one locally generated, non-sensitive document binding ID in every automatic and manual placeholder and in the corresponding Scrub Key. Complement this with a canonical SHA-256 mapping digest for accidental key-corruption detection. Reinsert must fail closed before any replacement when a bound key mismatches the document, the document contains mixed binding IDs, or the mapping digest is invalid.
```

Reason:

- Generic placeholder namespaces allow a wrong valid key to restore wrong originals without an audit mismatch.
- A binding token inside placeholders survives pasted-text, TXT, DOCX and PDF-text roundtrips when the placeholders themselves survive.
- Labels, filenames, metadata, content hashes and placeholder-list hashes are not reliable cross-format AI-roundtrip bindings.
- A digest detects accidental edits but is not authenticity; malicious tampering requires later protected signing-key infrastructure.

Compatibility and UX boundaries:

- Introduce an explicit new bound-key contract; do not silently reinterpret legacy v1.0 keys.
- Legacy unbound keys may remain dual-readable with a visible unbound warning.
- Preserve the document-first three-step reinsert flow and the final confidential-download acknowledgement.
- Add no repeated confirmation buttons or checkboxes.
- Preserve unknown, duplicate and missing-placeholder audit reporting.
- No cloud processing, server secret, OCR or restored-PDF behavior.
- Human review remains mandatory; no production-readiness claim.

Approved sequence:

1. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS`
2. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION`
3. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION`
4. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION`
5. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`

Evidence:

- `MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE.md`
- `output/validation/mvp_scrub_key_document_binding_gap_triage.json`
- `output/validation/mvp_scrub_key_roundtrip_validation_report.json`

---

## 2026-07-27 — D032 — Roundtrip evidence requires document/key-binding triage before implementation

Status: accepted evidence-routing decision

Decision:

```text
Treat the missing document/Scrub-Key binding as a critical Phase 6 finding. Do not implement an implicit heuristic or silently change the Scrub Key schema, export or reinsert semantics inside the validation package. Open a separate triage package to define the binding contract and migration boundaries first.
```

Reason:

- A wrong key with a disjoint placeholder namespace is visibly rejected through unknown/not-found audit evidence.
- A structurally valid wrong or tampered key with the same placeholder names restores wrong original values with no validation issue, unknown placeholder or missing-placeholder signal.
- Document labels are descriptive metadata and are not currently a verified binding mechanism.
- A safe correction may affect key creation, scrubbed output metadata, import compatibility and export semantics.

Boundaries:

- Preserve current deterministic local behavior until the triage decision is approved.
- Do not guess whether a key belongs to a document.
- Do not auto-repair malformed placeholders.
- Preserve existing audit evidence and human review.
- Use synthetic data only; no production-readiness claim.

Evidence:

- `output/validation/mvp_scrub_key_roundtrip_validation_report.json`
- `test_cases/mvp_phase6/scrub_key_roundtrip_manifest.json`
- `tests/test_mvp_scrub_key_roundtrip_validation.py`

---

## 2026-07-27 — D031 — Reinsert is document-first with automatic source/key processing

Status: accepted evidence-driven UX and safety decision

Decision:

```text
Present local reinsert as source document/text → corresponding Scrub Key → restored download. Automatically recognise the source type, structurally validate the supplied Scrub Key and run deterministic local reinsert when both inputs are valid. Keep one explicit confidentiality acknowledgement at the restored-output download boundary instead of repeating acknowledgements and action buttons before processing.
```

Reason:

- Live Phase 6 verification confirmed that DOCX restoration works, but users can reasonably interpret an uploaded and visibly listed file as already accepted.
- Requiring a checkbox and action button after each upload creates hidden completion states and unnecessary form friction.
- The highest-risk user action is obtaining and handling the restored confidential output, so the explicit acknowledgement remains at that boundary.
- Automatic key validation does not weaken structural validation or change Scrub Key semantics.

Boundaries:

- Keep warnings about pseudonymisation, key sensitivity and local-only use visible.
- Invalid or ambiguous keys must still fail clearly and must not be used.
- Preserve result/audit warnings for unknown, duplicate and missing placeholders.
- Preserve existing helpers, output bytes, filenames and MIME types.
- Do not add cloud, AI, OCR, restored-PDF or key-storage behavior.
- Human review remains required and no production-readiness claim is created.

Evidence:

- User-confirmed restored synthetic DOCX containing body, table, header and footer values.
- `tests/test_reinsert_auto_flow.py`
- `tests/test_reinsert_auto_flow_ui.py`
- `output/validation/mvp_reinsert_auto_flow_validation.json`

---

## 2026-07-17 — D030 — Restore existing DOCX header and footer text during deterministic reinsert

Status: accepted implementation decision

Decision:

```text
Extend the existing local deterministic DOCX reinsert helper to process WordprocessingML text nodes in word/header*.xml and word/footer*.xml in addition to word/document.xml.
```

Reason:

- The scrubbed DOCX export already replaces reviewed values in body, table, header and footer paragraphs.
- The Phase 6 matrix showed that reinsert restored body/table values but left header/footer placeholders behind.
- The gap belongs to document fidelity and reinsert scope, not detection or recognizer behavior.

Boundaries:

- Process only existing body, header and footer WordprocessingML text nodes.
- Preserve unrelated OOXML package parts byte-for-byte where they are not rewritten.
- Do not claim support for comments, tracked-change-only parts, footnotes/endnotes, text boxes, metadata or placeholders split across text nodes.
- Do not add OCR or restored-PDF behavior.
- Keep processing local, deterministic and Scrub Key driven.

Evidence:

- `output/validation/mvp_phase6_document_hygiene_fidelity_hardening_report.json`
- `output/validation/mvp_phase6_false_negative_gap_triage.json`

---

## 2026-07-17 — D029 — Current Phase 6 matrix does not justify a recognizer fix

Status: accepted evidence-routing decision

Decision:

```text
Do not open a recognizer or threshold implementation package from the first corrected Phase 6 synthetic matrix.
```

Reason:

- The corrected matrix contains no reproducible detection false negative, misclassification or legal-role over-masking evidence.
- The DOCX result concerns header/footer reinsert fidelity and helper scope.
- The PDF result reflects the approved restored-TXT-only/no-OCR product boundary.
- Treating either item as a recognizer problem would target the wrong layer and weaken evidence discipline.

Consequences:

- Route both findings to `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.
- Preserve current recognizer and threshold behavior.
- Keep the PDF limitation explicit; do not infer OCR or restored-PDF authorization.
- Preserve human review and the no-production-readiness-claim boundary.

Evidence:

- `output/validation/mvp_phase6_false_negative_gap_triage.json`
- `output/validation/mvp_phase6_synthetic_validation_report.json`

---

## 2026-07-17 — D028 — Phase 6 workflow validation becomes the active development line

Status: accepted product-direction decision

Decision:

```text
Close the verified MVP UI simplification line as the default development focus and activate Phase 6 end-to-end workflow validation and trust hardening.
```

Reason:

```text
The current import, review, manual correction and export interface has been live-app verified and works as expected. The next material risk reduction comes from proving the supported workflow with synthetic evidence, then fixing only reproducible trust gaps.
```

Consequences:

- Start with `SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX`.
- Open recognizer, document-hygiene, Scrub Key/roundtrip or audit fixes only from reproducible evidence.
- Do not start another broad UI package by default.
- Phase 7 pilots remain parked until the Phase 6 quality gate is explicitly approved.
- Local installer/packaging work remains deferred.
- Human review remains mandatory; no production-readiness claim is created by this decision.

---

## 2026-07-03 — D027 — Basiscontrole / Expertcontrole as review-mode direction

Status: accepted planning recommendation, implementation pending contract tests

Decision:

```text
Use Basiscontrole / Expertcontrole as the planning names for the two normal review-mode layers.
Basiscontrole is the default MVP path.
Expertcontrole exposes the full inspection/audit machinery.
Mode switching changes visibility only, not processing or export semantics.
```

Reason:

```text
The MVP interface needs a true less-is-more default path without weakening legal/privacy review controls. Basiscontrole communicates lower cognitive load while keeping the workflow framed as a serious control task.
```

Boundaries:

- Basiscontrole is not weaker review.
- The review table remains source of truth internally.
- Mode switching must not change recognizer behavior, replacement logic, export output, Scrub Key JSON, reinsert behavior or audit generation.
- Implementation requires contract tests first.

---

## 2026-06-18 — D026 — Temporarily prioritize MVP UI cleanup and export/download redesign

Status: accepted product-direction decision

Decision:

```text
Pause new recall/benchmark follow-up packages temporarily and prioritize MVP UI cleanup/export redesign.
```

Reason:

```text
The app must move from a prototype/debug interface toward a professional MVP workflow.
```

Consequence:

```text
Next packages focus on export/download UX and hiding/collapsing debug details without weakening safety controls.
```

Implications:

- Recall/benchmark follow-up packages are parked unless a concrete blocker appears.
- Export/download UX is now the active next user-visible improvement line.
- Technical/audit details must remain available but move out of the primary flow where appropriate.
- Scrub Key must stay clearly separated and visibly sensitive.
- Export semantics must not change silently.
- The review table remains source of truth and fallback.
- No Streamlit implementation is approved by this planning decision; implementation requires separate workpackages.

---

## 2026-06-18 — D025 — PERSON-name implementation requires green contract tests first

Status: accepted tests/specification decision

Decision:

```text
PERSON-name recognizer implementation may only start after contract tests are green.
```

Reason:

```text
Value-only matching and role preservation are safety-critical.
```

Consequence:

```text
Implementation package must satisfy the contract fixture before benchmark review.
```

---

## 2026-06-18 — D024 — PERSON-name improvement proceeds test-first

Status: accepted planning/specification decision

Decision:

```text
PERSON-name improvement will proceed test-first.
```

Reason:

```text
Single-surname and role/context cases are high-risk for over-masking and legal/care meaning damage.
```

Consequence:

```text
Contract tests are required before recognizer implementation.
```

---

## 2026-06-15 — D023 — Synchronized scrolling is default review behavior, not a user-facing technical control

Status: accepted bounded UX refinement decision

Decision:

```text
In the central side-by-side review surface, synchronized scrolling should be on by default and should not be exposed as a visible checkbox.
```

Boundary:

This decision does not change replacement behavior, export/download behavior, Scrub Key behavior or reinsert behavior.

---

## 2026-06-15 — D022 — Bounded synchronized side-by-side scrolling approved after prototype review

Status: accepted bounded UX implementation decision; refined by D023 for visible control behavior

Decision:

```text
After visual review of the isolated synchronized-scroll prototype, bounded synchronized scrolling may be integrated into the existing side-by-side review surface.
```

Implementation boundaries:

- Keep synchronized scrolling bounded to the side-by-side review surface.
- Do not change replacement behavior.
- Do not mutate review table state.
- Do not write or change Scrub Key data.
- Do not change export/download behavior.
- Do not change reinsert behavior.
- Do not use real data.

---

## 2026-06-14 — D021 — Unified side-by-side review surface is the target review UX

Status: accepted product/UX direction

Decision:

```text
The review UX should move toward one unified side-by-side main review surface: source text on the left, processed/checked text on the right, with optional highlights integrated in the processed-text pane. The product should not keep adding separate helper panels or duplicate preview expanders for every review feature.
```

Implications:

- Future review UX work should centralize around source-vs-processed comparison.
- The review table remains source of truth and fallback.
- Serial review remains a guided review layer, not a replacement of the table.
- The old replacement decision helper panel must not return as normal user-facing UI.
- Do not start panel removal, click-to-mark, advanced editor, full-document marking, Scrub Key writes, export blocking or reinsert behavior changes without separate approved packages.

---

## Historical note

Older decisions remain available in Git history.
