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

`GET /api/v1/realtime/eventos` is public to the global guard but requires a query `token`. The controller verifies JWT signature/expiry only; unlike normal bearer routes, it does not resolve active/known user state or apply a role. A missing, invalid, or expired token returns 401 through the standard error body.

Each SSE frame is `{type,data}`. `type` equals `data.tipo`; `data.tipo` is `evento.novo|evento.tratado|heartbeat`, `data.origem` is `api|banco|polling|sistema`, `data.em` is an ISO-8601 string, and `data.refId`/`data.situacao` are optional strings. The frame is invalidation only and causes the client to re-fetch the API.

Backend LISTEN/NOTIFY failure falls back to backend polling of `logs`; browser stream failure relies on EventSource reconnection. No separate client polling fallback or durable delivery guarantee is asserted.

## Purpose, Owned Entities, and Workflows
**Purpose:** reduce stale client views without creating a second data authority. **Owned/orchestrated entities:** invalidation signal and client refresh coordination. **Workflows/capabilities:** issue SSE change signal, heartbeat, deduplicate, re-fetch API, use backend polling when database notifications are unavailable, and let EventSource reconnect the browser stream. **Invariants/validation/auth:** signal has no business payload authority; API read remains authoritative. **Observed contracts:** the wire envelope above is evidenced; no client polling fallback or delivery SLO is claimed.

## Cross-Module Considerations and Failure Modes
Events and treatments cause refresh-relevant changes. Backend source degradation uses polling; browser stream interruption relies on EventSource reconnection. Neither path may manufacture event state.
