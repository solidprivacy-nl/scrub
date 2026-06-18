# PERSON-name recognizer contract tests

Workpackage: `WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS`

Repository: `solidprivacy-nl/scrub`

Status: tests/specification-only.

This document describes contract-only tests for safe future PERSON-name recognition. These tests specify future desired behavior; they do not implement a recognizer and do not change product behavior.

---

## 1. Purpose

Purpose:

```text
Define safe future PERSON-name recognizer behavior as contract data and tests before any implementation package is allowed to change recognition logic.
```

The fixture status is:

```text
contract_only
```

---

## 2. Non-goals

```text
No product code.
No recognizer implementation.
No candidate scanner implementation.
No runner/report changes.
No workflow changes.
No UI changes.
No export changes.
No Scrub Key changes.
No reinsert changes.
No threshold enforcement.
No production gate.
No product claim.
```

---

## 3. Fixture overview

Contract fixture:

```text
tests/fixtures/person_name_recognizer_contract_cases.json
```

Metadata:

```text
status = contract_only
synthetic = true
product_gate = false
thresholds_enforced = false
product_claim = false
```

Fixture groups:

```text
positive_cases
candidate_only_cases
negative_cases
preserve_terms
```

The tests validate fixture completeness and safety boundaries only. They do not run the current recognizers against these cases.

---

## 4. Positive case policy

Positive cases describe future hard-recognizer behavior for strong role/title context.

Examples include:

```text
arts Bakker
getuige Fatima El Amrani
cliënt Youssef Ait Ben
verpleegkundige Sara El Idrissi
mantelzorger Fatima Zahra
mr. Lina de Vries
mr. Noor van Dijk
```

Policy:

```text
role/title/context words must remain readable
expected_sensitive_value must contain only the name value
expected_sensitive_value must not equal the full sentence
future mode is hard_recognizer_future
```

Example expected behavior:

```text
Later noteerde arts Bakker dat de cliënt stabiel was.
```

Future sensitive span:

```text
Bakker
```

Preserved context:

```text
arts
cliënt
```

---

## 5. Candidate-only policy

Candidate-only cases describe weaker contexts that may be useful to surface for review later, but should not be automatically applied.

Examples include:

```text
Hassan El Amrani en Mila van Dijk near contact data
Omar Ben Salah near email
Nora El Yassini and Tariq de Jong near legal reference
Sami El Amrani near phone number
```

Policy:

```text
mode = candidate_only_future
review_required = true
automatic_replacement_allowed = false
review table remains source of truth
```

These cases may later support a candidate/audit layer, not automatic replacement.

---

## 6. Negative case policy

Negative cases prevent broad over-masking.

Examples include:

```text
Rechtbank Den Haag
Hof van Discipline
Afdeling Rozenhof 3
Parklaan 188
artikel 7:669 BW
productie 3
bijlage 2
```

Policy:

```text
mode = must_not_match_person
expected_sensitive_value = null
```

Purpose:

```text
Prevent future recognizer work from turning courts, locations, addresses, legal articles or document-navigation references into PERSON matches.
```

---

## 7. Single-surname policy

Single surnames are high ambiguity.

Explicit examples:

```text
Bakker
Jansen
```

Policy:

```text
single surname with strong role/title context may be a future hard-recognizer or candidate-only case
single surname without strong role/title context must_not_match_person
broad capitalization-based matching is not allowed
```

A later implementation package must prove with contract tests that single-surname handling does not over-mask ordinary words.

---

## 8. Preserve-term policy

Required preserve terms:

```text
cliënt
slachtoffer
minderjarige
arts
getuige
eiser
verweerder
verpleegkundige
zorgmedewerker
behandelaar
mantelzorger
mr.
```

Policy:

```text
role/context words remain readable
a future recognizer should return only the sensitive name value
legal/care meaning must not be merged into the name span
```

---

## 9. No product claim

Disallowed claims:

```text
Alle persoonsnamen worden altijd gevonden.
Alle persoonsgegevens worden altijd gevonden.
De app is veilig zonder menselijke review.
De benchmark bewijst production readiness.
```

Allowed wording:

```text
These contract tests specify future safe behavior for synthetic PERSON-name examples.
They do not prove production readiness.
Human review remains necessary.
```

---

## 10. No threshold or gate

Current status:

```text
No threshold enforcement.
No production gate.
No product claim.
No CI recall/precision gate.
```

The contract tests are normal tests for fixture/specification validity. They do not evaluate recall/precision thresholds and do not require the current recognizers to pass all future PERSON-name cases.

---

## 11. Next implementation route

Recommended next package after separate approval:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY
```

Implementation boundary for that future package:

```text
must satisfy the contract fixture
must preserve role/context terms
must avoid broad capitalization matching
must keep weak contexts candidate-only unless separately approved
must run benchmark review after implementation
```

A later implementation package must build against these contracts and then run a benchmark artifact review before any threshold/gate discussion resumes.
