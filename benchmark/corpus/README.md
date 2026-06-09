# Benchmark corpus

Status: WP20 corpus-first synthetic fixtures.

This directory contains messy synthetic Dutch professional benchmark documents for later recall/precision work.

## Structure

```text
benchmark/corpus/legal/   Dutch legal process-style fixtures
benchmark/corpus/zorg/    Dutch care/healthcare operational fixtures
benchmark/corpus/mixed/   Mixed legal-care professional fixtures
benchmark/gold/README.md  Future gold-label direction only
```

## Synthetic-only rule

All files in this corpus must be synthetic. Do not add real case files, real client data, real care records, real BSNs, real IBANs, real customer examples or copied confidential documents.

## WP20 boundary

WP20 creates corpus source text only. It does not create the full gold-label schema, offset sidecars, a runner, CI scorecard, recognizer changes, UI changes or production gates.

## Current fixture set

- `legal/legal_process_messy_001.txt`
- `zorg/care_operations_messy_001.txt`
- `mixed/legal_care_mixed_messy_001.txt`

The fixtures intentionally contain messy formatting, repeated values, legal/care context terms to preserve, and false-positive traps such as dates, times, amounts and legal article references.
