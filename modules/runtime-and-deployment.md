# Runtime and Deployment

## Module Intent & Boundaries
- **Core scope:** `monitor-de-notas`
- **Subscope:** `runtime-and-deployment`
- **EnvironmentType:** `landlord` (PACED technical adapter only; no business tenancy)
- **Out-of-scope guardrails:** Runtime modifications, secret values, or health claims not evidenced by product configuration.
- **Dependency boundaries:** Observed Docker, Railway, NestJS, React/Vite, PostgreSQL, and Prisma configuration.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Current`
- **Last Canonicalization Review:** `TODO-uninotas-foundation-project-rebase`
- **Remaining Migration Scope:** `none`

## Specification
Owns observed topology and the public health-read contract. Changes to Docker, Railway, database configuration, deployment, or health behavior require their own approved TODO and validation.

## Observed Runtime Contract

The observed runtime boundary composes NestJS, React/Vite, PostgreSQL/Prisma, Docker, and Railway. Routerfy remains the owner and sole writer of the external production `logs` table, which the application reads only. Development may use a local `logs` replica that is derived, disposable, and non-authoritative; only the explicit `backend/prisma/espelhar.ts` mirror tool may populate it, against the local shape declared by `backend/prisma/sql/002_logs_dev.sql`. The replica cannot become a source of truth and does not authorize application or production writes. This module owns no secret value, availability target, or service-level objective.

## Observed Health Contract

`GET /api/v1/saude` is public and accepts no request body or query contract. It returns HTTP 200 `application/json` with `{status,banco,em}`: `status` is `ok` when the database probe succeeds and `degradado` otherwise; `banco` is `ok` or `indisponivel`; `em` is an ISO-8601 timestamp. Database probe failure is represented in that body and is not converted to 503 by this controller.

## Purpose, Owned Entities, and Workflows
**Purpose:** preserve verified runtime navigation and the bounded health-read contract. **Owned/orchestrated entities:** documented topology, configuration boundary, disposable local replica boundary, and health projection. **Workflows/capabilities:** build/deploy topology, explicit development mirroring, plus public API/database probe. **Invariants/validation/auth:** external production `logs` remains read-only to the application; the local replica is never authoritative; no secrets, availability claims, SLOs, or runtime change are inferred. **Observed contracts:** NestJS, React/Vite, PostgreSQL/Prisma, Docker, Railway, the explicit mirror tool/local DDL, and the health controller are the evidence.

## Cross-Module Considerations and Failure Modes
All modules depend on this topology as an observed boundary. Configuration/deployment failure requires runtime evidence and a separate approved TODO, not documentary substitution.
