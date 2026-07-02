# SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_PLAN

Status: completed as planning/design-only.

Repository: `solidprivacy-nl/scrub`

## 1. Purpose

This workpackage defines the next MVP interface simplification direction for the normal anonymization workflow.

Coordinator feedback:

```text
The interface still has too many elements, too many collapsible sections and too much form feeling. The main flow is not obvious enough. Buttons are stacked vertically. The product should move toward a premium less-is-more interface.
```

The goal is not to remove privacy controls. The goal is to move them into a calmer hierarchy:

```text
Primary path first. Secondary controls available. Audit/debug details outside the main path.
```

## 2. Current problem

The current app is functionally strong but visually and cognitively busy.

Observed issues:

- Too many expanders are visible in the main review path.
- The primary action sequence is not dominant enough.
- Buttons and downloads feel like a technical form rather than a guided product surface.
- Review, correction, export, Scrub Key and audit controls compete for attention.
- Advanced controls are technically useful but too close to the normal user path.
- The current UI still exposes too much implementation language and status detail at once.

This can make a first-time user ask:

```text
What do I do now?
Which of these controls matter?
Can I safely download already?
Do I need to open every section?
```

## 3. Product target

The normal anonymization flow should feel like:

```text
1. Voeg document toe
2. Controleer resultaat
3. Download veilig
```

The user should see one dominant path, not a long technical checklist.

Target principles:

1. **One main surface**: the side-by-side review remains the central review surface.
2. **Progressive disclosure**: advanced controls are grouped behind one or two clear secondary sections.
3. **Action grouping**: downloads become a compact action area, not a vertical button list.
4. **Review table remains available**: source of truth and fallback, but not visually dominant by default.
5. **Safety controls remain**: Scrub Key, audit, DOCX hygiene and warning/acknowledgement controls remain available.
6. **No silent semantic changes**: export/download/Scrub Key/reinsert behavior must not change as part of UI polish.

## 4. Proposed primary page hierarchy

### 4.1 Top area

Keep:

- Product title and short purpose statement.
- One concise prototype warning.
- Work-mode selector.

Reduce:

- Long helper copy near the top.
- Multiple secondary expanders before the user starts.

Target:

```text
Scrub Legal
Lokale juridische documentcontrole
[prototype/safety notice]
Werkmodus: Anonimiseren | Originele waarden terugzetten
```

### 4.2 Step 1 — Input

Primary visible elements:

- Upload/dropzone.
- Paste text area.
- One sample/document example control, collapsed or compact.

Keep sidebar controls available, but avoid making the main path depend on opening them.

Target feeling:

```text
Start with the document. Everything else is optional.
```

### 4.3 Step 2 — Review

Primary visible elements:

- Side-by-side review.
- Marker toggle.
- Short status line: number of replacements used for export.
- Simple manual missed-value entry.
- One compact fallback control: `Vervangingen bekijken en aanpassen`.

Move under one secondary section `Meer controleopties`:

- Waarom controleren?
- Extra controlehulpen.
- Mogelijk extra te controleren waarden.
- Stap voor stap controleren.
- Herbruikbare vervangingen.
- Geavanceerde details bij de vervangtabel.

Rationale:

The user should not have to visually process six separate expanders after every run.

### 4.4 Step 3 — Export

Primary visible elements should be grouped as cards or a compact action row:

```text
Document downloaden
[TXT] [DOCX] [PDF]

Veiligheidsbestanden
[Scrub Key] [Auditrapport]
```

Advanced/technical downloads stay available but grouped lower:

```text
Technische details en audits
```

Rules:

- Do not change download content.
- Do not change filenames.
- Do not change MIME types.
- Do not change Scrub Key JSON semantics.
- Do not remove audit/DOCX hygiene access.

## 5. What should be less prominent

The following are useful but should not compete with the primary path:

- detailed recognition internals;
- long review guidance blocks;
- technical replacement table details;
- DOCX hygiene audit details;
- audit/technical downloads;
- repeated governance captions;
- multiple separate expanders after the side-by-side view.

These should move to grouped secondary layers, not disappear.

## 6. Proposed next workpackages

### WP A — Review surface simplification contract tests

Title:

```text
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS
```

Purpose:

Add source-level UI contract tests before implementation.

Contracts:

- The normal flow keeps a three-step primary structure.
- The side-by-side panel remains central and visible after processing.
- Secondary review controls are grouped under one `Meer controleopties` layer.
- The replacement table remains reachable as source of truth/fallback.
- Export controls remain reachable.
- Scrub Key and audit controls remain reachable.
- No export/Scrub Key/reinsert semantics change.
- No new OCR/cloud/AI/Word-rendering behavior.

Expected files:

- `tests/test_review_surface_simplification_contracts.py`
- Optional small contract note: `REVIEW_SURFACE_SIMPLIFICATION_CONTRACTS.md`

### WP B — Review surface simplification implementation

Title:

```text
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION
```

Purpose:

Implement the calmer normal review surface directly in source.

Likely changes:

- Edit `presidio_streamlit.py` only after contract tests exist.
- Group secondary review controls under one clear expander.
- Shorten visible copy.
- Keep side-by-side review visible.
- Keep manual missed-value entry visible or near-visible.
- Keep replacement table available but less dominant.

Do not change:

- review table data model;
- replacement logic;
- export content;
- download filenames or MIME types;
- Scrub Key JSON;
- reinsert behavior;
- recognizers;
- benchmark thresholds;
- Docker/startup patch order.

### WP C — Export action layout contract tests

Title:

```text
SCRUB-WP_EXPORT_ACTION_LAYOUT_CONTRACT_TESTS
```

Purpose:

Protect a premium export/download presentation before implementation.

Contracts:

- Primary document downloads appear as a compact group.
- Scrub Key appears as a separate safety/security download group.
- Audit/technical outputs remain available but secondary.
- No file content, name or MIME change.

### WP D — Export action layout implementation

Title:

```text
SCRUB-WP_EXPORT_ACTION_LAYOUT_IMPLEMENTATION
```

Purpose:

Make download/export feel like a product action surface rather than a vertical form.

Likely changes:

- Visual grouping of document downloads.
- Clear separation between document outputs and security/audit artifacts.
- Short copy and consistent labels.

### WP E — Reinsert surface polish

Title:

```text
SCRUB-WP_REINSERT_SURFACE_POLISH_PLAN
```

Purpose:

Plan visual polish for the already simplified reinsert flow, after the normal anonymization surface is calmer.

## 7. Recommended immediate next package

Start with:

```text
SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_CONTRACT_TESTS
```

Reason:

The next implementation will likely touch `presidio_streamlit.py` and the review flow. Contract tests should define the safety boundary before editing the main UI.

## 8. Acceptance criteria for this plan

This plan is complete when:

- It defines the target primary review hierarchy.
- It identifies which elements move out of the primary path.
- It preserves safety and audit controls.
- It defines the next contract-test package before implementation.
- It avoids implementation in this planning package.

## 9. Out of scope

This plan does not authorize:

- UI implementation;
- export/download semantic changes;
- Scrub Key semantic changes;
- reinsert behavior changes;
- recognizer changes;
- benchmark/recalibration work;
- local packaging or installer work;
- OCR/cloud/AI/Word-rendering or page reconstruction;
- removal of review controls without fallback.

## 10. Parked issue

DOCX first-page footer text can appear near the end of the plain-text preview because headers/footers are extracted outside the main body. This is understood and parked. It is not part of this UX simplification plan unless reopened as a dedicated footer-preview context package.
