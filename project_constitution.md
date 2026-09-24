# Monitor de Notas — Project Constitution

## Authority

1. This Foundation owns stable, product-specific documentation.
2. An explicit approved TODO owns bounded delivery evidence.
3. Product code, tests, and runtime configuration are evidence for current behavior.
4. `delphi-ai` owns PACED method, workflows, and guards; this repository links to it instead of copying it.

## Verified topology

NestJS, React/Vite, PostgreSQL/Prisma, Docker, and Railway are observed product technologies. Runtime or deployment changes require a separate approved TODO.

## Invariants

- Routerfy owns and writes the authoritative production `logs`; Monitor de Notas reads that external table only and writes only `monitor_usuarios` and `monitor_tratamentos`.
- The local development `logs` replica is derived, disposable, and non-authoritative. Only the explicit mirror tooling may populate it; it never transfers ownership from Routerfy or authorizes application writes to production `logs`.
- [Events](modules/events-and-classification.md) owns read projections, [treatments](modules/treatments-and-history.md) owns treatment writes, and [identity](modules/identity-and-team.md) owns user writes.
- `ref_id` is correlation, never uniqueness proof.
- The latest treatment supplies effective status; `PENDENTE` reopens original status.
- JWT authentication, profiles, and last-admin protection are product behavior.
- No business tenancy is inferred. `EnvironmentType=landlord` is PACED technical vocabulary only.

## Delivery governance

Every implementation has an active approved TODO, evidence, and an authority guard `go`. Every review finding is classified through the project taxonomy in [TODO governance](todos/README.md#review-finding-classification); promotion requires no open `release-blocker` and an explicit TODO owner for every real non-blocking follow-up. Backlog is not execution authority. Completed TODOs retain history but do not override canonical owners.
