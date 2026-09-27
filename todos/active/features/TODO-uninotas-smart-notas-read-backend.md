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
- **Planned next steps:** TODO de cutover/runtime para injetar segredos, habilitar a capacidade e promover ownership; TODO React para seletor/cache; TODO de DANFE/XML; TODO de falhas/casos operacionais.
- **Anticipatory implementation authorized now:** `none`.
- **Rationale:** o corte cria a menor fronteira funcional completa que respeita a autoridade Smart Notas e pode ser consumida sem acoplar o backend ao frontend ou ao PostgreSQL.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `Provisional`
- **Next exact step:** concluir a reconvergência técnica, atualizar/pushar o baseline, repetir as revisões e obter `preflight-go` antes de solicitar `APROVADO`.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** `D-06` foi resolvida pelo usuário; os findings técnicos estão sendo incorporados e precisam de nova revisão independente.
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
| Foundation module/TODO | `main@pending` | `n/a — main-only authority` | `n/a` | `origin/main@pending` | `planning baseline pending` |

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

- Ambos os endpoints exigem JWT ativo pelo guard global e permitem `ADMIN|GESTOR|ANALISTA|LEITOR`; o primeiro corte não diferencia setor, perfil ou emissor e não concede escrita fiscal.
- `SMART_NOTAS_READ_ENABLED=false` é o default seguro. Nesse estado, nenhuma chamada externa ocorre e as rotas respondem `503/SmartNotasDesabilitado`; o TODO de cutover injeta segredos e habilita a capacidade.

### `GET /api/v1/notas`

- Query obrigatória: `contextoFiscal=unifast|prosperar`, `dataInicio=YYYY-MM-DD`, `dataFim=YYYY-MM-DD`.
- Query opcional: `status`, `documento`, `idCompra`, `pagina` (default `1`). Campos desconhecidos são rejeitados pelo `ValidationPipe` global.
- `status` aceita somente `Pendente|Autorizada|Cancelada|Aguardando|Aguardando Cliente|Denegada|Pausada|Anulada`; um status novo recebido do provedor continua sendo devolvido literalmente em `providerStatus` e não quebra o decoder.
- `documento` aceita exatamente 11 ou 14 dígitos; `idCompra` aceita 1..100 caracteres após trim; `pagina` aceita inteiro 1..10000; intervalo é inclusivo, ordenado e limitado a 366 dias.
- Uma request consulta exatamente uma página de exatamente um contexto; não há page-walk, merge, prefetch ou fallback.

Resposta `200`:

| Campo | Tipo / nullability | Regra |
| --- | --- | --- |
| `items` | `FiscalNoteSummary[]` | array sempre presente; vazio é sucesso somente após `200` válido do provedor |
| `page` | integer `>=1` | página reportada pelo provedor |
| `perPage` | integer `>=0` | não é controlável pelo consumidor |
| `total` | integer `>=0` | total provider-scoped |
| `totalPages` | integer `>=0` | nunca combinado entre emissores |

`FiscalNoteSummary` sempre contém todas as chaves abaixo; campos provider-derived ausentes/inválidos tornam-se `null`, exceto os invariantes cuja ausência invalida a resposta:

| Campo | Tipo | Nullability / semântica |
| --- | --- | --- |
| `noteId` | string | obrigatório; identidade UniNotas opaca-by-contract |
| `fiscalContext` | `unifast|prosperar` | obrigatório, resolvido pelo backend |
| `providerStatus` | string | obrigatório, não vazio; vocabulário aberto na saída |
| `fiscalNumber`, `accessKey`, `purchaseId` | string | nullable; nunca são identidade da rota |
| `environment`, `model`, `purpose`, `platform`, `product` | string | nullable |
| `scheduledIssueDate`, `paymentDate` | `YYYY-MM-DD` | nullable; datas `DD/MM/YYYY` são normalizadas sem timezone |
| `competence` | string | nullable; preserva datetime sem inventar offset |
| `recipientName`, `recipientDocument`, `recipientEmail`, `recipientCity`, `recipientState`, `recipientCountry` | string | nullable |
| `unitValue`, `totalValue` | decimal string | nullable; forma canônica sem binary float |

### `GET /api/v1/notas/:noteId`

- Não aceita `contextoFiscal`, CNPJ ou identificador do provedor. O `noteId` determina o contexto confiável e dispara uma única chamada direta a `/notas/{idInterno}`; é proibido procurar a nota caminhando páginas da lista.
- Resposta `200` contém todos os campos de `FiscalNoteSummary` e acrescenta, sempre presentes porém nullable: `issueDate: YYYY-MM-DD|null`, `neighborhood`, `postalCode`, `referencedAccessKey`, `street`, `addressNumber`, `addressComplement`, `stateRegistration`, `municipalRegistration`, `operationNature`, `phone` como `string|null`, e `quantity` como decimal string ou `null`.
- `providerIdInterno`, `retorno` bruto e payload bruto não fazem parte do contrato público.

### Opaque `noteId` integrity contract

- Formato: `v1.<payload-base64url>.<mac-base64url>`, máximo 512 caracteres; payload JSON canônico contém somente `{c: fiscalContext, i: providerIdInterno}`.
- MAC: HMAC-SHA-256 com `SMART_NOTAS_NOTE_ID_SECRET_BASE64`, decodificado para no mínimo 32 bytes; comparação usa `timingSafeEqual` após validar comprimentos.
- “Opaco” significa que consumidores não podem construir, decodificar ou depender do conteúdo. HMAC garante integridade, não confidencialidade; por isso o valor também é redatado de logs/erros.
- Somente `v1` e uma chave ativa são aceitos neste corte. Rotação invalida IDs anteriores, que são recuperáveis por nova listagem; rotação multi-chave pertence ao cutover/hardening.

### Stable error catalog

| HTTP | `erro` estável | Condição |
| --- | --- | --- |
| `400` | `ConsultaDeNotasInvalida` | query, intervalo, bound ou `noteId` estruturalmente inválido/adulterado |
| `401` | contrato JWT atual | token UniNotas ausente/inválido/inativo |
| `404` | `NotaFiscalNaoEncontrada` | Smart Notas devolve 404 no detalhe |
| `502` | `SmartNotasCredencialRejeitada` | upstream 401/403 com configuração habilitada |
| `502` | `SmartNotasContratoInvalido` | upstream 2xx com JSON/shape/tamanho inválido ou 400/422 inesperado após validação local |
| `503` | `SmartNotasDesabilitado` | flag local desligada |
| `503` | `SmartNotasOcupado` | limite concorrente por instância atingido; não enfileira |
| `503` | `SmartNotasIndisponivel` | timeout, rede, upstream 429 ou 5xx |

- O envelope continua `{statusCode,erro,mensagem,caminho,timestamp}`; `mensagem` é estável/sanitizada e `caminho` usa template como `/api/v1/notas/:noteId`, nunca URL/query real.
- Resposta provider maior que 2 MiB é `SmartNotasContratoInvalido`. Nenhum erro vira lista vazia, fallback PostgreSQL ou mensagem/payload cru.

### Capacity and observability contract

- `SMART_NOTAS_TIMEOUT_MS`: default `10000`, range `1000..30000`; `SMART_NOTAS_MAX_CONCURRENCY`: default `8`, range `1..64`.
- Sem retry e sem fila local. O fetch é abortado no timeout ou desconexão do consumidor; o slot concorrente é liberado em `finally`.
- Log estruturado mínimo pertence ao adapter: correlation ID local, operação `list|detail`, contexto fiscal, outcome normalizado, status HTTP upstream quando existir e duração; proíbe query, `noteId`, documento, `idCompra`, CNPJ, Authorization e payload.

## Definition of Done

- [ ] `DOD-01` Lista context-scoped retorna DTO paginado normalizado e nunca mistura Unifast/Prosperar.
- [ ] `DOD-02` Detalhe resolve `noteId` assinado para um único contexto/`idInterno`, rejeita adulteração e não aceita CNPJ/token arbitrário.
- [ ] `DOD-03` Com a capacidade habilitada, configuração exige base URL HTTPS, credenciais independentes, CNPJs válidos e segredo HMAC base64 de 32+ bytes; desabilitada por padrão, não exige credenciais e nunca chama o provedor.
- [ ] `DOD-04` Provider status/nullabilidade/datas/decimais são mapeados defensivamente; payload bruto e retorno sensível não atravessam o contrato público.
- [ ] `DOD-05` Timeout/rede/401/403/5xx/shape inválido produzem falha explícita e sanitizada; 404 de detalhe permanece 404; nenhum caso cai para `logs`.
- [ ] `DOD-06` Controller é fino, integração fica atrás de porta/token explícito e o módulo não importa Prisma.
- [ ] `DOD-07` Testes unitários/integração e build/lint do backend passam no runner declarado.
- [ ] `DOD-08` Probes read-only redatados comprovam lista e detalhe nos dois contextos sem persistir identificadores, payloads ou valores privados.
- [ ] `DOD-09` Módulos canônicos registram o candidato local sem promover ownership: `events-and-classification` continua owner atual e `fiscal-notes-and-documents` continua `target_planned`.
- [ ] `DOD-10` `ADMIN|GESTOR|ANALISTA|LEITOR` ativos passam pelos dois GETs; usuário ausente/inativo continua bloqueado pelo JWT e nenhuma rota fiscal de escrita existe.
- [ ] `DOD-11` Uma request gera no máximo uma chamada Smart Notas; concorrência por instância é limitada, desconexão/timeout aborta o fetch, upstream `429` é explícito e nenhum retry/paginação implícita ocorre.
- [ ] `DOD-12` Respostas e logs de exceção usam template de rota sanitizado e nunca incluem query, `noteId`, documento, `idCompra`, token, CNPJ ou payload do provedor.
- [ ] `DOD-13` O contrato público abaixo é provado campo a campo, incluindo nullability, paginação, status desconhecido, bounds e catálogo estável de erros.

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

## Completion Evidence Matrix

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-01..07,DOD-10..13` | `Definition of Done` | contratos, isolamento, autorização, capacidade, redaction, arquitetura e testes | `code+test` | paths/testes e comandos acima | `backend local` | `planned` | evidência será itemizada antes do claim |
| `DOD-08` | `Definition of Done` | ambos os contextos respondem no adapter real | `runtime` | probe redatado sem dados privados | `Smart Notas read-only` | `planned` | sem mutações |
| `DOD-09` | `Definition of Done` | consolidação target-planned sem cutover | `doc+review` | módulos âncora + registry invariants + validator | `foundation` | `planned` | owner atual preservado |
| `VAL-01..10` | `Validation Steps` | validação completa do corte | `test+review` | comandos listados | `local/foundation` | `planned` | detalhar resultados na entrega |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas OpenAPI | contrato da fronteira externa | `healthy` | `2026-09-26` | SHA-256 `cc2a415962dcff00b7d91d3a1bfe99544ec3bd1543b2e5f9d93df1b8ce686502` | parar/revisar se fingerprint mudar |
| Credenciais Unifast/Prosperar | probes e execução local | `healthy` | `2026-09-25` | `GET /empresa` redatado confirmou cada CNPJ configurado; repetir antes do claim | nunca imprimir/persistir valores |
| Smart Notas quotas/SLA | políticas de retry/load | `unknown` | `2026-09-26` | contrato público não publica limites | zero retry automático; sem polling neste corte |

## Package-First Assessment

- **Queries executed:** `query_packages.sh --search "smart notas"`, `--search "http client"`, `--stack node --all`.
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
- [x] `D-11` A flag é false por default; quando habilitada, Joi exige credenciais/segredo e o adapter impõe timeout, concorrência sem fila, cancelamento, 2 MiB e zero retry. Ref: rollout/capacity findings.
- [x] `D-12` `noteId` HMAC é opaco-by-contract, não confidencial; filtro/logs redatam URL, query e parâmetros, e o contrato de erro é o catálogo congelado acima. Ref: security findings.

## Module Decision Baseline Snapshot

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `fiscal-notes-and-documents#authority` | Smart Notas é única fonte; sem aggregate/context leak | `Preserve` | `modules/fiscal-notes-and-documents.md` |
| `fiscal-notes-and-documents#documents` | documentos on-demand pertencem ao módulo | `Out of Scope` | `modules/fiscal-notes-and-documents.md` |
| `identity-and-team#protected-reads` | JWT ativo protege leitura e perfis atuais podem ler | `Preserve` | `modules/identity-and-team.md` |
| `runtime-and-deployment#config` | runtime/config é explícito e sem segredo na Foundation | `Preserve` | `modules/runtime-and-deployment.md` |

## Decision Baseline (Frozen Before Implementation)

- [ ] `D-01..D-12` estão resolvidas e serão recongeladas após novo baseline/revisões; implementação continua proibida até `preflight-go` e `APROVADO`.

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
| structural test | fiscal module imports | bounded import scan/Jest | Prisma/LogsModule, controller->fetch ou wire DTO escapando adapter | `implement-in-this-todo` | DOD-06/VAL-02 |
| analyzer | NestJS surface | `node_capability_surface_audit.py` | manifest/scripts/capability drift | `already-enforced` | VAL-01 |
| review | code/module diff | architecture adherence review | brittle shortcut/hidden dual-read | `implement-in-this-todo` | final review package |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-file-set`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** `initial fresh opinion findings integrated into D-06/D-10/D-12 and the frozen HTTP contract; authoritative rerun pending refreshed baseline`.
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
- **Baseline commit:** `pending refreshed baseline; predecessor 78825a4837ac91754bdd191e2db6a279ca78dfda`
- **Baseline push reference:** `origin/main`
- **Gate status:** `not_run`
- **Findings summary:** a decisão de acesso e a reconvergência material exigem novo commit/push antes das revisões autoritativas.
- **Evidence / reference:** predecessor `78825a4` permanece publicado; refresh ainda pendente.
- **Waiver authority / reference:** `n/a`.
- **Pre-freeze packet-prep rule:** review rows below are `prepared-pre-freeze`, not passed.

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** impede que o contrato revisado mude materialmente antes do approval.
- **Trigger stage:** `after review convergence and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-backend.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`.
- **Evidence / reference:** `pending`.
- **Waiver authority / reference:** `n/a`.

## Questions To Close

- [x] `Q-01` Resolvida em 2026-09-26: todos os setores/perfis ativos visualizam ambos os emissores, somente leitura.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | Node 22 oferece `fetch` estável sem pacote externo | `Dockerfile` usa `node:22-slim`; `package.json` target atual | reavaliar dependency/package-first | `High` | `Keep as Assumption` |
| `A-02` | JWT global continuará protegendo o novo controller sem guard adicional | `src/app.module.ts`; `JwtAuthGuard` global | corrigir wiring antes de approval | `High` | `Keep as Assumption` |
| `A-03` | Nenhum módulo Smart Notas/HTTP já existe no backend | `rg` e node capability audit em 2026-09-26 | reutilizar owner existente | `High` | `Keep as Assumption` |
| `A-04` | Tokens/CNPJs dos dois contextos estão disponíveis localmente | somente nomes em `.env`; probes redatados no discovery | probe real fica bloqueado, implementação/testes mockados continuam | `High` | `Keep as Assumption` |

## Execution Plan

### Touched Surfaces

- `backend/src/fiscal-notes/**`, configuração/bootstrap wiring, filtro global de exceções, `.env.example`, backend README, testes Jest.
- Módulos Foundation primário/runtime e lifecycle deste TODO.

### Ordered Steps

1. Ingerir regras vinculantes e confirmar routing/authority após `APROVADO`.
2. Criar testes fail-first para contrato público, configuração condicional, quatro perfis, `noteId`, normalização, contexto, catálogo de erros, redaction e limites de capacidade.
3. Implementar DTOs/erros, codec HMAC, porta, serviço de aplicação e teste estrutural sem Prisma/LogsModule.
4. Implementar adapter `fetch` com semaphore fail-fast, timeout/request-abort, resposta máxima de 2 MiB, headers server-side, shape guards, observabilidade sanitizada e zero retry.
5. Corrigir o filtro global para usar template de rota; registrar módulo/controller no AppModule e documentar flag/env/endpoints.
6. Rodar testes/build/lint; com flag opt-in, repetir `/empresa` binding e probes lista/detalhe redatados nos dois contextos.
7. Consolidar apenas o candidato `target_planned`, rodar audits/guards e encerrar no máximo como `Local-Implemented, Provisional`, abrindo o handoff de cutover.

### Test Strategy

- **Strategy:** `test-first`.
- **Why:** contrato externo genérico e isolamento de contexto exigem falhas explícitas antes do adapter.
- **Fail-first targets:** config disabled/enabled, quatro perfis, `noteId` adulterado, credencial errada por contexto, provider 400/401/403/404/422/429/5xx/timeout, oversize/shape inválido, decimal/data nullable, status desconhecido, saturation/abort, filtro com canários e ausência de Prisma/log fallback.

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
| `GET /api/v1/notas` | React Geral | novo contrato paginado context-scoped | `none` | TODO React selector/cache |
| `GET /api/v1/notas/:noteId` | React detalhe | novo DTO/erro estável | `none` | TODO React detalhe |
| env Smart Notas | Railway/runtime | flag false por default + variáveis server-only | exemplo/config apenas | TODO cutover injeta segredos e ativa |
| `note_read_model` | capability registry | candidato não altera owner atual | `none` | TODO cutover promove atomicamente |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| backend Jest | lógica/contrato mudam | lista/detalhe/DTO/nullability/status/bounds/error/config/HMAC/capacity/redaction | fixtures provider determinísticas + URL canaries + fake timers/abort | `npm test -- --runInBand` | `Local-Implemented` | `planned` | pending | sem dados reais |
| backend app/guard | acesso muda | quatro perfis ativos acessam list/detail; sem JWT/inativo falha | Nest testing app com guards reais e adapter fake | `npm test -- --runInBand` | `Local-Implemented` | `planned` | pending | não aceitar teste só de metadata |
| backend build | novo módulo/DTO | compilação Nest/TS | Node 22 + deps atuais | `npm run build` | `Local-Implemented` | `planned` | pending | runner Windows |
| backend lint | novos arquivos TS | regras estáticas/formatação | deps atuais | `npm run lint` | `Local-Implemented` | `planned` | pending | inspecionar rewrites |
| Smart Notas read probe | integração real | `/empresa` binding + lista/detalhe direto em ambos contextos | env local preenchido; flag opt-in; janela curta | probe opt-in redatado | `Local-Implemented` | `planned` | pending | sem persistir payload/identificador |
| Foundation validator | docs/TODO | coerência/publicação/privacidade | baseline main | validator + verify_context | `promotion` | `planned` | pending | Windows Git Bash para readiness |

### Runtime / Rollout Notes

- `SMART_NOTAS_READ_ENABLED=false` permite que a imagem inicialize sem credenciais e impede chamadas externas; quando true, Joi exige base URL, dois pares token/CNPJ, segredo HMAC, timeout e concorrência válidos.
- Este TODO não liga a flag fora do probe local nem muda `backend/.env`. O deploy precisa receber segredos antes de o TODO de cutover habilitar a flag.
- As rotas são aditivas e não consumidas pelo frontend atual; coexistem inativas com `/eventos`, sem promover ownership, até o cutover do consumidor.

## Plan Review Gate

- **Status:** `reconverged-first-party; refreshed-baseline independent gates pending`.

### Review Sections

- [x] Architecture — owner fiscal, porta explícita e source authority preservados.
- [x] Code Quality — controller fino, decoder separado e erros tipados evitam espalhar condicionais.
- [x] Tests — fail-first cobre contrato, wiring e falhas; live probe é complementar, não substitui fixtures.
- [x] Performance — uma chamada provider por request, semaphore sem fila, response cap, abort/timeout e zero retry/cache/polling limitam amplificação.
- [x] Security — segredo dedicado, context resolution server-side, input bounds e redaction do filtro/logs são obrigatórios.
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
  - **Severity:** `medium`
  - **Evidence:** `backend/src/config/configuration.ts:28-60`; `backend/src/common/filters/all-exceptions.filter.ts:39-58`; `fiscal-notes-and-documents.md:19-20`.
  - **Why it matters now:** credenciais/contextos e o `noteId` não podem ser controlados pelo consumidor nem aparecer em erros/logs.
  - **Option A (Recommended):** configuração Joi fail-fast, resolver server-side, HMAC com segredo dedicado e exceções sanitizadas próprias.
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
  - **Severity:** `low`
  - **Evidence:** OpenAPI não publica quotas/SLA; `Dockerfile:18-27` confirma Node 22 e build do backend; discovery API-02.
  - **Why it matters now:** retry/cache/polling prematuros podem amplificar tráfego em duas contas sem quota conhecida.
  - **Option A (Recommended):** uma chamada por request, `AbortSignal`/timeout configurável, zero retry e EPS evidence.
    - **Implementation effort:** `low`
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

- [x] Contexto ausente/inválido, CNPJ/token trocados, `noteId` adulterado, intervalo invertido/excessivo, caracteres inválidos no documento/idCompra.
- [x] Timeout, abort, DNS, 401/403, 404, 422, 429/5xx e conteúdo não JSON/shape inesperado.
- [x] Datas/provider fields nulos, decimal inválido, status desconhecido, page fora do range e lista vazia legítima.
- [x] Logs/exception não podem revelar Authorization, CNPJ, provider payload ou decoded `noteId`.

### Residual Unknowns / Risks

- [x] Quotas/SLA continuam desconhecidos; mitigação deste corte é uma chamada por request, timeout e zero retry/polling.
- [x] Shape detail não é formalmente tipado no OpenAPI; live evidence existe, mas decoder permanece defensivo.
- [x] Deploy secret injection é dependência de promoção, não autorização para mudar Railway neste TODO.

## Additional Architectural Opinions

- **Needed:** `yes`.
- **Why ambiguity remains:** HMAC stateless, error mapping e cutover coexistente precisam de challenge independente antes do contrato público ser aprovado.
- **Opinion count:** `1`.
- **Package mode:** `bounded-file-set`.
- **Internal reviewer mandate:** `required — fresh no-context reviewer after review baseline freeze`.
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`.
- **Review result:** `initial findings integrated; authoritative rerun pending refreshed baseline`.
- **Material findings:** separar implementação local de promoção canônica/cutover; decidir `D-06`; impedir vazamento de path/query no filtro global; explicitar contrato HTTP, HMAC, erros, limites e rollout.
- **Evidence:** fresh no-context architecture opinion over frozen baseline `78825a4`.

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-backend.md`
- **Latest TEACH evidence / artifact:** post-freeze guard `Overall outcome: go`, fingerprint `d2c83af51108`, against baseline `78825a4`.

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
- **Critique status:** `not_run`
- **Findings summary:** `initial four high and medium findings integrated into contract, decisions, rollout, capacity, tests and cutover boundary; rerun required`.
- **Evidence / reference:** `initial fresh critique over 78825a4; refreshed-baseline critique pending`.
- **Waiver authority / reference:** `n/a`.

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** A-01..A-04 sustentam dependency, guard e wiring decisions.
- **Trigger stage:** `after critique convergence and before APROVADO`.
- **Guard scope:** `A-01,A-02,A-03,A-04`.
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-smart-notas-read-backend.md`.
- **Gate status:** `not_run`
- **Findings summary:** `pending`.
- **Evidence / reference:** `pending`.
- **Waiver authority / reference:** `n/a`.

## Approval

- **Approved by:** `pending explicit APROVADO`.
- **Approval scope:** `list + detail backend Smart Notas, tests, docs/modules e configuração descritos neste TODO; inclui execução por routine executor subagent no principal checkout, single writer`.
- **Execution not authorized by approval:** todos os itens de `Out of Scope`, especialmente frontend, documentos, banco, mutações, deploy e worktrees.
- **Renewed approval required when:** contrato/escopo/autorização/persistência/dependency/runtime risk mudar materialmente.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | execução tática | gates/approval/evidência | código pré-approval | authority guards |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | lifecycle do TODO | phase order | pular gates | execução por fases |
| `delphi-ai/rules/stacks/nestjs/nestjs-architecture-always-on.md` | backend NestJS | módulo/DI/validation/config | controller gordo/acoplamento | estrutura e testes |
| `delphi-ai/workflows/nestjs/change-application-boundary-method.md` | novos endpoints | contrato/auth/error/test | input/config sem runtime validation | boundary implementation |
| `delphi-ai/skills/package-first-verification/SKILL.md` | novo adapter/service | reuse check | duplicar package | host-local justified |
| `delphi-ai/workflows/docker/performance-concurrency-validation-method.md` | endpoint externo | pcv-1 | evidência prose-only | EPS lane |

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
- **Guard outcome:** `pending post-approval routing guard`
- **Waiver / exception reference:** `n/a`

## Decision Adherence Validation

| Decision ID | Status | Evidence | Notes |
| --- | --- | --- | --- |
| `D-01..D-09` | `pending` | implementation/evidence pending | itemizar antes da entrega |

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
- **Attack surface in scope:** JWT read endpoints, provider Authorization/CNPJ, input bounds, SSRF/base URL config, error/log sanitization, context spoofing e identifier tampering.
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
| `EPS` | `endpoint-performance-scrutiny` | `required` | `medium` | `EPS-DATA-PATH-CHANGED` | `before_local_implemented` | `EPS-E2` | `pending` | provider latency/quota | `U-QUERY-PATH-UNKNOWN` |
| `FRC` | `frontend-race-condition-validation` | `not_needed` | `low` | `FRC-RETRIGGERABLE-LIST` | `before_local_implemented` | `FRC-POLICY` | `not_applicable` | none in backend-only slice | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `BCI-DUPLICATE-SUBMIT-OR-REPLAY` | `before_local_implemented` | `BCI-POLICY` | `not_applicable` | read-only, no shared mutation | `none` |
| `RLS` | `runtime-load-stress-validation` | `not_needed` | `low` | `RLS-SLO-CLAIM` | `before_production_ready` | `RLS-E1` | `not_applicable` | no SLO/load claim | `none` |

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

- **Trigger rationale:** sem fila/bulk/cache/index/SLO e sem autorização para load contra provedor externo.
- **Recorded at (UTC):** `2026-09-26T00:00:00Z`
- **Executor ID:** `n/a`
- **Evidence object:** `n/a — trigger_result=not_needed`.

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

- **Cutover audit decision:** `recommended`
- **Why this decision:** nova rota canônica coexiste com `/eventos`; precisa provar separação, não fallback oculto.
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
| `PLAN-SEC-01` | critique + architecture opinion | `high` | `release-blocker` | incluir redaction de path/query e esclarecer opacidade do `noteId` | `integrated-pending-rerun` | SCOPE-08/DOD-12/frozen contract |
| `PLAN-ARCH-01` | critique + architecture opinion | `high` | `release-blocker` | separar implementação local de cutover/promoção canônica | `integrated-pending-rerun` | D-10 + Provisional Notes + out-of-scope |
| `PLAN-CONTRACT-01` | critique | `high` | `release-blocker` | congelar DTOs, nullability, paginação, bounds e catálogo de erros | `integrated-pending-rerun` | Frozen Public HTTP Contract |

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** decisão humana resolvida; reconvergência/revisões/preflight e aprovação ainda pendentes.
- **Post-commit/push status:** `pending`
- **Next path/status action:** publicar o baseline reconvergido, repetir opinion/critique, executar guards pré-approval e então solicitar `APROVADO`.

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
