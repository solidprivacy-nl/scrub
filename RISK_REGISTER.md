# SolidPrivacy Scrub — Current Risk Register

This register tracks the **current** product, privacy, security, trust and execution risks for SolidPrivacy Scrub.

Detailed pre-convergence risk-history remains recoverable from exact baseline:

```text
54c73e0ebf5a3a3ed7039a50596fb57694add3cd
```

Git/CHANGELOG preserve execution history. This file should show the live risk picture rather than accumulate workpackage narrative.

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
- new recognizer changes must remain evidence-driven so precision fixes do not silently reduce recall.

Required principle:

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
- document-bound placeholders;
- mapping digest;
- structural key validation;
- fail-closed wrong/mixed/missing-binding handling;
- controlled TXT/DOCX/PDF-to-TXT reinsert paths;
- adversarial/roundtrip tests;
- legacy unbound state kept explicitly unverified.

Current gaps:

- Scrub Key remains inherently sensitive re-identification material;
- cryptographic authenticity/signing is not implied by the current mapping digest;
- user/operational handling remains part of the threat model.

---

## R3 — Placeholder corruption during AI/external roundtrip

Status: `mitigating`  
Impact: `high`

Risk:

```text
An external AI/process rewrites, translates, merges, deletes or corrupts placeholders, causing deterministic reinsert to fail or restore incompletely.
```

Current controls/evidence:

- stable bound placeholder grammar;
- mapping/document binding;
- roundtrip/adversarial mutation tests;
- unknown/missing placeholder diagnostics;
- fail-visible reinsert behavior.

Current gaps:

- malformed near-placeholders outside strict grammar may remain a diagnostic limitation;
- Scrub must not silently guess/repair values where binding cannot be proven.

---

## R4 — Hidden document content, metadata and unsupported-part leakage

Status: `mitigating`  
Impact: `high`

Risk:

```text
DOCX metadata, comments, tracked changes, unsupported XML parts, headers/footers or other hidden content retains sensitive information outside the supported scrub/reinsert surface.
```

Current controls/evidence:

- DOCX hygiene/audit reporting;
- body/table/header/footer supported handling;
- synthetic fidelity/hygiene tests;
- explicit unsupported-part warnings;
- PDF support is text-based with explicit product limitations.

Current gaps:

- unsupported DOCX parts remain a known boundary;
- hygiene reporting must not be presented as a complete clean-document guarantee where unsupported content may exist.

---

## R5 — Scrub Private content-retention / external-egress trust boundary

Status: `open`  
Impact: `critical`

Risk:

```text
A managed Private service retains customer document content, mappings or Scrub Keys, logs content, backs it up, or sends document content to a third party contrary to the intended service promise.
```

Current evidence on pre-convergence/full-feature application:

- `replacement_memory.py` intentionally persists original/replacement/entity values to `/data/replacement_memory.json` when persistent storage exists;
- current Expert functionality includes Azure AI Language and OpenAI/Azure synthesis paths;
- synthesis helper currently prints a content-bearing prompt.

These are not evidence that the current prototype is defective for every deployment model; they are **variant-specific conflicts** with Scrub Private.

Scrub Private target:

```text
no intentional persistent server-side customer document content
no content-bearing ordinary application logs
no document-content backup
no third-party document-processing egress
minimal non-document control-plane persistence only when required
```

Mitigation sequence:

- first complete Repository Convergence without destroying potentially useful Local/full-feature behavior;
- then remove/exclude hosted-incompatible persistence/egress from the Private line in separately tested/assured workpackages;
- prove application-level behavior on HF with synthetic data;
- prove infrastructure/service retention properties later on controlled production infrastructure.

Do not use HF application tests to claim provider-level zero retention.

---

## R6 — Review UX, stale state and workflow clarity

Status: `mitigating`  
Impact: `high`

Risk:

```text
The user misses a sensitive value, changes state without realizing downstream output is stale, or the interface obscures whether review is complete/current.
```

Current controls/evidence:

- staged Premium workspace;
- Standard/Expert modes over shared authoritative state;
- generation-bound analysis/review/export state;
- fail-closed stale export gating;
- explicit re-completion after review edits;
- source-versus-processed review;
- authoritative replacement table;
- direct/manual missed-value correction;
- AppTest and integration coverage.

Current gap:

- parent Premium live-verification issues contain stale/unfinished closeout state; current deployed behavior must be reconciled against merged marker/address repairs before declaring those historical gates closed.

---

## R7 — PDF limitations misunderstood by users

Status: `mitigating`  
Impact: `high`

Risk:

```text
Users interpret text-based PDF support as OCR or complete restored-PDF fidelity.
```

Current boundary:

- text-based PDF extraction is supported;
- OCR is not implied;
- restored PDF generation is not implied;
- reinsert output may be restored text rather than a reconstructed PDF.

Copy, audit and pilot guidance must keep these limitations explicit.

---

## R8 — Audit/evidence clarity and false confidence

Status: `mitigating`  
Impact: `high`

Risk:

```text
Multiple benchmark/report generations are mistaken for equivalent safety evidence, or diagnostic metrics are presented as production-readiness/individual-document safety scores.
```

Current controls:

- synthetic-only/report-only warnings in benchmark/residual-risk tooling;
- known limitations and human-review requirement;
- separate domain and workflow validation systems.

Current convergence requirement:

Classify existing evidence paths as:

```text
CANONICAL RELEASE VALIDATION
SUPPLEMENTAL DIAGNOSTIC
HISTORICAL / SUPERSEDED
```

Do not create a replacement Evidence Framework merely to make the hierarchy look cleaner.

Disallowed product behavior:

- per-document “94% safe” or similar false precision;
- production-safety claim solely from synthetic scores.

---

## R9 — Dutch Legal recognition precision/recall and context damage

Status: `mitigating`  
Impact: `high`

Risk:

```text
Legal identifiers/addresses/names are missed or misclassified, or ordinary legal/professional context is over-masked and loses meaning.
```

Current controls/evidence:

- Dutch deterministic recognizers and Legal profile;
- synthetic legal examples/corpus;
- address-span precision repair on current main;
- preserve/known-trap evidence;
- manual/direct review correction;
- human review.

Future fixes remain test-first and must preserve recall/context.

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
- eight synthetic care-document families plus long-form variants;
- current-engine baseline before dedicated rules;
- gap triage;
- dedicated care recognizer contracts/implementation;
- collision/negative tests;
- cross-profile regression;
- clinical preserve expectations;
- human review.

Current gap:

Synthetic and bounded app evidence does not establish complete production recall/precision or rare-case indirect-identification safety.

Required principle:

> Preserve diagnosis, medication, dosage, laboratory values, observations and useful care context unless there is a specific evidence-backed reason to treat a value as identifying.

---

## R11 — Repository/source-of-truth drift

Status: `mitigating`  
Impact: `high`

Risk:

```text
Workers follow stale ROADMAP/WORKPACKAGES/issues or duplicate already-built functionality because repository documentation and actual main no longer describe one coherent current truth.
```

Observed pre-convergence symptoms:

- old nine-phase/local-installer roadmap still active in docs;
- multiple stacked `Current execution status override` sections in WORKPACKAGES;
- open issues describing candidate states that already PASSed/merged;
- historical Premium packages still presented as future work despite current main containing integrated staged behavior;
- several generations of benchmark/report tooling with unclear release authority.

Current mitigation:

- Repository Convergence is the active execution line;
- exact pre-convergence SHA preserved;
- temporary capability/debt ledger;
- ROADMAP/WORKPACKAGES/PROJECT_PROMPT reset;
- stale issue/evidence hierarchy reconciliation before clean-baseline declaration;
- no new feature work until `SCRUB_REPOSITORY_CONVERGED`.

Exit condition:

One clean exact SHA whose source, tests, current issues and canonical docs agree materially.

---

## R12 — Legacy runtime mutation / hidden startup authority

Status: `mitigating`  
Impact: `medium`

Risk:

```text
Historical source-patch machinery remains in the startup path and can be mistaken for current product authority or accidentally reactivated.
```

Current evidence:

- Docker still invokes `fix_streamlit_nested_expanders.py` and `fix_streamlit_pdf_text_reinsert.py`;
- current Premium/direct-source markers cause both to exit without changing source.

Mitigation direction:

- verify no supported current path depends on the mutation scripts;
- retire invocation/obsolete scripts in a narrow consequential package if that proof holds;
- retain product-level behavior tests rather than tests whose only purpose is to keep dead patch machinery alive.

Do not combine this with hosted persistence/egress changes.

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
