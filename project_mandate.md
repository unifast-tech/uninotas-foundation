# Monitor de Notas — Project Mandate

Monitor de Notas helps the financial team inspect invoice-emission failures from SmartNotas and record their treatment. Routerfy owns ingestion and writes the external `logs` table; this product reads it and never writes it.

## Canonical identity

- **Product:** Monitor de Notas
- **Technical repository:** `MonitorDeNotas`
- **Documentation repository:** `uninotas-foundation`

## Target outcome

Operators can find, classify, inspect, and treat relevant events with traceable authorship, without mutating the source event stream.

## Principles

- `logs` is an external read-only boundary.
- `monitor_tratamentos` is append-only history; its latest record determines effective status.
- Authentication and active user profiles protect operations while deactivation preserves authorship.
- Realtime is invalidation only: clients re-fetch authoritative API data.
- Claims in this Foundation require product evidence and never include secrets or production payloads.
