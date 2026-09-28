# TODO — Exportar todas as notas do filtro fiscal ativo

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** `Draft`
- **Created:** `2026-09-28`
- **Owner:** `Delphi / Operational Coder`, sob autoridade humana do usuário

## Context

O usuário confirmou que `Exportar` deve baixar todos os registros correspondentes ao contexto e aos filtros aplicados na Geral, independentemente da página visível. O navegador não deve caminhar páginas: um endpoint NestJS autenticado percorre Smart Notas sequencialmente, valida consistência, monta o arquivo somente após sucesso integral e falha sem download quando a travessia excede limites ou fica incoerente.

Smart Notas evidencia paginação numérica, mas não cursor/snapshot nem ordenação estável. Portanto, esta entrega garante uma travessia completa e bounded das páginas retornadas, com verificações detectáveis; ela não promete fotografia transacional se dados mudarem de forma indetectável durante a exportação.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/uninotas-fiscal-workspace-improvements.md`
- **Story:** `ST-EXPORT`
- **Why this is bounded:** um endpoint read-only, um serializer fiscal-local e um CTA na Geral compartilham o mesmo contrato de filtro/arquivo e os mesmos riscos de carga/cancelamento.
- **Sequencing:** executar após ou de forma serializada com o TODO UX; nunca haverá dois escritores de produto simultâneos.

## Contract Boundary

- `GET /api/v1/notas/exportar` usa um único `FiscalIssuerContext`, os mesmos filtros da listagem e rejeita `pagina`.
- Todos os perfis leitores atuais (`ADMIN`, `GESTOR`, `ANALISTA`, `LEITOR`) podem exportar; nenhuma permissão de tratamento muda.
- O backend possui paginação, consistência, admissão, pacing, deadline, serialização e observabilidade.
- O frontend possui somente snapshot dos filtros aplicados, ciclo de vida/abort e entrega do Blob.
- Nenhum byte do CSV é enviado antes de toda a travessia e serialização passarem.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Next exact step:** congelar/revisar este contrato, obter `preflight-go` e solicitar `APROVADO`.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** achados de arquitetura/performance foram incorporados; novo baseline e reviews ainda são necessários.
- **Exit condition:** aprovação explícita e authority guard pós-aprovação em `go`, ou bloqueio formal.

## Provisional Notes

- **Missing for production-ready:** implementação, carga determinística, auditorias, smoke/capacidade real e cutover/deploy separado.
- **Revisit criteria:** necessidade acima dos limites, snapshot forte, XLSX, fila/worker, persistência, multi-contexto, nova configuração ou retry.
- **Dependencies unblocked:** ports/fixtures permitem implementação e verificação local; quota, latência e estabilidade reais continuam incertezas de cutover, não pré-requisitos para código local.

## Blocker Notes

- **Blocked:** `no` para implementação local com ports/fixtures.
- **Current blocker:** `none`.
- **Production caveat:** ativação real depende de smoke/capacity do cutover; não é autoridade para deploy.

## Scope

- [ ] `SCOPE-EX-01` Criar contrato compartilhado de filtros fiscais, com paginação apenas na listagem e DTO de exportação que rejeita `pagina`/campos desconhecidos.
- [ ] `SCOPE-EX-02` Expor `GET /api/v1/notas/exportar` antes de `:noteId`, protegido pelos leitores existentes e pelo feature gate fiscal.
- [ ] `SCOPE-EX-03` Percorrer páginas sequencialmente com limites de linhas, páginas, duração, bytes, pacing e admissão por contexto.
- [ ] `SCOPE-EX-04` Validar metadados/contagem/IDs e falhar sem arquivo em inconsistência, erro, abort, deadline ou saturação.
- [ ] `SCOPE-EX-05` Produzir CSV fiscal-local determinístico, seguro contra fórmula, sem payload/segredo/IDs internos opacos.
- [ ] `SCOPE-EX-06` Adicionar CTA `Exportar CSV` à Geral usando os filtros aplicados sem `pagina`, com estado/erro independente e ciclo de vida cancelável.
- [ ] `SCOPE-EX-07` Cobrir contrato, segurança, performance, concorrência, corrida frontend, browser e documentação antes de `Local-Implemented`.

## Out of Scope

- Snapshot/cursor que Smart Notas não oferece; exportação agregada; XLSX.
- Fila, worker, storage, arquivo temporário, link assíncrono, persistência/cache local de notas.
- Retry automático, novas variáveis ou alteração de credenciais/quota/deploy.
- DANFE/XML, emissão/cancelamento, Prisma/PostgreSQL e tela de processamento.
- Refatorar `backend/src/logs/**`; seu CSV legado terá item de hardening separado.
- Polimento global de marca/header/filtros/paginação, governado por `TODO-uninotas-fiscal-workspace-ux.md`.
- Worktrees, checkouts auxiliares e escritores paralelos de produto.

## Operational Envelope (Frozen)

| Bound | Value | Enforcement |
| --- | --- | --- |
| rows | `20,000` | após primeira página; `total` maior retorna 422 antes de buscar páginas seguintes |
| provider pages | `200` | após primeira página; `totalPages` maior retorna 422 |
| whole export deadline | `180s` | deadline absoluto monotônico; AbortController cobre espera/I/O e o serializer confere o deadline por chunks |
| CSV payload | `24 MiB` incluindo BOM | contador UTF-8 durante serialização; exceder retorna 422 sem response body CSV |
| exports per fiscal context | `1` ativo por instância | admission guard fail-fast; libera em success/error/abort |
| exports globally | `2` por instância | consequência de dois contextos e limite acima |
| upstream calls per export | `<= 200`, sequenciais | uma chamada ativa por export |
| shared provider-call budget | cada list/detail page e cada export page consome o mesmo budget configurado por contexto | contador/scheduler único; export nunca contorna `ratePerContextMinute` |
| export share of context budget | no máximo `floor(ratePerContextMinute * 0.75)` chamadas/minuto, mínimo 1 somente quando o budget total >=2 | reserva pelo menos 25% do budget configurado para chamadas interativas; export espera token até deadline |
| provider pacing | intervalo mínimo derivado de `ceil(60_000 / exportShare)` entre inícios de páginas do mesmo export | usa configuração efetiva e relógio injetável; sem retry |
| provider concurrency reserved for interactive paths | limite global de exports `min(2, maxConcurrency - 1)`; export indisponível quando `maxConcurrency < 2` | reserva efetivamente pelo menos um slot; com default 8, no máximo 2 exports e 6 slots permanecem |
| frontend active export | `1` por tela/sessão | ref síncrona + CTA disabled; duplicatas são descartadas |

Se o volume real não couber simultaneamente nesses limites, o usuário deve reduzir o filtro. Uma exportação assíncrona/persistida exige outro TODO e nova aprovação.

## Public HTTP Contract (Frozen Before Code)

### Request

`GET /api/v1/notas/exportar`

Query obrigatória:

- `contextoFiscal=unifast|prosperar`
- `dataInicio=YYYY-MM-DD`
- `dataFim=YYYY-MM-DD`

Query opcional:

- `status` na allowlist fiscal existente;
- `documento` com 11 ou 14 dígitos;
- `idCompra` trimmed, 1..100 caracteres.

`pagina` e qualquer campo desconhecido retornam `400 ConsultaDeNotasInvalida`. Listagem e exportação derivam do mesmo filtro base; paginação é camada exclusiva do DTO de listagem.

### Success / Empty

- `200` somente quando existe ao menos uma linha e o arquivo inteiro está pronto.
- `204` quando `total=0`; nenhum Blob/download; frontend informa “Nenhuma nota encontrada para exportar.”
- Headers do `200`:
  - `Content-Type: text/csv; charset=utf-8`
  - `Content-Disposition: attachment; filename="notas-{contextoFiscal}-{dataInicio}-{dataFim}.csv"`
  - `Cache-Control: private, no-store`
  - `Pragma: no-cache`
  - `X-Content-Type-Options: nosniff`
  - `Content-Length` do Buffer final
  - `X-Export-Row-Count` com a contagem validada
- O nome é ASCII por construção; o fallback frontend usa a mesma gramática.

### Failures

| Status | Code | Condition |
| --- | --- | --- |
| `400` | `ConsultaDeNotasInvalida` | filtro inválido, desconhecido ou `pagina` presente |
| `422` | `ExportacaoFiscalLimiteExcedido` | rows/pages/bytes excedem envelope; mensagem orienta reduzir filtros |
| `429` | `ExportacaoFiscalOcupada` | contexto/admission/budget sem capacidade dentro do contrato; `Retry-After: 5` |
| `502` | `ExportacaoFiscalPaginacaoInconsistente` | metadata, tamanho, contagem ou ID duplicado diverge |
| `504` | `ExportacaoFiscalPrazoExcedido` | deadline total de 180s |
| existing mapped status | existing provider code | credencial, contrato, indisponibilidade, quota externa ou timeout de uma página |

Abort por desconexão do cliente encerra o trabalho e não tenta responder. Não há retry.

## Pagination Consistency Contract

Após a primeira página válida, congelar `perPage`, `total`, `totalPages`. Se `total=0`, exigir `totalPages=0` e `items=[]`, retornar 204 e não aplicar regras de página final. Para `total>0`, exigir:

1. `returned.page === requestedPage`;
2. os quatro metadados permanecem idênticos;
3. `totalPages === Math.ceil(total / perPage)`;
4. página não-final contém exatamente `perPage` itens;
5. página final contém exatamente `total - perPage * (totalPages - 1)` itens;
6. soma final de itens é `total`;
7. cada `providerIdInterno` aparece uma única vez;
8. `total <= 20,000`, `totalPages <= 200`, deadline/bytes não excedidos.

Essas verificações detectam várias mutações da origem, mas não provam snapshot/ordem estável. O produto chama o resultado de “exportação do filtro”, nunca “snapshot”.

## CSV Contract (Frozen)

- UTF-8 com BOM; delimitador `;`; todas as células entre aspas; aspas internas duplicadas; linhas `CRLF`; uma linha final `CRLF`.
- Colunas/ordem: `contextoFiscal;numeroFiscal;status;produto;idCompra;chaveAcesso;ambiente;modelo;finalidade;plataforma;emissaoAgendada;dataPagamento;competencia;valorUnitario;valorTotal`.
- `null` vira string vazia.
- Datas normalizadas já existentes permanecem `YYYY-MM-DD`; `competencia` mantém a string ISO validada; decimais mantêm representação canônica com ponto e sem separador de milhar.
- `contextoFiscal` é o contexto do request; campos restantes vêm somente do record normalizado.
- `idCompra` e `chaveAcesso` são exportados completos porque todos os leitores já recebem os valores pelo contrato fiscal; a tela pode continuar mascarando-os. Não exportar `providerIdInterno`, `noteId`, destinatário, token, CNPJ configurado, payload cru ou campos fora da allowlist.
- Formula injection: se o primeiro caractere não-espaço do valor for `=`, `+`, `-` ou `@`, ou o primeiro caractere for TAB/CR/LF, prefixar um apóstrofo ASCII antes do valor original; depois aplicar quote/escape.
- O arquivo preserva zeros à esquerda e identificadores longos nos bytes. Autoformatação ao abrir diretamente em planilhas é comportamento do consumidor; não serão emitidas fórmulas para forçar tipo. Importação que exija fidelidade visual deve marcar essas colunas como texto.
- Testar explicitamente: zeros à esquerda, identificador numérico longo, decimal com ponto, null, aspas, ponto e vírgula, CR/LF, whitespace inicial e todos os prefixos de fórmula.

## Frontend Lifecycle Contract

- O clique captura os filtros **aplicados** atuais, exclui `pagina` e inicia um AbortController/generation owned por `ListaNotas` (ou hook local específico).
- Repetição enquanto ativo é `drop duplicate`, protegida sincronicamente por ref e visualmente pelo disabled.
- Mudança de contexto/status/datas/Documento/ID aplicado cancela a exportação anterior; mudança apenas de `pagina` não cancela.
- Unmount, navegação e logout abortam; `registrarLimpeza` integra a sessão.
- 401 limpa sessão pelo cliente existente e impede click tardio.
- `baixar` aceita `AbortSignal`, trata `204`, verifica signal/generation imediatamente antes de criar/clicar âncora e sempre revoga Object URL em success/failure/abort.
- A assinatura continua retrocompatível para `/eventos/exportar`; omitir options preserva download legado. Teste de regressão cobre filename/blob/âncora do CSV PostgreSQL.
- Erro/export state é independente de list/revalidation. CTA desabilita quando `state.data?.total === 0`, durante export ou sem dados válidos; não usa tamanho da página atual.

## Observability Contract

Um evento estruturado por exportação registra somente:

- `operation=export`, `context`, `actorId` interno autenticado e correlation ID único do export;
- outcome allowlisted: `success|empty|client_aborted|deadline_exceeded|busy|limit_exceeded|pagination_inconsistent|provider_error|serialization_error`;
- pages attempted/completed, rows serialized, output bytes e durationMs;
- flags `clientAborted`, `deadlineExceeded`, `rateLimited`.

Não registrar filtros, documento, ID da compra, número/chave fiscal, provider IDs, token/CNPJ, payload ou CSV. As chamadas do adapter podem manter logs por página, mas recebem/propagam o correlation ID do export para correlação, sem conteúdo sensível.

## Execution Lane Tracking (Required)

- **Local implementation branch:** `MonitorNotes:release/uninotas-smart-notas`
- **Foundation authority:** `uninotas-foundation:main`
- **Promotion lane:** `n/a — termina Local-Implemented; deploy fica no cutover`
- **Execution topology:** `principal checkout; single product-code writer`

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict`
- **Comparison mode:** `working_tree`
- **User validation:** `required on deviation`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `release/uninotas-smart-notas@a4b5a0eb6ae96291ffe5c6e16f297b64dcd62f29` | `working_tree`; mandatory rebaseline after UX closeout |
| `uninotas-foundation` | `foundation_documentation` | `main@feaf2e090927aa15087ee9ea4185886f749586e6` | `working_tree`; mandatory rebaseline after UX closeout |

### Expected Changed Paths

| Repository | Path glob | Change | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M, A` | filtro base, rota, scheduler/admission, erros, serializer e testes |
| `MonitorNotes` | `backend/src/common/filters/all-exceptions.filter.ts` | `M` | allowlist de novos códigos e Retry-After canônico |
| `MonitorNotes` | `backend/README.md` | `M` | contrato público/limites |
| `MonitorNotes` | `frontend/src/api/cliente.ts` | `M` | download cancelável/204 retrocompatível |
| `MonitorNotes` | `frontend/src/api/notas.ts` | `M` | filtros/export fiscal |
| `MonitorNotes` | `frontend/src/paginas/ListaNotas.tsx` | `M` | CTA e lifecycle |
| `MonitorNotes` | `frontend/src/estilos/*.css` | `M` | estado do CTA/erro se necessário |
| `MonitorNotes` | `frontend/e2e/notas-unit.ts` | `M` | contrato e regressão downloader legado |
| `MonitorNotes` | `frontend/e2e/notas-race.ts` | `M` | lifecycle/race |
| `MonitorNotes` | `frontend/e2e/notas.mjs` | `M` | browser/download |
| `MonitorNotes` | `frontend/README.md` | `M` | comportamento do download |
| `MonitorNotes` | `uninotas-foundation` | `M` | gitlink acompanha publicação Foundation governada |
| `MonitorNotes` | `artifacts/**` | `??` | estado preexistente do usuário; aceitar no diff, nunca stagear/alterar |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-filtered-csv-export.md` | `M, D` | evidência/closeout |
| `uninotas-foundation` | `todos/completed/features/TODO-uninotas-filtered-csv-export.md` | `A` | destino de closeout |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | contrato estável, antes do código como primeiro passo aprovado |
| `uninotas-foundation` | `artifacts/publication-manifest.txt` | `M` | publicação dos paths finais |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/src/logs/**` | `any` | sem mudar CSV/logs PostgreSQL |
| `MonitorNotes` | `backend/prisma/**` | `any` | sem banco |
| `MonitorNotes` | `frontend/src/componentes/Cabecalho.tsx` | `any` | pertence ao TODO UX e deverá estar no novo baseline |
| `MonitorNotes` | `Dockerfile` | `any` | runtime fora do escopo |
| `MonitorNotes` | `docker-compose.yml` | `any` | runtime fora do escopo |
| `MonitorNotes` | `.github/**` | `any` | pipeline fora do escopo |
| `MonitorNotes` | `backend/.env*` | `any` | sem nova configuração |
| `MonitorNotes` | `frontend/.env*` | `any` | sem nova configuração |
| `uninotas-foundation` | `project_constitution.md` | `any` | sem mudança estratégica |
| `uninotas-foundation` | `system_roadmap.md` | `any` | sem mudança estratégica |
| `uninotas-foundation` | `policies/**` | `any` | sem política nova |
| `uninotas-foundation` | `deterministic/**` | `any` | sem validator novo |

O serializer fica em `backend/src/fiscal-notes/`; não criar `common/csv.ts` enquanto o CSV legado de logs estiver fora do escopo. Abrir item separado para hardening do legado, sem bloquear esta feature.

## Definition of Done

- [ ] `DOD-EX-01` A rota aceita exatamente filtros fiscais sem `pagina`, um contexto e todos os leitores existentes.
- [ ] `DOD-EX-02` Um filtro vazio retorna 204 sem download; um filtro válido baixa todas as linhas atravessadas, não apenas a página atual.
- [ ] `DOD-EX-03` Rows/pages/deadline I/O+CPU/bytes/admission e budget/pacing derivados da configuração são aplicados e testados; nenhum limite trunca silenciosamente.
- [ ] `DOD-EX-04` Metadata/count/duplicidade são verificadas; erro intermediário/inconsistência/abort nunca produz arquivo parcial.
- [ ] `DOD-EX-05` CSV e headers seguem exatamente os contratos acima, inclusive injection/PII/identificadores/null/datas/decimais.
- [ ] `DOD-EX-06` CTA usa filtros aplicados, ignora página, evita duplicata e cancela por filtro/navegação/logout/unmount sem download tardio.
- [ ] `DOD-EX-07` List/detail continuam uma chamada upstream por request e mantêm resposta/contrato existentes.
- [ ] `DOD-EX-08` Carga concorrente em configuração mínima/default/saturada prova um export por contexto, limite global `min(2,maxConcurrency-1)`, budget comum, reserva interativa e recuperação de list/detail.
- [ ] `DOD-EX-09` Módulo fiscal e READMEs documentam contrato, limites e ausência de snapshot forte; nenhuma alegação de deploy.
- [ ] `DOD-EX-10` Local Verification, PCV, segurança, test-quality, arquitetura, final, triple review e guards passam.

## Decisions

- [x] `EX-D-01` Exportar todo o filtro aplicado, não a página; um único contexto; sem agregado.
- [x] `EX-D-02` Backend-owned sequential page walk; frontend faz uma requisição.
- [x] `EX-D-03` Buffer completo antes da resposta para garantir “arquivo inteiro ou erro”; limites tornam memória/duração finitas.
- [x] `EX-D-04` Sem snapshot forte; consistência detectável fail-closed e linguagem honesta.
- [x] `EX-D-05` Contrato HTTP, CSV, erros, observabilidade e lifecycle são os congelados neste TODO.
- [x] `EX-D-06` Serializer fiscal-local; nenhuma falsa abstração compartilhada com logs.
- [x] `EX-D-07` Exportação assíncrona/persistida fica fora; filtros acima do envelope precisam ser reduzidos.
- [x] `EX-D-08` Raw `idCompra`/`chaveAcesso` entram no arquivo para leitores autenticados; não logar esses valores.

## Assumptions Preview

| ID | Assumption | Concrete Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `EX-A-01` | primeira página informa total/perPage/totalPages antes do page walk | `backend/src/fiscal-notes/smart-notas.adapter.ts:247`; `backend/src/fiscal-notes/fiscal-notes.types.ts:24` | impossível rejeitar cedo | `High` | `Keep as Assumption` |
| `EX-A-02` | provider não oferece snapshot/cursor/order no contrato consumido | `backend/src/fiscal-notes/smart-notas.adapter.ts:28` | contrato poderia ficar mais forte | `High` | `Keep as Assumption` |
| `EX-A-03` | concorrência e rate são configuráveis e precisam governar list/detail/export em conjunto | `backend/src/config/configuration.ts:74`; `backend/src/fiscal-notes/smart-notas.adapter.ts:79`; `backend/src/fiscal-notes/fiscal-notes.service.ts:157` | reserva/pacing precisam de outro owner | `High` | `Keep as Assumption` |
| `EX-A-04` | os quatro leitores já recebem raw purchase/access keys pelo endpoint fiscal | `backend/src/fiscal-notes/fiscal-notes.controller.ts:10`; `backend/src/fiscal-notes/fiscal-notes.service.ts`; `frontend/src/api/notas.ts:18`; `frontend/src/paginas/ListaNotas.tsx:24` | export raw amplia autorização | `High` | `Keep as Assumption` |
| `EX-A-05` | downloader pode evoluir de forma retrocompatível com AbortSignal sem pacote | `frontend/src/api/cliente.ts:119`; `frontend/src/api/eventos.ts:63`; `frontend/src/auth/SessaoContexto.tsx:13` | lifecycle/legado precisa owner diferente | `High` | `Keep as Assumption` |

## Execution Plan

1. Como primeiro passo pós-aprovação, atualizar `modules/fiscal-notes-and-documents.md` com este contrato público congelado antes de editar código.
2. Criar testes backend fail-first para DTO/rota/erros, 0/1/200/201 páginas, 20k/20k+1, deadline I/O+CPU, bytes, budget/admission configuráveis, consistência, CSV e logs sanitizados.
3. Implementar filtro base + DTOs, erros/filtro global, coordinator/service com scheduler comum por contexto, serializer fiscal-local chunked e controller thin; não chamar recursivamente `FiscalNotesService.list()`.
4. Criar testes frontend/race/browser fail-first para filtros aplicados, 204, duplicate, filter change, navigation, logout, 401, abort, URL lifecycle e late response.
5. Implementar cliente/download cancelável e CTA com owner único de generation/AbortController.
6. Executar suites amplas, carga concorrente com list/detail, security review e browser preview fresco.
7. Executar auditorias/gates, consolidar docs/evidência e parar em `Local-Implemented`.

## Test Strategy

- **Backend test-first:** port/fetch, relógio e pacing injetáveis; nenhum acesso real no suite determinístico.
- **Deadline CPU:** serializer confere relógio monotônico em cada chunk (máximo 500 linhas), faz yield cooperativo entre chunks e aborta antes de produzir Buffer se o prazo venceu.
- **Frontend test-first:** extrair somente um pequeno coordinator/hook se necessário para testar ownership; não duplicar filtro.
- **Browser:** APIs interceptadas provam UX/download; não é prova cross-stack.
- **Cross-stack:** specs NestJS provam HTTP/CSV; smoke real fica no cutover.

## Validation Steps

- [ ] `VAL-EX-01` `cd backend && npm test -- --runInBand`
- [ ] `VAL-EX-02` `cd backend && npm run build && npx eslint "{src,test}/**/*.ts" --max-warnings=0` (não usar `npm run lint`, pois contém `--fix`).
- [ ] `VAL-EX-03` `cd frontend && npm run test:notas && npm run lint && npm run build`
- [ ] `VAL-EX-04` Para `export-duplicate`, `export-cancel-filter`, `export-cancel-session`, executar `DELPHI_RACE_SCENARIO=<scenario> DELPHI_RACE_BURST_LEVEL=<5|10|20> npm run test:notas:race`.
- [ ] `VAL-EX-05` Build fresco; iniciar preview, comprovar SHA/bundle servido, executar `ALVO=<preview> CHROME=<local> npm run e2e:notas` com APIs interceptadas/download capturado; encerrar preview.
- [ ] `VAL-EX-06` Perfil de runtime: exports simultâneos Unifast/Prosperar + tentativas extras + rajadas list/detail; comprovar caps, fail-fast e recuperação.
- [ ] `VAL-EX-07` Capability audits NestJS/React/Vite, endpoint scrutiny, race, load, security, test-quality, arquitetura, final, triple review e verification-debt.
- [ ] `VAL-EX-08` Foundation validators/guards e `git diff --check`.

## Local Verification Matrix

| Surface | Evidence | Status |
| --- | --- | --- |
| NestJS contract/unit | full Jest family, build, non-mutating ESLint | `planned` |
| React client/UI | unit, exact race scenarios, lint/build | `planned` |
| Browser | fresh preview, intercepted UX/download only | `planned` |
| Performance/concurrency | deterministic 200-page/20k/24MiB bounds and concurrent export+interactive profile | `planned` |
| Security | adversarial CSV/query/auth/log review | `planned` |
| Foundation | module + TODO validators/guards | `planned` |

Não há pipeline versionada no repositório; estas evidências são `Local Verification`, não alegação de CI-Equivalent.

## Plan Review Gate

### Incorporated Independent Findings

| ID | Severity | Finding | Resolution |
| --- | --- | --- | --- |
| `REV-01` | `high` | cap de linhas não limitava páginas/duração/quota/memória | envelope completo e RLS obrigatório |
| `REV-02` | `high` | sem snapshot, “completo” absoluto era indemonstrável | semântica de travessia bounded + consistência detectável + linguagem sem snapshot |
| `REV-03` | `high` | contrato HTTP/CSV incompleto | request/success/empty/errors/headers/serialization congelados |
| `REV-04` | `high` | baseline SHA inexistente | novo baseline exato será commitado/publicado antes dos novos reviews |
| `REV-05` | `medium` | fidelidade de planilha/injection insuficiente | bytes/format/injection/consumer tradeoff e fixtures explícitos |
| `REV-06` | `medium` | lifecycle frontend sem owner | generation/AbortController/ref/logout/filter policy congelados |
| `REV-07` | `medium` | observabilidade por export ausente | evento sanitizado e correlação congelados |
| `REV-08` | `medium` | filtro duplicado/helper comum conflituoso | filtro base compartilhado dentro do módulo; serializer fiscal-local |
| `REV-09` | `high` | suíte declarada não era executável/mutava lint | comandos exatos, lint não mutante, Local Verification e preview lifecycle |
| `R2-H1/EX-H01` | `high` | pacing/admission ignorava budget/config efetivos | scheduler comum, share <=75%, pacing derivado e reserva `maxConcurrency-1` |
| `R2-H2` | `high` | códigos/Retry-After exigem filtro global fora do diff | `all-exceptions.filter.ts` incluído como fonte única |
| `R2-H4/EX-M03` | `high` | export bulk não atribuía ator | `actorId` interno obrigatório no evento sanitizado |
| `R2-M1` | `medium` | regra da página final contradizia vazio | branch normativa `total=0` separada |
| `R2-M2` | `medium` | timer não interrompe CPU síncrona | deadline monotônico por chunk + yield cooperativo |
| `EX-M01` | `medium` | downloader também serve CSV PostgreSQL | assinatura retrocompatível e teste do legado |

### Residual Risks

- Quota/latência real pode impedir filtros grandes mesmo abaixo dos limites; falha explícita e cutover smoke são obrigatórios.
- Mudança de origem pode escapar das verificações sem cursor/snapshot; risco documentado e não vendido como snapshot.
- Buffer do backend + Buffer HTTP + Blob do browser ampliam memória; 24 MiB e RLS limitam e medem, sem afirmar SLO de produção.
- Admissão é por instância; stage atualmente usa uma réplica. Escalar réplicas requer reavaliar coordenação distribuída no cutover.

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review status:** `findings_integrated_pending_rerun`
- **Architecture adherence review:** `required after implementation`
- **Adherence status:** `not_run`
- **No-go handling:** `retornar ao plano; não aprovar/concluir com finding material aberto`.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Baseline branch:** `uninotas-foundation/main`
- **Baseline commit:** `pending material R3 commit`
- **Baseline push reference:** `pending`
- **Gate status:** `not_run`
- **Findings summary:** R2 gerou mudanças materiais integradas; novo freeze será publicado antes de R3.
- **Evidence / reference:** `pending R3 material commit`.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-filtered-csv-export.md`
- **Gate status:** `not_run`

## Audit Trigger Matrix

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `big` | public endpoint + bounded bulk + browser lifecycle |
| `blast_radius` | `cross-stack` | NestJS/React |
| `behavioral_change_or_bugfix` | `yes` | novo download |
| `changes_public_contract` | `yes` | GET exportar |
| `touches_auth_or_tenant` | `yes` | novo endpoint autenticado reutiliza e testa quatro perfis leitores |
| `touches_runtime_or_infra` | `no` | sem config/topologia |
| `touches_tests` | `yes` | broad |
| `critical_user_journey` | `yes` | fiscal export |
| `release_or_promotion_critical` | `yes` | entrega solicitada |
| `high_severity_plan_review_issue` | `yes` | integrado; requer rerun |
| `explicit_three_lane_request` | `no` | protocolo ainda obrigatório por escalonamento |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Critique status:** `not_run`
- **Isolation:** `fresh internal no-context reviewer; cannot implement`
- **Lenses:** `correctness|performance|security|elegance|structure|operational fit`.

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Guard scope:** `EX-A-01,EX-A-02,EX-A-03,EX-A-04,EX-A-05`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-filtered-csv-export.md`
- **Gate status:** `not_run`

## Approval

- **Approved by:** `pending explicit APROVADO`
- **Approval scope:** `SCOPE-EX-01..07` e contratos frozen deste TODO.
- **Not authorized:** `deploy/merge/snapshot claim/async export/runtime config/logs/worktrees`.
- **Renewed approval required:** volume, formato, colunas, raw identifiers, rota, auth, context, runtime ou diff boundary muda materialmente.

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Subagent / delegation authorization:** `pending APROVADO; workflow-required serialized executor`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree authorization:** `not-authorized`
- **Guard outcome:** `go`
- **Guard evidence:** `agent_role_routing_guard.py` para codex/implementation/routine-executor/gpt-5.6-terra/medium/declared; não concede autoridade antes do APROVADO.

## Security Risk Assessment

- **Risk:** `high`.
- **Attack surface:** authenticated bulk GET, query validation, provider amplification, CSV injection, raw fiscal identifiers, logs/download.
- **Attack simulation:** `required`.
- **Minimum:** unauthorized/role readers, unknown query/pagina, formula/whitespace/newline/quote, over-limit, saturation, abort, log redaction, no-store/nosniff.

## Frontend / Consumer Matrix

| Producer Surface In This TODO | Consumer | Delivery State | Evidence / Waiver |
| --- | --- | --- | --- |
| `GET /api/v1/notas/exportar` 200 CSV | React `ListaNotas` / browser download | `planned` | NestJS contract + intercepted browser download; filters applied without page |
| `GET /api/v1/notas/exportar` 204 | React export status | `planned` | no Blob/anchor; explicit empty message |
| export error catalog / `Retry-After` | shared HTTP client + `ListaNotas` error region | `planned` | filter contract tests + independent UI error state |
| extended `baixar(caminho,nome,options?)` | fiscal export and existing `/eventos/exportar` | `planned backward-compatible` | fiscal abort/204 tests plus legacy PostgreSQL CSV regression |
| fiscal module contract | backend/frontend READMEs and Foundation module | `planned` | exact route/headers/limits/no-snapshot language |

## Rules Acknowledgement / Ingestion

| Source | Why It Applies | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | tactical TODO | approval/diff/evidence | preapproval code | lifecycle governado |
| `delphi-ai/skills/rule-nestjs-nestjs-architecture-always-on/SKILL.md` | endpoint NestJS | controller thin, runtime validation | business logic no controller | service/coordinator owner |
| `delphi-ai/skills/wf-nestjs-change-application-boundary-method/SKILL.md` | public GET | DTO/auth/errors/bounds | work implícito/unbounded | contract tests |
| `delphi-ai/skills/rule-react-react-architecture-always-on/SKILL.md` | CTA/lifecycle | owner único, abort, pure render | stale effect/download | race/browser |
| `delphi-ai/skills/wf-react-change-ui-boundary-method/SKILL.md` | UI boundary | estados/ações explícitos | coupling oculto | coordinator local |
| `delphi-ai/skills/rule-vite-vite-build-runtime-always-on/SKILL.md` | browser bundle | same-origin/build fresco | env guess | build/preview proof |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | novos testes | fail-first/assertion efficacy | bypass/mock fallback | broad suites |
| `delphi-ai/skills/endpoint-performance-scrutiny/SKILL.md` | page walk externo | bounds/call budget | amplification | EPS obrigatório |
| `delphi-ai/skills/frontend-race-condition-validation/SKILL.md` | download async | cancel/drop/stale policy | late download | FRC obrigatório |
| `delphi-ai/skills/runtime-load-stress-validation/SKILL.md` | bulk/memória | profiles/thresholds/recovery | SLO sem prova | RLS obrigatório |
| `delphi-ai/skills/security-adversarial-review/SKILL.md` | CSV/raw IDs | injection/redaction/auth | conteúdo em logs | security gate |
| `delphi-ai/skills/ci-equivalent-governance/SKILL.md` | verificação | linguagem honesta | CI claim sem pipeline | Local Verification |

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `high`
- **Why this level:** bulk externo bounded, budget compartilhado, Buffer/Blob e CTA assíncrono.
- **Current delivery stage at review time:** `Pending, Provisional, review`

| Policy Schema Version | Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Trigger Rationale | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code | Recorded At UTC | Executor ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `pcv-1` | `EPS` | `endpoint-performance-scrutiny` | `required` | `high` | `EPS-DATA-PATH-CHANGED` | até 200 calls externos, serializer e shared budget | `before_local_implemented` | `EPS-E2` | `pending` | quota/latência real | `U-QUERY-PATH-UNKNOWN` | `2026-09-28T18:00:00Z` | `pending-routine-executor` |
| `pcv-1` | `FRC` | `frontend-race-condition-validation` | `required` | `high` | `FRC-STALE-RESPONSE` | abort/generation/download pode sobreviver a filtro/sessão | `before_local_implemented` | `FRC-E3` | `pending` | browser scheduling | `U-ASYNC-SURFACE-UNKNOWN` | `2026-09-28T18:00:00Z` | `pending-routine-executor` |
| `pcv-1` | `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `BCI-NO-WRITE-SIDE-EFFECT` | GET read-only sem mutation/idempotency | `before_local_implemented` | `BCI-INV` | `not_applicable` | none | `none` | `2026-09-28T18:00:00Z` | `pending-routine-executor` |
| `pcv-1` | `RLS` | `runtime-load-stress-validation` | `required` | `high` | `RLS-BATCH-OR-BULK-PATH-CHANGED` | paginação, memória, budget e concorrência afetam runtime | `before_local_implemented` | `RLS-E2` | `pending` | quota real e memória browser | `U-RUNTIME-PRESSURE-UNKNOWN` | `2026-09-28T18:00:00Z` | `pending-routine-executor` |

### EPS planned evidence

- Classificar `bounded-list + external-page-walk + in-memory-serialization`; registrar calls/pages/rows/bytes/duration e provar query/filter sem page.
- Artifact planejado: `foundation_documentation/artifacts/tmp/uninotas-export-pcv/eps-pcv1.json`, schema `pcv-1`, SHA-256 canônico.

### FRC planned evidence

- Políticas: `drop duplicate`; `cancel previous` em mudança de filtro; paginação não cancela; logout/unmount/401 abortam; generation suprime estado/download tardio.
- Bursts `5/10/20` para `export-duplicate`, `export-cancel-filter`, `export-cancel-session`.
- Artifact planejado: `foundation_documentation/artifacts/tmp/uninotas-export-pcv/frc-pcv1.json`.

### BCI invariant

- O endpoint não escreve nem possui side effect durável; admission/budget é controle efêmero e será coberto por EPS/RLS, não idempotência de mutation.

### RLS planned evidence

- **Profile RLS-P1 default:** fake config `maxConcurrency=8`, context rate `120/min`; dois exports (um/contexto) + list/detail controlados; 200 pages/20k rows/24MiB; extra export por contexto deve falhar 429.
- **Profile RLS-P2 constrained/saturated:** fake config `maxConcurrency=2`, context rate `4/min`; somente um export global, um slot interativo reservado; budgets e abort/recovery sob fake clock.
- **Thresholds:** export calls nunca ultrapassam `floor(rate*0.75)`/min/context; total calls nunca ultrapassa rate; export concurrency <= `min(2,maxConcurrency-1)`; admitted list/detail error rate `0%`; p95 list/detail <= `2x` baseline do mesmo stub; extra exports `100%` no erro esperado; output <=24MiB; peak heap delta <=96MiB no P1; cleanup/recovery <=1s após abort com fake port; zero late calls após deadline.
- Capturar p50/p95/p99, throughput, statuses, calls por classe/contexto, active/peak, RSS/heap, bytes, abort/recovery.
- Artifact planejado: `foundation_documentation/artifacts/tmp/uninotas-export-pcv/rls-pcv1.json`.

### Common `pcv-1` artifact rule

- Cada lane em `running|passed` registra evidence object machine-checkable, checkout SHA, profile, config, workload, thresholds, metrics, pass/fail e `artifact_sha256` calculado sobre JSON UTF-8 com chaves recursivamente ordenadas, arrays preservados e sem whitespace, excluindo o próprio hash.

## Required Delivery Gates

- `endpoint-performance-scrutiny`: `required`
- `frontend-race-condition-validation`: `required`
- `runtime-load-stress-validation`: `required`
- `security-adversarial-review`: `required`
- `test-quality-audit`: `required`
- `architecture-adherence`: `required`
- `independent-final-review`: `required`
- `audit-protocol-triple-review`: `required as a separate additive gate before Completed`
- `verification-debt-audit`: `required`
- `cutover-integrity-audit`: `not_needed; no deploy`

## Promotion Finding Routing Ledger

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `REV-01..09` | `high, medium` | `plan-correction` | `same TODO` | contrato original de exportação | `integrated_pending_rerun` | R3 architecture/critique |
| `R2-H1..H5,R2-M1..M2` | `high, medium` | `plan-correction` | `same TODO` | budget, audit, guards e gates pertencem ao endpoint | `integrated_pending_rerun` | R3 architecture/critique |
| `EX-M01..M03` | `medium` | `plan-correction` | `same TODO` | compatibilidade downloader/auth/audit dentro da feature | `integrated_pending_rerun` | R3 architecture/critique |
| `logs-csv-hardening` | `medium` | `security-follow-up` | `split` | serializer legado em `backend/src/logs/**` está fora deste diff | `deferred` | abrir TODO separado sem bloquear export fiscal |

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Reason:** aguardando baseline, fresh reviews e aprovação.
- **Target after implementation:** `Local-Implemented`, sem deploy.
