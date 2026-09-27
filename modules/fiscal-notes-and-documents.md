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
- **Canonical Coverage Status:** `Target-planned`; a locally implemented, feature-flagged NestJS candidate now exists for Smart Notas list/detail, but no runtime activation, deployment, or capability ownership is asserted.

## Purpose, Owned Entities, and Workflows
Owns the future boundary for `FiscalNoteDocument`, selected-context note facts, detail and DANFE/XML/document availability. Unifast and Prosperar are isolated `FiscalIssuerContext` values, not tenants.

The local candidate exposes authenticated `GET /api/v1/notas` and `GET /api/v1/notas/:noteId`. Each list request selects exactly one fiscal context; detail resolves an HMAC-signed opaque `noteId` directly to one provider `idInterno`. The adapter uses independent backend-only token/CNPJ pairs, the fixed Smart Notas `/api` origin, no redirects, no retry, bounded timeout/concurrency/rate/response size, and explicit DTO normalization that excludes recipient PII and raw provider payloads. The capability remains disabled by default and is not current runtime until the separate cutover TODO proves secret injection, issuer binding, quota calibration, audit sink, deployment, and rollback.

## Invariants
Smart Notas is the sole note/document source. Context selection never grants cross-context aggregation; document access does not persist provider identifiers, payloads, or captured URLs. The candidate list/detail boundary never falls back to PostgreSQL `logs`, never accepts a consumer-provided CNPJ/token, and never exposes raw `idInterno` as its route identity.

## Cross-Module Considerations
Integration-error evidence stays with the integration-error-occurrences boundary; operational workflow stays with operational-cases.
