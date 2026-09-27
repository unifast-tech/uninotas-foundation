# TODO — Entregar a central React de notas Smart Notas do UniNotas

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Created:** `2026-09-27`
- **Owner:** `Delphi / Operational Coder`, sob autoridade humana do usuário

## Context

O backend local já possui um candidato read-only para listar e detalhar notas Smart Notas por `FiscalIssuerContext`, mas permanece desabilitado e sem deploy. O frontend atual apresenta a projeção legada de `logs` como se ela fosse toda a base de notas. Este corte estabelece a experiência local do UniNotas: notas fiscais da API em `Geral`, erros de integração preservados em `Erros`, contexto fiscal textual e explícito, detalhe fiscal e cache transitório seguro para navegação.

## Framing Source & Story Slice

- **Feature brief:** `artifacts/feature-briefs/uninotas-smart-notas-central.md`
- **Primary story ID:** `ST-03` (subslice React list/detail/cache), incorporando a interação indivisível de `ST-04` (contexto fiscal)
- **Why this is the right current slice:** o usuário precisa navegar pelas notas antes do cutover; lista, detalhe, seletor e cache constituem um único fluxo observável e não exigem ativar produção.
- **Direct-to-TODO rationale:** `n/a — feature brief existente`.

## Contract Boundary

- Este TODO define somente a implementação e validação local do consumidor React.
- O backend continua desabilitado por padrão; deploy, segredo, flag e promoção de ownership pertencem ao TODO de cutover.
- O contrato é bounded but elastic apenas para componentes, hooks, tipos, estilos e testes necessários ao mesmo fluxo `Geral -> detalhe -> Erros -> Geral`.
- Qualquer documento fiscal, mutação, persistência, agregação de contextos ou alteração do contrato HTTP exige outro TODO e nova aprovação.

## Implementation Intent

- **Current delivery:** frontend local com navegação `Geral`/`Erros`, lista e detalhe Smart Notas por um contexto fiscal, filtros publicados, estados completos e cache de sessão stale-while-revalidate.
- **Planned next steps:** cutover backend/frontend conjunto e, em TODOs separados, DANFE/XML e evolução da fila de erros/casos.
- **Anticipatory implementation authorized now:** `none`.
- **Rationale:** entrega a experiência read-only completa sem acoplar a UI a segredos, `idInterno`, payload cru ou `logs` como fonte de notas.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Next exact step:** congelar e publicar o baseline documental para executar o Plan Review antes de solicitar `APROVADO` de implementação.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** o contrato está em refinamento pré-aprovação e nenhum arquivo de produto frontend foi alterado.
- **Exit condition:** Plan Review, guards pré-aprovação e aprovação humana explícita concluídos.

## Provisional Notes

- **Missing for production-ready:** ativação/deploy do backend, ambiente publicado, smoke real dos dois contextos e cutover coordenado.
- **Revisit criteria:** o TODO pode concluir somente como `Local-Implemented, Provisional`; produção pertence ao TODO de cutover.
- **Dependencies unblocked:** o contrato backend local permite tipos, mocks e integração frontend sem ativação externa.

## Scope

- [ ] `SCOPE-01` Reorganizar a navegação autenticada com destinos textuais `Geral` e `Erros`, preservando Equipe, Senha e sessão.
- [ ] `SCOPE-02` Tornar `/` a lista Smart Notas e preservar a lista legada de falhas em `/erros`; manter `/eventos/:refId` para detalhe/tratamento de erro.
- [ ] `SCOPE-03` Expor seletor textual Unifast/Prosperar, sem opção agregada, persistindo o contexto na URL e preservando filtros compatíveis na troca.
- [ ] `SCOPE-04` Consumir `GET /api/v1/notas` com contexto, intervalo, status, documento, idCompra e página; nunca enviar token, CNPJ ou inferir `noteId`.
- [ ] `SCOPE-05` Consumir `GET /api/v1/notas/:noteId` em `/notas/:noteId`, exibindo somente o DTO normalizado e tratando 404/indisponibilidade sem fallback para `logs`.
- [ ] `SCOPE-06` Manter cache em memória acima das rotas, com no máximo 20 chaves, freshness de 60 segundos, retenção stale de 10 minutos e descarte LRU.
- [ ] `SCOPE-07` Deduplicar requisições por chave, abortar/ignorar resposta obsoleta, isolar contexto/filtros/página na chave e limpar tudo sincronicamente no logout/unmount da sessão autenticada.
- [ ] `SCOPE-08` Exibir loading, vazio, stale/revalidando, erro sem cache, erro de revalidação com dados preservados, rate limit e sessão expirada com semântica acessível.
- [ ] `SCOPE-09` Atualizar identidade visível para UniNotas e manter a origem/escopo fiscal textual, sem depender apenas de cor.
- [ ] `SCOPE-10` Criar navegador determinístico com mocks para contexto, lista, detalhe, retorno rápido, resposta atrasada, stale failure, refresh explícito e logout; manter o e2e legado de erros.
- [ ] `SCOPE-11` Atualizar README frontend e consolidar os resultados estáveis no módulo `fiscal-notes-and-documents` sem promover runtime ownership.

## Out of Scope

- DANFE/PDF, XML, relatórios, CSV fiscal, emissão, cancelamento ou qualquer mutação Smart Notas.
- Lista agregada “Todos”, merge de Unifast/Prosperar, polling, webhook ou cache persistente/localStorage/IndexedDB.
- Alteração de endpoint/DTO NestJS, Prisma/PostgreSQL, writer/filter de erros, correlação, `OperationalCase` ou tratamento legado.
- Docker, Railway, domínio, ingresso, segredo, ativação de `SMART_NOTAS_READ_ENABLED`, deploy ou promoção canônica.
- Nova biblioteca de estado/cache ou pacote externo; a necessidade é pequena e específica ao host React atual.
- Worktrees, checkouts auxiliares ou execução paralela de escritores.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `MonitorNotes:delphi-and-foundation`; `uninotas-foundation:main`
- **Promotion lane path:** `n/a neste TODO — termina em Local-Implemented, Provisional`
- **Lane-promoted threshold for this TODO:** `n/a`
- **Production-ready threshold for this TODO:** `n/a — cutover separado`

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| React Smart Notas | `delphi-and-foundation@working-tree` | `n/a` | `n/a` | `n/a` | `Pending` |
| Foundation | `main@5494057` | `n/a` | `n/a` | `pending baseline freeze` | `planning` |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `delphi-and-foundation@5b4f5aeb1ef13b5b810f0b524d12c582954fadbf` | `working_tree` |
| `uninotas-foundation` | `foundation_documentation` | `main@54940576f949adbc0b7074f65eaad2984215dd0e` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `frontend/src/**` | `A,M,??` | UI, adapter, cache, rotas, estados e estilos do fluxo fiscal |
| `MonitorNotes` | `frontend/e2e/notas.mjs` | `A,??` | navegador determinístico do fluxo novo |
| `MonitorNotes` | `frontend/package.json` | `M` | script do e2e fiscal, sem nova dependência |
| `MonitorNotes` | `frontend/README.md` | `M` | contrato operacional e comandos |
| `MonitorNotes` | `uninotas-foundation` | `M` | gitlink documental governado |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-smart-notas-read-frontend.md` | `A,M,??` | contrato e evidência da entrega |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | consolidar consumidor local candidato |
| `uninotas-foundation` | `todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md` | `M` | registrar handoff frontend |
| `uninotas-foundation` | `artifacts/publication-manifest.txt` | `M` | publicar o TODO governado |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/**` | `any` | backend já entregue e fora deste corte |
| `MonitorNotes` | `Dockerfile` | `any` | runtime fora do escopo |
| `MonitorNotes` | `docker-compose.yml` | `any` | runtime fora do escopo |
| `MonitorNotes` | `frontend/package-lock.json` | `any` | nenhuma dependência nova planejada |
| `uninotas-foundation` | `project_constitution.md` | `any` | nenhuma mudança constitucional |
| `uninotas-foundation` | `policies/scope_subscope_governance.md` | `any` | ownership não é promovido aqui |
| `uninotas-foundation` | `deterministic/**` | `any` | guardas não mudam neste corte |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / agent defense | Decision | User validation / renewed approval |
| --- | --- | --- | --- | --- |
| alterações backend e closeout Foundation já presentes | `pre-existing package from completed backend TODO` | TODO backend concluído como `Local-Implemented`; nenhum arquivo frontend foi tocado | exigir checkpoint/baseline separado antes da implementação frontend | `pending` |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** pequenos componentes/hooks/tipos/test fixtures necessários ao mesmo fluxo e correções locais de acessibilidade/estilo.
- **Must update or split the TODO:** documento fiscal, mutação, novo backend, persistência, agregação, nova dependência, deploy ou ownership.

## Definition of Done

- [ ] `DOD-01` Usuário autenticado navega por `Geral` e `Erros`; o legado continua funcional em `/erros` e `/eventos/:refId`.
- [ ] `DOD-02` Geral lista notas do contexto textual selecionado com filtros/paginação compatíveis e sem dados cruzados.
- [ ] `DOD-03` Detalhe fiscal abre por `noteId` opaco e nunca expõe/decodifica `idInterno`, token ou CNPJ.
- [ ] `DOD-04` Cache cumpre cap/TTL/stale/LRU, sobrevive a troca de rota, isola chaves e é eliminado no logout.
- [ ] `DOD-05` Respostas atrasadas/abortadas não substituem o contexto ou a consulta ativa; chamadas idênticas em voo são deduplicadas.
- [ ] `DOD-06` Estados loading, vazio, revalidando, stale-error, erro sem cache, 429 e sessão expirada são distinguíveis e acessíveis.
- [ ] `DOD-07` Refresh explícito sempre chama a API; retorno rápido usa cache válido e stale revalida em segundo plano.
- [ ] `DOD-08` UI é responsiva, navegável por teclado e identifica contexto/status também por texto.
- [ ] `DOD-09` Build/lint passam e o navegador determinístico cobre os fluxos novos sem quebrar o e2e legado.
- [ ] `DOD-10` Documentação registra o candidato local sem ativar runtime, segredo ou capability ownership.

## Validation Steps

- [ ] `VAL-01` Executar `npm run lint && npm run build` em `frontend/`.
- [ ] `VAL-02` Executar e2e fiscal mockado com Chromium via script `npm run e2e:notas`.
- [ ] `VAL-03` Executar e2e legado read-only aplicável ou registrar blocker objetivo quando o runtime local de erros não estiver disponível.
- [ ] `VAL-04` Executar auditoria React/Vite, validação de races frontend, revisão de acessibilidade e busca por segredo/PII/decodificação de `noteId`.
- [ ] `VAL-05` Executar Foundation validator, guards de TODO e `git diff --check`.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-01..DOD-09` | `Definition of Done` | fluxos React observáveis | `navigation/browser+build` | `frontend/e2e/notas.mjs`; `npm run e2e:notas`; build/lint | `local browser` | `planned` | mocks determinísticos e sem segredo |
| `DOD-10` | `Definition of Done` | canon candidato sem promoção | `doc+guard` | módulo + Foundation validator | `local` | `planned` | ownership permanece target-planned |
| `VAL-01` | `Validation Steps` | lint/build | `command` | `npm run lint && npm run build` | `local` | `planned` | owning manifest frontend |
| `VAL-02` | `Validation Steps` | fluxo fiscal | `navigation/browser` | `npm run e2e:notas` | `local browser` | `planned` | cobre races/cache/contextos |
| `VAL-03` | `Validation Steps` | não regressão legado | `navigation/browser` | `npm run e2e` ou blocker documentado | `local browser/API` | `planned` | depende de runtime legado |
| `VAL-04` | `Validation Steps` | arquitetura/races/a11y/segurança | `audit` | ferramentas Delphi + revisão | `local` | `planned` | obrigatório antes de closeout |
| `VAL-05` | `Validation Steps` | governança/diff | `guard` | validator + guards + diff check | `local` | `planned` | obrigatório |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas real | necessário apenas no cutover, não no e2e local | `healthy` | `2026-09-27` | probes backend redatados já concluídos | usar mocks contratuais neste TODO |
| Chromium | navegador do Playwright | `unknown` | `n/a` | resolver `CHROME` antes do gate | bloquear somente evidência browser, não codificação |
| Backend local fiscal | contrato existe, flag desabilitada | `healthy` | `2026-09-27` | 223 testes/build/lint backend | mocks no frontend; smoke real no cutover |

## Profile Scope & Handoffs

- **Primary execution profile:** `operational-coder`
- **Active technical scope:** `react,vite`
- **Expected supporting profiles:** `assurance-tester-quality`
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `operational-coder` | `assurance-tester-quality` | auditoria obrigatória dos testes e races | testes/e2e/cache | `planned` |
| `operational-coder` | `operational-devops` | ativação/deploy não pertence ao frontend | cutover Smart Notas | `deferred to TODO-uninotas-smart-notas-read-cutover.md` |

## Complexity

- **Level:** `medium`
- **Checkpoint policy:** `one checkpoint before approval; delivery reviews after implementation`
- **Why this level:** fluxo crítico com rotas, cache assíncrono, isolamento entre dois contextos e navegador, mas sem schema, escrita ou deploy.

## Canonical Module Anchors

- **Primary module doc:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Secondary module docs:** `foundation_documentation/modules/events-and-classification.md`; `foundation_documentation/modules/identity-and-team.md`
- **Planned decision promotion targets:** `fiscal-notes-and-documents#Cross-Module Considerations`
- **Module decision consolidation targets:** `fiscal-notes-and-documents#Purpose, Owned Entities, and Workflows` e `#Invariants`

## Decision Pending

- [ ] `none — recomendações abaixo serão congeladas somente após Review Baseline Freeze e aprovação`.

## Decisions (Resolved Before Freeze)

- [x] `D-01` `/` é Geral Smart Notas; `/erros` preserva a fila legada; detalhes permanecem separados em `/notas/:noteId` e `/eventos/:refId`. Ref: feature brief ST-03/ST-04.
- [x] `D-02` `contexto=unifast|prosperar` vive na URL, default `unifast`, sem agregado; troca mantém datas/status/documento/idCompra e volta à página 1. Ref: module invariant.
- [x] `D-03` intervalo default são os últimos 30 dias corridos incluindo hoje, em `YYYY-MM-DD`, calculados localmente e materializados na URL; máximo 365 dias. Ref: backend query contract.
- [x] `D-04` cache: 20 chaves LRU, fresh 60 s, stale retido 10 min; primeiro load/hard refresh consulta API, refresh explícito sempre consulta, stale revalida. Ref: SD-08/G-20.
- [x] `D-05` cache key inclui usuário da sessão, contexto, datas, status, documento, idCompra e página; logout desmonta o provider, aborta requests e limpa entradas. Ref: race matrix da descoberta.
- [x] `D-06` nenhuma biblioteca nova; adapter e cache host-specific usam React e Web APIs já disponíveis. Ref: package-first sem resultados.
- [x] `D-07` erros de integração permanecem legados e não são mesclados em linhas/notas neste corte. Ref: ownership de módulos.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `fiscal-notes-and-documents#Invariants` | Smart Notas é fonte exclusiva; um contexto por request; sem payload bruto | `Preserve` | módulo canônico |
| `events-and-classification#Specification` | `/eventos` continua projeção atual de erros/eventos | `Preserve` | módulo canônico |
| `identity-and-team#Observed Authentication Contract` | JWT/perfis atuais protegem leitura | `Preserve` | módulo canônico |

## Decision Baseline (Frozen Before Implementation)

- [x] `D-01..D-07` congeladas como baseline de planejamento; implementação continua proibida até review convergir e `APROVADO`.

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** estabelece o novo steady-state da UI de notas e separa a lista fiscal da fila de erros hoje misturadas.
- **Deviation / debt being retired:** tratar a projeção `logs` como catálogo completo de notas e manter cache preso ao componente desmontável.
- **Target steady-state after closeout:** Geral API-only por contexto; Erros logs-only; cache transitório de sessão acima das rotas.
- **Temporary exceptions allowed:** backend desabilitado até cutover; nenhuma fallback/dual-read.
- **Cutover / removal condition:** ativação coordenada pelo TODO de cutover; `/eventos` permanece para erros.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| autoridade e estado separados | module invariants + `D-01/D-07` | rotas/adapters | evita sucesso derivado de logs |
| cache session-only isolado | `D-04/D-05` | provider/hook | evita vazamento e autoridade concorrente |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| fallback `/notas -> /eventos` | adapter/import/test scan | corrompe source ownership | `none` |
| cache global persistente ou sem contexto | storage/API scan e race e2e | mistura emissores/usuários | `none` |
| efeito async sem cancelamento | race audit | resposta velha pode trocar tela | `none` |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| browser test | frontend | `npm run e2e:notas` | contexto, cache, stale e races | `implement-in-this-todo` | DOD-04..DOD-08 |
| build/typecheck | frontend | `npm run lint && npm run build` | contrato/tipos/efeitos inválidos | `already-enforced` | VAL-01 |
| audit | frontend | `frontend-race-condition-validation` | stale response/cleanup/dedupe | `implement-in-this-todo` | VAL-04 |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after baseline freeze and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** `pending baseline freeze`
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending implementation`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** TODO medium architecture-corrective deve ser revisado a partir de baseline imutável.
- **Trigger stage:** `before first planning review`
- **Baseline branch:** `uninotas-foundation:main`
- **Baseline commit:** `983ac0c2e0ff24e1ef5e58100bef0bb5b9ab1cbc`
- **Baseline push reference:** `origin/main@983ac0c2e0ff24e1ef5e58100bef0bb5b9ab1cbc`
- **Gate status:** `no_material_findings`
- **Findings summary:** baseline documental commitado e publicado; revisões devem usar este checkpoint como origem.
- **Evidence / reference:** `uninotas-foundation:main@983ac0c2e0ff24e1ef5e58100bef0bb5b9ab1cbc`; `origin/main` confirmado no mesmo SHA em 2026-09-27.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** mudanças pós-review podem alterar cache/rotas/risco.
- **Trigger stage:** `after planning review and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `canonical template set`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-frontend.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Questions To Close

- [ ] `none — D-01..D-07 expressam as recomendações técnicas propostas para aprovação`.

## Package-First Assessment

- **Queries:** `query_packages.sh --search "react cache fiscal notes"`; `query_packages.sh --stack node`
- **Relevant packages found:** `none`
- **READMEs read:** `frontend/README.md`
- **Decision:** implementação host-specific sem nova dependência.
- **Tier:** `Local host application`
- **Rationale:** cache curto e adapter são específicos ao contrato UniNotas; nenhuma capacidade proprietária foi encontrada.

## Frontend / Consumer Matrix

| Producer Surface | Consumer Surface | Planned State | Evidence / Guardrail |
| --- | --- | --- | --- |
| `GET /api/v1/notas` | `/`, `ListaNotas`, cache/session provider | `consumer planned in this TODO` | tipos exatos + browser list/context/cache |
| `GET /api/v1/notas/:noteId` | `/notas/:noteId`, `DetalheNota` | `consumer planned in this TODO` | rota opaca + browser detail/404 |
| `GET /api/v1/eventos*` | `/erros`, `/eventos/:refId` | `existing consumer preserved` | e2e legado e route-scoped hooks |
| `GET /api/v1/eventos/stream` | somente shell/rota de erros | `existing consumer narrowed to legacy area` | scan estrutural + e2e; Geral não abre SSE |
| Smart Notas credentials/CNPJ | nenhum consumidor frontend | `consumer intentionally absent` | env/import/bundle scan; backend-only invariant |

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | DTO backend local é o contrato consumidor | testes `fiscal-notes.contract.spec.ts` | atualizar tipos e mocks antes de execução | `High` | `Keep as Assumption` |
| `A-02` | todos os perfis ativos podem ler ambos contextos | decisão do usuário + backend guards | revisar UI/autorizações | `High` | `Keep as Assumption` |
| `A-03` | cutover não ocorrerá dentro deste TODO | TODO separado ativo | reclassificar para cross-stack/devops | `High` | `Keep as Assumption` |

## Execution Plan

### Touched Surfaces

- `frontend/src/api`, `frontend/src/contextos`, `frontend/src/hooks`, `frontend/src/componentes`, `frontend/src/paginas`, `frontend/src/estilos`, `frontend/e2e`, frontend README/manifest e módulo/TODO Foundation.

### Ordered Steps

1. Criar e2e fiscal fail-first com mocks dos envelopes backend e cenários de race/cache.
2. Criar tipos/adapter fiscal sem alterar o cliente HTTP além de suporte a `AbortSignal` necessário.
3. Criar provider/cache de sessão e hook com dedupe, abort, TTL/stale/LRU e limpeza.
4. Criar lista, filtros, contexto, paginação e estados acessíveis.
5. Criar detalhe fiscal read-only e integrar rotas/navegação/cabeçalho; mover resumo/SSE/gatilho para o shell legado de erros para que `Geral` não consulte `/eventos` nem abra stream.
6. Ajustar estilos responsivos e identidade UniNotas.
7. Rodar auditorias/testes/build/browser; consolidar módulo e evidências.

### Test Strategy

- **Strategy:** `test-first`
- **Why:** cache e troca rápida de contexto têm falhas observáveis difíceis de provar por inspeção.
- **Fail-first targets:** contexto correto, retorno `Geral -> Erros -> Geral`, resposta fora de ordem, stale failure, refresh, logout e detalhe.

### Pre-APROVADO RED Evidence Capture

- **Decision:** `not_needed`
- **Why now:** não é bugfix; criar teste antes de aprovação seria implementação de feature.
- **Target symptom:** `n/a`
- **Allowed surfaces:** `none`
- **Forbidden surfaces reaffirmed:** `production code|runtime/config/deploy|canonical project docs outside TODO authoring`
- **Planned command / target:** `n/a`
- **Status:** `not_run`
- **Findings summary:** `n/a`

### Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Geral/contexto/filtros/detalhe | UI crítica | `web-only` | `Playwright readonly` | `no` | `no` | `e2e/notas.mjs` com mocks contratuais | `n/a` |
| cache/stale/race/logout | estado assíncrono visível/privado | `web-only` | `Playwright readonly` | `no` | `no` | delays/falhas controlados no navegador | `n/a` |
| Erros legado | navegação preservada | `web-only` | `Playwright readonly` | `no` | `yes` | `npm run e2e` quando runtime disponível | mutações legadas não são alteradas |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| frontend type/build | React/Vite mudam | tipos, bundle, imports | `npm ci` já disponível | `npm run lint && npm run build` | `Local-Implemented` | `planned` | command output | sem inferir deploy |
| frontend fiscal browser | fluxo novo | lista/detalhe/contexto/cache/races/a11y | Chromium + mocks | `npm run e2e:notas` | `Local-Implemented` | `planned` | runner output/screens | read-only |
| frontend legacy browser | rotas movidas | login/erros/detalhe/tratamento | API local + usuário de teste | `npm run e2e` | `Local-Implemented` | `planned` | runner output ou blocker | não usar produção |
| Foundation | docs/TODO | árvore/contratos | nenhum | `python3 deterministic/validate_foundation.py --root .` | `Local-Implemented` | `planned` | command output | executar no submodule |

### Runtime / Rollout Notes

- Entrega local apenas. Backend continua feature-flagged off; nenhum domínio publicado ou segredo é necessário para os mocks. Smoke real fica no cutover.

## Plan Review Gate

### Review Sections

- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

### Issue Cards

- **Issue ID:** `ARCH-01`
  - **Severity:** `high`
  - **Evidence:** `frontend/src/App.tsx` monta `useResumo` e `useTempoReal` globalmente; `frontend/src/componentes/Cabecalho.tsx` exige `Resumo`.
  - **Why it matters now:** trocar apenas a rota raiz manteria consultas/SSE de `logs` na tela Geral, ocultando acoplamento e aumentando carga.
  - **Option A (Recommended):** tornar o cabeçalho independente do resumo e encapsular resumo/SSE/gatilho em um shell legado montado apenas em `/erros` e `/eventos/:refId`.
    - **Effort:** `medium`; **Risk:** `low`; **Blast radius:** `module`; **Maintenance burden:** `low`; **Performance impact:** `improves`; **Elegance impact:** `improves`; **Structural soundness impact:** `improves`.
  - **Option B (Alternative):** manter hooks globais e ocultar indicadores em Geral.
    - **Effort:** `low`; **Risk:** `high`; **Blast radius:** `cross-module`; **Maintenance burden:** `high`; **Performance impact:** `regresses`; **Elegance impact:** `regresses`; **Structural soundness impact:** `regresses`.
  - **Option C (Do Nothing):** manter `/` como legado e criar Geral em rota secundária.
    - **Effort:** `low`; **Risk:** `medium`; **Blast radius:** `module`; **Maintenance burden:** `medium`; **Performance impact:** `neutral`; **Elegance impact:** `regresses`; **Structural soundness impact:** `regresses`.
  - **Recommendation:** `Integrate Option A`; preserva a separação de fontes também no comportamento de rede.
- **Issue ID:** `ARCH-02`
  - **Severity:** `medium`
  - **Evidence:** `frontend/src/hooks/useFiltros.ts` mistura parsing, defaults e escrita de query; novo backend exige datas canônicas antes do request.
  - **Why it matters now:** normalização em effects pode gerar request duplo/loop e chaves de cache semanticamente duplicadas.
  - **Option A (Recommended):** criar parser/normalizador fiscal puro e bloquear a busca até a URL canônica ser aplicada com `replace`.
    - **Effort:** `medium`; **Risk:** `low`; **Blast radius:** `local`; **Maintenance burden:** `low`; **Performance impact:** `improves`; **Elegance impact:** `improves`; **Structural soundness impact:** `improves`.
  - **Option B (Alternative):** defaults implícitos fora da URL.
    - **Effort:** `low`; **Risk:** `medium`; **Blast radius:** `local`; **Maintenance burden:** `medium`; **Performance impact:** `neutral`; **Elegance impact:** `neutral`; **Structural soundness impact:** `neutral`.
  - **Option C (Do Nothing):** iniciar fetch e corrigir URL depois.
    - **Effort:** `low`; **Risk:** `high`; **Blast radius:** `module`; **Maintenance burden:** `high`; **Performance impact:** `regresses`; **Elegance impact:** `regresses`; **Structural soundness impact:** `regresses`.
  - **Recommendation:** `Integrate Option A`; garante uma única identidade para URL, request e cache.

### Failure Modes & Edge Cases

- [ ] resposta Unifast chega depois da troca para Prosperar; cache não pode atualizar a tela ativa.
- [ ] retorno rápido usa cache correto; falha de revalidação mantém dados com aviso e timestamp.
- [ ] request idêntico em voo é compartilhado; refresh explícito não cria storm.
- [ ] logout durante request aborta/ignora resultado e apaga cache.
- [ ] 401 encerra sessão; 404 detalhe é vazio específico; 429 oferece retry explícito sem loop.
- [ ] status fiscal desconhecido é exibido como texto seguro, não descartado.
- [ ] URL inválida é normalizada sem loop e respeita limite de 365 dias.
- [ ] Geral não abre `/eventos`, `/eventos/resumo`, `/eventos/produtos` nem SSE; esses consumidores só vivem no shell legado.

### Residual Unknowns / Risks

- [ ] Chromium e runtime legado precisam ser resolvidos antes da evidência final.
- [ ] Provider page size é controlado externamente; UI deve confiar em `perPage/totalPages` retornados.

## Additional Architectural Opinions

- **Needed:** `yes`
- **Why ambiguity remains:** architecture-corrective e fluxo crítico com cache/races.
- **Opinion count:** `1`
- **Package mode:** `bounded-file-set`
- **Internal reviewer mandate:** `required after baseline freeze`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-frontend.md`
- **Latest TEACH evidence / artifact:** `pending baseline freeze`

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | cache/rotas/browser |
| `blast_radius` | `cross-module` | notas, erros e identidade visual/navegação |
| `behavioral_change_or_bugfix` | `yes` | nova experiência principal |
| `changes_public_contract` | `yes` | rotas UI públicas autenticadas mudam |
| `touches_auth_or_tenant` | `yes` | limpeza de cache no ciclo de sessão; sem tenancy |
| `touches_runtime_or_infra` | `no` | local only |
| `touches_tests` | `yes` | novo e2e e ajuste do legado |
| `critical_user_journey` | `yes` | fluxo central do UniNotas |
| `release_or_promotion_critical` | `yes` | prazo de entrega e cutover dependente |
| `high_severity_plan_review_issue` | `no` | ainda sem finding high |
| `explicit_three_lane_request` | `no` | não solicitado |

## Approval

- **Status:** `not_requested`
- **Approved by:** `n/a`
- **Approval reference:** `n/a`
- **Implementation authority:** `none until explicit APROVADO after gates`

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `rule-react-react-architecture-always-on` | React UI/state/effects/a11y | render puro, ownership único, estados/a11y explícitos | mutação em render, estado duplicado, effect sem cleanup | ingestão binding após aprovação; orientar componentes/hooks |
| `wf-react-change-ui-boundary-method` | rotas/componentes/hooks | comportamento observável e adapter isolado | acoplamento da UI ao provider/segredo | seguir passos e evidence lanes |
| `rule-vite-vite-build-runtime-always-on` | build/env/assets | manifest/scripts e env público restrito | tratar proxy/preview como produção ou expor segredo | build reproduzível; nenhuma env fiscal no cliente |
| `wf-vite-change-build-runtime-boundary-method` | bundle/runtime boundary | separação dev proxy/produção | claim de deploy neste TODO | validar apenas build local |
| `frontend-race-condition-validation` | cache/races/logout | chave completa, cancelamento, stale controlado, limpeza | last-response-wins e cache cross-session | FRC requerido antes de Local-Implemented |
| `test-creation-standard` | e2e behavior-defining | assertions observáveis e fixtures determinísticas | teste que apenas espelha implementação | teste fail-first e audit obrigatório |

## Security Risk Assessment

- **Risk level:** `medium`
- **Why this risk level:** dados fiscais autenticados ficam transitoriamente em memória e devem ser eliminados ao logout; nenhum segredo/PII novo deve ser exposto.
- **Attack surface in scope:** JWT client, URL params, noteId opaco, cache por sessão/contexto e mensagens de erro.
- **Attack simulation decision:** `required`
- **Review evidence:** `pending`
- **Residual security risk:** backend desabilitado até cutover.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `medium`
- **Why this level:** lista retriggerable com cache SWR, troca rápida de contexto e chamadas externas indiretamente caras.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `not_needed` | `low` | `EPS-DATA-PATH-CHANGED` | `before_local_implemented` | `EPS-E1` | `not_applicable` | `frontend não muda endpoint` | `none` |
| `FRC` | `frontend-race-condition-validation` | `required` | `high` | `FRC-STALE-RESPONSE` | `before_local_implemented` | `FRC-E2` | `pending` | `none` | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `BCI-DUPLICATE-SUBMIT-OR-REPLAY` | `before_local_implemented` | `BCI-POLICY` | `not_applicable` | `sem backend/write` | `none` |
| `RLS` | `runtime-load-stress-validation` | `recommended` | `medium` | `RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED` | `before_local_implemented` | `RLS-E1` | `pending` | `browser memory/request budget` | `none` |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** medium, cross-module, rota pública autenticada e critical journey.
- **Critique status:** `not_run`
- **Evidence / reference:** `pending baseline freeze`

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-frontend.md`
- **Gate status:** `not_run`
- **Evidence / reference:** `pending baseline freeze/review`

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** testes behavior-defining e critical journey.
- **Audit status:** `not_run`
- **Evidence / reference:** `pending implementation`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** medium cross-module com rota/autenticação/cache.
- **Final review status:** `not_run`
- **Evidence / reference:** `pending implementation`

## Dedicated Triple Review Audit Gate

- **Audit decision:** `required`
- **Why this decision:** audit floor classificou o fluxo como critical journey e release-sensitive.
- **Canonical protocol:** `audit-protocol-triple-review`
- **Lifecycle:** `delivery-side; additive à crítica e ao final review`
- **Audit status:** `not_run`
- **Evidence / reference:** `pending implementation`

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `recommended`
- **Why this decision:** separa Geral API-only de Erros logs-only sem retirar o legado.
- **Cutover signals in scope:** `legacy-path separation; no fallback bridge`
- **Cutover audit status:** `not_run`
- **Evidence / reference:** `pending implementation`

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| frontend diff + tests | races, auth cache, routes, a11y, contract | `planned` | `pending` | `none yet` | `pending implementation` |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| React/Vite/source authority | effect bypass, stale writes, persistent cache, logs fallback, secret env | `planned` | `pending` | `none yet` | `pending implementation` |

## Verification Debt Assessment

- **Audit outcome:** `pending`
- **Why this outcome:** execução ainda não começou.
- **Inline code TODO debt:** `pending`
- **Evidence / audit artifact:** `pending`
- **Accepted residual debt:** `none planned`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** contrato ainda precisa de baseline freeze, reviews e aprovação antes de implementação.
- **Post-commit/push status:** `pending`
- **Next path/status action:** publicar baseline Foundation, concluir planning gates e solicitar `APROVADO`.

## Module Consolidation Gate

- [ ] módulo fiscal atualizado com o consumidor local candidato.
- [ ] decisões estáveis D-01..D-07 consolidadas sem promover ownership.
- [ ] cross-links e caminho final do TODO atualizados.

## Commands (Run Locally)

- `python3 delphi-ai/tools/node_capability_surface_audit.py --repo frontend --expect react --manifest package.json --require-script build --require-script lint --require-script e2e`
- `python3 delphi-ai/tools/node_capability_surface_audit.py --repo frontend --expect vite --manifest package.json --require-script build --require-script lint`
- `cd frontend && npm run lint && npm run build && npm run e2e:notas`
- `python3 foundation_documentation/deterministic/validate_foundation.py --root foundation_documentation`

## Files Expected

- Use `Diff Expectation Contract` como inventário autoritativo.
