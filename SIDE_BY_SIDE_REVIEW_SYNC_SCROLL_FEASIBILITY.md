# WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_FEASIBILITY — Synchronized scroll feasibility review

Status: feasibility/documentation-only  
Repository: `solidprivacy-nl/scrub`

## 1. Executive summary

Synchronized scrolling is a valid UX wish for the side-by-side review surface, but it should not be implemented directly in the current Streamlit MVP flow.

Current state:

```text
Brontekst links | Verwerkte tekst rechts
                | Beide panelen even hoog
                | Rechter verwerkte/highlight-pane scrollt lokaal
```

Coordinator feedback confirms:

```text
height is now equal, but scrolling is not synchronized
```

Recommendation:

```text
Do not implement synchronized scrolling in the current Streamlit UI package.
Keep equal-height independent panes for now.
Only consider synchronized scrolling later through a separate approved spike with explicit contracts, security review and fallback behavior.
```

This document does not implement synchronized scroll, does not change UI code and does not change product behavior.

## 2. Why synchronized scroll is attractive

Synchronized scroll could help the user compare source and processed text while reading long documents.

Expected UX benefit:

- less manual matching between left and right panes;
- easier comparison of corresponding passages;
- more document-like review experience;
- better support for long source/processed content.

However, this benefit only holds if source and processed text remain structurally aligned.

## 3. Why synchronized scroll is risky here

The source and processed panes are not guaranteed to have a one-to-one line mapping.

Reasons:

- sensitive values may be replaced by shorter or longer placeholders;
- multiple values may be collapsed into a smaller token;
- line wrapping differs between panes;
- highlights add markup and can affect visual spacing;
- source and processed text may not have equal paragraph lengths;
- future replacement-review actions could change the right pane without changing the left pane.

Naive scroll syncing by percentage can therefore create false alignment:

```text
left scroll position 40% != same legal/contextual passage on right 40%
```

False visual alignment is risky in a privacy/legal review product because it may make the reviewer believe two passages correspond when they do not.

## 4. Streamlit feasibility assessment

### Option A — Keep independent scroll panes

Status:

```text
current safe baseline
```

Pros:

- works in plain Streamlit;
- no custom component;
- no JavaScript injection;
- no dependency changes;
- no review table behavior change;
- no export/Scrub Key/reinsert impact;
- simple fallback when documents are not aligned.

Cons:

- user must manually scroll both panes;
- less polished than synchronized document comparison;
- long documents remain harder to compare.

Risk level:

```text
low
```

Recommendation:

```text
Use as MVP baseline.
```

### Option B — Percentage-based synchronized scroll with custom component

Concept:

```text
When the user scrolls one pane, JavaScript sets the other pane to the same scroll percentage.
```

Pros:

- intuitive when panes have similar structure;
- easier reading in simple cases;
- closer to professional diff-view behavior.

Cons:

- requires custom HTML/JavaScript or a Streamlit component;
- source/processed text may not align by percentage;
- must handle accessibility and keyboard navigation;
- must not leak document text to a third-party component;
- requires careful escaping of document text;
- requires fallback when sync is misleading;
- increases runtime/startup risk after the earlier static-highlight startup mutation problems.

Risk level:

```text
medium/high
```

Recommendation:

```text
Do not implement in the current MVP package. Consider only as a separate spike.
```

### Option C — Anchor-based synchronized scroll

Concept:

```text
Use paragraph, sentence or token anchors to align corresponding sections instead of raw scroll percentage.
```

Pros:

- more semantically accurate than percentage sync;
- can avoid some false alignment;
- may support later review-item navigation.

Cons:

- requires building and testing alignment anchors;
- replacements and masking can disturb anchors;
- sentence/paragraph segmentation adds complexity;
- may require a custom renderer anyway;
- false alignment remains possible;
- harder to keep explainable to users.

Risk level:

```text
high
```

Recommendation:

```text
Not for current Streamlit MVP. Reconsider after core workflow is stable.
```

### Option D — Selected-item focus instead of synchronized scroll

Concept:

```text
Serial review selects an item; the side-by-side surface shows relevant context around that item.
```

Pros:

- fits current serial review model;
- does not need synchronized scroll;
- can be helper-driven and tested;
- keeps review table source of truth;
- helps users navigate without pretending whole-document alignment is exact.

Cons:

- not the same as free synchronized scrolling;
- still needs careful context rendering;
- may require additional UI work later.

Risk level:

```text
medium, lower than full synchronized scroll
```

Recommendation:

```text
Prefer this before synchronized scroll if more guided comparison is needed.
```

## 5. Security and privacy considerations

Any synchronized scroll implementation must preserve these rules:

- no cloud document processing;
- no third-party document-rendering service;
- no dependency that sends text out of the session;
- no raw user document text injected into unsafe HTML;
- all document text must be escaped before rendering;
- no Scrub Key writes;
- no Scrub Key schema changes;
- no export/download behavior changes;
- no reinsert behavior changes;
- no review table mutation;
- no automatic replacement.

A custom component may be acceptable later only if:

- it runs locally inside the Streamlit app context;
- it receives only the text already displayed in the app;
- it does not persist or transmit content;
- it has contract tests for escaping and boundary behavior;
- the app has a clear fallback when the component fails.

## 6. UX recommendation

For the current MVP:

```text
Keep equal-height independent panes.
Add no synchronized scroll claim.
Do not make users think passages are aligned when they may not be.
```

If users still struggle, prefer a lower-risk intermediate step:

```text
selected review item -> focused context in source and processed pane
```

This matches the existing serial review concept and avoids global false alignment.

## 7. Required contracts before any future sync implementation

Before implementation, create contract tests that require:

1. synchronized scroll is explicitly opt-in or separately approved;
2. implementation must not use cloud processing;
3. implementation must not add export/download behavior changes;
4. implementation must not write or change Scrub Key data;
5. implementation must not change reinsert behavior;
6. implementation must not mutate the review table;
7. implementation must not trigger automatic replacement;
8. all document text rendered through HTML must be escaped;
9. fallback UI exists when sync is unavailable;
10. no claim is made that source and processed passages always correspond exactly;
11. sync is disabled or clearly bounded when alignment cannot be trusted;
12. custom component implementation requires separate explicit coordinator approval.

## 8. Explicitly blocked by this feasibility package

This package does not approve:

- synchronized scroll implementation;
- custom Streamlit component rendering;
- JavaScript injection;
- click-to-mark;
- advanced editor;
- full-document marking;
- review table behavior changes;
- replacement behavior changes;
- Scrub Key writes;
- Scrub Key schema changes;
- export blocking;
- export/download behavior changes;
- reinsert behavior changes;
- dependency changes;
- cloud processing;
- real data.

## 9. Recommended next steps

Immediate:

```text
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION_VERIFY
```

Close out the current side-by-side implementation and height fix first after green Actions/Hugging Face sync and app screenshot.

Only if the coordinator still wants synchronized scroll after that:

```text
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_CONTRACT_TESTS
```

Later, only after separate explicit coordinator approval:

```text
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_SPIKE
```

The spike should be a contained prototype, not a production feature, and must include a fallback to independent panes.

## 10. Final recommendation

Do not implement synchronized scrolling now.

The current equal-height independent scroll panes are the safer MVP UX baseline. They solve the visual imbalance without introducing the false-alignment and custom-component risks of synchronized scrolling.
