# UniNotas — Project Constitution

## UniNotas canonical target

**UniNotas** is the canonical product and `uninotas` is the core scope; `MonitorDeNotas` remains the technical repository name.

Namespaces: nestjs, react, vite, postgresql, prisma, docker, railway

Smart Notas is the target-planned source of truth for fiscal notes and documents. Unifast and Prosperar are distinct `FiscalIssuerContext` values, not tenants. After the adapter transition, PostgreSQL `logs` retains only integration-failure evidence and never becomes the fiscal-note source.

Current runtime evidence and target-planned architecture are separate axes from PACED lifecycle/status. FastPay (Routerfy) -> n8n -> Smart Notas is the approved external flow; external writer/filter behavior for `logs` is unknown unless evidenced.

## Authority

1. This Foundation owns stable, product-specific documentation.
2. An explicit approved TODO owns bounded delivery evidence.
3. Product code, tests, and runtime configuration are evidence for current behavior.
4. `delphi-ai` owns PACED method, workflows, and guards; this repository links to it instead of copying it.

## Verified topology

NestJS, React/Vite, PostgreSQL/Prisma, Docker, and Railway are observed product technologies. Runtime or deployment changes require a separate approved TODO.

## Invariants

- Current `logs` is an external, read-only, mixed emission-event projection containing success, pending, and error records; its writer, ingestion, and filter semantics are unknown. Smart Notas becomes the complete fiscal-note/document authority only after the planned capability transition.
- The local development `logs` replica is derived, disposable, and non-authoritative. Only the explicit mirror tooling may populate it; this establishes no source ownership and authorizes no application writes to production `logs`.
- [Events](modules/events-and-classification.md) owns read projections, [treatments](modules/treatments-and-history.md) owns treatment writes, and [identity](modules/identity-and-team.md) owns user writes.
- `ref_id` is correlation, never uniqueness proof.
- The latest treatment supplies effective status; `PENDENTE` reopens original status.
- JWT authentication, profiles, and last-admin protection are product behavior.
- No business tenancy is inferred. `EnvironmentType=landlord` is PACED technical vocabulary only.

## Delivery governance

Every implementation has an active approved TODO, evidence, and an authority guard `go`. Every review finding is classified through the project taxonomy in [TODO governance](todos/README.md#review-finding-classification); promotion requires no open `release-blocker` and an explicit TODO owner for every real non-blocking follow-up. Backlog is not execution authority. Completed TODOs retain history but do not override canonical owners.
