# Events and Classification

## Module Intent & Boundaries
- **Core scope:** `monitor-de-notas`
- **Subscope:** `events-and-classification`
- **EnvironmentType:** `landlord` (PACED technical adapter only; no business tenancy)
- **Out-of-scope guardrails:** Writing Routerfy `logs`, defining source ingestion, or treating `ref_id` as a primary key.
- **Dependency boundaries:** Read-only SQL over `logs`; API consumers use explicit list, filter, summary, detail, and export contracts.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Current`
- **Last Canonicalization Review:** `TODO-uninotas-foundation-project-rebase`
- **Remaining Migration Scope:** `none`

## Specification
Owns external event observation, filters, pagination, export, and original/effective classification. Only records with `org_path = 'SmartNotas'` are relevant. SQL and TypeScript classification projections must preserve equivalent semantics. Effective status incorporates the latest treatment; `PENDENTE` restores original status.

## Observed API Contract

The protected events boundary observes `GET /eventos`, `GET /eventos/resumo`, `GET /eventos/produtos`, `GET /eventos/exportar`, `GET /eventos/:refId`, and `GET /eventos/:refId/payload`; batch treatment is routed to `POST /eventos/tratar-lote` and belongs jointly with the treatment owner below. List/filter, summary, detail, payload, and export responses are read projections. Invalid or absent authentication is rejected by the identity boundary; an unknown `refId` is a not-found result, not an empty event. The client preserves API error messages and treats transport failure as unavailable, not empty data.

```json
{"base_path":"/api/v1","routes":["GET /eventos","GET /eventos/resumo","GET /eventos/produtos","GET /eventos/exportar","GET /eventos/:refId","GET /eventos/:refId/payload","PATCH /eventos/:refId/tratamento","POST /eventos/tratar-lote"],"authorization":"JWT; treatment routes require ADMIN|GESTOR|ANALISTA","responses":"list|summary|products|csv|detail|payload; unknown refId=404","errors":"standard error body: statusCode, erro, mensagem, caminho, timestamp"}
```

## Ownership Invariant

Routerfy alone writes `logs`; Monitor de Notas reads `logs` only. Application writes belong only to `monitor_usuarios` and `monitor_tratamentos` through their owning modules.

## Purpose, Owned Entities, and Workflows
**Purpose:** provide the authoritative read model for emission-event investigation. **Owned/orchestrated entities:** `LogEvent` and classification projections; Routerfy remains owner of persisted source rows. **Workflows/capabilities:** list, filter, paginate, summarize, export, inspect detail, and register treatment through the observed API contract. **Invariants/validation/auth:** source remains read-only, SmartNotas filter applies, `ref_id` is correlation only, and protected API access is enforced by the identity boundary. **Observed contracts:** raw SQL, classifier, mapper, routes, and bounded errors above are evidenced; no SLO is asserted.

## Cross-Module Considerations
Routerfy owns `logs`; [treatments and history](treatments-and-history.md) owns application treatment writes.

## Failure and Degradation Modes
Source-query failure is not represented as zero matching events; clients use the API result/error contract rather than treating an export or summary as source truth.
