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
| whole export deadline | `180s` | AbortController filho do request, cobrindo espera, chamadas e serialização |
| CSV payload | `24 MiB` incluindo BOM | contador UTF-8 durante serialização; exceder retorna 422 sem response body CSV |
| exports per fiscal context | `1` ativo por instância | admission guard fail-fast; libera em success/error/abort |
| exports globally | `2` por instância | consequência de dois contextos e limite acima |
| upstream calls per export | `<= 200`, sequenciais | uma chamada ativa por export |
| provider pacing | início de páginas do mesmo export separado por pelo menos `600ms` | relógio injetável/testável; sem retry |
| provider concurrency reserved for interactive paths | export usa no máximo `2` dos `8` slots atuais | list/detail preservam capacidade mínima teórica de `6` slots quando apenas exports ocupam o adapter |
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
| `429` | `ExportacaoFiscalOcupada` | já há export ativo no contexto; `Retry-After: 5` |
| `502` | `ExportacaoFiscalPaginacaoInconsistente` | metadata, tamanho, contagem ou ID duplicado diverge |
| `504` | `ExportacaoFiscalPrazoExcedido` | deadline total de 180s |
| existing mapped status | existing provider code | credencial, contrato, indisponibilidade, quota externa ou timeout de uma página |

Abort por desconexão do cliente encerra o trabalho e não tenta responder. Não há retry.

## Pagination Consistency Contract

Após a primeira página válida, congelar `perPage`, `total`, `totalPages` e exigir:

1. `returned.page === requestedPage`;
2. os quatro metadados permanecem idênticos;
3. `totalPages === (total === 0 ? 0 : Math.ceil(total / perPage))`;
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
- Erro/export state é independente de list/revalidation. CTA desabilita quando `state.data?.total === 0`, durante export ou sem dados válidos; não usa tamanho da página atual.

## Observability Contract

Um evento estruturado por exportação registra somente:

- `operation=export`, `context`, correlation ID único do export;
- outcome allowlisted;
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

### Repository Baselines

| Repository | Baseline ref | Notes |
| --- | --- | --- |
| `MonitorNotes` | `release/uninotas-smart-notas@a4b5a0eb6ae96291ffe5c6e16f297b64dcd62f29` | preservar `artifacts/**` e gitlink preexistentes |
| `uninotas-foundation` | `main@9cffb901c063ad581d3519f5009814f38f7ec5db` | autoridade antes do split |

### Expected Changed Paths

| Repository | Path glob | Change | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M|A` | filtro base, rota, orquestração, erros, serializer e testes |
| `MonitorNotes` | `backend/README.md` | `M` | contrato público/limites |
| `MonitorNotes` | `frontend/src/api/cliente.ts`, `frontend/src/api/notas.ts` | `M` | download cancelável/204/filtros |
| `MonitorNotes` | `frontend/src/paginas/ListaNotas.tsx` | `M` | CTA e lifecycle |
| `MonitorNotes` | `frontend/src/estilos/*.css` | `M` | estado do CTA/erro se necessário |
| `MonitorNotes` | `frontend/e2e/notas-unit.ts`, `frontend/e2e/notas-race.ts`, `frontend/e2e/notas.mjs` | `M` | contrato/race/browser |
| `MonitorNotes` | `frontend/README.md` | `M` | comportamento do download |
| `uninotas-foundation` | este TODO e destino completed | `M|D|A` | evidência/closeout |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | contrato estável, antes do código como primeiro passo aprovado |

### Not Expected Changed Paths

| Repository | Path glob | Reason |
| --- | --- | --- |
| `MonitorNotes` | `backend/src/logs/**`, `backend/prisma/**` | sem logs/banco |
| `MonitorNotes` | `frontend/src/componentes/Cabecalho.tsx` | pertence ao TODO UX |
| `MonitorNotes` | `Dockerfile`, `docker-compose.yml`, `.github/**`, `*.env*` | sem runtime/config/pipeline |
| `MonitorNotes` | `artifacts/**` | estado preexistente do usuário |
| `uninotas-foundation` | `project_constitution.md`, `system_roadmap.md`, `policies/**`, `deterministic/**` | sem mudança estratégica/validator |

O serializer fica em `backend/src/fiscal-notes/`; não criar `common/csv.ts` enquanto o CSV legado de logs estiver fora do escopo. Abrir item separado para hardening do legado, sem bloquear esta feature.

## Definition of Done

- [ ] `DOD-EX-01` A rota aceita exatamente filtros fiscais sem `pagina`, um contexto e todos os leitores existentes.
- [ ] `DOD-EX-02` Um filtro vazio retorna 204 sem download; um filtro válido baixa todas as linhas atravessadas, não apenas a página atual.
- [ ] `DOD-EX-03` Rows/pages/deadline/bytes/admission/pacing são aplicados e testados; nenhum limite trunca silenciosamente.
- [ ] `DOD-EX-04` Metadata/count/duplicidade são verificadas; erro intermediário/inconsistência/abort nunca produz arquivo parcial.
- [ ] `DOD-EX-05` CSV e headers seguem exatamente os contratos acima, inclusive injection/PII/identificadores/null/datas/decimais.
- [ ] `DOD-EX-06` CTA usa filtros aplicados, ignora página, evita duplicata e cancela por filtro/navegação/logout/unmount sem download tardio.
- [ ] `DOD-EX-07` List/detail continuam uma chamada upstream por request e mantêm resposta/contrato existentes.
- [ ] `DOD-EX-08` Carga concorrente prova no máximo um export por contexto, no máximo duas chamadas export ativas e recuperação de list/detail.
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

| ID | Assumption | Concrete Evidence | If False | Handling |
| --- | --- | --- | --- | --- |
| `EX-A-01` | primeira página informa total/perPage/totalPages antes do page walk | `backend/src/fiscal-notes/smart-notas.adapter.ts:247-261`; `backend/src/fiscal-notes/fiscal-notes.types.ts:24-30` | impossível rejeitar cedo | bloquear e redesenhar |
| `EX-A-02` | provider não oferece snapshot/cursor/order no contrato consumido | `backend/src/fiscal-notes/smart-notas.adapter.ts:28-50` | contrato poderia ficar mais forte | renovar decisão com evidência |
| `EX-A-03` | adapter global tem 8 slots na configuração atual e falha ao saturar | `backend/src/fiscal-notes/smart-notas.adapter.ts:79-90`; runtime evidenciado no TODO backend concluído | reserva teórica muda | reclassificar carga |
| `EX-A-04` | todos os leitores já recebem raw purchase/access keys no DTO | `backend/src/fiscal-notes/fiscal-notes.service.ts`; `frontend/src/api/notas.ts:18-38`; UI mascara em `frontend/src/paginas/ListaNotas.tsx:24` | export raw amplia autorização | bloquear e revisar auth |
| `EX-A-05` | downloader atual pode evoluir com AbortSignal sem novo pacote | `frontend/src/api/cliente.ts:119-155`; `frontend/src/auth/SessaoContexto.tsx:13-44` | lifecycle precisa owner diferente | manter local, renovar se cruzar sessão |

## Execution Plan

1. Como primeiro passo pós-aprovação, atualizar `modules/fiscal-notes-and-documents.md` com este contrato público congelado antes de editar código.
2. Criar testes backend fail-first para DTO/rota/erros, 0/1/200/201 páginas, 20k/20k+1, deadline, bytes, admission, consistência, CSV e logs sanitizados.
3. Implementar filtro base + DTOs, erros, coordinator/service, serializer fiscal-local e controller thin; não chamar recursivamente `FiscalNotesService.list()`.
4. Criar testes frontend/race/browser fail-first para filtros aplicados, 204, duplicate, filter change, navigation, logout, 401, abort, URL lifecycle e late response.
5. Implementar cliente/download cancelável e CTA com owner único de generation/AbortController.
6. Executar suites amplas, carga concorrente com list/detail, security review e browser preview fresco.
7. Executar auditorias/gates, consolidar docs/evidência e parar em `Local-Implemented`.

## Test Strategy

- **Backend test-first:** port/fetch, relógio e pacing injetáveis; nenhum acesso real no suite determinístico.
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

### Residual Risks

- Quota/latência real pode impedir filtros grandes mesmo abaixo dos limites; falha explícita e cutover smoke são obrigatórios.
- Mudança de origem pode escapar das verificações sem cursor/snapshot; risco documentado e não vendido como snapshot.
- Buffer do backend + Buffer HTTP + Blob do browser ampliam memória; 24 MiB e RLS limitam e medem, sem afirmar SLO de produção.
- Admissão é por instância; stage atualmente usa uma réplica. Escalar réplicas requer reavaliar coordenação distribuída no cutover.

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review status:** `not_run after split/integration`
- **Architecture adherence review:** `required after implementation`
- **Adherence status:** `not_run`
- **No-go handling:** `retornar ao plano; não aprovar/concluir com finding material aberto`.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Baseline branch:** `uninotas-foundation/main`
- **Baseline commit:** `pending material split commit`
- **Baseline push reference:** `pending`
- **Gate status:** `not_run`

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
| `touches_auth_or_tenant` | `no` | leitores existentes, um contexto |
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
- **Governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `high`
- **Subagent authorization:** `pending APROVADO; workflow-required serialized executor`
- **Execution topology:** `primary-checkout-single-writer`
- **Guard outcome:** `pending`

## Security Risk Assessment

- **Risk:** `high`.
- **Attack surface:** authenticated bulk GET, query validation, provider amplification, CSV injection, raw fiscal identifiers, logs/download.
- **Attack simulation:** `required`.
- **Minimum:** unauthorized/role readers, unknown query/pagina, formula/whitespace/newline/quote, over-limit, saturation, abort, log redaction, no-store/nosniff.

## Performance & Concurrency Risk Assessment

- **Global sensitivity:** `high`.

| Lane | Decision | Reason | Minimum Evidence | State |
| --- | --- | --- | --- | --- |
| `EPS` | `required` | external multi-page data path | `EPS-E2` bounds/query/call profile | `pending` |
| `FRC` | `required` | async lifecycle/stale response | `FRC-E3`; `FRC-LIFECYCLE-ASYNC-EFFECT`, `FRC-STALE-RESPONSE` | `pending` |
| `BCI` | `not_needed` | read-only GET, no server mutation | invariant record | `n/a` |
| `RLS` | `required` | bulk/concurrent provider work and memory | `RLS-E2` 200-page/20k/bytes + export/list/detail concurrency/recovery | `pending` |

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

| Finding ID | Source | Severity | Required Action | Status |
| --- | --- | --- | --- | --- |
| `REV-01..09` | architecture + critique round before split | `high|medium` | incorporated contract; rerun fresh reviews | `integrated_pending_rerun` |

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Reason:** aguardando baseline, fresh reviews e aprovação.
- **Target after implementation:** `Local-Implemented`, sem deploy.
