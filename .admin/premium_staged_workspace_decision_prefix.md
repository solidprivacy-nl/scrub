## 2026-08-08 — D043 — Freeze Premium Standard as a single-page staged document workspace

Status: accepted product/UX architecture direction; implementation candidate subject to normal independent assurance.

Decision:

```text
For the Standard anonymization core flow, use one persistent document workspace containing Toevoegen → Controleren → Downloaden. Keep all three stage headers visible, allow exactly one expanded/dominant stage at a time, collapse completed stages to compact summaries, keep future stages passive, auto-advance after successful completion, and allow explicit return to an earlier stage with fail-closed downstream invalidation.
```

Explicitly rejected for Standard:

```text
Toevoegen page → Controleren page → Downloaden page
```

The three core stages are states of the same document, not three separate routed screens. Also reject a conventional long Streamlit form rebuilt as a tree of independent or nested expanders.

First-principles reason:
- the scarce resource is user attention during a privacy-sensitive review task;
- Scrub is iterative: review can legitimately send the user back to input/profile correction;
- the interface must preserve confidence about source identity, completed work and whether downstream state is still current;
- page routing maximizes isolation but removes spatial workflow context and adds state-restoration/routing complexity;
- one staged workspace preserves the cognitive benefit of one task at a time while representing document state directly;
- the model maps naturally to the merged source/processed/review/export generation lineage in `premium_core_flow_state.py`.

Binding interaction consequences:
- one dominant primary action per active stage;
- no permanent configuration sidebar in Standard;
- completed stage summaries contain orientation/trust information only, not mini-forms;
- future stages show status rather than disabled control forests;
- successful processing opens Controleren automatically;
- explicit review completion opens Downloaden automatically;
- earlier processing-affecting edits invalidate downstream review/export state before those results can be presented as current;
- no nested core-flow accordion hierarchy in Standard;
- stage surfaces should read as application panels even when Streamlit primitives are used internally.

Current workpackage consequence:
- insert `SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE` before further production integration in `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION`;
- retain PR #85's compatible pure helper/test work;
- require PR #85 to incorporate the staged-workspace semantics before touching/merging production `presidio_streamlit.py` integration;
- continue sequentially with Input, Review, Export, Expert parity and live app closeout packages.

Safety boundary:
- this decision changes presentation architecture, not anonymization semantics;
- recognizers, thresholds, review authority, direct masking, export bytes/names/MIME, Scrub Key, reinsert, audit and human-review requirements remain unchanged;
- Standard is lower cognitive load, not lower safety.

Evidence:
- coordinator/user approval on 2026-08-08 Europe/Amsterdam after explicit first-principles comparison;
- `PREMIUM_STAGED_WORKSPACE_DECISION.md`;
- `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`;
- merged Premium UI contract and state model.

---

