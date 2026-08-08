# SolidPrivacy Scrub — Current execution status override

> **2026-08-08 15:28 Europe/Amsterdam**  
> This block supersedes lower current-status fields until the next Premium package transition. Historical package descriptions remain retained below.

## Premium UI execution queue

1. `SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE` — **COMPLETED / independently PASSed / PR #87 merged** as `d54eb06f9c6fea7c1f36cdb082b475c0d4666507`.
2. `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION` — **RELEASE_CANDIDATE_READY / independent assurance pending**, issue #84 / PR #85. Production `presidio_streamlit.py` integration is present. Clean runtime/product head `0e1a5fbb3d6c3b8f8293779e598ececd6ea4aa1d` passed 1225 tests in 12.55s; final post-administration exact-head CI remains mandatory before assurance.
3. `SCRUB-WP_PREMIUM_INPUT_STAGE_SIMPLIFICATION` — **QUEUED**, may start only after package 2 independently PASSes, merges unchanged, exact-main/deployment evidence is green and required App Shell verification is closed.
4. `SCRUB-WP_PREMIUM_REVIEW_STAGE_SIMPLIFICATION` — queued after Input Stage.
5. `SCRUB-WP_PREMIUM_EXPORT_STAGE_SIMPLIFICATION` — queued after Review Stage.
6. `SCRUB-WP_PREMIUM_EXPERT_PARITY_REGRESSION` — queued after the three stage packages.
7. `SCRUB-WP_PREMIUM_CORE_FLOW_APP_VERIFY_CLOSEOUT` — final live Premium gate.

### App Shell candidate scope now implemented

- top-level `Anonimiseren | Terugzetten`;
- global `Standaard | Expert`;
- one persistent `Toevoegen → Controleren → Downloaden` workspace;
- exactly one active Standard stage;
- completed summaries, passive future stages and explicit return;
- automatic Add → Review and explicit Review → Download progression;
- deterministic processing lineage, fail-closed invalidation and current-generation analysis/review caching;
- no permanent Standard settings sidebar;
- Expert-only `highlight` / `synthesize` choices are preserved and require Expert rather than being silently rewritten;
- legacy runtime patching cannot re-inject the retired form shell into the direct Premium source.

### Governance gate

Do **not** merge PR #85 or start shared Streamlit work for package 3 until a fresh independent `governance_release_assurance` reviewer records `PASS` on the final exact PR head. Implementation does not self-certify.

---

