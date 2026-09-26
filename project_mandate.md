# UniNotas — Project Mandate

## UniNotas target

UniNotas is the canonical product identity. In the target architecture it centralizes Smart Notas fiscal notes and documents, while PostgreSQL `logs` serves only integration-failure evidence.

MonitorDeNotas is the current technical application for a read-only, mixed emission-event projection from `logs`—including success, pending, and error records—and for treatment. The external writer, ingestion, and filter semantics are unknown; this product never writes that source. Smart Notas becomes the complete fiscal-note/document authority only when the planned adapter transition is implemented.

## Canonical identity

- **Product:** UniNotas (`core_scope=uninotas`)
- **Technical repository:** `MonitorDeNotas`
- **Documentation repository:** `uninotas-foundation`

## Target outcome

Operators can find, classify, inspect, and treat relevant events with traceable authorship, without mutating the source event stream.

## Current and target

Current runtime remains the MonitorDeNotas technical application and its legacy read-only, mixed `logs`-derived note/event workflow. Target-planned UniNotas reads every fiscal note and document from Smart Notas and restricts PostgreSQL `logs` to integration-failure evidence. External writer, ingestion, and filter behavior remain unknown unless separately evidenced.

## Principles

- `logs` is an external read-only boundary.
- `monitor_tratamentos` is append-only history; its latest record determines effective status.
- Authentication and active user profiles protect operations while deactivation preserves authorship.
- Realtime is invalidation only: clients re-fetch authoritative API data.
- Claims in this Foundation require product evidence and never include secrets or production payloads.
