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

Current mitigations include human review, review guidance, diagnostic recall benchmark artifacts, PERSON-name diagnostic/contract/helper work, planning-only threshold policy and a verified simple manual missed-value entry that adds user-supplied values to the existing replacement table. Phase 6 now starts with a synthetic end-to-end validation matrix so new fixes are driven by reproducible false-negative, misclassification and over-masking evidence. The first machine-readable matrix baseline is stored in `output/validation/mvp_phase6_synthetic_validation_report.json` with 3 synthetic cases and 2 recorded evidence gaps or known limitations.

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

Current mitigations include warnings and acknowledgements. Export/download UX grouping is now implemented directly in `presidio_streamlit.py` so the key file is visually separated from normal document exports and shown with a specific warning. Live app verification confirmed the grouped export UI.

The manual missed-value entry flows through the existing replacement table and existing Scrub Key/export paths without changing key semantics.

---

## R3 — Placeholder corruption during AI roundtrip

Status: mitigating  
Impact: high

Risk:

```text
An AI system rewrites, translates, merges or deletes placeholders, causing deterministic reinsert to fail or restore incompletely.
```

Current mitigations include placeholder robustness helper/test work and reinsert audit reporting.

---

## R4 — Hidden document content and metadata leakage

Status: mitigating  
Impact: high

Risk:

```text
DOCX metadata, comments, tracked changes, headers, footers or hidden content contain sensitive data that is not scrubbed or cleaned.
```

DOCX hygiene audit remains report-only. Export grouping keeps audit details available and does not imply a clean-DOCX guarantee. The review debug collapse line explicitly keeps audit details available rather than removing them. The Phase 6 synthetic DOCX case now records header/footer findings and the existing main-document-only reinsert boundary as reproducible evidence for the document-hygiene hardening package.

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

Gaps:

- Additional copy polish may still be needed, but it should remain separate and small.
- Implementation must avoid weakening review controls or hiding audit details.

Recommended workpackages:

- The current UI baseline is completed and app-verified. Do not start another UI feature automatically; open a narrowly scoped UI package only when Phase 6 validation exposes a concrete safety or workflow blocker.

---

## R7 — PDF limitations misunderstood by users

Status: mitigating  
Impact: high

Risk:

```text
Users may assume PDF support means complete restored PDF reinsert or OCR, while the approved scope is text-based extraction to restored TXT only.
```

PDF limitations must remain clear in export/reinsert copy. The Phase 6 text-based PDF case verifies the current restored-TXT-only path and explicitly records that restored PDF and OCR are unsupported.

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

Current mitigations include diagnostic benchmark work, preservation guidance, PERSON-name contract/helper work and a verified manual missed-value entry path. The Phase 6 synthetic matrix is now the evidence source for `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE`; only reproducible under-detection, misclassification or role-over-masking findings may open a subsequent fix package.

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
