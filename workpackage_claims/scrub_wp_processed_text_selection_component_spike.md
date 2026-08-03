# Workpackage claim — SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE

Repository: `solidprivacy-nl/scrub`  
Branch: `scrub-processed-text-selection-component-spike`  
Claimed: 2026-08-04 01:00 Europe/Amsterdam  
Status: in_progress

## Dependency gate

- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT` completed and merged through PR #60.
- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL` completed and merged through PR #61 as `3e0e5be9457654d3dfb6e52e0e701a08b438a4d9`.
- Final action-model regression #1975: 1106 tests passed in 10.00s.

## Goal

Prove a local, bidirectional Streamlit v1 component can safely render the two review panes, preserve synchronized scrolling, calculate exact UTF-16 selection offsets around highlight nodes, expose an accessible context-menu/visible fallback, receive server inspection results and emit bounded inspect/commit intent events without mutating the replacement table or main application.

## Scope

- add a standalone custom-component wrapper using the currently pinned Streamlit 1.39 v1 API;
- add committed local HTML, CSS and JavaScript assets with no runtime build step;
- implement a minimal local Streamlit component protocol bridge;
- render source and processed text through text nodes, with server-supplied highlight spans;
- keep synchronized percentage-based scrolling;
- calculate processed-text UTF-16 selection offsets across plain and marked text nodes;
- reject selections outside the processed pane or intersecting marked content;
- expose right-click, Shift+F10/context-menu-key and visible `Masker selectie` entry points;
- display server-owned inspection results and emit commit intents for quick types;
- add a standalone synthetic demo which never applies a row;
- add pure Python and dependency-free Node tests for protocol, offsets, event schema, accessibility and security boundaries;
- document the proof and whether table integration may proceed.

## Boundaries

- non-mutating spike only;
- no import or use from `presidio_streamlit.py` or the current production side-by-side renderer;
- no replacement-table/session-state mutation outside the standalone demo's transient inspection display;
- no call to `commit_manual_mask` and no row construction from the component demo;
- no export, Scrub Key, reinsert, recognizer or profile change;
- no Streamlit upgrade or new runtime dependency;
- no external scripts, fonts, styles, analytics, fetch calls or browser persistence;
- no occurrence-specific masking;
- current static review renderer and manual form remain untouched.
