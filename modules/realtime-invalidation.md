# Realtime Invalidation

## Module Intent & Boundaries
- **Core scope:** `monitor-de-notas`
- **Subscope:** `realtime-invalidation`
- **EnvironmentType:** `landlord` (PACED technical adapter only; no business tenancy)
- **Out-of-scope guardrails:** Treating SSE messages as data truth or promising durable delivery.
- **Dependency boundaries:** SSE signals API, continuous backend polling, and optional parallel database notification; clients re-fetch the API.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Current`
- **Last Canonicalization Review:** `TODO-uninotas-foundation-project-rebase`
- **Remaining Migration Scope:** `none`

## Specification
Owns change invalidation semantics. Heartbeat and deduplication support the channel. Backend polling remains continuously active; LISTEN/NOTIFY is an optional parallel source. No event payload replaces a fresh API read.

## Observed Realtime Message Contract

`GET /api/v1/realtime/eventos` is public to the global guard but requires a query `token`. The controller verifies JWT signature/expiry only; unlike normal bearer routes, it does not resolve active/known user state or apply a role. A missing, invalid, or expired token returns 401 through the standard error body.

The endpoint returns HTTP 200 with `Content-Type: text/event-stream`. On the wire, each SSE frame carries an `event:` field whose value is `evento.novo|evento.tratado|heartbeat` and a `data:` field containing the serialized JSON object `{tipo,origem,em,refId?,situacao?}`. `tipo` equals the `event:` value, `origem` is `api|banco|polling|sistema`, and `em` is an ISO-8601 string. The signal is invalidation only and causes the client to re-fetch the API.

Backend polling of `logs` is continuously active independently of LISTEN/NOTIFY; database notifications are an optional parallel low-latency source. Browser stream failure relies on EventSource reconnection. No separate client polling fallback or durable delivery guarantee is asserted.

## Purpose, Owned Entities, and Workflows
**Purpose:** reduce stale client views without creating a second data authority. **Owned/orchestrated entities:** invalidation signal and client refresh coordination. **Workflows/capabilities:** issue SSE change signal, heartbeat, deduplicate, re-fetch API, keep backend polling active, optionally consume database notifications in parallel, and let EventSource reconnect the browser stream. **Invariants/validation/auth:** signal has no business payload authority; API read remains authoritative. **Observed contracts:** the wire representation above is evidenced; no client polling fallback or delivery SLO is claimed.

## Cross-Module Considerations and Failure Modes
Events and treatments cause refresh-relevant changes. Backend polling is the continuously active source while LISTEN/NOTIFY is optional and parallel; browser stream interruption relies on EventSource reconnection. Neither path may manufacture event state.
