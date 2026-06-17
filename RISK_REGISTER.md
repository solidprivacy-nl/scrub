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

Current mitigations:

- Human review workflow.
- Review guidance and final review summary.
- WP19-WP24 created the recall/trust benchmark and report-only residual-risk foundation.
- Dutch legal recall gap tests and pattern-fix verification are present.
- Synthetic gold-label corpus exists and has been expanded.
- Minimal diagnostic recall benchmark runner exists.
- Diagnostic report artifact workflow exists.
- First artifact review found mapping/counting noise.
- Artifact cleanup reduced that noise.
- Cleaned artifact review confirmed the output is substantially less noisy: missed required 34 -> 18, wrong-type 11 -> 1 and false-positive candidates 8 -> 1.
- `RECALL_BENCHMARK_THRESHOLDS_PLAN.md` now exists as a planning-only threshold policy document.

Gaps:

- No accepted production recall/precision threshold exists.
- No production benchmark gate exists.
- No production safety claim is supported.
- Threshold planning exists, but risk remains open.
- Cleaned artifact review still shows 18 missed required labels, concentrated in person names, care room/location references and one client-number example.
- One nested false-positive candidate remains inside a phone-like value.
- Corpus is synthetic and small.

Recommended workpackages:

- Next approved package — `WP_RECALL_PERSON_NAME_COVERAGE_REVIEW`.
- Alternative approved packages — `WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN`, `WP_CLIENT_REFERENCE_COVERAGE_REVIEW`, `WP_RECALL_BENCHMARK_THRESHOLDS_CONTRACT_TESTS`.
- Later planning package — `WP_RECALL_BENCHMARK_GATE_PLAN`; still planning only, not implementation.

---

## R2 — Scrub Key leakage or accidental sharing

Status: mitigating  
Impact: critical

Risk:

```text
The Scrub Key is shared, leaked, retained too long, tampered with or mishandled, allowing full re-identification of scrubbed content.
```

Current mitigations:

- UI warnings around Scrub Key reinsert.
- Local-only/no-AI/no-cloud positioning for reinsert.
- WP25-WP29C covered threat model, lifecycle specs, warning planning/implementation, import/export tests and warning UI test scaffolding.
- WP28C warning/acknowledgement UI is closed out after Actions/HF/app verification.

Gaps:

- UI acknowledgements are safety prompts only; they are not encryption, protected storage, automatic deletion or a managed key vault.
- No approved key recovery model.

Recommended workpackages:

- Later implementation package — protected local file handling.
- Later implementation package — encrypted key container.
- Later implementation package — local vault / managed key store.

---

## R3 — Placeholder corruption during AI roundtrip

Status: mitigating  
Impact: high

Risk:

```text
An AI system rewrites, translates, merges or deletes placeholders, causing deterministic reinsert to fail or restore incompletely.
```

Current mitigations:

- Unknown placeholders and not-found placeholders are reported in reinsert audit flows.
- WP30-WP34 created placeholder robustness review, future robust format proposal, validation helper, audit helper and synthetic AI-output corruption tests.

Gaps:

- Robust placeholder generation has not been implemented in product flow.
- No migration or backward-compatibility implementation exists yet.
- No Scrub Key schema/version support for robust placeholder metadata exists yet.

---

## R4 — Hidden document content and metadata leakage

Status: mitigating  
Impact: high

Risk:

```text
DOCX metadata, comments, tracked changes, headers, footers or hidden content contain sensitive data that is not scrubbed or cleaned.
```

Current mitigations:

- DOCX hidden-content risk review, visibility helpers and report-only hygiene audit are present.
- Clean DOCX export policy exists.
- DOCX hygiene audit UI is report-only and does not claim clean DOCX output.

Gaps:

- Word comments / kantlijncommentaren are still not scrubbed or removed by the current DOCX scrub/reinsert flow.
- No clean DOCX export implementation exists.
- No approved export-blocking implementation exists for high-risk hidden content.

---

## R5 — Cloud-demo trust gap and deferred installer risk

Status: mitigating  
Impact: high

Risk:

```text
The final product promise is local-first, but the current fast validation surface is the Hugging Face cloud demo.
```

Current mitigations:

- Roadmap includes local desktop/offline direction.
- UI messaging emphasizes local/no-AI/no-cloud where applicable.
- Local runtime/packaging decision line is completed through packaging deferral.

Gaps:

- No full offline demonstration.
- No production security certification is supported.
- No signed or managed enterprise deployment proof exists.

---

## R6 — Review UX and replace-flow ceiling

Status: mitigating  
Impact: medium

Risk:

```text
The review interface may not support the document-centric review experience needed for high-trust legal/care workflows.
```

Current mitigations:

- Review table remains source of truth and fallback.
- Side-by-side review surface, synced scrolling and collapsible review table are live and verified.
- Serial review remains available as a non-destructive review aid.

Gaps:

- The review table remains the source of truth and fallback.
- Percentage-based synchronized scrolling can be imperfect when source and processed text differ structurally.
- No professional document editor exists.

---

## R7 — PDF limitations misunderstood by users

Status: mitigating  
Impact: high

Risk:

```text
Users may assume PDF support means complete restored PDF reinsert or OCR, while the approved scope is text-based extraction to restored TXT only.
```

Boundaries:

- No restored PDF output.
- No OCR.
- No PDF-to-DOCX reconstruction.
- No layout preservation promises.

---

## R8 — Workflow status and benchmark evidence visibility

Status: mitigating  
Impact: medium

Risk:

```text
Evidence becomes ambiguous because connector status can be incomplete and diagnostic outputs are hard to inspect.
```

Current mitigations:

- Coordinator screenshots/evidence are recorded when connector lookup is incomplete.
- Workpackages record Actions/sync status.
- Diagnostic recall benchmark artifact workflow exists.
- First and cleaned artifact reviews exist.
- Planning-only threshold policy exists.

Gaps:

- Connector workflow-run lookup can still be incomplete for some push-triggered runs.
- No generalized automated status artifact exists yet.
- Future threshold work must remain planning-only until separate gate approval.

Recommended workpackages:

- Next approved benchmark package — `WP_RECALL_PERSON_NAME_COVERAGE_REVIEW` or another focused coverage package.
- Later status package — automated status artifact/check if connector limitations continue to slow closeouts.

---

## R9 — Dutch legal reference under-detection and role over-masking

Status: mitigating  
Impact: high

Risk:

```text
Dutch legal matter references can be missed or misclassified, while generic legal role words can be masked in ways that damage legal meaning.
```

Current mitigations:

- Human review table remains source of truth and fallback.
- Recall benchmark spec defines legal reference classes, context terms to preserve and over-masking traps.
- Dutch legal pattern fixes improve review-candidate visibility.
- Diagnostic runner/report artifacts make benchmark evidence visible.
- Cleaned artifact has `preserve_term_hit_count = 0`.
- Planning-only threshold policy exists.

Gaps:

- No accepted production threshold exists.
- No benchmark gate exists.
- Corpus is synthetic and not exhaustive.
- Remaining misses include 14 person labels, 3 care room/location references and 1 client-number example.
- Product claim remains blocked.

Recommended workpackages:

- `WP_RECALL_PERSON_NAME_COVERAGE_REVIEW`.
- `WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN`.
- `WP_CLIENT_REFERENCE_COVERAGE_REVIEW`.
- `WP_RECALL_BENCHMARK_THRESHOLDS_CONTRACT_TESTS`.

---

## Product-claim boundary

Disallowed claims:

```text
Alle persoonsgegevens worden altijd gevonden.
Alle juridische nummers worden altijd herkend.
De app is veilig voor productie zonder menselijke review.
De benchmark bewijst production readiness.
```

Allowed wording:

```text
De diagnostische benchmark helpt regressies zichtbaar te maken op een synthetische corpus.
De output ondersteunt engineeringbeslissingen, maar vervangt geen menselijke review.
```
