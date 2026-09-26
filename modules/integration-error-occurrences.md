# Integration Error Occurrences

## Module Intent & Boundaries
- **Core scope:** `uninotas`
- **Subscope:** `integration-error-occurrences`
- **EnvironmentType:** `landlord` (PACED adapter only; no business tenancy)
- **Runtime authority state:** `target_planned`
- **Owned capabilities:** none
- **Planned capabilities:** `integration_error_read_model`
- **Out-of-scope guardrails:** note/document authority, source writes, and assumptions about external writer/filter behavior.
- **Dependency boundaries:** PostgreSQL `logs` supplies external integration-error evidence only.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Target-planned`; no runtime query or normalization implementation is asserted.

## Purpose, Owned Entities, and Workflows
Owns the future `IntegrationErrorOccurrence` boundary: normalize retained PostgreSQL failure evidence and correlate it when evidence permits. The external `logs` writer/filter semantics remain unknown.

## Invariants
Correlation never converts an error into fiscal-note truth and never makes `ref_id` unique. No tenancy semantics attach to Unifast or Prosperar.

## Cross-Module Considerations
Smart Notas note facts belong to fiscal-notes-and-documents; application treatment belongs to operational-cases.
