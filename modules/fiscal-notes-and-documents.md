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

## Canonical Decision Register

| Decision ID | Status | Decision | Why | Evidence | Replaces | Cleanup Trigger |
| --- | --- | --- | --- | --- | --- | --- |
| `FISC-EX-01` | `Current` | Export always applies one fiscal context and every applied filter, never the visible page or both contexts. | Context isolation and user-requested semantics. | `API Endpoint Definitions > Export request` | `n/a` | `n/a` |
| `FISC-EX-02` | `Current` | The backend performs the sequential provider page walk; the browser makes one request. | Centralizes credentials, validation and quota ownership. | `API Endpoint Definitions > Export traversal` | `n/a` | `n/a` |
| `FISC-EX-03` | `Current` | The backend finishes a bounded Buffer before starting the response. | Provider/serialization failures must precede intentional response start. | `API Endpoint Definitions > Export success and transport boundary` | `n/a` | `n/a` |
| `FISC-EX-04` | `Current` | Export provides detectable consistency checks, not a transactional snapshot. | Smart Notas exposes no cursor/snapshot/stable order. | `API Endpoint Definitions > Export traversal` | `n/a` | `n/a` |
| `FISC-EX-05` | `Current` | HTTP, CSV, error, observation and browser lifecycle contracts below are the public boundary. | Avoids divergent clients/tests. | `API Endpoint Definitions` | `n/a` | `n/a` |
| `FISC-EX-06` | `Current` | CSV serialization remains local to the fiscal module. | The PostgreSQL integration-error CSV has different authority and schema. | `API Endpoint Definitions > CSV schema` | `n/a` | `n/a` |
| `FISC-EX-07` | `Current` | Synchronous export is bounded; larger/snapshot-grade exports require a new approved asynchronous design. | Protects quota, latency and memory. | `API Endpoint Definitions > Limits and admission` | `n/a` | `n/a` |
| `FISC-EX-08` | `Current` | Existing readers may export raw purchase/access keys, while internal provider IDs, PII, credentials and payloads remain excluded. | Matches current read authorization without broadening sensitive data. | `API Endpoint Definitions > CSV schema` | `n/a` | `n/a` |

## Canonical Coverage Status
- **Canonical Coverage Status:** `Target-planned`; locally implemented NestJS and React candidates now exist for Smart Notas list/detail and the separated integration-error queue. A filtered CSV export boundary is planned but not implemented. No runtime activation, deployment, real-context frontend smoke, or capability ownership is asserted.

## Purpose, Owned Entities, and Workflows
Owns the future boundary for `FiscalNoteDocument`, selected-context note facts, detail and DANFE/XML/document availability. Unifast and Prosperar are isolated `FiscalIssuerContext` values, not tenants.

The local candidate exposes authenticated `GET /api/v1/notas` and `GET /api/v1/notas/:noteId`. Each list request selects exactly one fiscal context; detail resolves an HMAC-signed opaque `noteId` directly to one provider `idInterno`. The adapter uses independent backend-only token/CNPJ pairs, the fixed Smart Notas `/api` origin, no redirects, no retry, bounded timeout/concurrency/rate/response size, and explicit DTO normalization that excludes recipient PII and raw provider payloads. The capability remains disabled by default and is not current runtime until the separate cutover TODO proves secret injection, issuer binding, quota calibration, audit sink, deployment, and rollback.

The local React candidate makes `/` the Smart Notas `Geral`, keeps PostgreSQL integration failures under `/erros` and `/eventos/:refId`, and exposes note detail at `/notas/:noteId`. It selects one textual `FiscalIssuerContext`, uses the backend's published fiscal-status catalog, keeps document/purchase filters out of URL and persistent browser storage, admits only normalized DTO fields, masks purchase/access keys, and maintains a session-only 20-key LRU cache with explicit freshness, hard expiry, deduplication, abort/generation ownership, and synchronous logout cleanup. Its browser evidence is fully intercepted; activation and real-context smoke remain in the cutover TODO.

### Planned filtered CSV export boundary

`GET /api/v1/notas/exportar` is the planned authenticated read endpoint for exporting every note matched by the currently applied filters of exactly one `FiscalIssuerContext`; it rejects `pagina`, never aggregates Unifast and Prosperar, and is available to the existing reader profiles only. The browser makes one cancelable request. The backend walks provider pages sequentially, validates stable `perPage`/`total`/`totalPages`, page identity, counts and duplicate provider IDs, and builds the entire CSV before intentionally starting the response. An empty result is `204`; a successful non-empty result is a no-store UTF-8 CSV. Traversal, consistency, abort, deadline, quota or envelope failure during generation starts no CSV response; wire-level transport failure remains outside the atomicity claim.

The planned synchronous path is bounded to 20,000 rows, 200 provider pages, 180 seconds and a 24 MiB final CSV. Admission reserves interactive provider capacity, permits at most one active export per fiscal context and actor per instance, and limits global export concurrency to `min(2, maxConcurrency - 1)`. Provider calls share the configured per-context budget; a start consumes the existing per-user fixed-window budget exactly once. The source exposes no snapshot/cursor/stable order, so the product calls this an “export of the filter”, detects specified inconsistencies fail-closed, and never claims a transactional snapshot. Larger or snapshot-grade exports require a separately approved asynchronous design.

## API Endpoint Definitions

This section is the source of truth for the fiscal read API.

| Endpoint | Method | Description | Required role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `/api/v1/notas` | `GET` | paginated normalized fiscal notes from one context | `ADMIN|GESTOR|ANALISTA|LEITOR` | fiscal query plus `pagina` | normalized JSON page |
| `/api/v1/notas/:noteId` | `GET` | normalized fiscal note detail addressed by signed opaque ID | `ADMIN|GESTOR|ANALISTA|LEITOR` | path `noteId` | normalized JSON detail |
| `/api/v1/notas/exportar` | `GET` | every traversed note matching applied filters in one context | `ADMIN|GESTOR|ANALISTA|LEITOR` | export query without `pagina` | `200` CSV or `204` empty |

### Export request

| Field | Type | Required | Contract |
| --- | --- | --- | --- |
| `contextoFiscal` | enum | yes | `unifast|prosperar`; one value only |
| `dataInicio` | ISO date | yes | `YYYY-MM-DD` |
| `dataFim` | ISO date | yes | `YYYY-MM-DD`; existing maximum interval applies |
| `status` | enum | no | existing published fiscal-status allowlist |
| `documento` | digits | no | exactly 11 or 14 digits |
| `idCompra` | string | no | trimmed, 1..100 characters |

**Field Definitions**

- `contextoFiscal`: valid values are `unifast` and `prosperar`; they select independent provider credentials and are never aggregated.
- `status`: valid values are exactly the existing fiscal-status catalog published by the backend; unknown values are invalid.

`pagina` and every unknown query field return `400 ConsultaDeNotasInvalida`. The export DTO and the list DTO derive from one shared fiscal-filter schema; only list adds pagination.

### Export success and transport boundary

- `204` means the validated first page was page 1 with `total=0`, `totalPages=0` and no items; no subsequent provider call or browser download occurs.
- `200` begins only after server-side generation completes within 180 seconds and the final Buffer is at most 24 MiB. Headers are `Content-Type: text/csv; charset=utf-8`, ASCII `Content-Disposition: attachment; filename="notas-{contextoFiscal}-{dataInicio}-{dataFim}.csv"`, `Cache-Control: private, no-store`, `Pragma: no-cache`, `X-Content-Type-Options: nosniff`, exact `Content-Length` and `X-Export-Row-Count`.
- The server checks client abort/deadline before admission, around every wait/I/O/serialization yield, and immediately before returning the Buffer. Exact deadline equality fails. Network/proxy failure after HTTP transmission begins can still truncate bytes and is not claimed as wire-level atomicity; the managed browser creates the download only after the response Blob completes and remains current.

### Export traversal

The backend requests pages sequentially from page 1, with one upstream call active per export. It freezes `perPage`, `total` and `totalPages`; validates every returned page identity, page sizes, final count and unique internal provider IDs; and fails without intentionally starting a CSV response on any mismatch. Limits are 20,000 rows and 200 provider pages. These checks can detect specified changes but cannot prove a snapshot or stable order.

### CSV schema

UTF-8 BOM, semicolon delimiter, every field quoted, doubled internal quotes, CRLF and final CRLF are mandatory. The fixed column order is `contextoFiscal;numeroFiscal;status;produto;idCompra;chaveAcesso;ambiente;modelo;finalidade;plataforma;emissaoAgendada;dataPagamento;competencia;valorUnitario;valorTotal`. Null becomes empty. Before CSV escaping, prefix an ASCII apostrophe when the first non-space character is `=`, `+`, `-` or `@`, or the first character is TAB/CR/LF. Raw `idCompra` and `chaveAcesso` are allowed for existing reader roles; `providerIdInterno`, `noteId`, recipient PII, token, configured CNPJ, raw payload and non-allowlisted fields are forbidden.

### Errors

| HTTP | Public code | Meaning |
| --- | --- | --- |
| `400` | `ConsultaDeNotasInvalida` | invalid/unknown query or `pagina` |
| `422` | `ExportacaoFiscalLimiteExcedido` | rows, pages or bytes exceed the synchronous envelope |
| `429` | `ExportacaoFiscalOcupada` | incapable configuration, active/cooldown/context/global admission |
| `429` | `LimiteDeConsultaExcedido` | user fixed-window budget or new-actor bucket capacity |
| `502` | `ExportacaoFiscalPaginacaoInconsistente` | page metadata, identity, size, count or duplicate ID mismatch |
| `504` | `ExportacaoFiscalPrazoExcedido` | server-side generation deadline reached |

Existing mapped provider errors retain their existing status/code. Client disconnect stops work and does not attempt another response.

`Retry-After` is `max(1,ceil(remainingMs/1000))`. Incapable configuration uses 60 seconds. Export-specific collisions use the maximum of lease floor 5 seconds, remaining actor cooldown and remaining effective fixed window when user/cap also blocks. When user fixed-window or new-actor capacity is the only blocker, the response is `LimiteDeConsultaExcedido` with time to the next non-regressing effective-window boundary.

### Limits and admission

One module-local coordinator owns the non-regressing fixed-window high-water and budgets used by list, detail, export start and export pages. List/detail atomically consume one user and one context unit before their provider call. Export consumes one user unit at accepted start; each page later consumes one context-total unit and one export-share unit. `exportShare = ratePerContextMinute < 2 ? 0 : floor(ratePerContextMinute * 0.75)`. Rejected prechecks mutate no raw state; accepted provider errors/aborts do not refund budget. Export admission is at most one active per actor and fiscal context, and `min(2, maxConcurrency - 1)` globally per instance. Coordination across multiple replicas is not claimed.

### Browser lifecycle

The export action snapshots applied filters without page. Duplicate clicks are dropped. Applied fiscal-filter changes cancel the active export; page-only changes do not. Logout, 401, navigation and unmount abort. A generation guard suppresses late state/download effects, and the temporary Object URL is always revoked. The existing PostgreSQL integration-error export keeps its backward-compatible download behavior.

### Observability

One aggregate export event may contain authenticated internal actor ID, context, correlation ID, allowlisted outcome, pages attempted/completed, rows, bytes, duration and abort/deadline/rate flags. It must not contain filters, document/purchase/access/fiscal/provider IDs, token, CNPJ, raw payload or CSV. Adapter page logs propagate only the correlation ID needed for tracing.

## Invariants
Smart Notas is the sole note/document source. Context selection never grants cross-context aggregation; document access does not persist provider identifiers, payloads, or captured URLs. The candidate list/detail boundary and planned export boundary never fall back to PostgreSQL `logs`, never accept a consumer-provided CNPJ/token, and never expose raw `idInterno` as route identity or CSV content. Frontend navigation may retain only non-sensitive canonical fiscal query state; fiscal DTO/cache/export state is memory-only, isolated by authenticated user/context/query, and cleared or aborted on logout/session disposal.

## Cross-Module Considerations
Integration-error evidence stays with the integration-error-occurrences boundary; operational workflow stays with operational-cases.
