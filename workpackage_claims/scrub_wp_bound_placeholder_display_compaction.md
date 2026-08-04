# Workpackage claim — SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION

Repository: `solidprivacy-nl/scrub`
Status: completed in GitHub; deployment synchronization and app verification pending
Claimed at: 2026-08-04 22:44 Europe/Amsterdam

## Goal

Make bound placeholders substantially easier to read in the review UI without shortening or changing the underlying document binding.

## Contract boundary

- Full internal/export token remains `[LABEL_B[A-Z2-7]{16}_INDEX]` or the manual equivalent.
- Review presentation may show a compact alias such as `[LOCATIE_02]`.
- The component must retain exact source UTF-16 offsets after compacted marked spans.
- Selections intersecting placeholders remain blocked.
- Full tokens remain available to server validation, the authoritative replacement table, exported documents, Scrub Key and reinsert.
- No binding entropy, schema, digest, filename, MIME, recognizer, profile or cloud-processing change.
- Static fallback and interactive component must fail safely.

## Execution order

1. Freeze display and offset contracts in tests.
2. Add pure display-segment helper behavior.
3. Integrate the interactive component and static fallback.
4. Run full regression and frontend tests.
5. Merge only when green, verify Hugging Face synchronization, then request focused app verification.
