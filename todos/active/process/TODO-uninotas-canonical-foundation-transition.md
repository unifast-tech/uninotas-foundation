# TODO — Canonicalizar a Foundation para a arquitetura UniNotas

## Artifact Identity

- **Artifact type:** `tactical_execution_contract`
- **Lifecycle state:** `Active — planning`
- **Created:** `2026-09-25`
- **Owner:** `Delphi / Strategic CTO-Tech-Lead`, sob autoridade humana do usuário

## Context

O produto em execução ainda é documentado como Monitor de Notas, com PostgreSQL `logs` como fonte de toda a experiência. A direção confirmada para UniNotas muda essa autoridade: Smart Notas passa a fornecer todas as notas e documentos; PostgreSQL permanece apenas como evidência de falhas de integração; Unifast e Prosperar são dois contextos fiscais, não tenants. Implementar o adapter NestJS antes de consolidar essa arquitetura criaria conflito entre código e Foundation.

O validador atual também congela exatamente a árvore criada no rebase inicial. Por isso, os artefatos de descoberta já aprovados aparecem como `frozen lifecycle tree mismatch`. A correção do contrato de publicação faz parte deste mesmo cutover canônico, preservando as proteções de privacidade, symlink, legado, identidade e contratos.

## Framing Source & Story Slice

- **Feature brief:** `artifacts/feature-briefs/uninotas-smart-notas-central.md`
- **Primary story ID:** `ST-02`
- **Why this is the right current slice:** a correção canônica é o pré-requisito explícito de `ST-03`; ela resolve uma única conversa de autoridade documental sem alterar o runtime.
- **Direct-to-TODO rationale:** `n/a — feature brief existente`.

## Objective

Estabelecer na Foundation a identidade UniNotas, a topologia `FastPay (Routerfy) -> n8n -> Smart Notas`, a separação entre notas da API e falhas do PostgreSQL, os dois contextos fiscais e os futuros owners de notas, falhas e casos operacionais, distinguindo rigorosamente comportamento atual de arquitetura-alvo e tornando o validador de publicação apto a governar a árvore evolutiva.

## Contract Boundary

- Este TODO define **WHAT** será entregue e o que conta como concluído.
- `Assumptions Preview` e `Execution Plan` definem **HOW** a entrega é atualmente planejada.
- O contrato é **bounded but elastic** somente para refinamentos locais da mesma transição canônica.
- Nova rota, código de produto, schema, migração, configuração runtime ou comportamento de UI exige TODO próprio e aprovação separada.

## Implementation Intent

- **Current delivery:** cutover documental da arquitetura UniNotas e evolução do validador/manifesto da própria Foundation.
- **Planned next steps:** TODO NestJS de leitura Smart Notas por contexto fiscal; TODO de DANFE; TODO React de contexto/cache; TODO de falhas/casos operacionais.
- **Anticipatory implementation authorized now:** `none`.
- **Rationale:** a Foundation deve declarar a arquitetura aprovada e separar `Current` de `Target` antes que o primeiro adapter de produto seja implementado.

## Delivery Status Canon (Required)

- **Current delivery stage:** `Pending`
- **Qualifiers:** `none`
- **Next exact step:** concluir o contrato, congelar e publicar o baseline de revisão, executar as revisões/guards de planejamento e obter `APROVADO`.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `implementation`
- **Why this state now:** o TODO está sendo refinado; nenhuma implementação de Foundation fora deste próprio arquivo foi iniciada.
- **Exit condition:** baseline aprovado, implementação validada e gates de entrega concluídos.

## Scope

- [ ] Canonicalizar `UniNotas` como nome do produto, preservando `MonitorDeNotas` como nome técnico do repositório nesta entrega.
- [ ] Registrar a topologia externa confirmada e a propriedade de dados: Smart Notas para notas/documentos, PostgreSQL `logs` somente para falhas de integração.
- [ ] Registrar Unifast e Prosperar como `FiscalIssuerContext`, sem tenancy e sem agregação inicial de notas.
- [ ] Separar explicitamente comportamento atual e arquitetura-alvo nas raízes, decisões, roadmap e módulos afetados.
- [ ] Criar owners canônicos planejados para notas/documentos fiscais, ocorrências de falha de integração e casos operacionais.
- [ ] Atualizar a política de scope/subscope e os índices sem inventar módulos de runtime já implementados.
- [ ] Evoluir o validador e seus testes para a nova identidade, módulos e publicação governada, mantendo proteções existentes.
- [ ] Publicar no manifesto os artefatos de descoberta e este TODO sem persistir segredos, CNPJs, IDs, payloads, respostas ou URLs privadas.

## Out of Scope

- [ ] Alterar backend, frontend, Prisma, PostgreSQL, Docker, Railway, `.env` ou qualquer configuração runtime.
- [ ] Criar rotas Smart Notas, cache, download de DANFE/XML ou UI de seleção fiscal.
- [ ] Implementar `OperationalCase`, migrar tratamentos ou decidir agrupamento/correlação de falhas.
- [ ] Investigar ou alterar a automação n8n/FastPay.
- [ ] Realizar chamadas adicionais à API Smart Notas ou registrar qualquer valor de credencial/identificador.
- [ ] Renomear repositórios, diretórios, pacotes, imagens ou serviços técnicos.
- [ ] Usar worktrees, checkouts auxiliares, `worker/*` ou `reconcile/*`.

## Delivery Status Semantics

- `Pending`: nenhuma entrega material foi concluída.
- `Local-Implemented`: o cutover documental e o harness foram implementados e validados localmente.
- `Lane-Promoted`: a entrega atingiu a lane `dev` declarada.
- `Production-Ready`: a entrega foi publicada em `main` após todos os gates.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `uninotas-foundation:feature/uninotas-canonical-foundation-transition`
- **Promotion lane path:** `feature/uninotas-canonical-foundation-transition -> dev -> stage -> main`
- **Lane-promoted threshold for this TODO:** `dev`
- **Production-ready threshold for this TODO:** `main`

## Promotion Evidence (Required Before Lane-Promoted / Production-Ready)

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| Foundation UniNotas cutover | `pending` | `pending` | `pending` | `pending` | planning |

## Diff Expectation Contract (Required Before Delivery)

- **Contract status:** `required`
- **Policy:** `strict; unclassified or forbidden paths block delivery`
- **User validation:** `required on deviation`
- **Comparison mode:** `working_tree`

### Repository Baselines

| Repository | Path | Baseline ref | Comparison mode |
| --- | --- | --- | --- |
| `uninotas-foundation` | `.` | `main@0fe906c` | `working_tree` |

### Expected Changed Paths

| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| `uninotas-foundation` | `README.md` | `M` | identidade canônica |
| `uninotas-foundation` | `project_mandate.md` | `M` | mandato UniNotas |
| `uninotas-foundation` | `project_constitution.md` | `M` | topologia e invariantes |
| `uninotas-foundation` | `domain_entities.md` | `M` | vocabulário do domínio |
| `uninotas-foundation` | `system_roadmap.md` | `M` | sequência de entrega |
| `uninotas-foundation` | `decisions/**` | `M|A` | decisões promovidas |
| `uninotas-foundation` | `modules/**` | `M|A` | owners atuais e alvo |
| `uninotas-foundation` | `policies/scope_subscope_governance.md` | `M` | novos subscopes explícitos |
| `uninotas-foundation` | `artifacts/README.md` | `M` | indexação dos artefatos |
| `uninotas-foundation` | `artifacts/feature-briefs/**` | `A|M` | framing já produzido |
| `uninotas-foundation` | `artifacts/publication-manifest.txt` | `M` | contrato de publicação |
| `uninotas-foundation` | `todos/active/process/**` | `A|M` | descoberta e autoridade tática |
| `uninotas-foundation` | `deterministic/validate_foundation.py` | `M` | validador evolutivo fail-closed |
| `uninotas-foundation` | `deterministic/tests/**` | `M|A` | mutações e regressões do validator |

### Not Expected Changed Paths

| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
| root/backend/frontend | `backend/**` | `any` | código de produto fora do escopo |
| root/backend/frontend | `frontend/**` | `any` | UI fora do escopo |
| root/backend/frontend | `Dockerfile` | `any` | runtime fora do escopo |
| root/backend/frontend | `.env*` | `any` | segredos/configuração fora do escopo |
| `uninotas-foundation` | `todos/completed/**` | `any` | história fechada é imutável nesta entrega |
| `uninotas-foundation` | `deterministic/legacy_reference_exceptions.json` | `any` | ledger histórico congelado não é reescrito |

### Diff Deviation Analysis (Required Only When the Guard Returns `no-go`)

| Diff item | Classification | Evidence / agent defense | Decision | User validation / renewed approval |
| --- | --- | --- | --- | --- |
| `n/a` | `n/a` | `guard ainda não executado` | `n/a` | `n/a` |

## Bounded But Elastic Guardrails

- **May stay inside this TODO:** correções locais de links, índices, fixtures do validador e semântica documental necessárias ao mesmo cutover.
- **Must update or split the TODO:** qualquer código de produto, mudança runtime, regra de autorização, contrato HTTP ou novo objetivo independente.

## Definition of Done

- [ ] `DOD-01` Identidade e mandato canônicos usam UniNotas sem renomear o repositório técnico.
- [ ] `DOD-02` Constituição e decisões registram a topologia externa e a separação de fontes aprovada.
- [ ] `DOD-03` Unifast/Prosperar são contextos fiscais explícitos e não tenants.
- [ ] `DOD-04` Módulos distinguem contratos atuais de owners/arquitetura-alvo, sem declarar código futuro como implementado.
- [ ] `DOD-05` Notas/documentos, falhas de integração e casos operacionais têm owners canônicos distintos.
- [ ] `DOD-06` Validator e suíte rejeitam regressões de identidade, ownership, tenancy, privacidade, symlink, legado e publicação.
- [ ] `DOD-07` Os artefatos atuais pertencem ao manifesto e a validação Foundation passa sem `frozen lifecycle tree mismatch`.
- [ ] `DOD-08` Nenhum segredo, CNPJ, ID, payload, resposta privada ou URL de documento foi persistido.
- [ ] `DOD-09` O roadmap aponta para o TODO NestJS de leitura como próximo slice, sem lhe conceder autoridade antecipada.

## Validation Steps

- [ ] `VAL-01` Executar fail-first e suíte: `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_foundation.py`.
- [ ] `VAL-02` Executar `python3 -B uninotas-foundation/deterministic/validate_foundation.py --root uninotas-foundation`.
- [ ] `VAL-03` Executar `bash delphi-ai/verify_context.sh` no runner aceito pelo projeto.
- [ ] `VAL-04` Executar os guards Delphi de diff, autoridade, conclusão e cutover definidos neste TODO.
- [ ] `VAL-05` Inspecionar `git diff --check` e o diff limitado a `uninotas-foundation`.

## Completion Evidence Matrix (Required Before Delivery Claim)

| Criterion ID | Source Section | Criterion | Evidence Type | Evidence Artifact / Command | Runtime Target | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DOD-01..DOD-05` | Definition of Done | coerência canônica UniNotas | doc/review | diff + validator + decisão de aderência | n/a | planned | sem runtime |
| `DOD-06..DOD-08` | Definition of Done | proteção determinística e privacidade | test | unittest + validator | local | planned | mutações negativas obrigatórias |
| `DOD-09` | Definition of Done | sequência do roadmap | doc/review | `system_roadmap.md` | n/a | planned | não autoriza backend |
| `VAL-01..VAL-05` | Validation Steps | comandos de validação | test/review | comandos exatos acima | local | planned | preencher após execução |

## External Dependency Readiness

| Dependency | Why It Matters | Status | Last Verified | Verification Method | Adjustment / Workaround |
| --- | --- | --- | --- | --- | --- |
| Smart Notas OpenAPI | fundamenta a arquitetura-alvo | healthy | 2026-09-25 | fingerprint e probes redigidos no ledger | nenhuma chamada nesta entrega |
| Git remote Foundation | necessário para baseline de revisão | unknown | n/a | `git_write_authority_guard` antes de commit/push | bloquear review até baseline publicado |

## Profile Scope & Handoffs (Required Before `APROVADO`)

- **Primary execution profile:** `strategic-cto`
- **Active technical scope:** `cross-stack`
- **Expected supporting profiles:** `operational-coder; assurance-tester-quality`
- **Scope-check command:** `python3 delphi-ai/tools/profile_scope_check.py --profile strategic-cto`

### Handoff Log

| From Profile | To Profile | Why the Handoff Exists | Touched Surfaces | Status / Evidence |
| --- | --- | --- | --- | --- |
| strategic-cto | operational-coder | implementar alterações determinísticas após congelamento estratégico | `deterministic/**` | planned |
| operational-coder | strategic-cto | consolidar constituição/mandato/decisões | roots, modules, policies | planned |
| strategic-cto | assurance-tester-quality | auditar harness e cutover | TODO + diff + tests | planned |

## Complexity

- **Level (`small|medium|big`):** `big`
- **Checkpoint policy:** `section-by-section`
- **Why this level:** altera identidade, ownership, módulo/scope e o harness fail-closed da autoridade documental, com blast radius transversal na Foundation.

## Canonical Module Anchors (Required Before APROVADO)

- **Primary module doc:** `modules/events-and-classification.md`
- **Secondary module docs:** `modules/treatments-and-history.md`, `modules/runtime-and-deployment.md`, `modules/identity-and-team.md`, `modules/realtime-invalidation.md`, `modules/operational-monitoring.md`
- **Planned decision promotion targets:** `project_mandate.md`, `project_constitution.md`, `domain_entities.md`, `system_roadmap.md`, `decisions/`, `modules/`, `policies/scope_subscope_governance.md`
- **Module decision consolidation targets:** novos owners `fiscal-notes-and-documents`, `integration-error-occurrences`, `operational-cases` e módulos atuais afetados.

## Decision Pending (Resolve Before Freeze)

- [ ] `none — decisões materiais abaixo serão confirmadas pelo APROVADO deste contrato`.

## Decisions (Resolved Before Freeze)

- [x] `D-01` O nome canônico do produto será UniNotas; o repositório técnico permanece `MonitorDeNotas` nesta entrega.
- [x] `D-02` Smart Notas é a fonte completa das notas e documentos; PostgreSQL `logs` é somente evidência de falhas de integração.
- [x] `D-03` Unifast e Prosperar são `FiscalIssuerContext` independentes, nunca tenants, organizações ou agregação implícita.
- [x] `D-04` A Foundation distinguirá `Current` de `Target`; documentação-alvo não poderá afirmar implementação inexistente.
- [x] `D-05` A arquitetura-alvo separa owners de notas/documentos, ocorrências de falha e casos operacionais.
- [x] `D-06` O validador deixa de ser uma fotografia do cutover inicial e passa a validar publicação governada e semântica atual, preservando todas as proteções existentes.

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `decisions#D-01` | produto Monitor de Notas | Supersede (Intentional) | `decisions/monitor-de-notas-foundation-decisions.md` |
| `decisions#D-04` | `logs` sustenta toda observação do monitor | Supersede (Intentional) | `project_constitution.md#invariants` |
| `decisions#D-05` | sem business tenancy | Preserve | `policies/scope_subscope_governance.md` |
| `events#ownership` | eventos de `logs` são o read model completo | Supersede (Intentional) | `modules/events-and-classification.md#ownership-invariant` |
| `treatments#ownership` | tratamento é ligado somente a `ref_id` | Supersede (Intentional) | `modules/treatments-and-history.md#specification` |
| `runtime#logs` | produção `logs` é externa e read-only | Preserve and narrow | `modules/runtime-and-deployment.md#observed-runtime-contract` |

## Decision Baseline (Frozen Before Implementation)

- [x] `D-01` UniNotas é a identidade canônica do produto; o nome técnico do repositório não muda.
- [x] `D-02` Toda nota/documento vem da Smart Notas; `logs` nunca é fallback ou espelho de notas bem-sucedidas.
- [x] `D-03` O contexto fiscal faz parte de identidade, resolução de credencial e isolamento, sem criar tenancy.
- [x] `D-04` Contratos atuais e arquitetura-alvo permanecem rotulados e verificáveis separadamente.
- [x] `D-05` Os três owners alvo são distintos e `OperationalCase` não altera fatos das fontes.
- [x] `D-06` A evolução do validator mantém fail-closed, privacidade e árvore manifestada sem congelar o produto no estado inicial.

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** a entrega supersede identidade, source ownership e arquitetura modular, além de corrigir um validator de cutover que bloqueia evolução normal.
- **Deviation / debt being retired:** Foundation afirma `logs` como fonte completa e valida apenas a árvore exata do rebase inicial.
- **Target steady-state after closeout:** UniNotas com verdade atual/alvo separada, owners explícitos e validação evolutiva fail-closed.
- **Temporary exceptions allowed:** documentos de comportamento atual podem conservar Monitor de Notas/rotas atuais apenas quando marcados como `Current` e sem autoridade sobre o alvo.
- **Cutover / removal condition:** todas as referências canônicas não-históricas aderem a D-01..D-06 e a suíte de mutação passa.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| current-versus-target explicit | D-04 | Foundation | evita declarar capacidade não implementada |
| source ownership split | D-02 | modules/domain | impede fallback silencioso em logs de sucesso |
| context is not tenancy | D-03 | scope/domain | impede vazamento conceitual e técnico |
| manifest + semantic guards | D-06 | deterministic | permite evolução sem perder fail-closed |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| `logs` como base de notas | ownership scanner/test | contradiz D-02 | nenhuma |
| Unifast/Prosperar como tenants | scope policy/test | contradiz D-03 | nenhuma |
| documento alvo rotulado Current sem código | status contract/test | cria falsa verdade | nenhuma |
| lista exata hard-coded sem política evolutiva | mutation test | repete o bloqueio atual | nenhuma |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| test | Foundation semantics | `test_validate_foundation.py` | identity/source/tenancy/current-target drift | implement-in-this-todo | mutation GREEN |
| guard | publication tree | `validate_foundation.py` + manifest | arquivo não governado, symlink, privacidade | implement-in-this-todo | validator GREEN |
| review | architecture | independent architecture/adherence review | supersede incompleto | implement-in-this-todo | review artifacts |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-summary`
- **Decision review status:** `not_run`
- **Decision review evidence / resolution:** `pending review baseline freeze`
- **Architecture adherence review:** `required`
- **Adherence review lifecycle:** `after implementation and before Completed`
- **Adherence review kind:** `architecture_adherence`
- **Adherence review package:** `bounded-file-set`
- **Adherence review status:** `not_run`
- **Adherence review evidence / resolution:** `pending implementation`
- **No-go handling:** retornar ao ciclo afetado; não solicitar aprovação nem concluir com divergência aberta.

## Gate: Review Baseline Freeze

- **Gate decision:** `required`
- **Why this decision:** a revisão altera decisões canônicas e precisa de pacote imutável.
- **Trigger stage:** `before the first planning-side review or guard run`
- **Baseline branch:** `feature/uninotas-canonical-foundation-transition`
- **Baseline commit:** `pending`
- **Baseline push reference:** `pending`
- **Gate status:** `not_run`
- **Findings summary:** `TODO ainda em preparação`.
- **Evidence / reference:** `pending git write authority guards`.
- **Waiver authority / reference:** `n/a`

## Gate: Review Scope Drift

- **Gate decision:** `required`
- **Why this decision:** decisões materiais devem permanecer idênticas ao baseline revisado.
- **Trigger stage:** `after planning reviews converge and before APROVADO`
- **Baseline source:** `Gate: Review Baseline Freeze -> Baseline commit`
- **Material sections compared:** `template canonical set`
- **Guard command:** `python3 delphi-ai/tools/review_scope_drift_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Questions To Close

- [x] Nome canônico: `UniNotas`.
- [x] Repositório técnico: permanece `MonitorDeNotas` nesta entrega.
- [x] Contextos fiscais: Unifast e Prosperar, sem tenancy.
- [x] Lista agregada: fora da primeira entrega.
- [x] Fonte das notas: Smart Notas somente.
- [x] Papel do PostgreSQL: falhas de integração somente.

## Assumptions Preview

| Assumption ID | Assumption | Evidence | If False | Confidence | Handling |
| --- | --- | --- | --- | --- | --- |
| `A-01` | O runtime atual continua funcionando durante o cutover documental | nenhuma mudança de produto neste TODO | cutover teria risco runtime | High | Keep as Assumption |
| `A-02` | O validator atual falha apenas pelo tree freeze nos novos artefatos | execução recente e código `EXPECTED_COMMON_FILES` | escopo do harness precisaria revisão | High | Keep as Assumption |
| `A-03` | O nome técnico não precisa mudar para lançar a arquitetura UniNotas | pedido nomeia produto, não repositório | novo TODO de rename seria necessário | Medium | Promote to Decision D-01 |

## Execution Plan

### Touched Surfaces

- `uninotas-foundation` roots, decisions, modules, policies, artifact index/manifest, TODOs e `deterministic/**`.

### Ordered Steps

1. Escrever testes de mutação fail-first para D-01..D-06 e o novo contrato de publicação.
2. Atualizar identidade, mandato, constituição, entidades, decisões e roadmap com separação Current/Target.
3. Criar os três owners alvo e atualizar módulos existentes, index e scope policy.
4. Evoluir validator/manifest sem enfraquecer privacidade, symlink, legado ou ownership.
5. Executar a suíte Foundation, validator, PACED readiness e guards de entrega.
6. Submeter diff consolidado às revisões independentes exigidas e promover decisões estáveis.

### Test Strategy

- **Strategy:** `test-first`
- **Why:** o validator é o harness arquitetural; cada semântica precisa de mutação negativa antes do cutover.
- **Fail-first target(s):** identidade UniNotas, source split, context-not-tenant, Current/Target, module set e publicação governada.

### Pre-APROVADO RED Evidence Capture

- **Decision:** `not_needed`
- **Why now:** não é bugfix runtime; a falha `frozen lifecycle tree mismatch` já está objetivamente reproduzida.
- **Target symptom:** `n/a`
- **Allowed surfaces:** `none`
- **Forbidden surfaces reaffirmed:** `production code|runtime/config/deploy|canonical project docs outside TODO authoring`
- **Planned command / target:** `n/a`
- **Status:** `not_run`
- **Findings summary:** `n/a`

### Flow Evidence Planning Matrix

| Criterion / Flow | Why Flow-Impacting | Platform Parity | Required Runtime Lane | Mutation Lane Required? | Backend Real-Data Required? | Planned Evidence | Non-Applicability Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Foundation cutover | structure-only; no runtime/UI | n/a | n/a | no | no | validator + reviews | nenhuma superfície de usuário muda |

### Local CI-Equivalent Suite Matrix

| Repository / CI Surface | Why In Scope | Behavior / Scenario Covered | Fixture / Seed / Runtime Preconditions | Local CI-Equivalent Command | Required Before | Status | Evidence Artifact / Command | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Foundation deterministic suite | validator e testes mudam | D-01..D-06 e mutações negativas | fixture temporária sem dados reais | `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_foundation.py` | Local-Implemented | planned | command output | suite canônica local |
| Foundation validator | publicação muda | árvore canônica completa | checkout consolidado | `python3 -B uninotas-foundation/deterministic/validate_foundation.py --root uninotas-foundation` | Local-Implemented | planned | command output | deve eliminar mismatch |
| PACED readiness | integração do alias/artefatos | contexto continua inicializável | Git Bash aceito | `bash delphi-ai/verify_context.sh` | Local-Implemented | planned | command output | runner conforme projeto |

### Runtime / Rollout Notes

- Sem runtime, migração, feature flag ou segredo. Rollout é somente documental e segue lanes Git.

## Plan Review Gate

### Review Sections

- [x] Architecture
- [x] Code Quality
- [x] Tests
- [x] Performance
- [x] Security
- [x] Elegance
- [x] Structural Soundness

### Issue Cards

- **Issue ID:** `ARCH-01`
  - **Severity:** `high`
  - **Evidence:** `deterministic/validate_foundation.py:EXPECTED_COMMON_FILES` e erro observado `frozen lifecycle tree mismatch`.
  - **Why it matters now:** a árvore congelada impede que a Foundation governe novos TODOs e artefatos legítimos.
  - **Option A (Recommended):** manter manifesto exato como allowlist versionada, mas derivar/validar famílias e contratos atuais sem lista duplicada rígida no código.
    - **Effort/Risk/Blast/Maintenance:** medium/medium/cross-module/low.
    - **Performance/Elegance/Structural:** neutral/improves/improves.
  - **Option B:** acrescentar manualmente cada novo caminho à constante e ao manifesto.
    - **Effort/Risk/Blast/Maintenance:** low/high/local/high.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Option C (Do Nothing):** conservar o bloqueio.
    - **Effort/Risk/Blast/Maintenance:** low/high/cross-module/high.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Recommendation:** Option A, preservando o manifesto fail-closed e eliminando duplicação frágil.

- **Issue ID:** `ARCH-02`
  - **Severity:** `high`
  - **Evidence:** `project_constitution.md#invariants` versus feature brief `Confirmed Direction`.
  - **Why it matters now:** substituir a verdade atual pela futura sem rotulagem faria a documentação mentir até o código migrar.
  - **Option A (Recommended):** seções explícitas `Current Runtime` e `Target Architecture` com status de módulo.
    - **Effort/Risk/Blast/Maintenance:** medium/low/cross-module/low.
    - **Performance/Elegance/Structural:** neutral/improves/improves.
  - **Option B:** publicar somente o alvo como atual.
    - **Effort/Risk/Blast/Maintenance:** low/high/cross-module/medium.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Option C (Do Nothing):** manter a autoridade antiga e bloquear backend.
    - **Effort/Risk/Blast/Maintenance:** low/high/cross-module/high.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Recommendation:** Option A, única que preserva verdade observada e direção aprovada.

### Failure Modes & Edge Cases

- [ ] Validator aceita arquivo não manifestado ou symlink.
- [ ] Termo UniNotas é atualizado, mas decisões/índices continuam Monitor de Notas sem rótulo histórico/current.
- [ ] `logs` permanece fallback implícito para notas.
- [ ] Fiscal context é confundido com tenancy.
- [ ] Novo módulo é marcado Current antes de existir no produto.
- [ ] Testes persistem exemplos que parecem credenciais ou dados pessoais.

### Residual Unknowns / Risks

- [ ] O writer/filter exato das falhas no PostgreSQL permanece investigação posterior e não será inventado aqui.
- [ ] Permissões por contexto, identidade opaca da nota e DANFE continuam decisões dos próximos TODOs.

## Additional Architectural Opinions

- **Needed:** `yes`
- **Why ambiguity remains:** o validator pode ser evoluído por manifesto único ou por inventário gerado; revisão independente deve desafiar a opção recomendada.
- **Opinion count:** `1`
- **Package mode:** `bounded-summary`
- **Internal reviewer mandate:** `required — fresh internal no-context reviewer after baseline freeze`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

| Reviewer | Recommendation | Performance view | Elegance view | Structural soundness view | Resolution | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| pending | pending | pending | pending | pending | pending | pending |

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- **Latest TEACH evidence / artifact:** `pending review baseline freeze`

| Trigger | Value | Notes |
| --- | --- | --- |
| `complexity` | `big` | identidade + módulos + validator |
| `blast_radius` | `cross-module` | múltiplos owners canônicos |
| `behavioral_change_or_bugfix` | `yes` | comportamento do validator |
| `changes_public_contract` | `yes` | contrato documental do produto |
| `touches_auth_or_tenant` | `yes` | negação explícita de tenancy/contexto |
| `touches_runtime_or_infra` | `no` | nenhuma mudança runtime |
| `touches_tests` | `yes` | suíte determinística |
| `critical_user_journey` | `no` | sem fluxo runtime |
| `release_or_promotion_critical` | `yes` | desbloqueia slices seguintes |
| `high_severity_plan_review_issue` | `yes` | ARCH-01/02 |
| `explicit_three_lane_request` | `no` | não solicitado pelo usuário |

## Independent No-Context Critique Gate

- **Critique decision:** `required`
- **Why this decision:** big/cross-module/public-contract/high-severity.
- **Impact signals in scope:** `cross-module blast radius|intentional module supersede|high-severity issue card`
- **Package mode:** `bounded-summary`
- **Package minimum contents:** `frozen baseline|scope|assumptions|plan|issue cards|residual risks`
- **Critique isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required after baseline freeze`
- **Canonical multi-lane audit protocol:** `pending audit floor`
- **Audit session / round evidence:** `n/a until run`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** A-01/A-02 dependem da árvore e validator reais.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `A-01,A-02`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Approval

- **Approved by:** `pending explicit APROVADO`
- **Approval scope:** `pending`
- **Execution not authorized by approval:** `backend, frontend, database, runtime, secrets, API calls, worktrees`
- **Renewed approval required when:** D-01..D-06, scope, module topology, validation semantics ou risco material mudar.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | contrato tático | APROVADO + guards | implementação prematura | bloqueia execução |
| `delphi-ai/rules/core/foundation-docs-sync-model-decision.md` | contratos/domínio mudam | scope/modules/roadmap alinhados | subscopes implícitos | sincronização 1:1 |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | ciclo completo | gates e evidência | atalhos de lifecycle | roteia execução |
| `delphi-ai/workflows/docker/todo-approval-gates-method.md` | revisão prévia | baseline publicado e reviews | aprovação sem preflight | exige freeze |
| `delphi-ai/workflows/docker/deterministic-todo-validation-method.md` | TODO tático | markdown canônico | editar bundle derivado | valida estrutura |
| `uninotas-foundation/policies/scope_subscope_governance.md` | novos owners | sem business tenancy | contexto como tenant | atualização explícita |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `primary-chat`
- **Selected model:** `gpt-6-astra`
- **Selected effort:** `xhigh`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `not-requested for implementation; required review agents are gate-specific`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `pending`
- **Waiver / exception reference:** `n/a`

## Decision Adherence Validation

| Decision ID | Status | Evidence | Notes |
| --- | --- | --- | --- |
| `D-01..D-06` | pending | pending implementation | preencher antes da entrega |

## Module Decision Consistency Validation

| Module Decision Ref | Planned Handling | Delivery Status | Evidence | Notes |
| --- | --- | --- | --- | --- |
| `baseline rows above` | mixed preserve/supersede | pending | pending | preencher 1:1 |

## Pipeline/Copilot P1/P2 Preflight

| Reviewer Surface / Package | Review Focus | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| bounded Foundation diff | P1/P2 contract/privacy/validator drift | planned | pending | pending | pre-delivery |

## Rule-Spirit Anti-Pattern Hunt

| Rule / Principle Surface | Bypass or Anti-Pattern Search Lens | Status | Evidence Artifact / Command | Findings | Resolution / Notes |
| --- | --- | --- | --- | --- | --- |
| TODO authority + Foundation sync | future-as-current, weakened validator, hidden tenancy/fallback | planned | pending | pending | pre-delivery |

## Security Risk Assessment

- **Risk level:** `medium`
- **Why this risk level:** o validator e os documentos processam conteúdo que pode conter segredo/PII, embora nenhuma chamada runtime seja feita.
- **Attack surface in scope:** `documentation privacy scanner; credential/PII persistence prevention`.
- **Attack simulation decision:** `recommended`
- **Review evidence:** `planned mutation tests + security review decision from audit floor`.
- **Residual security risk:** `pending review`.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `none`
- **Why this level:** sem endpoint, async UI, banco ou runtime.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | endpoint-performance-scrutiny | not_needed | low | EPS-DATA-PATH-CHANGED | before_local_implemented | EPS-E1 | not_applicable | none | none |
| `FRC` | frontend-race-condition-validation | not_needed | low | FRC-STALE-RESPONSE | before_local_implemented | FRC-POLICY | not_applicable | none | none |
| `BCI` | backend-concurrency-idempotency-validation | not_needed | low | BCI-EXACT-ONCE-SEMANTICS | before_local_implemented | BCI-INV | not_applicable | none | none |
| `RLS` | runtime-load-stress-validation | not_needed | low | RLS-SLO-CLAIM | before_production_ready | RLS-E1 | not_applicable | none | none |

## Verification Debt Assessment

- **Audit outcome:** `pending`
- **Why this outcome:** big architectural cutover requires audit before completion.
- **Inline code TODO debt:** `none expected`
- **Evidence / audit artifact:** `pending`
- **Accepted residual debt:** `none currently accepted`

## Independent Test Quality Audit Gate

- **Audit decision:** `required`
- **Why this decision:** validator/test logic and architectural semantics change.
- **Trigger signals in scope:** `changed test logic|architectural change|non-trivial validation risk`
- **Required evidence matrix:** `unit`
- **Package mode:** `bounded-file-set`
- **Canonical method:** `wf-docker-independent-test-quality-audit-method`
- **Audit isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `pending audit floor`
- **Audit status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** identidade e arquitetura cross-module.
- **Impact signals in scope:** `cross-module blast radius|intentional module supersede`
- **Package mode:** `bounded-summary`
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `pending audit floor`
- **Final review status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `required`
- **Why this decision:** cutover canônico e aposentadoria da autoridade antiga.
- **Cutover signals in scope:** `canonical cutover|legacy-path retirement`
- **Package mode:** `bounded-file-set`
- **Canonical multi-lane audit protocol:** `pending audit floor`
- **Audit session / round evidence:** `n/a until run`
- **Audit focus:** `true canonical path|current-target labels|hidden fallback|validator preservation`
- **Cutover audit status:** `not_run`
- **Findings summary:** `pending`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** planejamento e aprovação ainda não concluídos.
- **Post-commit/push status:** `pending`
- **Next path/status action:** congelar baseline e executar gates de aprovação.

## Module Consolidation Gate

- [ ] Canonical module docs updated with D-01..D-06.
- [ ] Decision promotion ledger links to this TODO.
- [ ] Prior decisions preserved or intentionally superseded.
- [ ] Conflicting tactical notes replaced by canonical references.
- [ ] TODO/module links updated after lifecycle movement.

## Commands (Run Locally)

- `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_foundation.py`
- `python3 -B uninotas-foundation/deterministic/validate_foundation.py --root uninotas-foundation`
- `bash delphi-ai/verify_context.sh`
- Guards Delphi declarados neste TODO.

## Files Expected (Compatibility Note)

- O `Diff Expectation Contract` é a autoridade exclusiva sobre paths esperados.
