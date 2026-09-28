# TODO — Exportar todas as notas do filtro fiscal ativo

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** `Approved`
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
- **Next exact step:** iniciar o executor serial de `ST-EXPORT` no checkout principal sobre os baselines revalidados abaixo.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `implementation`
- **Why this state now:** `ST-UX` foi fechado, o usuário aprovou o pacote serial e o rebaseline pós-UX preserva integralmente o contrato material revisado.
- **Exit condition:** implementação, evidência e gates obrigatórios concluem em `Local-Implemented`, ou bloqueio formal.

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
| server-side generation deadline | `180s` | deadline-derived AbortSignal cancela waits/I/O em andamento; do precheck ao check final antes do Buffer; expira quando `monotonicNow >= deadline`; não inclui transmissão HTTP |
| CSV payload | `24 MiB` incluindo BOM | contador UTF-8 durante serialização; exceder retorna 422 sem response body CSV |
| exports per fiscal context | `1` ativo por instância | admission guard fail-fast; libera em success/error/abort |
| exports globally | `min(2, maxConcurrency - 1)` por instância, com máximo absoluto `2` | com default `8`, são `2`; com `maxConcurrency=2`, é `1`; abaixo disso a exportação fica indisponível |
| export per actor | `1` ativo globalmente por instância e no máximo `1` início por rolling minute | start consome uma unidade de `ratePerUserMinute`; pages não duplicam user charge; cooldown impede reacquisition imediata |
| upstream calls per export | `<= 200`, sequenciais | uma chamada ativa por export |
| shared provider-call budget | cada list/detail request e cada export page consome o mesmo budget configurado por contexto | coordinator único; export nunca contorna `ratePerContextMinute` |
| export share of context budget | `ratePerContextMinute < 2 ? 0 : floor(ratePerContextMinute * 0.75)` chamadas/minuto | fórmula única; reserva pelo menos 25% para chamadas interativas; export espera token até deadline |
| provider pacing | `nextAllowedMono[context]` persistente impõe `ceil(60_000 / exportShare)` entre inícios de quaisquer export pages do mesmo contexto, inclusive entre exports sucessivos | dois contexts independentes; não reseta no exit; relógio injetável; sem retry |
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

- `200` somente quando existe ao menos uma linha e o Buffer inteiro passou pelo check final de signal/deadline.
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
| `429` | `ExportacaoFiscalOcupada` | configuração incapaz, contexto/global/actor admission ou rolling cooldown; `Retry-After` segue a precedência abaixo |
| `429` | `LimiteDeConsultaExcedido` | `ratePerUserMinute` esgotado ou actor identity capacity (`MAX_ACTOR_BUCKETS`) cheia para novo ator; `Retry-After` segue janela ou projected identity release |
| `502` | `ExportacaoFiscalPaginacaoInconsistente` | metadata, tamanho, contagem ou ID duplicado diverge |
| `504` | `ExportacaoFiscalPrazoExcedido` | deadline de geração server-side de 180s |
| existing mapped status | existing provider code | credencial, contrato, indisponibilidade, quota externa ou timeout de uma página |

Signal já abortado antes do precheck não admite nem cobra nada. No start, um timer/clock port injetável arma um deadline controller com o tempo monotônico restante; o signal efetivo é a composição de client disconnect + deadline. Toda espera e provider I/O recebe esse signal e usa `remainingMs`; o timeout efetivo da page é `min(providerTimeoutMs, remainingMs)`. Se deadline dispara, o coordinator distingue sua flag do client abort, aborta imediatamente a page/wait, mapeia 504, libera leases e impede novas chamadas. Client abort não tenta responder. Checks antes/depois de cada espera, I/O e yield/chunk e imediatamente antes de devolver o Buffer permanecem defesa adicional. Em `monotonicNow === deadline`, falha 504. Se a conexão encerrar depois do Buffer pronto mas antes do início da resposta, o Buffer é descartado e leases são liberados; depois que a transmissão HTTP começa, falhas de rede/proxy podem truncar o transporte e não são vendidas como atomicidade no fio. O frontend somente cria/clica o download após `fetch` e `blob()` terminarem e a generation continuar válida. Não há retry.

### Atomic Admission and `Retry-After`

Antes da primeira chamada provider, uma seção crítica síncrona por instância amostra `wallNow` e `monotonicNow` exatamente uma vez e avalia, sem mutação, configuração mínima, actor ativo/cooldown, contexto ativo, limite global, user fixed-window budget e capacidade de identidade de ator. Para ator novo, a capacidade conta a união de actor buckets da janela efetiva, cooldowns não expirados e actor leases ativos; o limite continua `MAX_ACTOR_BUCKETS=5.000`. A visão projetada ignora buckets stale e cooldowns expirados, mas não os remove. Se qualquer condição rejeitar, o estado bruto inteiro permanece byte-for-byte equivalente.

Somente quando todas passam, a mesma seção crítica faz um único commit atômico do start de export: remove estado expirado; avança o high-water da janela; consome exatamente uma unidade do user budget; grava o início do rolling cooldown de 60s; e adquire leases de actor/context/global. A primeira operação aceita de uma janela executa o cleanup uma vez; rejeições nunca o executam. O cooldown conta do start aceito e permanece consumido mesmo se a chamada posterior falhar, pois o trabalho foi admitido. Leases ativos são liberados em success/error/abort. Cada provider page consome depois o scheduler/budget de contexto; falta temporária de token do contexto não é bloqueio pré-admissão: exatamente um contender elegível é admitido, espera até o deadline e termina em 504 se não houver tempo, sem segunda cobrança de usuário. `exportShare=0` continua configuração incapaz e aceita zero.

Relógios têm papéis separados. Para cada decisão, `rawWindow=floor(wallNow/60_000)` e `effectiveWindow=max(lastCommittedWindow, rawWindow)`; o high-water só muda numa operação de budget aceita, seja list, detail, export start ou export page, logo regressão do wall clock nunca reabre budget já consumido. `monotonicNow` governa cooldown, pacing e deadline e nunca retrocede. Cooldown expira quando `monotonicNow >= acceptedStart + 60_000`. Todo `Retry-After` usa `max(1, ceil(remainingMs/1000))`; para budget/capacidade fixa, `remainingMs=(effectiveWindow+1)*60_000-wallNow`, que pode exceder 60s sob regressão e permanece fail-closed.

Mapeamento determinístico quando uma tentativa é rejeitada:

1. configuração incapaz de exportar (`maxConcurrency < 2` ou export share zero): `ExportacaoFiscalOcupada`, `Retry-After: 60`;
2. se qualquer bloqueio export-specific coexistir (actor ativo, actor cooldown, contexto ativo ou global cheio): `ExportacaoFiscalOcupada`, com `Retry-After = max(5 para lease ocupado, cooldown restante, user-window restante e actor-capacity retry quando coexistirem)`;
3. se o único bloqueio for user fixed-window ou capacidade sem slot para novo ator: `LimiteDeConsultaExcedido`; user budget usa a fronteira efetiva, e capacity usa o primeiro identity-release estimado abaixo;
4. token temporário do context budget após admissão espera; deadline produz `ExportacaoFiscalPrazoExcedido` 504.

Buckets de ator pertencem à janela efetiva em que foram aceitos. O precheck usa projeção read-only; somente commit aceito remove buckets stale e cooldowns expirados. Ator já presente na união bucket/cooldown/lease não precisa de slot. Para cada identidade ocupante, `releaseEstimateMs=max(fixedWindowRemaining se bucket atual, cooldownRemaining se ativo, 5_000 se lease ativo)`; `actorCapacityRetryMs=min(releaseEstimateMs dos ocupantes)`. O header aplica `max(1,ceil(ms/1000))`; é advisory para lease, cujo tempo real é desconhecido. Testes observam estado bruto e cobrem rejeição sem mutação, cleanup no primeiro aceito, salto/regressão, cap + wall jump com monotonic congelado, fronteiras, expiry e releases. Cooldown aceito permanece após success/error/abort; leases sempre são liberados.

### Shared Rate Coordinator Contract

Um único provider singleton local ao módulo fiscal possui `lastCommittedWindow`, actor buckets, context-total buckets, context-export buckets, cooldowns e leases. List, detail, export start e export page passam por sua mesma seção crítica; não existem high-waters ou rate maps paralelos.

| Operation | Read-only precheck | Atomic commit when accepted | Rejection / later failure |
| --- | --- | --- | --- |
| list/detail | enabled, user budget/cap e context-total budget | cleanup/high-water + `+1` user + `+1` context-total antes do provider | qualquer rejeição muta zero; provider error/abort não devolve unidades já aceitas |
| export start | signal/config, user budget/cap, cooldown e actor/context/global leases | cleanup/high-water + `+1` user + cooldown + leases | rejeição muta zero; falha/abort posterior mantém user/cooldown e libera leases uma vez |
| export page | signal/deadline, context-total token, context-export-share token e pacing | cleanup/high-water + `+1` context-total + `+1` context-export imediatamente antes do provider | indisponibilidade espera read-only; provider error/abort não devolve token aceito; exit libera leases do export |

List/detail continuam fail-fast quando seu user ou context-total budget está esgotado. Export page espera porque já existe um export admitido. Um list/detail aceito pode consumir a reserva interativa enquanto export espera; export jamais usa além de `exportShare`, e o total combinado jamais excede `ratePerContextMinute`. `nextAllowedMono[unifast|prosperar]` pertence ao coordinator, avança no commit de export page e persiste entre exports. O cleanup atômico de operação aceita remove buckets stale e cooldowns expirados; rejeições deixam ambos intactos. Estado transitório permanece bounded: a união de identidades em actor bucket atual, cooldown ativo ou actor lease é <=`MAX_ACTOR_BUCKETS`; contexts/nextAllowed são exatamente dois e leases globais no máximo dois.

O BCI misto obrigatório prova `list/detail aceito em W10 → wall W9 → export start/list/detail` sem reabrir unidades de W10, além de interleavings nos quais uma rejeição de contexto não cobra user budget. `rateSnapshot()` será estendido por test-only observation do estado bruto; não será exportado pelo módulo de produção.

## Pagination Consistency Contract

Toda página deve satisfazer `returned.page === requestedPage`. A primeira requisição é sempre `requestedPage=1`. Após a primeira página válida, congelar `perPage`, `total`, `totalPages`. Se `total=0`, exigir também `returned.page=1`, `totalPages=0`, `items=[]`, executar zero chamadas subsequentes, retornar 204 e não aplicar regras de tamanho da página final. Para `total>0`, exigir:

1. `returned.page === requestedPage` em todas as páginas;
2. os três metadados congelados (`perPage`, `total`, `totalPages`) permanecem idênticos; `page` varia e já é validado pela regra 1;
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
- `baixar` aceita `AbortSignal` e retorna `Promise<'downloaded'|'empty'>`; 204 retorna `empty` sem `blob()`/âncora/ObjectURL; sucesso retorna `downloaded`, verifica signal/generation antes de criar/clicar âncora e revoga cada ObjectURL exatamente uma vez em success/failure/abort.
- A assinatura continua retrocompatível para `/eventos/exportar`; omitir options preserva download legado. Teste de regressão cobre filename/blob/âncora do CSV PostgreSQL.
- Erro/export state é independente de list/revalidation. CTA desabilita quando `state.data?.total === 0`, durante export ou sem dados válidos; não usa tamanho da página atual.

## Observability Contract

Um evento estruturado por exportação registra somente:

- `operation=export`, `context`, `actorId` interno autenticado e correlation ID único do export;
- outcome allowlisted: `success|empty|client_aborted|deadline_exceeded|busy|limit_exceeded|pagination_inconsistent|provider_error|serialization_error`;
- pages attempted/completed, rows serialized, output bytes e durationMs;
- flags `clientAborted`, `deadlineExceeded`, `rateLimited`.

Não registrar filtros, documento, ID da compra, número/chave fiscal, provider IDs, token/CNPJ, payload ou CSV. As chamadas do adapter podem manter logs por página, mas recebem/propagam o correlation ID do export para correlação, sem conteúdo sensível.

`ratePerUserMinute` continua sendo orçamento de ações autenticadas: list/detail consomem uma unidade por request aceito e export consome uma unidade no start aceito. A amplificação de páginas é governada pelo budget do contexto; o ator também fica limitado a um export ativo e um início por minuto. Cada page call permanece atribuída ao `actorId` no evento agregado, sem cobrar novamente o contador de ações.

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
| `MonitorNotes` | `.` | `release/uninotas-smart-notas@f1a950a9fb48db68fd7370aed1a7605958a5d50b` | `working_tree` |
| `uninotas-foundation` | `foundation_documentation` | `main@0a3a9bc796b37f809b6d85a3649323d7b24409b9` | `working_tree` |

Os baselines foram refeitos em 2026-09-28 sobre o closeout consolidado de `ST-UX`. Coherence, diff, drift e authority foram repetidos sem mudança material; a aprovação existente permanece válida.

### Expected Changed Paths

| Repository | Path glob | Change | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M, A` | filtro base, rota, scheduler/admission, erros, serializer e testes |
| `MonitorNotes` | `backend/src/common/filters/all-exceptions.filter.ts` | `M` | allowlist de novos códigos e Retry-After canônico |
| `MonitorNotes` | `backend/src/common/filters/all-exceptions.filter.spec.ts` | `M` | teste owner do catálogo público e Retry-After |
| `MonitorNotes` | `backend/README.md` | `M` | contrato público/limites |
| `MonitorNotes` | `frontend/src/api/cliente.ts` | `M` | download cancelável/204 retrocompatível |
| `MonitorNotes` | `frontend/src/api/notas.ts` | `M` | filtros/export fiscal |
| `MonitorNotes` | `frontend/src/notas/exportacaoFiscal.ts` | `A` | owner único de geração/abort e commit tardio do download |
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
| `uninotas-foundation` | `artifacts/feature-briefs/uninotas-fiscal-workspace-improvements.md` | `M` | coordenação do objetivo de release |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | contrato estável consolidado no gate pré-aprovação |
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

## Canonical Module Anchors

- **Primary module doc:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Secondary module docs:** `none`
- **Planned decision promotion targets:** `Canonical Decision Register`; `API Endpoint Definitions`.
- **Module decision consolidation targets:** export request/success/traversal/CSV/errors/limits and admission.

## Definition of Done

- [ ] `DOD-EX-01` A rota aceita exatamente filtros fiscais sem `pagina`, um contexto e todos os leitores existentes.
- [ ] `DOD-EX-02` Um filtro vazio retorna 204 sem download; um filtro válido baixa todas as linhas atravessadas, não apenas a página atual.
- [ ] `DOD-EX-03` Rows/pages/deadline I/O+CPU/bytes/admission, actor start/cooldown e context budget/pacing derivados da configuração são aplicados e testados; nenhum limite trunca silenciosamente.
- [ ] `DOD-EX-04` Metadata/count/duplicidade são verificadas; erro de geração/inconsistência/abort não inicia CSV, e o cliente só comita download após Blob completo; truncamento de transporte não recebe claim de atomicidade.
- [ ] `DOD-EX-05` CSV e headers seguem exatamente os contratos acima, inclusive injection/PII/identificadores/null/datas/decimais.
- [ ] `DOD-EX-06` CTA usa filtros aplicados, ignora página, evita duplicata e cancela por filtro/navegação/logout/unmount sem download tardio.
- [ ] `DOD-EX-07` List/detail continuam uma chamada upstream por request e mantêm resposta/contrato existentes.
- [ ] `DOD-EX-08` BCI `5x2/10x3/20x5`, mixed-budget probes e RLS-E2 nos dois stages congelados provam coordinator único, exact-once admission, clocks, caps, context budget/share, reserva interativa, memória e recuperação de list/detail.
- [ ] `DOD-EX-09` Módulo fiscal e READMEs documentam contrato, limites e ausência de snapshot forte; nenhuma alegação de deploy.
- [ ] `DOD-EX-10` Local Verification, PCV, segurança, test-quality, arquitetura, final, triple review e guards passam.

## Decision Baseline (Frozen Before Implementation)

- [x] `EX-D-01` Exportar todo o filtro aplicado, não a página; um único contexto; sem agregado.
- [x] `EX-D-02` Backend-owned sequential page walk; frontend faz uma requisição.
- [x] `EX-D-03` Buffer completo antes da resposta para garantir “arquivo inteiro ou erro”; limites tornam memória/duração finitas.
- [x] `EX-D-04` Sem snapshot forte; consistência detectável fail-closed e linguagem honesta.
- [x] `EX-D-05` Contrato HTTP, CSV, erros, observabilidade e lifecycle são os congelados neste TODO.
- [x] `EX-D-06` Serializer fiscal-local; nenhuma falsa abstração compartilhada com logs.
- [x] `EX-D-07` Exportação assíncrona/persistida fica fora; filtros acima do envelope precisam ser reduzidos.
- [x] `EX-D-08` Raw `idCompra`/`chaveAcesso` entram no arquivo para leitores autenticados; não logar esses valores.
- [x] `EX-D-09` Um coordinator singleton é o único owner de high-water, user/context/export-share budgets e admission de list/detail/export; precheck é read-only e commit aceito é atômico.
- [x] `EX-D-10` Deadline cancela waits/I/O em andamento; pacing é persistente por contexto; actor capacity conta a união bucket/cooldown/lease e permanece bounded.

## Module Decision Baseline Snapshot (1-1 Mandatory Before APROVADO)

- **Primary module:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Gate status:** `no_material_findings`

| TODO Decision | Module Decision Ref | Current Module Decision | Planned Handling (`Preserve|Supersede (Intentional)|Out of Scope`) | Evidence |
| --- | --- | --- | --- | --- |
| `EX-D-01` | `FISC-EX-01` | todo o filtro aplicado, uma conta, sem página/agregado | `Preserve` | module `Canonical Decision Register` + `Export request` |
| `EX-D-02` | `FISC-EX-02` | page walk sequencial pertence ao backend | `Preserve` | module `Export traversal` |
| `EX-D-03` | `FISC-EX-03` | Buffer bounded completo antes de iniciar resposta | `Preserve` | module `Export success and transport boundary` |
| `EX-D-04` | `FISC-EX-04` | consistência detectável sem snapshot forte | `Preserve` | module `Export traversal` |
| `EX-D-05` | `FISC-EX-05` | HTTP/CSV/errors/observability/lifecycle formam o boundary | `Preserve` | module `API Endpoint Definitions` |
| `EX-D-06` | `FISC-EX-06` | serializer permanece fiscal-local | `Preserve` | module `CSV schema` |
| `EX-D-07` | `FISC-EX-07` | síncrono bounded; async exige novo TODO | `Preserve` | module `Limits and admission` |
| `EX-D-08` | `FISC-EX-08` | raw purchase/access permitidos; internal/PII/secret proibidos | `Preserve` | module `CSV schema` |
| `EX-D-09` | `FISC-EX-09` | coordinator único e commit atômico compartilhado | `Preserve` | module `Limits and admission` |
| `EX-D-10` | `FISC-EX-10` | deadline cancellation, pacing contextual e actor-state bound | `Preserve` | module `Limits and admission` + `Export success and transport boundary` |

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** export adiciona bulk reads ao mesmo orçamento de user/context já usado por list/detail e exige um único owner atômico.
- **Deviation / debt being retired:** `FiscalNotesService.consumeBudget()` possui cleanup mutante e clocks múltiplos; não há owner para export share/cooldown/leases.
- **Target steady-state after closeout:** um coordinator singleton fiscal governa high-water, budgets, pacing e export admission; controller/adapter não possuem rate state paralelo.
- **Temporary exceptions allowed:** `none`.
- **Cutover / removal condition:** suites mistas, BCI e RLS provam list/detail/export no coordinator; helpers antigos são removidos ou delegam integralmente a ele.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| projected read-only precheck + atomic accepted commit | `FISC-EXPORT-ADMISSION-01` | all fiscal budget operations | rejeição nunca polui state |
| one non-regressing fixed-window owner | `FISC-EX-09` | list/detail/export | impede reabertura/bypass sob wall regression |
| page budget separate from export start user charge | `FISC-EX-02` | export traversal | evita multiplicar rate do ator sem furar quota do contexto |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why Forbidden | Exception Policy |
| --- | --- | --- | --- |
| rate maps/high-water paralelos por operação | mixed-budget BCI diverge | permite quota bypass e cleanup conflitante | none |
| charge user por export page | user counter >1 por start | contradiz public admission contract | none |
| cleanup em request rejeitado | raw pre/post snapshot difere | quebra rejection atomicity | none |
| frontend page walk ou CSV streaming antes de validar | >1 browser request ou response inicia antes do final | owner errado/arquivo parcial por geração | none |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| test | shared fiscal coordinator | `cd backend && npm test -- --runInBand` | partial charge, parallel rate state, clock regression bypass | `implement-in-this-todo` | `DOD-EX-08`, `VAL-EX-01`, mixed Jest specs |
| guard/test | raw coordinator state + clocks | `cd backend && npm test -- --runInBand fiscal-notes` + `bci-pcv1.json` | non-atomic admission, unbounded actor state, pacing reset | `implement-in-this-todo` | `DOD-EX-08`, BCI-E3 artifact |
| test | React export lifecycle | exact normalized canonical-runner loop in `VAL-EX-04 Exact WSL Command` | duplicate/late download, missed abort, page-only cancellation | `implement-in-this-todo` | `DOD-EX-06/08`, `VAL-EX-04`, FRC-E3 artifact |
| audit | coordinator cutover | `triple_audit_session.py` lane `cutover-integrity` | surviving parallel `consumeBudget`/rate maps/shims | `implement-in-this-todo` | `VAL-EX-07`, cutover-integrity result |
| test | runtime load/memory | `cd backend && node --expose-gc ./node_modules/jest/bin/jest.js --runInBand fiscal-notes.rls` | quota starvation, missed deadline cleanup, RSS/external blowup | `implement-in-this-todo` | `DOD-EX-08`, `VAL-EX-06`, RLS-E2 artifact |

## Assumptions Preview

| ID | Assumption | Concrete Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `EX-A-01` | primeira página informa total/perPage/totalPages antes do page walk | `backend/src/fiscal-notes/smart-notas.adapter.ts:240-258`; `backend/src/fiscal-notes/fiscal-notes.types.ts:25-31` | impossível rejeitar cedo | `High` | `Keep as Assumption` |
| `EX-A-02` | provider não oferece snapshot/cursor/order no contrato consumido | `backend/src/fiscal-notes/smart-notas.adapter.ts:34-49`; `backend/src/fiscal-notes/fiscal-notes.types.ts:33-41` | contrato poderia ficar mais forte | `High` | `Keep as Assumption` |
| `EX-A-03` | concorrência e rate são configuráveis e precisam governar list/detail/export em conjunto | `backend/src/config/configuration.ts:64-94`; `backend/src/fiscal-notes/smart-notas.adapter.ts:74-89`; `backend/src/fiscal-notes/fiscal-notes.service.ts:157-205` | reserva/pacing precisam de outro owner | `High` | `Keep as Assumption` |
| `EX-A-04` | os quatro leitores já recebem raw purchase/access keys pelo endpoint fiscal | `backend/src/fiscal-notes/fiscal-notes.controller.ts:10-15`; `backend/src/fiscal-notes/fiscal-notes.service.ts:207-228`; `frontend/src/api/notas.ts:17-33`; `frontend/src/paginas/ListaNotas.tsx:19-24` | export raw amplia autorização | `High` | `Keep as Assumption` |
| `EX-A-05` | downloader pode evoluir de forma retrocompatível com AbortSignal sem pacote | `frontend/src/api/cliente.ts:79-111`; `frontend/src/api/cliente.ts:122-155`; `frontend/src/api/eventos.ts:63-77`; `frontend/src/auth/SessaoContexto.tsx:7-18`; `frontend/src/auth/SessaoContexto.tsx:30-47` | lifecycle/legado precisa owner diferente | `High` | `Keep as Assumption` |

## Execution Plan

1. Confirmar que o módulo fiscal consolidado e este TODO permanecem 1:1 antes de editar código.
2. Criar testes backend fail-first para DTO/rota/erros, 0/1/200/201 páginas, 20k/20k+1, deadline I/O+CPU, bytes, budget/admission configuráveis, consistência, CSV e logs sanitizados.
3. Implementar filtro base + DTOs, erros/filtro global, coordinator/service com scheduler comum por contexto, serializer fiscal-local chunked e controller thin; não chamar recursivamente `FiscalNotesService.list()`.
4. Criar testes frontend/race/browser fail-first para filtros aplicados, 204, duplicate, filter change, navigation, logout, 401, abort, URL lifecycle e late response.
5. Implementar cliente/download cancelável e CTA com owner único de generation/AbortController.
6. Executar suites amplas, carga concorrente com list/detail, security review e browser preview fresco.
7. Executar auditorias/gates, consolidar docs/evidência e parar em `Local-Implemented`.

## Test Strategy

- **Backend test-first:** port/fetch, relógio e pacing injetáveis; nenhum acesso real no suite determinístico.
- **Deadline I/O+CPU:** deadline-derived signal/remaining time aborta wait/provider pendurado; serializer confere relógio/signal antes e depois de cada chunk/yield (máximo 500 linhas); teste prova 504 na fronteira, cleanup e zero late calls.
- **Frontend test-first:** extrair somente um pequeno coordinator/hook se necessário para testar ownership; não duplicar filtro.
- **Browser:** APIs interceptadas provam UX/download; não é prova cross-stack.
- **Cross-stack:** specs NestJS provam HTTP/CSV; smoke real fica no cutover.

## Validation Steps

- [ ] `VAL-EX-01` `cd backend && npm test -- --runInBand`
- [ ] `VAL-EX-02` `cd backend && npm run build && npx eslint "{src,test}/**/*.ts" --max-warnings=0` (não usar `npm run lint`, pois contém `--fix`).
- [ ] `VAL-EX-03` `cd frontend && npm run test:notas && npm run lint && npm run build`
- [ ] `VAL-EX-04` Executar o bloco exato abaixo para cada `duplicate|filter-change|navigation|unmount|logout|401|page-only|empty-204`; ele usa o runner canônico normalizado somente em memória porque o arquivo montado possui CRLF, sem alterar Delphi.
- [ ] `VAL-EX-05` Build fresco; iniciar preview, comprovar SHA/bundle servido, executar `ALVO=<preview> CHROME=<local> npm run e2e:notas` com APIs interceptadas/download capturado; encerrar preview.
- [ ] `VAL-EX-06` Executar RLS-E2 `load 4:180s` default e `stress 2:185s` constrained com mixes/resultados/limites de heap/external/arrayBuffers/RSS congelados; comprovar caps e recuperação.
- [ ] `VAL-EX-07` Capability audits NestJS/React/Vite, endpoint scrutiny, race, load, security, test-quality, arquitetura, final, triple review com lane `cutover-integrity` e verification-debt.
- [ ] `VAL-EX-08` Foundation validators/guards e `git diff --check`.

### VAL-EX-04 Exact WSL Command

```bash
frc_status=0
frc_artifact_root="$PWD/foundation_documentation/artifacts/tmp/uninotas-export-pcv/frc"
for race_scenario in duplicate filter-change navigation unmount logout 401 page-only empty-204; do
  bash <(tr -d '\r' < delphi-ai/tools/frontend_race_probe.sh) --scenario "$race_scenario" --burst-level 5 --repetitions 2 --timeout-sec 120 --workdir frontend --runner "npm run test:notas:race" --output-dir "$frc_artifact_root/$race_scenario/low" --fail-fast || frc_status=1
  bash <(tr -d '\r' < delphi-ai/tools/frontend_race_probe.sh) --scenario "$race_scenario" --burst-level 10 --repetitions 3 --timeout-sec 120 --workdir frontend --runner "npm run test:notas:race" --output-dir "$frc_artifact_root/$race_scenario/medium" --fail-fast || frc_status=1
  bash <(tr -d '\r' < delphi-ai/tools/frontend_race_probe.sh) --scenario "$race_scenario" --burst-level 20 --repetitions 5 --timeout-sec 120 --workdir frontend --runner "npm run test:notas:race" --output-dir "$frc_artifact_root/$race_scenario/high" --fail-fast || frc_status=1
done
DELPHI_RACE_SCENARIO=aggregate DELPHI_RACE_INPUT_DIR="$frc_artifact_root" DELPHI_RACE_OUTPUT_FILE="$PWD/foundation_documentation/artifacts/tmp/uninotas-export-pcv/frc-pcv1.json" npm --prefix frontend run test:notas:race || frc_status=1
test "$frc_status" -eq 0
```

O modo `aggregate` de `frontend/e2e/notas-race.ts` consolida/valida as 80 attempts, políticas/oráculos e o hash canônico `pcv-1`; ausência/falha/duplicata invalida o JSON e retorna não zero. `foundation_documentation/artifacts/tmp/**` é o espaço derivado/ignorado governado; `MonitorNotes/artifacts/**` permanece intocado. O readiness command executável neste checkout é `bash delphi-ai/tools/verify_context.sh`; o wrapper `delphi-ai/verify_context.sh` também está CRLF e não é alterado por este TODO.

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

- **Complexity:** `big`
- **Checkpoint policy:** `section-by-section`
- **Why this level:** endpoint bulk cross-stack, contrato público, raw identifiers, rate/admission compartilhados e lifecycle de download.
- **Review lenses:** Architecture, Code Quality, Tests, Performance, Security, Elegance e Structural Soundness.

### Issue Card `PR-EX-01` — single owner para budgets/admission

- **Severity:** `high`
- **Evidence:** `backend/src/fiscal-notes/fiscal-notes.service.ts:157-205`; `backend/src/fiscal-notes/smart-notas.adapter.ts:74-89`.
- **Why now:** export start e pages entram no mesmo limite já usado por list/detail; owners paralelos permitiriam bypass sob regressão de relógio ou cobrança parcial.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — coordinator fiscal único para list/detail/export (recommended) | medium | low after tests | módulo fiscal | low | O(1) admission; pacing bounded | high | high; one state owner |
| B — high-waters separados com reconciliação | high | high | service/adapter | high | extra synchronization | low | low; hidden coupling |
| C — manter maps atuais e adicionar export isolado | low | high | aparentemente local | high | pode exceder quota | low | invalid; budget bypass |

### Issue Card `PR-EX-02` — topologia da exportação completa

- **Severity:** `high`
- **Evidence:** `backend/src/fiscal-notes/smart-notas.adapter.ts:34-49`; `frontend/src/api/cliente.ts:122-155`.
- **Why now:** o usuário pediu todo o filtro, enquanto o provider é paginado e credenciais/quota pertencem ao backend.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — page walk backend sequencial + Buffer bounded (recommended) | medium | bounded memory/quota | NestJS + CTA React | medium | até 200 calls/24MiB/180s | high para o envelope atual | high; clear ownership |
| B — fila/storage/link assíncrono | high | operational | runtime/infra/UI | high | melhor para volumes grandes | medium | high, mas fora do prazo/escopo |
| C — browser percorre páginas | low | credential/race/partial file | frontend/provider | high | amplification client-side | low | invalid; wrong owner |

### Issue Card `PR-EX-03` — consistência sem snapshot e fronteira de transporte

- **Severity:** `high`
- **Evidence:** `backend/src/fiscal-notes/fiscal-notes.types.ts:25-41`; `backend/src/fiscal-notes/smart-notas.adapter.ts:240-258`.
- **Why now:** Smart Notas não fornece cursor/snapshot/order; “arquivo integral” precisa ser verdadeiro sem prometer atomicidade de rede.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — metadados/IDs/counts fail-closed + linguagem sem snapshot (recommended) | medium | mutação indetectável residual | service/tests/docs | medium | checks O(rows) | high | high; honest contract |
| B — declarar snapshot sem suporte do provider | low | critical correctness | product/legal | high | none | low | invalid claim |
| C — exportar sem consistency checks | low | silent duplicate/missing rows | service | low initially | fastest | low | low; partial data risk |

### Issue Card `PR-EX-04` — ownership do download React

- **Severity:** `medium`
- **Evidence:** `frontend/src/paginas/ListaNotas.tsx:8-24`; `frontend/src/api/cliente.ts:79-111,140-155`; `frontend/src/auth/SessaoContexto.tsx:30-47`.
- **Why now:** filtros, logout, unmount e respostas tardias podem competir com Blob/âncora.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — owner local com ref/generation/AbortController (recommended) | medium | low after races | ListaNotas/client | low | one request, duplicate dropped | high | high; lifecycle explicit |
| B — estado global de export | medium | medium | context/session | medium | similar | medium | unnecessary coupling |
| C — apenas disabled visual | low | high | UI | low initially | duplicate calls possible | low | invalid race protection |

### Issue Card `PR-EX-05` — deadline durante I/O pendente

- **Severity:** `high`
- **Evidence:** `backend/src/fiscal-notes/smart-notas.adapter.ts:74-109`; provider timeout existente pode superar o tempo restante do export.
- **Why now:** checks depois do await não garantem o bound de 180s quando a page fica pendurada.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — deadline-derived signal + remaining-time em waits/I/O (recommended) | medium | low | coordinator/adapter port | low | cancela no bound | high | high; one deadline owner |
| B — checks apenas antes/depois do await | low | high | service | low | pode exceder 180s | medium | invalid bound |
| C — confiar só no provider timeout | low | high | config | medium | timeout pode ser maior | low | conflates contracts |

### Issue Card `PR-EX-06` — pacing e actor-state bounded

- **Severity:** `high`
- **Evidence:** `backend/src/fiscal-notes/fiscal-notes.service.ts:31-35,157-205`; state atual não possui pacing/cooldown/leases.
- **Why now:** dois contextos e saltos de wall clock podem resetar pacing ou acumular identidades se o owner/cardinalidade não forem exatos.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — `nextAllowedMono[context]` persistente + cap da união bucket/cooldown/lease (recommended) | medium | low after BCI | coordinator | medium | O(actors) projected cap, max 5k | high | high; bounded and context-correct |
| B — pacing por export e cap só de buckets | low | high | service | medium | bursts/heap growth | low | invalid under rollover |
| C — pacing global entre contextos | low | medium | all exports | low | needless cross-context starvation | medium | wrong isolation |

### Issue Card `PR-EX-07` — RLS de memória reproduzível

- **Severity:** `medium`
- **Evidence:** Node Buffers aparecem em `external` e `arrayBuffers`; dois CSVs podem coexistir.
- **Why now:** thresholds sem atores/timeline/GC/baseline ou com métricas somadas podem falhar por definição ou deixar RSS escapar.

| Option | Effort | Risk | Blast radius | Maintenance | Performance | Elegance | Structural soundness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — processo isolado, fixture fixa, métricas separadas e caps calibrados (recommended) | medium | low | RLS harness | medium | mede custo real local | high | high; reproducible |
| B — somar external+arrayBuffers | low | high false failure | tests | low | double counts | low | invalid metric |
| C — medir apenas heapUsed | low | high false pass | tests | low | ignora Buffer | low | incomplete |

### Failure Modes & Edge Cases

- Provider muda total/perPage/totalPages/page, duplica ID, encurta página ou falha no meio: 502/provider error e nenhum response CSV iniciado.
- Resultado zero, limite `20k/200/24MiB`, deadline exato, abort antes/depois do Buffer e falha de transporte têm branches separados.
- Wall regression/jump, fixed-window boundary, actor bucket cap, cooldown/lease collisions e context token starvation usam os oráculos BCI congelados.
- CSV cobre null, CR/LF/quotes/semicolon, fórmula, zeros iniciais e identificadores longos; logs não recebem filtros nem conteúdo fiscal.
- Repeated click, filter change, page change, logout, unmount, 401 e late Blob são cobertos por FRC `5x2/10x3/20x5`.

### Residual Unknowns / Risks

| Type | Item | Confidence / handling |
| --- | --- | --- |
| assumption | provider continua devolvendo metadados numéricos e ID interno único por travessia | high; contract tests + fail-closed |
| unknown | quota/latência reais podem impedir filtros abaixo dos caps | medium; RLS local + cutover smoke |
| unknown | mutação da origem pode preservar todos os metadados/IDs e ainda alterar campos | high confidence no risco; não alegar snapshot |
| risk | Buffer backend + resposta + Blob browser multiplicam memória | high; caps e RSS/external/heap thresholds |
| risk | coordenação é por instância | high; stage tem uma réplica; reavaliar antes de scale-out |
| risk | rede/proxy pode truncar transmissão já iniciada | high; contrato limita garantia à geração e commit do Blob cliente |

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
| `R3-EX-H01` | `high` | actor rate podia ser cobrado uma vez ou por página | uma unidade no start + um ativo e um start/min/ator; pages usam context budget |
| `R3-EX-M02` | `medium` | teste owner do filtro global faltava no diff | `all-exceptions.filter.spec.ts` incluído |
| `R4-EX-H01` | `high` | rejeição/collision/Retry-After ainda permitia implementações divergentes | admissão atômica sem charge em rejeição + precedência cause/header congelada |
| `R5-H01` | `high` | admission GET muta counters/cooldown/leases sob concorrência | BCI required com exact-once bursts 5/10/20 |
| `R5-H02` | `high` | clocks, rounding, actor bucket cap e incap branches incompletos | wall/monotonic separados + precedência e fixtures completas |
| `R6-H01/M02` | `high, medium` | BCI não distinguia eligible/pre-blocked e bucket cleanup estava implícito | oráculos 1/0 separados + lifecycle na janela fixa congelado |
| `R7-AR-H01/CR-H02` | `high` | cleanup mutante contradizia rejeição sem mutação | projeção read-only + cleanup somente no commit aceito; oráculo usa estado bruto |
| `R7-AR-M01/CR-H04` | `high` | regressão/amostras de relógio podiam reabrir budget ou divergir header | amostra única + `effectiveWindow` não regressiva + Retry-After fail-closed |
| `R7-CR-H01` | `high` | `page` era contado entre quatro metadados invariáveis | somente `perPage/total/totalPages` invariáveis; `page === requestedPage` |
| `R7-CR-H03/H05` | `high` | token de contexto e topologias BCI não tinham oráculos exatos | matriz setup/aceitos/erro/delta e distinção admission versus HTTP congeladas |
| `R7-AR-M02/CR-M01` | `medium` | limite global dizia 2 e fórmula variável | fórmula `min(2,maxConcurrency-1)`, máximo absoluto 2 |
| `R7-CR-M02` | `medium` | serializer não checava client abort por chunk | signal/deadline antes e depois de todo chunk/yield |
| `R7-AR-M03/CR-M03` | `medium` | módulo canônico ainda não continha o endpoint planejado | módulo sincronizado + gate `Preserve/Supersede (Intentional)/Out of Scope` |
| `R7-CR-M04` | `medium` | ledger usava taxonomia inválida | categorias normalizadas à taxonomia do projeto |
| `R8-AR-H01/CR-H01` | `high` | high-water/budgets não tinham owner comum para list/detail/export | coordinator singleton, tabela precheck/commit/failure e probes mistos congelados |
| `R8-CR-H02` | `high` | BCI-E3 não fixava distribuição, headers e estado observável | product/probe policies separadas, fixture/snapshot e 20-op oracles exatos |
| `R8-AR-H02/CR-M04` | `high` | módulo/gate não eram source-of-truth e 1:1 canônicos | decision register, API Endpoint Definitions e map EX-D/FISC-EX 1:1 |
| `R8-AR-M01/CR-M01` | `medium` | vazio não validava identidade da página | page identity universal; vazio exige page 1 e zero calls seguintes |
| `R8-CR-M02` | `medium` | “arquivo integral” misturava geração e transporte | boundary server/client explícito; sem claim de atomicidade no fio |
| `R8-AR-M02` | `medium` | export share não tinha fórmula única | ternário determinístico congelado |
| `R8-AR-M03` | `medium` | evidence loci de assumptions estavam imprecisos | ranges exatos do código atual registrados |
| `R8-CR-M03` | `medium` | FRC/RLS-E2 e memória não tinham workload suficiente | perfis/repetições/stages/resultados e heap/external/RSS congelados |
| `R8-GOV-M04` | `medium` | Plan Review não possuía issue cards/trade-offs canônicos | cards A/B/C, failure modes e residual unknowns adicionados |
| `R8-GOV-H03` | `high` | reviewer exigiu que o commit material referencie o próprio SHA | `Challenged`: auto-referência Git é impossível; commit de attestation posterior aponta ao baseline material publicado e drift compara contra ele |
| `R9-AR-H01/CR-H1` | `high` | architecture harness não obedecia schema determinístico | tabela de seis colunas com comandos/regressão/timing/evidence |
| `R9-CR-H2` | `high` | deadline não cancelava I/O em andamento | composed deadline signal + remaining time + hung-provider oracle |
| `R9-AR-M01/CR-H3` | `high` | pacing/cardinalidade podiam resetar ou crescer sob wall jump | pacing persistente por contexto + cap da união bucket/cooldown/lease + BCI misto |
| `R9-CR-H4` | `high` | RLS tinha actor collision e métricas de Buffer não reproduzíveis | atores/timeline/latência/retention/GC/sampling e memory caps separados |
| `R9-CR-H5` | `high` | coordinator/deadline/pacing não estavam no baseline 1:1 | `EX-D-09/10 ↔ FISC-EX-09/10` e módulo ampliado |
| `R9-CR-M1` | `medium` | FRC não individualizava todo lifecycle/204 | oito cenários 5x2/10x3/20x5 + downloader `downloaded|empty` |
| `R9-AR-M02` | `medium` | retirement do rate path exigia cutover-integrity | lane marcada required no triple review |
| `R10-AR-H01` | `high` | FRC command tinha placeholder e runner CRLF no WSL | loop exato por cenário/perfil usa runner canônico normalizado em memória; readiness usa helper LF |
| `R11-AR-H01/CR-H01` | `high` | matriz FRC podia mascarar falha intermediária | acumulador executa toda matriz e retorna não zero se qualquer profile/agregação falhar |
| `R11-CR-M02` | `medium` | output FRC colidia com `MonitorNotes/artifacts/**` preservado | output absoluto vai ao `foundation_documentation/artifacts/tmp/**` ignorado/governado e aggregate valida `frc-pcv1.json` |

### Residual Risks

- Quota/latência real pode impedir filtros grandes mesmo abaixo dos limites; falha explícita e cutover smoke são obrigatórios.
- Mudança de origem pode escapar das verificações sem cursor/snapshot; risco documentado e não vendido como snapshot.
- Buffer do backend + Buffer HTTP + Blob do browser ampliam memória; 24 MiB e RLS limitam e medem, sem afirmar SLO de produção.
- Admissão é por instância; stage atualmente usa uma réplica. Escalar réplicas requer reavaliar coordenação distribuída no cutover.

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review status:** `no_material_findings`
- **Decision review evidence / resolution:** `/root/filtered_export_architecture_r12` GO; all R1-R11 material findings integrated or challenged with rationale.
- **Architecture adherence review:** `required after implementation`
- **Adherence status:** `not_run`
- **No-go handling:** `retornar ao plano; não aprovar/concluir com finding material aberto`.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Baseline branch:** `uninotas-foundation/main`
- **Baseline commit:** `e0c41fe856bd16d735be971303bdf9e63c198b0a`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** o baseline R12 material permanece intacto; o commit atualizado registra apenas o closeout UX, os novos SHAs de comparação, a autoridade já aprovada e a admissão package-first/capability.
- **Evidence / reference:** `origin/main` contém `e0c41fe856bd16d735be971303bdf9e63c198b0a`; rota, filtros, CSV, limites, autorização, clocks e lifecycle não mudaram no rebaseline.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-filtered-csv-export.md`
- **Gate status:** `no_material_findings`
- **Evidence / reference:** `review_scope_drift_guard.py` sobre o baseline pós-UX `e0c41fe856bd16d735be971303bdf9e63c198b0a`: `go`, `0/23` seções materiais alteradas; rebaseline administrativo, sem renovação material de escopo.

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
- **Critique status:** `no_material_findings`
- **Findings summary:** R12 confirmou fail-closed, 24 invocações/80 attempts, aggregate `pcv-1`, artifact root governado e ausência de regressão material.
- **Evidence / reference:** reviewers `/root/filtered_export_architecture_r12` e `/root/filtered_export_critique_r12`; ambos GO sem finding material.
- **Isolation:** `fresh internal no-context reviewer; cannot implement`
- **Lenses:** `correctness|performance|security|elegance|structure|operational fit`.

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Guard scope:** `EX-A-01,EX-A-02,EX-A-03,EX-A-04,EX-A-05`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-filtered-csv-export.md`
- **Gate status:** `no_material_findings`
- **Evidence / reference:** paths do adapter/types/config/service/controller/downloader/session/eventos resolvidos no checkout e sustentam `EX-A-01..05`.
- **Post-UX rebaseline:** `go` em 2026-09-28 sobre `MonitorNotes@f1a950a9` e `uninotas-foundation@0a3a9bc`; nenhum owner/contrato das assumptions mudou.

## Approval

- **Status:** `approved-sequenced`
- **Approved by:** `project owner / user`
- **Approval reference:** resposta explícita `APROVADO` em 2026-09-28 para o pacote serial UX seguido de exportação; renovação explícita `aprovo` em 2026-09-28 para adicionar `frontend/src/notas/exportacaoFiscal.ts` como owner único de geração/abort e commit tardio do download. A execução permanece condicionada ao rebaseline renovado deste TODO.
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
- **Subagent / delegation authorization:** `authorized by explicit APROVADO on 2026-09-28 for one workflow-required serialized executor, only after the mandatory post-UX rebaseline guards return go`
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
| extended `baixar(caminho,nome,options?) -> downloaded|empty` | fiscal export and existing `/eventos/exportar` | `planned backward-compatible` | fiscal abort/204 tests plus legacy PostgreSQL CSV regression |
| fiscal module contract | backend/frontend READMEs and Foundation module | `planned` | exact route/headers/limits/no-snapshot language |

## Package-First Assessment

- **Query executed:** `bash delphi-ai/tools/query_packages.sh --project-root . --search "csv export nestjs react"`
- **Relevant packages found:** `none`.
- **Decision:** implementar nos owners existentes `backend/src/fiscal-notes/**` e frontend fiscal, sem criar pacote ou dependência.
- **Capability evidence:** audits NestJS, React e Vite retornaram `ready` para os manifests e scripts requeridos.
- **Rationale:** o serializer, coordinator de quota e lifecycle do download pertencem ao boundary fiscal local congelado; o catálogo proprietário não contém capacidade equivalente.

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
| `delphi-ai/skills/backend-concurrency-idempotency-validation/SKILL.md` | admissão concorrente em memória | exact-once counters/cooldown/leases | double charge/leak | BCI obrigatório |
| `delphi-ai/skills/runtime-load-stress-validation/SKILL.md` | bulk/memória | profiles/thresholds/recovery | SLO sem prova | RLS obrigatório |
| `delphi-ai/skills/security-adversarial-review/SKILL.md` | CSV/raw IDs | injection/redaction/auth | conteúdo em logs | security gate |
| `delphi-ai/skills/audit-protocol-triple-review/SKILL.md` | coordinator substitui rate path | performance/test/cutover lanes em pacote bounded | shim/map paralelo | triple audit com `cutover-integrity` |
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
| `pcv-1` | `BCI` | `backend-concurrency-idempotency-validation` | `required` | `high` | `BCI-EXACT-ONCE-SEMANTICS` | admissão muta counters/cooldown/leases sob starts sobrepostos | `before_local_implemented` | `BCI-E3` | `pending` | state leak/double charge | `U-CONCURRENCY-SURFACE-UNKNOWN` | `2026-09-28T18:00:00Z` | `pending-routine-executor` |
| `pcv-1` | `RLS` | `runtime-load-stress-validation` | `required` | `high` | `RLS-BATCH-OR-BULK-PATH-CHANGED` | paginação, memória, budget e concorrência afetam runtime | `before_local_implemented` | `RLS-E2` | `pending` | quota real e memória browser | `U-RUNTIME-PRESSURE-UNKNOWN` | `2026-09-28T18:00:00Z` | `pending-routine-executor` |

### EPS planned evidence

- Classificar `bounded-list + external-page-walk + in-memory-serialization`; registrar calls/pages/rows/bytes/duration e provar query/filter sem page.
- Artifact planejado: `foundation_documentation/artifacts/tmp/uninotas-export-pcv/eps-pcv1.json`, schema `pcv-1`, SHA-256 canônico.

### FRC planned evidence

- `baixar()` evolui retrocompativelmente para `Promise<'downloaded'|'empty'>`; 204 retorna `empty` sem chamar `blob()`, criar anchor/ObjectURL ou download.
- **Product policies:** duplicate=`drop duplicate`; filter/navigation/unmount/logout/401=`cancel previous`; generation guard=`last-write-wins` apenas para estado corrente; page-only=`keep current`.
- **Probe policy:** repeated synchronous trigger/barrier + resolve e reject tardios controlados. Rodar `FRC-SP-L=5x2`, `FRC-SP-M=10x3` e `FRC-SP-H=20x5` separadamente para `duplicate`, `filter-change`, `navigation`, `unmount`, `logout`, `401`, `page-only` e `empty-204`.
- **Oráculos:** duplicate gera 1 request, 1 Blob/anchor/click/ObjectURL/revoke e 1 `downloaded`; filter/navigation/unmount/logout/401 abortam 1 request e permanecem com zero Blob/anchor/click/download/late-state para resolve e reject; page-only não aborta e conclui exatamente 1 download; empty retorna 1 `empty`, zero Blob/anchor/ObjectURL e mensagem única. Todo ObjectURL criado é revogado exatamente uma vez.
- Artifact planejado: `foundation_documentation/artifacts/tmp/uninotas-export-pcv/frc-pcv1.json`.

### BCI planned evidence

- **Invariant `FISCAL-EXPORT-ADMISSION-01`:** “aceito” significa concessão atômica de admissão/leases, não HTTP 200. Cada aceito consome exatamente as unidades descritas; cada rejeitado preserva o snapshot bruto; success/error/abort liberam leases uma vez sem apagar budget/cooldown aceitos.
- **Product `concurrency_policy`:** `serialize atomic admission + reject excess`; **probe synchronization:** `simultaneous-start/barrier`, mantendo winners ativos até registrar todas as 20 decisões. Cada topologia roda `BCI-SP-L=5x2`, `BCI-SP-M=10x3` e `BCI-SP-H=20x5`; cada batch começa de fixture isolada.
- **Common exact fixture:** default `maxConcurrency=8`, rates `user=30/context=120`, `wallNow=W10+15s`, `monotonicNow=1_000_000`; portanto fixed-window Retry-After=`45`, lease floor=`5`, cooldown iniciado em `970_000` deixa `30`, e cooldown de winner novo deixa `60`. Atores distintos são `A01..A20`; contexto único é Unifast; topologia dual distribui `A01..A10` em Unifast e `A11..A20` em Prosperar; mesmo ator/dual distribui dez starts por contexto.
- **Canonical raw snapshot:** JSON ordenado contendo `lastCommittedWindow`, actor buckets `[actor,window,count]`, context-total/export-share buckets, cooldowns `[actor,acceptedAtMono]`, actor/context/global leases e scheduler `nextExportAtMono`; counters de `wallNow`, `monotonicNow` e provider calls são evidência separada. Snapshot pós-rejeição deve ser idêntico ao pré; cada admission decision chama cada relógio uma vez.

| 20-operation isolated topology | Accepted | Nineteen/twenty result | Post-admission / post-exit oracle |
| --- | --- | --- | --- |
| mesmo ator/Unifast elegível | `1` | `19 x 429 ExportacaoFiscalOcupada, Retry-After=60` | winner `+1` user/cooldown e 3 leases; losers delta zero; exit remove 3 leases |
| 20 atores/Unifast elegível | `1` | `19 x 429 ExportacaoFiscalOcupada, Retry-After=5` | somente winner tem user/cooldown/leases; exit remove leases |
| mesmo ator/10 starts por contexto | `1` | `19 x 429 ExportacaoFiscalOcupada, Retry-After=60` | somente winner cobrado; exit remove leases |
| 20 atores/10 por contexto | `2` | `18 x 429 ExportacaoFiscalOcupada, Retry-After=5` | um winner/contexto, dois charges/cooldowns, global=2; exit zera leases |
| user budget do ator esgotado | `0` | `20 x 429 LimiteDeConsultaExcedido, Retry-After=45` | snapshot idêntico; zero provider call |
| `maxConcurrency=1` ou `ratePerContextMinute=1` | `0` | `20 x 429 ExportacaoFiscalOcupada, Retry-After=60` | snapshot idêntico; zero provider call |
| context/global lease pré-ocupado sem cooldown/budget collision | `0` | `20 x 429 ExportacaoFiscalOcupada, Retry-After=5` | snapshot idêntico |
| actor cooldown iniciado em `970_000` | `0` | `20 x 429 ExportacaoFiscalOcupada, Retry-After=30` | snapshot idêntico |
| context tokens indisponíveis, 20 atores/Unifast | `1` | `19 x busy/5`; winner espera e termina `504` | user/cooldown permanecem; zero provider call; leases zeram no deadline |
| buckets em `cap-1`, 20 novos atores/Unifast | `1` | `19 x busy/45` pela colisão context lease + cap | winner ocupa último bucket; losers delta zero; exit zera leases |
| buckets no cap, 20 novos atores | `0` | `20 x LimiteDeConsultaExcedido/45` | nenhum bucket criado/removido |
| buckets no cap, mesmo ator existente elegível | `1` | `19 x busy/60` | nenhum slot novo; winner cobra unidade/cooldown; exit zera leases |
| W11 projetada com stale + configuração incapaz | `0` | `20 x busy/60` | stale permanece; high-water/raw state idênticos |
| W11 projetada com stale + mesmo ator/contexto elegível | `1` | `19 x busy/60` | primeiro commit remove stale uma vez, cria W11, cobra winner; exit zera leases |
| cap de W10 + wall W11 + 5.000 cooldowns ainda com 30s | `0` novos atores | `20 x LimiteDeConsultaExcedido/30` | buckets stale ignorados, cooldown union mantém cap; snapshot bruto idêntico |
| export anterior do contexto saiu com `nextAllowedMono=1_020_000` | `1` novo start, page ainda não reservada | page espera exatamente 20s; zero provider call antecipada | nextAllowed persiste entre exports e avança somente no commit da page |

- **Mixed-budget BCI-SP-H (`20x5` cada):** (a) último context-total token, `10 list + 10 detail` de atores distintos/Unifast: exatamente 1 aceita, context `+1`, somente o user bucket do winner `+1`, 19 `LimiteDeConsultaExcedido`, sem partial charge; (b) último user token do mesmo ator, `7 list + 7 detail + 6 export-start`: exatamente 1 aceita, user `+1`; se winner é list/detail, context `+1` e zero leases/cooldown; se export, cooldown+leases e zero context; 19 rejeitam sem delta; (c) último context token com export já admitido, `1 export-page + 9 list + 10 detail`: exatamente 1 reserva; se page vence, context-total/export-share `+1` e zero user; se interactive vence, context-total e winner user `+1`, export-share zero; losers delta zero. O artifact registra winner class e valida o oracle correspondente.
- List/detail aceitos em W10 avançam o mesmo high-water; wall W9 não reabre W10. Export page aceita cobra context-total+export-share mesmo se provider falhar; espera sem token não muta até reserva. Provider pendurado em `deadline-1ms` recebe deadline signal, termina 504 na fronteira, libera leases e produz zero calls posteriores.
- Cobrir também fronteira fixa exata, monotônico antes/exatamente/depois do expiry, wall regression `W10→W9→W10`, wall jump e colisões; o artifact registra fixture, distribuição das operações, clocks, statuses/headers, provider calls, snapshots pre/post-admission/post-exit e `concurrency_policy` separado de `probe_synchronization`.
- Artifact planejado: `foundation_documentation/artifacts/tmp/uninotas-export-pcv/bci-pcv1.json`.

### RLS planned evidence

- **RLS-E2 profile 1 / `load`:** config `maxConcurrency=8`, context `120/min`, user `30/min`; janela alinhada em `W0+1s`; fake provider latency fixa 5ms e páginas determinísticas geram `23MiB..24MiB` por CSV. Stage `4:180s`: export actors `EU/EP` (um/contexto, 200 pages/20k rows) e interactive actors distintos `IU/IP`, alternando list/detail nos segundos ímpares a exatamente 30/min/contexto. Responses dos dois exports ficam retidas até ambas concluírem. Esperado: dois CSVs completos <180s, 90/min máximo de export pages +30/min interativas/contexto, zero erro admitido.
- **RLS-E2 profile 2 / `stress`:** config `maxConcurrency=2`, context `4/min`, user `2/min`; janela alinhada em `W0+1s`; export actor `EU` e interactive actor distinto `IU`; stage `2:185s`: export Unifast de 200 páginas + list/detail nos segundos `1,61,121`; primeira export page é liberada em `t=2s`. Esperado: export inicia pages em `2,22,...,162` (9 calls), deadline signal aborta espera/I/O em 180s, retorna 504 sem CSV, três interativas concluem e leases zeram até 181s.
- **Functional incapable profile:** `maxConcurrency=1` e, separadamente, context rate `1/min` (`exportShare=0`); 100% dos starts retornam busy/60 com zero mutation/provider call. É BCI/contract evidence, não um terceiro RLS-E2 stage.
- **Measurement fixture:** processo Node isolado com `--expose-gc`; GC antes do baseline; baseline é mediana de 5 amostras idle e latência de 100 list/detail calls isoladas no mesmo fake provider; memória amostrada a cada 100ms. `arrayBuffers` é reportado separadamente por ser subconjunto de `external`, nunca somado. Threshold interativo é `p95 <= max(2 x baselineP95, baselineP95 + 25ms)`.
- **Thresholds comuns:** regras BCI; export calls <= share e total calls <= context rate; concurrency <= fórmula global; interactive error rate 0%; output individual <=24MiB; P1 deltas `heapUsed<=128MiB`, `external<=96MiB`, `arrayBuffers<=80MiB`, `rss<=256MiB`; browser Blob é risco separado; cleanup <=1s; zero provider calls após deadline.
- Capturar modo, stages `concurrency:duration`, actors, window offset, provider latency/body, response retention, GC/sampling, request mix/timeline, p50/p95/p99, throughput, statuses, calls por classe/contexto, active/peak, RSS/heap/external/arrayBuffers, bytes e abort/recovery.
- Artifact planejado: `foundation_documentation/artifacts/tmp/uninotas-export-pcv/rls-pcv1.json`.

### Common `pcv-1` artifact rule

- Cada lane em `running|passed` registra evidence object machine-checkable, checkout SHA, profile, config, workload, thresholds, metrics, pass/fail e `artifact_sha256` calculado sobre JSON UTF-8 com chaves recursivamente ordenadas, arrays preservados e sem whitespace, excluindo o próprio hash.

## Required Delivery Gates

- `endpoint-performance-scrutiny`: `required`
- `frontend-race-condition-validation`: `required`
- `runtime-load-stress-validation`: `required`
- `backend-concurrency-idempotency-validation`: `required`
- `security-adversarial-review`: `required`
- `test-quality-audit`: `required`
- `architecture-adherence`: `required`
- `independent-final-review`: `required`
- `audit-protocol-triple-review`: `required as a separate additive gate before Completed`
- `verification-debt-audit`: `required`
- `cutover-integrity-audit`: `required; coordinator cutover retires/delegates legacy consumeBudget/rate maps even without deploy`

## Promotion Finding Routing Ledger

| Finding ID | Severity | Classification | Routing Decision | Same TODO / Split Rationale | Status | Approval / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `REV-01..09` | `high, medium` | `release-blocker` | `same TODO` | contrato original de exportação | `integrated` | reviews R1-R12 |
| `R2-H1..H5,R2-M1..M2` | `high, medium` | `release-blocker` | `same TODO` | budget, audit, guards e gates pertencem ao endpoint | `integrated` | reviews R2-R12 |
| `EX-M01..M03` | `medium` | `release-blocker` | `same TODO` | compatibilidade downloader/auth/audit dentro da feature | `integrated` | reviews R2-R12 |
| `R3-EX-H01,R3-EX-M02,R4-EX-H01,R5-H01..H02,R6-H01/M02` | `high, medium` | `release-blocker` | `same TODO` | admissão, clocks, capacidade e owners pertencem ao endpoint | `integrated` | reviews R3-R12 |
| `R7-AR-H01,R7-AR-M01..M03,R7-CR-H01..H05,R7-CR-M01..M04` | `high, medium` | `release-blocker` | `same TODO` | contratos de paginação, admissão, BCI, módulo e governança | `integrated` | architecture/critique R7-R12 |
| `R8-AR-H01..H02,R8-AR-M01..M03,R8-CR-H01..H02,R8-CR-M01..M04` | `high, medium` | `release-blocker` | `same TODO` | coordinator compartilhado, contrato canônico, BCI/FRC/RLS e transport boundary | `integrated` | architecture/critique R8-R12 |
| `R8-GOV-H03` | `high` | `by-design/no-action` | `challenged` | commit material não pode conter seu próprio SHA; attestation não material referencia baseline e drift prova 0 seções materiais | `challenged_with_rationale` | Review Baseline Freeze + Scope Drift |
| `R9-AR-H01,R9-AR-M01..M02,R9-CR-H1..H5,R9-CR-M1` | `high, medium` | `release-blocker` | `same TODO` | harness, deadline, bounded state, pacing, decisions, FRC/RLS e cutover pertencem à feature | `integrated` | architecture/critique R9-R12 |
| `R10-AR-H01` | `high` | `release-blocker` | `same TODO` | executabilidade do FRC gate obrigatório | `integrated` | architecture R10-R12 |
| `R11-AR-H01,R11-CR-H01,R11-CR-M02` | `high, medium` | `release-blocker` | `same TODO` | fail-closed e destination do FRC gate obrigatório | `integrated` | architecture/critique R11-R12 |
| `logs-csv-hardening` | `medium` | `follow-up-hardening` | `split` | serializer legado em `backend/src/logs/**` está fora deste diff | `deferred` | requer TODO próprio antes do closeout se confirmado pelo security gate |

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Reason:** reviews R12 limpos, aprovação explícita registrada e rebaseline pós-UX verde; implementação serial em andamento.
- **Target after implementation:** `Local-Implemented`, sem deploy.
