# WP39 — Clean DOCX export policy

Status: completed policy/tests/documentation-only  
Repository: `solidprivacy-nl/scrub`

This policy defines when Scrub may warn, report, block or eventually claim a DOCX export is clean. It is policy-only and does not implement cleaning, removal, export blocking, UI changes or export semantic changes.

---

## 1. Current policy position

The current DOCX output must not be described as a clean DOCX export.

Allowed wording:

```text
DOCX output with current limitations
DOCX restored output with hygiene warnings
DOCX hygiene audit available
```

Not allowed yet:

```text
clean DOCX
safe DOCX
fully cleaned DOCX
metadata-free DOCX
comments removed
tracked changes removed
complete hidden-content handling
```

Reason: WP35-WP38 show that residual placeholders, comments, tracked changes, headers, footers and other hidden content remain high-risk unless explicitly audited and handled.

---

## 2. Current supported evidence

Current evidence is limited to detection/reporting:

- WP35 documents the risk.
- WP36A records residual placeholder and comments/kantlijncommentaren triage.
- WP37 extracts headers, footers, comments/person metadata and tracked-change markers.
- WP38 builds a report-only DOCX hygiene audit.

This evidence is enough for warnings and audit reporting. It is not enough for a clean-export claim.

---

## 3. Current export behavior

Current export behavior remains unchanged.

For now:

- standard DOCX export may continue with limitation warnings;
- restored DOCX export may continue with limitation warnings;
- DOCX hygiene audit can be produced as report-only output;
- no export is blocked by WP39;
- no content is removed by WP39;
- no export file bytes are changed by WP39.

---

## 4. Warning/report policy

### 4.1 No WP37/WP38-supported findings

If no supported findings are detected by the current audit:

Policy:

```text
warning-only
```

Required message:

```text
No supported hidden-content findings were detected, but this is not a clean-DOCX guarantee.
```

Reason:

WP37/WP38 do not yet cover all DOCX parts, such as metadata, footnotes, endnotes, custom XML, text boxes, shapes, charts or embedded objects.

### 4.2 Headers or footers detected

Policy:

```text
high-risk warning + audit finding
```

Required message:

```text
Headers or footers can contain confidential names, references or matter context outside normal body text. Review before sharing.
```

### 4.3 Comments/kantlijncommentaren detected

Policy:

```text
high-risk warning + audit finding
```

Required message:

```text
Comments or margin notes can contain reviewer identities, legal strategy, care notes or sensitive references. Review before sharing.
```

### 4.4 Tracked changes detected

Policy:

```text
high-risk warning + audit finding
```

Required message:

```text
Tracked changes can preserve deleted or moved sensitive text. Review before sharing.
```

### 4.5 Invalid DOCX or audit failed

Policy:

```text
unknown-risk warning
```

Required message:

```text
DOCX hygiene risk could not be fully assessed. Do not claim the file is clean.
```

---

## 5. Future export blocking policy candidates

Export blocking is not implemented in WP39.

Future export blocking may be considered only after explicit approval and tests.

Possible later blocking candidates:

- user selects a future `clean DOCX export` mode while high-risk findings are present;
- DOCX audit cannot parse the document;
- comments or tracked changes are detected and no cleaner/removal policy exists;
- a future cleaner fails to remove a high-risk part;
- residual placeholders are detected in output that is presented as restored/clean;
- unsupported high-risk parts are detected but not handled.

Blocking must not be silently added to existing standard/restored export behavior without a separate workpackage.

---

## 6. Minimum requirements before a clean-DOCX claim

A future clean-DOCX export claim requires all of the following:

1. explicit clean-export mode or policy decision;
2. extraction coverage for supported high-risk parts;
3. documented handling for comments, tracked changes, headers and footers;
4. documented handling or explicit exclusion for metadata;
5. documented handling or explicit exclusion for footnotes, endnotes, text boxes, shapes, charts, embedded objects and custom XML;
6. tests proving that handled parts are removed, sanitized or reported;
7. tests proving residual placeholders are detected or prevented;
8. audit output explaining what was handled and what remains unsupported;
9. no hidden recovery of removed content;
10. user-facing wording that does not overclaim.

Until these conditions are met, the product must not claim a DOCX export is clean.

---

## 7. Labels for future export modes

Allowed current labels:

```text
Download DOCX
Download hersteld DOCX-bestand
DOCX hygiene audit report
```

Recommended future labels:

```text
Download DOCX met beperkingen
Download hersteld DOCX-bestand met beperkingen
Bekijk DOCX-hygiënerapport
```

Potential later label only after approved implementation:

```text
Download schone DOCX-export
```

The later label is not allowed until a separate clean-export implementation and policy gate are complete.

---

## 8. Explicit non-changes in WP39

WP39 does not:

- implement a DOCX cleaner;
- remove comments;
- accept or remove tracked changes;
- remove metadata;
- block export;
- change export semantics;
- change DOCX reinsert behavior;
- change Streamlit UI;
- change Scrub Key schema;
- add dependencies;
- add real data;
- add cloud processing.

---

## 9. Recommended next step

Recommended next workpackage:

```text
WP40 — Document-centric review UX specification
```

Reason:

DOCX hygiene findings and audit reports need a document-centered review surface before export blocking or clean-export claims are safe to implement.

Alternative DOCX-specific follow-up if the coordinator wants to continue this line first:

```text
WP39B — DOCX hygiene audit UI planning
```

WP39B should plan how WP38 audit output is shown to users without yet blocking export or cleaning content.
