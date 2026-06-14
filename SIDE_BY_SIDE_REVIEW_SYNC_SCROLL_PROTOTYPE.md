# WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE

Status: prototype-only.

Prototype file:

```text
prototypes/side_by_side_sync_scroll_prototype.html
```

## Purpose

This package adds an isolated browser concept for two side-by-side panes that can scroll together.

The prototype demonstrates:

- source text left;
- processed text right;
- equal-height panes;
- highlighted placeholders in the right pane;
- a `Synchroon scrollen` checkbox;
- sync on/off fallback.

## Boundary

This prototype is not connected to the normal Scrub Legal app flow.

It does not change:

- production Streamlit UI;
- review table behavior;
- replacement behavior;
- Scrub Key behavior;
- export/download behavior;
- reinsert behavior.

It uses only synthetic content.

## UX note

The prototype proves that the interaction can work visually. It does not prove that source and processed passages always match semantically after masking or replacement.

## Next safe step

If this concept is useful, create contract tests before any real implementation spike.
