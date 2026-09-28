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
- **Next exact step:** publicar attestation round35 sobre material Foundation `985b5d13d96a46bd8107e8796986f4704838133c` / carrier root `b02b8c7646ed894b08abb4e76db6be1483f2ae8b`, então repetir arquitetura/crítica; coherence/drift continuam bloqueados. Nenhuma implementação ou mutação Railway está autorizada.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** a crítica round34 confirmou as correções arquiteturais, mas encontrou o ramo pré-merge com deployment inesperado fora da terminalização/zero; round35 integra esse gap.
- **Exit condition:** preflight read-only de capacidade conclusivo, decisões `D-CUT-06..42` congeladas, arquitetura/crítica/coherence/drift causalmente vinculadas ao mesmo round e `todo_authority_guard.py --pre-approval` em `preflight-go`.

## Provisional Notes

- **Missing for production-ready:** implementação reconvergida, configuração remota, probes reais, carga local do build candidato, attestation do rollback target, rebuild/cutover/smoke no Stage e promoção Foundation.
- **Revisit criteria:** concluir `DOD-CUT-01..40` com evidência redatada da deployment exata.
- **Dependencies unblocked:** o código local permite preparar o cutover sem redesenhar contratos de lista/detalhe.

## Blocker Notes

- **Blocker:** nenhuma mutação Railway pode ocorrer antes da revisão formal, `preflight-go` e nova aprovação operacional específica.
- **Why blocked now:** material round35 está publicado e integra o recovery pré-merge; attestation e reviews correntes ainda precisam ocorrer.
- **What unblocks it:** round35 publicado/atestado, arquitetura/crítica limpas, coherence/drift rerodados depois da crítica e vinculados aos dispatches correntes, capacidade e probes do prior preflighted, guards `preflight-go` e `APROVADO` explícito.
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
- [ ] `CUT-03` Manter toda leitura fiscal fechada por boot; um ADMIN executa probe redatado `/empresa`, lista e detalhe para os dois contextos e só então abre a barreira fiscal. Mismatch nunca libera dados. A UI só mostra cache mediante lease positiva do boot atual obtida por handshake no enter/focus/resume e renovada enquanto visível; restart não observado admite exposição stale residual de no máximo 5 s, explicitamente sujeita à aprovação final.
- [ ] `CUT-04` Exigir no startup timeout `10 s`, concorrência `4`, rate `15 req/min` por usuário e `60 req/min` por contexto na única réplica; validar esse envelope com carga/respostas próximas de 2 MiB. Qualquer mudança exige rebaseline e nova aprovação.
- [ ] `CUT-05` Comprovar destino, retenção, acesso e redaction dos logs operacionais antes da ativação.
- [ ] `CUT-06` Provar localmente a tree candidata com build Docker, readiness, probes Smart Notas redatados, smoke autenticado e jornada de navegador nos dois contextos; Railway fará rebuild remoto e os bits reais só serão validados pelo smoke no Stage.
- [ ] `CUT-07` Antes do changeset/merge, registrar deployment/plano/snapshot/Owner/capacidade de rollback, runner direto/session-affine e permissões `Remove`/Auto-deploy. Abort segue `REC-0/1/1X/2A/2B/3A/3B/3C/4`; todo Active termina `Removed`: 3A faz quiesce gracioso do reviewed antes de remove-all, 3B remove-all direto; zero2s precede Rollback no ID anterior exato e REC-3C prova a convergência. Auto-deploy/source stabilization<=24 h só se main foi promovida; RTO runtime10 é condicionado.
- [ ] `CUT-08` Executar um único cutover direto no `Stage` customer-facing entre 20:00–22:00, observar por no mínimo 30 minutos e abortar pelos thresholds congelados.
- [ ] `CUT-09` Validar rotação HMAC somente em teste local determinístico com chaves efêmeras: após substituição, `noteId` anterior falha fechado e a relistagem produz IDs válidos. Rotação de segredo no `Stage` é uma mudança operacional separada, fora deste cutover.
- [ ] `CUT-10` Promover atomicamente `note_read_model` para Smart Notas nos módulos/ledger somente após smoke e rollback aprovados.
- [ ] `CUT-11` Tornar PostgreSQL `logs` exclusivamente uma fonte de erros Routerfy/n8n: um predicado SQL canônico pela classificação original `ERRO` entra antes de `COUNT`, agrupamento, ordenação, paginação/limite e mutations em lista, resumo, produtos, exportação, detalhe, payload, histórico correlacionado, tratamento unitário/lote e monitoramento. Um espelho TypeScript é só defesa secundária. Tratamento/reabertura `PENDENTE` de erro original continua elegível; classificação original `PENDENTE`/`SUCESSO` não. Inventário externo é gate antes do deploy.
- [ ] `CUT-12` Propagar um único correlation ID do request autenticado até o adapter Smart Notas, limitar `actorId` a identificador interno pseudônimo e atualizar `DEPLOY.md` com ordem atômica de variáveis/readiness/deploy/rollback.
- [ ] `CUT-13` Promover por PR apenas uma tree Git equivalente ao candidato validado; registrar candidate SHA/tree OID, final main SHA/tree OID e revision Railway. A imagem local é evidência source-level, não o OCI implantado; mismatch de tree bloqueia/aborta, e o primeiro smoke Stage valida os bits do rebuild remoto.
- [ ] `CUT-14` Manter `uninotas-foundation:main` como autoridade independente após a promoção canônica; não sincronizar o gitlink documental em `MonitorNotes:main` neste closeout para evitar segundo auto-deploy. Registrar follow-up para o próximo release aprovado.
- [ ] `CUT-15` Antes do merge, migrar/atestar o consumidor UptimeRobot para `x-monitor-token` na release corrente sem rotacionar token; se o token não estiver configurado, atestar modo público. Consumidor/configuração desconhecidos bloqueiam o corte.
- [ ] `CUT-16` Endurecer export CSV e inputs legados: neutralizar fórmulas em todo texto externo, inclusive LF inicial, limitar `refId` a 1..64 após trim e token de monitoramento a 1..200, e coalescer bursts realtime em janelas fixas sem starvation.
- [ ] `CUT-17` Serializar tratamentos concorrentes por `refId` no PostgreSQL, com topologia Prisma candidata `read=4,pool_timeout=2`, `writer/fence=1,pool_timeout=2,max_idle_connection_lifetime=0`, `control=1,pool_timeout=1,connect_timeout=1,socket_timeout=1,statement_timeout=200ms` e teto **por processo candidato** `C=6`; control serve inspeção e sampler readiness single-flight, uma statement por chamada, sem transaction/`pg_sleep`/wait assíncrono. Lock namespaced, ordem lexical binária, timestamp monotônico pós-lock, `ReadCommitted`, budgets `2 s/15 s/1,5 s/12 s`, um writer/500 locks, retry só após rollback comprovado, 409/503 estáveis e SSE pós-commit. Separar orçamento steady-state do transitório e provar as inequalities global/database/role da matriz disjunta antes do switch.
- [ ] `CUT-18` Tornar o cutover cross-version fail-closed para tratamentos: overlap `0`/drain `20`; cada boot UUID nasce fechado e timer/abrir usam epoch-CAS. Abertura exige anterior terminal, datasource direto/session-affine, fence advisory session-level exclusivo no client writer de uma conexão e contagens separadas sem candidata anterior/não candidata. Toda transação valida PID/lock do fence antes de escrever; perder/recriar sessão nunca reacquire automaticamente. Lease local libera exact-once no settle; commit incerto pode deixar sessão/fence observáveis ou encerrados, mas em ambos falha 503/refresh sem SSE/retry e recovery aguarda prova externa. Runner externo é comprovado no preflight antes do APROVADO e repetido antes do merge; pós-switch distingue zero candidata de sessões legítimas do legado.
- [ ] `CUT-19` Fixar Prisma runtime/CLI exatamente em `6.19.3`; writer usa `max_idle_connection_lifetime=0`, heartbeat de fence <=30 s e opener single-flight/owner-token com profundidade advisory exatamente `1`. Connection-loss/commit incerto cobre separadamente sessão ainda observável e sessão encerrada, sempre sem retry/SSE e com refresh autoritativo.
- [ ] `CUT-20` Adicionar quiesce fiscal ADMIN one-way e integrá-lo ao SIGTERM antes de qualquer await; em rollback normal, invalidar epoch/leases antes de treatments. Se a API candidata estiver indisponível, usar somente o ramo out-of-band pré-atestado `Remove -> runner zero estável -> Rollback`.
- [ ] `CUT-21` Congelar revogação fiscal em até 35 s: cache de identidade monotônico de 30 s mais lease fiscal monotônica de no máximo 5 s; testar desativação imediatamente após cache fill. Mudança de perfil não revoga leitura porque todos os setores ativos são viewers.
- [ ] `CUT-22` Se `L` não puder ser provado autoritativamente, este TODO para sem release preparatória. Abrir TODO tático próprio para cap4; após sua promoção verde, recomeçar este cutover no novo `main`/rollback baseline e repetir freeze, CI, reviews e tree equivalence.
- [ ] `CUT-23` Readiness pública lê apenas snapshot atômico de sampler interno fixed-cadence 250 ms, nunca toca DB por request. Snapshot positivo expira em 500 ms; sampler é single-flight, deadline end-to-end 1000 ms e falha/atraso torna readiness 503. Flood não cria fila/statement PostgreSQL.
- [ ] `CUT-24` Compor autorização cacheada com conclusão assíncrona: carregar deadline monotônico da identidade em cada request, revalidar antes de serializar dado fiscal ou concluir CAS ADMIN se o deadline foi cruzado e encerrar SSE no deadline, sem evento posterior.
- [ ] `CUT-25` Criar fase `Active-fiscal-fechada` cuja allowance local178 s inicia abort até real180 s sob observador/control saudáveis; somente até esse deadline o 503/header exato é expected/contado separado. Recovery visível segue RTO10 condicionado.
- [ ] `CUT-26` Executar `L`/G/D/R/O*/Xd/Xr/runner/inequalities como preflight read-only antes de solicitar autoridade de implementação; resultado inconclusivo encerra este TODO e roteia imediatamente ao TODO cap4.
- [ ] `CUT-27` Separar shutdown interno de quiesce externo: SIGTERM fecha sincronamente sem auth; ambos POST quiesce exigem revalidação sem cache de usuário ativo+ADMIN e só então fazem compare-and-transition síncrono sem await intermediário.
- [ ] `CUT-28` Medir o deadline de início do abort desde Active com observador pré-merge, poll/deadline1 e atraso máximo2; usar local178 e sinalizar abort/breach em gap/restart, sem alegar recuperação concluída em180 s.
- [ ] `CUT-29` Após registrar o trigger candidato, desligar autodeploy. Sucesso o reativa somente após observação verde e source/runtime coerentes; abort mantém off e entra em estabilização de source com owner/prazo/revert revisado antes de reativar.
- [ ] `CUT-30` Vincular critique/coherence/scope-drift satisfatórios ao mesmo round e às refs material/attestation/architecture exatas; status histórico nunca satisfaz o preflight corrente, mesmo se o guard genérico retornar go.
- [ ] `CUT-31` Estabelecer freeze exclusivo de source antes do changeset: somente o merge revisado exato pode avançar, zero deployment queued/in-flight deve ser provado e qualquer push/revision extra aborta até prevenção/remoção e zeros externos.
- [ ] `CUT-32` Congelar o control plane Railway sob operador único: monitorar continuamente runtime/deployments por fingerprint redatado e validar configuração por changeset/activity checkpoints; qualquer restart/redeploy/scale/config/approval/platform deployment não aprovado é candidato inesperado e aborta sem restart allowance.
- [ ] `CUT-33` Tratar 178/180 s como deadline de classificação e início do abort, não de recuperação visível; depois do deadline o 503 deixa de ser esperado e o RTO condicionado de recovery governa.
- [ ] `CUT-34` Criar convergência pós-Rollback comum: prior image+variables exatos Active, probe real da imagem anterior verde e candidatos zero estável antes de REC-4.
- [ ] `CUT-35` Separar freeze do runtime de freeze da configuração: runtime/deployments permanecem sob polling contínuo; configuração usa changeset de dez chaves, zero staged changes e cursor/eventos da activity feed em cada transição irreversível. Mudança value-only com mesmo nome/escopo é proibida e aborta mesmo sem redeploy; incapacidade de obter sequência autoritativa/conclusiva bloqueia antes do changeset.
- [ ] `CUT-36` Congelar antes do merge um recovery probe específico da imagem anterior: rotas realmente suportadas, `/api/v1/saude` com corpo `status=ok,banco=ok` em vez de HTTP isolado, autenticação/consulta legada e `SELECT 1` externo. REC-3C não exige `/prontidao` de uma imagem que não a possui.
- [ ] `CUT-37` Classificar trigger/deployment inesperado desde a primeira mutação de configuração, mesmo antes do merge. REC-1 só restaura config quando há prova contínua de runtime inalterado e nenhum candidato possível; pre-merge never-Active exige terminal+zero, e qualquer Active exige remove-all+zero+Rollback+REC-3C. REC-4 só ocorre se `main` foi promovida.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `MonitorNotes:delphi-and-foundation`; `uninotas-foundation:main` (canonical main-only documentation authority)
- **Promotion lane path:** `delphi-and-foundation candidate tree -> local source/build validation -> PR with identical final tree on main -> Railway remote rebuild -> single Stage customer-facing cutover -> independent Foundation runtime promotion`
- **Lane-promoted threshold for this TODO:** `main com checkpoint aprovado e CI-equivalent verde`
- **Production-ready threshold for this TODO:** `Stage customer-facing com smoke e 30 minutos de observação; rollback target atestado e, se acionado, restaurado em até 10 minutos; promoção Foundation concluída`
- **Execution topology:** `principal checkout, single code writer; worktrees/auxiliary checkouts forbidden`

## Promotion Evidence

| Scope Item | Local Branch/Commit | Main / Authority | Local Source/Build Validation | Single Remote Target: Stage Customer-Facing | Current Status |
| --- | --- | --- | --- | --- | --- |
| Backend + frontend read-only | round35 material carrier `b02b8c7646ed894b08abb4e76db6be1483f2ae8b`; code-origin `31712a042cab3c796d5daca7350c6c58453e1c73`; attestation pending | `pending promotion to main` | `pending final cutover suite` | `pre-implementation capacity hard stop; otherwise direct fiscal cutover` | `round35 material published; attestation pending` |
| Foundation cutover contract | round35 material `985b5d13d96a46bd8107e8796986f4704838133c`; attestation pending | `main-only authority` | `n/a` | `pending runtime promotion after observed cutover` | `round35 material published; attestation pending` |

## Out of Scope

- Emissão/cancelamento, DANFE/XML e novos relatórios/exportações fiscais Smart Notas; a exportação legada de `/eventos` permanece em escopo apenas para restringi-la a erros.
- Alteração de schema Prisma/PostgreSQL ou persistência de espelho/cache de notas; a serialização usa advisory transaction locks e o schema existente.
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
| `D-CUT-20` | A rejeição de token em query do monitor só entra após migração comprovada do UptimeRobot na release atual: se `MONITORAMENTO_TOKEN` estiver configurado, cadastrar `x-monitor-token`, remover credential da URL e provar 200/401 sem revelar/rotacionar o valor; se ausente, atestar modo público. Estado/consumer desconhecido bloqueia merge. A rotação não pertence ao changeset de dez chaves. | Evita derrubar o monitor durante o hard cut e mantém segredo fora da URL sem criar segunda mudança Railway. | `frozen; approval-material` |
| `D-CUT-21` | Todo `refId` de path/lote é trimado, deve ter 1..64 caracteres e falha 400 se branco/oversize; só ref válido inexistente/inelegível retorna 404. `MONITORAMENTO_TOKEN` configurado e header oferecido devem ter 1..200 caracteres; config fora do bound falha startup e header fora do bound retorna 400. Export CSV prefixa `'` em todo scalar textual externo cujo primeiro caractere seja `=`, `+`, `-`, `@`, TAB, CR **ou LF** antes do escaping CSV. | Alinha varchar persistido, limita inputs e neutraliza spreadsheet formula injection. | `frozen; approval-material` |
| `D-CUT-22` | O consumidor React coalesce `evento.tratado` em janelas **fixas** de 250 ms iniciadas pelo primeiro evento ainda não representado; eventos posteriores nunca estendem a janela. No fechamento ocorre no máximo um refetch de lista e um de resumo. Se eventos chegarem durante refetch in-flight, agenda-se no máximo uma próxima janela, sem requests duplicadas/paralelas do mesmo recurso. O refetch começa <=250 ms após o primeiro evento da janela, mais apenas o tempo da request anterior já em voo; nenhum fluxo sustentado causa starvation. Um lote síncrono de 500 refs produz exatamente um par. | Evita tempestade de requests e o adiamento indefinido causado por debounce trailing sob eventos contínuos. | `frozen; approval-material` |
| `D-CUT-23` | Tratamentos usam `serialize`; Prisma/Client `6.19.3`. Clients: read `connection_limit=4,pool_timeout=2`; writer `1/2,max_idle_connection_lifetime=0`; control `1/1,connect_timeout=1,socket_timeout=1` e connection option `statement_timeout=200ms`; total candidato `C=6`. Control executa uma statement por inspeção/sampler, nunca transaction/`pg_sleep`/wait; operação async só após devolução. A matriz disjunta congela legado/candidato na mesma app role/database e runner `X=1` com flags `Xd/Xr`. `G=max_connections-superuser_reserved_connections-reserved_connections` (setting ausente=0); `D=datconnlimit`, `R=rolconnlimit`, `-1=infinito`. Budgets `Og/Od/Or` excluem explicitamente `L`, `C` e runner e vêm de cap/config autoritativo. Margens: `Mg=max(5,ceil(.20*(G-Og)))` e, se finitos, `Md/Mr` análogos. Exigir separadamente `L+C+1+Og+Mg<=G`, `L+C+Xd+Od+Md<=D` e `L+C+Xr+Or+Mr<=R`; classe/role/database/budget desconhecido bloqueia. Sem `L` autoritativo, hard stop/D-CUT-28. Writer/gate/locks/retry/SSE permanecem. Sampler readiness segue D-CUT-29: deadline1000 ms, inspeção adversarial+DB-drop, snapshot stale500 fail-closed, zero P2024 e zero query/sessão órfã 2 s após recovery. | Torna control bounded, capacidade reproduzível e readiness independente da admissão HTTP pública. | `frozen; approval-material` |
| `D-CUT-24` | `railway.json` usa overlap `0`/drain `20`. Cada boot nasce fechado; primeiro request autenticado arma uma vez 30 s. Timer/abrir usam CAS `{bootId,epoch,state}`. SIGTERM interno incrementa epoch antes de await; quiesce HTTP externo segue a prova fresca e a transição síncrona de `D-CUT-33`. `RuntimeIdentityService` gera UUID v4 lowercase. Clients session-affine usam nomes exatos base/writer/control/treatment 45/52/53/55; identidade incerta/multiplexing bloqueia. Antes de qualquer aquisição, `/abrir` faz transição síncrona single-flight para `abrindo`, cria owner token ligado a boot/epoch e rejeita outro opener; somente esse owner pode chamar `pg_try_advisory_lock` uma vez, garantindo profundidade `1`. O writer pool1 com `max_idle_connection_lifetime=0` registra PID e mantém heartbeat <=30 s: fora de transaction ele verifica PID/`pg_locks`; durante lease a própria transaction verifica. Falha ou políticas server-side/proxy incompatíveis quiescem sem auto-reacquire. Toda transaction exige mesmo PID e row granted antes do domínio. O control classifica cinco contagens sem expor UUID. O opener prova prazo/anterior terminal/runner, exige zeros aplicáveis e finaliza apenas por CAS do owner; stale/quiesced vence 409. Cleanup central idempotente faz no máximo um unlock pelo mesmo PID/owner; quiesce/SIGTERM esperam o single-flight assentar e nunca incrementam profundidade. Cada PATCH/lote adquire lease sync e libera exact-once no settle. Commit incerto tem dois casos válidos: (a) resposta perdida com PID/fence e possível transaction ainda observáveis; (b) sessão encerrada com PID/fence/transaction ausentes. Ambos liberam lease uma vez, retornam 503/refresh, não publicam SSE nem repetem; estado autoritativo é relido e rollback/sucessor só avançam após prova externa coerente. Recovery mantém os gates anteriores e pós-switch. Nenhuma variável/chave ou schema é adicionada. | Sustenta o fence além do idle padrão, elimina reentrância advisory e modela corretamente os dois resultados de connection-loss. | `frozen; approval-material; Config as Code válido no corte e requer migração IaC antes de 2026-12-01` |
| `D-CUT-25` | Barreira fiscal per-boot nasce fechada. `GET /notas`/detail fechados retornam header503 e zero provider. `GET /notas/estado` exige qualquer viewer autenticado, não chama Smart Notas/DB e retorna no-store `{estado,bootId,epoch,leaseExpiraEm}`. Antes do request, o cliente captura `requestStart=performance.now()` e geração; resposta aberta só instala deadline monotônico `requestStart+5000ms` se chegar antes dele, descontando toda latência e sem usar relógio de parede para estender. Todo render revalida `performance.now()<deadline`; timers atrasados/background nunca prolongam. Cache fica armazenado, invisível sem lease positiva do boot/epoch atual; enter/focus/resume suprime antes do handshake e, visível, renova a cada 3 s com timeout1 s. Falha/503, expiração, boot/epoch/generation diferente ou resposta antiga suprime e impede repopulação. Header fiscal invalida imediatamente. Após restart não observado, exposição máxima aceita é 5 s desde o início do último handshake válido. POST ADMIN continua único bypass de probe/abertura. | Preserva cache rápido, elimina clock-skew/RTT do bound e torna a exposição residual verificável por relógio monotônico. | `frozen; approval-material` |
| `D-CUT-26` | Fiscal gate possui `quiescida` one-way. POST ADMIN `/operacao/notas/quiescer` valida confirmação exata e segue `D-CUT-33`: prova identidade/ADMIN fresca sem cache e somente então incrementa epoch/fixa quiescida sincronamente, sem await entre prova e transição; `GET /notas/estado` a projeta como fechada com novo epoch. SIGTERM interno executa a transição síncrona antes do treatment shutdown e de qualquer await. Provar-e-abrir após quiesce retorna 409 até process exit. No REC-3 normal, quiesce fiscal precede treatment quiesce. | Torna a ação pré-rollback executável, impede quiesce externo por ADMIN revogado e invalida leases mesmo se waits posteriores falharem. | `frozen; approval-material` |
| `D-CUT-27` | `JwtStrategy` mede o cache de identidade com relógio monotônico por 30.000 ms. Usuário desativado logo após cache fill pode continuar viewer por no máximo 30 s e a última lease fiscal por no máximo mais 5 s desde seu request start: bound combinado <=35 s. Ao primeiro 401/ausência de identidade, frontend invalida lease/cache visível. Mudança de perfil entre setores não revoga leitura, pois todo usuário ativo pode visualizar notas; endpoints ADMIN revalidam perfil após o mesmo cache bound. | Reconcilia o contrato fiscal com a política canônica de identidade sem adicionar query DB a cada heartbeat. | `frozen; residual <=35 s requires final approval` |
| `D-CUT-28` | Falha em provar `L` é hard stop deste TODO. A release cap4 não ocorre nesta execução: exige TODO próprio, aprovação/promoção/evidência próprias; depois, este cutover reabre sobre novo main/deployment rollback, refaz baseline, CI-equivalent, reviews, capacidade e tree equivalence. | Evita esconder uma segunda release dentro de um cutover validado contra tree anterior. | `frozen; approval-material` |
| `D-CUT-29` | Readiness pública nunca consulta DB por request. Um sampler interno fixed-window a cada 250 ms, single-flight/sem overlap, usa o control client com uma statement e deadline end-to-end 1000 ms; publica snapshot atômico monotônico. `/prontidao` responde síncrono pelo snapshot: 2xx somente success com idade <=500 ms; ausência, failure ou stale retorna 503/no-store. Flood não cria waiter/fila/statement DB; se event-loop atrasar, snapshot expira fail-closed. Após DB drop, qualquer positivo expira em <=500 ms; então probes são 503 e p95 handler <=100 ms. | Isola healthcheck de tráfego público e ainda detecta banco indisponível sem falso positivo prolongado. | `frozen; approval-material` |
| `D-CUT-30` | Cada validação/cache fill de identidade produz `identityValidUntilMonotonic=validatedAt+30000ms`, carregado no request. Se uma resposta autenticada sensível estiver pronta após esse deadline, o backend revalida identidade ativa sem cache antes de serializar qualquer payload; falha retorna 401 sem dados. Streams duram `min(30s, remainingIdentityValidity)` e não emitem no/após deadline; reconnect reautentica. Todo opener ADMIN assíncrono revalida sem cache usuário ativo e role ADMIN imediatamente antes do CAS final irreversível, além do epoch/owner check. Mutation de tratamento que cruza o deadline revalida usuário ativo e role autorizada dentro da transaction imediatamente antes do write/commit. Quiesce externo irreversível também exige a prova fresca de `D-CUT-33`; somente SIGTERM interno prescinde do auth path. A lease frontend permanece limitada a `requestStart+5s`, de modo que revogação após fill fica <=35 s e APIs diretas/streams não ultrapassam o deadline sem nova prova. | Faz o bound valer na emissão/commit, não apenas na admissão, sem query por heartbeat nem por evento dentro da validade. | `frozen; approval-material; residual <=35 s requires final approval` |
| `D-CUT-31` | Cada boot candidato observado `Active` com gate fiscal fechada entra em `Active-fiscal-fechada`. O observador de `D-CUT-34` está contínuo antes do merge; deadline local `firstObservedActive+178s` inicia abort até 180 s após Active quando observador/control path satisfazem o bound <=2 s. Isso **não** promete recuperação visível em 180 s: ao deadline, 503/header deixa de ser esperado/excluído e vira incidente sob RTO condicionado de recovery <=10 min; perda do observador/control path é breach fail-closed. Restart pré-abertura não estende; gap>2 s/reconnect/ambiguidade inicia abort sem allowance. Antes do deadline, só 503/header exato é esperado/contado separado; demais falhas abortam. Abertura deve concluir antes do deadline. Primeiro restart pós-open recebe a mesma allowance de classificação apenas se aprovado/esperado por D-CUT-38; qualquer outro aborta. Segundo restart aborta. Janela 20:00–22:00 nunca estende. | Separa honestamente budget de detecção/início do abort do tempo de recuperação customer-facing e evita exclusão SLO indefinida. | `frozen; approval-material` |
| `D-CUT-32` | Antes de solicitar `APROVADO` de implementação, executar preflight exclusivamente read-only e redatado na release/baseline corrente: provar `L` por configuração/engine log autoritativo, app role/database, G/D/R, Og/Od/Or, Mg/Md/Mr, Xd/Xr, runner/ACL/session-affinity e viabilidade das três inequalities com `C=6`. Snapshot instantâneo não prova `L`. Qualquer fato/classe/cap inconclusivo encerra este TODO antes de código; abre-se TODO cap4 próprio. Resultado verde é gate de entrada, mas deve ser repetido <=15 min antes do merge; divergência posterior invalida implementação evidence pertinente e bloqueia `REC-2A`. | Resolve cedo a bifurcação que poderia descartar toda a implementação e mantém a prova fresca no corte. | `frozen; approval-material` |
| `D-CUT-33` | Shutdown interno e quiesce HTTP são caminhos separados. SIGTERM executa fechamento fiscal e treatment sincronamente antes de qualquer await. Cada POST externo `/operacao/{notas|tratamentos}/quiescer`, inclusive retry idempotente, primeiro revalida sem cache usuário ativo+ADMIN; falha 401/403 sem mudar estado. Após a prova, captura boot/epoch e executa compare-and-transition síncrono sem qualquer await intermediário; opener/mutation que avançou durante a revalidação é invalidado/drenado pelo novo epoch. Se auth/DB não for confiável em recovery, controles são considerados indisponíveis e usa-se REC-3B. | Impede que ADMIN revogado cause indisponibilidade irreversível sem sacrificar o shutdown interno fail-closed. | `frozen; approval-material` |
| `D-CUT-34` | O observador inicia antes do merge e consulta Railway status + bootId/barreira em intervalo<=1 s, request deadline<=1 s. Transição/restart só recebe fase com amostra anterior contínua e gap<=2 s; `firstObservedMonotonic+178s` limita o início do abort a <=180 s desde Active sob caminho saudável, não a conclusão da recuperação. Gap>2 s, reconnect/restart do observador, timestamp/event identity ausente ou estado ambíguo sinaliza abort/breach imediatamente e nunca cria allowance nova. A regra vale pós-open, subordinada ao fingerprint/control-plane de D-CUT-38. | Ancora a classificação ao evento com atraso bounded sem prometer que Railway Remove/Rollback termina no mesmo prazo. | `frozen; approval-material` |
| `D-CUT-35` | Antes de commit do changeset, atestar permissão do toggle e estabelecer o freeze exclusivo de `D-CUT-37`; após registrar o único trigger/revision permitido, desligar Auto-deploy sem cancelar esse trigger. Falha ou revision extra inicia abort. Em sucesso, reativar somente após 30 min verdes, main/runtime coerentes e zero queued/in-flight. Após main promovida, REC-2B ou REC-3C terminam runtime recovery em <=10 min e entram em `REC-4 source-stabilization`, mantendo Auto-deploy off: registrar divergência, Owner e prazo<=24 h; mergear revert revisado ou seguir novo TODO/aprovação; comprovar main seguro+zero queue antes de reativar. Antes do merge, REC-1/1X convergem sem REC-4 porque source permaneceu igual. Disconnect de source não é fallback implícito. | Remove tanto a janela de segundo deployment quanto o candidato rejeitado como risco latente, sem inventar source drift pré-merge. | `frozen; approval-material; official auto-deploy toggle verified 2026-09-28` |
| `D-CUT-36` | Cada gate planning-side satisfatório registra `reviewRound`, material ref, attestation ref e, quando aplicável, architecture ref exatos do mesmo round. `critique`, assumption coherence e scope drift antigos ficam apenas históricos; status `no_material_findings|findings_integrated` sem binding corrente é não-satisfatório. Ao evoluir material, resetar esses gates a `not_run`; após crítica corrente convergir, rerodar coherence e drift. Se guard genérico retornar go com binding ausente/mismatch, tratar como falso positivo bloqueador e não solicitar aprovação. | Impede evidência histórica de mascarar uma rodada material nova enquanto o guard ainda não codifica o vínculo. | `frozen; approval-material; paced rule candidate tracked` |
| `D-CUT-37` | Antes do changeset staged, estabelecer freeze exclusivo e auditável da source: bloquear todo push/merge exceto o PR de cutover com tree exata revisada, registrar Owner/janela e provar zero deployment Railway queued/in-flight. O freeze permanece até capturar o único trigger/revision permitido e desligar Auto-deploy. Qualquer push/revision/deployment inesperado aborta e entra no conjunto candidato. Never-Active deve ser conclusivamente cancelado/terminal; todo candidato que esteve Active, inclusive o reviewed, obrigatoriamente termina em `Remove -> Removed` antes do zero externo. Quando reviewed Active e controls confiáveis, quiesce fiscal+treatment/drain ocorre primeiro como shutdown gracioso, mas não substitui Remove. Runner prova o conjunto completo de sessões/transactions/fences candidatos zero estável2 s antes de restore/Rollback. | Garante um único candidato esperado, cobre qualquer extra e torna a prova zero2s alcançável ao terminalizar todos os deployments que chegaram a Active. | `frozen; approval-material` |
| `D-CUT-38` | O freeze abrange source **e** control plane Railway do changeset ao fim dos 30 min/REC-4, sob um operador autorizado. O plano separa duas provas: (a) fingerprint runtime contínuo em poll<=1 s de project/environment/service, replicas=`1`, região, source/branch, teardown `0/20`, health path, approvals e conjunto deployment/queue; (b) checkpoint de configuração antes/depois de cada transição irreversível conforme D-CUT-41. Proibir scale, region/config/variables, restart, Redeploy, Deploy Latest, Rollback ou approval fora da state machine. Mudança manual ou platform-initiated deployment/restart, mesmo mesma revision, é candidato inesperado e abort imediato sem first-restart allowance; alteração de réplica/capacidade exige rebaseline, não continuação. | Não atribui ao polling de nomes uma capacidade inexistente de detectar valores e preserva as premissas de uma réplica, C=6, boot único e único candidato. | `frozen; approval-material` |
| `D-CUT-39` | Após qualquer Rollback de REC-3A/3B, entrar em `REC-3C post-rollback-convergence` antes de REC-4: correlacionar ação no prior deployment exato ao Active resultante; provar stored image+variables/revision/identity esperadas; aplicar o probe baseline-specific de D-CUT-40, não a rota candidata inexistente; manter todos os boots/sessions/transactions/fences candidatos zero por janela estável2 s e fingerprints D-CUT-38/41 íntegros. Nova revision/boot/mismatch reinicia recovery; prova ausente ou RTO runtime>10 min é breach fail-closed. | Impede declarar recuperação apenas porque a ação Rollback foi aceita e evita exigir `/prontidao` de uma imagem anterior que não a implementa. | `frozen; approval-material` |
| `D-CUT-40` | Antes do changeset, identificar o prior deployment exato e congelar seu contrato real de recovery sem mutá-lo: confirmar rotas existentes e exigir no mínimo `GET /api/v1/saude` com **corpo** `status=ok,banco=ok` (HTTP 200 isolado não satisfaz), login/`GET /api/v1/auth/eu`, uma consulta legada autenticada read-only e `SELECT 1` pelo runner externo, todos correlacionados ao prior deployment e app role/database. REC-3C repete exatamente esse probe após o Rollback; `/api/v1/prontidao` só é exigida do candidato. Rota/corpo/credencial/runner inconclusivos bloqueiam antes do merge. | Fornece convergência observável compatível com a imagem anterior sem confundir seu health 2xx degradado com readiness. | `frozen; approval-material` |
| `D-CUT-41` | A configuração usa uma sequência auditável sem persistir valores: revisar o changeset exato de dez chaves no painel, registrar somente nomes/escopos, ação, ator, timestamp, commit message/cursor da activity feed e deployment ID; após o commit sem redeploy e antes de merge/abertura/REC-4, exigir zero staged changes e nenhuma mutação de config fora da sequência. Nomes iguais não tornam value-only change invisível: qualquer evento/changeset de variable update inesperado aborta; o runtime candidato prova semântica por startup budgets e probes `/empresa` dos dois contextos. Se activity feed/changeset/ator não forem legíveis ou exclusivos no plano Pro, o cutover para antes da primeira mutação. Valores, hashes de segredos e CNPJ integral nunca são persistidos. | Usa os sinais oficialmente expostos por staged changes/activity feed e validação semântica, sem criar fingerprint secreto fraco nem alegar audit logs Enterprise no plano Pro. | `frozen; approval-material` |
| `D-CUT-42` | A classificação de candidatos nasce na primeira mutação Railway, não no merge. `REC-1` é config-only e só pode restaurar snapshot quando runtime/deployment identity permaneceu continuamente igual, não houve trigger/approval/queued/building/deploying/Active nem possibilidade inconclusiva, e o runner confirma candidatos zero2s. Qualquer evento possível entra `REC-1X pre-merge-unexpected`: inventariar todos; never-Active deve ficar terminal e zero2s antes do restore; qualquer Active usa REC-3B remove-all, zero2s, Rollback prior exato e REC-3C. Como source/main não mudou, REC-1/1X conclui recovery sem REC-4 depois de config trail restaurada; REC-4 é obrigatório apenas se main foi promovida. | Fecha a janela changeset→merge sem restaurar configuração enquanto um candidato inesperado ainda pode executar e evita source stabilization fictícia quando a source permaneceu intacta. | `frozen; approval-material` |

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
| Abort threshold | durante `Active-fiscal-fechada`, allowance local178 s inicia abort até real180 s sob observação/control saudáveis; após deadline, 503/header deixa de ser expected e recovery RTO10 condicionado governa. Gap>2 s/reconnect/ambiguidade e demais falhas abortam/breach imediato. Pós-open: thresholds 429/5xx/p95/RSS congelados | observador pré-merge + fingerprint control-plane + logs/contador/smoke | `frozen; 180s is abort-initiation, not recovery-completion` |
| Atomic staged enable | dez variáveis commitadas sem redeploy; o único rebuild pós-merge consome flag `true` + bindings + budgets | diff redatado do changeset e controle commit-without-redeploy no painel | `required pre-merge; inability blocks cutover` |
| Recovery action | state machine `REC-0/1/1X/2A/2B/3A/3B/3C/4`; classificação começa na primeira mutação. 1 é config-only com runtime imutável; 1X cobre candidato pré-merge; 3A graceful reviewed+remove-all, 3B remove-all; terminal/Removed+zero2s precede restore/Rollback; 3C prova prior runtime. REC-4 só se main mudou | IDs/status/fingerprint, baseline-specific prior probe, runner/fence/gates/Remove/Rollback proof e conditional evidence | `runtime <=10 min condicionado; source <=24 h somente quando main divergiu` |
| External irreversible quiesce | POST fiscal/treatment revalida usuário ativo+ADMIN sem cache antes de qualquer transição; SIGTERM interno usa caminho separado fail-closed | testes de demotion/revocation, corrida opener/quiesce/SIGTERM e auth/DB indisponível | `frozen; 401/403 must leave epoch/state unchanged` |
| Transition observer | iniciar antes do merge; poll Railway+boot/gate <=1 s com deadline <=1 s, gap máximo2 s e allowance local178 s | simulação de late observation, reconnect, observer restart, gaps e restart de boot | `required pre-merge; any gap/ambiguity aborts without timer reset` |
| Source freeze/Auto-deploy stabilization | antes do changeset, permitir apenas o merge da tree revisada e provar zero queued/in-flight; desligar Auto-deploy após o único trigger/revision; manter off em abort até `REC-4`; reativar só com source/runtime coerentes e zero queue | proteção/freeze auditável, permissão/toggle, status/queue, source ref e Owner/deadline <=24 h | `required; unexpected revision aborts; source disconnect is not an implicit fallback` |
| Railway control-plane freeze | operador único; runtime fingerprint contínuo de réplica1/região/source/teardown/health/approvals/deployments; configuração separada por changeset/activity-feed checkpoints e validação semântica | poll runtime<=1 s + zero staged changes/cursor de atividade antes/depois de transições; nenhum valor/hash secreto persistido | `required; value-only/manual/platform change is unexpected; inconclusive config trail blocks before mutation` |
| Prior recovery probe | congelar rotas e respostas que o prior realmente suporta; `/saude` exige corpo ok/ok, mais auth/read legado e SELECT1 externo | read-only preflight do exact prior deployment + correlação role/database | `required before changeset; candidate /prontidao is not imposed on prior` |
| Planning evidence binding | crítica/coerência/drift satisfatórios pertencem ao mesmo round e refs exatas do material/attestation/arquitetura | metadata e dispatch correntes; mudança material reseta para `not_run` | `required; stale or mismatched evidence blocks approval` |
| External `/eventos` consumers | inventariar integrações fora deste repositório e obter attestation do Owner antes do deploy | lista redatada/declaração do Owner | `required pre-deploy; unknown consumer blocks deploy unless hard-cut risk is explicitly reapproved` |
| UptimeRobot auth migration | atestar token public/configured; se configured, migrar current monitor para `x-monitor-token` e limpar URL antes do merge | presença/bound redatados + current-release 200/401/URL proof | `required pre-merge; unknown or query-token consumer blocks cutover` |
| Treatment/readiness envelope | read `4/2 s`, writer `1/2 s/idle0`, control `1/1 s/connect1/socket1/statement200ms`; sampler250/single-flight/deadline1000/snapshot-age500; total `C=6` | healthy inspection overlap + compound inspection-owns-control→DB-drop + public flood1000/c100; handler p95<=100 ms; liveness<=250; zero orphan/P2024 | `frozen; change requires rebaseline` |
| Transitional PostgreSQL budget | três inequalities separadas global/database/role com `L`, `C=6`, runner flags `Xd/Xr`, O* disjuntos e margens por cap | settings/caps, matriz role/database, budgets autoritativos, cap legado e runner/affinity | `required before implementation approval and repeated <=15 min pre-merge; unknown/double-count/snapshot-only blocks` |
| PostgreSQL barrier connectivity | runtime datasource direto ou pooler session-affine; proibir transaction/statement multiplexing e credencial compartilhada | binding/endpoint/mode Railway redatados + teste de sessão/`application_name` em duas conexões; valores nunca impressos | `required before activation; unknown/multiplexed blocks` |
| External rollback runner | identidade/ACL, conexão direta/session-affine e classificador exato comprovados read-only antes do APROVADO e novamente <=15 min antes do merge; runner permanece disponível na janela | probe no mesmo target sem imprimir URL/credencial/UUID; perda pré-merge aborta antes de `REC-2A`; perda pós-merge é RTO breach fail-closed | `required pre-approval/pre-merge; unknown/unavailable blocks` |
| Cross-version writer barrier | session-affine; writer pool1 segura advisory session fence global e cada transaction verifica PID/`pg_locks`; timer/open epoch-CAS; cinco contagens; lease exact-once; pre-switch prior terminal/drained + zeros/fence; pós-switch runner externo exige toda candidata/fence zero | config/pooling + idle-old-boot/session-loss/commit-uncertain/restart harness + Stage evidence | `frozen; mismatch, multiplexing, fence loss, candidate session or unknown blocks` |
| Fiscal read activation | cache visível só com lease atual requestStart+5 s; payload/stream/CAS respeitam identity deadline. Gate fechada tem allowance local178 s para iniciar abort até real180 s sob caminho saudável; recovery visível pode consumir RTO10 condicionado | skew/RTT/restart/render + provider/SSE/demotion/observer/control-plane loss | `frozen; <=35 s auth residual; 180 s detection vs recovery residual requires approval` |

### PostgreSQL Transitional Connection Class Matrix

`Og`, `Od` e `Or` são budgets disjuntos das classes **fora** das três linhas modeladas; nunca incluem legado, candidato ou runner. Cada máximo e associação vem de config/cap autoritativo, não de snapshot. Mudança de role/database invalida a conta e bloqueia até rebaseline.

| Classe modelada | Processos | Role | Database | Máximo | Caps aplicáveis | Inclusão nos budgets O* |
| --- | --- | --- | --- | --- | --- | --- |
| legado UniNotas | deployment anterior | `app_role` igual ao candidato, a provar | `app_db` igual ao candidato, a provar | `L` autoritativo | `G/D/R` | excluído de `Og/Od/Or`; somado explicitamente |
| candidato UniNotas | uma réplica/processo | mesma `app_role` | mesmo `app_db` | `C=6` | `G/D/R` | excluído de `Og/Od/Or`; somado explicitamente |
| runner/inspector | um processo/conexão | role registrada; `Xr=1` se igual à app role, senão `0` | database registrado; `Xd=1` se igual ao app db, senão `0` | `X=1` | sempre `G`; `D` se Xd; `R` se Xr | excluído dos O* aplicáveis; somado por `1/Xd/Xr` |
| demais consumidores | inventário completo | roles registradas | databases registrados | budgets autoritativos | conforme associação | somente aqui: `Og/Od/Or`; classe desconhecida bloqueia |

Inequalities: global `L+C+1+Og+Mg<=G`; database finito `L+C+Xd+Od+Md<=D`; role finita `L+C+Xr+Or+Mr<=R`. `reserved_connections` ausente vale `0`; cap `-1` é ilimitado e sua inequality/margem é `n/a`, nunca zero.

## Diff Expectation Contract

- **Contract status:** `required; round35 material baseline will be frozen by publication; its attestation must not alter this field`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree after candidate checkpoint`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | round34 architecture-binding predecessor `c06c644e80c572d2377952b028f7c6f2e74c1062`; round35 material root será registrado no freeze metadata | `committed_diff`; `31712a0` remains code-origin; attestation-only carrier não é implementação |
| `uninotas-foundation` | `foundation_documentation` | `Gate: Review Baseline Freeze -> Baseline commit` | `committed_diff` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `railway.json` | `M` | readiness + teardown contract `overlapSeconds=0`, `drainingSeconds=20` |
| `MonitorNotes` | `DEPLOY.md` | `M` | fiscal cutover/rollback runbook |
| `MonitorNotes` | `README.md` | `M` | production source ownership after successful cutover |
| `MonitorNotes` | `backend/README.md` | `M` | remover contrato público/local de cinco abas e documentar `/eventos` original-ERRO-only |
| `MonitorNotes` | `backend/src/main.ts` | `M` | alinhar título/descrição global do Swagger à Smart Notas como fonte de sucesso e `logs` somente como erros de integração |
| `MonitorNotes` | `backend/src/health/**` | `A|M` | readiness correction if selected |
| `MonitorNotes` | `backend/src/auth/**` | `M` | tornar TTL de identidade monotônico e provar bound combinado de revogação fiscal/ADMIN sem mudar regra de acesso |
| `MonitorNotes` | `backend/src/common/**` | `M` | propagar correlation ID único até logs/erros |
| `MonitorNotes` | `backend/src/app.module.ts`, `backend/src/operacao/**` | `A|M` | registrar barreiras fiscal/treatment, endpoints ADMIN, boot/quiesce e lifecycle SIGTERM |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M` | bounded probe/capacity/rotation changes |
| `MonitorNotes` | `backend/src/config/**` | `M` | bounded runtime validation |
| `MonitorNotes` | `backend/src/prisma/**` | `M` | clients read/writer/control `4/1/1`, URL writer sem idle expiry, heartbeat, session fence/PID/lock, budget transitório e readiness isolada sem alterar schema |
| `MonitorNotes` | `backend/src/logs/**` | `M` | tornar `/eventos` error-only, serializar tratamentos por ref e testar bloqueio de sucessos/overlap |
| `MonitorNotes` | `backend/src/monitoramento/**` | `M` | remover sucesso da projeção operacional baseada em logs |
| `MonitorNotes` | `backend/src/realtime/**` | `M` | remover polling/LISTEN/JWT em query e manter stream autenticado somente para tratamentos elegíveis/heartbeat |
| `MonitorNotes` | `backend/package.json` | `M` | fixar Prisma/Client exatamente em `6.19.3`; remover `pg` do runtime e mantê-lo apenas como dev tooling de `espelhar.ts`; `@types/pg` permanece dev-only |
| `MonitorNotes` | `backend/package-lock.json` | `M` | alinhar lockfile à versão Prisma exata e à mudança de `pg` para devDependency sem afetar o runtime Prisma |
| `MonitorNotes` | `backend/.env.example` | `M` | approved non-secret production controls |
| `MonitorNotes` | `frontend/src/api/eventos.ts` | `M` | alinhar cliente ao boundary error-only |
| `MonitorNotes` | `frontend/src/api/notas.ts`, `frontend/src/api/cliente.ts` | `M` | adicionar handshake de estado e preservar metadata/header fiscal por abstração compartilhada sem text matching |
| `MonitorNotes` | `frontend/src/api/tipos.ts` | `M` | congelar filtros/DTOs error-only e remover campos de sucesso do resumo |
| `MonitorNotes` | `frontend/src/paginas/ListaEventos.tsx` | `M` | manter exclusivamente a fila Erros |
| `MonitorNotes` | `frontend/src/hooks/useTempoReal.ts` | `M` | substituir EventSource/JWT em query por fetch streaming autenticado e treatment-only |
| `MonitorNotes` | `frontend/src/hooks/useProdutos.ts` | `M` | consumir somente produtos com erro |
| `MonitorNotes` | `frontend/src/hooks/useResumo.ts` | `M` | remover semântica de sucesso do resumo legado |
| `MonitorNotes` | `frontend/src/contextos/NotasFiscaisContexto.tsx`, `frontend/src/notas/cacheFiscal.ts`, `frontend/src/notas/estadoFiscal.ts`, `frontend/src/paginas/ListaNotas.tsx`, `frontend/src/paginas/DetalheNota.tsx` | `M` | owner compartilhado do handshake/lease monotônica per-boot governa visibilidade; enter/focus/resume, heartbeat, render-time expiry e geração impedem stale rows/detail |
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
| `uninotas-foundation` | `artifacts/tmp/uninotas-cutover-pcv/**` | `A|M` | evidência JSON/hash canônica das quatro lanes `pcv-1`; somente conteúdo redatado |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/.env` | `A|M|D|R` | local secrets are not versioned |
| `MonitorNotes` | `frontend/src/notas/**` | `A|D|R` | arquitetura fiscal já validada; somente correção material exige renewed approval |
| `MonitorNotes` | `backend/prisma/schema.prisma`, `backend/prisma/sql/**`, `backend/prisma/migrations/**` | `A|M|D|R` | no schema/data migration; somente o runtime client em `backend/src/prisma/**` pode mudar |
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
| `A-CUT-09` | O deploy respeitará `railway.json` com overlap 0/drain 20; Config as Code segue suportado para o serviço legado na data do corte. | `railway.json`, `DEPLOY.md`, documentação Railway Deployment Teardown/Config as Code; prova remota pendente | writer legado pode sobrepor e o cutover deve abortar | `Medium` | `Promote to Decision` (`D-CUT-24`) |
| `A-CUT-10` | O runtime Railway usa endpoint PostgreSQL direto ou pooler session-affine, a credencial permite observar em `pg_stat_activity` as sessões do mesmo `current_user/current_database` e nenhum cliente não-UniNotas a compartilha. | `backend/src/prisma/prisma.service.ts`, `backend/.env.example`, `railway.json`; attestation redatada de binding/endpoint/pooling/ACL/compartilhamento ainda pendente | transaction/statement multiplexing, visibilidade inconclusiva ou sessão desconhecida tornam a prova por `application_name` inválida e bloqueiam abertura/cutover | `Low` | `Block` |
| `A-CUT-11` | Um runner externo autorizado consulta `pg_stat_activity`/`pg_locks` no target sem API candidata, e o Owner possui ação/permissão Railway `Remove`. | `backend/src/prisma/prisma.service.ts`, `backend/src/health/health.controller.ts`, `DEPLOY.md`, topology; probes/attestation ainda pendentes | REC-3A/3B não possuem prova/ação independente; aprovação de implementação e merge ficam bloqueados | `Low` | `Block` |
| `A-CUT-12` | No Prisma `6.19.3` exato, writer `connection_limit=1,max_idle_connection_lifetime=0` + heartbeat conserva a sessão/PID/fence; qualquer replacement é detectado antes de domínio. | `backend/package.json`, `backend/package-lock.json`, `backend/src/prisma/prisma.service.ts`; manifests resolvem `6.19.3`, mas usam caret e idle default 300 s; `VAL-CUT-21` pendente | fence pode expirar/reentrar e exige rebaseline | `Low` | `Block` |
| `A-CUT-13` | Pool legado, associação role/database, caps global/database/role e budgets disjuntos das demais classes são demonstráveis; as três inequalities de `D-CUT-23` cabem separadamente. | `backend/src/prisma/prisma.service.ts`, `backend/package.json`, `backend/package-lock.json`; legado sem cap e G/D/R/Og/Od/Or remotos pendentes | coexistência pode saturar um cap específico ou contar runner/consumidor duas vezes | `Low` | `Block before approval; separate cap4 TODO if L unprovable` |
| `A-CUT-14` | Ambos os contextos fiscais terão ao menos uma nota autorizada para provar detalhe antes de liberar reads. | `backend/src/fiscal-notes/__tests__/smart-notas-live.probe.spec.ts`, `backend/src/config/configuration.ts`; tokens/bindings preenchidos, probe não executado | contexto vazio mantém a barreira fiscal fechada até decisão operacional explícita | `Low` | `Block` |
| `A-CUT-15` | O frontend consegue tornar cache fiscal invisível até handshake positivo do boot atual, renovar a lease e rejeitar respostas de geração antiga. | `frontend/src/notas/cacheFiscal.ts`, `frontend/src/notas/estadoFiscal.ts`, `frontend/src/paginas/ListaNotas.tsx`, `frontend/src/paginas/DetalheNota.tsx`; comportamento atual preserva último resultado e não possui o handshake | dados do boot anterior podem aparecer antes da prova fiscal ou após restart não observado | `Low` | `Promote to Decision` (`D-CUT-25`) |

## Execution Plan

1. Antes de solicitar autoridade de implementação, executar o preflight read-only `D-CUT-32`: provar `L`, role/database, G/D/R, O*/margens, Xd/Xr, runner/ACL/afinidade e as três inequalities com `C=6`; atestar também permissão do toggle Auto-deploy, viabilidade do freeze exclusivo de source, activity feed/zero-staged de D-CUT-41, observador bounded de D-CUT-34 e prior recovery probe de D-CUT-40. Se qualquer fato for inconclusivo, parar este TODO e abrir o TODO cap4 quando aplicável; nenhuma implementação começa.
2. Confirmar topologia e obter inventário/attestation do Owner sobre consumidores externos de `/eventos`/`logs` e modo atual do UptimeRobot/`MONITORAMENTO_TOKEN`; consumidor ou monitor mode desconhecido bloqueia deploy.
3. Obter `APROVADO`, carregar regras e implementar na branch de trabalho: budgets fail-closed `10 s/4/15/60`, readiness snapshot-only, correlation ID, boundary error-only, barreiras fiscal/tratamento, deadline de autorização `D-CUT-30`, fase operacional `D-CUT-31`, Prisma exato `6.19.3` e runbook.
4. Executar testes focados: BCI 5/10/20; clients `4/1/1`; matriz disjunta/inequalities; sampler/readiness composto; fence/commit; handshake fiscal com cache/skew/RTT/restart/background; delayed-provider cruzando deadline, SSE near-expiry e demotion durante opener; fase Active-fechada/restart/abort; histórico; CSV-LF. Revisar diff e congelar SHA/tree.
5. Sobre essa tree exata, executar CI-equivalent completo e build Docker local, startup/readiness negativo, probes redatados dos dois emissores, lanes `pcv-1`, carga near-limit, performance de lista/detalhe/histórico/payload/monitoramento/eligibility e browser smoke. Não alegar OCI idêntico ao rebuild Railway.
6. Concluir auditorias delivery-side; rebasear somente se `main` mudou e, nesse caso, invalidar/repetir o checkpoint/validação e o preflight de capacidade. Preparar PR cuja tree final prevista seja idêntica à tree validada.
7. Ainda sobre a release corrente, se `MONITORAMENTO_TOKEN` estiver configurado, cadastrar `x-monitor-token` no UptimeRobot, remover token da URL e provar request autorizado 200/503 e request sem header 401; se ausente, atestar modo público. Não rotacionar valor. Falta de acesso/evidência aborta antes do merge.
8. Dentro de 20:00–22:00 e antes do changeset, ativar freeze exclusivo/auditável de source e control plane sob operador único: somente PR/tree revisada; fingerprint runtime replica1/região/source/0-20/health/approvals/deployments; zero queue/in-flight. Congelar o prior probe real. Revisar o changeset de dez variáveis, registrar somente nomes/escopos e cursor/evento da activity feed e commitá-lo sem redeploy. A partir desse instante toda revision/trigger é candidata por D-CUT-42. Exigir zero staged changes depois; feed/cursor/ator/value-change inconclusivo aborta antes do merge sem persistir segredo/hash.
9. Antes de promover `main`, registrar deployment/ID/plano/source/config-event/snapshot/changeset/teardown/logs/Owner/monitor/freeze e repetir D-CUT-32/40/41 <=15 min. Iniciar observador+runtime fingerprint poll<=1 s antes do merge e manter até fim de observation/REC-4; revalidar zero staged changes/activity cursor em cada transição irreversível. Push/revision, scale/config/restart/redeploy/approval/platform deployment inesperado, gap, classe desconhecida ou inequality falha bloqueia REC-2A/aborta e não recebe restart allowance.
10. Promover somente o PR permitido para `main`, verificar tree equivalente e entrar em `REC-2A`. Capturar o único trigger/approval/revision/build permitido; imediatamente após registrá-lo, desligar Auto-deploy sem cancelar esse trigger, mantendo o freeze de source. Falha do toggle ou qualquer segundo trigger/revision inicia abort e classifica todos como candidatos. Quando o único candidato fica ativo, comprovar `overlap=0`, `drain=20`, antigo ID rollbackable e boot/timer. Barreiras fiscal e de tratamento permanecem fechadas; quiesce/SIGTERM invalida callbacks por epoch.
11. Ao primeiro `Active`, iniciar deadline local178 s; sob observador/control path saudáveis, iniciar abort até real180 s. Não prometer conclusão da recuperação nesse prazo. Gap>2 s/reconnect/ambiguidade inicia abort/breach sem reset. Até o deadline, só 503/header exato é expected/contado separado; depois, deixa de ser excluído do incidente e o RTO recovery10 condicionado governa. Verificar rollback target/login/Erros/handshake; ADMIN prova bindings e revalida sem cache antes do CAS.
12. Após abertura, iniciar SLO geral e observação30 com fingerprint contínuo. Geral/detalhe só renderizam sob lease atual; payload/streams respeitam identity deadline. Somente um restart explicitamente esperado/autorizado e presente no fingerprint recebe allowance local178 de detecção; manual/platform/unapproved aborta sem allowance, e segundo restart aborta. Depois de anterior terminal, affinity, orçamento e runner, ADMIN treatment abre com auth fresca. Sucesso só reativa Auto-deploy após 30 min verdes, fingerprint/source/runtime coerentes e zero queue.
13. Em abort, seguir REC-1/1X/2A/2B/3A/3B. Desde a primeira mutação, inventariar reviewed/extras. Pré-merge sem candidato possível usa REC-1; qualquer evento possível usa REC-1X, com never-Active terminal+zero2s ou Active→REC-3B. Pós-merge, REC-2B cobre nenhum Active; REC-3A faz graceful reviewed e remove-all Active; REC-3B remove-all. Após terminal/Removed+zero2s, qualquer Rollback entra REC-3C: correlacionar prior exato ao novo Active, stored image+vars/revision, repetir `/saude` body ok/ok + auth/read legado + SELECT1 do probe congelado, manter fingerprints/config-trail íntegros e candidatos zero2s. Se main não mudou, restaurar config trail e encerrar recovery; se mudou, só então REC-4. Falha ou >10 min é breach; source divergente estabiliza <=24 h.
14. Após janela verde e inventário externo limpo, promover capabilities/policies/módulos/root docs Foundation atomicamente. Consumidor externo descoberto bloqueia promoção/deploy até coordenação ou novo aceite.
15. Não sincronizar novo Foundation commit em `MonitorNotes:main` neste closeout; registrar pin divergente e follow-up do próximo release de produto.

## Public Fiscal Activation API Contract

`GET /api/v1/notas` e `GET /api/v1/notas/:noteId` preservam seus contratos de sucesso, mas consultam a barreira antes do adapter. Enquanto não `aberta`, retornam envelope comum 503, `Retry-After: 1`, `Cache-Control: no-store`, `X-UniNotas-Fiscal-Gate: closed`, erro/mensagem congelados e zero chamada Smart Notas. A abstração compartilhada em `api/cliente.ts` preserva status/headers; `api/notas.ts` expõe o handshake sem raw fetch duplicado. O header invalida imediatamente a lease. Cache fiscal pode permanecer armazenado, porém só é visível com lease do `{bootId,epoch}` atual e deadline monotônico: `requestStart=performance.now()` antes do fetch e deadline máximo `requestStart+5000ms`; resposta após o deadline é descartada e `leaseExpiraEm` nunca estende pelo relógio de parede. Todo render revalida expiry. Enter/focus/resume suprime antes do handshake; heartbeat visível a cada 3 s usa timeout1 s. Falha, expiração, boot/epoch/generation diferente ou resposta antiga mantém supressão e impede repopulação. Outros 503 não usam text matching. No backend, cada request carrega `identityValidUntilMonotonic`; se o provider terminar depois desse limite, identidade ativa é revalidada sem cache antes de qualquer serialização e falha vira 401 sem payload. Risco residual: restart ainda não observado pode expor cache por no máximo 5 s desde o início do último handshake válido e revogação após fill por no máximo35 s.

| Method / path | Frozen request contract | Frozen success contract | Other status / headers |
| --- | --- | --- | --- |
| `GET /notas/estado` | Bearer de qualquer usuário autenticado autorizado a visualizar notas; sem body/query; não consulta Smart Notas nem PostgreSQL | 200 exatamente `{estado:'fechada'|'aberta',bootId,epoch,leaseExpiraEm}`; `bootId` UUID v4 lowercase, `epoch` inteiro >=0; `leaseExpiraEm` ISO no máximo 5 s no futuro quando aberta e null quando fechada | 401 para sessão inválida/inativa; `Cache-Control: no-store`; timeout cliente 1 s; nunca retorna CNPJ/token/noteId/upstream payload |
| `GET /operacao/notas/barreira` | Bearer + `ADMIN`; sem body/query | 200 exatamente `{estado:'fechada'|'validando'|'aberta'|'falha'|'quiescida',bootId,epoch,validadoEm}`; `validadoEm` ISO somente aberta, senão null | 401/403; `Cache-Control: no-store`; nunca retorna CNPJ/token/noteId/upstream payload |
| `POST /operacao/notas/provar-e-abrir` | Bearer + `ADMIN`; query vazia; body exato `{confirmacao:'VALIDAR_E_ABRIR',bootId:UUID v4 lowercase}`; single-flight faz CAS síncrono `fechada|falha -> validando` antes do primeiro await | 200 exatamente `{estado:'aberta',bootId,epoch,validadoEm,contextos:{unifast:'validado',prosperar:'validado'}}`; exige `/empresa`, lista e detalhe autorizados em ambos, bindings esperados, revalidação sem cache de usuário ativo+ADMIN imediatamente antes do CAS final e mesmo owner/epoch | 400 formato; 401/403, inclusive demotion/inatividade durante o probe; opener concorrente/stale/restart 409 `Conflito`; mismatch, upstream, contexto sem amostra de detalhe ou resultado inconclusivo 503 + `Retry-After: 1`, mantendo fechado/falha; `Cache-Control: no-store`; logs somente correlation/actor pseudônimo |
| `POST /operacao/notas/quiescer` | Bearer + `ADMIN`; query vazia; body exato `{confirmacao:'QUIESCER_FISCAL'}`; idempotente e one-way no boot; cada chamada/retry revalida sem cache usuário ativo+ADMIN antes de mudar estado | 200 exatamente `{estado:'quiescida',bootId,epoch}`; após a prova fresca, captura boot/epoch e incrementa/fixa estado por compare-and-transition síncrono sem await intermediário, invalida opener/leases e registra audit pseudônimo | 400 body/query; 401/403 sem alterar estado/epoch; `Cache-Control: no-store`; retry autorizado retorna o mesmo estado; provar-e-abrir posterior 409 até process exit |

## Public Error API Contract

Regras comuns: `/eventos/**` e `/realtime/eventos` exigem `Authorization: Bearer` e o guard global que revalida usuário ativo; ausente/inválido/inativo retorna 401. Cada request recebe o deadline monotônico da identidade; resposta assíncrona cruzando-o revalida antes de serializar, e stream nunca emite após ele. DTO/query inválido ou chave não allowlisted retorna 400. Tratamentos exigem `ADMIN|GESTOR|ANALISTA`; perfil sem permissão retorna 403 e qualquer CAS/commit privilegiado após await revalida role se cruzou o deadline. Ref original `PENDENTE|SUCESSO` falha como 404 indistinguível de inexistente. Todo erro JSON não-stream preserva o envelope exato `{statusCode:number, erro:string, mensagem:string|string[], caminho:string, timestamp:string ISO}`. Em tratamentos, 409 usa `erro='Conflito'` e `mensagem='Tratamento concorrente; atualize e tente novamente.'`; 503 usa `erro='Serviço indisponível'`, `mensagem='Não foi possível confirmar o tratamento; atualize antes de tentar novamente.'` e `Retry-After: 1`. Nos endpoints operacionais, 503 também usa `erro='Serviço indisponível'` e `Retry-After: 1`, com a mensagem específica congelada em cada row. `LogResumoDto`, `LogDetalheDto`, `ClienteDto`, `VendaDto`, `ProdutorDto`, `TentativaDto` e `CampoPendenteDto` preservam os campos atuais; somente eligibility e conteúdo do histórico mudam.

| Method / path | Frozen request contract | Frozen success contract | Other status / headers |
| --- | --- | --- | --- |
| `GET /eventos` | somente `situacao=TODOS|ERRO|TRATADOS` (default `ERRO`), `busca<=120`, `produto<=200`, `pagina` inteiro >=1 (default 1), `limite` inteiro 1..200 (default 25), `direcao=asc|desc` (default `desc`), `dataInicio/dataFim` ISO; `PENDENTE|SUCESSO` inválidos | 200 `{dados,meta}`; cada item mantém exatamente `refId,eventAt,situacao,situacaoOriginal,mensagem,idSmartNotas,clienteNome,clienteDocumento,produto,valorVenda,meioPagamento,tentativas`; meta mantém `total,pagina,limite,totalPaginas,temProxima`; somente erro original | 400 query/chave inválida; 401 auth |
| `GET /eventos/resumo` | aceita somente `busca<=120`, `produto<=200`, `dataInicio/dataFim` ISO; não aceita nem ignora `situacao,pagina,limite,direcao`; sem defaults além de ausência dos filtros | 200 exatamente `{total,erro,tratados}`; `erro` inclui não tratado/reaberto, `tratados` inclui resolvido/ignorado e `total=erro+tratados` | 400/401 |
| `GET /eventos/produtos` | sem body; eligibility antes de group/order | 200 array `{nome,eventos,erros}` com `eventos==erros`, somente produtos com erro original | 401 |
| `GET /eventos/exportar` | aceita somente `situacao=TODOS|ERRO|TRATADOS` (default `ERRO`), `busca<=120`, `produto<=200`, `dataInicio/dataFim` ISO; rejeita `pagina,limite,direcao`; teto interno fixo 20.000 | 200 CSV UTF-8/BOM com colunas exatas `refId;idTransacao;eventAt;situacao;mensagem;idSmartNotas;clienteNome;clienteDocumento;clienteEmail;produto;codProduto;valorVenda;meioPagamento`, somente erro original; antes de quote/escape, cada scalar textual externo iniciado por `=,+,-,@,TAB,CR,LF` recebe prefixo `'` | `Content-Type: text/csv; charset=utf-8`; `Content-Disposition` sanitizado; 400/401 |
| `GET /eventos/:refId` | path decodificado/trimado deve ter 1..64 caracteres; branco/oversize = 400; ref válida deve ser original-`ERRO` | 200 `LogDetalheDto`: campos de `LogResumoDto` mais `orientacao,origem,cliente,venda,produtor,historico,camposPendentes,payload,resposta`; cada tentativa mantém `em,mensagem,ok,autorNome`, mas histórico contém somente linhas originais `ERRO` | 400 input; 401; 404 ref válida inexistente/inelegível |
| `GET /eventos/:refId/payload` | mesmo bound 1..64/trim; ref elegível original-`ERRO` | 200 exatamente `{enviado,resposta}` | 400 input; 401; 404 válida inexistente/inelegível |
| `PATCH /eventos/:refId/tratamento` | mesmo bound 1..64/trim; body exatamente `{situacao: RESOLVIDO|IGNORADO|PENDENTE, observacao?: string<=1000}`; ref elegível; overlap na mesma ref é serializado por `D-CUT-23` | 200 `LogDetalheDto`; `PENDENTE` reabre para situação efetiva `ERRO`; cada comando aceito gera exatamente um append, sem lost update | 400 input/body; 401/403; 404 válida inexistente/inelegível; 409 após conflito comprovadamente abortado/retry único; 503 + `Retry-After: 1` em gate/pool/timeout/commit incerto, seguido de refresh obrigatório |
| `POST /eventos/tratar-lote` | body `{refIds: string[1..500], situacao, observacao?}`; cada ref é trimada, deve ter 1..64 e ser única após trim; branca/oversize/duplicata rejeita todo lote com 400; mesma enum/regra do unitário; locks de refs em ordem lexical binária | 200 exatamente `{solicitados,aplicados,ignorados}`; `solicitados` é tamanho validado/único; `ignorados` ecoa somente refs válidas não aplicadas, sem distinguir inexistente de inelegível; batch é atômico e não perde append em overlap unitário/lote | 400/401/403; 409 após conflito abortado/retry único; 503 + `Retry-After: 1` em gate/pool/timeout/commit incerto, sem retry cliente antes de refresh |
| `GET /operacao/tratamentos/barreira` | Bearer + perfil `ADMIN`; sem body/query; por ser autenticado pode iniciar a janela mínima, mas nunca abre a barreira | 200 exatamente `{estado,bootId,ativos,liberaEm,sessoesCandidatasAtuais,transacoesTratamentoAtuais,sessoesCandidatasNaoAtuais,transacoesTratamentoNaoAtuais,sessoesNaoCandidatas}`; `bootId` é UUID v4 lowercase canônico; `estado=inicializando|aguardando_abertura|aberta|quiescida`; `liberaEm` é ISO enquanto aguarda ou null após expirar/quiescer; todas as cinco contagens são inteiros >=0 | 401/403; em inspeção DB inconclusiva, 503 com `mensagem='Não foi possível comprovar o estado da barreira; mantenha os tratamentos bloqueados.'` + `Retry-After: 1`; `Cache-Control: no-store`; nunca retorna deployment ID, query text, segredo, UUID de outro boot ou usuário |
| `POST /operacao/tratamentos/abrir` | Bearer + perfil `ADMIN`; query vazia; body exato `{confirmacao:'ABRIR',bootId:UUID v4 lowercase canônico,deploymentAnteriorId:string 1..128,implantacaoAnteriorTerminal:true,postgresSessionAffineConfirmado:true}`; operador só confirma após observar terminal/removido, datasource e runner direto/session-affine | 200 exatamente `{estado:'aberta',bootId,ativos:0,liberaEm:null,sessoesCandidatasAtuais,transacoesTratamentoAtuais:0,sessoesCandidatasNaoAtuais:0,transacoesTratamentoNaoAtuais:0,sessoesNaoCandidatas:0}`; `sessoesCandidatasAtuais` inclui base/writer/control >=0; após 30 s, mesmo boot/epoch/state, fence global adquirido/validado por PID, demais contagens zero e revalidação sem cache de usuário ativo+ADMIN imediatamente antes do CAS final; registra audit redatado sem PID/key | 400 formato/body/query; 401/403, inclusive demotion/inatividade durante awaits; stale/quiesced sempre 409 com `erro='Conflito'`, `mensagem='Barreira de tratamento ainda não pode ser aberta.'`, sem `Retry-After`, mesmo se DB falhou; somente captura atual retorna essa 409 por contagem/fence ocupado ou 503 DB/identidade/unlock inconclusivo com `mensagem='Não foi possível comprovar o estado da barreira; mantenha os tratamentos bloqueados.'` + `Retry-After: 1`; `Cache-Control: no-store`; não existe auto-open |
| `POST /operacao/tratamentos/quiescer` | Bearer + perfil `ADMIN`; body exato `{confirmacao:'QUIESCER'}` e query vazia; idempotente no mesmo boot e one-way até process exit; cada chamada/retry revalida sem cache usuário ativo+ADMIN antes da transição | 200 exatamente `{estado:'quiescida',bootId,ativos,liberaEm:null,sessoesCandidatasAtuais,transacoesTratamentoAtuais,sessoesCandidatasNaoAtuais,transacoesTratamentoNaoAtuais,sessoesNaoCandidatas}`; após prova fresca, captura boot/epoch e fixa estado/incrementa epoch por compare-and-transition síncrono sem await intermediário; todas as contagens são inteiros >=0; sucesso exige lease/transaction drenadas e unlock do fence pelo mesmo PID; registra audit pseudônimo | 400 confirmação/body/query; 401/403 sem alterar estado/epoch; se inspeção/unlock for inconclusivo após quiesce autorizado, estado permanece quiescido e retorna 503 com `mensagem='Barreira quiescida, mas não foi possível comprovar a drenagem; consulte novamente.'` + `Retry-After: 1`; retry autorizado é idempotente e rollback/sucessor seguem bloqueados até prova dos zeros/fence; `Cache-Control: no-store`; não existe resume |
| `GET /monitoramento/erros` | `MONITORAMENTO_TOKEN`, se configurado, deve ter 1..200 ou startup falha; aceita somente header `x-monitor-token` 1..200, oversize/branco = 400; query `token` inválida; `minutos` inteiro 1..1440 default 60, `atencao` >=1 default 1, `critico` >=1 default 6, `alertarEm=atencao|critico`; demais chaves rejeitadas | 200 exatamente `{status,cor,erros,pendentes,sucessos,total,ultima_verificacao,janela:{inicio,fim,minutos},limites:{atencao,critico},detalhe}`; `erros=total` conta ativos/reabertos, tratados não contam, `pendentes=0`, `sucessos=0` | `Cache-Control: no-store`; 400 input; 401 token ausente/incorreto quando configurado; 503 banco indisponível ou severidade >= `alertarEm`, mesmo shape |
| `GET /realtime/eventos` | header Bearer obrigatório; nenhum token/query; consumidor usa `fetch` streaming e reconecta após término normal | 200 `text/event-stream`; apenas `evento.tratado` com `refId,situacao,origem='api',em` e `heartbeat` com `origem='sistema',em`; servidor encerra em `min(30 s, remainingIdentityValidity)` e não emite no/após deadline; sem polling/NOTIFY/`evento.novo` | 401 ausente/inválido/inativo a cada conexão/reconnect; cancelar em logout/unmount; `Cache-Control: no-store`; nenhum JWT em URL/log |

## Recovery State Machine

| State | Trigger / truth | Required recovery | Evidence and maximum RTO |
| --- | --- | --- | --- |
| `REC-0 no-remote-mutation` | qualquer estado de código/checkpoint, publicado ou não, enquanto nenhuma configuração Railway foi commitada | nenhuma recuperação Railway; reverter somente diff/commit do TODO conforme autoridade Git e manter Stage intocado | refs/status/diff classificados; `5 min` |
| `REC-1 staged-config-only` | changeset de dez chaves foi commitado sem redeploy, `main` não foi promovida **e** há prova contínua de que runtime/deployment identity não mudou e nenhum trigger/approval/revision queued/building/deploying/Active foi possível | runner prova candidatos/sessions/transactions/fences zero2s; só então restaurar snapshot redatado anterior via novo staged commit sem redeploy; confirmar deployment corrente inalterada e sequência activity-feed/zero staged sem evento inesperado. Qualquer possibilidade inconclusiva migra a REC-1X | nomes/escopo/ações/cursor antes/depois + zero2s + zero staged + mesmo deployment ID; `10 min`; encerra recovery sem REC-4 porque main não mudou |
| `REC-1X pre-merge-unexpected-deployment` | desde a primeira mutação e antes do merge existe trigger/approval/revision inesperado ou sua ausência não é conclusiva | congelar source/config e inventariar todo candidato. Never-Active deve ser impedido/cancelado/terminal; se nenhum esteve Active, runner full-set zero2s precede restore do snapshot e encerra sem REC-4. Se qualquer um esteve Active, usar REC-3B remove-all→Removed, full-set zero2s, Rollback prior exato e REC-3C; depois restaurar/confirmar config trail e encerrar sem REC-4. Runtime/config/source inconclusivos são breach | eventos/states/ações + runner zero2s + prior probe/REC-3C quando Active + config trail restaurada; `10 min`; main permanece igual |
| `REC-2A post-merge-not-safe` | começa imediatamente após promover o único PR permitido, inclusive sem deployment visível, trigger atrasado/rejeitado, awaiting approval, queued/building/deploying ou revision extra | manter freeze exclusivo; após trigger/revision permitido, desligar Auto-deploy; bloquear restore; impedir/rejeitar todos os triggers ou abortar deployments in-flight serialmente; observar até prova do estado de cada candidato. Qualquer revision extra aborta. Se nenhum esteve Active, ir REC-2B; se reviewed esteve Active e seus controls/auth são confiáveis, ir REC-3A; em qualquer outro conjunto contendo Active, inclusive extra-only Active, ir REC-3B | main SHA/tree + conjunto de revisions/states/ações/toggle; decisão 5 min; sem prova, breach/reassessment |
| `REC-2B candidate-conclusively-prevented` | o trigger revisado e todo extra foram conclusivamente rejeitados/impedidos sem deployment possível, ou todos os deployments ficaram terminais cancelados/falhos e nenhum esteve Active | inventariar separadamente reviewed/extras; runner externo prova o conjunto completo de sessões/transactions/fences candidatos zero estável2 s. Somente então restaurar snapshot anterior por staged commit sem redeploy, comprovar a sequência activity-feed/zero staged e a mesma deployment verde ativa; não usar `Rollback`; manter Auto-deploy off e seguir `REC-4` | prova de cada trigger impedido/status terminal never-Active + runner zeros2s + current deployment ID antes/depois + config trail redatada restaurada; runtime dentro do RTO total `10 min` |
| `REC-3A reviewed-active/control-available` | reviewed esteve Active e APIs ADMIN respondem; extras podem ter estado Active | separar reviewed/extras; quiesce fiscal+treatment/drain do reviewed; `Remove -> Removed` de reviewed+todo extra Active; never-Active terminal. Após full-set sessions/transactions/fences zero2s, executar Rollback no prior ID e entrar obrigatoriamente `REC-3C`; não declarar runtime recuperado aqui | IDs/revisions/boots/gates + todos Active Removed + zeros2s + Rollback action; runtime objetivo10 inclui 3C |
| `REC-3B active-remove-only` | existe Active, mas reviewed não esteve Active ou controls/auth não são confiáveis | terminalizar never-Active; Remove de todo Active; todos Removed; runner full-set zero2s; executar Rollback no prior ID e entrar obrigatoriamente REC-3C. Nova revision/boot reinicia; inconclusivo é breach | action/permission + extra-only/multi-candidate evidence + zeros2s + Rollback action; runtime objetivo10 inclui 3C |
| `REC-3C post-rollback-convergence` | Rollback de REC-3A/3B foi aceito | correlacionar prior deployment exato ao Active resultante; provar stored image+variables/revision selecionados; repetir o probe D-CUT-40 (`/saude` corpo ok/ok, auth/read legado e SELECT1 externo), sem exigir `/prontidao`; exigir runtime fingerprint, config trail e todos os candidatos/transactions/fences zero estável2 s. Nova revision/boot/mismatch reinicia recovery. Após tudo verde, seguir REC-4 somente se main mudou; senão restaurar/confirmar config trail e encerrar REC-1X. Ausência de prova ou total >10 min é breach fail-closed | deployment/action correlation + redacted config/image identity + baseline-specific probes + runner/fingerprint/config trail stable2s; <=10 min total |
| `REC-4 source-stabilization` | runtime legado verde foi restaurado **após main ter sido promovida**, mas `main` ainda contém candidato rejeitado e Auto-deploy está off | registrar divergência, Owner e prazo <=24 h; mergear revert revisado que restaura a tree verde ou abrir novo TODO/aprovação para candidato corrigido. Confirmar main segura, runtime coerente e zero queued/in-flight antes de reativar Auto-deploy; source disconnect não é fallback implícito. REC-1/1X nunca entram aqui porque main não mudou | refs/tree, toggle/queue e decisão do Owner; runtime RTO já encerrado, source estabilizada <=24 h |

Transições não pulam evidência: desde a primeira mutação, REC-1 exige nenhum candidato possível; dúvida/evento pré-merge usa REC-1X. REC-2B exige nenhum Active; REC-3A exige reviewed Active+controls confiáveis e graceful-before-remove; todo outro conjunto Active usa REC-3B. Todo Active Removed e never-Active terminal precedem full-set zero2s. REC-3A/3B sempre passam por REC-3C. REC-1/1X convergidos encerram sem REC-4; após merge, somente REC-2B ou REC-3C convergido entram REC-4. Nova revision/boot/PID reinicia. Runtime >10 min é breach; source stabilization tem prazo separado24 h somente quando main divergiu.

## Health, Readiness and Rollback Contract

- Healthcheck Railway não substitui probe externo nem monitoramento contínuo.
- Health não deve chamar Smart Notas a cada probe: indisponibilidade transitória não deve causar restart storm.
- Criar readiness em `/api/v1/prontidao`; Railway passa a usar essa rota. O handler público não toca PostgreSQL nem aguarda pool: lê snapshot atômico monotônico do sampler interno e responde 2xx apenas quando `success` tem idade <=500 ms; ausência/failure/stale responde 503/no-store. `/api/v1/saude` permanece liveness simples.
- O sampler roda em fixed-window 250 ms, single-flight sem overlap; usa control pool1 (`pool/connect/socket=1 s`, `statement=200 ms`) com uma statement, sem transaction/`pg_sleep`/wait e deadline end-to-end 1000 ms. Inspeção iniciada 1 ms antes deve expirar em até 200 ms; com DB saudável, snapshots seguem fresh, readiness faz 60/60 2xx p95 handler<=100 ms e zero P2024.
- No caso composto, inspeção adquire control, PostgreSQL cai e o sampler tenta 1 ms depois. O último positivo expira em <=500 ms; depois 60/60 readiness são 503 p95<=100 ms, liveness 2xx<=250 ms e não resta query/sessão órfã 2 s após recovery. Flood público 1.000 requests/concurrency100 não aumenta statements além da cadência, não cria waiters DB, não causa P2024 e memória recupera para baseline+10% em 5 s; atraso do event loop expira snapshot fail-closed.
- Binding token/CNPJ é comprovado pela barreira fiscal ADMIN no runtime implantado antes de qualquer read fiscal; health/readiness nunca carregam conteúdo sensível nem chamam Smart Notas.
- O recovery probe do prior é congelado read-only antes do changeset contra o deployment exato. Como a imagem anterior não possui `/prontidao`, REC-3C exige `/api/v1/saude` com corpo `status=ok,banco=ok`, login/`auth/eu`, uma consulta legada autenticada e `SELECT 1` no runner; HTTP 200 isolado nunca satisfaz.
- Pré-merge: atestar plano Pro, deployment ID corrente, prior probe, snapshot redatado de configuração/nomes de variáveis, zero staged changes, cursor/eventos esperados da activity feed, acesso do Owner, capacidade geral de rollback, permissão do toggle Auto-deploy e observador contínuo pronto; não alegar elegibilidade futura do alvo exato. Abort após a primeira mutação usa REC-1 somente com runtime comprovadamente imutável; qualquer evento/dúvida usa REC-1X.
- Pós-merge/pré-active: operador observa/cancela serialmente (`REC-2A`); config só restaura após todos never-Active terminal/impedidos e full-set zero2s (`REC-2B`). Se houver Active: reviewed Active+controls confiáveis usa 3A gracioso-then-remove; extra-only Active ou controls não confiáveis usa 3B remove-only.
- Pós-switch/pre-smoke amplo: assim que a nova deployment estiver ativa, confirmar que o ID antigo agora aparece como previous deployment com `Rollback` visível; a retenção Pro de `120 h` passa a governar a imagem removida/substituída.
- Capacidade: `C=6` é teto do candidato. Antes de aprovação de implementação e novamente <=15 min antes do merge, provar separadamente global `L+C+1+Og+Mg<=G`, database finito `L+C+Xd+Od+Md<=D`, role finita `L+C+Xr+Or+Mr<=R`; O* exclui participantes, `reserved_connections` ausente=0 e -1=n.a. Classe/role/database/budget ou `L` desconhecido bloqueia este TODO antes do código; cap4 exige outro TODO e rebaseline completo. Control devolve conexão após cada statement.
- Teardown: `railway.json` fixa overlap zero/drain 20; leituras fiscais nascem fechadas por boot. O primeiro tráfego autenticado agenda espera mínima de 30 s para treatments, mas a barrier só abre por POST ADMIN após anterior terminal/removido, runner/control session-affine, fence global adquirido uma única vez no writer pool1 e zeros aplicáveis. Health/readiness usa control isolado.
- Ativação fiscal: observador+fingerprint já ativos consultam em <=1 s/deadline1. Allowance local178 inicia abort até real180 sob caminho saudável; não limita conclusão do recovery. Após deadline, 503/header deixa de ser expected e RTO10 condicionado governa. Gap/control loss é breach. Restart só recebe allowance se explicitamente esperado/autorizado no fingerprint; qualquer platform/manual/unapproved aborta sem allowance.
- Config as Code está deprecado, mas a Railway documenta suporte aos serviços legados até `2026-12-01`; este cutover exige prova remota dos valores e abre follow-up de migração IaC antes dessa data, sem ampliar a janela atual.
- Rollback primário: runner/Remove/Auto-deploy preflighted. REC-3A graceful reviewed e depois todo Active Removed; REC-3B remove todos Active, inclusive extra pré-merge. Após zero2s, Rollback sempre entra REC-3C e só runtime prior exato Active com stored image+vars/revision, probe D-CUT-40, fingerprints/config trail e candidatos zero2s encerra recovery; REC-4 segue apenas quando main foi promovida. Objetivo runtime10 condicionado; source<=24 h quando aplicável.
- Fallback degradado: `Redeploy` reconstrói a deployment a partir do source/config original e não preserva identidade de bits; só pode ser usado após bloqueio/renovação explícita do risco e do RTO.
- Kill switch: `SMART_NOTAS_READ_ENABLED=false`; corta o provedor, mas não restaura integralmente a nova tela `Geral`.
- Fontes verificadas: [Railway Staged Changes](https://docs.railway.com/deployments/staged-changes), [Deployment Actions](https://docs.railway.com/deployments/deployment-actions), [Using Variables](https://docs.railway.com/variables), [Deployment Teardown](https://docs.railway.com/deployments/deployment-teardown), [Services](https://docs.railway.com/services), [Service CLI](https://docs.railway.com/cli/service), [Auto-deploy toggle](https://railway.com/changelog/2026-05-01-undoable-deletes), [Config as Code reference](https://docs.railway.com/config-as-code/reference), [image retention by plan](https://docs.railway.com/pricing/plans), [Prisma PostgreSQL connector](https://docs.prisma.io/docs/orm/v6/overview/databases/postgresql) e [PostgreSQL application_name](https://www.postgresql.org/docs/18/runtime-config-logging.html).

## Abort Conditions

- Mismatch token/CNPJ em qualquer contexto.
- Segredo, CNPJ integral, recurso upstream, URL assinada ou identificador sensível em saída não autorizada.
- Falha de startup/readiness/browser; falha de lista/detalhe, exceto 503/header fiscal exato antes do deadline local178. Depois do deadline ele é incidente e não fica excluído do recovery/SLO.
- Leitura fiscal chama Smart Notas antes da barreira aberta, barreira abre sem os dois contextos/detalhes, ou restart preserva estado fiscal aberto.
- Handshake fiscal ausente/fechado/falho/timeout/expirado ainda permite render, resposta de geração antiga repopula cache, header503 não invalida a lease, ou exposição stale após restart não observado ultrapassa 5 s.
- Deadline local178 expira sem abertura e abort não é iniciado até real180 sob caminho saudável; observador/fingerprint late/gap>2/reconnect/ambíguo; 503 segue expected após deadline; assinatura/contador incorreto; restart não aprovado recebe allowance ou reinicia relógio.
- Resposta fiscal serializa payload após `identityValidUntilMonotonic` sem revalidação ativa, SSE emite no/após deadline ou dura mais que `min(30 s, remainingIdentityValidity)`, opener ADMIN conclui CAS final sem revalidação não-cacheada imediatamente anterior, ou quiesce HTTP fiscal/treatment altera estado/epoch antes de revalidar sem cache usuário ativo+ADMIN.
- Fallback para `logs`, sucesso vazio mascarando erro, mistura ou acesso cross-context.
- `>=2` respostas 429 consecutivas ou `>=1%` de 429 em 5 minutos.
- Após a abertura fiscal, `>=5%` de 5xx/timeout em 5 minutos com ao menos 20 requisições, ou p95 `>8 s` durante 5 minutos; 503/header de gate contabilizado durante a fase fechada nunca entra silenciosamente neste denominador.
- RSS `>=80%` do limite Railway ou crescimento `>20%` sem recuperar em 10 minutos; qualquer saturação que impeça smoke também aborta.
- Sink ausente/inacessível ou retenção abaixo da política.
- Pré-merge sem plano/ID/snapshot/acesso, runner, observador/fingerprint, operador único, prior probe ou permissões; control-plane diverge; activity feed/cursor/zero-staged inconclusivo; value-only/config event inesperado; trigger/toggle falha; restore antes de terminal+zeros; Active sem Removed; 3A/3B incorreto; Rollback sem REC-3C ou REC-3C sem prior exact image+vars, `/saude` body ok/ok, auth/read legado, SELECT1 e candidate-zero; atomicidade falha; runtime>10 min; REC-4 sem Owner/prazo24 h.
- Freeze exclusivo ausente antes do changeset, push/merge diferente da tree revisada permitido, deployment queued/in-flight prévio, segundo trigger/revision não classificado como candidato, ou restore/Rollback antes de impedir/remover todos os candidatos e provar sessões/transactions/fences zero.
- Teardown diferente de `0/20`; opener reentrante/depth !=1; Prisma/idle/heartbeat divergente; multiplexing/runner; abertura sem fence/zeros; treatment sem lease; pools !=4/1/1; control fora dos limites 1 s/1 s/1 s/200 ms ou retido em transaction/wait; matriz/orçamento sem G/D/R/Og/Od/Or/Xd/Xr ou qualquer inequality separada falha; readiness 2xx com DB real down; ou rollback sem gates/runner/polling.

## Definition of Done

- [ ] `DOD-CUT-01` Novo checkpoint final contendo budgets/readiness/correlation/error-only/runbook é identificado, publicável e reproduzível antes do CI/build definitivo.
- [x] `DOD-CUT-02` Alvo Railway e responsáveis são registrados redatados e confirmados pelo usuário.
- [ ] `DOD-CUT-03` Os dois pares fiscais são validados contra a empresa esperada sem exposição de segredo/CNPJ.
- [ ] `DOD-CUT-04` Timeout, rate, concorrência e bytes/memória são calibrados para a topologia real sob carga near-limit.
- [ ] `DOD-CUT-05` Logs têm sink, retenção, acesso e redaction comprovados.
- [ ] `DOD-CUT-06` A tree candidata passa localmente em build, readiness, probes, API/browser smoke e `/erros`; essa evidência não é tratada como OCI Railway idêntico.
- [ ] `DOD-CUT-07` REC-0/1/1X/2A/2B/3A/3B/3C/4 separa reviewed/extras desde a primeira mutação. 1 é config-only; 1X terminaliza pre-merge unexpected; 2B never-Active terminal+zero2s; 3A graceful reviewed+remove-all; 3B remove-all. Após Rollback, 3C prova prior runtime. RTO runtime10 condicionado; REC-4/source<=24 h só se main mudou.
- [ ] `DOD-CUT-08` Abertura fiscal ocorre antes da allowance local178; se não, abort inicia até real180 sob caminho saudável e recuperação pode consumir RTO10 condicionado. Após abertura, Stage passa ambos contextos por 30 min com fingerprint íntegro.
- [ ] `DOD-CUT-09` Teste local determinístico com chaves efêmeras prova que rotação HMAC invalida ID antigo e relistagem produz IDs válidos; nenhuma rotação HMAC ocorre no `Stage` deste TODO.
- [ ] `DOD-CUT-10` Um predicado SQL canônico de classificação original `ERRO` é aplicado antes de count/group/order/limit/paginação e mutations em lista, resumo, produtos, exportação, detalhe, payload, histórico correlacionado, tratamento unitário/lote e monitoramento; defesa TypeScript não substitui query-side filtering; tratamento `PENDENTE` sobre erro original permanece elegível; o contrato público congelado em `D-CUT-17..19`, `backend/README.md`, decorators OpenAPI e a descrição Swagger global em `backend/src/main.ts` estão coerentes.
- [ ] `DOD-CUT-11` Railway readiness lê somente snapshot sampler250/single-flight/deadline1000: success age<=500 dá 2xx, ausente/failure/stale 503. Healthy overlap mantém 60/60 2xx p95 handler<=100 ms/zero P2024. Composto control-held→DB-drop expira positivo<=500 ms, depois 60/60 503; liveness<=250 ms e orphan-zero2s. Flood1000/c100 não cria DB waiters/statements além da cadência e memória recupera baseline+10%/5 s.
- [ ] `DOD-CUT-12` Request, aplicação, upstream e filtro de erro reutilizam o mesmo correlation ID; logs retêm por 30 dias somente metadados redatados/`actorId` pseudônimo com acesso restrito.
- [ ] `DOD-CUT-13` Candidate e final main possuem tree OID idêntico; revision/build remoto fica ligado ao final main e seus bits passam readiness/smoke Stage, sem alegar digest idêntico ao build local.
- [ ] `DOD-CUT-14` Promoção Foundation independente é concluída sem novo commit/deploy em `MonitorNotes:main`; gitlink divergente e follow-up do próximo product release ficam registrados.
- [ ] `DOD-CUT-15` Um changeset Railway de dez variáveis inclui flag `true`, cinco valores sensíveis/bindings e quatro budgets; é revisado e commitado sem redeploy da deployment antiga, e o único rebuild pós-merge comprova que consumiu esse estado.
- [ ] `DOD-CUT-16` Realtime não abre `LISTEN`, polling ou timer de varredura; stream usa `fetch` + Bearer/global guard, termina em `min(30 s, remainingIdentityValidity)` e não emite no/após deadline. Frontend reconecta/cancela e usa janelas fixas de 250 ms: lote síncrono 500 gera um par e fluxo contínuo nunca estende a janela nem causa starvation/paralelismo duplicado.
- [ ] `DOD-CUT-17` Queries críticas error-only de lista, resumo, produtos, export, detalhe com histórico de alta cardinalidade, payload, monitoramento e eligibility de mutation possuem planos `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)` redatados e p95 SQL/endpoint separados sobre fixture determinística de 20.000 linhas, sem schema/índice, e passam thresholds congelados.
- [ ] `DOD-CUT-18` Lista, resumo, produtos, exportação, detalhe, payload, tratamentos, monitoramento e SSE respeitam métodos, allowlists, defaults, bounds 1..64/1..200, campos, envelope, códigos, headers e negações; frontend types/README não expõem contratos removidos.
- [ ] `DOD-CUT-19` Modo atual de `MONITORAMENTO_TOKEN`/UptimeRobot é atestado; se configurado, consumidor usa header e URL está limpa antes do merge, provado contra a release corrente; nenhuma rotação/11ª chave ocorre.
- [ ] `DOD-CUT-20` Todo campo textual externo do CSV neutraliza inícios `=,+,-,@,TAB,CR,LF` antes do escaping, com testes coluna a coluna; Prisma Client/CLI estão fixos exatamente em `6.19.3`; runtime realtime não importa `pg`, enquanto `pg`/`@types/pg` permanecem somente dev tooling.
- [ ] `DOD-CUT-21` Clients candidatos `4/1/1`; control usa `pool/connect/socket=1 s`, `statement=200 ms`, exatamente uma statement e nenhuma transaction/`pg_sleep`/wait assíncrona. A matriz disjunta comprova `L/C/runner/O*` e, separadamente, `L+C+1+Og+Mg<=G`, `L+C+Xd+Od+Md<=D` e `L+C+Xr+Or+Mr<=R` quando os caps forem finitos; classe/role/database/budget desconhecido bloqueia. BCI satisfaz os SLOs de `DOD-CUT-11`, reads <=3 s, zero P2024/fence gap. Lease/commit-incertain/atomicidade e JSON `pcv-1` permanecem obrigatórios.
- [ ] `DOD-CUT-22` `railway.json` congela `0/20`; opener usa single-flight/owner/epoch, profundidade advisory `1`, cleanup/unlock idempotente e tests open/open↔quiesce/SIGTERM. Writer `6.19.3` usa `max_idle_connection_lifetime=0`, heartbeat <=30 s e teste idle >300 s; policies server-side são atestadas. Transactions validam PID/lock, loss quiesce sem auto-reacquire; lease é sync/exact-once. Rollback exige zeros/fence e runner externo; probes de loss/restart/commit incerto provam ambos os resultados legítimos. IaC antes de `2026-12-01`.
- [ ] `DOD-CUT-23` Barreira fiscal nasce fechada; lista/detalhe retornam 503/no-store/header e zero provider. `GET /notas/estado` é in-memory/no-store para viewer autenticado. Cliente usa deadline monotônico máximo `requestStart+5 s`, descarta resposta tardia, revalida em todo render e nunca estende por `leaseExpiraEm`/clock skew/timer atrasado. Enter/focus/resume suprime; heartbeat3/timeout1 renova; falha, expiração, boot/epoch/generation divergente ou header suprime e não repopula. `api/cliente.ts` preserva metadata sem text matching e `api/notas.ts` centraliza handshake. POST ADMIN prova ambos contextos. Residual aceito <=5 s desde request start.
- [ ] `DOD-CUT-24` Quiesce fiscal ADMIN é one-way/idempotente, revalida sem cache usuário ativo+ADMIN antes da transição síncrona sem await intermediário, invalida lease/opener e separa SIGTERM interno antes de treatment shutdown; 401/403 não mudam epoch e 409 impede reopen no boot. REC-3A/3B comprovam fechamento e REC-3C comprova convergência pós-Rollback; o frontend comprova invalidação.
- [ ] `DOD-CUT-25` Cache de identidade usa relógio monotônico 30 s; desativação logo após cache fill e última lease provam supressão <=35 s. 401 invalida lease; mudança de perfil entre setores não revoga visualização, por decisão de acesso universal.
- [ ] `DOD-CUT-26` `L` não autoritativo bloqueia este TODO e roteia cap4 a TODO próprio; após eventual promoção, nenhuma evidência/tree/baseline deste cutover é reutilizada sem refreeze/CI/reviews.
- [ ] `DOD-CUT-27` Readiness possui sampler/snapshot e admissão pública descritos em D-CUT-29, sem query por request nem crescimento de fila DB.
- [ ] `DOD-CUT-28` Deadline de identidade acompanha toda operação: payload sensível pós-deadline exige revalidação sem cache, SSE fecha no remaining deadline e nenhum evento posterior sai; opener ADMIN revalida antes do CAS final e treatment cruzando deadline revalida dentro da transaction antes do write/commit. Desativação/demotion durante provider/stream/open/mutation falha sem emissão/transição indevida.
- [ ] `DOD-CUT-29` Fase fechada possui local178 para iniciar abort até real180 sob caminho saudável, não recovery bound. 503/header só é expected até deadline; depois é incidente. Gap/control loss é breach; restart só recebe allowance se autorizado no fingerprint.
- [ ] `DOD-CUT-30` Preflight redatado de capacidade/afinidade completa D-CUT-32 antes de autoridade de implementação e é repetido <=15 min antes do merge; inconclusivo roteia ao TODO cap4 sem código neste TODO.
- [ ] `DOD-CUT-31` Quiesce HTTP fiscal/treatment revalida sem cache usuário ativo+ADMIN em toda chamada/retry e só então faz CAS síncrono; revocation/demotion retorna 401/403 sem mutação. SIGTERM interno permanece fail-closed e independente de auth/DB.
- [ ] `DOD-CUT-32` Observador inicia pré-merge, mantém poll/deadline <=1 s e gap <=2 s, usa allowance local178 s e aborta sem reset em late start, gap, reconnect/restart ou identidade ambígua, inclusive no restart pós-open.
- [ ] `DOD-CUT-33` Freeze exclusivo inicia antes do changeset; Auto-deploy é desligado após o único trigger/revision permitido, permanece off em rollback e só reativa após 30 min verdes ou REC-4 concluído, source/runtime coerentes e zero queue. Main rejeitada é estabilizada em <=24 h por revert revisado ou novo TODO/aprovação.
- [ ] `DOD-CUT-34` Gates planning-side satisfatórios registram round e refs exatas correntes; mudança material reseta crítica/coerência/drift para `not_run`, e stale/mismatch bloqueia mesmo se guard genérico retornar go.
- [ ] `DOD-CUT-35` Changeset só é commitado após freeze exclusivo e zero queued/in-flight. Revision inesperada aborta; never-Active termina impedida/cancelada e todo Active, inclusive reviewed, atinge Removed. Só full-set zero2s permite restore/Rollback; extra-only Active possui ramo 3B explícito.
- [ ] `DOD-CUT-36` Freeze control-plane contínuo sob operador único preserva fingerprint runtime de replica1/região/source/0-20/health/approvals/deployments até fim; qualquer mudança manual/platform vira candidato inesperado/abort sem restart allowance. Configuração segue DOD-CUT-38.
- [ ] `DOD-CUT-37` REC-3C comum correlaciona exact prior Rollback ao Active resultante e prova image+variables/revision, probe D-CUT-40, fingerprints/config trail e candidatos zero2s antes de REC-4; ausência ou runtime>10 min é breach.
- [ ] `DOD-CUT-38` Freeze de configuração registra o changeset de dez chaves e activity-feed sequence sem valores/hashes, exige zero staged changes em toda transição irreversível e detecta evento value-only mesmo com nomes/escopos iguais; ausência/inconclusão bloqueia antes da mutação.
- [ ] `DOD-CUT-39` Prior recovery probe é congelado read-only no deployment exato e REC-3C repete `/saude` body ok/ok, login/`auth/eu`, read legado e SELECT1 externo; `/prontidao` só é requisito do candidato.
- [ ] `DOD-CUT-40` Desde o changeset, REC-1 só restaura config com runtime identity contínua, nenhum candidato possível e zero2s. REC-1X terminaliza never-Active ou remove todo Active, exige zero2s e REC-3C após Rollback; fecha sem REC-4 quando main não mudou.

## Validation Steps

- [ ] `VAL-CUT-01` Executar pelo runtime canônico compatível `"/mnt/c/Program Files/Git/bin/bash.exe" -lc 'cd /c/unifast/monitordenotas && bash delphi-ai/verify_context.sh'` e exigir `PACED-Ready`. A falha CRLF do wrapper no bash WSL não é falha do projeto; `bash delphi-ai/tools/verify_context.sh` pode ser usado apenas como diagnóstico, não como evidência substituta.
- [ ] `VAL-CUT-02` Depois de toda implementação, congelar o novo SHA e reexecutar suites CI-equivalent backend, frontend e Foundation exatamente nele.
- [ ] `VAL-CUT-03` Construir imagem raiz e provar startup/health com flag desligada; com flag ativa, ausência de qualquer segredo/binding ou budget `10 s/4/15/60` deve falhar fechada; o live probe deve usar exatamente `10 s/4/15/60`, não `30 s/2/30/120`.
- [ ] `VAL-CUT-04` Executar `SMART_NOTAS_PROBE_ENABLED=true` somente em runner autorizado, com saída redatada, nos dois contextos.
- [ ] `VAL-CUT-05` Executar carga near-2MiB no candidato local com budgets `10 s/4/15/60` e registrar p95/p99, 429/5xx/timeout, RSS/heap e recuperação; confirmar métricas Railway antes do corte.
- [ ] `VAL-CUT-06` Executar smoke autenticado dos GETs e jornada browser `Geral -> detalhe -> Erros -> Geral` nos dois contextos.
- [ ] `VAL-CUT-07` Inspecionar logs/respostas por padrão sensível sem registrar os valores pesquisados.
- [ ] `VAL-CUT-08` Antes do merge, ensaio local de `REC-0/1/1X/2A/2B/3A/3B/3C/4`, incluindo record/trigger/cancel→active, controls/auth unavailable, fiscal quiesce, Remove→Removed, restart race, zeros/fence, Rollback→prior Active convergido, Auto-deploy off e estabilização pós-switch; nenhuma ação Railway destrutiva é executada. Remotamente, coletar fatos read-only e atestar no painel permissão/disponibilidade `Remove`/toggle, runner direto/session-affine repetido <=15 min. Falha aborta antes de REC-2A.
- [ ] `VAL-CUT-09` Executar `cutover_integrity_audit`, testes SQL e fixtures inelegíveis: count/páginas corretos, só `ERRO`, histórico filtrado e reabertura elegível; validar allowlists/defaults, ref path/lote whitespace/1/64/65/duplicata pós-trim, token config/header 0/1/200/201, 400 versus 404, envelope/DTO/header exatos e docs/OpenAPI sem contratos removidos.
- [ ] `VAL-CUT-10` Rodar guards Delphi de autoridade, diff, CI, revisão, completion e Foundation conforme a fase.
- [ ] `VAL-CUT-11` Fake clock + PostgreSQL controlado: sampler fixed250/single-flight/deadline1000/snapshot atomic. Healthy inspection+1ms mantém snapshot fresh e 60/60 2xx p95 handler<=100ms. Composto inspection-held→DB-drop faz último success expirar<=500ms e então 60/60 503; liveness<=250/orphan-zero2s. Flood público1000/c100 mantém statements na cadência, zero P2024/waiter DB e RSS volta baseline+10%/5s.
- [ ] `VAL-CUT-12` Correlacionar um request sintético em controller/request context, service, adapter/upstream e exception filter com um único ID; revisar logs por PII/payload/segredo sem persistir os valores pesquisados.
- [ ] `VAL-CUT-13` Comparar `candidate^{tree}` com `final-main^{tree}`, registrar SHAs/tree, build local como evidência separada, revision/build Railway e smoke dos bits remotos; tree mismatch ou smoke remoto falho aborta.
- [ ] `VAL-CUT-14` Provar que o Dockerfile não consome a Foundation, registrar `Foundation main@sha` versus root gitlink pin e abrir follow-up para sincronização no próximo release sem mutar `MonitorNotes:main` agora.
- [ ] `VAL-CUT-15` Capturar o changeset staged de dez chaves por nomes/redaction, provar commit sem redeploy da deployment antiga e correlacionar a única revision pós-merge com flag `true` e budgets aprovados.
- [ ] `VAL-CUT-16` Provar ausência de conexão `pg`/polling/`evento.novo`; fetch Bearer testa 401, término em `min(30 s, remainingIdentityValidity)`, zero evento no/após deadline, reconnect com nova autenticação, nenhuma credential em URL/log, treatment/heartbeat/cancel. Fake timers: 500 eventos síncronos geram exatamente um par após 250 ms; 50 eventos a cada 100 ms por 5 s geram um par por janela fixa não vazia, nenhum evento estende a janela, primeiro refetch de cada janela inicia <=250 ms salvo request anterior em voo, no máximo uma próxima janela fica pendente e não há requests duplicadas paralelas/starvation.
- [ ] `VAL-CUT-17` Gerar com seed versionada exatamente 20.000 logs (80% originais `PENDENTE/SUCESSO`, 20% `ERRO`; entre erros, 25% tratados e casos reabertos), incluindo uma ref elegível com 200 linhas de histórico correlacionado; registrar PostgreSQL/config/estatísticas. Workloads isolados e nesta ordem: lista `ERRO`, lista `TRATADOS`, resumo, produtos, export `TODOS`, detalhe da ref com 200 históricos, payload da mesma ref, monitoramento default 60 min e SELECT equivalente à eligibility da mutation dentro de transaction sempre revertida. O harness SQL usa filtros equivalentes sem inventar query keys. Para cada workload: 5 warm-ups, um `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)` redatado e 30 SQL sequenciais; depois processo endpoint reiniciado, 5 warm-ups + 50 requests concorrência 4 para todo GET não-export, e 20 requests concorrência 1 para export. Eligibility de mutation é somente SQL/rollback, nunca benchmark destrutivo HTTP. Calcular nearest-rank por série. Bloquear filtro tardio/scan correlacionado por linha; lista/resumo/produtos/detalhe/payload/monitoramento/eligibility >`3 s`, export >`8 s`. Falha exige TODO schema/índice e nova aprovação.
- [ ] `VAL-CUT-18` Antes do changeset/merge, inspecionar apenas presença/bound do `MONITORAMENTO_TOKEN` sem valor; se presente, provar UptimeRobot com `x-monitor-token`, URL sem query credential, current release 200/503 com header e 401 sem ele; se ausente, provar modo público. Desconhecido bloqueia corte; não rotacionar.
- [ ] `VAL-CUT-19` Para cada coluna textual externa do CSV, testar valores iniciados individualmente por `=`, `+`, `-`, `@`, TAB, CR e LF; output contém prefixo `'` dentro do valor escapado, preserva BOM/headers e não altera números seguros.
- [ ] `VAL-CUT-20` Executar PATCH/lotes `5x2/10x3/20x5`, lote500 e dois commit-incertain com Prisma6.19.3/clients4-1-1. Validar control pool/connect/socket1, statement200, uma statement, sem transaction/wait; sampler e readiness seguem `VAL-CUT-11`. Teste transitório registra role/database de legado/candidato/runner, Xd/Xr, G/D/R, O* disjuntos, margens e cada inequality. `L`/classe/cap desconhecido, P2024 ou fence gap reprova e não autoriza preparatória neste TODO. Gerar JSON BCI.
- [ ] `VAL-CUT-21` Em processos independentes, provar UUID/names, session affinity e negativo multiplex. Confirmar manifests/lock/runtime em `6.19.3`; writer URL redatada contém semanticamente `max_idle_connection_lifetime=0`. Boot A abre uma vez, heartbeat <=30 s e teste real idle >300 s mantêm mesmo PID/fence; policies PostgreSQL/proxy de idle são registradas redatadas. Open/open simultâneo aceita um owner e chama `pg_try_advisory_lock` uma vez; open/open↔quiesce e open/open↔SIGTERM terminam sem lock residual/unlock excedente. Derrubar a sessão encerra lock/transaction antes de B adquirir; A não reacquire e falha antes de domínio. Intercalar timer/open↔quiesce/SIGTERM/DB success/failure para stale409. Classificador/five counts, lease exact-once, cleanup owner-only, headers/no-store e reads verdes são obrigatórios.
- [ ] `VAL-CUT-22` Se abort real alcançar REC-3A/3B/3C: registrar remove/zeros, Rollback prior exato e 3C com image+vars/revision Active, probe D-CUT-40, fingerprints/config trail e candidatos zero2s. Se não ocorrer, `n/a — state not reached`; nunca autoriza drill remoto.
- [ ] `VAL-CUT-23` Preencher caches nos dois contextos e provar enter/focus/resume suprimindo antes de `GET /notas/estado`, inclusive cache fresco. Capturar `requestStart` monotônico, testar clock de parede ±, RTT quase1 s, resposta de boot antigo atrasada cruzando restart, deadline já exaurido e timer/background atrasado; todo render após `requestStart+5 s` deve ocultar mesmo sem callback. Provar heartbeat3/timeout1, header invalidando metadata, geração/stale Promise sem repopular e abstração `api/cliente.ts` preservando header sem text matching. Provar zero adapter fechado, POST negatives e novo 200 pós-lease sem dados sensíveis.
- [ ] `VAL-CUT-24` Provar quiesce fiscal simultâneo com opener/heartbeat/SIGTERM: após auth fresca epoch muda sync, stale opener409, estado público fechado, frontend invalida, zero provider; retry autorizado idempotente e reopen409. Simular REC-3A e REC-3B auth/API-unreachable: Remove→Removed, restart race, runner zeros estáveis2 s e Rollback somente depois; nenhuma ação remota em teste.
- [ ] `VAL-CUT-25` Com relógio monotônico fake, preencher identidade ativa, desativar imediatamente e solicitar estado a cada3 s: último 200 pode ocorrer antes de30 s, mas render fica oculto até35 s do fill; primeira revalidação retorna401 e invalida. Token expiry também invalida; perfil entre setores preserva viewer; ADMIN demotion perde operação após cache bound.
- [ ] `VAL-CUT-26` Guard estrutural falha se Execution Plan autorizar cap4 dentro deste TODO ou reutilizar SHA/tree/evidência após TODO preparatório; caminho permitido termina bloqueado com referência a novo TODO e exige rebaseline integral.
- [ ] `VAL-CUT-27` Verificar por instrumentação que `/prontidao` não chama Prisma, aguarda Promise ou cria fila; somente sampler toca control, no máximo uma execução, e stale snapshot falha 503/no-store.
- [ ] `VAL-CUT-28` Com fake monotonic clock, cache fill e desativação imediata: segurar provider até depois do identity deadline e provar revalidação sem cache/401/zero serialization; iniciar SSE próximo do deadline e provar lifetime restante/zero evento posterior; demover/desativar durante opener e treatment pausados, provando revalidação não-cacheada antes do CAS ou dentro da transaction antes do write/commit, sem transição. Identidade ainda ativa pode revalidar e concluir com novo deadline auditável.
- [ ] `VAL-CUT-29` Simular Active: 503/header expected só até local178; provar abort signal até real180 sob observer/control saudável, mas Remove/Rollback pode terminar depois sob RTO10. Após deadline, 503 entra no incidente. Simular observer/control loss, Remove latency e restart boundary sem alegar recovery180.
- [ ] `VAL-CUT-30` Antes de `todo_authority_guard.py --pre-approval`, coletar evidência redatada/autoritativa de L, role/database, G/D/R, O*/margens, Xd/Xr, runner/ACL/affinity e três inequalities com C=6. Guard estrutural exige esta evidência anterior a implementação; snapshot-only/inconclusivo termina este TODO no ramo cap4. Repetir <=15 min pre-merge e comparar fingerprint dos fatos.
- [ ] `VAL-CUT-31` Preencher cache ADMIN, desativar/demover e chamar ambos os quiesces, inclusive retry: exigir 401/403 e estado/epoch invariantes. Com identidade ativa, intercalar opener/mutation/quiesce e provar auth fresca seguida de CAS síncrono sem await; SIGTERM fecha ambos mesmo com auth/DB indisponível.
- [ ] `VAL-CUT-32` Observador pré-merge poll/deadline1 gap2 local178: demonstrar abort initiation<=real180 apenas com caminho saudável. Late/gap/reconnect/ambíguo sinaliza breach; control loss/Remove latency demonstram que recovery é separado. Restart não aprovado nunca recebe allowance.
- [ ] `VAL-CUT-33` Atestar read-only a disponibilidade/permissão do toggle e do freeze exclusivo pré-changeset. Em state-machine local, provar freeze+zero queue→changeset→único merge/trigger→Auto-deploy off; green30/source-runtime coerentes/zero queue→on; abort sem Active converge por REC-2B ou, após Rollback, somente por REC-3C, então runtime <=10 min→REC-4 off; push posterior enquanto off não dispara; revert revisado ou novo TODO estabiliza main em <=24 h e só então reativa. Nenhum drill remoto destrutivo.
- [ ] `VAL-CUT-34` Guard estrutural exige `reviewRound` e refs exatas do material/attestation/architecture correntes para crítica/coerência/drift. Evoluir material deve resetá-los para `not_run`; evidência histórica ou mismatch reprova ainda que guard genérico indique go.
- [ ] `VAL-CUT-35` Simular concorrência e quatro conjuntos: reviewed never-Active sem extra; reviewed Active; reviewed Active+extras Active; reviewed never-Active+extras Active com controls alcançáveis. Provar freeze/zero queue, classificação completa, REC-2B somente no primeiro, REC-3A somente quando reviewed Active+controls confiáveis e REC-3B no extra-only/control-fail. Após todo Active Remove→Removed, readiness sampler/clients cessam e runner atinge full-set zero2s antes de restore/Rollback.
- [ ] `VAL-CUT-36` Simular/pollar fingerprint contínuo e operador único; alterar replica, região, variable-name set, teardown, health, approval, manual restart/redeploy e platform deployment. Cada mudança aborta/classifica candidato sem allowance; replica !=1 invalida C=6 e exige rebaseline.
- [ ] `VAL-CUT-37` State-machine local REC-3C: Rollback aceito mas wrong image/vars/revision, prior probe falho, candidate reappears, config trail ou fingerprint muda não entra REC-4. Só exact green+baseline-specific probes+zero2s converge; timeout total>10 min registra breach.
- [ ] `VAL-CUT-38` State-machine/config harness injeta atualização value-only com mesmo nome/escopo, staged change pendente, commit sem redeploy por ator inesperado e activity cursor ausente. Cada caso bloqueia/aborta; somente a sequência de dez chaves, zero staged e eventos esperados avança. Nenhum valor/hash de segredo entra no artifact.
- [ ] `VAL-CUT-39` Antes da implementação, executar probe read-only do exact prior: confirmar ausência/presença real de `/prontidao`, exigir `/saude` body ok/ok, login+`auth/eu`, uma consulta legada autenticada e SELECT1/role/database externos. No harness REC-3C, prior sem `/prontidao` converge com esse contrato; HTTP 200 com `banco=indisponivel`, auth/read/SELECT1 falho ou deployment mismatch não converge.
- [ ] `VAL-CUT-40` State-machine local cobre quatro intervalos changeset→merge: nenhum evento permite REC-1 só após zero2s; queued/building never-Active deve ficar terminal+zero2s antes do restore; extra-only Active exige REC-3B Remove→Removed+zero2s+Rollback+REC-3C; estado/evento inconclusivo é breach. Nos quatro casos main fica igual e REC-4 é proibido.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-CUT-01` | Definition of Done | checkpoint final | git/build | novo `branch@sha` após implementação + build verde | local/CI | `planned` | `31712a0` é baseline inicial, não artefato final |
| `DOD-CUT-03` | Definition of Done | binding emissores | runtime/security | POST ADMIN fiscal redatado | deployed Stage runtime | `planned` | ambos os contextos antes de qualquer read fiscal |
| `DOD-CUT-04` | Definition of Done | capacidade | load | relatório RLS near-limit | local candidate build + Railway metrics | `planned` | budgets iniciais congelados |
| `DOD-CUT-05` | Definition of Done | auditoria | runtime/review | política + consulta redatada | Railway | `planned` | 30 dias confirmados; provar acesso/redaction |
| `DOD-CUT-06` | Definition of Done | smoke pré-cutover | runtime/browser | API + browser evidence | local candidate tree/build | `planned` | source-level; não prova OCI Railway |
| `DOD-CUT-07` | Definition of Done | recovery state machine | runtime/manual | local REC simulation + read-only runner preflight pré-merge + fence/zeros + conditional real-abort evidence in `VAL-CUT-22` | local/Railway Stage | `planned` | sem destructive drill; 10 min condicionado ao preflight; perda pós-merge é breach |
| `DOD-CUT-08` | Definition of Done | cutover | runtime/browser | smoke + observação 30 min | Railway Stage customer-facing | `planned` | corte direto na janela aprovada |
| `DOD-CUT-09` | Definition of Done | HMAC | test | relistagem após rotação com chaves efêmeras | local candidate build | `planned` | Stage rotation fora de escopo |
| `DOD-CUT-10` | Definition of Done | SQL error-only + promoção | tests/doc/validator/manual | predicate before count/group/order/limit/mutations + correlated-history/pagination negatives + external-consumer attestation | local + Owner + Foundation | `planned` | TS mirror secondary; docs/OpenAPI aligned |
| `DOD-CUT-11` | Definition of Done | readiness/runbook | test/doc/runtime | sampler250/deadline1000/snapshot500 + healthy/compound/flood1000 + liveness250/orphan-zero2s | local/Railway | `planned` | handler não toca DB |
| `DOD-CUT-12` | Definition of Done | correlação/privacy | test/log review | request ID end-to-end + redaction evidence | local/Railway | `planned` | actor interno, sem e-mail/nome |
| `DOD-CUT-13` | Definition of Done | source/deployed identity | git/build/runtime | candidate/main tree OID + local build record + Railway revision/smoke | local/GitHub/Railway | `planned` | SHA pode diferir; tree não; OCI pode diferir |
| `DOD-CUT-14` | Definition of Done | Foundation/gitlink topology | doc/git | canonical Foundation SHA + stale-pin record + follow-up | Foundation/MonitorNotes | `planned` | nenhum segundo deploy documental |
| `DOD-CUT-15` | Definition of Done | atomic staged enable | runtime/manual | redacted ten-key changeset + no-redeploy commit + final revision config | Railway Stage | `planned` | flag true faz parte do mesmo corte |
| `DOD-CUT-16` | Definition of Done | realtime auth/boundary | test/security/race | fetch Bearer + fixed-window sustained stream + no query JWT/poll/LISTEN | local backend/browser | `planned` | usuário inativo 401; sem starvation/refetch storm |
| `DOD-CUT-17` | Definition of Done | query performance | explain/load | fixture 20k + histórico200 + planos/p95 de toda query family | local PostgreSQL | `planned` | detalhe/payload/monitor/eligibility incluídos; schema/index fora |
| `DOD-CUT-18` | Definition of Done | public HTTP contract | contract/browser | métodos/campos/status/headers/negações exatos | local backend/frontend | `planned` | frontend types e OpenAPI coerentes |
| `DOD-CUT-19` | Definition of Done | monitor consumer migration | ops/security | mode attestation + header-only current-release probe | UptimeRobot/current Stage | `planned` | sem token value/rotation |
| `DOD-CUT-20` | Definition of Done | CSV/dependency/version hardening | test/security/manifest | adversarial incl. LF + runtime import scan + exact Prisma manifest/lock | local backend | `planned` | Prisma 6.19.3; `pg` somente dev tooling |
| `DOD-CUT-21` | Definition of Done | tratamento/capacidade | concurrency/domain | control 1s/1s/1s/200ms + matriz role/database + inequalities G/D/R + BCI/readiness + JSON/hash | local PostgreSQL/backend | `planned` | C=6; O* disjunto; classes/caps unknown block |
| `DOD-CUT-22` | Definition of Done | cross-version writer barrier | deployment/concurrency/security | owner/single-flight/depth1 + idle>300/heartbeat + PID/locks + runner | local multi-process + Railway Stage | `planned` | no reentry/idle expiry/auto-reacquire |
| `DOD-CUT-23` | Definition of Done | fiscal read barrier/cache | contract/security/runtime | monotonic requestStart+5s + skew/RTT/background/render expiry + metadata header + restart/stale generation + ADMIN CAS | local + Railway Stage | `planned` | cache visível só com lease atual; residual contado do request start |
| `DOD-CUT-24` | Definition of Done | fiscal shutdown/recovery | contract/ops/concurrency | quiesce sync/SIGTERM + REC-3A + Remove/REC-3B simulation/conditional evidence | local + Railway Stage | `planned` | unreachable control has executable branch |
| `DOD-CUT-25` | Definition of Done | identity revocation bound | security/race | monotonic identity30 + lease5 + deactivate/cache-fill composition | local backend/frontend | `planned` | <=35 s accepted residual |
| `DOD-CUT-26` | Definition of Done | preparatory release isolation | governance/git | structural guard + separate TODO/rebaseline requirement | Foundation/Git | `planned` | unknown L hard-stops this TODO |
| `DOD-CUT-27` | Definition of Done | public readiness admission | performance/runtime | no-DB handler + atomic snapshot/single-flight/flood evidence | local backend | `planned` | bounded DB work and fail-closed stale |
| `DOD-CUT-28` | Definition of Done | authorization completion bound | security/race | delayed-provider + near-expiry SSE + demotion-during-open | local backend/frontend | `planned` | no emission/CAS after deadline without fresh proof |
| `DOD-CUT-29` | Definition of Done | bounded fiscal abort initiation | ops/runtime | fake-clock local178/real180 abort-signal + separate recovery latency | local + Railway Stage | `planned` | no hard recovery180 claim |
| `DOD-CUT-30` | Definition of Done | pre-implementation capacity fork | runtime/governance | redacted authoritative preflight + repeat fingerprint | PostgreSQL/Railway/Foundation | `planned` | required before APROVADO and <=15 min pre-merge |
| `DOD-CUT-31` | Definition of Done | external quiesce fresh authorization | security/race | revoke/demote + opener/quiesce/SIGTERM harness | local backend | `planned` | 401/403 cannot mutate; internal shutdown remains fail-closed |
| `DOD-CUT-32` | Definition of Done | bounded transition observer | ops/runtime | pre-merge observer/gap/reconnect/restart simulation | local + Railway Stage | `planned` | poll/deadline1, gap2, allowance178 |
| `DOD-CUT-33` | Definition of Done | auto-deploy/source stabilization | ops/recovery | toggle/queue/source state-machine + conditional runtime evidence | local + Railway Stage/GitHub | `planned` | runtime10 separate from source24h |
| `DOD-CUT-34` | Definition of Done | current-round gate binding | governance | exact-ref structural validator | Foundation | `planned` | stale evidence blocks false-positive go |
| `DOD-CUT-35` | Definition of Done | exclusive source freeze | ops/recovery | protected-source + zero-queue + multi-candidate state-machine | GitHub/Railway/local | `planned` | required before staged changeset |
| `DOD-CUT-36` | Definition of Done | Railway control-plane freeze | ops/runtime | continuous redacted fingerprint + operator/action audit | Railway Stage | `planned` | replica1 and settings preserved continuously |
| `DOD-CUT-37` | Definition of Done | post-Rollback convergence | ops/recovery | REC-3C exact prior runtime + baseline-specific probes + candidates-zero | Railway Stage | `planned` | required before REC-4; no candidate-only route imposed on prior |
| `DOD-CUT-38` | Definition of Done | configuration mutation freeze | ops/security | ten-key sequence + activity cursor + zero staged + value-only negative | Railway Stage/local harness | `planned` | no secret values or hashes persisted |
| `DOD-CUT-39` | Definition of Done | prior recovery probe | ops/recovery | prior `/saude` body + auth/read + external SELECT1 | current Railway Stage/local harness | `planned` | read-only before changeset and repeated only on real REC-3C |
| `DOD-CUT-40` | Definition of Done | pre-merge unexpected deployment recovery | ops/recovery | REC-1/1X candidate classification + terminal/remove/zero/REC-3C harness | local state machine + conditional Railway Stage | `planned` | starts at first mutation; REC-4 forbidden while main unchanged |
| `VAL-CUT-01..40` | Validation Steps | validações | mixed | preencher cada evidência durante execução | mixed | `planned` | `VAL-CUT-22` é condicional ao REC-3A/3B/3C real, nunca drill |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas API | fonte/binding | `unknown` | `2026-09-27 local config only` | probe não executado neste cutover | bloquear ativação |
| Railway control plane | deploy/vars/logs/rollback | `degraded` | `2026-09-27` | target/scale/operator confirmados; sem CLI autenticada | revalidar revision/config imediatamente antes da mutação |
| Railway `Stage` | smoke/cutover customer-facing | `healthy` | `2026-09-27` | `/api/v1/saude` HTTP 200 + project-owner confirmation | cutover direto somente após gates e aprovação final |
| PostgreSQL Railway | auth, erros, pools e writer fence | `degraded` | `2026-09-27` | health público prova alcance, não L/caps/session affinity/ACL/locks | preflight direto read-only obrigatório antes de APROVADO e repetido pre-merge |
| External rollback runner | classificador/fence fora da API candidata | `unknown` | `not yet verified` | probe read-only no mesmo target pendente | indisponível bloqueia aprovação de implementação, changeset/merge e `REC-2A` |

## Profile Scope & Handoffs

- **Primary execution profile:** `operational-devops`
- **Active technical scope:** `railway,docker,nestjs,react,vite,prisma,postgresql,cross-stack`
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
| Cross-version writer barrier | `D-CUT-24` | Railway teardown, treatment mutations and rollback | impede writer legado sem lock concorrer com candidato ou rollback |
| Fiscal read barrier | `D-CUT-25` | `/notas`, adapter Smart Notas e endpoints ADMIN | impede qualquer dado fiscal antes de validar ambos os bindings no boot implantado |
| Fiscal stale-cache suppression | `D-CUT-25` | response header, cache/state, lista e detalhe React | impede que dado de boot anterior sobreviva à barreira fechada |
| System-wide connection budget | `D-CUT-23` | legado + candidato + runner + PostgreSQL settings | impede confundir teto por processo com headroom transitório real |
| Fresh authorization before external quiesce | `D-CUT-33` | endpoints ADMIN fiscal/treatment e recovery | impede ADMIN revogado de causar indisponibilidade irreversível |
| Bounded transition observation | `D-CUT-34` | Active/restart e fase fiscal fechada | inicia abort até real180 sob caminho saudável sem confundir com recovery RTO |
| Auto-deploy freeze and source stabilization | `D-CUT-35` | trigger, sucesso e rollback Railway/GitHub | impede redeploy latente de candidato rejeitado após runtime restore |
| Current-round evidence binding | `D-CUT-36` | reviews/gates planning-side | impede aprovação com evidência histórica de material diferente |
| Railway control-plane freeze | `D-CUT-38` | replica/region/config/actions/deployments | preserva uma réplica e detecta candidatos sem source push |
| Post-Rollback convergence | `D-CUT-39` | REC-3C antes de REC-4 | prova runtime verde exato e candidatos ausentes após ação Rollback |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why Forbidden | Exception Policy |
| --- | --- | --- | --- |
| Fallback de sucesso para `logs` | `/notas` ou Geral consultando Prisma/logs após falha Smart Notas | mascara indisponibilidade e cria duas verdades | `none` |
| Deploy de frontend/backend separados | commits/imagens diferentes no mesmo cutover | quebra compatibilidade da rota Geral | `none` |
| Flag-only tratada como rollback completo | nova UI permanece publicada com fiscal off | Geral fica indisponível | somente kill switch temporário enquanto a deployment anterior recebe `Rollback` |
| `Redeploy` confundido com `Rollback` | ação escolhida inicia novo build | perde identidade de bits e pode romper RTO com base/apt mutáveis | fallback degradado exige risco/RTO renovados |
| Probe/health expondo ou chamando segredo em loop | valores fiscais em output ou Smart Notas chamada por todo healthcheck | vazamento/restart storm | `none` |
| Escala sem budget agregado | `replicas × concurrency/rate` acima do aprovado | multiplica quota/memória silenciosamente | exige nova calibração e aprovação |
| Abrir treatments por relógio/health | estado muda para aberta ao expirar 30 s sem prova de deployment/sessões | drain temporal não prova que writer legado terminou | `none`; abertura ADMIN e prova positiva são obrigatórias |
| Opener assíncrono sem epoch compare-and-transition | quiesce/SIGTERM ocorre enquanto `/abrir` espera DB e resposta tardia muda para aberta | reverte fechamento one-way durante rollback | `none`; captura e CAS síncrono final obrigatórios |
| Timer sem epoch compare-and-transition | callback 30 s muda quiescida para aguardando após quiesce/SIGTERM | reabre caminho de ativação e viola one-way | `none`; cancelamento é secundário, CAS obrigatório |
| Boot/application name livre ou truncável | identidade não UUID, >63 bytes ou `current_setting` diverge | mistura sessões de boots/processos e invalida prova DB | `none`; startup/transaction falham fechado |
| Prova `pg_stat_activity` sobre pooler multiplexado | endpoint transaction/statement pooling reutiliza/reescreve sessões | zero por application name não representa processos clientes | `none`; direto/session-affine ou mecanismo alternativo aprovado |
| Rollback para writer legado sem quiesce contínuo | boot/status ausente, ativos/transações >0, espera +2 s ou polling/re-quiesce omitidos | restart candidato pode aceitar append enquanto legado retorna | `none`; bloquear recovery para reassessment |
| Contagem agregada de sessões legadas/candidatas | conexão do legado e sessão candidata coexistem pós-switch | o total legítimo do legado mascara writer candidato ainda vivo | `none`; cinco classes separadas e probe externo obrigatório |
| Lease retida ou solta antes do settle Prisma | conexão cai e commit permanece incerto/server-side ativo | deadlock local ou rollback autorizado por contador local enganoso | release idempotente exact-once no settle; contagens DB continuam cercando rollback |
| Snapshot de sessões tratado como fence | boot aberto fica ocioso/zero sessões e volta a conectar depois da inspeção | dois boots podem escrever apesar do snapshot limpo | writer pool1 mantém advisory session fence; toda transaction valida PID/lock e nunca auto-reacquire |
| Advisory lock reentrante por openers concorrentes | duas chamadas `/abrir` alcançam `pg_try_advisory_lock` na mesma sessão | profundidade fica invisível em `pg_locks` e um unlock não libera o fence | single-flight síncrono + owner token; exatamente uma aquisição e cleanup owner-only |
| Expiração idle ignorada no fence | writer Prisma usa 300 s implícitos ou proxy/server encerra sessão ociosa | lock pode desaparecer sem nova mutation | Prisma 6.19.3 exato, idle lifetime 0, heartbeat no máximo a cada 30 s e teste por mais de 300 s |
| Gate mutation tratado como reserva de read capacity | duas mutations ocupam pool compartilhado e reads/readiness disputam o restante | P2024/readiness flapping sob quarta operação | clients físicos read4/writer1/control1 + mixed-load thresholds; nenhuma alegação de reserva implícita |
| Teto candidato tratado como teto global | `C=6` ignora legado concorrente e runner | transição satura PostgreSQL apesar do steady-state verde | provar três inequalities; sem `L` autoritativo, hard stop + TODO cap4 próprio + rebaseline |
| Capacidade mistura classes/caps | cálculo único residual ou O* inclui runner/legado/candidato | dupla contagem ou `rolconnlimit`/`datconnlimit` rejeita antes do global | matriz disjunta role/database, Xd/Xr e inequalities separadas; classe desconhecida bloqueia |
| Readiness pública disputa control | request público chama DB ou aguarda pool; inspeção+drop atrasa sampler | flood causa P2024/falso health ou memória/fila | handler snapshot-only; sampler250/single-flight/deadline1000; age500 fail-closed; flood1000/c100 |
| Cache fiscal stale durante gate | deadline usa relógio de parede/response time, cache fresco evita request ou stale Promise repopula | skew/RTT/background estende exposição do boot anterior | monotonic requestStart+5s, render-time expiry, suprimir enter/focus/resume, geração/boot/epoch/header; testar skew/RTT/restart |
| Runner/Remove descoberto somente após merge | ACL/afinidade/ação faltam quando REC-3A/B começa | control API caída deixa rollback sem caminho | runner read-only + permissão/ação Remove preflight; 3B Removed+zero2s antes de Rollback |
| Quiesce HTTP confiando no cache de identidade | ADMIN revogado ainda muda epoch/estado irreversível | cache de 30 s vira janela de indisponibilidade não autorizada | prova sem cache antes do CAS; SIGTERM interno separado |
| Detection budget tratado como recovery bound | observer inicia abort em180 s mas Remove/Rollback demora | promessa falsa de recuperação customer-facing | declarar abort-initiation180 e recovery RTO10 condicionado |
| Rollback com Auto-deploy ativo e main rejeitada | runtime volta verde mas próximo push/redeploy relança candidato | restauração aparente deixa risco latente | desligar após trigger e usar REC-4 antes de reativar |
| Gate histórico satisfazendo round atual | status verde sem refs exatas do material corrente | plano materialmente novo escapa de nova revisão | binding round/ref obrigatório e reset para `not_run` |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan |
| --- | --- | --- | --- | --- | --- |
| structural/test | backend fiscal boundary | existing fiscal module/contract/structure specs | Prisma/logs fallback, public credential input, context leak | `already-enforced` | rerun obrigatório em `VAL-CUT-02` |
| structural/test | integration-error SQL boundary | SQL-shape + high-ineligible-ratio pagination tests across logs/monitoring | filtro pós-query, total/página falsa ou read/mutation `SUCESSO` escapando | `implement-in-this-todo` | `VAL-CUT-09` antes do deploy |
| contract/test | public `/eventos` + monitoramento + SSE | method/request/DTO/status/header matrix from `D-CUT-17..19` | zeros enganosos, filtros legados, disclosure, credential URL ou auth bypass | `implement-in-this-todo` | `VAL-CUT-09/16` antes do deploy |
| security/contract | realtime stream | Bearer/global guard + browser fetch parser/cancel/refetch + no pg/timer structure | JWT em URL/log, usuário inativo, reconnect leak ou insert externo alegado | `implement-in-this-todo` | `VAL-CUT-16` antes do deploy |
| security/test | CSV export | per-column formula-prefix fixture for `=,+,-,@,TAB,CR,LF` | spreadsheet formula injection or numeric corruption | `implement-in-this-todo` | `VAL-CUT-19` antes do deploy |
| ops/consumer | UptimeRobot | current-release header migration/public-mode attestation | query credential breakage or false outage | `manual-only-with-rationale` | `VAL-CUT-18`; ação manual porque o consumer vive fora do repo e precede o merge |
| race/load | treatment SSE consumer | fake-time burst500 + sustained 100 ms/5 s fixed windows | request storm, debounce starvation ou paralelismo duplicado | `implement-in-this-todo` | `VAL-CUT-16` antes do deploy |
| concurrency/domain | treatment mutations | Prisma6.19.3; clients4/1/1; control 1s/1s/1s/200ms one-statement; matriz/inequalities G/D/R; two uncertain outcomes | lost update, cap saturation, readiness starvation, false fence/retry | `implement-in-this-todo` | `VAL-CUT-20` antes de Local-Implemented |
| deployment/concurrency | legacy↔candidate treatment writers | owner single-flight/depth1 + writer idle0/heartbeat/PID/locks + five counts + runner | reentrant/residual lock, idle expiry, auto-reacquire, legacy masking ou unsafe recovery | `implement-in-this-todo` | `VAL-CUT-08/21/22`; Stage mutation só no abort real |
| security/runtime | fiscal read activation | per-boot closed gate + two-context ADMIN proof/CAS | customer traffic before binding proof, restart-open ou cross-context | `implement-in-this-todo` | `VAL-CUT-23` antes do smoke fiscal |
| frontend/security | fiscal cached-data suppression | shared metadata client + monotonic requestStart deadline + skew/RTT/background/render expiry + fresh cache/restart/header/stale generation | cached rows/detail visible beyond current-boot lease | `implement-in-this-todo` | `VAL-CUT-23` antes do smoke fiscal |
| capacity/runtime | PostgreSQL connection caps | pre-implementation G/D/R/O*/L/Xd/Xr/runner/inequalities + pre-merge repeat | role/database cap reached despite global headroom ou implementação descartada por fork tardio | `manual-only-with-rationale` | preflight read-only antes de APROVADO em `VAL-CUT-30`; carga `VAL-CUT-20` |
| health/runtime | snapshot-only readiness sampler | fake clock + inspection-holds-control→DB-drop + flood1000/c100; sampler250/single-flight/deadline1000/snapshot500 | query por request, fila/P2024, falso 2xx, liveness bloqueada ou query/sessão órfã | `implement-in-this-todo` | `VAL-CUT-11/20/27` antes do deploy |
| security/auth | identity revocation + async completion | identity30/lease5 + delayed provider + SSE near-expiry + demotion-during-open | payload/evento/CAS sai após deadline sem revalidação ou usuário inativo visualiza além de35 s | `implement-in-this-todo` | `VAL-CUT-25/28` antes do deploy |
| ops/runtime | Active-fiscal-fechada | fake clock, expected-503 until local178, abort-initiation180, separate Remove/Rollback latency | hard-recovery claim falso ou 503 excluído após deadline | `implement-in-this-todo` | `VAL-CUT-29/32` antes do deploy |
| deployment/runtime | fiscal quiesce | opener/heartbeat/SIGTERM races + REC-3A/3B local simulation | stale opener reabre fiscal, rollback precede epoch invalidation ou API caída não possui ramo seguro | `implement-in-this-todo` | `VAL-CUT-24`; evidência remota apenas se abort real alcançar o ramo |
| explain/performance | logs query family | JSON plans for lists/aggregates/export/detail-history/payload/monitor/eligibility | predicate late, correlated scan or uncovered high-cardinality path | `implement-in-this-todo` | `VAL-CUT-17` antes do deploy |
| config test | bootstrap variables | configuration specs with flag false/true-invalid | enable sem pares fiscais/HMAC ou valores fora de bound | `already-enforced` | rerun obrigatório em `VAL-CUT-03` |
| read-only runtime probe | Smart Notas binding | `smart-notas-live.probe.spec.ts` | token/CNPJ mismatch, lista/detail indisponível | `already-enforced` | execução real obrigatória em `VAL-CUT-04` |
| load/stress | external path and 2 MiB envelope | RLS report on approved topology | saturation, quota amplification, memory/recovery failure | `implement-in-this-todo` | `VAL-CUT-05` |
| browser smoke | same-origin React/Nest release | source-owned fiscal browser journey | incompatible UI/API, context/cache leak, `/erros` regression | `implement-in-this-todo` | `VAL-CUT-06` |
| operational recovery | Railway deployment | pre-merge facts + runner/Remove; 3A graceful reviewed then all Active Removed; 3B all Active Removed; full-set zero2s; exact old-ID Rollback | API candidata indisponível, runner/Remove/Rollback ausente, zero inalcançável, imagem/vars erradas ou drill destrutivo | `manual-only-with-rationale` | local `VAL-CUT-08/24/35`; real conditional `VAL-CUT-22` |
| deployment/recovery | exclusive-freeze multi-candidate invariant | classify reviewed/extras; REC-2B never-Active only; every Active Remove→Removed; sampler/clients stop; full-set zero2s; extra-only Active routes 3B | unreachable zero proof, executable REC weaker than D-CUT-37 or hidden candidate | `implement-in-this-todo` | `VAL-CUT-35` before staged changeset; conditional `VAL-CUT-22` |
| security/race | external fiscal+treatment quiesce | revoke/demote + opener/mutation/quiesce/SIGTERM interleavings | estado irreversível por identidade cacheada ou await entre prova/CAS | `implement-in-this-todo` | `VAL-CUT-31` antes do deploy |
| ops/runtime | transition observer | pre-merge poll/deadline1/gap2/local178 + control-loss/Remove-latency | abort tardio, timer reset ou recovery180 claim | `implement-in-this-todo` | `VAL-CUT-32` antes do deploy |
| deployment/recovery | Auto-deploy and source stabilization | trigger→off, success→on, abort→REC-4/revert/zero queue | candidato rejeitado volta em push/redeploy posterior | `manual-only-with-rationale` | local `VAL-CUT-33`; remoto somente no cutover autorizado |
| governance/structural | current-round review binding | exact material/attestation/architecture refs + reset-on-change | review/coherence/drift antigos mascaram novo material | `implement-in-this-todo` | `VAL-CUT-34` antes de solicitar aprovação |
| deployment/runtime | Railway runtime fingerprint | replica1/region/source/0-20/health/approvals/deployments polled <=1s | scale/restart/platform deployment invalida modelo sem push | `manual-only-with-rationale` | `VAL-CUT-36`; remoto na janela autorizada |
| deployment/security | Railway configuration mutation sequence | ten-key changeset + activity cursor + zero staged + same-name value-change negative | valor muda sem alteração de nome/escopo ou sem novo deployment | `manual-only-with-rationale` | `VAL-CUT-38`; remoto somente por checkpoints read-only/autorizados |
| deployment/recovery | post-Rollback convergence | exact prior image+vars/revision Active + baseline-specific prior probe + candidates zero2s | REC-4 declarado pela ação Rollback ou por candidate-only readiness | `implement-in-this-todo` | `VAL-CUT-37/39`; conditional real `VAL-CUT-22` |
| deployment/recovery | pre-merge unexpected candidates | first-mutation classification; REC-1 unchanged-only; REC-1X never-Active terminal or Active remove-all→zero→Rollback→REC-3C | config restore enquanto candidato pré-merge ainda pode executar ou REC-4 sem source drift | `implement-in-this-todo` | `VAL-CUT-40`; conditional real evidence only if state reached |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after review baseline freeze and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set: TODO + topology/dependency artifacts + railway/Docker/config/health/fiscal boundaries`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** arquitetura round34 limpa é histórica; a crítica R34 gerou D-CUT-42 e alterou recovery desde a primeira mutação. Reviewer fresco round35 será exigido após publication+attestation. Evidência histórica `/tmp/uninotas-cutover-round34b-architecture.GBSi7l/dispatch.json`, SHA-256 `23429a55ee1ca47103bf0b568332a8f745012a10641a15c37aea1f7b700ac742`.

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
| `REVAL-ARCH-01` | high | yes | `Integrated; superseded by R26-STRUCT-01` | a primeira definição isolava o cutover fiscal, mas ainda admitia cap4 preparatória; `D-CUT-28` agora bloqueia este TODO e exige TODO/promoção próprios e rebaseline integral. |
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
| `R12-OPS-01` | high | yes | `Integrated` | `REC-2A` inicia no merge e cobre record ausente, approval, delayed/rejected trigger e in-flight; restore exige prevenção/terminal conclusivo. |
| `R12-OPS-02` | high | yes | `Integrated` | `D-CUT-20`, Execution 1/6/8 e `VAL-CUT-18` migram/atestam UptimeRobot header-only antes do merge, sem rotação. |
| `R12-SEC-01` | high | yes | `Integrated` | `D-CUT-21` e `VAL-CUT-19` neutralizam `=,+,-,@,TAB,CR` e foram ampliados por R22 para LF em cada coluna textual externa. |
| `R12-ARCH-01` | high | yes | `Integrated` | path/lote usam ref 1..64; monitor config/header 1..200; whitespace/oversize dão 400 e ref válida inelegível dá 404. |
| `R12-PERF-01` | medium | no | `Integrated` | `D-CUT-22`/`VAL-CUT-16` coalescem burst500 e, após R22, usam janelas fixas testadas sob fluxo sustentado. |
| `R12-PERF-02` | medium | no | `Integrated` | workloads usam URIs portuguesas exatas e filtros SQL equivalentes separados. |
| `R12-STRUCT-01` | medium | no | `Integrated` | whitelist inclui manifest/lock; runtime realtime deixa de importar `pg`, posteriormente refinado para preservar `pg`/types somente como dev tooling de `espelhar.ts`. |
| `R12-DOC-01` | low | no | `Integrated` | round-12 refs exatas registradas e estados avançam para round 13. |
| `R13-PCV-01` | high | yes | `Integrated` | quatro rows usam registros/estados/deadlines/evidence rules fechados `pcv-1`; BCI é required/high com `serialize`, invariant e probes 5/10/20 que validam persistência, estado e SSE. |
| `R14-DOC-01` | high | yes | `Integrated` | `git rev-parse --verify` confirmou root material `da6ef14219e92e67428fd30cef98590512dc0832`, carrier `d60bffe4c57ffbc40477c2798d72ac87191b1a6e`, Foundation material `2368b5c7b0a8d3187caae08bd426a4bde63dfda0` e attestation `55ff86207e16255d4e63e014b591fc426e772590`. |
| `R14-BCI-01` | high | yes | `Integrated` | lock key namespaced, ordem lexical binária única e `GREATEST(clock_timestamp(), MAX(criado_em)+1us)` sob lock eliminam inversão/empate; `VAL-CUT-20` inclui wait inversion e collision. |
| `R15-GOV-01` | high | yes | `Integrated` | o `Contract status` definitivo round 16 já está no material publication commit; a attestation não pode alterar esse campo nem qualquer seção material comparada. |
| `R15-BCI-01` | high | yes | `Integrated` | isolation/waits/retry/error map permanecem; gate2/pool5 originais foram rebaselined por `R21-PERF-01` para clients4/1/1, gate1 e 500 locks. |
| `R16-OPS-BCI-01` | high | yes | `Integrated` | `D-CUT-24` fixa overlap0/drain20, barrier30 no primeiro tráfego autenticado e quiesce ADMIN same-boot/active0/+2s antes de rollback; BCI usa dois processos legacy↔candidate. |
| `R17-OPS-BCI-01` | high | yes | `Integrated` | `D-CUT-24` elimina auto-open: o prazo de 30 s é só mínimo; ADMIN atesta deployment anterior terminal/removido e o backend exige prova DB positiva. A contagem inicial foi posteriormente refinada nas cinco contagens de `R20-OPS-BCI-01`. |
| `R17-OPS-BCI-02` | high | yes | `Integrated` | `adquirirLease()` e quiesce fazem transição/contador sincronamente antes do primeiro `await`; rollback monitora <=1 s até remover candidato, e qualquer novo boot nasce fechado, é detectado e re-quiescido. `VAL-CUT-21` força ambas as corridas. |
| `R18-OPS-BCI-01` | high | yes | `Integrated; refined by R28-SEC-01` | `D-CUT-24` introduz epoch monotônico: opener captura boot/epoch/estado, faz prova async e só abre por compare-and-transition síncrono. SIGTERM interno incrementa antes de await; quiesce externo agora prova auth fresca antes da transição síncrona. `VAL-CUT-21/31` cobrem stale opener e revogação. |
| `R18-OPS-IDENTITY-01` | high | yes | `Integrated` | `bootId` é UUID v4 lowercase de 36 ASCII; base/treatment 45/55 foram preservados e writer/control 52/53 adicionados em R21; current_setting/reversão devem coincidir exatamente. |
| `R18-API-01` | medium | yes | `Integrated` | rows operacionais congelam envelope/mensagem/`Retry-After: 1`; quiesce 503 preserva fechamento, retry é idempotente e rollback permanece bloqueado até prova zero. |
| `R19-OPS-BCI-01` | high | yes | `Integrated` | primeiro request captura boot/epoch/inicializando uma vez; callback 30 s usa CAS e incrementa epoch; quiesce/SIGTERM cancelam best-effort e tornam callback no-op. Ambos os ordenamentos entram em `VAL-CUT-21`. |
| `R19-OPS-BCI-02` | high | yes | `Integrated` | `REC-3` mantém conjunto de boots observados, exige prior terminal/removido ou quiesced+drained e reinicia checklist/+2 s em boot change; os zeros inicialmente agregados foram refinados nas cinco contagens e no probe externo de `R20-OPS-BCI-01`. |
| `R19-OPS-DB-01` | high | yes | `Integrated` | datasource direto/session-affine e credencial exclusiva viram gate; transaction/statement multiplexing ou modo desconhecido bloqueia abertura/cutover e recebe negativo no harness. |
| `R19-API-01` | medium | yes | `Integrated` | após sucesso/falha DB, opener revalida boot/epoch/state primeiro; stale/quiesced sempre 409 sem Retry-After, e 503 só ocorre se captura ainda atual. |
| `R20-OPS-BCI-01` | high | yes | `Integrated` | classificador expõe cinco contagens: candidata atual, treatment atual, candidata não atual, treatment não atual e não candidata. Pré-switch exige os quatro zeros aplicáveis; pós-switch runner externo permite não candidata apenas com legado exato `Active` e exige qualquer UUID candidato, inclusive não observado, em zero. `VAL-CUT-08/21` mantém sessão legada e candidata simultâneas para provar que não há mascaramento. |
| `R20-OPS-BCI-02` | high | yes | `Integrated` | lease libera exact-once no settle. Após R22, rejeição commit-uncertain cobre explicitamente sessão ainda observável **ou** encerrada; nenhum caso publica/repete e recovery aguarda prova externa coerente. |
| `R21-OPS-BCI-01` | high | yes | `Integrated` | writer Prisma pool1 valida PID/lock e não auto-reacquire; R22 completou persistência com versão exata, idle lifetime0, heartbeat, owner single-flight e teste >300 s. |
| `R21-PERF-01` | high | yes | `Integrated` | pools fixam <=6 por candidato; R22 adicionou transição e R23 completou com caps global/database/role e budgets externos. |
| `R21-OPS-02` | high | yes | `Integrated` | runner externo/ACL/session-affinity/classifier viram gate read-only pré-changeset/pré-merge repetido <=15 min e requisito da janela; perda pré-merge aborta, perda pós-merge é breach fail-closed. |
| `R21-ADH-01` | medium | yes | `Integrated` | `VAL-CUT-08` contém apenas simulação local + fatos/probe remoto read-only; `VAL-CUT-22` coleta Rollback real somente se um abort alcançar `REC-3`, senão n/a. |
| `R22-ARCH-PERF-01` | high | yes | `Integrated` | `D-CUT-23` distingue candidato6 de budget transitório; R23 refinou capacidade pelo menor residual global/database/role. |
| `R22-ARCH-OPS-BCI-01` | high | yes | `Integrated` | Prisma/Client exatos `6.19.3`, writer idle lifetime0, heartbeat e teste real >300 s entram em `D-CUT-23/24` e `VAL-CUT-21`. |
| `R22-ARCH-OPS-BCI-02` | high | yes | `Integrated` | opener faz CAS single-flight/owner antes do await, uma aquisição/depth1 e cleanup idempotente; interleavings open/open entram em `VAL-CUT-21`. |
| `R22-ARCH-OPS-BCI-03` | high | yes | `Integrated` | commit incerto separa resposta perdida com sessão observável de sessão encerrada; ambos falham 503/refresh sem SSE/retry e exigem prova externa. |
| `R22-ARCH-GOV-01` | medium | no | `Integrated` | UptimeRobot usa enum canônico `manual-only-with-rationale` com justificativa no harness. |
| `R23-ARCH-FISCAL-01` | high | yes | `Integrated` | `D-CUT-25` adiciona header fiscal estável; cache/state/list/detail limpam/suprimem todo dado e stale response não repopula antes de 200 pós-abertura; `VAL-CUT-23` começa com cache preenchido. |
| `R23-ARCH-PG-01` | high | yes | `Integrated; superseded by R24-ARCH-PG-01` | R23 introduziu caps global/database/role; R24 corrigiu a fórmula única para matriz disjunta e inequalities separadas em `D-CUT-23`. |
| `R23-ARCH-READY-01` | high | yes | `Integrated` | `D-CUT-10/23` e `VAL-CUT-11/20` separam falha da inspeção com SELECT1 verde/2xx de PostgreSQL real down/bounded não-2xx. |
| `R24-ARCH-FISCAL-01` | high | yes | `Integrated` | `GET /notas/estado` fornece lease positiva curta do boot; enter/focus/resume suprime antes da prova, heartbeat3/TTL5/timeout1 e geração/epoch/header impedem cache sem prova. Residual <=5 s fica explícito para aprovação. |
| `R24-ARCH-READY-01` | high | yes | `Integrated` | control pool1 usa pool/connect/socket1 s e statement200 ms; cada chamada é uma statement sem transaction/wait. Harness inicia inspeção 1 ms antes e congela SLOs healthy/DB-down/liveness/cleanup numéricos. |
| `R24-ARCH-PG-01` | medium | yes | `Integrated` | matriz disjunta associa processo→role→database→máximo; runner usa Xd/Xr, O* exclui participantes modelados e cada cap recebe inequality/margem própria, com -1 como n.a. |
| `R25-ARCH-FISCAL-01` | high | yes | `Integrated` | lease frontend agora usa `performance.now()` capturado antes do request, deadline máximo requestStart+5 s, descarta resposta tardia, revalida no render e testa skew/RTT/restart/background timer. |
| `R25-STRUCT-FISCAL-02` | high | yes | `Integrated` | strict diff autoriza `api/notas.ts`, `api/cliente.ts` e `NotasFiscaisContexto.tsx`; client compartilhado preserva response metadata/header sem raw fetch/text matching duplicado. |
| `R25-OPS-READY-01` | high | yes | `Integrated` | readiness recebe deadline end-to-end <=1500 ms e harness composto inspection-owning-control→DB-drop→readiness+1 ms com cancelamento e cleanup pós-recovery. |
| `R26-OPS-01` | high | yes | `Integrated` | D-CUT-26/API/VAL adicionam quiesce fiscal one-way, epoch sync antes do await, SIGTERM, frontend invalidation e ordem REC-3A. |
| `R26-OPS-02` | high | yes | `Integrated` | REC-3B usa Railway Remove (ação oficial), espera Removed e runner candidata/transaction/fence zero estável2 s antes do Rollback; inconclusivo é breach. |
| `R26-SEC-01` | medium | yes | `Integrated` | D-CUT-27 fixa identity cache monotônico30 s + lease5 s = revogação<=35 s, teste deactivate/cache-fill e aceite final explícito. |
| `R26-STRUCT-01` | medium | yes | `Integrated` | D-CUT-28 torna L desconhecido hard stop; cap4 recebe TODO/promoção próprios e obriga rebaseline/CI/reviews ao retomar. |
| `R26-PERF-01` | medium | yes | `Integrated` | D-CUT-29 torna handler snapshot-only e sampler250/single-flight/deadline1000/age500; flood1000/c100 não cria DB queue e stale falha fechado. |
| `R29-ARCH-OPS-01` | high | yes | `Integrated in round30 candidate` | D-CUT-37 move freeze exclusivo/zero queue para antes do changeset, autoriza somente a tree revisada e classifica revision extra no conjunto completo de candidatos antes de restore/Rollback. |
| `R30-ARCH-OPS-01` | high | yes | `Integrated in round31 candidate` | REC-2B agora exige zeros externos do conjunto antes de restore; REC-3A permite quiesce somente ao reviewed e força Remove→Removed para todo extra Active; harness `VAL-CUT-35` protege a invariável. |
| `R31-ARCH-OPS-01` | high | yes | `Integrated in round32 candidate` | REC-3A faz quiesce/drain gracioso e depois Remove→Removed também do reviewed, cessando sampler/clients antes do full-set zero2s. |
| `R31-ARCH-OPS-02` | high | yes | `Integrated in round32 candidate` | REC-2A roteia reviewed never-Active+extra Active explicitamente a REC-3B remove-only; VAL-CUT-35 inclui a fixture. |
| `R33-ARCH-OPS-01` | high | yes | `Integrated in round34 candidate` | D-CUT-38/41 separam runtime polling de configuração, exigem ten-key changeset/activity cursor/zero staged em transições e negativo value-only sem persistir valores/hashes. |
| `R33-ARCH-OPS-02` | high | yes | `Integrated in round34 candidate` | D-CUT-39/40 congelam probe do exact prior: `/saude` body ok/ok, auth/read legado e SELECT1; REC-3C não exige `/prontidao` da imagem anterior. |
| `R34-GOV-01` | medium | yes | `Integrated as metadata-only binding` | material e attestation round34 agora aparecem com refs exatas no pacote; a primeira opinião permanece provisória e será repetida por reviewer fresco. |
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
- **Baseline commit:** `985b5d13d96a46bd8107e8796986f4704838133c`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** `R34-OPS-01` foi integrado, validado e publicado como material imutável round35; a attestation registra essas refs sem alterar as seções materiais.
- **Evidence / reference:** `reviewRound=35`; Foundation `origin/main@985b5d13d96a46bd8107e8796986f4704838133c`; root `MonitorNotes/delphi-and-foundation@b02b8c7646ed894b08abb4e76db6be1483f2ae8b`; code-origin `31712a042cab3c796d5daca7350c6c58453e1c73`; `todo_deterministic_validator.py=PASS`; `validate_foundation.py=PASS`; drift diagnóstico `go`, `0/23`, mas deliberadamente não satisfaz o gate causal antes da crítica conforme D-CUT-36.
- **Waiver authority / reference:** `n/a`.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impede alteração material entre o pacote revisado e o aprovado.
- **Trigger stage:** `after review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `canonical defaults, incluindo Diff Expectation Contract, Module Decision Baseline Snapshot e Decision Baseline (Frozen Before Implementation)`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- **Gate status:** `not_run`
- **Findings summary:** scope drift round35 será rerodado **após** arquitetura e crítica round35 limpas; nenhum resultado anterior satisfaz D-CUT-36.
- **Evidence / reference:** pendente causal; exigir `reviewRound=35`, refs material/attestation/architecture e digest/path do dispatch crítico resolvido.
- **Waiver authority / reference:** `n/a`.

## Frontend / Consumer Matrix

| Producer Surface In This TODO | Consumer | Delivery State | Evidence / Waiver |
| --- | --- | --- | --- |
| `GET /api/v1/notas/estado` | React `Geral`, detalhe e fiscal session-cache visibility gate | `D-CUT-25 frozen; new in-memory producer/consumer planned` | shared api client metadata; monotonic requestStart+5s; skew/RTT/background/render expiry; boot/epoch/generation; no DB/provider |
| `GET /api/v1/notas` | React `Geral`, `ListaNotas`, session cache | `implemented candidate; fiscal lease gate planned` | render only under current positive lease; header503 invalidates; no provider before ADMIN |
| `GET /api/v1/notas/:noteId` | React `/notas/:noteId`, detail cache | `implemented candidate; fiscal lease gate planned` | detail/list cache hidden without current lease; generation blocks stale detail/provider |
| `/api/v1/operacao/notas/barreira|provar-e-abrir|quiescer` | project Owner/ADMIN cutover/recovery runbook; React handles state/header invalidation | `D-CUT-25/26/30/31/33/34 frozen; new operational producer planned` | two-context proof, fresh no-cache ADMIN before opener/quiesce CAS, local178/real180 abort-initiation, internal SIGTERM separated, REC-3A/3B/3C, no-store/redaction |
| `/api/v1/eventos` list/resumo/produtos/export/detalhe/payload/history | React `/erros` + `/eventos/:refId`; external consumers unknown | `final contract frozen in D-CUT-17..19; implementation planned` | exact method/request/DTO/status/header matrix; SQL predicate incl. pagination/correlated attempts; Owner attestation before deploy; no waiver |
| `/api/v1/eventos` contract documentation | `backend/README.md` + `frontend/README.md` + Swagger/OpenAPI decorators in `backend/src/logs/logs.controller.ts` + global description in `backend/src/main.ts` | `known contract consumers; update required` | docs remove five-tab/log-success/EventSource claims and describe error-only + refresh + fetch/Bearer treatment stream |
| `/api/v1/eventos/*/tratamento` unitário/lote | React error-treatment flows | `producer guard + D-CUT-23 serialization planned; behavior preserved only when original class is ERRO` | mutation tests deny `PENDENTE`/`SUCESSO` without existence disclosure; BCI 5/10/20 proves append/state/SSE invariants |
| `/api/v1/operacao/tratamentos/barreira|abrir|quiescer` | project Owner/ADMIN runbook + external runner; React handles treatment 503/refresh | `D-CUT-24 frozen; new operational producer planned` | Prisma6.19.3; owner/depth1; idle0/heartbeat; PID/locks/five counts; exact-once; two uncertain outcomes |
| `GET /api/v1/realtime/eventos` | React `useTempoReal`/fetch streaming somente em `/erros` | `D-CUT-19/30 frozen; producer/consumer change planned` | Bearer/global guard, lifetime=min(30s,remaining identity), zero event pós-deadline, no query JWT/log, treatment-only stream, cancel/refetch |
| `GET /api/v1/monitoramento/erros` | UptimeRobot | `exact shape frozen; consumer migration required before merge by D-CUT-20` | current-release header migration/URL cleanup or public-mode attestation; 200/400/401/503 + no-store; tratados excluídos |
| `GET /api/v1/prontidao` | Railway deployment healthcheck + public callers | `new snapshot-only producer/config consumer planned` | handler no DB/wait; sampler250/deadline1000/snapshot500; healthy/compound/flood1000; exact path + deployed evidence |
| `GET /api/v1/saude` | human/public liveness consumers | `existing contract retained as liveness; removed from Railway readiness role` | existing shape/status test + runbook distinction |
| Smart Notas env/budgets | NestJS bootstrap / Railway sealed variables | `budgets fail-closed change planned; no frontend consumer` | missing-variable startup negatives + client bundle/env scan |
| `note_read_model` / `integration_error_read_model` | Foundation registry, modules and upper canonical docs | `promotion planned only after runtime evidence` | atomic diff across policy/modules/root docs + Foundation validator |

## Test Strategy

- **Strategy (`test-first|test-after|not-applicable`):** `test-first`.
- **Why:** budgets fail-closed, readiness e predicado error-only alteram contratos de segurança/produção; cada mudança começa por um teste negativo reproduzível antes do código.
- **Fail-first targets:** readiness snapshot sampler/flood/compound; SQL/error-only; `D-CUT-17..32`; CSV-LF; JWT/SSE deadline; Prisma/clients; pre-implementation matriz/inequalities/hard-stop L; control one-statement/200; fence/commit; fiscal handshake/quiesce/SIGTERM/REC-3B; delayed-provider/demotion/Active-fechada180; runner/Remove/recovery/correlation/context/HMAC/probe.
- **External read-only:** `/empresa`, lista e detalhe nos dois contextos, sem mutação fiscal e com saída redatada.
- **Browser:** build local da source tree com interceptação controlada; depois smoke imediato dos bits reconstruídos no único `Stage` customer-facing.
- **Capacity:** latência, quota, concorrência e memória near-limit; planos `EXPLAIN` redatados e p95 query-side cumprem `VAL-CUT-17` antes de promoção.
- **Rollback:** fatos atuais atestados pré-merge; alvo antigo exato confirmado como rollbackable somente pós-switch/pre-smoke amplo; restore real apenas em abort, com risco residual aprovado e RTO de 10 minutos.

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before (`APROVADO|Local-Implemented|promotion`) | Status (`planned|passed|blocked|waived|n/a`) | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PostgreSQL capacity preflight | seleciona cutover atual vs TODO cap4 | L autoritativo, role/database, G/D/R/O*/margens, Xd/Xr, runner/ACL/affinity e três inequalities | external runner read-only no target; output redatado; nenhuma credencial/query sensível persistida | bundle read-only `D-CUT-32` documentado no `DEPLOY.md`; repetir <=15 min pre-merge | `APROVADO` | `blocked` | fingerprint JSON redatado de `VAL-CUT-30` | snapshot instantâneo não prova L; inconclusivo encerra este TODO |
| backend NestJS | fiscal/config/readiness/error-only/correlation/auth mudam | startup fail-closed; DB-negative readiness; exact HTTP contract; SQL predicate; delayed-provider auth recheck; SSE deadline; ADMIN demotion-before-CAS; Active-fechada180; correlation ID | Node 22 host Windows; fixtures Jest/fake-clock determinísticas/Prisma SQL assertions; nenhum token live | no diretório `backend`: `npm test -- --runInBand && npm run lint && git diff --exit-code && npm run build`; se lint autofixar, invalidar/refazer freeze e toda validação | `Local-Implemented` | `planned` | output + SHA/tree antes/depois | `npm run lint` contém `--fix`; zero diff é obrigatório |
| backend SQL plan/performance | error-only muda toda query family | listas, resumo, produtos, export, detalhe-history200, payload, monitor e eligibility; p95 3 s/8 s | seed20k/80% inelegível; ref histórico200; PG config; ordem de `VAL-CUT-17` | 5 warmups + EXPLAIN + 30 SQL; GETs 50 concurrency4; export20 concurrency1; mutation eligibility SQL rollback-only | `Local-Implemented` | `planned` | seed + JSON plans + séries/p95 | falha abre TODO schema/index |
| backend BCI treatment/readiness | PATCH/lote e legacy↔candidate | Prisma6.19.3; 4/1/1; control1s/200ms; sampler250/deadline1000/snapshot500/flood; matriz/inequalities; owner/idle/uncertain | PostgreSQL direto + multiplex negative; old+candidate+runner; fault injection | `VAL-CUT-11/20/21`; `VAL-CUT-22` condicional | `Local-Implemented` | `planned` | `bci-pcv1.json` + SHA-256 | C=6; hard-stop unknown L; cleanup composto |
| backend/frontend fiscal activation | reads Smart Notas no Stage direto | per-boot closed, requestStart+5s, identity deadline at emission, ADMIN recheck, Active-fechada180/restart/SLO | adapter stub + fake clock + React API/context/cache/state/list/detail + live redacted probe | specs `VAL-CUT-23/28/29` + live probe após Active | `promotion` | `planned` | redacted phase/state/probe/browser record | residual restart<=5s and revocation<=35s; observation starts after open |
| backend near-limit | envelope externo/memória | 2 MiB, fairness, semaphore 4, rates 15/60, timeout/abort/recovery | loopback stub only; `RLS_OUTPUT_DIR` redatado | no diretório `backend`: `RLS_OUTPUT_DIR=../artifacts/cutover-rls npm test -- --runInBand --runTestsByPath src/fiscal-notes/__tests__/smart-notas-load.spec.ts` | `Local-Implemented` | `planned` | `artifacts/cutover-rls` redatado | sem tráfego provider real |
| frontend React/Vite unit/race | context/cache/contract mudam | Geral/detalhe/Erros, troca rápida de contexto, logout/401 cache purge e error-only | Node 22 host Windows; fixtures locais dos scripts | no diretório `frontend`: `npm run test:notas && npm run test:notas:race && npm run lint && npm run build` | `Local-Implemented` | `planned` | output dos cinco comandos | bundle same-origin |
| frontend Playwright intercepted | jornada visível muda | login -> Geral -> detalhe -> Erros -> Geral; ambos contextos; nenhuma origem externa; `/eventos` só erro | `npm run dev` em loopback; Chrome/Chromium local em `CHROME`; todas as APIs interceptadas pelo runner | no diretório `frontend`: `ALVO=http://127.0.0.1:5173 CHROME=<chromium-local> npm run e2e:notas` | `Local-Implemented` | `planned` | relatório console redatado | adicionar negativas do history/error-only neste TODO |
| root Docker | artefato único Railway | build, startup, liveness/readiness positiva e PostgreSQL-negativa | Docker daemon; env local não secreto; candidate tree limpa | `docker build -t monitornotes:cutover-candidate .` seguido do runbook de startup/probes em `DEPLOY.md` e comparação final de tree OID | `promotion` | `planned` | image ID local + probe outputs | source-level only; OCI Railway pode divergir |
| Foundation / Delphi | TODO/authority/canon mudam | schema, diff drift, Foundation integrity e contexto PACED | links existentes; nenhum repair salvo desvio Delphi-managed | `python3 delphi-ai/tools/todo_deterministic_validator.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md && python3 foundation_documentation/deterministic/validate_foundation.py --root foundation_documentation && "/mnt/c/Program Files/Git/bin/bash.exe" -lc 'cd /c/unifast/monitordenotas && bash delphi-ai/verify_context.sh'` | `APROVADO` | `planned` | stdout dos guards | runner canônico evita incompatibilidade CRLF do wrapper sob WSL; repetir no closeout |
| live provider | binding real dos dois emissores | `/empresa`, lista e detalhe read-only em Unifast/Prosperar usando `10 s/4/15/60` | runner autorizado; cinco bindings presentes; probe implementado com envelope exato; saída redatada | no diretório `backend`: `SMART_NOTAS_PROBE_ENABLED=true SMART_NOTAS_TIMEOUT_MS=10000 SMART_NOTAS_MAX_CONCURRENCY=4 SMART_NOTAS_RATE_PER_USER_MINUTE=15 SMART_NOTAS_RATE_PER_CONTEXT_MINUTE=60 npm test -- --runInBand --runTestsByPath src/fiscal-notes/__tests__/smart-notas-live.probe.spec.ts` | `promotion` | `blocked` | output agregado/redatado | código do probe deve consumir/validar os valores, sem hardcode legado |
| Railway browser | experiência real/deployed bits | login, fase fechada, abertura, Geral/detalhe/Erros/Geral, ambos contextos, revision/build correta | final main tree equal; ten-key changeset consumido; readiness verde; sessão autorizada | smoke autenticado conforme `DEPLOY.md`; abertura deve concluir antes de local178 ou o abort deve iniciar até real180 sob caminho saudável, com recovery governada separadamente; depois, observação de 30 minutos pós-open | `promotion` | `blocked` | deployment ID + relatório redatado | somente após deploy autorizado |

## Plan Review Gate

- **Review decision:** `required`
- **Review status:** `round35 candidate integrates R34 critique finding; publication/attestation/current architecture/critique pending`
- **Required lenses:** architecture, operations, rollback, security, tests, performance, observability and structural soundness.
- **Known plan finding:** o health atual retorna HTTP 2xx quando o banco está degradado; `D-CUT-10` agora exige readiness separada não-2xx e mantém Smart Notas fora do loop.
- **Approval request condition:** nova revisão confirma `D-CUT-06..42`, crítica limpa e somente depois coherence/drift convergem com refs/digest round35; preflight D-CUT-32/34/35/37/38/40/41/42 é conclusivo e guards `go/preflight-go`.

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

- **Issue ID:** `PLAN-CUT-04`
  - **Severity:** `high`
  - **Evidence:** `backend/src/prisma/prisma.service.ts:5`, `backend/package.json:36`, `backend/package-lock.json:2374`, `D-CUT-23`.
  - **Why it matters now:** a única réplica ainda produz mais de um processo durante deployment; seis conexões do candidato não incluem legado nem runner.
  - **Option A (Recommended):** provar autoritativamente `L`; se não for possível, bloquear este TODO e abrir outro TODO aprovado para cap4. Após sua promoção verde, recomeçar o cutover fiscal sobre novo baseline e repetir todos os gates/tree evidence.
    - **Effort:** `medium`
    - **Risk:** `low`
    - **Blast radius:** `runtime`
    - **Maintenance burden:** `low`
    - **Performance impact:** `improves`
    - **Elegance impact:** `neutral`
    - **Structural soundness impact:** `improves`
  - **Option B (Alternative):** criar pooler/role cap global e novo modelo de capacity governance.
    - **Effort:** `high`
    - **Risk:** `medium`
    - **Blast radius:** `database`
    - **Maintenance burden:** `medium`
    - **Performance impact:** `unknown`
    - **Elegance impact:** `improves`
    - **Structural soundness impact:** `improves`
  - **Option C (Do Nothing):** tratar `6` como teto global e usar apenas snapshot de sessões.
    - **Effort:** `low`
    - **Risk:** `high`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `high`
    - **Performance impact:** `regresses`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Recommendation:** Option A antes de solicitar APROVADO; isola a segunda release e impede implementar/validar contra uma tree que o ramo cap4 tornaria obsoleta.

### Failure Modes & Edge Cases

- [ ] Candidate e final `main` têm tree OID diferente: bloquear promoção e refazer freeze/CI.
- [ ] Changeset staged não pode ser commitado sem redeploy ou não contém exatamente dez chaves: abortar antes do merge.
- [ ] Pré-merge sem plano/ID/snapshot/acesso geral, ou pós-switch sem `Rollback` no antigo ID exato antes do smoke amplo: abortar ou renovar risco/RTO para fallback `Redeploy`.
- [ ] Railway cria revision de source/config inesperadas ou readiness/smoke falha: abortar e acionar rollback.
- [ ] Após merge, deployment ainda invisível/awaiting approval/trigger delayed ou rejected: permanecer `REC-2A`; nunca restaurar config sem prova conclusiva de prevenção/terminal.
- [ ] Binding fiscal diverge, ocorre cross-context, segredo/PII vaza, quota/memória satura: abortar imediatamente pelos thresholds.
- [ ] Linha principal é `ERRO`, mas histórico correlacionado contém `SUCESSO/PENDENTE` original: filtrar cada linha; tratamento `PENDENTE` do erro continua visível.
- [ ] Predicado aplicado só depois da query: bloquear por totais/páginas/agregações incorretos; teste estrutural deve provar filtro SQL antes de count/group/order/limit/mutations.
- [ ] Filtros `PENDENTE/SUCESSO` ainda aceitos, resumo mantém campos removidos, ou detalhe/tratamento revela ref inelegível: bloquear promoção por contrato público divergente.
- [ ] Defaults/allowlists divergem, resumo/export aceitam paginação ignorada, lote aceita ref branca/duplicada, ou erro sai fora do envelope comum: bloquear promoção.
- [ ] UptimeRobot ainda usa query token, consumer mode é desconhecido ou header não foi provado contra current release: bloquear merge sem rotacionar segredo.
- [ ] CSV permite scalar textual iniciado por `=,+,-,@,TAB,CR,LF` sem prefixo neutralizador: bloquear por spreadsheet injection.
- [ ] Lote500 causa mais de um par na janela, ou eventos sustentados estendem a janela/causam starvation/paralelismo duplicado: bloquear por request storm/staleness.
- [ ] README, decorators OpenAPI ou descrição Swagger global ainda anunciam cinco abas/sucesso legado: bloquear promoção por contrato incoerente.
- [ ] Realtime ainda aceita JWT em query, ignora o guard global, abre conexão PostgreSQL/polling/NOTIFY, emite `evento.novo`, permanece após logout/unmount ou emite no/após identity deadline: bloquear promoção.
- [ ] Plano SQL filtra inelegíveis após window/group/limit, executa scan correlacionado por linha, ou qualquer lista/resumo/produtos/detalhe/payload/monitoramento/eligibility excede p95 `3 s` (`8 s` export): bloquear e abrir TODO separado de schema/index.
- [ ] Abort restaura config antes de todos never-Active terminais/full-set zero2s, revision extra não entra no conjunto, algum Active não atinge Removed, reviewed Active+controls não executa 3A graceful-then-remove, ou extra-only Active não migra a 3B remove-all.
- [ ] Prazo de 30 s expira, mas deployment anterior não está terminal/removido, há sessão vazia/desconhecida/legada ou a ACL não permite prova: manter `aguardando_abertura`, retornar 409/503 e abortar sem tratamento; tempo sozinho nunca autoriza.
- [ ] Mutation tenta entrar ao mesmo tempo que quiesce: somente a lease adquirida sincronamente antes do primeiro `await` pode drenar; qualquer check assíncrono antes do incremento é regressão bloqueadora.
- [ ] `/abrir` espera inspeção DB enquanto quiesce/SIGTERM ocorre: epoch muda antes do await operacional; o compare final falha 409, estado permanece quiescido e nenhuma lease entra.
- [ ] Timer 30 s vence depois de quiesce/SIGTERM: cancelamento best-effort + CAS boot/epoch/inicializando fazem callback no-op; request posterior não rearma.
- [ ] Inspeção DB do opener falha depois de quiesce/SIGTERM: recheck stale precede o erro e produz 409 sem `Retry-After`, nunca 503 ambíguo.
- [ ] `application_name` diverge de base45/writer52/control53/treatment55, UUID não é v4 lowercase, sufixo é desconhecido ou treatment não reverte: falhar startup/transaction/barreira antes de mutation.
- [ ] Binding usa/possivelmente usa transaction ou statement multiplexing: a prova por sessão é inválida; bloquear ativação até endpoint direto/session-affine ou redesenho aprovado.
- [ ] Quiesce retorna 503 por prova DB inconclusiva: o fechamento continua aplicado; retry idempotente/status devem provar zeros, nunca executar rollback baseado apenas no erro/resposta.
- [ ] Boot A anteriormente aberto fica ocioso/sem sessão adicional quando B tenta abrir: o session fence exclusivo de A continua no writer pool1 e bloqueia B. Se a sessão de A cai, B só adquire após lock/transaction server-side sumirem; A detecta PID/lock divergente e jamais reacquire automaticamente.
- [ ] Após Rollback, o legado exato fica `Active` e abre sessões não candidatas enquanto uma sessão candidata persiste: o probe externo conta as classes separadamente; a candidata bloqueia conclusão e não pode ser mascarada pelo legado.
- [ ] Conexão writer cai com commit incerto: Promise rejeita/libera lease exact-once sem SSE/retry; sessão pode permanecer observável ou encerrar e liberar tudo. Nenhum resultado autoriza inferir commit/abort; refresh e prova externa cercam opener/Rollback.
- [ ] Read/auth bursts disputam capacidade: read pool4 pode enfileirar, mas writer1/control1 ficam isolados; qualquer P2024, snapshot healthy ausente/stale, handler p95>100 ms, read>3 s ou >6 conexões candidatas reprova.
- [ ] `C=6` é teto global ou `L` vem só de snapshot: bloquear; sem `L` autoritativo, encerrar este TODO e abrir cap4 separado, nunca executar preparatória aqui.
- [ ] Capacidade usa residual único, ignora `datconnlimit`/`rolconnlimit`, conta runner/legado/candidato em O*, não resolve Xd/Xr, trata cap -1 como zero, possui classe/role/database/budget desconhecido ou falha qualquer inequality: bloquear antes do APROVADO; repetir <=15 min pre-merge.
- [ ] Control excede pool/connect/socket1/statement200, usa transaction/wait, ou sampler sobrepõe; bloquear. Handler `/prontidao` chama Prisma/aguarda promise/cria fila, flood aumenta statements/P2024/RSS não recupera: bloquear.
- [ ] Sampler não cumpre fixed250/deadline1000/snapshot-age500, composto control-held→DB-drop mantém 2xx além500 ms, liveness>250 ou órfão2s: bloquear.
- [ ] Prisma/Client diverge de `6.19.3`, writer omite idle lifetime0, heartbeat falha, PID muda no idle >300 s ou policy server/proxy é incompatível: quiescer/bloquear sem auto-reacquire.
- [ ] Dois openers alcançam o advisory acquire, lock depth excede `1` ou cleanup não pertence ao owner: bloquear; quiesce/SIGTERM devem terminar sem lock residual/unlock excedente.
- [ ] Commit incerto assume obrigatoriamente transaction viva ou encerrada: bloquear. Harness deve provar os dois resultados, ambos sem SSE/retry e com refresh/prova externa.
- [ ] Deployment fica Active com fiscal gate fechada: somente 503/header exato é esperado até local178 s e contado separado; a abertura deve concluir antes desse instante ou o abort deve estar iniciado até real180 s sob observador/control saudáveis. Recovery visível permanece sob RTO10 condicionado; demais falhas, gap do observador, mudança do fingerprint ou expiry abortam. API compartilhada sem metadata, Date/response-time, skew/RTT/background estendendo lease, render sem revalidação, geração antiga, provider/200 precoce, restart estendendo deadline ou stale além de requestStart+5 s abortam.
- [ ] Runner externo falha antes de changeset/merge: abortar antes de `REC-2A`. Se falhar inesperadamente pós-merge, manter treatments quiescidos, registrar breach do RTO e reassessment; nunca completar Rollback por inferência local.
- [ ] Candidato reinicia após rollback iniciado: novo boot nasce fechado, não obtém fence enquanto o anterior o retém e é re-quiescido/reprovado no polling <=1 s antes de permitir conclusão.
- [ ] Rotação HMAC remota aparece no changeset Stage: remover; rotação operacional exige TODO/janela/aprovação próprios.
- [ ] Lint com `--fix` altera a tree: invalidar o checkpoint e repetir toda validação antes de novo freeze.

### Residual Unknowns / Risks

- [ ] **Assumption:** os budgets `10 s/4/15/60` cabem na quota. **Unknown:** quota real Smart Notas até probe/carga. **Confidence:** `Low`. **Handling:** 429 threshold aborta; aumento exige nova aprovação.
- [ ] **Assumption:** nenhum consumidor externo depende de sucesso em `/eventos`. **Unknown:** integrações fora do repositório até attestation do Owner. **Confidence:** `Low`. **Handling:** bloqueia deploy ou exige aceite explícito de hard cut.
- [ ] **Assumption:** o changeset staged e a deployment corrente correspondem ao alvo confirmado. **Unknown:** configuração/revision servidas até inspeção da janela. **Confidence:** `Medium`. **Handling:** bloquear antes do merge se divergir.
- [ ] **Assumption:** após o switch, o antigo deployment ID oferece `Rollback`. **Unknown:** visibilidade/elegibilidade do alvo exato até ele virar previous deployment. **Confidence:** `Medium`. **Handling:** verificar antes do smoke amplo; ausência aborta ou exige risco/RTO renovados.
- [ ] **Assumption:** a source tree validada produz um runtime aceitável. **Unknown:** bits exatos do rebuild com base/apt mutáveis. **Confidence:** `Medium`. **Handling:** readiness e smoke dos bits remotos são obrigatórios; não alegar OCI idêntico.
- [ ] **Assumption:** o dataset representativo reproduz seletividade/custo atual dos logs. **Unknown:** estatísticas reais do Stage sem capturar dados. **Confidence:** `Medium`. **Handling:** registrar cardinalidade/razão inelegível e revalidar p95/planos com evidência redatada antes do merge; falha abre TODO próprio.
- [ ] **Assumption:** o binding PostgreSQL é direto/session-affine, exclusivo e permite `pg_stat_activity`/`pg_locks`. **Unknown:** fatos efetivos até probe redatado pré-APROVADO. **Confidence:** `Low`. **Handling:** prova obrigatória em D-CUT-32 e repetida antes de `REC-2A`; multiplexing/ACL/visibilidade inconclusivos encerram/bloqueiam.
- [ ] **Assumption:** o runner preflighted permanecerá disponível durante toda a janela. **Unknown:** falha inesperada depois do merge. **Confidence:** `Medium`. **Handling:** health do runner durante a janela; perda pré-merge aborta, perda pós-merge mantém fail-closed e registra breach explícito do objetivo de 10 min.
- [ ] **Assumption:** o limite efetivo legado `L` e settings são comprováveis sem segredo. **Unknown:** pool default/headroom. **Confidence:** `Low`. **Handling:** resolver em preflight read-only antes de solicitar APROVADO; sem fonte autoritativa, hard stop imediato, TODO cap4 próprio e rebaseline total antes de retomar.
- [ ] **Assumption:** Owner consegue executar `Remove` no candidato e runner permanece disponível quando controls falham. **Unknown:** permissão/ação efetiva até preflight. **Confidence:** `Low`. **Handling:** atestar sem executar antes do merge; ausência bloqueia; pós-merge inconclusivo é breach fail-closed.
- [ ] **Assumption:** revogação de usuário em até 35 s é aceitável quando toda emissão/CAS que cruza o deadline exige nova prova e stream fecha no remaining validity. **Unknown:** necessidade operacional de revogação imediata. **Confidence:** `Medium`. **Handling:** aprovação final explícita; se rejeitada, redesenhar estado fiscal com revalidação por request/evento e rebaseline.
- [ ] **Assumption:** limites global/database/role, associação process→role/database e budgets disjuntos de outras classes são observáveis/autoritativos. **Unknown:** `datconnlimit`, `rolconnlimit`, Xd/Xr e consumers externos até preflight. **Confidence:** `Low`. **Handling:** qualquer classe/role/database/budget desconhecido bloqueia; validar cada cap finito separadamente e nunca contar participantes modelados em O*.
- [ ] **Assumption:** heartbeat fiscal visível detectará restart dentro do deadline monotônico máximo de 5 s contado antes do último handshake. **Unknown:** restart pode ocorrer imediatamente após uma resposta aberta. **Confidence:** `Medium`. **Handling:** enter/focus/resume suprime; render-time monotonic expiry impede skew/RTT/background de estender; o residual <=5 s desde request start precisa de aceite final.
- [ ] **Assumption:** ambos os contextos possuem nota autorizada para o detalhe do probe. **Unknown:** contexto vazio no dia do corte. **Confidence:** `Low`. **Handling:** barreira fiscal permanece fechada/503 até amostra disponível ou novo aceite operacional específico; nunca reduzir a prova silenciosamente.

## Security Risk Assessment

- **Risk level:** `high`
- **Why this risk level:** dois tokens fiscais, CNPJs, HMAC, dados autenticados e configuração de produção.
- **Attack surface in scope:** secret store, logs/ingress, probes, binding, fiscal cache/stale responses, noteId/refId, monitor token, Bearer/SSE, CSV, deploy output e rollback.
- **Attack simulation decision:** `required before Stage cutover`
- **Required result:** nenhum dado fiscal além dos bounds aceitos (lease5/revogação35), nenhuma serialização/evento/CAS após identity deadline sem nova prova, vazamento/query credential, JWT em URL/log, spreadsheet formula, input fora de bound, cross-context, SSRF/redirect ou noteId inválido; após os bounds, usuário inativo vê zero.
- **Current status:** `pending`.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `high`
- **Why this level:** cada réplica multiplica concorrência/rate contra API externa; payload aceito pode chegar a 2 MiB; tratamento unitário/lote e realtime alteram uma superfície de escrita sobreposta.
- **Current delivery stage at review time:** `Pending, Provisional, review`

| Policy Schema Version | Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Trigger Rationale | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code | Recorded At UTC | Executor ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `pcv-1` | `EPS` | `endpoint-performance-scrutiny` | `required` | `high` | `EPS-QUERY-SHAPE-CHANGED` | listas/agregações/export/detalhe/history/payload/monitor/eligibility mudam; paths fiscais externos permanecem materiais | `before_local_implemented` | `EPS-E2` | `pending` | seletividade real de Stage e quota Smart Notas permanecem desconhecidas | `none` | `2026-09-28T04:01:17Z` | `codex-primary` |
| `pcv-1` | `FRC` | `frontend-race-condition-validation` | `required` | `high` | `FRC-STALE-RESPONSE` | troca de contexto/cache, metadata/header, deadline monotônico, skew/RTT/background, restart, stale promises, SSE e logout se sobrepõem | `before_local_implemented` | `FRC-E3` | `pending` | cache fresco→handshake/deadline/render/restart e navegador Stage ainda não foram provados | `none` | `2026-09-28T04:01:17Z` | `codex-primary` |
| `pcv-1` | `BCI` | `backend-concurrency-idempotency-validation` | `required` | `high` | `BCI-LOST-UPDATE-RISK` | writers podem conflitar; caps global/database/role podem saturar; opener advisory pode reentrar | `before_local_implemented` | `BCI-E3` | `pending` | G/D/R/Og/Od/Or/L, idle>300, owner/depth1 e dois commit-uncertain não provados | `none` | `2026-09-28T04:01:17Z` | `codex-primary` |
| `pcv-1` | `RLS` | `runtime-load-stress-validation` | `required` | `high` | `RLS-SLO-CLAIM` | há SLOs para payload/bulk/SSE, provider budgets e readiness flood1000/c100 com recuperação de memória | `before_local_implemented` | `RLS-E3` | `pending` | quota real e pressão do OCI Railway permanecem até probe/observação | `none` | `2026-09-28T04:01:17Z` | `codex-primary` |

### EPS planned evidence

- **Access-pattern classification:** `bounded-list|aggregation|exact-lookup|correlated-history|monitoring|mutation`; o predicado original-`ERRO` entra antes de count/group/order/limit/mutation; detalhe/payload são lookups diretos e history200 não pode scanear por linha.
- **Evidence contract:** `EPS-SP-STRONG` / `EPS-A2`; touched-path audit, anti-pattern audit, planos `EXPLAIN` JSON redatados e benchmarks separados de `VAL-CUT-17` em `foundation_documentation/artifacts/tmp/uninotas-cutover-pcv/eps-pcv1.json`.

### FRC planned evidence

- **Concurrency policies:** `cancel previous` para troca de contexto/lista; geração handshake/lease fiscal governa render, deadline `performance.now()` ancora no request start, metadata/header invalida e resposta antiga não repopula; `drop duplicate` para submit; fixed-window 250 ms; cancelamento no logout/unmount.
- **Evidence contract:** `FRC-SP-H` / `FRC-A1`; runner determinístico em skew ±, RTT1 s, background timer, render após expiry, resposta velha cruzando restart, SSE remaining-deadline/logout, bursts 5/10/20, troca rápida/out-of-order/lifecycle e lote500 em `foundation_documentation/artifacts/tmp/uninotas-cutover-pcv/frc-pcv1.json`.

### BCI planned evidence

- **Invariant ID:** `CUT-TREATMENT-SERIAL-APPEND-01` — para cada ref elegível, todo comando aceito persiste exatamente um append monotônico sob lock; nenhum inelegível, retry incerto ou writer cross-version simultâneo ocorre; lote é atômico; SSE não antecede commit nem excede um sinal por append no processo.
- **Concurrency policy:** `serialize` por writer pool1/locks. Prisma6.19.3; candidato C=6; control pool/connect/socket1 s e statement200 ms one-statement; matriz disjunta com inequalities global/database/role. Writer idle0/heartbeat, owner/depth1, transaction budgets e two commit-uncertain permanecem.
- **Evidence contract:** `BCI-SP-H` / `BCI-A1`; pre-implementation capacity fingerprint e repeat pre-merge; PATCH/lote, transition old/candidate/runner, role/database/Xd/Xr/G/D/R/O*/margens/inequalities, hard-stop L desconhecido; sampler250/deadline1000/snapshot500, inspection+DB-drop, flood1000/c100, liveness250/orphan-zero2s; idle>300, open/open, fiscal quiesce/REC-3A/3B/3C, fingerprint control-plane contínuo e two uncertain outcomes. Registrar connections/locks/PIDs/owners/status no JSON.

### RLS planned evidence

- **Workload model:** `RLS-SP-H` com load/stress/recovery sobre stub loopback, budgets `10 s/4/15/60`, payload near-2MiB, bulk500, stream e readiness flood1000/c100; nenhuma carga destrutiva alcança Smart Notas/Stage.
- **Evidence contract:** `RLS-A1`; thresholds/métricas de `VAL-CUT-05`, incluindo p50/p95/p99, throughput, status, RSS/heap, saturação e recovery em `foundation_documentation/artifacts/tmp/uninotas-cutover-pcv/rls-pcv1.json`.

### Common `pcv-1` artifact rule

- Cada lane em `running|passed` deve registrar no TODO o evidence object completo. O JSON machine-checkable inclui todos os campos obrigatórios do `pcv-1`; `artifact_sha256` é SHA-256 da serialização JSON UTF-8 com chaves recursivamente ordenadas, arrays preservados e sem whitespace, excluindo o próprio campo durante o cálculo. Evidência somente em prosa ou somente por status HTTP não satisfaz o gate.

## Audit and Independent Review Gates

- **Audit escalation:** `required; high-risk release and runtime/infra change`.
- **Independent no-context critique:** `required after plan freeze and before APROVADO`.
- **Independent test-quality audit:** `required before Stage cutover`.
- **Independent final review:** `required after implementation and before Stage cutover`.
- **Dedicated triple review:** `required because release-critical + secrets + external provider`.
- **Current status:** `round34 critique blocked with one high finding integrated into round35 candidate; publication/attestation/current reviews and operational preflight pending`.

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
- **Findings summary:** crítica round34 bloqueou com `R34-OPS-01`, integrado no candidato round35 como D-CUT-42/REC-1X. Crítica round35 só ocorrerá após arquitetura corrente limpa; nenhuma autoridade de implementação foi concedida.

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `R21-OPS-BCI-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-CANDIDATE-BOOT-FENCING` | A decisão `D-CUT-24` usa writer pool1 + advisory session fence/PID/pg_locks; idle/loss/no-auto-reacquire entram em `VAL-CUT-21`. |
| `R21-PERF-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-DB-POOL-READINESS-HEADROOM` | A decisão `D-CUT-23` substitui headroom implícito por clients4/1/1 e thresholds mixed-load60 em `VAL-CUT-20`. |
| `R21-OPS-02` | `Integrated` | `useful` | `yes` | `project` | `CUT-EXTERNAL-RUNNER-PREFLIGHT` | runner/ACL/classifier são gate read-only pré-changeset/pré-merge; RTO é condicionado e perda pós-merge vira breach fail-closed. |
| `R21-ADH-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-RECOVERY-EVIDENCE-PHASE-SEPARATION` | A validação `VAL-CUT-08` virou simulação/fatos read-only e `VAL-CUT-22` é evidência real condicional ao abort alcançar REC-3. |
| `R22-OPS-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-DIRECT-STAGE-PRETRAFFIC-CLAIM` | `D-CUT-25` introduz barreira fiscal per-boot: Stage pode ficar Active, mas lista/detalhe retornam 503 e não chamam provider até POST ADMIN provar ambos os contextos. |
| `R22-SEC-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-CSV-FORMULA-PREFIX-COMPLETE` | `D-CUT-21`, contrato CSV, `DOD/VAL-CUT-19/20` incluem LF além dos seis prefixos anteriores. |
| `R22-PERF-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-CONTROL-POOL-BARRIER-READINESS-COEXISTENCE` | `D-CUT-23` libera control após query; `VAL-CUT-20` sobrepõe readiness a abrir/quiescer e falha somente da inspeção com SELECT1 verde, separada de DB-down. |
| `R22-PERF-02` | `Integrated` | `useful` | `yes` | `project` | `CUT-SSE-COALESCER-BOUNDED-STALENESS` | `D-CUT-22` troca trailing debounce por janelas fixas 250 ms; `VAL-CUT-16` prova fluxo 100 ms/5 s sem starvation/paralelismo. |
| `R22-TEST-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-ERROR-QUERY-PERF-SURFACE-COVERAGE` | `VAL-CUT-17` inclui detalhe/history200, payload, monitoramento e eligibility rollback-only com planos/p95. |
| `R26-OPS-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-FISCAL-GATE-REVERSIBILITY` | quiesce fiscal exato/one-way, epoch sync, SIGTERM, frontend invalidation e REC-3A em D-CUT-26/VAL24. |
| `R26-OPS-02` | `Integrated` | `useful` | `yes` | `project` | `CUT-ROLLBACK-OUT-OF-BAND-CONTROL` | REC-3B oficial Remove→Removed→runner zero2s→Rollback e preflight de permissão/ação. |
| `R26-SEC-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-FISCAL-LEASE-AUTH-REVOCATION-BOUND` | cache identidade monotônico30 + lease5, supressão<=35 e teste de desativação/401. |
| `R26-STRUCT-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-PREPARATORY-RELEASE-BOUNDARY` | L desconhecido encerra o TODO; cap4 separado e retorno exige rebaseline total. |
| `R26-PERF-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-PUBLIC-READINESS-ADMISSION` | endpoint snapshot-only, sampler bounded e flood sem DB queue/P2024. |
| `R27-SEC-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-AUTHORIZATION-DEADLINE-COMPOSITION` | D-CUT-30 carrega identity deadline até serialização/evento/CAS, revalida quando necessário e limita stream ao remaining validity. |
| `R27-OPS-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-DIRECT-ACTIVATION-PHASE-SLO` | D-CUT-31 define Active-fiscal-fechada com deadline de abertura e início do abort: local178/real180 não prometem recuperação concluída; assinatura esperada/contador separados cessam no deadline e então recovery/SLO registram o incidente. |
| `R27-STRUCT-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-PREIMPLEMENTATION-CAPACITY-FORK` | D-CUT-32 move prova L/G/D/R/O*/runner/inequalities para antes do APROVADO e repete <=15 min pre-merge. |
| `R28-SEC-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-EXTERNAL-QUIESCE-FRESH-AUTH` | D-CUT-33 separa SIGTERM interno do POST irreversível e exige revalidação sem cache antes do CAS síncrono; falha não muda estado. |
| `R28-OPS-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-ACTIVE-TRANSITION-OBSERVATION-BOUND` | D-CUT-34 inicia observador pré-merge, limita gap a2 s e usa allowance local178 s; perda/reconnect aborta sem reset. |
| `R28-OPS-02` | `Integrated` | `useful` | `yes` | `project` | `CUT-ROLLBACK-SOURCE-STABILIZATION` | D-CUT-35 desliga Auto-deploy após trigger, mantém off em abort e cria REC-4 com source segura em <=24 h. |
| `R28-GOV-01` | `Integrated` | `useful` | `yes` | `paced` | `CUT-CURRENT-ROUND-EVIDENCE-BINDING` | D-CUT-36 exige round/refs exatos e reset de crítica/coerência/drift quando o material evolui. |
| `R32-OPS-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-OBSERVED-DEADLINE-VS-RECOVERY-BOUND` | D-CUT-31/34 declaram 178/180 como abort-initiation; 503 deixa de ser expected no deadline e recovery usa RTO10 condicionado. |
| `R32-OPS-02` | `Integrated` | `useful` | `yes` | `project` | `CUT-CONTROL-PLANE-EXCLUSIVE-FREEZE` | D-CUT-38 congela/polla replica1, região, source, vars, teardown, health, approvals/deployments e classifica mudança manual/platform como candidato inesperado. |
| `R32-OPS-03` | `Integrated; refined by R33-ARCH-OPS-02` | `useful` | `yes` | `project` | `CUT-POST-ROLLBACK-CONVERGENCE` | D-CUT-39/40 e REC-3C exigem prior image+vars/revision Active, probe baseline-specific, fingerprints/config trail e candidate-zero antes de REC-4. |
| `R32-GOV-01` | `Integrated` | `useful` | `yes` | `paced` | `CUT-GATE-CAUSAL-BINDING` | scope drift/coherence permanecem not_run até arquitetura/crítica round35 limpas; evidência final vincula refs e dispatches correntes. |
| `R34-OPS-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-PREMERGE-UNEXPECTED-CANDIDATE-RECOVERY` | D-CUT-42 inicia classificação na primeira mutação; REC-1 exige runtime imutável/zero, REC-1X terminaliza never-Active ou remove/rollback/REC-3C Active, e REC-4 só ocorre quando main mudou. |

- **Evidence / reference:** crítica round34 `/tmp/uninotas-cutover-round34-critique.3Klw6p/dispatch.json`, SHA-256 `17f372ecb9b3c740107d90a5e2daad183e2e5bac9c3a84538d6259f2b2f5cb91`, assessment blocked; crítica round35 pendente; históricos preservados; fingerprint `453bba9462e3`.
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
- **Gate status:** `not_run`
- **Evidence / reference:** rounds anteriores são históricos; rerodar somente após arquitetura/crítica round35 limpas e vincular `reviewRound=35`, refs exatas e digest/path dos dispatches correntes.

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
| `delphi-ai/skills/rule-railway-railway-deployment-contract-always-on/SKILL.md` | deploy | vars/health/rollback, fingerprint control-plane e ação out-of-band `Remove` | produção sem evidence, ação fora do operador/state machine ou Rollback antes de Removed+zeros | staged config + REC-3A/3B/3C + freeze D-CUT-38 |
| `delphi-ai/skills/wf-railway-change-service-deployment-contract-method/SKILL.md` | mudança de readiness/vars/release Railway | target/revision/order/rollback, runner e permissão `Remove` atestados | inferir estado remoto por arquivos locais ou executar drill destrutivo | re-resolve antes da mutação |
| `delphi-ai/skills/rule-prisma-prisma-schema-migration-always-on/SKILL.md` | três clients, transactions e pool contract Prisma 6.19.3 | versão exata/lockfile, geração e URL seguras | caret, latest tooling ou pool implícito | schema permanece fora; harness prova sessão/PID/idle |
| `delphi-ai/skills/wf-prisma-change-schema-migration-contract-method/SKILL.md` | query/transaction/pool boundary muda sem schema | scripts/version owner e client state coerentes | db push/migration inventada | nenhum DDL; `prisma generate`/tests no CI |
| `delphi-ai/skills/rule-postgresql-postgresql-data-integrity-always-on/SKILL.md` | readiness, logs, locks e recovery | bounded queries; G/D/R/Og/Od/Or; inspection-fail distinto de DB-down | schema/fence/caps/readiness falsos | schema fora; BCI/transitional budget obrigatórios |
| `delphi-ai/skills/wf-postgresql-change-relational-contract-method/SKILL.md` | lock/session/pool/recovery contract muda | key/PID/pg_locks, roles/ACL e session-affinity testados | assumir snapshot como fence | BCI + runner preflight obrigatórios |
| `delphi-ai/skills/rule-nestjs-nestjs-architecture-always-on/SKILL.md` | readiness, auth e gates operacionais | handler snapshot-only, sampler bounded, cache monotônico e quiesce sync | query DB por probe público, restart storm ou stale opener | review health/auth/runtime boundaries |
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
- `approval final também aceita topologia PostgreSQL read4/writer1/control1 (máximo seis por processo candidato), mutation gate1, advisory session fence verificado por PID/pg_locks e objetivo de rollback de 10 minutos condicionado ao runner preflighted; perda pós-merge é breach fail-closed.`
- `approval final aceita que C=6 é teto por candidato e exige matriz/inequalities; sem L autoritativo, este TODO para e cap4 exige TODO/promoção próprios, seguido de rebaseline completo.`
- `approval final aceita 503 temporária após Active/restart e cache armazenado, mas visível só sob handshake do boot atual com deadline monotônico requestStart+5 s; skew/RTT/timer background não estendem, todo render revalida, heartbeat3/timeout1 e geração/header invalidam; contexto sem nota mantém fechado.`
- `approval final aceita cache de identidade monotônico30 s + lease5 s, logo desativação pode manter fiscal visível por até35 s; resposta/stream/CAS que cruza deadline exige nova prova, SSE fecha no remaining validity, e mudança de perfil entre setores não revoga leitura porque todos os setores ativos são viewers.`
- `approval final aceita que Active-fiscal-fechada deve abrir antes de local178 s ou iniciar abort até real180 s sob observador/control saudáveis; isso não promete recuperação visível em 180 s. Após local178, 503/header deixa de ser esperado e entra no incidente governado pelo RTO10 condicionado; gap/reconnect/control loss/expiry/outro erro aborta sem reset, restart pós-open só recebe allowance quando explicitamente esperado no fingerprint e o segundo aborta.`
- `approval final aceita freeze contínuo do runtime/control plane Railway com uma réplica, região/source/health/approvals/deployments fingerprintados de forma redatada e operador único; scale, restart, Redeploy, Deploy Latest, Rollback, approval ou mudança manual/platform fora da state machine vira candidato inesperado e aborta.`
- `approval final aceita separar runtime e configuração: runtime/deployments são polled continuamente; configuração só avança com changeset de dez chaves, zero staged changes e cursor/eventos esperados da activity feed em cada transição. Evento value-only inesperado aborta; nenhuma hash/value de segredo é persistida e, sem trilha conclusiva no plano Pro, o cutover não começa.`
- `nenhuma aprovação de implementação será solicitada antes do preflight read-only autoritativo de L/G/D/R/O*/runner/inequalities; inconclusivo encerra este TODO no ramo cap4.`
- `approval final aceita readiness snapshot-only: sampler250/single-flight/deadline1000, success age500, handler p95<=100 ms; flood/compound expiram fail-closed, liveness<=250 e orphan-zero2s.`
- `approval final aceita recovery 3B com downtime: se APIs candidatas falharem, operador usa Railway Remove, aguarda Removed+runner zero estável2 s e somente então Rollback; ausência de prova interrompe recovery.`
- `approval final aceita que qualquer Rollback de REC-3A/3B entra em REC-3C e só encerra runtime recovery após correlacionar o prior deployment exato ao Active resultante, provar image+variables/revision esperados, repetir o probe real congelado do prior (/saude body ok/ok, auth/read legado e SELECT1 externo), manter fingerprints/config trail íntegros e candidatos/transactions/fences zero estável2 s; /prontidao não é exigida da imagem anterior e ausência ou total acima de10 min é breach. REC-4 segue somente se main mudou.`
- `approval final aceita que a classificação de candidatos começa no commit do changeset: REC-1 só restaura config com runtime continuamente inalterado e zero2s; qualquer trigger/revision pré-merge usa REC-1X, terminaliza never-Active ou remove todo Active e passa por Rollback/REC-3C. Como main não mudou, REC-1/1X encerram sem REC-4.`
- `approval final aceita que quiesce HTTP irreversível exige identidade ativa+ADMIN revalidada sem cache antes do CAS; se auth estiver indisponível, REC-3B substitui o controle HTTP, enquanto SIGTERM interno permanece fail-closed.`
- `approval final aceita desligar Auto-deploy após registrar o trigger pós-merge, mantê-lo off em rollback pós-merge e estabilizar main em até24 h via REC-4 antes de reativar; runtime recovery de10 min continua separado. Recovery pré-merge não usa REC-4 porque main permanece igual.`
- `antes do deploy, o Owner deve atestar se existe consumidor externo de sucesso em /eventos/logs; se existir ou permanecer desconhecido, o deploy fica bloqueado até coordenação ou novo aceite explícito de hard cut.`
- `approval final também aceita o gitlink MonitorNotes intencionalmente atrás da Foundation pós-cutover até o próximo product release aprovado, evitando segundo auto-deploy documental.`

## Early Approval Signal

- **Received:** `Aprovado`, em 2026-09-27, incluindo autorização contextual para os checkpoints Git propostos.
- **Accepted decisions:** `D-CUT-07`, avanço do cutover e commit/push do candidato para revisão.
- **Authority effect:** `checkpoint Git concluído`; não autoriza deploy, alteração de variáveis Railway nem tráfego fiscal.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Reason:** contrato e checkpoint publicados; revisões e gates operacionais ainda precedem qualquer implementação remota/deploy.
