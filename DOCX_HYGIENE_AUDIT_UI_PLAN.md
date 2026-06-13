# WP39B — DOCX hygiene audit UI planning

Status: completed planning/documentation-only  
Repository: `solidprivacy-nl/scrub`

This plan describes how the existing report-only DOCX hygiene audit can be shown in the Streamlit app in a later implementation package.

This package does not implement UI, cleaning, export blocking, export/download changes, Scrub Key changes, reinsert behavior changes, dependencies, cloud processing or real-data fixtures.

---

## 1. Purpose

WP37 and WP38 made hidden DOCX hygiene risk visible in helper/report form. WP39 defined that current DOCX output must not be described as clean DOCX export.

WP39B plans the future UI surface for that audit.

Goal:

```text
Show DOCX hygiene risk clearly before users trust or share DOCX output, without changing export behavior yet.
```

The UI must help users understand that DOCX can contain hidden or side-channel content such as headers, footers, comments and tracked changes.

---

## 2. Existing helper to use later

Future implementation should use the existing helper:

```python
build_docx_hygiene_audit_report(content: bytes) -> dict
render_docx_hygiene_audit_markdown(report: dict) -> str
```

Source:

```text
docx_hygiene_audit.py
```

Important helper boundaries already defined by WP38:

```text
report_only: true
extraction_only: true
cleaning_applied: false
export_blocking: false
export_semantics_changed: false
safe_to_claim_clean: false
```

The UI must preserve these boundaries.

---

## 3. Placement in the current workflow

Future UI should show the DOCX hygiene audit only when DOCX bytes are available.

Recommended placement in the anonymization/export flow:

1. After upload of a DOCX file and before DOCX export buttons.
2. Near `Download opgeschoond Word-bestand (.docx)`.
3. In a compact section titled:

```text
DOCX-hygiënecontrole — rapportage, geen schoonmaak
```

Recommended placement in the reinsert flow:

1. Near restored DOCX output/download controls.
2. Below the existing DOCX limitation warning.
3. With the same report-only boundary text.

The section should be collapsed by default when severity is `low` and expanded by default when severity is `medium` or `high`.

---

## 4. Minimum visible UI content

The future UI should show a compact summary first:

```text
Er is een DOCX-hygiënerapport beschikbaar.
Dit rapport controleert ondersteunde verborgen DOCX-onderdelen.
Dit is geen schone-DOCX garantie.
Er is geen schoonmaak toegepast.
Er is geen exportblokkade toegepast.
```

Minimum fields:

```text
severity
summary.message
report_only
cleaning_applied
export_blocking
safe_to_claim_clean
counts.headers
counts.footers
counts.comments
counts.tracked_changes
unsupported_scope_note
```

Findings should be shown as a compact list with:

```text
finding.title
finding.severity
finding.count
finding.risk
finding.recommended_action
```

---

## 5. Dutch labels

Recommended Dutch UI labels:

```text
DOCX-hygiënecontrole — rapportage, geen schoonmaak
Risiconiveau
Verborgen onderdelen gevonden
Kopteksten
Voetteksten
Opmerkingen / kantlijncommentaren
Wijzigingen bijhouden
Aanbevolen controle
Rapport downloaden
Geen schone-DOCX garantie
```

Required boundary labels:

```text
Rapportage-only
Geen schoonmaak toegepast
Geen exportblokkade toegepast
Geen opmerkingen of wijzigingen verwijderd
Geen wijziging aan Scrub Key
Geen wijziging aan terugzetten/originele waarden
```

Forbidden labels until later approved implementation:

```text
Schone DOCX
Veilige DOCX
Volledig opgeschoonde DOCX
Metadata-vrij
Opmerkingen verwijderd
Wijzigingen verwijderd
Verborgen inhoud verwijderd
```

---

## 6. Severity behavior

The future UI should map helper severity as follows.

### `low`

Meaning:

```text
No WP37-supported hidden-content findings were detected.
```

Required warning:

```text
Geen ondersteunde verborgen DOCX-onderdelen gevonden, maar dit is geen schone-DOCX garantie.
```

UI behavior:

- compact info message;
- section collapsed by default;
- export/download buttons remain unchanged.

### `medium`

Meaning:

```text
DOCX hygiene risk could not be fully assessed.
```

Required warning:

```text
DOCX-hygiënerisico kon niet volledig worden beoordeeld. Claim het bestand niet als schoon.
```

UI behavior:

- warning message;
- section expanded by default;
- export/download buttons remain unchanged.

### `high`

Meaning:

```text
Headers, footers, comments or tracked changes were detected.
```

Required warning:

```text
Verborgen of moeilijk zichtbare DOCX-inhoud is gevonden. Controleer dit vóór delen of exporteren.
```

UI behavior:

- high-risk warning;
- section expanded by default;
- finding list visible;
- export/download buttons remain unchanged.

---

## 7. Export/download policy

WP39B does not change export/download behavior.

Future implementation may show or download an audit report, but only as report output. It must not silently change DOCX output bytes, filenames, MIME types, or export availability.

Allowed future UI actions:

```text
Bekijk DOCX-hygiënerapport
Download DOCX-hygiënerapport (.txt or .md)
```

Not allowed in WP39B or the first UI implementation unless separately approved:

```text
Blokkeer export
Maak schoon DOCX-bestand
Verwijder opmerkingen
Accepteer/verwijder bijgehouden wijzigingen
Verwijder metadata
Wijzig DOCX output bytes
Wijzig Scrub Key mapping
Wijzig reinsert output
```

---

## 8. Implementation constraints for later package

A later UI implementation should be small and helper-driven.

Technical direction:

```python
from docx_hygiene_audit import build_docx_hygiene_audit_report, render_docx_hygiene_audit_markdown
```

Allowed inputs:

```text
uploaded DOCX bytes already provided by the user in the current session
restored DOCX bytes already produced locally in the current session
```

Forbidden:

- no cloud document processing;
- no AI calls;
- no persistence of document bytes;
- no new dependencies;
- no raw HTML rendering of user document content;
- no export blocking;
- no cleaning/removal;
- no mutation of review table state;
- no mutation of Scrub Key state;
- no mutation of reinsert output.

Additional implementation boundaries:

- no cloud document processing
- no AI calls
- no persistence of document bytes
- no real data
- no cloud processing
- real-data fixtures are forbidden
- uploaded DOCX bytes already provided by the user in the current session may be audited report-only

---

## 9. Suggested future contract tests

Before UI implementation, add a contract-test package such as:

```text
WP39C — DOCX hygiene audit UI contract tests
```

Suggested test file:

```text
tests/test_docx_hygiene_audit_ui_plan.py
```

Minimum contract checks:

- plan says report-only;
- plan says no cleaning applied;
- plan says no export blocking;
- plan says no clean-DOCX guarantee;
- plan forbids clean/safe/metadata-free wording;
- plan requires `safe_to_claim_clean: false`;
- plan requires unsupported-scope note;
- plan requires high-risk findings for headers, footers, comments and tracked changes;
- plan forbids Scrub Key changes;
- plan forbids reinsert behavior changes;
- plan forbids cloud processing and real data.

---

## 10. Recommended next step

Recommended next package:

```text
WP39C — DOCX hygiene audit UI contract tests
```

Only after those contract tests are green and coordinator approval is explicit should a later package implement a small Streamlit UI surface.

Potential later implementation package:

```text
WP39D — DOCX hygiene audit UI implementation
```

The later implementation must remain report-only unless a separate approved policy package changes export-blocking or clean-DOCX semantics.
