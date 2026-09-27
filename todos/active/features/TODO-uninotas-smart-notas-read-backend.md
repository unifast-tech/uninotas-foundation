# TODO — Entregar leitura Smart Notas por contexto fiscal no backend UniNotas

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Created:** `2026-09-26`
- **Owner:** `Delphi / Operational Coder`, sob autoridade humana do usuário

## Context

O runtime atual ainda lê notas e eventos da projeção PostgreSQL `logs`. A arquitetura canônica de UniNotas já estabelece Smart Notas como única autoridade de notas/documentos e distingue Unifast e Prosperar como valores de `FiscalIssuerContext`, sem tenancy. O primeiro corte funcional precisa criar a fronteira NestJS read-only que permita ao frontend futuro listar e detalhar notas de um único contexto fiscal por vez, sem fallback de sucesso em `logs` e sem persistir espelho local.

## Framing Source & Story Slice

- **Feature brief:** `artifacts/feature-briefs/uninotas-smart-notas-central.md`
- **Primary story ID:** `ST-03` (subslice backend `list + detail`)
- **Why this is the right current slice:** entrega uma capacidade de valor independente e verificável, destrava o frontend e mantém DANFE/XML, cache React, falhas de integração e mutações em conversas de risco separadas.
- **Direct-to-TODO rationale:** `n/a — feature brief existente`.

## Contract Boundary

- Este TODO define **WHAT** será entregue e o que conta como concluído.
- `Assumptions Preview` e `Execution Plan` definem **HOW** a entrega está planejada.
- O contrato é **bounded but elastic** apenas para refinamentos locais da mesma fronteira read-only `list + detail`.
- Qualquer mudança em escopo, contrato HTTP, autorização, persistência, validação obrigatória ou decisões congeladas exige atualização deste TODO e novo `APROVADO`.
- Não há bridge temporária, dual-read ou fallback: a nova rota de notas consulta somente Smart Notas.

## Implementation Intent

- **Current delivery:** candidato local do módulo NestJS `fiscal-notes` com lista e detalhe Smart Notas por contexto fiscal, normalização defensiva, configuração validada e testes; não promove ainda o owner canônico nem ativa produção.
- **Planned next steps:** abrir `todos/active/features/TODO-uninotas-smart-notas-read-cutover.md` antes do closeout para injetar segredos, calibrar réplica×quota, comprovar sink de auditoria, habilitar/deployar, smoke/rollback, rotação HMAC e promover ownership; depois TODO React, DANFE/XML e falhas/casos.
- **Anticipatory implementation authorized now:** `none`.
- **Rationale:** o corte cria a menor fronteira funcional completa que respeita a autoridade Smart Notas e pode ser consumida sem acoplar o backend ao frontend ou ao PostgreSQL.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Next exact step:** solicitar `APROVADO`; após a resposta exata, ingerir regras, repetir routing/authority guards e iniciar a implementação test-first.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** contrato congelado, revisões independentes sem achados materiais e authority guard em `preflight-go`; aguarda somente aprovação humana explícita.
- **Exit condition:** implementação e validação locais concluídas, seguida pelos gates de revisão e promoção aplicáveis.

## Provisional Notes

- **Missing for production-ready:** cutover/runtime separado com segredos injetados, `SMART_NOTAS_READ_ENABLED=true`, probes dos dois emissores, promoção atômica do owner canônico e deploy validado; este TODO pode chegar somente a `Local-Implemented`.
- **Revisit criteria:** remover `Provisional` somente no TODO de cutover após ativação/promocão/deploy comprovados; não remover ao concluir apenas a implementação local.
- **Dependencies unblocked:** este candidato local destrava o TODO React e a preparação do cutover sem declarar a nova rota como runtime atual.

## Blocker Notes

- **Blocker:** `resolved` — matriz read-only confirmada.
- **Why blocked now:** `n/a`; o usuário resolveu a decisão em 2026-09-26.
- **What unblocks it:** `n/a`; todos os perfis ativos foram autorizados para ambos os contextos, somente leitura.
- **Owner / source:** usuário/produto; decisão explícita: “Todos os setores podem visualizar”.
- **Last confirmed truth:** `ADMIN|GESTOR|ANALISTA|LEITOR` ativos podem consultar Unifast e Prosperar; nenhuma permissão fiscal de escrita foi concedida.

## Scope

- [ ] `SCOPE-01` Criar módulo NestJS owner de notas fiscais com controller fino, serviço de aplicação, porta explícita e adapter Smart Notas substituível.
- [ ] `SCOPE-02` Expor `GET /api/v1/notas` com contexto fiscal obrigatório, intervalo de datas obrigatório, filtros publicados pelo provedor e paginação de uma única conta por chamada.
- [ ] `SCOPE-03` Expor `GET /api/v1/notas/:noteId` usando identificador opaco, assinado e context-bound; o consumidor não envia token, CNPJ ou `idInterno` cru como chave da rota.
- [ ] `SCOPE-04` Resolver `unifast|prosperar` exclusivamente no backend para pares independentes de token/CNPJ configurados por ambiente.
- [ ] `SCOPE-05` Normalizar lista/detalhe em DTOs explícitos, preservando status fiscal do provedor, nullabilidade, datas locais e valores decimais como strings.
- [ ] `SCOPE-06` Mapear falhas e timeouts do provedor para erros estáveis, sanitizados e não vazios; falha Smart Notas nunca vira lista vazia nem consulta de sucesso ao PostgreSQL.
- [ ] `SCOPE-07` Adicionar ativação segura por `SMART_NOTAS_READ_ENABLED=false`: credenciais são exigidas fail-fast apenas quando habilitada; documentar nomes/semântica em `.env.example` e README sem valores secretos.
- [ ] `SCOPE-08` Corrigir o filtro global para nunca devolver/logar query string nem valores de parâmetros dinâmicos; cobrir configuração, autorização, codec `noteId`, adapter, serviço, controller/wiring, limites de capacidade e erros com testes determinísticos.
- [ ] `SCOPE-09` Consolidar o contrato candidato nas seções `target_planned` de `modules/fiscal-notes-and-documents.md` e `modules/runtime-and-deployment.md`, preservando o owner/runtime atual até TODO de cutover.
- [ ] `SCOPE-10` Aplicar limite por instância de chamadas upstream, cancelamento por desconexão/timeout, zero retry e logs operacionais sanitizados com contexto, operação, outcome e duração, sem identificador fiscal ou PII.
- [ ] `SCOPE-11` Fixar origin/base path Smart Notas, rejeitar redirect, aplicar rate budget por ator/contexto, excluir PII do DTO, emitir `Cache-Control: no-store` e auditoria read-only sanitizada.

## Out of Scope

- [ ] Frontend React, seletor visual, cache de navegação ou qualquer arquivo em `frontend/**`.
- [ ] PDF/DANFE, XML, relatórios fiscais, exportação CSV, polling ou webhooks.
- [ ] Emissão, cancelamento, empresa, produtos ou qualquer chamada Smart Notas mutável.
- [ ] Lista agregada “Todos”, merge de páginas ou busca simultânea entre contextos.
- [ ] Prisma, schema/migration PostgreSQL, espelho/cache persistente de notas ou alterações em `logs`.
- [ ] Fila de erros de integração, correlação com notas, `OperationalCase` ou migração de tratamentos.
- [ ] Docker, Railway, domínio/ingress, mudança de deploy ou rotação operacional de credenciais.
- [ ] Permissões dinâmicas ou diferentes por emissor; a matriz estática read-only do primeiro corte será definida em `D-06`.
- [ ] Ativar a flag em produção, injetar/rotacionar segredos, promover `note_read_model`, alterar `scope_subscope_governance.md`, retirar `/eventos` ou declarar o módulo como `current_runtime`.
- [ ] Worktrees, checkouts auxiliares, `worker/*` ou `reconcile/*`.

## Delivery Status Semantics

- `Pending`: nenhuma entrega material concluída.
- `Local-Implemented`: implementação e validação local concluídas no branch declarado.
- `Lane-Promoted`: mudança integrada ao threshold definido pelo fluxo do repositório.
- `Production-Ready`: gates finais e promoção exigida concluídos.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `MonitorNotes:delphi-and-foundation`; `uninotas-foundation:main`
- **Promotion lane path:** `MonitorNotes: delphi-and-foundation -> fluxo remoto vigente`; `uninotas-foundation: main -> origin/main`
- **Lane-promoted threshold for this TODO:** `n/a — este corte termina em Local-Implemented, Provisional; promoção/ativação pertence ao TODO de cutover`.
- **Production-ready threshold for this TODO:** `n/a — proibido reivindicar Production-Ready neste TODO`.

## Promotion Evidence

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| Backend Smart Notas read | `delphi-and-foundation@pending` | `pending` | `n/a until lane discovery` | `n/a until lane discovery` | `planned` |
| Foundation module/TODO | `main@7a1c7a2` | `n/a — main-only authority` | `n/a` | `origin/main@7a1c7a2` | `planning baseline published` |

## Diff Expectation Contract

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `delphi-and-foundation@5b4f5aeb1ef13b5b810f0b524d12c582954fadbf` | `working_tree` |
| `uninotas-foundation` | `foundation_documentation` | `main@8a7de8b471868b94e453268e43e2760d0b3292bc` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `A|M` | módulo, DTOs, porta, adapter, codec e testes do corte read-only |
| `MonitorNotes` | `backend/src/app.module.ts` | `M` | registrar o novo módulo |
| `MonitorNotes` | `backend/src/config/configuration.ts` | `M` | resolver e validar configuração Smart Notas |
| `MonitorNotes` | `backend/src/config/configuration.spec.ts` | `M` | provar parsing/validação da configuração |
| `MonitorNotes` | `backend/src/common/filters/all-exceptions.filter.ts` | `M` | substituir URL crua por template de rota sanitizado em resposta/log |
| `MonitorNotes` | `backend/src/common/filters/all-exceptions.filter.spec.ts` | `A|M` | provar ausência de query, `noteId`, documento e `idCompra` em erro/log |
| `MonitorNotes` | `backend/.env.example` | `M` | documentar nomes e semântica sem segredo |
| `MonitorNotes` | `backend/README.md` | `M` | documentar endpoints e configuração operacional |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | promover contrato da capacidade entregue |
| `uninotas-foundation` | `modules/runtime-and-deployment.md` | `M` | registrar fronteira de configuração sem valores |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-smart-notas-read-backend.md` | `A|M|D|R` | contrato e evidência da entrega |
| `uninotas-foundation` | `todos/completed/features/TODO-uninotas-smart-notas-read-backend.md` | `A|R` | destino de closeout após gates |
| `uninotas-foundation` | `todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md` | `M` | apontar handoff da descoberta para o TODO funcional |
| `uninotas-foundation` | `artifacts/publication-manifest.txt` | `M` | publicar os paths governados do TODO |

### Not Expected Changed Paths

| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `frontend/**` | `any` | frontend pertence a TODO posterior |
| `MonitorNotes` | `backend/prisma/**` | `any` | nenhuma persistência de nota neste corte |
| `MonitorNotes` | `docker-compose.yml|Dockerfile|railway*` | `any` | runtime/deploy fora do escopo |
| `MonitorNotes` | `backend/.env` | `any` | segredo local não é alterado nem versionado |
| `MonitorNotes` | `backend/package.json|backend/package-lock.json` | `any` | Node 22 `fetch` atende o adapter; dependência nova não é esperada |
| `uninotas-foundation` | `project_constitution.md|project_mandate.md|system_roadmap.md` | `any` | canon estratégico já suporta o corte e não será reaberto pelo perfil operacional |
| `uninotas-foundation` | `policies/scope_subscope_governance.md|deterministic/capability_identity_ledger.json|deterministic/validate_foundation.py` | `any` | ownership/cutover canônico permanece planejado e pertence ao TODO de ativação |

### Diff Deviation Analysis

| Diff item | Classification | Evidence / agent defense | Decision | User validation / renewed approval |
| --- | --- | --- | --- | --- |
| `none` | `not_triggered` | guard ainda não executado | `n/a` | `n/a` |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** DTO/helper/teste local necessário ao mesmo contrato list/detail; pequenas correções documentais nos dois módulos âncora.
- **Must update or split the TODO:** documentos fiscais, cache, agregação, persistência, nova autorização, mutação fiscal, nova dependência ou mudança de deploy.

## Frozen Public HTTP Contract

### Authorization and activation

- Ambos os endpoints exigem JWT normal pelo guard global e permitem `ADMIN|GESTOR|ANALISTA|LEITOR`; o primeiro corte não diferencia setor, perfil ou emissor e não concede escrita fiscal.
- A janela canônica atual é aceita explicitamente: desativação pode levar até 30 segundos para surtir efeito por causa do cache da `JwtStrategy`; testes cobrem acesso imediato após cache aquecido e negação após expiração. Mudança de perfil não altera acesso porque os quatro perfis são permitidos.
- `SMART_NOTAS_READ_ENABLED=false` é o default seguro. Nesse estado, nenhuma chamada externa ocorre e as rotas respondem `503/SmartNotasDesabilitado`; o TODO de cutover injeta segredos e habilita a capacidade.
- Respostas `200` usam `Cache-Control: no-store`. O primeiro contrato exclui PII por padrão: nome/documento/e-mail/telefone/endereço/inscrições do tomador e retorno bruto não são expostos.

### `GET /api/v1/notas`

- Query obrigatória: `contextoFiscal=unifast|prosperar`, `dataInicio=YYYY-MM-DD`, `dataFim=YYYY-MM-DD`.
- Query opcional: `status`, `documento`, `idCompra`, `pagina` (default `1`). Campos desconhecidos são rejeitados pelo `ValidationPipe` global.
- `status` aceita somente `Pendente|Autorizada|Cancelada|Aguardando|Aguardando Cliente|Denegada|Pausada|Anulada`; um status novo recebido do provedor continua sendo devolvido literalmente em `providerStatus` e não quebra o decoder.
- `documento` aceita exatamente 11 ou 14 dígitos; `idCompra` aceita 1..100 caracteres após trim; `pagina` aceita inteiro 1..10000; intervalo é inclusivo, ordenado e limitado a 366 dias.
- Uma request consulta exatamente uma página de exatamente um contexto; não há page-walk, merge, prefetch ou fallback.

Resposta `200`:

| Campo | Tipo / nullability | Regra |
| --- | --- | --- |
| `items` | `FiscalNoteSummary[]` | sempre presente, máximo 1000; vazio somente após `200` válido |
| `page` | safe integer `1..10000` | página reportada pelo provedor |
| `perPage` | safe integer `1..1000` | não é controlável pelo consumidor; `items.length <= perPage` |
| `total` | safe integer `0..9007199254740991` | total provider-scoped |
| `totalPages` | safe integer `0..10000` | nunca combinado entre emissores |

`FiscalNoteSummary` sempre contém todas as chaves abaixo. Somente campo declarado nullable e realmente ausente ou `null` normaliza para `null`; valor presente vazio, com tipo/formato/range inválido, invalida toda a resposta. Invariantes ausentes também invalidam:

| Campo | Tipo | Nullability / semântica |
| --- | --- | --- |
| `noteId` | string | obrigatório; identidade UniNotas opaca-by-contract |
| `fiscalContext` | `unifast|prosperar` | obrigatório, resolvido pelo backend |
| `providerStatus` | string | obrigatório, não vazio; vocabulário aberto na saída |
| `fiscalNumber`, `accessKey`, `purchaseId` | string | nullable; nunca são identidade da rota |
| `environment`, `model`, `purpose`, `platform`, `product` | string | nullable |
| `scheduledIssueDate`, `paymentDate` | `YYYY-MM-DD` | nullable; datas `DD/MM/YYYY` são normalizadas sem timezone |
| `competence` | string | nullable; preserva datetime sem inventar offset |
| `unitValue`, `totalValue` | decimal string | nullable; forma canônica sem binary float |

Decoder bounds congelados:

- `providerStatus`: string trimada 1..64; vocabulário aberto. `providerIdInterno`: regex/bound do contrato `noteId`.
- `fiscalNumber|accessKey|purchaseId`: string 1..128; `environment|model|purpose|platform`: 1..64; `product`: 1..500.
- `scheduledIssueDate|paymentDate|issueDate`: `DD/MM/YYYY` válido na entrada e `YYYY-MM-DD` válido na saída; `competence`: string ISO-like 1..64, sem inventar timezone.
- `unitValue|totalValue|quantity`: decimal não negativo canônico, até 15 dígitos inteiros e 6 fracionários; exponent, `NaN`, infinito, sinal negativo e binary float são rejeitados.
- `referencedAccessKey`: string 1..128; `operationNature`: string 1..255. Limites são contados em Unicode code points após trim; strings vazias são malformadas, não `null`.
- Pagination usa `Number.isSafeInteger`, os bounds da tabela e coerência `items.length <= perPage`; propriedades provider extras são ignoradas dentro do adapter, mas nunca propagadas.

### `GET /api/v1/notas/:noteId`

- Não aceita `contextoFiscal`, CNPJ ou identificador do provedor. O `noteId` determina o contexto confiável e dispara uma única chamada direta a `/notas/{idInterno}`; é proibido procurar a nota caminhando páginas da lista.
- Resposta `200` contém todos os campos de `FiscalNoteSummary` e acrescenta, sempre presentes porém nullable: `issueDate: YYYY-MM-DD|null`, `referencedAccessKey: string|null`, `operationNature: string|null` e `quantity` como decimal string ou `null`.
- `providerIdInterno`, nome/documento/e-mail/telefone/endereço/inscrições do tomador, `retorno` bruto e payload bruto não fazem parte do contrato público. Ampliar campos pessoais exige decisão própria no TODO do consumidor.

### Opaque `noteId` integrity contract

- Formato: `v1.<payload-base64url>.<mac-base64url>`, máximo 512 caracteres; payload JSON canônico contém somente `{c: fiscalContext, i: providerIdInterno}`.
- MAC: HMAC-SHA-256 com `SMART_NOTAS_NOTE_ID_SECRET_BASE64`, decodificado para no mínimo 32 bytes; comparação usa `timingSafeEqual` após validar comprimentos.
- “Opaco” significa que consumidores não podem construir, decodificar ou depender do conteúdo. HMAC garante integridade, não confidencialidade; por isso o valor também é redatado de logs/erros.
- Somente `v1` e uma chave ativa são aceitos neste corte. Rotação invalida IDs anteriores, que são recuperáveis por nova listagem; rotação multi-chave pertence ao cutover/hardening.
- `providerIdInterno` decodificado deve ser string no formato documentado `^SN-[A-Za-z0-9-]{1,124}$`; qualquer valor fora do bound invalida o token. O adapter ainda aplica `encodeURIComponent` e concatena exatamente um segmento, nunca uma URL fornecida pelo payload.

### Credential destination and pairing

- A base efetiva é fixada ao origin `https://app.smart-notas.com` e base path `/api`. `SMART_NOTAS_BASE_URL`, quando presente, deve ser exatamente esse valor canônico, sem userinfo, query, fragmento ou path alternativo; testes usam override de DI, não configuração de produção.
- `fetch` usa `redirect: manual`; qualquer `3xx` é rejeitado sem seguir nem reenviar `Authorization`/CNPJ. Paths são construídos internamente a partir da base fixada.
- Cada contexto é um objeto indivisível `{token,cnpj}` na configuração; não existem lookups independentes que possam cruzar token de um emissor com CNPJ do outro.
- O probe opt-in chama `/empresa` para cada par, compara o CNPJ normalizado ao esperado e bloqueia cutover em mismatch antes de habilitar tráfego.

### Stable error catalog

| HTTP | `erro` estável | `mensagem` estável | Condição |
| --- | --- | --- | --- |
| `400` | `ConsultaDeNotasInvalida` | `Parâmetros da consulta de notas são inválidos.` | query, intervalo, bound ou `noteId` estruturalmente inválido/adulterado |
| `401` | contrato JWT atual | contrato JWT atual | token UniNotas ausente/inválido/inativo segundo a janela canônica |
| `404` | `NotaFiscalNaoEncontrada` | `Nota fiscal não encontrada.` | Smart Notas devolve 404 no detalhe |
| `429` | `LimiteDeConsultaExcedido` | `Limite temporário de consultas atingido.` | budget local por ator ou contexto; inclui `Retry-After`, sem chamada upstream |
| `sem resposta` | `client_aborted` apenas em métrica/log | `n/a` | cliente desconectou; aborta upstream e não escreve no socket |
| `502` | `SmartNotasDestinoInvalido` | `Destino configurado para o provedor é inválido.` | redirect upstream ou destino fora do allowlist |
| `502` | `SmartNotasCredencialRejeitada` | `O provedor rejeitou a configuração fiscal.` | upstream 401/403 com configuração habilitada |
| `502` | `SmartNotasContratoInvalido` | `O provedor retornou dados incompatíveis.` | status 2xx diferente de 200; 200 com JSON/shape/tamanho inválido; list 404; ou qualquer 4xx inesperado, inclusive 400/422 |
| `503` | `SmartNotasDesabilitado` | `Consulta fiscal temporariamente desabilitada.` | flag local desligada |
| `503` | `SmartNotasOcupado` | `Consultas fiscais temporariamente ocupadas.` | limite concorrente por instância; não enfileira |
| `503` | `SmartNotasLimiteExterno` | `O provedor limitou temporariamente as consultas.` | upstream 429; não faz retry |
| `503` | `SmartNotasIndisponivel` | `O provedor fiscal está temporariamente indisponível.` | rede ou upstream 5xx |
| `504` | `SmartNotasTimeout` | `O provedor fiscal excedeu o tempo de resposta.` | timeout local; distinto de disconnect |

- O envelope continua `{statusCode,erro,mensagem,caminho,timestamp}`. Validação Nest das duas rotas é remapeada explicitamente para `ConsultaDeNotasInvalida`; `mensagem` é estável/sanitizada e `caminho` usa o template registrado como `/api/v1/notas/:noteId` ou o fallback fixo `/api/*`, nunca URL/query/path real do cliente.
- Resposta provider maior que 2 MiB é `SmartNotasContratoInvalido`. Nenhum erro vira lista vazia, fallback PostgreSQL ou mensagem/payload cru.
- Campos legitimamente ausentes/nulláveis tornam-se `null`; campo presente com tipo, formato ou range inválido invalida toda a resposta como `SmartNotasContratoInvalido`. Somente `providerStatus` não vazio admite vocabulário futuro literal.

Precedência total / first-signal rule:

1. Roteamento e `JwtAuthGuard` globais: autenticação ausente/expirada/inativa após a janela canônica produz `401` antes de pipes, flag, HMAC ou budgets.
2. `ValidationPipe`: query e forma/tamanho externo do `noteId` produzem `400` antes da flag. Rotas não encontradas usam o `404` atual com caminho público fixo `/api/*`.
3. Flag: request autenticada e sintaticamente válida recebe `503/SmartNotasDesabilitado` antes de verificar MAC ou consumir rate budget.
4. Detalhe habilitado verifica versão/MAC/payload/`providerIdInterno`; falha produz `400` antes de budgets ou semaphore.
5. Rate: precheck atômico síncrono dos budgets do ator e contexto; se qualquer um esgotou, nenhum contador é incrementado e retorna `429`. Caso contrário, ambos incrementam juntos antes do semaphore.
6. Concorrência: semaphore cheio retorna `503/SmartNotasOcupado`; não há fila nem chamada upstream.
7. I/O: client disconnect e timeout competem por abort reason, e o primeiro sinal observado vence. Disconnect fecha sem resposta; timeout com socket aberto retorna `504`. Todo caminho libera slot em `finally`.
8. Provider: `3xx` destino inválido; `401/403`; detail `404`; `429`; `5xx/rede`; demais status/decoder seguem o catálogo, nessa ordem.

Testes de colisão obrigatórios: sem JWT + query inválida; query inválida + flag off; `noteId` sintaticamente inválido + flag off; MAC inválido + flag off/on; rate esgotado + semaphore cheio; disconnect antes/depois do timer; timeout antes/depois do disconnect; redirect e status/provider body inválido.

### Capacity and observability contract

- `SMART_NOTAS_TIMEOUT_MS`: default `10000`, range `1000..30000`; `SMART_NOTAS_MAX_CONCURRENCY`: default `8`, range `1..64`.
- Budgets locais configuráveis e fail-closed: por ator `SMART_NOTAS_RATE_PER_USER_MINUTE=30` (range 1..120) e por contexto `SMART_NOTAS_RATE_PER_CONTEXT_MINUTE=120` (range 1..600), janelas fixas em memória, mapas com limpeza/bound; ambos são aplicados antes do semaphore. O TODO de cutover deve recalibrar `réplicas × budget` contra quota real.
- Sem retry e sem fila local. O fetch é abortado no timeout ou desconexão do consumidor; o slot concorrente é liberado em `finally`.
- Log operacional estruturado do adapter: correlation ID local, operação `list|detail`, contexto fiscal, outcome normalizado, status HTTP upstream quando existir e duração.
- Evento de auditoria read-only pertence ao serviço de aplicação: actor ID interno, operação, contexto, outcome e correlation ID; não inclui query, `noteId`, documento, `idCompra`, CNPJ, Authorization, campos de nota ou payload. O cutover deve comprovar retenção/destino do sink antes de ativar produção.
- O filtro global nunca loga `request.url`, exception message, stack ou erro Prisma cru; usa somente método, template/fallback, código estável, correlation ID e status. Testes incluem rota não encontrada, validação, provider exception, stack canário e Prisma default.

## Definition of Done

- [ ] `DOD-01` Lista context-scoped retorna DTO paginado normalizado e nunca mistura Unifast/Prosperar.
- [ ] `DOD-02` Detalhe resolve `noteId` assinado para um único contexto/`idInterno`, rejeita adulteração e não aceita CNPJ/token arbitrário.
- [ ] `DOD-03` Com a capacidade habilitada, configuração exige base URL HTTPS, credenciais independentes, CNPJs válidos e segredo HMAC base64 de 32+ bytes; desabilitada por padrão, não exige credenciais e nunca chama o provedor.
- [ ] `DOD-04` Ausência/null legítimo, datas e decimais são mapeados defensivamente; valor presente malformado falha como contrato inválido, status futuro não vazio é preservado e payload/PII/retorno bruto não atravessam o contrato público.
- [ ] `DOD-05` Timeout/rede/401/403/5xx/shape inválido produzem falha explícita e sanitizada; 404 de detalhe permanece 404; nenhum caso cai para `logs`.
- [ ] `DOD-06` Controller é fino, integração fica atrás de porta/token explícito e o módulo não importa Prisma.
- [ ] `DOD-07` Testes unitários/integração e build/lint do backend passam no runner declarado.
- [ ] `DOD-08` Probes read-only redatados comprovam lista e detalhe nos dois contextos sem persistir identificadores, payloads ou valores privados.
- [ ] `DOD-09` Módulos canônicos registram o candidato local sem promover ownership: `events-and-classification` continua owner atual e `fiscal-notes-and-documents` continua `target_planned`.
- [ ] `DOD-10` `ADMIN|GESTOR|ANALISTA|LEITOR` passam pelos dois GETs; JWT ausente falha e a janela herdada de revogação de até 30 segundos é aceita/provada até a negação pós-expiração; nenhuma rota fiscal de escrita existe.
- [ ] `DOD-11` Uma request gera no máximo uma chamada Smart Notas; budgets por ator/contexto e concorrência por instância são limitados, disconnect/timeout aborta, `429` local/upstream é explícito e nenhum retry/paginação implícita ocorre.
- [ ] `DOD-12` Respostas e logs de exceção usam template/fallback fixo e nunca incluem URL/path/query real, stack/message cru, `noteId`, documento, `idCompra`, token, CNPJ, Prisma detail ou payload.
- [ ] `DOD-13` O contrato público é provado campo a campo, incluindo nullability, malformed-vs-missing, paginação, status desconhecido, bounds e catálogo exaustivo/precedência de erros.
- [ ] `DOD-14` Origin/base path são fixos, redirects não recebem credenciais, pares token/CNPJ são indivisíveis e verificados; DTOs excluem PII, respostas usam `no-store` e eventos de acesso registram ator/operação/contexto/outcome sem recurso sensível.
- [ ] `DOD-15` Load/stress local contra upstream stub comprova budgets, fairness entre usuários/contextos, máximo concorrente, degradação controlada, abort e recuperação sem tráfego contra Smart Notas real.

## Validation Steps

- [ ] `VAL-01` Rodar `python3 delphi-ai/tools/node_capability_surface_audit.py --repo backend --expect nestjs --manifest package.json --require-script test --require-script build --require-script lint`.
- [ ] `VAL-02` Rodar no backend via Node 22 do host Windows: `npm test -- --runInBand`.
- [ ] `VAL-03` Rodar no backend via Node 22 do host Windows: `npm run build`.
- [ ] `VAL-04` Rodar `npm run lint`, inspecionar qualquer rewrite e repetir testes/build se o lint alterar arquivos.
- [ ] `VAL-05` Executar probe opt-in read-only e redatado para lista/detalhe em `unifast` e `prosperar`; registrar apenas status, shape e ausência de vazamento.
- [ ] `VAL-06` Rodar `python3 foundation_documentation/deterministic/validate_foundation.py --root foundation_documentation` e o `verify_context` canônico do Windows Git Bash.
- [ ] `VAL-07` Rodar guards de diff, autoridade, conclusão e closeout conforme o lifecycle deste TODO.
- [ ] `VAL-08` Rodar teste de aplicação/guard para os quatro perfis nos dois GETs e negativas de autenticação, sem depender apenas de teste estrutural de metadata.
- [ ] `VAL-09` Rodar testes de saturação/abort/timeout/429 e confirmar `one request -> at most one upstream call`.
- [ ] `VAL-10` Rodar teste do filtro global com query/param canários e capturar logger/resposta para provar redaction.
- [ ] `VAL-11` Rodar testes hostis de origin/userinfo/query/fragment/base path/redirect e provar que nenhuma credencial é transmitida ao destino rejeitado.
- [ ] `VAL-12` Rodar teste de privacy contract/no-store/audit event e provar ausência de todos os campos pessoais excluídos.
- [ ] `VAL-13` Rodar RLS-E1 contra stub local com estágios congelados abaixo; capturar p50/p95/p99, throughput, error rate, pico upstream concorrente, respostas controladas 429/503 e recuperação.

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-01..07,DOD-10..15` | `Definition of Done` | contratos, isolamento, autorização, privacidade, capacidade/load, redaction, arquitetura e testes | `code+test` | paths/testes e comandos acima | `backend local` | `planned` | evidência será itemizada antes do claim |
| `DOD-08` | `Definition of Done` | ambos os contextos respondem no adapter real | `runtime` | probe redatado sem dados privados | `Smart Notas read-only` | `planned` | sem mutações |
| `DOD-09` | `Definition of Done` | consolidação target-planned sem cutover | `doc+review` | módulos âncora + registry invariants + validator | `foundation` | `planned` | owner atual preservado |
| `VAL-01..13` | `Validation Steps` | validação completa do corte | `test+review` | comandos listados | `local/foundation` | `planned` | detalhar resultados na entrega |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas OpenAPI | contrato da fronteira externa | `healthy` | `2026-09-26` | SHA-256 `cc2a415962dcff00b7d91d3a1bfe99544ec3bd1543b2e5f9d93df1b8ce686502` | parar/revisar se fingerprint mudar |
| Credenciais Unifast/Prosperar | probes e execução local | `healthy` | `2026-09-25` | `GET /empresa` redatado confirmou cada CNPJ configurado; repetir antes do claim | nunca imprimir/persistir valores |
| Smart Notas quotas/SLA | políticas de retry/load | `unknown` | `2026-09-26` | contrato público não publica limites | zero retry automático; sem polling neste corte |

## Package-First Assessment

- **Queries executed:** `query_packages.sh --search "smart notas"`, `--search "http client"`, `--search "rate limit"`, `--search "semaphore"`, `--stack node --all`.
- **Relevant proprietary packages found:** `none`.
- **READMEs read:** `n/a`.
- **Decision:** implementação host-local atrás de porta/adapter, usando `fetch` nativo do Node 22; nenhuma dependência nova.
- **Tier:** `local host-specific integration`.
- **Rationale:** o adapter é específico do provedor/produto e o runtime já fornece cliente HTTP suficiente.

## Profile Scope & Handoffs

- **Primary execution profile:** `operational-coder`
- **Active technical scope:** `nestjs`
- **Expected supporting profiles:** `assurance-tester-quality`, `assurance-security-adversarial`; handoff documental limitado aos módulos canônicos.
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `operational-coder` | `assurance-tester-quality` | auditar testes e contrato público | backend/tests | `planned` |
| `operational-coder` | `assurance-security-adversarial` | revisar segredo/context isolation/error sanitization | config/adapter/routes | `planned` |

## Complexity

- **Level:** `medium`
- **Checkpoint policy:** `one checkpoint before approval`, mais gates independentes derivados.
- **Why this level:** novo contrato HTTP e integração externa autenticada, com dois contextos e segredos, porém sem escrita, schema, frontend ou deploy.

## Canonical Module Anchors

- **Primary module doc:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Secondary module docs:**
  - `foundation_documentation/modules/identity-and-team.md`
  - `foundation_documentation/modules/runtime-and-deployment.md`
- **Planned decision promotion targets:** `Fiscal Notes and Documents > API Endpoint Definitions/Invariants/Failure Modes`; `Runtime and Deployment > Smart Notas Configuration Boundary`.
- **Module decision consolidation targets:** mesmas seções; `identity-and-team` será preservado e só muda se evidência exigir correção material, o que requer novo approval.

## Decision Pending

- [x] `none — a decisão de acesso foi resolvida pelo usuário; os demais findings foram convertidos em contrato técnico dentro do corte`.

## Decisions (Resolved Before Freeze)

- [x] `D-01` O corte entrega somente lista e detalhe, sob `/api/v1/notas`; módulos documentais/relatórios/mutações ficam fora. Ref: `fiscal-notes-and-documents` + `ST-03` split.
- [x] `D-02` `contextoFiscal=unifast|prosperar` é obrigatório na lista; o backend resolve credenciais e nunca aceita token/CNPJ do consumidor. Ref: invariant de `fiscal-notes-and-documents`.
- [x] `D-03` Smart Notas é a única fonte dessas rotas; não há Prisma, `logs`, fallback de sucesso ou espelho persistente. Ref: constitution/source ownership + módulo primário.
- [x] `D-04` `noteId` será um envelope opaco versionado, autenticado por HMAC com segredo dedicado, contendo somente contexto e `idInterno` necessários à resolução stateless; adulteração é rejeitada antes da chamada externa. Ref: identity contract do discovery.
- [x] `D-05` Lista exige `dataInicio`/`dataFim` ISO date, intervalo inclusivo coerente e máximo de 366 dias; filtros são `status`, `documento`, `idCompra`, `pagina`. Ref: OpenAPI/P-14.
- [x] `D-06` Todos os setores podem visualizar: `ADMIN|GESTOR|ANALISTA|LEITOR` ativos acessam Unifast e Prosperar, somente leitura; nenhuma permissão fiscal de escrita é criada. Ref: decisão explícita do usuário em 2026-09-26 + `identity-and-team`.
- [x] `D-07` Adapter usa timeout configurável e nenhum retry automático; 401/403/timeout/rede/5xx/shape inválido são indisponibilidade/contrato upstream sanitizado, 404 de detalhe é not-found. Ref: provider gaps API-02/API-06.
- [x] `D-08` Não haverá cache/polling no backend; cache stale-while-revalidate pertence ao TODO React. Ref: SD-08/ST-04.
- [x] `D-09` Controller fino -> serviço de aplicação -> porta -> adapter singleton; tipos wire do provedor não escapam da infraestrutura. Ref: NestJS architecture rule.
- [x] `D-10` Este TODO termina em `Local-Implemented, Provisional`; não altera ownership canônico nem ativa/deploya a capacidade. Cutover atômico pertence a TODO posterior. Ref: registry `planned` + reviewer convergence.
- [x] `D-11` A flag é false por default; quando habilitada, Joi exige pares indivisíveis de credenciais/segredo e o adapter impõe origin fixo/no-redirect, rate por ator/contexto, timeout, concorrência sem fila, cancelamento, 2 MiB e zero retry. Ref: rollout/capacity findings.
- [x] `D-12` `noteId` HMAC é opaco-by-contract, não confidencial; filtro/logs redatam URL, query e parâmetros, e o contrato de erro é o catálogo congelado acima. Ref: security findings.
- [x] `D-13` O primeiro DTO exclui PII de tomador, usa `Cache-Control: no-store` e gera auditoria read-only sanitizada; ampliação de campos depende do TODO consumidor. Ref: data minimization review.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `fiscal-notes-and-documents#authority` | Smart Notas é única fonte; sem aggregate/context leak | `Preserve` | `modules/fiscal-notes-and-documents.md` |
| `fiscal-notes-and-documents#documents` | documentos on-demand pertencem ao módulo | `Out of Scope` | `modules/fiscal-notes-and-documents.md` |
| `identity-and-team#protected-reads` | JWT ativo protege leitura e perfis atuais podem ler | `Preserve` | `modules/identity-and-team.md` |
| `runtime-and-deployment#config` | runtime/config é explícito e sem segredo na Foundation | `Preserve` | `modules/runtime-and-deployment.md` |

## Decision Baseline (Frozen Before Implementation)

- [x] `D-01..D-13` estão congeladas no commit autoritativo registrado em `Gate: Review Baseline Freeze`; implementação continua proibida até revisões, `preflight-go` e `APROVADO`.

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** implementa um candidato local para a futura boundary fiscal, sem promover ainda `note_read_model` nem alterar o owner legado.
- **Deviation / debt being retired:** reconstrução de notas de sucesso a partir de `logs` nas novas superfícies UniNotas.
- **Target steady-state after closeout:** código candidato local list/detail lê apenas Smart Notas por contexto quando habilitado; o canon continua declarando o caminho legado como runtime atual até cutover próprio.
- **Temporary exceptions allowed:** coexistência explícita das rotas legadas `/eventos` e novas `/notas`; não é fallback nem dual-read dentro da mesma capacidade.
- **Cutover / removal condition:** TODO separado injeta segredos, prova os dois emissores, habilita/deploya a flag e promove ownership atomicamente; retirada das rotas legadas só ocorre depois de frontend e error-boundary migrarem.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| Porta/adaptador externo explícito | NestJS rule + P-3/P-10 | `backend/src/fiscal-notes/**` | impede acoplamento de controller ao provedor |
| Context resolution server-side | SD-01/SD-07 + module invariant | config/adapter/routes | evita CNPJ/token arbitrário e mistura fiscal |
| Smart Notas-only note source | D-03 + constitution | list/detail | impede regressão para sucesso em `logs` |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why Forbidden | Exception Policy |
| --- | --- | --- | --- |
| Controller chama `fetch` diretamente | imports/uso de HTTP no controller | mistura transporte e infraestrutura | `none` |
| Nova rota consulta Prisma/logs | imports Prisma/LogsModule em fiscal-notes | cria autoridade concorrente | `none` |
| Credencial/CNPJ fornecido pelo cliente | DTO/query/header público | permite context spoofing | `none` |
| Payload bruto do provedor exposto | DTO público `unknown`/spread raw | vaza dados e contrato instável | `none` |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan |
| --- | --- | --- | --- | --- | --- |
| test | note application/adapter | Jest module/contract specs | context leak, fallback, raw shape, tampered `noteId` | `implement-in-this-todo` | DOD-01..06/VAL-02 |
| test | app wiring/auth | Nest testing module + real global guards | qualquer perfil ativo bloqueado, usuário ausente/inativo aceito, módulo não registrado | `implement-in-this-todo` | DOD-10/VAL-08 |
| test | exception filter | logger/response spies with canary URL | query, identifier ou PII em log/error | `implement-in-this-todo` | DOD-12/VAL-10 |
| structural test | fiscal module imports/exports/decorators | Jest usando TypeScript compiler API: AST de imports/calls/decorators + whitelist de exports | qualquer import `prisma-or-logs` no módulo; `fetch-or-node:http` no controller; `@Public`; tipo wire exportado fora de `infrastructure` | `implement-in-this-todo` | DOD-06/VAL-02 |
| analyzer | NestJS surface | `node_capability_surface_audit.py` | manifest/scripts/capability drift | `already-enforced` | VAL-01 |
| review | code/module diff | architecture adherence review | brittle shortcut/hidden dual-read | `implement-in-this-todo` | final review package |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `no_material_findings`
- **Decision review evidence / resolution:** `round 11 focused formal architecture_opinion over 7a1c7a2 returned GO with no material findings; harness row parses into six columns, semantics remain explicit and routing outcome/evidence are canonical; round 9 full-plan GO and round 10 anchor GO remain valid; reviewer made no changes`.
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending implementation`

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** contrato público/segredos/contextos exigem review a partir de baseline autoritativo reproduzível.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `uninotas-foundation:main`
- **Baseline commit:** `7a1c7a2072df7d5c4862f4a72847adcde31a9e9e`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** baseline congelou a linha do harness com delimiters parser-safe e o resultado de roteamento canônico, sem mudança funcional.
- **Evidence / reference:** commit/push `7a1c7a2072df7d5c4862f4a72847adcde31a9e9e`; `ls-remote refs/heads/main` retornou o mesmo SHA.
- **Waiver authority / reference:** `n/a`.
- **Pre-freeze packet-prep rule:** review rows below are `prepared-pre-freeze`, not passed.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impede que o contrato revisado mude materialmente antes do approval.
- **Trigger stage:** `after review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-backend.md`
- **Gate status:** `no_material_findings`
- **Findings summary:** zero das 22 seções materiais divergiram do baseline final `7a1c7a2`.
- **Evidence / reference:** `review_scope_drift_guard.py` retornou `Overall outcome: go` e `Changed material sections: 0` em 2026-09-27.
- **Waiver authority / reference:** `n/a`.

## Questions To Close

- [x] `Q-01` Resolvida em 2026-09-26: todos os setores/perfis ativos visualizam ambos os emissores, somente leitura.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | Node 22 oferece `fetch` estável sem pacote externo | `Dockerfile` usa `node:22-slim`; `backend/package.json`; bootstrap em `backend/src/main.ts` | reavaliar dependency/package-first | `High` | `Keep as Assumption` |
| `A-02` | JWT global continuará protegendo o novo controller sem guard adicional | `backend/src/app.module.ts`; `backend/src/auth/guards/jwt-auth.guard.ts` | corrigir wiring antes de approval | `High` | `Keep as Assumption` |
| `A-03` | Nenhum módulo Smart Notas/HTTP já existe no backend | inventário de imports/modules em `backend/src/app.module.ts` e `backend/src/logs/logs.module.ts`; node capability audit em 2026-09-26 | reutilizar owner existente | `High` | `Keep as Assumption` |
| `A-04` | Tokens/CNPJs dos dois contextos estão disponíveis localmente | probes redatados em `foundation_documentation/todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md`; boundary atual em `backend/src/config/configuration.ts`; valores permanecem somente no env ignorado | probe real fica bloqueado, implementação/testes mockados continuam | `High` | `Keep as Assumption` |
| `A-05` | O endpoint oficial usado pelos probes permanece `https://app.smart-notas.com/api` | OpenAPI/probes registrados em `foundation_documentation/artifacts/feature-briefs/uninotas-smart-notas-central.md`; boundary de allowlist será implementada em `backend/src/config/configuration.ts`; fingerprint `cc2a415...` em 2026-09-26 | parar, rever allowlist e recongelar antes de transmitir credenciais | `High` | `Keep as Assumption` |

## Execution Plan

### Touched Surfaces

- `backend/src/fiscal-notes/**`, configuração/bootstrap wiring, filtro global de exceções, `.env.example`, backend README, testes Jest.
- Módulos Foundation primário/runtime e lifecycle deste TODO.

### Ordered Steps

1. Ingerir regras vinculantes e confirmar routing/authority após `APROVADO`.
2. Criar testes fail-first para contrato público mínimo/no-store, configuração/origin/redirect, quatro perfis e revogação cacheada, `noteId`, normalização strict, contexto, catálogo exaustivo de erros, auditoria/redaction e rate/concurrency.
3. Implementar DTOs/erros, codec HMAC, porta, serviço de aplicação e teste estrutural sem Prisma/LogsModule.
4. Implementar adapter `fetch` com semaphore fail-fast, timeout/request-abort, resposta máxima de 2 MiB, headers server-side, shape guards, observabilidade sanitizada e zero retry.
5. Corrigir o filtro global para usar template de rota; registrar módulo/controller no AppModule e documentar flag/env/endpoints.
6. Rodar testes/build/lint e RLS-E1 contra stub local; com flag opt-in, repetir `/empresa` binding e probes lista/detalhe redatados nos dois contextos.
7. Consolidar apenas o candidato `target_planned`, rodar audits/guards e encerrar no máximo como `Local-Implemented, Provisional`, abrindo o handoff de cutover.

### Test Strategy

- **Strategy:** `test-first`.
- **Why:** contrato externo genérico e isolamento de contexto exigem falhas explícitas antes do adapter.
- **Fail-first targets:** config disabled/enabled e hostile origin/redirect, quatro perfis + cache de revogação, `noteId` adulterado/segment injection, credencial cruzada, provider 3xx/qualquer 4xx/5xx/timeout, oversize/shape malformed-vs-null, status desconhecido, rate/fairness/saturation/abort, PII/no-store/audit, filtro/stack/Prisma canários e ausência de Prisma/log fallback.

### Pre-APROVADO RED Evidence Capture

- **Decision:** `not_needed`.
- **Why now:** é feature nova, sem sintoma de regressão a reproduzir; código/teste de produto só começa após approval.
- **Status:** `not_run`.

### Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Lista por contexto | payload futuro da tela Geral | `web-only` | backend contract + futuro Playwright no TODO React | `no` | `yes` | test controller + probe redatado | browser deferido porque frontend não muda |
| Detalhe por `noteId` | alimenta detalhe futuro | `web-only` | backend contract + futuro Playwright no TODO React | `no` | `yes` | test controller + probe redatado | browser deferido porque rota UI não muda |

### Frontend / Consumer Matrix

| Producer Surface | Consumer | Contract Impact | Consumer Work In This TODO | Follow-up |
| --- | --- | --- | --- | --- |
| `GET /api/v1/notas` | React Geral | contrato paginado context-scoped, sem PII, `no-store` | `none` | TODO React selector/cache decide qualquer ampliação de campo |
| `GET /api/v1/notas/:noteId` | React detalhe | DTO fiscal mínimo sem PII + erro estável | `none` | TODO React detalhe decide necessidade/masking de PII |
| env Smart Notas | Railway/runtime | flag false por default + variáveis server-only | exemplo/config apenas | TODO cutover injeta segredos e ativa |
| `note_read_model` | capability registry | candidato não altera owner atual | `none` | TODO cutover promove atomicamente |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| backend Jest | lógica/contrato mudam | lista/detalhe/DTO strict/status/bounds/error/config/HMAC/origin/rate/capacity/privacy/redaction | fixtures provider determinísticas + URL/stack/PII canaries + fake timers/abort | `npm test -- --runInBand` | `Local-Implemented` | `planned` | pending | sem dados reais |
| backend app/guard | acesso muda | quatro perfis acessam; sem JWT falha; cache aquecido permite até 30s e nega após expiração | Nest testing app com guards reais, fake timers e adapter fake | `npm test -- --runInBand` | `Local-Implemented` | `planned` | pending | não aceitar teste só de metadata |
| backend local RLS | pressão/capacidade | bursts mistos provam rate/fairness/semaphore/recovery sem exceder stub | Nest local + upstream stub; atores sintéticos; somente loopback | Jest mixed-workload runner + JSON `pcv-1` | `Local-Implemented` | `planned` | pending | RLS-E1 abaixo |
| backend build | novo módulo/DTO | compilação Nest/TS | Node 22 + deps atuais | `npm run build` | `Local-Implemented` | `planned` | pending | runner Windows |
| backend lint | novos arquivos TS | regras estáticas/formatação | deps atuais | `npm run lint` | `Local-Implemented` | `planned` | pending | inspecionar rewrites |
| Smart Notas read probe | integração real | `/empresa` binding + lista/detalhe direto em ambos contextos | env local preenchido; flag opt-in; janela curta | probe opt-in redatado | `Local-Implemented` | `planned` | pending | sem persistir payload/identificador |
| Foundation validator | docs/TODO | coerência/publicação/privacidade | baseline main | validator + verify_context | `promotion` | `planned` | pending | Windows Git Bash para readiness |

### Runtime / Rollout Notes

- `SMART_NOTAS_READ_ENABLED=false` permite que a imagem inicialize sem credenciais e impede chamadas externas; quando true, Joi exige base URL, dois pares token/CNPJ, segredo HMAC, timeout e concorrência válidos.
- Este TODO não liga a flag fora do probe local nem muda `backend/.env`. O deploy precisa receber segredos antes de o TODO de cutover habilitar a flag.
- O cutover também precisa fixar replica count, recalibrar rate/context contra quota do provedor, validar o sink/retention de auditoria, rodar `/empresa`, staged smoke e rollback com flag false.
- As rotas são aditivas e não consumidas pelo frontend atual; coexistem inativas com `/eventos`, sem promover ownership, até o cutover do consumidor.

## Plan Review Gate

- **Status:** `no_material_findings`.

### Review Sections

- [x] Architecture — owner fiscal, porta explícita e source authority preservados.
- [x] Code Quality — controller fino, decoder separado e erros tipados evitam espalhar condicionais.
- [x] Tests — fail-first cobre contrato, wiring, privacidade, auth-cache, origin/redirect, rate/load e falhas; live probe é complementar.
- [x] Performance — rate por ator/contexto, uma chamada, semaphore sem fila, response cap, abort/timeout, zero retry e RLS local limitam amplificação.
- [x] Security — minimização de PII/no-store/audit, origin fixo, segredo dedicado, context resolution, bounds e redaction integral são obrigatórios.
- [x] Elegance — módulo coeso sem dependency nova, Prisma ou dual-read.
- [x] Structural Soundness — coexistência `/eventos` e `/notas` é explícita e sem fallback oculto.

### Issue Cards

- **Issue ID:** `ARCH-01`
  - **Severity:** `medium`
  - **Evidence:** `modules/fiscal-notes-and-documents.md:7-20`; `backend/src/app.module.ts:16-31`; busca do backend sem módulo Smart Notas.
  - **Why it matters now:** a primeira integração pode virar acoplamento direto de controller/provider ou criar uma segunda autoridade de notas.
  - **Option A (Recommended):** módulo fiscal com serviço de aplicação, porta explícita, adapter e DTO normalizado.
    - **Implementation effort:** `medium`
    - **Risk:** `low`
    - **Blast radius:** `module`
    - **Maintenance burden:** `low`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `improves`
    - **Structural soundness impact:** `improves`
  - **Option B:** serviço único chamando `fetch` diretamente do controller.
    - **Implementation effort:** `low`
    - **Risk:** `medium`
    - **Blast radius:** `local`
    - **Maintenance burden:** `medium`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Option C (Do Nothing):** manter notas em `logs`.
    - **Implementation effort:** `low`
    - **Risk:** `high`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `high`
    - **Performance impact:** `unknown`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Recommendation:** `A`, por preservar autoridade única, testabilidade e troca controlada do provedor.

- **Issue ID:** `SEC-01`
  - **Severity:** `high`
  - **Evidence:** `backend/src/config/configuration.ts:28-60`; `backend/src/common/filters/all-exceptions.filter.ts:39-58`; `fiscal-notes-and-documents.md:19-20`.
  - **Why it matters now:** credenciais/contextos e o `noteId` não podem ser controlados pelo consumidor nem aparecer em erros/logs.
  - **Option A (Recommended):** origin fixo/no-redirect, pares indivisíveis, DTO sem PII/no-store/audit, HMAC dedicado e filtro/logs sem dados derivados do request/exception.
    - **Implementation effort:** `medium`
    - **Risk:** `low`
    - **Blast radius:** `module`
    - **Maintenance burden:** `low`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `improves`
    - **Structural soundness impact:** `improves`
  - **Option B:** reutilizar `JWT_SECRET` para assinar `noteId` e confiar no filtro global para sanitização.
    - **Implementation effort:** `low`
    - **Risk:** `medium`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `medium`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Option C (Do Nothing):** expor contexto/`idInterno` cru e erros do provedor.
    - **Implementation effort:** `low`
    - **Risk:** `high`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `high`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Recommendation:** `A`; key separation e sanitização explícita reduzem acoplamento e vazamento.

- **Issue ID:** `PERF-01`
  - **Severity:** `high`
  - **Evidence:** OpenAPI não publica quotas/SLA; `Dockerfile:18-27` confirma Node 22 e build do backend; discovery API-02.
  - **Why it matters now:** retry/cache/polling prematuros podem amplificar tráfego em duas contas sem quota conhecida.
  - **Option A (Recommended):** rate fairness por ator/contexto, uma chamada, semaphore, `AbortSignal`/timeout, zero retry e EPS+RLS-E1 local.
    - **Implementation effort:** `medium`
    - **Risk:** `low`
    - **Blast radius:** `module`
    - **Maintenance burden:** `low`
    - **Performance impact:** `improves`
    - **Elegance impact:** `improves`
    - **Structural soundness impact:** `improves`
  - **Option B:** uma repetição automática em timeout/5xx.
    - **Implementation effort:** `medium`
    - **Risk:** `medium`
    - **Blast radius:** `module`
    - **Maintenance burden:** `medium`
    - **Performance impact:** `unknown`
    - **Elegance impact:** `neutral`
    - **Structural soundness impact:** `neutral`
  - **Option C (Do Nothing):** sem timeout explícito nem budget de chamadas.
    - **Implementation effort:** `low`
    - **Risk:** `high`
    - **Blast radius:** `runtime`
    - **Maintenance burden:** `medium`
    - **Performance impact:** `regresses`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Recommendation:** `A`; mantém pressão previsível sem inventar política do provedor.

### Failure Modes & Edge Cases

- [x] Contexto ausente/inválido, par CNPJ/token trocado, hostile origin/redirect, `noteId`/segment adulterado, intervalo/filtros fora do bound.
- [x] Timeout versus disconnect, DNS, qualquer 3xx/4xx/5xx, rate local/upstream, saturation e resposta oversize/non-JSON.
- [x] Campo ausente/null versus presente malformado, status desconhecido, page fora do range e lista vazia legítima.
- [x] PII/no-store/audit; unmatched path, validation, exception stack e Prisma detail não podem vazar em resposta/log.

### Residual Unknowns / Risks

- [x] Quotas/SLA continuam desconhecidos; mitigação local é rate/concurrency/timeout/zero retry; cutover recalibra orçamento por réplica antes de ativar.
- [x] Shape detail não é formalmente tipado no OpenAPI; live evidence existe, mas decoder permanece defensivo.
- [x] Deploy secret injection é dependência de promoção, não autorização para mudar Railway neste TODO.

## Additional Architectural Opinions

- **Needed:** `yes`.
- **Why ambiguity remains:** HMAC stateless, error mapping e cutover coexistente precisam de challenge independente antes do contrato público ser aprovado.
- **Opinion count:** `1`.
- **Package mode:** `bounded-file-set`.
- **Internal reviewer mandate:** `required — fresh no-context reviewer after review baseline freeze`.
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`.
- **Review result:** `round 11 focused GO over 7a1c7a2; no material findings; rounds 9/10 remain valid`.
- **Material findings:** none; parser-safe tokens preserve the Prisma/logs and direct-controller-HTTP prohibitions.
- **Evidence:** formal fresh no-context `architecture_opinion` over `7a1c7a2`; harness parsed into six cells, routing guard/evidence canonical, scope-drift `go/0`; no files edited by reviewer.

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-backend.md`
- **Latest TEACH evidence / artifact:** post-freeze guard `Overall outcome: go`, fingerprint `fb7cb2900ae1`, after `e2caa58` reconvergence.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | integração externa e API nova |
| `blast_radius` | `cross-module` | fiscal + identity + runtime + futuro consumidor |
| `behavioral_change_or_bugfix` | `yes` | nova capacidade comportamental |
| `changes_public_contract` | `yes` | novos endpoints/DTOs/erros |
| `touches_auth_or_tenant` | `yes` | JWT e isolamento de contexto; sem tenancy |
| `touches_runtime_or_infra` | `yes` | configuração/segredos/timeout runtime; sem infra change |
| `touches_tests` | `yes` | testes novos/alterados |
| `critical_user_journey` | `yes` | base da central de notas |
| `release_or_promotion_critical` | `yes` | entrega com prazo curto e dependência do frontend |
| `high_severity_plan_review_issue` | `yes` | primeira rodada trouxe quatro highs, agora incorporados e sujeitos a rerun |
| `explicit_three_lane_request` | `no` | não solicitado |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** medium + cross-module + API/auth/runtime-sensitive.
- **Impact signals in scope:** `cross-module blast radius|public API|auth|runtime configuration`.
- **Package mode:** `bounded-file-set`.
- **Package minimum contents:** TODO congelado + módulos primário/identity/runtime + app/config/auth files + package/Dockerfile.
- **Critique isolation mode:** `fresh internal no-context reviewer`.
- **Internal reviewer mandate:** `required after freeze`.
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`.
- **Critique status:** `no_material_findings`
- **Findings summary:** `round 11 focused GO: harness parser-safe preserva as proibições, adoption timing é válido e routing outcome/evidence não implicam approval; nenhum bloqueio material`.
- **Evidence / reference:** `formal fresh critique over 7a1c7a2; scope-drift go/0; assumption/audit/routing guards go; reviewer made no changes`.
- **Waiver authority / reference:** `n/a`.

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** A-01..A-05 sustentam dependency, guard, destination e wiring decisions.
- **Trigger stage:** `after critique convergence and before APROVADO`.
- **Guard scope:** `A-01,A-02,A-03,A-04,A-05`.
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-backend.md`.
- **Gate status:** `no_material_findings`
- **Findings summary:** A-01..A-05 citam pelo menos um anchor de código resolvível e nenhum path/evidence defect permanece.
- **Evidence / reference:** focused architecture/critique R10 GO; `assumption_code_coherence_guard.py` deve retornar `Overall outcome: go` após este registro.
- **Waiver authority / reference:** `n/a`.

## Approval

- **Approved by:** `pending explicit APROVADO`.
- **Approval scope:** `list + detail backend Smart Notas, tests, docs/modules e configuração descritos neste TODO; inclui execução por routine executor subagent no principal checkout, single writer`.
- **Execution not authorized by approval:** todos os itens de `Out of Scope`, especialmente frontend, documentos, banco, mutações, deploy e worktrees.
- **Renewed approval required when:** contrato/escopo/autorização/persistência/dependency/runtime risk mudar materialmente.
- **Pre-approval authority evidence:** `todo_authority_guard.py --pre-approval` retornou `Overall outcome: preflight-go`, zero violations, em 2026-09-27.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | execução tática | gates/approval/evidência | código pré-approval | authority guards |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | lifecycle do TODO | phase order | pular gates | execução por fases |
| `delphi-ai/rules/stacks/nestjs/nestjs-architecture-always-on.md` | backend NestJS | módulo/DI/validation/config | controller gordo/acoplamento | estrutura e testes |
| `delphi-ai/workflows/nestjs/change-application-boundary-method.md` | novos endpoints | contrato/auth/error/test | input/config sem runtime validation | boundary implementation |
| `delphi-ai/skills/package-first-verification/SKILL.md` | novo adapter/service | reuse check | duplicar package | host-local justified |
| `delphi-ai/workflows/docker/performance-concurrency-validation-method.md` | endpoint externo | pcv-1 | evidência prose-only | EPS lane |
| `delphi-ai/skills/endpoint-performance-scrutiny/SKILL.md` | list/detail externo | bounded list + direct lookup | page-walk/broad fetch | EPS-E2 |
| `delphi-ai/skills/runtime-load-stress-validation/SKILL.md` | claims de rate/concurrency | RLS local com métricas | load real no provedor | RLS-E1 |
| `delphi-ai/skills/security-adversarial-review/SKILL.md` | credenciais/JWT/PII | origin, authz, redaction, abuse | tráfego destrutivo/vazamento | post-implementation gate |

> As fontes acima estão preparadas para preflight; a ingestão vinculante pós-`APROVADO` será registrada antes do código.

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `pending explicit APROVADO of this TODO scope`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `go`
- **Guard evidence:** `routine-executor/gpt-5.6-terra/medium; primary-checkout-single-writer; worktrees not-authorized; rerun after APROVADO before implementation`.
- **Waiver / exception reference:** `n/a`

## Decision Adherence Validation

| Decision ID | Status | Evidence | Notes |
| --- | --- | --- | --- |
| `D-01` | `pending` | implementation/evidence pending | list/detail only |
| `D-02` | `pending` | implementation/evidence pending | trusted context resolution |
| `D-03` | `pending` | implementation/evidence pending | Smart Notas-only/no fallback |
| `D-04` | `pending` | implementation/evidence pending | HMAC noteId |
| `D-05` | `pending` | implementation/evidence pending | query/bounds |
| `D-06` | `pending` | implementation/evidence pending | all four profiles/both contexts |
| `D-07` | `pending` | implementation/evidence pending | upstream failures |
| `D-08` | `pending` | implementation/evidence pending | no backend cache/polling |
| `D-09` | `pending` | implementation/evidence pending | NestJS boundary |
| `D-10` | `pending` | implementation/evidence pending | local-only provisional/cutover split |
| `D-11` | `pending` | implementation/evidence pending | origin/rate/concurrency/timeout |
| `D-12` | `pending` | implementation/evidence pending | noteId/error/log redaction |
| `D-13` | `pending` | implementation/evidence pending | privacy/no-store/access audit |

## Module Decision Consistency Validation

| Module Decision Ref | Planned Handling | Delivery Status | Evidence | Notes |
| --- | --- | --- | --- | --- |
| `fiscal-notes-and-documents#authority` | `Preserve` | `pending` | pending | 1:1 delivery check |
| `fiscal-notes-and-documents#documents` | `Out of Scope` | `pending` | pending | nenhum PDF/XML |
| `identity-and-team#protected-reads` | `Preserve` | `pending` | pending | JWT global |
| `runtime-and-deployment#config` | `Preserve` | `pending` | pending | sem segredo/docs only |

## Security Risk Assessment

- **Risk level:** `high`.
- **Why this risk level:** credenciais de dois emissores, dados fiscais/PII, novo contrato autenticado e `noteId` context-bound.
- **Attack surface in scope:** JWT/cache de revogação, provider Authorization/CNPJ, allowlist/redirect, rate abuse, input bounds, error/log sanitization, context spoofing, identifier tampering e PII presente somente no payload upstream.
- **Attack simulation decision:** `required`.
- **Review evidence:** `pending security-adversarial review after implementation`.
- **Residual security risk:** quotas/URL documents remain outside; credentials dependem de injeção segura no deploy.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `medium`
- **Why this level:** cada chamada de lista/detalhe adiciona I/O externo; não há writes, cache, bulk ou polling.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `required` | `medium` | `EPS-DATA-PATH-CHANGED` | `before_local_implemented` | `EPS-E2` | `pending` | provider latency/quota | `none` |
| `FRC` | `frontend-race-condition-validation` | `not_needed` | `low` | `FRC-RETRIGGERABLE-LIST` | `before_local_implemented` | `FRC-POLICY` | `not_applicable` | none in backend-only slice | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `BCI-DUPLICATE-SUBMIT-OR-REPLAY` | `before_local_implemented` | `BCI-POLICY` | `not_applicable` | read-only, no shared mutation | `none` |
| `RLS` | `runtime-load-stress-validation` | `required` | `medium` | `RLS-SLO-CLAIM` | `before_local_implemented` | `RLS-E1` | `pending` | multi-replica/provider quota unknown | `none` |

### EPS

- **Trigger rationale:** novo data path HTTP externo para endpoints list/detail; requer touched-path audit e evidência forte de timeout/uma chamada por request.
- **Recorded at (UTC):** `2026-09-26T00:00:00Z`
- **Executor ID:** `pending-routine-executor`
- **Evidence object:** `pending implementation; JSON pcv-1 required before Local-Implemented`.

### FRC

- **Trigger rationale:** nenhum frontend/cache/state muda neste TODO; race contract permanece no TODO React.
- **Recorded at (UTC):** `2026-09-26T00:00:00Z`
- **Executor ID:** `n/a`
- **Evidence object:** `n/a — trigger_result=not_needed`.

### BCI

- **Trigger rationale:** somente GET read-through sem write, idempotency claim ou estado compartilhado.
- **Recorded at (UTC):** `2026-09-26T00:00:00Z`
- **Executor ID:** `n/a`
- **Evidence object:** `n/a — trigger_result=not_needed`.

### RLS

- **Trigger rationale:** o contrato faz claims explícitos de rate, fairness, concorrência, saturação, abort e recuperação; RLS roda somente contra upstream stub local, nunca contra Smart Notas.
- **Recorded at (UTC):** `2026-09-26T00:00:00Z`
- **Executor ID:** `pending-routine-executor`
- **Evidence object:** `pending RLS-E1 before Local-Implemented`.
- **Runner:** Jest dedicado `src/fiscal-notes/__tests__/smart-notas-load.spec.ts` abre Nest em porta efêmera com os mesmos pipes/filtro/controller/service e guard test-only que mapeia `X-Test-Actor` para 20 atores; upstream stub local em outra porta; um driver Promise-worker dentro do teste alterna ator, contexto e list/detail. `runtime_load_probe.sh` não é o runner principal porque não rotaciona identidade/contexto nem gera o JSON `pcv-1` exigido.
- **Workload model:** 20 atores sintéticos em ordem round-robin alternam `unifast|prosperar` e lista|detalhe; credenciais/IDs são fixtures falsas; nenhum socket alcança host não-loopback. O clock/rate state e o stub são controláveis pelo harness, mas Nest/stub permanecem no mesmo processo até terminar recovery.
- **Stage L — accepted load:** stub 100 ms, concurrency `5` por `5s`, `maxConcurrency=8`, budgets `user=120/context=600`; exige somente `200`, p95 `<=500 ms`, p99 `<=1000 ms`, throughput `>=5 req/s`, zero erro inesperado e peak upstream `<=8`.
- **Stage S — semaphore saturation:** rate state limpo por avanço do clock, stub 100 ms, concurrency `20` por `1s`, mesmos budgets altos; exige `SmartNotasOcupado > 0`, `LimiteDeConsultaExcedido = 0`, peak upstream exatamente `8`, zero fila e current concurrency `0` ao final.
- **Stage FU — actor budget isolated:** rate state limpo, `maxConcurrency=64`, budgets `user=30/context=600`; um ator envia 35 requests sequenciais dentro da mesma janela, alternando contexto e list/detail. Exige exatamente 30 aceites, exatamente 5 `LimiteDeConsultaExcedido`, exatamente 30 chamadas upstream, zero chamada upstream para as cinco requests posteriores ao limite e zero `SmartNotasOcupado`. O snapshot depois do 30º aceite é `actor=30, unifast=15, prosperar=15`; cada uma das cinco rejeições deve preservar exatamente esse snapshot, provando a atualização atômica e que o budget de contexto não mascara o limiter por ator.
- **Stage FC — context budget and fairness isolated:** rate state limpo, `maxConcurrency=64`, budgets `user=120/context=120`; os 20 atores, dez por contexto, enviam exatamente 13 requests cada em round-robin, alternando list/detail. Exige exatamente 120 aceites e 10 `LimiteDeConsultaExcedido` em cada contexto, exatamente 240 chamadas upstream no total, zero chamada upstream para as 20 requests rejeitadas e zero `SmartNotasOcupado`. O snapshot depois do 12º round é `unifast=120, prosperar=120` e cada um dos 20 atores tem exatamente `12`; a 13ª request de cada ator deve preservar todos esses counters sem incrementá-los, provando atomicidade, fairness/no-starvation e que o budget por ator não mascara os limiters de contexto.
- **Stage A — abort/timeout:** rate state limpo, stub 2000 ms, `maxConcurrency=8`; lança oito requests, desconecta deterministicamente quatro clientes após 50 ms e deixa quatro atingirem `timeout=1000 ms`. Exige `client_aborted >=4`, quatro `SmartNotasTimeout`, stub observa cancelamento dos oito upstream requests, slots/current concurrency retornam a zero em até 250 ms após o último abort e nenhuma escrita em socket fechado.
- **Stage R — recovery sem restart:** ainda no mesmo Nest/stub, clock avança além da janela, stub volta a 100 ms e concurrency `2` por `5s`; exige somente `200`, current concurrency zero ao final e latência/throughput dos thresholds de load. Restart-resilience smoke é separado e não substitui R.
- **Global acceptance:** statuses fora dos previstos falham; processo/memória permanecem vivos; FU e FC registram contagens aceitas/rejeitadas/upstream e snapshots before/after de counters por ator e contexto; todo threshold acima vira assertion pass/fail, não mera métrica registrada.
- **Evidence capture:** o teste escreve `foundation_documentation/artifacts/tmp/smart-notas-read-rls/rls-pcv1.json` com o envelope obrigatório: `policy_schema_version=pcv-1`, `schema_version`, `lane_id=RLS`, `todo_id`, `run_id`, `environment_id`, `executor_id`, `reviewer_id`, `recorded_at_utc`, `evidence_type`, `sample_profile_id=RLS-SP-H`, `acceptance_rule_id=RLS-A1`, `result_summary`, `artifact_payload={stage_profile_observed,thresholds,metrics_summary,status_counts,unexpected_error_rate,peak_and_current_concurrency,abort_and_timeout_counts,fairness,rate_counter_snapshots,recovery,git_baselines}` e `artifact_sha256`.
- **Hash rule:** `artifact_sha256` é SHA-256 do JSON completo sem esse campo, UTF-8, chaves ordenadas recursivamente, arrays na ordem declarada e sem whitespace insignificante; o evidence object do TODO registra também `evidence_type,environment_id,run_id,artifact_uri,artifact_schema_version,artifact_sha256,sample_profile_id,acceptance_rule_id,result_summary,reviewer_id`.
- **Raw artifacts:** traces/contadores auxiliares ficam no mesmo diretório tmp; o JSON canônico, não prosa, satisfaz o gate.
- **Exact command:** no diretório backend, `RLS_OUTPUT_DIR=../foundation_documentation/artifacts/tmp/smart-notas-read-rls npm test -- --runInBand --runTestsByPath src/fiscal-notes/__tests__/smart-notas-load.spec.ts`.

## Verification Debt Assessment

- **Audit outcome:** `pending`.
- **Why this outcome:** TODO medium e provider contract parcialmente genérico exigem audit antes de Completed.
- **Inline code TODO debt:** `pending`.
- **Evidence / audit artifact:** `pending`.
- **Accepted residual debt:** `none approved`.

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** comportamento/API/testes novos.
- **Trigger signals in scope:** `behavior-defining change|shared API contract|critical user journey`.
- **Package mode:** `bounded-file-set`.
- **Canonical method:** `wf-docker-independent-test-quality-audit-method`.
- **Audit isolation mode:** `fresh internal no-context reviewer`.
- **Audit status:** `not_run`
- **Findings summary:** `pending`.
- **Evidence / reference:** `pending`.
- **Waiver authority / reference:** `n/a`.

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** API/auth/runtime-sensitive e cross-module.
- **Impact signals in scope:** `cross-module|public API|auth|runtime configuration`.
- **Package mode:** `bounded-file-set`.
- **Review isolation mode:** `fresh internal no-context reviewer`.
- **Final review status:** `not_run`
- **Findings summary:** `pending`.
- **Evidence / reference:** `pending`.
- **Waiver authority / reference:** `n/a`.

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `required`
- **Why this decision:** nova rota candidata coexiste com `/eventos`, o audit floor exige triple-review e o closeout precisa provar separação sem fallback/promoção implícita.
- **Cutover signals in scope:** `canonical capability transition|legacy-path coexistence`.
- **Package mode:** `bounded-file-set`.
- **Cutover audit status:** `not_run`
- **Findings summary:** `pending`.

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| backend diff + tests + modules | contract/security/runtime P1/P2 | `planned` | pending | pending | pending |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Search Lens | Status | Evidence | Findings | Resolution |
| --- | --- | --- | --- | --- | --- |
| NestJS boundary + source authority | direct fetch controller, Prisma/log fallback, public credential/CNPJ, raw payload | `planned` | pending | pending | pending |

## Promotion Finding Routing Ledger

| Finding ID | Finding Source | Severity | Classification | Required Action | Status | Rationale / Follow-up Reference |
| --- | --- | --- | --- | --- | --- | --- |
| `PLAN-ACCESS-01` | critique + architecture opinion | `high` | `by-design/no-action` | decisão humana para `D-06` e testes da matriz | `resolved` | usuário autorizou todos os setores; D-06/DOD-10/VAL-08 |
| `PLAN-SEC-01` | critique + architecture opinion | `high` | `release-blocker` | incluir redaction de path/query e esclarecer opacidade do `noteId` | `resolved` | SCOPE-08/DOD-12/frozen contract |
| `PLAN-ARCH-01` | critique + architecture opinion | `high` | `release-blocker` | separar implementação local de cutover/promoção canônica | `resolved` | D-10 + Provisional Notes + out-of-scope |
| `PLAN-CONTRACT-01` | critique | `high` | `release-blocker` | congelar DTOs, nullability, paginação, bounds e catálogo de erros | `resolved` | Frozen Public HTTP Contract |
| `R3-PRIVACY-01` | critique R3 | `high` | `release-blocker` | minimizar PII, no-store e auditoria actor-aware | `resolved` | D-13/DOD-14/privacy contract |
| `R3-DESTINATION-01` | architecture + critique R3 | `high` | `release-blocker` | fixar origin/base path, reject redirect e par token/CNPJ | `resolved` | credential destination contract |
| `R3-CAPACITY-01` | architecture + critique R3 | `high` | `release-blocker` | rate fairness + RLS local além de semaphore | `resolved` | DOD-11/DOD-15/pcv RLS |
| `R3-DECODER-01` | architecture R3 | `high` | `release-blocker` | separar null/ausente de presente malformado | `resolved` | DOD-04/DOD-13 |
| `R3-ERROR-01` | architecture + critique R3 | `high` | `release-blocker` | caminho/log fail-closed e catálogo exaustivo | `resolved` | stable error catalog/DOD-12 |
| `R3-AUTH-01` | architecture + critique R3 | `medium` | `release-blocker` | aceitar/provar janela JWT de 30s | `resolved` | authorization contract/DOD-10 |
| `R3-STRUCTURE-01` | architecture R3 | `medium` | `release-blocker` | AST/import/export/decorator assertions | `resolved` | Architecture Protection Harness |
| `R3-ADHERENCE-01` | critique R3 | `medium` | `release-blocker` | itemizar D-01..D-13 | `resolved` | Decision Adherence Validation |
| `R3-CUTOVER-01` | critique R3 | `medium` | `follow-up-fast-follow` | abrir owner exato antes do closeout | `accepted` | planned `TODO-uninotas-smart-notas-read-cutover.md` |
| `R4-CONTRACT-DECODER-01` | architecture + critique R4 | `high` | `release-blocker` | remover contradição e congelar bounds por campo | `resolved` | decoder matrix + DOD-04/DOD-13 |
| `R4-ERROR-PRECEDENCE-01` | critique R4 | `high` | `release-blocker` | ordenar auth/pipe/flag/HMAC/rate/semaphore/abort/provider | `resolved` | Stable error catalog / first-signal rule |
| `R4-RLS-GOV-01` | critique R4 | `medium` | `release-blocker` | usar reason code fechado `RLS-SLO-CLAIM` | `resolved` | pcv-1 RLS row |
| `R4-RLS-HARNESS-01` | critique R4 | `medium` | `release-blocker` | mixed-workload runner + canonical hashed JSON + recovery sem restart | `resolved` | RLS subsection/exact command |
| `R5-RLS-PCV-01` | critique R5 | `medium` | `release-blocker` | envelope/evidence/hash pcv-1 exatos | `resolved` | RLS evidence capture/hash rule |
| `R5-RLS-ABORT-01` | critique R5 | `medium` | `release-blocker` | injetar disconnect/timeout e provar cancel/slot release | `resolved` | Stage A assertions |
| `R5-RLS-HARNESS-01` | architecture R5 | `medium` | `release-blocker` | saturação garantida, fairness/no-starvation e recovery sem restart | `resolved` | Stages S/FU/FC/R |
| `R6-RLS-RATE-BUDGET-01` | critique R6 | `medium` | `release-blocker` | forçar actor limiter e context limiter em substages independentes com contagens exatas | `resolved` | Stages FU/FC |
| `R7-RLS-ATOMIC-COUNTERS-01` | critique R7 | `medium` | `release-blocker` | provar snapshots exatos e imutáveis do outro budget em cada rejeição | `resolved` | Stages FU/FC + `rate_counter_snapshots` |

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** contrato e gates pré-approval convergiram; execução permanece proibida até aprovação humana explícita.
- **Post-commit/push status:** `baseline de planejamento 7a1c7a2 publicado; metadata final de revisão/preflight pronta para commit/push`.
- **Next path/status action:** publicar a metadata final e solicitar `APROVADO`.

## Module Consolidation Gate

- [ ] Contrato final promovido ao módulo primário/runtime.
- [ ] Decisões preservadas/superseded com traceabilidade.
- [ ] TODO movido para `completed/features/` somente após gates.

## Commands (Run Locally)

- `python3 delphi-ai/tools/node_capability_surface_audit.py --repo backend --expect nestjs --manifest package.json --require-script test --require-script build --require-script lint`
- Node/NPM via runner Windows no diretório `backend`: `npm test -- --runInBand`, `npm run build`, `npm run lint`.
- Guards Delphi e Foundation registrados nas seções acima.

## Files Expected

- Usar exclusivamente o `Diff Expectation Contract` como inventário autoritativo.
