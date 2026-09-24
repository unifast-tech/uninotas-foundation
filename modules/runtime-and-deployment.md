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
Owns topology documentation only. Changes to Docker, Railway, database configuration, or deployment require their own approved TODO and validation.

## Observed Runtime Contract

The observed runtime boundary composes NestJS, React/Vite, PostgreSQL/Prisma, Docker, and Railway. It supplies deployment topology only; it owns no API request/response, authorization, secret value, health, or availability contract.

## Purpose, Owned Entities, and Workflows
**Purpose:** preserve verified runtime navigation without taking runtime ownership. **Owned/orchestrated entities:** documented topology and configuration boundary only. **Workflows/capabilities:** build and deploy topology is observed through Docker/Railway configuration. **Invariants/validation/auth:** no secrets, health claims, endpoint contracts, SLOs, or runtime change are inferred. **Observed contracts:** NestJS, React/Vite, PostgreSQL/Prisma, Docker, and Railway files are the evidence.

## Cross-Module Considerations and Failure Modes
All modules depend on this topology as an observed boundary. Configuration/deployment failure requires runtime evidence and a separate approved TODO, not documentary substitution.
