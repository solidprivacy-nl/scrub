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

Current mitigations include human review, review guidance, diagnostic recall benchmark artifacts, PERSON-name diagnostic/contract/helper work and planning-only threshold policy.

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

Current mitigations include warnings and acknowledgements. Export/download UX grouping is now implemented so the Scrub Key is visually separated from normal document exports and shown with a specific warning. Risk remains open until live app verification confirms the final UI.

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

DOCX hygiene audit remains report-only. Export grouping keeps audit details available and does not imply a clean-DOCX guarantee.

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
- Serial review remains available as a non-destructive review aid.
- `MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md` defines a route to move debug/audit details out of the primary flow and improve export/download hierarchy.
- `EXPORT_DOWNLOAD_UX_CONTRACTS.md` and `tests/test_export_download_ux_contracts.py` protect the professional export/download direction before implementation.
- Export/download UX grouping is implemented through `fix_streamlit_export_download_ux.py` and protected by implementation tests.

Gaps:

- Debug-like labels and technical captions still need to be collapsed, renamed or moved.
- Risk remains open until app verification confirms the live grouped export UI.

Recommended workpackages:

- `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN`
- `WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION`
- `WP_REVIEW_COPY_POLISH_IMPLEMENTATION`

---

## R7 — PDF limitations misunderstood by users

Status: mitigating  
Impact: high

Risk:

```text
Users may assume PDF support means complete restored PDF reinsert or OCR, while the approved scope is text-based extraction to restored TXT only.
```

PDF limitations must remain clear in export/reinsert copy.

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
- Export/download UX now groups document downloads, Scrub Key, and audit/technical files while keeping audit details available.

Gaps:

- App verification is still needed for the live grouped export UI.
- No generalized automated status artifact exists yet.

---

## R9 — Dutch legal reference under-detection and role over-masking

Status: mitigating  
Impact: high

Risk:

```text
Dutch legal matter references can be missed or misclassified, while generic legal/care role words can be masked in ways that damage meaning.
```

Current mitigations include diagnostic benchmark work, preservation guidance and PERSON-name contract/helper work. Benchmark follow-up is temporarily parked for UI/export work unless a concrete blocker appears.

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
