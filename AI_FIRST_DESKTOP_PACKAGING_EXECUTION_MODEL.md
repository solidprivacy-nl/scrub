# AI-first desktop packaging execution model

Status: approved roadmap-alignment direction; implementation remains gated.  
Repository: `solidprivacy-nl/scrub`  
Workpackage: `SCRUB-WP_AI_FIRST_DESKTOP_PACKAGING_ROADMAP_ALIGNMENT`

## Purpose

This document records how extensive AI-agent autonomy may reduce the cost and lead time of the final Windows desktop/offline distribution line without transferring signing, security-claim or public-release authority to an autonomous worker.

## Product target

```text
One signed setup.exe for individual installation
One signed MSI for managed organizational deployment
Tauri desktop shell
Bundled local Python/Presidio engine as a PyInstaller onedir sidecar
All required models and assets available offline
Loopback-only communication on the same PC
No required cloud processing or document telemetry
```

The existing portable Python launcher remains a technical validation asset. It is not the intended low-friction end-user distribution.

## Cost-substitution assumption

For the first professional installer implementation, approximately 60–70% of development and integration labor may be executed by scoped AI agents with extensive rights inside isolated build and test environments. Repetitive later release work may be automated at approximately 75–90%.

Indicative planning ranges:

| Cost area | Conventional planning range | AI-first planning range / retained cost |
| --- | ---: | ---: |
| Development and integration | EUR 20,000–54,000 | EUR 8,000–24,000 |
| Agent/build compute | not separated | EUR 1,000–4,000 |
| Code signing | retained | approximately EUR 120–300/year |
| Windows test devices | retained | EUR 0–1,500 initial |
| Targeted independent security review | retained | EUR 5,000–15,000 |
| Broader penetration test/retest | retained when required | EUR 15,000–30,000 |

These values are planning assumptions, not quotations.

## Agent authority model

### Development agents

May modify the repository, install approved local SDKs in disposable environments, run tests, build unsigned artifacts and open pull requests.

### Windows test agents

May provision disposable VMs, install and remove release candidates, run offline and network evidence checks, inspect temp/log/cache behavior and execute synthetic workflow tests.

### Release automation

May prepare signing jobs and release candidates after CI is green, but must not possess unrestricted long-lived publisher credentials or independently publish production releases.

### Human release authority

Must approve signing, publication, product security claims, user acceptance and any change to export, Scrub Key or document-processing semantics.

## Required safeguards

- synthetic documents and Scrub Keys only;
- least-privilege credentials;
- protected signing/release environment;
- no one agent with unrestricted repository, signing and public-release authority;
- reproducible builds, checksums and SBOM;
- no silent telemetry or runtime model downloads;
- no weakening of privacy/review controls;
- independent validation before strong local-only production claims.

## Recommended Phase 9 sequence

```text
1. Desktop distribution and local-only security contract
2. Offline dependency, native-library and model inventory
3. PyInstaller onedir engine-sidecar packaging spike
4. Tauri shell and sidecar lifecycle proof
5. Network, temp-file, logging, crash and endpoint-security validation
6. Signed setup.exe and MSI release candidate
7. Managed Windows pilot, upgrade, rollback and uninstall validation
8. Independent security review and quality-gate closeout
```

## Implementation gate

This document does not open Phase 9. Installer work remains gated by:

1. `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`;
2. `SCRUB-WP_MVP_AUDIT_RESIDUAL_RISK_EVIDENCE`;
3. `SCRUB-WP_MVP_PHASE6_QUALITY_GATE_CLOSEOUT`;
4. explicit coordinator approval.
