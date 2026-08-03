# SolidPrivacy Scrub — Risk Register

This register tracks product, privacy, security and trust risks.

Status values: `open`, `mitigating`, `accepted`, `closed`.

Impact values: `critical`, `high`, `medium`, `low`.

---

## R1 — False negatives / missed sensitive data

Status: mitigating  
Impact: critical

Risk:

```text
Sensitive data remains in the scrubbed output and the user wrongly trusts the result.
```

Current mitigations include human review, review guidance, diagnostic recall benchmark artifacts, PERSON-name diagnostic/contract/helper work, planning-only threshold policy and a verified simple manual missed-value entry that adds user-supplied values to the existing replacement table. A selection-driven processed-text correction path is approved with an all-exact version-one boundary. Its frozen contract and pure action model require a two-stage server-authoritative inspect/commit protocol and may not bypass validation or the authoritative replacement table. The model now proves UTF-16 selection validation, exact impact bands, Unicode collision blocking, stale/replay rejection, bound manual-row construction and fail-closed undo without connecting to the UI. Phase 6 now starts with a synthetic end-to-end validation matrix so new fixes are driven by reproducible false-negative, misclassification and over-masking evidence. The first machine-readable matrix baseline is stored in `output/validation/mvp_phase6_synthetic_validation_report.json` with 3 synthetic cases and 2 recorded evidence gaps or known limitations. Triage confirms that neither remaining item is a detection false negative, so no recognizer fix is justified by this bounded baseline.

Remaining gaps:

- No accepted production recall/precision threshold exists.
- No production benchmark gate exists.
- No production safety claim is supported.
- Human review remains necessary.

---

## R2 — Scrub Key leakage or accidental sharing

Status: mitigating  
Impact: critical

Risk:

```text
The Scrub Key is shared, leaked, retained too long, tampered with or mishandled, allowing full re-identification of scrubbed content.
```

Current mitigations include warnings and acknowledgements. Export/download UX grouping is implemented directly in `presidio_streamlit.py` so the key file is visually separated from normal document exports and shown with a specific warning. Live app verification confirmed the grouped export UI. Reinsert now keeps the key-sensitivity warning visible, automatically applies the existing structural validation to a supplied key, and preserves one explicit confidentiality acknowledgement at the restored-output download boundary. Redundant pre-processing acknowledgements are removed because they obscured workflow state without adding key validation.

The manual missed-value entry flows through the existing replacement table and existing Scrub Key/export paths without changing key semantics. No key storage, schema or lifecycle behavior is added by the automatic reinsert flow. The Phase 6 adversarial roundtrip matrix exposes a critical unresolved gap: a structurally valid wrong or tampered key that reuses the same placeholder namespace can restore incorrect original values without a detectable mismatch. This is routed to `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE`; no schema or export change is authorized by the validation package. Triage recommends a non-sensitive document binding ID inside every automatic/manual placeholder and the corresponding key, plus a canonical mapping digest for accidental corruption. Contract tests now freeze legacy v1.0 unbound behavior, a document-specific base32 binding ID, canonical SHA-256 mapping digest and fail-closed mismatch/mixed-ID/digest-error statuses before model implementation. The pure model implements those contracts, and anonymization/export now creates bound placeholders plus schema-1.1 keys when all selected mappings are bound. Arbitrary custom replacement text is preserved but visibly blocks verified key export. Reinsert now validates the complete supported document text surface before replacement. Correct bound matches are verified; wrong, mixed, missing or digest-invalid bindings fail closed with zero replacements, and DOCX failures return the exact original package bytes. Legacy v1.0 compatibility remains explicitly unverified. The accidental pairing/corruption path is technically mitigated but the risk remains open until deployed app verification passes. Signatures/HMAC remain deferred until protected local signing-key management exists.

---

## R3 — Placeholder corruption during AI roundtrip

Status: mitigating  
Impact: high

Risk:

```text
An AI system rewrites, translates, merges or deletes placeholders, causing deterministic reinsert to fail or restore incompletely.
```

Current mitigations include placeholder robustness helper/test work and reinsert audit reporting. The Phase 6 roundtrip matrix validates translated, merged, unknown, repeated and malformed mutations. Unknown grammar-valid placeholders are visible, while malformed tokens outside the strict grammar are signalled indirectly through expected placeholders not found. This diagnostic limitation is included in the document-binding gap triage. It is not part of the critical binding implementation line; an optional later diagnostic-hardening package may report malformed near-placeholders directly without guessing or repairing values.

---

## R4 — Hidden document content and metadata leakage

Status: mitigating  
Impact: high

Risk:

```text
DOCX metadata, comments, tracked changes, headers, footers or hidden content contain sensitive data that is not scrubbed or cleaned.
```

DOCX hygiene audit remains report-only. Export grouping keeps audit details available and does not imply a clean-DOCX guarantee. The review debug collapse line explicitly keeps audit details available rather than removing them. The Phase 6 synthetic DOCX case now records header/footer findings and the existing main-document-only reinsert boundary as reproducible evidence for the document-hygiene hardening package. Gap triage classifies this as document fidelity and reinsert scope and routes it to `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`. The hardening package now restores placeholders in existing DOCX header and footer XML parts while retaining hygiene reporting and explicit unsupported-part warnings.

---

## R5 — Cloud-demo trust gap and deferred installer risk

Status: mitigating  
Impact: high

Risk:

```text
The final product promise is local-first, but the current fast validation surface is the Hugging Face cloud demo.
```

Local/offline installer work remains later. The current focus is making the web prototype workflow credible first.

---

## R6 — Review UX and interface clarity risk

Status: mitigating  
Impact: high

Risk:

```text
The interface still feels like a technical prototype, which can reduce confidence and increase review mistakes.
```

Current mitigations:

- Review table remains source of truth and fallback.
- Side-by-side review surface, synced scrolling and collapsible review table are live and verified.
- Export/download UX is directly implemented in `presidio_streamlit.py` and live verified.
- `REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN.md` narrows review UI cleanup to a small interface pass, not a new review loop.
- `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION` made the existing step-by-step review aid collapsed by default and removed debug/governance wording from the primary UI.
- `WP_MVP_FAST_MANUAL_MASK_ENTRY` adds a verified simple user-facing path to add missed values to the existing replacement table.
- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT` freezes the approved route, and `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL` implements its pure server-authoritative validation and row-construction logic; the table remains source of truth and component/UI integration remains sequentially gated.

Gaps:

- Live reinsert verification exposed a concrete workflow-state problem: uploaded source and key files still required non-obvious follow-up checkboxes and buttons. `SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION` addresses this narrowly with document-first ordering and automatic validation/processing.
- Additional copy polish may still be needed, but it should remain separate and small.
- The pure action model now proves exact-occurrence bands, Unicode collision guards, replay/stale-event protection and safe undo. The remaining high-risk gate is a non-mutating component spike proving text-node offsets, accessible menu behavior and replay-safe bidirectional transport before promotion.
- Implementation must avoid weakening review controls or hiding audit details; one final confidentiality acknowledgement remains at download.

Recommended workpackages:

- The general UI baseline is completed and app-verified. The automatic reinsert-flow package is permitted as a narrow exception because live Phase 6 validation exposed a concrete workflow blocker; broader UI work remains gated.

---

## R7 — PDF limitations misunderstood by users

Status: mitigating  
Impact: high

Risk:

```text
Users may assume PDF support means complete restored PDF reinsert or OCR, while the approved scope is text-based extraction to restored TXT only.
```

PDF limitations must remain clear in export/reinsert copy. The Phase 6 text-based PDF case verifies the current restored-TXT-only path and explicitly records that restored PDF and OCR are unsupported. Gap triage retains this as an explicit product boundary and does not authorize OCR or restored-PDF work. Document-fidelity hardening preserves that boundary unchanged.

---

## R8 — Workflow status, audit visibility and evidence clarity

Status: mitigating  
Impact: medium

Risk:

```text
Evidence and audit controls become either too hidden to trust or too technical for normal users.
```

Current mitigations:

- Coordinator screenshots/evidence are recorded when connector lookup is incomplete.
- Diagnostic recall benchmark artifact workflow exists.
- Audit/report details exist.
- `MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md` states that technical/audit details must remain available but become secondary.
- Export/download UX now groups document downloads, key file, and audit/technical files while keeping audit details available.
- The step-by-step review aid is now secondary by default, while review table and audit controls remain available.
- The verified manual missed-value entry is intentionally placed in the primary review path because it directly supports faster anonymization.
- The approved selection-driven route may reduce navigation friction, but every accepted action must still become a visible normal replacement-table row and must not mutate export or Scrub Key state directly from the browser component.

Gaps:

- No generalized automated status artifact exists yet. `SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE` is scheduled after the synthetic validation, gap-triage and roundtrip packages.

---

## R9 — Dutch legal reference under-detection and role over-masking

Status: mitigating  
Impact: high

Risk:

```text
Dutch legal matter references can be missed or misclassified, while generic legal/care role words can be masked in ways that damage meaning.
```

Current mitigations include diagnostic benchmark work, preservation guidance, PERSON-name contract/helper work and a verified manual missed-value entry path. The Phase 6 synthetic matrix is now the evidence source for `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE`; only reproducible under-detection, misclassification or role-over-masking findings may open a subsequent fix package. The first triage found none of those categories; recognizer behavior remains unchanged.

---

## R10 — Care-profile under-detection and clinical over-masking

Status: mitigating  
Impact: critical

Risk:

```text
A care document retains patient or trajectory identifiers, or Scrub removes diagnosis, medication, laboratory values, observations or care context and makes the document misleading or unusable.
```

Mitigation direction:

- explicit Zorgfilter v1 policy contract;
- fully synthetic corpus across eight care-document families;
- exact replace, review and preserve expectations;
- current-engine baseline before recognizer changes;
- separate care taxonomy and recognizers;
- negative tests for medical numbers, dosages, times, vital signs and laboratory values;
- cross-profile regression before UI promotion;
- human review and residual-risk evidence remain mandatory.

Approved policy boundary:

```text
Patient identity and date of birth: replace.
Other exact care dates and provider identity: review, selected by default.
Clinical meaning: preserve.
Rare-case indirect identification: audit warning, not blind masking.
```

The current broad `NL_HEALTHCARE_REFERENCE` category is insufficient because it combines patient numbers, referral references, insurance identifiers and DBC/clinical codes under one behavior.

Current bounded baseline evidence:

- 25/81 expected replace/review values were found as exact spans;
- 14/81 were found under the intended entity type;
- 11 were misclassified and 56 missed;
- only 4/42 review-selected values were found;
- one AGB value collided with BSN recognition;
- no designated clinical preserve phrase was overlapped by the current custom rules.

Generic NER was excluded, so the PERSON and e-mail findings do not represent complete live-app behavior. This evidence increases confidence that dedicated care patterns and review policy are necessary, but does not establish production quality.

Gap triage classified all 81 expectations. The largest unresolved family is contextual review recognition (36 values), followed by generic profile dependencies (13), care-specific reclassification (10), dedicated care references (5) and AGB/numeric collision guards (3). The recognizer contract package must freeze these routes before any care pattern implementation.

The recognizer contract is now frozen with sixteen dedicated entities, 37 positive exact-span cases and 16 negative/collision/preservation cases. Implementation must pass these fixtures before any app registration or UI promotion.

The pure recognizer implementation now passes all frozen fixtures and all 54 dedicated corpus expectations with zero protected-clinical overlaps. Risk R10 remains open because generic NER composition, AGB/BSN cross-recognizer precedence, visible profile policy, cross-profile regression and live app verification are not yet complete.

The central profile model now freezes Care composition and exact-span precedence without changing the live application. Risk R10 remains open until the current app registers the care recognizers, uses the profile policy, runs cross-profile regression and passes deployed app verification.

The current Streamlit integration registers the sixteen care recognizers and applies the central profile policy. Review-selected care detections are selected by default but visibly marked `Controle nodig`; unresolved strongly labelled references remain unchecked candidates. Cross-profile regression, byte-for-byte deployment verification and live app verification are green, including confirmation that clinical meaning remains readable and existing review, export, Scrub Key and reinsert flows remain present. Risk R10 remains mitigating because synthetic and bounded app evidence does not establish production recall, precision or rare-case safety; human review remains mandatory.

The deterministic cross-profile matrix now passes all hard gates: 108/108 dedicated Care expectations are retained across Care and International, no dedicated Care or Legal entities leak into the wrong profiles, dedicated-type parity holds, and no protected clinical phrase is overlapped. Historical legal metadata remains explicitly recorded as 132/148 deterministic expectations, sixteen gaps and four negative observations. Risk R10 remains mitigating because GitHub-to-Hugging-Face deployment sync, generic-NER behavior and live app verification are still unconfirmed.

Deployment sync is now independently verified: twelve relevant GitHub/Hugging Face files match byte-for-byte, all correctly scoped markers pass and the Space is healthy. Risk R10 remains mitigating only for the remaining human-visible app verification, generic-NER observation and the broader limitation that synthetic evidence does not prove production recall or precision.

The tester-facing care corpus now uses long-form structured variants across all eight approved document families. Each addition supplies substantial clinical and workflow context without adding new names, identifiers, dates, addresses, contact details, organizations, locations or digits. This improves usability and preservation testing but does not change recognizer behavior or establish production recall, precision or rare-case safety.

---

## Product-claim boundary

Disallowed claims:

```text
Alle persoonsnamen worden altijd gevonden.
Alle persoonsgegevens worden altijd gevonden.
Alle juridische nummers worden altijd herkend.
De app is veilig voor productie zonder menselijke review.
De benchmark bewijst production readiness.
```

Allowed wording:

```text
Scrub helpt gevonden gegevens te controleren en exporteren, maar menselijke review blijft noodzakelijk.
Technische en auditdetails blijven beschikbaar voor controle.
```
