# Operational Monitoring

## Module Intent & Boundaries
- **Core scope:** `monitor-de-notas`
- **Subscope:** `operational-monitoring`
- **EnvironmentType:** `landlord` (PACED technical adapter only; no business tenancy)
- **Out-of-scope guardrails:** Claiming availability from an empty result or changing runtime monitoring.
- **Dependency boundaries:** Reuses the events summary semantics for an external monitor or alert.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Current`
- **Last Canonicalization Review:** `TODO-uninotas-foundation-project-rebase`
- **Remaining Migration Scope:** `none`

## Specification
Owns the documented operational summary contract. A database failure is distinct from a successful zero-error window; time window and limits remain explicit.

## Observed Monitoring Contract

`GET /api/v1/monitoramento/erros` is open when `MONITORAMENTO_TOKEN` is unset. When configured, the credential may be supplied as query `token` (string, maximum 200 characters; no trim transform is observed) or header `x-monitor-token` (no DTO length bound observed); missing/mismatch returns 401 through `{statusCode,erro,mensagem,caminho,timestamp}`.

Query fields are integer `minutos` default 60/range 1..1440, integer `atencao` default 1/minimum 1, integer `critico` default 6/minimum 1, and optional `alertarEm=atencao|critico`. The response is `{status,cor,erros,pendentes,sucessos,total,ultima_verificacao,janela,limites,detalhe}` where `status=ok|atencao|critico|indisponivel`, `cor=verde|amarelo|vermelho|cinza`, `janela={inicio,fim,minutos}`, and `limites={atencao,critico}`.

The same `application/json` monitoring body is returned with HTTP 200 normally or HTTP 503 when the database is unavailable or `alertarEm` is reached; those operational 503 responses are not the standard error body. Responses set `Cache-Control: no-store`. These are observed status semantics, not a service-level objective.

## Purpose, Owned Entities, and Workflows
**Purpose:** provide an external operational check from observed event-summary semantics. **Owned/orchestrated entities:** monitoring summary projection. **Workflows/capabilities:** query rolling window and distinguish no errors from data-store unavailability. **Invariants/validation/auth:** reuse summary semantics; do not recast failure as zero. **Observed contracts:** the request bounds, response body, conditional credential, 200/503 behavior, and no-cache rule above are evidenced; no SLO is asserted.

## Cross-Module Considerations and Failure Modes
Events/classification owns source semantics. Database unavailability produces an unavailable outcome, not a successful empty result.
