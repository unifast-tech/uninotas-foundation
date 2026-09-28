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
- **Next exact step:** concluir a attestation metadata-only do material round 22 e repetir arquitetura + crítica independente; nenhuma mutação Railway está autorizada.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** a topologia customer-facing e o baseline Git estão confirmados; a revisão arquitetural formal é o gate corrente.
- **Exit condition:** fatos remotos confirmados, decisões `D-CUT-06..24` congeladas, revisão pré-aprovação limpa e `todo_authority_guard.py --pre-approval` em `preflight-go`.

## Provisional Notes

- **Missing for production-ready:** implementação reconvergida, configuração remota, probes reais, carga local do build candidato, attestation do rollback target, rebuild/cutover/smoke no Stage e promoção Foundation.
- **Revisit criteria:** concluir `DOD-CUT-01..22` com evidência redatada da deployment exata.
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
- [ ] `CUT-07` Antes do changeset/merge, registrar deployment/plano/snapshot/Owner/capacidade de rollback e provar o runner externo direto/session-affine no target. Abort segue `REC-0/1/2A/2B/3`; active usa `Rollback` no ID anterior exato. O objetivo de 10 min só vale com preconditions comprovadas; ausência pré-merge aborta, perda pós-merge é breach fail-closed, e `Redeploy` exige risco/RTO renovados. A flag é apenas kill switch.
- [ ] `CUT-08` Executar um único cutover direto no `Stage` customer-facing entre 20:00–22:00, observar por no mínimo 30 minutos e abortar pelos thresholds congelados.
- [ ] `CUT-09` Validar rotação HMAC somente em teste local determinístico com chaves efêmeras: após substituição, `noteId` anterior falha fechado e a relistagem produz IDs válidos. Rotação de segredo no `Stage` é uma mudança operacional separada, fora deste cutover.
- [ ] `CUT-10` Promover atomicamente `note_read_model` para Smart Notas nos módulos/ledger somente após smoke e rollback aprovados.
- [ ] `CUT-11` Tornar PostgreSQL `logs` exclusivamente uma fonte de erros Routerfy/n8n: um predicado SQL canônico pela classificação original `ERRO` entra antes de `COUNT`, agrupamento, ordenação, paginação/limite e mutations em lista, resumo, produtos, exportação, detalhe, payload, histórico correlacionado, tratamento unitário/lote e monitoramento. Um espelho TypeScript é só defesa secundária. Tratamento/reabertura `PENDENTE` de erro original continua elegível; classificação original `PENDENTE`/`SUCESSO` não. Inventário externo é gate antes do deploy.
- [ ] `CUT-12` Propagar um único correlation ID do request autenticado até o adapter Smart Notas, limitar `actorId` a identificador interno pseudônimo e atualizar `DEPLOY.md` com ordem atômica de variáveis/readiness/deploy/rollback.
- [ ] `CUT-13` Promover por PR apenas uma tree Git equivalente ao candidato validado; registrar candidate SHA/tree OID, final main SHA/tree OID e revision Railway. A imagem local é evidência source-level, não o OCI implantado; mismatch de tree bloqueia/aborta, e o primeiro smoke Stage valida os bits do rebuild remoto.
- [ ] `CUT-14` Manter `uninotas-foundation:main` como autoridade independente após a promoção canônica; não sincronizar o gitlink documental em `MonitorNotes:main` neste closeout para evitar segundo auto-deploy. Registrar follow-up para o próximo release aprovado.
- [ ] `CUT-15` Antes do merge, migrar/atestar o consumidor UptimeRobot para `x-monitor-token` na release corrente sem rotacionar token; se o token não estiver configurado, atestar modo público. Consumidor/configuração desconhecidos bloqueiam o corte.
- [ ] `CUT-16` Endurecer export CSV e inputs legados: neutralizar fórmulas em todo texto externo, limitar `refId` a 1..64 após trim e token de monitoramento a 1..200, e coalescer bursts de tratamentos realtime no frontend.
- [ ] `CUT-17` Serializar tratamentos concorrentes por `refId` no PostgreSQL, com topologia Prisma `read=4`, `writer/fence=1`, `control/readiness=1`, todos com wait `2 s` e teto total `6` na única réplica; lock namespaced, ordem lexical binária, timestamp monotônico pós-lock, `ReadCommitted`, budgets `2 s/15 s/1,5 s/12 s`, um writer/500 locks, retry só após rollback comprovado, 409/503 estáveis e SSE pós-commit. Validar sobreposição, lote 500 e carga mista sem alegar três conexões implicitamente reservadas.
- [ ] `CUT-18` Tornar o cutover cross-version fail-closed para tratamentos: overlap `0`/drain `20`; cada boot UUID nasce fechado e timer/abrir usam epoch-CAS. Abertura exige anterior terminal, datasource direto/session-affine, fence advisory session-level exclusivo no client writer de uma conexão e contagens separadas sem candidata anterior/não candidata. Toda transação valida PID/lock do fence antes de escrever; perder/recriar sessão nunca reacquire automaticamente. Lease local é liberada exact-once no settle Prisma; commit incerto continua cercado pela mesma sessão/lock DB. Runner externo é comprovado antes do changeset/merge e, pós-switch, distingue zero candidata de sessões legítimas do legado.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `MonitorNotes:delphi-and-foundation`; `uninotas-foundation:main` (canonical main-only documentation authority)
- **Promotion lane path:** `delphi-and-foundation candidate tree -> local source/build validation -> PR with identical final tree on main -> Railway remote rebuild -> single Stage customer-facing cutover -> independent Foundation runtime promotion`
- **Lane-promoted threshold for this TODO:** `main com checkpoint aprovado e CI-equivalent verde`
- **Production-ready threshold for this TODO:** `Stage customer-facing com smoke e 30 minutos de observação; rollback target atestado e, se acionado, restaurado em até 10 minutos; promoção Foundation concluída`
- **Execution topology:** `principal checkout, single code writer; worktrees/auxiliary checkouts forbidden`

## Promotion Evidence

| Scope Item | Local Branch/Commit | Main / Authority | Local Source/Build Validation | Single Remote Target: Stage Customer-Facing | Current Status |
| --- | --- | --- | --- | --- | --- |
| Backend + frontend read-only | round-22 material root `9269d9fccca7c9f1628741ba390644b5e0d18fa8`; code-origin `31712a0`; attestation carrier pending | `pending promotion to main` | `pending final cutover suite` | `pending one direct cutover` | `round-22 material frozen; metadata attestation pending` |
| Foundation cutover contract | round-22 material `3cbfac6cb5bdcdf0a342eb74fa8994b8dd6c76ba`; attestation pending | `main-only authority` | `n/a` | `pending runtime promotion after observed cutover` | `round-22 material frozen; metadata attestation pending` |

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
| `D-CUT-21` | Todo `refId` de path/lote é trimado, deve ter 1..64 caracteres e falha 400 se branco/oversize; só ref válido inexistente/inelegível retorna 404. `MONITORAMENTO_TOKEN` configurado e header oferecido devem ter 1..200 caracteres; config fora do bound falha startup e header fora do bound retorna 400. Export CSV prefixa `'` em todo scalar textual externo cujo primeiro caractere seja `=`, `+`, `-`, `@`, TAB ou CR antes do escaping CSV. | Alinha varchar persistido, limita inputs e neutraliza spreadsheet formula injection. | `frozen; approval-material` |
| `D-CUT-22` | O consumidor React coalesce eventos `evento.tratado` em janela trailing de 250 ms: qualquer burst produz no máximo um refetch de lista e um de resumo por janela, mantendo o refetch idempotente. Um lote síncrono de 500 refs deve produzir exatamente um par de invalidações após aquietar. | Evita tempestade de até 1.000 requests por tratamento em lote sem alterar o contrato SSE. | `frozen; approval-material` |
| `D-CUT-23` | Tratamentos unitário/lote usam política `serialize`. Três Prisma clients derivados por URL API segura, sem logar valor, fixam: read/auth/logs `connection_limit=4,pool_timeout=2`; writer/fence `1/2`; control/readiness/barrier `1/2`; teto agregado `6` na única réplica. Read capacity é compartilhada, não uma reserva implícita. Só o writer executa treatment, portanto gate process-local fail-fast `1` e no máximo `500` locks por lote. Após trim/validação/deduplicação, refs seguem ordem lexical binária; transaction `ReadCommitted` (`maxWait=2 s`,`timeout=15 s`) primeiro valida o fence de `D-CUT-24`, então aplica `lock_timeout=1500ms`, `statement_timeout=12000ms`, locks `hashtextextended('uninotas:treatment:' || refId,0)`, revalida eligibility e grava `criado_em=GREATEST(clock_timestamp(),MAX(criado_em)+1us)`; situação usa `criado_em DESC,id DESC`. Um retry integral após `25 ms` só para `40P01|40001|55P03|P2034` com abort provado; `P2024|P2028|57014`, conexão/fence perdida ou commit incerto nunca repetem. Conflito esgotado 409; capacity/timeout/incerto 503 + `Retry-After: 1`/refresh. SSE somente após resolve, uma vez por append. Carga mista por 60 s mantém <=6 conexões, 60/60 probes control 2xx com p95 <=500 ms, zero `P2024`, reads p95 <=3 s e nenhum PID/fence gap; mudança de réplica/pools/gate exige rebaseline. | Isola fisicamente writer e readiness, remove a falsa reserva de três conexões e preserva serialização/causalidade sem novo schema. | `frozen; approval-material` |
| `D-CUT-24` | `railway.json` usa overlap `0`/drain `20`. Cada boot nasce fechado; primeiro request autenticado arma uma vez 30 s e timer/abrir usam CAS `{bootId,epoch,state}`; quiesce/SIGTERM incrementam epoch antes de await. `RuntimeIdentityService` gera UUID v4 lowercase. Clients session-affine usam nomes exatos base `uninotas:<uuid>` (45), `:writer` (52), `:control` (53) e transaction-local `:treatment` (55); startup/current_setting e reversão devem coincidir, multiplexing/identidade incerta bloqueiam. O writer de uma conexão adquire por `pg_try_advisory_lock(int,int)` um par fixo namespaced global e registra seu `pg_backend_pid`; falha mantém fechado. A sessão conserva o lock quando o pool fica ocioso. Toda transaction writer, antes de qualquer domínio, exige mesmo PID e row `pg_locks` granted para o par; sessão recriada, PID/lock divergente ou unlock inesperado quiesce localmente e retorna 503 sem write/retry. Assim boot antigo ocioso continua cercado; se a sessão cai, lock e transaction vivem/morrem juntos no servidor, novo boot não adquire até liberação, e o antigo nunca reacquire automaticamente. O control classifica `pg_stat_activity` do mesmo DB/user, exclui PID inspetor e não expõe UUID: base/writer/control/treatment permitidos; sufixo desconhecido falha prova; retorna as cinco contagens públicas atual/treatment-atual/não-atual/treatment-não-atual/não-candidata. `abrir` captura estado, prova prazo/anterior terminal/runner pré-validado e, mantendo o fence writer, exige treatment atual, candidata não atual e não candidata zero; depois de await, stale/quiesced vence com 409, senão DB-503/count-409 ou abre. Se CAS final falha, unlock só pelo mesmo PID e estado continua fechado. Cada PATCH/lote adquire lease local antes do primeiro await; release idempotente exact-once ocorre no settle Prisma, resolve publica depois e reject incerto não publica/retry. Quiesce fecha sync, drena lease/transaction, desbloqueia o fence pelo mesmo PID exatamente uma vez; unlock inconclusivo bloqueia sucessor até prova DB. Rollback rastreia boots, exige anteriores terminal/removidos ou quiesced+drained, current zeros e fence liberado; pós-switch runner externo pré-comprovado permite não candidata >0 só com legado exato `Active` e exige toda candidata/lock/transaction zero até remoção. Nenhuma variável/chave ou schema é adicionada. | O session fence persistente fecha o intervalo entre snapshots e impede boot ocioso/reiniciado de voltar a escrever; a prova externa continua separando legado de candidato. | `frozen; approval-material; Config as Code válido no corte e requer migração IaC antes de 2026-12-01` |

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
| Recovery action | state machine `REC-0/1/2A/2B/3`; runner preflighted; config restore só após terminal não ativo; active força stored-image rollback; `Redeploy` degradado | IDs/status, local simulation, config snapshot, runner/fence proof e conditional real-abort evidence | `10 min objective after preconditions; pre-merge inability aborts; post-merge loss is explicit breach` |
| External `/eventos` consumers | inventariar integrações fora deste repositório e obter attestation do Owner antes do deploy | lista redatada/declaração do Owner | `required pre-deploy; unknown consumer blocks deploy unless hard-cut risk is explicitly reapproved` |
| UptimeRobot auth migration | atestar token public/configured; se configured, migrar current monitor para `x-monitor-token` e limpar URL antes do merge | presença/bound redatados + current-release 200/401/URL proof | `required pre-merge; unknown or query-token consumer blocks cutover` |
| Treatment concurrency envelope | clients Prisma read `4/2 s`, writer `1/2 s`, control `1/2 s`; total `6`; `ReadCommitted`; transaction `15 s`; PG lock/statement `1,5 s/12 s`; gate `1`, max `500` locks; retry `25 ms` só após rollback provado | BCI held-lock/batch500/saturation/error map + 60 s mixed load com 60 readiness probes, p95 control <=500 ms, reads <=3 s, zero P2024/fence gap | `frozen; change requires rebaseline` |
| PostgreSQL barrier connectivity | runtime datasource direto ou pooler session-affine; proibir transaction/statement multiplexing e credencial compartilhada | binding/endpoint/mode Railway redatados + teste de sessão/`application_name` em duas conexões; valores nunca impressos | `required before activation; unknown/multiplexed blocks` |
| External rollback runner | identidade/ACL, conexão direta/session-affine e classificador exato comprovados read-only antes de changeset/merge e novamente <=15 min antes do merge; runner permanece disponível na janela | probe no mesmo target sem imprimir URL/credencial/UUID; perda pré-merge aborta antes de `REC-2A`; perda pós-merge é RTO breach fail-closed | `required pre-changeset/pre-merge; unknown/unavailable blocks` |
| Cross-version writer barrier | session-affine; writer pool1 segura advisory session fence global e cada transaction verifica PID/`pg_locks`; timer/open epoch-CAS; cinco contagens; lease exact-once; pre-switch prior terminal/drained + zeros/fence; pós-switch runner externo exige toda candidata/fence zero | config/pooling + idle-old-boot/session-loss/commit-uncertain/restart harness + Stage evidence | `frozen; mismatch, multiplexing, fence loss, candidate session or unknown blocks` |

## Diff Expectation Contract

- **Contract status:** `required; round-22 material baseline frozen by publication; attestation must not alter this field`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree after candidate checkpoint`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | round-21 predecessor material root `94f3d9446a3abbf96e74887ba6430a63eaa5db28`; round-22 material root será registrado no freeze metadata | `committed_diff`; `31712a0` remains code-origin; attestation-only carrier não é implementação |
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
| `MonitorNotes` | `backend/src/common/**` | `M` | propagar correlation ID único até logs/erros |
| `MonitorNotes` | `backend/src/app.module.ts`, `backend/src/operacao/**` | `A|M` | registrar treatment barrier, endpoints ADMIN, boot/quiesce e lifecycle SIGTERM |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M` | bounded probe/capacity/rotation changes |
| `MonitorNotes` | `backend/src/config/**` | `M` | bounded runtime validation |
| `MonitorNotes` | `backend/src/prisma/**` | `M` | clients read/writer/control `4/1/1`, URLs seguras, session fence/PID/lock e readiness isolada sem alterar schema |
| `MonitorNotes` | `backend/src/logs/**` | `M` | tornar `/eventos` error-only, serializar tratamentos por ref e testar bloqueio de sucessos/overlap |
| `MonitorNotes` | `backend/src/monitoramento/**` | `M` | remover sucesso da projeção operacional baseada em logs |
| `MonitorNotes` | `backend/src/realtime/**` | `M` | remover polling/LISTEN/JWT em query e manter stream autenticado somente para tratamentos elegíveis/heartbeat |
| `MonitorNotes` | `backend/package.json` | `M` | remover `pg` do runtime e mantê-lo apenas como dev tooling de `espelhar.ts`; `@types/pg` permanece dev-only |
| `MonitorNotes` | `backend/package-lock.json` | `M` | alinhar lockfile à mudança de `pg` para devDependency sem afetar o runtime Prisma |
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
| `A-CUT-11` | Um runner externo autorizado consegue consultar `pg_stat_activity`/`pg_locks` no mesmo target direto/session-affine sem depender da API candidata. | `backend/src/prisma/prisma.service.ts`, `backend/src/health/health.controller.ts`, `DEPLOY.md`, `foundation_documentation/artifacts/environment-topology.md`; probe read-only ainda pendente | REC-3 não possui prova independente e o merge deve ser abortado | `Low` | `Block` |
| `A-CUT-12` | No Prisma 6.5 fixado, um client `connection_limit=1` conserva a mesma sessão/PID e advisory session lock enquanto o pool fica ocioso; replacement é detectável antes de domínio. | `backend/src/prisma/prisma.service.ts`, `backend/src/prisma/prisma.module.ts`, `backend/package.json`, `backend/package-lock.json`; harness `VAL-CUT-21` pendente | o fence proposto não é confiável e exige novo mecanismo/rebaseline antes da implementação aprovada | `Low` | `Block` |

## Execution Plan

1. Confirmar topologia e obter inventário/attestation do Owner sobre consumidores externos de `/eventos`/`logs` e modo atual do UptimeRobot/`MONITORAMENTO_TOKEN`; consumidor ou monitor mode desconhecido bloqueia deploy.
2. Obter `APROVADO`, carregar regras e implementar na branch de trabalho: budgets fail-closed `10 s/4/15/60`, readiness PostgreSQL-aware, correlation ID, boundary error-only, serialização `D-CUT-23`, barreira cross-version `D-CUT-24` e runbook.
3. Executar testes focados, incluindo BCI 5/10/20, clients Prisma `4/1/1`, mixed load/readiness, session fence idle/loss/PID, lease admission↔quiesce, legacy bloqueado, abertura manual, legacy↔candidate e restart simulado, além de histórico/situação/SSE; revisar o diff e congelar SHA/tree. Nenhum build anterior é evidência de entrega.
4. Sobre essa tree exata, executar CI-equivalent completo e build Docker local como evidência source-level, além de startup/readiness negativo, probes redatados dos dois emissores, lanes `pcv-1` com JSON/hash canônicos, carga near-limit e browser smoke autenticado. Não alegar OCI idêntico ao rebuild Railway.
5. Concluir auditorias delivery-side; rebasear somente se `main` mudou e, nesse caso, invalidar/repetir o checkpoint/validação. Preparar PR cuja tree final prevista seja idêntica à tree validada.
6. Ainda sobre a release corrente, se `MONITORAMENTO_TOKEN` estiver configurado, cadastrar `x-monitor-token` no UptimeRobot, remover token da URL e provar request autorizado 200/503 e request sem header 401; se ausente, atestar modo público. Não rotacionar valor. Falta de acesso/evidência aborta antes do merge.
7. Dentro de 20:00–22:00, criar um único changeset Railway com dez variáveis: cinco valores sensíveis/bindings, quatro budgets exatos e `SMART_NOTAS_READ_ENABLED=true`; revisar presença/escopo sem imprimir valores e usar commit staged sem redeploy. A deployment anterior continua servindo; se atomicidade não for comprovada, abortar antes do merge.
8. Antes de promover `main`, registrar deployment corrente/ID, plano Pro, source/config, snapshot, changeset de dez variáveis sem redeploy, teardown/logs/Owner/migração do monitor e binding PostgreSQL direto/session-affine sem imprimir endpoint/credencial. Provar também runner externo autorizado no mesmo target: identidade/ACL, afinidade, cinco contagens e fence visíveis; repetir <=15 min antes do merge e mantê-lo disponível na janela. Falha, multiplexing ou modo desconhecido abortam antes de `REC-2A`. Não alegar revision candidata/previous target inexistentes.
9. Promover PR para `main`, verificar tree equivalente e entrar em `REC-2A`. Capturar trigger/approval/revision/build; quando ativa, comprovar `overlap=0`, `drain=20`, antigo ID rollbackable e primeiro request/boot iniciando timer 30 s. Quiesce/SIGTERM antes do prazo deve invalidar callback por epoch; a barreira permanece fechada após o prazo até abertura manual.
10. Durante a barreira, validar reads/login e 503. Depois de confirmar anterior terminal/removido, session affinity e runner, ADMIN `abrir` deve adquirir o fence global no writer pool1, registrar PID e exigir treatment atual, candidata não atual e não candidata zero; writer/control/base atuais são permitidos. Forçar stale 409 sobre DB 503; só `aberta` com fence válido autoriza mutation/SSE. Concluir smoke/API/browser/erros/CSV/monitor/correlação/redaction e observar 30 minutos.
11. Em abort, seguir `REC-1`, `REC-2A/2B` ou `REC-3`. Em `REC-3`, quiescer, provar boots anteriores terminal/drenados, zeros pré-switch e fence liberado; boot change reinicia checklist/+2 s. Só então Rollback. O runner preflighted consulta <=1 s: após legado exato `Active`, não candidatas podem existir, mas candidata/transaction/fence permanecem zero até remoção Railway. Evidência real só é coletada se abort alcançar `REC-3`; sem esse estado, `VAL-CUT-22=n/a`. Perda inesperada do runner pós-merge é RTO breach fail-closed. `Redeploy` exige risco/RTO renovados.
12. Após janela verde e inventário externo limpo, promover capabilities/policies/módulos/root docs Foundation atomicamente. Consumidor externo descoberto bloqueia promoção/deploy até coordenação ou novo aceite.
13. Não sincronizar novo Foundation commit em `MonitorNotes:main` neste closeout; registrar pin divergente e follow-up do próximo release de produto.

## Public Error API Contract

Regras comuns: `/eventos/**` e `/realtime/eventos` exigem `Authorization: Bearer` e o guard global que revalida usuário ativo; ausente/inválido/inativo retorna 401. DTO/query inválido ou chave não allowlisted retorna 400. Tratamentos exigem `ADMIN|GESTOR|ANALISTA`; perfil sem permissão retorna 403. Ref original `PENDENTE|SUCESSO` falha como 404 indistinguível de inexistente. Todo erro JSON não-stream preserva o envelope exato `{statusCode:number, erro:string, mensagem:string|string[], caminho:string, timestamp:string ISO}`. Em tratamentos, 409 usa `erro='Conflito'` e `mensagem='Tratamento concorrente; atualize e tente novamente.'`; 503 usa `erro='Serviço indisponível'`, `mensagem='Não foi possível confirmar o tratamento; atualize antes de tentar novamente.'` e `Retry-After: 1`. Nos endpoints operacionais, 503 também usa `erro='Serviço indisponível'` e `Retry-After: 1`, com a mensagem específica congelada em cada row. `LogResumoDto`, `LogDetalheDto`, `ClienteDto`, `VendaDto`, `ProdutorDto`, `TentativaDto` e `CampoPendenteDto` preservam os campos atuais; somente eligibility e conteúdo do histórico mudam.

| Method / path | Frozen request contract | Frozen success contract | Other status / headers |
| --- | --- | --- | --- |
| `GET /eventos` | somente `situacao=TODOS|ERRO|TRATADOS` (default `ERRO`), `busca<=120`, `produto<=200`, `pagina` inteiro >=1 (default 1), `limite` inteiro 1..200 (default 25), `direcao=asc|desc` (default `desc`), `dataInicio/dataFim` ISO; `PENDENTE|SUCESSO` inválidos | 200 `{dados,meta}`; cada item mantém exatamente `refId,eventAt,situacao,situacaoOriginal,mensagem,idSmartNotas,clienteNome,clienteDocumento,produto,valorVenda,meioPagamento,tentativas`; meta mantém `total,pagina,limite,totalPaginas,temProxima`; somente erro original | 400 query/chave inválida; 401 auth |
| `GET /eventos/resumo` | aceita somente `busca<=120`, `produto<=200`, `dataInicio/dataFim` ISO; não aceita nem ignora `situacao,pagina,limite,direcao`; sem defaults além de ausência dos filtros | 200 exatamente `{total,erro,tratados}`; `erro` inclui não tratado/reaberto, `tratados` inclui resolvido/ignorado e `total=erro+tratados` | 400/401 |
| `GET /eventos/produtos` | sem body; eligibility antes de group/order | 200 array `{nome,eventos,erros}` com `eventos==erros`, somente produtos com erro original | 401 |
| `GET /eventos/exportar` | aceita somente `situacao=TODOS|ERRO|TRATADOS` (default `ERRO`), `busca<=120`, `produto<=200`, `dataInicio/dataFim` ISO; rejeita `pagina,limite,direcao`; teto interno fixo 20.000 | 200 CSV UTF-8/BOM com colunas exatas `refId;idTransacao;eventAt;situacao;mensagem;idSmartNotas;clienteNome;clienteDocumento;clienteEmail;produto;codProduto;valorVenda;meioPagamento`, somente erro original; antes de quote/escape, cada scalar textual externo iniciado por `=,+,-,@,TAB,CR` recebe prefixo `'` | `Content-Type: text/csv; charset=utf-8`; `Content-Disposition` sanitizado; 400/401 |
| `GET /eventos/:refId` | path decodificado/trimado deve ter 1..64 caracteres; branco/oversize = 400; ref válida deve ser original-`ERRO` | 200 `LogDetalheDto`: campos de `LogResumoDto` mais `orientacao,origem,cliente,venda,produtor,historico,camposPendentes,payload,resposta`; cada tentativa mantém `em,mensagem,ok,autorNome`, mas histórico contém somente linhas originais `ERRO` | 400 input; 401; 404 ref válida inexistente/inelegível |
| `GET /eventos/:refId/payload` | mesmo bound 1..64/trim; ref elegível original-`ERRO` | 200 exatamente `{enviado,resposta}` | 400 input; 401; 404 válida inexistente/inelegível |
| `PATCH /eventos/:refId/tratamento` | mesmo bound 1..64/trim; body exatamente `{situacao: RESOLVIDO|IGNORADO|PENDENTE, observacao?: string<=1000}`; ref elegível; overlap na mesma ref é serializado por `D-CUT-23` | 200 `LogDetalheDto`; `PENDENTE` reabre para situação efetiva `ERRO`; cada comando aceito gera exatamente um append, sem lost update | 400 input/body; 401/403; 404 válida inexistente/inelegível; 409 após conflito comprovadamente abortado/retry único; 503 + `Retry-After: 1` em gate/pool/timeout/commit incerto, seguido de refresh obrigatório |
| `POST /eventos/tratar-lote` | body `{refIds: string[1..500], situacao, observacao?}`; cada ref é trimada, deve ter 1..64 e ser única após trim; branca/oversize/duplicata rejeita todo lote com 400; mesma enum/regra do unitário; locks de refs em ordem lexical binária | 200 exatamente `{solicitados,aplicados,ignorados}`; `solicitados` é tamanho validado/único; `ignorados` ecoa somente refs válidas não aplicadas, sem distinguir inexistente de inelegível; batch é atômico e não perde append em overlap unitário/lote | 400/401/403; 409 após conflito abortado/retry único; 503 + `Retry-After: 1` em gate/pool/timeout/commit incerto, sem retry cliente antes de refresh |
| `GET /operacao/tratamentos/barreira` | Bearer + perfil `ADMIN`; sem body/query; por ser autenticado pode iniciar a janela mínima, mas nunca abre a barreira | 200 exatamente `{estado,bootId,ativos,liberaEm,sessoesCandidatasAtuais,transacoesTratamentoAtuais,sessoesCandidatasNaoAtuais,transacoesTratamentoNaoAtuais,sessoesNaoCandidatas}`; `bootId` é UUID v4 lowercase canônico; `estado=inicializando|aguardando_abertura|aberta|quiescida`; `liberaEm` é ISO enquanto aguarda ou null após expirar/quiescer; todas as cinco contagens são inteiros >=0 | 401/403; em inspeção DB inconclusiva, 503 com `mensagem='Não foi possível comprovar o estado da barreira; mantenha os tratamentos bloqueados.'` + `Retry-After: 1`; `Cache-Control: no-store`; nunca retorna deployment ID, query text, segredo, UUID de outro boot ou usuário |
| `POST /operacao/tratamentos/abrir` | Bearer + perfil `ADMIN`; query vazia; body exato `{confirmacao:'ABRIR',bootId:UUID v4 lowercase canônico,deploymentAnteriorId:string 1..128,implantacaoAnteriorTerminal:true,postgresSessionAffineConfirmado:true}`; operador só confirma após observar terminal/removido, datasource e runner direto/session-affine | 200 exatamente `{estado:'aberta',bootId,ativos:0,liberaEm:null,sessoesCandidatasAtuais,transacoesTratamentoAtuais:0,sessoesCandidatasNaoAtuais:0,transacoesTratamentoNaoAtuais:0,sessoesNaoCandidatas:0}`; `sessoesCandidatasAtuais` inclui base/writer/control >=0; após 30 s, mesmo boot/epoch/state, fence global adquirido/validado por PID e demais contagens zero; registra audit redatado sem PID/key | 400 formato/body/query; 401/403; após await, stale/quiesced sempre 409 com `erro='Conflito'`, `mensagem='Barreira de tratamento ainda não pode ser aberta.'`, sem `Retry-After`, mesmo se DB falhou; somente captura atual retorna essa 409 por contagem/fence ocupado ou 503 DB/identidade/unlock inconclusivo com `mensagem='Não foi possível comprovar o estado da barreira; mantenha os tratamentos bloqueados.'` + `Retry-After: 1`; `Cache-Control: no-store`; não existe auto-open |
| `POST /operacao/tratamentos/quiescer` | Bearer + perfil `ADMIN`; body exato `{confirmacao:'QUIESCER'}` e query vazia; idempotente no mesmo boot e one-way até process exit; incrementa epoch e fixa estado sincronamente antes do primeiro `await` | 200 exatamente `{estado:'quiescida',bootId,ativos,liberaEm:null,sessoesCandidatasAtuais,transacoesTratamentoAtuais,sessoesCandidatasNaoAtuais,transacoesTratamentoNaoAtuais,sessoesNaoCandidatas}`; todas as contagens são inteiros >=0; sucesso exige lease/transaction drenadas e unlock do fence pelo mesmo PID; registra audit pseudônimo | 400 confirmação/body/query; 401/403; se inspeção/unlock for inconclusivo, estado permanece quiescido e retorna 503 com `mensagem='Barreira quiescida, mas não foi possível comprovar a drenagem; consulte novamente.'` + `Retry-After: 1`; retry é idempotente e rollback/sucessor seguem bloqueados até prova dos zeros/fence; `Cache-Control: no-store`; não existe resume |
| `GET /monitoramento/erros` | `MONITORAMENTO_TOKEN`, se configurado, deve ter 1..200 ou startup falha; aceita somente header `x-monitor-token` 1..200, oversize/branco = 400; query `token` inválida; `minutos` inteiro 1..1440 default 60, `atencao` >=1 default 1, `critico` >=1 default 6, `alertarEm=atencao|critico`; demais chaves rejeitadas | 200 exatamente `{status,cor,erros,pendentes,sucessos,total,ultima_verificacao,janela:{inicio,fim,minutos},limites:{atencao,critico},detalhe}`; `erros=total` conta ativos/reabertos, tratados não contam, `pendentes=0`, `sucessos=0` | `Cache-Control: no-store`; 400 input; 401 token ausente/incorreto quando configurado; 503 banco indisponível ou severidade >= `alertarEm`, mesmo shape |
| `GET /realtime/eventos` | header Bearer obrigatório; nenhum token/query; consumidor usa `fetch` streaming e reconecta após término normal | 200 `text/event-stream`; apenas `evento.tratado` com `refId,situacao,origem='api',em` e `heartbeat` com `origem='sistema',em`; servidor encerra em <=30 s; sem polling/NOTIFY/`evento.novo` | 401 ausente/inválido/inativo a cada conexão; cancelar em logout/unmount; `Cache-Control: no-store`; nenhum JWT em URL/log |

## Recovery State Machine

| State | Trigger / truth | Required recovery | Evidence and maximum RTO |
| --- | --- | --- | --- |
| `REC-0 no-remote-mutation` | qualquer estado de código/checkpoint, publicado ou não, enquanto nenhuma configuração Railway foi commitada | nenhuma recuperação Railway; reverter somente diff/commit do TODO conforme autoridade Git e manter Stage intocado | refs/status/diff classificados; `5 min` |
| `REC-1 staged-config` | changeset de dez chaves foi commitado sem redeploy, mas `main` ainda não foi promovida | restaurar o snapshot redatado anterior via novo staged commit sem redeploy; confirmar deployment corrente inalterada | nomes/escopo antes/depois + mesmo deployment ID; `10 min` |
| `REC-2A post-merge-not-safe` | começa imediatamente após promover `main`, inclusive sem deployment visível, trigger atrasado/rejeitado, awaiting approval, queued/building/deploying | bloquear qualquer restore; impedir/rejeitar approval/trigger quando disponível, ou cancelar deployment visível uma vez; observar serialmente até prova conclusiva de que nenhum candidato pode iniciar/ficar ativo; se active em qualquer instante, ir a `REC-3` | main SHA + trigger/approval/deployment states + ação; decisão em `5 min`; sem prova, recovery falha e exige reassessment humano |
| `REC-2B candidate-conclusively-prevented` | trigger conclusivamente rejeitado/impedido sem deployment possível, ou deployment terminal cancelado/falho e nunca active | somente então restaurar snapshot anterior por staged commit sem redeploy e comprovar mesma deployment verde ativa; não usar `Rollback` | prova do trigger impedido ou status terminal + current deployment ID antes/depois + config redatada restaurada; concluir dentro do RTO total `10 min` |
| `REC-3 candidate-active` | candidato tornou-se ativo e a deployment verde antiga virou previous | confirmar ID antigo e usar o runner preflighted com polling <=1 s. Quiesce invalida timer/opener e fica aplicado em 503. Antes do Rollback, boots anteriores estão terminal/removidos ou quiesced+drained; atual prova `quiescida,ativos=0`, quatro zeros e advisory fence ausente/liberado. Writer session/PID ou boot change reinicia checklist/+2 s. Só então Rollback. Pós-ação, runner prova candidata/transaction/fence zero; somente após legado exato `Active` não candidatas podem ser >0; seguir até Railway remover candidatos | preflight do runner pré-merge + IDs/boots/fence/quiesce/action redatados + testes locais; evidência Railway real somente se abort alcançar REC-3 (`VAL-CUT-22`), senão n/a; objetivo `10 min` condicionado às dependências preflighted; perda pós-merge é breach fail-closed |

Transições não pulam evidência: `REC-1 -> REC-2A` ocorre no merge; `REC-2A -> REC-2B` exige trigger impedido/terminal não ativo; qualquer `Active` força `REC-3`; mutation smoke espera target rollbackable, runner válido e abertura ADMIN com fence. Um operador serializa ações. Em `REC-3`, rollback sem prior terminal/drained, zeros/fence pré-switch, +2 s e probe externo pós-switch candidata/fence-zero é proibido. O session fence impede boot anteriormente aberto e ocioso de desaparecer do snapshot: enquanto vivo segura o lock; se a sessão cai, toda transaction usa a mesma conexão e o boot não reacquire. Novo boot/PID reinicia prova. Falta de prova em 5 min ou recovery >10 min é breach explícito fail-closed, não autorização para caminho inseguro.

## Health, Readiness and Rollback Contract

- Healthcheck Railway não substitui probe externo nem monitoramento contínuo.
- Health não deve chamar Smart Notas a cada probe: indisponibilidade transitória não deve causar restart storm.
- Criar readiness em `/api/v1/prontidao`, respondendo não-2xx se PostgreSQL estiver indisponível; Railway passa a usar essa rota. `/api/v1/saude` permanece liveness simples.
- Binding token/CNPJ é comprovado por probe pré-tráfego, nunca por conteúdo sensível no health.
- Pré-merge: atestar plano Pro, deployment ID corrente, snapshot redatado de configuração/nomes de variáveis, acesso do Owner e capacidade geral de rollback; não alegar elegibilidade futura do alvo exato. Abort antes do merge segue `REC-1` se config já foi commitada.
- Pós-merge/pré-active: um operador observa approval/trigger/cancela serialmente (`REC-2A`); config só é restaurada após trigger conclusivamente impedido ou terminal não ativo (`REC-2B`). Se ficar active, migrar imediatamente para `REC-3`.
- Pós-switch/pre-smoke amplo: assim que a nova deployment estiver ativa, confirmar que o ID antigo agora aparece como previous deployment com `Rollback` visível; a retenção Pro de `120 h` passa a governar a imagem removida/substituída.
- Teardown: `railway.json` fixa overlap zero/drain 20; o primeiro tráfego autenticado agenda espera mínima de 30 s por epoch-CAS, mas a barrier só abre por POST ADMIN após anterior terminal/removido, runner/control session-affine, fence global adquirido no writer pool1 e treatment atual/candidata não atual/não candidata zero. Base/writer/control atuais são permitidos. Health/readiness usa client control isolado.
- Config as Code está deprecado, mas a Railway documenta suporte aos serviços legados até `2026-12-01`; este cutover exige prova remota dos valores e abre follow-up de migração IaC antes dessa data, sem ampliar a janela atual.
- Rollback primário: runner externo deve estar provado/online antes do changeset/merge. Após prior terminal/drained, current quiesce/zeros, fence liberado e 2 s sem boot/PID change, Railway `Rollback` restaura imagem/variáveis sem rebuild. Depois, o runner permite não candidata somente com legado exato `Active` e exige candidata/transaction/fence zero até remoção. O objetivo `10 min` vale com preconditions comprovadas; perda inesperada pós-merge registra breach e mantém fail-closed.
- Fallback degradado: `Redeploy` reconstrói a deployment a partir do source/config original e não preserva identidade de bits; só pode ser usado após bloqueio/renovação explícita do risco e do RTO.
- Kill switch: `SMART_NOTAS_READ_ENABLED=false`; corta o provedor, mas não restaura integralmente a nova tela `Geral`.
- Fontes verificadas: [Railway Staged Changes](https://docs.railway.com/deployments/staged-changes), [Deployment Actions](https://docs.railway.com/deployments/deployment-actions), [Deployment Teardown](https://docs.railway.com/deployments/deployment-teardown), [Config as Code reference](https://docs.railway.com/config-as-code/reference), [image retention by plan](https://docs.railway.com/pricing/plans), [Prisma PostgreSQL connector](https://docs.prisma.io/docs/orm/v6/overview/databases/postgresql) e [PostgreSQL application_name](https://www.postgresql.org/docs/18/runtime-config-logging.html).

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
- Teardown diferente de `0/20`; timer/opener stale; UUID/name truncado; multiplexing; runner não preflighted/indisponível; abertura sem anterior terminal, fence writer exclusivo ou prova zero; transaction sem PID/`pg_locks`; treatment sem lease exact-once; pools diferentes de `4/1/1`/total6; writer sobreposto; ou rollback sem prior terminal/drained, current zeros/fence, +2 s resetável, probe externo e polling até candidata/fence zero/remoção.

## Definition of Done

- [ ] `DOD-CUT-01` Novo checkpoint final contendo budgets/readiness/correlation/error-only/runbook é identificado, publicável e reproduzível antes do CI/build definitivo.
- [x] `DOD-CUT-02` Alvo Railway e responsáveis são registrados redatados e confirmados pelo usuário.
- [ ] `DOD-CUT-03` Os dois pares fiscais são validados contra a empresa esperada sem exposição de segredo/CNPJ.
- [ ] `DOD-CUT-04` Timeout, rate, concorrência e bytes/memória são calibrados para a topologia real sob carga near-limit.
- [ ] `DOD-CUT-05` Logs têm sink, retenção, acesso e redaction comprovados.
- [ ] `DOD-CUT-06` A tree candidata passa localmente em build, readiness, probes, API/browser smoke e `/erros`; essa evidência não é tratada como OCI Railway idêntico.
- [ ] `DOD-CUT-07` `REC-0/1/2A/2B/3` cobre record ausente, approval/trigger/in-flight/terminal/active; um operador serializa ações, restore exige prevenção/terminal conclusivo e active força `REC-3`. Antes de changeset/merge, runner externo direto/session-affine prova ACL/classificador no target e permanece disponível na janela. Rollback exige boots anteriores terminal/removidos ou quiescidos+drenados, atual quiescido com `ativos=0`, quatro zeros e fence liberado, +2 s resetável; pós-ação o runner exige candidata/transaction/fence zero enquanto não candidata só é aceita com legado exato `Active`. O objetivo de 10 min só é declarado após essas dependências provadas; perda inesperada pós-merge é falha/RTO breach fail-closed, nunca rollback inseguro.
- [ ] `DOD-CUT-08` `Stage` customer-facing passa em lista/detalhe para ambos sem fallback/mistura por no mínimo 30 minutos na janela.
- [ ] `DOD-CUT-09` Teste local determinístico com chaves efêmeras prova que rotação HMAC invalida ID antigo e relistagem produz IDs válidos; nenhuma rotação HMAC ocorre no `Stage` deste TODO.
- [ ] `DOD-CUT-10` Um predicado SQL canônico de classificação original `ERRO` é aplicado antes de count/group/order/limit/paginação e mutations em lista, resumo, produtos, exportação, detalhe, payload, histórico correlacionado, tratamento unitário/lote e monitoramento; defesa TypeScript não substitui query-side filtering; tratamento `PENDENTE` sobre erro original permanece elegível; o contrato público congelado em `D-CUT-17..19`, `backend/README.md`, decorators OpenAPI e a descrição Swagger global em `backend/src/main.ts` estão coerentes.
- [ ] `DOD-CUT-11` Railway usa readiness PostgreSQL-aware não-2xx, liveness não chama Smart Notas e o runbook descreve variáveis fiscais, ordem atômica e rollback.
- [ ] `DOD-CUT-12` Request, aplicação, upstream e filtro de erro reutilizam o mesmo correlation ID; logs retêm por 30 dias somente metadados redatados/`actorId` pseudônimo com acesso restrito.
- [ ] `DOD-CUT-13` Candidate e final main possuem tree OID idêntico; revision/build remoto fica ligado ao final main e seus bits passam readiness/smoke Stage, sem alegar digest idêntico ao build local.
- [ ] `DOD-CUT-14` Promoção Foundation independente é concluída sem novo commit/deploy em `MonitorNotes:main`; gitlink divergente e follow-up do próximo product release ficam registrados.
- [ ] `DOD-CUT-15` Um changeset Railway de dez variáveis inclui flag `true`, cinco valores sensíveis/bindings e quatro budgets; é revisado e commitado sem redeploy da deployment antiga, e o único rebuild pós-merge comprova que consumiu esse estado.
- [ ] `DOD-CUT-16` Realtime não abre `LISTEN`, polling ou timer de varredura; stream usa `fetch` + Bearer/global guard, termina em <=30 s e emite tratamento/heartbeat; frontend reconecta/cancela e coalesce em 250 ms, de modo que lote síncrono de 500 gere um refetch de lista e um de resumo.
- [ ] `DOD-CUT-17` Queries críticas error-only possuem plano `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)` redatado e p95 SQL/endpoint separados sobre fixture determinística de 20.000 linhas, sem alteração de schema/índice, e passam os thresholds pré-promoção congelados.
- [ ] `DOD-CUT-18` Lista, resumo, produtos, exportação, detalhe, payload, tratamentos, monitoramento e SSE respeitam métodos, allowlists, defaults, bounds 1..64/1..200, campos, envelope, códigos, headers e negações; frontend types/README não expõem contratos removidos.
- [ ] `DOD-CUT-19` Modo atual de `MONITORAMENTO_TOKEN`/UptimeRobot é atestado; se configurado, consumidor usa header e URL está limpa antes do merge, provado contra a release corrente; nenhuma rotação/11ª chave ocorre.
- [ ] `DOD-CUT-20` Todo campo textual externo do CSV neutraliza inícios `=,+,-,@,TAB,CR` antes do escaping, com testes adversariais coluna a coluna; runtime realtime não importa `pg`, enquanto `pg`/`@types/pg` permanecem somente em devDependencies para `espelhar.ts`.
- [ ] `DOD-CUT-21` Tratamentos unitário/lote são serializados sem deadlock, inversão, lost update, retry ambíguo ou saturação: clients Prisma read/writer/control fixam `4/1/1`, waits `2 s`, total <=6; `ReadCommitted`, transaction `15 s`, lock `1,5 s`, statement `12 s`, gate `1` e teto `500` locks. A lease libera exact-once no settle: resolve libera e depois publica; commit incerto libera local, retorna 503/refresh, não publica/repete e a sessão writer/fence ainda observável bloqueia rollback. Cada comando aceito deixa um append, lote é atômico. BCI 5/10/20 e carga mista de 60 s provam 60/60 readiness 2xx/p95 <=500 ms, read p95 <=3 s, zero P2024, <=6 conexões e nenhum fence gap, com JSON `pcv-1`.
- [ ] `DOD-CUT-22` `railway.json` congela overlap `0`/drain `20`; health ignora barrier; timer/opener usam boot/epoch/state CAS e quiesce/SIGTERM invalidam one-way. Abertura exige anterior terminal, runner/control session-affine, advisory session fence global adquirido no writer pool1 e cinco contagens exatas. Nomes base/writer/control/treatment 45/52/53/55 bytes são observados. Cada transaction valida PID e lock granted antes de domínio; session recreate/loss quiesce e falha 503 sem auto-reacquire. PATCH/lote adquire lease antes do primeiro await e libera exact-once no settle. ADMIN/no-store preserva stale-409 sobre DB-503. Rollback exige fence/current/prior zeros e runner externo pré-comprovado prova qualquer candidata/fence zero pós-switch. Probes idle-old-boot, session loss, timer/open↔quiesce/SIGTERM, commit incerto e restart provam ausência de overlap; IaC antes de `2026-12-01`.

## Validation Steps

- [ ] `VAL-CUT-01` Executar pelo runtime canônico compatível `"/mnt/c/Program Files/Git/bin/bash.exe" -lc 'cd /c/unifast/monitordenotas && bash delphi-ai/verify_context.sh'` e exigir `PACED-Ready`. A falha CRLF do wrapper no bash WSL não é falha do projeto; `bash delphi-ai/tools/verify_context.sh` pode ser usado apenas como diagnóstico, não como evidência substituta.
- [ ] `VAL-CUT-02` Depois de toda implementação, congelar o novo SHA e reexecutar suites CI-equivalent backend, frontend e Foundation exatamente nele.
- [ ] `VAL-CUT-03` Construir imagem raiz e provar startup/health com flag desligada; com flag ativa, ausência de qualquer segredo/binding ou budget `10 s/4/15/60` deve falhar fechada; o live probe deve usar exatamente `10 s/4/15/60`, não `30 s/2/30/120`.
- [ ] `VAL-CUT-04` Executar `SMART_NOTAS_PROBE_ENABLED=true` somente em runner autorizado, com saída redatada, nos dois contextos.
- [ ] `VAL-CUT-05` Executar carga near-2MiB no candidato local com budgets `10 s/4/15/60` e registrar p95/p99, 429/5xx/timeout, RSS/heap e recuperação; confirmar métricas Railway antes do corte.
- [ ] `VAL-CUT-06` Executar smoke autenticado dos GETs e jornada browser `Geral -> detalhe -> Erros -> Geral` nos dois contextos.
- [ ] `VAL-CUT-07` Inspecionar logs/respostas por padrão sensível sem registrar os valores pesquisados.
- [ ] `VAL-CUT-08` Antes do changeset/merge, executar somente ensaio local determinístico de `REC-0/1/2A/2B/3`, incluindo record ausente, approval, trigger atrasado/rejeitado, cancel→active, terminal, fence/boot/contagens e pós-switch simulado; nenhuma ação Railway de cancel/restore/Rollback é executada. Remotamente, coletar apenas fatos read-only: deployment/ID/plano/snapshot/teardown/capacidade geral de rollback e probe do runner externo direto/session-affine no mesmo target, repetido <=15 min antes do merge. Falha/indisponibilidade aborta antes de `REC-2A`.
- [ ] `VAL-CUT-09` Executar `cutover_integrity_audit`, testes SQL e fixtures inelegíveis: count/páginas corretos, só `ERRO`, histórico filtrado e reabertura elegível; validar allowlists/defaults, ref path/lote whitespace/1/64/65/duplicata pós-trim, token config/header 0/1/200/201, 400 versus 404, envelope/DTO/header exatos e docs/OpenAPI sem contratos removidos.
- [ ] `VAL-CUT-10` Rodar guards Delphi de autoridade, diff, CI, revisão, completion e Foundation conforme a fase.
- [ ] `VAL-CUT-11` Forçar PostgreSQL indisponível em ambiente local controlado e comprovar readiness não-2xx enquanto liveness do processo permanece bounded.
- [ ] `VAL-CUT-12` Correlacionar um request sintético em controller/request context, service, adapter/upstream e exception filter com um único ID; revisar logs por PII/payload/segredo sem persistir os valores pesquisados.
- [ ] `VAL-CUT-13` Comparar `candidate^{tree}` com `final-main^{tree}`, registrar SHAs/tree, build local como evidência separada, revision/build Railway e smoke dos bits remotos; tree mismatch ou smoke remoto falho aborta.
- [ ] `VAL-CUT-14` Provar que o Dockerfile não consome a Foundation, registrar `Foundation main@sha` versus root gitlink pin e abrir follow-up para sincronização no próximo release sem mutar `MonitorNotes:main` agora.
- [ ] `VAL-CUT-15` Capturar o changeset staged de dez chaves por nomes/redaction, provar commit sem redeploy da deployment antiga e correlacionar a única revision pós-merge com flag `true` e budgets aprovados.
- [ ] `VAL-CUT-16` Provar ausência de conexão `pg`/polling/`evento.novo`; fetch Bearer testa 401, <=30 s, reconexão após desativação, nenhuma credential em URL/log, treatment/heartbeat/cancel; fake timers provam que 500 eventos síncronos geram zero refetch antes de 250 ms e exatamente um list + um resumo ao aquietar.
- [ ] `VAL-CUT-17` Gerar com seed versionada fixture local de exatamente 20.000 logs (80% originais `PENDENTE/SUCESSO`, 20% `ERRO`; entre erros, 25% `RESOLVIDO/IGNORADO` e casos reabertos), registrar versão/config PostgreSQL e estatísticas. Workloads HTTP fixos, isolados e nesta ordem: `GET /eventos?situacao=ERRO&pagina=1&limite=25&direcao=desc`, `GET /eventos?situacao=TRATADOS&pagina=1&limite=25&direcao=desc`, `GET /eventos/resumo`, `GET /eventos/produtos`, `GET /eventos/exportar?situacao=TODOS`; o harness SQL usa filtros equivalentes sem inventar query keys. Para **cada** workload: 5 warm-ups descartados, um `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)` redatado e 30 execuções SQL sequenciais; depois, processo endpoint separado/reiniciado, 5 warm-ups e 50 requests medidos com concorrência 4 para cada workload não-export, e 5 warm-ups + 20 requests com concorrência 1 para export. Por série ordenar wall-clock e calcular nearest-rank `p95 = amostra[ceil(0.95*n)-1]`; não misturar séries. Bloquear se filtro vier após limit/window/group, houver scan correlacionado por linha, lista/resumo/produtos >`3 s` ou export >`8 s`. Falha exige TODO separado de schema/índice e nova aprovação.
- [ ] `VAL-CUT-18` Antes do changeset/merge, inspecionar apenas presença/bound do `MONITORAMENTO_TOKEN` sem valor; se presente, provar UptimeRobot com `x-monitor-token`, URL sem query credential, current release 200/503 com header e 401 sem ele; se ausente, provar modo público. Desconhecido bloqueia corte; não rotacionar.
- [ ] `VAL-CUT-19` Para cada coluna textual externa do CSV, testar valores iniciados individualmente por `=`, `+`, `-`, `@`, TAB e CR; output deve conter prefixo `'` dentro do valor CSV escapado, preservar BOM/headers e não alterar números seguros.
- [ ] `VAL-CUT-20` Executar PATCH/lotes sobrepostos em níveis `5 x 2`, `10 x 3`, `20 x 5` com gate writer1, incluindo wait inversion, collision, linha futura, lock >1,5 s, lote500 e falhas `40P01/40001/55P03/P2034/P2024/P2028/57014`, conexão/fence perdida e commit incerto. Exigir clients efetivos read/writer/control `4/1/1`, wait2 e <=6 conexões sem URL em output; um retry 25 ms só após rollback, <=1 mutation/500 locks, monotonicidade, atomicidade e SSE pós-resolve. Em connection-loss, Promise rejeita/libera lease exact-once; a mesma sessão writer mantém fence+transaction server-side até encerramento, bloqueando novo opener/rollback. Rodar também 60 s com uma transaction writer/lote e concorrência autenticada >4 reads, control probe 1 Hz: 60/60 2xx, p95 control <=500 ms, reads <=3 s, zero P2024 e nenhum PID/fence gap. Lote500 sem contenção <12 s; lock persistente falha bounded. Gerar JSON BCI `pcv-1`; HTTP-only não satisfaz.
- [ ] `VAL-CUT-21` Em processos independentes, provar UUID/names base45/writer52/control53/treatment55, session affinity e negativo multiplex; sufixo desconhecido falha prova. Boot A abre, mantém session fence mesmo com pool ocioso/zero sessões adicionais e impede B. Derrubar/recriar a sessão writer de A: lock/transaction server-side devem encerrar antes de B adquirir; A permanece sem auto-reacquire e toda mutation posterior falha PID/`pg_locks` antes de domínio, mesmo se B já abriu. Pausar opener e intercalar timer/open↔quiesce/SIGTERM/DB success/failure para provar stale 409 sobre 503 e uma vencedora. Classificador devolve cinco contagens, inclui UUID nunca observado e não mascara candidata com legado >0. Lease sync/exact-once, quiesce idempotente, unlock pelo mesmo PID, bodies/status/headers/no-store e reads verdes são obrigatórios; qualquer overlap, fence gap, multiplexing ou polling interrompido falha.
- [ ] `VAL-CUT-22` Somente se um abort real pós-merge alcançar `REC-3`, coletar evidência operacional condicional: ação `Rollback` no ID antigo exato, runner externo já preflighted consultando <=1 s, candidata/transaction/fence zero, sessão não candidata aceita apenas após legado exato `Active`, re-quiesce/restart e conclusão/falha/RTO. Se `REC-3` não ocorrer, registrar `n/a — state not reached`; esta linha nunca autoriza drill remoto nem é prerequisite pré-merge.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-CUT-01` | Definition of Done | checkpoint final | git/build | novo `branch@sha` após implementação + build verde | local/CI | `planned` | `31712a0` é baseline inicial, não artefato final |
| `DOD-CUT-02` | Definition of Done | alvo/responsáveis | doc/manual | `environment-topology.md` redatado | Railway | `passed` | Owner/topologia confirmados |
| `DOD-CUT-03` | Definition of Done | binding emissores | runtime | live probe redatado | local authorized runner | `planned` | ambos os contextos antes da janela |
| `DOD-CUT-04` | Definition of Done | capacidade | load | relatório RLS near-limit | local candidate build + Railway metrics | `planned` | budgets iniciais congelados |
| `DOD-CUT-05` | Definition of Done | auditoria | runtime/review | política + consulta redatada | Railway | `planned` | 30 dias confirmados; provar acesso/redaction |
| `DOD-CUT-06` | Definition of Done | smoke pré-cutover | runtime/browser | API + browser evidence | local candidate tree/build | `planned` | source-level; não prova OCI Railway |
| `DOD-CUT-07` | Definition of Done | recovery state machine | runtime/manual | local REC simulation + read-only runner preflight pré-merge + fence/zeros + conditional real-abort evidence in `VAL-CUT-22` | local/Railway Stage | `planned` | sem destructive drill; 10 min condicionado ao preflight; perda pós-merge é breach |
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
| `DOD-CUT-19` | Definition of Done | monitor consumer migration | ops/security | mode attestation + header-only current-release probe | UptimeRobot/current Stage | `planned` | sem token value/rotation |
| `DOD-CUT-20` | Definition of Done | CSV/dependency hardening | test/security/manifest | adversarial columns + runtime import scan + manifest/lock diff | local backend | `planned` | `pg` somente dev tooling de espelhamento |
| `DOD-CUT-21` | Definition of Done | tratamento concorrente | concurrency/domain | BCI 5/10/20 + clients 4/1/1 + gate1/batch500 + mixed-load60/readiness + exact-once/uncertain commit + JSON/hash | local PostgreSQL/backend | `planned` | <=6 connections; no implicit read reserve; HTTP-only inválida |
| `DOD-CUT-22` | Definition of Done | cross-version writer barrier | deployment/concurrency/security | writer session fence/PID/pg_locks + five counts + epoch-CAS + idle/lost-session boot + runner preflight/post-switch | local multi-process + Railway Stage | `planned` | boot ocioso não some; no auto-reacquire; reads/control disponíveis |
| `VAL-CUT-01..22` | Validation Steps | validações | mixed | preencher cada evidência durante execução | mixed | `planned` | `VAL-CUT-22` é condicional ao REC-3 real, nunca drill |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas API | fonte/binding | `unknown` | `2026-09-27 local config only` | probe não executado neste cutover | bloquear ativação |
| Railway control plane | deploy/vars/logs/rollback | `degraded` | `2026-09-27` | target/scale/operator confirmados; sem CLI autenticada | revalidar revision/config imediatamente antes da mutação |
| Railway `Stage` | smoke/cutover customer-facing | `healthy` | `2026-09-27` | `/api/v1/saude` HTTP 200 + project-owner confirmation | cutover direto somente após gates e aprovação final |
| PostgreSQL Railway | auth, erros, pools e writer fence | `degraded` | `2026-09-27` | health público prova alcance, não session affinity/ACL/locks | probe direto pré-changeset/pré-merge obrigatório |
| External rollback runner | classificador/fence fora da API candidata | `unknown` | `not yet verified` | probe read-only no mesmo target pendente | indisponível bloqueia changeset/merge e `REC-2A` |

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
| Gate mutation tratado como reserva de read capacity | duas mutations ocupam pool compartilhado e reads/readiness disputam o restante | P2024/readiness flapping sob quarta operação | clients físicos read4/writer1/control1 + mixed-load thresholds; nenhuma alegação de reserva implícita |
| Runner de rollback descoberto somente após merge | ACL/afinidade/visibilidade faltam quando REC-3 começa | fail-closed excede RTO sem caminho seguro | probe read-only pré-changeset/pré-merge e disponibilidade durante a janela |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan |
| --- | --- | --- | --- | --- | --- |
| structural/test | backend fiscal boundary | existing fiscal module/contract/structure specs | Prisma/logs fallback, public credential input, context leak | `already-enforced` | rerun obrigatório em `VAL-CUT-02` |
| structural/test | integration-error SQL boundary | SQL-shape + high-ineligible-ratio pagination tests across logs/monitoring | filtro pós-query, total/página falsa ou read/mutation `SUCESSO` escapando | `implement-in-this-todo` | `VAL-CUT-09` antes do deploy |
| contract/test | public `/eventos` + monitoramento + SSE | method/request/DTO/status/header matrix from `D-CUT-17..19` | zeros enganosos, filtros legados, disclosure, credential URL ou auth bypass | `implement-in-this-todo` | `VAL-CUT-09/16` antes do deploy |
| security/contract | realtime stream | Bearer/global guard + browser fetch parser/cancel/refetch + no pg/timer structure | JWT em URL/log, usuário inativo, reconnect leak ou insert externo alegado | `implement-in-this-todo` | `VAL-CUT-16` antes do deploy |
| security/test | CSV export | per-column formula-prefix fixture for `=,+,-,@,TAB,CR` | spreadsheet formula injection or numeric corruption | `implement-in-this-todo` | `VAL-CUT-19` antes do deploy |
| ops/consumer | UptimeRobot | current-release header migration/public-mode attestation | query credential breakage or false outage | `manual pre-merge gate` | `VAL-CUT-18` antes do changeset/merge |
| race/load | treatment SSE consumer | fake-time burst of 500 events | unbounded list/summary refetch storm | `implement-in-this-todo` | `VAL-CUT-16` antes do deploy |
| concurrency/domain | treatment mutations | clients 4/1/1 + writer gate1 + namespaced locks/order/timestamp + bounded retry/error + exact-once settle + BCI/mixed-load60/batch500/connection-loss | causal inversion, lost update, pool/readiness saturation, false headroom, ambiguous retry, partial batch or duplicate SSE | `implement-in-this-todo` | `VAL-CUT-20` antes de Local-Implemented |
| deployment/concurrency | legacy↔candidate treatment writers | direct/session-affine + writer session fence/PID/pg_locks + five counts + UUID/names + epoch-CAS + runner preflight/external post-switch | multiplexing, identity truncation, idle old boot absent from snapshot, session recreate/auto-reacquire, legacy masking, uncertain commit or restart overlap | `implement-in-this-todo` | `VAL-CUT-08/21/22`; Stage mutation só no abort real |
| explain/performance | logs query family | redacted JSON plans on representative high-ineligible dataset | predicate late, correlated per-row scan or p95 above promotion budget | `implement-in-this-todo` | `VAL-CUT-17` antes do deploy |
| config test | bootstrap variables | configuration specs with flag false/true-invalid | enable sem pares fiscais/HMAC ou valores fora de bound | `already-enforced` | rerun obrigatório em `VAL-CUT-03` |
| read-only runtime probe | Smart Notas binding | `smart-notas-live.probe.spec.ts` | token/CNPJ mismatch, lista/detail indisponível | `already-enforced` | execução real obrigatória em `VAL-CUT-04` |
| load/stress | external path and 2 MiB envelope | RLS report on approved topology | saturation, quota amplification, memory/recovery failure | `implement-in-this-todo` | `VAL-CUT-05` |
| browser smoke | same-origin React/Nest release | source-owned fiscal browser journey | incompatible UI/API, context/cache leak, `/erros` regression | `implement-in-this-todo` | `VAL-CUT-06` |
| operational recovery | Railway deployment | pre-merge facts + runner read-only preflight; exact old-ID rollback/restore somente se abort alcançar o estado | runner/rollback unavailable, expired image, wrong vars ou destructive drill indevido | `manual-only-with-rationale` | local simulation `VAL-CUT-08`; real conditional `VAL-CUT-22` |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after review baseline freeze and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set: TODO + topology/dependency artifacts + railway/Docker/config/health/fiscal boundaries`
- **Decision review status:** `round-22 confirmations pending`
- **Decision review evidence / resolution:** a arquitetura round 21 retornou `CLEAN/APROVÁVEL` nas refs congeladas, mas a crítica no-context obrigatória encontrou quatro riscos novos: snapshot sem fence persistente, headroom não reservado, runner tardio e mistura entre ensaio/ação real. O candidato round 22 integra writer session fence, clients `4/1/1`, runner pre-merge e `VAL-CUT-08/22` separados; publicação e novas confirmações são obrigatórias.

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
| `R12-OPS-01` | high | yes | `Integrated` | `REC-2A` inicia no merge e cobre record ausente, approval, delayed/rejected trigger e in-flight; restore exige prevenção/terminal conclusivo. |
| `R12-OPS-02` | high | yes | `Integrated` | `D-CUT-20`, Execution 1/6/8 e `VAL-CUT-18` migram/atestam UptimeRobot header-only antes do merge, sem rotação. |
| `R12-SEC-01` | high | yes | `Integrated` | `D-CUT-21` e `VAL-CUT-19` neutralizam `=,+,-,@,TAB,CR` em cada coluna textual externa do CSV. |
| `R12-ARCH-01` | high | yes | `Integrated` | path/lote usam ref 1..64; monitor config/header 1..200; whitespace/oversize dão 400 e ref válida inelegível dá 404. |
| `R12-PERF-01` | medium | no | `Integrated` | `D-CUT-22`/`VAL-CUT-16` coalescem 500 eventos em um par list/resumo por janela 250 ms. |
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
| `R18-OPS-BCI-01` | high | yes | `Integrated` | `D-CUT-24` introduz epoch monotônico: opener captura boot/epoch/estado, faz prova async e só abre por compare-and-transition síncrono; quiesce/SIGTERM incrementam epoch antes do primeiro await. `VAL-CUT-21` pausa inspeção e prova stale opener 409/sem lease. |
| `R18-OPS-IDENTITY-01` | high | yes | `Integrated` | `bootId` é UUID v4 lowercase de 36 ASCII; base/treatment 45/55 foram preservados e writer/control 52/53 adicionados em R21; current_setting/reversão devem coincidir exatamente. |
| `R18-API-01` | medium | yes | `Integrated` | rows operacionais congelam envelope/mensagem/`Retry-After: 1`; quiesce 503 preserva fechamento, retry é idempotente e rollback permanece bloqueado até prova zero. |
| `R19-OPS-BCI-01` | high | yes | `Integrated` | primeiro request captura boot/epoch/inicializando uma vez; callback 30 s usa CAS e incrementa epoch; quiesce/SIGTERM cancelam best-effort e tornam callback no-op. Ambos os ordenamentos entram em `VAL-CUT-21`. |
| `R19-OPS-BCI-02` | high | yes | `Integrated` | `REC-3` mantém conjunto de boots observados, exige prior terminal/removido ou quiesced+drained e reinicia checklist/+2 s em boot change; os zeros inicialmente agregados foram refinados nas cinco contagens e no probe externo de `R20-OPS-BCI-01`. |
| `R19-OPS-DB-01` | high | yes | `Integrated` | datasource direto/session-affine e credencial exclusiva viram gate; transaction/statement multiplexing ou modo desconhecido bloqueia abertura/cutover e recebe negativo no harness. |
| `R19-API-01` | medium | yes | `Integrated` | após sucesso/falha DB, opener revalida boot/epoch/state primeiro; stale/quiesced sempre 409 sem Retry-After, e 503 só ocorre se captura ainda atual. |
| `R20-OPS-BCI-01` | high | yes | `Integrated` | classificador expõe cinco contagens: candidata atual, treatment atual, candidata não atual, treatment não atual e não candidata. Pré-switch exige os quatro zeros aplicáveis; pós-switch runner externo permite não candidata apenas com legado exato `Active` e exige qualquer UUID candidato, inclusive não observado, em zero. `VAL-CUT-08/21` mantém sessão legada e candidata simultâneas para provar que não há mascaramento. |
| `R20-OPS-BCI-02` | high | yes | `Integrated` | lease é liberada de forma idempotente exatamente uma vez no settle da Promise Prisma. Resolve libera antes da publicação pós-commit; rejeição commit-uncertain libera contador local, mas não publica/não repete; sessão/transação server-side ainda observável mantém rollback cercado pelas contagens DB e recebe teste connection-loss dedicado. |
| `R21-OPS-BCI-01` | high | yes | `Integrated` | writer Prisma pool1 mantém advisory session fence global; toda transaction valida PID/`pg_locks`, session loss não auto-reacquire e boot ocioso continua bloqueando sucessor. `VAL-CUT-21` força idle/loss/reconnect/interleavings. |
| `R21-PERF-01` | high | yes | `Integrated` | pools físicos read4/writer1/control1 substituem a falsa reserva; gate1/500 locks e mixed-load60 congelam <=6 conexões, 60/60 readiness p95 <=500 ms, read p95 <=3 s e zero P2024/fence gap. |
| `R21-OPS-02` | high | yes | `Integrated` | runner externo/ACL/session-affinity/classifier viram gate read-only pré-changeset/pré-merge repetido <=15 min e requisito da janela; perda pré-merge aborta, perda pós-merge é breach fail-closed. |
| `R21-ADH-01` | medium | yes | `Integrated` | `VAL-CUT-08` contém apenas simulação local + fatos/probe remoto read-only; `VAL-CUT-22` coleta Rollback real somente se um abort alcançar `REC-3`, senão n/a. |
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
- **Baseline commit:** `3cbfac6cb5bdcdf0a342eb74fa8994b8dd6c76ba`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** os quatro achados R21 foram integrados e publicados no material round 22; esta attestation não altera seções materiais; confirmações independentes permanecem pendentes.
- **Evidence / reference:** Foundation material `origin/main@3cbfac6cb5bdcdf0a342eb74fa8994b8dd6c76ba`; root material `MonitorNotes/delphi-and-foundation@9269d9fccca7c9f1628741ba390644b5e0d18fa8`; refs verificadas com `git rev-parse --verify`; code-origin `31712a042cab3c796d5daca7350c6c58453e1c73`; Delphi guard `ee9b448`.
- **Waiver authority / reference:** `n/a`.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impede alteração material entre o pacote revisado e o aprovado.
- **Trigger stage:** `after review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `canonical defaults, incluindo Diff Expectation Contract, Module Decision Baseline Snapshot e Decision Baseline (Frozen Before Implementation)`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** attestation round 22 preserva todas as seções materiais do baseline publicado; arquitetura e crítica ainda devem confirmar o pacote.
- **Evidence / reference:** `review_scope_drift_guard.py` contra `uninotas-foundation:main@3cbfac6cb5bdcdf0a342eb74fa8994b8dd6c76ba`; resultado esperado `go`, `0/23` seções materiais alteradas.
- **Waiver authority / reference:** `n/a`.

## Frontend / Consumer Matrix

| Producer Surface In This TODO | Consumer | Delivery State | Evidence / Waiver |
| --- | --- | --- | --- |
| `GET /api/v1/notas` | React `Geral`, `ListaNotas`, session cache | `implemented candidate; final tree validation pending` | fiscal contract/browser/cache suites + Stage smoke |
| `GET /api/v1/notas/:noteId` | React `/notas/:noteId`, `DetalheNota` | `implemented candidate; final tree validation pending` | opaque-ID/detail/error tests + Stage smoke |
| `/api/v1/eventos` list/resumo/produtos/export/detalhe/payload/history | React `/erros` + `/eventos/:refId`; external consumers unknown | `final contract frozen in D-CUT-17..19; implementation planned` | exact method/request/DTO/status/header matrix; SQL predicate incl. pagination/correlated attempts; Owner attestation before deploy; no waiver |
| `/api/v1/eventos` contract documentation | `backend/README.md` + `frontend/README.md` + Swagger/OpenAPI decorators in `backend/src/logs/logs.controller.ts` + global description in `backend/src/main.ts` | `known contract consumers; update required` | docs remove five-tab/log-success/EventSource claims and describe error-only + refresh + fetch/Bearer treatment stream |
| `/api/v1/eventos/*/tratamento` unitário/lote | React error-treatment flows | `producer guard + D-CUT-23 serialization planned; behavior preserved only when original class is ERRO` | mutation tests deny `PENDENTE`/`SUCESSO` without existence disclosure; BCI 5/10/20 proves append/state/SSE invariants |
| `/api/v1/operacao/tratamentos/barreira|abrir|quiescer` | project Owner/ADMIN cutover runbook + preflighted external runner; React only handles treatment 503/refresh | `D-CUT-24 frozen; new operational producer planned` | ADMIN/no-store; clients 4/1/1; writer session fence/PID/pg_locks; five counts; epoch-CAS; stale-409; exact-once; preflight + conditional post-switch probe |
| `GET /api/v1/realtime/eventos` | React `useTempoReal`/fetch streaming somente em `/erros` | `D-CUT-19 frozen; producer/consumer change planned` | Bearer/global guard/inactive-user negatives, no query JWT/log, treatment-only stream, cancel/refetch; Geral/detalhe fiscal não conectam |
| `GET /api/v1/monitoramento/erros` | UptimeRobot | `exact shape frozen; consumer migration required before merge by D-CUT-20` | current-release header migration/URL cleanup or public-mode attestation; 200/400/401/503 + no-store; tratados excluídos |
| `GET /api/v1/prontidao` | Railway deployment healthcheck | `new producer/config consumer planned` | PostgreSQL-down non-2xx test + `railway.json` exact path + deployed readiness evidence |
| `GET /api/v1/saude` | human/public liveness consumers | `existing contract retained as liveness; removed from Railway readiness role` | existing shape/status test + runbook distinction |
| Smart Notas env/budgets | NestJS bootstrap / Railway sealed variables | `budgets fail-closed change planned; no frontend consumer` | missing-variable startup negatives + client bundle/env scan |
| `note_read_model` / `integration_error_read_model` | Foundation registry, modules and upper canonical docs | `promotion planned only after runtime evidence` | atomic diff across policy/modules/root docs + Foundation validator |

## Test Strategy

- **Strategy (`test-first|test-after|not-applicable`):** `test-first`.
- **Why:** budgets fail-closed, readiness e predicado error-only alteram contratos de segurança/produção; cada mudança começa por um teste negativo reproduzível antes do código.
- **Fail-first targets:** budgets/readiness; SQL/error-only; contratos `D-CUT-17..24`; bounds/CSV/query token; JWT/SSE; lote500; clients diferentes de 4/1/1; falsa reserva de read; mixed-load/readiness; treatment sem lease/fence/PID; session recreate/idle old boot/auto-reacquire; commit incerto; multiplexing/name; timer/open↔quiesce/SIGTERM; stale409/DB503; legacy masking candidate; runner ausente pré-merge; tentativa de drill Railway em `VAL-CUT-08`; correlation/context/cache/HMAC/probe.
- **External read-only:** `/empresa`, lista e detalhe nos dois contextos, sem mutação fiscal e com saída redatada.
- **Browser:** build local da source tree com interceptação controlada; depois smoke imediato dos bits reconstruídos no único `Stage` customer-facing.
- **Capacity:** latência, quota, concorrência e memória near-limit; planos `EXPLAIN` redatados e p95 query-side cumprem `VAL-CUT-17` antes de promoção.
- **Rollback:** fatos atuais atestados pré-merge; alvo antigo exato confirmado como rollbackable somente pós-switch/pre-smoke amplo; restore real apenas em abort, com risco residual aprovado e RTO de 10 minutos.

## Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before (`APROVADO|Local-Implemented|promotion`) | Status (`planned|passed|blocked|waived|n/a`) | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| backend NestJS | fiscal/config/readiness/error-only/correlation/auth mudam | startup fail-closed; DB-negative readiness; exact HTTP contract; SQL predicate before count/group/order/limit/mutations; high-ineligible pagination; correlated history; fetch-SSE global auth/no polling; same correlation ID | Node 22 host Windows; fixtures Jest determinísticas/Prisma SQL assertions; nenhum token live | no diretório `backend`: `npm test -- --runInBand && npm run lint && git diff --exit-code && npm run build`; se lint autofixar, invalidar/refazer freeze e toda validação | `Local-Implemented` | `planned` | output + SHA/tree antes/depois | `npm run lint` contém `--fix`; zero diff é obrigatório |
| backend SQL plan/performance | error-only muda todas as queries críticas | workloads fixos lista ERRO/TRATADOS, resumo, produtos, export; predicate placement; p95 SQL/HTTP 3 s/8 s | seed 20k: 80% inelegível/20% erro; 25% erros tratados; PG version/config; ordem/isolamento de `VAL-CUT-17` | por workload: 5 warmups + EXPLAIN + 30 SQL; novo processo: 5 warmups + 50 HTTP concurrency 4, ou 20 export concurrency 1; nearest-rank por série | `Local-Implemented` | `planned` | seed + JSON plans redatados + séries/p95 separados | falha abre TODO de schema/index; não amplia este diff |
| backend BCI treatment overlap | PATCH/lote e cutover legacy↔candidate | 5/10/20; clients4/1/1/gate1; mixed-load60; writer fence/PID/pg_locks; idle/session-loss boot; five counts; epoch-CAS/stale409; exact-once/uncertain commit; runner preflight | PostgreSQL local direto + simulador multiplex; legacy/múltiplos boots; clocks/awaits/connection-loss observáveis | runners Jest `VAL-CUT-20/21`; helper `backend_concurrency_probe.sh`; `VAL-CUT-22` só abort real | `Local-Implemented` | `planned` | `foundation_documentation/artifacts/tmp/uninotas-cutover-pcv/bci-pcv1.json` + SHA-256 | `BCI-SP-H`/`BCI-A1`; <=6 connections; cross-version |
| backend near-limit | envelope externo/memória | 2 MiB, fairness, semaphore 4, rates 15/60, timeout/abort/recovery | loopback stub only; `RLS_OUTPUT_DIR` redatado | no diretório `backend`: `RLS_OUTPUT_DIR=../artifacts/cutover-rls npm test -- --runInBand --runTestsByPath src/fiscal-notes/__tests__/smart-notas-load.spec.ts` | `Local-Implemented` | `planned` | `artifacts/cutover-rls` redatado | sem tráfego provider real |
| frontend React/Vite unit/race | context/cache/contract mudam | Geral/detalhe/Erros, troca rápida de contexto, logout/401 cache purge e error-only | Node 22 host Windows; fixtures locais dos scripts | no diretório `frontend`: `npm run test:notas && npm run test:notas:race && npm run lint && npm run build` | `Local-Implemented` | `planned` | output dos cinco comandos | bundle same-origin |
| frontend Playwright intercepted | jornada visível muda | login -> Geral -> detalhe -> Erros -> Geral; ambos contextos; nenhuma origem externa; `/eventos` só erro | `npm run dev` em loopback; Chrome/Chromium local em `CHROME`; todas as APIs interceptadas pelo runner | no diretório `frontend`: `ALVO=http://127.0.0.1:5173 CHROME=<chromium-local> npm run e2e:notas` | `Local-Implemented` | `planned` | relatório console redatado | adicionar negativas do history/error-only neste TODO |
| root Docker | artefato único Railway | build, startup, liveness/readiness positiva e PostgreSQL-negativa | Docker daemon; env local não secreto; candidate tree limpa | `docker build -t monitornotes:cutover-candidate .` seguido do runbook de startup/probes em `DEPLOY.md` e comparação final de tree OID | `promotion` | `planned` | image ID local + probe outputs | source-level only; OCI Railway pode divergir |
| Foundation / Delphi | TODO/authority/canon mudam | schema, diff drift, Foundation integrity e contexto PACED | links existentes; nenhum repair salvo desvio Delphi-managed | `python3 delphi-ai/tools/todo_deterministic_validator.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-cutover.md && python3 foundation_documentation/deterministic/validate_foundation.py --root foundation_documentation && "/mnt/c/Program Files/Git/bin/bash.exe" -lc 'cd /c/unifast/monitordenotas && bash delphi-ai/verify_context.sh'` | `APROVADO` | `planned` | stdout dos guards | runner canônico evita incompatibilidade CRLF do wrapper sob WSL; repetir no closeout |
| live provider | binding real dos dois emissores | `/empresa`, lista e detalhe read-only em Unifast/Prosperar usando `10 s/4/15/60` | runner autorizado; cinco bindings presentes; probe implementado com envelope exato; saída redatada | no diretório `backend`: `SMART_NOTAS_PROBE_ENABLED=true SMART_NOTAS_TIMEOUT_MS=10000 SMART_NOTAS_MAX_CONCURRENCY=4 SMART_NOTAS_RATE_PER_USER_MINUTE=15 SMART_NOTAS_RATE_PER_CONTEXT_MINUTE=60 npm test -- --runInBand --runTestsByPath src/fiscal-notes/__tests__/smart-notas-live.probe.spec.ts` | `promotion` | `blocked` | output agregado/redatado | código do probe deve consumir/validar os valores, sem hardcode legado |
| Railway browser | experiência real/deployed bits | login, Geral/detalhe/Erros/Geral, ambos contextos, revision/build correta | final main tree equal; ten-key changeset consumido; readiness verde; sessão autorizada | smoke autenticado conforme `DEPLOY.md`, seguido de observação de 30 minutos | `promotion` | `blocked` | deployment ID + relatório redatado | somente após deploy autorizado |

## Plan Review Gate

- **Review decision:** `required`
- **Review status:** `round-22 material frozen; metadata-only attestation and independent confirmations pending`
- **Required lenses:** architecture, operations, rollback, security, tests, performance, observability and structural soundness.
- **Known plan finding:** o health atual retorna HTTP 2xx quando o banco está degradado; `D-CUT-10` agora exige readiness separada não-2xx e mantém Smart Notas fora do loop.
- **Approval request condition:** nova revisão confirma `D-CUT-06..24`, crítica converge, baseline é atualizado e guards retornam `go/preflight-go`.

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
- [ ] Após merge, deployment ainda invisível/awaiting approval/trigger delayed ou rejected: permanecer `REC-2A`; nunca restaurar config sem prova conclusiva de prevenção/terminal.
- [ ] Binding fiscal diverge, ocorre cross-context, segredo/PII vaza, quota/memória satura: abortar imediatamente pelos thresholds.
- [ ] Linha principal é `ERRO`, mas histórico correlacionado contém `SUCESSO/PENDENTE` original: filtrar cada linha; tratamento `PENDENTE` do erro continua visível.
- [ ] Predicado aplicado só depois da query: bloquear por totais/páginas/agregações incorretos; teste estrutural deve provar filtro SQL antes de count/group/order/limit/mutations.
- [ ] Filtros `PENDENTE/SUCESSO` ainda aceitos, resumo mantém campos removidos, ou detalhe/tratamento revela ref inelegível: bloquear promoção por contrato público divergente.
- [ ] Defaults/allowlists divergem, resumo/export aceitam paginação ignorada, lote aceita ref branca/duplicada, ou erro sai fora do envelope comum: bloquear promoção.
- [ ] UptimeRobot ainda usa query token, consumer mode é desconhecido ou header não foi provado contra current release: bloquear merge sem rotacionar segredo.
- [ ] CSV permite scalar textual iniciado por `=,+,-,@,TAB,CR` sem prefixo neutralizador: bloquear por spreadsheet injection.
- [ ] Lote 500 causa mais de um refetch list + um resumo na mesma janela 250 ms: bloquear por request storm.
- [ ] README, decorators OpenAPI ou descrição Swagger global ainda anunciam cinco abas/sucesso legado: bloquear promoção por contrato incoerente.
- [ ] Realtime ainda aceita JWT em query, ignora o guard global, abre conexão PostgreSQL/polling/NOTIFY, emite `evento.novo`, ou deixa stream vivo após logout/unmount: bloquear promoção.
- [ ] Plano SQL filtra inelegíveis após window/group/limit, executa scan correlacionado por linha, ou excede p95 `3 s` (`8 s` export): bloquear e abrir TODO separado de schema/index.
- [ ] Abort com candidato in-flight restaura config antes do terminal, ou candidato fica active durante cancel sem migrar para `REC-3`: interromper ações concorrentes, classificar estado real e seguir somente a transição canônica.
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
- [ ] Conexão writer cai com commit incerto: Promise assenta por rejeição/libera lease exact-once sem SSE/retry; a mesma sessão server-side conserva transaction+fence até encerrar, bloqueando opener/Rollback mesmo com `ativos=0`.
- [ ] Read/auth bursts disputam capacidade: read pool4 pode enfileirar, mas não afeta writer1/control1; qualquer P2024, readiness !=60/60, p95 control >500 ms, read >3 s ou >6 conexões reprova a topologia.
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
- [ ] **Assumption:** o binding PostgreSQL é direto/session-affine, exclusivo e permite `pg_stat_activity`/`pg_locks`. **Unknown:** fatos efetivos até probe redatado pré-changeset/pré-merge. **Confidence:** `Low`. **Handling:** prova obrigatória antes de `REC-2A`; multiplexing/ACL/visibilidade inconclusivos abortam o merge.
- [ ] **Assumption:** o runner preflighted permanecerá disponível durante toda a janela. **Unknown:** falha inesperada depois do merge. **Confidence:** `Medium`. **Handling:** health do runner durante a janela; perda pré-merge aborta, perda pós-merge mantém fail-closed e registra breach explícito do objetivo de 10 min.

## Security Risk Assessment

- **Risk level:** `high`
- **Why this risk level:** dois tokens fiscais, CNPJs, HMAC, dados autenticados e configuração de produção.
- **Attack surface in scope:** secret store, logs/ingress, probes, binding, noteId/refId, monitor token, Bearer/SSE, CSV/spreadsheet, deploy output, responses e rollback.
- **Attack simulation decision:** `required before Stage cutover`
- **Required result:** nenhum vazamento/query credential, JWT em URL/log, usuário inativo no stream, spreadsheet formula, input fora de bound, cross-context, SSRF/redirect ou noteId antigo/corrompido.
- **Current status:** `pending`.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `high`
- **Why this level:** cada réplica multiplica concorrência/rate contra API externa; payload aceito pode chegar a 2 MiB; tratamento unitário/lote e realtime alteram uma superfície de escrita sobreposta.
- **Current delivery stage at review time:** `Pending, Provisional, review`

| Policy Schema Version | Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Trigger Rationale | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code | Recorded At UTC | Executor ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `pcv-1` | `EPS` | `endpoint-performance-scrutiny` | `required` | `high` | `EPS-QUERY-SHAPE-CHANGED` | queries de lista/agregação/export/detalhe/histórico mudam eligibility, paginação e ordenação; paths fiscais externos permanecem materiais | `before_local_implemented` | `EPS-E2` | `pending` | seletividade real de Stage e quota Smart Notas permanecem desconhecidas até evidência autorizada | `none` | `2026-09-28T04:01:17Z` | `codex-primary` |
| `pcv-1` | `FRC` | `frontend-race-condition-validation` | `required` | `high` | `FRC-STALE-RESPONSE` | troca de contexto/cache, reconexão fetch-SSE, logout/unmount e burst de 500 tratamentos podem sobrepor reads e invalidações | `before_local_implemented` | `FRC-E3` | `pending` | navegador Stage customer-facing só é provado no cutover | `none` | `2026-09-28T04:01:17Z` | `codex-primary` |
| `pcv-1` | `BCI` | `backend-concurrency-idempotency-validation` | `required` | `high` | `BCI-LOST-UPDATE-RISK` | PATCH/lote e writer legado/candidato durante activation/rollback podem gravar comandos conflitantes na mesma ref | `before_local_implemented` | `BCI-E3` | `pending` | replay é novo comando; clients4/1/1, writer session fence/PID/pg_locks, five counts, epoch-CAS, exact-once settle, uncertain commit e runner preflight/post-switch foram desenhados mas não provados; treatments ficam indisponíveis >=30 s e enquanto fence/prova não convergir | `none` | `2026-09-28T04:01:17Z` | `codex-primary` |
| `pcv-1` | `RLS` | `runtime-load-stress-validation` | `required` | `high` | `RLS-SLO-CLAIM` | há SLOs explícitos, bulk 500, SSE, limite 2 MiB, budgets externos e pressão de memória/concorrência | `before_local_implemented` | `RLS-E3` | `pending` | quota real do provedor e pressão do OCI Railway permanecem até probe/observação | `none` | `2026-09-28T04:01:17Z` | `codex-primary` |

### EPS planned evidence

- **Access-pattern classification:** `bounded-list|aggregation|exact-lookup|mutation`; o predicado original-`ERRO` deve entrar no SQL antes de count/group/order/limit/mutation, e lookup por ref permanece direto e bounded.
- **Evidence contract:** `EPS-SP-STRONG` / `EPS-A2`; touched-path audit, anti-pattern audit, planos `EXPLAIN` JSON redatados e benchmarks separados de `VAL-CUT-17` em `foundation_documentation/artifacts/tmp/uninotas-cutover-pcv/eps-pcv1.json`.

### FRC planned evidence

- **Concurrency policies:** `cancel previous` para troca de contexto/lista; `drop duplicate` para submit enquanto mutation está em flight; `last-write-wins` somente para invalidação/refetch coalescida; cancelamento obrigatório no logout/unmount.
- **Evidence contract:** `FRC-SP-H` / `FRC-A1`; runner determinístico nos bursts 5/10/20, troca rápida/out-of-order/lifecycle e lote de 500 em `foundation_documentation/artifacts/tmp/uninotas-cutover-pcv/frc-pcv1.json`.

### BCI planned evidence

- **Invariant ID:** `CUT-TREATMENT-SERIAL-APPEND-01` — para cada ref elegível, todo comando aceito persiste exatamente um append monotônico sob lock; nenhum inelegível, retry incerto ou writer cross-version simultâneo ocorre; lote é atômico; SSE não antecede commit nem excede um sinal por append no processo.
- **Concurrency policy:** `serialize` por writer client pool1 e lock namespaced/order lexical. Clients Prisma read4/writer1/control1, wait2, total6; `ReadCommitted`, transaction15, lock1,5, statement12, gate1 e teto500 locks. Read capacity não é reserva implícita; control é isolado. Timestamp é `max(clock,previous+1us)`. Somente abort provado `40P01|40001|55P03|P2034` recebe retry 25 ms; capacity/timeout/fence/connection/commit incerto exigem refresh. Lease libera exact-once no settle; writer session fence/PID/pg_locks, não `ativos`, governa exclusão cross-boot.
- **Evidence contract:** `BCI-SP-H` / `BCI-A1`; PATCH/lote 5/10/20, mixed-load60/readiness 1 Hz, clients4/1/1/total6, direct/session-affine/multiplex-negative, UUID/names/five counts, writer fence ocioso/session-loss/no-auto-reacquire, wait30/manual-open, epoch-CAS/stale409, exact-once/commit incerto, legacy+candidata pós-switch e restart. Validar status/side effects/retry, connections/locks/PIDs/sessions, linhas/atomicidade/epoch/polling/SSE em `foundation_documentation/artifacts/tmp/uninotas-cutover-pcv/bci-pcv1.json`.

### RLS planned evidence

- **Workload model:** `RLS-SP-H` com load, stress e recovery sobre stub loopback, budgets `10 s/4/15/60`, payload near-2MiB, bulk 500 e stream; nenhuma carga destrutiva alcança Smart Notas/Stage.
- **Evidence contract:** `RLS-A1`; thresholds/métricas de `VAL-CUT-05`, incluindo p50/p95/p99, throughput, status, RSS/heap, saturação e recovery em `foundation_documentation/artifacts/tmp/uninotas-cutover-pcv/rls-pcv1.json`.

### Common `pcv-1` artifact rule

- Cada lane em `running|passed` deve registrar no TODO o evidence object completo. O JSON machine-checkable inclui todos os campos obrigatórios do `pcv-1`; `artifact_sha256` é SHA-256 da serialização JSON UTF-8 com chaves recursivamente ordenadas, arrays preservados e sem whitespace, excluindo o próprio campo durante o cálculo. Evidência somente em prosa ou somente por status HTTP não satisfaz o gate.

## Audit and Independent Review Gates

- **Audit escalation:** `required; high-risk release and runtime/infra change`.
- **Independent no-context critique:** `required after plan freeze and before APROVADO`.
- **Independent test-quality audit:** `required before Stage cutover`.
- **Independent final review:** `required after implementation and before Stage cutover`.
- **Dedicated triple review:** `required because release-critical + secrets + external provider`.
- **Current status:** `round-21 architecture clean; critique findings integrated in round-22 candidate; both confirmations pending publication`.

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
- **Critique status:** `findings_integrated`
- **Findings summary:** reviewer `fresh-internal-no-context-critique` retornou `blocked`: três high (`R21-OPS-BCI-01`, `R21-PERF-01`, `R21-OPS-02`) e um medium (`R21-ADH-01`). Todos foram integrados no candidato round 22; nenhuma autoridade de implementação foi concedida.

| Finding ID | Resolution (`Integrated|Challenged|Deferred`) | Usefulness (`useful|noise|mixed|unknown`) | Formalizable (`yes|partial|no|unknown`) | Candidate Rule Level (`paced|project|none|unknown`) | Candidate Rule ID | Rationale / Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `R21-OPS-BCI-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-CANDIDATE-BOOT-FENCING` | A decisão `D-CUT-24` usa writer pool1 + advisory session fence/PID/pg_locks; idle/loss/no-auto-reacquire entram em `VAL-CUT-21`. |
| `R21-PERF-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-DB-POOL-READINESS-HEADROOM` | A decisão `D-CUT-23` substitui headroom implícito por clients4/1/1 e thresholds mixed-load60 em `VAL-CUT-20`. |
| `R21-OPS-02` | `Integrated` | `useful` | `yes` | `project` | `CUT-EXTERNAL-RUNNER-PREFLIGHT` | runner/ACL/classifier são gate read-only pré-changeset/pré-merge; RTO é condicionado e perda pós-merge vira breach fail-closed. |
| `R21-ADH-01` | `Integrated` | `useful` | `yes` | `project` | `CUT-RECOVERY-EVIDENCE-PHASE-SEPARATION` | A validação `VAL-CUT-08` virou simulação/fatos read-only e `VAL-CUT-22` é evidência real condicional ao abort alcançar REC-3. |

- **Evidence / reference:** dispatch `/tmp/uninotas-cutover-round21-critique.ud5izP/dispatch.json`; result/merge schema-valid; reviewer assessment `blocked`, performance/elegance `mixed`, structural/operational `regresses`; audit fingerprint `453bba9462e3`.
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
- **Evidence / reference:** `Overall outcome: go`; sete assumptions vivas verificadas; `A-CUT-01..12` possuem anchors em Railway, config/health/logs, Prisma service/module, env e artifacts adjacentes.

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
| `delphi-ai/skills/rule-prisma-prisma-schema-migration-always-on/SKILL.md` | três clients, transactions e pool contract Prisma 6.5 | major/lockfile, geração e URL seguras | latest tooling ou pool implícito | schema permanece fora; harness prova sessão/PID |
| `delphi-ai/skills/wf-prisma-change-schema-migration-contract-method/SKILL.md` | query/transaction/pool boundary muda sem schema | scripts/version owner e client state coerentes | db push/migration inventada | nenhum DDL; `prisma generate`/tests no CI |
| `delphi-ai/skills/rule-postgresql-postgresql-data-integrity-always-on/SKILL.md` | readiness, logs, advisory locks e recovery | queries bounded, lock order/timeouts, pool budget total6 e credencial protegida | schema ou sessão-fence não provado | schema permanece fora de escopo |
| `delphi-ai/skills/wf-postgresql-change-relational-contract-method/SKILL.md` | lock/session/pool/recovery contract muda | key/PID/pg_locks, roles/ACL e session-affinity testados | assumir snapshot como fence | BCI + runner preflight obrigatórios |
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
- `approval final também aceita topologia PostgreSQL read4/writer1/control1 (máximo seis conexões na única réplica), mutation gate1, advisory session fence verificado por PID/pg_locks e objetivo de rollback de 10 minutos condicionado ao runner preflighted; perda pós-merge é breach fail-closed.`
- `antes do deploy, o Owner deve atestar se existe consumidor externo de sucesso em /eventos/logs; se existir ou permanecer desconhecido, o deploy fica bloqueado até coordenação ou novo aceite explícito de hard cut.`
- `approval final também aceita o gitlink MonitorNotes intencionalmente atrás da Foundation pós-cutover até o próximo product release aprovado, evitando segundo auto-deploy documental.`

## Early Approval Signal

- **Received:** `Aprovado`, em 2026-09-27, incluindo autorização contextual para os checkpoints Git propostos.
- **Accepted decisions:** `D-CUT-07`, avanço do cutover e commit/push do candidato para revisão.
- **Authority effect:** `checkpoint Git concluído`; não autoriza deploy, alteração de variáveis Railway nem tráfego fiscal.

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Reason:** contrato e checkpoint publicados; revisões e gates operacionais ainda precedem qualquer implementação remota/deploy.
