# Operational Monitoring

## Module Intent & Boundaries
- **Core scope:** `monitor-de-notas`
- **Subscope:** `operational-monitoring`
- **EnvironmentType:** `landlord` (PACED technical adapter only; no business tenancy)
- **Out-of-scope guardrails:** Claiming availability from an empty result or changing runtime monitoring.
- **Dependency boundaries:** Reuses the events summary semantics for an external monitor or alert.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Current`
- **Last Canonicalization Review:** `TODO-uninotas-foundation-project-rebase`
- **Remaining Migration Scope:** `none`

## Specification
Owns the documented operational summary contract. A database failure is distinct from a successful zero-error window; time window and limits remain explicit.

## Observed Monitoring Contract

`GET /monitoramento/erros` requires the configured monitoring credential and returns a bounded error-window summary. A missing or mismatched credential is rejected. Database unavailability is an unavailable result, distinct from a successful summary with zero errors; this module does not assert an alert threshold or service-level objective.

## Purpose, Owned Entities, and Workflows
**Purpose:** provide an external operational check from observed event-summary semantics. **Owned/orchestrated entities:** monitoring summary projection. **Workflows/capabilities:** query rolling window and distinguish no errors from data-store unavailability. **Invariants/validation/auth:** reuse summary semantics; do not recast failure as zero. **Observed contracts:** monitoring and logs services are evidenced; alert endpoint, threshold, and SLO are unknown/not asserted.

## Cross-Module Considerations and Failure Modes
Events/classification owns source semantics. Database unavailability produces an unavailable outcome, not a successful empty result.
