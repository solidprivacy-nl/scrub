# Processed-text selection component spike

Status: implemented as an isolated non-mutating proof  
Workpackage: `SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE`  
Repository: `solidprivacy-nl/scrub`  
Date: 2026-08-04 Europe/Amsterdam

## Purpose

This spike proves that the approved selection-driven correction interaction can be transported through the currently pinned Streamlit 1.39 Components v1 API without changing the production review flow or mutating a replacement table.

The proof covers:

```text
render source and processed text
→ preserve server-owned highlights
→ select text in the processed pane
→ calculate exact UTF-16 offsets
→ invoke right-click, keyboard or visible fallback
→ emit inspect_selection
→ display a server-owned inspection result
→ choose a quick type
→ emit commit_manual_mask intent
```

The final step is intentionally an **intent only**. The standalone demo never calls `commit_manual_mask`, never creates a manual row and never writes to the product's review table, export, Scrub Key or reinsert state.

## Architecture

### Python wrapper

`processed_text_selection_component.py`:

- declares a local Streamlit v1 component lazily through `components.declare_component(path=...)`;
- remains importable when Streamlit is not installed because the import occurs only when rendering;
- validates Python code-point highlight spans;
- converts highlight spans to browser UTF-16 code-unit offsets;
- sends JSON-only source text, processed text, highlights, scope, hash, inspection result and scroll restoration values;
- returns only a raw inspect or commit-intent event;
- contains no table or session-state mutation.

### Local frontend

`frontend/processed_text_selection_component/` contains only committed local assets:

- `index.html`;
- `styles.css`;
- `streamlit_bridge.js`;
- `component_core.js`;
- `component.js`;
- `NOTICE.md`.

There is no React, npm dependency, runtime build step, CDN, external font, remote script or remote stylesheet.

### Minimal protocol bridge

The local bridge uses only the Streamlit Components v1 iframe message types required for this proof:

```text
listen: streamlit:render
send:   streamlit:componentReady
send:   streamlit:setFrameHeight
send:   streamlit:setComponentValue
```

The bridge is independently implemented and attributed in `NOTICE.md`. No external component library is loaded at runtime.

## Unicode and coordinate handling

Python indexes Unicode code points. JavaScript DOM ranges and string indexes use UTF-16 code units. Passing Python highlight indexes unchanged would make every later position incorrect when supplementary characters occur before a highlight.

The wrapper therefore converts every validated Python span:

```text
Python code-point start/end
→ UTF-16LE code-unit length of the prefix
→ browser highlight start/end
```

The frontend:

- rejects highlight boundaries inside surrogate pairs;
- renders plain and marked segments from UTF-16 coordinates;
- derives a selection offset by creating a DOM `Range` from the processed-pane start to each endpoint;
- uses `Range.toString().length`, which follows JavaScript UTF-16 length semantics;
- trims outer whitespace while adjusting UTF-16 offsets;
- marks a selection invalid when it intersects a server-supplied highlight.

Tests include an emoji before a highlighted range, accented text, combining marks and selections across plain and `<mark>` text nodes.

## Safe rendering

Document text is inserted only through:

- `document.createTextNode(...)`;
- `.textContent`;
- explicitly created fixed DOM elements.

The component contains no:

- `innerHTML`;
- `eval` or dynamic function construction;
- `document.write`;
- external network call;
- browser storage;
- cookie or URL persistence;
- analytics or telemetry.

## Interaction proof

### Entry points

The processed pane supports:

- right-click with a valid unmarked selection;
- Shift+F10;
- the keyboard Context Menu key;
- visible `Masker selectie` button.

The native browser context menu remains available when no valid selection exists or the pointer is outside the processed selection path.

### Accessibility

The menu includes:

- `role="menu"` and `role="menuitem"`;
- Arrow Up/Down navigation;
- Home/End navigation;
- Enter/Space through native buttons;
- Escape close and focus restoration;
- visible focus outline;
- `role="status"` and `aria-live="polite"` feedback;
- no color-only state.

### Server-result binding

A server inspection result is reused only when its selection text matches the current browser selection, or when the browser selection was cleared by the Streamlit rerun. A newly selected different value cannot inherit an older type menu.

A new inspection token automatically reopens the result menu at the previous menu position. Repeated renders with the same token do not repeatedly reopen it.

## Standalone synthetic demo

`processed_text_selection_component_spike_demo.py` provides a separate technical app with:

- an emoji before a current highlighted placeholder;
- one existing synthetic replacement;
- the unmasked synthetic value `SYNTHETIC-ALFA` appearing twice;
- the real pure `inspect_selection` action model;
- transient replay and inspection state;
- explicit display of the latest raw event;
- validated commit-intent parsing only.

The demo deliberately imports no `commit_manual_mask` function and reports:

```text
replacement rows added: 0
production UI integrated: false
```

## Automated validation

Python tests verify:

- complete local asset set;
- lazy Streamlit import;
- Python-to-UTF-16 highlight conversion;
- invalid, overlapping and out-of-range span rejection;
- JSON component contract;
- no production imports;
- demo inspection-only boundary;
- no network, storage, dynamic-code or unsafe HTML paths;
- minimal Streamlit message protocol;
- accessibility and stale-inspection protections.

Dependency-free Node tests verify:

- UTF-16 boundaries and split-surrogate rejection;
- segmentation around marked nodes;
- offsets after marked text nodes;
- whitespace-trimmed selection offsets;
- marked-range intersections;
- deterministic event ID shape;
- inspect and commit-intent envelopes;
- scroll ratios and menu viewport clamping.

Initial standard PR run #1977 passed **1126 tests in 13.83s**. Clean post-governance run #1989 passed **1126 tests in 10.87s**.

A dedicated Streamlit 1.39 smoke run additionally validates:

- the complete regression suite with Streamlit installed;
- standalone demo script execution through `streamlit.testing.v1.AppTest`;
- local headless server startup;
- `_stcore/health` returning `ok`;
- root application HTML and startup logging.

## What this spike proves

The spike is sufficient to show that:

- a local bidirectional v1 component is feasible on Streamlit 1.39;
- text selection can use the same UTF-16 contract as the pure action model;
- highlight nodes do not inherently break offset accounting;
- an accessible context menu and visible fallback can emit bounded inspect/commit intent events;
- server inspection results can return through a Streamlit rerun;
- no frontend build system or new runtime dependency is required.

## What this spike does not prove

It does not yet prove:

- production integration with the current review table;
- row insertion and undo inside `presidio_streamlit.py`;
- live browser behavior in the deployed Hugging Face app;
- cross-browser behavior in Edge, Chrome and Firefox;
- end-to-end export, Scrub Key and reinsert after a selection action;
- occurrence-specific masking.

Those belong to the sequential integration, cross-flow and app-verification packages.

## Recommendation

When the spike regression and Streamlit smoke are green, proceed to:

```text
SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION
```

The integration must:

- preserve the existing static/manual path as rollback;
- process inspect and commit events through `selection_mask_action.py`;
- add rows only through the existing document-scoped manual-row flow;
- keep the review table authoritative;
- preserve export, Scrub Key and reinsert semantics;
- remain sequential because it touches the central review flow.
