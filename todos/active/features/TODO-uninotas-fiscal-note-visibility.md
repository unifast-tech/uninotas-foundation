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

### Architecture Protection Harness
| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| `test` | Smart Notas adapter/DTO | `backend/src/fiscal-notes/smart-notas.adapter.spec.ts`; backend full suite | PII não aprovada atravessando a allowlist | `implement-in-this-todo` | `DOD-03`, `VAL-01`, `VAL-02` |
| `test` | React normalization/UI | frontend fiscal tests + `npm run e2e:notas` | nome ausente quebrando UI ou identificadores ainda mascarados | `implement-in-this-todo` | `DOD-01`, `DOD-02`, `DOD-05`, `VAL-03`, `VAL-04` |
| `audit` | contrato de privacidade | `security-adversarial-review` | PII/IDs em URL, storage, logs ou erro | `implement-in-this-todo` | `DOD-06`, `VAL-05` |

## Architecture Review Gates (Deterministically Derived From Architecture Change Governance)
- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-summary`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** `pending`
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending`
- **No-go handling:** `when either required review is absent, blocked, or exposes an unresolved approval-breaking divergence, return to the affected diagnosis/decision or delivery-evidence loop; do not claim APROVADO or Completed.`

## Assumptions Preview
| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | `nome` é o nome/razão social do tomador | `todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md`; observed field matrix | label/semantics must be corrected before implementation | `High` | `Promote to Decision` via `D-01` |
| `A-02` | leitores atuais são membros da equipe financeira | user confirmation dated 2026-09-28; `frontend/src/paginas/Equipe.tsx` roles | authorization contract must be redesigned | `High` | `Promote to Decision` via `D-02` |
| `A-03` | compra/chave already arrive complete and are masked only in React | `backend/src/fiscal-notes/smart-notas.adapter.ts`; `frontend/src/notas/normalizacaoFiscal.ts`; `frontend/src/paginas/ListaNotas.tsx` | backend/provider contract work would be required | `High` | `Keep as Assumption` |
| `A-04` | Smart Notas não oferece filtro por número | official OpenAPI plus redacted probe; discovery search matrix | exclusion remains harmless, but a future TODO may reconsider | `High` | `Keep as Assumption` |

## Execution Plan
### Touched Surfaces
- `backend/src/fiscal-notes/**`
- `frontend/src/api/notas.ts`
- `frontend/src/notas/normalizacaoFiscal.ts`
- `frontend/src/paginas/ListaNotas.tsx`
- `frontend/src/paginas/DetalheNota.tsx`
- `frontend/src/estilos/**`
- `frontend/e2e/notas.mjs`
- canonical fiscal module, feature brief and this TODO

### Ordered Steps
1. Adicionar testes fail-first para `recipientName`, allowlist e exibição integral.
2. Estender adapter, tipos e serviço fiscal sem alterar query/filtros.
3. Estender tipos/normalização, Geral e detalhe React.
4. Ajustar tabela responsiva e preservar a jornada existente de filtros/exportação.
5. Executar testes focados, suites completas, browser fresco e segurança.
6. Consolidar módulo/feature brief e executar gates de entrega/closeout.

## Test Strategy
- **Intent:** `critical-user-journey` e `compatibility`.
- **Strategy:** `test-first` para DTO/normalização e regressões visuais; fixtures exclusivamente sintéticas.
- **Why:** a mudança é observável, aditiva no contrato e sensível à privacidade.
- **Fail-first target(s):** nome presente/ausente, PII extra descartada, compra/chave completas, quebra visual de valores longos e preservação dos filtros/exportação existentes.
- **Deliberate exclusions:** nenhum payload real, segredo, CNPJ, nome real ou identificador real será persistido em teste/artifact.

### Pre-APROVADO RED Evidence Capture
- **Decision:** `not_needed`
- **Why now:** não é correção de bug/regressão e o comportamento solicitado está suficientemente definido.
- **Target symptom:** `n/a`
- **Allowed surfaces:** `n/a`
- **Forbidden surfaces reaffirmed:** `production code|runtime/config/deploy|canonical project docs outside TODO authoring`
- **Planned command / target:** `n/a`
- **Status:** `not_run`
- **Findings summary:** `n/a`

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

## Plan Review Gate

### Review Sections
- [x] Architecture — Smart Notas permanece autoridade; o DTO público amplia somente a allowlist de nome.
- [x] Code Quality — um campo canônico `recipientName`; nenhuma lógica de filtro, busca ou persistência nova.
- [x] Tests — contrato e browser cobrem valores longos/ausentes e preservam filtros/exportação.
- [x] Performance — nenhuma chamada upstream, varredura, query ou cardinalidade nova.
- [x] Security — ampliação allowlisted e autorizada para leitores financeiros; demais PII continua proibida.
- [x] Elegance — extensão aditiva do record existente e remoção da máscara no consumidor, sem novo serviço/abstração.
- [x] Structural Soundness — adapter continua sendo o limite de payload e o frontend recebe somente DTO normalizado.

### Issue Cards
- **Issue ID:** `SEC-01`
  - **Severity:** `medium`
  - **Evidence:** contrato atual exclui PII em `modules/fiscal-notes-and-documents.md`; usuário autorizou nome completo a todos os leitores financeiros.
  - **Why it matters now:** ampliar PII sem allowlist estreita poderia expor documento, contato ou endereço por acidente.
  - **Option A (Recommended):** adicionar somente `recipientName` ao record normalizado e manter todos os demais campos fora do DTO.
    - **Effort:** `low`
    - **Risk:** `medium`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `low`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `improves`
    - **Structural soundness impact:** `improves`
  - **Option B (Alternative):** expor um objeto completo do tomador e ocultar campos no React.
    - **Effort:** `low`
    - **Risk:** `high`
    - **Blast radius:** `cross-module`
    - **Maintenance burden:** `high`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `regresses`
    - **Structural soundness impact:** `regresses`
  - **Option C (Do Nothing):** manter nome excluído e identificadores mascarados.
    - **Effort:** `low`
    - **Risk:** `low`
    - **Blast radius:** `local`
    - **Maintenance burden:** `low`
    - **Performance impact:** `neutral`
    - **Elegance impact:** `neutral`
    - **Structural soundness impact:** `neutral`
  - **Recommendation:** `Option A`, pois atende a equipe financeira com minimização explícita e preserva o adapter como trust boundary.

### Failure Modes & Edge Cases
- [x] `nome` ausente/null: renderizar `Não disponível` sem falhar a página.
- [x] compra/chave ausentes: manter `Não disponível` em vez de string vazia.
- [x] valores longos: permitir quebra/cópia sem alargar indefinidamente a tabela.
- [x] payload com PII adicional: descartar no adapter/normalizador e provar por teste negativo.
- [x] CSV existente: não adicionar nome e preservar contrato/ordem atual.

### Residual Unknowns / Risks
- [x] Uma conta financeira comprometida verá os dados completos autorizados; risco residual aceito para esta superfície autenticada e revisto no gate de segurança.

## Additional Architectural Opinions
- **Needed:** `no`
- **Why ambiguity remains:** `n/a`; o filtro foi cancelado e resta um único caminho dominante de DTO allowlisted.
- **Opinion count:** `0`
- **Package mode:** `bounded-summary`
- **Internal reviewer mandate:** `not_needed`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

## Audit Trigger Matrix (Required Before Audit Decisions Are Trusted)
- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-visibility.md`
- **Latest TEACH evidence / artifact:** `Overall outcome: go`; fingerprint `44e80676b588`; architecture decision review and critique required before approval; delivery audits derived as recorded below.

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `medium` | cross-stack API/UI/privacy change |
| `blast_radius` | `cross-stack` | NestJS producer and React consumers |
| `behavioral_change_or_bugfix` | `yes` | new visible field and unmasked identifiers |
| `changes_public_contract` | `yes` | additive `recipientName` field |
| `touches_auth_or_tenant` | `no` | profiles and guards remain unchanged |
| `touches_runtime_or_infra` | `no` | no deploy/runtime/config change |
| `touches_tests` | `yes` | contract/unit/browser fixtures and assertions change |
| `critical_user_journey` | `yes` | finance note identification in Geral/detail |
| `release_or_promotion_critical` | `yes` | requested for the pending delivery package |
| `high_severity_plan_review_issue` | `no` | SEC-01 is medium and resolved in the plan |
| `explicit_three_lane_request` | `no` | user did not request dedicated three-lane protocol |

## Independent No-Context Critique Gate
- **Critique decision:** `required`
- **Why this decision:** medium cross-stack public-contract and privacy change.
- **Impact signals in scope:** `cross-stack blast radius|public contract/api|intentional module supersede`
- **Package mode:** `bounded-summary`
- **Package minimum contents:** `frozen baseline|scope boundary|assumptions|execution plan|SEC-01|security residual`
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required; fresh no-context reviewer distinct from the architecture-opinion reviewer and implementing agent`
- **Canonical multi-lane audit protocol:** `audit-protocol-triple-review` (required before Completed; additive, not a substitute for planning critique)
- **Audit session / round evidence:** `delivery-side; pending implementation`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Gate: Assumption Code Coherence
- **Gate decision:** `required`
- **Why this decision:** A-01 through A-03 directly determine the public DTO and presentation change.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-01,A-02,A-03,A-04`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-visibility.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Gate: Review Baseline Freeze
- **Gate decision:** `required`
- **Why this decision:** planning-side reviews must evaluate a committed and pushed scope-bearing contract.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `main`
- **Baseline commit:** `9d389bdcbbf2858cf068335936f82eb808064172`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** scope-bearing contract frozen after removal of number search.
- **Evidence / reference:** authority guards returned `go`; remote advanced `c4056a9..9d389bd`.
- **Waiver authority / reference:** `n/a`
- **Pre-freeze packet-prep rule:** `satisfied; no review result predates the freeze`

## Gate: Review Scope Drift
- **Gate decision:** `required`
- **Why this decision:** scope-bearing sections must remain aligned with the frozen no-number-search contract.
- **Trigger stage:** `after the planning-side review/guard cycle converges and before APROVADO`
- **Baseline source:** `Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `Context|Contract Boundary|Scope|Out of Scope|Definition of Done|Validation Steps|Execution Lane Tracking|Canonical Module Anchors|Decisions|Decision Baseline|Architecture Change Governance|Questions To Close|Assumptions Preview|Execution Plan|Flow Evidence Planning Matrix|Local CI-Equivalent Suite Matrix|Runtime / Rollout Notes|Security Risk Assessment|Performance & Concurrency Risk Assessment`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo foundation_documentation/todos/active/features/TODO-uninotas-fiscal-note-visibility.md`
- **No-go handling rule:** `return to review, revalidate material changes with the user and refresh the pushed baseline`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Questions To Close
- [x] Nenhuma pergunta material permanece; o filtro por número foi explicitamente cancelado.

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
