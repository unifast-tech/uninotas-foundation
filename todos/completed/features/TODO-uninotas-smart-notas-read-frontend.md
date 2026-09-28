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

- **Current delivery stage:** `Local-Implemented`
- **Qualifiers:** `Provisional`
- **Next exact step:** executar o TODO de cutover sob sua própria autoridade antes de qualquer ativação/deploy ou smoke real.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `completed`
- **Why this state now:** implementação, suíte local, browser interceptado, auditoria tripla, segurança, aderência arquitetural e guards finais estão concluídos.
- **Exit condition:** alcançada em 2026-09-27 com o movimento para `completed/features/`, sem promover runtime.

## Provisional Notes

- **Missing for production-ready:** ativação/deploy do backend, ambiente publicado, smoke real dos dois contextos e cutover coordenado.
- **Revisit criteria:** o TODO pode concluir somente como `Local-Implemented, Provisional`; produção pertence ao TODO de cutover.
- **Dependencies unblocked:** o contrato backend local permite tipos, mocks e integração frontend sem ativação externa.

## Scope

- [x] `SCOPE-01` Reorganizar a navegação autenticada com destinos textuais `Geral` e `Erros`, preservando Equipe, Senha e sessão.
- [x] `SCOPE-02` Tornar `/` a lista Smart Notas e preservar a lista legada de falhas em `/erros`; manter `/eventos/:refId` para detalhe/tratamento de erro.
- [x] `SCOPE-03` Expor seletor textual Unifast/Prosperar, sem opção agregada; persistir na URL apenas contexto, datas, status e página, mantendo `documento` e `idCompra` em estado efêmero da sessão autenticada.
- [x] `SCOPE-04` Consumir `GET /api/v1/notas` com contexto, intervalo, status, documento, idCompra e página; nunca enviar ao cliente credenciais/CNPJ configurado do emissor nem inferir `noteId`.
- [x] `SCOPE-05` Consumir `GET /api/v1/notas/:noteId` em `/notas/:noteId`, exibindo somente o DTO normalizado e tratando 404/indisponibilidade sem fallback para `logs`.
- [x] `SCOPE-06` Manter cache em memória acima das rotas, com no máximo 20 chaves, freshness de 60 segundos, retenção stale de 10 minutos e descarte LRU.
- [x] `SCOPE-07` Deduplicar requisições por chave, tratar abort como cancelamento não exibível, impedir commits tardios por geração de request/sessão, isolar contexto/filtros/página na chave e limpar tudo sincronicamente no logout/unmount da sessão autenticada.
- [x] `SCOPE-08` Exibir loading, vazio, stale/revalidando, erro sem cache, erro de revalidação com dados preservados, rate limit e sessão expirada com semântica acessível.
- [x] `SCOPE-09` Atualizar identidade visível para UniNotas e manter a origem/escopo fiscal textual, sem depender apenas de cor.
- [x] `SCOPE-10` Criar navegador determinístico com mocks para contexto, lista, detalhe, retorno rápido, resposta atrasada, stale failure, refresh explícito, logout, rotas legadas e ciclo resolver/reabrir com PATCH interceptado; preservar o runner legado real como ferramenta opcional e fail-closed.
- [x] `SCOPE-11` Atualizar README frontend e consolidar os resultados estáveis no módulo `fiscal-notes-and-documents` sem promover runtime ownership.

## Out of Scope

- DANFE/PDF, XML, relatórios, CSV fiscal, emissão, cancelamento ou qualquer mutação Smart Notas.
- Lista agregada “Todos”, merge de Unifast/Prosperar, polling, webhook ou cache persistente/localStorage/IndexedDB.
- Alteração de endpoint/DTO NestJS, Prisma/PostgreSQL, writer/filter de erros, correlação, `OperationalCase` ou tratamento legado.
- Docker, Railway, domínio, ingresso, segredo, ativação de `SMART_NOTAS_READ_ENABLED`, deploy ou promoção canônica.
- Nova biblioteca de estado/cache ou pacote de runtime; somente o lint oficial/dev-only de React Hooks pode ser adicionado para tornar o gate de effects real.
- Worktrees, checkouts auxiliares ou execução paralela de escritores.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `MonitorNotes:delphi-and-foundation`; `uninotas-foundation:main`
- **Promotion lane path:** `n/a neste TODO — termina em Local-Implemented, Provisional`
- **Lane-promoted threshold for this TODO:** `n/a`
- **Production-ready threshold for this TODO:** `n/a — cutover separado`

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| React Smart Notas | `delphi-and-foundation@working-tree` | `n/a` | `n/a` | `n/a` | `Local-Implemented, Provisional` |
| Foundation | `main@working-tree` | `n/a` | `n/a` | `origin/main@0b36337` | `local closeout documentation` |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `delphi-and-foundation@5b4f5aeb1ef13b5b810f0b524d12c582954fadbf` | `working_tree` |
| `uninotas-foundation` | `foundation_documentation` | `main@0b36337ed963348aa112be29416b4b5b99cb7ce5` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `frontend/src/**` | `A,M,??` | UI, adapter, cache, rotas, estados e estilos do fluxo fiscal |
| `MonitorNotes` | `frontend/e2e/notas.mjs` | `A,??` | navegador determinístico do fluxo novo |
| `MonitorNotes` | `frontend/e2e/notas-unit.ts` | `A,??` | invariantes determinísticas de parser, DTO, cache, timers, LRU e privacidade |
| `MonitorNotes` | `frontend/e2e/notas-race.ts` | `A,??` | runner determinístico para bursts de dedupe, detach e limpeza de sessão |
| `MonitorNotes` | `frontend/e2e/fluxo.mjs` | `M` | apontar o fluxo legado para `/erros` e exigir autorização explícita para mutação |
| `MonitorNotes` | `frontend/package.json` | `M` | scripts do e2e/lint e dependências dev-only do React Hooks lint |
| `MonitorNotes` | `frontend/package-lock.json` | `M` | lockfile do lint dev-only de React Hooks aprovado no plano |
| `MonitorNotes` | `frontend/eslint.config.js` | `A,??` | configuração flat restrita a TypeScript/React/Hooks e zero suppressions novas |
| `MonitorNotes` | `frontend/vite.config.ts` | `M` | atestação dev-only da topologia local descartável antes do runner mutável opcional |
| `MonitorNotes` | `frontend/README.md` | `M` | contrato operacional e comandos |
| `MonitorNotes` | `artifacts/tmp/uninotas-frontend-race*/**` | `A,??` | evidência local determinística gerada pelos probes de race deste corte |
| `MonitorNotes` | `backend/**` | `A,M,??` | pacote backend preexistente do TODO concluído, preservado sem modificação e aprovado como desvio de baseline |
| `MonitorNotes` | `uninotas-foundation` | `M` | gitlink documental governado |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-smart-notas-read-frontend.md` | `A,M,D,??` | contrato/evidência e remoção governada no closeout |
| `uninotas-foundation` | `todos/completed/features/TODO-uninotas-smart-notas-read-frontend.md` | `A,M,??` | destino governado do mesmo TODO concluído |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | consolidar consumidor local candidato |
| `uninotas-foundation` | `todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md` | `M` | registrar handoff frontend |
| `uninotas-foundation` | `artifacts/publication-manifest.txt` | `M` | publicar o TODO governado |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `Dockerfile` | `any` | runtime fora do escopo |
| `MonitorNotes` | `docker-compose.yml` | `any` | runtime fora do escopo |
| `uninotas-foundation` | `project_constitution.md` | `any` | nenhuma mudança constitucional |
| `uninotas-foundation` | `policies/scope_subscope_governance.md` | `any` | ownership não é promovido aqui |
| `uninotas-foundation` | `deterministic/**` | `any` | guardas não mudam neste corte |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / agent defense | Decision | User validation / renewed approval |
| --- | --- | --- | --- | --- |
| alterações backend já presentes no checkout raiz | `pre-existing package from completed backend TODO` | TODO backend concluído como `Local-Implemented`; execução frontend não alterou esses arquivos | excluir do pacote frontend e preservar sem modificação | `APROVADO humano posterior à divulgação do baseline sujo` |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** pequenos componentes/hooks/tipos/test fixtures necessários ao mesmo fluxo e correções locais de acessibilidade/estilo.
- **Must update or split the TODO:** documento fiscal, mutação, novo backend, persistência, agregação, nova dependência, deploy ou ownership.

## Definition of Done

- [x] `DOD-01` Usuário autenticado navega por `Geral` e `Erros`; volta à última URL fiscal canônica sem perder cache e o legado continua funcional, inclusive resolver/reabrir mockado, em `/erros` e `/eventos/:refId`.
- [x] `DOD-02` Geral lista notas do contexto textual selecionado com filtros/paginação compatíveis e sem dados cruzados.
- [x] `DOD-03` Detalhe fiscal abre por `noteId` opaco, usa allowlist do DTO público, mascara chaves de acesso e nunca expõe/decodifica `idInterno`, token ou CNPJ configurado do emissor.
- [x] `DOD-04` Cache cumpre cap/TTL/stale/LRU, sobrevive a troca de rota, isola chaves e é eliminado no logout.
- [x] `DOD-05` Respostas atrasadas/abortadas não substituem o contexto ou a consulta ativa; chamadas idênticas em voo são deduplicadas.
- [x] `DOD-06` Estados loading, vazio, revalidando, stale-error, erro sem cache, 429 e sessão expirada são distinguíveis e acessíveis.
- [x] `DOD-07` Refresh explícito garante uma requisição upstream: inicia uma quando não há outra idêntica em voo e compartilha/desabilita enquanto ela está pendente; retorno rápido usa cache válido e stale revalida uma única vez em segundo plano.
- [x] `DOD-08` UI é responsiva, navegável por teclado e identifica contexto/status também por texto.
- [x] `DOD-09` Build/lint passam; o navegador determinístico cobre os fluxos novos e as rotas legadas; o runner mutável legado aponta para `/erros` e falha fechado sem autoridade explícita.
- [x] `DOD-10` Documentação registra o candidato local sem ativar runtime, segredo ou capability ownership.

## Validation Steps

- [x] `VAL-01` Executar `npm run lint && npm run build` em `frontend/`.
- [x] `VAL-02` Executar e2e fiscal mockado com Chromium via script `npm run e2e:notas`.
- [x] `VAL-03` Executar navegação, detalhe e ciclo resolver/reabrir legados com GET/PATCH interceptados dentro de `npm run e2e:notas`; não executar o runner real `npm run e2e` sem fixture descartável, runtime local controlado e autoridade explícita (`AUTORIZAR_MUTACAO=1`).
- [x] `VAL-04` Executar auditoria React/Vite, validação de races frontend, revisão de acessibilidade e busca por segredo/PII/decodificação de `noteId`.
- [x] `VAL-05` Executar Foundation validator, guards de TODO e `git diff --check`.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `SCOPE-01` | `Scope` | `SCOPE-01` Reorganizar a navegação autenticada com destinos textuais `Geral` e `Erros`, preservando Equipe, Senha e sessão. | `browser+code` | `npm run e2e:notas`; `App.tsx`; `Cabecalho.tsx` | `local browser` | `passed` | navegação e sessão preservadas |
| `SCOPE-02` | `Scope` | `SCOPE-02` Tornar `/` a lista Smart Notas e preservar a lista legada de falhas em `/erros`; manter `/eventos/:refId` para detalhe/tratamento de erro. | `browser+code` | `npm run e2e:notas`; matriz de rotas | `local browser` | `passed` | isolamento de autoridade confirmado |
| `SCOPE-03` | `Scope` | `SCOPE-03` Expor seletor textual Unifast/Prosperar, sem opção agregada; persistir na URL apenas contexto, datas, status e página, mantendo `documento` e `idCompra` em estado efêmero da sessão autenticada. | `unit+browser` | parser/sinks em `test:notas` e `e2e:notas` | `local browser` | `passed` | URL/storage/referrer protegidos |
| `SCOPE-04` | `Scope` | `SCOPE-04` Consumir `GET /api/v1/notas` com contexto, intervalo, status, documento, idCompra e página; nunca enviar ao cliente credenciais/CNPJ configurado do emissor nem inferir `noteId`. | `browser+adapter` | requests interceptadas; `api/notas.ts` | `local browser` | `passed` | parâmetros e ausência de segredos provados |
| `SCOPE-05` | `Scope` | `SCOPE-05` Consumir `GET /api/v1/notas/:noteId` em `/notas/:noteId`, exibindo somente o DTO normalizado e tratando 404/indisponibilidade sem fallback para `logs`. | `browser+adapter` | detalhe/404/canários em `e2e:notas` | `local browser` | `passed` | noteId opaco; sem fallback |
| `SCOPE-06` | `Scope` | `SCOPE-06` Manter cache em memória acima das rotas, com no máximo 20 chaves, freshness de 60 segundos, retenção stale de 10 minutos e descarte LRU. | `unit+race` | `test:notas`; race reports `r3b` | `local` | `passed` | limites e LRU determinísticos |
| `SCOPE-07` | `Scope` | `SCOPE-07` Deduplicar requisições por chave, tratar abort como cancelamento não exibível, impedir commits tardios por geração de request/sessão, isolar contexto/filtros/página na chave e limpar tudo sincronicamente no logout/unmount da sessão autenticada. | `unit+race+review` | 27 probes; architecture merge | `local` | `passed` | logout manual e 401 sincrônicos |
| `SCOPE-08` | `Scope` | `SCOPE-08` Exibir loading, vazio, stale/revalidando, erro sem cache, erro de revalidação com dados preservados, rate limit e sessão expirada com semântica acessível. | `browser` | cenários interceptados em `e2e:notas` | `local browser` | `passed` | estados observáveis e acessíveis |
| `SCOPE-09` | `Scope` | `SCOPE-09` Atualizar identidade visível para UniNotas e manter a origem/escopo fiscal textual, sem depender apenas de cor. | `browser` | headings, labels e contexto em `e2e:notas` | `local browser` | `passed` | identidade textual confirmada |
| `SCOPE-10` | `Scope` | `SCOPE-10` Criar navegador determinístico com mocks para contexto, lista, detalhe, retorno rápido, resposta atrasada, stale failure, refresh explícito, logout, rotas legadas e ciclo resolver/reabrir com PATCH interceptado; preservar o runner legado real como ferramenta opcional e fail-closed. | `navigation/browser+guard` | `frontend/e2e/notas.mjs`; `npm run e2e:notas`; `frontend/e2e/fluxo.mjs`; Vite attestation curl 200/404 probes | `local browser` | `passed` | runner mutável protegido e fail-closed; jornada local interceptada passou |
| `SCOPE-11` | `Scope` | `SCOPE-11` Atualizar README frontend e consolidar os resultados estáveis no módulo `fiscal-notes-and-documents` sem promover runtime ownership. | `doc+validator` | `frontend/README.md`; `foundation_documentation/modules/fiscal-notes-and-documents.md`; Foundation validator | `local` | `passed` | ownership canônico permanece inalterado |
| `DOD-01` | `Definition of Done` | `DOD-01` Usuário autenticado navega por `Geral` e `Erros`; volta à última URL fiscal canônica sem perder cache e o legado continua funcional, inclusive resolver/reabrir mockado, em `/erros` e `/eventos/:refId`. | `browser` | `npm run e2e:notas` | `local browser` | `passed` | retorno/cache e PATCH interceptado |
| `DOD-02` | `Definition of Done` | `DOD-02` Geral lista notas do contexto textual selecionado com filtros/paginação compatíveis e sem dados cruzados. | `browser` | requests/linhas Unifast e Prosperar | `local browser` | `passed` | paginação 1→2→3 e contexto isolado |
| `DOD-03` | `Definition of Done` | `DOD-03` Detalhe fiscal abre por `noteId` opaco, usa allowlist do DTO público, mascara chaves de acesso e nunca expõe/decodifica `idInterno`, token ou CNPJ configurado do emissor. | `unit+browser+security` | canários, sinks e security review | `local` | `passed` | allowlist antes do cache |
| `DOD-04` | `Definition of Done` | `DOD-04` Cache cumpre cap/TTL/stale/LRU, sobrevive a troca de rota, isola chaves e é eliminado no logout. | `unit+navigation/browser` | `npm run test:notas`; `npm run e2e:notas` cobre troca de route/rota e logout | `local browser` | `passed` | limites exatos e clear observados |
| `DOD-05` | `Definition of Done` | `DOD-05` Respostas atrasadas/abortadas não substituem o contexto ou a consulta ativa; chamadas idênticas em voo são deduplicadas. | `race+browser` | 27 probes `r3b`; out-of-order browser | `local` | `passed` | zero stale commit |
| `DOD-06` | `Definition of Done` | `DOD-06` Estados loading, vazio, revalidando, stale-error, erro sem cache, 429 e sessão expirada são distinguíveis e acessíveis. | `browser` | cenários controlados `e2e:notas` | `local browser` | `passed` | mensagens/roles distintos |
| `DOD-07` | `Definition of Done` | `DOD-07` Refresh explícito garante uma requisição upstream: inicia uma quando não há outra idêntica em voo e compartilha/desabilita enquanto ela está pendente; retorno rápido usa cache válido e stale revalida uma única vez em segundo plano. | `unit+race+browser` | contagens exatas de requests | `local` | `passed` | refresh/dedupe comprovados |
| `DOD-08` | `Definition of Done` | `DOD-08` UI é responsiva, navegável por teclado e identifica contexto/status também por texto. | `browser` | grid desktop, foco e viewport 390 px | `local browser` | `passed` | sem overflow horizontal |
| `DOD-09` | `Definition of Done` | `DOD-09` Build/lint passam; o navegador determinístico cobre os fluxos novos e as rotas legadas; o runner mutável legado aponta para `/erros` e falha fechado sem autoridade explícita. | `command+navigation/browser+guard` | `npm run lint`; `npm run build`; browser `npm run e2e:notas`; runner guard exits 1 | `local browser` | `passed` | bundle 60 módulos |
| `DOD-10` | `Definition of Done` | `DOD-10` Documentação registra o candidato local sem ativar runtime, segredo ou capability ownership. | `doc+navigation/browser+validator` | módulo/TODO + browser `npm run e2e:notas` sem request externo + Foundation validator | `local browser` | `passed` | Local-Implemented, Provisional |
| `VAL-01` | `Validation Steps` | `VAL-01` Executar `npm run lint && npm run build` em `frontend/`. | `command` | ambos exit 0 em 2026-09-27 | `local` | `passed` | ESLint Hooks + TS + Vite |
| `VAL-02` | `Validation Steps` | `VAL-02` Executar e2e fiscal mockado com Chromium via script `npm run e2e:notas`. | `browser` | Chrome + preview 5390 exit 0 | `local browser` | `passed` | todas APIs interceptadas |
| `VAL-03` | `Validation Steps` | `VAL-03` Executar navegação, detalhe e ciclo resolver/reabrir legados com GET/PATCH interceptados dentro de `npm run e2e:notas`; não executar o runner real `npm run e2e` sem fixture descartável, runtime local controlado e autoridade explícita (`AUTORIZAR_MUTACAO=1`). | `browser+guard` | PATCH mockado + três probes fail-closed | `local` | `passed` | nenhuma mutação externa |
| `VAL-04` | `Validation Steps` | `VAL-04` Executar auditoria React/Vite, validação de races frontend, revisão de acessibilidade e busca por segredo/PII/decodificação de `noteId`. | `audit+navigation/browser` | `npm run e2e:notas`; `artifacts/tmp/uninotas-frontend-delivery/`; `artifacts/tmp/uninotas-frontend-race-r3b/` | `local browser` | `passed` | a11y/PII browser; zero finding material aberto |
| `VAL-05` | `Validation Steps` | `VAL-05` Executar Foundation validator, guards de TODO e `git diff --check`. | `guard` | validator/guards/diff check finais | `local` | `passed` | resultados reconciliados no closeout |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas real | necessário apenas no cutover, não no e2e local | `healthy` | `2026-09-27` | probes backend redatados já concluídos | usar mocks contratuais neste TODO |
| Chromium | navegador do Playwright | `healthy` | `2026-09-27` | Chrome local + `vite preview` 5390; `npm run e2e:notas` PASS | navegador interceptado; nenhum backend real |
| Backend local fiscal | contrato existe, flag desabilitada | `healthy` | `2026-09-27` | 223 testes/build/lint backend | mocks no frontend; smoke real no cutover |

## Profile Scope & Handoffs

- **Primary execution profile:** `operational-coder`
- **Active technical scope:** `react,vite`
- **Expected supporting profiles:** `assurance-tester-quality`
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `operational-coder` | `assurance-tester-quality` | auditoria obrigatória dos testes e races | testes/e2e/cache | `completed; triple audit Round 06 clean` |
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

- [x] `none — D-01..D-07 permanecem resolvidas e implementadas no candidato local`.

## Decisions (Resolved Before Freeze)

- [x] `D-01` `/` é Geral Smart Notas; `/erros` preserva a fila legada; detalhes permanecem separados em `/notas/:noteId` e `/eventos/:refId`. Ref: feature brief ST-03/ST-04.
- [x] `D-02` `contexto=unifast|prosperar`, datas, status e página vivem na URL; default `unifast`, sem agregado. `documento` (CPF/CNPJ do destinatário) e `idCompra` ficam somente no estado efêmero autenticado, nunca em URL/history/referrer; troca de contexto mantém esses filtros em memória e volta à página 1. Ref: module invariant + `ARCH-03/CRIT-02`.
- [x] `D-03` intervalo default são 30 datas de calendário incluindo hoje (`início = hoje - 29 dias`) no calendário `America/Sao_Paulo`, serializadas sem conversão de instante em `YYYY-MM-DD`; o backend aceita diferença máxima de 365 dias entre endpoints, equivalente a até 366 datas inclusivas. Ref: backend query contract + `ARCH-05`.
- [x] `D-04` cache: 20 chaves com LRU real, fresh até 60 s inclusive e stale retido até 10 min inclusive; ausente ou >10 min carrega da API. Refresh ignora freshness, inicia request se não houver um idêntico em voo e compartilha o já ativo. Ref: SD-08/G-20 + `ARCH-04/TEST-02`.
- [x] `D-05` cache key inclui usuário da sessão, contexto, datas, status, documento, idCompra e página; cada request guarda controller, promise, geração do request e geração da sessão. Logout/unmount aborta e limpa; resposta após substituição, eviction, troca de query, logout ou dispose não reinsere nem atualiza UI. Ref: race matrix + `ARCH-04`.
- [x] `D-06` nenhuma biblioteca de runtime/estado/cache; adapter e cache usam React e Web APIs. Admitir somente `eslint`, configuração TypeScript compatível e `eslint-plugin-react-hooks` como tooling dev-only, após package-first não encontrar owner interno, para que `npm run lint` valide regras/dependências de Hooks além do `tsc`. Ref: `ARCH-R2-02`.
- [x] `D-07` erros de integração permanecem legados e não são mesclados em linhas/notas neste corte. Ref: ownership de módulos.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `fiscal-notes-and-documents#Invariants` | Smart Notas é fonte exclusiva; um contexto por request; sem payload bruto | `Preserve` | módulo canônico |
| `events-and-classification#Specification` | `/eventos` continua projeção atual de erros/eventos | `Preserve` | módulo canônico |
| `identity-and-team#Observed Authentication Contract` | JWT/perfis atuais protegem leitura | `Preserve` | módulo canônico |

## Decision Baseline (Frozen Before Implementation)

- [x] `D-01..D-07` congeladas no plano material `db851c8`, aprovado pelas revisões R4 sem findings; implementação continua proibida até `APROVADO` humano.

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
| lint + build/typecheck | frontend | `npm run lint && npm run build` | regras/dependências de Hooks, suppression nova, contrato/tipos/imports inválidos | `implement-in-this-todo` | VAL-01 + revisão de adherence |
| audit | frontend | `frontend-race-condition-validation` | stale response/cleanup/dedupe | `implement-in-this-todo` | VAL-04 |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after baseline freeze and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `no_material_findings`
- **Decision review evidence / resolution:** R4 fresh/no-context sobre `db851c8` retornou `ready_for_APROVADO` e zero findings; arquitetura route-scoped, cache/session, parser, privacy e evidence consideradas coerentes.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `no_material_findings`
- **Adherence review evidence / resolution:** merge em `artifacts/tmp/uninotas-frontend-delivery/architecture.merge.{json,md}`; confirmou D-01..D-07 e limpeza fiscal síncrona no logout manual e 401.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** TODO medium architecture-corrective deve ser revisado a partir de baseline imutável.
- **Trigger stage:** `before first planning review`
- **Baseline branch:** `uninotas-foundation:main`
- **Baseline commit:** `e1fe4c92da4e4a694f1cc2dd59323dd980ca7378`
- **Baseline push reference:** `origin/main`
- **Gate status:** `findings_integrated`
- **Findings summary:** R1..R3 geraram findings todos integrados; R4 aprovou o plano material `db851c8` sem findings.
- **Evidence / reference:** plano material revisado em `db851c8`; metadados finais congelados/publicados em `uninotas-foundation:main@e1fe4c92da4e4a694f1cc2dd59323dd980ca7378`; dispatches/resultados em `artifacts/tmp/uninotas-frontend-review/`.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** mudanças pós-review podem alterar cache/rotas/risco.
- **Trigger stage:** `after planning review and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `canonical template set`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/completed/features/TODO-uninotas-smart-notas-read-frontend.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** zero das 22 seções materiais divergiu do freeze final `e1fe4c9`.
- **Evidence / reference:** `review_scope_drift_guard.py` retornou `Overall outcome: go` em 2026-09-27.
- **Waiver authority / reference:** `n/a`

## Questions To Close

- [x] `none — D-01..D-07 estão fechadas e prontas para aprovação humana`.

## Package-First Assessment

- **Queries:** `query_packages.sh --search "react cache fiscal notes"`; `query_packages.sh --stack node`; `query_packages.sh --search "eslint react hooks typescript"`
- **Relevant packages found:** `none`
- **READMEs read:** `frontend/README.md`
- **Decision:** runtime/cache host-specific sem nova dependência; tooling dev-only oficial de ESLint/TypeScript/React Hooks admitido após ausência de owner interno.
- **Tier:** `Local host application`
- **Rationale:** cache curto e adapter são específicos ao contrato UniNotas; o linter não é capacidade de produto, mas proteção estática necessária para effects/Hooks que o `tsc` não cobre.

## Frontend / Consumer Matrix

| Producer Surface | Consumer Surface | Planned State | Evidence / Guardrail |
| --- | --- | --- | --- |
| `GET /api/v1/notas` | `/`, `ListaNotas`, cache/session provider | `local consumer implemented; inactive` | tipos exatos + browser list/context/cache |
| `GET /api/v1/notas/:noteId` | `/notas/:noteId`, `DetalheNota` | `local consumer implemented; inactive` | rota opaca + browser detail/404 |
| `GET /api/v1/eventos`, `/eventos/resumo`, `/eventos/produtos` | somente `/erros` | `existing list consumers narrowed to error list` | e2e + route-scoped hooks; nenhuma chamada em detalhe fiscal/legado |
| `GET /api/v1/eventos/:refId` | somente `/eventos/:refId` | `existing detail consumer preserved` | smoke legado read-only |
| `GET /api/v1/realtime/eventos?token=...` | somente `/erros` | `existing consumer narrowed to error list` | scan estrutural + e2e; nenhuma outra rota abre SSE |
| Smart Notas credentials/CNPJ | nenhum consumidor frontend | `consumer intentionally absent` | env/import/bundle scan; backend-only invariant |

### Fiscal UI Data & Privacy Allowlist

| Data class | Frontend handling | URL / logging rule |
| --- | --- | --- |
| `noteId`, `fiscalContext`, status, número, ambiente, modelo, finalidade, plataforma, produto, datas, competência, valores, natureza e quantidade | campos permitidos do DTO público; `noteId` é opaco e pode existir apenas no path de detalhe | não logar payload/identificadores; `noteId` não pode ser decodificado |
| `purchaseId` retornado | permitido no DTO normalizado/cache apenas em memória; DOM usa `••••` + 4 finais quando houver mais de 4 caracteres, caso contrário “Não disponível”; sem cópia integral | valor integral proibido em DOM, URL, storage, console/log, erro e screenshot |
| `accessKey`, `referencedAccessKey` | somente valores com exatamente 44 dígitos podem ser renderizados mascarados (`••••••••` + 8 finais); ausente, curto ou malformado vira “Não disponível”; sem cópia integral | nunca incluir valor integral em query params, console, screenshot ou mensagem de erro |
| filtro `documento` e filtro `idCompra` | estado controlado efêmero dentro do provider da sessão; o valor exato é permitido somente no próprio input autenticado, na cache/request key em memória e na query autenticada `/notas` | proibidos em URL/history/referrer, local/session storage, logs/console, screenshots, textos de status/erro, DOM não relacionado e qualquer request não fiscal; limpar no logout |
| token Smart Notas, CNPJ configurado do emissor, `providerIdInterno`, payload cru | não fazem parte do modelo de UI | proibidos em DOM, URL, bundle, mocks, console, erro e cache; o JWT de sessão existente continua sob o contrato atual de autenticação |

O adapter faz normalização runtime por allowlist antes de qualquer escrita no cache: propriedades desconhecidas são descartadas; tipos/formas inválidos não são type-cast como DTO válido. Uma fixture adversarial inclui canários sintéticos em `providerIdInterno`, campo desconhecido, chave curta/malformada e payload aninhado; os testes provam que nenhum canário chega ao cache, DOM, console, erro ou screenshot. Mocks usam somente identificadores sintéticos que não representem CPF/CNPJ real.

### Sensitive Value Allowed-Sink Matrix

| Value | Allowed sinks | Forbidden sinks |
| --- | --- | --- |
| `documento` / `idCompra` digitado | input correspondente; request/cache key e DTO normalizado apenas em memória; query autenticada `GET /api/v1/notas`; resposta `purchaseId` somente mascarada no DOM | URL/history/referrer, storage, outro DOM com valor integral, status/erro, console/log, screenshot com valor integral, request não fiscal |
| chave de acesso válida | DTO normalizado/cache em memória; DOM apenas mascarado com 8 finais | valor integral em qualquer DOM, URL, storage, console/log, erro ou screenshot |
| credencial Smart Notas / CNPJ configurado / `providerIdInterno` / campo desconhecido | nenhum sink frontend | todos os sinks client-side, inclusive cache e mocks persistidos |

### Canonical Fiscal URL Truth Table

O parser é puro, separado de `useFiltros` legado, recebe o “hoje” já calculado em `America/Sao_Paulo` e produz `{ query, canonicalSearch, needsReplace }`. A rota executa no máximo um `replace` e bloqueia todo fetch até `needsReplace=false`. A cache key nasce somente da query canônica mais os filtros efêmeros.

| Input class | Canonical output | Fetch behavior |
| --- | --- | --- |
| parâmetros ausentes | `contexto=unifast`, `dataInicio=hoje-29`, `dataFim=hoje`, `pagina=1`; status omitido | um `replace`, depois uma request |
| `contexto` desconhecido/duplicado | `contexto=unifast` único | um `replace`, nenhum fetch antes dele |
| `status` fora do catálogo/duplicado | remover status | um `replace`, depois fetch sem status |
| `pagina` ausente, não inteira ou fora de `1..10000` | `pagina=1` | um `replace`, depois fetch da página 1 |
| uma/ambas datas ausentes, formato inválido ou data impossível | substituir o par inteiro pelo default de 30 datas | um `replace`, nenhum request inválido |
| datas válidas invertidas | ordenar as duas pontas | um `replace`, depois fetch do intervalo ordenado |
| datas válidas com diferença `>365` dias | preservar `dataFim` e definir `dataInicio=dataFim-365` | um `replace`, depois fetch; backend nunca recebe range inválido |
| `documento`, `idCompra` ou chave desconhecida na URL | remover sem hidratar os inputs efêmeros | um `replace`; valores removidos nunca entram na request/cache |
| URL já canônica | mesma URL e identidade estável | zero replace; exatamente a política de cache/request aplicável |

### Ephemeral Fiscal Filter Contract

- `documento`: o input pode conter dígitos, espaço, `.`, `-` e `/`; o normalizador remove somente essa formatação. Vazio omite o filtro. Qualquer outro caractere ou resultado diferente de 11/14 dígitos mantém o valor no input, mostra erro inline associado e bloqueia request/cache key nova.
- `idCompra`: aplicar `trim`; vazio omite, 1..100 caracteres aceita e acima de 100 mantém o input com erro inline e bloqueia request/cache key nova.
- Somente os valores canônicos entram na cache key e em `URLSearchParams` da request; inputs equivalentes convergem para uma identidade e uma chamada.
- Aplicar uma mudança válida de filtro reseta a página exatamente uma vez para 1; mudança inválida não altera URL, cache ativa ou resultado já exibido.
- Provas table-driven: documento vazio/formatado/10/11/14/15 dígitos/caractere proibido; compra whitespace/1/100/101 caracteres; encoding e contagem exata de requests.

### Geral Return Navigation Contract

- O provider da sessão mantém um único `lastCanonicalGeralHref` não sensível, atualizado somente após canonicalização bem-sucedida de `/` e composto por pathname + contexto/datas/status/página.
- O link textual `Geral` e a volta do detalhe fiscal usam esse href; `documento` e `idCompra` nunca fazem parte dele.
- Logout/401/dispose limpam o pointer junto com o cache; hard reload começa sem pointer e usa `/` para materializar defaults.
- O navegador parte de contexto/data/status/página não default, vai a `/erros`, clica `Geral` e prova a mesma URL/cache key e zero request quando a entrada ainda está fresh.

### Cache / Request Transition Contract

| Trigger and current state | Visible result | Network behavior | Commit guard |
| --- | --- | --- | --- |
| navigation with entry age `<= 60s` | cached data, not revalidating | no request | access promotes key to MRU |
| navigation/subscription with age `> 60s` and `<= 10min` | stale data + revalidating indicator | exactly one background request per key | matching request and session generations only |
| navigation absent or age `> 10min` | loading without old data | exactly one request per key | expired entry is removed before fetch |
| explicit refresh, no identical request active | current data retained + revalidating | exactly one new request even when fresh | new request generation owns completion |
| explicit refresh, identical request active | current state retained; refresh control disabled/joins | no duplicate; share the active promise | active generation remains owner |
| active query/context changes | new key state only | previous request is aborted when its last subscriber detaches | abort is not a UI error; old generation cannot commit |
| LRU insert would create key 21 | current requested key retained | evict least-recently-used key and abort its active request | evicted generation cannot reinsert on late completion |
| logout, automatic 401 or provider dispose | authenticated fiscal state disappears | abort every request and clear all 20 keys synchronously | increment session generation before abort/clear |
| any subscribed successful entry reaches success age `600_001ms` | remove fiscal data and show expired/error-without-cache + Retry | no automatic retry/request storm | exactly one boundary timer per subscribed key; generation guard prevents revival |

TTL boundaries use the injected clock and the age of the last successful response. Ten minutes is a hard visible-data maximum, not only a lookup boundary. Every subscribed successful entry arma/reschedules one timer against `successAt + 600_001ms`, whether subscribed fresh or stale. Successful replacement cancels the old deadline and arms from the new `successAt`; last detach, eviction, logout and dispose cancel it. Failed revalidation never advances success age. Expiry is network-silent. A hard reload has no session-memory cache and therefore requests normally.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | DTO backend local é o contrato consumidor | `backend/src/fiscal-notes/fiscal-notes.contract.spec.ts`; `backend/src/fiscal-notes/fiscal-notes.service.ts` | atualizar tipos e mocks antes de execução | `High` | `Keep as Assumption` |
| `A-02` | todos os perfis ativos podem ler ambos contextos | `backend/src/fiscal-notes/fiscal-notes.controller.ts` declara os quatro perfis leitores sem restrição por contexto | revisar UI/autorizações | `High` | `Keep as Assumption` |
| `A-03` | cutover não ocorrerá dentro deste TODO | `backend/src/config/configuration.ts` mantém `SMART_NOTAS_READ_ENABLED=false` por padrão | reclassificar para cross-stack/devops | `High` | `Keep as Assumption` |

## Execution Plan

### Touched Surfaces

- `frontend/src/api`, `frontend/src/contextos`, `frontend/src/hooks`, `frontend/src/componentes`, `frontend/src/paginas`, `frontend/src/estilos`, `frontend/e2e`, frontend README/manifest e módulo/TODO Foundation.

### Ordered Steps

1. Configurar ESLint/TypeScript/React Hooks dev-only, sem alterar runtime, e tornar `npm run lint` complementar ao `tsc`.
2. Criar e2e fiscal fail-first com mocks normais/adversariais dos envelopes backend e cenários de race/cache.
3. Criar tipos/normalizador/adapter fiscal e estender o cliente HTTP com `AbortSignal`, preservando `AbortError` como cancelamento e não como falha status 0.
4. Criar provider/cache de sessão com relógio/scheduler injetáveis e estado por chave (`promise`, controller, gerações), além de hook com dedupe, abort, TTL/stale/LRU e limpeza.
5. Criar lista, filtros, contexto, paginação e estados acessíveis.
6. Criar detalhe fiscal read-only e integrar rotas/navegação/cabeçalho; montar lista/resumo/produtos/SSE somente em `/erros`; manter `/eventos/:refId` apenas com seu fetch de detalhe, sem resumo/SSE/gatilho não consumido.
7. Ajustar estilos responsivos e identidade UniNotas.
8. Rodar auditorias/testes/build/browser; consolidar módulo e evidências.

### Test Strategy

- **Strategy:** `test-first`
- **Why:** cache e troca rápida de contexto têm falhas observáveis difíceis de provar por inspeção.
- **Fail-first targets:** contexto correto, retorno `Geral -> Erros -> Geral`, resposta fora de ordem, stale failure, refresh, logout e detalhe.
- **Deterministic temporal targets:** `60_000ms` ainda fresh, `60_001ms` revalida no próximo acesso, `600_000ms` ainda visível e `600_001ms` expira mesmo continuamente montado; sucesso intermediário cancela o deadline antigo e rearma; detach/eviction/logout cancelam timer; 21ª chave remove a LRU e late completion não reinsere.
- **Request-count targets:** duas montagens/consumidores da mesma chave fazem uma chamada; cliques repetidos durante refresh fazem uma chamada; troca rápida de contexto nunca permite que a resposta anterior apareça; logout manual e 401 automático resultam em cache vazio e zero commits tardios.
- **Calendar parser targets:** tabela canônica completa; virada de mês/ano, 29/02, timezone diferente do navegador, formato/data impossível, default de 30 datas, diferença de 365 dias preservada e diferença superior normalizada antes do fetch, sem reutilizar conversão UTC do filtro legado.
- **Adversarial normalization targets:** campos desconhecidos/canários são removidos antes do cache; `providerIdInterno` nunca entra no modelo; chave válida é mascarada, chave curta/malformada é totalmente redatada e `purchaseId` igual ao filtro aparece somente mascarado.

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
| cache/stale/race/logout | estado assíncrono visível/privado | `web-only` | `Playwright readonly + focused deterministic harness` | `no` | `no` | relógio injetável, contagem exata de requests e delays/falhas controlados | `n/a` |
| Erros legado — jornada mockada obrigatória | navegação/tratamento preservados sem persistência | `web-only` | `Playwright intercepted` | `mocked mutation only` | `no` | `/erros`, `/eventos/:refId`, resolver/reabrir com PATCH local e ausência de request/SSE legado em Geral | `n/a` |
| Erros legado — tratamento completo opcional | resolve/reabre estado persistente | `web-only` | `Playwright controlled mutation` | `yes` | `yes` | `npm run e2e` somente com fixture descartável e `AUTORIZAR_MUTACAO=1` | indisponibilidade não bloqueia este corte; nenhuma execução remota/ambiente compartilhado é autorizada |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| frontend lint/type/build | React/Vite, Hooks, tipos e bundle mudam | `npm run test:notas && npm run lint && npm run build` | `Local-Implemented` | `passed` | exit 0 em 2026-09-27; Vite 60 módulos | lockfile atual; sem inferir deploy |
| frontend fiscal browser | lista/detalhe/contexto/cache/a11y e legado mockado | `ALVO=http://127.0.0.1:5390 npm run e2e:notas` | `Local-Implemented` | `passed` | `OK mocked fiscal/cache/privacy/session and legacy PATCH flows` | Chrome + bundle produzido; todas APIs interceptadas |
| frontend cache/provider race | TTL/LRU/dedupe/detach/clear/late completion | `npm run test:notas` + `frontend_race_probe.sh` | `Local-Implemented` | `passed` | `artifacts/tmp/uninotas-frontend-race-r3b/`; 27/27 | relógio/transport determinísticos |
| frontend legacy browser mutável | jornada real exige fixture externa e não pertence ao corte interceptado | `npm run e2e` com guardas explícitos | `cutover` | `n/a` | invocation sem autoridade, alvo remoto e proxy divergente retornam exit 1 | não executado; produção/ambiente compartilhado proibidos |
| Foundation | docs/TODO/publication e contratos | `python3 deterministic/validate_foundation.py --root .` | `Local-Implemented` | `passed` | `Foundation validation passed` | executado no submodule |

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
  - **Option A (Recommended):** tornar o cabeçalho independente do resumo e encapsular lista/resumo/produtos/SSE somente em `/erros`; `/eventos/:refId` preserva apenas seu fetch de detalhe.
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

### Independent Review Finding Resolution

| Finding | Severity | Disposition | Contract change | State |
| --- | --- | --- | --- | --- |
| `ARCH-03` + `CRIT-02` | `high security/privacy` | `Integrated` | somente contexto/datas/status/página ficam na URL; documento/compra são efêmeros; allowlist e mascaramento explícitos | `resolved; R4 no findings` |
| `TEST-01` + `CRIT-01` | `high tests/safety` | `Integrated` | smoke legado obrigatório é mockado/read-only; `fluxo.mjs` é mutável, opcional e fail-closed; path autorizado no diff | `resolved; R4 no findings` |
| `ARCH-04` + `CRIT-04` | `medium architecture` | `Integrated` | state machine por chave/geração; refresh compartilha request idêntico; abort não vira erro | `resolved; R4 no findings` |
| `TEST-02` + `CRIT-06` | `medium tests` | `Integrated` | relógio injetável, limites exatos, request counts, 21ª chave, promoção LRU, logout/401 e late completion | `resolved; R4 no findings` |
| `ARCH-05` | `medium correctness` | `Integrated` | calendário `America/Sao_Paulo`, default de 30 datas, diferença máxima de 365 dias, parser separado do legado | `resolved; R4 no findings` |
| `CRIT-03` | `medium performance` | `Integrated` | SSE corrigido para `/api/v1/realtime/eventos?token=...`; lista/resumo/produtos/SSE só em `/erros`, nunca no detalhe | `resolved; R4 no findings` |
| `CRIT-05` | `medium adherence` | `Integrated` | rota canônica de Geral permanece `/` em todo o pacote | `resolved; R4 no findings` |
| `ARCH-R2-01` | `medium privacy tests` | `Integrated` | matriz de sinks permite o valor sensível somente no input/request/cache key fiscal e o proíbe em todos os demais destinos | `resolved; R4 no findings` |
| `ARCH-R2-02` | `medium structural` | `Integrated` | dependências dev-only e config ESLint React Hooks entram no diff; harness deixa de atribuir validação de effects ao `tsc` | `resolved; R4 no findings` |
| `CRIT-07` | `high bounded evidence` | `Integrated` | pacote de review passa a incluir contract spec, controller e configuration citados por `A-01..03` | `resolved; R4 no findings` |
| `CRIT-08` | `medium governance` | `Integrated` | checkpoint material `db851c8` publicado; freeze/guards finalizados antes do pedido | `resolved by gate checkpoint` |
| `CRIT-09` | `medium correctness` | `Integrated` | truth table fecha defaults, inválidos, duplicados, sensíveis, replace/fetch e cache identity | `resolved; R4 no findings` |
| `CRIT-10` | `medium correctness/performance` | `Integrated` | 10 min vira hard visible maximum com scheduler único por chave subscribed e sem retry automático | `resolved; superseded by complete lifecycle` |
| `CRIT-11` | `medium security/tests` | `Integrated` | normalização runtime + fixture canário; chave curta/malformada totalmente redatada | `resolved; R4 no findings` |
| `CRIT-10-REOPENED` + `ARCH-R3-02` | `medium cache lifecycle` | `Integrated` | todo successful entry subscribed recebe timer; sucesso rearma; detach/eviction/logout cancelam; expiry é network-silent | `resolved; R4 no findings` |
| `CRIT-12` | `medium navigation state` | `Integrated` | provider guarda somente o último href canônico não sensível de Geral e o limpa com a sessão | `resolved; R4 no findings` |
| `CRIT-13` | `medium filter contract` | `Integrated` | normalizador efêmero fecha documento/compra, validação acessível, key/request canônicas e reset único de página | `resolved; R4 no findings` |
| `ARCH-R3-01` | `high privacy coherence` | `Integrated` | `purchaseId` integral fica apenas no DTO/cache em memória e renderiza mascarado; fixture usa o mesmo id do filtro | `resolved; R4 no findings` |
| `ARCH-R3-03` | `medium test evidence` | `Integrated` | e2e obrigatório intercepta GET/PATCH e prova resolver/reabrir sem banco; runner real continua opcional/fail-closed | `resolved; R4 no findings` |

### Failure Modes & Edge Cases

- [x] resposta Unifast chega depois da troca para Prosperar; cache não pode atualizar a tela ativa.
- [x] retorno rápido usa cache correto; falha de revalidação mantém dados com aviso e timestamp.
- [x] request idêntico em voo é compartilhado; refresh explícito não cria storm.
- [x] fresh/stale/expired respeitam exatamente `60_000/60_001ms` e `600_000/600_001ms`; 21ª chave, promoção por leitura e late completion pós-eviction são determinísticos.
- [x] stale montado após revalidação falha desaparece no hard limit sem nova request automática, timer duplicado ou retorno do dado expirado.
- [x] fresh continuamente montado também expira; sucesso anterior ao deadline cancela o timer velho e move a expiração; detach/eviction/logout não deixam timers órfãos.
- [x] logout durante request aborta/ignora resultado e apaga cache.
- [x] 401 encerra sessão; 404 detalhe é vazio específico; 429 oferece retry explícito sem loop.
- [x] status fiscal desconhecido é exibido como texto seguro, não descartado.
- [x] cada classe da truth table produz URL/cache key canônicas com no máximo um `replace`, zero request pré-canonicalização e intervalo máximo de 365 dias entre endpoints.
- [x] `documento`/`idCompra` são normalizados/validados antes da key; aparecem integrais somente no input/request/cache fiscal em memória, nunca em URL/history/storage/referrer/console/outro DOM; `purchaseId` de resposta aparece apenas mascarado.
- [x] `Geral -> Erros -> Geral` restaura pathname/search não sensíveis e resultado fresh sem request; logout remove o pointer.
- [x] Geral não abre `/eventos*` nem SSE; `/eventos/:refId` abre somente seu fetch de detalhe; lista/resumo/produtos/SSE vivem apenas em `/erros`.

### Residual Unknowns / Risks

- [x] Chromium resolvido para a evidência final interceptada; runtime legado real continua deliberadamente fora do corte e o runner opcional falha fechado.
- [x] Provider page size é controlado externamente; UI usa `perPage/totalPages` normalizados retornados pelo contrato.

## Additional Architectural Opinions

- **Needed:** `yes`
- **Why ambiguity remains:** architecture-corrective e fluxo crítico com cache/races.
- **Opinion count:** `1`
- **Package mode:** `bounded-file-set`
- **Internal reviewer mandate:** `required after baseline freeze`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/completed/features/TODO-uninotas-smart-notas-read-frontend.md`
- **Latest TEACH evidence / artifact:** audit floor `go`; architecture/critique R4 em `db851c8` sem findings.

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
| `high_severity_plan_review_issue` | `yes` | findings high integrados e confirmados resolvidos pela R4 sem findings |
| `explicit_three_lane_request` | `no` | não solicitado |

## Approval

- **Status:** `approved`
- **Approved by:** `project owner / user`
- **Approval reference:** resposta explícita `APROVADO` em 2026-09-27, após confirmação de `preflight-go` e publicação Foundation `0b36337`.
- **Approval scope:** `SCOPE-01..SCOPE-11 e D-01..D-07 exatamente como congelados; frontend React/Vite local, testes/documentação associados, sem ativação/deploy/backend`
- **Implementation authority:** `granted for the frozen frontend scope D-01..D-07; one routine executor in principal checkout; no worktrees/auxiliary checkouts`

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/skills/rule-react-react-architecture-always-on/SKILL.md` | React UI/state/effects/a11y | render puro, ownership único, estados/a11y explícitos, lint real de Hooks | mutação em render, estado duplicado, effect sem cleanup/suppression | ESLint React Hooks + adherence review + browser races |
| `delphi-ai/skills/wf-react-change-ui-boundary-method/SKILL.md` | rotas/componentes/hooks | comportamento observável, normalizador/adapter isolado | type-cast de JSON cru, acoplamento da UI ao provider/segredo | seguir passos e evidence lanes |
| `delphi-ai/skills/rule-vite-vite-build-runtime-always-on/SKILL.md` | build/env/assets | manifest/scripts e env público restrito | tratar proxy/preview como produção ou expor segredo | build reproduzível; nenhuma env fiscal no cliente |
| `delphi-ai/skills/wf-vite-change-build-runtime-boundary-method/SKILL.md` | bundle/runtime boundary | separação dev proxy/produção | claim de deploy neste TODO | validar apenas build local |
| `delphi-ai/skills/package-first-verification/SKILL.md` | dependência dev-only de lint | query interna antes do pacote host | adicionar estado/cache externo | resultados zero; somente lint tooling admitido |
| `delphi-ai/skills/frontend-race-condition-validation/SKILL.md` | cache/races/logout | chave completa, cancelamento, stale controlado, limpeza | last-response-wins e cache cross-session | FRC requerido antes de Local-Implemented |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | e2e behavior-defining | assertions observáveis e fixtures determinísticas | teste que apenas espelha implementação | teste fail-first e audit obrigatório |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `authorized by explicit APROVADO on 2026-09-27 for one routine executor`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree authorization:** `not-authorized`
- **Worktree authorization reference:** `n/a — worktrees/auxiliary checkouts remain forbidden`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `go`
- **Guard evidence:** `todo_authority_guard.py --pre-approval` retornou `Overall outcome: preflight-go`; routine-executor/gpt-5.6-terra/medium; principal checkout only; rerun after APROVADO before implementation.
- **Waiver / exception reference:** `n/a`

> Ingestão vinculante pós-`APROVADO` concluída em 2026-09-27 antes do código: React/Vite, TODO execution boundary, package-first, test creation e frontend race validation foram recarregados; `verify_context` retornou `PACED-Ready` no Git Bash do Windows e os capability audits React/Vite retornaram `ready`.

## Security Risk Assessment

- **Risk level:** `medium`
- **Why this risk level:** dados fiscais autenticados ficam transitoriamente em memória e devem ser eliminados ao logout; nenhum segredo/PII novo deve ser exposto.
- **Attack surface in scope:** JWT client, URL params, noteId opaco, cache por sessão/contexto e mensagens de erro.
- **Attack simulation decision:** `required`
- **Review evidence:** `artifacts/tmp/uninotas-frontend-delivery/security-review.md`; `no_material_findings` no delta, com sinks de privacidade, DTO allowlist, isolamento de rotas e guardas do runner verificados.
- **Residual security risk:** `SEC-RES-01` baixo e preexistente — JWT da sessão em `sessionStorage`; backend/desempenho de produção permanecem para auth hardening/cutover.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `medium`
- **Why this level:** lista retriggerable com cache SWR, troca rápida de contexto e chamadas externas indiretamente caras.
- **Current delivery stage at review time:** `Local-Implemented, Provisional`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `not_needed` | `low` | `EPS-DATA-PATH-CHANGED` | `before_local_implemented` | `EPS-E1` | `not_applicable` | `frontend não muda endpoint` | `none` |
| `FRC` | `frontend-race-condition-validation` | `required` | `high` | `FRC-STALE-RESPONSE` | `before_local_implemented` | `FRC-E2` | `passed` | `none` | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `BCI-DUPLICATE-SUBMIT-OR-REPLAY` | `before_local_implemented` | `BCI-POLICY` | `not_applicable` | `sem backend/write` | `none` |
| `RLS` | `runtime-load-stress-validation` | `recommended` | `medium` | `RLS-CACHE-INDEX-SENSITIVE-PATH-CHANGED` | `before_local_implemented` | `RLS-E1` | `passed` | `bounded local evidence; produção não aferida` | `none` |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** medium, cross-module, rota pública autenticada e critical journey.
- **Critique status:** `no_material_findings`
- **Evidence / reference:** crítica R4 fresh/no-context sobre `db851c8` retornou `READY_FOR_APROVADO` e zero findings; confirmou resolução de `CRIT-01..13`.

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/completed/features/TODO-uninotas-smart-notas-read-frontend.md`
- **Gate status:** `no_material_findings`
- **Evidence / reference:** guard confirmou os anchors de código no rerun final de 2026-09-27.

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** testes behavior-defining e critical journey.
- **Audit status:** `no_material_findings`
- **Evidence / reference:** lane `test-quality` da auditoria dedicada, Round 06 clean; testes determinísticos, navegador e 27 probes de race inspecionados.

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** medium cross-module com rota/autenticação/cache.
- **Final review status:** `no_material_findings`
- **Evidence / reference:** `artifacts/tmp/uninotas-frontend-delivery/final-confirmation-2.merge.{json,md}`; configuração Vite/runner final, sessão e diff revistos sem findings.

## Dedicated Triple Review Audit Gate

- **Audit decision:** `required`
- **Why this decision:** audit floor classificou o fluxo como critical journey e release-sensitive.
- **Canonical protocol:** `audit-protocol-triple-review`
- **Lifecycle:** `delivery-side; additive à crítica e ao final review`
- **Audit status:** `clean`
- **Evidence / reference:** sessão em `artifacts/tmp/uninotas-frontend-delivery/audit/session.json`; Round 06 clean nas lanes performance, test-quality e cutover-integrity, sem conflitos/findings.

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `recommended`
- **Why this decision:** separa Geral API-only de Erros logs-only sem retirar o legado.
- **Cutover signals in scope:** `legacy-path separation; no fallback bridge`
- **Cutover audit status:** `no_material_findings`
- **Evidence / reference:** lane `cutover-integrity` Round 06 confirmou `/notas` API-only e `/erros` logs-only, sem fallback ou promoção de ownership.

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| frontend diff + tests | races, auth cache, routes, a11y, contract | `passed` | lint/build/unit/browser/race + final review merge | `none active` | pacote local provisório liberado; produção fora do corte |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| React/Vite/source authority | effect bypass, stale writes, persistent cache, logs fallback, secret env | `passed` | `artifacts/tmp/uninotas-frontend-delivery/rule-spirit.json` + inspeção | false positive em `dia.test(value)` | `by-design/no-action`: `.test` é RegExp de data, não alvo hard-coded |

## Promotion Finding Routing Ledger

| Finding ID | Finding Source | Severity | Classification | Required Action | Status | Rationale / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `PLAN-ARCH/CRIT-01..13` | architecture opinion + no-context critique | `high/medium` | `release-blocker` | congelar privacidade, URL, cache/races, calendário, rotas e evidência | `resolved` | D-01..D-07; `Independent Review Finding Resolution`; planning R4 clean |
| `PERF/TQA/CUTOVER-R1` | triple audit Round 01 | `high/medium` | `release-blocker` | corrigir paginação, timer/LRU, calendário, sinks, estados browser, SSE e runner | `resolved` | `audit/round-01/resolution.md` |
| `PERF/TQA/CUTOVER-R2` | triple audit Round 02 | `medium` | `release-blocker` | estabilizar filtros, timers, privacidade e catálogo de status | `resolved` | `audit/round-02/resolution.md` |
| `PERF/TQA-R3` | triple audit Round 03 | `medium` | `release-blocker` | restaurar estado após refresh cruzar expiry e ampliar canário visível | `resolved` | `audit/round-03/resolution.md` |
| `ARCH-ADHERENCE-01` | architecture adherence | `medium` | `release-blocker` | limpar cache/controladores sincronicamente no logout manual e 401 | `resolved` | callback registrado no owner da sessão; `architecture.merge.md` |
| `FINAL-01` | no-context final review | `medium` | `release-blocker` | vincular runner mutável à topologia Vite efetiva e rejeitar API base externa | `resolved` | atestação no Vite exige proxy loopback + `VITE_API_BASE` vazio; live positive/negative probes; `final-confirmation-2.merge.md` |
| `SEC-RES-01` | adversarial security review | `low` | `by-design/no-action` | avaliar token HttpOnly em contrato de auth separado | `accepted` | armazenamento JWT em `sessionStorage` é preexistente e não foi ampliado |
| `RULE-SPIRIT-01` | rule-spirit scan | `review` | `by-design/no-action` | classificar `dia.test(value)` | `resolved` | chamada é teste de RegExp de data, não alvo local hard-coded |

## Verification Debt Assessment

- **Audit outcome:** `no blocking verification debt`
- **Why this outcome:** critérios do corte possuem evidência unitária, browser interceptada, race, arquitetura, segurança e auditoria tripla; limites reais estão explicitamente no cutover.
- **Inline code TODO debt:** `none found in affected frontend surfaces`
- **Evidence / audit artifact:** pacote `artifacts/tmp/uninotas-frontend-delivery/`; race reports `artifacts/tmp/uninotas-frontend-race-r3b/`; completion matrix.
- **Accepted residual debt:** `SEC-RES-01` baixo/preexistente; live backend, deploy e smoke dos dois contextos pertencem ao TODO de cutover.

## TODO Closeout Disposition

- **Disposition:** `move-completed`
- **Disposition reason:** escopo frontend implementado e validado localmente, sem findings materiais abertos; limites de produção permanecem governados pelo cutover.
- **Post-commit/push status:** `local working tree only; no commit/push/deploy performed`
- **Next path/status action:** mover este TODO para `completed/features/`; iniciar cutover somente sob contrato e aprovação próprios.

## Module Consolidation Gate

- [x] módulo fiscal atualizado com o consumidor local candidato.
- [x] decisões estáveis D-01..D-07 consolidadas sem promover ownership.
- [x] cross-links e caminho final do TODO atualizados no movimento para `completed/features/`.

## Commands (Run Locally)

- `python3 delphi-ai/tools/node_capability_surface_audit.py --repo frontend --expect react --manifest package.json --require-script build --require-script lint --require-script e2e`
- `python3 delphi-ai/tools/node_capability_surface_audit.py --repo frontend --expect vite --manifest package.json --require-script build --require-script lint`
- `cd frontend && npm run lint && npm run build && npm run e2e:notas`
- `python3 foundation_documentation/deterministic/validate_foundation.py --root foundation_documentation`

## Files Expected

- Use `Diff Expectation Contract` como inventário autoritativo.
