# TODO — Ativar e promover a leitura Smart Notas do UniNotas

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Created:** `2026-09-27`
- **Owner:** `Delphi / Operational DevOps`, sob autoridade humana do usuário
- **Origin:** follow-up obrigatório `R3-CUTOVER-01` do TODO `TODO-uninotas-smart-notas-read-backend.md`

## Context

O backend e o frontend read-only do UniNotas estão implementados e validados localmente, mas ainda são candidatos provisórios: não existe release publicada com a integração habilitada, as variáveis fiscais não foram injetadas no Railway e a autoridade canônica de leitura de notas ainda não foi promovida. Este TODO é o owner exclusivo do cutover operacional da Smart Notas para os contextos fiscais separados `unifast` e `prosperar`.

O artefato de produção é único: o `Dockerfile` da raiz compila o frontend React e o backend NestJS, e o backend serve a SPA na mesma origem. Portanto, frontend e backend devem ser promovidos como uma única release compatível.

## Framing Source & Story Slice

- **Feature brief:** `foundation_documentation/artifacts/feature-briefs/uninotas-smart-notas-central.md`
- **Primary story ID:** `ST-03` (ativação operacional da leitura) + condição transversal `ST-04` (contextos fiscais separados)
- **Why this is the right current slice:** os candidatos locais já existem; o próximo incremento observável é provar, publicar e promover a integração sem transformar o PostgreSQL em fallback de sucesso.
- **Direct-to-TODO rationale:** `n/a — feature brief existente`.

## Contract Boundary

- Este TODO define o que deve ser preparado, implantado, validado e promovido no cutover.
- `Assumptions Preview` e `Execution Plan` definem como o plano pretende entregar o contrato; fatos remotos ainda não comprovados permanecem bloqueadores explícitos.
- A execução exige novo `APROVADO` específico após refinamento, revisão do plano e `preflight-go`.
- Nenhum segredo, token, CNPJ integral, URL assinada ou `noteId` real pode ser copiado para TODO, log, comentário, evidência ou chat.
- O cutover não pode introduzir dual-read silencioso, cache persistente de notas, agregação entre emissores ou uso de `logs` como fonte de notas emitidas com sucesso.
- Descoberta que altere escopo, contrato público, rollback ou topologia aprovada exige atualização deste TODO e aprovação renovada.

## Implementation Intent

- **Current delivery:** preparar e executar uma release coordenada React/NestJS no único `Stage` customer-facing, habilitar a leitura Smart Notas nos dois contextos, provar smoke/rollback e promover o ownership canônico somente depois de comprovar que nenhum consumidor do repositório usa `logs` como fonte de sucesso.
- **Planned next steps:** emissão/cancelamento e DANFE/XML terão TODOs próprios; qualquer consumidor externo de sucesso descoberto bloqueia a promoção e recebe owner/prazo em TODO separado.
- **Anticipatory implementation authorized now:** `none` antes do novo `APROVADO`.
- **Rationale:** uma release única evita combinações incompatíveis entre frontend fiscal e backend com feature flag desligada.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Next exact step:** publicar o baseline reconvergido com os findings arquiteturais integrados, executar revalidação/crítica independente e buscar `preflight-go`; nenhuma mutação Railway está autorizada.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** a topologia customer-facing e o baseline Git estão confirmados; a revisão arquitetural formal é o gate corrente.
- **Exit condition:** fatos remotos confirmados, decisões `D-CUT-06..08` congeladas, revisão pré-aprovação limpa e `todo_authority_guard.py --pre-approval` em `preflight-go`.

## Provisional Notes

- **Missing for production-ready:** checkpoint implantável, configuração remota, probes reais, carga na topologia final, deploy, smoke, rollback ensaiado e promoção Foundation.
- **Revisit criteria:** concluir `DOD-CUT-01..12` com evidência redatada da release exata.
- **Dependencies unblocked:** o código local permite preparar o cutover sem redesenhar contratos de lista/detalhe.

## Blocker Notes

- **Blocker:** nenhuma mutação Railway pode ocorrer antes da revisão formal, `preflight-go` e nova aprovação operacional específica.
- **Why blocked now:** o checkpoint está publicado, mas os gates pré-cutover ainda não convergiram.
- **What unblocks it:** revisão arquitetural sem achados bloqueadores, guards em `preflight-go` e resposta explícita `APROVADO` ao plano operacional congelado.
- **Owner / source:** project Owner confirmado privadamente / painel Railway; o identificador pessoal não é persistido na Foundation.
- **Last confirmed truth:** `Unifast Products / Stage / MonitorNotes / US East / main / Pro`, domínio `https://monitornotes-stage.up.railway.app` e project Owner operador foram confirmados; retenção de 30 dias e janela 20:00–22:00 foram aceitas; health respondeu HTTP 200 com aplicação/banco `ok`.

## Entry Criteria

- [x] Backend read-only concluído como `Local-Implemented, Provisional`, com testes/build/lint e revisões finais aceitos.
- [x] Frontend read-only concluído como `Local-Implemented, Provisional`, com testes/build/lint/browser e revisões finais aceitos.
- [x] `SMART_NOTAS_READ_ENABLED` permanece desligada por padrão no código.
- [x] Nenhum segredo ou identificador fiscal foi versionado nos candidatos.
- [x] Contratos locais distinguem `unifast` e `prosperar` sem agregação.
- [x] Estado candidato exato recebe checkpoint Git publicável antes de qualquer deploy.
- [x] Alvo remoto customer-facing confirmado: `MonitorNotes`, `Stage`, US East, uma réplica, Pro, source `main`.

## Scope

- [x] `CUT-01` Criar checkpoint publicável e reproduzível dos candidatos backend/frontend e da documentação operacional correspondente.
- [ ] `CUT-02` Injetar no secret store Railway os pares independentes token/CNPJ, a chave HMAC e os budgets aprovados, sem imprimir valores.
- [ ] `CUT-03` Executar probe redatado `/empresa`, lista e detalhe para os dois contextos e bloquear mismatch antes de tráfego de usuário.
- [ ] `CUT-04` Iniciar com timeout `10 s`, concorrência `4`, rate `15 req/min` por usuário e `60 req/min` por contexto na única réplica; calibrar somente para baixo ou mediante nova evidência de quota/carga, incluindo respostas válidas próximas de 2 MiB.
- [ ] `CUT-05` Comprovar destino, retenção, acesso e redaction dos logs operacionais antes da ativação.
- [ ] `CUT-06` Provar a imagem exata localmente com readiness, probes Smart Notas redatados, smoke autenticado e jornada de navegador nos dois contextos antes da janela; não existe ambiente Railway isolado.
- [ ] `CUT-07` Antes do deploy, registrar a release Railway verde anterior e comprovar que o Owner consegue acionar seu redeploy; em abort, restaurá-la em até 10 minutos e validar recuperação. A flag é apenas kill switch do provedor.
- [ ] `CUT-08` Executar um único cutover direto no `Stage` customer-facing entre 20:00–22:00, observar por no mínimo 30 minutos e abortar pelos thresholds congelados.
- [ ] `CUT-09` Validar rotação HMAC por substituição da chave e relistagem obrigatória; `noteId` anterior deve falhar fechado.
- [ ] `CUT-10` Promover atomicamente `note_read_model` para Smart Notas nos módulos/ledger somente após smoke e rollback aprovados.
- [ ] `CUT-11` Preservar PostgreSQL `logs` exclusivamente para erros Routerfy/n8n e registrar a retirada dos consumidores legados de sucesso.
- [ ] `CUT-12` Propagar um único correlation ID do request autenticado até o adapter Smart Notas, limitar `actorId` a identificador interno pseudônimo e atualizar `DEPLOY.md` com ordem atômica de variáveis/readiness/deploy/rollback.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `MonitorNotes:delphi-and-foundation`; `uninotas-foundation:main` (canonical main-only documentation authority)
- **Promotion lane path:** `delphi-and-foundation -> main -> Railway validation environment -> Railway production`
- **Lane-promoted threshold for this TODO:** `main com checkpoint aprovado e CI-equivalent verde`
- **Production-ready threshold for this TODO:** `produção com smoke, observação, rollback ensaiado e promoção Foundation concluídos`
- **Execution topology:** `principal checkout, single code writer; worktrees/auxiliary checkouts forbidden`

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR / Main | Validation Environment | Production | Current Status |
| --- | --- | --- | --- | --- | --- |
| Backend + frontend read-only | `delphi-and-foundation@31712a042cab3c796d5daca7350c6c58453e1c73` | `pending promotion to main` | `pending` | `pending` | `published review candidate` |
| Foundation cutover contract | `main@815a0edd5141cc1d44bd5617df5884353fbc10eb` | `n/a — main-only authority` | `n/a` | `pending runtime promotion` | `published reconverged review baseline` |

## Out of Scope

- Emissão/cancelamento, DANFE/XML, relatórios ou exportação.
- Alteração de schema Prisma/PostgreSQL ou persistência de espelho/cache de notas.
- Agregação “Todos”, polling, webhook ou retry automático da Smart Notas.
- Mudança do tratamento das falhas Routerfy/n8n além de manter `logs` como fonte exclusiva desses erros.
- Redesign visual; correção indispensável à compatibilidade exigirá desvio explícito.
- Worktrees, checkouts auxiliares ou branches de reconciliação sem autorização humana separada e nominal.
- Deploy direto em produção sem alvo comprovado, aprovação específica e rollback disponível.

## Decision Baseline (Frozen)

| ID | Decision | Rationale | State |
| --- | --- | --- | --- |
| `D-CUT-01` | Frontend e backend formam uma release Docker indivisível e serão promovidos juntos. | O backend serve o bundle Vite na mesma origem. | `frozen` |
| `D-CUT-02` | Unifast e Prosperar são contextos fiscais separados; não há lista agregada. | Preserva identidade fiscal e contrato aprovado. | `frozen` |
| `D-CUT-03` | Smart Notas é a fonte de sucesso; PostgreSQL `logs` continua somente como fonte de erros. | Evita dual-read e divergência de verdade. | `frozen` |
| `D-CUT-04` | Segredos entram apenas por variáveis seladas do Railway; evidências não contêm valores. | Mantém configuração fora da imagem. | `frozen` |
| `D-CUT-05` | Rollback primário reimplanta a release anterior; flag `false` é kill switch secundário. | A nova UI depende das rotas fiscais. | `frozen` |
| `D-CUT-06` | `Stage` é o único alvo e recebe usuários reais; não existe staging/PR environment. O corte é direto após validação local da imagem exata, durante 20:00–22:00, com risco residual explícito de o primeiro smoke/rollback Railway ocorrer diante de usuários. | Remove a topologia fictícia e torna a limitação operacional parte da aprovação. | `frozen topology; renewed user approval required` |
| `D-CUT-07` | Rotação HMAC invalida `noteId` anterior e exige relistagem; sem grace period neste corte. | IDs são opacos/transitórios; reduz janela de segredo. | `frozen; user accepted 2026-09-27` |
| `D-CUT-08` | Adotar os logs estruturados Railway com retenção Pro de 30 dias neste primeiro cutover; forwarding externo fica como hardening se surgir requisito superior. | O cutover não registra payload fiscal/segredo, e 30 dias cobre diagnóstico inicial sem infraestrutura extra. | `frozen; user accepted 2026-09-27` |
| `D-CUT-09` | Ownership `note_read_model` só muda após smoke e rollback de produção. | Documentação não pode antecipar realidade operacional. | `frozen` |
| `D-CUT-10` | Railway usará readiness separada que responde não-2xx quando PostgreSQL estiver indisponível; liveness não chama Smart Notas e o binding fiscal permanece em probe explícito. | Impede promover release sem autenticação/Erros e evita restart storm por dependência externa. | `frozen; implementation pending approval` |
| `D-CUT-11` | Valores iniciais: timeout `10 s`, concorrência `4`, `15 req/min` por usuário, `60 req/min` por contexto, uma réplica; aumentar qualquer budget exige evidância e renovação do plano. | Limita amplificação enquanto a quota real do provedor é desconhecida. | `frozen initial envelope` |
| `D-CUT-12` | Logs operacionais guardam no máximo correlation ID e `actorId` interno pseudônimo por 30 dias; nunca e-mail/nome/payload fiscal; acesso restrito ao Owner e mantenedores autorizados. | Mantém correlação com minimização de dados. | `frozen` |

## Required Operational Decisions Before Approval

| Decision | Recommended direction | Required evidence | State |
| --- | --- | --- | --- |
| Railway target | `Unifast Products` / `Stage` / `MonitorNotes` / `monitornotes-stage.up.railway.app` / `main` | confirmação redatada + health HTTP 200 | `confirmed` |
| Validation environment | não existe alvo isolado; `Stage` é customer-facing | confirmação do project owner | `confirmed; direct-cutover risk awaits final approval` |
| Secret/rotation owner | project Owner confirmado privadamente; não persistir e-mail | papel informado pelo usuário; revalidar antes da mutação | `confirmed` |
| Replica/region/plan | Pro + US East + uma réplica | confirmação do project owner | `confirmed` |
| Production timeout | iniciar em `10 s`; reduzir se probe mostrar p95 seguro; nunca elevar acima disso neste corte | latência de ambos os contextos | `frozen initial value; validation pending` |
| Concurrency/rates | uma réplica: concorrência `4`, `15 req/min` por usuário e `60 req/min` por contexto | carga + quota/429 do provedor | `frozen initial values; validation pending` |
| Audit retention | 30 dias nos logs Railway; sem forwarding inicial | plano Pro + aprovação do project owner | `confirmed` |
| Cutover window/operator | project Owner; `20:00–22:00 America/Sao_Paulo` | aprovação do project owner + Stage customer-facing | `confirmed` |
| Abort threshold | abort imediato em mismatch/vazamento/readiness; ou `>=2` 429 consecutivos, `>=1%` 429 em 5 min, `>=5%` 5xx/timeout em 5 min com ao menos 20 requests, p95 `>8 s` por 5 min, RSS `>=80%` do limite ou crescimento `>20%` sem recuperar em 10 min | logs/métricas Railway + smoke | `frozen; validate observability before deploy` |

## Diff Expectation Contract

- **Contract status:** `required; baseline checkpoint frozen`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree after candidate checkpoint`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `31712a042cab3c796d5daca7350c6c58453e1c73` | `committed_diff` |
| `uninotas-foundation` | `foundation_documentation` | `815a0edd5141cc1d44bd5617df5884353fbc10eb` | `committed_diff` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `railway.json` | `M` | health/readiness contract if required by approved topology |
| `MonitorNotes` | `DEPLOY.md` | `M` | fiscal cutover/rollback runbook |
| `MonitorNotes` | `README.md` | `M` | production source ownership after successful cutover |
| `MonitorNotes` | `backend/src/health/**` | `A|M` | readiness correction if selected |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M` | bounded probe/capacity/rotation changes |
| `MonitorNotes` | `backend/src/config/**` | `M` | bounded runtime validation |
| `MonitorNotes` | `backend/.env.example` | `M` | approved non-secret production controls |
| `MonitorNotes` | `artifacts/**` | `A|M` | redacted evidence |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-smart-notas-read-cutover.md` | `M|D` | evidence/closeout movement |
| `uninotas-foundation` | `todos/completed/features/TODO-uninotas-smart-notas-read-cutover.md` | `A` | closeout destination |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | promote read ownership |
| `uninotas-foundation` | `modules/runtime-and-deployment.md` | `M` | validated topology/runbook |
| `uninotas-foundation` | `modules/events-and-classification.md` | `M` | retain integration-error ownership |
| `uninotas-foundation` | `artifacts/dependency-readiness.md` | `A|M` | dependency state |
| `uninotas-foundation` | `artifacts/environment-topology.md` | `A|M` | validated Railway topology |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/.env` | `A|M|D|R` | local secrets are not versioned |
| `MonitorNotes` | `frontend/src/**` | `A|M|D|R` | frontend changes need deviation analysis/renewed approval |
| `MonitorNotes` | `backend/prisma/**` | `A|M|D|R` | no schema/data migration |
| `MonitorNotes` | `.github/**` | `A|M|D|R` | CI redesign is not authorized |
| `MonitorNotes` | `Dockerfile` | `A|M|D|R` | change to artifact topology needs renewed approval |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / agent defense | Decision | User validation / renewed approval |
| --- | --- | --- | --- | --- |
| `pending` | `pending` | baseline must be frozen first | `pending` | `pending` |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** scripts/probes redatados, readiness, configuração Railway, runbook, carga e documentação diretamente necessárias ao cutover.
- **Must update or split the TODO:** nova funcionalidade fiscal, mudança visual, persistência, CI/CD novo, agregação, escrita Smart Notas ou mudança de origem.

## Assumptions Preview

| ID | Assumption | Evidence | If False |
| --- | --- | --- | --- |
| `A-CUT-01` | Railway constrói a raiz com `Dockerfile` e publica um serviço único. | `railway.json`, `Dockerfile`, `DEPLOY.md` | atualizar topologia e renovar aprovação |
| `A-CUT-02` | `main` é a branch atualmente conectada ao deploy. | confirmação do project owner em 2026-09-27 + `DEPLOY.md` | corrigir lane path antes do checkpoint |
| `A-CUT-03` | Flag `true` falha no startup se os cinco valores fiscais obrigatórios estiverem ausentes/inválidos. | `backend/src/config/configuration.ts` + specs | bloquear e corrigir validação |
| `A-CUT-04` | O health atual retorna HTTP 2xx com banco degradado e não serve como readiness. | `backend/src/health/health.controller.ts` + `railway.json` | implementar readiness DB-aware e apontar Railway para ela |
| `A-CUT-05` | Railway permite selecionar/reimplantar a release verde anterior, mas a disponibilidade concreta ainda precisa ser atestada no painel. | confirmação do Owner imediatamente antes da janela | abortar o cutover se release/controle não estiverem disponíveis |
| `A-CUT-06` | Domínio, serviço, região e uma réplica estão confirmados e saudáveis; commit servido segue desconhecido. | project-owner confirmation + health HTTP 200; sem CLI autenticada | atestar revision/config imediatamente antes do deploy |
| `A-CUT-07` | Não há consumidor de sucesso em `logs` fora deste repositório. | inventário local é insuficiente para consumidores externos | se falso, bloquear promoção `error-only`, registrar owner/prazo e manter estado provisório |

## Execution Plan

1. Confirmar e registrar topologia Railway sem valores secretos.
2. Congelar checkpoint Git dos candidatos e Foundation; não implantar working tree não identificado.
3. Fechar readiness, capacidade, sink e janela; revisar plano e obter `APROVADO`.
4. Reexecutar CI-equivalent completo e build Docker no checkpoint exato.
5. Executar localmente a imagem exata com configuração fail-closed, probes redatados dos dois emissores, carga near-limit e browser smoke autenticado; nenhuma evidência local substitui o risco do único alvo customer-facing.
6. Atualizar o runbook e implementar readiness PostgreSQL-aware separada de liveness; confirmar que Railway usará a readiness sem chamar Smart Notas em loop.
7. No painel Railway, registrar de forma redatada a release verde anterior, revision candidata, diff de configuração, acesso aos logs e disponibilidade da ação de redeploy; abortar antes da mutação se faltar qualquer item.
8. Preparar os segredos/limites selados e executar um único deploy atômico do candidato já habilitado em `Stage`, dentro de 20:00–22:00; não usar a flag desligada como falsa validação da nova UI.
9. Executar imediatamente smoke de API/navegador para os dois contextos, `/erros`, correlação, redaction e ausência de fallback; observar por no mínimo 30 minutos.
10. Em qualquer abort condition, acionar kill switch se necessário para conter o provedor e reimplantar a release anterior em até 10 minutos; validar login, `/erros` e UI anterior.
11. Inventariar consumidores de `/eventos`/`logs`; promover módulos/ledger para Smart Notas + error-only somente se nenhum consumidor de sucesso permanecer. Descoberta externa bloqueia a promoção, não o rollback da release.

## Health, Readiness and Rollback Contract

- Healthcheck Railway não substitui probe externo nem monitoramento contínuo.
- Health não deve chamar Smart Notas a cada probe: indisponibilidade transitória não deve causar restart storm.
- Criar readiness separada (rota alvo a ser fixada na implementação, preferencialmente `/api/v1/prontidao`) que responde não-2xx se PostgreSQL estiver indisponível; `/api/v1/saude` permanece liveness simples.
- Binding token/CNPJ é comprovado por probe pré-tráfego, nunca por conteúdo sensível no health.
- Rollback primário: redeploy da release anterior verde, identificada e acessível no painel antes do corte; RTO máximo `10 min` desde o abort.
- Kill switch: `SMART_NOTAS_READ_ENABLED=false`; corta o provedor, mas não restaura integralmente a nova tela `Geral`.

## Abort Conditions

- Mismatch token/CNPJ em qualquer contexto.
- Segredo, CNPJ integral, recurso upstream, URL assinada ou identificador sensível em saída não autorizada.
- Falha de startup/readiness, lista/detalhe ou browser em qualquer contexto.
- Fallback para `logs`, sucesso vazio mascarando erro, mistura ou acesso cross-context.
- `>=2` respostas 429 consecutivas ou `>=1%` de 429 em 5 minutos.
- `>=5%` de 5xx/timeout em 5 minutos com ao menos 20 requisições, ou p95 `>8 s` durante 5 minutos.
- RSS `>=80%` do limite Railway ou crescimento `>20%` sem recuperar em 10 minutos; qualquer saturação que impeça smoke também aborta.
- Sink ausente/inacessível ou retenção abaixo da política.
- Release anterior/redeploy indisponível antes do corte, ou restauração não concluída em 10 minutos após abort.

## Definition of Done

- [x] `DOD-CUT-01` Checkpoint backend/frontend/Foundation é identificado, publicável e reproduzível.
- [x] `DOD-CUT-02` Alvo Railway e responsáveis são registrados redatados e confirmados pelo usuário.
- [ ] `DOD-CUT-03` Os dois pares fiscais são validados contra a empresa esperada sem exposição de segredo/CNPJ.
- [ ] `DOD-CUT-04` Timeout, rate, concorrência e bytes/memória são calibrados para a topologia real sob carga near-limit.
- [ ] `DOD-CUT-05` Logs têm sink, retenção, acesso e redaction comprovados.
- [ ] `DOD-CUT-06` Imagem exata passa localmente em readiness, probes, API smoke, browser smoke e `/erros`; a ausência de alvo Railway isolado permanece risco aceito, não evidência simulada.
- [ ] `DOD-CUT-07` Release anterior e controle de redeploy são comprovados antes do corte; se acionado, rollback restaura a UI anterior em até 10 minutos.
- [ ] `DOD-CUT-08` `Stage` customer-facing passa em lista/detalhe para ambos sem fallback/mistura por no mínimo 30 minutos na janela.
- [ ] `DOD-CUT-09` Rotação HMAC falha fechado para ID antigo e relistagem produz IDs válidos.
- [ ] `DOD-CUT-10` Ownership é promovido somente após smoke, inventário de consumidores e prova de que `events-and-classification`/`logs` servem apenas erros; consumidor externo desconhecido mantém a promoção bloqueada.
- [ ] `DOD-CUT-11` Railway usa readiness PostgreSQL-aware não-2xx, liveness não chama Smart Notas e o runbook descreve variáveis fiscais, ordem atômica e rollback.
- [ ] `DOD-CUT-12` Logs unem request e upstream pelo mesmo correlation ID e retêm por 30 dias somente metadados redatados/`actorId` pseudônimo com acesso restrito.

## Validation Steps

- [ ] `VAL-CUT-01` Executar `bash delphi-ai/verify_context.sh` no contexto compatível e exigir `PACED-Ready`.
- [ ] `VAL-CUT-02` Reexecutar suites CI-equivalent backend, frontend e Foundation no checkpoint.
- [ ] `VAL-CUT-03` Construir imagem raiz e provar startup/health com flag desligada e configuração inválida falhando fechada.
- [ ] `VAL-CUT-04` Executar `SMART_NOTAS_PROBE_ENABLED=true` somente em runner autorizado, com saída redatada, nos dois contextos.
- [ ] `VAL-CUT-05` Executar carga near-2MiB no candidato local com budgets `10 s/4/15/60` e registrar p95/p99, 429/5xx/timeout, RSS/heap e recuperação; confirmar métricas Railway antes do corte.
- [ ] `VAL-CUT-06` Executar smoke autenticado dos GETs e jornada browser `Geral -> detalhe -> Erros -> Geral` nos dois contextos.
- [ ] `VAL-CUT-07` Inspecionar logs/respostas por padrão sensível sem registrar os valores pesquisados.
- [ ] `VAL-CUT-08` Ensaiar redeploy da release anterior e recuperação do candidato.
- [ ] `VAL-CUT-09` Executar `cutover_integrity_audit` e provar ausência de bridge/dual-read de sucesso.
- [ ] `VAL-CUT-10` Rodar guards Delphi de autoridade, diff, CI, revisão, completion e Foundation conforme a fase.
- [ ] `VAL-CUT-11` Forçar PostgreSQL indisponível em ambiente local controlado e comprovar readiness não-2xx enquanto liveness do processo permanece bounded.
- [ ] `VAL-CUT-12` Correlacionar um request sintético ponta a ponta e revisar logs por PII/payload/segredo sem persistir os valores pesquisados.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-CUT-01` | Definition of Done | checkpoint | git/build | `31712a042cab3c796d5daca7350c6c58453e1c73` + build verde | local/CI | `passed` | checkpoint publicado |
| `DOD-CUT-02` | Definition of Done | alvo/responsáveis | doc/manual | `environment-topology.md` redatado | Railway | `passed` | Owner/topologia confirmados |
| `DOD-CUT-03` | Definition of Done | binding emissores | runtime | live probe redatado | local authorized runner | `planned` | ambos os contextos antes da janela |
| `DOD-CUT-04` | Definition of Done | capacidade | load | relatório RLS near-limit | local exact image + Railway metrics | `planned` | budgets iniciais congelados |
| `DOD-CUT-05` | Definition of Done | auditoria | runtime/review | política + consulta redatada | Railway | `planned` | 30 dias confirmados; provar acesso/redaction |
| `DOD-CUT-06` | Definition of Done | smoke pré-cutover | runtime/browser | API + browser evidence | local exact image | `planned` | sem alegar staging inexistente |
| `DOD-CUT-07` | Definition of Done | rollback | runtime | deployment IDs redatados + restore se acionado | Railway Stage | `planned` | alvo e controle antes do corte; RTO 10 min |
| `DOD-CUT-08` | Definition of Done | cutover | runtime/browser | smoke + observação 30 min | Railway Stage customer-facing | `planned` | corte direto na janela aprovada |
| `DOD-CUT-09` | Definition of Done | HMAC | test/runtime | relistagem após rotação | local exact image/Stage | `planned` | sem chave antiga |
| `DOD-CUT-10` | Definition of Done | promoção | doc/validator | module diffs + validator | Foundation | `planned` | após produção verde |
| `DOD-CUT-11` | Definition of Done | readiness/runbook | test/doc/runtime | HTTP negative test + `railway.json` + `DEPLOY.md` | local/Railway | `planned` | sem probe Smart Notas no health loop |
| `DOD-CUT-12` | Definition of Done | correlação/privacy | test/log review | request ID end-to-end + redaction evidence | local/Railway | `planned` | actor interno, sem e-mail/nome |
| `VAL-CUT-01..12` | Validation Steps | validações | mixed | preencher cada evidência durante execução | mixed | `planned` | agregado não substitui linhas no closeout |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas API | fonte/binding | `unknown` | `2026-09-27 local config only` | probe não executado neste cutover | bloquear ativação |
| Railway control plane | deploy/vars/logs/rollback | `degraded` | `2026-09-27` | target/scale/operator confirmados; sem CLI autenticada | revalidar revision/config imediatamente antes da mutação |
| Railway `Stage` | smoke/cutover customer-facing | `healthy` | `2026-09-27` | `/api/v1/saude` HTTP 200 + project-owner confirmation | cutover direto somente após gates e aprovação final |
| PostgreSQL Railway | auth e erros | `healthy` | `2026-09-27` | health público reportou `banco: ok` | ainda falta smoke do checkpoint candidato |

## Profile Scope & Handoffs

- **Primary execution profile:** `operational-devops`
- **Active technical scope:** `railway,nestjs,react,vite,cross-stack`
- **Expected supporting profiles:** `operational-coder, assurance-security-adversarial, assurance-tester-quality`
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-devops`

| From Profile | To Profile | Why | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `operational-devops` | `operational-coder` | readiness/probe/runbook code | backend/root | `planned after approval` |
| `operational-devops` | `assurance-security-adversarial` | secrets/redaction/isolation | runtime/logs/config | `required before production` |
| `operational-devops` | `assurance-tester-quality` | smoke/load/rollback | validation lanes | `required before production` |

## Complexity

- **Level:** `big`
- **Checkpoint policy:** `section-by-section: published checkpoint -> exact-image local validation -> direct Stage cutover -> 30-minute observation -> conditional canonical promotion`
- **Why this level:** release crítica cross-stack, dois contextos fiscais, dependência externa, segredos, capacidade, observabilidade e rollback real.

## Canonical Module Anchors

- **Primary module doc:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Secondary module docs:** `foundation_documentation/modules/runtime-and-deployment.md`; `foundation_documentation/modules/events-and-classification.md`
- **Planned decision promotion targets:** ownership de `note_read_model`, topologia/rollback e `logs` error-only.
- **Module decision consolidation targets:** source of truth, runtime topology e boundaries nos três módulos.

## Module Coherence Gate

- **Gate status:** `no_material_findings`
- **Findings summary:** `events-and-classification` ainda documenta o runtime legado de `logs`, enquanto `fiscal-notes-and-documents` permanece target-planned; essa sobreposição é provisória e não autoriza promoção antecipada.
- **Promotion rule:** somente promover `note_read_model` e afirmar `logs error-only` após smoke e inventário de consumidores; qualquer consumidor externo de sucesso mantém o estado provisório.
- **Evidence / reference:** `modules/fiscal-notes-and-documents.md`, `modules/events-and-classification.md`, `modules/runtime-and-deployment.md` e `D-CUT-03/D-CUT-09`.

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** o cutover muda a autoridade operacional de `note_read_model` para Smart Notas e consolida `logs` como fonte exclusiva de erros de integração.
- **Deviation / debt being retired:** reconstrução ou apresentação de notas emitidas com sucesso a partir do PostgreSQL `logs`, além da ausência de binding operacional comprovado dos dois emissores.
- **Target steady-state after closeout:** `Geral` e detalhe leem somente Smart Notas por `FiscalIssuerContext`; `Erros` lê somente falhas Routerfy/n8n; uma release Docker única serve frontend/backend habilitados e observáveis.
- **Temporary exceptions allowed:** coexistência técnica das rotas `/eventos` exclusivamente para o fluxo de erros; nenhum consumidor conhecido pode continuar apresentando sucesso a partir de `logs`. Consumidor externo descoberto não recebe exceção silenciosa: bloqueia a promoção e exige owner/prazo/TODO.
- **Cutover / removal condition:** smoke e rollback aprovados nos dois contextos, janela estável e promoção canônica; consumidores de sucesso remanescentes saem de `/eventos` por owner/critério registrado.
- **Promotion timing:** somente depois de smoke e rollback de produção; antes disso este TODO é a verdade provisória.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| Smart Notas-only success source | `D-CUT-03` + project constitution | `/notas`, Geral e detalhe | impede autoridade concorrente e sucesso divergente |
| Context binding server-side | `D-CUT-02` + fiscal module invariant | Unifast/Prosperar config, adapter and routes | impede token/CNPJ arbitrário e mistura fiscal |
| Atomic same-image release | `D-CUT-01` | root Docker artifact + Railway service | impede frontend fiscal apontar para backend desabilitado |
| Release rollback, flag kill switch | `D-CUT-05` | Railway deployments and runtime config | restaura UI/API compatíveis e mantém corte emergencial do provedor |
| Redacted structured operations | `D-CUT-04`, `D-CUT-08` | variables, probes, logs and evidence | protege segredos/dados fiscais e mantém diagnóstico por 30 dias |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why Forbidden | Exception Policy |
| --- | --- | --- | --- |
| Fallback de sucesso para `logs` | `/notas` ou Geral consultando Prisma/logs após falha Smart Notas | mascara indisponibilidade e cria duas verdades | `none` |
| Deploy de frontend/backend separados | commits/imagens diferentes no mesmo cutover | quebra compatibilidade da rota Geral | `none` |
| Flag-only tratada como rollback completo | nova UI permanece publicada com fiscal off | Geral fica indisponível | somente kill switch temporário enquanto release anterior é reimplantada |
| Probe/health expondo ou chamando segredo em loop | valores fiscais em output ou Smart Notas chamada por todo healthcheck | vazamento/restart storm | `none` |
| Escala sem budget agregado | `replicas × concurrency/rate` acima do aprovado | multiplica quota/memória silenciosamente | exige nova calibração e aprovação |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan |
| --- | --- | --- | --- | --- | --- |
| structural/test | backend fiscal boundary | existing fiscal module/contract/structure specs | Prisma/logs fallback, public credential input, context leak | `already-enforced` | rerun obrigatório em `VAL-CUT-02` |
| config test | bootstrap variables | configuration specs with flag false/true-invalid | enable sem pares fiscais/HMAC ou valores fora de bound | `already-enforced` | rerun obrigatório em `VAL-CUT-03` |
| read-only runtime probe | Smart Notas binding | `smart-notas-live.probe.spec.ts` | token/CNPJ mismatch, lista/detail indisponível | `already-enforced` | execução real obrigatória em `VAL-CUT-04` |
| load/stress | external path and 2 MiB envelope | RLS report on approved topology | saturation, quota amplification, memory/recovery failure | `implement-in-this-todo` | `VAL-CUT-05` |
| browser smoke | same-origin React/Nest release | source-owned fiscal browser journey | incompatible UI/API, context/cache leak, `/erros` regression | `implement-in-this-todo` | `VAL-CUT-06` |
| operational drill | Railway deployment | previous-release redeploy + candidate recovery | rollback unavailable or stale revision | `manual-only-with-rationale` | Railway rollback é ação operacional real; evidência em `VAL-CUT-08` |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after review baseline freeze and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set: TODO + topology/dependency artifacts + railway/Docker/config/health/fiscal boundaries`
- **Decision review status:** `findings_integrated`
- **Decision review evidence / resolution:** reviewer `/root/cutover_architecture_opinion` retornou `BLOCKED` com 8 findings; o plano removeu a topologia isolada inexistente, congelou readiness, budgets/abort/RTO, tornou a promoção error-only condicional ao inventário, exigiu correlation ID ponta a ponta e incluiu atualização do runbook. Revalidação independente ainda é obrigatória antes de `preflight-go`.

| Finding ID | Severity | Approval-material | Resolution | Evidence in evolved plan |
| --- | --- | --- | --- | --- |
| `ARCH-01` | critical | yes | `Integrated` | `D-CUT-06`, Execution Plan e DOD removem staging fictício e declaram corte direto. |
| `ARCH-02` | high | yes | `Integrated` | `D-CUT-10` congela readiness PostgreSQL-aware separada de liveness. |
| `ARCH-03` | high | yes | `Integrated` | `D-CUT-11`, Abort Conditions e `CUT-04` congelam budgets/thresholds iniciais. |
| `ARCH-04` | high | yes | `Integrated` | release anterior obrigatória antes do corte, Owner, RTO `10 min` e risco residual explícito. |
| `ARCH-05` | high | yes | `Integrated` | promoção error-only depende de inventário; consumidor externo bloqueia promoção. |
| `ARCH-06` | medium | yes | `Integrated` | estados/topologia/perguntas foram alinhados; novo baseline ainda deve ser publicado. |
| `ARCH-07` | medium | no | `Integrated` | `CUT-12`/`DOD-CUT-12` exigem correlation ID ponta a ponta e retenção minimizada. |
| `ARCH-08` | medium | yes | `Integrated` | `CUT-12`/`DOD-CUT-11` tornam a atualização de `DEPLOY.md` parte do corte. |
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before cutover closeout`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `exact deployed revision + TODO + runtime evidence`
- **Adherence review status:** `pending`
- **Adherence review evidence / resolution:** `not run; no cutover implementation/deploy exists`.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** release, segredos, dois contextos e promoção canônica exigem revisão reproduzível.
- **Trigger stage:** `before first planning-side review or guard run`
- **Baseline branch:** `MonitorNotes:delphi-and-foundation` + `uninotas-foundation:main`
- **Baseline commit:** `MonitorNotes@31712a042cab3c796d5daca7350c6c58453e1c73` + `uninotas-foundation@815a0edd5141cc1d44bd5617df5884353fbc10eb`.
- **Baseline push reference:** `MonitorNotes/delphi-and-foundation` + `uninotas-foundation:main`; ambos publicados e resolvidos remotamente para os SHAs registrados.
- **Gate status:** `no_material_findings`
- **Findings summary:** pacote reconvergido com `ARCH-01..08` foi publicado na autoridade Foundation main-only; código candidato permanece no checkpoint funcional imutável.
- **Evidence / reference:** push Foundation `6fbd343..815a0ed`; `rev-parse`/`ls-remote` iguais em `815a0edd5141cc1d44bd5617df5884353fbc10eb`; MonitorNotes remoto preservado em `31712a0` para a revisão funcional.
- **Waiver authority / reference:** `n/a`.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impede alteração material entre o pacote revisado e o aprovado.
- **Trigger stage:** `after review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Decision Baseline|Architecture Change Governance|Assumptions Preview|Execution Plan|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- **Gate status:** `blocked`
- **Findings summary:** a architecture opinion identificou drift material necessário no plano; o baseline original permanece rastreado, mas o pacote reconvergido precisa de novo checkpoint/review antes do guard poder retornar `go`.
- **Evidence / reference:** reviewer `/root/cutover_architecture_opinion`; findings topology/readiness/capacity/rollback/error-only/runbook integrados no TODO.
- **Waiver authority / reference:** `n/a`.

## Test Strategy

- **Strategy:** verification-first para deploy; nenhuma mutação fiscal externa.
- **Local:** suites, fail-closed config, build Docker, lint/build e Foundation.
- **External read-only:** `/empresa`, lista e detalhe nos dois contextos.
- **Browser:** imagem exata local com fingerprint e interceptação controlada; depois smoke imediato no único `Stage` customer-facing.
- **Capacity:** latência, quota, concorrência e memória near-limit.
- **Rollback:** release anterior identificada/acionável antes do corte; restore real somente em abort porque não há alvo isolado, com risco residual explicitamente aprovado e RTO de 10 minutos.

## Local CI-Equivalent Suite Matrix

| Repository / Surface | Why In Scope | Command / Gate | Required Before | Status |
| --- | --- | --- | --- | --- |
| backend NestJS | fiscal/config/health | `npm test`, lint e build do pacote | checkpoint/deploy | `planned rerun` |
| frontend React/Vite | bundle na mesma imagem | fiscal unit/race/e2e + lint + build | checkpoint/deploy | `planned rerun` |
| root Docker | artefato Railway | build + startup/health smoke | validation deploy | `planned` |
| Foundation | owner/contract | deterministic + Foundation validator | approval/closeout | `in progress` |
| live provider | binding/read-only | live redacted probe | enable | `blocked` |
| Railway browser | experiência real | browser smoke contra fingerprint | production-ready | `blocked` |

## Plan Review Gate

- **Review decision:** `required`
- **Review status:** `findings_integrated; independent reconfirmation pending`
- **Required lenses:** architecture, operations, rollback, security, tests, performance, observability and structural soundness.
- **Known plan finding:** o health atual retorna HTTP 2xx quando o banco está degradado; `D-CUT-10` agora exige readiness separada não-2xx e mantém Smart Notas fora do loop.
- **Approval request condition:** nova revisão confirma `D-CUT-06..12`, crítica converge, baseline é atualizado e guards retornam `go/preflight-go`.

## Security Risk Assessment

- **Risk level:** `high`
- **Why this risk level:** dois tokens fiscais, CNPJs, HMAC, dados autenticados e configuração de produção.
- **Attack surface in scope:** secret store, logs, probes, binding, noteId, deploy output, responses e rollback.
- **Attack simulation decision:** `required before production`
- **Required result:** nenhum vazamento, cross-context, SSRF/redirect ou aceitação de noteId antigo/corrompido.
- **Current status:** `pending`.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `high`
- **Why this level:** cada réplica multiplica concorrência/rate contra API externa; payload aceito pode chegar a 2 MiB.
- **Current delivery stage at review time:** `Pending, Provisional, review`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `required` | `high` | `EPS-EXTERNAL-DATA-PATH` | `before_enable` | provider latency/body evidence | `planned` | quota unknown | `external_topology_unknown` |
| `FRC` | `frontend-race-condition-validation` | `required` | `medium` | `FRC-REAL-BACKEND-CUTOVER` | `before_production` | real browser context/cache switch | `planned` | mocks passed | `runtime_target_unknown` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `BCI-READ-ONLY` | `n/a` | policy justification | `not_applicable` | no write | `none` |
| `RLS` | `runtime-load-stress-validation` | `required` | `high` | `RLS-REPLICA-EXTERNAL-QUOTA-MEMORY` | `before_enable` | production-like load/recovery/body | `planned` | provider quota unknown | `provider_quota_unknown` |

## Audit and Independent Review Gates

- **Audit escalation:** `required; high-risk release and runtime/infra change`.
- **Independent no-context critique:** `required after plan freeze and before APROVADO`.
- **Independent test-quality audit:** `required before production`.
- **Independent final review:** `required after implementation and before production`.
- **Dedicated triple review:** `required because release-critical + secrets + external provider`.
- **Current status:** `audit floor derived; architecture opinion running; critique pending`.

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- **Latest TEACH evidence / artifact:** `Overall outcome: go`; fingerprint `453bba9462e3`; floor derivado em 2026-09-27.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `big` | Release cross-stack com dois contextos fiscais e rollback real. |
| `blast_radius` | `cross-stack` | React, NestJS, imagem Docker e runtime Railway. |
| `behavioral_change_or_bugfix` | `yes` | Geral passa a ler Smart Notas como fonte de sucesso. |
| `changes_public_contract` | `yes` | Rotas autenticadas `/notas` e semântica de contexto fiscal entram no produto. |
| `touches_auth_or_tenant` | `yes` | Acesso autenticado e isolamento entre contextos fiscais devem permanecer fechados. |
| `touches_runtime_or_infra` | `yes` | Variáveis, release, health, rollback e observação Railway. |
| `touches_tests` | `yes` | Suites backend/frontend, probe, carga e browser fazem parte do corte. |
| `critical_user_journey` | `yes` | Central de notas será usada pelos setores autorizados. |
| `release_or_promotion_critical` | `yes` | O TODO governa promoção e cutover customer-facing. |
| `high_severity_plan_review_issue` | `yes` | Não existe ambiente isolado e `Stage` recebe usuários reais. |
| `explicit_three_lane_request` | `yes` | O próprio contrato exige dedicated triple review para o release crítico. |

## Independent No-Context Critique Gate (Deterministic Floor From Audit Escalation)

- **Critique decision:** `required`
- **Why this decision:** baseline obrigatório com profundidade expandida por blast radius cross-stack, contrato público, jornada crítica e release customer-facing.
- **Impact signals in scope:** `cross-module blast radius|public contract/schema/api|auth/tenant isolation|runtime/infra|high-severity direct-cutover issue`
- **Package mode:** `bounded-file-set`
- **Package minimum contents:** `frozen baseline|scope|assumptions|execution plan|issue cards|residual risks|blockers`
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required; dispatch after architecture_opinion convergence`
- **Canonical multi-lane audit protocol (when required):** `audit-protocol-triple-review; additive delivery-side gate before Completed`
- **Audit session / round evidence (when protocol used):** `pending post-implementation evidence`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `not_run`
- **Findings summary:** `pending architecture_opinion convergence`
- **Evidence / reference:** audit guard fingerprint `453bba9462e3`, `critique=required`, depth `expanded`.
- **Waiver authority / reference (required if waived):** `n/a`

## Verification Debt Assessment

- **Decision:** `required`
- **Gate deadline:** `before_completed`
- **Current status:** `planned`
- **Reason / evidence:** `VDA-MEDIUM-BIG-OR-RELEASE`; validar dívidas e evidências pendentes após execução.

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** testes, mudança comportamental, contrato público, jornada crítica e promoção estão em escopo.
- **Gate deadline:** `before_completed`
- **Depth:** `full`
- **Audit status:** `not_run`
- **Evidence / reference:** audit guard fingerprint `453bba9462e3`; execução é delivery-side.

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** `FINAL-BASELINE-ALWAYS` + sinais de risco cross-stack/release-critical.
- **Gate deadline:** `before_completed`
- **Depth:** `expanded`
- **Final review status:** `not_run`
- **Evidence / reference:** audit guard fingerprint `453bba9462e3`; execução é delivery-side.

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- **Gate status:** `blocked`
- **Evidence / reference:** executar depois que a topologia for confirmada e antes do pedido de `APROVADO`; validar `A-CUT-01..06` contra o checkpoint candidato e os artefatos de ambiente.

## Approval

- **Status:** `not_requested`
- **Approved by:** `n/a`
- **Approval reference:** `n/a`
- **Approval scope:** `pending frozen cutover plan`
- **Implementation authority:** `none`
- **Required approval:** resposta explícita `APROVADO` após `preflight-go`; aprovações backend/frontend não autorizam deploy deste TODO.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/skills/rule-docker-shared-core-instructions-always-on/SKILL.md` | governança Delphi | gates/evidência/autoridade | planejamento como deploy autorizado | TODO bloqueado |
| `delphi-ai/skills/rule-docker-shared-project-mandate-always-on/SKILL.md` | mandato | Smart Notas sucesso; logs erros | dual-read/fallback | cutover audit |
| `delphi-ai/skills/rule-docker-shared-todo-driven-execution-model-decision/SKILL.md` | tactical TODO | preflight/approval/diff | implementar antes do APROVADO | authority none |
| `delphi-ai/skills/rule-docker-shared-environment-topology-contract-model-decision/SKILL.md` | alvo desconhecido | fatos/user validation | inventar target | topology artifact |
| `delphi-ai/skills/rule-railway-railway-deployment-contract-always-on/SKILL.md` | deploy | vars/health/rollback | produção sem evidence | staged config |
| `delphi-ai/skills/rule-nestjs-nestjs-architecture-always-on/SKILL.md` | readiness | boundaries/fail-closed | restart storm | review health |
| `delphi-ai/skills/rule-react-react-architecture-always-on/SKILL.md` | SPA smoke | context/session/cache isolation | hidden fallback | runtime journey |
| `delphi-ai/skills/rule-vite-vite-build-runtime-always-on/SKILL.md` | bundle | same-origin/provenance | dev proxy como produção | fingerprint |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `todo-approval`
- **Selected role:** `primary-chat`
- **Selected model:** `gpt-5.4`
- **Selected effort:** `highest_review_tier`
- **Proof mode:** `declared`
- **Execution topology:** `primary-checkout-single-writer`
- **Subagent / delegation authorization:** `not requested for this turn`
- **Worktree authorization:** `not-authorized`
- **Guard outcome:** `go`
- **Guard evidence:** perfil/scope declarados; principal checkout, single writer e nenhuma delegação/worktree solicitada; não concede autoridade de execução.

## Questions To Close

- `approval final deve aceitar explicitamente o cutover direto no único Stage customer-facing, o risco de o primeiro rollback Railway ocorrer com usuários, os thresholds/RTO congelados e retenção por 30 dias do actorId interno pseudônimo.`

## Early Approval Signal

- **Received:** `Aprovado`, em 2026-09-27, incluindo autorização contextual para os checkpoints Git propostos.
- **Accepted decisions:** `D-CUT-07`, avanço do cutover e commit/push do candidato para revisão.
- **Authority effect:** `checkpoint Git concluído`; não autoriza deploy, alteração de variáveis Railway nem tráfego fiscal.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Reason:** contrato e checkpoint publicados; revisões e gates operacionais ainda precedem qualquer implementação remota/deploy.
