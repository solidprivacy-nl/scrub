# Export/download UX contracts

Workpackage: `WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS`

Repository: `solidprivacy-nl/scrub`

Status: tests/documentation-only.

This document records the contract for the professional export/download UX redesign before implementation.

---

## 1. Purpose

The export/download UX may be grouped and renamed, but export semantics must stay unchanged unless a later approved implementation package explicitly changes them.

The contract protects these boundaries:

```text
Export UX is grouped but semantics stay unchanged.
Scrub Key is separate and visibly sensitive.
Audit/technical downloads remain available but secondary.
Debug labels are planned for cleanup.
Implementation requires separate package.
```

---

## 2. Required export groups

The planned export/download section must separate:

```text
Document downloaden
Scrub Key
Audit en technische bestanden
```

Meaning:

- normal document outputs belong under `Document downloaden`;
- Scrub Key belongs in its own visibly warned section;
- audit/technical files remain available but move to a secondary/audit layer.

---

## 3. Primary and secondary outputs

Primary/normal document outputs:

```text
Opgeschoonde tekst (.txt)
Word-document (.docx)
PDF (.pdf)
```

Secondary/audit outputs:

```text
Vervangtabel (.csv)
Scrubrapport (.txt)
DOCX hygiene audit
Geavanceerde technische informatie
```

The contract is about grouping and hierarchy. It does not approve a change to download bytes, filenames, MIME types or availability.

---

## 4. Export semantics boundary

No export semantics change is approved by this contract package.

The redesign must not change:

```text
filenames
MIME types
payloads
export eligibility
Scrub Key contents
report contents
```

The current implementation package must only be allowed to group/label existing downloads unless a later package explicitly approves an export-behavior change.

---

## 5. Scrub Key safety

The Scrub Key must be clearly separated from normal document downloads.

Scrub Key is sensitive because it can restore original values.

The future UI must include a separate warning near the Scrub Key download.

Required concepts:

```text
Scrub Key clearly separated
Scrub Key is sensitive
can restore original values
separate warning
```

---

## 6. Audit and technical details remain available

Audit and technical details must not disappear.

They should become secondary layers such as:

```text
Audit en risico’s
Geavanceerd
Audit en technische bestanden
Geavanceerde technische informatie
```

The implementation may make these details calmer or collapsed by default, but it must not remove them.

---

## 7. Planned debug/prototype copy cleanup

The direction is locked by contract tests:

```text
Serial review — experimentele reviewhulp -> Stap voor stap controleren
Download opgeschoonde bestanden -> Exporteer resultaat
Technische details bij de vervangtabel -> Geavanceerde details bij de vervangtabel
Technische herkenningen -> Geavanceerde herkenningsdetails
```

These are planning contracts only. They are not implemented in this package.

---

## 8. Follow-up implementation route

Implementation sequence:

```text
WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION
WP_REVIEW_COPY_POLISH_IMPLEMENTATION
WP_MVP_UI_APP_VERIFICATION_CLOSEOUT
```

The immediate next implementation package is:

```text
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION
```

Do not start it automatically.

---

## 9. Explicit non-goals

```text
No Streamlit implementation.
No export payload change.
No Scrub Key change.
No reinsert change.
No recognizer/benchmark change.
No product claim.
No threshold enforcement.
No production gate.
```

No product UI implementation is approved by this contract package. The implementation requires a separate workpackage and must preserve export semantics.
