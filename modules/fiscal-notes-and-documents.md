# Fiscal Notes and Documents

## Module Intent & Boundaries
- **Core scope:** `uninotas`
- **Subscope:** `fiscal-notes-and-documents`
- **EnvironmentType:** `landlord` (PACED adapter only; no business tenancy)
- **Runtime authority state:** `target_planned`
- **Owned capabilities:** none
- **Planned capabilities:** `note_read_model`, `fiscal_document_read`
- **Out-of-scope guardrails:** provider writes, credential persistence, and aggregate fiscal-context lists.
- **Dependency boundaries:** Smart Notas owns note facts, DANFE/XML and document access; PostgreSQL `logs` is never note authority.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Target-planned`; locally implemented NestJS and React candidates now exist for Smart Notas list/detail and the separated integration-error queue. A filtered CSV export boundary is planned but not implemented. No runtime activation, deployment, real-context frontend smoke, or capability ownership is asserted.

## Purpose, Owned Entities, and Workflows
Owns the future boundary for `FiscalNoteDocument`, selected-context note facts, detail and DANFE/XML/document availability. Unifast and Prosperar are isolated `FiscalIssuerContext` values, not tenants.

The local candidate exposes authenticated `GET /api/v1/notas` and `GET /api/v1/notas/:noteId`. Each list request selects exactly one fiscal context; detail resolves an HMAC-signed opaque `noteId` directly to one provider `idInterno`. The adapter uses independent backend-only token/CNPJ pairs, the fixed Smart Notas `/api` origin, no redirects, no retry, bounded timeout/concurrency/rate/response size, and explicit DTO normalization that excludes recipient PII and raw provider payloads. The capability remains disabled by default and is not current runtime until the separate cutover TODO proves secret injection, issuer binding, quota calibration, audit sink, deployment, and rollback.

The local React candidate makes `/` the Smart Notas `Geral`, keeps PostgreSQL integration failures under `/erros` and `/eventos/:refId`, and exposes note detail at `/notas/:noteId`. It selects one textual `FiscalIssuerContext`, uses the backend's published fiscal-status catalog, keeps document/purchase filters out of URL and persistent browser storage, admits only normalized DTO fields, masks purchase/access keys, and maintains a session-only 20-key LRU cache with explicit freshness, hard expiry, deduplication, abort/generation ownership, and synchronous logout cleanup. Its browser evidence is fully intercepted; activation and real-context smoke remain in the cutover TODO.

### Planned filtered CSV export boundary

`GET /api/v1/notas/exportar` is the planned authenticated read endpoint for exporting every note matched by the currently applied filters of exactly one `FiscalIssuerContext`; it rejects `pagina`, never aggregates Unifast and Prosperar, and is available to the existing reader profiles only. The browser makes one cancelable request. The backend walks provider pages sequentially, validates stable `perPage`/`total`/`totalPages`, page identity, counts and duplicate provider IDs, and builds the entire CSV before sending any bytes. An empty result is `204`; a successful non-empty result is a no-store UTF-8 CSV; any traversal, consistency, abort, deadline, quota or envelope failure produces no partial file.

The planned synchronous path is bounded to 20,000 rows, 200 provider pages, 180 seconds and a 24 MiB final CSV. Admission reserves interactive provider capacity, permits at most one active export per fiscal context and actor per instance, and limits global export concurrency to `min(2, maxConcurrency - 1)`. Provider calls share the configured per-context budget; a start consumes the existing per-user fixed-window budget exactly once. The source exposes no snapshot/cursor/stable order, so the product calls this an “export of the filter”, detects specified inconsistencies fail-closed, and never claims a transactional snapshot. Larger or snapshot-grade exports require a separately approved asynchronous design.

## Invariants
Smart Notas is the sole note/document source. Context selection never grants cross-context aggregation; document access does not persist provider identifiers, payloads, or captured URLs. The candidate list/detail boundary and planned export boundary never fall back to PostgreSQL `logs`, never accept a consumer-provided CNPJ/token, and never expose raw `idInterno` as route identity or CSV content. Frontend navigation may retain only non-sensitive canonical fiscal query state; fiscal DTO/cache/export state is memory-only, isolated by authenticated user/context/query, and cleared or aborted on logout/session disposal.

## Cross-Module Considerations
Integration-error evidence stays with the integration-error-occurrences boundary; operational workflow stays with operational-cases.
