# Operational Cases

## Module Intent & Boundaries
- **Core scope:** `uninotas`
- **Subscope:** `operational-cases`
- **EnvironmentType:** `landlord` (PACED adapter only; no business tenancy)
- **Runtime authority state:** `target_planned`
- **Owned capabilities:** none
- **Planned capabilities:** `operational_workflow`
- **Out-of-scope guardrails:** rewriting provider notes or external error facts.
- **Dependency boundaries:** application workflow/treatment/authorship only; source facts remain external.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Target-planned`; no workflow implementation is asserted.

## Purpose, Owned Entities, and Workflows
Owns the future `OperationalCase` workflow, including treatment and authorship around optional note and error references. It does not alter source facts.

## Invariants
An operational case is not a tenant and does not create aggregate fiscal-context authority. Correlation is evidence, not ownership transfer.

## Cross-Module Considerations
Fiscal facts remain in fiscal-notes-and-documents; integration failures remain in integration-error-occurrences.
