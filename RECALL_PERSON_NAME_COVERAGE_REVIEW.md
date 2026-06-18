# PERSON-name coverage review

Workpackage: `WP_RECALL_PERSON_NAME_COVERAGE_REVIEW`

Repository: `solidprivacy-nl/scrub`

Status: review/planning/documentation-only.

This document reviews the remaining 14 missed `PERSON` labels from the cleaned diagnostic recall benchmark artifact. It does not fix recognizers, change product behavior, enforce thresholds or create a gate.

---

## 1. Goal and non-goals

Goal:

```text
Classify remaining PERSON-name recall gaps and define a safe follow-up route for tests, recognizer planning and later contract work.
```

Non-goals:

```text
This is a coverage review.
This is not a fix.
This does not change recognizers.
This does not change candidate scanner behavior.
This does not change runner/report code.
This does not change product behavior.
This does not create a threshold.
This does not create a gate.
This does not prove product safety.
```

---

## 2. PERSON-gap inventory

| document_id | domain | source_file | missed_person_text | context snippet | gold_label_id | likely pattern | likely cause | risk | recommended follow-up |
|---|---|---|---|---|---|---|---|---|---|
| care_mixed_identifiers_seed_001 | care | corpus/care/care_mixed_identifiers_seed_001.txt | Hassan El Amrani | `Hassan El Amrani en Mila van Dijk zijn bereikbaar via ...` | L009 | Arabic/Moroccan-style full name near another name and contact details | recognizer coverage issue; not mapping noise | direct identifier left visible | add coverage tests for multi-token Arabic/Moroccan-style names near email/phone |
| care_mixed_identifiers_seed_001 | care | corpus/care/care_mixed_identifiers_seed_001.txt | Mila van Dijk | `Hassan El Amrani en Mila van Dijk zijn bereikbaar via ...` | L010 | Dutch full name with tussenvoegsel | recognizer coverage issue; conjunction-separated names may be weak | direct identifier left visible | add paired-name tests with Dutch tussenvoegsel |
| care_reference_seed_001 | care | corpus/care/care_reference_seed_001.txt | Ahmed El Idrissi | `Ahmed El Idrissi is contactpersoon en is bereikbaar via ...` | L007 | Arabic/Moroccan-style full name as contact person | recognizer coverage issue; care contact-person context may be weak | direct identifier left visible | add contactpersoon-name tests |
| care_role_preservation_seed_001 | care | corpus/care/care_role_preservation_seed_001.txt | Bakker | `Later noteerde arts Bakker dat ...` | L001 | single surname after professional role | single surname is ambiguous; current legal-party recognizer does not target care role `arts` | direct identifier but high ambiguity | design tests before any recognizer change; require role-word preservation |
| care_role_preservation_seed_001 | care | corpus/care/care_role_preservation_seed_001.txt | Sara El Idrissi | `... verpleegkundige Sara El Idrissi de cliënt ...` | L002 | care role + Arabic/Moroccan-style full name | recognizer coverage issue; care role not covered by legal-party pattern | direct identifier tied to care role | add care-role + full-name tests |
| care_role_preservation_seed_001 | care | corpus/care/care_role_preservation_seed_001.txt | Youssef Ait Ben | `... de cliënt Youssef Ait Ben had begeleid.` | L003 | care role + Arabic/Moroccan-style full name | recognizer coverage issue; care role context and multi-token name | direct identifier tied to cliënt role | add cliënt + full-name tests with role preservation |
| care_role_preservation_seed_001 | care | corpus/care/care_role_preservation_seed_001.txt | Fatima Zahra | `Mantelzorger Fatima Zahra kreeg ...` | L004 | care role + first name + surname-like token | recognizer coverage issue; care role `Mantelzorger` not in legal party pattern | direct identifier tied to care role | add mantelzorger + name tests |
| legal_false_positive_traps_seed_001 | legal | corpus/legal/legal_false_positive_traps_seed_001.txt | Lina de Vries | `mr. Lina de Vries bespreekt de zaak ...` | L004 | legal/professional title + Dutch tussenvoegsel name | recognizer coverage issue; title `mr.` alone is not in legal-party role pattern unless preceded by role word | direct identifier in legal context | add `mr.` title + name tests |
| legal_false_positive_traps_seed_001 | legal | corpus/legal/legal_false_positive_traps_seed_001.txt | Omar Ben Salah | `... met Omar Ben Salah via omar.bensalah@example.test ...` | L005 | Arabic/Moroccan-style full name near email/phone | recognizer coverage issue; unlabelled name near contact details | direct identifier left visible | add unlabelled person near contact details tests |
| legal_mixed_identifiers_seed_001 | legal | corpus/legal/legal_mixed_identifiers_seed_001.txt | Nora El Yassini | `... wordt genoemd naast Nora El Yassini en Tariq de Jong.` | L010 | Arabic/Moroccan-style full name in pair | recognizer coverage issue; unlabelled paired names | direct identifier in legal note | add paired-name tests after legal reference context |
| legal_mixed_identifiers_seed_001 | legal | corpus/legal/legal_mixed_identifiers_seed_001.txt | Tariq de Jong | `... naast Nora El Yassini en Tariq de Jong.` | L011 | Dutch/Arabic mixed name with tussenvoegsel | recognizer coverage issue; conjunction-separated second name | direct identifier in legal note | add conjunction-separated second-name tests |
| legal_reference_seed_001 | legal | corpus/legal/legal_reference_seed_001.txt | Noor van Dijk | `mr. Noor van Dijk bespreekt dit met Sami El Amrani ...` | L014 | legal/professional title + Dutch tussenvoegsel name | recognizer coverage issue; title context not enough | direct identifier near phone/email | add legal title + two-party-name tests |
| legal_reference_seed_001 | legal | corpus/legal/legal_reference_seed_001.txt | Sami El Amrani | `... bespreekt dit met Sami El Amrani via 06-12345678 ...` | L015 | Arabic/Moroccan-style full name near phone/email | recognizer coverage issue; unlabelled name near contact details | direct identifier near direct contact data | add name-near-phone/email tests |
| legal_role_preservation_seed_001 | legal | corpus/legal/legal_role_preservation_seed_001.txt | Jansen | `Later noteerde arts Jansen dat getuige Fatima El Amrani ...` | L001 | single surname after professional role | single surname ambiguity; `arts` role not currently covered by legal-party pattern | direct identifier but high ambiguity | design single-surname rules carefully before implementation |
| legal_role_preservation_seed_001 | legal | corpus/legal/legal_role_preservation_seed_001.txt | Fatima El Amrani | `... getuige Fatima El Amrani de minderjarige ...` | L002 | legal role + Arabic/Moroccan-style full name | recognizer coverage issue despite legal role context; mapping already cleaned | direct identifier tied to legal role | add legal role + full-name regression tests |

Note: `Sami El Amrani` also appears in `legal_role_preservation_seed_001`, but the cleaned artifact reports one exact match in that document; the remaining listed 14 misses do not include that occurrence as a missed label after cleanup. The diagnostic test inventory keeps the full review inventory visible and is not an automatic recall claim.

---

## 3. Name-type classification

| Category | Count | Examples | Why likely difficult | Future test needed |
|---|---:|---|---|---|
| Full Dutch name with tussenvoegsel | 4 | `Mila van Dijk`, `Lina de Vries`, `Tariq de Jong`, `Noor van Dijk` | Particles such as `van`, `de` can also be normal words; names may be unlabelled or title-led. | Tests for first name + Dutch particle + surname in legal/care text. |
| Arabic/Moroccan-style full name | 9 | `Hassan El Amrani`, `Ahmed El Idrissi`, `Sara El Idrissi`, `Youssef Ait Ben`, `Omar Ben Salah`, `Nora El Yassini`, `Sami El Amrani`, `Fatima El Amrani`, `Fatima Zahra` | Multi-token names and particles such as `El`, `Ait`, `Ben` may not be covered robustly by spaCy or custom legal-party patterns. | Tests for multi-token Dutch/Moroccan synthetic names. |
| First name + surname | 10 | `Ahmed El Idrissi`, `Sara El Idrissi`, `Fatima Zahra`, `Lina de Vries`, `Omar Ben Salah`, `Nora El Yassini`, `Tariq de Jong`, `Noor van Dijk`, `Sami El Amrani`, `Mila van Dijk` | Not always preceded by a legal role; current custom party recognizer is context-bound. | Tests with unlabelled first-name/surname values near references and contact details. |
| Single surname | 2 | `Bakker`, `Jansen` | High ambiguity; many surnames can be normal words or roles in other contexts. | Separate single-surname tests with strong role/title context only. |
| Professional title/context + name | 4 | `arts Bakker`, `mr. Lina de Vries`, `mr. Noor van Dijk`, `arts Jansen` | Titles must remain readable; only the name value should be sensitive. `arts` is a role/context word and `mr.` is a professional title. | Title/role + value-only name tests. |
| Care role + name | 4 | `verpleegkundige Sara El Idrissi`, `cliënt Youssef Ait Ben`, `Mantelzorger Fatima Zahra`, `arts Bakker` | Care roles are intentionally preserve terms, but following names may be sensitive. | Care role + name tests with role preservation. |
| Legal role + name | 1 | `getuige Fatima El Amrani` | Legal role should remain readable while the following name is masked. | Legal role + full-name tests. |
| Name near phone/email/address | 6 | `Hassan El Amrani`, `Mila van Dijk`, `Ahmed El Idrissi`, `Omar Ben Salah`, `Noor van Dijk`, `Sami El Amrani` | Contact details are detected, but nearby person names may not be linked by the recognizer. | Name-near-contact tests. |
| Name near client/care/legal reference | 7 | `Hassan El Amrani`, `Mila van Dijk`, `Ahmed El Idrissi`, `Nora El Yassini`, `Tariq de Jong`, `Noor van Dijk`, `Sami El Amrani` | Nearby codes are detected, but personal name detection remains separate and weaker. | Combined reference + person-name corpus tests. |

---

## 4. Cause analysis

Likely causes, stated cautiously:

### Recognizer coverage issue

Most misses appear to be recognizer coverage issues rather than mapping noise. `NL_LEGAL_PARTY_NAME -> PERSON` mapping was already cleaned, so when no prediction is present the remaining problem is likely that the relevant name span was not produced by the analyzer/helper path.

### Legal-party recognizer context limitation

The current `NL_LEGAL_PARTY_NAME` recognizer is role-context-bound to legal party words such as `eiser`, `verweerder`, `slachtoffer`, `minderjarige`, `cliënt` and similar terms. It does not broadly target all professional/care roles or all title-led names.

### Care role/person gap

Care roles such as `verpleegkundige`, `mantelzorger`, `zorgmedewerker`, `behandelaar` and role/title combinations need careful handling: the role word should remain context, while the following name may need masking.

### Single surname ambiguity

`Bakker` and `Jansen` are direct identifiers in the synthetic text, but single surnames are ambiguous. A future recognizer should not broadly mask arbitrary capitalized words without strong context.

### Name-near-contact gap

Some names are adjacent to phone/email values. The current benchmark shows the contact values can be detected while the adjacent names remain missed. A future candidate approach may use proximity to contact details, but must avoid over-masking normal sentence text.

### Candidate scanner scope

The candidate scanner is currently designed for suspicious reference-like values, not person names. This is good for scope control, but it means person-name fallback requires a separate design if pursued.

### Corpus/taxonomy issue

The 14 gaps look mostly valid as direct identifier gold labels. There is no strong evidence that these are mainly corpus-taxonomy or acceptable-entity mapping issues.

---

## 5. Risk assessment

PERSON misses matter because:

```text
PERSON is a direct identifier.
False negatives can leave sensitive personal data visible.
In legal and care contexts, names can be linked to roles such as cliënt, slachtoffer, arts, getuige, mantelzorger or verpleegkundige.
```

Important safety constraints:

```text
Not every capitalized word should be treated as a person name.
Single surnames can be ambiguous.
Role words must remain readable.
Legal/care meaning must not be destroyed by broad over-masking.
```

Risk status:

- `PERSON` false-negative risk is now analyzed but not fixed.
- No recognizer change was made.
- Risk remains open until tests, contract design and implementation follow separately.

---

## 6. Recommended follow-up route

Recommended next package:

```text
WP_RECALL_PERSON_NAME_COVERAGE_TESTS
```

Purpose:

- convert the 14 missed-name examples into focused tests;
- include care-role, legal-role, professional-title, name-near-contact and single-surname cases;
- keep tests diagnostic/contract-focused first.

Recommended follow-up after tests:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN
WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS
```

Only if tests confirm the need:

```text
WP_DUTCH_LEGAL_PARTY_NAME_PATTERN_REVIEW
WP_CARE_ROLE_PERSON_NAME_PATTERN_REVIEW
```

Important boundary:

```text
Do not implement recognizer changes directly from this review.
Add tests and contracts first.
No product claim.
No gate.
```

---

## 7. Threshold impact

Threshold impact:

```text
PERSON exact/text-normalized match should become high over time.
With 14 remaining PERSON misses, a hard PERSON threshold is too early.
First coverage review, then coverage tests, then recognizer/candidate planning.
```

Planning implication:

- `PERSON` should be tracked as a separate high-risk direct-identifier class.
- Any later threshold should be class-specific.
- Overlap-only matches should not be accepted as the main PERSON threshold.
- Single-surname cases may require a separate rule or review category.

---

## 8. Product-claim policy

Disallowed claims:

```text
Alle persoonsnamen worden altijd gevonden.
Alle persoonsgegevens worden altijd gevonden.
De app is veilig zonder menselijke review.
De benchmark bewijst production readiness.
```

Allowed wording:

```text
De diagnostische benchmark laat zien welke synthetische persoonsnamen nog gemist worden.
Deze analyse helpt vervolgtests en herkenningslogica te plannen.
Menselijke review blijft noodzakelijk.
```

---

## 9. Diagnostic tests

`WP_RECALL_PERSON_NAME_COVERAGE_TESTS` adds diagnostic tests for the gap inventory.

The tests do not require current recognizers to pass all PERSON examples.

The tests preserve the gap inventory and non-claim boundaries.

The tests are intentionally diagnostic: they keep the known PERSON-name risk visible without converting it into a CI gate, threshold enforcement or product claim.
