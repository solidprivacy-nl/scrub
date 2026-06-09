# Handover — WP19 Recall benchmark specification

Repository: solidprivacy-nl/scrub  
Status: completed specification-only

## Summary

Created `RECALL_BENCHMARK_SPEC.md` to define how Scrub should measure recall and precision on messy synthetic Dutch legal and care documents. The specification focuses on the highest product risk: false negatives / missed sensitive data.

The work also updates the false-negative risk status, records WP19 completion in the workpackage queue, and adds a changelog entry.

## Files added

- `RECALL_BENCHMARK_SPEC.md`
- `handover/workpackages/20260609_2200_recall_benchmark_spec.md`

## Files changed

- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- No tests were added.
- No tests were changed.
- No test suite was run because this was a specification/test-design-only workpackage with no code changes.

## Validation status

- Documentation/specification review completed.
- Verified scope remained specification-only.
- Verified no recognizer logic, runner, UI, dependency, export or reinsert behavior was changed.

## GitHub Actions status

- Unknown at handover creation time. This was documentation-only; no tests were expected to be required.

## Hugging Face sync status

- Unknown at handover creation time. No app behavior changed.

## App verification status

- Not applicable. No UI behavior changed.

## Remaining risks

- R1 false negatives remains critical and only partially mitigated. WP19 defines the measurement approach, but no corpus, gold-label schema, runner or CI gate exists yet.
- Synthetic benchmark results will not prove real-world safety; human review and residual-risk reporting remain required.
- Future work must ensure context terms remain readable while sensitive values are still detected.

## Next recommended step

- WP20 — Synthetic messy Dutch legal/zorg benchmark corpus.
