# Benchmark reports

This directory is reserved for generated benchmark report artifacts.

WP23 adds a report-only entity-class scorecard builder that can write:

```text
benchmark/reports/entity_scorecard.json
benchmark/reports/entity_scorecard.md
```

WP24 adds a report-only false-negative residual-risk report builder that can write:

```text
benchmark/reports/false_negative_residual_risk_report.json
benchmark/reports/false_negative_residual_risk_report.md
```

Generated benchmark reports are intended for CI visibility and internal/support risk communication only.

They must not be interpreted as a production safety claim and they must not create a recall/precision threshold gate until a later approved workpackage defines one.

Only synthetic benchmark data may be used here. Do not store real legal, care, customer or personal data in generated reports.
