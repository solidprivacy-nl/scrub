# WP42D claim

Workpackage: `WP42D — Static highlight preview UI integration`

Status: `in_progress`

Repository: `solidprivacy-nl/scrub`

Claimed by: `ChatGPT webinterface worker`

Explicit coordinator approval: user said `Please continue` after WP42D was presented as the next UI step requiring explicit approval.

Scope:

- Integrate the existing static highlight preview helper as a small experimental read-only UI panel.
- Keep the existing review table authoritative.
- Preserve export, Scrub Key, reinsert and helper runtime semantics.
- Add/adjust static tests for the UI integration boundary.

Do not change:

- export/download semantics;
- Scrub Key schema or behavior;
- reinsert behavior;
- authoritative review decision mutation from highlights;
- dependencies;
- cloud processing;
- real data;
- broad document-centric UI rewrite;
- click-to-mark sensitive text.
