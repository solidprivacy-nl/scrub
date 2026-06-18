# MVP UI cleanup and export/download redesign plan

Workpackage: `WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN`

Repository: `solidprivacy-nl/scrub`

Status: planning/design/specification-only.

This document pauses new recall/benchmark follow-up work temporarily and defines the next visible product-improvement line: make the MVP interface calmer, less debug-like and more professional, especially the export/download step.

No product UI is implemented in this package. No Streamlit code, export semantics, Scrub Key behavior, reinsert behavior, recognizer behavior, benchmark gate or product claim is changed.

---

## 1. Goal and non-goals

Goals:

```text
A normal user gets a calmer professional workflow.
Technical/debug-like elements move out of the primary flow.
Download/export becomes one finished product step with clear choices.
Audit and technical details remain available, but become secondary.
```

Non-goals:

```text
No implementation in this package.
No export semantics change.
No Scrub Key or reinsert change.
No recognizer or benchmark change.
No new frontend stack.
No professional document editor.
No click-to-mark.
No full-document editor.
No production gate or product claim.
```

---

## 2. Current UI problems

The current UI is functionally useful, but it still reads like a technical prototype in several places.

| Current item | Current location | Why it feels prototype/debug-like | Recommended treatment |
|---|---|---|---|
| Download buttons as a loose technical list | Section `5. Download opgeschoonde bestanden` | TXT, CSV, scrub report, DOCX and PDF are shown as separate equal-weight buttons. There is no product hierarchy or primary export action. | Redesign as one `Exporteer resultaat` step with a primary export and secondary grouped options. |
| `Download vervangtabel (.csv)` | Export/download section | Useful for audit, but it is not a normal user’s primary export. | Move under `Meer exportopties` or `Audit en technische bestanden`. |
| `Download scrubrapport (.txt)` | Export/download section | Important, but currently visually equal to the cleaned document output. | Move under audit/download options, not primary document export. |
| DOCX hygiene audit | Currently shown near DOCX export | Valuable safety report, but named as technical audit and can dominate the export flow. | Keep, but put under `Audit en risico’s` or `Geavanceerde details`; surface only a compact risk summary in primary flow. |
| `Technische herkenningen` | Bottom expander after normal flow | Technical enough to be secondary, but its naming confirms debug/developer feel. | Rename to `Geavanceerde herkenningsdetails`; keep collapsed by default. |
| `Technische details bij de vervangtabel` | Below review table | Needed for audit/debug, but not primary user task. | Keep collapsed; move wording to `Geavanceerde details bij de vervangtabel`. |
| `Serial review — experimentele reviewhulp` | Below replacement table | The word `experimentele` makes the UI look unfinished. `Serial review` is also product-internal language. | Rename to `Stap voor stap controleren` or `Gevonden gegevens één voor één controleren`; recommendation: `Stap voor stap controleren`. |
| `table-first baseline · non-destructive · report-only...` | Serial review caption | This is governance/debug copy, not user-facing copy. | Move to technical/audit copy or remove from primary UI. Keep the safety boundary in docs/tests. |
| `Vervangtabel controleren — <items> items` | Under found-data section | Better than before, but still feels technical. | Keep as source-of-truth fallback, but rename later to `Alle gevonden gegevens controleren — <items> items` if table remains primary fallback. |
| `Mogelijke gemiste waarden` | In review flow | Valuable review safety layer, but still audit-like. | Keep visible when findings exist, but use user-facing wording: `Mogelijk extra te controleren waarden`. |
| Too many equal blocks | Entire lower half of app | Review table, serial review, memory, downloads and technical details compete visually. | Rebuild hierarchy around one clear task sequence: review → export → audit. |

Classification:

```text
Primary flow: source/processed comparison, review status, simple found-data review, primary export.
Advanced: full replacement table, technical table columns, candidate audit layer, DOCX hygiene details, raw recognitions.
Audit: scrub report, replacement table CSV, DOCX hygiene audit, technical recognition details.
Later removal/rename: debug wording such as experimentele reviewhulp, report-only governance captions in the primary surface.
```

---

## 3. New information architecture

Recommended structure:

```text
1. Document toevoegen
2. Gegevens controleren
3. Export kiezen
4. Audit en risico’s bekijken
```

Why this structure:

- It matches the real user task better than the current many-step technical flow.
- It keeps review and export as separate mental tasks.
- It makes audit/risk visible without letting it dominate the normal path.
- It keeps the review table source-of-truth role while making the normal route calmer.

Detailed target:

```text
1. Document toevoegen
   - upload or paste text
   - profile and replacement settings in sidebar

2. Gegevens controleren
   - central side-by-side source/processed review
   - marker toggle remains simple
   - guided item-by-item review as optional support
   - full replacement table remains fallback/source of truth in a collapsed section

3. Export kiezen
   - one primary export path
   - document outputs grouped together
   - Scrub Key clearly separated because it is sensitive
   - audit files grouped separately

4. Audit en risico’s bekijken
   - DOCX hygiene summary/details
   - technical recognition details
   - replacement table CSV / scrub report
   - advanced details for expert review
```

The current numbering can be migrated incrementally. The implementation should not attempt a full UI rewrite in one package.

---

## 4. Export/download redesign

### Design choice

Use a grouped export section rather than a single combined package selector in the first implementation.

Reason:

```text
Streamlit supports separate download_button outputs more reliably than dynamic multi-file bundles.
Changing to a bundled ZIP would change export semantics and should not happen silently.
Grouped buttons can improve UX without changing payloads.
```

### Target section title

Replace:

```text
5. Download opgeschoonde bestanden
```

with:

```text
3. Export kiezen
```

or, if keeping old numbering temporarily:

```text
5. Exporteer resultaat
```

Recommendation for first implementation:

```text
5. Exporteer resultaat
```

This reduces implementation risk because it does not force renumbering all earlier sections in the first export package.

### Target wireframe

```text
5. Exporteer resultaat

[Info]
Je export wordt gemaakt op basis van de gecontroleerde vervangtabel.
Controleer bij twijfel eerst de gevonden gegevens hierboven.

Document downloaden
[Primaire knop] Download opgeschoonde tekst (.txt)
[Secundair] Word-document (.docx)
[Secundair] PDF (.pdf)

Scrub Key
[Waarschuwing]
De Scrub Key kan originele waarden herstellen. Bewaar dit bestand veilig.
[Knop] Download Scrub Key (.json)

Audit en technische bestanden
[Ingeklapt: Meer downloads]
  Download vervangtabel (.csv)
  Download scrubrapport (.txt)
  DOCX hygiene audit
  Geavanceerde technische informatie
```

### If no upload file is present

Current copy:

```text
Geen uploadbestand aanwezig. Export wordt gemaakt op basis van het tekstvak.
```

Recommended copy:

```text
Je gebruikt tekst uit het invoervak. De export wordt daarom gemaakt als tekstbestand en, waar mogelijk, als nieuw Word/PDF-bestand.
```

### Export grouping policy

Primary:

```text
Opgeschoonde tekst (.txt)
```

Secondary document outputs:

```text
Word-document (.docx)
PDF (.pdf)
```

Sensitive key output:

```text
Scrub Key (.json)
```

Audit/technical outputs:

```text
Vervangtabel (.csv)
Scrubrapport (.txt)
DOCX hygiene audit
Technische herkenningen
```

### Explicit non-change

```text
The redesign must not change bytes, filenames, MIME types, Scrub Key contents, export eligibility or report contents unless a later package explicitly approves it.
```

---

## 5. Debug/audit layer cleanup

### Normal user text

Should explain decisions and safety in plain language:

```text
Controleer de gevonden gegevens voordat je exporteert.
De vervangtabel blijft leidend.
De Scrub Key kan originele waarden herstellen.
Auditdetails helpen bij controle, maar vervangen geen menselijke review.
```

### Expert/audit text

Should move under advanced/audit sections:

```text
table-first baseline
non-destructive
report-only
no Scrub Key mutation
no export blocking
no reinsert behavior change
technical score
technical source
recognizer entity type
analysis explanation
```

### Specific placement decisions

| Item | Future placement | Default state |
|---|---|---|
| Technical details by replacement table | `Geavanceerde details bij de vervangtabel` | collapsed |
| Technical recognitions | `Audit en risico’s` → `Geavanceerde herkenningsdetails` | collapsed |
| DOCX hygiene audit | `Audit en risico’s` or inside export as compact risk summary + details | collapsed unless medium/high risk |
| Replacement table CSV | `Audit en technische bestanden` | collapsed |
| Scrub report TXT | `Audit en technische bestanden` | collapsed |
| Candidate/missed-value audit | In review section if candidates exist, with plain warning | expanded only when candidates exist |
| Governance captions | Remove from primary UI; preserve in docs/tests | hidden from primary flow |

---

## 6. Review-flow cleanup

The review-flow cleanup should preserve safety while reducing prototype language.

Keep:

```text
Review table remains source of truth and fallback.
Side-by-side source/processed review remains central.
Markeringen tonen remains simple.
Candidate/missed-value warnings remain visible when relevant.
```

Rename:

```text
Serial review — experimentele reviewhulp
```

to:

```text
Stap voor stap controleren
```

Reason:

```text
It is short, Dutch, user-task-oriented and no longer says the interface is experimental.
```

New supporting copy:

```text
Controleer gevonden gegevens één voor één. De vervangtabel blijft leidend voor beslissingen en export.
```

Remove or move out of primary flow:

```text
table-first baseline · non-destructive · report-only · no Scrub Key mutation · no export blocking · no reinsert behavior change
```

These are important engineering boundaries, but they should not be a normal user-facing caption.

Review table title recommendation:

```text
Vervangtabel controleren — 16 items
```

later becomes:

```text
Alle gevonden gegevens controleren — 16 items
```

But because review table terminology is already established, this should be implemented in a separate review-copy package, not mixed into the export package.

---

## 7. Dutch copy cleanup list

Recommended copy changes:

| Current copy | Recommended copy |
|---|---|
| `Serial review — experimentele reviewhulp` | `Stap voor stap controleren` |
| `Alleen-lezen hulpweergave. De bestaande vervangtabel blijft leidend voor beslissingen, Scrub Key en export.` | `Controleer gevonden gegevens één voor één. De vervangtabel blijft leidend voor beslissingen en export.` |
| `table-first baseline · non-destructive · report-only · no Scrub Key mutation · no export blocking · no reinsert behavior change` | Move to docs/tests, not primary UI. |
| `Download opgeschoonde bestanden` | `Exporteer resultaat` |
| `Geen uploadbestand aanwezig. Export wordt gemaakt op basis van het tekstvak.` | `Je gebruikt tekst uit het invoervak. De export wordt gemaakt op basis van deze tekst.` |
| `Download vervangtabel (.csv)` | `Vervangtabel downloaden (.csv)` under `Audit en technische bestanden` |
| `Download scrubrapport (.txt)` | `Scrubrapport downloaden (.txt)` under `Audit en technische bestanden` |
| `DOCX hygiene audit` | `Word-bestand controleren op verborgen inhoud` or `DOCX-hygiënecontrole` |
| `Technische details bij de vervangtabel` | `Geavanceerde details bij de vervangtabel` |
| `Technische herkenningen` | `Geavanceerde herkenningsdetails` |
| `Mogelijke gemiste waarden` | `Mogelijk extra te controleren waarden` |

Recommended first copy package:

```text
WP_REVIEW_COPY_POLISH_IMPLEMENTATION
```

Do not combine all copy changes with export implementation unless the diff remains small and low-risk.

---

## 8. Risks and safety

Safety constraints:

```text
UI cleanup must not weaken privacy controls.
Export semantics must not silently change.
Scrub Key must remain clearly marked as sensitive.
Audit details must not disappear; they move to secondary layers.
Human review remains necessary.
The review table remains source of truth and fallback.
```

Specific risks:

| Risk | Mitigation |
|---|---|
| Hiding technical details too much | Keep details under `Audit en risico’s` / `Geavanceerd`, not removed. |
| Scrub Key becomes just another download | Separate Scrub Key into its own clearly warned group. |
| Export redesign changes payloads | Contract tests must assert labels/grouping only; payload semantics unchanged. |
| Users skip review because export looks polished | Keep pre-export reminder: export is based on checked replacement table. |
| DOCX hygiene warnings become invisible | Show compact risk summary and expand details on medium/high risk. |
| Too much UI in one implementation | Split export/download, debug collapse and copy polish packages. |

---

## 9. Follow-up workpackages

Recommended sequence:

```text
1. WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS
2. WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION
3. WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN
4. WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION
5. WP_REVIEW_COPY_POLISH_IMPLEMENTATION
6. WP_MVP_UI_APP_VERIFICATION_CLOSEOUT
```

Rules:

```text
No parallel edits to presidio_streamlit.py.
Keep export/download flow separate from review-flow cleanup.
First contract/spec, then implementation.
Avoid mixing Scrub Key/reinsert semantics into export UX polish.
```

### WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS

Tests/specification-only. Should verify:

- this plan exists;
- export step target is `Exporteer resultaat`;
- primary document export and secondary audit downloads are separated;
- Scrub Key is a separate warned group;
- no export semantics change is allowed;
- technical details remain available under audit/advanced sections.

### WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION

Small Streamlit implementation. Scope:

- group existing buttons;
- rename section and copy;
- move CSV/report under audit/technical expander;
- keep all existing download data/filenames/MIME types unchanged;
- do not alter Scrub Key, reinsert or review table behavior.

### WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN

Planning-only. Scope:

- decide exact placement of serial review governance captions;
- decide final label for serial review;
- decide exact advanced/audit nesting for technical recognition and DOCX hygiene.

### WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION

Small implementation package. Scope:

- rename `Serial review — experimentele reviewhulp`;
- hide governance captions from primary flow;
- rename technical expanders;
- keep all review controls and safety warnings available.

### WP_REVIEW_COPY_POLISH_IMPLEMENTATION

Small copy-only package. Scope:

- user-facing Dutch text polish;
- no control-flow changes;
- no export payload changes.

### WP_MVP_UI_APP_VERIFICATION_CLOSEOUT

Verification-only. Scope:

- Actions green;
- HF sync green;
- app screenshot verifies: no debug language in primary flow, export grouped, audit details still accessible.

---

## 10. Definition of Done for MVP UI cleanup

This area is good enough when:

```text
Normal users do not see debug language in the primary flow.
Export feels like one finished product step.
Technical details are available but secondary.
Review remains safe and controllable.
Scrub Key remains clearly marked and safe.
Download buttons are logically grouped.
Audit/report downloads are not visually equal to the main document export.
No regression in import/scrub/review/export/reinsert.
No export semantics change happened silently.
Human review remains necessary.
```

---

## 11. Active direction decision

Decision:

```text
Pause new recall/benchmark follow-up packages temporarily and prioritize MVP UI cleanup/export redesign.
```

Reason:

```text
The app must move from a prototype/debug interface toward a professional MVP workflow.
```

Consequence:

```text
Next packages focus on export/download UX and hiding/collapsing debug details without weakening safety controls.
```

This does not undo the recall/benchmark work. It parks it until UI/export quality is back in the active line.

---

## 12. Next recommended step

Next package after separate coordinator approval:

```text
WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS
```

Do not start automatically.
