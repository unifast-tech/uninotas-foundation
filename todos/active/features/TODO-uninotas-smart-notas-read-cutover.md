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

- **Current delivery:** preparar e executar uma release coordenada React/NestJS no Railway, habilitar a leitura Smart Notas nos dois contextos, provar smoke/rollback e promover o ownership canônico.
- **Planned next steps:** retirar consumidores restantes da leitura legada de sucesso em `/eventos`; emissão/cancelamento e DANFE/XML terão TODOs próprios.
- **Anticipatory implementation authorized now:** `none` antes do novo `APROVADO`.
- **Rationale:** uma release única evita combinações incompatíveis entre frontend fiscal e backend com feature flag desligada.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Next exact step:** executar a revisão arquitetural formal sobre o baseline publicado e buscar `preflight-go`; nenhuma mutação Railway está autorizada.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** a topologia customer-facing e o baseline Git estão confirmados; a revisão arquitetural formal é o gate corrente.
- **Exit condition:** fatos remotos confirmados, decisões `D-CUT-06..08` congeladas, revisão pré-aprovação limpa e `todo_authority_guard.py --pre-approval` em `preflight-go`.

## Provisional Notes

- **Missing for production-ready:** checkpoint implantável, configuração remota, probes reais, carga na topologia final, deploy, smoke, rollback ensaiado e promoção Foundation.
- **Revisit criteria:** concluir `DOD-CUT-01..10` com evidência redatada da release exata.
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
- [ ] `CUT-04` Calibrar timeout, concorrência, rate budgets e memória para `réplicas × limite local`, quota observável e respostas válidas próximas do limite de 2 MiB.
- [ ] `CUT-05` Comprovar destino, retenção, acesso e redaction dos logs operacionais antes da ativação.
- [ ] `CUT-06` Implantar a imagem única em ambiente isolado, provar readiness, smoke autenticado e jornada de navegador nos dois contextos.
- [ ] `CUT-07` Ensaiar rollback para a release anterior e provar a recuperação; a flag desligada é somente kill switch do provedor, não rollback completo da UI.
- [ ] `CUT-08` Implantar a mesma release aprovada em produção, observar a janela e abortar segundo thresholds objetivos.
- [ ] `CUT-09` Validar rotação HMAC por substituição da chave e relistagem obrigatória; `noteId` anterior deve falhar fechado.
- [ ] `CUT-10` Promover atomicamente `note_read_model` para Smart Notas nos módulos/ledger somente após smoke e rollback aprovados.
- [ ] `CUT-11` Preservar PostgreSQL `logs` exclusivamente para erros Routerfy/n8n e registrar a retirada dos consumidores legados de sucesso.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `MonitorNotes:delphi-and-foundation`; `uninotas-foundation:main`
- **Promotion lane path:** `delphi-and-foundation -> main -> Railway validation environment -> Railway production`
- **Lane-promoted threshold for this TODO:** `main com checkpoint aprovado e CI-equivalent verde`
- **Production-ready threshold for this TODO:** `produção com smoke, observação, rollback ensaiado e promoção Foundation concluídos`
- **Execution topology:** `principal checkout, single code writer; worktrees/auxiliary checkouts forbidden`

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR / Main | Validation Environment | Production | Current Status |
| --- | --- | --- | --- | --- | --- |
| Backend + frontend read-only | `delphi-and-foundation@31712a042cab3c796d5daca7350c6c58453e1c73` | `pending promotion to main` | `pending` | `pending` | `published review candidate` |
| Foundation cutover contract | `main@38c0771aa6b44f56b81d6a08eecd9111c37ae8af` | `n/a` | `n/a` | `pending promotion` | `published review baseline` |

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
| `D-CUT-06` | `Stage` é o único alvo informado e recebe usuários reais; não existe ambiente/PR environment separado. O cutover será direto, na janela aprovada, com validação local/pré-tráfego e rollback por release. | Evita tratar o domínio customer-facing como sandbox e torna o risco explícito para a aprovação final. | `frozen topology; execution pending final APROVADO` |
| `D-CUT-07` | Rotação HMAC invalida `noteId` anterior e exige relistagem; sem grace period neste corte. | IDs são opacos/transitórios; reduz janela de segredo. | `frozen; user accepted 2026-09-27` |
| `D-CUT-08` | Adotar os logs estruturados Railway com retenção Pro de 30 dias neste primeiro cutover; forwarding externo fica como hardening se surgir requisito superior. | O cutover não registra payload fiscal/segredo, e 30 dias cobre diagnóstico inicial sem infraestrutura extra. | `frozen; user accepted 2026-09-27` |
| `D-CUT-09` | Ownership `note_read_model` só muda após smoke e rollback de produção. | Documentação não pode antecipar realidade operacional. | `frozen` |

## Required Operational Decisions Before Approval

| Decision | Recommended direction | Required evidence | State |
| --- | --- | --- | --- |
| Railway target | `Unifast Products` / `Stage` / `MonitorNotes` / `monitornotes-stage.up.railway.app` / `main` | confirmação redatada + health HTTP 200 | `confirmed` |
| Validation environment | não existe alvo isolado; `Stage` é customer-facing | confirmação do project owner | `confirmed; direct-cutover risk awaits final approval` |
| Secret/rotation owner | project Owner confirmado privadamente; não persistir e-mail | papel informado pelo usuário; revalidar antes da mutação | `confirmed` |
| Replica/region/plan | Pro + US East + uma réplica | confirmação do project owner | `confirmed` |
| Production timeout | não congelar default de 10 s sem probe real | latência de ambos os contextos | `open` |
| Concurrency/rates | com uma réplica, budget agregado = budget local; começar conservador | carga + quota/429 do provedor | `open; calibrated during cutover` |
| Audit retention | 30 dias nos logs Railway; sem forwarding inicial | plano Pro + aprovação do project owner | `confirmed` |
| Cutover window/operator | project Owner; `20:00–22:00 America/Sao_Paulo` | aprovação do project owner + Stage customer-facing | `confirmed` |
| Abort threshold | mismatch/vazamento/falha de um contexto sempre aborta; taxa numérica depende do baseline | métrica e janela de staging | `open` |

## Diff Expectation Contract

- **Contract status:** `required; baseline checkpoint frozen`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree after candidate checkpoint`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `31712a042cab3c796d5daca7350c6c58453e1c73` | `committed_diff` |
| `uninotas-foundation` | `foundation_documentation` | `38c0771aa6b44f56b81d6a08eecd9111c37ae8af` | `committed_diff` |

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
| `A-CUT-04` | O health atual comprova processo+banco, mas não Smart Notas; retorna HTTP 2xx com banco degradado. | `backend/src/health/health.controller.ts` | selecionar readiness segura |
| `A-CUT-05` | Railway mantém release anterior até health 2xx e permite redeploy. | docs oficiais; projeto real ainda não comprovado | definir rollback alternativo |
| `A-CUT-06` | Domínio, serviço, região e uma réplica estão confirmados e saudáveis; commit servido segue desconhecido. | project-owner confirmation + health HTTP 200; sem CLI autenticada | atestar revision/config imediatamente antes do deploy |

## Execution Plan

1. Confirmar e registrar topologia Railway sem valores secretos.
2. Congelar checkpoint Git dos candidatos e Foundation; não implantar working tree não identificado.
3. Fechar readiness, capacidade, sink e janela; revisar plano e obter `APROVADO`.
4. Reexecutar CI-equivalent completo e build Docker no checkpoint exato.
5. Preparar variáveis seladas no ambiente isolado com flag inicialmente `false`.
6. Habilitar o ambiente isolado e executar probes dos emissores, carga near-limit e browser smoke autenticado.
7. Ensaiar rollback para release anterior; reaplicar o mesmo checkpoint e confirmar recuperação.
8. Preparar produção, revisar diff de configuração, implantar o mesmo checkpoint e observar health/logs.
9. Executar smoke de API/navegador para os dois contextos e verificar `/erros`, ausência de fallback e redaction.
10. Em abort condition, reimplantar release anterior; usar a flag como kill switch adicional quando necessário.
11. Após janela verde, promover módulos/ledger e fechar o TODO com evidência redatada.

## Health, Readiness and Rollback Contract

- Healthcheck Railway não substitui probe externo nem monitoramento contínuo.
- Health não deve chamar Smart Notas a cada probe: indisponibilidade transitória não deve causar restart storm.
- Antes da aprovação, decidir se `/api/v1/saude` responde não-2xx com banco indisponível ou se haverá readiness separada; a solução deve manter rollback compatível.
- Binding token/CNPJ é comprovado por probe pré-tráfego, nunca por conteúdo sensível no health.
- Rollback primário: redeploy da release anterior verde.
- Kill switch: `SMART_NOTAS_READ_ENABLED=false`; corta o provedor, mas não restaura integralmente a nova tela `Geral`.

## Abort Conditions

- Mismatch token/CNPJ em qualquer contexto.
- Segredo, CNPJ integral, recurso upstream, URL assinada ou identificador sensível em saída não autorizada.
- Falha de startup/readiness, lista/detalhe ou browser em qualquer contexto.
- Fallback para `logs`, sucesso vazio mascarando erro, mistura ou acesso cross-context.
- Saturação sem recuperação, memória fora do budget ou 429/5xx/timeout sustentado acima do threshold congelado após staging.
- Sink ausente/inacessível ou retenção abaixo da política.
- Impossibilidade de reimplantar release anterior durante o ensaio.

## Definition of Done

- [ ] `DOD-CUT-01` Checkpoint backend/frontend/Foundation é identificado, publicável e reproduzível.
- [ ] `DOD-CUT-02` Alvo Railway e responsáveis são registrados redatados e confirmados pelo usuário.
- [ ] `DOD-CUT-03` Os dois pares fiscais são validados contra a empresa esperada sem exposição de segredo/CNPJ.
- [ ] `DOD-CUT-04` Timeout, rate, concorrência e bytes/memória são calibrados para a topologia real sob carga near-limit.
- [ ] `DOD-CUT-05` Logs têm sink, retenção, acesso e redaction comprovados.
- [ ] `DOD-CUT-06` Ambiente isolado passa em readiness, API smoke, browser smoke e `/erros` no checkpoint exato.
- [ ] `DOD-CUT-07` Rollback restaura release anterior e redeploy do candidato recupera os dois contextos.
- [ ] `DOD-CUT-08` Produção passa em lista/detalhe para ambos sem fallback/mistura durante a janela.
- [ ] `DOD-CUT-09` Rotação HMAC falha fechado para ID antigo e relistagem produz IDs válidos.
- [ ] `DOD-CUT-10` Ownership é promovido após smoke; `events-and-classification` permanece somente para erros/legado rastreado.

## Validation Steps

- [ ] `VAL-CUT-01` Executar `bash delphi-ai/verify_context.sh` no contexto compatível e exigir `PACED-Ready`.
- [ ] `VAL-CUT-02` Reexecutar suites CI-equivalent backend, frontend e Foundation no checkpoint.
- [ ] `VAL-CUT-03` Construir imagem raiz e provar startup/health com flag desligada e configuração inválida falhando fechada.
- [ ] `VAL-CUT-04` Executar `SMART_NOTAS_PROBE_ENABLED=true` somente em runner autorizado, com saída redatada, nos dois contextos.
- [ ] `VAL-CUT-05` Executar carga near-2MiB e registrar p95/p99, 429/5xx/timeout, RSS/heap, recuperação e limite por réplica.
- [ ] `VAL-CUT-06` Executar smoke autenticado dos GETs e jornada browser `Geral -> detalhe -> Erros -> Geral` nos dois contextos.
- [ ] `VAL-CUT-07` Inspecionar logs/respostas por padrão sensível sem registrar os valores pesquisados.
- [ ] `VAL-CUT-08` Ensaiar redeploy da release anterior e recuperação do candidato.
- [ ] `VAL-CUT-09` Executar `cutover_integrity_audit` e provar ausência de bridge/dual-read de sucesso.
- [ ] `VAL-CUT-10` Rodar guards Delphi de autoridade, diff, CI, revisão, completion e Foundation conforme a fase.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-CUT-01` | Definition of Done | checkpoint | git/build | `branch@sha + build fingerprint` | local/CI | `planned` | não usar HEAD atual como falso checkpoint |
| `DOD-CUT-02` | Definition of Done | alvo/responsáveis | doc/manual | `environment-topology.md` redatado | Railway | `blocked` | depende do usuário |
| `DOD-CUT-03` | Definition of Done | binding emissores | runtime | live probe redatado | validation env | `planned` | ambos os contextos |
| `DOD-CUT-04` | Definition of Done | capacidade | load | relatório RLS near-limit | validation env | `planned` | réplica/agregado |
| `DOD-CUT-05` | Definition of Done | auditoria | runtime/review | política + consulta redatada | Railway | `blocked` | plano/retenção desconhecidos |
| `DOD-CUT-06` | Definition of Done | smoke isolado | runtime/browser | API + browser evidence | staging/PR env | `blocked` | alvo ausente |
| `DOD-CUT-07` | Definition of Done | rollback | runtime | deployment IDs redatados + smoke | staging/PR env | `planned` | anterior/candidata |
| `DOD-CUT-08` | Definition of Done | produção | runtime/browser | smoke + observação | production | `planned` | após staging |
| `DOD-CUT-09` | Definition of Done | HMAC | test/runtime | relistagem após rotação | validation env | `planned` | sem chave antiga |
| `DOD-CUT-10` | Definition of Done | promoção | doc/validator | module diffs + validator | Foundation | `planned` | após produção verde |
| `VAL-CUT-01..10` | Validation Steps | validações | mixed | preencher cada evidência durante execução | mixed | `planned` | agregado não substitui linhas no closeout |

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
- **Checkpoint policy:** `section-by-section: checkpoint -> validation environment -> rollback drill -> production -> canonical promotion`
- **Why this level:** release crítica cross-stack, dois contextos fiscais, dependência externa, segredos, capacidade, observabilidade e rollback real.

## Canonical Module Anchors

- **Primary module doc:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Secondary module docs:** `foundation_documentation/modules/runtime-and-deployment.md`; `foundation_documentation/modules/events-and-classification.md`
- **Planned decision promotion targets:** ownership de `note_read_model`, topologia/rollback e `logs` error-only.
- **Module decision consolidation targets:** source of truth, runtime topology e boundaries nos três módulos.

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** o cutover muda a autoridade operacional de `note_read_model` para Smart Notas e consolida `logs` como fonte exclusiva de erros de integração.
- **Deviation / debt being retired:** reconstrução ou apresentação de notas emitidas com sucesso a partir do PostgreSQL `logs`, além da ausência de binding operacional comprovado dos dois emissores.
- **Target steady-state after closeout:** `Geral` e detalhe leem somente Smart Notas por `FiscalIssuerContext`; `Erros` lê somente falhas Routerfy/n8n; uma release Docker única serve frontend/backend habilitados e observáveis.
- **Temporary exceptions allowed:** coexistência das rotas legadas `/eventos` exclusivamente para o fluxo de erros e para consumidores legados explicitamente rastreados; nunca como fallback de sucesso de `/notas`.
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
- **Decision review status:** `ready`
- **Decision review evidence / resolution:** `baseline commits published and remote SHAs verified; formal review is the next gate`.
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
- **Baseline commit:** `MonitorNotes@31712a042cab3c796d5daca7350c6c58453e1c73` + `uninotas-foundation@38c0771aa6b44f56b81d6a08eecd9111c37ae8af`
- **Baseline push reference:** `MonitorNotes/delphi-and-foundation` + `origin/main`; ambos resolvidos remotamente para os SHAs do baseline em 2026-09-27.
- **Gate status:** `no_material_findings`
- **Findings summary:** checkpoint funcional e contrato Foundation foram publicados sem incluir segredos nem `artifacts/` temporários; os SHAs locais e remotos coincidem.
- **Evidence / reference:** push Foundation `0b36337..38c0771`; push MonitorNotes `5b4f5ae..31712a0`; verificação `rev-parse`/`ls-remote` confirmou igualdade.
- **Waiver authority / reference:** `n/a`.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impede alteração material entre o pacote revisado e o aprovado.
- **Trigger stage:** `after review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Decision Baseline|Architecture Change Governance|Assumptions Preview|Execution Plan|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- **Gate status:** `blocked`
- **Findings summary:** baseline de revisão ainda não existe.
- **Evidence / reference:** executar somente após freeze e reviews.
- **Waiver authority / reference:** `n/a`.

## Test Strategy

- **Strategy:** verification-first para deploy; nenhuma mutação fiscal externa.
- **Local:** suites, fail-closed config, build Docker, lint/build e Foundation.
- **External read-only:** `/empresa`, lista e detalhe nos dois contextos.
- **Browser:** ambiente isolado servindo fingerprint exato; depois mesmo smoke em produção.
- **Capacity:** latência, quota, concorrência e memória near-limit.
- **Rollback:** exercício real isolado antes de produção.

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
- **Review status:** `pending topology confirmation`
- **Required lenses:** architecture, operations, rollback, security, tests, performance, observability and structural soundness.
- **Known plan finding:** health atual retorna HTTP 2xx quando o banco está degradado e não prova binding Smart Notas; a solução deve preservar rollback.
- **Approval request condition:** revisão não pode ficar limpa enquanto `D-CUT-06..08` e threshold numérico de abort não forem congelados.

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
- **Current delivery stage at review time:** `Pending, Provisional+Blocked`

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
- **Current status:** `not run for this cutover; blocked on topology freeze`.

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

- `none — remote topology decisions are closed; checkpoint authorization and formal review gates remain process actions.`

## Early Approval Signal

- **Received:** `Aprovado`, em 2026-09-27, incluindo autorização contextual para os checkpoints Git propostos.
- **Accepted decisions:** `D-CUT-07`, avanço do cutover e commit/push do candidato para revisão.
- **Authority effect:** `checkpoint Git concluído`; não autoriza deploy, alteração de variáveis Railway nem tráfego fiscal.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Reason:** contrato e checkpoint publicados; revisões e gates operacionais ainda precedem qualquer implementação remota/deploy.
