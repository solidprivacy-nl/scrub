# Zorgfilter v1 — gap triage

Status: completed triage direction; recognizer contracts not yet implemented  
Workpackage: `SCRUB-WP_CARE_PROFILE_GAP_TRIAGE`

## Purpose

Translate every result from the current-engine care baseline into an explicit implementation route. This prevents aggregate recall percentages from driving broad, unsafe pattern additions.

Source evidence:

```text
81 expectations
14 correct intended entities
11 exact spans found under the wrong entity
56 missed values
0 protected clinical phrase overlaps in the bounded custom-rule baseline
```

## Triage result

Every expectation is classified. No baseline item remains without a follow-up route.

| Route | Expectations | Meaning |
| --- | ---: | --- |
| Reuse current recognizer | 14 | Current exact entity behavior is suitable for Zorg profile composition. |
| Generic profile dependency | 13 | PERSON and e-mail depend on the generic local profile/NER layer excluded from this baseline. |
| Contextual care review recognizer | 36 | Provider, organization, location, room/bed and exact care-date values need context-bound review recognition. |
| Care-specific reclassification | 10 | The exact span is already found under a broad legal/healthcare entity but needs a care-specific entity and policy. |
| Dedicated care reference recognizer | 5 | The patient-specific administrative reference is currently absent. |
| Care collision guard | 3 | AGB requires explicit context and BSN/numeric collision prevention. |

## Route 1 — reuse existing Dutch identifiers

Reuse and regression-protect:

- address;
- BIG number;
- BSN;
- date of birth;
- Dutch telephone number.

The Zorg profile must include these existing entities without duplicating their recognizers.

## Route 2 — generic local profile dependency

The custom-rule baseline intentionally excluded generic NER. Therefore:

- unlabeled patient and relative names remain a generic `PERSON` responsibility;
- e-mail remains a generic Presidio/profile responsibility;
- these gaps must be measured in the later cross-profile matrix rather than solved with broad numeric or name regexes.

Context-labeled provider names are different: they need care-aware classification because their default policy is review-selected rather than replace-by-default.

## Route 3 — care-specific reference entities

The current broad `NL_HEALTHCARE_REFERENCE` or legal reference categories find several exact values, but cannot express the approved care policy.

Dedicated entities are required for:

- patient number;
- care client number;
- medical record number;
- EPD/ECD number;
- personal health-insurance number;
- referral number;
- treatment/care-trajectory reference;
- laboratory/sample number;
- care incident number;
- care indication/allocation reference.

Where a current broad recognizer already finds the exact value, implementation should split or reclassify based on strong care context rather than add a duplicate overlapping result.

## Route 4 — contextual review recognition

The largest gap is the review-selected layer: 36 expectations require context-bound recognition.

### Care-provider names

Recognize names following bounded roles such as:

- huisarts;
- behandelend arts;
- hoofd- or regiebehandelaar;
- verpleegkundige;
- verzorgende IG;
- persoonlijk begeleider;
- fysiotherapeut;
- psycholoog;
- apotheker;
- rapporteur or melder.

Return only the name. Preserve the professional role.

### Organizations and locations

Recognize bounded values after labels such as:

- zorgorganisatie;
- ziekenhuis;
- praktijk;
- apotheek;
- laboratorium;
- verzendende/ontvangende organisatie;
- locatie, woonlocatie, afdeling or team.

Do not blindly treat all organization names in narrative text as care organizations.

### Room and bed references

Use explicit context such as `kamer`, `appartement` and `bed`. Reject dosages, ages, dates, scores and laboratory numbers.

### Exact care-event dates

Classify labeled dates such as:

- admission and discharge dates;
- appointment and treatment dates;
- report and evaluation dates;
- incident and sample dates.

Keep date of birth in its existing replace-by-default entity. Care-event dates are review-selected.

## Route 5 — AGB and numeric collision prevention

AGB needs a separate context-bound recognizer and precedence rule.

Required safeguards:

- accept eight digits only after strong `AGB` context;
- do not accept an AGB-labeled value as BSN;
- do not infer AGB from an arbitrary eight-digit number;
- preserve vital signs, dosages, times, room values and laboratory results;
- make overlapping recognizer behavior deterministic.

The baseline finding `01020304 → NL_BSN` is an explicit regression case.

## Clinical-preservation contract

The recognizer contracts must include negative cases for:

- diagnoses and symptoms;
- medication names and dosages;
- administration times and schedules;
- laboratory results, units and reference ranges;
- blood pressure, pulse, temperature and saturation;
- observations, allergies, treatment and care goals;
- professional role words;
- clinical classification codes unless proven patient-specific.

Rare-case indirect identifiability stays in audit evidence. It is not a regex target in Zorgfilter v1.

## Contract package scope

The next workpackage must freeze tests before implementation for four families:

```text
1. Care-reference identifier contracts
2. Contextual care-review contracts
3. AGB/numeric collision and negative medical-number contracts
4. Clinical-context preservation contracts
```

Generic PERSON and e-mail profile behavior is tested later in cross-profile integration; it is not reimplemented in the care-recognizer module.

## Implementation boundaries

- use value-only spans;
- preserve labels, roles and clinical meaning;
- separate care modules from the legal taxonomy;
- no UI change before recognizer contracts and implementation are green;
- no export, Scrub Key or reinsert semantic change;
- synthetic data only;
- human review remains mandatory;
- production readiness remains false.
