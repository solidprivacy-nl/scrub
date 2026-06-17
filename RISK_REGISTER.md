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
- Dutch legal recall gap tests and pattern-fix verification are present.
- Synthetic gold-label corpus exists and has been expanded.
- Minimal diagnostic recall benchmark runner exists.
- Diagnostic report artifact workflow exists.
- First and cleaned artifact reviews exist.
- Planning-only threshold policy exists.
- PERSON-name coverage review now classifies the 14 remaining missed `PERSON` labels.

Gaps:

- No accepted production recall/precision threshold exists.
- No production benchmark gate exists.
- No production safety claim is supported.
- Threshold planning exists, but risk remains open.
- PERSON-name false-negative risk is analyzed but not fixed.
- No recognizer change was made.
- No candidate scanner change was made.
- Risk remains open until tests and implementation follow separately.
- Remaining non-PERSON gaps include care room/location references, one client-number example and one nested false-positive hit inside a phone-like value.
- Corpus is synthetic and small.

Recommended workpackages:

- Next approved package — `WP_RECALL_PERSON_NAME_COVERAGE_TESTS`.
- Alternative if design should come first — `WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN`.
- Other approved packages — `WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN`, `WP_CLIENT_REFERENCE_COVERAGE_REVIEW`, `WP_RECALL_BENCHMARK_THRESHOLDS_CONTRACT_TESTS`.

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
- Scrub Key warning/acknowledgement UI is closed out after Actions/HF/app verification.

Gaps:

- UI acknowledgements are safety prompts only; they are not encryption, protected storage, automatic deletion or a managed key vault.
- No approved key recovery model.

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
- Placeholder robustness review, future robust format proposal, validation helper, audit helper and synthetic AI-output corruption tests exist.

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
- PERSON-name coverage review exists.

Gaps:

- Connector workflow-run lookup can still be incomplete for some push-triggered runs.
- No generalized automated status artifact exists yet.

Recommended workpackages:

- Next approved benchmark package — `WP_RECALL_PERSON_NAME_COVERAGE_TESTS` or `WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN`.
- Later status package — automated status artifact/check if connector limitations continue to slow closeouts.

---

## R9 — Dutch legal reference under-detection and role over-masking

Status: mitigating  
Impact: high

Risk:

```text
Dutch legal matter references can be missed or misclassified, while generic legal/care role words can be masked in ways that damage meaning.
```

Current mitigations:

- Human review table remains source of truth and fallback.
- Recall benchmark spec defines reference classes, context terms to preserve and over-masking traps.
- Diagnostic runner/report artifacts make benchmark evidence visible.
- Cleaned artifact has `preserve_term_hit_count = 0`.
- Planning-only threshold policy exists.
- PERSON-name coverage review classifies role-linked missed names, including care-role and legal-role examples.

Gaps:

- No accepted production threshold exists.
- No benchmark gate exists.
- Corpus is synthetic and not exhaustive.
- PERSON-name false-negative risk is analyzed but not fixed.
- Names after care/legal roles need tests before recognizer changes.
- Single-surname examples remain high ambiguity.
- Product claim remains blocked.

Recommended workpackages:

- `WP_RECALL_PERSON_NAME_COVERAGE_TESTS`.
- `WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN`.
- `WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS`.
- `WP_CARE_LOCATION_REFERENCE_CANDIDATE_PLAN`.
- `WP_CLIENT_REFERENCE_COVERAGE_REVIEW`.

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
De diagnostische benchmark laat zien welke synthetische persoonsnamen nog gemist worden.
Deze analyse helpt vervolgtests en herkenningslogica te plannen.
Menselijke review blijft noodzakelijk.
```
