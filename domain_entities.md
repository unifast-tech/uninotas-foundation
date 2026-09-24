# Monitor de Notas — Domain Entities

- **LogEvent:** externally owned Routerfy record read through SQL; `ref_id` correlates work but is not a primary key.
- **Classification:** original and effective event situation. SQL and TypeScript projections must remain semantically aligned.
- **Tratamento:** append-only application record correlated by `ref_id`; the latest entry determines current treatment.
- **Usuario:** authenticated team member with a profile; disabled users remain as historical authors.
- **Realtime invalidation:** a signal that causes clients to refresh, not a durable event record.

There is no documented business tenancy, tenant, business unit, or organization model in the product.
