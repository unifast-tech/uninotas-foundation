# Events and Classification

## Module Intent & Boundaries
- **Core scope:** `uninotas`
- **Subscope:** `events-and-classification`
- **EnvironmentType:** `landlord` (PACED technical adapter only; no business tenancy)
- **Runtime authority state:** `current_runtime`
- **Owned capabilities:** `note_read_model`, `integration_error_read_model`
- **Planned capabilities:** none
- **Out-of-scope guardrails:** Writing external `logs`, defining source ingestion/ownership, or treating `ref_id` as a primary key.
- **Dependency boundaries:** Read-only SQL over `logs`; API consumers use explicit list, filter, summary, detail, and export contracts.

## Canonical Coverage Status
- **Canonical Coverage Status:** `Current`
- **Last Canonicalization Review:** `TODO-uninotas-foundation-project-rebase`
- **Remaining Migration Scope:** `none`

## Specification
Owns the current mixed external emission-event projection—success, pending, error, and treated views—plus filters, pagination, export, and original/effective classification. The external source-row owner, writer, ingestion, and filter semantics are unknown. SQL and TypeScript classification projections must preserve equivalent semantics. Effective status incorporates the latest treatment; `PENDENTE` restores original status.

## Observed API Contract

All routes below use base path `/api/v1`, require the normal bearer JWT guard, and accept active users of any profile. Common list filters are `pagina` integer default 1/minimum 1, `limite` integer default 25/range 1..200, `direcao=asc|desc` default `desc`, `situacao=TODOS|ERRO|PENDENTE|SUCESSO|TRATADOS` default `ERRO`, optional trimmed `busca` up to 120 characters, optional exact `produto` up to 200 characters, and optional ISO-8601 `dataInicio`/`dataFim`.

| Route | Request | Status / media | Successful response |
| --- | --- | --- | --- |
| `GET /eventos` | common filters | HTTP 200 `application/json` | `{dados,meta}`; `meta={total,pagina,limite,totalPaginas,temProxima}` and each summary has `refId,eventAt,situacao,situacaoOriginal,mensagem,idSmartNotas,clienteNome,clienteDocumento,produto,valorVenda,meioPagamento,tentativas` |
| `GET /eventos/resumo` | common filters | HTTP 200 `application/json` | `{total,erro,pendente,sucesso,tratados}` |
| `GET /eventos/produtos` | none | HTTP 200 `application/json` | array of `{nome,eventos,erros}` |
| `GET /eventos/exportar` | common filters; pagination is replaced by export cap | HTTP 200 `text/csv; charset=utf-8` | attachment filename, semicolon-separated fixed columns `refId,idTransacao,eventAt,situacao,mensagem,idSmartNotas,clienteNome,clienteDocumento,clienteEmail,produto,codProduto,valorVenda,meioPagamento`, capped at 20,000 rows |
| `GET /eventos/:refId` | correlation `refId` | HTTP 200 `application/json` | summary fields plus `orientacao,origem,cliente,venda,produtor,historico,camposPendentes,payload,resposta` |
| `GET /eventos/:refId/payload` | correlation `refId` | HTTP 200 `application/json` | `{enviado,resposta}` |

Within event detail, `cliente={nome,documento,email,telefone,logradouro,numero,complemento,bairro,cidade,cep,pais}`, `venda={produto,codProduto,valorVenda,avista,meioPagamento,dataPagamento,idTransacao,garantia,split,tipoProduto}`, `produtor={razaoSocial,documento}`, each `historico` entry is `{em,mensagem,ok,autorNome}`, and each `camposPendentes` entry is `{caminho,rotulo,recusadoPeloSmartNotas}`. Nullable/optional source fields remain nullable/optional; the contract does not invent completeness.

Validation/auth/not-found failures use the standard error body `{statusCode,erro,mensagem,caminho,timestamp}`; an unknown `refId` is 404, not an empty projection. Treatment commands are owned exclusively by [treatments and history](treatments-and-history.md#observed-treatment-contract).

## Ownership Invariant

The cross-module data-ownership invariant is owned by the [project constitution](../project_constitution.md#invariants). This module performs read-only projections over external `logs` evidence and owns no application write contract.

## Purpose, Owned Entities, and Workflows
**Purpose:** provide the current authoritative read model for legacy emission-event investigation until the planned capability transitions complete. **Owned/orchestrated entities:** `LogEvent` and classification projections; external persisted source-row owner/writer/ingestion semantics remain unknown. **Workflows/capabilities:** list, filter, paginate, summarize, export, and inspect detail. **Invariants/validation/auth:** source remains read-only, SmartNotas filter applies, `ref_id` is correlation only, and protected API access is enforced by the identity boundary. **Observed contracts:** raw SQL, classifier, mapper, routes, request bounds, response fields, media type, and errors above are evidenced; no SLO is asserted.

## Cross-Module Considerations
External `logs` writer/filter behavior is unknown; [treatments and history](treatments-and-history.md) owns application treatment writes.

## Failure and Degradation Modes
Source-query failure is not represented as zero matching events; clients use the API result/error contract rather than treating an export or summary as source truth.
