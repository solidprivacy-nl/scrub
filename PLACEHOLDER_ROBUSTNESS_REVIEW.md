# WP30 — Placeholder robustness review

Status: completed architecture/specification-only.

This review covers the risk that placeholders may be altered during an AI roundtrip before deterministic Scrub Key reinsert. It is deliberately specification-only: no placeholder migration, no Scrub Key schema change, no reinsert helper change, no UI change, no AI/cloud integration and no tests are implemented here.

---

## 1. Current placeholder format

The current reinsert helper recognizes placeholder-looking tokens with this pattern:

```text
\[[A-Z][A-Z0-9_:-]*_[0-9]+\]
```

Typical current examples are:

```text
[PERSOON_1]
[ZAAKNUMMER_1]
[ADRES_1]
[ORGANISATIE_01]
```

The format is compact and human-readable. It uses a single square-bracket pair, uppercase entity text, an underscore and a numeric suffix. The current implementation replaces exact placeholder strings from the Scrub Key mapping.

---

## 2. Current reinsert assumptions

The current deterministic reinsert path assumes:

1. The placeholder in the AI output is exactly the same string as the placeholder in the Scrub Key.
2. The placeholder is not translated, reformatted, split or normalized by another system.
3. A placeholder maps to one original value unless duplicate placeholder entries are detected in the Scrub Key.
4. Duplicate placeholders in the Scrub Key are ambiguous and excluded from deterministic replacement.
5. Repeated occurrences of the same placeholder in the text are valid and should all restore to the same original value.
6. Unknown placeholders in the text are reported and left unchanged.
7. Placeholders from the Scrub Key that are not found in the text are reported as missing.
8. For DOCX, placeholders must be present inside the processed `word/document.xml` text nodes; placeholders split across Word runs/text nodes are not restored in the current helper.
9. For PDF text reinsert, the placeholder must survive selectable-text extraction and appear in the extracted text exactly.
10. There is no fuzzy matching, no placeholder repair and no AI-based interpretation in the current reinsert path.

These assumptions are safe and deterministic, but they are fragile when the scrubbed text is rewritten by an LLM, translated, summarized, copied between formats, rendered through markdown/HTML or edited by humans.

---

## 3. How LLMs may corrupt placeholders

LLMs may treat placeholders as normal text rather than protected tokens. That can lead to:

- translating the entity label;
- changing singular/plural or spelling;
- adding spaces or punctuation;
- removing brackets;
- converting square brackets into parentheses;
- normalizing accents or casing;
- wrapping placeholders in markdown or HTML;
- splitting placeholders across lines or formatting spans;
- inventing new placeholders for readability;
- merging several placeholders into one;
- deleting placeholders during summarization;
- reordering placeholders in a way that changes legal or factual meaning.

The core risk is not only that reinsert fails. The more dangerous risk is partial restoration: some values restore while other sensitive values remain as placeholders or are lost, making the user think the workflow succeeded when the output is incomplete.

---

## 4. Examples of placeholder corruption

| Intended placeholder | Possible corrupted form | Likely consequence |
| --- | --- | --- |
| `[PERSOON_1]` | `[PERSON_1]` | Unknown placeholder; original value not restored. |
| `[PERSOON_1]` | `[PERSOON 1]` | Not recognized by current regex; original value not restored. |
| `[PERSOON_1]` | `PERSOON_1` | Brackets removed; not restored. |
| `[ZAAKNUMMER_1]` | `[ZAAK NUMMER_1]` | Spacing breaks exact match. |
| `[ADRES_1]` | `[ADRES_01]` | Looks valid, but does not match key if key uses `[ADRES_1]`. |
| `[ORGANISATIE_01]` | `[Organisatie_01]` | Case change breaks current regex and exact match. |
| `[BSN_1]` | `[BSN-1]` | Separator change breaks exact match. |
| `[PERSOON_1]` and `[PERSOON_2]` | `[PERSOON_1]` only | Merge risk; distinct people may collapse into one identity. |
| `[PERSOON_1]` | `<span>[PERSOON_</span><span>1]</span>` | Formatting split may break extraction/reinsert. |
| `[PERSOON_1]` | `` `[PERSOON_1]` `` | Plain text may still work, but downstream markdown conversion can split or escape it. |

---

## 5. Risk of translation

Translation is high risk because current placeholders contain natural-language entity labels. A translation model may translate or normalize labels:

```text
[PERSOON_1] → [PERSON_1]
[ADRES_1]   → [ADDRESS_1]
[ZAAKNUMMER_1] → [CASE_NUMBER_1]
```

Even if the translated placeholder still looks meaningful to a human, deterministic reinsert will treat it as unknown. Translation may also change word order around placeholders, which is usually acceptable if the placeholder remains intact, but dangerous if multiple placeholders represent different roles in a legal sentence.

Specification implication: future placeholder formats should avoid language-specific labels where possible, or treat the label as a stable technical code rather than human language.

---

## 6. Risk of summarization

Summarization is higher risk than rewriting because it may intentionally remove detail. A summarizer may:

- delete a placeholder because the sentence is considered unimportant;
- merge two people into one summary reference;
- replace several case references with one generic phrase;
- collapse repeated placeholders;
- move placeholders away from their original context.

Example:

```text
Input: [PERSOON_1] sprak met [PERSOON_2] over dossier [ZAAKNUMMER_1].
Output: De betrokkenen spraken over het dossier.
```

No placeholder corruption is visible because the placeholders are gone. Reinsert cannot restore missing values. The audit must therefore compare expected placeholders from the Scrub Key against observed placeholders after the AI roundtrip.

---

## 7. Risk of punctuation and spacing changes

LLMs and editors often normalize punctuation and spacing. Current placeholders are exact-match tokens, so small edits can break restoration:

```text
[PERSOON_1]  → [ PERSOON_1 ]
[PERSOON_1]  → [PERSOON_1 ].
[BSN_1]      → [BSN_ 1]
```

Some punctuation changes may still leave the placeholder intact, for example adding a period after the closing bracket. Others change the token itself. Future validation should identify near-miss tokens separately from completely unknown placeholders.

---

## 8. Risk of markdown/HTML formatting

Markdown and HTML can preserve visible text while changing underlying structure. Risks include:

- placeholder split across markdown emphasis markers;
- placeholder split across HTML spans;
- placeholder escaped as entities;
- placeholder wrapped in links or code tags;
- line breaks inserted inside the token;
- document conversion splitting a placeholder across DOCX runs.

Examples:

```html
<span>[PERSOON_</span><span>1]</span>
```

```markdown
[PERSOON_**1**]
```

In plain text these may not equal the original token. For DOCX, a visually intact placeholder can still be split across text nodes, which current DOCX reinsert intentionally does not repair.

---

## 9. Risk of duplicate placeholders

There are two different duplicate cases:

1. Repeated occurrence in output text: valid when the same placeholder represents the same original value multiple times.
2. Duplicate placeholder entries in the Scrub Key: unsafe because the same placeholder maps to more than one original value.

The current helper already treats duplicate key entries as ambiguous and excludes them from replacement. The future AI-roundtrip risk is different: an LLM may convert distinct placeholders into the same placeholder.

Example:

```text
Before: [PERSOON_1] tekent namens [PERSOON_2].
After:  [PERSOON_1] tekent namens [PERSOON_1].
```

This would restore deterministically, but incorrectly. A future audit should compare placeholder counts and positions or at least count changes per placeholder before and after AI processing.

---

## 10. Risk of unknown placeholders

Unknown placeholders may come from:

- LLM invention;
- translated placeholders;
- user edits;
- old Scrub Keys with a different format;
- corrupted formatting;
- mixing a document with the wrong Scrub Key.

The current helper reports unknown placeholders and leaves them unchanged. That is safe for deterministic behavior, but future UX should make unknown placeholders hard to miss before export. Unknown placeholders may mean original values cannot be restored, or that the wrong key is being used.

---

## 11. Candidate robust placeholder formats

This workpackage does not mandate a new placeholder format. The following are candidate directions for WP31 evaluation only:

```text
[[SP_PERSON_0001_A7F3]]
[[SP_BSN_0002_C91B]]
[[SP_ADDRESS_0003_D41A]]
```

Possible properties:

- double square brackets to make the token visually stronger than ordinary text;
- stable `SP` prefix for SolidPrivacy;
- uppercase ASCII only;
- stable technical entity code, preferably not translated;
- zero-padded sequence number;
- short checksum suffix;
- no spaces;
- no accents;
- no natural punctuation except `_` and brackets;
- easy to detect with a strict regex;
- easy to explain in UI and audit reports.

Candidate regex direction for evaluation only:

```text
\[\[SP_[A-Z0-9]+_[0-9]{4}_[A-F0-9]{4}\]\]
```

This is not an implementation decision. WP31 should compare this against alternatives before any migration.

---

## 12. Checksum idea

A checksum can help distinguish intact placeholders from corrupted or invented ones.

Possible goals:

1. Detect typos or formatting corruption inside a placeholder.
2. Detect invented placeholders that look valid but were not issued by Scrub.
3. Support clearer audit messages before deterministic reinsert.

Open design questions for WP31/WP32:

- Should the checksum validate only the visible placeholder components?
- Should the checksum bind the placeholder to a non-sensitive Scrub Key item id or nonce?
- Should the checksum use a simple checksum for typo detection or a keyed HMAC-like value for stronger authenticity?
- How can checksum validation avoid leaking information about the original sensitive value?
- How long should the checksum be to balance readability and collision risk?

Important safety boundary:

```text
Do not derive a visible checksum directly from the original sensitive value unless the privacy impact has been reviewed.
```

A safer first design may use non-sensitive placeholder metadata or a random per-item nonce stored in the Scrub Key, but that would require schema review in a later workpackage.

---

## 13. Validation and audit idea

Future validation should happen before reinsert and before export of restored output.

Suggested audit classes:

| Audit class | Meaning |
| --- | --- |
| `expected_placeholder_count` | Count from Scrub Key. |
| `observed_placeholder_count` | Count found in AI output. |
| `exact_placeholders_preserved` | Expected placeholders found exactly. |
| `placeholders_missing` | Expected placeholders not found. |
| `unknown_placeholders` | Placeholder-like tokens not in the Scrub Key. |
| `checksum_failed_placeholders` | Tokens matching the robust shape but failing checksum. |
| `duplicate_placeholder_count_changes` | Placeholder occurrence counts changed materially. |
| `near_miss_placeholders` | Tokens that look like corrupted placeholders. |
| `format_split_risk` | Placeholder split across markup or document nodes where detectable. |

Recommended behavior direction:

- exact matches may proceed;
- missing placeholders should be visible as high-severity warnings;
- checksum failures should block automatic reinsert until reviewed;
- unknown placeholders should remain unchanged and be flagged;
- near-miss tokens should not be guessed silently;
- the audit should clearly state that restored output may be incomplete when placeholders are missing.

---

## 14. Migration risks

A placeholder migration can create product risk if handled too early.

Key risks:

- existing scrubbed documents may contain legacy placeholders;
- existing Scrub Keys may map only legacy placeholders;
- old AI outputs may need legacy restoration;
- users may have learned the old placeholder style;
- tests and examples may assume current placeholders;
- regex updates may accidentally detect unrelated bracketed legal text;
- DOCX split-run behavior may still affect a stronger format;
- longer placeholders may reduce readability in legal/professional documents;
- changing placeholder labels can alter perceived legal meaning if not explained well;
- export/download semantics could accidentally change if migration is mixed with implementation.

Migration should therefore be a separate, gated workpackage after the proposal, validation helper and compatibility tests exist.

---

## 15. Backward compatibility concerns

Backward compatibility should be explicit:

1. Legacy placeholders such as `[PERSOON_1]` must remain restorable for existing documents and Scrub Keys until a migration policy says otherwise.
2. A future helper may need to detect both legacy and robust placeholder formats.
3. Scrub Key schema versioning must identify which placeholder format was issued.
4. Audit output should distinguish legacy-format limitations from robust-format validation failures.
5. Mixed-format documents should be supported only if deliberately designed and tested.
6. The UI should not silently rewrite old placeholders into new placeholders without user-visible explanation and audit evidence.

The safe default is additive support first, not replacement.

---

## 16. Main architecture findings

1. The current placeholder format is deterministic and readable but fragile under AI rewriting, translation and formatting conversion.
2. The current audit already reports unknown, duplicate and not-found placeholders, which is a useful foundation.
3. The highest-risk corruption is not obvious token damage, but silent placeholder deletion or merging during summarization.
4. A robust future format should use a stable prefix, strict machine-readable structure and some integrity marker.
5. Checksum design must avoid leaking original sensitive values.
6. Placeholder validation should be treated as part of the audit layer, not as silent auto-repair.
7. Backward compatibility is mandatory because existing Scrub Keys and documents use the current format.

---

## 17. Recommended next workpackages

Recommended immediate next step:

```text
WP31 — LLM-resistant placeholder format proposal
```

WP31 should compare candidate formats and decide a proposal, without migrating existing behavior yet.

Follow-up workpackages:

```text
WP32 — Placeholder checksum/validation helper
WP33 — Unknown/changed placeholder audit hardening
WP34 — Synthetic AI-output placeholder corruption tests
```

Suggested dependency order:

1. WP31 decides the proposed format and compatibility strategy.
2. WP32 implements validation/checksum helpers behind tests.
3. WP33 strengthens audit behavior for unknown, missing, changed and near-miss placeholders.
4. WP34 adds synthetic AI-output corruption tests for translation, summarization, markdown/HTML and formatting changes.

---

## 18. Intentionally not changed in WP30

- No placeholder migration.
- No Scrub Key schema change.
- No reinsert helper change.
- No UI change.
- No AI/cloud integration.
- No tests added.
- No export behavior change.
- No final placeholder format mandated.
