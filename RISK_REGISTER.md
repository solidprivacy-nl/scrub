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

Current mitigations include human review, review guidance, diagnostic recall benchmark artifacts, PERSON-name diagnostic/contract/helper work, planning-only threshold policy and a verified simple manual missed-value entry that adds user-supplied values to the existing replacement table.

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

DOCX hygiene audit remains report-only. Export grouping keeps audit details available and does not imply a clean-DOCX guarantee. The review debug collapse line explicitly keeps audit details available rather than removing them.

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

- Do not start a new feature automatically; consider `WP_MVP_UI_APP_VERIFICATION_CLOSEOUT` or a very small UI simplification package only with coordinator approval.

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
- Export/download UX now groups document downloads, key file, and audit/technical files while keeping audit details available.
- The step-by-step review aid is now secondary by default, while review table and audit controls remain available.
- The verified manual missed-value entry is intentionally placed in the primary review path because it directly supports faster anonymization.

Gaps:

- No generalized automated status artifact exists yet.

---

## R9 — Dutch legal reference under-detection and role over-masking

Status: mitigating  
Impact: high

Risk:

```text
Dutch legal matter references can be missed or misclassified, while generic legal/care role words can be masked in ways that damage meaning.
```

Current mitigations include diagnostic benchmark work, preservation guidance, PERSON-name contract/helper work and a verified manual missed-value entry path. Benchmark follow-up is temporarily parked for UI/export work unless a concrete blocker appears.

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
