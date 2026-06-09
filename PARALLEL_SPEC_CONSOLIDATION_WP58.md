# WP58 — Parallel specification consolidation and next execution queue

Status: completed documentation/planning-only.  
Repository: `solidprivacy-nl/scrub`.

Scope: coordination, documentation and planning only. No code, tests, UI, dependencies, implementation, recognizer logic, Scrub Key encryption, placeholder migration, DOCX cleaner implementation, export behavior change, real data or cloud processing.

---

## 1. Purpose

WP58 consolidates the four completed parallel specification tracks:

```text
WP19 — Recall benchmark specification
WP25 — Scrub Key threat model
WP30 — Placeholder robustness review
WP35 — DOCX hidden content risk review
```

The goal is to convert those findings into one coherent next execution queue, remove sequencing ambiguity and prevent premature implementation in high-risk areas.

---

## 2. Summary of WP19 findings

WP19 defined the recall benchmark needed to make Scrub's highest product risk measurable:

```text
false negatives / missed sensitive data
```

Key findings:

- A false negative can leave sensitive data in scrubbed output and create the privacy incident the product is meant to prevent.
- The benchmark must measure recall and precision overall, per domain and per entity class.
- The first benchmark taxonomy should include Dutch legal and care identifiers such as names, addresses, BSN, phone, e-mail, IBAN, dates, postcodes, case numbers, dossier numbers, client numbers, claim numbers, incident numbers, ECLI, organizations and medical/care references.
- Context terms such as `slachtoffer`, `minderjarige`, `verzoeker`, `verweerder`, `eiser`, `rechtbank`, `arts`, `cliënt` and `zorgmedewerker` should normally remain readable unless identifying context makes them sensitive.
- The first corpus must be synthetic, messy and reviewable.
- CI should start report-only, then move toward malformed-label failures, regression gates and later per-entity recall thresholds.

Next mitigation from WP19:

```text
WP20 — Synthetic messy Dutch legal/zorg benchmark corpus
```

WP20 should not change recognizer logic. It should create synthetic corpus and gold-label material only.

---

## 3. Summary of WP25 findings

WP25 treats the Scrub Key as sensitive re-identification data.

Key findings:

- Scrub Key-based output is pseudonymized, not fully anonymized, as long as the key exists.
- The Scrub Key and scrubbed document are separate security objects.
- The Scrub Key can contain or enable access to names, addresses, e-mail addresses, phone numbers, client numbers, matter numbers, case references, claim numbers, care references and other confidential values.
- Accidental sharing, local Downloads retention, e-mail/AI upload, shared-computer use, unmanaged local storage and long retention are critical risks.
- Loss of the key prevents deterministic reinsert.
- Tampered or malformed keys can cause incorrect or unsafe reinsert.
- Encryption, lifecycle, expiry/delete and tamper protection require a separate approved specification before implementation.

Next mitigation from WP25:

```text
WP26 — Scrub Key encryption/lifecycle specification
```

WP26 should remain specification-only. It must not implement encryption or migrate the Scrub Key schema.

---

## 4. Summary of WP30 findings

WP30 reviewed placeholder robustness during AI roundtrip.

Key findings:

- Current placeholders such as `[PERSOON_1]`, `[ZAAKNUMMER_1]`, `[ADRES_1]` and `[ORGANISATIE_01]` are deterministic and readable but fragile under AI rewriting, translation, summarization, punctuation/spacing changes, markdown/HTML formatting and document conversion.
- Current reinsert depends on exact placeholder strings from the Scrub Key mapping.
- Existing audit fields for unknown, duplicate and not-found placeholders are useful but not enough.
- The highest-risk corruption is silent placeholder deletion or merge during summarization.
- Candidate robust formats such as `[[SP_PERSON_0001_A7F3]]` should remain proposal-only until a dedicated format proposal is accepted.
- Checksum design must avoid deriving visible values from original sensitive data.
- Backward compatibility with legacy placeholders is mandatory.

Next mitigation from WP30:

```text
WP31 — LLM-resistant placeholder format proposal
```

WP31 should compare formats and define compatibility strategy, but must not implement migration.

---

## 5. Summary of WP35 findings

WP35 reviewed DOCX hidden content and metadata risks.

Key findings:

- Current DOCX support covers `word/document.xml` text nodes, including normal body paragraphs and tables, but does not provide full DOCX package hygiene.
- Headers, footers, comments, tracked changes, metadata, custom XML, footnotes/endnotes, text boxes/shapes and embedded objects can contain sensitive values outside visible body text.
- Tracked changes are a critical leakage risk because deleted text, author names and timestamps can remain in XML.
- Metadata and custom XML are separate cleaning problems, not normal visible-text scrubbing.
- Future audit output should distinguish inspected parts, unsupported parts, cleaning actions, warnings and blocking reasons.
- Blocking export is a product semantics change and must not be introduced silently.

Proposed next mitigation from WP35 was:

```text
WP36 — DOCX metadata cleaner helper
```

WP58 adjusts the execution timing: WP36 should not be part of the immediate parallel worker set. It should wait until the metadata-cleaning helper boundary is tightened enough to avoid accidental export/document semantics changes.

---

## 6. Cross-workpackage dependencies

### WP19 → WP20/WP21/WP22/WP23/WP24

WP19 is the root of the recall/trust line. WP20 must create the synthetic corpus before a robust gold-label schema, runner, scorecard gate or residual-risk report can be useful.

Dependency chain:

```text
WP20 corpus → WP21 gold-label schema → WP22 runner → WP23 CI scorecard → WP24 residual-risk report
```

### WP25 → WP26/WP27/WP28/WP29

WP25 establishes that the Scrub Key is sensitive. WP26 must specify lifecycle and protection choices before encryption, expiry/delete policy or secure import/export tests are implemented.

Dependency chain:

```text
WP26 lifecycle/protection spec → WP27 warning UX → WP28 expiry/delete policy → WP29 secure import/export tests
```

### WP30 → WP31/WP32/WP33/WP34

WP30 establishes placeholder-corruption risk. WP31 must propose a format and compatibility strategy before checksum helpers, audit hardening or corruption tests are implemented.

Dependency chain:

```text
WP31 format proposal → WP32 checksum/validation helper → WP33 audit hardening → WP34 corruption tests
```

### WP35 → future DOCX hygiene work

WP35 establishes hidden-content and metadata risks. A metadata cleaner helper is useful, but it touches document package semantics. WP58 therefore blocks immediate WP36 implementation until the helper boundary is refined.

Recommended DOCX hygiene dependency chain:

```text
WP36-SPEC / tighter helper boundary → WP36 metadata cleaner helper → WP37 hidden-content extraction helper → WP38 hygiene audit report → WP39 clean DOCX export policy
```

If the coordinator wants to keep the existing WP36 name, the next version of WP36 should be explicitly scoped as metadata-only, helper-only, no UI, no export blocking, no comment/tracked-change removal and no clean-export claim.

---

## 7. Shared risks

The four specifications share these product risks:

1. **False confidence** — users may believe a document is safe when detection, key handling, placeholder integrity or hidden-content hygiene still has gaps.
2. **Silent semantic change** — over-masking, wrong reinsert, placeholder merge or DOCX cleaning can alter legal/care meaning.
3. **Partial restoration** — AI-modified placeholders or malformed keys can restore only part of the intended content.
4. **Hidden leakage** — visible text may be scrubbed while metadata, tracked changes, comments or headers still leak data.
5. **Wrong artifact handling** — a Scrub Key, scrubbed document, restored document and clean-export claim are different artifacts with different risks.
6. **Premature implementation** — encryption, placeholder migration, DOCX cleaning or export blocking can harm trust if implemented before the policy/spec layer is clear.
7. **Cloud trust gap** — Hugging Face remains a development/demo environment, not the target confidential processing environment.

---

## 8. Conflicts or inconsistencies found

No direct contradiction was found between WP19, WP25, WP30 and WP35.

The main sequencing tension is:

```text
WP35 recommends WP36 as the next DOCX mitigation,
but WP36 as a helper may affect document/export semantics if scoped too broadly.
```

Resolution:

- Do not start WP36 in the immediate four-worker set.
- Keep WP36 blocked until the coordinator approves a tight helper boundary.
- The future WP36 task must be metadata-only and helper-only unless a separate policy approves broader cleaning.
- Export blocking, comments removal, tracked-change acceptance/removal and clean-export claims remain blocked until dedicated later workpackages.

A second coordination issue is that WP25 and WP30 can both touch integrity/checksum language. Resolution:

- WP26 may discuss Scrub Key file integrity/tamper detection.
- WP31 may discuss placeholder token integrity/checksum.
- Neither should implement schema migration or checksum helpers.
- Later WP32/WP29 must reconcile Scrub Key integrity and placeholder integrity before implementation.

---

## 9. Resolved sequencing recommendation

The immediate next execution queue should prioritize high-risk but separable work.

Recommended next parallel set:

```text
Worker 1: WP20 — Synthetic messy Dutch legal/zorg benchmark corpus
Worker 2: WP26 — Scrub Key encryption/lifecycle specification
Worker 3: WP31 — LLM-resistant placeholder format proposal
Worker 4: WP45 — Local runtime architecture plan
```

Rationale:

- WP20 should start first because recall/false negatives remain the highest product risk.
- WP26 can run in parallel because Scrub Key lifecycle/specification is separate from detection benchmarking.
- WP31 can run in parallel because placeholder format proposal is specification-only and must not implement migration.
- WP45 can run in parallel because local runtime architecture is a separate specification track and addresses the cloud-demo trust gap.
- WP36 should wait because DOCX metadata cleaning can affect export/document hygiene semantics.

---

## 10. Next execution queue

### Immediate queue — recommended now

#### Worker 1: WP20 — Synthetic messy Dutch legal/zorg benchmark corpus

Type: benchmark data/specification artifacts.  
Allowed direction:

- create synthetic corpus documents;
- create or draft gold-label sidecars if included in WP20 scope;
- use only synthetic Dutch legal/care/mixed professional data;
- do not change recognizer logic;
- do not add CI gates yet unless separately approved.

Primary risk mitigated:

```text
R1 — False negatives / missed sensitive data
```

#### Worker 2: WP26 — Scrub Key encryption/lifecycle specification

Type: security/lifecycle specification.  
Allowed direction:

- define lifecycle states;
- compare warning-only, protected file, encrypted file and local vault options;
- specify deletion/retention/passphrase-loss behavior;
- specify future tamper-detection direction;
- do not implement encryption;
- do not change Scrub Key JSON schema or import/export behavior.

Primary risk mitigated:

```text
R2 — Scrub Key leakage or accidental sharing
```

#### Worker 3: WP31 — LLM-resistant placeholder format proposal

Type: architecture/specification.  
Allowed direction:

- compare candidate placeholder formats;
- define compatibility strategy for legacy placeholders;
- define checksum requirements at proposal level;
- do not implement migration;
- do not change reinsert helper logic.

Primary risk mitigated:

```text
R3 — Placeholder corruption during AI roundtrip
```

#### Worker 4: WP45 — Local runtime architecture plan

Type: architecture/specification.  
Allowed direction:

- compare local Streamlit launcher, PyInstaller, Tauri and Electron paths;
- define local file-handling and offline/trust requirements at plan level;
- do not implement packaging;
- do not change Docker/runtime startup behavior;
- do not introduce cloud processing.

Primary risk mitigated:

```text
R5 — Cloud-demo trust gap
```

---

## 11. Parallelization recommendation

Safe to run now in parallel:

```text
WP20, WP26, WP31, WP45
```

Condition:

- each worker must stay inside its own allowed file set;
- no UI files should be touched;
- no code/helpers should be changed unless the workpackage explicitly allows it;
- no export/download semantics should change;
- no Scrub Key schema or placeholder format migration should occur;
- no real data should be committed.

Additional safe parallel candidates if capacity exists:

```text
WP50 — Pilot design: Legal vs Zorg
WP56 — User-facing release notes split and documentation hygiene
WP57 — Workflow status monitoring runbook and checks
```

Priority note:

- WP50 is useful for GTM/validation but should not use real customer documents in the repo.
- WP56 and WP57 are lower-risk documentation/operations cleanup tasks.
- Do not let WP56 rewrite the meaning of technical changelog entries while other workers depend on them.
- Do not let WP57 change GitHub workflows unless separately approved.

---

## 12. What must remain blocked

The following must remain blocked until later workpackages or coordinator approval:

```text
WP36 — DOCX metadata cleaner helper
```

Reason:

- metadata cleaning may alter document package contents and user expectations;
- DOCX cleaning sits close to export/document hygiene semantics;
- WP35 explicitly says blocking export is a product semantics change;
- comments removal, tracked-change handling, custom XML removal and clean-export claims require separate policy decisions.

Also blocked:

- Scrub Key encryption implementation;
- Scrub Key JSON schema migration;
- placeholder migration;
- placeholder checksum/validation helper implementation before WP31 is accepted;
- unknown/changed placeholder audit hardening before the format proposal is stable;
- DOCX comment/tracked-change removal;
- clean DOCX export blocking;
- restored PDF output;
- OCR;
- cloud document processing;
- real-data benchmark fixtures;
- batch/CLI scale features before single-document trust/security/review/local-runtime foundations are credible.

---

## 13. What can run now

The coordinator can start this parallel set now:

```text
Worker 1: WP20 — Synthetic messy Dutch legal/zorg benchmark corpus
Worker 2: WP26 — Scrub Key encryption/lifecycle specification
Worker 3: WP31 — LLM-resistant placeholder format proposal
Worker 4: WP45 — Local runtime architecture plan
```

If only one worker is available, start with:

```text
WP20 — Synthetic messy Dutch legal/zorg benchmark corpus
```

Reason:

```text
False negatives remain the highest product risk.
```

---

## 14. What requires coordinator approval

Coordinator approval is required before:

- starting implementation work that changes helper behavior;
- changing export/download semantics;
- blocking export based on DOCX hygiene findings;
- changing Scrub Key JSON schema;
- implementing encryption or vault behavior;
- changing placeholder format or migrating legacy placeholders;
- adding AI/cloud processing;
- adding OCR or restored PDF output;
- using real pilot/customer/legal/care documents;
- changing GitHub workflow files or deployment behavior;
- asking for app verification after future UI changes.

---

## 15. Remaining risks

After WP58, the four major risks remain active but better sequenced:

- R1 false negatives remains critical until WP20–WP24 deliver corpus, labels, runner, scorecard and residual-risk reporting.
- R2 Scrub Key leakage remains critical until lifecycle, protection, warning UX, expiry/delete and secure import/export tests exist.
- R3 placeholder corruption remains high until a robust format proposal, validation helper, audit hardening and corruption tests exist.
- R4 hidden DOCX content remains high until metadata cleaning, hidden-part extraction, hygiene audit and clean export policy exist.
- R5 cloud-demo trust gap remains high until local runtime architecture and implementation are credible.

WP58 does not close these risks. It only defines the next safe execution order.

---

## 16. Roadmap and release notes impact

Roadmap update: not required.

Reason:

```text
WP58 does not change the strategic phase order. It operationalizes the existing roadmap into a next execution queue.
```

Release notes update: not required.

Reason:

```text
WP58 adds internal planning documentation only. It does not change user-facing product capabilities.
```

---

## 17. Final WP58 decision

Accepted next execution queue:

```text
1. WP20 — Synthetic messy Dutch legal/zorg benchmark corpus
2. WP26 — Scrub Key encryption/lifecycle specification
3. WP31 — LLM-resistant placeholder format proposal
4. WP45 — Local runtime architecture plan
```

Parallelization:

```text
WP20, WP26, WP31 and WP45 may run in parallel.
```

Blocked until later:

```text
WP36 — DOCX metadata cleaner helper
```

WP36 may resume only after a tighter metadata-cleaner helper scope is approved, with no silent export/document semantics change.

---

## 18. Intentionally not changed in WP58

- No code changed.
- No tests added or changed.
- No UI changed.
- No dependencies changed.
- No recognizer logic changed.
- No Scrub Key encryption implemented.
- No Scrub Key schema changed.
- No placeholder migration.
- No DOCX cleaner implemented.
- No export behavior changed.
- No real data added.
- No cloud processing added.
- No roadmap change made.
- No release notes change made.
