# Realtime Invalidation

## Module Intent & Boundaries
- **Core scope:** `monitor-de-notas`
- **Subscope:** `realtime-invalidation`
- **EnvironmentType:** `landlord` (PACED technical adapter only; no business tenancy)
- **Out-of-scope guardrails:** Treating SSE messages as data truth or promising durable delivery.
- **Dependency boundaries:** SSE signals API, optional database notification, or polling; clients re-fetch the API.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Current`
- **Last Canonicalization Review:** `TODO-uninotas-foundation-project-rebase`
- **Remaining Migration Scope:** `none`

## Specification
Owns change invalidation semantics. Heartbeat and deduplication support the channel, while polling is an explicit fallback. No event payload replaces a fresh API read.

## Observed Realtime Message Contract

`GET /realtime/eventos` is an authenticated SSE stream that requires a valid stream token. Observed messages carry `tipo`, `origem`, and `em`; change messages cause a client API re-fetch, while `heartbeat` maintains channel liveness. Invalid or expired stream tokens are rejected. LISTEN/NOTIFY interruption or stream failure degrades to polling and re-fetch, never to an authoritative event payload.

```json
{"base_path":"/api/v1","route":"GET /realtime/eventos?token=<JWT>","authorization":"validated query JWT","sse":{"type":"evento.tipo","data":{"tipo":"string","origem":"string","em":"ISO-8601","refId":"optional string","situacao":"optional string"}},"errors":"missing|invalid|expired token=401"}
```

## Purpose, Owned Entities, and Workflows
**Purpose:** reduce stale client views without creating a second data authority. **Owned/orchestrated entities:** invalidation signal and client refresh coordination. **Workflows/capabilities:** issue SSE change signal, heartbeat, deduplicate, re-fetch API, and fall back to polling. **Invariants/validation/auth:** signal has no business payload authority; API read remains authoritative. **Observed contracts:** the wire envelope above is evidenced; no delivery SLO is claimed.

## Cross-Module Considerations and Failure Modes
Events and treatments cause refresh-relevant changes. SSE interruption degrades to polling/re-fetch; it must not manufacture event state.
