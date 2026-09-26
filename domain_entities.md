# UniNotas — Domain Entities

## UniNotas target entities

`FiscalIssuerContext` identifies Unifast or Prosperar and is not a tenant. `FiscalNoteDocument`, `IntegrationErrorOccurrence`, and `OperationalCase` have distinct target-planned ownership.

In the target-planned architecture, Smart Notas owns all fiscal notes/documents and PostgreSQL `logs` is restricted to integration-failure evidence. Current runtime still exposes a mixed read-only `logs` projection until the capability transition is completed; its external writer, ingestion, and filter semantics are unknown.

- **LogEvent:** external read-only record with unknown source-row owner/writer semantics, read through SQL; `ref_id` correlates work but is not a primary key.
- **Classification:** original and effective event situation. SQL and TypeScript projections must remain semantically aligned.
- **Tratamento:** append-only application record correlated by `ref_id`; the latest entry determines current treatment.
- **Usuario:** authenticated team member with a profile; disabled users remain as historical authors.
- **Realtime invalidation:** a signal that causes clients to refresh, not a durable event record.

There is no documented business tenancy, tenant, business unit, or organization model in the product.
