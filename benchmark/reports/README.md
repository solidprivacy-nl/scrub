# Benchmark reports

This directory is reserved for generated benchmark report artifacts.

WP23 adds a report-only entity-class scorecard builder that can write:

```text
benchmark/reports/entity_scorecard.json
benchmark/reports/entity_scorecard.md
```

The generated scorecard is intended for CI visibility only. It must not be interpreted as a production safety claim and it must not create a recall/precision threshold gate until a later approved workpackage defines one.

Only synthetic benchmark data may be used here. Do not store real legal, care, customer or personal data in generated reports.
