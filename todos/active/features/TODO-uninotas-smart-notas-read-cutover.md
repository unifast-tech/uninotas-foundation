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
- **Next exact step:** concluir sync/attestation do freeze round 12 e executar nova confirmação arquitetural independente; nenhuma mutação Railway está autorizada.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** a topologia customer-facing e o baseline Git estão confirmados; a revisão arquitetural formal é o gate corrente.
- **Exit condition:** fatos remotos confirmados, decisões `D-CUT-06..19` congeladas, revisão pré-aprovação limpa e `todo_authority_guard.py --pre-approval` em `preflight-go`.

## Provisional Notes

- **Missing for production-ready:** implementação reconvergida, configuração remota, probes reais, carga local do build candidato, attestation do rollback target, rebuild/cutover/smoke no Stage e promoção Foundation.
- **Revisit criteria:** concluir `DOD-CUT-01..18` com evidência redatada da deployment exata.
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
- [ ] `CUT-02` Criar um único changeset staged Railway com os cinco valores sensíveis/bindings, os quatro budgets aprovados e `SMART_NOTAS_READ_ENABLED=true`; revisar presença/escopo sem imprimir valores e commitá-lo sem redeploy para que o único rebuild pós-merge o consuma atomicamente.
- [ ] `CUT-03` Executar probe redatado `/empresa`, lista e detalhe para os dois contextos e bloquear mismatch antes de tráfego de usuário.
- [ ] `CUT-04` Exigir no startup timeout `10 s`, concorrência `4`, rate `15 req/min` por usuário e `60 req/min` por contexto na única réplica; validar esse envelope com carga/respostas próximas de 2 MiB. Qualquer mudança exige rebaseline e nova aprovação.
- [ ] `CUT-05` Comprovar destino, retenção, acesso e redaction dos logs operacionais antes da ativação.
- [ ] `CUT-06` Provar localmente a tree candidata com build Docker, readiness, probes Smart Notas redatados, smoke autenticado e jornada de navegador nos dois contextos; Railway fará rebuild remoto e os bits reais só serão validados pelo smoke no Stage.
- [ ] `CUT-07` Antes do merge, registrar deployment Railway corrente, plano Pro, snapshot redatado, Owner e capacidade geral de rollback. Abort segue `REC-0/1/2A/2B/3`: pré-active só restaura config depois de terminal não ativo; active usa `Rollback` no ID anterior exato, confirmado antes do smoke amplo. Qualquer recovery conclui em até 10 minutos; ausência aborta ou exige risco/RTO renovados para `Redeploy`. A flag é apenas kill switch.
- [ ] `CUT-08` Executar um único cutover direto no `Stage` customer-facing entre 20:00–22:00, observar por no mínimo 30 minutos e abortar pelos thresholds congelados.
- [ ] `CUT-09` Validar rotação HMAC somente em teste local determinístico com chaves efêmeras: após substituição, `noteId` anterior falha fechado e a relistagem produz IDs válidos. Rotação de segredo no `Stage` é uma mudança operacional separada, fora deste cutover.
- [ ] `CUT-10` Promover atomicamente `note_read_model` para Smart Notas nos módulos/ledger somente após smoke e rollback aprovados.
- [ ] `CUT-11` Tornar PostgreSQL `logs` exclusivamente uma fonte de erros Routerfy/n8n: um predicado SQL canônico pela classificação original `ERRO` entra antes de `COUNT`, agrupamento, ordenação, paginação/limite e mutations em lista, resumo, produtos, exportação, detalhe, payload, histórico correlacionado, tratamento unitário/lote e monitoramento. Um espelho TypeScript é só defesa secundária. Tratamento/reabertura `PENDENTE` de erro original continua elegível; classificação original `PENDENTE`/`SUCESSO` não. Inventário externo é gate antes do deploy.
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
| Backend + frontend read-only | round-11 predecessor root `28f585b`/carrier `3ab03e2`; round-12 material root em `Gate: Review Baseline Freeze`; code-origin `31712a0` | `pending promotion to main` | `pending final cutover suite` | `pending one direct cutover` | `planning freeze/attestation governed by review gate` |
| Foundation cutover contract | round-11 predecessor `0be6ca8`/attestation `aa57ddb`; round-12 material em `Gate: Review Baseline Freeze` | `main-only authority` | `n/a` | `pending runtime promotion after observed cutover` | `round-12 material frozen; attestation may follow` |

## Out of Scope

- Emissão/cancelamento, DANFE/XML e novos relatórios/exportações fiscais Smart Notas; a exportação legada de `/eventos` permanece em escopo apenas para restringi-la a erros.
- Alteração de schema Prisma/PostgreSQL ou persistência de espelho/cache de notas.
- Agregação “Todos”, polling, webhook ou retry automático da Smart Notas.
- Detecção realtime de inserts externos em `logs`: neste corte, novos erros aparecem ao abrir/atualizar a tela; o stream cobre somente tratamentos gravados pela API e heartbeat.
- Mudança de escrita das falhas Routerfy/n8n; o boundary `/eventos` será restrito somente a linhas cuja classificação original é `ERRO`, tratadas ou não. `PENDENTE` e `SUCESSO` deixam de ser elegíveis.
- Redesign visual; correção indispensável à compatibilidade exigirá desvio explícito.
- Worktrees, checkouts auxiliares ou branches de reconciliação sem autorização humana separada e nominal.
- Deploy direto no `Stage` customer-facing sem alvo comprovado, aprovação específica e rollback disponível.

## Decision Baseline (Frozen Before Implementation)

| ID | Decision | Rationale | State |
| --- | --- | --- | --- |
| `D-CUT-01` | Frontend e backend formam uma release Docker indivisível e serão promovidos juntos. | O backend serve o bundle Vite na mesma origem. | `frozen` |
| `D-CUT-02` | Unifast e Prosperar são contextos fiscais separados; não há lista agregada. | Preserva identidade fiscal e contrato aprovado. | `frozen` |
| `D-CUT-03` | Smart Notas é a única fonte de sucesso. Um predicado SQL canônico autoriza somente classificação original `ERRO` e deve ser aplicado antes de `COUNT`, agregação, ordenação, paginação/limite e mutations em toda query, inclusive detalhe e histórico correlacionado; espelho TypeScript é defesa secundária. `PENDENTE`/`SUCESSO` originais falham fechado, mas situação de tratamento `PENDENTE` sobre erro original permanece elegível. | Evita vazamento, páginas curtas, totais incorretos e leitura desnecessária de linhas inelegíveis. | `frozen; implementation pending renewed approval` |
| `D-CUT-04` | Segredos entram apenas por variáveis seladas do Railway; evidências não contêm valores. | Mantém configuração fora da imagem. | `frozen` |
| `D-CUT-05` | Rollback primário usa a ação Railway `Rollback` sobre a deployment verde anterior, restaurando imagem e variáveis sem rebuild; `Redeploy` é fallback degradado somente se a imagem expirou e exige risco/RTO renovados. Flag `false` é kill switch secundário. | A nova UI depende das rotas fiscais, e rebuild de base/apt mutáveis não é restauração determinística. | `frozen; Railway semantics verified 2026-09-27` |
| `D-CUT-06` | `Stage` é o único alvo e recebe usuários reais; não existe staging/PR environment. O corte é direto após validação local da source tree/build candidato, durante 20:00–22:00; o primeiro smoke valida os bits do rebuild Railway diante de usuários. | Remove a topologia fictícia e explicita que build local não é OCI remoto. | `frozen topology; renewed user approval required` |
| `D-CUT-07` | Rotação HMAC invalida `noteId` anterior e exige relistagem; neste cutover a prova é exclusivamente local, determinística e usa chaves efêmeras. Nenhum segredo do `Stage` será rotacionado; rotação remota exige TODO, janela e aprovação próprios. | Preserva o contrato criptográfico sem introduzir uma segunda mutação operacional no corte direto. | `frozen; local-only proof` |
| `D-CUT-08` | Adotar os logs estruturados Railway com retenção Pro de 30 dias neste primeiro cutover; forwarding externo fica como hardening se surgir requisito superior. | O cutover não registra payload fiscal/segredo, e 30 dias cobre diagnóstico inicial sem infraestrutura extra. | `frozen; user accepted 2026-09-27` |
| `D-CUT-09` | Ownership `note_read_model` só muda após smoke/observação verde, attestation pré-merge dos fatos atuais, verificação pós-switch do rollback target exato e restore bem-sucedido caso tenha havido abort. | Documentação não pode antecipar realidade operacional nem alegar elegibilidade futura/drill inexistentes. | `frozen` |
| `D-CUT-10` | Railway usará readiness separada que responde não-2xx quando PostgreSQL estiver indisponível; liveness não chama Smart Notas e o binding fiscal permanece em probe explícito. | Impede promover release sem autenticação/Erros e evita restart storm por dependência externa. | `frozen; implementation pending approval` |
| `D-CUT-11` | Com a flag ativa, timeout `10 s`, concorrência `4`, `15 req/min` por usuário e `60 req/min` por contexto são variáveis obrigatórias sem fallback; ausência/valor divergente do envelope aprovado falha no startup. Aumentar budget exige nova evidência/aprovação. | Impede que defaults atuais `8/30/120` dobrem silenciosamente o envelope enquanto a quota do provedor é desconhecida. | `frozen fail-closed envelope` |
| `D-CUT-12` | Logs operacionais guardam no máximo correlation ID e `actorId` interno pseudônimo por 30 dias; nunca e-mail/nome/payload fiscal; acesso restrito ao Owner e mantenedores autorizados. | Mantém correlação com minimização de dados. | `frozen` |
| `D-CUT-13` | A identidade source promovida é a tree Git validada: PR pode gerar novo SHA somente se `candidate^{tree} == final-main^{tree}`. Railway reconstrói com base/apt mutáveis, portanto o build local não é o mesmo OCI; revision/build remoto e smoke Stage validam os bits reais. | Preserva source equivalence sem alegar reprodutibilidade inexistente do Dockerfile atual. | `frozen; remote-rebuild risk requires final approval` |
| `D-CUT-14` | A Foundation pós-cutover é autoridade em seu próprio `main`; o gitlink de `MonitorNotes` pode ficar intencionalmente no pin pré-promoção até o próximo release de produto aprovado. Não criar commit apenas documental em `MonitorNotes:main`, pois ele dispararia rebuild remoto. | Desacopla autoridade documental de deploy e evita um segundo cutover sem valor runtime. | `frozen; follow-up required` |
| `D-CUT-15` | O changeset Railway contém exatamente os cinco valores sensíveis/bindings, quatro budgets `10 s/4/15/60` e `SMART_NOTAS_READ_ENABLED=true`; ele é revisado e commitado sem redeploy da release antiga, e o único rebuild após merge deve consumir esse estado. Se o commit sem redeploy ou a atomicidade não puderem ser comprovados, o corte é abortado. | Evita subir o novo código desabilitado ou criar uma segunda deployment/configuração fora do cutover único. | `frozen; official staged-changes contract verified 2026-09-27` |
| `D-CUT-16` | `main` é a source branch conectada ao serviço `MonitorNotes`; deve ser reatestada antes do merge, e qualquer divergência bloqueia a promoção. | A branch de deploy altera revision, tree verification e blast radius. | `frozen from Owner confirmation; remote re-attestation required` |
| `D-CUT-17` | `/api/v1/eventos` aceita somente filtros `TODOS`, `ERRO` e `TRATADOS`. `ERRO` inclui erro original sem tratamento ou reaberto por tratamento `PENDENTE`; `TRATADOS` inclui `RESOLVIDO`/`IGNORADO`; `PENDENTE` e `SUCESSO` como filtros retornam HTTP 400. Resumo retorna exatamente `{total, erro, tratados}`. Produtos preservam temporariamente `{nome, eventos, erros}`, com `eventos == erros`, por compatibilidade. Detalhe/payload/histórico de ref inelegível retornam 404 sem revelar existência; histórico contém apenas linhas de erro original. | Congela o contrato público final do hard cut e impede que compatibilidade nominal reintroduza sucesso oriundo de logs. | `frozen; approval-material` |
| `D-CUT-18` | `/api/v1/monitoramento/erros` calcula somente erros originais ativos e preserva exatamente os dez campos existentes: `status`, `cor`, `erros`, `pendentes`, `sucessos`, `total`, `ultima_verificacao`, `janela`, `limites`, `detalhe`. `total == erros`; `pendentes=0` e `sucessos=0` são depreciados; erros `RESOLVIDO/IGNORADO` não contam, e tratamento `PENDENTE` volta a contar. A única credencial aceita é `x-monitor-token`; token em query é rejeitado. | Mantém o UptimeRobot compatível sem representar logs como autoridade fiscal nem expor credencial em URL. | `frozen; approval-material` |
| `D-CUT-19` | O SSE não detecta inserts externos neste corte. `GET /api/v1/realtime/eventos` usa o guard JWT global e `Authorization: Bearer`, nunca token/query; o React consome por `fetch`/ReadableStream, cancela no unmount/logout e rebusca dados. Cada stream termina no servidor em no máximo 30 s e o cliente reconecta com novo request autenticado, de modo que o `JwtStrategy` reavalie o usuário ativo no mesmo envelope de cache das demais rotas. O stream emite somente `evento.tratado` originado por mutation elegível e `heartbeat`; novos erros chegam por refresh ao abrir/atualizar `/erros`. Nenhum URL/log contém JWT. | Elimina bypass prolongado de usuário inativo e vazamento em ingress, e remove paginação impossível de provar numa tabela externa sem PK. | `frozen; approval-material` |

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
| Atomic staged enable | dez variáveis commitadas sem redeploy; o único rebuild pós-merge consome flag `true` + bindings + budgets | diff redatado do changeset e controle commit-without-redeploy no painel | `required pre-merge; inability blocks cutover` |
| Recovery action | state machine `REC-0/1/2A/2B/3`: config restore somente após terminal não ativo; qualquer active força stored-image rollback; `Redeploy` só fallback degradado | current/candidate IDs e status, cancel action, config snapshot/restore, previous-target option após switch | `required per reached state; inability aborts or requires renewed risk/RTO` |
| External `/eventos` consumers | inventariar integrações fora deste repositório e obter attestation do Owner antes do deploy | lista redatada/declaração do Owner | `required pre-deploy; unknown consumer blocks deploy unless hard-cut risk is explicitly reapproved` |

## Diff Expectation Contract

- **Contract status:** `required; round-12 material baseline frozen by this checkpoint`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree after candidate checkpoint`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | round-11 material root `28f585baadd0b0e814552a7c212dafa030dfddc9`; attestation carrier `3ab03e2428f5cb022a49ccb53fb61f256e6e4b05` | `committed_diff`; `31712a0` remains code-origin; round-12 material/root refs serão registrados no review gate; attestation-only gitlink carrier não é implementação |
| `uninotas-foundation` | `foundation_documentation` | `Gate: Review Baseline Freeze -> Baseline commit` | `committed_diff` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `railway.json` | `M` | health/readiness contract if required by approved topology |
| `MonitorNotes` | `DEPLOY.md` | `M` | fiscal cutover/rollback runbook |
| `MonitorNotes` | `README.md` | `M` | production source ownership after successful cutover |
| `MonitorNotes` | `backend/README.md` | `M` | remover contrato público/local de cinco abas e documentar `/eventos` original-ERRO-only |
| `MonitorNotes` | `backend/src/main.ts` | `M` | alinhar título/descrição global do Swagger à Smart Notas como fonte de sucesso e `logs` somente como erros de integração |
| `MonitorNotes` | `backend/src/health/**` | `A|M` | readiness correction if selected |
| `MonitorNotes` | `backend/src/common/**` | `M` | propagar correlation ID único até logs/erros |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M` | bounded probe/capacity/rotation changes |
| `MonitorNotes` | `backend/src/config/**` | `M` | bounded runtime validation |
| `MonitorNotes` | `backend/src/logs/**` | `M` | tornar `/eventos` error-only e testar bloqueio de sucessos |
| `MonitorNotes` | `backend/src/monitoramento/**` | `M` | remover sucesso da projeção operacional baseada em logs |
| `MonitorNotes` | `backend/src/realtime/**` | `M` | remover polling/LISTEN/JWT em query e manter stream autenticado somente para tratamentos elegíveis/heartbeat |
| `MonitorNotes` | `backend/.env.example` | `M` | approved non-secret production controls |
| `MonitorNotes` | `frontend/src/api/eventos.ts` | `M` | alinhar cliente ao boundary error-only |
| `MonitorNotes` | `frontend/src/api/tipos.ts` | `M` | congelar filtros/DTOs error-only e remover campos de sucesso do resumo |
| `MonitorNotes` | `frontend/src/paginas/ListaEventos.tsx` | `M` | manter exclusivamente a fila Erros |
| `MonitorNotes` | `frontend/src/hooks/useTempoReal.ts` | `M` | substituir EventSource/JWT em query por fetch streaming autenticado e treatment-only |
| `MonitorNotes` | `frontend/src/hooks/useProdutos.ts` | `M` | consumir somente produtos com erro |
| `MonitorNotes` | `frontend/src/hooks/useResumo.ts` | `M` | remover semântica de sucesso do resumo legado |
| `MonitorNotes` | `frontend/README.md` | `M` | documentar fila error-only, refresh de inserts e stream fetch/Bearer treatment-only |
| `MonitorNotes` | `frontend/e2e/**` | `A|M` | fail-first/unit/race/browser evidence for context cache and strict error-only journeys |
| `MonitorNotes` | `artifacts/**` | `A|M` | redacted evidence |
| `MonitorNotes` | `uninotas-foundation` | `M` | sync do material freeze e, no máximo, seu carrier de attestation metadata antes da implementação; `D-CUT-14` proíbe novo sync isolado em `main` após o cutover |
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
| post-baseline attestation gitlink carrier | `accepted preexisting metadata-only delta` | por construção, o único delta permitido após o material root sync é o gitlink do freeze Foundation para sua attestation; material root SHA e carrier observados são registrados no freeze/review package | iniciar o product diff no material root sync exato e classificar separadamente o carrier; nenhum arquivo de produto pode entrar nesse commit | regra resolve a referência circular Foundation→root; não autoriza sync pós-cutover |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** scripts/probes redatados, readiness, configuração Railway, runbook, carga e documentação diretamente necessárias ao cutover.
- **Must update or split the TODO:** nova funcionalidade fiscal, mudança visual, persistência, CI/CD novo, agregação, escrita Smart Notas ou mudança de origem.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence (`High|Medium|Low`) | Handling (`Keep as Assumption|Promote to Decision|Block`) |
| --- | --- | --- | --- | --- | --- |
| `A-CUT-01` | Railway constrói a raiz com `Dockerfile` e publica um serviço único. | `Dockerfile`, `railway.json`, `backend/src/main.ts`, `DEPLOY.md` | atualizar topologia e renovar aprovação | `High` | `Promote to Decision` (`D-CUT-01`) |
| `A-CUT-02` | `main` é a branch atualmente conectada ao deploy. | `foundation_documentation/artifacts/environment-topology.md`, `backend/src/main.ts`, confirmação do project Owner em 2026-09-27 | corrigir lane path antes do checkpoint | `High` | `Promote to Decision` (`D-CUT-16`) |
| `A-CUT-03` | Flag `true` já falha se os cinco segredos/bindings fiscais estiverem ausentes, mas os quatro budgets ainda recebem defaults `10 s/8/30/120`. | `backend/src/config/configuration.ts` + specs | startup pode aceitar envelope não aprovado | `High` | `Promote to Decision` (`D-CUT-11`) |
| `A-CUT-04` | O health atual retorna HTTP 2xx com banco degradado e não serve como readiness. | `backend/src/health/health.controller.ts` + `railway.json` | Railway pode promover release sem autenticação/Erros funcionais | `High` | `Promote to Decision` (`D-CUT-10`) |
| `A-CUT-05` | Após o novo deploy ficar ativo, o deployment ID antigo exato estará dentro da retenção Pro de `120 h`, com `Rollback` visível e variáveis restauráveis. | `railway.json`, `backend/src/config/configuration.ts`, `foundation_documentation/artifacts/environment-topology.md`; confirmação pós-switch pendente | rollback rápido/RTO deixam de ser comprováveis e o corte aborta ou exige risco renovado | `Medium` | `Block` |
| `A-CUT-06` | Domínio, serviço, região e uma réplica estão confirmados e saudáveis; deployment/commit servido seguem desconhecidos. | `railway.json`, `backend/src/health/health.controller.ts`, `foundation_documentation/artifacts/environment-topology.md`; sem CLI autenticada | revision/config podem divergir do plano | `Medium` | `Block` |
| `A-CUT-07` | Não há consumidor de sucesso em `logs` fora deste repositório. | inventário local em `backend/src/logs/logs.controller.ts`, `frontend/src/api/eventos.ts` e `frontend/src/hooks/useResumo.ts`; consumidor externo ainda não atestado | hard cut pode quebrar integração desconhecida | `Low` | `Block` |
| `A-CUT-08` | Railway permitirá commit do changeset de dez variáveis sem redeploy via staged changes, e o rebuild Git seguinte consumirá esse estado. | `railway.json`, `backend/src/config/configuration.ts`, `backend/src/config/configuration.spec.ts`; controle remoto ainda não atestado | cutover único/atômico não pode ser garantido | `Medium` | `Block` |

## Execution Plan

1. Confirmar topologia e obter inventário/attestation do Owner sobre consumidores externos de `/eventos`/`logs`; consumidor desconhecido bloqueia o deploy, salvo novo aceite explícito de hard cut.
2. Obter `APROVADO`, carregar regras e implementar na branch de trabalho: budgets fail-closed `10 s/4/15/60`, readiness PostgreSQL-aware, correlation ID ponta a ponta, boundary error-only central e runbook.
3. Executar testes focados, revisar o diff e congelar um novo checkpoint candidato contendo toda a implementação; registrar SHA e tree OID. Nenhum build anterior é evidência de entrega.
4. Sobre essa tree exata, executar CI-equivalent completo e build Docker local como evidência source-level, além de startup/readiness negativo, probes redatados dos dois emissores, carga near-limit e browser smoke autenticado. Não alegar OCI idêntico ao rebuild Railway.
5. Concluir auditorias delivery-side; rebasear somente se `main` mudou e, nesse caso, invalidar/repetir o checkpoint/validação. Preparar PR cuja tree final prevista seja idêntica à tree validada.
6. Dentro de 20:00–22:00, criar um único changeset Railway com dez variáveis: cinco valores sensíveis/bindings, quatro budgets exatos e `SMART_NOTAS_READ_ENABLED=true`; revisar o diff/presença/escopo sem imprimir valores e usar o commit de staged changes sem redeploy (controle `Alt` ao aplicar). A deployment anterior deve continuar servindo; se não for possível provar esse estado atômico, abortar antes do merge.
7. Antes de promover `main`, registrar redatados: deployment corrente verde, deployment ID, plano Pro, source branch/configuração esperada, snapshot dos nomes/escopo das variáveis, changeset de dez variáveis commitado sem redeploy, acesso aos logs e Owner com acesso à capacidade geral de rollback. Não alegar que a deployment corrente já aparece como alvo anterior; a revision candidata ainda não existe.
8. Promover o PR para `main`, verificar imediatamente `candidate^{tree} == final-main^{tree}` e atestar o novo main SHA/tree. Capturar revision/build Railway e aguardar readiness tornar a nova deployment ativa. Nesse instante, antes do smoke amplo, localizar o deployment ID antigo agora anterior e confirmar que a opção `Rollback` exata está visível dentro da retenção; ausência aciona abort ou o gate explícito de risco/RTO do fallback. Mismatch de tree/revision aciona abort.
9. Somente após o gate pós-switch de rollback, executar smoke de API/navegador para os dois contextos, `/erros`, payload/tratamentos elegíveis, correlação, redaction e ausência de `SUCESSO`/fallback; observar por no mínimo 30 minutos.
10. Em abort, seguir exatamente o estado `REC-1`, `REC-2A/2B` ou `REC-3`: antes de candidate-active restaurar somente configuração após terminal não ativo confirmado; depois de candidate-active usar `Rollback` da deployment verde anterior em até 10 minutos. Kill switch é contenção; `Redeploy` só é fallback degradado após risco/RTO renovados. Sem abort, nenhum drill remoto é alegado.
11. Após janela verde e inventário externo limpo, promover capabilities/policies/módulos/root docs Foundation de forma atômica. Consumidor externo descoberto bloqueia a promoção e o deploy até coordenação ou novo aceite de hard cut.
12. Não sincronizar o novo commit Foundation em `MonitorNotes:main` neste closeout. Registrar o pin divergente e um follow-up para atualizar o gitlink dentro do próximo release de produto, onde a mudança entrará na tree validada sem deploy documental isolado.

## Public Error API Contract

Regras comuns: `/eventos/**` e `/realtime/eventos` exigem `Authorization: Bearer` e o guard global que revalida usuário ativo; ausente/inválido/inativo retorna 401. DTO/query inválido ou chave não allowlisted retorna 400. Tratamentos exigem `ADMIN|GESTOR|ANALISTA`; perfil sem permissão retorna 403. Ref original `PENDENTE|SUCESSO` falha como 404 indistinguível de inexistente. Todo erro JSON não-stream preserva o envelope exato `{statusCode:number, erro:string, mensagem:string|string[], caminho:string, timestamp:string ISO}`. `LogResumoDto`, `LogDetalheDto`, `ClienteDto`, `VendaDto`, `ProdutorDto`, `TentativaDto` e `CampoPendenteDto` preservam os campos atuais; somente eligibility e conteúdo do histórico mudam.

| Method / path | Frozen request contract | Frozen success contract | Other status / headers |
| --- | --- | --- | --- |
| `GET /eventos` | somente `situacao=TODOS|ERRO|TRATADOS` (default `ERRO`), `busca<=120`, `produto<=200`, `pagina` inteiro >=1 (default 1), `limite` inteiro 1..200 (default 25), `direcao=asc|desc` (default `desc`), `dataInicio/dataFim` ISO; `PENDENTE|SUCESSO` inválidos | 200 `{dados,meta}`; cada item mantém exatamente `refId,eventAt,situacao,situacaoOriginal,mensagem,idSmartNotas,clienteNome,clienteDocumento,produto,valorVenda,meioPagamento,tentativas`; meta mantém `total,pagina,limite,totalPaginas,temProxima`; somente erro original | 400 query/chave inválida; 401 auth |
| `GET /eventos/resumo` | aceita somente `busca<=120`, `produto<=200`, `dataInicio/dataFim` ISO; não aceita nem ignora `situacao,pagina,limite,direcao`; sem defaults além de ausência dos filtros | 200 exatamente `{total,erro,tratados}`; `erro` inclui não tratado/reaberto, `tratados` inclui resolvido/ignorado e `total=erro+tratados` | 400/401 |
| `GET /eventos/produtos` | sem body; eligibility antes de group/order | 200 array `{nome,eventos,erros}` com `eventos==erros`, somente produtos com erro original | 401 |
| `GET /eventos/exportar` | aceita somente `situacao=TODOS|ERRO|TRATADOS` (default `ERRO`), `busca<=120`, `produto<=200`, `dataInicio/dataFim` ISO; rejeita `pagina,limite,direcao`; teto interno fixo 20.000 | 200 CSV UTF-8/BOM com colunas exatas `refId;idTransacao;eventAt;situacao;mensagem;idSmartNotas;clienteNome;clienteDocumento;clienteEmail;produto;codProduto;valorVenda;meioPagamento`, somente erro original | `Content-Type: text/csv; charset=utf-8`; `Content-Disposition` sanitizado; 400/401 |
| `GET /eventos/:refId` | ref elegível original-`ERRO` | 200 `LogDetalheDto`: campos de `LogResumoDto` mais `orientacao,origem,cliente,venda,produtor,historico,camposPendentes,payload,resposta`; cada tentativa mantém `em,mensagem,ok,autorNome`, mas histórico contém somente linhas originais `ERRO` | 401; 404 inexistente/inelegível |
| `GET /eventos/:refId/payload` | ref elegível original-`ERRO` | 200 exatamente `{enviado,resposta}` | 401; 404 inexistente/inelegível |
| `PATCH /eventos/:refId/tratamento` | body exatamente `{situacao: RESOLVIDO|IGNORADO|PENDENTE, observacao?: string<=1000}`; ref elegível | 200 `LogDetalheDto`; `PENDENTE` reabre para situação efetiva `ERRO` | 400/401/403; 404 inexistente/inelegível |
| `POST /eventos/tratar-lote` | body `{refIds: string[1..500], situacao, observacao?}`; cada ref é trimada, deve permanecer não vazia e ser única após trim; branco/duplicata rejeita todo lote com 400; mesma enum/regra do unitário | 200 exatamente `{solicitados,aplicados,ignorados}`; `solicitados` é o tamanho do array já validado e único; `ignorados` ecoa somente refs fornecidas não aplicadas, sem distinguir inexistente de inelegível | 400/401/403 |
| `GET /monitoramento/erros` | público se `MONITORAMENTO_TOKEN` ausente; se configurado, aceita somente header `x-monitor-token`; query `token` é inválida; aceita `minutos` inteiro 1..1440 default 60, `atencao` inteiro >=1 default 1, `critico` inteiro >=1 default 6 (sem relação adicional), `alertarEm=atencao|critico` opcional; demais chaves rejeitadas | 200 exatamente `{status,cor,erros,pendentes,sucessos,total,ultima_verificacao,janela:{inicio,fim,minutos},limites:{atencao,critico},detalhe}`; `erros=total` conta ativos/reabertos, tratados não contam, `pendentes=0`, `sucessos=0` | `Cache-Control: no-store`; 400 query/chave inválida; 401 token ausente/incorreto quando configurado; 503 banco indisponível ou severidade >= `alertarEm`, com o mesmo shape |
| `GET /realtime/eventos` | header Bearer obrigatório; nenhum token/query; consumidor usa `fetch` streaming e reconecta após término normal | 200 `text/event-stream`; apenas `evento.tratado` com `refId,situacao,origem='api',em` e `heartbeat` com `origem='sistema',em`; servidor encerra em <=30 s; sem polling/NOTIFY/`evento.novo` | 401 ausente/inválido/inativo a cada conexão; cancelar em logout/unmount; `Cache-Control: no-store`; nenhum JWT em URL/log |

## Recovery State Machine

| State | Trigger / truth | Required recovery | Evidence and maximum RTO |
| --- | --- | --- | --- |
| `REC-0 no-remote-mutation` | qualquer estado de código/checkpoint, publicado ou não, enquanto nenhuma configuração Railway foi commitada | nenhuma recuperação Railway; reverter somente diff/commit do TODO conforme autoridade Git e manter Stage intocado | refs/status/diff classificados; `5 min` |
| `REC-1 staged-config` | changeset de dez chaves foi commitado sem redeploy, mas `main` ainda não foi promovida | restaurar o snapshot redatado anterior via novo staged commit sem redeploy; confirmar deployment corrente inalterada | nomes/escopo antes/depois + mesmo deployment ID; `10 min` |
| `REC-2A candidate-in-flight` | merge ocorreu e candidato está queued/building/deploying | solicitar cancelamento uma vez e observar serialmente; não restaurar configuração enquanto o candidato não estiver terminal; se ficar ativo em qualquer instante, transicionar imediatamente para `REC-3` | candidate/revision + cancel action + estado observado; decisão em `5 min`, RTO total ainda `10 min` |
| `REC-2B candidate-terminal-not-active` | cancelamento/falha terminal confirmado e candidato nunca ficou ativo | restaurar snapshot anterior por staged commit sem redeploy e comprovar mesma deployment verde ativa; não usar `Rollback` | status terminal + current deployment ID antes/depois + config redatada restaurada; concluir dentro do RTO total `10 min` |
| `REC-3 candidate-active` | candidato tornou-se ativo e a deployment verde antiga virou previous | confirmar o ID antigo e executar `Rollback` armazenado; validar readiness/login/UI anterior; kill switch é somente contenção | action/target IDs redatados + probes + RTO; `10 min` desde abort |

Transições não podem pular evidência: `REC-1 -> REC-2A` exige merge/tree equivalentes; `REC-2A -> REC-2B` exige terminal não ativo confirmado; qualquer observação `Active` força `REC-2A -> REC-3`; o smoke amplo só começa após o target de `REC-3` estar comprovadamente rollbackable. Um único operador serializa cancelamento, observação e restauração; nenhuma ação concorrente/retry automático é permitida. Falha de recuperação encerra o corte e exige nova avaliação humana.

## Health, Readiness and Rollback Contract

- Healthcheck Railway não substitui probe externo nem monitoramento contínuo.
- Health não deve chamar Smart Notas a cada probe: indisponibilidade transitória não deve causar restart storm.
- Criar readiness em `/api/v1/prontidao`, respondendo não-2xx se PostgreSQL estiver indisponível; Railway passa a usar essa rota. `/api/v1/saude` permanece liveness simples.
- Binding token/CNPJ é comprovado por probe pré-tráfego, nunca por conteúdo sensível no health.
- Pré-merge: atestar plano Pro, deployment ID corrente, snapshot redatado de configuração/nomes de variáveis, acesso do Owner e capacidade geral de rollback; não alegar elegibilidade futura do alvo exato. Abort antes do merge segue `REC-1` se config já foi commitada.
- Pós-merge/pré-active: um operador observa/cancela serialmente (`REC-2A`); config só é restaurada após terminal não ativo confirmado (`REC-2B`). Se ficar active durante a corrida, migrar imediatamente para `REC-3`.
- Pós-switch/pre-smoke amplo: assim que a nova deployment estiver ativa, confirmar que o ID antigo agora aparece como previous deployment com `Rollback` visível; a retenção Pro de `120 h` passa a governar a imagem removida/substituída.
- Rollback primário: ação Railway `Rollback` sobre esse alvo antigo exato restaura imagem/variáveis sem rebuild; RTO máximo `10 min` desde o abort.
- Fallback degradado: `Redeploy` reconstrói a deployment a partir do source/config original e não preserva identidade de bits; só pode ser usado após bloqueio/renovação explícita do risco e do RTO.
- Kill switch: `SMART_NOTAS_READ_ENABLED=false`; corta o provedor, mas não restaura integralmente a nova tela `Geral`.
- Fonte operacional verificada: [Railway Staged Changes](https://docs.railway.com/deployments/staged-changes), [Deployment Actions](https://docs.railway.com/deployments/deployment-actions) e [image retention by plan](https://docs.railway.com/pricing/plans).

## Abort Conditions

- Mismatch token/CNPJ em qualquer contexto.
- Segredo, CNPJ integral, recurso upstream, URL assinada ou identificador sensível em saída não autorizada.
- Falha de startup/readiness, lista/detalhe ou browser em qualquer contexto.
- Fallback para `logs`, sucesso vazio mascarando erro, mistura ou acesso cross-context.
- `>=2` respostas 429 consecutivas ou `>=1%` de 429 em 5 minutos.
- `>=5%` de 5xx/timeout em 5 minutos com ao menos 20 requisições, ou p95 `>8 s` durante 5 minutos.
- RSS `>=80%` do limite Railway ou crescimento `>20%` sem recuperar em 10 minutos; qualquer saturação que impeça smoke também aborta.
- Sink ausente/inacessível ou retenção abaixo da política.
- Pré-merge sem plano/ID/snapshot/acesso geral; restore iniciado antes de terminal não ativo; candidate active sem transição para `REC-3`; pós-switch sem `Rollback` visível para o alvo antigo exato; atomicidade staged não comprovada; ou recovery não concluído em 10 minutos.

## Definition of Done

- [ ] `DOD-CUT-01` Novo checkpoint final contendo budgets/readiness/correlation/error-only/runbook é identificado, publicável e reproduzível antes do CI/build definitivo.
- [x] `DOD-CUT-02` Alvo Railway e responsáveis são registrados redatados e confirmados pelo usuário.
- [ ] `DOD-CUT-03` Os dois pares fiscais são validados contra a empresa esperada sem exposição de segredo/CNPJ.
- [ ] `DOD-CUT-04` Timeout, rate, concorrência e bytes/memória são calibrados para a topologia real sob carga near-limit.
- [ ] `DOD-CUT-05` Logs têm sink, retenção, acesso e redaction comprovados.
- [ ] `DOD-CUT-06` A tree candidata passa localmente em build, readiness, probes, API/browser smoke e `/erros`; essa evidência não é tratada como OCI Railway idêntico.
- [ ] `DOD-CUT-07` Cada estado `REC-0`, `REC-1`, `REC-2A`, `REC-2B` e `REC-3` possui ação/evidência executável; um operador serializa cancelamento/observação/restore, candidate-active durante abort força `REC-3`, e rollback sem rebuild restaura imagem/variáveis/UI em até 10 minutos. `Redeploy` não é confundido com rollback.
- [ ] `DOD-CUT-08` `Stage` customer-facing passa em lista/detalhe para ambos sem fallback/mistura por no mínimo 30 minutos na janela.
- [ ] `DOD-CUT-09` Teste local determinístico com chaves efêmeras prova que rotação HMAC invalida ID antigo e relistagem produz IDs válidos; nenhuma rotação HMAC ocorre no `Stage` deste TODO.
- [ ] `DOD-CUT-10` Um predicado SQL canônico de classificação original `ERRO` é aplicado antes de count/group/order/limit/paginação e mutations em lista, resumo, produtos, exportação, detalhe, payload, histórico correlacionado, tratamento unitário/lote e monitoramento; defesa TypeScript não substitui query-side filtering; tratamento `PENDENTE` sobre erro original permanece elegível; o contrato público congelado em `D-CUT-17..19`, `backend/README.md`, decorators OpenAPI e a descrição Swagger global em `backend/src/main.ts` estão coerentes.
- [ ] `DOD-CUT-11` Railway usa readiness PostgreSQL-aware não-2xx, liveness não chama Smart Notas e o runbook descreve variáveis fiscais, ordem atômica e rollback.
- [ ] `DOD-CUT-12` Request, aplicação, upstream e filtro de erro reutilizam o mesmo correlation ID; logs retêm por 30 dias somente metadados redatados/`actorId` pseudônimo com acesso restrito.
- [ ] `DOD-CUT-13` Candidate e final main possuem tree OID idêntico; revision/build remoto fica ligado ao final main e seus bits passam readiness/smoke Stage, sem alegar digest idêntico ao build local.
- [ ] `DOD-CUT-14` Promoção Foundation independente é concluída sem novo commit/deploy em `MonitorNotes:main`; gitlink divergente e follow-up do próximo product release ficam registrados.
- [ ] `DOD-CUT-15` Um changeset Railway de dez variáveis inclui flag `true`, cinco valores sensíveis/bindings e quatro budgets; é revisado e commitado sem redeploy da deployment antiga, e o único rebuild pós-merge comprova que consumiu esse estado.
- [ ] `DOD-CUT-16` Realtime não abre `LISTEN`, polling ou timer de varredura; stream usa `fetch` + Bearer/global guard, nunca JWT em URL, termina em <=30 s para nova validação e emite somente tratamento elegível/heartbeat; frontend reconecta, cancela em unmount/logout e refaz fetch ao receber tratamento.
- [ ] `DOD-CUT-17` Queries críticas error-only possuem plano `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)` redatado e p95 SQL/endpoint separados sobre fixture determinística de 20.000 linhas, sem alteração de schema/índice, e passam os thresholds pré-promoção congelados.
- [ ] `DOD-CUT-18` Lista, resumo, produtos, exportação, detalhe, payload, tratamentos, monitoramento e SSE respeitam integralmente métodos, allowlists, defaults, bounds, campos, envelope de erro, códigos, headers e negações do `Public Error API Contract`; frontend types/README não expõem filtros, contadores ou EventSource removidos.

## Validation Steps

- [ ] `VAL-CUT-01` Executar pelo runtime canônico compatível `"/mnt/c/Program Files/Git/bin/bash.exe" -lc 'cd /c/unifast/monitordenotas && bash delphi-ai/verify_context.sh'` e exigir `PACED-Ready`. A falha CRLF do wrapper no bash WSL não é falha do projeto; `bash delphi-ai/tools/verify_context.sh` pode ser usado apenas como diagnóstico, não como evidência substituta.
- [ ] `VAL-CUT-02` Depois de toda implementação, congelar o novo SHA e reexecutar suites CI-equivalent backend, frontend e Foundation exatamente nele.
- [ ] `VAL-CUT-03` Construir imagem raiz e provar startup/health com flag desligada; com flag ativa, ausência de qualquer segredo/binding ou budget `10 s/4/15/60` deve falhar fechada; o live probe deve usar exatamente `10 s/4/15/60`, não `30 s/2/30/120`.
- [ ] `VAL-CUT-04` Executar `SMART_NOTAS_PROBE_ENABLED=true` somente em runner autorizado, com saída redatada, nos dois contextos.
- [ ] `VAL-CUT-05` Executar carga near-2MiB no candidato local com budgets `10 s/4/15/60` e registrar p95/p99, 429/5xx/timeout, RSS/heap e recuperação; confirmar métricas Railway antes do corte.
- [ ] `VAL-CUT-06` Executar smoke autenticado dos GETs e jornada browser `Geral -> detalhe -> Erros -> Geral` nos dois contextos.
- [ ] `VAL-CUT-07` Inspecionar logs/respostas por padrão sensível sem registrar os valores pesquisados.
- [ ] `VAL-CUT-08` Antes do merge, atestar deployment corrente/ID/plano/snapshot redatado/acesso geral e ensaiar `REC-0/1/2A/2B/3`, incluindo corrida cancelamento→active; se houver abort pré-ativação, provar terminal não ativo antes do restore, config restaurada e deployment verde inalterada; depois do switch e antes do smoke amplo, comprovar `Rollback` no antigo ID exato. Registrar RTO e não reimplantar automaticamente.
- [ ] `VAL-CUT-09` Executar `cutover_integrity_audit`, testes estruturais SQL e fixtures com alta proporção inelegível: count/total/páginas corretos e só `ERRO` original pós-query; histórico filtra `SUCESSO/PENDENTE`; reabertura permanece elegível; validar allowlists/defaults/bounds, 400 para filtro/chave/ref branca/duplicada, envelope de erro, 404 sem disclosure, DTOs/headers exatos e revisar `backend/README.md`, `frontend/README.md`, decorators e `backend/src/main.ts` por cinco abas/sucesso/EventSource removidos.
- [ ] `VAL-CUT-10` Rodar guards Delphi de autoridade, diff, CI, revisão, completion e Foundation conforme a fase.
- [ ] `VAL-CUT-11` Forçar PostgreSQL indisponível em ambiente local controlado e comprovar readiness não-2xx enquanto liveness do processo permanece bounded.
- [ ] `VAL-CUT-12` Correlacionar um request sintético em controller/request context, service, adapter/upstream e exception filter com um único ID; revisar logs por PII/payload/segredo sem persistir os valores pesquisados.
- [ ] `VAL-CUT-13` Comparar `candidate^{tree}` com `final-main^{tree}`, registrar SHAs/tree, build local como evidência separada, revision/build Railway e smoke dos bits remotos; tree mismatch ou smoke remoto falho aborta.
- [ ] `VAL-CUT-14` Provar que o Dockerfile não consome a Foundation, registrar `Foundation main@sha` versus root gitlink pin e abrir follow-up para sincronização no próximo release sem mutar `MonitorNotes:main` agora.
- [ ] `VAL-CUT-15` Capturar o changeset staged de dez chaves por nomes/redaction, provar commit sem redeploy da deployment antiga e correlacionar a única revision pós-merge com flag `true` e budgets aprovados.
- [ ] `VAL-CUT-16` Provar que realtime não cria conexão `pg`, polling/timer ou `evento.novo`; abrir stream por fetch com Bearer e testar 401 para ausente/inválido/inativo, encerramento <=30 s, reconexão com nova checagem após desativação, nenhuma query credential/log, tratamento elegível, heartbeat, cancelamento em logout/unmount e refetch idempotente. Inspecionar logs de aplicação/ingress redatados por ausência de JWT/Authorization.
- [ ] `VAL-CUT-17` Gerar com seed versionada fixture local de exatamente 20.000 logs (80% originais `PENDENTE/SUCESSO`, 20% `ERRO`; entre erros, 25% `RESOLVIDO/IGNORADO` e casos reabertos), registrar versão/config PostgreSQL e estatísticas. Workloads fixos, isolados e nesta ordem: lista `ERRO?page=1&limit=25&desc`, lista `TRATADOS?page=1&limit=25&desc`, resumo sem filtros, produtos, export `TODOS`/20k. Para **cada** workload: 5 warm-ups descartados, um `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)` redatado e 30 execuções SQL sequenciais; depois, processo endpoint separado com estado reiniciado, 5 warm-ups e 50 requests medidos com concorrência 4 para cada workload não-export, e 5 warm-ups + 20 requests medidos com concorrência 1 para export. Para cada série ordenar wall-clock crescente e calcular nearest-rank `p95 = amostra[ceil(0.95*n)-1]`; não misturar operações/séries. Bloquear se filtro original-`ERRO` vier após limit/window/group, houver scan correlacionado por linha, qualquer lista/resumo/produtos exceder p95 `3 s` ou export exceder p95 `8 s`. Falha exige TODO separado de schema/índice e nova aprovação.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-CUT-01` | Definition of Done | checkpoint final | git/build | novo `branch@sha` após implementação + build verde | local/CI | `planned` | `31712a0` é baseline inicial, não artefato final |
| `DOD-CUT-02` | Definition of Done | alvo/responsáveis | doc/manual | `environment-topology.md` redatado | Railway | `passed` | Owner/topologia confirmados |
| `DOD-CUT-03` | Definition of Done | binding emissores | runtime | live probe redatado | local authorized runner | `planned` | ambos os contextos antes da janela |
| `DOD-CUT-04` | Definition of Done | capacidade | load | relatório RLS near-limit | local candidate build + Railway metrics | `planned` | budgets iniciais congelados |
| `DOD-CUT-05` | Definition of Done | auditoria | runtime/review | política + consulta redatada | Railway | `planned` | 30 dias confirmados; provar acesso/redaction |
| `DOD-CUT-06` | Definition of Done | smoke pré-cutover | runtime/browser | API + browser evidence | local candidate tree/build | `planned` | source-level; não prova OCI Railway |
| `DOD-CUT-07` | Definition of Done | recovery state machine | runtime/manual | evidência `REC-0/1/2A/2B/3`, corrida active e exact old-ID rollback pós-ativação | local/Railway Stage | `planned` | serializado; retenção Pro 120 h; sem rebuild; RTO 10 min |
| `DOD-CUT-08` | Definition of Done | cutover | runtime/browser | smoke + observação 30 min | Railway Stage customer-facing | `planned` | corte direto na janela aprovada |
| `DOD-CUT-09` | Definition of Done | HMAC | test | relistagem após rotação com chaves efêmeras | local candidate build | `planned` | Stage rotation fora de escopo |
| `DOD-CUT-10` | Definition of Done | SQL error-only + promoção | tests/doc/validator/manual | predicate before count/group/order/limit/mutations + correlated-history/pagination negatives + external-consumer attestation | local + Owner + Foundation | `planned` | TS mirror secondary; docs/OpenAPI aligned |
| `DOD-CUT-11` | Definition of Done | readiness/runbook | test/doc/runtime | HTTP negative test + `railway.json` + `DEPLOY.md` | local/Railway | `planned` | sem probe Smart Notas no health loop |
| `DOD-CUT-12` | Definition of Done | correlação/privacy | test/log review | request ID end-to-end + redaction evidence | local/Railway | `planned` | actor interno, sem e-mail/nome |
| `DOD-CUT-13` | Definition of Done | source/deployed identity | git/build/runtime | candidate/main tree OID + local build record + Railway revision/smoke | local/GitHub/Railway | `planned` | SHA pode diferir; tree não; OCI pode diferir |
| `DOD-CUT-14` | Definition of Done | Foundation/gitlink topology | doc/git | canonical Foundation SHA + stale-pin record + follow-up | Foundation/MonitorNotes | `planned` | nenhum segundo deploy documental |
| `DOD-CUT-15` | Definition of Done | atomic staged enable | runtime/manual | redacted ten-key changeset + no-redeploy commit + final revision config | Railway Stage | `planned` | flag true faz parte do mesmo corte |
| `DOD-CUT-16` | Definition of Done | realtime auth/boundary | test/security | fetch Bearer/global guard + no query JWT/poll/LISTEN + treatment-only | local backend/browser | `planned` | usuário inativo 401; cancel/refetch comprovados |
| `DOD-CUT-17` | Definition of Done | query performance | explain/load | fixture 20k versionada + planos JSON + p95 SQL/endpoint | local PostgreSQL | `planned` | 80% inelegível; schema/index fora do escopo |
| `DOD-CUT-18` | Definition of Done | public HTTP contract | contract/browser | métodos/campos/status/headers/negações exatos | local backend/frontend | `planned` | frontend types e OpenAPI coerentes |
| `VAL-CUT-01..17` | Validation Steps | validações | mixed | preencher cada evidência durante execução | mixed | `planned` | agregado não substitui linhas no closeout |

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

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `scope_subscope_governance#note-read-model-001` | `note_read_model` pertence a `events-and-classification`; transferência para `fiscal-notes-and-documents` está `planned`. | `Supersede (Intentional)` | concluir a transferência somente após Stage verde e promoção atômica |
| `scope_subscope_governance#integration-error-read-model-001` | `integration_error_read_model` pertence a `events-and-classification`; `integration-error-occurrences` está `target_planned` sem capability owned. | `Supersede (Intentional)` | promover o novo owner somente após enforcement error-only e evidência runtime |
| `scope_subscope_governance#operational-workflow-001` | transferência de `operational_workflow` para `operational-cases` está `planned`. | `Out of Scope` | este cutover não transfere workflow; `treatments-and-history` permanece owner atual |
| `scope_subscope_governance#fiscal-document-read-001` | `fiscal_document_read` para DANFE/XML está `planned`. | `Out of Scope` | DANFE/XML terá TODO próprio; este corte entrega somente lista/detalhe fiscal |
| `modules/events-and-classification#runtime-authority` | módulo atual possui os dois read models sobre `logs`. | `Supersede (Intentional)` | retirar sucesso fiscal e reter somente o legado necessário até as duas transfers acima |
| `modules/runtime-and-deployment#runtime-topology-health` | topologia atual não contém readiness DB-aware nem rollback Railway comprovado. | `Supersede (Intentional)` | registrar serviço único, changeset staged, readiness, janela e rollback observado |
| `modules/operational-monitoring#legacy-log-monitoring` | projeção herdada pode contabilizar estados originais não elegíveis. | `Supersede (Intentional)` | monitorar somente linhas cuja classificação original é `ERRO` |
| `modules/realtime-invalidation#legacy-log-invalidation` | stream pode refletir inserts/eventos legados e usa JWT em query. | `Supersede (Intentional)` | fetch-SSE autenticado apenas para tratamentos de ocorrências originais `ERRO`; inserts externos aparecem por refresh |
| `modules/treatments-and-history#operational-workflow` | tratamento/histórico atual opera sobre referências legadas. | `Supersede (Intentional)` | manter ownership, mas filtrar cada linha correlacionada e mutação por erro original |
| `modules/identity-and-team#authentication-team-profiles` | roles/autenticação atuais autorizam os setores confirmados. | `Preserve` | nenhuma mudança de identidade, role ou tenancy neste cutover |
| `project_constitution#source-authority` | autoridade atual ainda não declara o cutover observado. | `Supersede (Intentional)` | fixar Smart Notas-only para sucesso e PostgreSQL error-only após evidência |
| `project_mandate#uninotas-direction` | mandato descreve a mudança como alvo. | `Supersede (Intentional)` | refletir a central operacional sem dual-read |
| `domain_entities#fiscal-note-integration-error` | entidades ainda coexistem com semântica histórica de `logs`. | `Supersede (Intentional)` | separar `FiscalNote` de `IntegrationErrorOccurrence` definitivamente |
| `system_roadmap#smart-notas-read` | entrega permanece futura/provisória. | `Supersede (Intentional)` | registrar entrega observada e próximos TODOs de escrita/documentos |
| `technology_baseline#smart-notas-adapter` | adapter/config permanecem target, não runtime comprovado. | `Supersede (Intentional)` | promover somente após revision/smoke Stage observados |
| `policies/query_path_guardrails#note-event-reads` | paths ainda admitem read model legado misto. | `Supersede (Intentional)` | fixar `/notas` Smart Notas-only e `/eventos` error-only por linha |

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
| Query-side error-eligibility predicate | `D-CUT-03` | SQL antes de count/group/order/limit/mutations em todos os reads/monitoramento de `/eventos` | impede bypass, totais/páginas falsos e leitura desnecessária de sucesso |
| Public error API shape | `D-CUT-17` | filtros/DTOs/status codes de lista, resumo, produtos, detalhe, histórico e tratamentos | impede implementação ambígua e mantém hard cut testável |
| Header-authenticated treatment stream | `D-CUT-19` | fetch streaming com Bearer/global guard; sem query JWT, polling, LISTEN ou evento de insert externo | impede bypass de usuário inativo, segredo em URL e algoritmo não determinístico sem PK |
| Context binding server-side | `D-CUT-02` + fiscal module invariant | Unifast/Prosperar config, adapter and routes | impede token/CNPJ arbitrário e mistura fiscal |
| Atomic same-image release | `D-CUT-01` | root Docker artifact + Railway service | impede frontend fiscal apontar para backend desabilitado |
| Stored-image rollback, flag kill switch | `D-CUT-05` | Railway deployments and runtime config | restaura imagem/variáveis sem rebuild e mantém corte emergencial do provedor |
| Atomic staged enable | `D-CUT-15` | Railway ten-key changeset | garante que a única revision nova sobe habilitada com envelope exato |
| Redacted structured operations | `D-CUT-04`, `D-CUT-08` | variables, probes, logs and evidence | protege segredos/dados fiscais e mantém diagnóstico por 30 dias |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why Forbidden | Exception Policy |
| --- | --- | --- | --- |
| Fallback de sucesso para `logs` | `/notas` ou Geral consultando Prisma/logs após falha Smart Notas | mascara indisponibilidade e cria duas verdades | `none` |
| Deploy de frontend/backend separados | commits/imagens diferentes no mesmo cutover | quebra compatibilidade da rota Geral | `none` |
| Flag-only tratada como rollback completo | nova UI permanece publicada com fiscal off | Geral fica indisponível | somente kill switch temporário enquanto a deployment anterior recebe `Rollback` |
| `Redeploy` confundido com `Rollback` | ação escolhida inicia novo build | perde identidade de bits e pode romper RTO com base/apt mutáveis | fallback degradado exige risco/RTO renovados |
| Probe/health expondo ou chamando segredo em loop | valores fiscais em output ou Smart Notas chamada por todo healthcheck | vazamento/restart storm | `none` |
| Escala sem budget agregado | `replicas × concurrency/rate` acima do aprovado | multiplica quota/memória silenciosamente | exige nova calibração e aprovação |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan |
| --- | --- | --- | --- | --- | --- |
| structural/test | backend fiscal boundary | existing fiscal module/contract/structure specs | Prisma/logs fallback, public credential input, context leak | `already-enforced` | rerun obrigatório em `VAL-CUT-02` |
| structural/test | integration-error SQL boundary | SQL-shape + high-ineligible-ratio pagination tests across logs/monitoring | filtro pós-query, total/página falsa ou read/mutation `SUCESSO` escapando | `implement-in-this-todo` | `VAL-CUT-09` antes do deploy |
| contract/test | public `/eventos` + monitoramento + SSE | method/request/DTO/status/header matrix from `D-CUT-17..19` | zeros enganosos, filtros legados, disclosure, credential URL ou auth bypass | `implement-in-this-todo` | `VAL-CUT-09/16` antes do deploy |
| security/contract | realtime stream | Bearer/global guard + browser fetch parser/cancel/refetch + no pg/timer structure | JWT em URL/log, usuário inativo, reconnect leak ou insert externo alegado | `implement-in-this-todo` | `VAL-CUT-16` antes do deploy |
| explain/performance | logs query family | redacted JSON plans on representative high-ineligible dataset | predicate late, correlated per-row scan or p95 above promotion budget | `implement-in-this-todo` | `VAL-CUT-17` antes do deploy |
| config test | bootstrap variables | configuration specs with flag false/true-invalid | enable sem pares fiscais/HMAC ou valores fora de bound | `already-enforced` | rerun obrigatório em `VAL-CUT-03` |
| read-only runtime probe | Smart Notas binding | `smart-notas-live.probe.spec.ts` | token/CNPJ mismatch, lista/detail indisponível | `already-enforced` | execução real obrigatória em `VAL-CUT-04` |
| load/stress | external path and 2 MiB envelope | RLS report on approved topology | saturation, quota amplification, memory/recovery failure | `implement-in-this-todo` | `VAL-CUT-05` |
| browser smoke | same-origin React/Nest release | source-owned fiscal browser journey | incompatible UI/API, context/cache leak, `/erros` regression | `implement-in-this-todo` | `VAL-CUT-06` |
| operational recovery | Railway deployment | pre-merge current ID/config/access + post-switch exact old-ID rollback gate; restore only on abort | rollback unavailable, expired image or wrong variables | `manual-only-with-rationale` | sem alvo isolado, não executar drill destrutivo; evidência em `VAL-CUT-08` |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after review baseline freeze and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set: TODO + topology/dependency artifacts + railway/Docker/config/health/fiscal boundaries`
- **Decision review status:** `round-12 confirmation pending`
- **Decision review evidence / resolution:** onze revisores independentes retornaram `BLOCKED` em rodadas sucessivas. Round 11 confirmou recovery, monitoring, realtime scope/auth, HMAC, runner e SQL; encontrou defaults/limites HTTP, `frontend/README.md`, amostras por workload e metadata exata. Todos estão integrados neste baseline round 12; nova confirmação independente é obrigatória.

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
| `R7-ARCH-01` | high | yes | `Integrated` | `31712a0`, `922957f` e `c9c2e42` têm papéis distintos; base operacional é `c9c2e42` e o delta gitlink conhecido foi classificado. |
| `R7-ARCH-02` | high | yes | `Integrated` | snapshot usa decisão/capability 1:1; integration-error é supersede e operational-workflow/fiscal-document-read são out of scope. |
| `R7-ARCH-03` | high | yes | `Integrated` | assumptions usam enums canônicos; issue cards, failure modes e residual risks seguem schema integral. |
| `R7-ARCH-04` | high | yes | `Integrated` | whitelist inclui `frontend/e2e/**`; matrix inclui Playwright, lint+zero-diff/refreeze e probe `10 s/4/15/60`. |
| `R7-ARCH-05` | high | yes | `Integrated` | changeset staged contém dez variáveis incluindo flag `true`, commitado sem redeploy antes do único rebuild pós-merge. |
| `R7-ARCH-06` | high | yes | `Integrated` | stored-image `Rollback` restaura imagem/variáveis sem rebuild; alvo exato é verificado pós-switch e `Redeploy` é fallback degradado com renewed risk/RTO. |
| `R7-ARCH-07` | high | yes | `Integrated` | predicado é por linha e cobre histórico/tentativas correlacionadas; tratamento pendente de erro foi desambiguado. |
| `R8-ARCH-01` | high | yes | `Integrated` | rollback virou gate em duas fases: facts atuais pré-merge e alvo antigo exato somente após switch/pre-smoke amplo. |
| `R8-ARCH-02` | high | no | `Integrated` | assumptions vivas citam paths resolvíveis, D-CUT-16 absorve source branch e gate cobre A-CUT-01..08. |
| `R8-ARCH-03` | medium | no | `Integrated` | issue cards usam `file:line`; residual risks declaram Assumption/Unknown/Confidence/Handling. |
| `R8-ARCH-04` | medium | no | `Integrated` | whitelist e consumer matrix incluem `backend/README.md` e Swagger/OpenAPI. |
| `R8-ARCH-05` | medium | no | `Integrated` | predicado canônico entra no SQL antes de count/group/order/limit/mutations; TS é defesa secundária e paginação adversarial é testada. |
| `R9-ARCH-01` | high | yes | `Integrated` | `Recovery State Machine` congela `REC-0/1/2A/2B/3`, terminal-not-active antes de restore e transição race-safe para rollback. |
| `R9-ARCH-02` | high | yes | `Integrated` | `D-CUT-17..19` e `Public Error API Contract` congelam métodos, requests, DTOs, códigos, headers, monitoramento e SSE. |
| `R9-ARCH-03` | medium | yes | `Integrated` | rotação HMAC é teste local com chaves efêmeras; Stage rotation saiu deste TODO e requer mudança aprovada separada. |
| `R9-ARCH-04` | medium | yes | `Integrated` | LISTEN/NOTIFY e polling de inserts saem do corte; refresh cobre novos erros e SSE autenticado cobre somente tratamentos API/heartbeat. |
| `R9-DOC-01` | medium | no | `Integrated` | whitelist inclui `backend/src/main.ts`; README, decorators e descrição global Swagger ficam no mesmo teste de coerência. |
| `R9-PERF-01` | medium | no | `Integrated` | `VAL-CUT-17` exige planos JSON redatados, cardinalidade, filtro antecipado e p95 3 s/8 s sem autorizar schema/index. |
| `R9-OPS-01` | medium | no | `Integrated` | `VAL-CUT-01` usa Windows Git Bash canônico; WSL direct-tool é somente diagnóstico e a falha CRLF conhecida não mascara readiness. |
| `R10-ARCH-01` | high | yes | `Integrated` | `REC-0` inclui checkpoint publicado sem mutação remota; `REC-2A/2B` serializa cancel/terminal/restore e active race força `REC-3`. |
| `R10-ARCH-02` | high | yes | `Integrated` | matriz congela método/path, campos preservados/removidos, requests, 200/400/401/403/404/503, headers, monitoramento e tratamento. |
| `R10-ARCH-03` | high | yes | `Integrated by scope reduction` | polling externo foi removido; novos erros usam refresh e stream não depende de tabela sem PK. |
| `R10-SEC-01` | high | yes | `Integrated` | EventSource/query JWT é substituído por fetch streaming com Bearer e guard global/JwtStrategy de usuário ativo; logs/URL não recebem credencial. |
| `R10-STRUCT-01` | medium | yes | `Integrated` | whitelist inclui `frontend/src/api/tipos.ts` e `frontend/src/hooks/useTempoReal.ts`; backend realtime já estava incluído. |
| `R10-PERF-01` | medium | no | `Integrated` | fixture seedada 20k/80% inelegível, PG config, warm-up, amostras, concorrência e p95 SQL versus endpoint estão congelados. |
| `R10-DOC-01` | low | no | `Integrated` | estados avançam para round 11 pending publication e repository baseline nomeia corretamente o predecessor round 10. |
| `R11-ARCH-01` | high | yes | `Integrated` | contrato congela defaults/bounds/allowlist por rota, envelope de erro e rejeição de refs brancas/duplicadas em lote. |
| `R11-STRUCT-01` | medium | no | `Integrated` | whitelist e consumer matrix incluem `frontend/README.md` com error-only/refresh/fetch-Bearer. |
| `R11-PERF-01` | medium | no | `Integrated` | `VAL-CUT-17` congela workloads, ordem, warm-ups e amostras por operação, concorrência, isolamento e fórmula nearest-rank. |
| `R11-DOC-01` | low | no | `Integrated` | round-11 material/attestation e root material/carrier são registrados exatamente; estados avançam para round 12. |
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
- **Baseline commit:** `05e27650bc717c4ad0e08bbd5d2a0517b68ebeee`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** `R11-ARCH-01`, `R11-STRUCT-01`, `R11-PERF-01` e `R11-DOC-01` integrados e publicados; round 12 governa nova confirmação.
- **Evidence / reference:** `origin/main@05e27650bc717c4ad0e08bbd5d2a0517b68ebeee`; material root baseline `MonitorNotes@85442f5ee4e6343b5ccb3b4c58b9f3d229361730`; round-11 predecessor refs preservadas no diff contract; code-origin `31712a0`; Delphi `ee9b448`.
- **Waiver authority / reference:** `n/a`.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impede alteração material entre o pacote revisado e o aprovado.
- **Trigger stage:** `after review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `canonical defaults, incluindo Diff Expectation Contract, Module Decision Baseline Snapshot e Decision Baseline (Frozen Before Implementation)`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** nenhum drift material entre o freeze round 12 e esta attestation metadata; confirmação arquitetural independente continua pendente.
- **Evidence / reference:** `review_scope_drift_guard.py@ee9b448`; baseline `uninotas-foundation:main@05e27650bc717c4ad0e08bbd5d2a0517b68ebeee`; material root baseline `MonitorNotes@85442f5ee4e6343b5ccb3b4c58b9f3d229361730`; `Overall outcome: go`.
- **Waiver authority / reference:** `n/a`.

## Frontend / Consumer Matrix

| Producer Surface In This TODO | Consumer | Delivery State | Evidence / Waiver |
| --- | --- | --- | --- |
| `GET /api/v1/notas` | React `Geral`, `ListaNotas`, session cache | `implemented candidate; final tree validation pending` | fiscal contract/browser/cache suites + Stage smoke |
| `GET /api/v1/notas/:noteId` | React `/notas/:noteId`, `DetalheNota` | `implemented candidate; final tree validation pending` | opaque-ID/detail/error tests + Stage smoke |
| `/api/v1/eventos` list/resumo/produtos/export/detalhe/payload/history | React `/erros` + `/eventos/:refId`; external consumers unknown | `final contract frozen in D-CUT-17..19; implementation planned` | exact method/request/DTO/status/header matrix; SQL predicate incl. pagination/correlated attempts; Owner attestation before deploy; no waiver |
| `/api/v1/eventos` contract documentation | `backend/README.md` + `frontend/README.md` + Swagger/OpenAPI decorators in `backend/src/logs/logs.controller.ts` + global description in `backend/src/main.ts` | `known contract consumers; update required` | docs remove five-tab/log-success/EventSource claims and describe error-only + refresh + fetch/Bearer treatment stream |
| `/api/v1/eventos/*/tratamento` unitário/lote | React error-treatment flows | `producer guard planned; behavior preserved only when original class is ERRO` | mutation tests deny `PENDENTE`/`SUCESSO` without existence disclosure |
| `GET /api/v1/realtime/eventos` | React `useTempoReal`/fetch streaming somente em `/erros` | `D-CUT-19 frozen; producer/consumer change planned` | Bearer/global guard/inactive-user negatives, no query JWT/log, treatment-only stream, cancel/refetch; Geral/detalhe fiscal não conectam |
| `GET /api/v1/monitoramento/erros` | UptimeRobot | `exact ten-field shape frozen by D-CUT-18; source projection becomes active-error-only` | header-only token, 200/401/503 + no-store; `total == erros`, `pendentes=0`, `sucessos=0`, tratados excluídos |
| `GET /api/v1/prontidao` | Railway deployment healthcheck | `new producer/config consumer planned` | PostgreSQL-down non-2xx test + `railway.json` exact path + deployed readiness evidence |
| `GET /api/v1/saude` | human/public liveness consumers | `existing contract retained as liveness; removed from Railway readiness role` | existing shape/status test + runbook distinction |
| Smart Notas env/budgets | NestJS bootstrap / Railway sealed variables | `budgets fail-closed change planned; no frontend consumer` | missing-variable startup negatives + client bundle/env scan |
| `note_read_model` / `integration_error_read_model` | Foundation registry, modules and upper canonical docs | `promotion planned only after runtime evidence` | atomic diff across policy/modules/root docs + Foundation validator |

## Test Strategy

- **Strategy (`test-first|test-after|not-applicable`):** `test-first`.
- **Why:** budgets fail-closed, readiness e predicado error-only alteram contratos de segurança/produção; cada mudança começa por um teste negativo reproduzível antes do código.
- **Fail-first targets:** flag ativa sem cada budget; PostgreSQL indisponível em readiness; SQL sem predicado `ERRO` antes de count/group/order/limit/mutations; paginação com alta proporção de `SUCESSO/PENDENTE`; filtros legados aceitos; métodos/DTOs/status/headers fora de `D-CUT-17..19`; detalhe/histórico `erro + tentativa não elegível`; JWT em query, usuário inativo no SSE, polling/LISTEN remanescente, stream não cancelado; correlation ID divergente; context/cache switch; noteId anterior após rotação local; live probe `30 s/2/30/120` até usar `10 s/4/15/60`.
- **External read-only:** `/empresa`, lista e detalhe nos dois contextos, sem mutação fiscal e com saída redatada.
- **Browser:** build local da source tree com interceptação controlada; depois smoke imediato dos bits reconstruídos no único `Stage` customer-facing.
- **Capacity:** latência, quota, concorrência e memória near-limit; planos `EXPLAIN` redatados e p95 query-side cumprem `VAL-CUT-17` antes de promoção.
- **Rollback:** fatos atuais atestados pré-merge; alvo antigo exato confirmado como rollbackable somente pós-switch/pre-smoke amplo; restore real apenas em abort, com risco residual aprovado e RTO de 10 minutos.

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before (`APROVADO|Local-Implemented|promotion`) | Status (`planned|passed|blocked|waived|n/a`) | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| backend NestJS | fiscal/config/readiness/error-only/correlation/auth mudam | startup fail-closed; DB-negative readiness; exact HTTP contract; SQL predicate before count/group/order/limit/mutations; high-ineligible pagination; correlated history; fetch-SSE global auth/no polling; same correlation ID | Node 22 host Windows; fixtures Jest determinísticas/Prisma SQL assertions; nenhum token live | no diretório `backend`: `npm test -- --runInBand && npm run lint && git diff --exit-code && npm run build`; se lint autofixar, invalidar/refazer freeze e toda validação | `Local-Implemented` | `planned` | output + SHA/tree antes/depois | `npm run lint` contém `--fix`; zero diff é obrigatório |
| backend SQL plan/performance | error-only muda todas as queries críticas | workloads fixos lista ERRO/TRATADOS, resumo, produtos, export; predicate placement; p95 SQL/HTTP 3 s/8 s | seed 20k: 80% inelegível/20% erro; 25% erros tratados; PG version/config; ordem/isolamento de `VAL-CUT-17` | por workload: 5 warmups + EXPLAIN + 30 SQL; novo processo: 5 warmups + 50 HTTP concurrency 4, ou 20 export concurrency 1; nearest-rank por série | `Local-Implemented` | `planned` | seed + JSON plans redatados + séries/p95 separados | falha abre TODO de schema/index; não amplia este diff |
| backend near-limit | envelope externo/memória | 2 MiB, fairness, semaphore 4, rates 15/60, timeout/abort/recovery | loopback stub only; `RLS_OUTPUT_DIR` redatado | no diretório `backend`: `RLS_OUTPUT_DIR=../artifacts/cutover-rls npm test -- --runInBand --runTestsByPath src/fiscal-notes/__tests__/smart-notas-load.spec.ts` | `Local-Implemented` | `planned` | `artifacts/cutover-rls` redatado | sem tráfego provider real |
| frontend React/Vite unit/race | context/cache/contract mudam | Geral/detalhe/Erros, troca rápida de contexto, logout/401 cache purge e error-only | Node 22 host Windows; fixtures locais dos scripts | no diretório `frontend`: `npm run test:notas && npm run test:notas:race && npm run lint && npm run build` | `Local-Implemented` | `planned` | output dos cinco comandos | bundle same-origin |
| frontend Playwright intercepted | jornada visível muda | login -> Geral -> detalhe -> Erros -> Geral; ambos contextos; nenhuma origem externa; `/eventos` só erro | `npm run dev` em loopback; Chrome/Chromium local em `CHROME`; todas as APIs interceptadas pelo runner | no diretório `frontend`: `ALVO=http://127.0.0.1:5173 CHROME=<chromium-local> npm run e2e:notas` | `Local-Implemented` | `planned` | relatório console redatado | adicionar negativas do history/error-only neste TODO |
| root Docker | artefato único Railway | build, startup, liveness/readiness positiva e PostgreSQL-negativa | Docker daemon; env local não secreto; candidate tree limpa | `docker build -t monitornotes:cutover-candidate .` seguido do runbook de startup/probes em `DEPLOY.md` e comparação final de tree OID | `promotion` | `planned` | image ID local + probe outputs | source-level only; OCI Railway pode divergir |
| Foundation / Delphi | TODO/authority/canon mudam | schema, diff drift, Foundation integrity e contexto PACED | links existentes; nenhum repair salvo desvio Delphi-managed | `python3 delphi-ai/tools/todo_deterministic_validator.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md && python3 foundation_documentation/deterministic/validate_foundation.py --root foundation_documentation && "/mnt/c/Program Files/Git/bin/bash.exe" -lc 'cd /c/unifast/monitordenotas && bash delphi-ai/verify_context.sh'` | `APROVADO` | `planned` | stdout dos guards | runner canônico evita incompatibilidade CRLF do wrapper sob WSL; repetir no closeout |
| live provider | binding real dos dois emissores | `/empresa`, lista e detalhe read-only em Unifast/Prosperar usando `10 s/4/15/60` | runner autorizado; cinco bindings presentes; probe implementado com envelope exato; saída redatada | no diretório `backend`: `SMART_NOTAS_PROBE_ENABLED=true SMART_NOTAS_TIMEOUT_MS=10000 SMART_NOTAS_MAX_CONCURRENCY=4 SMART_NOTAS_RATE_PER_USER_MINUTE=15 SMART_NOTAS_RATE_PER_CONTEXT_MINUTE=60 npm test -- --runInBand --runTestsByPath src/fiscal-notes/__tests__/smart-notas-live.probe.spec.ts` | `promotion` | `blocked` | output agregado/redatado | código do probe deve consumir/validar os valores, sem hardcode legado |
| Railway browser | experiência real/deployed bits | login, Geral/detalhe/Erros/Geral, ambos contextos, revision/build correta | final main tree equal; ten-key changeset consumido; readiness verde; sessão autorizada | smoke autenticado conforme `DEPLOY.md`, seguido de observação de 30 minutos | `promotion` | `blocked` | deployment ID + relatório redatado | somente após deploy autorizado |

## Plan Review Gate

- **Review decision:** `required`
- **Review status:** `round-12 material frozen; sync/attestation and architecture confirmation pending`
- **Required lenses:** architecture, operations, rollback, security, tests, performance, observability and structural soundness.
- **Known plan finding:** o health atual retorna HTTP 2xx quando o banco está degradado; `D-CUT-10` agora exige readiness separada não-2xx e mantém Smart Notas fora do loop.
- **Approval request condition:** nova revisão confirma `D-CUT-06..19`, crítica converge, baseline é atualizado e guards retornam `go/preflight-go`.

### Review Sections

- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

### Issue Cards

- **Issue ID:** `PLAN-CUT-01`
  - **Severity:** `high`
  - **Evidence:** `foundation_documentation/artifacts/environment-topology.md:24`, `foundation_documentation/artifacts/environment-topology.md:25`, `foundation_documentation/artifacts/environment-topology.md:28`, `foundation_documentation/artifacts/environment-topology.md:30`, `railway.json:7`.
  - **Why it matters now:** o primeiro rebuild e smoke alcançam usuários reais; fatos atuais devem ser atestados antes do merge e o rollback target exato só pode ser confirmado após o switch, antes do smoke amplo.
  - **Option A (Recommended):** cutover direto somente 20:00–22:00, após source/build local, ten-key changeset staged, facts atuais/Owner atestados e gate pós-switch do antigo ID com `Rollback`.
    - **Effort:** `medium`
    - **Risk:** `medium`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `low`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `neutral`
    - **Structural soundness impact:** `improves`
  - **Option B (Alternative):** criar ambiente isolado/PR antes do corte.
    - **Effort:** `high`
    - **Risk:** `low`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `medium`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `improves`
    - **Structural soundness impact:** `improves`
  - **Option C (Do Nothing):** ativar fora da janela sem gates.
    - **Effort:** `low`
    - **Risk:** `high`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `high`
    - **Performance impact:** `unknown`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Recommendation:** Option A, porque mantém o prazo aceito sem ocultar risco e exige contenção/rollback em até 10 minutos; B requer novo escopo e C é proibida.

- **Issue ID:** `PLAN-CUT-02`
  - **Severity:** `high`
  - **Evidence:** `backend/src/logs/logs.service.ts:64`, `backend/src/logs/logs.service.ts:201`, `backend/src/logs/logs.service.ts:284`, `backend/src/logs/logs.service.ts:301`, `backend/src/logs/logs.sql.ts:194`, `backend/src/logs/logs.mapper.ts:262`.
  - **Why it matters now:** um detalhe de erro pode vazar uma tentativa `SUCESSO/PENDENTE` e reintroduzir PostgreSQL como fonte de sucesso.
  - **Option A (Recommended):** aplicar o predicado central por linha em reads, histórico correlacionado, mutations, monitoramento, realtime e UI; consumidor externo desconhecido bloqueia deploy.
    - **Effort:** `medium`
    - **Risk:** `low`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `low`
    - **Performance impact:** `improves`
    - **Elegance impact:** `improves`
    - **Structural soundness impact:** `improves`
  - **Option B (Alternative):** criar endpoint temporário separado para compatibilidade de sucessos.
    - **Effort:** `high`
    - **Risk:** `high`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `high`
    - **Performance impact:** `regresses`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Option C (Do Nothing):** manter inventário sem enforcement por linha.
    - **Effort:** `low`
    - **Risk:** `high`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `high`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Recommendation:** Option A; é a única que entrega uma autoridade única e verificável sem dual-read.

- **Issue ID:** `PLAN-CUT-03`
  - **Severity:** `high`
  - **Evidence:** `backend/src/config/configuration.ts:38`, `backend/src/config/configuration.ts:170`, `railway.json:3`, `foundation_documentation/artifacts/environment-topology.md:28`, `foundation_documentation/artifacts/environment-topology.md:29`, `foundation_documentation/artifacts/environment-topology.md:75`.
  - **Why it matters now:** identidade de source, atomicidade da flag e recuperação não podem depender de uma revision inexistente ou de rebuild mutável.
  - **Option A (Recommended):** validar source tree, exigir tree OID igual no `main`, commit staged de dez variáveis sem redeploy, capturar revision só após merge, validar bits remotos e usar stored-image `Rollback`.
    - **Effort:** `medium`
    - **Risk:** `medium`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `low`
    - **Performance impact:** `improves`
    - **Elegance impact:** `improves`
    - **Structural soundness impact:** `improves`
  - **Option B (Alternative):** publicar OCI imutável por pipeline dedicado e criar alvo isolado.
    - **Effort:** `high`
    - **Risk:** `low`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `medium`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `improves`
    - **Structural soundness impact:** `improves`
  - **Option C (Do Nothing):** tratar build local como implantado, ativar flag separadamente e usar redeploy como rollback.
    - **Effort:** `low`
    - **Risk:** `high`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `high`
    - **Performance impact:** `unknown`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Recommendation:** Option A no escopo/prazo atual; B é follow-up de hardening e C é proibida.

### Failure Modes & Edge Cases

- [ ] Candidate e final `main` têm tree OID diferente: bloquear promoção e refazer freeze/CI.
- [ ] Changeset staged não pode ser commitado sem redeploy ou não contém exatamente dez chaves: abortar antes do merge.
- [ ] Pré-merge sem plano/ID/snapshot/acesso geral, ou pós-switch sem `Rollback` no antigo ID exato antes do smoke amplo: abortar ou renovar risco/RTO para fallback `Redeploy`.
- [ ] Railway cria revision de source/config inesperadas ou readiness/smoke falha: abortar e acionar rollback.
- [ ] Binding fiscal diverge, ocorre cross-context, segredo/PII vaza, quota/memória satura: abortar imediatamente pelos thresholds.
- [ ] Linha principal é `ERRO`, mas histórico correlacionado contém `SUCESSO/PENDENTE` original: filtrar cada linha; tratamento `PENDENTE` do erro continua visível.
- [ ] Predicado aplicado só depois da query: bloquear por totais/páginas/agregações incorretos; teste estrutural deve provar filtro SQL antes de count/group/order/limit/mutations.
- [ ] Filtros `PENDENTE/SUCESSO` ainda aceitos, resumo mantém campos removidos, ou detalhe/tratamento revela ref inelegível: bloquear promoção por contrato público divergente.
- [ ] Defaults/allowlists divergem, resumo/export aceitam paginação ignorada, lote aceita ref branca/duplicada, ou erro sai fora do envelope comum: bloquear promoção.
- [ ] README, decorators OpenAPI ou descrição Swagger global ainda anunciam cinco abas/sucesso legado: bloquear promoção por contrato incoerente.
- [ ] Realtime ainda aceita JWT em query, ignora o guard global, abre conexão PostgreSQL/polling/NOTIFY, emite `evento.novo`, ou deixa stream vivo após logout/unmount: bloquear promoção.
- [ ] Plano SQL filtra inelegíveis após window/group/limit, executa scan correlacionado por linha, ou excede p95 `3 s` (`8 s` export): bloquear e abrir TODO separado de schema/index.
- [ ] Abort com candidato in-flight restaura config antes do terminal, ou candidato fica active durante cancel sem migrar para `REC-3`: interromper ações concorrentes, classificar estado real e seguir somente a transição canônica.
- [ ] Rotação HMAC remota aparece no changeset Stage: remover; rotação operacional exige TODO/janela/aprovação próprios.
- [ ] Lint com `--fix` altera a tree: invalidar o checkpoint e repetir toda validação antes de novo freeze.

### Residual Unknowns / Risks

- [ ] **Assumption:** os budgets `10 s/4/15/60` cabem na quota. **Unknown:** quota real Smart Notas até probe/carga. **Confidence:** `Low`. **Handling:** 429 threshold aborta; aumento exige nova aprovação.
- [ ] **Assumption:** nenhum consumidor externo depende de sucesso em `/eventos`. **Unknown:** integrações fora do repositório até attestation do Owner. **Confidence:** `Low`. **Handling:** bloqueia deploy ou exige aceite explícito de hard cut.
- [ ] **Assumption:** o changeset staged e a deployment corrente correspondem ao alvo confirmado. **Unknown:** configuração/revision servidas até inspeção da janela. **Confidence:** `Medium`. **Handling:** bloquear antes do merge se divergir.
- [ ] **Assumption:** após o switch, o antigo deployment ID oferece `Rollback`. **Unknown:** visibilidade/elegibilidade do alvo exato até ele virar previous deployment. **Confidence:** `Medium`. **Handling:** verificar antes do smoke amplo; ausência aborta ou exige risco/RTO renovados.
- [ ] **Assumption:** a source tree validada produz um runtime aceitável. **Unknown:** bits exatos do rebuild com base/apt mutáveis. **Confidence:** `Medium`. **Handling:** readiness e smoke dos bits remotos são obrigatórios; não alegar OCI idêntico.
- [ ] **Assumption:** o dataset representativo reproduz seletividade/custo atual dos logs. **Unknown:** estatísticas reais do Stage sem capturar dados. **Confidence:** `Medium`. **Handling:** registrar cardinalidade/razão inelegível e revalidar p95/planos com evidência redatada antes do merge; falha abre TODO próprio.

## Security Risk Assessment

- **Risk level:** `high`
- **Why this risk level:** dois tokens fiscais, CNPJs, HMAC, dados autenticados e configuração de produção.
- **Attack surface in scope:** secret store, logs/ingress, probes, binding, noteId, Bearer/SSE, deploy output, responses e rollback.
- **Attack simulation decision:** `required before Stage cutover`
- **Required result:** nenhum vazamento, JWT em URL/log, usuário inativo no stream, cross-context, SSRF/redirect ou aceitação de noteId antigo/corrompido.
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
- **Gate status:** `no_material_findings`
- **Evidence / reference:** `Overall outcome: go`; `A-CUT-01..08` cobertos; assumptions vivas `A-CUT-05..08` resolvem para `railway.json`, `backend/src/config/configuration.ts`, `backend/src/health/health.controller.ts`, `backend/src/logs/logs.controller.ts` e testes/artefatos adjacentes.

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
