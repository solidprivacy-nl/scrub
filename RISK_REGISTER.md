# SolidPrivacy Scrub — Current Risk Register

This register tracks the **current** product, privacy, security, trust and execution risks for SolidPrivacy Scrub.

Detailed pre-convergence risk history remains recoverable from exact baseline:

```text
54c73e0ebf5a3a3ed7039a50596fb57694add3cd
```

Git/CHANGELOG preserve execution history. This file represents the live risk picture rather than workpackage history.

Status values: `open`, `mitigating`, `accepted`, `closed`.  
Impact values: `critical`, `high`, `medium`, `low`.

---

## R1 — False negatives / missed sensitive data

Status: `mitigating`  
Impact: `critical`

Risk:

```text
Sensitive data remains in scrubbed output and the user wrongly trusts the result.
```

Current controls/evidence:

- layered deterministic Dutch recognizers plus generic NER;
- dedicated Legal/Zorg rules and profile policy;
- recognizer-backed synthetic corpus benchmark/reporting;
- domain-specific baseline/gap-triage/cross-profile tests;
- manual missed-value addition and direct processed-text correction;
- mandatory human review;
- residual-risk/known-limitation language.

Current gaps:

- no accepted real-world production recall guarantee exists;
- synthetic corpora do not prove complete production coverage;
- human review remains necessary;
- recognizer changes must remain evidence-driven so precision fixes do not silently reduce recall.

> Do not claim perfect recall or production safety from synthetic benchmark results.

---

## R2 — Scrub Key leakage, mismatch or misuse

Status: `mitigating`  
Impact: `critical`

Risk:

```text
A Scrub Key leaks, is paired with the wrong document, is corrupted/tampered with, or is otherwise mishandled, enabling incorrect or unauthorized re-identification.
```

Current controls/evidence:

- explicit sensitive-key treatment in UI;
- document-bound placeholders and mapping digest;
- structural validation;
- fail-closed wrong/mixed/missing-binding handling;
- controlled TXT/DOCX/PDF-to-TXT reinsert paths;
- adversarial/roundtrip tests;
- legacy unbound state remains explicitly unverified.

Current gaps:

- Scrub Key remains inherently sensitive re-identification material;
- mapping digest is not a cryptographic authenticity/signing claim;
- user/operational handling remains part of the threat model.

---

## R3 — Placeholder corruption during AI/external roundtrip

Status: `mitigating`  
Impact: `high`

Risk:

```text
An external AI/process rewrites, translates, merges, deletes or corrupts placeholders, causing deterministic reinsert to fail or restore incompletely.
```

Controls include stable bound placeholder grammar, document/mapping binding, adversarial mutation tests, unknown/missing diagnostics and fail-visible reinsert. Scrub must not guess original values when binding cannot be proven.

---

## R4 — Hidden document content, metadata and unsupported-part leakage

Status: `mitigating`  
Impact: `high`

Risk:

```text
DOCX metadata, comments, tracked changes, unsupported XML parts, headers/footers or other hidden content retains sensitive information outside the supported scrub/reinsert surface.
```

Current controls include DOCX hygiene/audit reporting, body/table/header/footer support, synthetic fidelity tests, explicit unsupported-part warnings and bounded text-PDF support. Hygiene reporting must not be presented as a complete clean-document guarantee where unsupported content may exist.

---

## R5 — Scrub Private content-retention / external-egress trust boundary

Status: `open`  
Impact: `critical`

Risk:

```text
A managed Private service retains customer document content, mappings or Scrub Keys, logs content, backs it up, or sends document content to a third party contrary to the intended service promise.
```

Current full-feature application evidence:

- `replacement_memory.py` intentionally persists original/replacement/entity values to `/data/replacement_memory.json` when persistent storage exists;
- Expert functionality includes Azure AI Language and OpenAI/Azure synthesis paths;
- synthesis helper currently prints a content-bearing prompt.

These are variant-specific conflicts with Scrub Private, not proof that every current deployment model is defective.

Scrub Private target:

```text
no intentional persistent server-side customer document content
no content-bearing ordinary application logs
no document-content backup
no third-party document-processing egress
minimal non-document control-plane persistence only when required
```

Mitigation sequence: first complete Repository Convergence without destroying potentially useful full-feature behavior; then remove/exclude hosted-incompatible persistence/egress from the Private line; prove application behavior on HF with synthetic data; prove infrastructure/service retention properties later on controlled production infrastructure.

Do not use HF application tests to claim provider-level zero retention.

---

## R6 — Review UX, stale state and workflow clarity

Status: `mitigating`  
Impact: `high`

Risk:

```text
The user misses a sensitive value, changes state without realizing downstream output is stale, or the interface obscures whether review is complete/current.
```

Controls include staged Premium workspace, Standard/Expert over shared authoritative state, generation-bound review/export state, fail-closed stale export, explicit re-completion, source-versus-processed review and direct/manual correction.

Current gap: parent Premium live-verification issues contain stale/unfinished closeout state; deployed behavior must be reconciled against merged marker/address repairs before those historical gates are declared closed.

---

## R7 — PDF limitations misunderstood by users

Status: `mitigating`  
Impact: `high`

Risk:

```text
Users interpret text-based PDF support as OCR or complete restored-PDF fidelity.
```

Boundary: text-based extraction is supported; OCR is not implied; restored PDF generation is not implied; reinsert output may be restored text rather than reconstructed PDF. Copy, audit and pilot guidance must keep these limitations explicit.

---

## R8 — Audit/evidence clarity and false confidence

Status: `mitigating`  
Impact: `high`

Risk:

```text
Multiple benchmark/report generations are mistaken for equivalent safety evidence, or diagnostic metrics are presented as production-readiness/individual-document safety scores.
```

Current convergence requirement:

```text
CANONICAL RELEASE VALIDATION
SUPPLEMENTAL DIAGNOSTIC
HISTORICAL / SUPERSEDED
```

Synthetic/report warnings and mandatory human review remain. Do not create a replacement Evidence Framework or per-document false-precision safety score.

---

## R9 — Dutch Legal recognition precision/recall and context damage

Status: `mitigating`  
Impact: `high`

Risk:

```text
Legal identifiers/addresses/names are missed or misclassified, or ordinary legal/professional context is over-masked and loses meaning.
```

Controls include Dutch deterministic recognizers, Legal profile, synthetic legal corpus, address-span repair, preserve/known-trap evidence, manual/direct correction and human review. Future fixes remain test-first and must preserve recall/context.

---

## R10 — Zorg under-detection and clinical over-masking

Status: `mitigating`  
Impact: `critical`

Risk:

```text
A care document retains patient/trajectory identifiers or Scrub removes clinical meaning and makes the document misleading/unusable.
```

Current controls/evidence:

- explicit Zorg profile/policy;
- synthetic care-document families plus long-form variants;
- baseline/gap triage;
- dedicated care recognizer contracts/implementation;
- collision/negative tests;
- cross-profile regression;
- clinical preserve expectations;
- human review.

Current gap: synthetic and bounded app evidence does not establish complete production recall/precision or rare-case indirect-identification safety.

> Preserve diagnosis, medication, dosage, laboratory values, observations and useful care context unless a specific evidence-backed reason treats a value as identifying.

---

## R11 — Repository/source-of-truth drift

Status: `mitigating`  
Impact: `high`

Risk:

```text
Workers follow stale ROADMAP/WORKPACKAGES/issues or duplicate already-built functionality because repository documentation and actual main no longer describe one coherent current truth.
```

Current mitigation:

- Repository Convergence is active;
- exact pre-convergence SHA is preserved;
- bootstrap PR #114 PASSed/merged with exact-main Tests and HF sync green;
- one current roadmap/workpackage model is in place;
- temporary debt ledger is explicitly non-authoritative after convergence;
- stale issue/evidence hierarchy reconciliation remains required;
- normal feature work remains paused until `SCRUB_REPOSITORY_CONVERGED`.

Exit: one clean exact SHA whose source, tests, active issues and canonical docs materially agree.

---

## R12 — Legacy runtime mutation / hidden startup authority

Status: `mitigating`  
Impact: `medium`

Risk:

```text
Historical source-patch machinery remains in or near the runtime path and can be mistaken for current product authority or accidentally reactivated.
```

Accepted-main finding before current workpackage:

- Docker invoked `fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py`;
- current Premium/direct-source markers caused both to exit without source mutation.

Current PR #116 candidate mitigation:

- Docker no longer invokes either historical source-patch script;
- Streamlit starts the existing `presidio_streamlit.py` directly with the previous server flags unchanged;
- tests are being rebound from historical patch-order assertions to direct-source/no-runtime-mutation contracts;
- the two historical mutation scripts still remain in the repository and therefore remain separate `RETIRE` candidates.

Residual risk:

- dormant historical patch code can still be mistaken for current authority or accidentally reintroduced;
- script/test retirement must be evidence-based rather than a mass deletion.

Do not combine this residual cleanup with Scrub Private persistence/egress changes.

---

# Product-claim boundary

Disallowed claims include:

```text
Scrub vindt altijd alle persoonsgegevens.
Scrub garandeert volledige anonymisering.
De synthetische benchmark bewijst production readiness.
Hugging Face tests bewijzen zero retention op provider-infrastructuurniveau.
Een scrubbed document is veilig zonder menselijke controle.
```

Allowed direction:

```text
Scrub helpt gevoelige waarden te detecteren, controleren en pseudonimiseren terwijl context behouden blijft. Menselijke review en zichtbare beperkingen blijven onderdeel van het veiligheidsmodel.
```

For Scrub Private, content-retention/security claims must match independently verified application and service behavior exactly.
