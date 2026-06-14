# WP_REPLACE_LOGIC_UI_REDESIGN_PLAN — Intuitive replacement review flow

Status: planning/design/documentation-only  
Repository: `solidprivacy-nl/scrub`

## 1. Executive summary

The previous replacement decision helper panel is product-rejected as a normal user-facing feature. It worked technically, but it exposed helper/audit internals and made the review flow feel more complex.

The redesign direction is:

```text
one found item -> context -> suggested replacement -> one simple choice -> optional exact-same scope -> existing table remains fallback
```

The user should not see replacement-decision internals as the main interface. The review flow should feel like reviewing a document, not operating a helper model.

The first redesigned UI, if later approved, should be a small task-focused control area inside or near the existing serial review context. It should use four visible choices:

```text
Vervangen
Zichtbaar houden
Aanpassen
Later controleren
```

Only when relevant, show scope:

```text
Alleen deze plek
Alle exact dezelfde waarden
```

The review table remains the source of truth and fallback. This plan does not implement UI and does not change product code.

## 2. Why the previous panel failed

The previous replacement decision helper panel failed product-wise for these reasons:

1. It showed helper/audit structure instead of a user task.
2. It used terms like decision state, scope, affected count, mapping candidates and export readiness in the main surface.
3. It made the user think about implementation mechanics before answering the real question: “what should happen with this found value?”
4. It competed visually with the existing review table and serial review panel.
5. It created an extra layer instead of reducing cognitive load.
6. It exposed staged/applied safety language as interface content instead of keeping it as an implementation boundary.
7. It did not feel natural for legal users who want to preserve meaning and quickly decide whether a value should be replaced.

Technical helper assets remain useful, but helper internals must not become the normal user-facing panel.

## 3. User task model

The real user task is not “create a ReplacementDecision”.

The real task is:

```text
For this detected value, decide whether it should be replaced, kept visible, adjusted, or reviewed later.
```

The user needs to answer only four practical questions:

1. What value did Scrub find?
2. Is the context enough to understand it?
3. Is the proposed replacement correct?
4. Should this decision apply only here or to exact same values too?

The UI should optimize for that task and hide everything else unless the user asks for details.

## 4. Proposed simple interaction model

### 4.1 Primary interaction

For the current item, show:

```text
Gevonden waarde
Context
Voorgestelde vervanging
Keuze
Bereik, alleen als relevant
```

Primary choice buttons:

| Label | User meaning | Helper concept behind the scenes |
|---|---|---|
| Vervangen | Use the suggested replacement. | `accepted` |
| Zichtbaar houden | Do not replace this value. | `ignored` |
| Aanpassen | Change the proposed replacement. | `edited` |
| Later controleren | Leave it unresolved for now. | `unresolved` |

The UI should not present helper names (`accepted`, `ignored`, `edited`, `unresolved`) as main labels.

### 4.2 Optional edit

When the user chooses `Aanpassen`, show one small text input:

```text
Vervangen door
```

Do not show advanced fields by default.

### 4.3 Optional scope

Only show scope when the choice can logically apply beyond one occurrence.

Allowed first scopes:

| Label | Meaning |
|---|---|
| Alleen deze plek | Apply this review choice only to the current occurrence. |
| Alle exact dezelfde waarden | Apply to exact same values only, after showing the count. |

Do not expose `all_normalized` in the first redesigned UI. It is too technical and too easy to misunderstand.

### 4.4 Confirmation language

For exact same values, use plain language:

```text
Deze waarde komt 3 keer exact hetzelfde voor.
Wil je dezelfde keuze ook daar gebruiken?
```

Avoid technical wording:

```text
apply_to_same_value_actions
all_exact
matching_occurrence_ids
```

Those remain internal concepts.

## 5. Placement in current Scrub Legal flow

Recommended placement:

```text
1. Review guidance
2. Existing review table
3. Serial review / current item context
4. Simple replacement choice strip for the current item
5. Preview text / highlight toggle
6. Existing export/download area
```

The current product already has:

- review table as source of truth;
- serial review panel as guided one-by-one review aid;
- context preview / context card data;
- optional visual highlight toggle for already masked/replaced values;
- export based on the checked replacement table.

The redesigned replacement flow should attach to the serial review current item, not as a separate helper/audit panel.

## 6. Relationship to existing surfaces

### 6.1 Review table

The review table remains source of truth and fallback.

The redesigned flow may eventually help set or explain table choices, but not in the first planning package and not without separate implementation approval.

First implementation candidate should be either:

```text
read-only design prototype
```

or a very small controlled UI that clearly does not change the table unless a later package explicitly allows it.

### 6.2 Serial review

Serial review is the best placement because it already shows one item at a time.

Serial review remains:

```text
guided review layer, not replacement for the table
```

The redesigned replacement controls should feel like the natural next step below the current item:

```text
Gevonden waarde -> Context -> Voorgestelde vervanging -> Wat wil je doen?
```

### 6.3 Context preview

Context preview is essential. Replacement choice without context creates wrong decisions.

The redesigned flow should always keep the value and local context close to the choice buttons.

### 6.4 Highlight toggle

The highlight toggle is a visual aid only.

It may help users see where already-replaced values appear in preview text, but it must not become a marking mechanism.

Product principle:

```text
Markeringen zijn visuele hulp, geen mutation mechanism.
```

### 6.5 Scrub Key

This flow must not write Scrub Key mappings.

Scrub Key behavior stays separate until a dedicated package approves writes/schema/lifecycle changes.

The UI may later say, in a non-technical way:

```text
Deze vervanging kan later worden gebruikt voor terugzetten.
```

But it must not expose `creates_mapping` or `mapping_candidates` as main UI concepts.

### 6.6 Export

Export remains based on the checked replacement table.

The redesigned flow must not block export or alter download payloads without a separate approved package.

Do not show `export_readiness` internals as a main UI field. A later user-facing warning may simply say:

```text
Er staan nog items open voor controle.
```

### 6.7 Reinsert

Reinsert behavior is unchanged.

Replacement review choices must not change original-value reinsert behavior in this phase.

## 7. UI copy / Dutch labels

### 7.1 Section title

Recommended title:

```text
Controleer deze waarde
```

Avoid:

```text
Replacement decision helper
Decision state
Audit fields
Mapping candidates
Export readiness
```

### 7.2 Current item labels

```text
Gevonden waarde
Context
Voorgestelde vervanging
Wat wil je doen?
```

### 7.3 Action labels

```text
Vervangen
Zichtbaar houden
Aanpassen
Later controleren
```

Optional extra later, not first implementation default:

```text
Als context behouden
```

Use `Als context behouden` only if users clearly understand it. Otherwise merge it into `Zichtbaar houden` plus explanatory copy.

### 7.4 Scope labels

```text
Alleen deze plek
Alle exact dezelfde waarden
```

Do not show:

```text
Alle genormaliseerde gelijke waarden
```

in the first redesigned UI.

### 7.5 Plain-language explanations

For `Vervangen`:

```text
Gebruik de voorgestelde vervanging voor deze waarde.
```

For `Zichtbaar houden`:

```text
Laat deze waarde zichtbaar in de tekst.
```

For `Aanpassen`:

```text
Pas de vervanging aan voordat je verdergaat.
```

For `Later controleren`:

```text
Laat dit item openstaan voor latere controle.
```

For table fallback:

```text
De vervangtabel blijft leidend. Controleer bij twijfel de tabel hieronder.
```

For exact same value:

```text
Deze waarde komt vaker exact hetzelfde voor. Je kunt dezelfde keuze ook daar gebruiken.
```

## 8. Safe first implementation candidate

The safest next implementation path is not direct implementation.

Next package should be:

```text
WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS
```

That package should test the redesign plan and prevent regression toward the old helper/audit panel.

Only after that, and only after separate coordinator approval, consider:

```text
WP_REPLACE_LOGIC_UI_REDESIGNED_IMPLEMENTATION
```

The first implementation should be small and should probably start as:

```text
simple current-item action strip in the serial review area
```

It should not reintroduce `replacement_decision_panel_ui.py` as the normal user-facing panel.

## 9. Explicitly blocked behavior

This redesign plan does not approve:

- Streamlit UI implementation;
- changes to `presidio_streamlit.py`;
- changes to `serial_review_panel_ui.py`;
- changes to `replacement_decision_panel_ui.py`;
- review table behavior changes;
- mutating replacement decisions;
- automatic replacement;
- Scrub Key writes;
- Scrub Key schema changes;
- export blocking;
- export/download behavior changes;
- reinsert behavior changes;
- click-to-mark;
- advanced editor;
- full-document marking;
- dependency changes;
- cloud processing;
- real-data fixtures;
- fuzzy matching;
- guessed intent;
- `all_normalized` as a first user-facing scope;
- exposing helper/audit internals as the main UI.

## 10. Contract test requirements

`WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS` should verify at minimum:

1. `REPLACE_LOGIC_UI_REDESIGN_PLAN.md` exists.
2. The plan says the old helper panel must not return as normal user-facing UI.
3. The plan includes the four primary actions:
   - `Vervangen`;
   - `Zichtbaar houden`;
   - `Aanpassen`;
   - `Later controleren`.
4. The plan includes only first-phase scopes:
   - `Alleen deze plek`;
   - `Alle exact dezelfde waarden`.
5. The plan excludes `all_normalized` from first user-facing scope.
6. The plan says review table remains source of truth and fallback.
7. The plan says serial review is a guided review layer, not replacement of the table.
8. The plan says highlight markers are visual aid only, not mutation mechanism.
9. The plan blocks Scrub Key writes.
10. The plan blocks export blocking and export/download behavior changes.
11. The plan blocks reinsert behavior changes.
12. The plan blocks automatic or guessed replacement.
13. The plan blocks fuzzy matching.
14. The plan blocks click-to-mark, advanced editor and full-document marking.
15. The plan requires separate coordinator approval before implementation.
16. The plan uses user-facing Dutch copy instead of helper/audit terms as the main UI.
17. The plan states that technical details may only live in a compact details section.
18. Existing tests should continue to ensure `replacement_decision_panel_ui.py` is not rendered in the normal flow.

## 11. Product principles

The redesign is governed by these product principles:

```text
The review table remains source of truth.
Serial review is a guided review layer, not a replacement of the table.
Markeringen zijn visuele hulp, geen mutation mechanism.
Replacement logic must be task-oriented, not helper-oriented.
Helper internals must not be shown as the main UI.
Scrub Key is not written from this flow without a separate package.
Export is not blocked from this flow without a separate package.
Reinsert is not changed from this flow.
No automatic or guessed replacement.
No fuzzy matching.
No click-to-mark in this phase.
```

## 12. Next recommended implementation package

Next package:

```text
WP_REPLACE_LOGIC_UI_REDESIGN_CONTRACT_TESTS
```

After that, only with separate coordinator approval:

```text
WP_REPLACE_LOGIC_UI_REDESIGNED_IMPLEMENTATION
```

Do not start automatically:

- new replacement UI implementation;
- mutating replacement decisions;
- automatic replacement;
- Scrub Key writes;
- export blocking;
- click-to-mark;
- advanced editor;
- full-document marking.
