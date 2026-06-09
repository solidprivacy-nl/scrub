# WP31 — LLM-resistant placeholder format proposal

Status: completed architecture/proposal-only.  
Repository: `solidprivacy-nl/scrub`.

Scope: placeholder-format proposal only. No placeholder migration, no reinsert helper change, no Scrub Key schema change, no UI change, no export behavior change, no tests, no AI/cloud integration and no dependency changes.

---

## 1. Purpose

WP31 proposes and compares placeholder formats that are more resistant to AI rewriting, translation, summarization, copy/paste, markdown/HTML conversion and document-format conversion.

This proposal follows `PLACEHOLDER_ROBUSTNESS_REVIEW.md` from WP30.

The current deterministic reinsert design remains unchanged:

```text
placeholder in text + matching Scrub Key item → exact deterministic replacement
```

This document does not implement or mandate migration. It defines a recommended architecture direction for later workpackages.

---

## 2. Current placeholder limitations

The current placeholder format is compact and readable:

```text
[PERSOON_1]
[ZAAKNUMMER_1]
[ADRES_1]
[ORGANISATIE_01]
```

Current recognizer direction in the reinsert helper is based on a single-bracket pattern like:

```text
\[[A-Z][A-Z0-9_:-]*_[0-9]+\]
```

Current strengths:

- short;
- readable for Dutch users;
- easy to insert in documents;
- easy to replace exactly;
- already supported by existing Scrub Key and reinsert tests.

Current limitations:

- labels are language-like and may be translated by an LLM, for example `[PERSOON_1]` → `[PERSON_1]`;
- single square brackets are common in ordinary writing, markdown links and legal annotations;
- sequence numbers are not zero-padded, making sort and visual comparison less stable;
- no explicit product prefix identifies the token as a SolidPrivacy control token;
- no integrity token exists to detect typo, invention or corruption;
- small spacing/casing changes break deterministic reinsert;
- summarization can delete or merge placeholders silently;
- markdown/HTML/DOCX conversion may split the visible token across markup or runs;
- current format cannot distinguish legacy limitations from robust-format validation failures.

The core problem is not only failed replacement. The dangerous case is silent partial restoration, where some placeholders restore but others are missing, merged, translated or corrupted.

---

## 3. Candidate formats compared

WP31 compares four required candidate styles:

```text
[PERSOON_1]
[[SP_PERSON_0001_A7F3]]
{{SP:PERSON:0001:A7F3}}
⟦SP_PERSON_0001_A7F3⟧
```

### 3.1 Candidate A — legacy Dutch placeholder

Example:

```text
[PERSOON_1]
```

Shape:

```text
[ENTITY_COUNTER]
```

Strengths:

- already implemented;
- short and readable;
- fits existing Scrub Key items;
- works in TXT and simple DOCX body text when not split across runs;
- no migration needed for current documents.

Weaknesses:

- language-specific label may be translated;
- no SolidPrivacy prefix;
- no integrity token;
- single brackets are less distinctive;
- does not help detect invented placeholder-like tokens;
- zero-padding is inconsistent;
- weak for LLM roundtrip robustness.

Recommendation:

```text
Keep as legacy-supported format only. Do not use as the recommended future robust format.
```

---

### 3.2 Candidate B — double-square SolidPrivacy token

Example:

```text
[[SP_PERSON_0001_A7F3]]
```

Shape:

```text
[[SP_ENTITY_0001_INTEGRITY]]
```

Strengths:

- visually distinct;
- `SP` prefix marks it as a SolidPrivacy control token;
- ASCII-only;
- stable technical entity code reduces translation risk;
- zero-padded counter improves ordering and readability;
- short uppercase integrity token can support future validation;
- easy to detect with a strict regex;
- plain-text friendly;
- copy/paste friendly;
- likely to survive common AI rewriting better than the legacy format if prompt instructions say to preserve tokens exactly;
- avoids uncommon Unicode brackets;
- simpler than colon-delimited braces in many markdown contexts.

Weaknesses:

- double square brackets can occur in wiki-style links, though less commonly in legal/care text;
- longer than current placeholders;
- still can be split by DOCX runs or markdown/HTML formatting;
- checksum/integrity semantics require a future WP32 helper and possibly later Scrub Key metadata;
- not currently implemented.

Recommendation:

```text
Recommended future robust placeholder format direction.
```

---

### 3.3 Candidate C — double-curly colon-delimited token

Example:

```text
{{SP:PERSON:0001:A7F3}}
```

Shape:

```text
{{SP:ENTITY:COUNTER:INTEGRITY}}
```

Strengths:

- visually distinct;
- explicit field separators;
- common enough in templating contexts for humans to recognize as a token;
- `SP` prefix and technical entity code reduce translation risk;
- easy to parse by splitting on `:`.

Weaknesses:

- curly braces are common in templates, JSON-like examples and some document automation systems;
- colons can be visually noisy in legal/care text;
- more likely to be treated by some systems as template syntax;
- copy/paste into systems with templating semantics could create confusion;
- not clearly better than double-square in TXT/DOCX/PDF extraction.

Recommendation:

```text
Keep as a secondary alternative, not the primary recommendation.
```

---

### 3.4 Candidate D — Unicode bracket token

Example:

```text
⟦SP_PERSON_0001_A7F3⟧
```

Shape:

```text
⟦SP_ENTITY_COUNTER_INTEGRITY⟧
```

Strengths:

- very visually distinctive;
- unlikely to collide with normal text;
- clearly marks the token as special.

Weaknesses:

- Unicode brackets may be normalized, lost, substituted or unsupported in some systems;
- harder to type manually;
- may break in legacy encodings or copy/paste flows;
- PDF text extraction may normalize or omit the bracket glyphs;
- some LLMs or editors may replace them with ordinary brackets;
- less friendly for CLI, logs, JSON and basic text tooling.

Recommendation:

```text
Do not use as the main product format. The visual distinctiveness is useful, but compatibility risk is too high.
```

---

## 4. Recommended candidate format

Recommended architecture direction:

```text
[[SP_PERSON_0001_A7F3]]
```

General shape:

```text
[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]
```

Example set:

```text
[[SP_PERSON_0001_A7F3]]
[[SP_CASE_NUMBER_0002_C91B]]
[[SP_ADDRESS_0003_D41A]]
[[SP_BSN_0004_8E2C]]
[[SP_CARE_REF_0005_F0A9]]
```

Proposed strict detection regex for a future helper:

```text
\[\[SP_[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*_[0-9]{4}_[A-F0-9]{4}\]\]
```

This regex is proposal-only. It must not be added to `scrub_key_reinsert.py` in WP31.

Why this candidate is recommended:

- stable technical prefix reduces translation risk;
- double brackets are visually distinct but remain ASCII-compatible;
- underscores are robust in plain text and common developer tooling;
- zero-padded counter is readable and sortable;
- integrity token creates a clear path for WP32 validation;
- the shape remains easy to explain in audit output;
- it is more compatible with TXT/DOCX/PDF extraction than Unicode brackets;
- it is less likely than curly braces to be confused with template syntax.

---

## 5. Entity naming convention

Entity names should be stable technical codes, not user-facing Dutch labels.

Recommended rules:

1. Use uppercase ASCII only.
2. Use English or stable domain-neutral technical names, not translatable UI labels.
3. Use underscores between words.
4. Avoid accents, spaces, hyphens and punctuation.
5. Keep the code descriptive but not too long.
6. Keep user-facing Dutch labels separate in the Scrub Key `type_label` field.
7. Do not encode sensitive values or legal meaning into the entity name.

Recommended examples:

| Concept | Recommended entity code | Avoid |
| --- | --- | --- |
| Person/name | `PERSON` | `PERSOON`, `NAAM`, `CLIENT_JAN` |
| Address | `ADDRESS` | `ADRES`, `HOME_ADDRESS_OF_CLIENT` |
| BSN | `BSN` | `BURGERSERVICENUMMER_123` |
| Phone | `PHONE` | `TELEFOON`, `MOBILE_OF_CLIENT` |
| E-mail | `EMAIL` | `E_MAIL_ADRES` |
| Case number | `CASE_NUMBER` | `ZAAKNUMMER`, `ROLNUMMER_CASE_X` |
| Dossier number | `DOSSIER_NUMBER` | `DOSSIERNUMMER` |
| Client number | `CLIENT_NUMBER` | `CLIËNTNUMMER` |
| Claim number | `CLAIM_NUMBER` | `CLAIMREFERENTIE` |
| Incident number | `INCIDENT_NUMBER` | `INCIDENTNUMMER` |
| Care reference | `CARE_REF` | `ZORGREFERENTIE` |
| Organization | `ORGANIZATION` | `ORGANISATIE` |
| Date | `DATE` | `GEBOORTEDATUM` when a more specific classification is not needed |

Entity naming should align with future benchmark class mapping where possible, but does not have to expose benchmark terminology to users.

---

## 6. Counter format

Recommended counter format:

```text
0001
0002
0003
...
9999
```

Rules:

- Use four digits, zero-padded.
- Start at `0001` per Scrub Key/document generation context.
- Counters are identifiers, not quantities.
- Do not encode original value order if that order itself would reveal sensitive meaning beyond normal document order.
- Do not reuse the same full placeholder for different original values in one Scrub Key.
- Repeated occurrences of the same placeholder in the output text remain allowed when they represent the same original value.

Open future question:

```text
Should counters be per entity class or global per document/key?
```

WP31 recommendation:

```text
Use a global per-key counter in the future robust format unless a later implementation design proves per-entity counters are safer or clearer.
```

Reason:

- global counters reduce ambiguity;
- every placeholder becomes unique without relying on entity class;
- audit reports can count expected/observed placeholders more simply.

---

## 7. Checksum or integrity token direction

Recommended integrity token format:

```text
A7F3
```

Rules:

- four uppercase hexadecimal characters for the visible token in the first proposal;
- enough for typo/corruption detection, not enough for cryptographic authenticity by itself;
- generated from non-sensitive placeholder metadata or a random per-item nonce stored in the Scrub Key in a later approved design;
- validated by a future WP32 helper before reinsert/export of restored output.

Clear safety warning:

```text
Do not derive visible checksum/integrity values directly from original sensitive data.
```

Reason:

A visible integrity token derived directly from a name, BSN, address or case number could leak information or create a value that supports guessing attacks. The integrity token should prove that the placeholder is one issued by Scrub, not encode the original value.

Possible future approaches for WP32:

1. **Simple visible checksum over placeholder metadata only**
   - Detects typos and formatting corruption.
   - Does not prove authenticity.
   - Lowest complexity.

2. **Checksum over a non-sensitive item id and per-key nonce**
   - Better at detecting invented placeholders.
   - Requires storing non-sensitive nonce/id metadata in the Scrub Key.
   - Requires schema planning.

3. **HMAC-like integrity token**
   - Stronger authenticity.
   - Requires key material or a per-key secret.
   - Should be coordinated with WP26/WP29 because it overlaps with Scrub Key protection and tamper detection.

WP31 recommendation:

```text
WP32 should start with validation semantics and test vectors before choosing cryptographic strength. The first implementation may use a non-sensitive metadata checksum for corruption detection, while leaving stronger authenticity for Scrub Key security work.
```

---

## 8. Human readability

The recommended format is longer than the legacy placeholder, but still readable:

```text
[[SP_PERSON_0001_A7F3]]
```

Human-readable parts:

- `SP` tells the user this is a SolidPrivacy token.
- `PERSON` tells the rough entity class.
- `0001` gives a stable identifier.
- `A7F3` shows that the token has an integrity component.

User-facing explanations should avoid technical overload. Suggested future UI wording:

```text
Laat tokens zoals [[SP_PERSON_0001_A7F3]] exact staan. Verander, vertaal of verwijder deze tokens niet. Ze zijn nodig om originele waarden later lokaal terug te zetten met de Scrub Key.
```

Readability trade-off:

- More robust placeholders are less natural in a legal/care document.
- That is acceptable because placeholders are control tokens, not final prose.
- Legal/care meaning should remain in surrounding words, not in the placeholder label.

---

## 9. LLM robustness

The recommended format improves LLM robustness because:

- `SP` prefix signals a product/control token;
- technical English entity codes are less likely to be translated when accompanied by instruction;
- double brackets make the token boundary clearer;
- uppercase ASCII and underscores reduce normalization risk;
- fixed-length counter and integrity suffix make corruption easier to detect;
- future audit can compare exact expected tokens, missing tokens, unknown tokens and failed-integrity tokens.

It does not solve every LLM problem.

Remaining LLM risks:

- summarization may remove placeholders entirely;
- an LLM may still invent plausible tokens;
- placeholders may be reordered and change meaning;
- multiple placeholders may be merged into one;
- markdown/HTML may still split tokens;
- a model may still translate `PERSON` if instructed poorly.

Required future prompt guidance:

```text
Do not translate, edit, remove, merge, split or reformat tokens that look like [[SP_...]]. Preserve them exactly.
```

Audit must still check whether expected placeholders survived.

---

## 10. Copy/paste robustness

Recommended format copy/paste properties:

- ASCII-only, so it is safer across browsers, editors, terminals and logs;
- no curly braces, reducing accidental template interpretation;
- no Unicode brackets, reducing glyph conversion risk;
- no spaces, reducing line-wrapping ambiguity;
- underscores are stable in most environments;
- double square brackets remain visually recognizable.

Known copy/paste risks:

- some rich-text editors may insert zero-width characters;
- line wrapping may visually split but not actually alter the token;
- markdown/wiki systems may treat double square brackets as link syntax;
- copy from PDF may lose brackets or insert spaces.

Future validation should detect:

- missing outer brackets;
- single instead of double brackets;
- spaces inside the token;
- lowercase variants;
- invalid counter length;
- invalid integrity token length;
- tokens that match shape but are not issued by the Scrub Key.

---

## 11. DOCX/PDF/TXT compatibility

### TXT

Recommended candidate is strong for TXT because it is ASCII-only and exact-match friendly.

Expected future behavior:

```text
TXT input/output can preserve [[SP_PERSON_0001_A7F3]] as plain text.
```

### DOCX

Recommended candidate is compatible with DOCX body text, but not immune to Word run splitting.

Known DOCX risks:

- a visually intact token may be split across multiple `w:t` nodes;
- track changes, comments, headers/footers and metadata remain separate risks;
- longer tokens may be more likely to split across runs due to formatting.

Future DOCX audit should report possible split robust placeholders, but should not silently repair ambiguous fragments.

### PDF text extraction

Recommended candidate is better than Unicode brackets for PDF extraction because it is ASCII-only.

Known PDF risks:

- selectable-text extraction may lose layout or reading order;
- brackets may be separated from text;
- line breaks or spaces may be inserted;
- scanned/image-only PDFs remain unsupported.

PDF support remains TXT-only for restored output. This proposal does not add restored PDF output, OCR or PDF-to-DOCX reconstruction.

---

## 12. Scrub Key compatibility

Current Scrub Key items already contain:

```text
placeholder
entity_type
type_label
original_value
```

The recommended future placeholder can still fit in the existing `placeholder` field:

```json
{
  "placeholder": "[[SP_PERSON_0001_A7F3]]",
  "entity_type": "PERSON",
  "type_label": "Naam"
}
```

However, full robust validation may require future schema additions such as:

```text
placeholder_format
placeholder_counter
placeholder_integrity
placeholder_nonce
placeholder_version
```

WP31 does not change the Scrub Key schema.

Compatibility principle:

```text
A future Scrub Key version may store robust placeholders, but legacy keys with [PERSOON_1] must remain restorable until a separate migration policy says otherwise.
```

---

## 13. Backward compatibility strategy

Recommended strategy:

```text
additive support first, replacement later only if separately approved
```

Rules:

1. Existing legacy placeholders such as `[PERSOON_1]` remain valid for current Scrub Keys.
2. Future validation may detect both legacy and robust placeholder shapes.
3. Robust-format validation failures must not be confused with legacy-format limitations.
4. Mixed legacy/robust documents should be supported only after explicit design and tests.
5. The UI must not silently rewrite legacy placeholders into robust placeholders.
6. Migration, if ever added, must be a separate workpackage with tests, audit output and user-visible explanation.
7. Reinsert should not guess that `[PERSON_1]` means `[PERSOON_1]` or that `[[SP_PERSON_0001_A7F3]]` means another nearby token.

Safe compatibility phases:

```text
Phase 1: document proposal only.
Phase 2: validate robust tokens without generating them.
Phase 3: generate robust tokens in new Scrub Keys only after schema decision.
Phase 4: support legacy and robust reinsert together.
Phase 5: optional migration tool only if approved.
```

---

## 14. Migration risks

Migration risks:

- old scrubbed documents contain legacy placeholders;
- old Scrub Keys map legacy placeholders only;
- old AI outputs may still need restoration;
- current tests and examples use legacy placeholders;
- changing placeholder shape may break user expectations;
- robust placeholders are longer and may reduce document readability;
- robust placeholders may split across DOCX runs;
- checksum/integrity validation may create confusing warnings if the UI is not clear;
- Scrub Key schema changes can break import/export compatibility;
- migration mixed with implementation can silently change export/reinsert semantics.

Migration must not be combined with WP32 unless explicitly approved. WP32 should implement validation helper behavior behind tests, not switch the product to new placeholder generation.

---

## 15. Audit and validation requirements

Future validation should happen before reinsert and before export of restored output.

Minimum audit fields for a future helper:

| Field | Meaning |
| --- | --- |
| `placeholder_format_version` | `legacy`, `robust_v1`, `mixed` or `unknown`. |
| `expected_placeholders` | Placeholders listed in the Scrub Key. |
| `observed_placeholders` | Placeholders found in the AI output/document text. |
| `missing_placeholders` | Expected placeholders not found. |
| `unknown_placeholders` | Placeholder-like tokens not in the Scrub Key. |
| `integrity_failed_placeholders` | Robust-shaped tokens that fail integrity validation. |
| `near_miss_placeholders` | Tokens that look like damaged placeholders. |
| `duplicate_placeholder_entries` | Duplicate placeholder mappings inside the Scrub Key. |
| `placeholder_count_changes` | Count differences per placeholder between expected and observed text. |
| `format_split_risk` | Possible split token across markup or document runs where detectable. |
| `validation_severity` | `info`, `warning`, `strong_warning`, `block_reinsert_until_reviewed`. |

Recommended validation behavior:

- exact valid robust tokens may proceed;
- legacy exact tokens may proceed with legacy-format limitation note;
- missing placeholders should be high-severity warnings;
- integrity failures should block automatic reinsert until reviewed;
- unknown placeholders should remain unchanged and be flagged;
- near-miss tokens should never be silently repaired;
- mixed-format documents require explicit audit output;
- audit should state when restored output may be incomplete.

---

## 16. Implementation phases

WP31 does not implement any of these phases. Recommended future implementation phases are:

### Phase A — WP32 validation helper

Purpose:

- implement detection/validation helpers for robust placeholder shapes;
- add unit tests with synthetic values only;
- validate legacy and robust tokens without changing generation or reinsert behavior.

Possible files later:

```text
placeholder_validation.py
tests/test_placeholder_validation.py
```

### Phase B — WP33 audit hardening

Purpose:

- integrate validation output into reinsert/audit flows;
- report missing, unknown, failed-integrity and near-miss placeholders clearly;
- do not silently repair placeholders.

### Phase C — WP34 synthetic AI-output corruption tests

Purpose:

- add synthetic examples for translation, summarization, markdown/HTML, spacing, punctuation and DOCX/PDF extraction damage;
- confirm validation reports failures clearly.

### Phase D — future robust placeholder generation decision

Purpose:

- decide when new Scrub Keys may generate robust placeholders;
- coordinate with Scrub Key schema/lifecycle work;
- preserve legacy support.

### Phase E — optional migration policy

Purpose:

- only if needed;
- separate workpackage;
- explicit user-facing explanation and audit trail;
- no silent migration.

---

## 17. Recommended next workpackages

Immediate next workpackage:

```text
WP32 — Placeholder checksum/validation helper
```

Recommended WP32 scope:

- helper-only;
- tests first;
- no UI;
- no placeholder generation change;
- no migration;
- no Scrub Key schema migration;
- no export behavior change;
- support strict parsing of the recommended robust shape;
- support legacy detection as a separate mode;
- report validation issues without guessing repair.

Follow-up workpackages:

```text
WP33 — Unknown/changed placeholder audit hardening
WP34 — Synthetic AI-output placeholder corruption tests
```

Coordination note:

- WP32 should coordinate with WP26/WP29 if integrity semantics move toward HMAC, signatures or authenticated Scrub Key design.
- WP32 should not implement cryptographic authenticity without a security specification.

---

## 18. Final recommendation

WP31 recommends this future robust placeholder format direction:

```text
[[SP_<ENTITY>_<COUNTER>_<INTEGRITY>]]
```

Primary example:

```text
[[SP_PERSON_0001_A7F3]]
```

This recommendation is architecture/proposal-only. It is not an implementation, not a migration and not a change to current reinsert behavior.

---

## 19. Intentionally not changed in WP31

- No placeholder migration.
- No reinsert helper change.
- No Scrub Key schema change.
- No UI change.
- No export behavior change.
- No tests added or changed.
- No AI/cloud integration.
- No dependency changes.
- No code changed.
