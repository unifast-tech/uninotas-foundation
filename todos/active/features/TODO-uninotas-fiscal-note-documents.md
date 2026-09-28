# TODO — Disponibilizar PDF/XML por nota e ampliar ações visuais

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Status:** `Pending Approval`
- **Created:** `2026-09-28`
- **Owner:** `Delphi / Operational Coder`, sob autoridade humana do usuário

## Context

O UniNotas já consulta o endpoint oficial de detalhe e mostra a allowlist completa aprovada ao abrir uma nota. Falta resolver, sob demanda, as URLs oficiais de PDF e XML e oferecê-las sem expor credenciais, CNPJ ou `idInterno` como autoridade pública. No mesmo pacote visual, o glifo de configurações precisa ficar maior sem alterar o disclosure já entregue.

## Framing Source & Story Slice

- **Feature brief:** `artifacts/feature-briefs/uninotas-fiscal-note-documents.md`
- **Primary story ID:** `ST-DOCUMENT-ACTIONS`
- **Why this is the right current slice:** PDF/XML formam uma única capacidade documental read-only sobre a identidade fiscal já existente; a verificação do detalhe evita duplicação. O aumento do glifo é uma correção visual local absorvida pela mesma jornada browser.
- **Direct-to-TODO rationale:** `n/a`

## Contract Boundary

- O detalhe existente continua em `GET /api/v1/notas/:noteId` e deve permanecer com exatamente os 27 campos públicos já aprovados; nenhuma segunda rota de detalhe será criada.
- Novas rotas autenticadas resolvem, separadamente, PDF e XML usando somente o `noteId` assinado/context-bound.
- O backend chama SmartNotas com token/CNPJ do contexto decodificado, admite `200 { url }` ou `202 { mensagem }` e devolve um contrato público mínimo e estável.
- A URL disponível é efêmera: HTTPS, sem credenciais embutidas, nunca persiste, não entra em cache, logs, erro, telemetria ou estado de sessão.
- A Geral e o detalhe expõem um disclosure `⋮` com `Abrir PDF` e `Abrir XML`; nenhum documento é consultado antes da escolha explícita.
- Todos os perfis leitores atuais (`ADMIN`, `GESTOR`, `ANALISTA`, `LEITOR`) mantêm o mesmo acesso.
- O glifo de configurações aumenta, preservando nome acessível, foco, Escape, clique externo, permissões e conteúdo.

## Implementation Intent

- **Current delivery:** integração read-only de links documentais SmartNotas, ações React responsivas e ajuste do gatilho de configurações.
- **Planned next steps:** `cutover/smoke real continuam no TODO de cutover existente`.
- **Anticipatory implementation authorized now:** `none`.
- **Rationale:** reutilizar o módulo, codec, coordenação de taxa e cliente HTTP existentes; resolver somente a URL solicitada e não criar armazenamento, proxy binário ou nova configuração.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Next exact step:** congelar/publicar o baseline documental, concluir gates de planejamento e obter `APROVADO` antes de modificar código.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `implementation`
- **Why this state now:** o contrato está em preparação e nenhuma implementação foi autorizada.
- **Exit condition:** após aprovação, implementação/evidências locais concluídas e movimento para `completed/features/`; deploy permanece separado.

## Provisional Notes

- **Missing for production-ready:** aprovação, implementação, testes, browser, auditorias e smoke/cutover real.
- **Revisit criteria:** mudança do contrato oficial, necessidade de proxy binário, host não HTTPS ou alteração de auth/perfis.
- **Dependencies unblocked:** fixtures determinísticas permitem implementação local sem chamar a API real; o smoke real pertence ao cutover.

## Blocker Notes

- **Blocked:** `no`.
- **Current blocker:** `none`.
- **Unblock condition:** `n/a`.

## Scope

- [ ] `SCOPE-DOC-01` Preservar e regressar o detalhe completo existente; não duplicar `notasDetalhe`.
- [ ] `SCOPE-DOC-02` Adicionar ao port/adapter SmartNotas resoluções independentes para `/notas/{idInterno}/pdf` e `/xml`, com decoder positivo de `200`/`202`, limites, cancelamento e redaction existentes.
- [ ] `SCOPE-DOC-03` Expor rotas públicas `GET /api/v1/notas/:noteId/documentos/pdf` e `GET /api/v1/notas/:noteId/documentos/xml`, protegidas pelos quatro perfis leitores e pelo mesmo `noteId` assinado.
- [ ] `SCOPE-DOC-04` Adicionar disclosure vertical `⋮` em cada linha/card da Geral e no detalhe, com ações sob demanda, loading, pendente, erro e recuperação.
- [ ] `SCOPE-DOC-05` Abrir URL disponível em nova aba com `noopener`/`noreferrer`; se a abertura automática for bloqueada, manter link visível e acionável; limpar a URL efêmera ao fechar/trocar nota/logout.
- [ ] `SCOPE-DOC-06` Evitar navegação ao detalhe quando o usuário interagir com o menu e preservar navegação normal ao selecionar o restante da linha/card.
- [ ] `SCOPE-DOC-07` Aumentar o glifo de configurações e garantir caixa interativa mínima de `44x44px` nos viewports desktop e móvel.
- [ ] `SCOPE-DOC-08` Atualizar documentação modular/README e testes backend, frontend e browser afetados.

## Delivery Status Semantics

- `Pending`: sem marco de entrega implementado.
- `Local-Implemented`: código e evidências locais concluídos.
- `Provisional`: deploy/smoke real permanecem no cutover.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `MonitorNotes:release/uninotas-smart-notas`, `uninotas-foundation:main`
- **Promotion lane path:** `release/uninotas-smart-notas -> main via PR`; Foundation permanece em `main` como autoridade documental.
- **Lane-promoted threshold for this TODO:** `n/a — entrega termina Local-Implemented antes do PR humano`.
- **Production-ready threshold for this TODO:** `main + Railway/smoke do TODO de cutover`.
- **Execution topology:** `primary-checkout-single-writer`; sem worktree, checkout auxiliar ou branch worker/reconcile.

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| `ST-DOCUMENT-ACTIONS` | `pending` | `n/a` | `n/a` | `human follow-through after local closeout` | `pending` |

## Out of Scope

- Persistir ou cachear URL/PDF/XML; salvar anexos no PostgreSQL/Prisma; proxy/stream binário; baixar os dois documentos em lote.
- Pré-carregar documentos ao listar ou abrir o menu; agregar contextos; usar `idInterno` cru em rota pública.
- Alterar campos/PII/CSV/filtros do detalhe/lista já aprovados.
- Emissão, cancelamento, correção, reprocessamento ou qualquer mutation SmartNotas.
- Nova dependência, biblioteca de menu/ícones, variável Railway, Docker, migração, deploy ou merge.
- Mudar conteúdo, permissões ou comportamento do painel de configurações além do tamanho visual do gatilho.
- Worktrees, checkouts auxiliares ou escritores concorrentes de produto.

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `release/uninotas-smart-notas@f2984b42010e63d61ccd6e63d47a6c2f63bbcd03` | `working_tree` |
| `uninotas-foundation` | `uninotas-foundation` | `main@0c085293b33c61bd12b54d9f308f7985a2adac90` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M` | port, adapter, service/controller e testes documentais |
| `MonitorNotes` | `frontend/src/api/notas.ts` | `M` | contrato efêmero de documento |
| `MonitorNotes` | `frontend/src/paginas/ListaNotas.tsx` | `M` | menu por nota |
| `MonitorNotes` | `frontend/src/paginas/DetalheNota.tsx` | `M` | ações documentais e regressão do detalhe |
| `MonitorNotes` | `frontend/src/componentes/**` | `A|M` | disclosure reutilizável e gatilho de configurações |
| `MonitorNotes` | `frontend/src/estilos/*.css` | `M` | layout das ações e tamanho do glifo |
| `MonitorNotes` | `frontend/e2e/notas-unit.ts` | `M` | normalização/estado documental |
| `MonitorNotes` | `frontend/e2e/notas.mjs` | `M` | jornada desktop/mobile/teclado |
| `MonitorNotes` | `backend/README.md` | `M` | rotas documentais, se necessário |
| `MonitorNotes` | `frontend/README.md` | `M` | comportamento visível, se necessário |
| `MonitorNotes` | `uninotas-foundation` | `M` | gitlink acompanha publicação Foundation |
| `MonitorNotes` | `artifacts/**` | `??` | estado preexistente do usuário; preservar, nunca stagear/alterar |
| `uninotas-foundation` | `artifacts/feature-briefs/uninotas-fiscal-note-documents.md` | `A|M` | framing e encerramento |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-fiscal-note-documents.md` | `A|M|D` | contrato/evidência/closeout |
| `uninotas-foundation` | `todos/completed/features/TODO-uninotas-fiscal-note-documents.md` | `A` | destino do closeout |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | contrato documental durável |
| `uninotas-foundation` | `artifacts/publication-manifest.txt` | `M` | publicação Foundation |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/prisma/**` | `any` | nenhuma persistência/migração |
| `MonitorNotes` | `backend/.env*` | `any` | nenhuma variável nova |
| `MonitorNotes` | `frontend/.env*` | `any` | nenhuma variável nova |
| `MonitorNotes` | `Dockerfile` | `any` | runtime fora do escopo |
| `MonitorNotes` | `docker-compose.yml` | `any` | runtime fora do escopo |
| `MonitorNotes` | `railway.json` | `any` | deploy fora do escopo |
| `MonitorNotes` | `.github/**` | `any` | pipeline fora do escopo |
| `uninotas-foundation` | `project_constitution.md` | `any` | invariantes não mudam |
| `uninotas-foundation` | `system_roadmap.md` | `any` | sem mudança estratégica |
| `uninotas-foundation` | `policies/**` | `any` | sem mudança de política |
| `uninotas-foundation` | `deterministic/**` | `any` | sem mudança do validator |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** componentes auxiliares locais, tipos, erros estáveis, ajustes CSS/testes diretamente necessários ao menu e à resolução documental.
- **Must update or split the TODO:** proxy binário, persistência, nova configuração/host allowlist operacional, mutation fiscal, mudança de perfis ou novo objetivo de UX.

## Definition of Done

- [ ] `DOD-DOC-01` Abrir uma nota continua exibindo exatamente os 27 campos públicos aprovados, obtidos pelo endpoint de detalhe já existente.
- [ ] `DOD-DOC-02` PDF e XML resolvem pelo contexto contido no `noteId`; adulteração, raw `idInterno`, contexto/credencial cruzados e identidade divergente falham antes de vazar dados.
- [ ] `DOD-DOC-03` `200` aceita somente objeto com URL HTTPS absoluta, sem userinfo ou fragmento; `202` vira estado público pendente; redirects, status/shape inválidos, timeout, oversize, abort e limites seguem erros estáveis.
- [ ] `DOD-DOC-04` Nenhuma URL/token/CNPJ/`noteId`/payload entra em logs, erros, storage, cache fiscal ou telemetria; a URL existe apenas na resposta e estado efêmero da ação.
- [ ] `DOD-DOC-05` Cada nota na Geral e o detalhe oferecem `⋮`, `Abrir PDF` e `Abrir XML`; consulta ocorre somente após clique e uma ação em andamento não duplica chamadas.
- [ ] `DOD-DOC-06` O menu é operável por teclado, possui nome/estado acessível, fecha por Escape/clique externo/navegação, preserva foco e não aciona o link da nota ao selecionar documento.
- [ ] `DOD-DOC-07` Documento pendente/erro é anunciado e recuperável; popup bloqueado mantém link seguro visível; logout/unmount/nova ação aborta ou invalida resultado tardio.
- [ ] `DOD-DOC-08` Configurações mantém comportamento existente com glifo visual maior e alvo mínimo `44x44px` em desktop/mobile.
- [ ] `DOD-DOC-09` Quatro perfis leitores passam; JWT ausente/inválido/expirado falha; nenhuma rota pública aceita token/CNPJ/provider ID do consumidor.
- [ ] `DOD-DOC-10` Testes, browser, revisões e guards passam no checkout principal sem tocar persistência/runtime/deploy.

## Validation Steps

- [ ] `VAL-DOC-01` `cd backend && npm test -- --runInBand && npm run build && npm run lint`.
- [ ] `VAL-DOC-02` `cd frontend && npm run test:notas && npm run lint && npm run build`.
- [ ] `VAL-DOC-03` build/preview fresco + `npm run e2e:notas`, cobrindo desktop/mobile, mouse/teclado, lista/detalhe, PDF/XML disponível/pendente/erro, popup fallback e configurações.
- [ ] `VAL-DOC-04` capability audits NestJS/React/Vite, `git diff --check`, validators e guards Foundation.
- [ ] `VAL-DOC-05` probe real redatado de um documento autorizado por contexto fica no cutover; nunca imprimir URL/token/CNPJ/IDs.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-DOC-01` | `Definition of Done` | detalhe de 27 campos preservado | `test+browser` | exact-key tests + `e2e:notas` detalhe | `local browser` | `planned` | regressão, sem nova rota |
| `DOD-DOC-02` | `Definition of Done` | identidade/contexto protegidos | `integration-test` | Nest application/contract matrices | `backend local` | `planned` | inclui tamper/raw ID/cross-context |
| `DOD-DOC-03` | `Definition of Done` | contrato 200/202 e falhas | `adapter-test` | SmartNotas adapter fixtures | `backend local` | `planned` | URL nunca impressa |
| `DOD-DOC-04` | `Definition of Done` | zero retenção/vazamento | `test+review` | canários de log/storage/cache | `local` | `planned` | privacy boundary |
| `DOD-DOC-05` | `Definition of Done` | menu/consulta sob demanda | `browser` | `frontend/e2e/notas.mjs` | `Chrome local` | `planned` | uma chamada por escolha |
| `DOD-DOC-06` | `Definition of Done` | acessibilidade e navegação | `browser` | teclado/Escape/foco/click propagation | `Chrome local` | `planned` | desktop/mobile |
| `DOD-DOC-07` | `Definition of Done` | pending/erro/race/fallback | `unit+browser` | unit ownership + browser states | `local browser` | `planned` | late result invalidado |
| `DOD-DOC-08` | `Definition of Done` | settings 44x44 e glifo maior | `browser` | computed CSS e jornada disclosure | `Chrome local` | `planned` | sem mudar conteúdo |
| `DOD-DOC-09` | `Definition of Done` | auth dos quatro perfis | `integration-test` | controller/application matrix | `backend local` | `planned` | inclui 401 |
| `DOD-DOC-10` | `Definition of Done` | pacote verde e bounded | `command+review` | suites/guards finais | `local` | `planned` | sem runtime/persistence |
| `VAL-DOC-01` | `Validation Steps` | backend completo | `command` | comando exato | `local` | `planned` | Jest/build/lint |
| `VAL-DOC-02` | `Validation Steps` | frontend completo | `command` | comando exato | `local` | `planned` | unit/lint/build |
| `VAL-DOC-03` | `Validation Steps` | browser fiel | `browser` | preview fresco + `e2e:notas` | `Chrome local` | `planned` | APIs interceptadas |
| `VAL-DOC-04` | `Validation Steps` | audits/guards | `guard` | capability/diff/Foundation | `local` | `planned` | exact owners |
| `VAL-DOC-05` | `Validation Steps` | smoke real redatado | `runtime` | TODO cutover | `Railway stage` | `blocked` | explicitamente fora do closeout local |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| SmartNotas OpenAPI | define detalhe/PDF/XML e 200/202 | `healthy` | `2026-09-28` | `https://app.smart-notas.com/docs/api-docs.json`, hash congelado | fixtures locais; contrato muda => parar/revisar |
| SmartNotas runtime | smoke dos dois contextos | `unknown` | `n/a neste slice` | cutover separado | não bloqueia Local-Implemented; bloqueia Production-Ready |

## Profile Scope & Handoffs

- **Primary execution profile:** `operational-coder`
- **Active technical scope:** `nestjs|react|vite|cross-stack`
- **Expected supporting profiles:** `assurance-security-adversarial|assurance-tester-quality`
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `operational-coder` | `assurance-security-adversarial` | URL externa, PII e credenciais backend-only | adapter/API/browser handoff | `planned` |
| `operational-coder` | `assurance-tester-quality` | matriz 200/202/races/a11y | testes backend/frontend/browser | `planned` |

## Complexity

- **Level:** `medium`
- **Checkpoint policy:** `one checkpoint after backend contract; one after integrated browser; consolidated closeout`.
- **Why this level:** contrato público e externo novo, quatro perfis, URL fiscal efêmera e interação assíncrona cross-stack; sem banco ou runtime.

## Canonical Module Anchors

- **Primary module doc:** `modules/fiscal-notes-and-documents.md`
- **Secondary module docs:** `modules/authentication-and-access.md`
- **Planned decision promotion targets:** `fiscal-notes-and-documents.md > API Endpoint Definitions; Invariants; Frontend behavior`.
- **Module decision consolidation targets:** `fiscal-notes-and-documents.md > Smart Notas read boundary; document availability; errors`.

## Decisions

- [ ] `D-01` Preservar o detalhe atual de 27 propriedades; nenhuma nova implementação de `notasDetalhe`.
- [ ] `D-02` Expor dois endpoints subordinados a `noteId`, nunca `idInterno` cru.
- [ ] `D-03` Resolver URL somente por clique; sem prefetch, persistência ou cache.
- [ ] `D-04` Retornar allowlist pública `{ documentType, availability, url }`, com `url` presente somente quando `availability=available`; `pending` representa o `202` oficial.
- [ ] `D-05` Validar URL absoluta HTTPS sem username/password/hash; como ela não é buscada pelo servidor, não há superfície SSRF; frontend usa `noopener`/`noreferrer` e fallback acionável.
- [ ] `D-06` Reutilizar rate/concurrency/audit do módulo; operação documental é interativa e possui nomes fixos `pdf|xml`, nunca paths/URLs dinâmicos em log.
- [ ] `D-07` Menu por nota é disclosure acessível, não `role=menu`; apenas um fica aberto, com ownership único e proteção contra resultado tardio/duplo clique.
- [ ] `D-08` Aumentar glifo para pelo menos `20px` e caixa para `44x44px`, sem biblioteca de ícones.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `FISC-VIS-03` | `noteId` é única identidade de rota | `Preserve` | `modules/fiscal-notes-and-documents.md` |
| `Smart Notas sole source` | documentos vêm apenas da API | `Preserve` | módulo > Invariants |
| `no captured URL persistence` | URLs não persistem | `Preserve` | módulo > Invariants |
| `detail exact 27` | detalhe público allowlisted | `Preserve` | módulo > Fiscal read response allowlists |
| `four reader roles` | todos podem consultar | `Preserve` | módulo > API Endpoint Definitions |

## Decision Baseline (Frozen Before Implementation)

- [ ] `D-01..D-08` serão congeladas após review baseline, sem decisão material pendente.

## Architecture Change Governance

- **Applicability:** `not_needed`
- **Why this applies:** extensão coerente do port/application/controller e do consumer React existentes; não corrige nem supersede arquitetura compartilhada.
- **Deviation / debt being retired:** `n/a`.
- **Target steady-state after closeout:** `n/a`.
- **Temporary exceptions allowed:** `none`.
- **Cutover / removal condition:** `n/a`.

## Architecture Review Gates

- **Architecture decision review:** `pending audit guard`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion or n/a per guard`
- **Decision review package:** `bounded-summary`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** `pending`
- **Architecture adherence review:** `pending audit guard`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence or n/a per guard`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending`
- **No-go handling:** `retornar ao loop afetado e não alegar aprovação/conclusão`.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** TODO medium/cross-stack com contrato público e URL fiscal externa.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `uninotas-foundation:main`
- **Baseline commit:** `pending`
- **Baseline push reference:** `origin/main`
- **Gate status:** `not_run`
- **Findings summary:** `packet prepared pre-freeze; nenhuma review marcada passed`.
- **Evidence / reference:** `pending commit/push`.
- **Waiver authority / reference:** `n/a`.
- **Pre-freeze packet-prep rule:** `planning rows remain prepared-pre-freeze until the pushed baseline exists`.

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** as premissas A-01, A-03 e A-05 determinam se o detalhe será duplicado, se haverá proxy e como o consumer React será composto.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-01,A-02,A-03,A-04,A-05`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo uninotas-foundation/todos/active/features/TODO-uninotas-fiscal-note-documents.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending pushed freeze and planning review`.
- **Evidence / reference:** `pending`.
- **Waiver authority / reference:** `n/a`.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** garantir que review não amplie para proxy/persistência/deploy.
- **Trigger stage:** `after planning review converges and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo uninotas-foundation/todos/active/features/TODO-uninotas-fiscal-note-documents.md`
- **No-go handling rule:** `revalidar qualquer drift material com o usuário e repetir freeze/review afetada`.
- **Gate status:** `not_run`
- **Findings summary:** `pending`.
- **Evidence / reference:** `pending`.
- **Waiver authority / reference:** `n/a`.

## Questions To Close

- [x] O detalhe precisa ser refeito? `Não; já usa notasDetalhe e apresenta a allowlist completa.`
- [x] PDF/XML devem aparecer em todas as notas? `Sim; Geral e detalhe.`
- [x] As URLs devem ser armazenadas? `Não; handoff efêmero sob demanda.`
- [x] Documento pendente é erro? `Não; estado explícito derivado do 202 oficial.`

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | detalhe já chama endpoint oficial e tem 27 propriedades públicas | adapter/service/DetalheNota + módulo | reabre escopo de detalhe | `High` | `Keep as Assumption` |
| `A-02` | PDF e XML devolvem `{url}` em 200 e `{mensagem}` em 202 | OpenAPI oficial, hash congelado | decoder/contrato precisam revisão | `High` | `Promote to D-04` |
| `A-03` | URL pode ser entregue ao browser sem fetch server-side | contrato oficial descreve URL de download | proxy vira decisão material e exige nova aprovação | `High` | `Promote to D-05` |
| `A-04` | mesmos quatro leitores podem acessar documentos | direção prévia “todos os setores podem visualizar”; contratos atuais | exige decisão de autorização | `High` | `Promote to Contract Boundary` |
| `A-05` | menu pode ser adicionado sem biblioteca | React/CSS atual já implementam disclosure do header | dependência nova seria fora de escopo | `High` | `Keep as Assumption` |

## Execution Plan

### Touched Surfaces

- `backend/src/fiscal-notes/**`
- `frontend/src/api/notas.ts`, `frontend/src/paginas/{ListaNotas,DetalheNota}.tsx`, componente local de ações, CSS e testes
- módulo/README Foundation afetados

### Ordered Steps

1. Criar testes fail-first backend para port/adapter/service/controller: PDF/XML, 200/202, auth, `noteId`, URL inválida, limites/cancelamento/redaction.
2. Implementar resolução documental no port/adapter e application service; manter controller fino e contrato público exato.
3. Criar testes fail-first frontend para normalização, ownership, duplicidade, pending/error, resultado tardio e cleanup.
4. Implementar disclosure `⋮` reutilizável, integrar Geral/detalhe e garantir que a ação não navegue a linha.
5. Ajustar glifo/caixa de configurações; atualizar browser suite para desktop/mobile/teclado/foco.
6. Rodar suites completas, browser fresco, security/performance/test-quality/final reviews, guards e consolidar módulo/closeout.

### Test Strategy

- **Strategy:** `test-first`.
- **Why:** há novo contrato público/externo e races de interação; os casos 200/202/falha precisam estar congelados antes do código.
- **Fail-first targets:** endpoints inexistentes; port sem PDF/XML; menu inexistente; pending e late-result sem owner; alvo de configurações menor que 44px.

### Pre-APROVADO RED Evidence Capture

- **Decision:** `not_needed`.
- **Why now:** feature nova, não bug de diagnóstico ambíguo.
- **Target symptom:** `n/a`.
- **Allowed surfaces:** `none`.
- **Forbidden surfaces reaffirmed:** `production code|runtime/config/deploy|canonical project docs outside TODO authoring`.
- **Planned command / target:** `n/a`.
- **Status:** `not_run`.
- **Findings summary:** `n/a`.

### Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Geral `⋮` -> PDF/XML | nova interação/documento | `web-only` | `Playwright readonly` | `no` | `no` | intercepted 200/202/error URLs | API real fica no cutover |
| detalhe completo + ações | DTO consumido por tela | `web-only` | `Playwright readonly` | `no` | `no` | exact fields + actions | n/a |
| teclado/foco/fora/Escape | acessibilidade | `web-only` | `Playwright readonly` | `no` | `no` | desktop/mobile browser | n/a |
| settings maior | UI/touch target | `web-only` | `Playwright readonly` | `no` | `no` | computed style/geometry | n/a |
| auth/context/URL contract | alimenta UI autenticada | `web-only` | `Nest integration + Playwright` | `no` | `no` | deterministic provider fixtures | n/a |

### Frontend / Consumer Matrix

| Producer Surface | Consumer | Contract | Failure/Compatibility |
| --- | --- | --- | --- |
| `GET /api/v1/notas/:noteId` | `DetalheNota` | 27 propriedades exatas | inalterado; regressão obrigatória |
| `GET /api/v1/notas/:noteId/documentos/pdf` | menu Geral/detalhe | `{documentType:'pdf', availability, url}` | pending/erro visível; no raw provider shape |
| `GET /api/v1/notas/:noteId/documentos/xml` | menu Geral/detalhe | `{documentType:'xml', availability, url}` | idem |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| backend Jest | contrato Nest/SmartNotas muda | 200/202, errors, auth, noteId, redaction, bounds | fetch loopback/determinístico, sem segredo real | `cd backend && npm test -- --runInBand` | `Local-Implemented` | `planned` | command output | suite completa |
| backend static/build | tipos/wiring/controller | build/lint do módulo | install existente | `cd backend && npm run build && npm run lint` | `Local-Implemented` | `planned` | command output | project-owned |
| frontend unit | API/state/menu | normalização, race, cleanup, no duplicate | DOM/unit fixtures existentes | `cd frontend && npm run test:notas` | `Local-Implemented` | `planned` | command output | deterministic |
| frontend static/build | React/TS/CSS | hooks e bundle | install existente | `cd frontend && npm run lint && npm run build` | `Local-Implemented` | `planned` | command output | project-owned |
| frontend browser | jornada visível | Geral/detalhe/docs/a11y/settings | build fresco, preview e APIs interceptadas | `cd frontend && npm run e2e:notas` | `Local-Implemented` | `planned` | browser report | desktop/mobile |
| Foundation | contrato/guards | TODO, módulo, diff/authority/closeout | baseline publicado | validators/guards declarados | `Completed` | `planned` | outputs | não alegar CI hospedada |

### Runtime / Rollout Notes

- Nenhuma variável, banco, migração ou infra nova.
- Capability usa o mesmo `SMART_NOTAS_READ_ENABLED` e credenciais existentes.
- Smoke real de PDF/XML por contexto e tratamento de URL real pertence ao cutover, redatado.

## Plan Review Gate

- **Gate status:** `prepared-pre-freeze`.
- [ ] Architecture
- [ ] Code Quality
- [ ] Tests
- [ ] Performance
- [ ] Security
- [ ] Elegance
- [ ] Structural Soundness

### Issue Cards

- **Issue ID:** `SEC-01`
  - **Severity:** `high`
  - **Evidence:** OpenAPI entrega URL externa; módulo proíbe URL capturada persistida.
  - **Why it matters now:** URL fiscal não pode virar storage/log nem vetor de esquema inseguro.
  - **Option A (Recommended):** validar HTTPS sem userinfo/fragmento, devolver allowlist efêmera e abrir com `noopener`/`noreferrer`; não buscar no servidor.
    - **Effort:** `medium`; **Risk:** `low`; **Blast radius:** `module`; **Maintenance burden:** `low`; **Performance impact:** `neutral`; **Elegance impact:** `improves`; **Structural soundness impact:** `improves`.
  - **Option B:** proxy/stream do arquivo pelo backend.
    - **Effort:** `high`; **Risk:** `medium`; **Blast radius:** `cross-stack`; **Maintenance burden:** `high`; **Performance impact:** `regresses`; **Elegance impact:** `regresses`; **Structural soundness impact:** `neutral`.
  - **Option C:** expor a resposta SmartNotas sem validação.
    - **Effort:** `low`; **Risk:** `high`; **Blast radius:** `cross-stack`; **Maintenance burden:** `medium`; **Performance impact:** `neutral`; **Elegance impact:** `regresses`; **Structural soundness impact:** `regresses`.
  - **Recommendation:** `Option A`.

- **Issue ID:** `UX-01`
  - **Severity:** `medium`
  - **Evidence:** linha inteira é um `<Link>`; botão não pode ser aninhado nele.
  - **Why it matters now:** nesting inválido causaria navegação acidental e regressão de teclado.
  - **Option A (Recommended):** linha/card como container; link ocupa células e ação é sibling com propagação isolada.
    - **Effort:** `medium`; **Risk:** `low`; **Blast radius:** `local`; **Maintenance burden:** `low`; **Performance impact:** `neutral`; **Elegance impact:** `improves`; **Structural soundness impact:** `improves`.
  - **Option B:** colocar botão dentro do link e cancelar eventos.
    - **Effort:** `low`; **Risk:** `high`; **Blast radius:** `local`; **Maintenance burden:** `medium`; **Performance impact:** `neutral`; **Elegance impact:** `regresses`; **Structural soundness impact:** `regresses`.
  - **Option C:** menu apenas no detalhe.
    - **Effort:** `low`; **Risk:** `low`; **Blast radius:** `local`; **Maintenance burden:** `low`; **Performance impact:** `neutral`; **Elegance impact:** `neutral`; **Structural soundness impact:** `neutral`.
  - **Recommendation:** `Option A`; C não cumpre “em cada nota”.

### Failure Modes & Edge Cases

- [ ] `202` pendente não abre aba vazia e anuncia estado.
- [ ] URL inválida/HTTP/userinfo/fragmento falha fechada sem ecoar valor.
- [ ] clique duplo e troca rápida PDF/XML não entregam resultado tardio incorreto.
- [ ] fechar menu, navegar, logout ou unmount invalida/aborta request.
- [ ] ação `⋮` não navega para detalhe; restante da linha continua navegável.
- [ ] mobile não corta disclosure e settings mantém 44x44.
- [ ] `noteId` adulterado/ID cru/contexto cruzado nunca chama documento errado.

### Residual Unknowns / Risks

- [ ] Browser pode bloquear abertura automática após fetch; fallback visível obrigatório remove o bloqueio funcional.
- [ ] Host real da URL não é normativo no OpenAPI; contrato valida segurança sintática e não faz fetch server-side. Se o produto decidir allowlist de host, isso exige decisão/material scope refresh.

## Additional Architectural Opinions

- **Needed:** `pending audit guard`.
- **Why ambiguity remains:** `nenhuma material após D-01..D-08; guard decide floor`.
- **Opinion count:** `0 pending guard`.
- **Package mode:** `bounded-summary`.
- **Internal reviewer mandate:** `pending audit guard`.
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`.

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo uninotas-foundation/todos/active/features/TODO-uninotas-fiscal-note-documents.md`
- **Latest TEACH evidence / artifact:** `pending pushed freeze`.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | cross-stack read contract |
| `blast_radius` | `cross-stack` | NestJS + React |
| `behavioral_change_or_bugfix` | `yes` | novo acesso documental |
| `changes_public_contract` | `yes` | duas rotas públicas |
| `touches_auth_or_tenant` | `yes` | quatro perfis e contexto fiscal |
| `touches_runtime_or_infra` | `no` | sem deploy/config |
| `touches_tests` | `yes` | backend/frontend/browser |
| `critical_user_journey` | `yes` | conferência fiscal |
| `release_or_promotion_critical` | `yes` | próxima entrega |

## Security Risk Assessment

- **Risk:** `high` pela combinação URL externa, documentos fiscais, PII e credenciais de dois contextos.
- **Controls:** auth/perfis, `noteId` assinado, credenciais backend-only, HTTPS strict, no userinfo/fragment, exact DTO, no-store/no persistence/no logs, `noopener`/`noreferrer`, stable errors, rate/concurrency/timeout/cancel.
- **Required review:** `security-adversarial` conforme audit floor.

## Performance & Concurrency Risk Assessment

- **Risk:** `medium`; cada escolha adiciona uma chamada SmartNotas, sem download/proxy pelo backend.
- **Controls:** zero prefetch, uma chamada por ação, reuse de rate/concurrency, abort/invalidation, disabled while pending.
- **Load claim:** nenhuma; targeted deterministic concurrency/race evidence e suites completas.

## Package-First Verification

- `query_packages.sh --search pdf|download|document` retornou zero package reutilizável em 2026-09-28.
- Decisão: implementação local mínima, sem nova dependência.

## Rules Acknowledgement / Ingestion

| Rule / Workflow | Why In Scope | Status |
| --- | --- | --- |
| `skills/rule-nestjs-nestjs-architecture-always-on/SKILL.md` | boundary NestJS | `loaded for planning; reload after approval` |
| `workflows/nestjs/change-application-boundary-method.md` | novas rotas/controller/port | `loaded for planning; reload after approval` |
| `skills/rule-react-react-architecture-always-on/SKILL.md` | UI state/effects/a11y | `loaded for planning; reload after approval` |
| `workflows/react/change-ui-boundary-method.md` | menu/list/detail | `loaded for planning; reload after approval` |
| `skills/frontend-race-condition-validation/SKILL.md` | resultados tardios/duplicate actions | `planned post-approval` |
| `skills/test-creation-standard/SKILL.md` | testes novos | `planned post-approval` |

## Agent Routing Preflight

- **Planned implementation tuple:** `surface=primary-checkout; role=operational-coder; model=inherited; topology=single-writer`
- **Subagent / delegation authorization:** `not requested; implementation remains root single writer unless separately authorized`.
- **Git isolation authorization:** `not authorized; no worktrees or auxiliary checkouts`.
- **Authority guard:** `pending pre-approval after review convergence`.

## Approval

- **Status:** `pending`.
- **Requested phrase:** `APROVADO`.
- **Authorized scope:** `pending`.
- **Exclusions:** `proxy/persistence/runtime/deploy/worktrees`.
- **Renewal trigger:** qualquer mudança material em contrato público, segurança da URL, perfis, proxy/persistência, runtime ou validação.
