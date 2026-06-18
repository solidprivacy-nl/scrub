# PERSON-name recognizer improvement plan

Workpackage: `WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN`

Repository: `solidprivacy-nl/scrub`

Status: planning/specification-only.

This document plans a safe route for future `PERSON`-name recognition improvements. It is not an implementation package.

---

## 1. Goal and non-goals

Goal:

```text
Define a safe, test-first strategy for improving PERSON-name recognition while preserving legal/care meaning and avoiding over-masking.
```

Non-goals:

```text
This is a recognizer plan.
This is not an implementation.
This does not change product behavior.
This does not change recognizers.
This does not change the candidate scanner.
This does not change runner/report behavior.
This does not create a threshold.
This does not create a gate.
This does not prove product safety.
```

---

## 2. Current PERSON gaps

The remaining `PERSON` gaps were classified in `RECALL_PERSON_NAME_COVERAGE_REVIEW.md` and preserved in `tests/test_recall_person_name_coverage_diagnostics.py`.

Main name/context types:

```text
Arabic/Moroccan-style multi-token names
Dutch names with tussenvoegsel
first name + surname
single surname
professional title + name
care role + name
legal role + name
name near phone/email/address
name near client/care/legal reference
```

Relevant synthetic examples:

```text
Hassan El Amrani
Mila van Dijk
Ahmed El Idrissi
Bakker
Sara El Idrissi
Youssef Ait Ben
Fatima Zahra
Lina de Vries
Omar Ben Salah
Nora El Yassini
Tariq de Jong
Noor van Dijk
Sami El Amrani
Jansen
Fatima El Amrani
```

Current diagnosis:

- Most remaining misses look like recognition coverage/design issues, not benchmark mapping noise.
- Single-surname cases are high ambiguity.
- Care/legal role words must remain readable.
- Names near contact/reference data may be useful as review candidates, but should not be automatically applied without review.

---

## 3. Design principles

Required principles:

```text
mask sensitive name values, not legal/care role meaning
preserve role/context words
avoid broad capitalization-based matching
avoid masking generic words as PERSON
single-surname handling requires strong context
all rules must be synthetic-test driven
human review remains necessary
```

Role/context words that must remain readable include:

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
```

Implementation implication:

```text
A future recognizer must return only the name value span, never the role/context word, unless a later approved spec explicitly changes that boundary.
```

---

## 4. Possible recognition strategies

### Option A — Context-bound role/title + name recognizer

Pattern family:

```text
arts <Achternaam>
getuige <Voornaam Achternaam>
cliënt <Voornaam Achternaam>
verpleegkundige <Voornaam Achternaam>
mantelzorger <Voornaam Achternaam>
mr. <Voornaam Achternaam>
```

Required behavior:

```text
role/title word remains readable
only name value becomes PERSON/NL_LEGAL_PARTY_NAME candidate
spans do not cross sentence or line boundaries
```

Possible output class:

```text
NL_LEGAL_PARTY_NAME or a future explicit PERSON-name candidate type, mapped to PERSON in benchmark only after approval.
```

Benefits:

- Strong context lowers false positives.
- Supports legal/care role-name cases directly.
- Preserves legal/care meaning if value-only spans are enforced.
- Good first implementation candidate after contract tests.

Risks:

- Single-surname cases can still over-match ordinary capitalized words.
- Role vocabulary expansion can accidentally include generic context terms.
- `mr.` title handling may confuse professional title with abbreviation punctuation.
- If regex is too broad, it may cross sentence boundaries or absorb contact/reference text.

Required tests before implementation:

- `arts Bakker` returns only `Bakker`.
- `getuige Fatima El Amrani` returns only `Fatima El Amrani`.
- `verpleegkundige Sara El Idrissi` returns only `Sara El Idrissi`.
- `cliënt Youssef Ait Ben` returns only `Youssef Ait Ben`.
- `mr. Noor van Dijk` returns only `Noor van Dijk`.
- Role words themselves remain unmasked/preserve terms.
- Normal role-only mentions do not match.

Planning recommendation:

```text
Option A is the safest first recognizer route, but only after contract tests.
```

### Option B — Multi-token Dutch/Moroccan name candidate recognizer

Pattern family may include name particles:

```text
El
Al
Ait
Ben
van
de
der
den
```

When it may be safe:

- multi-token name-like phrase is in a legal/care sentence;
- adjacent sentence has contact/reference context;
- phrase appears after a role/title cue;
- phrase appears in a known person-name test fixture;
- result is candidate-only if context is weaker.

Why broad matching is dangerous:

- many Dutch particles are ordinary words;
- capitalized words can be organizations, court names, section titles, months or sentence starts;
- Moroccan/Arabic-style particles can appear in organizations or locations;
- broad matching can damage legal/care meaning by masking non-person text.

Possible false positives:

```text
Rechtbank Den Haag
Hof van Discipline
Afdeling Rozenhof
Artikel De ...
Parklaan 188
```

Required context:

- role/title cue; or
- nearby contact cue; or
- nearby client/legal/care reference; or
- strong multi-token name grammar plus negative checks for courts/addresses/organizations.

Planning recommendation:

```text
Option B should initially be candidate-only unless strong role/title context exists.
```

### Option C — Name-near-contact/reference candidate

Pattern family:

```text
name in same sentence as phone/email/address
name in same sentence as client number/case number/dossier number
name near care/legal reference values
```

Likely behavior:

```text
candidate-only
not automatically applied
review table remains source of truth
serial review may surface the candidate later
```

Benefits:

- Directly targets missed names near already-detected contact/reference values.
- Reduces false-negative review risk without automatic masking.
- Fits the existing human-review workflow.

Risks:

- Can increase review load.
- Nearby capitalized phrases may be organizations or locations.
- Context windows can cross sentence boundaries if not carefully bounded.

Required tests before implementation:

- name near email/phone becomes a candidate.
- address/court/organization near email/phone does not become PERSON.
- candidate span is only the name, not contact data.
- no automatic inclusion without review.

Planning recommendation:

```text
Option C is suitable for a candidate/audit layer, not as automatic replacement logic.
```

---

## 5. Single-surname policy

Relevant examples:

```text
Bakker
Jansen
```

Policy:

```text
single surnames are highly ambiguous
never broadly match capitalized words as PERSON
only consider single surnames with strong context such as arts <Achternaam> or getuige <Achternaam>
prefer candidate-only when ambiguity remains
```

Hard constraints:

- The role word must remain readable.
- Single surname matching must not trigger on sentence-start words.
- Single surname matching must not trigger on generic organization/court/location words.
- Strong context must be within a small, bounded window.

Recommended first stance:

```text
single surname after strong role/title context may become a candidate first, not a hard automatic recognizer, unless contract tests prove low false-positive risk.
```

---

## 6. Contract-test plan before implementation

No test files are added in this workpackage. The next package should be:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS
```

Required future test categories:

```text
care role + name value only
legal role + name value only
professional title + name
Dutch tussenvoegsel names
Moroccan/Arabic-style multi-token names
single surname with strong context
single surname without strong context should not match
role words should not be masked
known trap normal capitalized words should not match
name near phone/email should become candidate
```

Minimum contract tests:

- `arts Bakker` → only `Bakker`, not `arts`.
- `getuige Fatima El Amrani` → only name value.
- `cliënt Youssef Ait Ben` → only name value.
- `verpleegkundige Sara El Idrissi` → only name value.
- `mr. Lina de Vries` → only name value.
- `Bakker` alone in normal sentence → no match or candidate-only, depending on approved policy.
- `Rechtbank Den Haag` → not `PERSON`.
- `afdeling Rozenhof 3` → not `PERSON`.
- `Parklaan 188` → not `PERSON`.
- role/context terms remain preserve terms.

Contract tests should fail against an over-broad capitalization-based recognizer.

---

## 7. Output behavior and review boundary

Future desired output behavior:

```text
hard recognizer match for clear role/title + full-name cases
candidate-only for weaker context
no automatic replacement without review
review table remains source of truth
serial review may show PERSON candidates later
```

Strict current boundaries:

```text
no current UI change
no current replacement-flow change
no current export change
no Scrub Key change
no reinsert change
no threshold or gate
```

Future implementation should keep separate:

- recognizer output;
- candidate/audit output;
- user inclusion decision;
- export behavior.

---

## 8. Risk analysis

False negatives:

```text
PERSON names remain visible in scrubbed output.
```

False positives:

```text
ordinary capitalized words, court names, organizations, locations or role words are masked as PERSON.
```

Legal meaning damage:

```text
role words such as eiser, verweerder, slachtoffer, getuige or minderjarige disappear or are merged into a name span.
```

Care meaning damage:

```text
care roles such as arts, verpleegkundige, mantelzorger, zorgmedewerker or behandelaar disappear or are merged into a name span.
```

Review load:

```text
too many weak candidates can make review slower and reduce trust.
```

Bias/coverage risk:

```text
Dutch names are detected while Moroccan/Arabic-style names remain missed, or vice versa.
```

Mitigation strategy:

- contract tests before implementation;
- value-only span rules;
- candidate-only mode for weak contexts;
- explicit known-trap tests;
- no product claim;
- human review remains required.

---

## 9. Recommended implementation route

Recommended order:

```text
1. WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS
2. WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY
3. WP_RECALL_PERSON_NAME_RECOGNIZER_BENCHMARK_REVIEW
4. WP_RECALL_PERSON_NAME_RECOGNIZER_APP_VERIFICATION_CLOSEOUT, only if product behavior/UI later changes
```

Strict sequencing:

```text
first contract tests
then helper/recognizer implementation
then artifact review
then only later threshold reconsideration
```

Implementation boundary for later package:

- keep implementation small;
- prefer helper/recognizer tests before app changes;
- avoid broad capitalization matching;
- preserve role words;
- use synthetic data only;
- do not introduce cloud processing;
- do not change export or Scrub Key semantics.

---

## 10. Product-claim policy

Disallowed claims:

```text
Alle persoonsnamen worden altijd gevonden.
Alle persoonsgegevens worden altijd gevonden.
De app is veilig zonder menselijke review.
De benchmark bewijst production readiness.
```

Allowed wording:

```text
De PERSON-name recognizer planning beschrijft hoe synthetische naamgaps veilig kunnen worden aangepakt.
Menselijke review blijft noodzakelijk.
```

---

## 11. Decision summary

Decision:

```text
PERSON-name improvement will proceed test-first.
```

Reason:

```text
Single-surname and role/context cases are high-risk for over-masking and legal/care meaning damage.
```

Consequence:

```text
Contract tests are required before recognizer implementation.
```
