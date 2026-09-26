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
- **Canonical Coverage Status:** `Target-planned`; no runtime adapter or route is asserted.

## Purpose, Owned Entities, and Workflows
Owns the future boundary for `FiscalNoteDocument`, selected-context note facts, detail and DANFE/XML/document availability. Unifast and Prosperar are isolated `FiscalIssuerContext` values, not tenants.

## Invariants
Smart Notas is the sole note/document source. Context selection never grants cross-context aggregation; document access does not persist provider identifiers, payloads, or captured URLs.

## Cross-Module Considerations
Integration-error evidence stays with the integration-error-occurrences boundary; operational workflow stays with operational-cases.
