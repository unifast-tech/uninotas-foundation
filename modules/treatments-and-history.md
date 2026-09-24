# Treatments and History

## Module Intent & Boundaries
- **Core scope:** `monitor-de-notas`
- **Subscope:** `treatments-and-history`
- **EnvironmentType:** `landlord` (PACED technical adapter only; no business tenancy)
- **Out-of-scope guardrails:** Changing `logs`, overwriting treatment history, or asserting `ref_id` uniqueness.
- **Dependency boundaries:** Writes only `monitor_tratamentos`; reads event context through the events module boundary.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Current`
- **Last Canonicalization Review:** `TODO-uninotas-foundation-project-rebase`
- **Remaining Migration Scope:** `none`

## Specification
Owns treatment commands and append-only audit history correlated by `ref_id`. The most recent treatment defines current treatment state and preserves its author; `PENDENTE` exposes the event's original classification.

## Observed Treatment Contract

`POST /eventos/tratar-lote` accepts an authenticated treatment command for selected event references and records append-only treatment history. Treatment reads are returned through the event detail projection rather than a competing history authority. Invalid command input is rejected; unavailable history leaves effective status unavailable rather than inventing a value. The response preserves the resulting treatment state and authorship relation evidenced by the application model.

## Purpose, Owned Entities, and Workflows
**Purpose:** preserve an auditable financial-team response to an event. **Owned/orchestrated entities:** `Tratamento` and its author relation. **Workflows/capabilities:** register treatment, read history, and derive effective situation. **Invariants/validation/auth:** write only application-owned `monitor_tratamentos`, append rather than overwrite, require authenticated active users, and retain authorship. **Observed contracts:** Prisma model/service behavior is evidenced; endpoint payload and SLO are not asserted.

## Cross-Module Considerations and Failure Modes
Events/classification owns source observation; identity/team owns authorization. If treatment history cannot be read, effective status is unavailable rather than inferred.
