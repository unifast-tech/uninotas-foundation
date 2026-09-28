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
- **Next exact step:** executar confirmação arquitetural round 7 e crítica independente sobre o baseline publicado, depois coherence/authority guards e `preflight-go`; nenhuma mutação Railway está autorizada.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** a topologia customer-facing e o baseline Git estão confirmados; a revisão arquitetural formal é o gate corrente.
- **Exit condition:** fatos remotos confirmados, decisões `D-CUT-06..08` congeladas, revisão pré-aprovação limpa e `todo_authority_guard.py --pre-approval` em `preflight-go`.

## Provisional Notes

- **Missing for production-ready:** implementação reconvergida, configuração remota, probes reais, carga local do build candidato, attestation do rollback target, rebuild/cutover/smoke no Stage e promoção Foundation.
- **Revisit criteria:** concluir `DOD-CUT-01..14` com evidência redatada da release exata.
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
- [ ] `CUT-04` Exigir no startup timeout `10 s`, concorrência `4`, rate `15 req/min` por usuário e `60 req/min` por contexto na única réplica; validar esse envelope com carga/respostas próximas de 2 MiB. Qualquer mudança exige rebaseline e nova aprovação.
- [ ] `CUT-05` Comprovar destino, retenção, acesso e redaction dos logs operacionais antes da ativação.
- [ ] `CUT-06` Provar localmente a tree candidata com build Docker, readiness, probes Smart Notas redatados, smoke autenticado e jornada de navegador nos dois contextos; Railway fará rebuild remoto e os bits reais só serão validados pelo smoke no Stage.
- [ ] `CUT-07` Antes do deploy, registrar a release Railway verde anterior e comprovar que o Owner consegue acionar seu redeploy; em abort, restaurá-la em até 10 minutos e validar recuperação. A flag é apenas kill switch do provedor.
- [ ] `CUT-08` Executar um único cutover direto no `Stage` customer-facing entre 20:00–22:00, observar por no mínimo 30 minutos e abortar pelos thresholds congelados.
- [ ] `CUT-09` Validar rotação HMAC por substituição da chave e relistagem obrigatória; `noteId` anterior deve falhar fechado.
- [ ] `CUT-10` Promover atomicamente `note_read_model` para Smart Notas nos módulos/ledger somente após smoke e rollback aprovados.
- [ ] `CUT-11` Tornar PostgreSQL `logs` exclusivamente uma fonte de erros Routerfy/n8n no boundary do produto: um predicado central derivado da classificação original nega `SUCESSO` em lista, resumo, produtos, exportação, detalhe, payload, tratamento unitário/lote, monitoramento, realtime e UI. Inventário/attestation de consumidores externos é gate antes do deploy.
- [ ] `CUT-12` Propagar um único correlation ID do request autenticado até o adapter Smart Notas, limitar `actorId` a identificador interno pseudônimo e atualizar `DEPLOY.md` com ordem atômica de variáveis/readiness/deploy/rollback.
- [ ] `CUT-13` Promover por PR apenas uma tree Git equivalente ao candidato validado; registrar candidate SHA/tree OID, final main SHA/tree OID e revision Railway. A imagem local é evidência source-level, não o OCI implantado; mismatch de tree bloqueia/aborta, e o primeiro smoke Stage valida os bits do rebuild remoto.
- [ ] `CUT-14` Manter `uninotas-foundation:main` como autoridade independente após a promoção canônica; não sincronizar o gitlink documental em `MonitorNotes:main` neste closeout para evitar segundo auto-deploy. Registrar follow-up para o próximo release aprovado.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `MonitorNotes:delphi-and-foundation`; `uninotas-foundation:main` (canonical main-only documentation authority)
- **Promotion lane path:** `delphi-and-foundation candidate tree -> local source/build validation -> PR with identical final tree on main -> Railway remote rebuild -> single Stage customer-facing cutover -> independent Foundation runtime promotion`
- **Lane-promoted threshold for this TODO:** `main com checkpoint aprovado e CI-equivalent verde`
- **Production-ready threshold for this TODO:** `Stage customer-facing com smoke e 30 minutos de observação; rollback target atestado e, se acionado, restaurado em até 10 minutos; promoção Foundation concluída`
- **Execution topology:** `principal checkout, single code writer; worktrees/auxiliary checkouts forbidden`

## Promotion Evidence

| Scope Item | Local Branch/Commit | Main / Authority | Local Source/Build Validation | Single Remote Target: Stage Customer-Facing | Current Status |
| --- | --- | --- | --- | --- | --- |
| Backend + frontend read-only | implementation baseline `delphi-and-foundation@922957f`; code-origin `31712a0` | `pending promotion to main` | `pending final cutover suite` | `pending one direct cutover` | `published round-7 implementation baseline` |
| Foundation cutover contract | `main@cdf6fb1a1308e462d137e12b3c48c9b6d080f0f5` | `main-only authority` | `n/a` | `pending runtime promotion after observed cutover` | `published round-7 material baseline` |

## Out of Scope

- Emissão/cancelamento, DANFE/XML e novos relatórios/exportações fiscais Smart Notas; a exportação legada de `/eventos` permanece em escopo apenas para restringi-la a erros.
- Alteração de schema Prisma/PostgreSQL ou persistência de espelho/cache de notas.
- Agregação “Todos”, polling, webhook ou retry automático da Smart Notas.
- Mudança de escrita das falhas Routerfy/n8n; o boundary `/eventos` será restrito somente a linhas cuja classificação original é `ERRO`, tratadas ou não. `PENDENTE` e `SUCESSO` deixam de ser elegíveis.
- Redesign visual; correção indispensável à compatibilidade exigirá desvio explícito.
- Worktrees, checkouts auxiliares ou branches de reconciliação sem autorização humana separada e nominal.
- Deploy direto no `Stage` customer-facing sem alvo comprovado, aprovação específica e rollback disponível.

## Decision Baseline (Frozen Before Implementation)

| ID | Decision | Rationale | State |
| --- | --- | --- | --- |
| `D-CUT-01` | Frontend e backend formam uma release Docker indivisível e serão promovidos juntos. | O backend serve o bundle Vite na mesma origem. | `frozen` |
| `D-CUT-02` | Unifast e Prosperar são contextos fiscais separados; não há lista agregada. | Preserva identidade fiscal e contrato aprovado. | `frozen` |
| `D-CUT-03` | Smart Notas é a única fonte de sucesso. Um predicado central autoriza somente linhas cuja classificação original é `ERRO`, tratadas ou não; `PENDENTE` e `SUCESSO` falham fechado em toda leitura/mutação `/eventos`, payload, resumo/produtos/exportação, monitoramento, realtime e UI, sem revelar existência. | Mantém `IntegrationErrorOccurrence` semanticamente fiel a falhas reais. | `frozen; implementation pending renewed approval` |
| `D-CUT-04` | Segredos entram apenas por variáveis seladas do Railway; evidências não contêm valores. | Mantém configuração fora da imagem. | `frozen` |
| `D-CUT-05` | Rollback primário reimplanta a release anterior; flag `false` é kill switch secundário. | A nova UI depende das rotas fiscais. | `frozen` |
| `D-CUT-06` | `Stage` é o único alvo e recebe usuários reais; não existe staging/PR environment. O corte é direto após validação local da source tree/build candidato, durante 20:00–22:00; o primeiro smoke valida os bits do rebuild Railway diante de usuários. | Remove a topologia fictícia e explicita que build local não é OCI remoto. | `frozen topology; renewed user approval required` |
| `D-CUT-07` | Rotação HMAC invalida `noteId` anterior e exige relistagem; sem grace period neste corte. | IDs são opacos/transitórios; reduz janela de segredo. | `frozen; user accepted 2026-09-27` |
| `D-CUT-08` | Adotar os logs estruturados Railway com retenção Pro de 30 dias neste primeiro cutover; forwarding externo fica como hardening se surgir requisito superior. | O cutover não registra payload fiscal/segredo, e 30 dias cobre diagnóstico inicial sem infraestrutura extra. | `frozen; user accepted 2026-09-27` |
| `D-CUT-09` | Ownership `note_read_model` só muda após smoke/observação verde no Stage, attestation pré-corte do rollback target e restore bem-sucedido caso tenha havido abort. | Documentação não pode antecipar realidade operacional nem alegar drill inexistente. | `frozen` |
| `D-CUT-10` | Railway usará readiness separada que responde não-2xx quando PostgreSQL estiver indisponível; liveness não chama Smart Notas e o binding fiscal permanece em probe explícito. | Impede promover release sem autenticação/Erros e evita restart storm por dependência externa. | `frozen; implementation pending approval` |
| `D-CUT-11` | Com a flag ativa, timeout `10 s`, concorrência `4`, `15 req/min` por usuário e `60 req/min` por contexto são variáveis obrigatórias sem fallback; ausência/valor divergente do envelope aprovado falha no startup. Aumentar budget exige nova evidência/aprovação. | Impede que defaults atuais `8/30/120` dobrem silenciosamente o envelope enquanto a quota do provedor é desconhecida. | `frozen fail-closed envelope` |
| `D-CUT-12` | Logs operacionais guardam no máximo correlation ID e `actorId` interno pseudônimo por 30 dias; nunca e-mail/nome/payload fiscal; acesso restrito ao Owner e mantenedores autorizados. | Mantém correlação com minimização de dados. | `frozen` |
| `D-CUT-13` | A identidade source promovida é a tree Git validada: PR pode gerar novo SHA somente se `candidate^{tree} == final-main^{tree}`. Railway reconstrói com base/apt mutáveis, portanto o build local não é o mesmo OCI; revision/build remoto e smoke Stage validam os bits reais. | Preserva source equivalence sem alegar reprodutibilidade inexistente do Dockerfile atual. | `frozen; remote-rebuild risk requires final approval` |
| `D-CUT-14` | A Foundation pós-cutover é autoridade em seu próprio `main`; o gitlink de `MonitorNotes` pode ficar intencionalmente no pin pré-promoção até o próximo release de produto aprovado. Não criar commit apenas documental em `MonitorNotes:main`, pois ele dispararia rebuild remoto. | Desacopla autoridade documental de deploy e evita um segundo cutover sem valor runtime. | `frozen; follow-up required` |

## Required Operational Decisions Before Approval

| Decision | Recommended direction | Required evidence | State |
| --- | --- | --- | --- |
| Railway target | `Unifast Products` / `Stage` / `MonitorNotes` / `monitornotes-stage.up.railway.app` / `main` | confirmação redatada + health HTTP 200 | `confirmed` |
| Validation environment | não existe alvo isolado; `Stage` é customer-facing | confirmação do project owner | `confirmed; direct-cutover risk awaits final approval` |
| Secret/rotation owner | project Owner confirmado privadamente; não persistir e-mail | papel informado pelo usuário; revalidar antes da mutação | `confirmed` |
| Replica/region/plan | Pro + US East + uma réplica | confirmação do project owner | `confirmed` |
| Production timeout | exigir exatamente `10 s` neste corte; qualquer alteração exige rebaseline/aprovação | latência de ambos os contextos | `frozen fail-closed value; validation pending` |
| Concurrency/rates | uma réplica: concorrência `4`, `15 req/min` por usuário e `60 req/min` por contexto | carga + quota/429 do provedor | `frozen initial values; validation pending` |
| Audit retention | 30 dias nos logs Railway; sem forwarding inicial | plano Pro + aprovação do project owner | `confirmed` |
| Cutover window/operator | project Owner; `20:00–22:00 America/Sao_Paulo` | aprovação do project owner + Stage customer-facing | `confirmed` |
| Abort threshold | abort imediato em mismatch/vazamento/readiness; ou `>=2` 429 consecutivos, `>=1%` 429 em 5 min, `>=5%` 5xx/timeout em 5 min com ao menos 20 requests, p95 `>8 s` por 5 min, RSS `>=80%` do limite ou crescimento `>20%` sem recuperar em 10 min | logs/métricas Railway + smoke | `frozen; validate observability before deploy` |
| External `/eventos` consumers | inventariar integrações fora deste repositório e obter attestation do Owner antes do deploy | lista redatada/declaração do Owner | `required pre-deploy; unknown consumer blocks deploy unless hard-cut risk is explicitly reapproved` |

## Diff Expectation Contract

- **Contract status:** `required; round-7 structural baseline frozen by this checkpoint`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree after candidate checkpoint`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | final planning/tool/gitlink sync recorded in `Gate: Review Baseline Freeze` evidence | `committed_diff`; `31712a042cab3c796d5daca7350c6c58453e1c73` remains code-origin evidence only |
| `uninotas-foundation` | `foundation_documentation` | `Gate: Review Baseline Freeze -> Baseline commit` | `committed_diff` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `railway.json` | `M` | health/readiness contract if required by approved topology |
| `MonitorNotes` | `DEPLOY.md` | `M` | fiscal cutover/rollback runbook |
| `MonitorNotes` | `README.md` | `M` | production source ownership after successful cutover |
| `MonitorNotes` | `backend/src/health/**` | `A|M` | readiness correction if selected |
| `MonitorNotes` | `backend/src/common/**` | `M` | propagar correlation ID único até logs/erros |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M` | bounded probe/capacity/rotation changes |
| `MonitorNotes` | `backend/src/config/**` | `M` | bounded runtime validation |
| `MonitorNotes` | `backend/src/logs/**` | `M` | tornar `/eventos` error-only e testar bloqueio de sucessos |
| `MonitorNotes` | `backend/src/monitoramento/**` | `M` | remover sucesso da projeção operacional baseada em logs |
| `MonitorNotes` | `backend/src/realtime/**` | `M` | impedir publicação de eventos de sucesso do legado |
| `MonitorNotes` | `backend/.env.example` | `M` | approved non-secret production controls |
| `MonitorNotes` | `frontend/src/api/eventos.ts` | `M` | alinhar cliente ao boundary error-only |
| `MonitorNotes` | `frontend/src/paginas/ListaEventos.tsx` | `M` | manter exclusivamente a fila Erros |
| `MonitorNotes` | `frontend/src/hooks/useProdutos.ts` | `M` | consumir somente produtos com erro |
| `MonitorNotes` | `frontend/src/hooks/useResumo.ts` | `M` | remover semântica de sucesso do resumo legado |
| `MonitorNotes` | `artifacts/**` | `A|M` | redacted evidence |
| `MonitorNotes` | `uninotas-foundation` | `M` | somente sync de planejamento/attestation anterior ao baseline de implementação; `D-CUT-14` proíbe novo sync isolado em `main` após o cutover |
| `uninotas-foundation` | `project_constitution.md` | `M` | promover invariantes/runtime authority após cutover |
| `uninotas-foundation` | `project_mandate.md` | `M` | alinhar mandato atual com Smart Notas/error-only |
| `uninotas-foundation` | `domain_entities.md` | `M` | promover entidades/owners atuais |
| `uninotas-foundation` | `system_roadmap.md` | `M` | registrar entrega observada e retirar estado futuro superseded |
| `uninotas-foundation` | `technology_baseline.md` | `M` | promover adapter/config Smart Notas de target para runtime observado |
| `uninotas-foundation` | `policies/query_path_guardrails.md` | `M` | retirar `logs` como note/event read model misto e fixar error-only |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-smart-notas-read-cutover.md` | `M|D` | evidence/closeout movement |
| `uninotas-foundation` | `todos/completed/features/TODO-uninotas-smart-notas-read-cutover.md` | `A` | closeout destination |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | promote read ownership |
| `uninotas-foundation` | `modules/runtime-and-deployment.md` | `M` | validated topology/runbook |
| `uninotas-foundation` | `modules/events-and-classification.md` | `M` | retain integration-error ownership |
| `uninotas-foundation` | `modules/integration-error-occurrences.md` | `M` | consolidar boundary error-only |
| `uninotas-foundation` | `modules/operational-monitoring.md` | `M` | remover sucesso da projeção de logs |
| `uninotas-foundation` | `modules/realtime-invalidation.md` | `M` | limitar invalidação a eventos de erro |
| `uninotas-foundation` | `modules/treatments-and-history.md` | `M` | tratamentos somente sobre ocorrências elegíveis |
| `uninotas-foundation` | `policies/scope_subscope_governance.md` | `M` | promover capabilities e transitions atomicamente |
| `uninotas-foundation` | `artifacts/dependency-readiness.md` | `A|M` | dependency state |
| `uninotas-foundation` | `artifacts/environment-topology.md` | `A|M` | validated Railway topology |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/.env` | `A|M|D|R` | local secrets are not versioned |
| `MonitorNotes` | `frontend/src/notas/**` | `A|D|R` | arquitetura fiscal já validada; somente correção material exige renewed approval |
| `MonitorNotes` | `backend/prisma/**` | `A|M|D|R` | no schema/data migration |
| `MonitorNotes` | `.github/**` | `A|M|D|R` | CI redesign is not authorized |
| `MonitorNotes` | `Dockerfile` | `A|M|D|R` | change to artifact topology needs renewed approval |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / agent defense | Decision | User validation / renewed approval |
| --- | --- | --- | --- | --- |
| `legacy error-only boundary` | `planned approval-material` | revalidação `REVAL-ARCH-03` provou que inventário sem enforcement não basta | integrar `/eventos`/monitoramento/realtime/frontend nos paths aprovados | exige novo `APROVADO` sobre o plano reconvergido |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** scripts/probes redatados, readiness, configuração Railway, runbook, carga e documentação diretamente necessárias ao cutover.
- **Must update or split the TODO:** nova funcionalidade fiscal, mudança visual, persistência, CI/CD novo, agregação, escrita Smart Notas ou mudança de origem.

## Assumptions Preview

| ID | Assumption | Evidence | Confidence | Handling | If False |
| --- | --- | --- | --- | --- | --- |
| `A-CUT-01` | Railway constrói a raiz com `Dockerfile` e publica um serviço único. | `railway.json`, `Dockerfile`, `DEPLOY.md` | `high` | `verify-before-cutover` | atualizar topologia e renovar aprovação |
| `A-CUT-02` | `main` é a branch atualmente conectada ao deploy. | confirmação do project owner em 2026-09-27 + `DEPLOY.md` | `high` | `re-attest-before-merge` | corrigir lane path antes do checkpoint |
| `A-CUT-03` | Flag `true` já falha se os cinco segredos/bindings fiscais estiverem ausentes, mas os quatro budgets ainda recebem defaults `10 s/8/30/120`. | `backend/src/config/configuration.ts` + specs | `high` | `change-and-test-first` | implementar `D-CUT-11`: budgets obrigatórios e exatos `10 s/4/15/60`, com teste de ausência |
| `A-CUT-04` | O health atual retorna HTTP 2xx com banco degradado e não serve como readiness. | `backend/src/health/health.controller.ts` + `railway.json` | `high` | `change-and-test-first` | implementar readiness DB-aware e apontar Railway para ela |
| `A-CUT-05` | Railway permite selecionar/reimplantar a release verde anterior, mas a disponibilidade concreta ainda precisa ser atestada no painel. | confirmação do Owner imediatamente antes da janela | `medium` | `block-until-attested` | abortar o cutover se release/controle não estiverem disponíveis |
| `A-CUT-06` | Domínio, serviço, região e uma réplica estão confirmados e saudáveis; commit servido segue desconhecido. | project-owner confirmation + health HTTP 200; sem CLI autenticada | `medium` | `re-attest-before-merge` | atestar revision/config imediatamente antes do deploy |
| `A-CUT-07` | Não há consumidor de sucesso em `logs` fora deste repositório. | inventário local é insuficiente para consumidores externos | `low` | `block-until-owner-attestation` | se falso, bloquear promoção `error-only`, registrar owner/prazo e manter estado provisório |

## Execution Plan

1. Confirmar topologia e obter inventário/attestation do Owner sobre consumidores externos de `/eventos`/`logs`; consumidor desconhecido bloqueia o deploy, salvo novo aceite explícito de hard cut.
2. Obter `APROVADO`, carregar regras e implementar na branch de trabalho: budgets fail-closed `10 s/4/15/60`, readiness PostgreSQL-aware, correlation ID ponta a ponta, boundary error-only central e runbook.
3. Executar testes focados, revisar o diff e congelar um novo checkpoint candidato contendo toda a implementação; registrar SHA e tree OID. Nenhum build anterior é evidência de entrega.
4. Sobre essa tree exata, executar CI-equivalent completo e build Docker local como evidência source-level, além de startup/readiness negativo, probes redatados dos dois emissores, carga near-limit e browser smoke autenticado. Não alegar OCI idêntico ao rebuild Railway.
5. Concluir auditorias delivery-side; rebasear somente se `main` mudou e, nesse caso, invalidar/repetir o checkpoint/validação. Preparar PR cuja tree final prevista seja idêntica à tree validada.
6. Dentro de 20:00–22:00, preparar no Railway os cinco segredos/bindings e quatro budgets selados enquanto a release anterior continua servindo; revisar presença/escopo sem imprimir valores.
7. Antes de promover `main`, registrar redatados: release verde anterior atualmente servida, source branch/configuração esperada, diff de configuração, acesso aos logs e controle de redeploy. A revision candidata ainda não existe; este passo é attestation pré-merge, não drill.
8. Promover o PR para `main`, verificar imediatamente `candidate^{tree} == final-main^{tree}` e atestar o novo main SHA/tree. Somente então capturar a nova revision/build Railway criada pelo rebuild da mesma source tree, cujos bits podem diferir do build local, e usar readiness/smoke Stage para validá-los. Mismatch de tree aciona abort antes do deploy quando possível; revision incorreta ou smoke remoto falho aciona abort/rollback.
9. Executar imediatamente smoke de API/navegador para os dois contextos, `/erros`, payload/tratamentos elegíveis, correlação, redaction e ausência de `SUCESSO`/fallback; observar por no mínimo 30 minutos.
10. Em qualquer abort condition, usar o kill switch apenas como contenção e reimplantar a release anterior em até 10 minutos; validar login, `/erros` e UI anterior. Sem abort, nenhum drill remoto é alegado.
11. Após janela verde e inventário externo limpo, promover capabilities/policies/módulos/root docs Foundation de forma atômica. Consumidor externo descoberto bloqueia a promoção e o deploy até coordenação ou novo aceite de hard cut.
12. Não sincronizar o novo commit Foundation em `MonitorNotes:main` neste closeout. Registrar o pin divergente e um follow-up para atualizar o gitlink dentro do próximo release de produto, onde a mudança entrará na tree validada sem deploy documental isolado.

## Health, Readiness and Rollback Contract

- Healthcheck Railway não substitui probe externo nem monitoramento contínuo.
- Health não deve chamar Smart Notas a cada probe: indisponibilidade transitória não deve causar restart storm.
- Criar readiness em `/api/v1/prontidao`, respondendo não-2xx se PostgreSQL estiver indisponível; Railway passa a usar essa rota. `/api/v1/saude` permanece liveness simples.
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

- [ ] `DOD-CUT-01` Novo checkpoint final contendo budgets/readiness/correlation/error-only/runbook é identificado, publicável e reproduzível antes do CI/build definitivo.
- [x] `DOD-CUT-02` Alvo Railway e responsáveis são registrados redatados e confirmados pelo usuário.
- [ ] `DOD-CUT-03` Os dois pares fiscais são validados contra a empresa esperada sem exposição de segredo/CNPJ.
- [ ] `DOD-CUT-04` Timeout, rate, concorrência e bytes/memória são calibrados para a topologia real sob carga near-limit.
- [ ] `DOD-CUT-05` Logs têm sink, retenção, acesso e redaction comprovados.
- [ ] `DOD-CUT-06` A tree candidata passa localmente em build, readiness, probes, API/browser smoke e `/erros`; essa evidência não é tratada como OCI Railway idêntico.
- [ ] `DOD-CUT-07` Release anterior e controle de redeploy são comprovados antes do corte; se acionado, rollback restaura a UI anterior em até 10 minutos.
- [ ] `DOD-CUT-08` `Stage` customer-facing passa em lista/detalhe para ambos sem fallback/mistura por no mínimo 30 minutos na janela.
- [ ] `DOD-CUT-09` Rotação HMAC falha fechado para ID antigo e relistagem produz IDs válidos.
- [ ] `DOD-CUT-10` Um predicado central autoriza somente classificação original `ERRO` (tratada ou não) e nega `PENDENTE`/`SUCESSO` em lista, resumo, produtos, exportação, detalhe, payload, tratamento unitário/lote, monitoramento, realtime e UI; deploy/promoção exigem inventário externo limpo ou novo aceite de hard cut.
- [ ] `DOD-CUT-11` Railway usa readiness PostgreSQL-aware não-2xx, liveness não chama Smart Notas e o runbook descreve variáveis fiscais, ordem atômica e rollback.
- [ ] `DOD-CUT-12` Request, aplicação, upstream e filtro de erro reutilizam o mesmo correlation ID; logs retêm por 30 dias somente metadados redatados/`actorId` pseudônimo com acesso restrito.
- [ ] `DOD-CUT-13` Candidate e final main possuem tree OID idêntico; revision/build remoto fica ligado ao final main e seus bits passam readiness/smoke Stage, sem alegar digest idêntico ao build local.
- [ ] `DOD-CUT-14` Promoção Foundation independente é concluída sem novo commit/deploy em `MonitorNotes:main`; gitlink divergente e follow-up do próximo product release ficam registrados.

## Validation Steps

- [ ] `VAL-CUT-01` Executar `bash delphi-ai/verify_context.sh` no contexto compatível e exigir `PACED-Ready`.
- [ ] `VAL-CUT-02` Depois de toda implementação, congelar o novo SHA e reexecutar suites CI-equivalent backend, frontend e Foundation exatamente nele.
- [ ] `VAL-CUT-03` Construir imagem raiz e provar startup/health com flag desligada; com flag ativa, ausência de qualquer segredo/binding ou budget `10 s/4/15/60` deve falhar fechada.
- [ ] `VAL-CUT-04` Executar `SMART_NOTAS_PROBE_ENABLED=true` somente em runner autorizado, com saída redatada, nos dois contextos.
- [ ] `VAL-CUT-05` Executar carga near-2MiB no candidato local com budgets `10 s/4/15/60` e registrar p95/p99, 429/5xx/timeout, RSS/heap e recuperação; confirmar métricas Railway antes do corte.
- [ ] `VAL-CUT-06` Executar smoke autenticado dos GETs e jornada browser `Geral -> detalhe -> Erros -> Geral` nos dois contextos.
- [ ] `VAL-CUT-07` Inspecionar logs/respostas por padrão sensível sem registrar os valores pesquisados.
- [ ] `VAL-CUT-08` Antes do corte, atestar no painel a release anterior, o controle de redeploy e o acesso do Owner sem acionar restore; se houver abort, registrar restore real/RTO e não reimplantar candidato automaticamente.
- [ ] `VAL-CUT-09` Executar `cutover_integrity_audit` e testes do predicado central: somente `ERRO` original passa; `PENDENTE` e `SUCESSO` não podem ser lidos/tratados em lista, resumo, produtos, exportação, detalhe, payload, lote, monitoramento, realtime ou UI.
- [ ] `VAL-CUT-10` Rodar guards Delphi de autoridade, diff, CI, revisão, completion e Foundation conforme a fase.
- [ ] `VAL-CUT-11` Forçar PostgreSQL indisponível em ambiente local controlado e comprovar readiness não-2xx enquanto liveness do processo permanece bounded.
- [ ] `VAL-CUT-12` Correlacionar um request sintético em controller/request context, service, adapter/upstream e exception filter com um único ID; revisar logs por PII/payload/segredo sem persistir os valores pesquisados.
- [ ] `VAL-CUT-13` Comparar `candidate^{tree}` com `final-main^{tree}`, registrar SHAs/tree, build local como evidência separada, revision/build Railway e smoke dos bits remotos; tree mismatch ou smoke remoto falho aborta.
- [ ] `VAL-CUT-14` Provar que o Dockerfile não consome a Foundation, registrar `Foundation main@sha` versus root gitlink pin e abrir follow-up para sincronização no próximo release sem mutar `MonitorNotes:main` agora.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-CUT-01` | Definition of Done | checkpoint final | git/build | novo `branch@sha` após implementação + build verde | local/CI | `planned` | `31712a0` é baseline inicial, não artefato final |
| `DOD-CUT-02` | Definition of Done | alvo/responsáveis | doc/manual | `environment-topology.md` redatado | Railway | `passed` | Owner/topologia confirmados |
| `DOD-CUT-03` | Definition of Done | binding emissores | runtime | live probe redatado | local authorized runner | `planned` | ambos os contextos antes da janela |
| `DOD-CUT-04` | Definition of Done | capacidade | load | relatório RLS near-limit | local candidate build + Railway metrics | `planned` | budgets iniciais congelados |
| `DOD-CUT-05` | Definition of Done | auditoria | runtime/review | política + consulta redatada | Railway | `planned` | 30 dias confirmados; provar acesso/redaction |
| `DOD-CUT-06` | Definition of Done | smoke pré-cutover | runtime/browser | API + browser evidence | local candidate tree/build | `planned` | source-level; não prova OCI Railway |
| `DOD-CUT-07` | Definition of Done | rollback | runtime | deployment IDs redatados + restore se acionado | Railway Stage | `planned` | alvo e controle antes do corte; RTO 10 min |
| `DOD-CUT-08` | Definition of Done | cutover | runtime/browser | smoke + observação 30 min | Railway Stage customer-facing | `planned` | corte direto na janela aprovada |
| `DOD-CUT-09` | Definition of Done | HMAC | test/runtime | relistagem após rotação | local candidate build/Stage | `planned` | sem chave antiga |
| `DOD-CUT-10` | Definition of Done | error-only + promoção | tests/doc/validator/manual | central-predicate negative tests + external-consumer attestation + module/policy diffs | local + Owner + Foundation | `planned` | inventário antes do deploy; promoção após Stage verde |
| `DOD-CUT-11` | Definition of Done | readiness/runbook | test/doc/runtime | HTTP negative test + `railway.json` + `DEPLOY.md` | local/Railway | `planned` | sem probe Smart Notas no health loop |
| `DOD-CUT-12` | Definition of Done | correlação/privacy | test/log review | request ID end-to-end + redaction evidence | local/Railway | `planned` | actor interno, sem e-mail/nome |
| `DOD-CUT-13` | Definition of Done | source/deployed identity | git/build/runtime | candidate/main tree OID + local build record + Railway revision/smoke | local/GitHub/Railway | `planned` | SHA pode diferir; tree não; OCI pode diferir |
| `DOD-CUT-14` | Definition of Done | Foundation/gitlink topology | doc/git | canonical Foundation SHA + stale-pin record + follow-up | Foundation/MonitorNotes | `planned` | nenhum segundo deploy documental |
| `VAL-CUT-01..14` | Validation Steps | validações | mixed | preencher cada evidência durante execução | mixed | `planned` | agregado não substitui linhas no closeout |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas API | fonte/binding | `unknown` | `2026-09-27 local config only` | probe não executado neste cutover | bloquear ativação |
| Railway control plane | deploy/vars/logs/rollback | `degraded` | `2026-09-27` | target/scale/operator confirmados; sem CLI autenticada | revalidar revision/config imediatamente antes da mutação |
| Railway `Stage` | smoke/cutover customer-facing | `healthy` | `2026-09-27` | `/api/v1/saude` HTTP 200 + project-owner confirmation | cutover direto somente após gates e aprovação final |
| PostgreSQL Railway | auth e erros | `healthy` | `2026-09-27` | health público reportou `banco: ok` | ainda falta smoke do checkpoint candidato |

## Profile Scope & Handoffs

- **Primary execution profile:** `operational-devops`
- **Active technical scope:** `railway,docker,nestjs,react,vite,postgresql,cross-stack`
- **Expected supporting profiles:** `operational-coder, assurance-security-adversarial, assurance-tester-quality`
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-devops`

| From Profile | To Profile | Why | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `operational-devops` | `operational-coder` | readiness/probe/runbook code | backend/root | `planned after approval` |
| `operational-devops` | `assurance-security-adversarial` | secrets/redaction/isolation | runtime/logs/config | `required before Stage cutover` |
| `operational-devops` | `assurance-tester-quality` | smoke/load/rollback | validation lanes | `required before Stage cutover` |

## Complexity

- **Level:** `big`
- **Checkpoint policy:** `section-by-section: published source checkpoint -> local candidate build validation -> Railway remote rebuild -> direct Stage smoke/30-minute observation -> conditional canonical promotion`
- **Why this level:** release crítica cross-stack, dois contextos fiscais, dependência externa, segredos, capacidade, observabilidade e rollback real.

## Canonical Module Anchors

- **Primary module doc:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Secondary module docs:** `runtime-and-deployment.md`; `events-and-classification.md`; `integration-error-occurrences.md`; `operational-monitoring.md`; `realtime-invalidation.md`; `treatments-and-history.md`.
- **Planned decision promotion targets:** ownership de `note_read_model`/`integration_error_read_model`, topologia/rollback, boundary `logs` error-only e capability transitions em `policies/scope_subscope_governance.md`.
- **Module decision consolidation targets:** source of truth, runtime topology, leitura/tratamento/monitoramento/realtime de erros e registry de capabilities.

## Module Decision Baseline Snapshot

| Canonical source | Current decision / authority | Handling | Intended closeout decision |
| --- | --- | --- | --- |
| `modules/fiscal-notes-and-documents.md` | Smart Notas read model permanece `target_planned`. | `Supersede (Intentional)` | promover Smart Notas como owner observado de lista/detalhe após Stage verde |
| `modules/events-and-classification.md` | `logs` ainda representa read model misto no runtime legado. | `Supersede (Intentional)` | restringir autoridade a ocorrências cuja classificação original é `ERRO` |
| `modules/integration-error-occurrences.md` | owner conceitual de falhas de integração. | `Preserve` | fortalecer enforcement error-only sem ampliar a entidade |
| `modules/runtime-and-deployment.md` | topologia anterior não contém readiness/cutover Railway completos. | `Supersede (Intentional)` | registrar serviço único, readiness DB-aware, janela e rollback observado |
| `modules/operational-monitoring.md` | projeção herdada pode contabilizar estados não elegíveis. | `Supersede (Intentional)` | monitorar somente ocorrências elegíveis de erro |
| `modules/realtime-invalidation.md` | stream pode refletir qualquer evento legado. | `Supersede (Intentional)` | emitir invalidação apenas para ocorrências elegíveis de erro |
| `modules/treatments-and-history.md` | tratamento aceita referência legada sem contrato central explícito. | `Supersede (Intentional)` | tratamento unitário/lote somente para classificação original `ERRO` |
| `modules/identity-and-team.md` | todos os setores autenticados mantêm leitura autorizada conforme roles existentes. | `Preserve` | nenhuma mudança de identidade/role neste cutover |
| `policies/scope_subscope_governance.md` | transitions de `note_read_model` e `integration_error_read_model` ainda planejadas. | `Supersede (Intentional)` | promover transitions concluídas atomicamente com evidência runtime |
| `project_constitution.md` | autoridade atual ainda não declara o cutover observado. | `Supersede (Intentional)` | fixar Smart Notas-only para sucesso e PostgreSQL error-only |
| `project_mandate.md` | mandato ainda descreve a evolução como alvo. | `Supersede (Intentional)` | refletir a central de notas operacional sem dual-read |
| `domain_entities.md` | entidades ainda coexistem com semântica histórica de `logs`. | `Supersede (Intentional)` | separar `FiscalNote` de `IntegrationErrorOccurrence` definitivamente |
| `system_roadmap.md` | entrega permanece futura/provisória. | `Supersede (Intentional)` | registrar entrega observada e próximos TODOs de escrita/documentos |
| `technology_baseline.md` | adapter/config Smart Notas permanecem target, não runtime comprovado. | `Supersede (Intentional)` | promover somente após revision/smoke Stage observados |
| `policies/query_path_guardrails.md` | ainda admite paths herdados do read model misto. | `Supersede (Intentional)` | fixar `/notas` Smart Notas-only e `/eventos` error-only |

## Module Coherence Gate

- **Gate status:** `no_material_findings`
- **Findings summary:** `events-and-classification` ainda documenta o runtime legado de `logs`, enquanto `fiscal-notes-and-documents` permanece target-planned; essa sobreposição é provisória e não autoriza promoção antecipada.
- **Promotion rule:** somente promover `note_read_model`/`integration_error_read_model` e afirmar `logs error-only` após enforcement central, smoke e inventário externo; atualizar atomicamente owner modules e `scope_subscope_governance.md`.
- **Evidence / reference:** `modules/fiscal-notes-and-documents.md`, `modules/events-and-classification.md`, `modules/runtime-and-deployment.md` e `D-CUT-03/D-CUT-09`.

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** o cutover muda a autoridade operacional de `note_read_model` para Smart Notas e consolida `logs` como fonte exclusiva de erros de integração.
- **Deviation / debt being retired:** reconstrução ou apresentação de notas emitidas com sucesso a partir do PostgreSQL `logs`, além da ausência de binding operacional comprovado dos dois emissores.
- **Target steady-state after closeout:** `Geral` e detalhe leem somente Smart Notas por `FiscalIssuerContext`; `Erros` lê somente falhas Routerfy/n8n; uma release Docker única serve frontend/backend habilitados e observáveis.
- **Temporary exceptions allowed:** coexistência técnica das rotas `/eventos` exclusivamente para o fluxo de erros; nenhum consumidor conhecido pode continuar apresentando sucesso a partir de `logs`. Consumidor externo descoberto não recebe exceção silenciosa: bloqueia a promoção e exige owner/prazo/TODO.
- **Cutover / removal condition:** smoke e rollback aprovados nos dois contextos, janela estável e promoção canônica; consumidores de sucesso remanescentes saem de `/eventos` por owner/critério registrado.
- **Promotion timing:** somente depois de smoke/observação verde no Stage, rollback target atestado e restore validado se acionado; antes disso este TODO é a verdade provisória.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| Smart Notas-only success source | `D-CUT-03` + project constitution | `/notas`, Geral e detalhe | impede autoridade concorrente e sucesso divergente |
| Central error-eligibility predicate | `D-CUT-03` | todos os reads/mutations/monitoramento/realtime de `/eventos` | impede bypass por detalhe, payload ou tratamento direto de sucesso |
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
| structural/test | integration-error boundary | new central-predicate contract tests across logs/monitoring/realtime | qualquer read/mutation ou evento `SUCESSO` escapando | `implement-in-this-todo` | `VAL-CUT-09` antes do deploy |
| config test | bootstrap variables | configuration specs with flag false/true-invalid | enable sem pares fiscais/HMAC ou valores fora de bound | `already-enforced` | rerun obrigatório em `VAL-CUT-03` |
| read-only runtime probe | Smart Notas binding | `smart-notas-live.probe.spec.ts` | token/CNPJ mismatch, lista/detail indisponível | `already-enforced` | execução real obrigatória em `VAL-CUT-04` |
| load/stress | external path and 2 MiB envelope | RLS report on approved topology | saturation, quota amplification, memory/recovery failure | `implement-in-this-todo` | `VAL-CUT-05` |
| browser smoke | same-origin React/Nest release | source-owned fiscal browser journey | incompatible UI/API, context/cache leak, `/erros` regression | `implement-in-this-todo` | `VAL-CUT-06` |
| operational recovery | Railway deployment | pre-cutover previous-release/control attestation; real restore only on abort | rollback unavailable or stale revision | `manual-only-with-rationale` | sem alvo isolado, não executar drill destrutivo; evidência em `VAL-CUT-08` |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after review baseline freeze and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set: TODO + topology/dependency artifacts + railway/Docker/config/health/fiscal boundaries`
- **Decision review status:** `round-7 confirmation pending`
- **Decision review evidence / resolution:** seis revisores independentes retornaram `BLOCKED` em rodadas sucessivas. Round 6 confirmou o conteúdo operacional e encontrou cinco lacunas estruturais: ordem da revision Railway, baseline/gitlink, cobertura do scope-drift, snapshot 1:1 de módulos e schema completo de aprovação. Todas foram integradas; round-7 freeze/confirmação limpa ainda são obrigatórios.

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
| `REVAL-ARCH-01` | high | yes | `Integrated` | lane/promotion matrix agora possuem uma única transição remota para `Stage`; validação anterior é somente local. |
| `REVAL-ARCH-02` | high | yes | `Integrated` | `D-CUT-11`, `A-CUT-03` e `VAL-CUT-03` exigem budgets sem fallback quando a flag está ativa. |
| `REVAL-ARCH-03` | high | yes | `Integrated` | `D-CUT-03`/`CUT-11` e paths esperados tornam todo boundary legado error-only com testes negativos. |
| `REVAL-ARCH-04` | high | yes | `Integrated` | pré-corte usa somente attestation; restore real acontece apenas em abort e não há claim de drill remoto. |
| `REVAL-ARCH-05` | medium | yes | `Integrated` | estados serão atualizados no novo checkpoint; scope-drift permanece bloqueado até a nova convergência. |
| `REVAL-ARCH-06` | medium | yes | `Integrated` | scope inclui `docker`/`postgresql`; topology registra PostgreSQL como dependência ativa observada. |
| `CONFIRM-ARCH-01` | high | yes | `Integrated` | inventário/attestation externo agora é gate antes do deploy, não apenas da promoção. |
| `CONFIRM-ARCH-02` | high | yes | `Integrated` | predicado central cobre detalhe, payload e tratamentos unitário/lote além de todas as projeções; export legado foi desambiguado. |
| `CONFIRM-ARCH-03` | high | yes | `Integrated` | whitelist inclui policy registry e todos os owner modules de errors/monitoring/realtime/treatments. |
| `CONFIRM-ARCH-04` | high | yes | `Integrated` | `backend/src/common/**` autorizado e validação exige mesmo correlation ID em request/aplicação/upstream/erro. |
| `CONFIRM-ARCH-05` | high | yes | `Integrated` | implementação precede novo checkpoint/CI/build; somente a mesma source tree segue para main/Stage. |
| `CONFIRM-ARCH-06` | medium | yes | `Integrated` | estados refletem novo drift e serão congelados no round 4 antes de reviews/guards. |
| `R4-ARCH-01` | high | yes | `Integrated` | freeze passa a registrar somente Foundation commit/ref resolvível; código/root ficam em evidência separada. |
| `R4-ARCH-02` | high | yes | `Integrated` | `Frontend / Consumer Matrix` cobre React, EventSource, UptimeRobot, Railway readiness, env e canon Foundation. |
| `R4-ARCH-03` | high | yes | `Integrated` | `D-CUT-13` congela equivalência por tree OID entre candidate e final main via PR, sem equiparar OCI local/remoto. |
| `R4-ARCH-04` | high | yes | `Integrated` | whitelist inclui constituição, mandato, entidades e roadmap para promoção canônica atômica. |
| `R5-ARCH-01` | high | yes | `Integrated` | build local virou evidência source-level; rebuild Railway é não idêntico e seus bits são validados por readiness/smoke Stage. |
| `R5-ARCH-02` | high | yes | `Integrated` | elegibilidade central exige classificação original `ERRO`; `PENDENTE` e `SUCESSO` são negados. |
| `R5-ARCH-03` | high | yes | `Integrated` | whitelist inclui `technology_baseline.md` e `policies/query_path_guardrails.md`. |
| `R5-ARCH-04` | high | yes | `Integrated` | Foundation fica autoridade independente; gitlink root não é sincronizado pós-cutover e recebe follow-up no próximo product release. |
| `R6-ARCH-01` | high | yes | `Integrated` | attestation pré-merge não inventa revision candidata; revision/build novos só são capturados depois do merge/rebuild. |
| `R6-ARCH-02` | high | yes | `Integrated` | `31712a0` fica como origem do código; baseline de implementação passa a ser o sync final de planejamento/tool/gitlink e o gitlink recebe regra explícita. |
| `R6-ARCH-03` | high | yes | `Integrated` | heading canônico foi restaurado e `Diff Expectation Contract` entrou no guard material com teste de regressão. |
| `R6-ARCH-04` | high | yes | `Integrated` | `Module Decision Baseline Snapshot` registra 1:1 cada fonte canônica com enum exato de handling. |
| `R6-ARCH-05` | high | yes | `Integrated` | assumptions, test strategy, CI matrix, issue cards e routing tuple agora seguem o schema completo de aprovação. |
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
- **Baseline branch:** `uninotas-foundation:main`
- **Baseline commit:** `cdf6fb1a1308e462d137e12b3c48c9b6d080f0f5`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** `R6-ARCH-01..05` integrados e publicados; round 7 governa a confirmação e a crítica.
- **Evidence / reference:** `origin/main@cdf6fb1a1308e462d137e12b3c48c9b6d080f0f5`; implementation baseline `MonitorNotes@922957f`; code-origin separado `MonitorNotes@31712a0`; Delphi guard `ee9b448`.
- **Waiver authority / reference:** `n/a`.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impede alteração material entre o pacote revisado e o aprovado.
- **Trigger stage:** `after review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `canonical defaults, incluindo Diff Expectation Contract, Module Decision Baseline Snapshot e Decision Baseline (Frozen Before Implementation)`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** nenhum drift material entre o checkpoint round 7 e esta attestation metadata.
- **Evidence / reference:** `review_scope_drift_guard.py@ee9b448`; baseline `uninotas-foundation:main@cdf6fb1a1308e462d137e12b3c48c9b6d080f0f5`; implementation baseline `MonitorNotes@922957f`; `Overall outcome: go`.
- **Waiver authority / reference:** `n/a`.

## Frontend / Consumer Matrix

| Producer Surface In This TODO | Consumer | Delivery State | Evidence / Waiver |
| --- | --- | --- | --- |
| `GET /api/v1/notas` | React `Geral`, `ListaNotas`, session cache | `implemented candidate; final tree validation pending` | fiscal contract/browser/cache suites + Stage smoke |
| `GET /api/v1/notas/:noteId` | React `/notas/:noteId`, `DetalheNota` | `implemented candidate; final tree validation pending` | opaque-ID/detail/error tests + Stage smoke |
| `/api/v1/eventos` list/resumo/produtos/export/detalhe/payload | React `/erros` + `/eventos/:refId`; external consumers unknown | `producer restricted to original ERRO rows; alignment planned in this TODO` | central-predicate matrix denies `PENDENTE`/`SUCESSO`; Owner attestation before deploy; no waiver |
| `/api/v1/eventos/*/tratamento` unitário/lote | React error-treatment flows | `producer guard planned; behavior preserved only when original class is ERRO` | mutation tests deny `PENDENTE`/`SUCESSO` without existence disclosure |
| `GET /api/v1/realtime/eventos` | React `useTempoReal`/EventSource somente em `/erros` | `producer filter + consumer evidence planned` | SSE contract test + browser proof that Geral/detalhe fiscal do not connect |
| `GET /api/v1/monitoramento/erros` | UptimeRobot | `response shape preserved; source projection becomes error-only` | controller/service contract + authorized monitor smoke; no success count authority |
| `GET /api/v1/prontidao` | Railway deployment healthcheck | `new producer/config consumer planned` | PostgreSQL-down non-2xx test + `railway.json` exact path + deployed readiness evidence |
| `GET /api/v1/saude` | human/public liveness consumers | `existing contract retained as liveness; removed from Railway readiness role` | existing shape/status test + runbook distinction |
| Smart Notas env/budgets | NestJS bootstrap / Railway sealed variables | `budgets fail-closed change planned; no frontend consumer` | missing-variable startup negatives + client bundle/env scan |
| `note_read_model` / `integration_error_read_model` | Foundation registry, modules and upper canonical docs | `promotion planned only after runtime evidence` | atomic diff across policy/modules/root docs + Foundation validator |

## Test Strategy

- **Strategy (`test-first|test-after|not-applicable`):** `test-first`.
- **Why:** budgets fail-closed, readiness e predicado error-only alteram contratos de segurança/produção; cada mudança começa por um teste negativo reproduzível antes do código.
- **Fail-first targets:** flag ativa sem cada budget; PostgreSQL indisponível em readiness; `PENDENTE`/`SUCESSO` em lista, resumo, produtos, exportação, detalhe, payload, tratamentos, monitoramento e realtime; correlation ID divergente; context/cache switch; noteId anterior após rotação.
- **External read-only:** `/empresa`, lista e detalhe nos dois contextos, sem mutação fiscal e com saída redatada.
- **Browser:** build local da source tree com interceptação controlada; depois smoke imediato dos bits reconstruídos no único `Stage` customer-facing.
- **Capacity:** latência, quota, concorrência e memória near-limit.
- **Rollback:** release anterior identificada/acionável antes do corte; restore real somente em abort porque não há alvo isolado, com risco residual explicitamente aprovado e RTO de 10 minutos.

## Local CI-Equivalent Suite Matrix

| Repository / Surface | Scenarios | Preconditions / Fixtures | Exact Command / Gate | Required Before | Status |
| --- | --- | --- | --- | --- | --- |
| backend NestJS | fiscal/config/readiness/error-only/correlation/negative auth | Node 22 host Windows; deterministic Jest fixtures; no live token | no diretório `backend`: `npm test -- --runInBand && npm run lint && npm run build` | candidate freeze | `planned rerun` |
| backend near-limit | 2 MiB, fairness, semaphore 4, rates 15/60, timeout/recovery | loopback stub only; `RLS_OUTPUT_DIR` redacted | no diretório `backend`: `RLS_OUTPUT_DIR=../artifacts/cutover-rls npm test -- --runInBand --runTestsByPath src/fiscal-notes/__tests__/smart-notas-load.spec.ts` | merge | `planned` |
| frontend React/Vite | context/cache switch, Geral/detalhe/Erros, race and contract | Node 22 host Windows; backend/stubs definidos pelo script | no diretório `frontend`: `npm run test:notas && npm run test:notas:race && npm run lint && npm run build` | candidate freeze | `planned rerun` |
| root Docker | single-image build, startup, liveness/readiness positive and DB-negative | Docker daemon; non-secret local env; candidate tree clean | `docker build -t monitornotes:cutover-candidate .` seguido do runbook de startup/probes em `DEPLOY.md` | merge | `planned` |
| Foundation / Delphi | TODO schema, authority, Foundation integrity and context | links existentes; nenhum repair salvo desvio Delphi-managed | `python3 delphi-ai/tools/todo_deterministic_validator.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md && python3 foundation_documentation/deterministic/validate_foundation.py --root foundation_documentation && bash delphi-ai/verify_context.sh` | approval and closeout | `in progress` |
| live provider | `/empresa`, lista e detalhe read-only em Unifast/Prosperar | runner autorizado; cinco bindings presentes; output redatado | no diretório `backend`: `SMART_NOTAS_PROBE_ENABLED=true npm test -- --runInBand --runTestsByPath src/fiscal-notes/__tests__/smart-notas-live.probe.spec.ts` | enable | `blocked until authority` |
| Railway browser | login, Geral/detalhe/Erros/Geral, ambos contextos, deployed revision | final main tree equal; revision/build capturados; readiness verde | smoke autenticado conforme `DEPLOY.md`, seguido de observação de 30 minutos | cutover closeout | `blocked until deploy` |

## Plan Review Gate

- **Review decision:** `required`
- **Review status:** `round-7 frozen; architecture confirmation and independent critique pending`
- **Required lenses:** architecture, operations, rollback, security, tests, performance, observability and structural soundness.
- **Known plan finding:** o health atual retorna HTTP 2xx quando o banco está degradado; `D-CUT-10` agora exige readiness separada não-2xx e mantém Smart Notas fora do loop.
- **Approval request condition:** nova revisão confirma `D-CUT-06..12`, crítica converge, baseline é atualizado e guards retornam `go/preflight-go`.

### Issue Card 1 — Único Stage recebe usuários reais

- **A — Recommended:** cutover direto somente na janela 20:00–22:00, após source/build local, rollback target atestado, thresholds ativos e Owner presente. Impacto: menor prazo com risco operacional explícito e contenção em até 10 minutos.
- **B — Alternative:** criar ambiente isolado/PR antes do corte. Impacto: reduz risco, mas amplia escopo/topologia e inviabiliza o prazo atual sem nova aprovação.
- **C — Do nothing:** ativar fora da janela sem gates. Impacto: risco inaceitável de indisponibilidade e mistura fiscal; proibido.

### Issue Card 2 — `/eventos` deve ser estritamente error-only

- **A — Recommended:** predicado central pela classificação original `ERRO`, cobrindo todos os reads, mutations, monitoramento, realtime e UI; consumidor externo desconhecido bloqueia deploy. Impacto: uma semântica única e verificável.
- **B — Alternative:** compatibilidade temporária para sucessos por endpoint separado. Impacto: preserva consumidor, mas mantém duas autoridades e exige novo TODO/aprovação.
- **C — Do nothing:** manter inventário sem enforcement. Impacto: sucesso legado continua escapando e invalida o cutover; proibido.

### Issue Card 3 — Railway reconstrói a imagem após merge

- **A — Recommended:** validar source tree local, exigir tree OID igual no `main`, capturar revision/build somente após merge e validar os bits remotos por readiness/smoke. Impacto: identidade de source forte com risco de build mutável explicitado.
- **B — Alternative:** publicar imagem OCI imutável construída em CI. Impacto: melhora reprodutibilidade, mas exige redesenho de pipeline fora deste prazo/TODO.
- **C — Do nothing:** tratar build local como imagem implantada. Impacto: falsa evidência e rollback ambíguo; proibido.

### Failure Modes

- Merge produz tree diferente, Railway constrói revision inesperada, readiness falha, binding fiscal diverge, `/eventos` expõe estado não elegível, quota/memória satura ou rollback target fica indisponível; qualquer caso bloqueia ou aborta conforme a fase.

### Residual Unknowns

- Quota real Smart Notas, consumidores externos de `/eventos`, revision/config atualmente servidas e acionabilidade concreta do redeploy anterior permanecem desconhecidos até as attestations/probes definidos; nenhum deles é assumido verde.

## Security Risk Assessment

- **Risk level:** `high`
- **Why this risk level:** dois tokens fiscais, CNPJs, HMAC, dados autenticados e configuração de produção.
- **Attack surface in scope:** secret store, logs, probes, binding, noteId, deploy output, responses e rollback.
- **Attack simulation decision:** `required before Stage cutover`
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
- **Independent test-quality audit:** `required before Stage cutover`.
- **Independent final review:** `required after implementation and before Stage cutover`.
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
- **Evidence / reference:** executar depois da convergência das revisões no novo baseline; validar `A-CUT-01..07`, budgets fail-closed, boundary error-only e target único contra código/artefatos.

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
| `delphi-ai/skills/wf-railway-change-service-deployment-contract-method/SKILL.md` | mudança de readiness/vars/release Railway | target/revision/order/rollback atestados | inferir estado remoto por arquivos locais | re-resolve antes da mutação |
| `delphi-ai/skills/rule-postgresql-postgresql-data-integrity-always-on/SKILL.md` | readiness e leitura `logs` dependem de PostgreSQL | queries bounded, credencial protegida e nenhum schema implícito | migração/lock/pool inventado | schema permanece fora de escopo |
| `delphi-ai/skills/rule-nestjs-nestjs-architecture-always-on/SKILL.md` | readiness | boundaries/fail-closed | restart storm | review health |
| `delphi-ai/skills/rule-react-react-architecture-always-on/SKILL.md` | SPA smoke | context/session/cache isolation | hidden fallback | runtime journey |
| `delphi-ai/skills/rule-vite-vite-build-runtime-always-on/SKILL.md` | bundle | same-origin/provenance | dev proxy como produção | fingerprint |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Execution topology:** `primary-checkout-single-writer`
- **Subagent / delegation authorization:** `not-requested`; routing declara a lane futura e não autoriza execução antes do `APROVADO`
- **Worktree authorization:** `not-authorized`
- **Guard outcome:** `go`
- **Guard evidence:** `python3 delphi-ai/tools/agent_role_routing_guard.py --client codex --surface implementation --role routine-executor --model gpt-5.6-terra --effort medium --proof-mode declared --execution-topology primary-checkout-single-writer --worktree-authorization not-authorized`; principal checkout/single writer e nenhuma delegação/worktree; não concede autoridade de execução.

## Questions To Close

- `approval final deve aceitar explicitamente o cutover direto no único Stage customer-facing, o rebuild Railway não idêntico ao build local, o primeiro smoke/rollback com usuários, os thresholds/RTO congelados e retenção por 30 dias do actorId interno pseudônimo.`
- `antes do deploy, o Owner deve atestar se existe consumidor externo de sucesso em /eventos/logs; se existir ou permanecer desconhecido, o deploy fica bloqueado até coordenação ou novo aceite explícito de hard cut.`
- `approval final também aceita o gitlink MonitorNotes intencionalmente atrás da Foundation pós-cutover até o próximo product release aprovado, evitando segundo auto-deploy documental.`

## Early Approval Signal

- **Received:** `Aprovado`, em 2026-09-27, incluindo autorização contextual para os checkpoints Git propostos.
- **Accepted decisions:** `D-CUT-07`, avanço do cutover e commit/push do candidato para revisão.
- **Authority effect:** `checkpoint Git concluído`; não autoriza deploy, alteração de variáveis Railway nem tráfego fiscal.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Reason:** contrato e checkpoint publicados; revisões e gates operacionais ainda precedem qualquer implementação remota/deploy.
