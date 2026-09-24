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

`GET /monitoramento/erros` is open when no monitoring credential is configured; when configured, a missing or mismatched query/header credential is rejected. Database unavailability is an unavailable result, distinct from a successful summary with zero errors; `alertarEm` is an observed request condition for 503, not an alert threshold or service-level objective.

```json
{"base_path":"/api/v1","route":"GET /monitoramento/erros","authorization":"open when MONITORAMENTO_TOKEN unset; otherwise query token or x-monitor-token header; missing|mismatch=401","responses":"200 summary; 503 database unavailable or alertarEm reached","errors":"standard error body","cache":"no-store"}
```

## Purpose, Owned Entities, and Workflows
**Purpose:** provide an external operational check from observed event-summary semantics. **Owned/orchestrated entities:** monitoring summary projection. **Workflows/capabilities:** query rolling window and distinguish no errors from data-store unavailability. **Invariants/validation/auth:** reuse summary semantics; do not recast failure as zero. **Observed contracts:** monitoring and logs services are evidenced; alert endpoint, threshold, and SLO are unknown/not asserted.

## Cross-Module Considerations and Failure Modes
Events/classification owns source semantics. Database unavailability produces an unavailable outcome, not a successful empty result.
