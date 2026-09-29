# Fiscal Notes and Documents

## Module Intent & Boundaries
- **Core scope:** `uninotas`
- **Subscope:** `fiscal-notes-and-documents`
- **EnvironmentType:** `landlord` (PACED adapter only; no business tenancy)
- **Runtime authority state:** `target_planned`
- **Owned capabilities:** none
- **Planned capabilities:** `note_read_model`, `fiscal_document_read`, `fiscal_note_cancellation`
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
| `FISC-EX-09` | `Current` | One fiscal coordinator owns the non-regressing window, all read budgets and export admission with read-only precheck and atomic accepted commit. | Prevents quota bypass and partial charging across list/detail/export. | `API Endpoint Definitions > Limits and admission` | `n/a` | `n/a` |
| `FISC-EX-10` | `Current` | Deadline cancellation covers active waits/I/O; pacing persists per context; actor-state capacity covers current buckets, unexpired cooldowns and active leases. | Keeps time, quota and state cardinality bounded. | `API Endpoint Definitions > Export success and transport boundary`; `Limits and admission` | `n/a` | `n/a` |
| `FISC-VIS-01` | `Current` | The list summary exposes `recipientName` plus complete purchase/access identifiers to existing authenticated readers; the detail exposes the approved recipient identity/location fields and provider internal reference. | Financial readers need operational identification without a second data source. | `API Endpoint Definitions > Fiscal read response allowlists` | Previous no-recipient-PII/masked-presentation contract | `n/a` |
| `FISC-VIS-02` | `Current` | Public responses are positive allowlists of exactly 17 summary properties and 27 detail properties; list/export and detail use structurally distinct internal records. | Prevents provider payload drift and detail-only PII from entering list/export accumulation. | `API Endpoint Definitions > Fiscal read response allowlists` | Shared `FiscalNoteRecord` projection | `n/a` |
| `FISC-VIS-03` | `Current` | The signed, context-bound `noteId` remains the only detail route input; it provides integrity, not confidentiality, while `providerInternalId` is only a displayed detail reference. | Prevents raw provider IDs from becoming caller-controlled authority. | `API Endpoint Definitions > Fiscal read response allowlists`; `Invariants` | `n/a` | `n/a` |
| `FISC-DOC-01` | `Current` | PDF/XML access resolves an ephemeral allowlisted provider URL through two explicit authenticated routes; UniNotas neither proxies nor persists document bytes or URLs. | Keeps Smart Notas authoritative and avoids a second sensitive-document store. | `API Endpoint Definitions > Fiscal document URL resolution` | `n/a` | Revisit only if the provider contract or proxy requirement changes. |
| `FISC-DOC-02` | `Current` | Document URLs require explicit absolute HTTPS authority syntax, default port, no userinfo/fragment/control/backslash, exact approved origin, and an 8 KiB bound both before and after canonicalization. | The browser sink must receive exactly the destination validated by the backend. | `API Endpoint Definitions > Fiscal document URL resolution` | `n/a` | Revisit only with a separately approved origin/policy change. |
| `FISC-DOC-03` | `Current` | The React disclosure uses drop-duplicate ownership, abort/late-result suppression and a protected external sink with a neutral safe fallback. | Prevents duplicate effects and stale capability exposure across close/navigation/unmount. | `API Endpoint Definitions > Document browser lifecycle` | `n/a` | `n/a` |
| `FISC-CAN-01` | `Proposed / inactive until TODO approval` | Permit exactly one Smart Notas write: editor-only single-note cancellation addressed by the signed context-bound `noteId`, with no automatic retry, durable PostgreSQL leader/uncertain/tombstone state and terminal local `Cancelada` precedence. | Adds the requested irreversible operation without authorizing any other provider write or treating PostgreSQL as fiscal fact authority. | `Proposed fiscal cancellation boundary`; `todos/active/features/TODO-uninotas-fiscal-note-cancellation.md` | The `provider writes` guardrail only for this exact endpoint after explicit approval | Activate on TODO approval; revisit only if provider idempotency or a new write capability is proposed. |

## Canonical Coverage Status
- **Canonical Coverage Status:** `Local-Implemented, Provisional`; locally implemented NestJS and React candidates now exist for Smart Notas list/detail, filtered CSV export and the separated integration-error queue. No runtime activation, deployment, real-context frontend smoke, quota calibration or capability ownership is asserted.

## Purpose, Owned Entities, and Workflows
Owns the future boundary for `FiscalNoteDocument`, selected-context note facts, detail and DANFE/XML/document availability. Unifast and Prosperar are isolated `FiscalIssuerContext` values, not tenants.

The local candidate exposes authenticated `GET /api/v1/notas` and `GET /api/v1/notas/:noteId`. Each list request selects exactly one fiscal context; detail resolves an HMAC-signed `noteId` directly to one provider `idInterno`. The token is tamper-resistant and context-bound but decodifiable, so it is not a confidentiality mechanism. The adapter uses independent backend-only token/CNPJ pairs, the fixed Smart Notas `/api` origin, no redirects, no retry, bounded timeout/concurrency/rate/response size, and explicit positive DTO allowlists. The list adds only the normalized recipient name as PII; document, e-mail and location exist only in the authenticated detail. Raw provider payloads and non-allowlisted fields remain excluded. The capability remains disabled by default and is not current runtime until `todos/active/features/TODO-uninotas-smart-notas-read-cutover.md` proves secret injection, issuer binding, quota calibration, audit sink, deployment, and rollback.

The local React candidate makes `/` the Smart Notas `Geral`, keeps PostgreSQL integration failures under `/erros` and `/eventos/:refId`, and exposes note detail at `/notas/:noteId`. It selects one textual `FiscalIssuerContext`, uses the backend's published fiscal-status catalog, keeps document/purchase filters out of URL and persistent browser storage, admits only normalized DTO fields, and shows recipient name plus complete purchase/access identifiers to authenticated financial readers. The detail presents every approved provider field, including the internal reference, recipient document/e-mail/location and the existing detail-only fields. Long values wrap without truncation in the desktop grid and labeled mobile cards. A session-only 20-key LRU cache retains list data with explicit freshness, hard expiry, deduplication, abort/generation ownership, and synchronous logout cleanup; detail is not cached. Its browser evidence is fully intercepted; activation and real-context smoke remain in `todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`.

The authenticated workspace uses the official local Unifast mark and exposes `Smart Notas` plus `Processamento das notas` (`/erros`) to every authenticated profile. Account identity, theme, password and logout live in an accessible settings disclosure; `Equipe` remains ADMIN-only. Fiscal context, status and dates reload automatically, while document and purchase ID apply explicitly; list failure retains a same-filter retry. Native field tokens, focus/hover borders, mobile disclosure containment and centered pagination are validated in the declared Chrome surface, without claiming cross-OS control of the native select popup.

The locally implemented document candidate exposes PDF and XML actions on both the fiscal list and the 27-field detail. Each action resolves exactly one provider URL from the signed context-bound `noteId`; `200 available` carries a canonical allowlisted URL and `202 pending` carries `url:null`. Responses are private/no-store and provider messages are never echoed. The adapter accepts only exact envelopes, bounds the body to 16 KiB and both the supplied and canonical URL to 8 KiB, rejects redirects and unsafe URL syntax, and never logs or stores the capability. The frontend admits one request/effect at a time, aborts or invalidates late results on close/navigation/unmount, opens with `noopener,noreferrer`, and keeps a neutral protected fallback link when opening cannot be observed. List/detail mobile disclosures remain within the viewport. The existing settings trigger is at least 44x44 with a glyph of at least 20px; its behavior and permissions are unchanged.

### Proposed fiscal cancellation boundary (inactive until TODO approval)

`FISC-CAN-01` is a proposed narrow supersession of the module-level `provider writes` guardrail. It does not become runtime authority until the governing TODO receives explicit approval, and it authorizes no issue, edit, reprocess, bulk action or client-supplied provider ID.

The proposed public endpoint is `POST /api/v1/notas/:noteId/cancelar`, with no query or request body, for `ADMIN|GESTOR|ANALISTA`; any query/body/payload content type is `400 CancelamentoFiscalRequisicaoInvalida`, unauthenticated callers receive `401`, and `LEITOR` receives `403` before the service/adapter. The backend decodes the signed context-bound ID and sends exactly one non-retried `POST /api/notas/{providerIdInterno}/cancelar` with backend-selected credentials. PostgreSQL atomically elects one leader per `{contextoFiscal,providerIdInterno}`. Same-process callers may share its promise; another replica receives `CancelamentoFiscalEmAndamento`. Every caller consumes actor admission, while only the leader consumes one context/upstream unit. Client disconnect is checked before dispatch but cannot cancel an already dispatched mutation.

Only HTTP `200` with a body of at most 16 KiB and exactly `{cancelada:boolean,mensagem:string}` is admitted. `mensagem` is trimmed, normalized to LF, limited to 1..2048 code points and rejects NUL/unsupported control characters. Public known results are exact `{cancelled:boolean,message:string}` with `Cache-Control: private, no-store`, `Pragma: no-cache` and `X-Content-Type-Options: nosniff`. Exact `200 true` persists `cancelled`; exact `200 false` persists terminal `not_cancelled` and never permits another Monitor write. Provider `401|403` maps to `502 SmartNotasCredencialRejeitada`; `404` to `409 CancelamentoFiscalNaoDisponivel`; `429` to `503 SmartNotasLimiteExterno`; active leader to `409 CancelamentoFiscalEmAndamento`; each of those post-dispatch outcomes, lease expiry and every transport/`5xx`/invalid response persists `uncertain`. Local pre-dispatch saturation remains `503 SmartNotasOcupado` and leaves no claim. No automatic or later manual Monitor retry is allowed from a terminal row.

The durable operation states are `in_flight`, `cancelled`, `not_cancelled` and `uncertain`; the row stores an opaque owner token, lease timestamps and nullable `dispatchStartedAt`, but no provider message, actor or recipient data. Auth, invalid request, actor admission, DB readiness or caller-abort failures before claim leave `absent`. A leader/context admission failure after claim may delete only its own row while `dispatchStartedAt IS NULL`. Immediately before the network call the leader stamps `dispatchStartedAt`; every later non-exact result becomes terminal. An expired leader lease transitions fail-closed to `uncertain`, never to write-ready. Reconciliation may promote `uncertain|not_cancelled` to `cancelled` only from an authoritative provider read; an audited operator-resolution workflow is outside this TODO.

When `cancelled=true`, Smart Notas remains authoritative. The `cancelled` tombstone and update of any existing cache row commit together. Every bootstrap/rolling upsert atomically checks both existing cache status and the tombstone at statement execution, so a stale page writes `Cancelada` even when the cache row did not exist before. After provider detail retrieval, an indexed operation lookup adds `cancellationState`; durable `cancelled` overrides a stale provider status to `Cancelada`, and every non-available state suppresses the action. The browser invalidates its fiscal list cache after known success and refetches detail. A DB failure before provider dispatch blocks the write; a local commit failure after external success becomes uncertain and never triggers another provider POST.

The additive migration must pass against disposable empty and baseline PostgreSQL schemas and expose the unique context/provider key, constrained state domain, owner/lease/dispatch fields and lookup indexes. Startup/activation fails closed when the migration is unavailable. Rollback is forward-only: route and UI may be disabled, but the migration, terminal rows, detail overlay and tombstone-aware cache writers remain active so prior cancellations cannot regress.

### Locally implemented filtered CSV export boundary

`GET /api/v1/notas/exportar` is the locally implemented authenticated read endpoint for exporting every note matched by the currently applied filters of exactly one `FiscalIssuerContext`; it rejects `pagina`, never aggregates Unifast and Prosperar, and is available to the existing reader profiles only. The browser makes one cancelable request. The backend walks provider pages sequentially, validates stable `perPage`/`total`/`totalPages`, page identity, counts and duplicate provider IDs, and builds the entire CSV before intentionally starting the response. An empty result is `204`; a successful non-empty result is a no-store UTF-8 CSV. Traversal, consistency, abort, deadline, quota or envelope failure during generation starts no CSV response; wire-level transport failure remains outside the atomicity claim. This is a local candidate at `MonitorNotes@8a0dba94a39da67fdd9979563beabb364371968a`, not a deployed runtime claim.

The locally implemented synchronous path is bounded to 20,000 rows, 200 provider pages, 180 seconds and a 24 MiB final CSV. Admission reserves interactive provider capacity, permits at most one active export per fiscal context and actor per instance, and limits global export concurrency to `min(2, maxConcurrency - 1)`. Provider calls share the configured per-context budget; a start consumes the existing per-user fixed-window budget exactly once. The source exposes no snapshot/cursor/stable order, so the product calls this an “export of the filter”, detects specified inconsistencies fail-closed, and never claims a transactional snapshot. Larger or snapshot-grade exports require a separately approved asynchronous design.

## API Endpoint Definitions

This section is the source of truth for the fiscal read API.

| Endpoint | Method | Description | Required role | Request | Response |
| --- | --- | --- | --- | --- | --- |
| `/api/v1/notas` | `GET` | paginated normalized fiscal notes from one context | `ADMIN|GESTOR|ANALISTA|LEITOR` | fiscal query plus `pagina` | normalized JSON page |
| `/api/v1/notas/:noteId` | `GET` | normalized fiscal note detail addressed by signed opaque ID | `ADMIN|GESTOR|ANALISTA|LEITOR` | path `noteId` | normalized JSON detail |
| `/api/v1/notas/:noteId/documentos/pdf` | `GET` | ephemeral Smart Notas PDF capability addressed by signed opaque ID | `ADMIN|GESTOR|ANALISTA|LEITOR` | path `noteId` | `200 available` or `202 pending` exact document DTO |
| `/api/v1/notas/:noteId/documentos/xml` | `GET` | ephemeral Smart Notas XML capability addressed by signed opaque ID | `ADMIN|GESTOR|ANALISTA|LEITOR` | path `noteId` | `200 available` or `202 pending` exact document DTO |
| `/api/v1/notas/exportar` | `GET` | every traversed note matching applied filters in one context | `ADMIN|GESTOR|ANALISTA|LEITOR` | export query without `pagina` | `200` CSV or `204` empty |

### Fiscal document URL resolution

Both document endpoints return exactly `{documentType, availability, url}` with `Cache-Control: private, no-store`, `Pragma: no-cache` and `X-Content-Type-Options: nosniff`. An available response is HTTP `200`, has the fixed requested `documentType`, `availability:"available"` and a non-null canonical URL. A pending response is HTTP `202`, has `availability:"pending"` and `url:null`; the required bounded provider message is never exposed.

The upstream call is a single direct `GET /api/notas/{providerIdInterno}/{pdf|xml}` using credentials selected solely by the decoded context. It never calls list/detail, retries, follows redirects or fetches the returned document. The provider body is limited to 16 KiB. Available URLs must begin with explicit `https://`, contain no ASCII control/space or backslash, use the default HTTPS port, contain no userinfo or fragment, and have exact origin `https://files.smart-notas.com` or `https://storage.smart-notas.com.br`. Both the raw provider string and canonical `URL.href` are limited to 8 KiB; only canonical `href` crosses the public boundary.

Unexpected `2xx`/other `4xx`/malformed envelopes/body or URL overflow map to `502 SmartNotasContratoInvalido`; invalid destinations/redirects map to `502 SmartNotasDestinoInvalido`; upstream `404` maps to `404 NotaFiscalNaoEncontrada`; provider auth maps to `502 SmartNotasCredencialRejeitada`; provider `429` and `5xx` map to `503 SmartNotasLimiteExterno` and `503 SmartNotasIndisponivel`; timeout maps to `504 SmartNotasTimeout`. Existing invalid-ID, disabled-capability, local rate/saturation and authentication contracts remain unchanged.

### Document browser lifecycle

The list permits one disclosure at a time and neither list nor detail prefetches a document. The controller reference synchronously drops repeated PDF/XML actions while active and disables both action buttons. Success, rejection and finalization update UI only while the request still owns the controller and is not aborted. Close, replacement, navigation and unmount abort/release ownership and clear feedback, so late resolve/reject outcomes cannot open a window or overwrite a current request. The external sink uses `_blank` with `noopener,noreferrer`; a null/blocked result produces neutral text and an explicit fallback anchor with the same protections, without rendering the capability as text.

### Fiscal read response allowlists

Every JSON property below is required. Nullable properties accept `null`, never absence, an invalid type or an empty present string. Summary items contain exactly 17 properties: `noteId`, `fiscalContext`, `providerStatus`, `fiscalNumber`, `accessKey`, `purchaseId`, `environment`, `model`, `purpose`, `platform`, `product`, `scheduledIssueDate`, `paymentDate`, `competence`, `unitValue`, `totalValue`, `recipientName`.

Detail contains those 17 plus the existing approved detail-only fields and one cancellation projection property, `cancellationState`, whose exact values are `available|unavailable|in_progress|uncertain|not_cancelled|cancelled`. Recipient document accepts only 11 or 14 digits; name/city are bounded to 255 code points, e-mail to 320, state to 64 and country to 128. List normalization maps only `recipientName`; its internal record and the export accumulator cannot structurally hold recipient fields exclusive to detail. `providerInternalId` is projected only in detail and is never accepted as a raw route parameter. The cancel action requires both editor role and `cancellationState=available`; `providerStatus=Autorizada` alone is insufficient.

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
- The server creates a deadline-derived AbortSignal and passes the composed client/deadline signal plus remaining time to every wait and provider I/O; active work is canceled at 180 seconds even if the provider timeout is longer. It also checks abort/deadline before admission, around every wait/I/O/serialization yield, and immediately before returning the Buffer. Exact deadline equality fails; deadline maps to 504 while client disconnect attempts no response. Network/proxy failure after HTTP transmission begins can still truncate bytes and is not claimed as wire-level atomicity; the managed browser creates the download only after the response Blob completes and remains current.

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

`Retry-After` is `max(1,ceil(remainingMs/1000))`. Incapable configuration uses 60 seconds. Export-specific collisions use the maximum of lease floor 5 seconds, remaining actor cooldown, remaining effective fixed window and actor-capacity retry when those causes coexist. User fixed-window alone uses its next effective boundary. Actor capacity uses the earliest projected identity release, where each identity's estimate is the maximum of its bucket boundary, cooldown expiry and 5-second active-lease hint.

### Limits and admission

One module-local coordinator owns the non-regressing fixed-window high-water and budgets used by list, detail, export start and export pages. List/detail atomically consume one user and one context unit before their provider call. Export consumes one user unit at accepted start, creates a 60-second monotonic actor cooldown and acquires actor/context/global leases; each page later consumes one context-total unit and one export-share unit. `exportShare = ratePerContextMinute < 2 ? 0 : floor(ratePerContextMinute * 0.75)`. `nextAllowedMono` is keyed by fiscal context, advances by `ceil(60_000/exportShare)` when a page reserves its token and does not reset between exports. Rejected prechecks mutate no raw state; accepted provider errors/aborts do not refund budget. The 5,000-actor capacity counts the union of current-window actor buckets, unexpired cooldowns and active actor leases, so wall-window jumps cannot grow state beyond the cap. Export admission is at most one active per actor and fiscal context, and `min(2, maxConcurrency - 1)` globally per instance. Coordination across multiple replicas is not claimed.

### Browser lifecycle

The export action snapshots applied filters without page. Duplicate clicks are dropped. Applied fiscal-filter changes cancel the active export; page-only changes do not. Logout, 401, navigation and unmount abort. A generation guard suppresses late state/download effects, and every temporary Object URL is revoked exactly once. The shared downloader returns `downloaded|empty`; 204 returns `empty` without reading a Blob or creating an anchor/Object URL. The existing PostgreSQL integration-error export keeps its backward-compatible download behavior.

### Observability

One aggregate export event may contain authenticated internal actor ID, context, correlation ID, allowlisted outcome, pages attempted/completed, rows, bytes, duration and abort/deadline/rate flags. It must not contain filters, document/purchase/access/fiscal/provider IDs, token, CNPJ, raw payload or CSV. Adapter page logs propagate only the correlation ID needed for tracing.

## Invariants
Smart Notas is the sole note/document source. Context selection never grants cross-context aggregation; document access does not persist provider identifiers, payloads, recipient PII or captured URLs. The candidate list/detail and export boundaries never fall back to PostgreSQL `logs` and never accept a consumer-provided CNPJ/token. Raw `idInterno` is not route authority or CSV content; it is visible only as `providerInternalId` in authenticated detail, while the signed `noteId` remains the context-bound route identity without a confidentiality claim. Frontend navigation may retain only non-sensitive canonical fiscal query state; fiscal DTO/cache/export state is memory-only, isolated by authenticated user/context/query, and cleared or aborted on logout/session disposal. CSV remains unchanged and excludes recipient name, recipient detail fields and provider internal ID.

## Cross-Module Considerations
Integration-error evidence stays with the integration-error-occurrences boundary; operational workflow stays with operational-cases.
