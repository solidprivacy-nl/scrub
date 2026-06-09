# WP19 — Recall benchmark specification

Status: completed specification-only.  
Repository: `solidprivacy-nl/scrub`.  
Scope: benchmark/test-design only; no recognizer logic, runner, UI, dependency, export or reinsert changes.

---

## 1. Benchmark purpose

The recall benchmark exists to make Scrub's highest product risk measurable:

```text
false negatives / missed sensitive data
```

A false positive can usually be corrected during review. A false negative can leave real sensitive data in scrubbed output and create the privacy incident the user wanted to prevent.

The benchmark must therefore answer, per entity class and per document domain:

1. Which sensitive values were present in the synthetic source document?
2. Which values did Scrub detect?
3. Which values were missed?
4. Which non-sensitive context terms were incorrectly flagged?
5. Which entity classes are safe enough to trust only with human review and residual-risk warning?

The benchmark is not a marketing accuracy claim. It is an internal trust and regression-control layer.

---

## 2. Target entity classes

The first benchmark taxonomy must include at least these classes:

| Benchmark class | Meaning | Typical handling expectation |
|---|---|---|
| `PERSON` | Natural-person names, initials plus surname, named witnesses, clients, patients, employees, professionals when identifying | Detect value span only. Preserve role/context word. |
| `ADDRESS` | Street, house number, city, full residential or office address when identifying | Detect address value; postcode may also be separately labeled. |
| `EMAIL` | Email addresses | Detect full email value. |
| `PHONE` | Dutch mobile and landline numbers, including `+31`, `0031`, spaced and punctuated variants | Detect full phone value. |
| `BSN` | Dutch burgerservicenummer-like values | Detect only valid/supported BSN values; avoid dates and phone numbers. |
| `IBAN` | Dutch/EU IBAN values | Detect full IBAN value. |
| `DATE` | Dates that are identifying or case-relevant, especially birth dates and appointment dates when configured for scrubbing | Detect the date value. Report separately from BSN/phone false positives. |
| `NL_POSTCODE` | Dutch postcodes | Detect postcode value. |
| `CASE_NUMBER` | Court case numbers, rolnummers, rekestnummers, parketnummers and ECLI-adjacent matter numbers | Detect value only, not labels such as `zaaknummer`. |
| `DOSSIER_NUMBER` | Lawyer/internal dossier numbers | Detect value only. |
| `CLIENT_NUMBER` | Client/patient/customer numbers | Detect value only. |
| `CLAIM_NUMBER` | Insurance or claim references | Detect value only. |
| `INCIDENT_NUMBER` | Incident references, care incidents, police/shop/security incidents | Detect value only. |
| `ECLI` | ECLI references | Detect full ECLI value. |
| `ORGANIZATION` | Organizations when identifying or linked to a matter | Detect organization name when in scope. |
| `MEDICAL_OR_CARE_REFERENCE` | BIG numbers, patient/client identifiers, care-plan IDs, zorgdossier references, room/department references when identifying | Detect value only; preserve care role/context words. |
| `ROLE_OR_CONTEXT_TERM_TO_PRESERVE` | Role or legal/care context words that should stay readable | Must usually remain undetected unless the term is part of a unique identifying value or label-value construct. |

Mapping to existing implementation labels can be handled by the future runner. For example, `PHONE` may map to `NL_PHONE_NUMBER`, and `CASE_NUMBER` may map to `NL_LEGAL_CASE_NUMBER`, `NL_ROLNUMMER`, `NL_REKESTNUMMER` or `NL_PARKETNUMMER`.

---

## 3. Context terms that must be preserved

The benchmark must explicitly test that generic legal and care context terms are not automatically treated as sensitive values.

Examples that should normally remain readable:

```text
slachtoffer
minderjarige
verzoeker
verweerder
eiser
rechtbank
arts
cliënt
zorgmedewerker
```

These terms may become sensitive only when the surrounding context makes them identifying. Examples:

- `slachtoffer A` may be preserved as role/context if it is a generic procedural label.
- `slachtoffer Pieter van Dam` contains a `PERSON` value and should detect `Pieter van Dam`, not necessarily the word `slachtoffer`.
- `cliëntnummer CL-FAM-55201` should detect `CL-FAM-55201` as `CLIENT_NUMBER`, not the label `cliëntnummer`.
- `arts dr. Pieter van Leeuwen, BIG-nummer 12345678901` should detect the person name and BIG value, while preserving the professional role word `arts`.

The scorecard must include a preservation section for these context terms because over-masking can destroy legal meaning.

---

## 4. Gold-label format

The benchmark corpus should use a simple, explicit gold-label format that can be stored in version control and reviewed by humans.

Preferred future format: one JSON or YAML sidecar per synthetic document.

Minimum fields:

```json
{
  "document_id": "legal_family_001",
  "domain": "legal",
  "document_type": "verzoekschrift",
  "language": "nl",
  "source_file": "corpus/legal_family_001.txt",
  "synthetic": true,
  "labels": [
    {
      "id": "L001",
      "entity_class": "PERSON",
      "text": "Fatima El Amrani",
      "start": 120,
      "end": 136,
      "sensitivity": "direct_identifier",
      "required": true,
      "notes": "Party name"
    }
  ],
  "preserve_terms": [
    {
      "term": "minderjarige",
      "start": 248,
      "end": 260,
      "reason": "legal role/context term"
    }
  ],
  "known_traps": [
    {
      "text": "03-09-2015",
      "trap_type": "date_must_not_be_bsn_or_phone"
    }
  ]
}
```

### Required label rules

1. `start` is zero-based inclusive character offset.
2. `end` is zero-based exclusive character offset.
3. Offsets must refer to the exact plain-text benchmark source.
4. `text` must equal `source_text[start:end]`.
5. Labels must point to the sensitive value span, not the surrounding label, unless the label itself is uniquely identifying.
6. One sensitive value may have multiple acceptable implementation mappings, but the gold class remains canonical.
7. Synthetic-only data is mandatory; no real customer, legal or care documents may be committed.

---

## 5. Synthetic corpus requirements

The first corpus should be messy but controlled. It must be synthetic, representative and reviewable.

Minimum corpus shape for WP20:

| Domain | Minimum documents | Examples |
|---|---:|---|
| Legal | 8 | arbeidsrecht, familierecht, strafrecht, bestuursrecht, vreemdelingenrecht, civiel, huurrecht, letselschade/claim |
| Care/Zorg | 8 | incidentmelding, zorgplan, cliëntverslag, rooster/aanwezigheid, MDO-verslag, klachtenbrief, medicatie-administratief voorbeeld, verpleegoproep/logboek |
| Mixed professional | 4 | gemeente, verzekeraar, school/jeugd, HR/care-employer context |

Each document should contain:

- at least 20 gold labels;
- at least 5 context terms to preserve;
- at least 5 false-positive traps;
- at least 3 repeated values to test consistent detection;
- at least 2 label-value patterns where only the value should be detected;
- at least 1 paragraph where legal or care meaning would be damaged by over-masking.

---

## 6. Messy text requirements

The corpus must not only contain clean examples. It must include common professional-document messiness:

- inconsistent spacing: `06 12345678`, `06-12345678`, `+31 6 1234 5678`;
- punctuation near identifiers: `Dossiernummer: ARB-2026-00421;`;
- line breaks inside addresses and matter references;
- tables converted to text with columns running together;
- headers and footers repeated as plain text;
- OCR-like noise without implementing OCR: `Zaaknr.` / `Zaak nr` / `Zaa knummer` as synthetic text traps;
- initials and particles in names: `mr. N. van Dijk`, `Fatima El Amrani`;
- Dutch accents and apostrophes;
- mixed legal and care vocabulary;
- duplicate values across different sections;
- values appearing in attachment lists;
- values next to non-sensitive labels that should remain readable.

The benchmark should deliberately include negative examples where numbers resemble other entity types:

- dates that must not become BSN or phone;
- legal article references like `7:669 BW` that must not become case numbers;
- money amounts that must not become references;
- generic room numbers that may or may not be identifying depending on context;
- role labels without names.

---

## 7. Legal-domain examples

Synthetic legal examples should cover at least:

```text
Zaaknummer: 10598721 / UE VERZ 26-441
Dossiernummer: ARB-2026-00421
Cliëntnummer: CL-FAM-55201
Parketnummer: 10/456789-26
Proces-verbaalnummer: PL1700-20260518-334455
Claimreferentie: CLM-2026-112233
Incidentnummer: INC-2026-0912
ECLI: ECLI:NL:RBAMS:2026:1234
```

Context preservation examples:

```text
Namens cliënt Jan Jansen wordt verweer gevoerd.
De minderjarige Sami El Amrani staat ingeschreven op het adres van verzoeker.
Slachtoffer Pieter van Dam heeft verklaard dat hij verdachte niet kent.
De rechtbank beoordeelt het verzoek van eiser en verweerder.
```

Expected behavior:

- detect `Jan Jansen`, `Sami El Amrani`, `Pieter van Dam`;
- preserve `cliënt`, `minderjarige`, `slachtoffer`, `rechtbank`, `eiser`, `verweerder` unless identifying context requires otherwise;
- detect matter-reference values only, not labels such as `Zaaknummer` or `Dossiernummer`.

---

## 8. Care-domain examples

Synthetic care examples should cover at least:

```text
Cliëntnummer: ZORG-CL-2026-00441
Zorgdossier: ZD-2026-99121
Incidentnummer: MIC-2026-0188
Kamer: B-214
Afdeling: Magnolia 2
Verpleegoproepreferentie: VOS-2026-000778
BIG-nummer: 12345678901
Contactpersoon: Ahmed El Idrissi, 06 33445566
```

Care context preservation examples:

```text
De cliënt kreeg ondersteuning van de zorgmedewerker.
De arts beoordeelde het wondbeleid.
De mantelzorger is geïnformeerd volgens afspraak.
De verpleegkundige noteerde dat kamer B-214 extra toezicht nodig had.
```

Expected behavior:

- preserve generic words such as `cliënt`, `zorgmedewerker`, `arts`, `mantelzorger`, `verpleegkundige`;
- detect names, phone numbers, care references and strongly identifying room/client combinations;
- report ambiguous care-location terms separately when context is not enough to mark them sensitive.

---

## 9. Recall metric

Recall measures how many gold sensitive values Scrub found.

```text
recall = true_positives / (true_positives + false_negatives)
```

A detection counts as a true positive when:

1. the predicted span overlaps the gold span enough to identify the same value;
2. the predicted entity maps to an acceptable benchmark class;
3. the span contains the sensitive value, not only the label/context word.

Recommended matching tiers:

| Tier | Rule | Use |
|---|---|---|
| exact | predicted start/end exactly match gold start/end | strict reporting |
| value-normalized | normalized text equals gold value, ignoring whitespace/punctuation variants | practical Dutch references and phones |
| overlap | sufficient character overlap with same value | diagnostic only |

The minimum CI scorecard should report exact and value-normalized recall. Overlap recall may be included as a diagnostic but must not hide missed sensitive values.

False negatives should be grouped by failure class:

- missed class entirely;
- detected wrong type;
- span too narrow;
- span too broad;
- only label detected;
- value split across line/run/table boundary;
- duplicate occurrence missed;
- context required but absent;
- unsupported class.

---

## 10. Precision metric

Precision measures how many Scrub predictions were correct.

```text
precision = true_positives / (true_positives + false_positives)
```

A false positive includes:

- a preserved context word incorrectly treated as sensitive;
- a legal article reference treated as a case number;
- a date treated as BSN or phone;
- a money amount treated as a reference;
- a generic role term masked without identifying context;
- a label such as `Dossiernummer` detected instead of the actual value.

Precision matters because over-masking can destroy legal or care meaning, but recall remains the higher-priority safety metric.

---

## 11. Per-entity scorecard

The future runner should produce a per-entity scorecard with at least:

| Field | Meaning |
|---|---|
| `entity_class` | Canonical benchmark class. |
| `gold_count` | Number of expected labels. |
| `prediction_count` | Number of predictions mapped to the class. |
| `true_positive_exact` | Exact span matches. |
| `true_positive_normalized` | Normalized value matches. |
| `false_negative_count` | Missed gold labels. |
| `false_positive_count` | Incorrect predictions. |
| `recall_exact` | Exact recall. |
| `recall_normalized` | Value-normalized recall. |
| `precision_exact` | Exact precision. |
| `precision_normalized` | Value-normalized precision. |
| `top_failure_classes` | Most frequent failure reasons. |
| `examples` | Small synthetic snippets for failed cases. |

The scorecard must always show classes with zero detections if the gold corpus contains those labels.

---

## 12. Minimum acceptable reporting format

The first CI-capable report should include:

1. overall recall and precision;
2. per-domain recall and precision: legal, care, mixed;
3. per-entity recall and precision;
4. false-negative list with document ID, entity class, expected text and failure class;
5. false-positive list with document ID, predicted text and reason where known;
6. context-preservation failures;
7. known unsupported cases;
8. pass/fail threshold summary;
9. generated timestamp and corpus version;
10. clear warning that the corpus is synthetic and does not prove real-world safety.

Suggested future output paths:

```text
benchmark/reports/recall_scorecard.json
benchmark/reports/recall_scorecard.md
```

---

## 13. CI execution guidance for later workpackages

WP19 does not implement the runner. Later CI work should follow this sequence:

1. WP20 creates the messy synthetic Dutch legal/zorg corpus.
2. WP21 defines the final gold-label schema and validates offsets.
3. WP22 implements a local benchmark runner.
4. WP23 adds a CI scorecard gate.
5. WP24 creates a residual-risk report suitable for user-facing audit/support material.

Future CI should:

- run locally without cloud document processing;
- use only synthetic corpus files committed to the repository;
- fail on malformed gold labels;
- fail on severe recall regressions after baselines are accepted;
- initially warn rather than fail on classes without accepted thresholds;
- produce artifacts that show missed values in synthetic snippets only;
- avoid storing real documents or secrets.

Recommended first threshold policy:

```text
CI phase 1: report-only baseline.
CI phase 2: fail on benchmark runner errors or malformed labels.
CI phase 3: fail on recall regression against accepted baseline.
CI phase 4: require minimum per-entity recall thresholds before trust claims.
```

Do not set aggressive pass/fail thresholds before the corpus and runner are stable.

---

## 14. Known limitations

- A synthetic benchmark cannot prove safety on real confidential documents.
- Character offsets can become brittle if source text is edited without updating labels.
- Exact span matching may penalize useful near-matches; normalized matching must therefore be reported separately.
- Entity mapping from implementation labels to benchmark classes needs WP21/WP22 design.
- Current examples may not cover all Dutch legal and care document forms.
- Benchmarking text output does not fully cover DOCX hidden content, metadata, comments, headers or footers.
- OCR/scanned PDFs remain out of scope unless separately approved.
- High recall in the benchmark does not remove the need for human review and residual-risk warnings.

---

## 15. Next implementation workpackages

Recommended next sequence:

1. `WP20 — Synthetic messy Dutch legal/zorg benchmark corpus`.
2. `WP21 — Gold-label entity schema`.
3. `WP22 — Recall/precision test runner`.
4. `WP23 — Entity-class scorecard in CI`.
5. `WP24 — False-negative residual-risk report`.

WP20 should create only synthetic documents and labels. It must not change recognizer logic.

---

## 16. Intentionally not changed in WP19

- No recognizer logic changed.
- No benchmark runner implemented.
- No tests added or changed.
- No UI changed.
- No dependencies changed.
- No real data added.
- No export or reinsert behavior changed.
