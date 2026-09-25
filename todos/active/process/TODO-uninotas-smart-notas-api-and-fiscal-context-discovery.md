# TODO — UniNotas Smart Notas API and Fiscal Context Discovery

## 0. Artifact Role

- **Artifact type:** `capped_no_code_ledger`
- **Active profile:** `strategic-cto`
- **Current phase (if Genesis):** `n/a`
- **Purpose in this session:** study the published Smart Notas contract and close the strategic decisions required to distinguish the Unifast and Prosperar fiscal contexts before implementation.
- **What it is not:** a tactical TODO, approval gate, implementation plan, code-execution contract, or authorization to call fiscal mutation endpoints.
- **Code-touch boundary:** `no code`
- **Companion artifacts:** `artifacts/feature-briefs/uninotas-smart-notas-central.md`

## 1. Current Objective

- Produce an evidence-backed recommendation for integrating Smart Notas into UniNotas, including API coverage, credential lifecycle, account-context semantics, source ownership, security boundaries, and story-sized implementation handoffs.

## 2. Confirmed Baseline

- The current canonical product is Monitor de Notas: it reads pipeline results persisted in the PostgreSQL `logs` table, writes only application-owned users/treatments, and has no documented business tenancy or organization model.
- The desired future product direction is UniNotas, a central for fiscal notes using Smart Notas, with two fiscal contexts: Unifast and Prosperar.
- The confirmed emission flow is `FastPay (Routerfy) -> n8n -> Smart Notas`. UniNotas obtains its complete note base, including note data and PDF/DANFE, from the Smart Notas API. The PostgreSQL `logs` boundary is retained only for integration failures.
- On 2026-09-25, the user explicitly confirmed the resulting source-ownership consequences: Smart Notas is the complete note source; PostgreSQL is error-only; `ref_id` is not note identity; ambiguous errors remain unlinked; and the first target has no persistent local note mirror.
- The official Smart Notas document is OpenAPI `3.0.0`, API version `1.0.0`, with relative server base `/api`.
- `POST /auth/login` returns a Bearer token documented with six-month validity; `POST /auth/logout` revokes the current token and `GET /auth/me` identifies its owner.
- Company-scoped operations require `X-Empresa-CNPJ`; the API documents that the CNPJ must belong to the authenticated user.
- The same document says each user may have one company, while company-scoped endpoints still require the CNPJ header. The confirmed product model is two independent fiscal contexts, one for Unifast and one for Prosperar; their exact company binding remains subject to the read-only CNPJ probes.
- The published surface includes authentication; company read/create/update; fiscal reports; note list/issue/detail/cancel/PDF/XML; and product list/read/create/update for NFS-e, NF-e, and split products.
- Issuance is asynchronous (`202`) and is followed through note detail; PDF/XML may also return `202` while unavailable.
- The published specification exposes no webhook and no explicit rate-limit, idempotency, retry, sandbox, or service-level contract.
- A local ignored backend environment file exists. Both independent token/CNPJ pairs are populated locally. No secret value or company identifier belongs in this TODO or Foundation.
- Redacted read-only probes on 2026-09-24 returned HTTP `200` from `GET /auth/me` for both tokens, with the documented `nome` and `email` fields. The two returned identities are distinct; their values were neither printed nor persisted.
- Company-context validation completed through redacted `GET /empresa` probes: both configured pairs returned `200`, and each normalized response CNPJ matched its configured context without any value being printed or persisted.
- Official OpenAPI fingerprint observed on 2026-09-24 America/Sao_Paulo: SHA-256 `cc2a415962dcff00b7d91d3a1bfe99544ec3bd1543b2e5f9d93df1b8ce686502`.
- The public OpenAPI was fetched again on 2026-09-25; its SHA-256 remained unchanged while completing the `logs` consumer and field/capability matrices.
- The current Foundation validator intentionally freezes the prior cutover tree; adding this ledger and its feature brief produces only `frozen lifecycle tree mismatch`. Publishing these new artifacts requires a separately approved process change rather than silently weakening that guard.

### 2.1 Confirmed Strategic Decisions

The following decisions and their stated architectural consequences were explicitly confirmed by the user on 2026-09-25. They define the target direction for this discovery ledger; they do not, by themselves, supersede the current canonical Foundation or authorize implementation.

| Decision ID | Confirmed decision | Consequence |
| --- | --- | --- |
| `SD-01` | Unifast and Prosperar are different fiscal contexts only. | Model them as separate `FiscalIssuerContext` values; do not introduce business tenancy, organizations, or independent product workspaces from this distinction. |
| `SD-02` | Delivery will proceed in stages, beginning with read-only capabilities. | List/detail/report/download discovery and integration precede issuance, cancellation, company mutation, and product mutation. |
| `SD-03` | The Smart Notas API is the source for the complete UniNotas note base, including list, detail, fiscal state, and documents. | Replace target note reads derived from `logs` with context-scoped Smart Notas API contracts. Any cache/projection is derived and must never become a competing note authority. |
| `SD-04` | Smart Notas fiscal state, integration-error state, and UniNotas work state are separate dimensions. | Preserve exact API fiscal status; classify PostgreSQL integration failures independently; use `OperationalCase.workflowStatus=ABERTO|RESOLVIDO|IGNORADO` without overwriting either source. |
| `SD-05` | FastPay (Routerfy) remains the long-term commercial origin and n8n orchestrates the Smart Notas call; PostgreSQL `logs` remains only the integration-failure source. | Exclude successful note rows from the target `logs` read model. Normalize actionable failed attempts as integration occurrences and correlate them to an API note only when evidence is deterministic. |
| `SD-06` | `OperationalCase` is the sole owner of UniNotas workflow state and treatment history. | A case may contain one optional Smart Notas API note and zero or more integration-error occurrences, but must have at least one source anchor; this supports both provider-note problems and failures that never created a note. |
| `SD-07` | The first delivery has an explicit active fiscal context, Unifast or Prosperar, and no aggregate “Todos” note list. | Query and paginate one Smart Notas context at a time; retain context in URL/navigation state and never merge provider pages implicitly. |
| `SD-08` | Returning quickly from `Erros` to `Geral` should reuse recently loaded note data. | Use a bounded in-memory session cache with stale-while-revalidate behavior; this is a UX optimization, never a persistent note mirror or fiscal authority. |

The current canonical documents and READMEs omit FastPay and n8n and describe `logs` as the complete event read model. That target-source statement is now known to be stale. A future canonical correction must record the confirmed pipeline, establish Smart Notas as the note-data source, and narrow PostgreSQL `logs` to integration failures while preserving the current running-code facts until implementation is approved.

### 2.2 Public OpenAPI Study Snapshot

The public-specification study is complete for the document fingerprint recorded above. It does not depend on company CNPJs; CNPJs are required only for later live company/resource validation.

| Surface | Operations | Public contract observed |
| --- | ---: | --- |
| Authentication | 3 | Login, logout, and current-user identity; login is the only operation without Bearer security |
| Company | 3 | Read, create, and update; read/update use `X-Empresa-CNPJ`; create is tied to the token owner and documents one company per user |
| Fiscal | 1 | Paginated fiscal reports by required date range, optional note type, document, and page |
| Notes | 6 | List, asynchronous issue, detail, cancel, PDF URL, and XML URL |
| Products | 8 | List/detail plus create/update for NFS-e, NF-e, and split products |
| **Total** | **21** | **9 GET, 8 POST, 4 PUT; no PATCH or DELETE operations are published** |

#### Confirmed Contract Characteristics

- Twenty operations require Bearer authentication; seventeen company/resource operations additionally require `X-Empresa-CNPJ`.
- Note and fiscal lists require a start/end date. Notes additionally filter by status, recipient document, purchase identifier, and page; no caller-controlled page size is documented.
- Note issuance returns HTTP `202` with an internal identifier and must be followed asynchronously. PDF/XML reads may also return `202` while the document is unavailable.
- Issuance type values (`55|56`), fiscal-report type values (`1|2`), and product type values (`1|2|3`) are separate provider vocabularies and must not be conflated in one unchecked enum.
- Company create/update uses `multipart/form-data` because it handles a digital certificate and certificate password. The published update operation is `PUT /empresa`, but its description instructs clients to send `POST` with `_method=PUT`.
- Company creation states that one user can have one company, but most operational endpoints still require a company CNPJ that belongs to that user. The header must remain explicit until live evidence resolves whether it is selection, defense-in-depth, or future multi-company preparation.
- Cancellation is a `POST` without a documented request body or cancellation-reason contract. Some NFS-e municipalities may require a manual procedure.
- Errors use several shapes (`error` versus `message` plus `errors`) across HTTP `400|401|403|404|409|422`; no single canonical provider error schema is published.

#### Published Contract Gaps

| Gap ID | Missing or underspecified contract | Product consequence | Required handling before implementation |
| --- | --- | --- | --- |
| `API-01` | No idempotency key or duplicate-issuance guarantee | A retry may create a duplicate fiscal note | Block issuance implementation until provider clarification or an approved application idempotency design exists |
| `API-02` | No rate-limit, timeout, retry, or backoff contract | Polling two contexts can overload or be throttled unpredictably | Establish conservative adapter policies and obtain provider limits |
| `API-03` | No webhook/callback contract | Async status requires polling | Keep polling bounded and preserve a future event-ingestion boundary |
| `API-04` | No sandbox/test-company contract | Fiscal mutations cannot be validated safely against production by default | Require provider sandbox or a separately approved controlled mutation lane |
| `API-05` | Fiscal reports and note detail return generic object schemas | Live evidence can guide an adapter but is not a formal provider compatibility guarantee | Redacted live shapes are captured; keep defensive decoding and request formal schemas before treating every field/type as stable |
| `API-06` | No documented token refresh flow; login tokens last six months | Rotation can interrupt both fiscal contexts | Model independent credential health/rotation per context; never refresh implicitly with stored passwords |
| `API-07` | No documented PDF/XML URL lifetime or access semantics | Persisted URLs may expire or leak document access | Treat returned URLs as transient until the provider confirms lifetime and authorization behavior |
| `API-08` | Most strings/numbers lack explicit size/range bounds | Provider validation behavior remains partly hidden | Apply product-owned defensive bounds and validate them against provider responses |
| `API-09` | No request/correlation identifier or SLA contract | Support and reconciliation may be difficult | Generate local correlation/audit identifiers without presenting them as provider guarantees |
| `API-10` | Company update method override conflicts with the declared HTTP operation | A conventional generated client may fail | Use an explicit provider adapter and contract test rather than raw generated-client assumptions |

#### Redacted Live Read Evidence — 2026-09-25

All five local Smart Notas settings required for read discovery are populated: base URL plus independent token/CNPJ pairs for Unifast and Prosperar. No value was printed, persisted, or copied into Foundation. The official OpenAPI SHA-256 remained `cc2a415962dcff00b7d91d3a1bfe99544ec3bd1543b2e5f9d93df1b8ce686502`.

Read-only probes used a bounded trailing 30-day window and produced the same endpoint-level outcome in both contexts:

| Endpoint | Unifast | Prosperar | Redacted structural evidence |
| --- | --- | --- | --- |
| `GET /empresa` | `200` | `200` | company object returned; normalized response CNPJ matched the configured context CNPJ |
| `GET /notas` | `200` | `200` | `{notas,page,perPage,total,totalPages}`; non-empty `notas`; pagination fields are numeric |
| `GET /notas/{idInterno}` | `200` | `200` | stable detail object shape observed from an API-listed note |
| `GET /notas/{idInterno}/pdf` | `200` | `200` | `{url}`; URL value was neither printed nor persisted |
| `GET /fiscal/relatorios` (`tipo=1`) | `200` | `200` | `{currentPage,paginacao,perPage,total,totalPages}` with rows under `paginacao.data` |

Observed note-list fields are `ambiente,chave,cidade,competencia,dataEmitir,dataPagamento,documento,email,estado,finalidade,idCompra,idInterno,modelo,nome,numeroNota,pais,plataforma,produto,status,valorTotal,valorUnitario`. All are strings in the sample except nullable `chave`, `competencia`, and `numeroNota`.

Observed detail fields are `ambiente,bairro,cep,chave,chaveNotaRef,cidade,competencia,complemento,dataEmissao,dataEmitir,dataPagamento,documento,email,estado,finalidade,idCompra,idInterno,inscricaoEstadual,inscricaoMunicipal,modelo,naturezaOperacao,nome,numero,numeroNota,pais,plataforma,produto,qnt,retorno,rua,status,telefone,valorTotal,valorUnitario`. Values are strings in the sample; `chaveNotaRef` and `complemento` demonstrated nullability.

Observed fiscal-report rows expose `cfop,chave,chaveNotaRef,cidade,cnpj,competencia,dataEmissao,dataPagamento,documento,estado,finalidade,idCompra,modelo,nome,nomeFantasia,nomeFiscal,numeroNota,pais,pdf,status,valorTotal,valorUnitario,xml`. Unlike note list/detail, report `modelo` and `finalidade` are numbers; `cfop` and `chaveNotaRef` demonstrated nullability.

Format evidence is consistent across both contexts: `dataEmitir`, `dataEmissao`, and `dataPagamento` use `DD/MM/YYYY`; `competencia` is an ISO-like datetime or null; monetary values are string integers or dot-decimal strings; detail `qnt` is a numeric string. `idInterno` and `idCompra` were present with no duplicate on either sampled first page, and sampled `idInterno` values did not overlap across contexts. This bounded observation does not prove provider-wide uniqueness.

#### Confirmed Initial Normalized Read Contract

- **Context-first query:** the first delivery requires one explicit `FiscalIssuerContext` per note-list request and maps provider pagination directly. A cross-context “Todos” list is deferred until stable merge/cursor semantics exist.
- **`FiscalNoteSummary`:** opaque `noteId`; `fiscalContext`; `providerIdInterno`; `purchaseId`; exact `providerStatus`; nullable fiscal number/access key/competence; environment/model/purpose/platform; recipient summary; product; and decimal-string unit/total values.
- **`FiscalNoteDetail`:** extends the summary with emission date, address/contact, state/municipal registrations, referenced key, operation nature, quantity, and sanitized provider return. Nullability follows observed live evidence and remains defensive for all provider fields.
- **Dates:** normalize provider `DD/MM/YYYY` into ISO local-date strings. Keep `competencia` as a provider-local datetime until timezone semantics are confirmed; never invent an offset.
- **Money/quantity:** parse with decimal-safe backend logic and expose canonical decimal strings; never use binary floating-point as the fiscal contract.
- **Reports:** use a dedicated adapter because `modelo` and `finalidade` have different wire types from note list/detail. Do not reuse the raw provider DTO across endpoints.
- **Raw data:** provider payloads stay behind the backend adapter and are not exposed wholesale to the frontend or persisted in Foundation.
- **Freshness/cache:** the first load and hard browser refresh read Smart Notas. Returning quickly to an already visited `Geral` query uses its in-memory session entry immediately; stale entries remain visible while the API revalidates in the background. Explicit refresh always requests the API. Automatic polling and persistent caching remain deferred.
- **Cache scope:** key every entry by authenticated session/user, `FiscalIssuerContext`, normalized filters, sort, and provider page. Keep it in process memory only—never `localStorage`, `sessionStorage`, IndexedDB, PostgreSQL, or Prisma—and clear it on logout/session expiry/user change.
- **Cache bounds:** store a fetch timestamp, use a short freshness window and bounded retention/entry count. Exact TTL/cap are tactical performance settings; the initial recommendation is 60 seconds fresh and five minutes retained in memory.
- **Stale failure:** if revalidation fails, preserve the cached table with an explicit stale/error warning and last-update time. With no cached entry, render the normal error state; never convert provider failure into an empty result.
- **Race safety:** deduplicate concurrent requests for the same key; cancel superseded filter/page/context requests when possible; apply a response to visible state only when its key still matches the active query; clear/ignore pending work on logout or unmount.
- **Failure semantics:** an unavailable selected context returns an explicit provider-unavailable error. Any future aggregate view must carry independent per-context outcomes and may never turn one context failure into an empty-success response.
- **Documents:** resolve PDF/XML on demand from the API note identity. Redirect versus backend proxy remains open until URL lifetime and authorization behavior are confirmed.

#### Strategic Recommendation From Public Evidence

- Model Unifast and Prosperar as separate `FiscalIssuerContext` values, not tenants. Each context owns one backend-only credential reference, one expected CNPJ reference, health/rotation state, and an immutable internal key.
- Never accept a raw token or arbitrary provider CNPJ from the frontend. The backend resolves the selected internal context to its configured credential/header pair.
- Preserve issuer provenance on every API note, document request, integration error, audit entry, cache key, and asynchronous readiness check. Aggregated views may combine contexts only after each record retains its origin.
- Deliver read-only Smart Notas note list/detail/PDF capabilities before issuance, cancellation, company mutation, or product mutation. Mutation stories stay separate because their provider contracts lack idempotency and safe-environment guarantees.
- Use the Smart Notas API as the note source for lists, detail, fiscal status, customer/sale data, reports, and documents. Do not use a successful `logs` row as a note record or fallback fiscal truth.
- Introduce a product-facing note identity mapped to `(provider, fiscalContext, providerIdInterno)`; retain provider `idCompra` as non-unique correlation/search data. This identity contract does not require UniNotas to own a second authoritative note database.
- Preserve a dedicated, sanitized integration-error projection from PostgreSQL instead of exposing raw automation payloads as the UniNotas domain model.

### 2.3 Smart Notas Note-Identity Contract

- **Product identity:** each normalized API note receives an opaque immutable `noteId` owned by UniNotas. The tactical design may materialize or deterministically derive it, but clients never construct provider credentials or company identifiers.
- **Provider identity:** map `provider=smart_notas`, `fiscalContext`, and API `providerIdInterno`; enforce logical uniqueness on `(provider, fiscalContext, providerIdInterno)` wherever notes are normalized or cached.
- **Provider scope:** `providerIdInterno` is the documented lookup identifier for Smart Notas detail/PDF/XML calls, but the public contract does not guarantee global uniqueness and every call is still company-scoped. It is therefore not the standalone product key.
- **Order correlation:** retain API `idCompra`, but do not make it unique. A PostgreSQL error's `idTransacao` may be compared with `idCompra` only after semantic and uniqueness evidence exists.
- **Fiscal number:** `numeroNota` is display/search data only. It may be absent before authorization and is not globally unique without issuer, model, series, and provider rules.
- **Error correlation:** `ref_id` identifies/correlates PostgreSQL integration-error work only. It is never a note route key, provider identity, or uniqueness proof.
- **Route boundary:** the backend resolves `noteId` to its trusted fiscal context and API `idInterno`, then selects the correct backend-only token and CNPJ. No consumer supplies provider credentials or an arbitrary CNPJ.
- **Authority boundary:** the first target does not persist a local fiscal-note mirror. Any later performance cache/projection requires separate approval, is derived from the API, and must have explicit freshness/staleness and rebuild semantics.

### 2.4 Source-Ownership Consequence

The sources describe different responsibilities in the confirmed pipeline. FastPay (Routerfy) originates commercial data, n8n automates the Smart Notas request, Smart Notas owns the resulting fiscal-note data exposed by its API, and PostgreSQL preserves integration failures for operational diagnosis.

Therefore, the target has one note source plus one failure-evidence source:

- **FastPay (Routerfy) owns:** originating sale/order data supplied to the automation flow.
- **n8n owns:** orchestration of the Smart Notas request and the still-to-be-confirmed write of failed integration evidence to PostgreSQL.
- **Smart Notas API owns for UniNotas:** the complete fiscal-note read source, including list, detail, status, issuer-scoped data, PDF/DANFE, XML, and approved reports.
- **PostgreSQL `logs` owns for UniNotas:** durable evidence only for failed integration attempts, including sanitized request/response context needed for diagnosis.
- **UniNotas owns:** fiscal-context resolution, normalized API contracts, safe association of notes with integration errors, `OperationalCase`, workflow/treatments, audit authorship, and product-facing identifiers.

The error store must never populate or override an API note's fiscal fields. UniNotas exposes provenance and keeps an unlinked error actionable when deterministic note correlation is unavailable.

### 2.5 Confirmed Pipeline-Occurrence Contract

Failed attempts persisted by the FastPay/n8n/Smart Notas integration remain a permanent operational capability. They are normalized as `EmissionPipelineIssue`; successful notes are read from the API rather than reconstructed from `logs`.

- **Identity:** each occurrence has an opaque UniNotas `issueId`. Because `logs` has no primary key and `ref_id` may repeat, ingestion must deduplicate through a deterministic source fingerprint defined and tested in the tactical design.
- **Minimum normalized evidence:** `source=postgresql_integration_error`, internal `fiscalContext`, observed timestamp, sanitized category/summary, rejected field paths when present, optional `idTransacao`, optional Smart Notas identifier, source reference, correlation result, and optional operational-case link.
- **Categories:** begin with `VALIDATION`, `ALREADY_ISSUED_OR_DUPLICATE`, `TRANSPORT`, `PROVIDER_FAILURE`, and `UNKNOWN`; classification preserves the sanitized source message so operators can audit the derived category.
- **Fiscal-context resolution:** derive context only from trusted issuer evidence mapped server-side to `FiscalIssuerContext`. Unknown or ambiguous context is quarantined; it is never guessed from customer data.
- **API correlation order:** exact Smart Notas identifier plus fiscal context first; exact and proven-unique `(fiscalContext,idTransacao/idCompra)` second; otherwise remain unlinked. Never match by customer, value, product, or timestamp.
- **Presentation:** linked occurrences appear in a separate “Ocorrências de integração” section on note detail. Unlinked occurrences remain actionable in a dedicated “Falhas de integração” queue.
- **State:** the Smart Notas API fiscal status is unchanged. The confirmed owner of `ABERTO|RESOLVIDO|IGNORADO` and treatment history is a UniNotas `OperationalCase` with one optional API note and zero or more occurrences, requiring at least one source anchor. A case may therefore represent an API-note problem or integration failures for which no note exists.
- **Raw-data boundary:** do not copy or expose full `req_raw`, stack traces, secrets, or unrestricted `req_resp` by default. Keep the external source read-only and persist only the minimum sanitized evidence required for diagnosis and audit.
- **Lifecycle:** this is a long-term capability while the FastPay/n8n pipeline persists integration errors. Its later retirement requires a separately approved topology change.

### 2.6 Complete Capability Matrix — Smart Notas Notes plus PostgreSQL Integration Errors

Legend: `documented` is guaranteed by the current public OpenAPI; `live-shape` requires a redacted read-only probe; `error-store` comes only from failed integration rows; `local` is UniNotas-owned.

| Capability | Current `logs` behavior | Smart Notas public evidence | Target disposition | Evidence state / gate |
| --- | --- | --- | --- | --- |
| Note identity | `ref_id` correlates event rows but may repeat | `idInterno` drives detail/PDF/XML | Opaque `noteId` mapped to `(provider,fiscalContext,idInterno)`; never derive note identity from `logs` | identity design confirmed; materialization tactical |
| Fiscal-context isolation | No issuer-context domain; `org_path='SmartNotas'` only | Every resource call requires token plus `X-Empresa-CNPJ` | Mandatory `FiscalIssuerContext` on API queries, normalized notes, cache, audit, and error correlation | **Confirmed design and live binding evidence** |
| Note list | SQL currently projects event rows | `GET /notas` lists provider notes | Replace the target note list with context-scoped API reads; query Unifast and Prosperar independently and preserve provenance | `documented`; live response proof pending |
| Date range | Optional bounds over persisted `event_at` | API list requires start/end dates | Adopt the API date contract; define safe default and maximum windows from quotas/volume | policy pending |
| Ordering | SQL currently controls `event_at` ordering | No API ordering guarantee is published | Do not promise global ordering beyond proven API fields; cross-context merge semantics require explicit design | provider gap |
| Pagination | UniNotas currently controls SQL limit/page | API accepts `page` but not caller page size | Model independent provider cursors/pages per fiscal context; do not fake stable global pagination | tactical contract pending |
| Fiscal status | SQL heuristics currently derive `ERRO|PENDENTE|SUCESSO` | API publishes provider note statuses | Use exact normalized API status for notes; integration errors remain a separate occurrence state | `documented`; vocabulary/live shape pending |
| Local workflow | Latest treatment currently overwrites effective display status | No provider equivalent | `OperationalCase` exclusively owns `ABERTO|RESOLVIDO|IGNORADO`; never overwrite API fiscal status | **Confirmed design** |
| Summary counters | SQL currently groups event classifications | No API summary endpoint | Compute only from an explicitly bounded API query or derived cache with visible freshness; never use success rows from `logs` | volume/quotas blocker |
| Search | SQL currently supports broad free text | API filters status, recipient document, `idCompra`, dates, and page | First contract exposes only provider-supported search; richer indexed search requires a separate derived projection decision | `documented`; UX decision pending |
| Product data | SQL currently extracts request product data | Product and note APIs expose provider-side data | Source note product data from API response; use product catalog only as supporting provider data | detail live shape pending |
| Customer data | SQL currently extracts request customer data | Note detail schema is generic | Source customer data from API note detail; freeze DTO only after redacted live-shape proof | `live-shape` blocker |
| Sale/order data | SQL currently extracts request/sale fields | API list exposes `idCompra` and `valorTotal`; detail is generic | Source note business fields from API; do not backfill missing fields from successful log rows | `live-shape` blocker |
| Issuer/company data | SQL currently extracts producer snapshot | `GET /empresa` has typed company response | Resolve issuer through `FiscalIssuerContext`; distinguish current company profile from historical note fields | `documented` and live-probed in both contexts |
| Integration error | SQL parses response/transport failures | API cannot expose failures that never created a note | Retain only sanitized failed-attempt evidence from PostgreSQL, including missing address and duplicate/already-issued outcomes | `error-store` |
| Rejected fields | SQL parses captured `422` payloads | API documents structured validation for calls | Preserve verified field paths on the integration occurrence; do not inject them into the API note DTO | `error-store` |
| Attempt history | SQL groups retries by transaction/reference | No provider attempt-history endpoint | Keep failed pipeline attempt history in `OperationalCase`; successful notes come from API | `error-store`; grouping pending |
| Treatment | Current writes are keyed by `ref_id` | No provider equivalent | Move workflow/history to `OperationalCase`, which may anchor an API note, integration errors, or both | **Confirmed domain boundary** |
| Raw payload/response | Current UI can expose `req_raw`/`req_resp` | API has no equivalent | Replace routine raw display with sanitized failure evidence; privileged raw access needs a separate security decision | access/retention pending |
| CSV export | Current export is SQL-backed | No API export endpoint | Build a bounded API-backed export only after pagination, quotas, and field-shape contracts are proven | provider/tactical blocker |
| Operational monitoring | Current monitor counts SQL classifications | No provider aggregate/health endpoint | Separate Smart Notas API health/freshness from PostgreSQL integration-error counts | design pending |
| Near-real-time | Current flow polls/listens to `logs` | No API webhook/callback | `logs` invalidation refreshes only the error queue; note refresh requires bounded API polling/manual refresh until a provider event contract exists | cadence/quotas pending |
| PDF/DANFE | Not a first-class current capability | `GET /notas/{idInterno}/pdf` returns URL or `202` | Fetch through the same context-scoped API note identity; no PostgreSQL correlation is needed for normal document access | `documented`; URL lifetime pending |
| Fiscal reports | Not represented in current UI | `GET /fiscal/relatorios` exists with generic response schema | API-backed read capability after live-shape proof | `live-shape` blocker |
| Issuance/cancellation | FastPay/n8n currently own issuance flow | API exposes asynchronous issuance and cancellation | Keep outside the first read-only slice; any ownership change requires a separate strategic decision | explicitly deferred |
| Development data | Current tooling mirrors `logs` | Provider offers no documented sandbox | Use API contract fixtures for notes/documents and privacy-safe failed-attempt fixtures for `logs` | policy pending |

### 2.7 Field-Level Source Matrix

| Current product field/group | Target source | Target contract |
| --- | --- | --- |
| `refId` | PostgreSQL integration error | Retain only as failure-occurrence/treatment migration correlation; it is not a note identifier |
| `idSmartNotas` | PostgreSQL integration error | Optional exact correlation candidate to API `idInterno`; absence is expected when failure occurred before note creation |
| `eventAt` | PostgreSQL integration error | Preserve as failed-attempt observation time, never as API note issuance/update time |
| `situacaoOriginal` | Split | Replace note classification with exact API fiscal status; retain a separate normalized error category for log occurrences |
| `situacao` | Smart Notas API plus UniNotas | Keep `providerFiscalStatus` independent from `OperationalCase.workflowStatus`; log-error state remains occurrence evidence |
| `mensagem` and `orientacao` | PostgreSQL error plus UniNotas rules | Preserve sanitized integration-failure message and derive operator guidance without injecting it into the API note's fiscal status |
| `clienteNome`, `clienteDocumento`, `cliente.*` | Smart Notas note API | Freeze normalized fields/nullability only after redacted detail probes; error evidence may retain only the minimum needed for diagnosis |
| `produto`, `codProduto` | Smart Notas note/product API | Source note product information from API; do not reconstruct successful notes from request logs |
| `valorVenda` | Smart Notas note API | Map the verified API monetary field and scale |
| `idTransacao` | PostgreSQL integration error | Keep as failure correlation and verify semantics against API `idCompra`; neither is note identity or assumed unique |
| API `idCompra` | Smart Notas note API | Use as provider-supported search/correlation data, not as product identity |
| payment/date/warranty/split/type fields | Smart Notas detail API or removal | Each field requires live response proof; missing API fields are not silently backfilled from success logs |
| `produtor.*` | Fiscal context plus Smart Notas API | Resolve current issuer through context/`GET /empresa`; historical issuer fields require note-detail evidence |
| `tentativas` and history entries | PostgreSQL integration errors | Represent failed pipeline occurrences only; do not treat absence as proof of first-attempt success |
| `camposPendentes` | PostgreSQL sanitized integration errors | Preserve verified rejected paths on the occurrence; do not present guesses as provider-note fields |
| `payload`, `resposta`, provenance | PostgreSQL integration errors | Minimize/sanitize and identify FastPay, n8n, Smart Notas, PostgreSQL, and UniNotas roles explicitly |

### 2.8 Smart Notas Note Base and Integration-Error Boundary

The Smart Notas API is the target source for all fiscal-note data. PostgreSQL is not a note mirror or success-result fallback; UniNotas reads it only for failed integration attempts that may not exist in Smart Notas.

The safe composition contract is:

1. Resolve the selected internal `FiscalIssuerContext` to its backend-only token and CNPJ.
2. Query Smart Notas independently for Unifast and Prosperar; preserve context on every normalized note and never collapse provider pagination silently.
3. Read note detail, fiscal status, PDF/DANFE, XML, and approved reports from the Smart Notas API using context-scoped identifiers.
4. Treat API `202` for document readiness as provider state independent from local workflow.
5. Treat context authentication, authorization, timeout, rate-limit, and provider failures as explicit partial/unavailable outcomes; never return an empty-success note base.
6. Read PostgreSQL only through an integration-error adapter that excludes successful note rows from the target domain.
7. Correlate an error to an API note only by exact trusted context plus provider identifier, or by a separately proven exact business-key rule; otherwise keep it unlinked.
8. Let `OperationalCase` combine the optional API note and zero or more integration errors without mutating source facts.
9. Do not persist a local note mirror in the first target. Any later cache/projection is a separately approved, disposable optimization with freshness, rebuild, and isolation contracts.
10. Use `logs` notifications only for error-queue invalidation. Define API note refresh separately because the provider publishes no webhook.

### 2.9 Migration Surface Inventory

| Surface | Current coupling | Required target action |
| --- | --- | --- |
| Backend `logs` module | Raw SQL currently powers all event list/detail/filter/export contracts | Narrow to an integration-error adapter and case evidence; add a context-scoped Smart Notas note gateway/application boundary for primary note reads |
| Prisma/database | Treatments keyed by `ref_id`; no case model | Introduce `OperationalCase` and source links through a later approved schema TODO; any API-note cache is derived, optional, and separately justified |
| Realtime | Database polling/LISTEN on all `logs` rows | Restrict database invalidation to the error queue; define bounded API refresh/manual refresh for notes |
| Monitoring | Reuses log classification counters | Separate Smart Notas API availability/freshness by context from integration-error volume and ingestion health |
| Frontend | Event routes and log vocabulary represent all notes; `ListaEventos` already uses a component-local `Map` cache | Establish API-backed note list/detail/documents plus a distinct integration-failure queue; lift a bounded cache above tab/route unmount when necessary so `Geral -> Erros -> Geral` preserves recent data without persistent storage |
| Dev tooling | Mirrors broad production `logs` data | Retain only privacy-safe failed-attempt fixtures; use controlled API fixtures for note list/detail/PDF and both fiscal contexts |
| Tests/docs | Journeys assume `ref_id` and SQL are the complete note source | Add API pagination/context isolation/partial-failure/live-shape coverage and prove that successful log rows cannot populate target note views |

The matrices establish Smart Notas as the sole fiscal-note source and PostgreSQL `logs` as the complementary integration-error source.

### 2.10 Planned Async Race Contract for Note Navigation

| Surface | Failure mode | Required policy | Later validation |
| --- | --- | --- | --- |
| `Geral -> Erros -> Geral` | note screen remount loses useful data or late response changes the wrong screen | session-memory cache survives route/tab unmount; pending response is ignored outside its active key | browser journey with immediate return and delayed API |
| Fiscal-context switch | Unifast response appears under Prosperar or vice versa | strict context in cache/request key; cancel previous; last active key alone may update visible state | rapid alternating context changes |
| Filter/page change | older slower response overwrites newer selection | cancel previous plus keyed last-write-wins guard | burst levels `5/10/20` across filter/page changes |
| Repeated refresh | duplicate provider calls race and flicker state | deduplicate/serialize per exact key; one visible refresh state | burst levels `5/10/20` on refresh |
| Revalidation failure with cache | valid rows disappear or failure looks empty | keep stale rows, label them stale, expose retry/error | cached success followed by forced provider error |
| Logout/session expiry during request | another user can observe prior cached fiscal data | abort/ignore requests and synchronously clear all cache entries | logout/navigation while delayed request is in flight |

These are planning requirements, not executed race evidence. The later React tactical TODO must route them through the frontend race-validation lane.

## 3. Gap / Decision Register

| ID | Topic | Current State | Why It Matters | Current Handling | Next Target |
| --- | --- | --- | --- | --- | --- |
| `G-01` | Product identity and mandate | `Open` | UniNotas materially expands the current monitor purpose | strategic review now | Decide whether UniNotas is a canonical rename or a new product boundary |
| `G-02` | Smart Notas notes versus PostgreSQL errors | `Closed` | Note data and failed-attempt evidence must not be conflated | Smart Notas API is the complete note source; PostgreSQL `logs` is retained only for integration failures | Carry the split ownership into canonical correction and tactical adapters |
| `G-03` | Fiscal-context vocabulary | `Closed` | “Account” could incorrectly introduce tenancy or conflate company and credential | Unifast and Prosperar are separate `FiscalIssuerContext` values only; they are not tenants | Carry the vocabulary into canonical entities and consumer contracts |
| `G-04` | Unifast/Prosperar credential topology | `Closed` | Prevents cross-company leakage and unsafe rotation | distinct token identities validated; both context-scoped `GET /empresa` probes returned `200`, and each response CNPJ matched its configured context | Carry independent credential/CNPJ resolution into the tactical adapter |
| `G-05` | Secret lifecycle | `Open` | Tokens last six months and must be rotated without frontend exposure | security design now | Define storage, injection, rotation, revocation, and failure behavior |
| `G-06` | Endpoint and schema matrix | `Closed` | Normalization and consumer contracts require more than route names | current public specification mapped with explicit gap register | Refresh on OpenAPI fingerprint change or provider clarification |
| `G-07` | Read/write release boundary | `Closed` | Issuance, cancellation, company, and product mutations have higher fiscal risk | user confirmed staged, read-only-first delivery | Decompose read and mutation work into separate tactical TODOs |
| `G-08` | API refresh and asynchronous readiness | `Partial` | API notes need freshness behavior and PDF/XML may return `202` | expose explicit loading/stale/partial/document-processing outcomes; never substitute an empty list or `logs` result | Confirm polling/refresh cadence, URL lifetime, timeouts, quotas, and terminal document failures |
| `G-09` | Idempotency and duplicate issuance | `Open` | Retried writes can create fiscal duplicates | blocking provider question for mutations | Obtain provider guarantee or define application idempotency strategy |
| `G-10` | Rate limits and resilience | `Open` | Two accounts multiply call volume and failure modes | provider clarification | Determine quotas, retry headers, timeouts, and backoff expectations |
| `G-11` | Authorization and audit | `Open` | Users may have different rights per issuer and action | strategic/security design | Define view/issue/cancel/download permissions and audit fields |
| `G-12` | UI distinction | `Partial` | Operators must never confuse Unifast with Prosperar | context-first list and no initial aggregate view are confirmed; explicit textual context remains mandatory | Define selector/tab presentation, default context, and URL persistence in the UI tactical TODO |
| `G-13` | Data ownership and retention | `Partial` | Must distinguish commercial origin, automation, API note data, integration errors, and local workflow | FastPay originates, n8n orchestrates, Smart Notas API owns note reads, PostgreSQL stores failed-attempt evidence, and UniNotas owns normalization/workflow/audit | Confirm the error writer/filter and define sanitized evidence, API-cache, document URL, and raw-source retention policies |
| `G-14` | Test/sandbox availability | `Open` | Safe integration validation cannot rely on production fiscal mutations | provider clarification | Obtain sandbox/test company or approved controlled validation process |
| `G-15` | OpenAPI drift | `Partial` | Provider spec is served dynamically without an advertised version lifecycle | track fingerprint | Define snapshot/fingerprint and change-detection policy |
| `G-16` | Foundation publication guard | `Open` | The frozen cutover validator rejects any newly tracked artifact by design | separate process TODO | Evolve the publication-tree contract without weakening privacy, identity, ownership, or lifecycle checks |
| `G-17` | Canonical API-note identity | `Partial` | Current routes use PostgreSQL `ref_id`, while all target note resources use context-scoped Smart Notas `idInterno` | opaque `noteId` maps to `(provider,fiscalContext,idInterno)` without treating `ref_id` or `idCompra` as note identity | Decide materialized versus deterministic mapping and freeze context-safe routes |
| `G-18` | Smart Notas field parity | `Partial` | The target UI must source note/customer/sale/status fields from API rather than successful log payloads | redacted list/detail/report live shapes and wire-type differences are recorded; a normalized DTO candidate is defined | Confirm target UI field selection and retain defensive handling because the live shape is not a formal provider schema |
| `G-19` | Treatment and history migration | `Partial` | Treatments are local product data, but their only link is `ref_id` | confirmed `OperationalCase` owns workflow/history and contains one optional note plus zero or more pipeline occurrences, with at least one source anchor | Define existing-treatment migration, case grouping, merge/split, and deduplication rules |
| `G-20` | API note read strategy | `Partial` | Provider pagination, no webhook, tab navigation, and generic detail shapes affect usability and resilience | selected-context API reads plus bounded session-memory stale-while-revalidate cache are confirmed; no persistent mirror or initial aggregate list | Freeze tactical TTL/cap, route ownership, request cancellation/deduplication, document delivery, and safe error mapping |
| `G-21` | Pipeline failure visibility | `Closed` | FastPay/n8n/Smart Notas pipeline errors may explain missing notes, invalid addresses, or duplicate issuance | retain permanent sanitized pipeline occurrences, linked to notes when deterministic and otherwise shown in a dedicated queue | Carry contract into canonical modules and tactical ingestion/UI TODOs |
| `G-22` | Integration-error-to-note correlation | `Partial` | Wrong links can mix companies or attach a failure to the wrong API note | exact context plus provider identifier first; proven exact `idTransacao/idCompra` second; otherwise unlinked; no fuzzy matching | Verify identifier availability and fiscal-context evidence in redacted error rows |
| `G-23` | Integration-error persistence ownership | `Partial` | Runtime ownership and incident diagnosis depend on knowing who writes and filters PostgreSQL failures | the target role is error-only, but the exact writer and failure-selection contract are not evidenced in this repository | Confirm whether n8n performs the write and exactly which failures are persisted, without copying production payloads |

## 4. Current Order

1. Confirm which component writes PostgreSQL integration errors and the exact rule that excludes successes from the target error boundary.
2. Validate deterministic error-to-note correlation fields against redacted failure rows; keep all ambiguous failures unlinked.
3. Define `OperationalCase` grouping and existing-treatment migration rules.
4. Produce the canonical correction and bounded tactical TODO candidates for separate approval, including separate API-note and error/case delivery slices.

## 5. Explicitly Out of Scope

- Product code, tests, database migrations, tracked runtime configuration, deployment changes, or canonical Foundation rewrites.
- Persisting tokens, passwords, company identifiers, production payloads, personal data, or provider responses in Git or Foundation.
- Calling note issuance, cancellation, company mutation, product mutation, logout, or any other state-changing Smart Notas endpoint.
- Treating Unifast/Prosperar as tenants or organizations; the confirmed distinction is fiscal context only. User permissions per fiscal context remain a separate authorization decision.
- Renaming Monitor de Notas, changing repository identity, or rewriting the confirmed FastPay/n8n/Smart Notas plus error-only PostgreSQL topology in canonical docs during this ledger.
- Modifying or weakening the Foundation deterministic validator as an incidental part of API discovery.

## 6. Exit Condition

- The API study has evidence-backed contracts for Smart Notas as the full note source and PostgreSQL as the integration-error source; both credential contexts are validated through redacted read-only evidence or explicitly marked blocked; API DTO/pagination/freshness, error correlation, treatment/history migration, and ownership are ready for canonical approval; and each implementation story has a bounded tactical TODO candidate with module anchors and validation expectations.

## 7. Next Exact Step

- Investigate the error-only PostgreSQL writer/filter boundary without persisting production payloads, then validate deterministic error-to-note correlation evidence.
