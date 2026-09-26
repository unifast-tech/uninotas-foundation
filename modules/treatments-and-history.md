# Treatments and History

## Module Intent & Boundaries
- **Core scope:** `uninotas`
- **Subscope:** `treatments-and-history`
- **EnvironmentType:** `landlord` (PACED technical adapter only; no business tenancy)
- **Runtime authority state:** `current_runtime`
- **Owned capabilities:** `operational_workflow`
- **Planned capabilities:** none
- **Out-of-scope guardrails:** Changing `logs`, overwriting treatment history, or asserting `ref_id` uniqueness.
- **Dependency boundaries:** Writes only `monitor_tratamentos`; reads event context through the events module boundary.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Current`
- **Last Canonicalization Review:** `TODO-uninotas-foundation-project-rebase`
- **Remaining Migration Scope:** `none`

## Specification
Owns treatment commands and append-only audit history correlated by `ref_id`. The most recent treatment defines current treatment state and preserves its author; `PENDENTE` exposes the event's original classification.

## Observed Treatment Contract

Both commands use base path `/api/v1`, require the normal bearer JWT guard, and allow only `ADMIN|GESTOR|ANALISTA`.

| Route | Request | Status / media | Successful response |
| --- | --- | --- | --- |
| `PATCH /eventos/:refId/tratamento` | path correlation `refId`; body `situacao=RESOLVIDO|IGNORADO|PENDENTE`; optional string `observacao` up to 1,000 characters | HTTP 200 `application/json` | complete event-detail projection after appending the treatment |
| `POST /eventos/tratar-lote` | the same `situacao`/`observacao` plus non-empty string array `refIds` with at most 500 entries | HTTP 200 `application/json` | `{solicitados,aplicados,ignorados}` where `ignorados` lists references absent from `logs` |

Validation, 401, 403, and single-event 404 failures use `{statusCode,erro,mensagem,caminho,timestamp}`. A database/history query failure rejects the request; it is not represented as a partial “unavailable” treatment state. Treatment reads appear inside the event detail projection rather than a competing history endpoint.

## Purpose, Owned Entities, and Workflows
**Purpose:** preserve an auditable financial-team response to an event. **Owned/orchestrated entities:** `Tratamento` and its author relation. **Workflows/capabilities:** register single or batch treatment, read history, and derive effective situation. **Invariants/validation/auth:** write only application-owned `monitor_tratamentos`, append rather than overwrite, require authenticated active users, and retain authorship. **Observed contracts:** the bounded single/batch request, response, and error semantics above are evidenced; no SLO is asserted.

## Cross-Module Considerations and Failure Modes
Events/classification owns source observation; identity/team owns authorization. If treatment history cannot be read, effective status is unavailable rather than inferred.
