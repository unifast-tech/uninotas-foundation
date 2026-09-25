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
- **Next exact step:** congelar em `main` a remediação R3 de capability/core scope/estado, repetir arquitetura e crítica, e então executar os guards pré-aprovação.

## Active Work State (Required While TODO Remains In `active/`)

- **Work state:** `review`
- **Why this state now:** o contrato está em refinamento/revisão pré-aprovação; nenhuma implementação canônica ou determinística foi iniciada.
- **Exit condition:** baseline aprovado, implementação validada e gates de entrega concluídos.

## Scope

- [ ] Canonicalizar `UniNotas` como nome do produto e `uninotas` como `core_scope`, preservando `MonitorDeNotas` como nome técnico do repositório nesta entrega.
- [ ] Registrar a topologia externa confirmada e a propriedade de dados: Smart Notas para notas/documentos, PostgreSQL `logs` somente para falhas de integração.
- [ ] Registrar Unifast e Prosperar como `FiscalIssuerContext`, sem tenancy e sem agregação inicial de notas.
- [ ] Separar explicitamente comportamento atual e arquitetura-alvo nas raízes, decisões, roadmap e módulos afetados.
- [ ] Criar os owners canônicos planejados exatos `modules/fiscal-notes-and-documents.md`, `modules/integration-error-occurrences.md` e `modules/operational-cases.md`.
- [ ] Atualizar a política de scope/subscope e os índices sem inventar módulos de runtime já implementados.
- [ ] Evoluir o validador e seus testes para a nova identidade, módulos e publicação governada, mantendo proteções existentes.
- [ ] Publicar no manifesto os artefatos de descoberta e este TODO sem persistir segredos, valores reais de CNPJ/identificador do provedor, payloads/respostas privadas ou URLs capturadas de documentos.

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
- `Lane-Promoted`: n/a para esta autoridade documental single-branch.
- `Production-Ready`: a entrega foi validada e publicada em `main` após todos os gates.

## Execution Lane Tracking (Required)

- **Local implementation branches:** `uninotas-foundation:main` (autoridade single-branch/single-checkout)
- **Promotion lane path:** `main -> origin/main`
- **Lane-promoted threshold for this TODO:** `origin/main`
- **Production-ready threshold for this TODO:** `origin/main` após gates de conclusão

## Promotion Evidence (Required Before Lane-Promoted / Production-Ready)

| Scope Item | Local Branch/Commit | PR to lane threshold | PR to `stage` | PR to `main` | Current Status |
| --- | --- | --- | --- | --- | --- |
| Foundation UniNotas cutover | `main@72b25ee` | `n/a — main-only authority` | `n/a` | `origin/main@72b25ee` | R3 review baseline published |

## Diff Expectation Contract

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
| `uninotas-foundation` | `technology_baseline.md` | `M` | identidade no baseline observado sem alterar fatos técnicos |
| `uninotas-foundation` | `evolution_lifecycle.md` | `M` | relacionar lifecycle PACED ao estado separado de autoridade runtime |
| `uninotas-foundation` | `contracts/README.md` | `M` | índice deixa de presumir exatamente seis owners |
| `uninotas-foundation` | `decisions/monitor-de-notas-foundation-decisions.md` | `M` | decisões promovidas e arquivo renomeado somente se o diff contract for renovado |
| `uninotas-foundation` | `modules/README.md` | `M` | índice/lifecycle dos owners |
| `uninotas-foundation` | `modules/events-and-classification.md` | `M` | owner current e sucessores target |
| `uninotas-foundation` | `modules/treatments-and-history.md` | `M` | owner current e sucessor target |
| `uninotas-foundation` | `modules/identity-and-team.md` | `M` | no-tenancy e contexto fiscal |
| `uninotas-foundation` | `modules/realtime-invalidation.md` | `M` | current logs invalidation versus target source split |
| `uninotas-foundation` | `modules/operational-monitoring.md` | `M` | current logs summary versus target monitoring split |
| `uninotas-foundation` | `modules/runtime-and-deployment.md` | `M` | current runtime e target external boundary |
| `uninotas-foundation` | `modules/fiscal-notes-and-documents.md` | `A` | target provider-backed fiscal owner |
| `uninotas-foundation` | `modules/integration-error-occurrences.md` | `A` | target external failure-evidence owner |
| `uninotas-foundation` | `modules/operational-cases.md` | `A` | target application workflow owner |
| `uninotas-foundation` | `policies/scope_subscope_governance.md` | `M` | novos subscopes explícitos |
| `uninotas-foundation` | `policies/query_path_guardrails.md` | `M` | separar current logs queries do target note source |
| `uninotas-foundation` | `policies/validation_evidence_policy.md` | `M` | promover boundary de CNPJ/identifier/document URL |
| `uninotas-foundation` | `artifacts/README.md` | `M` | indexação dos artefatos |
| `uninotas-foundation` | `artifacts/feature-briefs/uninotas-smart-notas-central.md` | `A, M` | framing já produzido e reconciliação ST-02 |
| `uninotas-foundation` | `artifacts/publication-manifest.txt` | `M` | contrato de publicação |
| `uninotas-foundation` | `todos/active/process/TODO-uninotas-smart-notas-api-and-fiscal-context-discovery.md` | `A, M` | ledger de descoberta e sequência corrigida |
| `uninotas-foundation` | `todos/active/process/TODO-uninotas-canonical-foundation-transition.md` | `A, M` | autoridade tática e evidência |
| `uninotas-foundation` | `deterministic/validate_foundation.py` | `M` | validador evolutivo fail-closed |
| `uninotas-foundation` | `deterministic/tests/**` | `A, M` | mutações e regressões do validator |

### Not Expected Changed Paths

| Repository | Path glob | Change types (`A|M|D|R|any`) | Reason |
| --- | --- | --- | --- |
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

- [ ] `DOD-01` Identidade/mandato usam UniNotas e todos os anchors usam `core_scope=uninotas`, sem renomear o repositório técnico.
- [ ] `DOD-02` Constituição e decisões registram a topologia externa e a separação de fontes aprovada.
- [ ] `DOD-03` Unifast/Prosperar são contextos fiscais explícitos e não tenants.
- [ ] `DOD-04` Registry e módulos distinguem `current_runtime` de `target_planned`, com precedência, predecessor/sucessor e condição de promoção/retirada, sem declarar código futuro como implementado.
- [ ] `DOD-05` Notas/documentos, falhas de integração e casos operacionais têm owners canônicos distintos.
- [ ] `DOD-06` Validator e suíte rejeitam regressões de identidade, ownership, tenancy, privacidade, symlink, legado e publicação, além de módulo ausente/duplicado, successor inválido/cíclico, target com `owned_capabilities`, capability ativa sem owner e dupla autoridade runtime para o mesmo ID estável.
- [ ] `DOD-07` Os artefatos atuais pertencem ao manifesto e a validação Foundation passa sem `frozen lifecycle tree mismatch`.
- [ ] `DOD-08` Nenhum segredo, valor real de CNPJ/identificador do provedor, payload/resposta privada ou URL capturada de documento foi persistido; CNPJ válido é coberto deterministicamente e identificador/URL contextual por regra precisa mais revisão de diff.
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
| Git remote Foundation | necessário para baseline de revisão | healthy | 2026-09-25 | `main`/`origin/main@72b25ee`; guard main-only instalado e Git for Windows é o writer válido | nenhum ajuste |

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
- **Module decision consolidation targets:** `modules/fiscal-notes-and-documents.md`, `modules/integration-error-occurrences.md`, `modules/operational-cases.md` e os seis módulos atuais afetados.

## Decision Pending (Resolve Before Freeze)

- [ ] `none — decisões materiais abaixo serão confirmadas pelo APROVADO deste contrato`.

## Planned Module Registry Contract

O JSON machine-readable de `policies/scope_subscope_governance.md` terá `core_scope=uninotas` e uma coleção `modules`; cada entrada declara `subscope`, `path`, `runtime_authority_state`, `owned_capabilities`, `planned_capabilities`, `predecessors` e `successors`. `runtime_authority_state=current_runtime|target_planned` é um eixo distinto do lifecycle PACED de `evolution_lifecycle.md`; ele responde somente qual módulo possui autoridade sobre comportamento executável observado. Um `target_planned` sempre tem `owned_capabilities=[]`; sua intenção aparece somente em `planned_capabilities`.

Os IDs de capability são estáveis entre predecessor e successor: `note_read_model`, `integration_error_read_model` e `operational_workflow` não mudam durante a transferência. `fiscal_document_read` é capability nova, sem predecessor. Promoção é atômica por capability: o TODO implementador remove o ID de `owned_capabilities` do predecessor e o adiciona ao successor no mesmo diff; capabilities novas passam de `planned_capabilities` para `owned_capabilities` somente quando entregues. Nenhuma capability pode ter dois owners `current_runtime`, e toda capability ativa tem exatamente um. Um predecessor com capabilities restantes continua `current_runtime` apenas para elas; sem nenhuma, sai do registry/index ativo e permanece no histórico Git.

| Subscope / path | Runtime authority state | Owned / planned capability IDs | Predecessor/successor handling |
| --- | --- | --- | --- |
| `events-and-classification` / `modules/events-and-classification.md` | `current_runtime` | owned: `note_read_model`, `integration_error_read_model`; planned: none | successors fiscais/erros; IDs saem separadamente |
| `treatments-and-history` / `modules/treatments-and-history.md` | `current_runtime` | owned: `operational_workflow`; planned: none | successor `operational-cases` após migração aprovada |
| `identity-and-team` / `modules/identity-and-team.md` | `current_runtime` | `authentication`, `team_profiles` | preservar; futuras permissões por contexto exigem TODO |
| `realtime-invalidation` / `modules/realtime-invalidation.md` | `current_runtime` | `legacy_log_invalidation` | preservar; adaptar fontes em TODO futuro |
| `operational-monitoring` / `modules/operational-monitoring.md` | `current_runtime` | `legacy_log_monitoring` | preservar; separar métricas em TODO futuro |
| `runtime-and-deployment` / `modules/runtime-and-deployment.md` | `current_runtime` | `runtime_topology`, `health_read` | preservar fatos observados; registrar alvo sem inventar writer |
| `fiscal-notes-and-documents` / `modules/fiscal-notes-and-documents.md` | `target_planned` | owned: none; planned: `note_read_model`, `fiscal_document_read` | predecessor `events-and-classification` para `note_read_model`; document read é novo |
| `integration-error-occurrences` / `modules/integration-error-occurrences.md` | `target_planned` | owned: none; planned: `integration_error_read_model` | predecessor `events-and-classification`; writer/filter desconhecido |
| `operational-cases` / `modules/operational-cases.md` | `target_planned` | owned: none; planned: `operational_workflow` | predecessor `treatments-and-history` |

## Decisions (Resolved Before Freeze)

- [x] `D-01` O nome canônico do produto e o `core_scope` serão `UniNotas`/`uninotas`; o repositório técnico permanece `MonitorDeNotas` nesta entrega.
- [x] `D-02` Smart Notas é a fonte completa das notas e documentos; PostgreSQL `logs` é somente evidência de falhas de integração.
- [x] `D-03` Unifast e Prosperar são `FiscalIssuerContext` independentes, nunca tenants, organizações ou agregação implícita.
- [x] `D-04` O registry usará `runtime_authority_state=current_runtime|target_planned`, distinto do lifecycle PACED. IDs estáveis transferem atomicamente entre `owned_capabilities`; planned nunca concede autoridade; cada capability ativa tem exatamente um owner current.
- [x] `D-05` Os owners alvo exatos são: `fiscal-notes-and-documents` para fatos/documentos do provedor; `integration-error-occurrences` para evidência externa, normalização e correlação determinística; `operational-cases` para workflow, membership, tratamento e autoria da aplicação.
- [x] `D-06` `artifacts/publication-manifest.txt` será o único inventário exato da árvore; o validator manterá singletons/famílias/status permitidos, derivará o registry de módulos do scope policy + metadata dos módulos e isolará o ledger histórico do inventário geral de TODOs, sem duplicar a árvore completa em Python.
- [x] `D-07` O writer/filter externo de falhas permanece desconhecido nesta entrega; a Foundation pode afirmar somente o alvo PostgreSQL read-only/error-evidence e não pode nomear n8n ou outro writer sem evidência posterior.

## Frozen Decision Coherence Matrix (1:1)

| Decision | Prior decision / module reference | Handling | Evidence / intended consolidation |
| --- | --- | --- | --- |
| `D-01` | foundation decision `D-01`; scope policy `monitor-de-notas` | Supersede (Intentional) | identity roots + `core_scope=uninotas` + todos os module anchors |
| `D-02` | foundation decisions `D-04`; events ownership | Supersede (Intentional) | constitution + current/target source matrix |
| `D-03` | foundation decision `D-05`; identity no-tenancy | Preserve | scope policy + identity module |
| `D-04` | `evolution_lifecycle.md` capability lifecycle | Preserve | declare separate runtime-authority axis and relationship |
| `D-05` | events/treatments current ownership | Supersede (Intentional) | three exact target module paths/boundaries |
| `D-06` | foundation decision `D-02`; frozen validator tree | Supersede (Intentional) | preserve Git-history recovery while making manifest sole active inventory |
| `D-07` | No Prior Decision | Preserve | explicit unknown in feature brief, discovery ledger, runtime/target docs |

## Module Decision Baseline Snapshot (Required Before APROVADO)

| Module Decision Ref | Current Module Decision | Planned Handling | Evidence |
| --- | --- | --- | --- |
| `decisions#D-01` | produto Monitor de Notas | Supersede (Intentional) | `decisions/monitor-de-notas-foundation-decisions.md` |
| `decisions#D-04` | `logs` sustenta toda observação do monitor | Supersede (Intentional) | `project_constitution.md#invariants` |
| `decisions#D-05` | sem business tenancy | Preserve | `policies/scope_subscope_governance.md` |
| `events#ownership` | eventos de `logs` são o read model completo | Supersede (Intentional) | `modules/events-and-classification.md#ownership-invariant` |
| `treatments#ownership` | tratamento é ligado somente a `ref_id` | Supersede (Intentional) | `modules/treatments-and-history.md#specification` |
| `runtime#logs` | produção `logs` é externa e read-only | Preserve | `modules/runtime-and-deployment.md#observed-runtime-contract` |
| `identity#no-tenancy` | não há business tenancy | Preserve | `modules/identity-and-team.md#module-intent--boundaries` |
| `realtime#logs-invalidation` | polling/LISTEN atuais invalidam a experiência baseada em logs | Preserve | `modules/realtime-invalidation.md#specification` |
| `monitoring#logs-summary` | monitor atual resume classificações de logs | Preserve | `modules/operational-monitoring.md#specification` |

## Decision Baseline (Frozen Before Implementation)

- [x] `D-01` UniNotas/`uninotas` são identidade e core scope canônicos; o nome técnico do repositório não muda.
- [x] `D-02` Toda nota/documento vem da Smart Notas; `logs` nunca é fallback ou espelho de notas bem-sucedidas.
- [x] `D-03` O contexto fiscal faz parte de identidade, resolução de credencial e isolamento, sem criar tenancy.
- [x] `D-04` O eixo de autoridade runtime, IDs estáveis e condições de promoção/retirada impedem overlap ou gap de ownership sem competir com o lifecycle PACED.
- [x] `D-05` Os três paths/owners alvo e seus limites exclusivos são os definidos acima; `OperationalCase` não altera fatos das fontes.
- [x] `D-06` Manifesto é a única enumeração exata; código valida famílias/singletons/semântica/privacidade e não mantém uma segunda cópia da árvore.
- [x] `D-07` O writer/filter de falhas não é pré-condição do cutover Current/Target enquanto permanecer explicitamente desconhecido e bloquear apenas o futuro error-adapter.

## Architecture Change Governance

- **Applicability:** `required`
- **Why this applies:** a entrega supersede identidade, source ownership e arquitetura modular, além de corrigir um validator de cutover que bloqueia evolução normal.
- **Deviation / debt being retired:** Foundation afirma `logs` como fonte completa e valida apenas a árvore exata do rebase inicial.
- **Target steady-state after closeout:** UniNotas com registry `current_runtime|target_planned`, precedência e sucessão explícitas, owners alvo exclusivos e validação evolutiva fail-closed.
- **Temporary exceptions allowed:** documentos de comportamento atual podem conservar Monitor de Notas/rotas atuais apenas quando marcados como `Current` e sem autoridade sobre o alvo.
- **Cutover / removal condition:** todas as referências canônicas não-históricas aderem a D-01..D-07 e a suíte de mutação passa.

### Patterns To Enforce

| Pattern / Decision | Source / ID | Scope | Why It Must Hold After Cutover |
| --- | --- | --- | --- |
| current-versus-target runtime-authority axis | D-04 | Foundation | evita declarar capacidade não implementada ou dois owners runtime ativos sem redefinir lifecycle PACED |
| source ownership split | D-02 | modules/domain | impede fallback silencioso em logs de sucesso |
| context is not tenancy | D-03 | scope/domain | impede vazamento conceitual e técnico |
| manifest + semantic guards | D-06 | deterministic | permite evolução sem perder fail-closed |

### Prohibited Anti-Patterns

| Anti-Pattern / Wrong Path | Detection Signal | Why It Is Forbidden After Cutover | Exception Policy |
| --- | --- | --- | --- |
| `logs` como base de notas | ownership scanner/test | contradiz D-02 | nenhuma |
| Unifast/Prosperar como tenants | scope policy/test | contradiz D-03 | nenhuma |
| documento alvo rotulado Current sem código | status contract/test | cria falsa verdade | nenhuma |
| árvore exata duplicada no manifesto e no Python | mutation test | repete o bloqueio atual e cria duas autoridades | nenhuma |

### Architecture Protection Harness

| Harness Type | Surface | Command / Rule / Artifact | Regression It Must Catch | Adoption Timing | Evidence Plan / Follow-up |
| --- | --- | --- | --- | --- | --- |
| test | Foundation semantics | `test_validate_foundation.py` | identity/source/tenancy/current-target drift | implement-in-this-todo | mutation GREEN |
| guard | publication tree | `validate_foundation.py` + manifest | arquivo não governado, symlink, privacidade | implement-in-this-todo | validator GREEN |
| test | privacy boundary | valid formatted/compact CNPJ + contextual provider-ID/document-URL mutations | captured business/provider values without banning official docs or generic IDs | implement-in-this-todo | mutation GREEN + bounded diff review |
| review | architecture | independent architecture/adherence review | supersede incompleto | implement-in-this-todo | review artifacts |

## Architecture Review Gates

- **Architecture decision review:** `required`
- **Decision review lifecycle:** `after diagnosis is closed and before APROVADO`
- **Decision review kind:** `architecture_opinion`
- **Decision review package:** `bounded-summary`
- **Decision review status:** `findings_integrated`
- **Decision review evidence / resolution:** `R3 retornou no-go por capability IDs/core scope/terminologia; achados integrados e nova revisão aguardará baseline R3`
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
- **Baseline branch:** `main`
- **Baseline commit:** `72b25ee91a2f86c21bb04ded66e59c432dd76d4b`
- **Baseline push reference:** `origin/main`
- **Gate status:** `no_material_findings`
- **Findings summary:** capability IDs estáveis, `core_scope=uninotas` e estado temporal foram congelados na autoridade `main`.
- **Evidence / reference:** `origin/main@72b25ee`; diff guard e validator do TODO retornaram `go`/`PASS` antes do freeze.
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
| `none` | Não há hipótese viva: ausência de mudança runtime é boundary verificável; o mismatch é fato observado; identidade técnica é D-01 | Scope, diff contract, `validate_foundation.py` e D-01 | n/a | High | Keep as Assumption |

## Execution Plan

### Touched Surfaces

- `uninotas-foundation` roots, decisions, modules, policies, artifact index/manifest, TODOs e `deterministic/**`.

### Ordered Steps

1. Escrever testes de mutação fail-first para D-01..D-07, eixo de autoridade runtime/IDs estáveis e o novo contrato de publicação.
2. Atualizar identidade, mandato, constituição, entidades, decisões e roadmap com separação Current/Target.
3. Criar os três owners alvo e atualizar módulos existentes, index e scope policy.
4. Tornar o manifesto a única enumeração exata; extrair validadores puros para registry/privacidade/ownership e manter poucos testes full-tree, sem enfraquecer symlink, legado ou ownership.
5. Executar a suíte Foundation, validator, PACED readiness e guards de entrega.
6. Submeter diff consolidado às revisões independentes exigidas e promover decisões estáveis.

### Test Strategy

- **Strategy:** `test-first`
- **Why:** o validator é o harness arquitetural; cada semântica precisa de mutação negativa antes do cutover.
- **Fail-first target(s):** identidade/core scope UniNotas, source split, context-not-tenant, runtime-authority/lifecycle separation, módulo ausente/duplicado, successor inválido/cíclico, target com owned capability, capability ativa sem owner, dupla autoridade pelo mesmo ID, manifesto único, CNPJ válido e URL/identificador privado contextual.

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
| Foundation deterministic suite | validator e testes mudam | D-01..D-07 e mutações negativas | fixtures mínimas + poucos testes full-tree; sem dados reais | `python3 -B -m unittest uninotas-foundation/deterministic/tests/test_validate_foundation.py` | Local-Implemented | planned | command output + duração | evitar crescimento multiplicativo sobre baseline observado ~179s |
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
  - **Option A (Recommended):** manifesto como única enumeração exata; Python mantém singletons/famílias/status e deriva registry de módulos do scope policy + metadata, sem copiar a árvore completa.
    - **Effort/Risk/Blast/Maintenance:** medium/medium/cross-module/low.
    - **Performance/Elegance/Structural:** neutral/improves/improves.
  - **Option B:** acrescentar manualmente cada novo caminho à constante e ao manifesto.
    - **Effort/Risk/Blast/Maintenance:** low/high/local/high.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Option C (Do Nothing):** conservar o bloqueio.
    - **Effort/Risk/Blast/Maintenance:** low/high/cross-module/high.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Recommendation:** Option A congelada em D-06; adição legítima exige mudança explícita do manifesto e aprovação nas famílias/semântica permitidas.

- **Issue ID:** `ARCH-02`
  - **Severity:** `high`
  - **Evidence:** `project_constitution.md#invariants` versus feature brief `Confirmed Direction`.
  - **Why it matters now:** substituir a verdade atual pela futura sem rotulagem faria a documentação mentir até o código migrar.
  - **Option A (Recommended):** registry `current_runtime|target_planned`, matriz de precedência/sucessão e condição de promoção/retirada, refletidos nas seções de módulo.
    - **Effort/Risk/Blast/Maintenance:** medium/low/cross-module/low.
    - **Performance/Elegance/Structural:** neutral/improves/improves.
  - **Option B:** publicar somente o alvo como atual.
    - **Effort/Risk/Blast/Maintenance:** low/high/cross-module/medium.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Option C (Do Nothing):** manter a autoridade antiga e bloquear backend.
    - **Effort/Risk/Blast/Maintenance:** low/high/cross-module/high.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Recommendation:** Option A, única que preserva verdade observada e direção aprovada.

- **Issue ID:** `SEC-01`
  - **Severity:** `medium`
  - **Evidence:** `DOD-08` versus os patterns atuais em `deterministic/validate_foundation.py`.
  - **Why it matters now:** CNPJ e URL privada capturada ainda não têm cobertura objetiva, enquanto “ID” genérico causaria falso positivo.
  - **Option A (Recommended):** detectar CNPJ formatado/compacto válido; rejeitar identifier/URL somente em contexto de valor capturado/provedor e complementar com diff review.
    - **Effort/Risk/Blast/Maintenance:** medium/low/local/low.
    - **Performance/Elegance/Structural:** neutral/improves/improves.
  - **Option B:** banir qualquer número longo ou URL.
    - **Effort/Risk/Blast/Maintenance:** low/high/cross-module/high.
    - **Performance/Elegance/Structural:** regresses/regresses/regresses.
  - **Option C (Do Nothing):** depender apenas de revisão humana.
    - **Effort/Risk/Blast/Maintenance:** low/medium/local/medium.
    - **Performance/Elegance/Structural:** neutral/neutral/regresses.
  - **Recommendation:** Option A, refletida em DOD-08 e no harness.

- **Issue ID:** `TEST-01`
  - **Severity:** `medium`
  - **Evidence:** suíte atual observada em aproximadamente 179 segundos e cópias/full scans por mutação em `deterministic/tests/test_validate_foundation.py`.
  - **Why it matters now:** novas matrizes de mutação podem tornar o feedback local impraticável.
  - **Option A (Recommended):** extrair validadores puros, usar fixtures mínimas e manter poucos testes end-to-end full-tree com duração registrada.
    - **Effort/Risk/Blast/Maintenance:** medium/low/local/low.
    - **Performance/Elegance/Structural:** improves/improves/improves.
  - **Option B:** apenas adicionar mutações ao harness atual.
    - **Effort/Risk/Blast/Maintenance:** low/medium/local/high.
    - **Performance/Elegance/Structural:** regresses/regresses/neutral.
  - **Option C (Do Nothing):** não adicionar cobertura.
    - **Effort/Risk/Blast/Maintenance:** low/high/local/medium.
    - **Performance/Elegance/Structural:** neutral/regresses/regresses.
  - **Recommendation:** Option A como obrigação de entrega, sem SLO rígido inventado.

### Failure Modes & Edge Cases

- [ ] Validator aceita arquivo não manifestado ou symlink.
- [ ] Termo UniNotas é atualizado, mas decisões/índices continuam Monitor de Notas sem rótulo histórico/current.
- [ ] `logs` permanece fallback implícito para notas.
- [ ] Fiscal context é confundido com tenancy.
- [ ] Novo módulo é marcado Current antes de existir no produto.
- [ ] Testes persistem exemplos que parecem credenciais ou dados pessoais.
- [ ] A suíte de mutação repete cópias/full scans e cresce muito além do baseline de aproximadamente 179 segundos.

### Residual Unknowns / Risks

- [ ] O writer/filter exato das falhas no PostgreSQL permanece investigação posterior, explicitamente não bloqueia este cutover e não será inventado aqui.
- [ ] Permissões por contexto, identidade opaca da nota e DANFE continuam decisões dos próximos TODOs.

### Diagnostic Review Finding Resolution

Os pareceres executados sobre a branch indevida são diagnóstico útil, mas não satisfazem os gates formais. Ambos serão repetidos por revisores frescos sobre um baseline válido em `main`.

| Finding ID | Source | Resolution | Evidence / rationale |
| --- | --- | --- | --- |
| `CRIT-01` | plan critique | Integrated | autoridade restaurada em `main`; branch remota/local removida; guard main-only instalado |
| `CRIT-02` | plan critique | Integrated | SHA incorreta descartada; novo baseline main pendente |
| `ARCH-01` | both | Integrated | D-04 congela eixo de autoridade runtime, precedência, sucessão e promoção/retirada |
| `ARCH-02` | both | Integrated | D-06 congela manifesto como inventário exato único e registry derivado |
| `DISC-01` | both | Integrated | AMB-11/G-23/ST-02 revisados; writer permanece desconhecido e bloqueia apenas error-adapter |
| `COHERENCE-01` | plan critique | Integrated | Frozen Decision Coherence Matrix cobre D-01..D-07; module baseline cobre os seis owners atuais |
| `SEC-01` | both | Integrated | DOD/harness distinguem CNPJ determinístico de ID/URL contextual |
| `DIFF-01` | plan critique | Integrated | globs de decisions/modules/feature-brief/TODOs foram substituídos por paths exatos |
| `ASSUME-01` | plan critique | Integrated | hipóteses redundantes removidas; decisões/fatos/constraints assumem seus owners corretos |
| `TEST-01` | both | Integrated | fixtures mínimas, validadores puros e duração viram obrigação de entrega |
| `ARCH-R2-01` | formal architecture review | Integrated | transferências atômicas por capability permitem promoção fiscal antes do error-adapter |
| `ARCH-R2-02` | formal architecture review | Integrated | matriz congelada agora é 1:1 por D-01..D-07 |
| `DIFF-R2-01` | both formal reviews | Integrated | heading canônico, único repo declarado e roots/policies/contracts omitidos classificados |
| `LIFECYCLE-R2-01` | formal critique | Integrated | `runtime_authority_state` é eixo separado e explicitamente relacionado ao lifecycle PACED |
| `DISC-R2-01` | formal critique | Integrated | n8n possui apenas orchestration; writer PostgreSQL permanece desconhecido |
| `STATE-R2-01` | formal critique | Integrated | work state e próximos passos sincronizados para review/fresh baseline |
| `TEMPLATE-R2-01` | formal critique | Integrated | module template adicionado à ingestão obrigatória |
| `ARCH-R3-01` | both formal reviews | Integrated | capability IDs estáveis + planned/owned tornam transferências e overlaps verificáveis |
| `ARCH-R3-02` | formal architecture review | Integrated | toda terminologia congelada reserva lifecycle ao PACED e usa eixo/estado para runtime authority |
| `SCOPE-R3-01` | formal architecture review | Integrated | D-01 fixa `core_scope=uninotas` e atualiza todos os anchors/validator |
| `STATE-R3-01` | formal critique | Integrated | status, next step, gate evidence e baseline preparados para freeze R3 |

## Additional Architectural Opinions

- **Needed:** `yes`
- **Why ambiguity remains:** o validator pode ser evoluído por manifesto único ou por inventário gerado; revisão independente deve desafiar a opção recomendada.
- **Opinion count:** `2`
- **Package mode:** `bounded-summary`
- **Internal reviewer mandate:** `required — fresh internal no-context reviewer after baseline freeze`
- **Required lenses:** `correctness|performance|elegance|structural-soundness|operational-fit`

| Reviewer | Recommendation | Performance view | Elegance view | Structural soundness view | Resolution | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `uninotas_architecture_opinion_main` | manifesto único + transferências por capability + matrix 1:1 | runtime neutral; harness precisa ser otimizado | melhora ao remover autoridades duplicadas | exigiu promoção parcial explícita | Integrated | formal R2 |
| `uninotas_architecture_opinion_r3` | IDs estáveis e core scope explícito | runtime neutral | remove aliases ambíguos | exige ownership verificável pelo mesmo ID | Integrated | formal R3; nova revisão clean pendente |

## Audit Trigger Matrix

- **Canonical method:** `wf-docker-audit-escalation-method`
- **Guard command:** `python3 delphi-ai/tools/audit_escalation_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- **Latest TEACH evidence / artifact:** `audit_escalation_guard.py: Overall outcome go; fingerprint bdde6668065b; critique, architecture decision/adherence, security, test-quality, final review, verification debt and delivery triple-review required; performance/concurrency recommended`.

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
- **Canonical multi-lane audit protocol:** `n/a for planning critique; audit-protocol-triple-review required additively before Completed`
- **Audit session / round evidence:** `n/a until run`
- **Critique lenses:** `correctness|performance|elegance|structural-soundness|risk`
- **Critique status:** `findings_integrated`
- **Findings summary:** `R3 confirmou diff/main/lifecycle separation e apontou capability map + estado temporal; ambos integrados`.
- **Evidence / reference:** `uninotas_plan_critique_r3; nova crítica será executada sobre baseline R3`.
- **Waiver authority / reference:** `n/a`

## Gate: Assumption Code Coherence

- **Gate decision:** `required`
- **Why this decision:** embora não haja hipótese viva, o guard confirma que fatos e decisões citam código/docs reais antes da aprovação.
- **Trigger stage:** `after critique convergence and before APROVADO`
- **Guard scope:** `none — fatos/decisões substituíram as hipóteses vivas; o guard ainda confirma coerência dos anchors`
- **Guard command:** `python3 delphi-ai/tools/assumption_code_coherence_guard.py --todo uninotas-foundation/todos/active/process/TODO-uninotas-canonical-foundation-transition.md`
- **Gate status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`
- **Waiver authority / reference:** `n/a`

## Approval

- **Approved by:** `pending explicit APROVADO`
- **Approval scope:** `pending`
- **Execution not authorized by approval:** `backend, frontend, database, runtime, secrets, API calls, worktrees`
- **Renewed approval required when:** D-01..D-07, scope, module topology, validation semantics ou risco material mudar.

## Rules Acknowledgement / Ingestion

| Source | Why It Applies Now | Must Preserve | Must Avoid | Execution Impact |
| --- | --- | --- | --- | --- |
| `delphi-ai/rules/core/todo-driven-execution-model-decision.md` | contrato tático | APROVADO + guards | implementação prematura | bloqueia execução |
| `delphi-ai/rules/core/foundation-docs-sync-model-decision.md` | contratos/domínio mudam | scope/modules/roadmap alinhados | subscopes implícitos | sincronização 1:1 |
| `delphi-ai/workflows/docker/todo-driven-execution-method.md` | ciclo completo | gates e evidência | atalhos de lifecycle | roteia execução |
| `delphi-ai/workflows/docker/todo-approval-gates-method.md` | revisão prévia | baseline publicado e reviews | aprovação sem preflight | exige freeze |
| `delphi-ai/workflows/docker/deterministic-todo-validation-method.md` | TODO tático | markdown canônico | editar bundle derivado | valida estrutura |
| `delphi-ai/templates/module_template.md` | três módulos serão criados | anchors canônicos e coverage status | inventar formato paralelo ou sobrecarregar lifecycle PACED | blueprint obrigatório dos novos módulos |
| `uninotas-foundation/policies/scope_subscope_governance.md` | novos owners | sem business tenancy | contexto como tenant | atualização explícita |

## Agent Routing Preflight

- **Client surface:** `codex`
- **Current governed action:** `implementation`
- **Selected role:** `routine-executor`
- **Selected model:** `gpt-5.6-terra`
- **Selected effort:** `medium`
- **Proof mode:** `declared`
- **Exception reason:** `n/a`
- **Subagent / delegation authorization:** `governed routine-executor lane required by the applicable routing workflow; no parallel code writers`
- **Execution topology:** `primary-checkout-single-writer`
- **Worktree / auxiliary-checkout authorization:** `not-authorized`
- **Worktree authorization evidence:** `n/a`
- **Writer scheduling policy:** `single-writer-serialized`
- **Guard outcome:** `go`
- **Waiver / exception reference:** `n/a`

## Decision Adherence Validation

| Decision ID | Status | Evidence | Notes |
| --- | --- | --- | --- |
| `D-01` | pending | pending implementation | identidade UniNotas + `core_scope=uninotas` |
| `D-02` | pending | pending implementation | source ownership split |
| `D-03` | pending | pending implementation | fiscal context sem tenancy |
| `D-04` | pending | pending implementation | runtime-authority state e transferências por capability |
| `D-05` | pending | pending implementation | três owners target exclusivos |
| `D-06` | pending | pending implementation | manifesto único + semantic registry |
| `D-07` | pending | pending implementation | writer/filter explicitamente desconhecido |

## Module Decision Consistency Validation

| Module Decision Ref | Planned Handling | Delivery Status | Evidence | Notes |
| --- | --- | --- | --- | --- |
| `decisions#D-01` | Supersede (Intentional) | pending | pending | identity/core scope |
| `decisions#D-04` | Supersede (Intentional) | pending | pending | source ownership target split |
| `decisions#D-05` | Preserve | pending | pending | no business tenancy |
| `events#ownership` | Supersede (Intentional) | pending | pending | current capabilities e successors |
| `treatments#ownership` | Supersede (Intentional) | pending | pending | successor operational-cases |
| `runtime#logs` | Preserve | pending | pending | facts observed; writer unknown |
| `identity#no-tenancy` | Preserve | pending | pending | context is not tenancy |
| `realtime#logs-invalidation` | Preserve | pending | pending | current invalidation |
| `monitoring#logs-summary` | Preserve | pending | pending | current monitoring |

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
- **Attack simulation decision:** `required`
- **Review evidence:** `audit floor SEC-AUTH-OR-TENANT; security-adversarial-review required before Completed`.
- **Residual security risk:** `pending review`.

## Performance & Concurrency Risk Assessment

- **Policy schema version:** `pcv-1`
- **Global sensitivity level:** `low`
- **Why this level:** nenhuma superfície runtime muda, mas o piso recomenda classificação independente por ser release-sensitive.
- **Current delivery stage at review time:** `Pending`

| Lane ID | Lane | Trigger Result | Trigger Severity | Trigger Reason Code | Gate Deadline | Minimum Evidence Rule | State | Residual Risk | Uncertainty Reason Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EPS` | endpoint-performance-scrutiny | not_needed | low | EPS-DATA-PATH-CHANGED | before_local_implemented | EPS-E1 | not_applicable | none | none |
| `FRC` | frontend-race-condition-validation | not_needed | low | FRC-STALE-RESPONSE | before_local_implemented | FRC-POLICY | not_applicable | none | none |
| `BCI` | backend-concurrency-idempotency-validation | not_needed | low | BCI-EXACT-ONCE-SEMANTICS | before_local_implemented | BCI-INV | not_applicable | none | none |
| `RLS` | runtime-load-stress-validation | not_needed | low | RLS-SLO-CLAIM | before_production_ready | RLS-E1 | not_applicable | none | none |

## Verification Debt Assessment

- **Audit outcome:** `required before Completed`
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
- **Internal reviewer mandate:** `required — fresh internal no-context reviewer before Completed`
- **Audit status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`

## Independent No-Context Final Review Gate

- **Final review decision:** `required`
- **Why this decision:** identidade e arquitetura cross-module.
- **Impact signals in scope:** `cross-module blast radius|intentional module supersede`
- **Package mode:** `bounded-summary`
- **Review isolation mode:** `fresh internal no-context reviewer`
- **Internal reviewer mandate:** `required — fresh internal no-context reviewer before Completed`
- **Final review status:** `not_run`
- **Findings summary:** `pending`
- **Evidence / reference:** `pending`

## Independent Cutover Integrity Audit Gate

- **Cutover audit decision:** `required`
- **Why this decision:** cutover canônico e aposentadoria da autoridade antiga.
- **Cutover signals in scope:** `canonical cutover|legacy-path retirement`
- **Package mode:** `bounded-file-set`
- **Canonical multi-lane audit protocol:** `audit-protocol-triple-review required additively before Completed`
- **Audit session / round evidence:** `n/a until run`
- **Audit focus:** `true canonical path|current-target labels|hidden fallback|validator preservation`
- **Cutover audit status:** `not_run`
- **Findings summary:** `pending`

## TODO Closeout Disposition

- **Disposition:** `keep-active`
- **Disposition reason:** planejamento e aprovação ainda não concluídos.
- **Post-commit/push status:** `pending`
- **Next path/status action:** congelar baseline R3 em `main`, repetir arquitetura/crítica e executar guards pré-aprovação.

## Module Consolidation Gate

- [ ] Canonical module docs updated with D-01..D-07.
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
