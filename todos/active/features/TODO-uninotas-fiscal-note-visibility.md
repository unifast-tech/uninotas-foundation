# Exibir tomador e identificadores fiscais completos

## Artifact Identity
- **Artifact type:** `tactical_execution_contract`

## Context

A equipe financeira precisa identificar rapidamente quem é o tomador de cada nota e copiar os identificadores operacionais completos diretamente da Geral. O payload real de listagem do Smart Notas contém `nome`, `idCompra` e `chave`; o produto já normaliza compra/chave, mas hoje exclui o nome e mascara os identificadores na apresentação.

## Framing Source & Story Slice
- **Feature brief:** `direct-to-todo`
- **Primary story ID:** `n/a`
- **Why this is the right current slice:** é uma única evolução da capacidade de identificação visual de notas na Geral e no detalhe, ainda que atravesse o contrato NestJS e a apresentação React.
- **Direct-to-TODO rationale:** o pedido possui uma tela principal, um objetivo de usuário e uma conversa de aprovação; não exige decomposição adicional.

## Contract Boundary
- Este TODO define **WHAT** deve ser entregue e o que conta como pronto.
- A implementação somente começa após congelamento/revisão do contrato e resposta explícita `APROVADO`.
- Descoberta que amplie fonte de dados, persistência local, infraestrutura, autorização ou campos pessoais exige atualização e nova aprovação.

## Implementation Intent
- **Current delivery:** ampliar o resumo fiscal autenticado com nome do tomador e exibir nome/compra/chave completos na Geral e no detalhe.
- **Planned next steps:** atualizar o feature brief e o módulo fiscal com as decisões estáveis após aprovação; implementar e validar backend/frontend no checkout principal.
- **Anticipatory implementation authorized now:** `none`
- **Rationale:** o DTO normalizado continua sendo o único limite entre Smart Notas e navegador; nenhum payload bruto ou credencial atravessa a API do UniNotas.

## Delivery Status Canon (Required)
- **Current delivery stage:** `Pending`
- **Qualifiers:** `none`
- **Next exact step:** congelar e revisar o contrato, executar os gates pré-aprovação e solicitar `APROVADO`.

## Active Work State (Required While TODO Remains In `active/`)
- **Work state:** `implementation`
- **Why this state now:** o contrato está em preparação pré-aprovação para a implementação local.
- **Exit condition:** implementação e validação locais concluídas, seguindo para review/closeout.

## Execution Lane Tracking (Required)
- **Local implementation branches:** `MonitorNotes:release/uninotas-smart-notas`; `uninotas-foundation:main`
- **Promotion lane path:** `release/uninotas-smart-notas -> main` por PR já planejado para a entrega local consolidada
- **Lane-promoted threshold for this TODO:** `main`
- **Production-ready threshold for this TODO:** `Railway stage` após o cutover governante

## Scope
- [ ] `SCOPE-01` Mapear o campo Smart Notas `nome` para `recipientName` opcional no DTO fiscal normalizado de resumo e detalhe, com limite defensivo e sem expor os demais campos pessoais.
- [ ] `SCOPE-02` Exibir na Geral uma coluna `Tomador` com o nome completo ou `Não disponível`, mantendo tabela acessível e responsiva.
- [ ] `SCOPE-03` Exibir `purchaseId`, `accessKey` e `referencedAccessKey` integralmente na área fiscal autenticada, com quebra/cópia visual segura, removendo apenas a máscara de apresentação.
- [ ] `SCOPE-04` Preservar os filtros, paginação, cache, atualização e exportação existentes sem alterar sua semântica.
- [ ] `SCOPE-05` Cobrir contrato NestJS, normalização React, estados ausentes e jornada browser da Geral/detalhe.
- [ ] `SCOPE-06` Atualizar módulo fiscal, feature brief e contratos operacionais estáveis sem registrar valores reais de PII ou identificadores fiscais.

## Out of Scope
- [ ] Alterar perfis, autenticação ou conceder acesso a usuários não autenticados.
- [ ] Expor documento, e-mail, telefone, endereço, inscrições, retorno bruto ou `providerIdInterno`.
- [ ] Persistir notas/PII em Prisma, PostgreSQL, arquivo, `localStorage`, `sessionStorage` ou IndexedDB.
- [ ] Alterar emissão, cancelamento, PDF/DANFE, XML, Routerfy/n8n, Railway ou deploy.
- [ ] Criar lista agregada Unifast + Prosperar.
- [ ] Criar filtro por número da nota, varrer páginas do provedor ou criar projeção/índice fiscal local.
- [ ] Adicionar o nome do tomador ao CSV existente.

## Bounded But Elastic Guardrails
- **May stay inside this TODO:** DTO/campo normalizado, adapter, Geral/detalhe, CSS e testes diretamente necessários ao mesmo objetivo.
- **Must update or split the TODO:** novo filtro, índice/projeção fiscal persistente, worker/sincronização, novo endpoint externo, mudança de perfis, nova fonte ou ampliação do CSV.

## Definition of Done
- [ ] `DOD-01` A Geral mostra o nome do tomador para registros que o Smart Notas devolve com `nome`, sem consultar PostgreSQL.
- [ ] `DOD-02` Compra e chaves são mostradas completas somente dentro das rotas autenticadas existentes e continuam ausentes de logs, URLs e armazenamento persistente.
- [ ] `DOD-03` Campos pessoais não aprovados continuam excluídos por allowlist do adapter e do DTO público.
- [ ] `DOD-04` Filtros, paginação, cache e exportação mantêm a semântica atual sem regressão.
- [ ] `DOD-05` A tabela permanece utilizável em desktop e mobile, incluindo valores longos de compra/chave e nome ausente.
- [ ] `DOD-06` Testes e documentação provam a ampliação deliberada de PII/identificadores sem persistir exemplos reais.

## Validation Steps
- [ ] `VAL-01` Executar testes unitários/contratuais do adapter, DTO, serviço e controller fiscal com fixtures sintéticas.
- [ ] `VAL-02` Executar `cd backend && npm test -- --runInBand && npm run build && npm run lint` no runner proprietário do projeto.
- [ ] `VAL-03` Executar `cd frontend && npm run test:notas && npm run test:notas:race && npm run build && npm run lint` no runner proprietário do projeto.
- [ ] `VAL-04` Executar `cd frontend && npm run e2e:notas` contra bundle fresco, cobrindo nome, valores completos, paginação e exportação sem regressão.
- [ ] `VAL-05` Executar revisão de segurança sobre PII, identificadores, logs, URL, cache, logout e respostas de erro.

## Diff Expectation Contract (Required Before Delivery)
- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines
| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `MonitorNotes` | `.` | `release/uninotas-smart-notas@8a0dba94a39da67fdd9979563beabb364371968a` | `working_tree` |
| `uninotas-foundation` | `foundation_documentation` | `main@c4056a9726eebd857f6288049b3ca7cfd08384f9` | `working_tree` |

### Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/src/fiscal-notes/**` | `M|A` | contrato, adapter, serviço e testes fiscais |
| `MonitorNotes` | `frontend/src/api/notas.ts` | `M` | DTO público do cliente |
| `MonitorNotes` | `frontend/src/notas/**` | `M` | normalização e testes |
| `MonitorNotes` | `frontend/src/paginas/ListaNotas.tsx` | `M` | filtro e coluna do tomador/identificadores |
| `MonitorNotes` | `frontend/src/paginas/DetalheNota.tsx` | `M` | tomador e identificadores completos |
| `MonitorNotes` | `frontend/src/estilos/**` | `M` | tabela responsiva e valores longos |
| `MonitorNotes` | `frontend/e2e/**` | `M` | jornada browser |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `M` | decisões estáveis |
| `uninotas-foundation` | `artifacts/feature-briefs/uninotas-fiscal-workspace-improvements.md` | `M` | terceira story e estado |
| `uninotas-foundation` | `todos/active/features/TODO-uninotas-fiscal-note-visibility.md` | `A|M|D` | contrato e closeout |

### Not Expected Changed Paths
| Repository | Path glob | Change types | Reason |
| --- | --- | --- | --- |
| `MonitorNotes` | `backend/prisma/**` | `any` | nenhuma persistência ou migração |
| `MonitorNotes` | `backend/src/logs/**` | `any` | PostgreSQL não participa da lista fiscal |
| `MonitorNotes` | `.env*` | `any` | nenhum segredo/config novo |
| `MonitorNotes` | `Dockerfile` | `any` | runtime fora do escopo |
| `MonitorNotes` | `artifacts/**` | `any` | artefatos locais preexistentes não pertencem ao TODO |

## Package-First Assessment
- **Queries executed:** `bash delphi-ai/tools/query_packages.sh --project-root . --search "fiscal"`; `--search "export"`.
- **Relevant packages found:** nenhum.
- **READMEs read:** `n/a`.
- **Decision:** implementação host-local nos módulos fiscal NestJS/React existentes; nenhum pacote novo.
- **Tier:** `Local`.
- **Rationale:** alteração específica do contrato Smart Notas e da tela Geral, sem utilitário reutilizável novo.

## Profile Scope & Handoffs (Required Before `APROVADO`)
- **Primary execution profile:** `operational-coder`
- **Active technical scope:** `react,vite,nestjs,cross-stack`
- **Expected supporting profiles:** `assurance-tester-quality,assurance-security-adversarial`
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile operational-coder`

### Handoff Log
| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| `operational-coder` | `assurance-tester-quality` | contrato público e jornada visível | backend/frontend/tests | `planned` |
| `operational-coder` | `assurance-security-adversarial` | nova PII e identificadores completos | DTO/cache/log/UI | `planned` |

## Complexity
- **Level:** `medium`
- **Checkpoint policy:** `one checkpoint`
- **Why this level:** mudança coesa, porém cross-stack, pública, visível e sensível a PII e identificadores fiscais.

## Canonical Module Anchors (Required Before APROVADO)
- **Primary module doc:** `foundation_documentation/modules/fiscal-notes-and-documents.md`
- **Secondary module docs:** `none`
- **Planned decision promotion targets:** `Canonical Decision Register`, `Purpose, Owned Entities, and Workflows`, `API Endpoint Definitions`, `Invariants`.
- **Module decision consolidation targets:** decisões de visibilidade/autorização e DTO do tomador.

## Decision Pending (Resolve Before Freeze)
- [x] Nenhuma decisão material permanece pendente.

## Decisions (Resolved Before Freeze)
- [x] `D-01` `nome` do Smart Notas será exposto como `recipientName` e apresentado como `Tomador`; somente esse campo pessoal adicional entra na allowlist.
- [x] `D-02` Todos os perfis autenticados atuais (`ADMIN|GESTOR|ANALISTA|LEITOR`) pertencem à equipe financeira e podem ver nome, compra e chaves completos nas rotas fiscais já protegidas.
- [x] `D-03` Documento e compra continuam efêmeros e aplicados explicitamente; contexto/status/datas continuam automáticos.
- [x] `D-04` O filtro por número foi cancelado pelo usuário em 2026-09-28 e está fora do escopo; nenhuma varredura de páginas, filtro local parcial ou projeção persistente será criada.
- [x] `D-05` A exportação existente já contém compra/chave completas e não ganha automaticamente o nome do tomador; ampliar o CSV com PII exige pedido/decisão separado.
- [x] `D-06` Nome/compra/chaves não entram em URL, logs, telemetria ou armazenamento persistente; o cache continua apenas em memória e é limpo com a sessão.

## Module Decision Baseline Snapshot (Required Before APROVADO)
| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `FISC-EX-01` | exporta todos os filtros aplicados | `Preserve` | módulo `Canonical Decision Register` |
| `FISC-EX-08` | compra/chave brutas permitidas no CSV; PII excluída | `Preserve` | módulo `CSV schema` |
| fiscal read DTO | DTO atual exclui toda PII do tomador | `Supersede (Intentional)` | módulo `Purpose, Owned Entities, and Workflows` |
| provider-supported search | primeiro contrato expõe somente filtros do provedor | `Preserve`; número permanece fora do escopo | discovery `Complete Capability Matrix > Search` |

## Decision Baseline (Frozen Before Implementation)
- [x] `D-01` Expor apenas `recipientName` como nova PII normalizada.
- [x] `D-02` Mostrar tomador, compra e chaves completos a todos os leitores autenticados atuais.
- [x] `D-03` Manter campos sensíveis efêmeros, fora da URL/persistência/logs.
- [x] `D-04` Não implementar filtro por número neste TODO.
- [x] `D-05` Não ampliar o CSV com nome do tomador neste TODO.
- [x] `D-06` Preservar filtros, cache, paginação e exportação existentes.

## Architecture Change Governance
- **Applicability:** `required`
- **Why this applies:** o TODO amplia intencionalmente o contrato de privacidade que antes excluía toda PII do tomador.
- **Deviation / debt being retired:** máscara visual deixou de atender à necessidade da equipe financeira; nenhuma dívida de origem de dados será resolvida por fallback.
- **Target steady-state after closeout:** DTO allowlisted expõe somente o nome aprovado e os identificadores já existentes; a pesquisa continua limitada aos filtros publicados pelo provedor.
- **Temporary exceptions allowed:** `none`.
- **Cutover / removal condition:** `n/a`.

### Patterns To Enforce
| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| DTO allowlist | NestJS fiscal adapter | provider -> API | impede vazamento de payload/PII não aprovado |
| ephemeral sensitive filters | módulo fiscal `Invariants` | React cache/query | evita URL/storage/log exposure |
| provider-supported filter boundary | `D-04` | list/export | impede filtro parcial ou varredura dispendiosa |

### Anti-Patterns To Prohibit
| Anti-Pattern | Prohibited Surface | Protection Harness |
| --- | --- | --- |
| espalhar payload bruto do Smart Notas | adapter/DTO/frontend | contract tests e normalização allowlisted |
| introduzir pesquisa por número disfarçada | React/adapter | diff review e contract tests dos filtros permitidos |
| persistir nome/chaves/compra | URL/browser/db/logs | testes de URL/cache/logout e security review |

## Assumptions Preview
| ID | Assumption | Evidence | Contract Impact |
| --- | --- | --- | --- |
| `A-01` | `nome` é o nome/razão social do tomador | live-shape redigida em ambos os contextos no discovery; payload Prosperar revalidado em 2026-09-28 | nova coluna/DTO |
| `A-02` | leitores atuais são membros da equipe financeira | confirmação explícita do usuário em 2026-09-28 | autorização existente é preservada |
| `A-03` | compra/chave já chegam completos e só são mascarados no React | adapter, DTO e `normalizacaoFiscal.ts` | mudança predominantemente de apresentação |
| `A-04` | Smart Notas não oferece filtro por número | OpenAPI e probe redigido com quatro aliases ignorados | justifica a exclusão aprovada em `D-04` |

## Execution Plan
1. Adicionar testes fail-first para `recipientName`, allowlist e exibição integral.
2. Estender adapter, tipos e serviço fiscal sem alterar query/filtros.
3. Estender tipos/normalização, Geral e detalhe React.
4. Ajustar tabela responsiva e preservar a jornada existente de filtros/exportação.
5. Executar testes focados, suites completas, browser fresco e segurança.
6. Consolidar módulo/feature brief e executar gates de entrega/closeout.

## Test Strategy
- **Intent:** `critical-user-journey` e `compatibility`.
- **Approach:** `test-first` para DTO/normalização e regressões visuais; fixtures exclusivamente sintéticas.
- **Fail-first targets:** nome presente/ausente, PII extra descartada, compra/chave completas, quebra visual de valores longos e preservação dos filtros/exportação existentes.
- **Deliberate exclusions:** nenhum payload real, segredo, CNPJ, nome real ou identificador real será persistido em teste/artifact.

## Frontend / Consumer Matrix
| Producer | Consumer | Contract Change | Compatibility / Evidence |
| --- | --- | --- | --- |
| `GET /api/v1/notas` | `ListaNotas` | adiciona `recipientName`; filtros permanecem inalterados | additive DTO + contract/browser tests |
| `GET /api/v1/notas/:noteId` | `DetalheNota` | adiciona `recipientName`; valores já existentes deixam de ser mascarados | additive DTO + browser tests |
| `GET /api/v1/notas/exportar` | export action | nenhum contrato muda | regression tests existentes |

## Flow Evidence Planning Matrix
| Flow | Intended Evidence | Preconditions | Status |
| --- | --- | --- | --- |
| Geral com tomador/IDs completos | `frontend/e2e/notas.mjs` | bundle fresco e API interceptada com fixtures sintéticas | `planned` |
| detalhe com tomador/IDs completos | `frontend/e2e/notas.mjs` | bundle fresco e API interceptada com fixtures sintéticas | `planned` |
| filtro + paginação + exportação sem regressão | unit/race/browser | contratos atuais preservados | `planned` |

## Local CI-Equivalent Suite Matrix
| Owner | Command | Scenario Proved | Preconditions | Status |
| --- | --- | --- | --- | --- |
| backend | `npm test -- --runInBand` | adapter/DTO/query/list/export/privacy | runner Node do projeto e fixtures sintéticas | `planned` |
| backend | `npm run build && npm run lint` | tipos/build/estilo | dependências instaladas | `planned` |
| frontend | `npm run test:notas && npm run test:notas:race` | normalização e regressão de cache/filtros/corridas | runner Node do projeto | `planned` |
| frontend | `npm run build && npm run lint` | bundle/tipos/estilo | dependências instaladas | `planned` |
| frontend | `npm run e2e:notas` | jornada visível e responsiva | bundle fresco + Chrome local | `planned` |

## Audit Trigger Matrix
| Signal | Result | Rationale |
| --- | --- | --- |
| shared/public API contract | `yes` | DTO fiscal recebe campo aditivo |
| security/privacy | `yes` | nome e identificadores completos |
| performance-sensitive search | `no` | pesquisa por número foi cancelada e query não muda |
| retriggerable async UI | `no-new-risk` | async/cache/filtros permanecem inalterados |
| persistence/schema | `no` | nenhuma persistência ou migração |
| architecture decision review | `required` | supersede intencional do contrato de privacidade |
| independent critique | `required` | complexidade medium + API/privacy |
| triple review | `pending-guard` | será derivado pelo audit escalation guard |

## Plan Review Gate
- **Status:** `prepared-pending-freeze`
- **Architecture:** Smart Notas permanece autoridade; o DTO público amplia somente a allowlist de nome.
- **Code quality:** um campo canônico `recipientName`; sem lógica duplicada de masking/filtering.
- **Tests:** contrato e browser cobrem valores longos/ausentes e preservam filtros/exportação.
- **Performance:** nenhuma chamada upstream, varredura, query ou cardinalidade nova.
- **Security:** ampliação é allowlisted e autorizada para leitores financeiros; demais PII continua proibida.

## Gate: Review Baseline Freeze
- **Status:** `pending-freeze`
- **Branch / commit / push:** `pending`
- **Reason:** o contrato foi reconvergido após o cancelamento do filtro e aguarda commit/push antes das revisões.

## Rules Acknowledgement / Ingestion
| Rule / Workflow / Skill | Why It Applies | Pre-Approval Status |
| --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | autoridade e gates | `prepared` |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | estado do TODO | `prepared` |
| `delphi-ai/workflows/react/change-ui-boundary-method.md` | Geral/detalhe/filtros | `prepared` |
| `delphi-ai/workflows/nestjs/change-application-boundary-method.md` | DTO/query/serviço | `prepared` |
| `delphi-ai/skills/package-first-verification/SKILL.md` | package-first | `ingested` |
| `delphi-ai/skills/test-creation-standard/SKILL.md` | cobertura cross-stack | `prepared` |
| `delphi-ai/skills/security-adversarial-review/SKILL.md` | PII/identificadores | `prepared` |

## Agent Routing Preflight
- **Status:** `planned`
- **Execution surface:** `product-code`
- **Role:** `operational-coder`
- **Model / effort:** `inherited / implementation-focused`
- **Topology:** `primary-checkout-single-writer`
- **Subagent / delegation authorization:** `not_authorized_for_implementation`
- **Git isolation authorization:** `not_authorized`; worktrees/auxiliary checkouts remain forbidden.

## Approval
- **Status:** `not_requested`
- **Reason:** planning reviews and authority preflight are pending.
- **Renewed approval trigger:** any new persistence, source, role, export PII or partial-search semantics.

## Security Risk Assessment
- **Risk level:** `high`
- **Why this risk level:** intentional exposure of one PII field and full fiscal/order identifiers through an authenticated public contract.
- **Attack surface in scope:** JWT authorization, DTO allowlist, provider payload, browser memory/cache, URL/log/error/telemetry and long-value rendering.
- **Attack simulation decision:** `recommended`
- **Review evidence:** `planned via security-adversarial-review`.
- **Residual security risk:** disclosure remains possible to any compromised authorized finance account; no field-level role reduction was requested.

## Performance & Concurrency Risk Assessment
- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `low`
- **Why this level:** os mesmos registros e chamadas são mantidos; somente um campo allowlisted adicional e a apresentação deixam de mascarar identificadores já recebidos.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | `endpoint-performance-scrutiny` | `not_needed` | `low` | `n/a-query-unchanged` | `before_local_implemented` | `n/a` | `not_applicable` | `none` | `none` |
| `FRC` | `frontend-race-condition-validation` | `not_needed` | `low` | `n/a-async-unchanged` | `before_local_implemented` | `n/a` | `not_applicable` | `none` | `none` |
| `BCI` | `backend-concurrency-idempotency-validation` | `not_needed` | `low` | `n/a-read-only` | `before_local_implemented` | `n/a` | `not_applicable` | `none` | `none` |
| `RLS` | `runtime-load-stress-validation` | `not_needed` | `low` | `n/a-load-shape-unchanged` | `before_local_implemented` | `n/a` | `not_applicable` | `none` | `none` |

## TODO Closeout Disposition
- **Disposition:** `keep-active`
- **Disposition reason:** contrato reconvergido e aguardando aprovação/implementação.
- **Post-commit/push status:** `pending`
- **Next path/status action:** completar gates pré-aprovação e solicitar `APROVADO`.

## Commands (Run Locally)
- `bash delphi-ai/tools/query_packages.sh --project-root . --search "fiscal"`
- `python3 delphi-ai/tools/node_capability_surface_audit.py --repo . --expect react --manifest frontend/package.json`
- `python3 delphi-ai/tools/node_capability_surface_audit.py --repo . --expect nestjs --manifest backend/package.json`
- comandos de validação definidos em `Local CI-Equivalent Suite Matrix` após aprovação.
